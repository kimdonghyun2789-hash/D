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
cp.title = '투자유치 사업계획서 (Seed) · 사람용 도구를 잡고 사용하는 소프트 로봇핸드 개발 및 사업화'
cp.subject = '4지·5지 소프트 로봇핸드와 도구 사용 제어 소프트웨어, 천장 이동형 양팔 로봇 주방 · Seed 20억 원 / 24개월'
cp.author = '[회사명 입력 필요]'; cp.last_modified_by = ''
cp.created = cp.modified = datetime.datetime(2026, 10, 6, 9, 0, 0)
prs.save(OUTPUT)
print('saved', OUTPUT, 'slides', len(prs.slides), '| fit issues', len(kit.FIT))
for f in kit.FIT: print('  FIT', f)
if '--pdf' in sys.argv:
    import to_pdf
    to_pdf.convert(OUTPUT, PREVIEW)
    print('saved', PREVIEW)
