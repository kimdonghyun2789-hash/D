# MH (ex-ARKI) kitchen concept renders -> MH/assets/renders (PNG + label-anchor JSON). Requires: npm install (three 0.170) + playwright Chromium.
set -e
cd "$(dirname "$0")"
O=../assets/renders
N="node shot.js"
$N linear $O/cover_hero.png 2400 1350 "task=hero&view=hero&path=1&leftwall=0&cam=405,182,345&look=200,104,30&fov=39" > /dev/null
$N linear $O/cover_tall.png 1800 1500 "task=hero&view=hero&path=1&leftwall=0&cam=505,215,500&look=196,108,40&fov=39" > /dev/null
i=1; for t in detect pick load unload store; do $N linear $O/seq_${i}_$t.png 1100 840 "task=$t&view=seq" > /dev/null; i=$((i+1)); done
$N before $O/before.png 1500 1075 "" > /dev/null
$N linear $O/after.png 1500 1075 "task=load&view=after&zones=1&human=1&hx=64&hz=168&hr=-1.57&ret=1" > /dev/null
for t in 2 3 4; do
  $N apt $O/apt${t}_unit.png 1500 1125 "type=$t&mode=unit" > /dev/null
  $N apt $O/apt${t}_kitchen.png 1500 1125 "type=$t&mode=kitchen" > /dev/null
done
python3 - <<'PY'
import os, glob
from PIL import Image
for f in glob.glob('../assets/renders/*.png'):
    im = Image.open(f); im.save(f, optimize=True)
print('optimized', len(glob.glob('../assets/renders/*.png')))
PY
