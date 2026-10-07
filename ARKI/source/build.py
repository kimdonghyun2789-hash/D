# Build the ARKI IR deck:  python3 ARKI/source/build.py [--pdf] [--png]
#   --pdf  also writes the review PDF (LibreOffice, Asian/Latin auto-spacing switched off)
#   --png  also renders PNG previews of every slide into ARKI/source/_png (for visual QA, not committed)
import os, sys, json, datetime, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import kit
from kit import new_prs, set_theme
import common
from common import OUTPUT, PREVIEW, MAIN_PDF
common.load()
import slides_main
import slides_apx2

set_theme('light')
prs = new_prs()
for f in slides_main.MAIN:
    f(prs)
N_MAIN = len(prs.slides)
slides_apx2.build(prs)
cp = prs.core_properties
cp.title = 'ARKI Robotics — Seed Investment Proposal (Draft v3)'
cp.subject = 'Robot-ready Kitchen + Robot System · Kitchen Clean-up · 구축 Validation / 신축 Scale'
cp.author = 'ARKI Robotics (가칭)'; cp.last_modified_by = ''
cp.created = cp.modified = datetime.datetime(2026, 10, 7, 9, 0, 0)
prs.save(OUTPUT)
print('saved', OUTPUT, 'slides', len(prs.slides), f'(main {N_MAIN})', '| fit issues', len(kit.FIT))
for f in kit.FIT: print('  FIT', f)
json.dump({'meta': common.META, 'log': kit.LOG}, open(os.path.join(HERE, '_deck_text.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
if '--pdf' in sys.argv or '--png' in sys.argv:
    import to_pdf
    to_pdf.convert(OUTPUT, PREVIEW)
    print('saved', PREVIEW)
    from pypdf import PdfReader, PdfWriter      # main-only PDF (slides 1..N_MAIN) for sharing
    rd = PdfReader(PREVIEW); wr = PdfWriter()
    for i in range(N_MAIN): wr.add_page(rd.pages[i])
    with open(MAIN_PDF, 'wb') as fh: wr.write(fh)
    print('saved', MAIN_PDF)
if '--png' in sys.argv:
    out = os.path.join(HERE, '_png'); os.makedirs(out, exist_ok=True)
    import shutil
    shutil.rmtree(out, ignore_errors=True); os.makedirs(out, exist_ok=True)
    subprocess.run(['pdftoppm', '-png', '-r', '55', PREVIEW, os.path.join(out, 's')], check=True)
    print('png ->', out)
