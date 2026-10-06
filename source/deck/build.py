import sys, importlib
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deckkit; from deckkit import *
from paths import TEMPLATE, OUTPUT
mods = [m for m in ['slides_main_a', 'slides_main_b', 'slides_main_c', 'slides_appx'] if importlib.util.find_spec(m)]
prs = open_base(TEMPLATE)
order = sys.argv[1].split(',') if len(sys.argv) > 1 and sys.argv[1] != 'all' else None
fns = []
for m in mods:
    mod = importlib.import_module(m)
    for name in sorted(n for n in dir(mod) if (n.startswith('s') and n[1:3].isdigit()) or n.startswith('a')):
        f = getattr(mod, name)
        if callable(f) and (name[0] == 's' and name[1:3].isdigit() or (name[0] == 'a' and name[1:3].isdigit())):
            fns.append((name, f))
for name, f in fns:
    if order and name not in order: continue
    f(prs)
out = sys.argv[2] if len(sys.argv) > 2 else OUTPUT
import datetime
cp = prs.core_properties
cp.title = 'ONE HAND. MANY TOOLS. — 창업 및 Seed 투자 제안서 (최종본)'
cp.subject = '기존 설비를 크게 바꾸지 않는 Machine Tending 자동화 · SoftHand-4 + Skill Pack · Seed ₩2.0B'
cp.author = '[회사명 입력 필요]'; cp.last_modified_by = ''
cp.created = cp.modified = datetime.datetime(2026, 10, 6, 9, 0, 0)
prs.save(out)
print('saved', out, 'slides', len(prs.slides))
for l in deckkit.FIT_LOG: print('FIT', l)
