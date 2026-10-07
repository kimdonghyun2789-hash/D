# Build the ARKI IR deck:  python3 ARKI/source/build.py [--pdf] [--png]
#   --pdf  also writes the review PDF (LibreOffice, Asian/Latin auto-spacing switched off)
#   --png  also renders PNG previews of every slide into ARKI/source/_png (for visual QA, not committed)
import os, sys, json, datetime, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import kit
from kit import new_prs, set_theme
import common
from common import OUTPUT, PREVIEW
import slides_main
try:
    import slides_appx
    APPX = slides_appx.APPX
except ImportError:
    APPX = []

common.load()
set_theme('light')
prs = new_prs()
for f in slides_main.MAIN + APPX:
    f(prs)
cp = prs.core_properties
cp.title = 'ARKI Robotics — Seed Investment Proposal (Draft v1)'
cp.subject = '주거공간 일체형 Robotics System · Kitchen Clean-up · 구축 Validation / 신축 Scale'
cp.author = 'ARKI Robotics (가칭)'; cp.last_modified_by = ''
cp.created = cp.modified = datetime.datetime(2026, 10, 7, 9, 0, 0)
prs.save(OUTPUT)
print('saved', OUTPUT, 'slides', len(prs.slides), '| fit issues', len(kit.FIT))
for f in kit.FIT: print('  FIT', f)
json.dump({'meta': common.META, 'log': kit.LOG}, open(os.path.join(HERE, '_deck_text.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
if '--pdf' in sys.argv or '--png' in sys.argv:
    import to_pdf
    to_pdf.convert(OUTPUT, PREVIEW)
    print('saved', PREVIEW)
if '--png' in sys.argv:
    out = os.path.join(HERE, '_png'); os.makedirs(out, exist_ok=True)
    import shutil
    shutil.rmtree(out, ignore_errors=True); os.makedirs(out, exist_ok=True)
    subprocess.run(['pdftoppm', '-png', '-r', '55', PREVIEW, os.path.join(out, 's')], check=True)
    print('png ->', out)
