#!/usr/bin/env python3
"""
Trim transparent or uniform padding from GIFs in Gifs/ so digits sit close when displayed side by side.
Requires: pip install Pillow
Usage: python3 trim_gifs.py
"""
from pathlib import Path

try:
    from PIL import Image, ImageSequence
except ImportError:
    print("Please install Pillow: pip install Pillow")
    raise SystemExit(1)

GIFS_DIR = Path(__file__).parent / "Gifs"
DIGITS = "0123456789"


def trim_gif(path):
    """Trim one GIF in place by removing transparent/uniform borders. Keeps original palette and transparency."""
    img = Image.open(path)
    n_frames = getattr(img, "n_frames", 1) or 1

    # Use RGBA only to compute bbox of non-transparent content; then crop the original P-mode image(s) so we keep palette and transparency
    rgba = img.convert("RGBA")
    bbox = rgba.getbbox()
    if not bbox:
        return

    trans_index = img.info.get("transparency")

    if n_frames <= 1:
        out = img.crop(bbox)
        kwargs = {}
        if trans_index is not None:
            kwargs["transparency"] = trans_index
        out.save(path, "GIF", **kwargs)
        return

    # Animated: crop each frame in place (keep P mode and palette)
    frames = []
    durations = []
    for frame in ImageSequence.Iterator(img):
        f = frame.crop(bbox)
        frames.append(f)
        durations.append(frame.info.get("duration", 100))
    loop = img.info.get("loop", 0)
    dur = durations[0] if durations else 100
    kwargs = {"save_all": True, "append_images": frames[1:], "duration": dur, "loop": loop}
    if trans_index is not None:
        kwargs["transparency"] = trans_index
    frames[0].save(path, "GIF", **kwargs)


def main():
    if not GIFS_DIR.is_dir():
        print("Gifs directory not found:", GIFS_DIR)
        return
    for d in DIGITS:
        path = GIFS_DIR / f"{d}.gif"
        if path.is_file():
            print("Trimming", path.name)
            try:
                trim_gif(path)
            except Exception as e:
                print("  Error:", e)
    print("Done.")


if __name__ == "__main__":
    main()
