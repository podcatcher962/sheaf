# -*- coding: utf-8 -*-
"""拾幅 —— 桌面壳（pywebview / WebView2）。

整份界面就是一个 index.html，壳只负责三件事：
  1. 用内建 HTTP 服务把目录喂给 WebView2（报名照换背景要动态 import 一个
     ES 模块去跑 MediaPipe 模型，file:// 下 Chromium 会按 CORS 直接拒掉）；
  2. 保证 .mjs / .wasm / .tflite 的 Content-Type 是对的，否则模块脚本加载失败；
  3. 记住主题（localStorage 落盘），并换掉窗口图标。
"""
import os
import sys
import mimetypes

import webview

# 必须在 WebView2 取资源之前注册，Windows 注册表里不一定有这几条
for _ext, _ty in (
    (".mjs", "text/javascript"),
    (".js", "text/javascript"),
    (".wasm", "application/wasm"),
    (".tflite", "application/octet-stream"),
    (".json", "application/json"),
):
    mimetypes.add_type(_ty, _ext)


def res(rel=""):
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, rel) if rel else base


def store_dir():
    base = os.environ.get("LOCALAPPDATA") or os.path.expanduser("~")
    p = os.path.join(base, "SheafPic")
    try:
        os.makedirs(p, exist_ok=True)
    except OSError:
        return None
    return p


def main():
    webview.create_window(
        "拾幅 — 图片批处理",
        res("index.html"),
        width=1200,
        height=840,
        min_size=(860, 560),
        background_color="#0e1014",
        text_select=False,
    )
    # http_server=True：以 index.html 所在目录为根起一个本地服务，随机端口。
    # 不这样开，换背景用的模型（9.4 MB wasm）会加载不了，只能退回颜色抠图。
    webview.start(
        debug=False,
        http_server=True,
        private_mode=False,
        storage_path=store_dir(),
    )


if __name__ == "__main__":
    main()
