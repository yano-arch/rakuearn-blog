#!/bin/sh
# チェック済みのバッチを書き出して公開する: sh tools/publish.sh b11 b12 ...
set -e
cd "$(dirname "$0")/.."
python3 tools/export_batch.py "$@" > /dev/null
for b in "$@"; do
  git add -f "art_items/$b.py" "data/items/$b.json"
  for s in $(python3 -c "import json;print(' '.join(i['slug'] for i in json.load(open('data/items/$b.json'))))"); do
    git add -f "public/images/svg/$s.svg" "public/images/png/$s.png"
  done
done
python3 tools/readings.py > /dev/null && git add data/readings_ja.json
python3 build.py
git -c user.name="yano-arch" -c user.email="yano@studyshort.co.jp" commit -qm "Add illustrations: $*

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01EDMcckEBDPXo8Z4fnALAoH"
git fetch -q origin main && git rebase -q origin/main && git push -q origin main
git log --oneline -1
