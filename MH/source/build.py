# Build the MH Robotics Seed · TIPS IR deck (최종본):  python3 MH/source/build.py [--pdf] [--png]
#   제출용  MH_Robotics_Seed_TIPS_IR_Final.pptx  = 본문 + 부록   (--pdf: 전체 PDF + 본문만 PDF)
#   내부용  MH_Robotics_IR_Internal_QA.pptx      = 예상질문 · 방어논리 · Evidence · Founder 입력 · 투자심사 Memo · Tag 원칙 (제출 제외)
#   --png  also renders PNG previews of every slide into MH/source/_png (for visual QA, not committed)
import os, sys, json, datetime, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import kit
from kit import new_prs, set_theme
import common
from common import OUTPUT, PREVIEW, MAIN_PDF, INTERNAL, INTERNAL_PDF
common.load()
import slides_mh
import slides_mh_apx


def props(p, title):
    cp = p.core_properties
    cp.title = title
    cp.subject = 'Adaptive Robot Hand · Manipulation Skill · Calibration · Environment Interface · CLEAN → ASSIST → COOK'
    cp.author = 'MH Robotics'; cp.last_modified_by = ''
    cp.created = cp.modified = datetime.datetime(2026, 10, 8, 9, 0, 0)


set_theme('light')
prs = new_prs()
for f in slides_mh.MAIN:
    f(prs)
N_MAIN = len(prs.slides)
slides_mh_apx.build(prs)
props(prs, 'MH Robotics — Kitchen Manipulation Robotics System · Seed · TIPS IR (최종본)')
prs.save(OUTPUT)
print('saved', OUTPUT, 'slides', len(prs.slides), f'(main {N_MAIN})')

N_INT = 0
if hasattr(slides_mh_apx, 'build_internal'):
    prs2 = new_prs()
    slides_mh_apx.build_internal(prs2)
    N_INT = len(prs2.slides)
    props(prs2, 'MH Robotics — IR 내부 검토용 (예상질문 · 방어논리 · Evidence · 투자심사 Memo, 제출 제외)')
    prs2.save(INTERNAL)
    print('saved', INTERNAL, 'slides', N_INT)

print('fit issues', len(kit.FIT))
for f in kit.FIT: print('  FIT', f)
json.dump({'meta': common.META, 'log': kit.LOG, 'n_main': N_MAIN, 'n_internal': N_INT},
          open(os.path.join(HERE, '_deck_text.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

if '--pdf' in sys.argv or '--png' in sys.argv:
    import to_pdf
    to_pdf.convert(OUTPUT, PREVIEW)
    print('saved', PREVIEW)
    from pypdf import PdfReader, PdfWriter      # main-only PDF (slides 1..N_MAIN) for sharing
    rd = PdfReader(PREVIEW); wr = PdfWriter()
    for i in range(N_MAIN): wr.add_page(rd.pages[i])
    with open(MAIN_PDF, 'wb') as fh: wr.write(fh)
    print('saved', MAIN_PDF)
    if N_INT:
        to_pdf.convert(INTERNAL, INTERNAL_PDF)
        print('saved', INTERNAL_PDF)
if '--png' in sys.argv:
    out = os.path.join(HERE, '_png'); os.makedirs(out, exist_ok=True)
    import shutil
    shutil.rmtree(out, ignore_errors=True); os.makedirs(out, exist_ok=True)
    subprocess.run(['pdftoppm', '-png', '-r', '55', PREVIEW, os.path.join(out, 's')], check=True)
    if N_INT:
        subprocess.run(['pdftoppm', '-png', '-r', '55', INTERNAL_PDF, os.path.join(out, 'i')], check=True)
    print('png ->', out)
