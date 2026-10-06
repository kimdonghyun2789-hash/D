# 5-year plan, market sizing, customer payback and Seed use of funds from the business plan
# (사업계획서 08~10장, 작성일 2026-10-06). Unit: 억 원. Single source of numbers for the deck and the report.
# Every value is a plan assumption, not a result. Y1 = 투자 집행 시작연도 (Seed 24개월 = Y1~Y2).
import json, copy, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

Y = ['Y1', 'Y2', 'Y3', 'Y4', 'Y5']
A = dict(
    hands=[0, 30, 100, 200, 350],        # 핸드 단품 판매 대수 (주방 셀에 들어가는 핸드는 제외)
    cells=[0, 0, 5, 12, 25],             # 주방 셀 판매 대수
    sw=[0, 10, 40, 120, 250],            # 연간 SW 유효 계약 수 (당해 매출 인식 가능한 연간 계약 환산치)
    pilot=[1.0, 2.0, 2.0, 2.0, 2.0],     # 유료 실증·개발 매출
    hand_price=0.15, hand_cost=0.08,     # 4지 중심 핸드 패키지 평균 1,500만 원 / 직접원가 800만 원
    cell_price=2.0, cell_cost=1.4,       # 주방 셀 1식 2억 원 / 1억4,000만 원 (팔 2·핸드 2·레일/프레임·제어/안전·설치·보증)
    sw_price=0.03, sw_cost=0.009,        # 소프트웨어 연간 계약 300만 원 / 90만 원
    gm_pilot=0.40,                       # 실증·개발 매출 총이익률
    opex=[8.0, 10.0, 14.0, 20.0, 28.0],  # 운영비 (연구개발·영업·관리·감가상각 포함 계획값)
)
SEED = 20.0
UOF = [  # Seed 20억 원 사용 계획 (24개월 현금 집행 한도, 손익계산서 운영비와 일대일로 일치하지 않음)
    ('개발 인력', 10.0, '기구·구동·제어·AI·통합 인력의 단계 채용'),
    ('시제품·시험 설비', 3.5, '핸드 반복 제작, 팔·센서·지그·내구 시험'),
    ('AI 데이터·연산', 1.5, '시연·실험 데이터, 저장·학습·검증 환경'),
    ('주방 통합 실증', 2.0, '레일/프레임, 세척·가열 연동, 설치 시험'),
    ('안전·품질·지식재산', 1.0, '시험·외부 검토·선행조사·출원'),
    ('운영·예비비', 2.0, '사업 운영, 공급 지연·재작업 대비'),
]
TEAM = [  # 초기 핵심 역할 7명 (단계 채용 전제)
    ('사업·제품 책임자', 1), ('핸드 기구/구동', 2), ('제어·임베디드', 1), ('비전·조작 AI', 2), ('시스템 통합', 1),
]
SAM = dict(hand_sites=100, hand_units=5, cell_sites=30, cells_per_site=1)   # 초기 접근시장 가정 (고객 명단 미확인)
ROI = dict(capex=2.0, wage=25000, days=300, hours=[6, 10], extra=1000)   # 주방 셀 고객 투자회수 예시 (원·만 원)


def model(a=None):
    a = a or A
    out = {k: [] for k in ['rev_hand', 'rev_cell', 'rev_sw', 'rev_pilot', 'rev', 'gp_hand', 'gp_cell', 'gp_sw', 'gp_pilot',
                           'gp', 'gm', 'opex', 'op', 'op_margin', 'cum_op']}
    cum = 0.0
    for i in range(5):
        rh, rc, rs, rp = a['hands'][i] * a['hand_price'], a['cells'][i] * a['cell_price'], a['sw'][i] * a['sw_price'], a['pilot'][i]
        gh = a['hands'][i] * (a['hand_price'] - a['hand_cost'])
        gc = a['cells'][i] * (a['cell_price'] - a['cell_cost'])
        gs = a['sw'][i] * (a['sw_price'] - a['sw_cost'])
        gpl = rp * a['gm_pilot']
        rev = rh + rc + rs + rp; gp = gh + gc + gs + gpl; op = gp - a['opex'][i]; cum += op
        for k, v in [('rev_hand', rh), ('rev_cell', rc), ('rev_sw', rs), ('rev_pilot', rp), ('rev', rev), ('gp_hand', gh), ('gp_cell', gc),
                     ('gp_sw', gs), ('gp_pilot', gpl), ('gp', gp), ('gm', gp / rev if rev else 0), ('opex', a['opex'][i]), ('op', op),
                     ('op_margin', op / rev if rev else 0), ('cum_op', cum)]:
            out[k].append(v)
    return out


def scaled(year, f):
    """All volumes, contracts and pilot revenue of one year scaled by f, same margins and opex (사업계획서 민감도 방식)."""
    a = copy.deepcopy(A)
    for k in ['hands', 'cells', 'sw', 'pilot']:
        a[k][year] = a[k][year] * f
    return model(a)


def sam():
    hand = SAM['hand_sites'] * SAM['hand_units'] * A['hand_price']
    cell = SAM['cell_sites'] * SAM['cells_per_site'] * A['cell_price']
    return dict(hand=hand, cell=cell, hand_units=SAM['hand_sites'] * SAM['hand_units'], cell_units=SAM['cell_sites'] * SAM['cells_per_site'])


def roi():
    out = []
    for h in ROI['hours']:
        saving = ROI['wage'] * h * ROI['days'] / 1e4 - ROI['extra']          # 만 원/년
        out.append(dict(hours=h, saving=saving, payback=ROI['capex'] * 1e4 / saving))
    return out


def gm_unit():
    return dict(hand=1 - A['hand_cost'] / A['hand_price'], cell=1 - A['cell_cost'] / A['cell_price'], sw=1 - A['sw_cost'] / A['sw_price'])


if __name__ == '__main__':
    b = model(); r = lambda x: round(x, 2)
    for k in b: print(k.ljust(10), [r(x) for x in b[k]])
    s3 = scaled(2, 0.5); s4 = scaled(3, 0.8)
    print('sens Y3 50%: rev', r(s3['rev'][2]), 'gp', r(s3['gp'][2]), 'op', r(s3['op'][2]))
    print('sens Y4 80%: rev', r(s4['rev'][3]), 'gp', r(s4['gp'][3]), 'op', r(s4['op'][3]))
    print('Y1~Y2 cumulative OP', r(b['cum_op'][1]), '| UoF total', sum(v for _, v, _ in UOF), '| team', sum(n for _, n in TEAM))
    print('SAM', sam(), '| ROI', [(x['hours'], r(x['saving']), r(x['payback'])) for x in roi()], '| GM', {k: r(v) for k, v in gm_unit().items()})
    # the business plan's published figures must be reproduced exactly
    assert [r(x) for x in b['rev']] == [1.0, 6.8, 28.2, 59.6, 112.0]
    assert [r(x) for x in b['gp']] == [0.4, 3.11, 11.64, 24.52, 45.55]
    assert [r(x) for x in b['op']] == [-7.6, -6.89, -2.36, 4.52, 17.55]
    assert (r(s3['rev'][2]), r(s3['op'][2]), r(s4['gp'][3])) == (14.1, -8.18, 19.62)
    assert r(-b['cum_op'][1]) == 14.49 and sum(v for _, v, _ in UOF) == SEED
    json.dump(dict(base=b, assumptions=A, uof=UOF, team=TEAM, seed=SEED, sam=sam(), roi=roi(), gm_unit=gm_unit(),
                   sens=dict(y3_50=dict(rev=s3['rev'][2], gp=s3['gp'][2], op=s3['op'][2]),
                             y4_80=dict(rev=s4['rev'][3], gp=s4['gp'][3], op=s4['op'][3]))),
              open(__import__('paths').MODEL_JSON, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('saved model.json')
