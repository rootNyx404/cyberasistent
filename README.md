# 🛡️ CYBERASISTENT

### 🚀 Media Metadata Extractor — Powerful Edition

<p align="center">
  <img src="https://img.shields.io/badge/CYBERASISTENT-Media%20Intelligence-00FFFF?style=for-the-badge&logo=hackthebox&logoColor=white" alt="Cyberasistent">
  <img src="https://img.shields.io/badge/Python-3.x-7B2CFF?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Security-Metadata%20Analysis-FF00CC?style=for-the-badge&logo=shield&logoColor=white" alt="Security">
</p>

<p align="center">

**A powerful, professional-grade media intelligence toolkit for deep metadata analysis.**

Analyze **images, videos, and audio** — inspect metadata, detect anomalies, calculate hashes, analyze colors, inspect streams, and export detailed reports.

</p>

---

## 🌌 What is CYBERASISTENT?

**CYBERASISTENT** is a powerful Python-based **Media Metadata Intelligence Tool** designed to go beyond basic file information.

It combines:

```text
┌──────────────────────────────────────────────────────────────┐
│                      CYBERASISTENT                           │
│                                                              │
│   📷 IMAGE        🎬 VIDEO        🎵 AUDIO        🔐 SECURITY │
│      │               │               │               │       │
│      └───────────────┴───────────────┴───────────────┘       │
│                              │                               │
│                       🧠 ANALYSIS ENGINE                    │
│                              │                               │
│                📊 JSON / CSV INTELLIGENCE                   │
└──────────────────────────────────────────────────────────────┘
```

### ⚡ Core Capabilities

* 🔍 Deep metadata extraction
* 🛰️ GPS & location metadata analysis
* 🎨 Advanced color analysis
* 🕵️ Steganography heuristics
* 🎬 Video stream inspection
* 🎵 Audio tag & waveform analysis
* 🛡️ File signature verification
* 🔐 Cryptographic hashing
* ⚡ Parallel directory scanning
* 📊 JSON & CSV reporting

---

# 🧠 Feature Matrix

| 🔥 Category               | ⚙️ Capabilities                                          |
| ------------------------- | -------------------------------------------------------- |
| 📷 **Image Intelligence** | EXIF, GPS, ICC, DPI, dimensions, color mode              |
| 🛰️ **GPS Analysis**      | Latitude, longitude, altitude, speed, direction          |
| 🎨 **Color Analysis**     | Dominant colors, average color, brightness, transparency |
| 🕵️ **Steganography**     | LSB ratio, size anomalies, PNG chunk heuristics          |
| 🎬 **Video Intelligence** | Codec, resolution, FPS, bitrate, HDR, streams, chapters  |
| 🎵 **Audio Intelligence** | Duration, bitrate, sample rate, ID3/Vorbis/MP4 tags      |
| 🛡️ **Security Analysis** | Magic bytes, MIME detection, extension mismatch          |
| 🔐 **File Hashing**       | MD5, SHA1, SHA256                                        |
| ⚡ **Performance**         | Configurable parallel directory scanning                 |
| 📊 **Reporting**          | JSON & CSV export                                        |

---

# 📷 Image Intelligence

CYBERASISTENT can extract detailed image metadata including:

```text
EXIF
 ├── Camera information
 ├── Date / Time
 ├── Lens information
 ├── Orientation
 ├── Software
 └── Other embedded metadata

GPS
 ├── Latitude
 ├── Longitude
 ├── Altitude
 ├── Speed
 └── Direction

IMAGE
 ├── Resolution
 ├── DPI
 ├── Color Mode
 ├── ICC Profile
 └── Transparency
```

GPS information can also be converted into a Google Maps location URL when coordinates are available.

---

# 🎨 Color Intelligence

Analyze the visual characteristics of images.

### Extracted information

* 🌈 Dominant colors
* 🎨 Average color
* 💡 Brightness score
* 🏷️ Brightness classification
* 👻 Transparency percentage
* 🔢 Color information in HEX format

Example:

```json
{
  "average_color_hex": "#a3b2c1",
  "brightness": 0.712,
  "brightness_label": "bright",
  "dominant_colors": [
    {
      "hex": "#ffffff"
    },
    {
      "hex": "#3a3a3a"
    }
  ]
}
```

---

# 🕵️ Steganography Heuristics

CYBERASISTENT includes lightweight heuristic checks that can flag files for further investigation.

### 🔎 Detection Signals

```text
LSB Analysis
      │
      ▼
File Size Anomaly
      │
      ▼
PNG Chunk Analysis
      │
      ▼
Suspicion Score
      │
      ▼
LOW / MEDIUM / HIGH
```

> ⚠️ These checks are **heuristics**, not proof that steganography is present. Suspicious files should be investigated with dedicated forensic tools.

---

# 🎬 Video Intelligence

Analyze video containers and streams in depth.

### Extracts

* 🎞️ Codec
* 📐 Resolution
* 🎥 FPS
* 📊 Bitrate
* 🌈 HDR information
* 🔀 All available streams
* 📚 Chapters
* 📦 Container information

Useful for quickly understanding the technical structure of media files.

---

# 🎵 Audio Intelligence

Analyze common audio metadata and technical properties.

### Supported analysis includes

* ⏱️ Duration
* 📊 Bitrate
* 🎚️ Sample rate
* 🏷️ ID3 tags
* 🏷️ Vorbis comments
* 🏷️ MP4 metadata
* 🌊 WAV waveform statistics

---

# 🛡️ Security & File Integrity

CYBERASISTENT checks the difference between what a file **claims to be** and what its internal signature indicates.

### Example

```text
filename.jpg
     │
     ▼
Extension Check
     │
     ▼
Magic Bytes
     │
     ▼
MIME Guess
     │
     ▼
Integrity Analysis
```

This can help identify situations such as:

```text
photo.jpg
   ↓
Internal signature → PNG

⚠️ Extension mismatch detected
```

---

# 🔐 Cryptographic Hashes

Every analyzed file can generate:

```text
MD5
SHA1
SHA256
```

Example:

```json
"hashes": {
  "md5": "...",
  "sha1": "...",
  "sha256": "..."
}
```

Hashes can be useful for:

* File identification
* Integrity verification
* Duplicate detection
* Digital investigations
* Evidence tracking

---

# ⚡ Parallel Scanning Engine

Need to analyze hundreds or thousands of files?

CYBERASISTENT supports configurable parallel processing.

```bash
python main.py ./media --dir -r -w 8
```

Architecture:

```text
                 MEDIA DIRECTORY
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
       Worker 1     Worker 2     Worker 3
          │            │            │
          └────────────┼────────────┘
                       ▼
                 ANALYSIS ENGINE
                       │
                 ┌─────┴─────┐
                 ▼           ▼
               JSON         CSV
```

---

# 📊 Export Intelligence

Export analysis results into machine-readable reports.

### JSON

Perfect for:

* Automation
* APIs
* Data processing
* Security pipelines

### CSV

Perfect for:

* Spreadsheets
* Bulk analysis
* Reports
* Investigations

---

# 🚀 Installation

### 1️⃣ Clone the project

```bash
git clone <YOUR_REPOSITORY_URL>
cd cyberasistent
```

### 2️⃣ Install Python dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Install MediaInfo

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

# 💻 Usage

## 📷 Analyze a Single Image

```bash
python main.py photo.jpg
```

---

## 🎬 Analyze a Video & Export JSON

```bash
python main.py video.mp4 -o result.json
```

---

## 📁 Scan a Directory & Export CSV

```bash
python main.py ./media --dir --csv report.csv
```

---

## ⚡ Recursive Scan with 8 Workers

```bash
python main.py ./media --dir -r -w 8
```

---

## 🤫 Quiet Mode

Output JSON only without status messages:

```bash
python main.py photo.jpg --quiet
```

---

# 📂 Project Structure

```text
cyberasistent/
│
├── main.py
├── requirements.txt
├── README.md
│
└── media_extractor/
    │
    ├── analyzer.py
    │   └── Dispatcher + parallel engine + CSV
    │
    ├── image.py
    │   └── EXIF + GPS + color + steganography
    │
    ├── video.py
    │   └── Codec + HDR + streams + chapters
    │
    ├── audio.py
    │   └── Tags + waveform statistics
    │
    └── utils.py
        └── Hashes + magic bytes + anomaly detection
```

---

# 🧪 Example Output

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
    "detected_signatures": [
      "JPEG"
    ],
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
      "brightness_label": "bright",

      "dominant_colors": [
        {
          "hex": "#ffffff"
        },
        {
          "hex": "#3a3a3a"
        }
      ]
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

# 🎯 Use Cases

CYBERASISTENT can be useful for:

```text
🔎 Digital Forensics
🛡️ Security Analysis
📸 Image Investigation
🎬 Media Investigation
🎵 Audio Analysis
🧪 File Research
📊 Bulk Media Analysis
🔐 File Integrity Verification
```

Use it only on media you own or are authorized to analyze.

---

# 🧩 Technology Stack

```text
🐍 Python
│
├── Pillow
├── PyMediaInfo
├── Color Analysis
├── Hashing
├── File Signature Analysis
└── Parallel Processing
```

---

# 🌐 Architecture

```text
                 ┌───────────────────┐
                 │     USER INPUT    │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │    MAIN.PY CLI    │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │  ANALYSIS ENGINE  │
                 └─────────┬─────────┘
                           │
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
      📷 IMAGE          🎬 VIDEO          🎵 AUDIO
          │                │                │
          └────────────────┼────────────────┘
                           ▼
                 ┌───────────────────┐
                 │ SECURITY ANALYSIS │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │  JSON / CSV DATA  │
                 └───────────────────┘
```

---

# ⚠️ Disclaimer

**CYBERASISTENT is intended for legitimate security research, digital forensics, file analysis, and authorized investigations.**

Do not use this tool to access, analyze, or investigate media or data without appropriate authorization.

The steganography detection module provides **heuristic indicators only** and should not be treated as definitive proof of hidden data.

---

# ⭐ Project Philosophy

> **"Every file has a story. CYBERASISTENT helps you read its digital footprint."**

---

<p align="center">

### 🧠 Analyze the File.

### 🔍 Understand the Metadata.

### 🛡️ Investigate the Digital Footprint.

**CYBERASISTENT**

</p>

---

<p align="center">
  <sub>Built for cybersecurity research, digital forensics & media intelligence.</sub>
</p>
