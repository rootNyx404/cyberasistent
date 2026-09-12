"""Image metadata extraction: EXIF, GPS, ICC, color palette, steganography hints."""
from pathlib import Path


# ── GPS helpers ───────────────────────────────────────────────────────────────
def _gps_decimal(values, ref) -> float:
    try:
        d, m, s = [float(v.numerator) / float(v.denominator) for v in values]
    except Exception:
        d, m, s = [float(v) for v in values]
    dec = d + m / 60 + s / 3600
    return round(-dec if ref in ("S", "W") else dec, 7)


def _parse_gps_block(g: dict) -> dict:
    """Parse full GPS IFD block including altitude, speed, direction."""
    result = {}
    try:
        lat = _gps_decimal(g[2], g[1])
        lon = _gps_decimal(g[4], g[3])
        result["latitude"] = lat
        result["longitude"] = lon
        result["maps_url"] = f"https://maps.google.com/?q={lat},{lon}"
    except Exception:
        pass
    # Altitude
    try:
        alt_val = g.get(6)
        alt_ref = g.get(5, 0)  # 0 = above sea level
        if alt_val is not None:
            alt = float(alt_val.numerator) / float(alt_val.denominator)
            result["altitude_m"] = round(-alt if alt_ref == 1 else alt, 2)
    except Exception:
        pass
    # Speed
    try:
        spd = g.get(13)
        spd_ref = g.get(12, "K")  # K=km/h, M=mph, N=knots
        if spd is not None:
            result["speed"] = f"{float(spd.numerator)/float(spd.denominator):.2f} {spd_ref}"
    except Exception:
        pass
    # Direction / bearing
    try:
        img_dir = g.get(17)
        if img_dir is not None:
            result["direction_deg"] = round(float(img_dir.numerator) / float(img_dir.denominator), 2)
    except Exception:
        pass
    # Timestamp
    try:
        date = g.get(29, "")
        time_vals = g.get(7, [])
        if date and time_vals:
            h, m, s = [float(v.numerator) / float(v.denominator) for v in time_vals]
            result["gps_timestamp"] = f"{date} {int(h):02d}:{int(m):02d}:{int(s):02d} UTC"
    except Exception:
        pass
    return result


# ── Color analysis ────────────────────────────────────────────────────────────
def _color_analysis(img) -> dict:
    """Dominant colors, brightness, entropy estimate."""
    result = {}
    try:
        # Convert to RGB for uniform analysis
        rgb = img.convert("RGB")
        # Resize to speed up processing
        small = rgb.resize((100, 100))
        pixels = list(small.getdata())
        total = len(pixels)

        # Average color
        avg_r = sum(p[0] for p in pixels) // total
        avg_g = sum(p[1] for p in pixels) // total
        avg_b = sum(p[2] for p in pixels) // total
        result["average_color_rgb"] = [avg_r, avg_g, avg_b]
        result["average_color_hex"] = f"#{avg_r:02x}{avg_g:02x}{avg_b:02x}"

        # Brightness (perceived luminance)
        brightness = (0.299 * avg_r + 0.587 * avg_g + 0.114 * avg_b) / 255
        result["brightness"] = round(brightness, 3)
        result["brightness_label"] = (
            "dark" if brightness < 0.33 else "medium" if brightness < 0.66 else "bright"
        )

        # Top 5 dominant colors via quantize
        quantized = small.quantize(colors=5)
        palette = quantized.getpalette()[:15]  # 5 colors * 3 channels
        dominant = []
        for i in range(5):
            r, g, b = palette[i*3], palette[i*3+1], palette[i*3+2]
            dominant.append({"rgb": [r, g, b], "hex": f"#{r:02x}{g:02x}{b:02x}"})
        result["dominant_colors"] = dominant

        # Transparency check
        if img.mode in ("RGBA", "LA", "PA"):
            alpha_channel = img.split()[-1]
            alpha_pixels = list(alpha_channel.getdata())
            transparent = sum(1 for a in alpha_pixels if a < 128)
            result["transparent_pixels_pct"] = round(transparent / len(alpha_pixels) * 100, 2)

    except Exception as e:
        result["color_error"] = str(e)
    return result


# ── Steganography hints ───────────────────────────────────────────────────────
def _steg_hints(path: Path, img) -> dict:
    """Heuristic checks that may indicate hidden data."""
    hints = []
    score = 0

    try:
        # 1. File size vs expected size ratio
        stat_size = path.stat().st_size
        expected = img.width * img.height * len(img.getbands())
        ratio = stat_size / max(expected, 1)
        if ratio > 1.5:
            hints.append(f"File size ({stat_size}B) is {ratio:.1f}x larger than raw pixel data — possible appended data.")
            score += 2

        # 2. Unusual comment/metadata chunks (PNG)
        if img.format == "PNG":
            text_chunks = img.info
            if len(text_chunks) > 5:
                hints.append(f"PNG has {len(text_chunks)} metadata chunks — unusually high.")
                score += 1

        # 3. LSB randomness check on small sample
        try:
            rgb = img.convert("RGB")
            small = rgb.resize((50, 50))
            pixels = list(small.getdata())
            lsb_values = [(p[0] & 1, p[1] & 1, p[2] & 1) for p in pixels]
            ones = sum(v for triple in lsb_values for v in triple)
            total_bits = len(lsb_values) * 3
            lsb_ratio = ones / total_bits
            # Natural images: LSB ratio ~0.5 but with some bias
            if 0.48 <= lsb_ratio <= 0.52:
                hints.append(f"LSB ratio {lsb_ratio:.3f} is near-perfect 50% — may indicate LSB steganography.")
                score += 2
        except Exception:
            pass

    except Exception as e:
        hints.append(f"Steg check error: {e}")

    return {
        "suspicion_score": score,
        "suspicion_level": "high" if score >= 3 else "medium" if score >= 1 else "low",
        "hints": hints,
    }


# ── Main extractor ────────────────────────────────────────────────────────────
def extract(path: Path) -> dict:
    meta = {}

    # Pillow
    try:
        from PIL import Image
        from PIL.ExifTags import TAGS, GPSTAGS

        with Image.open(path) as img:
            meta["format"] = img.format
            meta["mode"] = img.mode
            meta["width"] = img.width
            meta["height"] = img.height
            meta["megapixels"] = round(img.width * img.height / 1_000_000, 2)
            meta["aspect_ratio"] = f"{img.width}:{img.height}"
            meta["color_bands"] = img.getbands()
            meta["icc_profile_present"] = img.info.get("icc_profile") is not None
            meta["dpi"] = img.info.get("dpi")

            # Color analysis
            meta["color_analysis"] = _color_analysis(img)

            # Steganography hints
            meta["steganography_hints"] = _steg_hints(path, img)

            # EXIF
            raw_exif = img._getexif() if hasattr(img, "_getexif") else None
            if raw_exif:
                exif = {}
                for tag_id, val in raw_exif.items():
                    tag = TAGS.get(tag_id, str(tag_id))
                    if tag == "GPSInfo":
                        continue  # handled separately
                    try:
                        exif[tag] = str(val)
                    except Exception:
                        exif[tag] = "<unreadable>"
                meta["exif"] = exif

                # GPS
                GPS_IFD = 34853
                if GPS_IFD in raw_exif:
                    meta["gps"] = _parse_gps_block(raw_exif[GPS_IFD])

    except ImportError:
        meta["warning"] = "Pillow not installed (pip install Pillow)"
    except Exception as e:
        meta["pillow_error"] = str(e)

    # exifread (deeper EXIF coverage)
    try:
        import exifread
        with open(path, "rb") as f:
            tags = exifread.process_file(f, details=True)
        meta["exifread"] = {k: str(v) for k, v in tags.items()}
    except ImportError:
        pass
    except Exception as e:
        meta["exifread_error"] = str(e)

    # pymediainfo
    try:
        from pymediainfo import MediaInfo
        info = MediaInfo.parse(path)
        for track in info.tracks:
            if track.track_type == "General":
                meta["mediainfo"] = {k: v for k, v in track.to_data().items() if v not in (None, "")}
    except ImportError:
        pass
    except Exception as e:
        meta["mediainfo_error"] = str(e)

    return meta
