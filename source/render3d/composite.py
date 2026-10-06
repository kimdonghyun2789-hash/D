# composite color+mask: fade non-mask pixels radially toward edges, put on slide bg for preview
import sys
from PIL import Image, ImageFilter, ImageChops
import numpy as np
def fade(color_path, mask_path, out_path, cx=0.42, cy=0.42, rx=0.55, ry=0.65, power=1.6, preview=None, bg=(11,12,14), keep_floor=0.0):
    c = Image.open(color_path).convert('RGBA'); m = Image.open(mask_path).convert('L')
    m = m.filter(ImageFilter.GaussianBlur(1.2))
    W, H = c.size
    yy, xx = np.mgrid[0:H, 0:W]
    d = np.sqrt(((xx / W - cx) / rx) ** 2 + ((yy / H - cy) / ry) ** 2)
    f = np.clip(1.0 - d, 0, 1) ** power  # 1 at center -> 0 at edge
    f = np.maximum(f, keep_floor)
    mk = np.asarray(m, dtype=np.float32) / 255.0
    a = np.asarray(c, dtype=np.float32)[..., 3] / 255.0
    na = a * np.maximum(f, mk)
    arr = np.asarray(c).copy(); arr[..., 3] = (na * 255).astype(np.uint8)
    out = Image.fromarray(arr, 'RGBA'); out.save(out_path)
    if preview:
        b = Image.new('RGBA', out.size, bg + (255,)); b.alpha_composite(out); b.convert('RGB').save(preview, quality=88)
if __name__ == '__main__':
    args = sys.argv[1:]
    kw = {}
    for a in args[3:]:
        k, v = a.split('='); kw[k] = v if k == 'preview' else float(v)
    fade(args[0], args[1], args[2], **kw)
