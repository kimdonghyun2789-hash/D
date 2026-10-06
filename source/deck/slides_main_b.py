from deckkit import *
import json
from paths import RENDERS as A, ORIGINAL as O, MODEL_JSON
M = json.load(open(MODEL_JSON, encoding='utf-8'))
B = M['base']; SEEDP = M['seed']

def fmt(v, d=1):
    return f'{v:,.{d}f}'

# ================================================================ 05 MACHINE TENDING
def s05(prs):
    s = new_slide(prs, '05')
    header(s, '05', '첫 번째 시장', '첫 번째 Product는 Machine Tending이다', 'Brownfield Machine Tending.', tag='CONCEPT RENDERING')
    picture(s, A + 'cell_overview.jpg', 0.6, 1.92, w=6.35, name='Machine tending cell rendering')
    pill(s, 0.78, 5.62, None, 0.28, 'SoftHand-4  +  Machine Tending Skill Pack', color=TEXT, line=OR, fill=OR_FILL, size=9)
    text(s, 0.6, 6.12, 6.4, 0.32, '기존 설비를 크게 개조하지 않는 다품종 머신텐딩 자동화', size=14, f='K')
    text(s, 0.6, 6.48, 6.4, 0.5, [[('첫 구매자 [가설]  ', {'f': 'S', 'color': OR_LIGHT}), ('다품종 가공 라인을 운영하는 중견 · 중소 제조기업 생산기술팀 · 도입 경로 Robot SI', {})]], size=9.5, color=TEXT2, ls=1.15)
    x0 = 7.25; w0 = 5.48
    label(s, x0, 1.95, w0, '왜 Machine Tending부터 시작하는가', color=OR, size=9.5)
    reasons = [('사람용 Interface가 한 Cell에 모여 있다', '문 · 손잡이 · 바이스 레버 · 버튼 · 트레이 — Hand 하나의 가치가 가장 크게 드러나는 공정'),
               ('전환비용을 숫자로 측정할 수 있다', 'SKU 변경 · 엔지니어링 시간 · 사람 개입을 PoC에서 고객 Baseline과 비교'),
               ('SI가 이미 판매하는 Application이다', '새 시장을 만드는 대신 기존 Cell의 유연성을 높인다 — SI 채널로 바로 진입')]
    yy = 2.28
    for i, (t, d) in enumerate(reasons):
        num_badge(s, x0, yy + 0.02, i + 1, d=0.3, size=10)
        text(s, x0 + 0.45, yy, w0 - 0.45, 0.3, t, size=12.5, f='K')
        text(s, x0 + 0.45, yy + 0.32, w0 - 0.45, 0.42, d, size=9.5, color=TEXT2, ls=1.12)
        yy += 0.86
    yb = 4.95; hb = 1.9
    card(s, x0, yb, w0, hb, fill=OR_FILL, line=OR, lw=1.25)
    text(s, x0 + 0.22, yb + 0.14, w0 - 0.4, 0.3, [[('원칙  ', {'f': 'S', 'color': OR, 'size': 9.5, 'spc': 100}), ('Hand가 경제적 가치를 만드는 작업부터 자동화한다', {'f': 'K'})]], size=12)
    cw = (w0 - 0.6) / 2
    text(s, x0 + 0.22, yb + 0.55, cw, 0.22, '✓  우선 공략', size=9.5, f='S', color=OR_LIGHT)
    text(s, x0 + 0.22, yb + 0.8, cw, 0.92, ['다품종 부품 Handling', '문 · 손잡이 개폐', '레버 · 노브 · 래치', '설비 조작부 조작'], size=9.5, color=TEXT, ls=1.12)
    text(s, x0 + 0.38 + cw, yb + 0.55, cw, 0.22, '×  공략하지 않음 (전용 툴이 유리)', size=9.5, f='S', color=MUTED)
    text(s, x0 + 0.38 + cw, yb + 0.8, cw, 0.92, ['고속 단일 SKU 반복 집기', '고토크 · 정밀 체결 (Screwdriver)', '진공이 유리한 평판 Handling', '→ Screwdriver는 기술 Demo (A9)'], size=9.5, color=TEXT2, ls=1.12)
    footer(s, '05')
    notes(s, "첫 번째 상용 Wedge는 기존 생산설비를 크게 개조하지 않는 다품종 머신텐딩입니다. 제품은 SoftHand-4와 Machine Tending Skill Pack, 즉 Hand, 컨트롤러, 로봇 어댑터와 문 열기, 부품 투입·배출, 레버·버튼 조작 Skill의 묶음입니다. "
             "머신텐딩을 고른 이유는 세 가지입니다. 첫째, 문과 손잡이, 바이스 레버, 버튼, 트레이처럼 사람용 Interface가 한 Cell에 모여 있어 하나의 Hand가 주는 가치가 가장 크게 드러납니다. 둘째, SKU 변경과 엔지니어링 시간, 사람 개입을 고객의 현재 Baseline과 숫자로 비교할 수 있습니다. 셋째, 이미 SI가 판매하는 Application이라 새로운 시장을 만들 필요 없이 SI 채널로 진입할 수 있습니다. "
             "그리고 원칙이 있습니다. 모든 공구를 Hand로 대체한다고 주장하지 않습니다. 고속 단일 SKU 반복 작업이나 고토크 체결은 전용 툴이 더 싸고 좋습니다. 그래서 Screwdriver는 기술 Demo로 옮겼습니다. Hand를 썼을 때 설비 개조와 End-effector 수가 줄어드는 작업부터 공략합니다. "
             "첫 구매자는 다품종 가공 라인을 운영하는 중견·중소 제조기업의 생산기술팀이고, 도입은 Robot SI를 통해 이뤄진다는 것이 저희 가설이며 창업 후 90일 안에 인터뷰로 검증합니다.")

# ================================================================ 06 ONE HAND ONE PROCESS
def s06(prs):
    s = new_slide(prs, '06')
    header(s, '06', 'Product Vision', '하나의 Hand로 하나의 공정을 끝낸다', 'One Hand. One Process.', tag='CONCEPT RENDERING')
    steps = [('s1_door', '설비 문 열기', '문 · 손잡이'), ('s2_pick', '소재 집기', '부품 Pick'), ('s3_load', '설비에 투입', 'Loading'),
             ('s4_press', '버튼 · 레버 조작', '기존 Interface'), ('s5_unload', '완성품 꺼내기', 'Unload'), ('s6_close', '문 닫기', '같은 Skill 재사용')]
    gap = 0.2; cw = (12.13 - 5 * gap) / 6; y0 = 1.95
    ih = (cw - 0.12) / 1.3158
    for i, (img, ko, en) in enumerate(steps):
        x = 0.6 + i * (cw + gap)
        card(s, x, y0, cw, ih + 0.84)
        picture(s, A + img + '.jpg', x + 0.06, y0 + 0.06, w=cw - 0.12, h=ih, name=f'Step {i+1} rendering')
        num_badge(s, x + 0.1, y0 + ih + 0.16, i + 1, d=0.27, size=9)
        text(s, x + 0.43, y0 + ih + 0.14, cw - 0.48, 0.3, ko, size=10.5, f='K')
        text(s, x + 0.43, y0 + ih + 0.44, cw - 0.48, 0.24, en, size=8.5, color=OR_LIGHT if i == 5 else MUTED)
        if i < 5: tri(s, x + cw + 0.05, y0 + (ih + 0.84) / 2 - 0.05, s=0.1, color=MUTED)
    yb = y0 + ih + 1.05
    big = [('1', 'HAND', 'SoftHand-4 하나로', TEXT), ('5', 'TASKS', '문 · 집기 · 투입 · 조작 · 배출', TEXT), ('0', 'HAND CHANGES', ['Tool Changer · 추가 End-effector 없이', 'Seed 기간 검증 목표'], OR)]
    bw = 12.13 / 3
    for i, (n, w, cap, c) in enumerate(big):
        x = 0.6 + i * bw
        if i > 0: line(s, x, yb + 0.12, x, yb + 1.2, color=LINE2, w=0.75)
        text(s, x + 0.15, yb - 0.08, 1.05, 1.35, n, size=66, f='K', color=c, ls=1.0, align='r')
        text(s, x + 1.32, yb + 0.2, bw - 1.42, 0.42, w, size=21, f='K', color=c, ls=1.0)
        text(s, x + 1.32, yb + 0.68, bw - 1.42, 0.45, cap, size=9.5, color=TEXT2, ls=1.12)
    y2 = 5.75
    card(s, 0.6, y2, 12.13, 0.82)
    text(s, 0.85, y2 + 0.1, 1.4, 0.24, '기존 방식', size=9, f='S', color=MUTED, spc=80)
    text(s, 0.85, y2 + 0.36, 5.0, 0.36, 'Gripper 2종 + Tool Changer + 자동문 · I/O 개조', size=12, f='S', color=TEXT2)
    tri(s, 6.05, y2 + 0.38, s=0.12, color=OR)
    text(s, 6.4, y2 + 0.1, 1.4, 0.24, 'SoftHand-4', size=9, f='S', color=OR, spc=80)
    text(s, 6.4, y2 + 0.36, 6.1, 0.36, [[('1 Hand + Machine Tending Skill Pack', {'f': 'K', 'color': TEXT}), ('   6단계 = 5종 Task (열기 · 닫기는 같은 Skill)', {'size': 9.5, 'color': TEXT2})]], size=12)
    text(s, 0.6, 6.68, 12.13, 0.22, '개념 Workflow · 창업 후 6개월 내 대표 공정으로 반복시험, 단계별 완료율과 사람 개입 시간을 분리 보고', size=8.5, color=MUTED2, check=True)
    footer(s, '06')
    notes(s, "이 장이 저희 제품 비전을 가장 잘 보여줍니다. 하나의 로봇 팔에 SoftHand-4 하나를 달고, Hand를 바꾸지 않고 한 공정을 끝냅니다. "
             "설비 문을 열고, 소재를 집고, 설비 안에 넣고, 레버나 버튼 같은 기존 Interface를 조작하고, 완성품을 꺼내고, 문을 닫습니다. 여섯 단계지만 문 열기와 닫기는 같은 Skill이므로 다섯 종류의 Task입니다. "
             "기존 방식이라면 그리퍼 두 종과 툴 체인저, 자동문이나 I/O 개조가 필요한 공정입니다. 저희 목표는 1 Hand, 5 Tasks, 0 Hand Changes입니다. "
             "화면은 Concept Workflow이고, 창업 후 6개월 안에 이 대표 Sequence로 반복시험을 하고 단계별 완료율과 사람 개입 시간을 분리해서 보고하겠습니다.")

# ================================================================ 07 CUSTOMER ECONOMICS
def s07(prs):
    s = new_slide(prs, '07')
    header(s, '07', '고객 가치', '고객은 Hand가 아니라 Automation Flexibility에 돈을 낸다', 'We Sell Automation Flexibility.')
    vals = [('기존 설비 개조 최소화', '설비 개조 · Fixture · 추가 구동기를 줄일 가능성'),
            ('반복 엔지니어링 감소', '전용 Finger · Jig · 티칭 · 통합 작업을 줄일 가능성'),
            ('다음 작업에서 재사용', '같은 Hand와 Skill 구조를 새 SKU · 다른 설비에 재사용')]
    gap = 0.17; vw = (12.13 - 2 * gap) / 3; y0 = 1.95
    for i, (t, d) in enumerate(vals):
        x = 0.6 + i * (vw + gap)
        card(s, x, y0, vw, 1.12)
        num_badge(s, x + 0.22, y0 + 0.2, i + 1, d=0.3, size=10)
        text(s, x + 0.65, y0 + 0.19, vw - 0.8, 0.32, t, size=13.5, f='K')
        text(s, x + 0.65, y0 + 0.56, vw - 0.8, 0.45, d, size=9.5, color=TEXT2, ls=1.12)
    # flows
    def flow(y, lab, sub, items, labcol, hl=()):
        text(s, 0.6, y + 0.02, 1.35, 0.3, lab, size=13, f='K', color=labcol)
        text(s, 0.6, y + 0.32, 1.35, 0.22, sub, size=8.5, color=TEXT2)
        x = 2.05; total = 12.73 - x; n = len(items)
        wts = [it[1] for it in items]; unit = (total - (n - 1) * 0.2) / sum(wts)
        for i, (t, wt) in enumerate(items):
            w = wt * unit
            on = i in hl
            b = box(s, x, y, w, 0.56, fill=OR_FILL if on else CARD, line=OR if on else None, lw=1.0, r=0.06)
            box_text(b, t, size=9.5, f='S', color=TEXT if on else TEXT2)
            if i < n - 1: tri(s, x + w + 0.05, y + 0.23, s=0.1, color=OR if on else MUTED)
            x += w + 0.2
    y1 = 3.32
    flow(y1, '기존 방식', 'TODAY', [('새 작업', 1), ('새 Gripper', 1), ('새 Finger', 1), ('새 Jig', 1), ('엔지니어링', 1.05), ('티칭', 1), ('검증', 1)], TEXT2)
    flow(y1 + 0.82, '우리 방식', 'WITH US', [('새 작업', 1), ('같은 Hand', 1), ('기존 Skill 재사용  또는  새 Skill 구성', 2.6), ('Calibration', 1.1), ('검증', 1.05)], OR, hl=(1, 2))
    text(s, 2.05, y1 + 1.46, 10.6, 0.24, '엔지니어링과 검증은 사라지지 않는다 — 얼마나 줄어드는지를 고객 현장에서 측정한다', size=9.5, f='M', color=MUTED)
    # KPI tiles
    y2 = 5.05; kw = (8.6 - 4 * 0.15) / 5
    label(s, 0.6, y2, 8.6, 'PoC에서 고객 Baseline 대비 측정할 KPI', color=OR, size=9.5)
    kp = [('엔지니어링 시간', 'Engineering Hours'), ('전용 툴링 비용', 'Custom Tooling Cost'), ('통합 리드타임', 'Integration Lead Time'), ('사람 개입', 'Human Intervention'), ('전환 시간', 'Changeover Time')]
    for i, (en, ko) in enumerate(kp):
        x = 0.6 + i * (kw + 0.15)
        card(s, x, y2 + 0.3, kw, 1.5)
        text(s, x + 0.15, y2 + 0.42, kw - 0.25, 0.3, en, size=11, f='K', ls=1.0)
        text(s, x + 0.15, y2 + 0.74, kw - 0.25, 0.24, ko, size=8, color=MUTED)
        text(s, x + 0.15, y2 + 1.04, kw - 0.25, 0.6, [[('↓ ', {'color': TEXT2, 'size': 20}), ('?', {})]], size=24, f='K', color=OR, ls=1.0)
    xr = 9.35; wr = 12.73 - xr
    card(s, xr, y2 + 0.3, wr, 1.5, fill=OR_FILL, line=OR, lw=1.25)
    text(s, xr + 0.2, y2 + 0.4, wr - 0.35, 0.26, 'Seed 투자의 사업 실험', size=11.5, f='K', color=OR)
    text(s, xr + 0.2, y2 + 0.7, wr - 0.35, 1.05, ['Hand 가격(가정 ₩1,500만)의 비교 대상은', [('전용 툴링 + 설비 개조 + 엔지니어링', {'f': 'S', 'color': TEXT}), (' × 연간 전환 횟수', {})], '→ 유료 PoC에서 지불의사로 검증'], size=9.5, color=TEXT2, ls=1.15)
    footer(s, '07')
    notes(s, "고객에게 1,500만원짜리 로봇 손을 파는 회사가 되려는 것이 아닙니다. 고객이 사는 것은 Automation Flexibility이고, SoftHand-4는 그것을 가능하게 하는 하드웨어 Interface입니다. "
             "고객 가치는 세 가지로 단순화했습니다. 기존 설비 개조를 줄일 가능성, 반복 엔지니어링을 줄일 가능성, 그리고 같은 Hand와 Skill 구조를 다음 작업에서 재사용하는 것입니다. "
             "다만 엔지니어링과 검증이 사라진다고 말하지 않겠습니다. 새 작업에는 기존 Skill 재사용 또는 새 Skill 구성, 캘리브레이션, 검증이 여전히 필요합니다. 얼마나 줄어드는지는 아직 모릅니다. "
             "그래서 숫자를 물음표로 두었습니다. 엔지니어링 시간, 전용 툴링 비용, 통합 리드타임, 사람 개입, 전환 시간을 고객의 현재 Baseline 대비 PoC에서 측정하는 것이 Seed 투자의 Business Experiment입니다. "
             "Hand 가격 가정 1,500만원의 비교 대상은 다른 Hand가 아니라, 전용 툴링과 설비 개조, 엔지니어링 비용에 연간 전환 횟수를 곱한 금액입니다. 고객이 실제로 지불하는지는 Paid PoC로 확인하겠습니다.")

# ================================================================ 08 COMPETITION
def s08(prs):
    s = new_slide(prs, '08')
    header(s, '08', '경쟁 구도', '경쟁은 손가락 수가 아니라, 설비변경 없이 끝낸 작업 수다', 'Task Completion, Not Finger Count.')
    cats = [('전통 Gripper', '정확성과 신뢰성이 높지만 특정 작업 중심', '정밀 · 저가 · 고속', '작업이 바뀌면 Finger · Jig 교체, 문 · 레버는 설비 개조', 3, 3, False),
            ('Adaptive Gripper', '다양한 형상 Handling에 강점', '여러 형상을 하나로 집기', '손잡이를 감싸 당기기 · 레버 토크는 제한적 → 결국 설비 개조', 2, 2, False),
            ('Dexterous Hand', '높은 자유도와 복잡한 조작 가능성', '사람 손에 가까운 조작', '비용 · 내구성 · 통합 난이도 → 연구 · 휴머노이드 중심', 1, 1, False),
            ('Our Target', '기존 사람용 Interface를 활용해 실제 Task 완료', '부품 · 문 · 레버를 Hand 교체 없이', '산업 내구성 · 재사용 Skill — Seed 기간 검증 대상', 1, 3, True)]
    gap = 0.2; cw = (12.13 - 3 * gap) / 4; y0 = 1.95; ch = 3.35
    for i, (name, one, plus, minus, mod, field, ours) in enumerate(cats):
        x = 0.6 + i * (cw + gap)
        card(s, x, y0, cw, ch, fill=OR_FILL if ours else CARD, line=OR if ours else None, lw=1.25)
        text(s, x + 0.22, y0 + 0.2, cw - 0.4, 0.36, name, size=16, f='K', color=OR if ours else TEXT)
        text(s, x + 0.22, y0 + 0.62, cw - 0.4, 0.5, one, size=10, f='M', color=TEXT, ls=1.12)
        text(s, x + 0.22, y0 + 1.2, cw - 0.4, 0.22, '강점' if not ours else '목표', size=8.5, f='S', color=OR_LIGHT if ours else MUTED)
        text(s, x + 0.22, y0 + 1.42, cw - 0.4, 0.3, plus, size=10, color=TEXT if ours else TEXT2)
        text(s, x + 0.22, y0 + 1.76, cw - 0.4, 0.22, '한계' if not ours else '조건', size=8.5, f='S', color=OR_LIGHT if ours else MUTED)
        text(s, x + 0.22, y0 + 1.98, cw - 0.4, 0.5, minus, size=9.5, color=TEXT2, ls=1.12)
        line(s, x + 0.22, y0 + 2.6, x + cw - 0.22, y0 + 2.6, color='5A3A26' if ours else LINE, w=0.75)
        for j, (lab, val) in enumerate([('설비변경 필요', mod), ('현장 적용성', field)]):
            yy = y0 + 2.72 + j * 0.27
            text(s, x + 0.22, yy, 1.3, 0.22, lab, size=8.5, color=TEXT2)
            for k in range(3):
                on = k < val
                box(s, x + 1.55 + k * 0.2, yy + 0.06, 0.12, 0.12, fill=(OR if ours else TEXT2) if on else CARD3, shape='oval', name='meter')
        if ours: pill(s, None, y0 + 0.24, None, 0.24, 'TARGET', right=x + cw - 0.2, size=7.5, spc=40, color=OR, line=OR)
    y1 = 5.5
    card(s, 0.6, y1, 12.13, 1.33)
    label(s, 0.85, y1 + 0.14, 5, 'Seed 기간에 증명할 것', color=OR, size=9.5)
    proofs = [('동일 조건 비교시험', '같은 작업 · 같은 Robot에서 전용 Gripper 대비'), ('승인 Task 완료율', '≥ 95% (목표) · 최초 시도 / 재시도 분리'), ('산업 내구성', '30만 회 반복 (목표)'), ('총비용 우위', "'Hand + Skill' < '전용 Gripper N개 + 엔지니어링'")]
    pw = (11.6 - 3 * 0.2) / 4
    for i, (t, d) in enumerate(proofs):
        x = 0.85 + i * (pw + 0.2)
        num_badge(s, x, y1 + 0.47, i + 1, d=0.26, size=9)
        text(s, x + 0.36, y1 + 0.44, pw - 0.36, 0.28, t, size=11, f='K')
        text(s, x + 0.36, y1 + 0.74, pw - 0.36, 0.45, d, size=9, color=TEXT2, ls=1.1)
    text(s, 5.2, y1 + 0.15, 7.3, 0.2, 'Category 비교는 공개 정보 기반 정성 비교 · 회사명 · 상세 Spec · OEM 내재화 분석은 Appendix A4', size=8, color=MUTED2, align='r')
    footer(s, '08')
    notes(s, "경쟁을 손가락 수나 자유도로 비교하지 않겠습니다. 기준은 실제 작업을 얼마나 적은 설비변경으로 완료하느냐입니다. "
             "전통 그리퍼는 정확하고 싸고 신뢰성이 높지만 특정 작업 중심이라, 작업이 바뀌면 핑거와 지그를 바꾸고 문이나 레버는 설비를 개조해야 합니다. "
             "Adaptive Gripper는 다양한 형상을 잘 잡습니다. 그러나 문 손잡이를 감싸 당기거나 레버를 돌리는 것처럼 사람용 Interface를 조작하고 토크를 쓰는 일은 제한적이라, 결국 그 부분은 설비 개조나 추가 End-effector로 해결합니다. 이것이 Adaptive Gripper로 충분하지 않은 이유입니다. "
             "Dexterous Hand는 자유도가 높지만 비용과 내구성, 통합 난이도 때문에 주로 연구와 휴머노이드에 쓰입니다. 저희 목표는 기존 Human Interface를 활용해 실제 Task를 끝내는 영역입니다. 아직 증명하지 않았기 때문에 Seed 기간에 동일 조건 비교시험, 완료율, 내구성, 총비용으로 증명하겠습니다.")

# ================================================================ 09 PRODUCTIZATION LOOP
def s09(prs):
    s = new_slide(prs, '09')
    header(s, '09', '제품화 구조', '고객 프로젝트를 반복 가능한 Skill로 만든다', 'Every Project Leaves a Product Behind.')
    # design partners
    x0 = 0.6; w0 = 3.2; y0 = 1.95
    text(s, x0, y0, w0 - 1.0, 0.24, 'Design Partner 3곳', size=11, f='K')
    pill(s, None, y0 - 0.01, None, 0.24, 'TARGET · 미확보', right=x0 + w0, size=7.5, spc=40, color=YEL, line=YEL, fill=YEL_FILL, dash=True)
    dps = [('A', 'Machine Tending', '기존 CNC Cell · 문 · 바이스 · 버튼'), ('B', 'High-mix Handling', '다품종 부품 · 트레이 · 용기'), ('C', 'Inspection / Loading', '검사기 투입 · 레버 · 래치')]
    yy = y0 + 0.36
    for k, t, d in dps:
        card(s, x0, yy, w0, 0.86)
        box_text(box(s, x0 + 0.16, yy + 0.2, 0.42, 0.42, fill=CARD3, r=0.06), k, size=13, f='K', color=OR)
        text(s, x0 + 0.72, yy + 0.14, w0 - 0.85, 0.3, t, size=11.5, f='K')
        text(s, x0 + 0.72, yy + 0.46, w0 - 0.85, 0.3, d, size=8.5, color=TEXT2)
        yy += 0.98
    text(s, x0, yy + 0.02, w0, 0.42, ['대상: Robot SI · 제조기업 · Automation Integrator', '서로 다른 문제에서 공통 Task를 추출'], size=8.5, color=MUTED, ls=1.15)
    # loop
    import math
    cx, cy, R = 6.45, 4.02, 1.62
    nodes = [('고객 프로젝트', 'CUSTOMER PROJECT'), ('공통 Task 추출', 'COMMON TASK'), ('재사용 Skill', 'REUSABLE SKILL'), ('검증된 Skill Pack', 'VALIDATED PACK'), ('다음 고객', 'NEXT CUSTOMER')]
    pts = []
    for i in range(5):
        a = -math.pi / 2 + i * 2 * math.pi / 5
        pts.append((cx + R * 1.18 * math.cos(a), cy + R * math.sin(a)))
    nw, nh = 1.72, 0.62
    for i in range(5):
        (x1, y1), (x2, y2) = pts[i], pts[(i + 1) % 5]
        dx, dy = x2 - x1, y2 - y1; L = math.hypot(dx, dy); ux, uy = dx / L, dy / L
        def clip(u, v):  # distance from center to rectangle edge along (u,v), plus margin
            tx = (nw / 2) / abs(u) if abs(u) > 1e-6 else 1e9; ty = (nh / 2) / abs(v) if abs(v) > 1e-6 else 1e9
            return min(tx, ty) + 0.06
        d0 = clip(ux, uy)
        line(s, x1 + ux * d0, y1 + uy * d0, x2 - ux * d0, y2 - uy * d0, color=OR, w=1.25, arrow=True)
    for i, (ko, en) in enumerate(nodes):
        x, y = pts[i]
        on = i == 3
        b = box(s, x - nw / 2, y - nh / 2, nw, nh, fill=OR_FILL if on else CARD2, line=OR if on else LINE2, lw=1.0, r=0.1)
        box_text(b, [[(ko, {'f': 'K', 'size': 10.5, 'color': TEXT})], [(en, {'f': 'S', 'size': 7, 'color': OR_LIGHT if on else MUTED, 'spc': 40})]], ls=1.05)
    text(s, cx - 1.1, cy - 0.33, 2.2, 0.3, 'Product Library', size=13, f='K', color=OR, align='c')
    text(s, cx - 1.1, cy + 0.0, 2.2, 0.42, ['Custom Code가 아니라', '재사용 자산이 쌓인다'], size=8.5, color=TEXT2, align='c', ls=1.1)
    # what is reused from customer #2
    rx = 4.2; ry = 5.72
    text(s, rx, ry, 4.95, 0.24, [[('2번째 고객부터 재사용  ', {'f': 'S', 'color': OR}), ('Hand · Runtime · Primitive · Task Skill · Calibration', {'color': TEXT})]], size=8.5)
    text(s, rx, ry + 0.26, 4.95, 0.24, [[('고객마다 새로 구성  ', {'f': 'S', 'color': MUTED}), ('부품 형상 등록 · Cell Layout · 안전 Validation', {'color': TEXT2})]], size=8.5)
    # reusability KPI
    xr = 9.45; wr = 12.73 - xr
    card(s, xr, y0, wr, 2.05, fill=OR_FILL, line=OR, lw=1.25)
    label(s, xr + 0.2, y0 + 0.14, wr - 0.3, '핵심 사업 KPI', color=OR, size=8.5)
    text(s, xr + 0.2, y0 + 0.38, wr - 0.3, 0.36, [[('재사용률', {'f': 'K', 'size': 16}), ('  Reusability Ratio', {'f': 'S', 'size': 9.5, 'color': OR_LIGHT})]], size=16)
    text(s, xr + 0.2, y0 + 0.8, wr - 0.35, 0.62, '신규 고객에 적용할 때 그대로 재사용한 하드웨어 · 제어 로직 · ToolSkill · 소프트웨어 모듈의 비중', size=9, color=TEXT, ls=1.15)
    text(s, xr + 0.2, y0 + 1.48, wr - 0.35, 0.45, [[('M12 ', {'f': 'K', 'color': OR}), ('측정 시작  →  ', {}), ('M24 ', {'f': 'K', 'color': OR}), ('상승 추세 확인', {})], '임의의 목표치를 쓰지 않는다'], size=9.5, color=TEXT2, ls=1.12)
    # revenue mix bars
    y2 = y0 + 2.2; card(s, xr, y2, wr, 2.2)
    text(s, xr + 0.2, y2 + 0.12, wr - 0.3, 0.24, '매출 구성 변화  ·  Base Case 가정', size=9, f='S', color=TEXT)
    bx = xr + 0.35; bw = 0.38; gap = (wr - 0.7 - 5 * bw) / 4; top = y2 + 0.48; hmax = 1.25
    for i in range(5):
        tot = B['rev'][i]; cust = B['poc_int'][i] / tot; reuse = 1 - cust
        x = bx + i * (bw + gap)
        hc = hmax * cust; hr = hmax * reuse
        if hr > 0.005: box(s, x, top, bw, hr, fill=OR, shape='rect', name='mix reusable')
        box(s, x, top + hr, bw, hc, fill='4A4F57', shape='rect', name='mix custom')
        text(s, x - 0.15, top + hmax + 0.04, bw + 0.3, 0.2, f'Y{i+1}', size=8, color=TEXT2, align='c')
        if i > 0: text(s, x - 0.2, top + max(0, hr / 2 - 0.1), bw + 0.4, 0.2, f'{reuse*100:.0f}%', size=7.5, f='S', color='FFFFFF' if hr > 0.25 else TEXT, align='c')
    text(s, xr + 0.2, y2 + 1.94, wr - 0.3, 0.22, [[('■ ', {'color': OR}), ('재사용 제품 · Skill   ', {}), ('■ ', {'color': '4A4F57'}), ('고객별 엔지니어링', {})]], size=7.5, color=TEXT2)
    # bottom
    yb = 6.35
    text(s, 0.6, yb, 12.13, 0.32, [[('고객이 늘어날수록 Custom Code가 아니라 ', {}), ('재사용 가능한 Product Library', {'color': OR}), ('가 쌓인다', {})]], size=14, f='K')
    text(s, 0.6, yb + 0.36, 12.13, 0.24, 'SI가 되지 않는 규칙: 승인 Task 목록 안에서만 수주 · 비표준 요청은 별도 견적 · 프로젝트 종료 시 공통 모듈을 Library에 반영 · 재사용 매출 비중을 경영 KPI로 관리', size=9, color=TEXT2)
    footer(s, '09')
    notes(s, "투자자께서 반드시 물으실 질문이 있습니다. 고객마다 다른 작업을 개발하다가 결국 SI 회사가 되는 것 아니냐는 질문입니다. 이 장이 그 답입니다. "
             "저희는 제품을 다 만든 뒤 고객을 찾지 않습니다. 창업 초기부터 머신텐딩, 다품종 핸들링, 검사·투입이라는 서로 다른 문제를 가진 Design Partner 세 곳과 함께 만듭니다. 아직 확보한 곳은 없으며 목표입니다. "
             "각 고객 프로젝트에서 공통 Task를 추출해 재사용 Skill로 만들고, 검증을 거쳐 Skill Pack으로 묶어 다음 고객에게 판매합니다. 고객이 늘수록 Custom Code가 아니라 Product Library가 쌓입니다. "
             "이를 숫자로 관리하기 위해 재사용률, 즉 신규 고객에 적용할 때 하드웨어, 제어 로직, ToolSkill, 소프트웨어 모듈 중 몇 퍼센트를 그대로 썼는지를 12개월차부터 측정하고, 24개월까지 상승 추세를 확인하겠습니다. 임의의 목표치는 쓰지 않았습니다. "
             "Base Case에서도 매출 구성은 Custom Engineering에서 재사용 가능한 제품과 Skill로 이동합니다. 승인된 Task 목록 안에서만 수주하고 비표준 요청은 별도 견적으로 처리하는 것이 SI가 되지 않는 운영 규칙입니다.")

# ================================================================ 10 SKILL PORTABILITY
def s10(prs):
    s = new_slide(prs, '10')
    header(s, '10', 'Platform 검증', '하나의 Skill이 여러 Robot에서 동작해야 Platform이다', 'One Skill. Multiple Robots.', tag='CONCEPT RENDERING')
    y0 = 1.95; cw = 4.2; ih = (cw - 0.12) / 1.3333
    for x, img, lab, sub in [(0.6, 'portA', 'Robot Platform A', '협동로봇 · 화이트 6축'), (8.53, 'portB', 'Robot Platform B', '다른 브랜드 · 다른 링크 길이')]:
        card(s, x, y0, cw, ih + 0.62)
        picture(s, A + img + '.jpg', x + 0.06, y0 + 0.06, w=cw - 0.12, h=ih, name=lab + ' rendering')
        text(s, x + 0.2, y0 + ih + 0.14, cw - 0.4, 0.28, [[(lab, {'f': 'K'}), ('   ' + sub, {'size': 9, 'color': TEXT2})]], size=12)
    # middle column
    xm = 5.0; wm = 3.33; ym = y0 + 0.05
    b = box(s, xm, ym, wm, 0.95, fill=OR_FILL, line=OR, lw=1.25, r=0.08)
    text(s, xm + 0.2, ym + 0.12, wm - 0.3, 0.28, 'Handle Opening Skill', size=12.5, f='K', color=OR)
    text(s, xm + 0.2, ym + 0.44, wm - 0.3, 0.45, '파지 전략 · 힘 프로파일 · 동작 순서 — Robot과 무관한 Task 정의', size=9, color=TEXT, ls=1.12)
    tri(s, xm + wm / 2 - 0.06, ym + 1.05, s=0.12, color=OR, rot=180)
    b2 = box(s, xm, ym + 1.27, wm, 0.95, fill=CARD2, line=LINE2, lw=1.0, r=0.08)
    text(s, xm + 0.2, ym + 1.39, wm - 0.3, 0.28, 'Calibration', size=12.5, f='K')
    text(s, xm + 0.2, ym + 1.71, wm - 0.3, 0.45, 'Robot 어댑터 · TCP · 카메라 · 작업공간만 다시 맞춘다', size=9, color=TEXT2, ls=1.12)
    tri(s, xm + wm / 2 - 0.06, ym + 2.32, s=0.12, color=OR, rot=180)
    b3 = box(s, xm, ym + 2.54, wm, 0.58, fill=CARD2, line=OR, lw=1.0, r=0.08)
    box_text(b3, [[('같은 Task 수행', {'f': 'K', 'size': 12.5, 'color': TEXT}), ('  Robot B', {'f': 'S', 'size': 9, 'color': OR_LIGHT})]])
    line(s, 4.83, y0 + 1.5, 4.98, y0 + 1.5, color=OR, w=1.25, arrow=True)
    line(s, 8.35, y0 + 1.5, 8.51, y0 + 1.5, color=OR, w=1.25, arrow=True)
    # bottom
    y1 = 5.48
    card(s, 0.6, y1, 7.0, 1.38, fill=OR_FILL, line=OR, lw=1.25)
    label(s, 0.82, y1 + 0.14, 6.5, 'Seed 24개월 목표 · 기술 KPI이자 사업모델 KPI', color=OR, size=8.5)
    text(s, 0.82, y1 + 0.4, 6.6, 0.34, '동일 Task Skill을 최소 2개 Robot Platform에서 재사용 검증', size=14, f='K')
    text(s, 0.82, y1 + 0.8, 6.6, 0.5, ['측정: Platform B 적용 시 추가 엔지니어링 시간 · Task 완료율 · 재사용 모듈 비중', 'Platform B 통합은 M12~M18, 이식성 검증은 M18~M24'], size=9, color=TEXT2, ls=1.15)
    card(s, 7.8, y1, 4.93, 1.38, dash=True, line=YEL, fill=YEL_FILL)
    pill(s, 8.0, y1 + 0.14, None, 0.22, '스스로 인정하는 가설', size=7.5, spc=40, color=YEL, line=YEL)
    text(s, 8.0, y1 + 0.45, 4.6, 0.85, ['Robot 브랜드가 바뀔 때마다 처음부터 다시 티칭해야 한다면,', '우리는 Platform이 아니라 SI 사업에 가깝다.', '→ Seed 기간에 반드시 검증할 가설'], size=9.5, color=TEXT, ls=1.15)
    footer(s, '10')
    notes(s, "Physical AI Platform이라는 말이 실제 Platform이 되려면 조건이 하나 있습니다. 같은 Skill이 여러 로봇에서 재사용되어야 합니다. "
             "예를 들어 손잡이 열기 Skill은 Grasp 전략, 힘 프로파일, 동작 순서처럼 로봇과 무관한 Task 정의로 만듭니다. 로봇이 바뀌면 로봇 어댑터, TCP, 카메라, 작업공간 캘리브레이션만 다시 맞추고 같은 Task를 수행해야 합니다. "
             "그래서 Seed 24개월 목표로 동일 Task Skill을 최소 두 개의 로봇 플랫폼에서 재사용 검증하겠습니다. 이것은 기술 KPI이면서 동시에 비즈니스 모델 KPI입니다. "
             "솔직하게 말씀드리면, 로봇 브랜드가 바뀔 때마다 처음부터 다시 티칭해야 한다면 저희는 Platform 회사가 아니라 SI에 가깝습니다. 그래서 이것을 Seed 기간에 반드시 검증할 가설로 두고, Platform B 적용 시 추가 엔지니어링 시간과 완료율, 재사용 모듈 비중으로 측정하겠습니다.")
