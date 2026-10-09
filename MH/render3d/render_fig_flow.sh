# MH deck figures, group "flow" (m02 kitchen Physical Workflow · m10 three installation levels) -> MH/assets/renders
# Scenes: web/fig_flow.js (opt-in scene names flowPlain / flowInstall; existing scenes unchanged). PNG + anchors JSON (+ IK / penetration for m10).
set -e
cd "$(dirname "$0")"
O=../assets/renders
# m02: ordinary kitchen, no MH element; human tasks between appliances = dark dashed paths 1-2-3
node shot.js flowPlain $O/fig_flow_kitchen.png 1600 760 "fov=28" > /dev/null
# m10: same camera and scale for the three integration levels (CONCEPT)
C="cam=390,165,580&lx=168&ly=106&lz=30&fov=27"
for l in retrofit remodel newbuild; do node shot.js flowInstall $O/fig_flow_$l.png 1500 800 "level=$l&$C" > /dev/null; done
python3 - <<'PY'
import glob, json
from PIL import Image
for f in sorted(glob.glob('../assets/renders/fig_flow_*.png')):
    Image.open(f).save(f, optimize=True)
    j = json.load(open(f[:-4] + '.json')); print(f.split('/')[-1], Image.open(f).size, 'ik', j.get('ik'))
PY
