"""Audio metadata extraction: tags, technical info, waveform stats."""
from pathlib import Path


def _waveform_stats(path: Path) -> dict:
    """Basic waveform statistics for WAV files using stdlib wave module."""
    stats = {}
    try:
        import wave, struct, math
        with wave.open(str(path), "rb") as wf:
            n_frames = wf.getnframes()
            n_channels = wf.getnchannels()
            sampwidth = wf.getsampwidth()
            framerate = wf.getframerate()
            raw = wf.readframes(min(n_frames, 44100))  # read up to 1 sec

        fmt = {1: "b", 2: "h", 4: "i"}.get(sampwidth, "h")
        samples = struct.unpack(f"{len(raw)//sampwidth}{fmt}", raw)
        if samples:
            max_val = max(abs(s) for s in samples)
            rms = math.sqrt(sum(s*s for s in samples) / len(samples))
            peak_db = 20 * math.log10(max_val / (2 ** (sampwidth * 8 - 1))) if max_val > 0 else -float("inf")
            rms_db = 20 * math.log10(rms / (2 ** (sampwidth * 8 - 1))) if rms > 0 else -float("inf")
            stats["peak_amplitude_db"] = round(peak_db, 2)
            stats["rms_db"] = round(rms_db, 2)
            stats["sample_count_analyzed"] = len(samples)
    except Exception as e:
        stats["waveform_error"] = str(e)
    return stats


def extract(path: Path) -> dict:
    meta = {}

    # mutagen
    try:
        from mutagen import File as MFile
        from mutagen.id3 import ID3NoHeaderError
        af = MFile(path, easy=False)
        if af is not None:
            info = af.info
            meta["duration_sec"] = round(getattr(info, "length", 0), 3)
            meta["duration_human"] = _fmt_duration(getattr(info, "length", 0))
            meta["bitrate_kbps"] = getattr(info, "bitrate", None)
            meta["sample_rate_hz"] = getattr(info, "sample_rate", None)
            meta["channels"] = getattr(info, "channels", None)
            meta["encoder"] = getattr(info, "encoder_info", None)
            meta["codec"] = type(info).__name__

            if af.tags:
                raw_tags = {}
                for k, v in af.tags.items():
                    try:
                        raw_tags[k] = str(v)
                    except Exception:
                        raw_tags[k] = "<unreadable>"
                meta["tags"] = raw_tags

                # Friendly tag summary
                meta["tag_summary"] = _friendly_tags(af.tags)

    except ImportError:
        meta["warning"] = "mutagen not installed (pip install mutagen)"
    except Exception as e:
        meta["mutagen_error"] = str(e)

    # WAV waveform stats
    if path.suffix.lower() == ".wav":
        meta["waveform_stats"] = _waveform_stats(path)

    # pymediainfo
    try:
        from pymediainfo import MediaInfo
        info = MediaInfo.parse(path)
        streams = []
        for track in info.tracks:
            if track.track_type in ("General", "Audio"):
                streams.append({k: v for k, v in track.to_data().items() if v not in (None, "")})
        meta["mediainfo"] = streams
    except ImportError:
        pass
    except Exception as e:
        meta["mediainfo_error"] = str(e)

    return meta


def _fmt_duration(seconds: float) -> str:
    seconds = int(seconds)
    h, rem = divmod(seconds, 3600)
    m, s = divmod(rem, 60)
    return f"{h:02d}:{m:02d}:{s:02d}"


def _friendly_tags(tags) -> dict:
    """Extract common tag fields into a clean dict."""
    friendly = {}
    mapping = {
        # ID3
        "TIT2": "title", "TPE1": "artist", "TALB": "album",
        "TDRC": "year", "TRCK": "track", "TCON": "genre",
        "TCOM": "composer", "TPUB": "publisher", "COMM": "comment",
        "APIC": "cover_art_present",
        # Vorbis / FLAC
        "title": "title", "artist": "artist", "album": "album",
        "date": "year", "tracknumber": "track", "genre": "genre",
        "composer": "composer", "comment": "comment",
        # MP4
        "\xa9nam": "title", "\xa9ART": "artist", "\xa9alb": "album",
        "\xa9day": "year", "trkn": "track", "\xa9gen": "genre",
    }
    for raw_key, friendly_key in mapping.items():
        val = tags.get(raw_key)
        if val is not None:
            if friendly_key == "cover_art_present":
                friendly[friendly_key] = True
            else:
                friendly[friendly_key] = str(val)
    return friendly
