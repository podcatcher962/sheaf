# -*- mode: python ; coding: utf-8 -*-
import os

HERE = os.path.abspath(SPECPATH) if "SPECPATH" in globals() else os.getcwd()

# 界面本体 + 图标
datas = [("index.html", "."), ("app.ico", ".")]

# 换背景用的本地模型（MediaPipe 运行时 + 抠图模型），约 9.9 MB
# 目录结构必须原样带过去：index.html 里写的是 ./mp/vision_bundle.mjs、./mp/wasm
for root, _dirs, files in os.walk(os.path.join(HERE, "mp")):
    for f in files:
        src = os.path.join(root, f)
        dst = os.path.relpath(root, HERE)
        datas.append((src, dst.replace("\\", "/")))

a = Analysis(
    ["launcher.py"],
    pathex=[HERE],
    binaries=[],
    datas=datas,
    hiddenimports=["webview.platforms.edgechromium"],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name="Sheaf",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=["vision_wasm_internal.wasm", "selfie_segmenter.tflite", "vcruntime140.dll", "python312.dll"],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=["app.ico"],
)
