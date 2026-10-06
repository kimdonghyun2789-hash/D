# Build the IR deck:  python3 source/deck/build.py [--pdf]
#   --pdf  also writes the review PDF (LibreOffice, Asian/Latin auto-spacing switched off)
import os, sys, datetime
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from paths import OUTPUT, PREVIEW
import kit
from kit import new_prs, set_theme
import slides_main, slides_appx

slides_main.load_model()
set_theme('light')
prs = new_prs()
for f in slides_main.MAIN + slides_appx.APPX:
    f(prs)
cp = prs.core_properties
cp.title = 'SoftHand-4 Seed 투자 제안서'
cp.subject = '사람용 설비를 그대로 쓰는 로봇 핸드 · 머신텐딩 · Seed 20억 원'
cp.author = '[회사명 입력 필요]'; cp.last_modified_by = ''
cp.created = cp.modified = datetime.datetime(2026, 10, 6, 9, 0, 0)
prs.save(OUTPUT)
print('saved', OUTPUT, 'slides', len(prs.slides), '| fit issues', len(kit.FIT))
for f in kit.FIT: print('  FIT', f)
if '--pdf' in sys.argv:
    import to_pdf
    to_pdf.convert(OUTPUT, PREVIEW)
    print('saved', PREVIEW)
