# MH Adaptive Kitchen Hand concept renders -> MH/assets/renders (PNG + label-anchor JSON). CONCEPT only.
set -e
cd "$(dirname "$0")"
O=../assets/renders
node shot.js handHero $O/hand_hero.png 1400 1200 "cam=34,22,30&look=0,9.8,0&fov=25" > /dev/null
for o in plate cup bowl tool; do node shot.js handGrasp $O/hand_$o.png 900 900 "obj=$o" > /dev/null; done
python3 - <<'PY'
import glob
from PIL import Image
for f in sorted(glob.glob('../assets/renders/hand_*.png')):
    Image.open(f).save(f, optimize=True); print(f.split('/')[-1])
PY
