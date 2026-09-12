#!/usr/bin/env python3
"""
Media Metadata Extractor  -  Powerful CLI
==========================================
Extracts deep metadata from images, videos, and audio files.

Features:
  - EXIF, GPS (lat/lon/altitude/speed/direction), ICC, DPI
  - Color palette, brightness, dominant colors
  - Steganography heuristic detection
  - File signature / magic bytes verification
  - Anomaly detection (extension mismatch, hidden archives)
  - MD5 + SHA1 + SHA256 hashes
  - HDR info for videos
  - Waveform stats for WAV audio
  - Parallel directory scanning
  - JSON and CSV export

Usage:
  python main.py photo.jpg
  python main.py video.mp4 -o result.json
  python main.py ./media --dir -r --csv report.csv
  python main.py ./media --dir -r -w 8
"""
import argparse
import json
import sys
from pathlib import Path

from media_extractor.analyzer import analyze_file, analyze_directory, to_csv


# ── ANSI colour palette ────────────────────────────────────────────────────────
RESET   = "\033[0m"
RED     = "\033[91m"
GREEN   = "\033[92m"
YELLOW  = "\033[93m"
BLUE    = "\033[94m"
MAGENTA = "\033[95m"
CYAN    = "\033[96m"
WHITE   = "\033[97m"
BOLD    = "\033[1m"
DIM     = "\033[2m"
# ──────────────────────────────────────────────────────────────────────────────


BANNER = (
    f"{CYAN}"
    r"""
 ███╗   ███╗███████╗██████╗ ██╗ █████╗     ███████╗██╗  ██╗████████╗
 ████╗ ████║██╔════╝██╔══██╗██║██╔══██╗    ██╔════╝╚██╗██╔╝╚══██╔══╝
 ██╔████╔██║█████╗  ██║  ██║██║███████║    █████╗   ╚███╔╝    ██║
 ██║╚██╔╝██║██╔══╝  ██║  ██║██║██╔══██║    ██╔══╝   ██╔██╗    ██║
 ██║ ╚═╝ ██║███████╗██████╔╝██║██║  ██║    ███████╗██╔╝ ██╗   ██║
 ╚═╝     ╚═╝╚══════╝╚═════╝ ╚═╝╚═╝  ╚═╝    ╚══════╝╚═╝  ╚═╝   ╚═╝"""
    + f"""
{RESET}
{MAGENTA}{BOLD}          Media Metadata Extractor  |  cyberasistent{RESET}
{CYAN}{'═' * 68}{RESET}
  {YELLOW}🛡️  Tool     :{RESET} {WHITE}Media Metadata Extractor — Deep Forensics CLI{RESET}
  {GREEN}👨‍💻 Built by :{RESET} {BOLD}{MAGENTA}Arup Halder{RESET}
  {BLUE}🐙 GitHub   :{RESET} {CYAN}https://github.com/rootNyx404{RESET}
  {RED}⚡ Version  :{RESET} {WHITE}v1.0.0{RESET}
{CYAN}{'═' * 68}{RESET}
{DIM}{YELLOW}        [ All rights reserved © Arup Halder 2024 ]{RESET}
{CYAN}{'═' * 68}{RESET}
"""
)


def parse_args():
    p = argparse.ArgumentParser(
        description="Extract deep metadata from images, videos, and audio files.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    p.add_argument("target", help="File or directory to analyze")
    p.add_argument("-o", "--output", help="Save JSON result to this file")
    p.add_argument("--csv", dest="csv_output", help="Save CSV report to this file")
    p.add_argument("--dir", action="store_true", help="Treat target as a directory")
    p.add_argument("-r", "--recursive", action="store_true",
                   help="Recurse into sub-directories (requires --dir)")
    p.add_argument("-w", "--workers", type=int, default=4,
                   help="Parallel worker threads for directory scan (default: 4)")
    p.add_argument("--no-banner", action="store_true", help="Suppress ASCII banner")
    p.add_argument("--quiet", action="store_true",
                   help="Only output JSON/CSV, no status messages")
    return p.parse_args()


def _print(msg, quiet=False):
    if not quiet:
        print(msg, file=sys.stderr)


def main():
    args = parse_args()

    if not args.no_banner and not args.quiet:
        print(BANNER)

    target = Path(args.target)

    if args.dir:
        if not target.is_dir():
            print(f"{RED}[ERROR]{RESET} '{target}' is not a directory.", file=sys.stderr)
            sys.exit(1)
        _print(f"{BLUE}[*]{RESET} Scanning directory: {target} "
               f"(recursive={args.recursive}, workers={args.workers})",
               args.quiet)
        result = analyze_directory(target, recursive=args.recursive, max_workers=args.workers)
        _print(f"{GREEN}[+]{RESET} Found {result['total_files']} media files | "
               f"Total size: {result['total_size_human']} | "
               f"Anomalies in: {result['files_with_anomalies'] or 'none'}",
               args.quiet)

        if args.csv_output:
            csv_data = to_csv(result["files"])
            Path(args.csv_output).write_text(csv_data, encoding="utf-8")
            _print(f"{GREEN}[+]{RESET} CSV saved to: {args.csv_output}", args.quiet)

    else:
        _print(f"{BLUE}[*]{RESET} Analyzing: {target}", args.quiet)
        result = analyze_file(target)
        mtype = result.get("media_type", "?")
        anomalies = result.get("anomalies", [])
        _print(f"{GREEN}[+]{RESET} Type: {mtype} | Anomalies: {anomalies or 'none'}", args.quiet)

        if args.csv_output:
            csv_data = to_csv([result])
            Path(args.csv_output).write_text(csv_data, encoding="utf-8")
            _print(f"{GREEN}[+]{RESET} CSV saved to: {args.csv_output}", args.quiet)

    json_output = json.dumps(result, indent=2, ensure_ascii=False, default=str)

    if args.output:
        Path(args.output).write_text(json_output, encoding="utf-8")
        _print(f"{GREEN}[+]{RESET} JSON saved to: {args.output}", args.quiet)
    else:
        print(json_output)


if __name__ == "__main__":
    main()
