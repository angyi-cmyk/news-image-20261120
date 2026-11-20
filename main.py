#!/usr/bin/env python3
"""Entry program for make.fun news-image-20261120 (Python 3.13, stdlib only).

Copies the entry image beside this file to /output/entry.png.
The image is a newspaper-style front page summing up the world news of
Friday 20 November 2026; it is drawn by draw_image.py in this repo.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os
import shutil

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)

here = os.path.dirname(os.path.abspath(__file__))
shutil.copyfile(
    os.path.join(here, "entry.png"),
    os.path.join(out_dir, "entry.png"),
)
