#!/bin/bash
# Render the A4 one-pager(s) to PDF with headless Chrome.
#   ./tools/build-pdf.sh            renders both languages
#   ./tools/build-pdf.sh cs         renders one
#
# Chrome needs a real http origin for the webfonts, so this serves ./public on a
# throwaway port, renders, then kills the server. Nothing is left running.

set -euo pipefail
cd "$(dirname "$0")/.."

CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
PORT=8791
PAGES=("${@:-en cs}")
[ $# -gt 0 ] && PAGES=("$@")

python3 -m http.server "$PORT" --directory public --bind 127.0.0.1 >/dev/null 2>&1 &
SERVER=$!
trap 'kill $SERVER 2>/dev/null || true' EXIT
sleep 1

for lang in ${PAGES[@]}; do
  if [ "$lang" = "en" ]; then src="onepager.html"; out="public/PuppetSports-Partnership-EN.pdf";
  else src="onepager.$lang.html"; out="public/PuppetSports-Partnership-$(echo "$lang" | tr '[:lower:]' '[:upper:]').pdf"; fi
  [ -f "public/$src" ] || { echo "skip $lang: public/$src missing"; continue; }
  "$CHROME" --headless --disable-gpu --no-pdf-header-footer --print-to-pdf-no-header \
    --virtual-time-budget=8000 --run-all-compositor-stages-before-draw \
    --print-to-pdf="$PWD/$out" "http://127.0.0.1:$PORT/$src" >/dev/null 2>&1
  echo "$out  $(du -h "$out" | cut -f1)"
done
