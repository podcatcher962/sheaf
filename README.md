# 拾幅 · Sheaf

**v1.0.0** · 2026-11-18 · 第一版

把手机拍的照片，整理成能交上去的样子。

**报名照**（7 种规格 · 三色底 · 体积上限 · 能不能用的体检）、**压体积 / 转格式**、
**九宫格切图**、**拼长图**——全部在本机做完。不联网、不上传、不要账号。

Windows 10 / 11 64 位 · 单文件 exe 20.7 MB · MIT

> 仓库：**https://github.com/podcatcher962/sheaf**
> 作者：**永远的兰兰（Lanlan Eternal）**
> 下载：**[Releases](https://github.com/podcatcher962/sheaf/releases)**
> 在线版（免下载）：**https://podcatcher962.github.io/sheaf/** — 同一份代码在浏览器里跑，照片不出本机

*A small offline image tool for Windows. Four modes: ID photo (7 specs, 3 background
colors, size ceiling, and a readiness check), compress / convert, 3×3 grid split, and
vertical stitching. Nothing is uploaded — no network code in the program.*
*— [English section below ↓](#english)*

---

## 先说清楚这是什么

这是一件**裁剪和整理**的工具，不是修图工具，也不是 AI 生成器。

它不会给你磨皮、瘦脸、换发型、长出一副肩膀。它能做的是：按规格框好人、把脸摆在中间、
把背景换成白/蓝/红、把体积压到 10 KB 以内、再告诉你这张照片**到底能不能交上去**。

第一版只做到这里。**能不能用**是这一版的目标，好不好看不是。

---

## 四个模式

| 模式 | 干什么 |
|---|---|
| **报名照** | 7 种规格，换白/蓝/红底，自动对齐构图，压到指定体积，出 `报名照片.JPG`；另附 7 项「体检」告诉你能不能交 |
| **压缩 / 转换** | 长边 / 宽 / 百分比缩放（默认只缩不放），转 JPG / PNG / WebP，质量 40–100 |
| **九宫格切图** | 3×3 / 2×2 / 4×4 切分，可选先裁正方形，输出 `图-1-1.jpg` 按行优先编号，依次发出去就是完整一张 |
| **拼长图** | 多张竖着拼，统一宽度、可设间距与底色 |

另有：水印（字号 / 颜色 / 浓淡 / 九宫格位置 / 平铺整张）、清除拍摄信息（GPS、机型、时间）、
重命名（原名 / 加序号 / 加前缀）、从视频里取一帧当照片。

---

## 报名照

### 规格

| 规格 | 像素 | 默认体积上限 | 底色 |
|---|---|---|---|
| 国考 / 省考 | 295 × 413 | 10 KB | 白、蓝 |
| 一寸 | 295 × 413 | 不限 | 白/蓝/红 |
| 大一寸 | 390 × 567 | 不限 | 白/蓝/红 |
| 二寸 | 413 × 579 | 不限 | 白/蓝/红 |
| 小二寸 | 413 × 531 | 不限 | 白/蓝/红 |
| 护照 | 390 × 567 | 不限 | 白 |
| 社保卡 | 358 × 441 | 不限 | 白 |

构图按证件照惯例：头顶落在画面 **10%** 处，下巴在 **77.5%** 处，眼睛大致在 **42%** 处，
头部高度约等于**头宽 × 1.5**。三条参考线可以直接显示在预览上。

### 换底色

默认走本地人像分割模型（MediaPipe Selfie Segmentation），不挑背景颜色，室内室外都能抠；
遮罩边缘再经过一次导向滤波贴合原图边缘，头发丝不会糊成一块。纯色墙也可以改走「容差」模式，
从画面四边向内抠近似色，容差 6–44 可调。

换底时画框**允许越界**——外面补的就是纯底色。这样脸偏一边的照片才不会被迫贴边。

### 体积上限

填数字就自动降 JPEG 质量，压到限制以内；填 0 不限制。国考 295×413 一般落在 **9–10 KB**。

### 体检：7 项，会直说「不行」

| 项 | 看什么 | 不合格时它说什么 |
|---|---|---|
| 像素 | 取景范围够不够输出尺寸 | 「像素不够：要放大 1.4 倍才够，出图会发虚」 |
| 清晰度 | 固定尺度上的拉普拉斯方差 | 「可能手抖：锐度 210（<320）」 |
| 曝光 | 主体亮度、背景/脸亮度比 | 「偏暗」「过曝」「逆光」「脸偏暗」 |
| 光线 | 左半与右半的亮度差 | 「左右光差大：左 168 / 右 102」 |
| 姿态 | 人脸关键点算偏航角、肩宽比 | 「脸偏过去了」「身体是侧着的」「取景偏窄」 |
| 背景 | 背景占比、是否抠到人脸 | 「背景杂乱：只认出 41%，想换底得找面纯色墙」 |
| 来源 | JPEG 量化均值 | 「被多次转发：这是群里存回来的图，细节大半没了」 |

**体检是这一版最实用的部分**：照片不行，它不会假装修好了，而是告诉你为什么不行、该怎么重拍。

### 它明确不做的事

| 不做 | 为什么 |
|---|---|
| 磨皮、美颜、瘦脸、换发型 | 国考《报考指南》原文：照片**不得美化、修饰** |
| 把侧身「转正」、补出肩膀和衣服 | 那已经不是本人照片了，属于合成 |
| 换脸、拼脸、只留五官其余重画 | 同上，且「确保为本人照片」是报考人的责任 |
| 把不够像素的照片放大凑数 | 官方明确：**禁止**将不满足像素要求的照片放大后使用 |

所以**本软件只接受正面照**：正对镜头、双肩放平、露耳露眉。侧身、凑近自拍、美颜修过的照片，
它会在体检里直接标红，而不是硬做成一张"看着像证件照"的图。

拍法：相机与眼睛同高，退后 1.5–2 米，站在纯色墙前，**让别人帮你拍**；手机别自己举着。

---

## 怎么用

1. 双击 `Sheaf.exe`
2. 把照片拖进窗口，或点「选择图片」；也可以整文件夹拖进来批量处理
3. 顶部选模式（默认就是**报名照**）
4. 左边选规格、底色、体积上限
5. 看右侧「体检」——有标红就先重拍，别急着导出
6. 拖动照片或滚轮缩放，把头顶 / 眼睛 / 下巴对到参考线（点「自动摆正」也可以）
7. 点「开始处理」，成品在下面的结果区，点右键另存

视频也可以：直接把 `.mp4` 拖进来，它会按清晰度和正脸程度筛出 6 帧让你挑一张。

---

## 关于隐私

- **不上传**。程序里没有任何联网代码，不上报、不统计、不检查更新。断网拔网线一样用。
- **不落盘**。拖进来的照片只在内存里读一次，处理完就丢；只有你点保存的那一张会写到你选的文件夹。
- **不进安装包**。exe 里只有界面、图标和两个模型，没有任何示例人像。
- **默认清除拍摄信息**。重新编码时 EXIF（GPS 位置、机型、拍摄时间）自然丢弃。

---

## 本版实测

在真 exe 里跑的，不是浏览器里跑源码：

| 项目 | 结果 |
|---|---|
| 真 exe 内全流程（加载 → 两个模型就绪 → 真实照片 → 出图） | **10/10** |
| 13 张真实手机照片批量回归（构图头顶比例落在 7–14% 算合格） | **63/65** |
| 国考成品 | 295 × 413、**9.9 KB**、底色纯度 **95%** |
| 自动摆正（倾斜 6° 的合成样本） | 残余 **0.64°**；正立的照片一次都不转 |
| 启动 | 界面先出来，两个模型按需加载，不阻塞操作 |

不完美的地方，也写在这里：

- 一张小尺寸 PNG 换底后边缘留了一圈杂色，底色纯度只有 **88.8%**（其余 12 张都在 94–98%），
  体检会标黄提醒，但导出的图确实不算干净；
- 一张正面全身照头顶压到 **20.3%**，因为缩放已到上限（8 倍），构图偏下——这种片子让人退后重拍最省事；
- 侧身、举手机自拍这类源片，构图能对齐，但**身体还是歪的**——这是不做合成的前提，改不了。

---

## 常见问题

**为什么我的自拍被说「取景偏窄」？**
肩宽只有 1.6 个头宽左右，说明是举着手机凑近拍的，肩膀根本没进画面。这种源片怎么裁都不像报名照，
退后让别人拍一张，比修十次都强。

**底色边缘有一圈白边 / 锯齿？**
用「容差」模式时把容差调大一点；模型模式对深色头发+浅色墙最稳，逆光和花背景本来就难。
体检里「背景不好抠」是在提醒这件事。

**视频拖进去说放不了？**
部分手机默认用 HEVC（H.265）编码，Windows 自带的解码器不认。程序会明确告诉你这条视频是
HEVC，让你先在相册里「另存为 H.264」或直接选一张照片，而不是转圈转到超时。

**会不会偷偷上传？**
不会。可以拔掉网线、关掉 Wi-Fi 再试一遍，全部功能照常。

**能批量吗？**
能。一次拖多张，参数统一应用，成品可以「下载全部」打包成 zip。

---

## 系统要求

- Windows 10 / 11（64 位）
- 内存 2 GB 以上即可
- 硬盘 60 MB 可用空间
- WebView2 运行时（Win11 自带；Win10 如果没装过，程序会提示，装一次永久有效）

---

## 从源码跑

```bash
python -m pip install pywebview
python launcher.py
```

`mp/` 目录必须和 `index.html` 在一起（两个 `.tflite` + wasm 推理引擎，共 9.9 MB），
少一个模型就会退化成「容差抠图」，界面会提示。

自己打包：

```bash
python -m pip install pyinstaller
python -m PyInstaller Sheaf.spec --noconfirm --clean
```

`Sheaf.spec` 已经把 `mp/` 整个目录和 `app.ico` 写进 `datas`，无需再改。

---

## 免责声明

- 本软件只做裁剪、缩放、换底色、压缩，**不改变人物本身的样貌**；出图是否满足具体考试的
  要求，请以招考单位当年发布的公告为准。
- 证件照的合规责任在报考人本人。体检项是根据常见要求做的经验判断，**不是官方审核**。
- 软件按 MIT 许可「按现状」提供，不附带任何担保；用它造成的报名失败、格式不符等后果，
  作者不承担责任。

---

## 授权与署名

- 本体代码：MIT，见 `LICENSE`
- 第三方组件（MediaPipe、模型、pywebview 等）：见 `THIRD-PARTY-NOTICES.md`
- 作者：**永远的兰兰（Lanlan Eternal）**

---

# English

**v1.0.0** · 2026-11-18 · first release

A small offline image tool for Windows: turn phone photos into something you can actually
submit. No upload, no account, no network code.

## Four modes

| Mode | What it does |
|---|---|
| **ID photo** | 7 Chinese document-photo specs (295×413 exam photo, 1-inch, 2-inch, passport, social-security card…), white/blue/red background, auto-composition, JPEG size ceiling (10 KB default for the exam spec), plus a 7-point "is this usable" check |
| **Compress / convert** | Resize by long edge / width / percent (downscale only by default), JPG / PNG / WebP, quality 40–100 |
| **Grid split** | 3×3 / 2×2 / 4×4, optional square crop, outputs `name-1-1.jpg` in row-major order |
| **Stitch** | Stack images vertically with a unified width, gap and background color |

Extras: watermark (size / color / opacity / 9 positions / tile), EXIF stripping (GPS, camera,
timestamp), renaming, and frame extraction from a video.

## What it deliberately does not do

It does **not** retouch, slim, beautify, generate shoulders, generate clothing, or "turn" a
side-facing body to the front, and it does not upscale an undersized photo. Chinese civil-service
application rules explicitly forbid retouched or composited photos and forbid enlarging photos
that are below the pixel requirement. So this tool only accepts a **front-facing** photo and
says so plainly instead of faking one.

## The check (7 points)

Resolution, sharpness (Laplacian variance), exposure (including backlight detection from the
background/face luminance ratio), left-right lighting difference, pose (face yaw and shoulder
width from face keypoints), background (mask coverage, whether the face got masked out), and
JPEG re-compression level. Each item returns ok / warn / bad with a number and a one-line reason.

## Measured, not estimated

| Item | Result |
|---|---|
| Full pipeline inside the packaged exe | **10/10** |
| 13 real phone photos, batch regression | **63/65** |
| Exam-spec output | 295 × 413, **9.9 KB**, background purity **95 %** |
| Auto-level on a 6° tilted sample | **0.64°** residual; upright photos are left untouched |
| Cold start to first process | ~3 s (models load on demand) |

Known rough edges: one small low-resolution PNG leaves a fringe after mask-based background
replacement (purity 88.8 % while the other twelve sit at 94–98 %); one full-body shot lands at
20.3 % headroom because zoom is capped at 8×; and a selfie shot with the arm raised keeps a
tilted body — that is the trade-off of not compositing.

## Privacy

No network code at all. Photos are read into memory once, never written anywhere except the
output file you choose. No sample faces ship inside the exe. EXIF is dropped on re-encode.

## Requirements & build

Windows 10/11 x64, 2 GB RAM, WebView2 runtime (bundled with Win11).

```bash
python -m pip install pywebview
python launcher.py

python -m pip install pyinstaller
python -m PyInstaller Sheaf.spec --noconfirm --clean
```

`mp/` (two `.tflite` models + the wasm runtime, 9.9 MB) must sit next to `index.html`.

## License

MIT for the app itself (`LICENSE`). MediaPipe, its models, pywebview and PyInstaller keep their
own licenses — see `THIRD-PARTY-NOTICES.md`.
