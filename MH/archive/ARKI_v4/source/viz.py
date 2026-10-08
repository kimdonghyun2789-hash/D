# Reusable diagram blocks for the v3 main deck (money flow, financial bars, section with height budget).
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_CONNECTOR, MSO_SHAPE
from pptx.enum.dml import MSO_LINE
import kit
from kit import T, text, rect, arrow, text_w, chip

GREY = '8C9198'

def seg(s, x1, y1, x2, y2, color=None, lw=0.75, dash=False, head=False):
    c = s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x1), Inches(y1), Inches(x2), Inches(y2))
    c.line.color.rgb = RGBColor.from_string(color or T['text2']); c.line.width = Pt(lw)
    kit._nostyle(c)
    if dash: c.line.dash_style = MSO_LINE.DASH
    if head:
        from pptx.oxml.ns import qn
        from lxml import etree
        ln = c.line._get_or_add_ln(); te = etree.SubElement(ln, qn('a:tailEnd')); te.set('type', 'triangle'); te.set('w', 'med'); te.set('len', 'med')
    return c

def actor(s, x, y, w, h, title, sub=None, dark=False, line=None):
    rect(s, x, y, w, h, fill=T['text'] if dark else T['soft'], line=line)
    text(s, x + 0.12, y + (0.1 if sub else 0), w - 0.24, (0.36 if sub else h), title, size=12.5, bold=True,
         color='FFFFFF' if dark else T['text'], align='c', anchor='t' if sub else 'm')
    if sub:
        text(s, x + 0.12, y + 0.44, w - 0.24, h - 0.5, sub, size=9.5, color='C9CDD2' if dark else T['text2'], align='c', line=1.0)

def flow_label(s, x, y, w, txt, size=9.5, color=None, bold=True, align='c'):
    h = kit.text_h(txt, size, w, bold=bold) + 0.02
    text(s, x, y, w, h, txt, size=size, bold=bold, color=color or T['text'], align=align, check=False)
    return h

def money_arrow(s, x1, y1, x2, y2, label, lx, ly, lw=1.9, color=None, weight=1.75, label_color=None, size=9.5, dash=False):
    seg(s, x1, y1, x2, y2, color=color or T['text'], lw=weight, dash=dash, head=True)
    flow_label(s, lx, ly, lw, label, size=size, color=label_color or color or T['text'])

def bars(s, x, y, w, h, vals, labels, fmt, color='15171A', neg_color='C9CDD2', vmax=None, vmin=None, label_size=10, cat_size=10, accent_idx=None):
    """Simple bar chart drawn with rectangles (supports negatives, exact label control)."""
    n = len(vals); vmax = vmax if vmax is not None else max(0, max(vals)); vmin = vmin if vmin is not None else min(0, min(vals))
    span = (vmax - vmin) or 1; bw = w / n * 0.56; zero = y + h * (vmax / span)
    seg(s, x, zero, x + w, zero, color=T['line'], lw=0.75)
    for i, v in enumerate(vals):
        cx = x + w * (i + 0.5) / n; top = zero - h * (max(v, 0) / span); bot = zero + h * (max(-v, 0) / span)
        col = T['accent'] if accent_idx == i else (color if v >= 0 else neg_color)
        if abs(bot - top) > 0.005: rect(s, cx - bw / 2, top, bw, bot - top, fill=col)
        ly = top - 0.27 if v >= 0 else bot + 0.03
        text(s, cx - 0.6, ly, 1.2, 0.24, fmt(v), size=label_size, bold=True, align='c', check=False,
             color=T['accent'] if accent_idx == i else T['text'])
        text(s, cx - 0.6, y + h + 0.06, 1.2, 0.24, labels[i], size=cat_size, color=T['text2'], align='c', check=False)


def module_strip(s, x, y, w, h, parts, accent_idx=(0,), label_size=10, dim_size=9.5, sub=None):
    """Plan-view strip of the standard run: parts = [(label, width_cm, fill_or_None)], widths drawn to scale.
    accent_idx parts get an orange outline (robot zone items). Returns list of (x0, x1) per part."""
    tot = sum(p[1] for p in parts); xs = []; cx = x
    for i, (lab, wcm, fill) in enumerate(parts):
        ww = w * wcm / tot
        rect(s, cx, y, ww, h, fill=fill or T['soft'], line='FFFFFF', lw=1.5)
        text(s, cx + 0.04, y + 0.06, ww - 0.08, h * 0.55, lab, size=label_size, bold=True, align='c', anchor='m', check=False,
             color='FFFFFF' if fill in ('15171A', '3A3F46') else T['text'])
        text(s, cx, y + h + 0.04, ww, 0.24, f"{wcm:g}", size=dim_size, color=T['text2'], align='c', check=False)
        xs.append((cx, cx + ww)); cx += ww
    seg(s, x, y + h + 0.34, x + w, y + h + 0.34, color=GREY, lw=0.6)
    for xx in [x, x + w]: seg(s, xx, y + h + 0.26, xx, y + h + 0.42, color=GREY, lw=0.6)
    if sub: text(s, x, y + h + 0.38, w, 0.26, sub, size=dim_size, color=T['text2'], align='c', check=False)
    return xs


def level_marks(s, pts, x_text, w_text=1.25, size=9.5, color=None, tick_len=0.18, side='l'):
    """Height marks on a section image: pts = [(slide_x, slide_y, label, highlight)]; draws a short tick and a right-aligned label."""
    for (px, py, lab, hi) in pts:
        col = T['accent'] if hi else (color or T['text2'])
        seg(s, px - tick_len, py, px, py, color=col, lw=1.0 if hi else 0.6)
        text(s, x_text, py - 0.13, w_text, 0.26, lab, size=size, bold=hi, color=col, align='r' if side == 'l' else 'l', anchor='m', check=False)
