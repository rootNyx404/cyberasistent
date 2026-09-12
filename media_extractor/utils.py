"""Shared utility functions."""
import hashlib
import mimetypes
import struct
from datetime import datetime
from pathlib import Path

# ── Extension sets ────────────────────────────────────────────────────────────
IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".tif",
               ".webp", ".heic", ".heif", ".ico", ".svg"}
VIDEO_EXTS = {".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv",
               ".webm", ".m4v", ".3gp", ".ts", ".mpeg", ".mpg"}
AUDIO_EXTS = {".mp3", ".wav", ".flac", ".aac", ".ogg",
               ".m4a", ".wma", ".opus", ".aiff", ".alac"}
ALL_MEDIA_EXTS = IMAGE_EXTS | VIDEO_EXTS | AUDIO_EXTS

# ── Magic bytes signatures ────────────────────────────────────────────────────
# (offset, bytes, label)
MAGIC_SIGNATURES = [
    (0, b"\xff\xd8\xff",          "JPEG"),
    (0, b"\x89PNG\r\n\x1a\n",    "PNG"),
    (0, b"GIF87a",                "GIF87"),
    (0, b"GIF89a",                "GIF89"),
    (0, b"BM",                    "BMP"),
    (0, b"II\x2a\x00",           "TIFF-LE"),
    (0, b"MM\x00\x2a",           "TIFF-BE"),
    (0, b"RIFF",                  "RIFF"),       # WAV / AVI
    (0, b"fLaC",                  "FLAC"),
    (0, b"OggS",                  "OGG"),
    (0, b"ID3",                   "MP3-ID3"),
    (0, b"\xff\xfb",              "MP3"),
    (4, b"ftyp",                  "MP4/MOV"),
    (0, b"\x1aE\xdf\xa3",        "MKV/WEBM"),
    (0, b"FLV",                   "FLV"),
    (0, b"RIFF",                  "AVI"),
    (0, b"\x00\x00\x00\x0cftyp", "MP4"),
    (0, b"\x52\x61\x72\x21",     "RAR"),
    (0, b"PK\x03\x04",           "ZIP"),
]


def detect_magic(path: Path) -> dict:
    """Read first 16 bytes and match against known signatures."""
    try:
        with open(path, "rb") as f:
            header = f.read(16)
        detected = []
        for offset, sig, label in MAGIC_SIGNATURES:
            if header[offset: offset + len(sig)] == sig:
                detected.append(label)
        mime, _ = mimetypes.guess_type(str(path))
        return {
            "detected_signatures": detected,
            "mime_guess": mime,
            "header_hex": header.hex(),
        }
    except Exception as e:
        return {"error": str(e)}


def detect_anomalies(path: Path, magic: dict, media_type_str: str) -> list:
    """Return a list of anomaly warning strings."""
    warnings = []
    ext = path.suffix.lower()
    sigs = magic.get("detected_signatures", [])

    # Extension vs magic mismatch
    if sigs:
        sig_str = " ".join(sigs).upper()
        if ext in (".jpg", ".jpeg") and "JPEG" not in sig_str:
            warnings.append(f"Extension '{ext}' does not match detected signature(s): {sigs}")
        elif ext == ".png" and "PNG" not in sig_str:
            warnings.append(f"Extension '{ext}' does not match detected signature(s): {sigs}")
        elif ext in (".mp4", ".m4v") and "MP4" not in sig_str and "MOV" not in sig_str:
            warnings.append(f"Extension '{ext}' does not match detected signature(s): {sigs}")
        elif ext in (".zip", ".rar") and not any(s in sig_str for s in ("ZIP", "RAR")):
            warnings.append(f"Extension '{ext}' does not match detected signature(s): {sigs}")

    # Archive disguised as media
    if any(s in ("ZIP", "RAR") for s in sigs) and media_type_str in ("image", "video", "audio"):
        warnings.append("File appears to be an archive disguised as a media file!")

    # Zero-byte file
    if path.stat().st_size == 0:
        warnings.append("File is empty (0 bytes).")

    return warnings


def human_size(n: int) -> str:
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if n < 1024:
            return f"{n:.2f} {unit}"
        n /= 1024
    return f"{n:.2f} PB"


def compute_hashes(path: Path) -> dict:
    """Compute MD5, SHA1, and SHA256 of a file."""
    md5 = hashlib.md5()
    sha1 = hashlib.sha1()
    sha256 = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            md5.update(chunk)
            sha1.update(chunk)
            sha256.update(chunk)
    return {
        "md5": md5.hexdigest(),
        "sha1": sha1.hexdigest(),
        "sha256": sha256.hexdigest(),
    }


def file_info(path: Path) -> dict:
    st = path.stat()
    return {
        "name": path.name,
        "path": str(path.resolve()),
        "extension": path.suffix.lower(),
        "size_bytes": st.st_size,
        "size_human": human_size(st.st_size),
        "created_at": datetime.fromtimestamp(st.st_ctime).isoformat(),
        "modified_at": datetime.fromtimestamp(st.st_mtime).isoformat(),
        "hashes": compute_hashes(path),
    }


def media_type(path: Path) -> str:
    ext = path.suffix.lower()
    if ext in IMAGE_EXTS:
        return "image"
    if ext in VIDEO_EXTS:
        return "video"
    if ext in AUDIO_EXTS:
        return "audio"
    return "unknown"
