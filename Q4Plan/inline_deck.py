#!/usr/bin/env python3
"""Make a single-file copy of the Q4 kickoff deck for sharing.

Usage: python3 inline_deck.py
Reads q4-kickoff-prezentace.html (the editable source, references assets/) and writes
q4-kickoff-prezentace-share.html with images and fonts embedded as data URIs.
Edit the source, then rerun this. Fonts are downloaded once into assets/fonts/google/.
"""
import base64
import mimetypes
import re
import urllib.request
from pathlib import Path

HERE = Path(__file__).parent
SRC = HERE / "q4-kickoff-prezentace.html"
OUT = HERE / "q4-kickoff-prezentace-share.html"
FONT_DIR = HERE / "assets" / "fonts" / "google"
SUBSETS = ("latin", "latin-ext")
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"


def fetch(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA})).read()


def data_uri(path, mime=None):
    mime = mime or mimetypes.guess_type(path.name)[0]
    return f"data:{mime};base64,{base64.b64encode(path.read_bytes()).decode()}"


def fonts_css(css_url):
    FONT_DIR.mkdir(parents=True, exist_ok=True)
    css_file = FONT_DIR / "fonts.css"
    if not css_file.exists():
        css_file.write_bytes(fetch(css_url))
    out = []
    for subset, block in re.findall(r"/\* ([\w-]+) \*/\s*(@font-face\s*{[^}]*})", css_file.read_text()):
        if subset not in SUBSETS:
            continue
        url = re.search(r"url\((https://[^)]+)\)", block).group(1)
        local = FONT_DIR / url.rsplit("/", 1)[1]
        if not local.exists():
            local.write_bytes(fetch(url))
        out.append(block.replace(url, data_uri(local, "font/woff2")))
    return "\n".join(out)


def main():
    s = SRC.read_text()
    link = re.search(r'<link href="(https://fonts\.googleapis\.com/css2[^"]+)" rel="stylesheet">', s)
    s = s.replace(link.group(0), f"<style>\n{fonts_css(link.group(1))}\n</style>")
    s = re.sub(r'<link rel="preconnect"[^>]*>', "", s)
    cache = {}

    def embed(m):
        rel = m.group(1)
        if rel not in cache:
            cache[rel] = data_uri(HERE / rel)
        return f'src="{cache[rel]}"'

    s = re.sub(r'src="(assets/[^"]+)"', embed, s)
    # outbound <a href> links (YouTube) are fine, only resources must be embedded
    left = re.findall(r'src="(?!data:)[^"]*"|<link[^>]*>|url\((?!data:)[^)]*\)', s)
    assert not left, left
    OUT.write_text(s)
    print(f"{OUT.name}: {OUT.stat().st_size / 1e6:.1f} MB, {len(cache)} images embedded")


if __name__ == "__main__":
    main()
