<div align="center">

# 🧠⚡ CYBERASISTENT

### 🌌 Media Metadata Intelligence Engine

<img src="https://capsule-render.vercel.app/api?type=waving&height=220&color=0:00F5FF,50:7B2CFF,100:FF00CC&text=CYBERASISTENT&fontColor=ffffff&fontSize=55&fontAlignY=40&desc=Media%20Metadata%20%7C%20Digital%20Forensics%20%7C%20Security%20Analysis&descAlignY=62&descSize=18" width="100%"/>

<br>

[![Python](https://img.shields.io/badge/Python-3.x-00F5FF?style=for-the-badge\&logo=python\&logoColor=white)](https://www.python.org/)
[![Security](https://img.shields.io/badge/Cybersecurity-Analysis-7B2CFF?style=for-the-badge\&logo=hackthebox\&logoColor=white)](https://github.com/rootNyx404)
[![Forensics](https://img.shields.io/badge/Digital-Forensics-FF00CC?style=for-the-badge\&logo=protonmail\&logoColor=white)](https://github.com/rootNyx404)
[![Metadata](https://img.shields.io/badge/Metadata-Intelligence-00FFA3?style=for-the-badge\&logo=datadog\&logoColor=white)](https://github.com/rootNyx404)

<br>

### 🔮 Built by **Arup Halder**

### 👾 GitHub: **rootNyx404**

</div>

---

# 🌈 What is CYBERASISTENT?

> **Every file leaves a digital footprint.
> CYBERASISTENT helps you discover it.**

**CYBERASISTENT** is a powerful Python-based **Media Metadata Intelligence & Analysis Toolkit** designed for deep inspection of:

```text
        📷 IMAGES
           │
           ▼
      🧠 METADATA
           │
           ▼
   ┌───────┼────────┐
   ▼       ▼        ▼
  🎨      🛰️       🔐
 COLOR     GPS     SECURITY
   │       │        │
   └───────┼────────┘
           ▼
      🔍 ANALYSIS
           │
           ▼
      📊 REPORTING
```

It can analyze **images, videos and audio**, extract technical metadata, inspect file signatures, calculate cryptographic hashes, perform color analysis, and generate structured reports.

---

# 🚀 THE CORE

<div align="center">

### 🧠 `CORE` + 👁️ `SENTIENT` = ⚡ `CYBERASISTENT`

</div>

The project is designed around a simple idea:

```text
┌─────────────────────────────────────────────┐
│                                             │
│              🧠 CYBERASISTENT               │
│                                             │
│     📷 IMAGE     🎬 VIDEO     🎵 AUDIO      │
│          \          │          /            │
│           \         │         /             │
│            ▼        ▼        ▼              │
│          ┌─────────────────────┐            │
│          │   🔮 CORE ENGINE    │            │
│          └──────────┬──────────┘            │
│                     │                       │
│          ┌──────────┼──────────┐            │
│          ▼          ▼          ▼            │
│       🔍 META     🛡️ SEC     🔐 HASH        │
│                     │                       │
│                     ▼                       │
│              📊 INTELLIGENCE               │
│                                             │
└─────────────────────────────────────────────┘
```

---

# 💎 Feature Matrix

|       🌈 Module       | ⚡ Capabilities                                                |
| :-------------------: | ------------------------------------------------------------- |
|      📷 **IMAGE**     | EXIF • GPS • ICC • DPI • Resolution • Color Mode              |
|      🛰️ **GPS**      | Latitude • Longitude • Altitude • Speed • Direction           |
|      🎨 **COLOR**     | Dominant Colors • Average Color • Brightness • Transparency   |
| 🕵️ **STEGANOGRAPHY** | LSB Ratio • File Size Anomaly • PNG Chunk Heuristics          |
|      🎬 **VIDEO**     | Codec • Resolution • FPS • Bitrate • HDR • Streams • Chapters |
|      🎵 **AUDIO**     | Duration • Bitrate • Sample Rate • ID3 • Vorbis • MP4 Tags    |
|    🛡️ **SECURITY**   | Magic Bytes • MIME Guess • Extension Mismatch                 |
|     🔐 **HASHING**    | MD5 • SHA1 • SHA256                                           |
|   ⚡ **PERFORMANCE**   | Parallel Processing • Multi-Worker Scanning                   |
|     📊 **EXPORT**     | JSON • CSV                                                    |

---

# 📷 IMAGE INTELLIGENCE

```text
                 📷 IMAGE
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
       📋 EXIF              🛰️ GPS
          │                   │
     ┌────┼────┐         ┌────┼────┐
     ▼    ▼    ▼         ▼    ▼    ▼
   Camera Date Lens     Lat  Lon Alt
          │                   │
          └─────────┬─────────┘
                    ▼
              🧠 ANALYSIS
```

### Extracted Image Data

* 📐 Width & Height
* 🔢 Megapixels
* 📋 EXIF metadata
* 📷 Camera information
* 🔭 Lens information
* 🛰️ GPS coordinates
* ⛰️ Altitude
* 🧭 Direction
* 🚗 Speed
* 🎨 ICC profile
* 🖥️ DPI
* 🌈 Color mode
* 👻 Transparency

---

# 🛰️ GPS INTELLIGENCE

When GPS metadata exists, CYBERASISTENT can extract:

```text
🌍 LATITUDE
🌍 LONGITUDE
⛰️ ALTITUDE
🚗 SPEED
🧭 DIRECTION
```

Example:

```json
{
  "latitude": 48.8566,
  "longitude": 2.3522,
  "altitude_m": 35.0,
  "speed": "0.00 K",
  "direction_deg": 270.5
}
```

📍 Coordinates can also be represented as a map URL for investigation workflows.

---

# 🎨 COLOR INTELLIGENCE

Turn pixels into data.

```text
              🖼️ IMAGE
                 │
                 ▼
          🌈 COLOR ENGINE
                 │
       ┌─────────┼─────────┐
       ▼         ▼         ▼
    🎨 AVG    🔥 DOMINANT 💡 LIGHT
       │         │         │
       └─────────┼─────────┘
                 ▼
           📊 COLOR DATA
```

### Analysis

* 🌈 Average color
* 🎨 Dominant colors
* 💡 Brightness score
* 🏷️ Brightness label
* 👻 Transparency percentage
* 🔢 HEX color values

Example:

```json
{
  "average_color_hex": "#a3b2c1",
  "brightness": 0.712,
  "brightness_label": "bright",
  "dominant_colors": [
    {"hex": "#ffffff"},
    {"hex": "#3a3a3a"}
  ]
}
```

---

# 🕵️ STEGANOGRAPHY HINTS

CYBERASISTENT provides lightweight **heuristic indicators** for possible hidden-data anomalies.

```text
                 📁 FILE
                   │
                   ▼
             🔬 ANALYSIS
                   │
        ┌──────────┼──────────┐
        ▼          ▼          ▼
      LSB       SIZE        PNG
     CHECK     ANOMALY      CHUNKS
        │          │          │
        └──────────┼──────────┘
                   ▼
             🎯 SCORE
                   │
          ┌────────┼────────┐
          ▼        ▼        ▼
        🟢 LOW  🟡 MEDIUM  🔴 HIGH
```

> ⚠️ These are **heuristics**, not definitive proof of steganography.

---

# 🎬 VIDEO INTELLIGENCE

CYBERASISTENT can inspect video containers and streams.

### 🎥 Extracted Information

```text
🎬 VIDEO
 │
 ├── 🎞️ Codec
 ├── 📐 Resolution
 ├── 🎥 FPS
 ├── 📊 Bitrate
 ├── 🌈 HDR
 ├── 🔀 Streams
 ├── 📚 Chapters
 └── 📦 Container Data
```

---

# 🎵 AUDIO INTELLIGENCE

Deep inspection of supported audio files.

```text
🎵 AUDIO
 │
 ├── ⏱️ Duration
 ├── 📊 Bitrate
 ├── 🎚️ Sample Rate
 ├── 🏷️ ID3
 ├── 🏷️ Vorbis
 ├── 🏷️ MP4 Tags
 └── 🌊 WAV Waveform Statistics
```

---

# 🛡️ FILE SECURITY

A file's extension can lie.

CYBERASISTENT compares:

```text
        filename.jpg
             │
             ▼
       📎 Extension
             │
             ▼
       🔬 Magic Bytes
             │
             ▼
        🧬 MIME Guess
             │
             ▼
      🛡️ SECURITY CHECK
```

Example:

```text
photo.jpg

Extension:
    JPEG ❓

Internal Signature:
    PNG ❗

Result:
    ⚠️ EXTENSION MISMATCH
```

---

# 🔐 HASH ENGINE

Every analyzed file can generate:

<div align="center">

`MD5`  ✦  `SHA1`  ✦  `SHA256`

</div>

Example:

```json
{
  "md5": "...",
  "sha1": "...",
  "sha256": "..."
}
```

Useful for:

* 🔎 File identification
* 🧬 Integrity verification
* ♻️ Duplicate detection
* 🛡️ Security investigations
* 📁 Evidence tracking

---

# ⚡ PARALLEL SCANNING

Large directory?

No problem.

CYBERASISTENT supports configurable workers.

```bash
python main.py ./media --dir -r -w 8
```

Architecture:

```text
                  📁 MEDIA
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
     ⚡ WORKER 1  ⚡ WORKER 2  ⚡ WORKER 3
        │            │            │
        └────────────┼────────────┘
                     ▼
              🧠 CORE ENGINE
                     │
             ┌───────┴───────┐
             ▼               ▼
          📄 JSON          📊 CSV
```

---

# 📊 REPORTING ENGINE

Export results into structured formats.

### 🟣 JSON

Perfect for:

* APIs
* Automation
* Data processing
* Security pipelines

### 🔵 CSV

Perfect for:

* Reports
* Bulk analysis
* Spreadsheet workflows
* Investigations

---

# 🚀 INSTALLATION

## 1️⃣ Clone

```bash
git clone <YOUR_REPOSITORY_URL>
cd cyberasistent
```

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

## 3️⃣ MediaInfo Dependency

`pymediainfo` requires the native **libmediainfo** library.

### 🐧 Debian / Ubuntu / Parrot OS

```bash
sudo apt update
sudo apt install libmediainfo0v5
```

### 🍎 macOS

```bash
brew install libmediainfo
```

### 🪟 Windows

Install MediaInfo from the official MediaArea distribution.

---

# 💻 USAGE

### 📷 Single Image

```bash
python main.py photo.jpg
```

### 🎬 Video → JSON

```bash
python main.py video.mp4 -o result.json
```

### 📁 Directory → CSV

```bash
python main.py ./media --dir --csv report.csv
```

### ⚡ Recursive + 8 Workers

```bash
python main.py ./media --dir -r -w 8
```

### 🤫 Quiet JSON Mode

```bash
python main.py photo.jpg --quiet
```

---

# 📂 PROJECT STRUCTURE

```text
🧠 cyberasistent/
│
├── ⚡ main.py
├── 📦 requirements.txt
├── 📖 README.md
│
└── 🔬 media_extractor/
    │
    ├── 🧠 analyzer.py
    │   └── Dispatcher + Parallel Engine + CSV
    │
    ├── 📷 image.py
    │   └── EXIF + GPS + Color + Steganography
    │
    ├── 🎬 video.py
    │   └── Codec + HDR + Streams + Chapters
    │
    ├── 🎵 audio.py
    │   └── Tags + Waveform Statistics
    │
    └── 🛡️ utils.py
        └── Hashes + Magic Bytes + Anomaly Detection
```

---

# 🧪 SAMPLE OUTPUT

```json
{
  "media_type": "image",

  "file": {
    "name": "photo.jpg",
    "size_human": "3.45 MB",

    "hashes": {
      "md5": "...",
      "sha1": "...",
      "sha256": "..."
    }
  },

  "magic_bytes": {
    "detected_signatures": ["JPEG"],
    "mime_guess": "image/jpeg"
  },

  "anomalies": [],

  "metadata": {
    "format": "JPEG",
    "width": 4032,
    "height": 3024,
    "megapixels": 12.19,

    "gps": {
      "latitude": 48.8566,
      "longitude": 2.3522,
      "altitude_m": 35.0,
      "speed": "0.00 K",
      "direction_deg": 270.5
    },

    "color_analysis": {
      "average_color_hex": "#a3b2c1",
      "brightness": 0.712,
      "brightness_label": "bright"
    },

    "steganography_hints": {
      "suspicion_score": 0,
      "suspicion_level": "low",
      "hints": []
    }
  }
}
```

---

# 🌐 ANALYSIS PIPELINE

```text
                    👤 USER
                      │
                      ▼
                📁 MEDIA FILE
                      │
                      ▼
              ⚡ CYBERASISTENT
                      │
       ┌──────────────┼──────────────┐
       ▼              ▼              ▼
    📷 IMAGE        🎬 VIDEO        🎵 AUDIO
       │              │              │
       └──────────────┼──────────────┘
                      ▼
                 🧠 ANALYZER
                      │
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
      🎨 COLOR      🛡️ SECURITY    🔐 HASH
        │             │             │
        └─────────────┼─────────────┘
                      ▼
                 📊 REPORT
                      │
              ┌───────┴───────┐
              ▼               ▼
           🟣 JSON          🔵 CSV
```

---

# 🎯 USE CASES

<div align="center">

|  🔎 Digital Forensics  |  🛡️ Security Research  |
| :--------------------: | :---------------------: |
| 📷 Image Investigation |    🔐 File Integrity    |
| 🎬 Media Investigation |   🧬 Hash Verification  |
|    📊 Bulk Analysis    | 🕵️ Metadata Inspection |
|    🔍 File Research    |   🧪 Security Analysis  |

</div>

---

# 🧰 TECHNOLOGY STACK

```text
                    🧠 CYBERASISTENT
                           │
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
       🐍 Python        🔬 MediaInfo      🖼️ Pillow
          │                │                │
          └────────────────┼────────────────┘
                           ▼
                    ⚡ ANALYSIS ENGINE
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
           📊 JSON        CSV        🔐 HASHES
```

---

# 👨‍💻 CREATOR

<div align="center">

## ⚡ Arup Halder

### Cybersecurity • Programming • Digital Forensics

**GitHub:** [rootNyx404](https://github.com/rootNyx404)

<br>

> 🧠 Building tools for understanding the hidden digital footprint behind files.

</div>

---

# ⭐ PROJECT PHILOSOPHY

<div align="center">

### 🔍 Inspect.

### 🧠 Understand.

### 🛡️ Analyze.

### ⚡ Secure.

<br>

**"Every file has a story.
CYBERASISTENT helps you read its digital footprint."**

</div>

---

# ⚠️ DISCLAIMER

CYBERASISTENT is intended for:

* ✅ Legitimate security research
* ✅ Digital forensics
* ✅ Authorized investigations
* ✅ Media analysis
* ✅ File integrity research

Do not use this tool to access, analyze, or investigate media or data without appropriate authorization.

The steganography module provides **heuristic indicators only** and should not be considered definitive proof of hidden data.

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&height=150&color=0:FF00CC,50:7B2CFF,100:00F5FF&section=footer" width="100%"/>

### 🧠 CYBERASISTENT

### ⚡ Built by Arup Halder

### 👾 `rootNyx404`

**Made with Python • Curiosity • Cybersecurity**

</div>
