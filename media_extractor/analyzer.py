"""Top-level analyzer: dispatches to image/video/audio extractors with parallel support."""
import csv
import io
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from typing import List

from . import image, video, audio
from .utils import (
    file_info, media_type, ALL_MEDIA_EXTS,
    detect_magic, detect_anomalies,
)


def analyze_file(path: Path) -> dict:
    """Return a full metadata dict for a single media file."""
    path = Path(path)
    if not path.exists():
        return {"error": f"File not found: {path}"}
    if not path.is_file():
        return {"error": f"Not a regular file: {path}"}

    mtype = media_type(path)
    magic = detect_magic(path)
    anomalies = detect_anomalies(path, magic, mtype)

    result = {
        "analyzed_at": datetime.now(timezone.utc).isoformat(),
        "media_type": mtype,
        "file": file_info(path),
        "magic_bytes": magic,
    }

    if anomalies:
        result["anomalies"] = anomalies

    if mtype == "image":
        result["metadata"] = image.extract(path)
    elif mtype == "video":
        result["metadata"] = video.extract(path)
    elif mtype == "audio":
        result["metadata"] = audio.extract(path)
    else:
        result["metadata"] = {}
        result["warning"] = f"Unknown media type for extension '{path.suffix}'"

    return result


def analyze_directory(
    directory: Path,
    recursive: bool = False,
    max_workers: int = 4,
) -> dict:
    """Analyze all media files in a directory using parallel threads."""
    directory = Path(directory)
    pattern = "**/*" if recursive else "*"
    files: List[Path] = sorted(
        p for p in directory.glob(pattern)
        if p.is_file() and p.suffix.lower() in ALL_MEDIA_EXTS
    )

    results = [None] * len(files)
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_idx = {executor.submit(analyze_file, f): i for i, f in enumerate(files)}
        for future in as_completed(future_to_idx):
            idx = future_to_idx[future]
            try:
                results[idx] = future.result()
            except Exception as e:
                results[idx] = {"error": str(e), "file": str(files[idx])}

    # Summary statistics
    type_counts = {"image": 0, "video": 0, "audio": 0, "unknown": 0}
    total_bytes = 0
    anomaly_files = []
    for r in results:
        if r:
            t = r.get("media_type", "unknown")
            type_counts[t] = type_counts.get(t, 0) + 1
            total_bytes += r.get("file", {}).get("size_bytes", 0)
            if r.get("anomalies"):
                anomaly_files.append(r["file"]["name"])

    from .utils import human_size
    return {
        "directory": str(directory.resolve()),
        "total_files": len(results),
        "total_size_human": human_size(total_bytes),
        "type_breakdown": type_counts,
        "files_with_anomalies": anomaly_files,
        "files": results,
    }


def to_csv(results: list) -> str:
    """Convert a list of file analysis results to a flat CSV string."""
    output = io.StringIO()
    fieldnames = [
        "name", "media_type", "extension", "size_human",
        "sha256", "md5", "created_at", "modified_at",
        "anomalies", "magic_signatures",
        # image
        "width", "height", "megapixels", "format",
        "gps_latitude", "gps_longitude", "gps_maps_url",
        "brightness", "dominant_color_hex",
        "steg_suspicion_level",
        # video
        "video_format", "video_duration_sec", "video_bitrate",
        # audio
        "audio_duration_sec", "audio_bitrate_kbps",
        "audio_title", "audio_artist", "audio_album",
    ]
    writer = csv.DictWriter(output, fieldnames=fieldnames, extrasaction="ignore")
    writer.writeheader()

    for r in results:
        if not r or "error" in r:
            continue
        fi = r.get("file", {})
        hashes = fi.get("hashes", {})
        md = r.get("metadata", {})
        mtype = r.get("media_type", "")

        row = {
            "name": fi.get("name"),
            "media_type": mtype,
            "extension": fi.get("extension"),
            "size_human": fi.get("size_human"),
            "sha256": hashes.get("sha256"),
            "md5": hashes.get("md5"),
            "created_at": fi.get("created_at"),
            "modified_at": fi.get("modified_at"),
            "anomalies": "; ".join(r.get("anomalies", [])),
            "magic_signatures": ", ".join(r.get("magic_bytes", {}).get("detected_signatures", [])),
        }

        if mtype == "image":
            row["width"] = md.get("width")
            row["height"] = md.get("height")
            row["megapixels"] = md.get("megapixels")
            row["format"] = md.get("format")
            gps = md.get("gps", {})
            row["gps_latitude"] = gps.get("latitude")
            row["gps_longitude"] = gps.get("longitude")
            row["gps_maps_url"] = gps.get("maps_url")
            ca = md.get("color_analysis", {})
            row["brightness"] = ca.get("brightness")
            dom = ca.get("dominant_colors", [{}])
            row["dominant_color_hex"] = dom[0].get("hex") if dom else None
            steg = md.get("steganography_hints", {})
            row["steg_suspicion_level"] = steg.get("suspicion_level")

        elif mtype == "video":
            gen = md.get("general", {})
            row["video_format"] = gen.get("format")
            row["video_duration_sec"] = gen.get("duration")
            row["video_bitrate"] = gen.get("overall_bit_rate")

        elif mtype == "audio":
            row["audio_duration_sec"] = md.get("duration_sec")
            row["audio_bitrate_kbps"] = md.get("bitrate_kbps")
            ts = md.get("tag_summary", {})
            row["audio_title"] = ts.get("title")
            row["audio_artist"] = ts.get("artist")
            row["audio_album"] = ts.get("album")

        writer.writerow(row)

    return output.getvalue()
