# Base Case financial model + Seed 24M plan (unit: 억원). Single source of truth for deck + report.
import json, copy, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

Y = ['Y1', 'Y2', 'Y3', 'Y4', 'Y5']
A = dict(
    poc_n=[1, 4, 5, 6, 6], poc_price=0.5,                # Paid PoC (8~12주, 대여 Hand 포함)
    int_n=[0, 2, 6, 8, 8], int_price=0.4,                # 고객별 통합 Engineering
    hand_direct=[0, 6, 24, 50, 80], hand_price=0.15,     # Hand 패키지 직판 (₩1,500만)
    hand_partner=[0, 0, 12, 50, 120], partner_price=0.12, # SI 파트너 경유 (20% 할인, 순매출)
    skill_per_hand=[0, 1.0, 1.2, 1.4, 1.6], skill_price=0.03, skill_partner_price=0.024,
    runtime_fee=0.015,                                    # 설치 Hand당 연 ₩150만 (평균 설치기반)
    unit_cost=[0.095, 0.095, 0.090, 0.082, 0.075],        # Hand 원가 (BOM+조립)
    gm_poc=0.40, gm_skill=0.85, gm_runtime=0.70,
    fte=[None, None, 14, 19, 23], fte_cost=[None, None, 0.72, 0.74, 0.76], nonpers=[None, None, 4.5, 5.4, 6.2],
)

# ---------------- Seed 24-month plan (monthly) ----------------
FOUNDER_M = 0.0480   # 창업자 월 인건비(4대보험·퇴직 포함, 연 ₩5,000만 기준)
ENG_M = 0.0671       # 엔지니어 월 인건비(연 ₩7,000만 기준, 15% 가산)
HIRES = [  # (role, start month, monthly cost)
    ('대표 · 사업/제품 (Founder)', 1, FOUNDER_M),
    ('CTO · Hand 메카트로닉스 (Co-founder)', 1, FOUNDER_M),
    ('기구·구동 엔지니어', 2, ENG_M),
    ('제어·임베디드 엔지니어', 3, ENG_M),
    ('Robot SW · Skill 엔지니어', 5, ENG_M),
    ('현장 통합(FAE) 엔지니어', 8, ENG_M),
    ('Vision · 조작 AI 엔지니어', 10, ENG_M),
    ('DFM · 품질 엔지니어', 13, ENG_M),
]
months = list(range(1, 25))
pers = [sum(c for _, s, c in HIRES if m >= s) for m in months]
headcount = [sum(1 for _, s, _ in HIRES if m >= s) for m in months]

def spread(total, m0, m1):
    n = m1 - m0 + 1
    return {m: total / n for m in range(m0, m1 + 1)}
NP = {
    'Prototype · 내구시험': [spread(0.9, 1, 6), spread(0.6, 7, 12), spread(0.8, 13, 18), spread(0.4, 19, 24)],
    'Robot 2종 · 시험 Cell': [{2: 0.45, 3: 0.35, 4: 0.10, 13: 0.40}],
    '고객 PoC · 현장통합(비청구)': [spread(0.3, 7, 12), spread(0.45, 13, 18), spread(0.45, 19, 24)],
    'SW · AI · Data': [spread(0.6, 1, 24)],
    '제조 · 품질 · 안전 · IP': [spread(0.15, 1, 6), spread(0.2, 7, 12), spread(0.45, 13, 18), spread(0.3, 19, 24)],
    'Kitchen Bench Demo': [spread(0.3, 19, 24)],
    '운영 (임차·법무·회계·보험·출장)': [spread(1.5, 1, 24)],
}
np_month = {k: [sum(d.get(m, 0) for d in v) for m in months] for k, v in NP.items()}
CONTINGENCY = 1.7
SEED = 20.0

def seed_plan():
    tot_pers = sum(pers)
    others = tot_pers + sum(sum(v) for v in np_month.values())
    uof = [('핵심 인력 (8명 단계 채용)', tot_pers)] + [(k, sum(v)) for k, v in np_month.items()] + [('예비비 · 운전자본', SEED - others)]
    s = sum(v for _, v in uof)
    opex_m = [pers[i] + sum(np_month[k][i] for k in np_month) for i in range(24)]
    core = sum(opex_m[:18]); ext = sum(opex_m[18:])
    y1 = sum(opex_m[:12]); y2 = sum(opex_m[12:])
    return dict(uof=uof, uof_total=s, opex_m=opex_m, core18=core, ext6=ext, opex_y1=y1, opex_y2=y2,
                pers_total=tot_pers, pers_y1=sum(pers[:12]), pers_y2=sum(pers[12:]), headcount_end=headcount[-1],
                burn_m18=opex_m[17], burn_m24=opex_m[23])

def model(a=None, opex12=None):
    a = a or A
    sp = seed_plan()
    out = {k: [] for k in ['poc_int', 'hw', 'skill', 'runtime', 'partner', 'rev', 'cogs', 'gp', 'gm', 'opex', 'op', 'reuse_share', 'installed_end', 'hands_new']}
    installed = 0
    for i in range(5):
        poc = a['poc_n'][i] * a['poc_price'] + a['int_n'][i] * a['int_price']
        hd, hp = a['hand_direct'][i], a['hand_partner'][i]
        hw = hd * a['hand_price']
        skill = hd * a['skill_per_hand'][i] * a['skill_price']
        start = installed; installed += hd + hp
        rt = (start + (hd + hp) / 2) * a['runtime_fee']
        partner = hp * (a['partner_price'] + a['skill_per_hand'][i] * a['skill_partner_price'])
        rev = poc + hw + skill + rt + partner
        uc = a['unit_cost'][i]
        cogs = poc * (1 - a['gm_poc']) + (hd + hp) * uc + (skill + hp * a['skill_per_hand'][i] * a['skill_partner_price']) * (1 - a['gm_skill']) + rt * (1 - a['gm_runtime'])
        gp = rev - cogs
        if i == 0: opex = sp['opex_y1'] if opex12 is None else opex12[0]
        elif i == 1: opex = sp['opex_y2'] if opex12 is None else opex12[1]
        else: opex = a['fte'][i] * a['fte_cost'][i] + a['nonpers'][i]
        for k, v in [('poc_int', poc), ('hw', hw), ('skill', skill), ('runtime', rt), ('partner', partner), ('rev', rev), ('cogs', cogs), ('gp', gp),
                     ('gm', gp / rev if rev else 0), ('opex', opex), ('op', gp - opex), ('reuse_share', (rev - poc) / rev if rev else 0),
                     ('installed_end', installed), ('hands_new', hd + hp)]:
            out[k].append(v)
    return out

def scaled(f_units=1.0, f_poc=1.0, from_year=2, cost_flat=False, partner_delay=False):
    a = copy.deepcopy(A)
    for i in range(from_year, 5):
        a['hand_direct'][i] = round(a['hand_direct'][i] * f_units)
        a['hand_partner'][i] = round(a['hand_partner'][i] * f_units)
        a['poc_n'][i] = round(a['poc_n'][i] * f_poc); a['int_n'][i] = round(a['int_n'][i] * f_poc)
    if cost_flat: a['unit_cost'] = [0.095, 0.095, 0.090, 0.090, 0.090]
    if partner_delay: a['hand_partner'] = [0, 0, 0, a['hand_partner'][2], a['hand_partner'][3]]
    return model(a)

if __name__ == '__main__':
    sp = seed_plan(); b = model()
    r = lambda x: round(x, 2)
    print('Seed plan: total', r(sp['uof_total']), 'core18', r(sp['core18']), 'ext6', r(sp['ext6']), 'opexY1', r(sp['opex_y1']), 'opexY2', r(sp['opex_y2']), 'pers', r(sp['pers_total']), 'burn M18', r(sp['burn_m18']), 'M24', r(sp['burn_m24']))
    for k, v in sp['uof']: print('  UoF', k, r(v), f"{v/SEED*100:.1f}%")
    for k in ['poc_int', 'hw', 'skill', 'runtime', 'partner', 'rev', 'cogs', 'gp', 'gm', 'opex', 'op', 'reuse_share', 'installed_end', 'hands_new']:
        print(k.ljust(14), [r(x) for x in b[k]])
    cum = 0
    for i in range(5): cum += b['op'][i]; print(Y[i], 'cum OP', r(cum))
    print('cash end M24 (no WC)', r(SEED - sum(sp['opex_m']) + b['gp'][0] + b['gp'][1]))
    print('cash end M24 if zero revenue', r(SEED - sum(sp['opex_m'])))
    for name, m in [('vol-30%', scaled(0.7, 0.7)), ('cost flat', scaled(cost_flat=True)), ('partner delay 1y', scaled(partner_delay=True)), ('vol-50% Y3', scaled(0.5, 0.5, 2))]:
        print(name, 'Y5 rev', r(m['rev'][4]), 'Y5 GP', r(m['gp'][4]), 'Y5 OP', r(m['op'][4]), 'Y3 OP', r(m['op'][2]), 'cumY3-5', r(sum(m['op'][2:])))
    json.dump(dict(seed=sp, base=b, hires=HIRES, assumptions=A,
                   sens={n: scaled(*args) for n, args in [('vol70', (0.7, 0.7)), ('vol50', (0.5, 0.5))]}), open(__import__('paths').MODEL_JSON, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
