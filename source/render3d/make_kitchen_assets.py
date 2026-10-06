# Convert kitchen renders from final/ (written by batch_kitchen.sh) into deck assets: ../../assets/renders/kitchen/*.jpg
import glob, os
from PIL import Image

OUT = '../../assets/renders/kitchen/'
os.makedirs(OUT, exist_ok=True)
for f in sorted(glob.glob('final/lx_*_color.png') + glob.glob('final/pro_*_color.png') + glob.glob('final/ck_*_color.png')):
    name = os.path.basename(f).replace('_color.png', '')
    im = Image.open(f).convert('RGBA')
    bg = (42, 43, 46) if name.startswith('pro') else (17, 18, 20)   # fill any transparent pixels with the scene tone
    base = Image.new('RGBA', im.size, bg + (255,)); base.alpha_composite(im)
    base.convert('RGB').save(OUT + name + '.jpg', quality=90)
    print(name, im.size)
