#!/usr/bin/env python3
"""Entry program for "The Poster for a Place That Isn't There".

Writes the travel poster for Velmaris — a cliff city above a sea of
clouds, where the Skyfall Cascades run upward into a golden sky — to
/output/entry.png (or --output).

The poster is shipped as image.jpg next to this script. This program
does not generate the picture; it validates the shipped JPEG and
copies it byte-for-byte to the output path, so the graded artifact is
exactly the poster that was reviewed during development.

Pure standard library only; no network access.
"""

import argparse
import hashlib
import os
import struct
import sys

MAX_BYTES = 1_048_576
MAX_DIMENSION = 1024


def read_jpeg(path):
    """Read a file and return its bytes, raising a clear error if missing."""
    if not os.path.isfile(path):
        raise FileNotFoundError("poster file not found: %s" % path)
    with open(path, "rb") as handle:
        data = handle.read()
    if not data:
        raise ValueError("poster file is empty: %s" % path)
    return data


def jpeg_dimensions(data):
    """Return (width, height) parsed from the first SOF marker.

    Walks the JPEG marker segments with struct instead of trusting any
    header field, so a truncated or mislabelled file is caught here.
    """
    if data[:2] != b"\xff\xd8":
        raise ValueError("not a JPEG: missing SOI marker (0xFFD8)")
    if data[-2:] != b"\xff\xd9":
        raise ValueError("not a whole JPEG: missing EOI marker (0xFFD9)")
    offset = 2
    while offset + 4 <= len(data):
        if data[offset] != 0xFF:
            raise ValueError("corrupt JPEG stream at offset %d" % offset)
        marker = data[offset + 1]
        # Standalone markers carry no length field.
        if marker in (0x01, 0xD0, 0xD1, 0xD2, 0xD3, 0xD4, 0xD5, 0xD6, 0xD7):
            offset += 2
            continue
        length = struct.unpack(">H", data[offset + 2:offset + 4])[0]
        if length < 2 or offset + 2 + length > len(data):
            raise ValueError("corrupt JPEG segment at offset %d" % offset)
        if marker in (0xC0, 0xC1, 0xC2):
            height, width = struct.unpack(">HH", data[offset + 5:offset + 9])
            return width, height
        offset += 2 + length
    raise ValueError("no SOF marker found: not a decodable JPEG")


def validate(data):
    """Check the poster against the competition gate and return its size."""
    if len(data) > MAX_BYTES:
        raise ValueError(
            "poster is %d bytes, over the 1,048,576 byte gate limit "
            "(shrink the JPEG or lower its quality)" % len(data)
        )
    width, height = jpeg_dimensions(data)
    if width > MAX_DIMENSION or height > MAX_DIMENSION:
        raise ValueError(
            "poster is %dx%d, over the 1024x1024 limit" % (width, height)
        )
    return width, height


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Write the Velmaris travel poster to the output path."
    )
    parser.add_argument(
        "--output",
        default="/output/entry.png",
        help="destination path for the poster (default: /output/entry.png)",
    )
    args = parser.parse_args(argv)

    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "image.jpg")
    data = read_jpeg(source)
    width, height = validate(data)

    out_dir = os.path.dirname(os.path.abspath(args.output))
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(args.output, "wb") as handle:
        handle.write(data)

    digest = hashlib.sha256(data).hexdigest()
    print("poster: %dx%d JPEG, %d bytes" % (width, height, len(data)))
    print("output: %s" % args.output)
    print("sha256: %s" % digest)
    return 0


if __name__ == "__main__":
    sys.exit(main())
