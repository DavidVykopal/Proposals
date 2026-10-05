#!/bin/bash
# Render rozpocet-2027.html to A4 PDF with headless Chrome.
# Serves the folder on a throwaway port (webfonts need an http origin), renders, kills the server.
set -euo pipefail
cd "$(dirname "$0")/.."

CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
PORT=8793
OUT="NOXGAMES-Vydaje-odmenovani-rozpocet-2027.pdf"

python3 -m http.server "$PORT" --bind 127.0.0.1 >/dev/null 2>&1 &
SERVER=$!
trap 'kill $SERVER 2>/dev/null || true' EXIT
sleep 1

"$CHROME" --headless --disable-gpu --no-pdf-header-footer --print-to-pdf-no-header \
  --virtual-time-budget=8000 --run-all-compositor-stages-before-draw \
  --print-to-pdf="$PWD/$OUT" "http://127.0.0.1:$PORT/rozpocet-2027.html" >/dev/null 2>&1
echo "$OUT  $(du -h "$OUT" | cut -f1)"
