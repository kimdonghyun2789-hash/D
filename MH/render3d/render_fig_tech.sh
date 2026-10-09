# MH deck figures, group "tech" (m03 kitchen work area · m05 card image · B5 zoning) -> MH/assets/renders/fig_tech_*
# Existing scenes and parameters only (web/*.js unchanged). PNG (transparent background) + anchors JSON. CONCEPT images.
#  m05 cards 2-4 reuse existing renders (v2_seq_3_load · v2_seq_1_detect · v2_stow_2_open, cropped on the slide).
set -e
cd "$(dirname "$0")"
O=../assets/renders
# m03: secured plan 구축 2Bay A kitchen with the MH Interface fitted (arki=1, as in B4) · robot zone + reach volume (zones=1) · robot loading the dishwasher
node shot.js plan $O/fig_tech_m03_kitchen.png 1382 1200 "id=old2a&arki=1&task=load&zones=1&view=persp&cam=545,390,600&look=175,78,415&fov=40" > /dev/null
# B5: v2 kitchen run + return counter seen from above (about 18 deg off vertical): robot zone · human zone · no-go over the cooktop
node shot.js run2 $O/fig_tech_b5_zones.png 1300 872 "railz=30&task=hero&zones=1&ret=1&cam=175,1100,420&lx=175&ly=40&lz=85&fov=16" > /dev/null
python3 - <<'PY'
import glob, json
from PIL import Image
# m05 card 1: one hand, three grasps = existing renders hand_tool | hand_cup | hand_plate (render_hand.sh), portrait crops side by side
O = '../assets/renders'; PW, PH, G = 452, 603, 12
out = Image.new('RGBA', (3 * PW + 2 * G, PH), (0, 0, 0, 0))
for i, (n, fx) in enumerate([('hand_tool', 0.42), ('hand_cup', 0.56), ('hand_plate', 0.45)]):
    im = Image.open(f'{O}/{n}.png').convert('RGBA'); s = im.height; cw = round(s * PW / PH)
    x0 = min(max(round(fx * im.width - cw / 2), 0), im.width - cw)
    out.alpha_composite(im.crop((x0, 0, x0 + cw, s)).resize((PW, PH), Image.LANCZOS), (i * (PW + G), 0))
    if i: out.paste((255, 255, 255, 255), (i * (PW + G) - G, 0, i * (PW + G), PH))     # white gap between panels
out.save(f'{O}/fig_tech_m05_hand.png', optimize=True)
json.dump({'anchors': {}, 'source': 'hand_tool | hand_cup | hand_plate (render_hand.sh), portrait crops, CONCEPT'}, open(f'{O}/fig_tech_m05_hand.json', 'w'))
for f in sorted(glob.glob('../assets/renders/fig_tech_*.png')):
    Image.open(f).save(f, optimize=True)
    j = json.load(open(f[:-4] + '.json')); print(f.split('/')[-1], Image.open(f).size, 'ik', j.get('ik'))
PY
