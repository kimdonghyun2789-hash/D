# Copy renders from final/ (written by batch.sh) into the deck assets.
#   raw/  : scene renders used as rectangular photos (the deck crops them per slide)
#   *.png : transparent cut-outs trimmed to their content (hand, screwdriver demo)
import os, shutil
from PIL import Image

OUT = '../../assets/renders/'
RAW = OUT + 'raw/'
os.makedirs(RAW, exist_ok=True)

for n in ['cover', 'overview', 'kitchen', 'portA', 'portB',
          's1_door', 's2_pick', 's3_load', 's4_press', 's5_unload', 's6_close']:
    shutil.copy(f'final/{n}_color.png', RAW + f'{n}_color.png')

def trim(name, pad=20):
    im = Image.open(f'final/{name}.png').convert('RGBA')
    x0, y0, x1, y1 = im.getchannel('A').point(lambda v: 255 if v > 8 else 0).getbbox()
    return im.crop((max(0, x0 - pad), max(0, y0 - pad), min(im.width, x1 + pad), min(im.height, y1 + pad)))

for n in ['product', 'closing', 'screwdriver']:
    t = trim(n); t.save(OUT + f'{n}.png'); print(n, t.size)
