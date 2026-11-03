#!/bin/zsh
# Render the one page (PDF + PNG) and the wide card (PNG) with headless Chrome.
# Needs Google Chrome and poppler (pdftoppm). Outputs land in the repo root.
set -e
cd "${0:A:h}"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
OUT=..
"$CHROME" --headless=new --disable-gpu --virtual-time-budget=15000 --no-pdf-header-footer \
  --print-to-pdf="$OUT/loop-engineering.pdf" "file://$PWD/loop-engineering.html"
pdftoppm -png -r 220 -singlefile "$OUT/loop-engineering.pdf" "$OUT/loop-engineering"
python3 build_wide.py
"$CHROME" --headless=new --disable-gpu --virtual-time-budget=15000 --hide-scrollbars \
  --window-size=1600,900 --force-device-scale-factor=2 \
  --screenshot="$OUT/loop-engineering-wide.png" "file://$PWD/loop-engineering-wide.html"
