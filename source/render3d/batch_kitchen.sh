# Kitchen renders for the v3 deck (reference style: dark cabinetry, backlit niche, marble counter, ceiling-mounted arm).
# Writes final/*_color.png; then run: python3 make_kitchen_assets.py
set -e
N="node shot.js"
$N kluxe final/lx_hero.png 2400 1350 "task=stir&off=95,42,150&lookOff=12,14,0&fov=36" > /dev/null
$N kluxe final/lx_front.png 2400 1350 "task=stir&view=front" > /dev/null
$N kluxe final/lx_wide.png 2000 1250 "task=stir&view=wide" > /dev/null
$N kluxe final/lx_insight.png 1600 1000 "norobot=1" > /dev/null
for t in lid pick drop tongs stir knob; do $N kluxe final/lx_$t.png 1000 760 "task=$t" > /dev/null; done
$N kluxe final/lx_plate.png 1000 760 "task=plate&bx=18" > /dev/null
$N kpro final/pro_wide.png 2000 1250 "task=wide&mount=over&q0=0,30,80,40,-90,0&env=0.7" > /dev/null
for t in tongs pick lid plate; do $N kpro final/pro_$t.png 1000 760 "task=$t&mount=over&env=0.7" > /dev/null; done
echo done
