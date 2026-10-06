from PIL import Image, ImageFilter
import numpy as np
SLIDE=(11,12,14); CARD=(21,23,27)
def faded(name, cx, cy, rx, ry, power=1.6, floor=0.0, bg=SLIDE, left_dark=None):
    c=Image.open(f'final/{name}_color.png').convert('RGBA'); m=Image.open(f'final/{name}_mask.png').convert('L').filter(ImageFilter.GaussianBlur(1.2))
    W,H=c.size; yy,xx=np.mgrid[0:H,0:W]
    d=np.sqrt(((xx/W-cx)/rx)**2+((yy/H-cy)/ry)**2); f=np.clip(1-d,0,1)**power; f=np.maximum(f,floor)
    mk=np.asarray(m,dtype=np.float32)/255; a=np.asarray(c,dtype=np.float32)[...,3]/255
    na=a*np.maximum(f,mk)
    rgb=np.asarray(c,dtype=np.float32)[...,:3]
    bgc=np.array(bg,dtype=np.float32)
    out=rgb*na[...,None]+bgc*(1-na[...,None])
    if left_dark is not None:
        x0,x1,strength=left_dark
        ramp=np.clip((x1-xx/W)/(x1-x0),0,1)*strength  # 1 at x0 -> 0 at x1
        out=out*(1-ramp[...,None])+bgc*ramp[...,None]
    return Image.fromarray(np.clip(out,0,255).astype(np.uint8),'RGB')
def trim(name, pad=20):
    im=Image.open(f'final/{name}.png').convert('RGBA'); bb=im.getchannel('A').point(lambda v:255 if v>8 else 0).getbbox()
    x0,y0,x1,y1=bb; x0=max(0,x0-pad); y0=max(0,y0-pad); x1=min(im.width,x1+pad); y1=min(im.height,y1+pad)
    return im.crop((x0,y0,x1,y1))
# cover: full bleed, darken left 45% for text
OUT='../../assets/renders/'
import os; os.makedirs(OUT, exist_ok=True)
im=faded('cover',0.58,0.42,0.75,0.95,power=1.3,left_dark=(0.0,0.62,0.88)); im.save(OUT+'cover_fullbleed.jpg',quality=92)
im=faded('overview',0.5,0.5,0.72,0.85); im.save(OUT+'cell_overview.jpg',quality=92)
for n in ['s1_door','s2_pick','s3_load','s4_press','s5_unload','s6_close']:
    faded(n,0.5,0.5,0.75,0.85,power=1.4,bg=CARD).save(OUT+f'{n}.jpg',quality=92)
for n in ['portA','portB']:
    faded(n,0.5,0.5,0.75,0.85,power=1.4,bg=CARD).save(OUT+f'{n}.jpg',quality=92)
faded('kitchen',0.45,0.45,0.75,0.9,power=1.4,bg=CARD).save(OUT+'kitchen_bench.jpg',quality=92)
for n in ['product','cutaway','closing','screwdriver']:
    t=trim(n); t.save(OUT+f'{n}.png'); print(n,t.size)
