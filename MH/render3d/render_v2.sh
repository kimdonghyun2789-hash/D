# MH (ex-ARKI v2) kitchen concept renders (collision-checked robot run) -> MH/assets/renders  (PNG + anchors JSON incl. IK/penetration)
set -e
cd "$(dirname "$0")"
O=../assets/renders
N="node shot.js run2"
Q="railz=30"
$N $O/v2_cover.png 1800 1500 "$Q&task=hero&path=1&leftwall=0&cam=470,215,480&lx=165&ly=100&lz=40&fov=39" > /dev/null
$N $O/v2_seq_1_detect.png 1100 840 "$Q&task=detect&lx=85&ly=100&lz=34&cam=235,162,264" > /dev/null
$N $O/v2_seq_2_pick.png 1100 840 "$Q&task=pick&lx=85&ly=100&lz=34&cam=235,162,264" > /dev/null
$N $O/v2_seq_3_load.png 1100 840 "$Q&task=load&lx=292&ly=62&lz=60&cam=140,150,310" > /dev/null
$N $O/v2_seq_4_unload.png 1100 840 "$Q&task=unload&lx=292&ly=70&lz=60&cam=140,155,310" > /dev/null
$N $O/v2_seq_5_store.png 1100 840 "$Q&task=store&lx=235&ly=72&lz=62&cam=105,160,320" > /dev/null
$N $O/v2_stow_1_closed.png 1100 840 "$Q&task=park&door=0&lx=75&ly=135&lz=30&cam=265,205,330" > /dev/null
$N $O/v2_stow_2_open.png 1100 840 "$Q&task=park&door=1&lx=75&ly=135&lz=30&cam=265,205,330" > /dev/null
$N $O/v2_stow_3_deploy.png 1100 840 "$Q&task=deploy&t=0.6&tcppath=1&sweep=1&lx=60&ly=125&lz=50&cam=290,200,380" > /dev/null
$N $O/v2_stow_4_exit.png 1100 840 "$Q&task=exit&dx=0&arrow=1&lx=95&ly=120&lz=40&cam=300,195,340" > /dev/null
$N $O/v2_stow_5_low.png 1100 840 "$Q&task=load&lx=292&ly=60&lz=62&cam=420,120,250" > /dev/null
$N $O/v2_section_low.png 1000 1150 "$Q&task=load&section=1&span=290" > /dev/null
$N $O/v2_after.png 1500 1075 "$Q&task=load&zones=1&ret=1&human=1&hx=64&hz=168&hr=-1.57&cam=460,330,560&lx=180&ly=70&lz=80&fov=38" > /dev/null
python3 - <<'PY'
import glob, json
from PIL import Image
for f in sorted(glob.glob('../assets/renders/v2_*.png')):
    Image.open(f).save(f, optimize=True)
    j = json.load(open(f[:-4] + '.json')); ik = j.get('ik') or {}
    print(f.split('/')[-1], 'pen', ik.get('pen'), 'posErr', ik.get('posErr'), 'env', ik.get('envelope'))
PY
