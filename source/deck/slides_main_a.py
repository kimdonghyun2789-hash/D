from deckkit import *
from paths import RENDERS as A, ORIGINAL as O, MODEL_JSON

# ================================================================ 01 COVER
def s01(prs):
    s = new_slide(prs, '01')
    picture(s, A + 'cover_fullbleed.jpg', 0, 0, w=13.333, h=7.5, name='Cover rendering')
    placeholder(s, 0.6, 0.45, 2.1, 0.32, '[회사명 입력 필요]', size=9.5, align='c')
    text(s, 0.6, 1.5, 7.0, 0.3, 'FOUNDING & SEED INVESTMENT PROPOSAL', size=11, f='S', color=OR, spc=200, name='Kicker')
    text(s, 0.6, 1.88, 7.2, 1.85, ['ONE HAND.', 'MANY TOOLS.'], size=50, f='K', color=TEXT, ls=0.9, name='Title')
    text(s, 0.6, 3.83, 6.6, 0.9, ['기존 설비를 크게 바꾸지 않고,', 'Robot이 사람용 Interface를 사용할 수 있게 합니다.'], size=18, f='M', color=TEXT, ls=1.18, name='Statement')
    text(s, 0.6, 4.78, 6.6, 0.3, [[('첫 제품   ', {'color': MUTED, 'f': 'S', 'size': 11}), ('SoftHand-4 + Machine Tending Skill Pack', {'f': 'S', 'color': TEXT2})]], size=12.5, name='First product')
    cols = [('SEED 투자 요청', '₩2.0B', '20억원 · 회사 설립 자본', OR),
            ('검증 기간', '24개월', '제품 → 유료 고객 → 반복 발주', TEXT),
            ('첫 시장', 'Machine Tending', '기존 생산설비 (Brownfield)', TEXT)]
    x = 0.6; ws = [1.95, 2.05, 2.55]
    for (lab, val, sub, c), w in zip(cols, ws):
        text(s, x, 5.42, w, 0.22, lab, size=9, f='S', color=MUTED, spc=120)
        text(s, x, 5.66, w + 0.4, 0.45, val, size=22, f='K', color=c, ls=1.0)
        text(s, x, 6.12, w + 0.3, 0.24, sub, size=9.5, f='R', color=TEXT2)
        x += w + 0.25
        if x < 6.8: line(s, x - 0.13, 5.45, x - 0.13, 6.32, color=LINE2, w=0.75)
    pill(s, None, 6.55, None, 0.27, 'CONCEPT RENDERING', right=12.73, fill=BG)
    text(s, 0.6, 7.0, 10.5, 0.24, '2026.10  ·  Pre-seed 창업 제안  ·  대외비  ·  이미지는 실제 시제품이 아닌 Concept Rendering입니다', size=9.5, color=MUTED2, name='Footer')
    notes(s, "안녕하십니까. 저희는 사람이 쓰도록 만들어진 기존 생산설비를 크게 뜯어고치지 않고, 로봇이 그 설비를 그대로 사용할 수 있게 만드는 회사를 창업하려 합니다. "
             "첫 제품은 SoftHand-4와 Machine Tending Skill Pack입니다. 하나의 Hand로 설비 문 열기, 부품 투입, 레버·버튼 조작, 완성품 배출까지 한 공정을 끝내는 것이 목표입니다. "
             "이 자료는 운영 중인 회사의 성장자금 요청이 아니라, 회사를 설립하고 첫 고객을 확보하기 위한 Founding & Seed 제안서입니다. 요청 금액은 20억원이며, 24개월 안에 기술이 아니라 사업성을 증명하는 계획을 말씀드리겠습니다. "
             "화면의 이미지는 실제 시제품이 아니라 Concept Rendering입니다.")

# ================================================================ 02 PROBLEM
def s02(prs):
    s = new_slide(prs, '02')
    header(s, '02', '문제 정의', '기존 설비 자동화에는 여전히 너무 많은 재설계가 필요하다', 'Too Much Re-engineering for Every New Task.', tag='CONCEPT RENDERING')
    y0, hh = 1.95, 1.55
    # 1 existing equipment
    c1 = card(s, 0.6, y0, 2.85, hh)
    label(s, 0.78, y0 + 0.14, 2.5, '① 기존 설비', color=MUTED, size=9)
    text(s, 0.78, y0 + 0.38, 2.6, 0.32, '사람 손에 맞춰 설계됨', size=13, f='K')
    chips = ['문', '손잡이', '레버', '노브', '트레이', '공구']
    for i, t in enumerate(chips):
        chip(s, 0.78 + (i % 3) * 0.86, y0 + 0.82 + (i // 3) * 0.33, 0.78, 0.26, t, size=8.5, fill=CARD3, color=TEXT2)
    tri(s, 3.53, y0 + hh / 2 - 0.05)
    # 2 robot
    c2 = card(s, 3.73, y0, 1.85, hh)
    label(s, 3.9, y0 + 0.14, 1.6, '② Robot 도입', color=MUTED, size=9)
    text(s, 3.9, y0 + 0.38, 1.6, 0.62, ['Robot은', '이미 표준 제품'], size=13, f='K', ls=1.05)
    text(s, 3.9, y0 + 1.05, 1.6, 0.38, 'Arm · Controller는 구매 가능', size=8.5, color=TEXT2, ls=1.1)
    tri(s, 5.66, y0 + hh / 2 - 0.05)
    # 3 added re-engineering
    c3 = card(s, 5.86, y0, 4.35, hh)
    label(s, 6.04, y0 + 0.14, 4.0, '③ 작업마다 추가되는 재설계', color=OR, size=9)
    items = ['전용 Finger', 'Jig · Fixture', '설비 개조', '엔지니어링', '티칭', '검증']
    for i, t in enumerate(items):
        chip(s, 6.04 + (i % 3) * 1.37, y0 + 0.5 + (i // 3) * 0.48, 1.27, 0.38, t, size=10, fill=CARD3)
    tri(s, 10.29, y0 + hh / 2 - 0.05, color=OR)
    # 4 result
    c4 = card(s, 10.49, y0, 2.24, hh, fill=OR_FILL, line=OR, lw=1.25)
    label(s, 10.67, y0 + 0.14, 2.0, '④ 결과', color=OR, size=9)
    text(s, 10.67, y0 + 0.4, 1.95, 0.7, ['높은', '자동화 전환비용'], size=16, f='K', color=OR, ls=1.05)
    text(s, 10.67, y0 + 1.1, 1.95, 0.32, '작업이 바뀔 때마다 반복', size=9, color=OR_LIGHT)
    # bottom left: image card
    y1 = 3.78; h1 = 2.62
    card(s, 0.6, y1, 6.4, h1)
    text(s, 0.85, y1 + 0.18, 5.9, 0.3, [[('오늘의 자동화  ', {'f': 'K', 'size': 12}), ('작업마다 늘어나는 전용 End-effector · Jig', {'f': 'R', 'size': 11, 'color': TEXT2})]])
    picture_fit(s, O + 'hero02_dedicated_grippers.png', 1.35, y1 + 0.52, 4.9, 1.68, crop=(0.0467, 0.0733, 0.0667, 0.1015), name='HERO02 dedicated grippers')
    text(s, 0.85, y1 + 2.27, 5.9, 0.24, 'Parallel · Vacuum · 3-Jaw · Custom Finger · Magnetic · Jig / Fixture', size=9, color=MUTED2, align='c')
    # bottom right: stat
    card(s, 7.25, y1, 5.48, h1)
    text(s, 7.55, y1 + 0.1, 4.8, 1.1, '~75%', size=54, f='K', color=OR, ls=1.0)
    text(s, 7.55, y1 + 1.12, 4.95, 0.34, '로봇 시스템 TCO 중 초기 셋업 · 재설계에 묶인 비중', size=13, f='M')
    text(s, 7.55, y1 + 1.55, 4.95, 0.62, ['고객의 진짜 비용은 Robot Hand 가격이 아니라,', [('작업이 바뀔 때마다 반복되는 ', {}), ('자동화 전환비용', {'color': OR, 'f': 'S'}), ('이다', {})]], size=11.5, color=TEXT2, ls=1.15)
    text(s, 7.55, y1 + 2.27, 4.95, 0.24, 'Source: BCG, How Physical AI Is Reshaping Robotics Today (2026.4)', size=8.5, color=MUTED2)
    text(s, 0.6, 6.58, 12.13, 0.3, '다품종 · 소량 현장일수록 전환이 잦다 → 이 비용 때문에 자동화 자체가 성립하지 않는 공정이 남는다', size=11, color=TEXT2)
    footer(s, '02')
    notes(s, "기존 공장에는 문, 손잡이, 레버, 노브, 트레이처럼 사람 손에 맞춰 설계된 Interface가 이미 있습니다. 로봇 본체는 이제 표준 제품이라 사면 됩니다. "
             "문제는 그 다음입니다. 작업마다 Custom Finger, Jig와 Fixture, 설비 개조, 엔지니어링, 티칭, 검증이 추가되고, 제품이나 작업이 바뀌면 이 과정이 반복됩니다. "
             "BCG는 2026년 4월 보고서에서 전통적인 로봇 도입 총소유비용의 약 75%가 초기 셋업과 재설계에 묶여 있다고 분석했습니다. "
             "그래서 고객의 진짜 비용은 Robot Hand 가격이 아니라 자동화 전환비용입니다. 다품종·소량 현장일수록 이 비용 때문에 자동화가 성립하지 않습니다.")

# ================================================================ 03 INSIGHT (+ installed base)
def s03(prs):
    s = new_slide(prs, '03')
    header(s, '03', '핵심 Insight', '설비를 Robot에 맞추는 대신, Robot이 기존 설비를 사용하게 한다', "Don't Rebuild the Workstation.", tag='CONCEPT RENDERING')
    y0, h0 = 1.95, 3.85
    # left: today
    card(s, 0.6, y0, 4.45, h0)
    label(s, 0.85, y0 + 0.2, 4.0, '기존 방식', color=MUTED, size=9.5)
    text(s, 0.85, y0 + 0.45, 4.0, 0.42, '설비를 Robot에 맞춘다', size=17, f='K')
    rows = [('설비 개조', '자동문 · 공압 구동기 · I/O 추가'), ('전용 툴링', '작업별 전용 Finger · Jig · Fixture'), ('End-effector 추가', 'Tool Changer · Gripper 여러 개'),
            ('반복', '작업이 바뀌면 다시 설계 · 티칭 · 검증')]
    yy = y0 + 1.08
    for a, b in rows:
        text(s, 0.85, yy, 1.5, 0.3, a, size=11, f='S', color=TEXT)
        text(s, 2.35, yy + 0.02, 2.6, 0.5, b, size=10, color=TEXT2, ls=1.1)
        yy += 0.6
    line(s, 0.85, y0 + h0 - 0.42, 4.8, y0 + h0 - 0.42, color=LINE, w=0.75)
    text(s, 0.85, y0 + h0 - 0.34, 4.0, 0.26, '→ 작업마다 재설계 비용이 반복된다', size=10.5, f='S', color=MUTED)
    # center: product
    picture_fit(s, A + 'product.png', 5.25, 1.78, 2.8, 4.0, name='SoftHand-4 product rendering')
    text(s, 5.15, 5.62, 3.0, 0.24, 'SoftHand-4 (Concept)', size=9.5, f='S', color=TEXT2, align='c')
    # right: our way
    card(s, 8.28, y0, 4.45, h0, fill=OR_FILL, line=OR, lw=1.25)
    label(s, 8.53, y0 + 0.2, 4.0, '우리 방식', color=OR, size=9.5)
    text(s, 8.53, y0 + 0.45, 4.0, 0.42, 'Robot이 설비를 사용한다', size=17, f='K', color=TEXT)
    text(s, 8.53, y0 + 0.98, 4.0, 0.26, '사람용 Interface를 고치지 않고 그대로 사용', size=10.5, f='S', color=OR_LIGHT)
    ch = ['문', '손잡이', '레버', '노브', '트레이', '용기', '설비 조작부', '공구']
    pos = [(8.53, 1.36, 0.6), (9.21, 1.36, 0.82), (10.11, 1.36, 0.7), (10.89, 1.36, 0.7), (11.67, 1.36, 0.8), (8.53, 1.72, 0.6), (9.21, 1.72, 1.1), (10.39, 1.72, 0.7)]
    for t, (x, yy, w) in zip(ch, pos):
        chip(s, x, y0 + yy, w, 0.28, t, size=8.5, fill='3A2618', color=TEXT)
    line(s, 8.53, y0 + 2.3, 12.48, y0 + 2.3, color='5A3A26', w=0.75)
    text(s, 8.53, y0 + 2.45, 4.0, 0.9, [[('SoftHand-4', {'f': 'K', 'color': TEXT}), ('는 자동화 유연성', {})], '(Automation Flexibility)을 만드는 하드웨어 Interface'], size=12, f='M', color=TEXT2, ls=1.2)
    # bottom: installed base strip
    yb = 6.0
    card(s, 0.6, yb, 12.13, 0.82, fill=CARD)
    text(s, 0.85, yb + 0.14, 2.6, 0.26, '첫 시장은 이미 설치된 Robot', size=11.5, f='K', color=TEXT)
    text(s, 0.85, yb + 0.44, 2.7, 0.24, '휴머노이드를 기다리지 않는다', size=9.5, color=TEXT2)
    stats = [('508만 대', '가동 중 산업용 Robot (2025)'), ('60만+ 대', '2025년 신규 설치 · +11%'), ('3.0만 대', '한국 연간 설치 · 로봇밀도 세계 1위')]
    x = 3.75
    for v, t in stats:
        line(s, x - 0.18, yb + 0.16, x - 0.18, yb + 0.66, color=LINE2, w=0.75)
        text(s, x, yb + 0.1, 1.45, 0.42, v, size=19, f='K', color=OR if v.startswith('508') else TEXT, ls=1.0)
        text(s, x + 1.42, yb + 0.25, 1.5, 0.45, t, size=9, color=TEXT2, ls=1.1)
        x += 3.0
    text(s, 0.6, 6.86, 12.13, 0.2, 'Source: IFR World Robotics 2026 (2026.9) · IFR Robot Density (2026.4)', size=8, color=MUTED2, align='r')
    footer(s, '03')
    notes(s, "그래서 저희의 핵심 Insight는 단순합니다. 설비를 로봇에 맞게 바꾸는 대신, 로봇이 기존 설비를 사용하게 하자는 것입니다. "
             "기존 방식은 자동문과 공압 액추에이터를 달고, 작업마다 전용 핑거와 지그를 만들고, 툴 체인저로 그리퍼를 바꿉니다. 저희 방식은 문, 손잡이, 레버, 트레이처럼 사람용 Interface를 그대로 사용합니다. "
             "고객이 사는 것은 로봇 손이 아니라 Automation Flexibility이고, SoftHand-4는 그것을 가능하게 하는 하드웨어 Interface입니다. "
             "그리고 이 시장은 이미 존재합니다. IFR에 따르면 2025년 말 전 세계 약 508만 대의 산업용 로봇이 가동 중이고, 2025년에만 60만 대 이상이 새로 설치됐습니다. 한국은 연 3만 대가 설치되는, 로봇밀도 세계 1위 시장입니다. 저희는 휴머노이드를 기다리지 않고 이미 설치된 로봇과 기존 설비에서 시작합니다.")

# ================================================================ 04 CORE TECH
def s04(prs):
    s = new_slide(prs, '04')
    header(s, '04', '핵심 기술', '잡을 때는 부드럽게, 일할 때는 단단하게', 'Soft to Grasp. Rigid to Work.', tag='CONCEPT RENDERING')
    y0, h0 = 1.95, 2.62
    def side(x, lab, title, items, tagt, orange=False):
        card(s, x, y0, 3.7, h0, fill=CARD)
        label(s, x + 0.25, y0 + 0.2, 3.2, lab, color=OR, size=9.5)
        text(s, x + 0.25, y0 + 0.45, 3.3, 0.42, title, size=17, f='K')
        yy = y0 + 1.05
        for a, b in items:
            dot(s, x + 0.27, yy + 0.1, 0.08, OR)
            text(s, x + 0.45, yy, 3.1, 0.28, [[(a, {'f': 'S', 'color': TEXT}), ('   ' + b, {'size': 9.5, 'color': TEXT2})]], size=11.5)
            yy += 0.38
        pill(s, x + 0.25, y0 + h0 - 0.42, None, 0.26, tagt, color=OR if orange else TEXT2, line=OR if orange else LINE2)
    side(0.6, '잡기 · GRASP', '부드러워야 잘 잡는다', [('형상 차이 대응', '다른 SKU · 용기 · 부품'), ('위치 오차 흡수', 'Jig 의존도 감소'), ('미끄러짐 대응', '촉각 · 힘 제어')], '순응성 Compliance')
    side(9.03, '일하기 · WORK', '단단해야 일을 끝낸다', [('토크 전달', '레버 · 노브'), ('반력 지지', '문 · 손잡이'), ('모멘트 저항', '투입 자세 유지')], '강성 Stiffness', orange=True)
    # center image + markers
    p, (px, py, pw, ph) = picture_fit(s, A + 'cutaway.png', 4.55, 1.75, 4.23, 4.85, name='SoftHand-4 cutaway rendering')
    marks = [(1, 0.16, 0.05), (2, 0.50, 0.22), (3, 0.90, 0.33), (4, 0.30, 0.235), (5, 0.52, 0.86)]
    for n, fx, fy in marks:
        num_badge(s, px + pw * fx - 0.13, py + ph * fy - 0.13, n, d=0.26, size=9)
    # conflict marker between columns
    text(s, 0.6, 4.7, 3.7, 0.26, '⇅  잡기와 일하기는 서로 충돌한다', size=9.5, f='S', color=MUTED)
    # five elements (bottom)
    y1 = 5.05
    els = [(1, '부드러운 접촉면', 'Soft Contact Surface', '교체형 탄성 패드', 'CONCEPT'),
           (2, '하중 지지 골격', 'Load-bearing Skeleton', '토크 · 반력은 골격이 부담', 'CONCEPT'),
           (3, '대향 엄지', 'Opposable Thumb', '손잡이 · 레버를 감싸 쥔다', 'CONCEPT'),
           (4, '가변 강성 · 잠금', 'Variable Stiffness', '작업 순간 관절 강성 상승', '검증 예정'),
           (5, '힘 · 미끄러짐 제어', 'Force & Slip Control', '촉각 + 손목 힘센서', 'TARGET')]
    # left group 1-3 under left card, right group 4-5 under right card
    def el(x, y, n, ko, en, desc, tg, w=3.7):
        num_badge(s, x, y + 0.02, n, d=0.26, size=9)
        text(s, x + 0.36, y, w - 1.4, 0.26, [[(ko, {'f': 'S'}), ('  ' + en, {'size': 8, 'color': MUTED})]], size=10.5)
        text(s, x + 0.36, y + 0.26, w - 1.4, 0.22, desc, size=9, color=TEXT2)
        tw = max(0.8, text_width_in(tg, 'S', 7.5, 40) + 0.24)
        pill(s, x + w - tw, y + 0.04, tw, 0.22, tg, size=7.5, spc=40, color=YEL if tg == '검증 예정' else (OR if tg == 'TARGET' else TEXT2), line=YEL if tg == '검증 예정' else (OR if tg == 'TARGET' else LINE2))
    for i, e in enumerate(els[:3]): el(0.6, y1 + i * 0.52, *e)
    for i, e in enumerate(els[3:]): el(9.03, y1 + i * 0.52, *e)
    card(s, 9.03, y1 + 1.06, 3.7, 0.48, fill=OR_FILL, line=OR, lw=1.0)
    text(s, 9.18, y1 + 1.1, 3.45, 0.42, [[('우리의 접근  ', {'f': 'S', 'size': 8.5, 'color': OR, 'spc': 60}), ('부드러운 접촉 + 단단한 골격 + 전환 가능한 강성', {'f': 'S', 'size': 9.5})]], size=9, anchor='m', ls=1.05)
    text(s, 0.6, 6.68, 12.13, 0.26, '구조는 Concept · 구동 방식(전동 Tendon / 유압 / 공압)은 창업 후 3개월 내 비교시험으로 결정 · 4지(손가락 3 + 대향 엄지)는 머신텐딩에 필요한 최소 구성, 5지는 Series A 이후 (Appendix A7)', size=8.5, color=MUTED2)
    footer(s, '04')
    notes(s, "사람용 Interface를 쓰려면 손이 두 가지를 동시에 해야 합니다. 잡을 때는 형상 차이와 위치 오차, 미끄러짐을 흡수하는 부드러움이 필요하고, 일할 때는 레버의 토크와 문의 반력, 부품을 넣을 때의 모멘트를 견디는 단단함이 필요합니다. "
             "부드럽기만 한 손은 잘 잡지만 일할 때 처지고, 단단한 그리퍼는 힘은 좋지만 형상에 적응하지 못합니다. 저희 방향은 Soft to Grasp, Rigid to Work입니다. "
             "교체형 탄성 접촉면, 하중을 받는 골격, 손잡이와 레버를 감싸 쥐는 대향 엄지, 작업 순간 강성을 높이는 구조, 촉각과 손목 힘센서 기반 제어입니다. "
             "4지 구조는 Machine Tending 작업에 필요한 최소 구성이며, 부품 수와 비용, 내구성을 우선했습니다. 5지는 Seed 성공조건에서 제외했고 Series A 이후 확장 제품입니다. 구동 방식은 창업 후 3개월 안에 비교시험으로 결정합니다.")
