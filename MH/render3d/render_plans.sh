# Representative real plan (user drawing, 구축 2Bay A) as drawn and with the MH kitchen Interface -> MH/assets/renders
set -e
cd "$(dirname "$0")"
O=../assets/renders
N="node shot.js plan"
$N $O/plan_old2a_top_orig.png 1400 1320 "id=old2a&arki=0&view=top&pad=0.03" > /dev/null
$N $O/plan_old2a_top_arki.png 1400 1320 "id=old2a&arki=1&task=hero&zones=1&view=top&pad=0.03" > /dev/null
$N $O/plan_old2a_kitchen.png 1600 1100 "id=old2a&arki=1&task=hero&view=persp&cam=455,215,600&look=160,100,362&fov=50" > /dev/null
$N $O/plan_old2a_unit.png 1600 1200 "id=old2a&arki=1&task=hero&zones=1&dir3=-0.5,1.05,1.0&pad=0.03" > /dev/null
$N $O/plan_old2a_verify.png 200 150 "id=old2a&arki=1&task=deploy&verify=1" > /dev/null
python3 - <<'PY'
import glob, json
from PIL import Image
for f in sorted(glob.glob('../assets/renders/plan_old2a_*.png')):
    if 'verify' in f: continue
    Image.open(f).save(f, optimize=True)
    j = json.load(open(f[:-4] + '.json')); print(f.split('/')[-1], 'ik', j.get('ik'))
print('verify', json.load(open('../assets/renders/plan_old2a_verify.json'))['ik'])
PY
# second old plan (as drawn) for the appendix
$N $O/plan_old2b_top_orig.png 1400 1100 "id=old2b&arki=0&view=top&pad=0.03" > /dev/null
$N $O/plan_old2b_unit.png 1600 1200 "id=old2b&arki=0&pad=0.03" > /dev/null
$N $O/plan_old2a_unit_orig.png 1600 1200 "id=old2a&arki=0&dir3=-0.5,1.05,1.0&pad=0.03" > /dev/null
# new 4Bay (as drawn)
$N $O/plan_new4_top_orig.png 1400 1000 "id=new4&arki=0&view=top&pad=0.03" > /dev/null
$N $O/plan_new4_unit.png 1600 1200 "id=new4&arki=0&pad=0.03" > /dev/null
# new 3Bay (as drawn; not used in the deck — one representative plan only)
$N $O/plan_new3_top_orig.png 1400 1250 "id=new3&arki=0&view=top&pad=0.03" > /dev/null
$N $O/plan_new3_unit.png 1600 1200 "id=new3&arki=0&pad=0.03" > /dev/null
