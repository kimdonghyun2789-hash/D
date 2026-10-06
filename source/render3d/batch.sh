set -e
N="node shot.js"
# cover (full-bleed 16:9)
$N cell final/cover.png 2400 1350 "task=door&door=0.12&mask=1&cam=-150,175,290&look=16,110,62&fov=15" > /dev/null
# cell overview
$N cell final/overview.png 1800 1150 "task=load&door=0.62&tray=1&mask=1&cam=-190,200,330&look=0,96,70&fov=24" > /dev/null
# workflow panels
$N cell final/s1_door.png 1000 760 "task=door&door=0.25&mask=1&off=-62,30,100" > /dev/null
$N cell final/s2_pick.png 1000 760 "task=pick&mask=1&off=-70,45,85&lookOff=0,-4,0" > /dev/null
$N cell final/s3_load.png 1000 760 "task=load&door=0.62&mask=1&off=12,52,100&lookOff=0,-4,0&fov=26" > /dev/null
$N cell final/s4_press.png 1000 760 "task=press&mask=1&off=-75,38,48&fov=26&lookOff=-4,0,0" > /dev/null
$N cell final/s5_unload.png 1000 760 "task=unload&door=0.62&mask=1&off=12,52,100&lookOff=0,-2,0&fov=26" > /dev/null
$N cell final/s6_close.png 1000 760 "task=close&door=0.04&mask=1&off=-95,28,62&fov=24&lookOff=4,-2,0" > /dev/null
# portability
$N cell final/portA.png 1200 900 "task=door&door=0.12&style=A&mask=1&off=-150,10,215&lookOff=8,-22,0&fov=30" > /dev/null
$N cell final/portB.png 1200 900 "task=door&door=0.12&style=B&mask=1&bx=48&bz=118&q0=200,30,-100,-80,-40,-90&off=-150,10,215&lookOff=14,-22,0&fov=30" > /dev/null
# product / cutaway / closing / kitchen / screwdriver
$N product final/product.png 1200 1733 "cam=0,16,112&look=0,15.5,0" > /dev/null
$N product final/cutaway.png 1200 1733 "cut=1&cam=0,16,112&look=0,15.5,0" > /dev/null
$N closing final/closing.png 1200 1600 "" > /dev/null
$N kitchen final/kitchen.png 1800 1200 "q0=150,-50,-90,-30,90,0&mask=1&lift=3" > /dev/null
$N tool final/screwdriver.png 1200 1000 "kind=screwdriver" > /dev/null
echo done
