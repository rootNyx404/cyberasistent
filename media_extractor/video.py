"""Video metadata extraction: streams, codec, HDR, chapters, thumbnails."""
from pathlib import Path


def _clean(track) -> dict:
    return {k: v for k, v in track.to_data().items() if v not in (None, "")}


def _hdr_info(video_track) -> dict:
    """Extract HDR-related fields from a video track."""
    hdr = {}
    fields = [
        "color_primaries", "transfer_characteristics", "matrix_coefficients",
        "mastering_display_color_primaries", "mastering_display_luminance",
        "maximum_content_light_level", "maximum_frame_average_light_level",
        "hdr_format", "hdr_format_compatibility",
    ]
    for f in fields:
        val = getattr(video_track, f, None)
        if val:
            hdr[f] = val
    return hdr


def extract(path: Path) -> dict:
    meta = {}

    try:
        from pymediainfo import MediaInfo
        info = MediaInfo.parse(path)

        for track in info.tracks:
            t = track.track_type
            d = _clean(track)

            if t == "General":
                meta["general"] = d
                # Chapters
                chapters = getattr(track, "count_of_menu_streams", None)
                if chapters:
                    meta["chapters_count"] = chapters

            elif t == "Video":
                stream = d.copy()
                # HDR
                hdr = _hdr_info(track)
                if hdr:
                    stream["hdr"] = hdr
                # Frame rate as float
                try:
                    fr = getattr(track, "frame_rate", None)
                    if fr:
                        stream["frame_rate_float"] = float(fr)
                except Exception:
                    pass
                # Pixel aspect ratio
                stream["pixel_aspect_ratio"] = getattr(track, "pixel_aspect_ratio", None)
                meta.setdefault("video_streams", []).append(stream)

            elif t == "Audio":
                meta.setdefault("audio_streams", []).append(d)

            elif t == "Text":
                meta.setdefault("subtitle_streams", []).append(d)

            elif t == "Menu":
                meta.setdefault("menu", []).append(d)

            else:
                meta.setdefault("other", []).append(d)

        # Summary
        gen = meta.get("general", {})
        meta["summary"] = {
            "duration_sec": gen.get("duration"),
            "overall_bitrate_kbps": gen.get("overall_bit_rate"),
            "format": gen.get("format"),
            "video_stream_count": len(meta.get("video_streams", [])),
            "audio_stream_count": len(meta.get("audio_streams", [])),
            "subtitle_stream_count": len(meta.get("subtitle_streams", [])),
            "encoded_application": gen.get("encoded_application"),
            "encoded_date": gen.get("encoded_date"),
            "tagged_date": gen.get("tagged_date"),
        }

    except ImportError:
        meta["error"] = "pymediainfo not installed. Run: pip install pymediainfo"
    except Exception as e:
        meta["error"] = str(e)

    return meta
