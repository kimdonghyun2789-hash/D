import sys, os
from PIL import Image
d = sys.argv[1]; per = int(sys.argv[2]) if len(sys.argv) > 2 else 4
fs = sorted(f for f in os.listdir(d) if f.startswith('s-') and f.endswith('.png'))
out = os.path.join(d, 'm'); os.makedirs(out, exist_ok=True)
for i in range(0, len(fs), per):
    ims = [Image.open(os.path.join(d, f)) for f in fs[i:i + per]]
    w, h = ims[0].size; cols = 2; rows = (len(ims) + 1) // 2
    m = Image.new('RGB', (w * cols + 10, h * rows + 10 * (rows - 1)), 'white')
    for j, im in enumerate(ims):
        m.paste(im, ((j % 2) * (w + 10), (j // 2) * (h + 10)))
    m.save(os.path.join(out, f'm{i // per + 1:02d}.png'))
print(len(fs))
