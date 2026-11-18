# 第三方组件与许可证 · Third-Party Notices

拾幅（Sheaf）本体以 MIT 许可发布（见 `LICENSE`）。程序里用到的第三方组件与模型如下，
它们的许可**不覆盖**本项目自己的代码。

This project is released under the MIT License (see `LICENSE`). The third-party
components and models listed below carry their own licenses.

---

## 1. MediaPipe Tasks Vision（Google LLC）

| 项 | 内容 |
|---|---|
| 用途 | 人像分割（换底色）、人脸检测（判断正脸/侧脸、倾斜角） |
| 许可 | Apache License 2.0 |
| 仓库内文件 | `mp/vision_bundle.mjs`、`mp/wasm/vision_wasm_internal.js`、`mp/wasm/vision_wasm_internal.wasm` |
| 许可全文 | https://www.apache.org/licenses/LICENSE-2.0 |
| 项目主页 | https://github.com/google-ai-edge/mediapipe |

## 2. 人像分割模型 Selfie Segmenter

| 项 | 内容 |
|---|---|
| 上游名称 | `selfie_segmenter.tflite`（MediaPipe Selfie Segmentation, landscape 256×256） |
| 仓库内文件 | `mp/selfie_segmenter.tflite`（249 537 字节，二进制未改动） |
| 许可 | Apache License 2.0（随 MediaPipe 项目发布） |
| 上游地址 | https://github.com/google-ai-edge/mediapipe |

## 3. 人脸检测模型 BlazeFace（short-range）

| 项 | 内容 |
|---|---|
| 上游名称 | `face_detection_short_range.tflite`（MediaPipe Face Detection） |
| 仓库内文件 | `mp/blaze.tflite`（229 746 字节，**仅重命名**，二进制未改动） |
| 许可 | Apache License 2.0（随 MediaPipe 项目发布） |
| 上游地址 | https://github.com/google-ai-edge/mediapipe |

## 4. 界面外壳

| 组件 | 许可 | 说明 |
|---|---|---|
| pywebview | BSD 3-Clause | 把本地页面装进系统自带 WebView 的窗口壳 |
| WebView2 Runtime | 微软免费分发（Microsoft Software License Terms） | Windows 10/11 通常已自带；本程序不捆绑、不下载 |
| PyInstaller | GPL 2.0 + bootloader exception | 仅打包用，允许打包商业/闭源程序 |
| Python | PSF License | 运行时 |
| Pillow | MIT-CMU | 仅开发期做测试图对比，不随程序发布 |

## 5. 关于模型权重

两个 `.tflite` 都是**图像领域的通用模型**，由 Google 随 MediaPipe 公开发布，
不含任何个人数据，也不是在本项目里训练出来的。

本程序**不包含**任何人的照片、人脸模板或声纹特征。用户拖进来的照片只在运行时读进内存，
处理完就丢，不落盘、不上传、不进安装包。

---

模型若需替换，改 `index.html` 里 `./mp/selfie_segmenter.tflite` 与 `./mp/blaze.tflite` 两处路径即可；
换成别的模型请自行核对其许可。
