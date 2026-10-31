#!/usr/bin/env python3
"""Copy the retained deck and its logos into the ready-to-publish site."""
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs/decks"
SITE = ROOT / "site"

deck = SITE / "decks/nontech"
deck.mkdir(parents=True, exist_ok=True)
shutil.copy2(SOURCE / "nontech.html", deck / "index.html")
shutil.copytree(SOURCE / "assets", deck / "assets", dirs_exist_ok=True)
shutil.copytree(
    SOURCE / "assets/company-logos",
    SITE / "assets/company-logos",
    dirs_exist_ok=True,
)
print("Synced the retained nontech deck and company logos into site/.")
