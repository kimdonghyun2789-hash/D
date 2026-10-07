# Main deck (24 slides). Every slide answers one or more of the six investor questions (Q1~Q6).
from common import *
from common import M
import drawings as DR

Q = {1: '누가 가장 먼저 돈을 내는가', 2: '고객이 얼마까지 지불할 가능성이 있는가', 3: '한 세대 설치 시 회사가 얼마를 버는가',
     4: '집마다 다른 주방을 얼마나 표준화할 수 있는가', 5: '설치대수 증가 시 반복매출·Gross Margin이 개선되는가',
     6: 'Seed 20억원 이후 어떤 핵심 Risk가 제거되는가'}

def N():
    hh3 = M['household']['purchase_direct_Y3']; hh5 = M['household']['purchase_direct_Y5']
    rt3 = M['household']['rental_direct_Y3']; rt5 = M['household']['rental_direct_Y5']
    return dict(hh3=hh3, hh5=hh5, rt3=rt3, rt5=rt5, r3=M['rental']['Y3'], r5=M['rental']['Y5'],
                c3=M['care']['Y3'], c5=M['care']['Y5'], mk=M['market']['B'], v=M['value'], F=M['funds'])

# ---------------------------------------------------------------- 01 cover
def s01(prs):
    kit.set_theme('dark')
    s = start(prs, 'cover', 1, 'ARKI Robotics — 주거공간 일체형 Robotics System', bg='15171A',
              visual='Charcoal 배경. 좌측 회사명·정의, 우측 Kitchen 단면 CONCEPT 선화 (상부장 하단 Rail + 역설치 Arm + Reach + Human Zone).',
              chart='단면 선화 1개 (CONCEPT 표기)',
              note=('ARKI Robotics는 주방용 Robot Arm 회사가 아니라 Robot과 주방 공간을 함께 설계하는 Residential Built-in Robotics 회사입니다. '
                    '첫 Application은 Kitchen Clean-up이고, 첫 시장은 구축 아파트 Premium Kitchen Remodeling입니다. '
                    '오늘 자료는 완성된 미래주방이 아니라, Seed 20억원으로 어떤 Commercial Risk를 어떤 순서로 제거할지에 대한 투자 제안입니다. '
                    '모든 수치는 FACT, DERIVED, ASSUMPTION, TARGET으로 구분했고, 현재 실적·계약·고객·Partner는 없습니다.'))
    text(s, MX, 0.9, 6.4, 0.3, 'SEED INVESTMENT PROPOSAL  ·  2026.10  ·  DRAFT v1', size=11, bold=True, color=T['accent'])
    text(s, MX, 1.5, 6.6, 1.0, 'ARKI Robotics', size=48, bold=True)
    text(s, MX, 2.45, 6.6, 0.4, '아키로보틱스 (가칭)  ·  Architecture + Robotics', size=15, color=T['text2'])
    text(s, MX, 3.15, 6.6, 1.25, '주거공간 일체형\nRobotics System', size=30, bold=True, line=1.0)
    hline(s, MX, 4.55, 5.6, color=T['line'])
    text(s, MX, 4.75, 6.3, 1.3,
         ['Robot과 Kitchen을 공간 설계 단계에서 함께 구성',
          '첫 Application: Kitchen Clean-up (식기 이동 · 식세기 연동 · 수납 복귀)',
          '구축 Premium Remodeling = Validation  →  신축 Robot-ready Option = Scale'],
         size=12, color=T['text2'], bullet='–', space_after=4)
    text(s, MX, 6.45, 6.6, 0.4, '모든 수치: FACT · DERIVED · ASSUMPTION · TARGET 표기  |  실적·계약·고객·Partner 없음 (Concept 단계)',
         size=9, color=T['muted'])
    DR.section(s, 7.9, 1.25, 4.7, 4.9, detail=True, dark=True)
    kit.tag(s, 7.9, 6.35, 'CONCEPT')
    text(s, 9.1, 6.33, 3.5, 0.25, 'Kitchen 단면 · 상부장 하단 Rail · 역설치 Arm (도식)', size=9, color=T['muted'], check=False)
    kit.set_theme('light')

# ---------------------------------------------------------------- 02 six questions
def s02(prs):
    n = N(); hh3, hh5, mk, F = n['hh3'], n['hh5'], n['mk'], n['F']
    s = start(prs, 'thesis', 2, 'Seed 투자 판단을 위한 6개 질문과 현재 답', q=[1, 2, 3, 4, 5, 6],
              visual='6행 표: 질문 / 현재 답 / 근거 Tag / Seed 검증 방법. 하단에 Seed 목적 Statement.',
              chart='없음 (표)',
              note=('투자 판단에 필요한 질문은 여섯 가지로 정리했습니다. 이후 모든 슬라이드는 이 중 하나 이상에 답하도록 구성했고, 우측 상단 Q 표시가 해당 질문입니다. '
                    '현재 답은 모두 가설이며, 오른쪽 열이 Seed 기간에 이를 사실로 바꾸는 방법입니다. 특히 2번 지불의사와 3번 세대 경제성은 Robot 가격과 BOM에 가장 민감합니다.'))
    y = head(s, '01  투자 판단 요약', 'Seed 투자 판단을 위한 6개 질문과 현재 답',
             sub='모든 Slide는 아래 질문 중 하나 이상에 답함 (우측 상단 Q 표시). 현재 답은 가설, Seed 기간에 Evidence로 전환.')
    rows = [
        ['Q1', '누가 가장 먼저 돈을 내는가?', '구축 아파트 Premium Kitchen Remodeling 세대 (철거·가구 신규 시공 예정 세대)', ttxt('ASSUMPTION'), 'Interview 50명 · 유료 Pilot 3~5세대'],
        ['Q2', '얼마까지 지불할 가능성이 있는가?', f"Robot-ready 증분 {mann(inp('p_rr'))} + Robot {mann(inp('p_robot'))}만원 또는 월 {mann(inp('p_rent'))}만원 Rental.\n가치 Anchor 월 {n['v']['lo']:.0f}~{n['v']['hi']:.0f}만원과 Gap 존재", ttxt('ASSUMPTION'), 'PSM · Conjoint (n≥300) · 예약금 Test'],
        ['Q3', '한 세대에서 회사가 얼마를 버는가?', f"5년 매출 {mann(hh3['rev5'])}만원, Lifetime Contribution {mann(hh3['contrib5'])}만원 (Y3 원가) → {mann(hh5['contrib5'])}만원 (Y5 원가)", ttxt('DERIVED'), 'BOM · 설치시간 · Service 원가 실측'],
        ['Q4', '집마다 다른 주방을 얼마나 표준화하는가?', 'Kitchen Geometry 5종 × Robot Architecture 4종 → Template 3~5개로 주요 평면 Cover 가설', ttxt('ASSUMPTION'), '실제 평면 30개 분석 · Standard Module 사용률 65%'],
        ['Q5', '설치대수 증가 시 반복매출·GM이 개선되는가?', f"매출총이익률 {pct(B('gm')[2])} (Y3) → {pct(B('gm')[4])} (Y5). Recurring 비중은 Y5 {pct(B('recurring')[4] / B('rev')[4])}, 정상상태 약 {pct(M['steady']['rec_share'])}", ttxt('DERIVED'), 'Care 방문원가 · Consumables 교체주기 실측'],
        ['Q6', 'Seed 이후 어떤 Risk가 제거되는가?', 'Apartment Fit · 기술 · 표준화 · WTP · 설치/Rental/Service 경제성 · Channel의 8개 Risk', ttxt('TARGET'), 'M6~M24 Kill Criteria 5단계'],
    ]
    table(s, MX, y, CW, ['#', '질문', '현재 답 (가설)', 'Tag', 'Seed 검증'], rows,
          col_w=[0.45, 2.75, 5.0, 1.05, 2.58], size=10, label='q6', max_h=4.2)
    statement(s, MX, 6.15, CW, 'Seed 20억원 = 완성형 미래주방 개발자금이 아닌, 공간성·기술성·표준화·가격·설치경제성·고객수요·Channel을 검증하는 자본',
              size=12)
    foot(s, 2)

# ---------------------------------------------------------------- 03 investment proof
def s03(prs):
    s = start(prs, 'proof', 3, 'Investment Proof: 현재 있는 것과 계획인 것', q=[6],
              visual='좌우 2분할. 좌 CURRENT EVIDENCE (현재 존재 항목만, 없음은 회색), 우 SEED TARGET (M24 목표, TARGET Tag).',
              chart='없음',
              note=('현재 있는 것과 앞으로 만들 것을 한 장에서 분리했습니다. 왼쪽은 오늘 기준 실제로 존재하는 Evidence입니다. '
                    '공식 통계 정리와 사업·재무 가설 외에는 Prototype, 고객 인터뷰, Partner, 특허 모두 아직 없습니다. 창업자 정보는 입력이 필요합니다. '
                    '오른쪽은 Seed 24개월 동안 만들 Evidence이며, 투자 판단은 이 검증 계획의 구체성과 Founder 적합성에 달려 있습니다.'))
    y = head(s, '02  Investment Proof', 'Investment Proof: 현재 있는 것과 계획인 것',
             sub='현재 Evidence와 Seed Target을 혼합하지 않음. 존재하지 않는 항목은 "없음"으로 표기.')
    cw = (CW - 0.4) / 2
    rect(s, MX, y, cw, 0.42, fill=T['text']); text(s, MX + 0.15, y, cw, 0.42, 'CURRENT EVIDENCE  (2026.10 기준)', size=12, bold=True, color='FFFFFF', anchor='m')
    rect(s, MX + cw + 0.4, y, cw, 0.42, fill=T['accent']); text(s, MX + cw + 0.55, y, cw, 0.42, 'SEED TARGET  (M24까지)', size=12, bold=True, color='FFFFFF', anchor='m')
    cur = [('Founder Experience', '[Founder 정보 필요]', 'TBV'),
           ('실제 Kitchen 설계자료 · 평면 분석', '없음', '없음'),
           ('Prototype · Demo', '없음', '없음'),
           ('Customer Interview', '없음', '없음'),
           ('Partner Meeting · LOI', '없음', '없음'),
           ('Patent', '없음 (출원 후보 10건 정리, A10)', '없음'),
           ('BOM', '공개가 기반 추정만 (A4)', 'ASSUMPTION'),
           ('시장 데이터', '공식 통계 정리 (A2, A23)', 'FACT'),
           ('사업·재무 모델', '가설 수립 (본 자료, xlsx)', 'ASSUMPTION')]
    tgt = [('Working Prototype + Full-scale Mock-up 2식', 'M6~M12'),
           ('실제 평면 30개 분석 · Kitchen Template 3~5개', 'M3~M12'),
           ('Approved Task 3개 이상 · Clean-up Integrated Demo', 'M9~M12'),
           ('Consumer Interview 50명 · WTP Test (PSM·Conjoint)', 'M3~M12'),
           ('Home Pilot 3~5세대 (Paid Pilot 포함)', 'M12~M24'),
           ('Validated BOM · 설치비 · 설치시간', 'M12~M24'),
           ('Rental · Care · Consumables Economics 실측', 'M18~M24'),
           ('Kitchen 가구·Interior Partner Pilot 협의', 'M12~M24'),
           ('Patent 출원 5~8건 (선행기술조사 후)', 'M3~M18')]
    rh = 0.43; yy = y + 0.5
    for i, (a, b, tg) in enumerate(cur):
        ry = yy + i * rh
        hline(s, MX, ry + rh, cw)
        text(s, MX + 0.1, ry + 0.03, 2.65, rh - 0.04, a, size=10, bold=True, anchor='m')
        col = T['muted'] if tg == '없음' else T['text2']
        text(s, MX + 2.8, ry + 0.03, cw - 4.05, rh - 0.04, b, size=9.5, color=col, anchor='m')
        kit.tag(s, MX + cw - 1.15, ry + 0.12, tg)
    for i, (a, when) in enumerate(tgt):
        ry = yy + i * rh; xx = MX + cw + 0.4
        hline(s, xx, ry + rh, cw)
        text(s, xx + 0.1, ry + 0.03, cw - 1.9, rh - 0.04, a, size=10, bold=True, anchor='m')
        text(s, xx + cw - 1.75, ry + 0.03, 0.85, rh - 0.04, when, size=9.5, color=T['text2'], anchor='m')
        kit.tag(s, xx + cw - 0.82, ry + 0.12, 'TARGET')
    note_line(s, '판단 포인트: 현재 Evidence는 "공식 시장 통계 + 사업 가설" 수준 → Seed 투자 판단은 ① Founder 적합성 ② 검증 계획의 구체성 ③ Kill Criteria의 명확성에 의존',
              y=6.62, size=10, color=T['text'])
    foot(s, 3)

# ---------------------------------------------------------------- 04 problem
def s04(prs):
    s = start(prs, 'problem', 4, '개별 가전 자동화와 Kitchen Workflow의 단절', q=[1, 2],
              visual='3열 (Dishwasher / Induction / Storage): 상단 "가전 자동화" 검정 블록, 하단 "사람 수행" 주황 테두리 블록. 하단에 Workflow 띠 (식탁→Sink→식세기→수납)와 Gap 표시.',
              chart='Workflow Gap Diagram',
              note=('식기세척기, 인덕션, 수납장은 각각 자동화되어 있지만 그 사이를 잇는 물리적 작업은 여전히 사람이 합니다. '
                    '식기세척기는 세척을 자동화했지만 투입·인출·수납은 사람 몫입니다. ARKI가 겨냥하는 것은 가전 내부가 아니라 가전과 가전 사이의 Physical Task입니다. '
                    '다만 이 Pain이 돈을 낼 만큼 큰지는 아직 검증되지 않았고, Seed 첫 3개월에 30세대 Time-diary로 측정합니다.'))
    y = head(s, '03  Problem', '개별 가전 자동화와 Kitchen Workflow의 단절',
             sub='가전 내부 공정은 자동화. 가전과 가전 사이의 Physical Task는 여전히 사람 수행.')
    cols = [('Dishwasher', '세척 · 건조', ['식기 투입', '인출', '수납']),
            ('Induction', '가열 · 온도 유지', ['재료 투입', '젓기', '뚜껑 조작']),
            ('Storage', '보관', ['정리', '복귀', '분류'])]
    cw = 2.55; gap = 0.25; x0 = MX
    for i, (name, auto, human) in enumerate(cols):
        x = x0 + i * (cw + gap)
        text(s, x, y, cw, 0.32, name, size=15, bold=True)
        rect(s, x, y + 0.42, cw, 0.62, fill=T['text'])
        text(s, x + 0.15, y + 0.42, cw - 0.3, 0.62, [[('가전 자동화  ', {'size': 9, 'color': 'A9AEB5'}), (auto, {'bold': True})]],
             size=13, color='FFFFFF', anchor='m')
        for j, h in enumerate(human):
            yy = y + 1.16 + j * 0.5
            rect(s, x, yy, cw, 0.42, line=T['accent'], lw=1.0)
            text(s, x + 0.15, yy, cw - 0.3, 0.42, [[('사람 수행  ', {'size': 9, 'color': T['accent']}), (h, {'bold': True})]],
                 size=12, anchor='m')
    # right: key statement
    rx = x0 + 3 * (cw + gap) + 0.1; rw = W - MX - rx
    rect(s, rx, y, rw, 2.62, fill=T['soft'])
    text(s, rx + 0.25, y + 0.2, rw - 0.5, 0.3, '핵심', size=11, bold=True, color=T['accent'])
    text(s, rx + 0.25, y + 0.5, rw - 0.5, 1.1, 'Appliance Automation\n≠ Kitchen Workflow Automation', size=16, bold=True, line=1.0)
    text(s, rx + 0.25, y + 1.55, rw - 0.5, 0.95, ['ARKI Target: 가전 사이 Physical Task 자동화',
                                                    'V1 범위: 식기 이동 · 식세기 연동 · 수납 복귀'],
         size=11, color=T['text2'], bullet='–', space_after=3)
    # workflow band
    yb = y + 2.95
    text(s, MX, yb, 6, 0.3, 'Kitchen Clean-up Workflow  (식사 후)', size=12, bold=True)
    steps = ['식탁 / Counter', 'Sink', 'Dishwasher', 'Storage']
    fills = [T['soft'], T['soft'], T['text'], T['soft']]; colors = [T['text'], T['text'], 'FFFFFF', T['text']]
    bw = 2.1; gap2 = 1.05; yy = yb + 0.42
    for i, st in enumerate(steps):
        bx = MX + i * (bw + gap2)
        chip(s, bx, yy, bw, 0.55, st, fill=fills[i], color=colors[i], size=12)
        if i < 3:
            arrow(s, bx + bw + 0.04, yy + 0.27, bx + bw + gap2 - 0.04, yy + 0.27, color=T['accent'], lw=2)
            lab = ['이동 · 분류', '투입', '인출 · 수납'][i]
            text(s, bx + bw, yy + 0.62, gap2, 0.25, lab, size=9, bold=True, color=T['accent'], align='c', check=False)
    text(s, MX, yy + 0.98, CW, 0.3, '주황 화살표 = 사람이 수행하는 Physical Task (ARKI 자동화 대상)   |   검정 = 가전이 이미 자동화한 공정',
         size=9, color=T['muted'])
    note_line(s, 'Pain 크기는 미검증 (TO BE VALIDATED): Clean-up 소요시간·빈도는 Seed M0~M3 Time-diary 30세대로 측정. 식기세척기 보급률 최신 공식 통계 없음 (2019~2020 업계 추정 10%대, A3).',
              y=6.45)
    foot(s, 4)

# ---------------------------------------------------------------- 05 integration
def s05(prs):
    s = start(prs, 'integration', 5, '가정용 Robot의 난이도는 AI보다 Integration에서 발생', q=[4],
              visual='좌측 5행 비교표 (공간·안전·설치·가구·유지관리 × 기존 Robot 추가형 vs ARKI Robot-ready 설계형). 우측 ARKI 접근 5개 원칙과 기대효과.',
              chart='비교표',
              note=('가정용 Robot이 어려운 이유를 AI 성능만으로 보지 않습니다. 실제 설치 현장에서는 공간, 안전, 설치, 가구, 유지관리가 동시에 문제가 됩니다. '
                    '기존 주방에 Robot을 나중에 추가하면 이 모든 변수를 AI가 현장에서 해결해야 합니다. '
                    'ARKI는 공간의 일부를 구조화해서 Robot이 움직이는 영역과 사람 영역을 나누고, Home Position과 표준 Interface를 미리 만들어 둡니다. '
                    '효과의 크기는 아직 수치로 주장하지 않고, Mock-up에서 설치시간과 Task 성공률로 측정합니다.'))
    y = head(s, '04  Integration 문제', '가정용 Robot의 난이도는 AI보다 Integration에서 발생',
             sub='Robot AI에 모든 Complexity를 맡기지 않음. 공간 설계로 Task 조건을 먼저 고정.')
    rows = [['공간', 'Reach 불일치 · 동선 침해 · 수납 위치 제각각', 'Robot Home·Rail 위치 선정 · 식세기 상향 배치 · Robot-friendly 수납'],
            ['안전', '머리 위 작업 · 사람 근접 · 낙하물', 'Human Zone / Robot Zone 분리 · Zone 진입 시 정지 · 통로 위 운반 금지'],
            ['설치', '구조체 정착·전원·통신 현장 대응 · 장시간 Calibration', '보강 Frame·전용 회로·통신 사전 시공 · Auto Calibration Target'],
            ['가구', 'Kitchen 기본기능 저하 · 도어·서랍 간섭', 'Robot 고장 시 일반 Kitchen 사용 · 간섭 없는 Garage·Dock'],
            ['유지관리', 'A/S 접근 불가 · 위생 · 소모품 관리 부재', 'Service Access Panel · 세척 Dock · Care·Consumables 정기 운영']]
    table(s, MX, y, 7.9, ['변수', '기존: 기존 주방 + Robot 추가', 'ARKI: Robot-ready 설계'], rows, col_w=[1.0, 3.2, 3.7],
          size=10, label='integ', max_h=3.6)
    rx = MX + 8.2; rw = W - MX - rx
    rect(s, rx, y, rw, 4.45, fill=T['soft'])
    text(s, rx + 0.2, y + 0.15, rw - 0.4, 0.3, 'ARKI 접근', size=13, bold=True)
    text(s, rx + 0.2, y + 0.55, rw - 0.4, 2.0, ['공간 일부 구조화', 'Robot 이동영역 제한 (Rail · Dock)', 'Human Zone 분리',
                                                 'Robot Home Position 확보', '표준 Kitchen Interface'],
         size=12, bullet='–', space_after=5)
    hline(s, rx + 0.2, y + 2.6, rw - 0.4)
    text(s, rx + 0.2, y + 2.7, rw - 0.4, 0.3, '기대 효과 (Mock-up 측정 대상)', size=11, bold=True, color=T['accent'])
    text(s, rx + 0.2, y + 3.05, rw - 0.4, 1.3, ['Robot Task 난이도 · 실패 가능성 감소', '설치 Complexity · 현장 Custom Engineering 감소',
                                                 '효과 크기는 수치 주장 없음 → 설치시간·성공률로 측정'],
         size=10.5, color=T['text2'], bullet='–', space_after=3)
    statement(s, MX, 6.2, CW, '가정용 Robot의 문제 = AI + 공간 · 안전 · 설치 · 가구 · 유지관리의 Integration 문제  →  ARKI는 Robot과 Kitchen을 함께 설계', size=12)
    foot(s, 5)

# ---------------------------------------------------------------- 06 housing environment
def s06(prs):
    mk = M['market']['B']
    s = start(prs, 'housing', 6, '적용환경: Bay는 변수, 표준화 기준은 Kitchen Geometry', q=[1, 4],
              visual='좌측 FACT KPI 6개 (주택총조사·주택통계). 우측 3단 분류 Diagram: 적용환경 변수(신축/구축·Bay·평형) → Kitchen Geometry 5종 → Robot Architecture 4종 → Product Code 예시.',
              chart='KPI Tile + 분류 Diagram',
              note=('국내 주택 2,018만호 중 65.8%가 아파트이고, 20년 이상 주택이 56%입니다. 이 숫자는 공식 통계입니다. '
                    '제품 표준화 기준은 2Bay·3Bay 같은 Bay 구성이 아니라 주방의 기하학적 형태입니다. Bay는 적용환경 변수로만 씁니다. '
                    '주방을 일자형부터 아일랜드형까지 5가지로 나누고, Robot 설치 방식 4가지와 조합해 REMODEL + 11자형 + Rail Type A처럼 제품을 분류합니다.'))
    y = head(s, '05  국내 공동주택 적용환경', '적용환경: Bay는 변수, 표준화 기준은 Kitchen Geometry',
             sub='한국 공동주택은 신축/구축 · 2/3/4Bay · 다양한 평형이 공존. 제품 분류는 Kitchen Geometry × Robot Installation Architecture.')
    k = [('2,018만호', '총주택 (2025.11)', 'FACT'), ('65.8%', '아파트 비중 → 약 1,328만호', 'FACT'),
         ('56.0%', '준공 20년 이상 주택 비중', 'FACT'), ('30.6%', '준공 30년 이상 주택 비중', 'FACT'),
         ('34.2만호', '2025 주택 준공 (−17.8%)', 'FACT'), ('23.6만 → 18.3만', '아파트 입주 2025 → 2026E', 'FACT')]
    for i, (v, l, tg) in enumerate(k):
        cx = MX + (i % 2) * 2.45; cy = y + (i // 2) * 1.32
        text(s, cx, cy, 2.35, 0.45, v, size=22, bold=True)
        text(s, cx, cy + 0.47, 2.35, 0.45, l, size=10, color=T['text2'])
        kit.tag(s, cx, cy + 0.93, tg)
    text(s, MX, y + 4.0, 4.8, 0.6, '출처: 국가데이터처 2025 인구주택총조사(2026.7), 국토부 2025.12 주택통계, 부동산114. 1,328만호 = 2,018만 × 65.8% (DERIVED)',
         size=8.5, color=T['muted'])
    # classification diagram
    rx = MX + 5.25; rw = W - MX - rx
    colw = (rw - 0.5) / 3
    heads = ['적용환경 변수', 'Kitchen Geometry', 'Robot Architecture']
    lists = [['신축 / 구축', '2Bay / 3Bay / 4Bay', '59 · 74 · 84 · 101㎡+', '천장고 · 벽체 구조'],
             ['일자형', '11자형', 'ㄱ자형', 'ㄷ자형', 'Island / 대면형'],
             ['Rail Type', 'Dock Type', 'Fold-out Type', 'Hybrid Type']]
    for i in range(3):
        cx = rx + i * (colw + 0.25)
        fill = T['soft'] if i == 0 else (T['text'] if i == 1 else T['accent'])
        col = T['text'] if i == 0 else 'FFFFFF'
        chip(s, cx, y, colw, 0.45, heads[i], fill=fill, color=col, size=12)
        for j, it in enumerate(lists[i]):
            yy = y + 0.6 + j * 0.5
            rect(s, cx, yy, colw, 0.42, line=T['line'])
            text(s, cx + 0.12, yy, colw - 0.2, 0.42, it, size=11, anchor='m')
        if i < 2:
            arrow(s, cx + colw + 0.03, y + 0.22, cx + colw + 0.22, y + 0.22, color=T['muted'])
    text(s, rx, y + 3.12, rw, 0.3, 'Product Classification 예시', size=11, bold=True)
    codes = [('REMODEL', '11자형', 'Rail Type A'), ('REMODEL', '59㎡ ㄱ자형', 'Fold-out Type'), ('NEW', 'ㄷ자형', 'Corner Dock + Partial Rail')]
    for j, (a, b_, c) in enumerate(codes):
        yy = y + 3.45 + j * 0.36
        text(s, rx, yy, rw, 0.36, [[(a, {'bold': True, 'color': T['accent']}), ('  +  ', {}), (b_, {'bold': True}), ('  +  ', {}), (c, {'bold': True})]],
             size=12, anchor='m')
    note_line(s, 'Bay는 거실·침실 배치 변수로만 사용. 벽식구조 아파트는 단지 내 동일 평면 Type이 반복 → Template 재사용 근거 (TO BE VALIDATED, 평면 30개 분석으로 확인).',
              y=6.45)
    foot(s, 6)

# ---------------------------------------------------------------- 07 ARKI Kitchen System
def s07(prs):
    s = start(prs, 'system', 7, 'ARKI Kitchen System: Robot과 Kitchen을 하나의 제품체계로 통합', q=[3, 5],
              visual='5개 구성 Card (Robot-ready Kitchen · Robot Module · Kitchen Software · Installation System · Care/Consumables) + 하단 ARKI vs Partner 역할 띠.',
              chart='구성 Card + 역할 분담 띠',
              note=('ARKI의 제품은 다섯 개 층으로 구성됩니다. Robot이 작업하기 쉬운 Kitchen, Robot Module, 주방 Software, 설치 System, 그리고 Care와 소모품입니다. '
                    '중요한 것은 역할 분담입니다. 철거, 가구, 전기, 배관 같은 일반 시공은 Partner가 하고, ARKI는 Product Architecture, Robot, Interface, Software, Calibration, Safety QA를 맡습니다. '
                    '공사업체가 되지 않기 위한 구조를 처음부터 설계에 반영했습니다.'))
    y = head(s, '06  ARKI Kitchen System', 'ARKI Kitchen System: Robot과 Kitchen을 하나의 제품체계로 통합',
             sub='Robot Arm 단품 판매가 아닌 Robot · Kitchen Furniture · Built-in Module · Installation · Software · Rental · Care · Consumables 통합')
    cards = [('Robot-ready Kitchen', 'Robot Mount · Rail Interface · Dock\n전용 전원 · 통신 · Vision 위치\n식세기 상향 Housing\nRobot-friendly Storage · Service Access', ['ASSUMPTION']),
             ('Robot Module', '6축 Arm (가반 3~5kg급)\nLinear Rail · End-effector\nVision · Safety Sensor\nController · Garage Door', ['CONCEPT']),
             ('Kitchen Software', '식기 인식 · Task Planner\n식세기 연동 (Loading / Unloading)\nZone Safety Monitoring\n원격진단 · Update', ['CONCEPT']),
             ('Installation System', 'Layout Classification\nStandard Module 선택\nSite Adjustment\nAuto Calibration · Commissioning', ['CONCEPT']),
             ('Care · Consumables', '정기 안전점검 · Calibration\nRemote Diagnosis · A/S\nGrip · Cleaning · Protection Kit', ['ASSUMPTION'])]
    n = len(cards); gap = 0.18; cw = (CW - gap * (n - 1)) / n
    for i, (t, b, tg) in enumerate(cards):
        card(s, MX + i * (cw + gap), y, cw, 2.75, t, b, tag_kinds=tg, size=10.5, title_size=13, accent_top=(i == 0))
    yb = y + 2.98
    text(s, MX, yb, CW, 0.3, '역할 분담: 공사업체가 되지 않는 구조', size=13, bold=True)
    hw = (CW - 0.3) / 2
    rect(s, MX, yb + 0.42, hw, 1.05, fill=T['text'])
    text(s, MX + 0.2, yb + 0.48, hw - 0.4, 0.3, 'ARKI 담당', size=11, bold=True, color=T['accent'])
    text(s, MX + 0.2, yb + 0.8, hw - 0.4, 0.65, 'Product Architecture · Robot Module · Kitchen Interface · Software · Design Standard · Calibration · Safety QA · Commissioning',
         size=11, color='FFFFFF')
    rect(s, MX + hw + 0.3, yb + 0.42, hw, 1.05, fill=T['soft'])
    text(s, MX + hw + 0.5, yb + 0.48, hw - 0.4, 0.3, 'Partner 담당', size=11, bold=True, color=T['text2'])
    text(s, MX + hw + 0.5, yb + 0.8, hw - 0.4, 0.65, '철거 · 가구 제작/시공 · 전기 · 배관 · 일반 시공  →  장기: Certified Installation Partner',
         size=11)
    note_line(s, 'KPI: Installation 매출 비중이 아닌 Robot · Rental · Care · Consumables 매출 비중이 Installed Base와 함께 증가하는지 (16·19장).', y=6.5)
    foot(s, 7)

# ---------------------------------------------------------------- 08 first product
def s08(prs):
    s = start(prs, 'product', 8, '첫 제품: ARKI Kitchen Assist V1 — Kitchen Clean-up', q=[1, 2],
              visual='상단 6단계 Workflow 띠. 좌하 Approved Task / 초기 제외 / Roadmap(CLEAN→ASSIST→COOK). 우하 Clean-up 선택 기준표 (Clean-up vs Cooking Assist vs Full Cooking).',
              chart='Workflow 띠 + 기준 비교표',
              note=('첫 제품은 완전자율 요리가 아니라 식사 후 정리입니다. 식기를 인식해 집고, 식기세척기에 넣고, 세척이 끝나면 꺼내 수납장에 복귀시키는 흐름입니다. '
                    '조리는 온도와 칼, 비정형 재료 때문에 위험과 난이도가 높습니다. 반면 Clean-up은 매 식사마다 반복되고, 식세기와 수납장이라는 고정된 끝점이 있어 표준화가 쉽습니다. '
                    '여기서 확보한 집기·놓기 Skill은 V2 조리 보조에서 그대로 재사용합니다. V2와 V3는 Future Concept이며 Seed 범위가 아닙니다.'))
    y = head(s, '07  첫 제품', '첫 제품: ARKI Kitchen Assist V1 — Kitchen Clean-up',
             sub='완전자율 Cooking은 Seed 핵심범위에서 제외. 식기 이동 · 식세기 연동 · 수납 복귀 중심 초기 자동화.')
    steps = ['식기 인식', 'Pick', 'Dishwasher\nLoading', '세척 (가전)', 'Dishwasher\nUnloading', 'Storage\nReturn']
    fills = [T['soft']] * 6; fills[3] = T['text']; cols = [T['text']] * 6; cols[3] = 'FFFFFF'
    flow(s, MX, y, CW, steps, h=0.62, gap=0.25, size=11, fills=fills, colors=cols)
    y2 = y + 0.85
    lw = 6.25
    text(s, MX, y2, 3.0, 0.3, 'Approved Task (V1)', size=12, bold=True); kit.tag(s, MX + 1.9, y2 + 0.04, 'TARGET')
    text(s, MX, y2 + 0.35, 3.0, 1.2, ['Dish Handling', 'Dishwasher Loading', 'Dishwasher Unloading', 'Storage Return'],
         size=11, bullet='–', space_after=2)
    text(s, MX + 3.1, y2, 3.1, 0.3, '초기 제외', size=12, bold=True, color=T['text2'])
    text(s, MX + 3.1, y2 + 0.35, 3.1, 1.3, ['Dining Table · Floor', '냉장고 깊은 내부', '고속 칼 작업 · 복합 튀김', '무거운 팬 장거리 이동'],
         size=11, color=T['text2'], bullet='–', space_after=2)
    yr_ = y2 + 1.75
    text(s, MX, yr_, lw, 0.3, 'Roadmap', size=12, bold=True)
    rm = [('CLEAN · V1', '식기 이동 · 식세기 · 수납', T['accent'], 'FFFFFF', 'TARGET'),
          ('ASSIST · V2', '재료 투입 · 저속 젓기 · 뚜껑 · 도구 전달', T['soft'], T['text'], 'FUTURE'),
          ('COOK · V3', '다단계 Cooking Workflow', T['soft'], T['text'], 'FUTURE')]
    bw = (lw - 0.4) / 3
    for i, (a, b_, f, c, tg) in enumerate(rm):
        bx = MX + i * (bw + 0.2)
        rect(s, bx, yr_ + 0.38, bw, 1.1, fill=f)
        text(s, bx + 0.12, yr_ + 0.45, bw - 0.24, 0.3, a, size=12, bold=True, color=c)
        text(s, bx + 0.12, yr_ + 0.78, bw - 0.24, 0.65, b_, size=9.5, color=c)
        kit.tag(s, bx, yr_ + 1.55, tg)
    # criteria table
    rx = MX + lw + 0.35; rw = W - MX - rx
    text(s, rx, y2, rw, 0.3, '왜 Clean-up부터인가  (정성 평가, ASSUMPTION)', size=12, bold=True)
    G, Mi, Bd = '유리', '보통', '불리'
    def c_(v):
        return (v, {'color': T['accent'] if v == G else (T['text2'] if v == Mi else T['muted']), 'bold': v == G})
    rows = [['Task 반복빈도', c_(G), c_(Mi), c_(Mi)], ['기술 난이도', c_(G), c_(Mi), c_(Bd)],
            ['온도 위험', c_(G), c_(Bd), c_(Bd)], ['칼 사용 위험', c_(G), c_(Mi), c_(Bd)],
            ['Task 표준화', c_(G), c_(Mi), c_(Bd)], ['소비자 체감가치', c_(Mi), c_(Mi), c_(G)],
            ['Dishwasher · Storage Integration', c_(G), c_(Bd), c_(Bd)], ['Manipulation Skill 재사용', c_(G), c_(G), c_(Mi)]]
    table(s, rx, y2 + 0.38, rw, ['기준', 'Clean-up', 'Cooking Assist', 'Full Cooking'], rows,
          col_w=[rw - 3.3, 1.0, 1.15, 1.15], size=9.5, align=['l', 'c', 'c', 'c'], label='crit', max_h=3.6)
    note_line(s, '체감가치는 Full Cooking이 가장 높으나 Seed 기간 검증 불가 → 검증 가능한 범위 우선. V2·V3는 FUTURE CONCEPT (Seed 범위 아님).', y=6.62)
    foot(s, 8)

# ---------------------------------------------------------------- 09 placement rules & architecture
def s09(prs):
    s = start(prs, 'architecture', 9, '배치 기준과 Robot Installation Architecture', q=[4],
              visual='좌측 Product Requirement 8개 (번호 목록). 우측 Architecture 4종 Card (적합 Geometry·장단점). 하단 핵심 설계 규칙 Statement (식세기 상향 배치).',
              chart='Card Grid',
              note=('배치의 최우선 요구사항은 거주자 생활동선을 침해하지 않는 것입니다. 바닥 통행영역을 점유하지 않고, 미사용 시 Robot은 Home Position에 들어가 문이 닫힙니다. '
                    'Robot이 고장 나도 주방은 일반 주방으로 쓸 수 있어야 합니다. 설치 방식은 Rail, Dock, Fold-out, Hybrid 네 가지로 나눴습니다. '
                    '가장 중요한 공간 설계 규칙은 식기세척기를 키큰장 안에 허리 높이로 올리는 것입니다. Robot의 Reach가 짧아지고, 사람도 허리를 덜 숙입니다.'))
    y = head(s, '08  주거공간 Robot 배치 기준', '배치 기준과 Robot Installation Architecture',
             sub='핵심 Requirement: 거주자 생활동선 비침해. 초기 Robot Working Zone = Sink · Counter · Dishwasher · Induction · Storage.')
    reqs = ['바닥 통행영역 점유 최소화', 'Robot Working Zone / Human Working Zone 분리', 'Robot Home Position 확보',
            '미사용 시 Fold · Dock · Storage', '상부장 · 벽면 · 키큰장 공간 우선 활용', 'Kitchen 기본기능 유지',
            'Robot 고장 시 일반 Kitchen 사용 가능', 'Service Access 확보']
    lw = 4.6
    text(s, MX, y, lw, 0.3, 'Product Requirement', size=13, bold=True)
    for i, r in enumerate(reqs):
        yy = y + 0.42 + i * 0.47
        text(s, MX, yy, 0.4, 0.4, f'{i + 1:02d}', size=12, bold=True, color=T['accent'], anchor='m')
        text(s, MX + 0.45, yy, lw - 0.45, 0.4, r, size=11.5, anchor='m')
        hline(s, MX, yy + 0.44, lw)
    rx = MX + lw + 0.35; rw = W - MX - rx
    arch = [('Rail Type', '상부장 하단 Linear Rail + 역설치 Arm', '적합: 11자 · 일자형 · 긴 작업대', '장점: 바닥 점유 0 · 긴 작업범위 / 과제: 머리 위 안전 · 상부장 보강'),
            ('Dock Type', '코너·키큰장 고정 Dock', '적합: ㄷ자 · ㄱ자 Corner', '장점: 구조 단순 · 안전 Zone 명확 / 과제: Reach 한계'),
            ('Fold-out Type', '키큰장 내부 수납 후 전개', '적합: 59㎡ Compact', '장점: 미사용 시 완전 은폐 / 과제: 전개 기구 · 수납공간 손실'),
            ('Hybrid Type', 'Partial Rail + Dock', '적합: Island · 대면형 · 신축 Option', '장점: 설계 자유도 / 과제: 부품 수 증가')]
    cw2 = (rw - 0.2) / 2; ch = 1.75
    for i, (t, a, b_, c) in enumerate(arch):
        cx = rx + (i % 2) * (cw2 + 0.2); cy = y + (i // 2) * (ch + 0.18)
        rect(s, cx, cy, cw2, ch, fill=T['soft'])
        rect(s, cx, cy, 0.06, ch, fill=T['accent'])
        text(s, cx + 0.2, cy + 0.12, cw2 - 0.3, 0.32, t, size=13, bold=True)
        text(s, cx + 0.2, cy + 0.48, cw2 - 0.3, 0.3, a, size=10.5, bold=True, color=T['text2'])
        text(s, cx + 0.2, cy + 0.8, cw2 - 0.3, 0.3, b_, size=10, color=T['accent'], bold=True)
        text(s, cx + 0.2, cy + 1.1, cw2 - 0.3, 0.6, c, size=9.5, color=T['text2'])
    statement(s, MX, 6.15, CW, '공간 설계 규칙 #1: 식세기 상향 배치 (키큰장 Housing, Rack 높이 약 450~1,050mm)  →  Robot Reach 단축 + 사람 허리 굽힘 감소 (A6 단면)',
              size=12)
    foot(s, 9)

# ---------------------------------------------------------------- 10 concept layouts
def s10(prs):
    s = start(prs, 'layouts', 10, '대표 Concept Layout: 평형 · Geometry별 Robot Architecture', q=[4],
              visual='2×2 평면도 (Case A~D). 각 평면에 Robot Home·Rail/Dock·Reach·Robot Working Zone·Human Working Zone·No-go Zone과 Sink·DW·Counter·IH·Storage 표시. 상단 범례, CONCEPT LAYOUT 표기.',
              chart='축척 평면 Diagram 4개',
              note=('특정 3Bay 평면만 보여주지 않기 위해 네 가지 대표 사례를 그렸습니다. 실제 단지 도면이 아니라 개념 평면입니다. '
                    'A는 구축 59제곱미터 소형 ㄱ자 주방으로 키큰장 Fold-out, B는 구축 84제곱미터 11자 주방으로 상부장 하단 Rail, '
                    'C는 신축 ㄷ자 주방으로 코너 Dock과 부분 Rail, D는 신축 4Bay 아일랜드 주방으로 벽면 Rail과 Dock입니다. '
                    '공통 원칙은 Robot이 벽면 작업대 쪽에서만 일하고, 통로와 아일랜드는 사람 영역으로 남기는 것입니다.'))
    y = head(s, '09  Concept Layout', '대표 Concept Layout: 평형 · Geometry별 Robot Architecture',
             sub='CONCEPT LAYOUT — 실제 특정 단지 도면 아님. 치수는 업계 통상 치수 기반 개념값 (실측으로 검증).')
    DR.legend(s, MX, y - 0.05, size=8.5)
    kit.tag(s, W - MX - 1.0, y - 0.03, 'CONCEPT')
    cases = [('A', 'Case A · 구축 59㎡ Compact (ㄱ자)', 'Remodeling · Tall Cabinet Fold-out', 'Robot·식세기 키큰장 통합, 미사용 시 완전 수납'),
             ('B', 'Case B · 구축 84㎡ 11자', 'Remodeling · Upper Cabinet Rail', 'Sink 측 작업대 전체 Rail 커버, IH 측은 Human 우선'),
             ('C', 'Case C · 신축 84㎡ ㄷ자', 'Robot-ready Design · Corner Dock + Partial Rail', '코너 Dock 중심 Reach, 출입부 No-go'),
             ('D', 'Case D · 신축 4Bay Island', 'Built-in Rail + Dock', '벽면 Run만 Robot Zone, Island는 Human 전용')]
    gx = (CW - 0.3) / 2; gy = 2.25
    for i, (key, t, a, b_) in enumerate(cases):
        cx = MX + (i % 2) * (gx + 0.3); cy = y + 0.35 + (i // 2) * (gy + 0.15)
        rect(s, cx, cy, gx, gy, line=T['line'])
        DR.plan(s, cx + 0.12, cy + 0.12, 3.0, gy - 0.42, key)
        tx = cx + 3.3; tw = gx - 3.4
        text(s, tx, cy + 0.15, tw, 0.55, t, size=11.5, bold=True)
        text(s, tx, cy + 0.75, tw, 0.5, a, size=10, bold=True, color=T['accent'])
        text(s, tx, cy + 1.3, tw, 0.8, b_, size=9.5, color=T['text2'])
    foot(s, 10, 'DW = 식기세척기 (키큰장 상향 배치) · IH = 인덕션 · Rail = 상부장 하단 (머리 위, 점선)')

# ---------------------------------------------------------------- 11 standardization
def s11(prs):
    a = M['scenarios']['B']
    s = start(prs, 'standard', 11, 'Kitchen Customization의 Productization', q=[4, 5],
              visual='상단 4단계 Flow (Layout Classification → Architecture Selection → Standard Module → Site Adjustment). 좌하 평면 30개 분석계획(표본 구성·분석항목). 우하 KPI TARGET 표 + 원가 연동.',
              chart='Flow + KPI 표',
              note=('투자자가 가장 먼저 물을 질문은 "집마다 다르면 결국 인테리어 회사 아니냐"입니다. 답은 네 단계 분류 체계입니다. '
                    '주방 형태를 분류하고, 설치 방식을 고르고, 표준 모듈을 적용한 뒤, 현장 조정만 남깁니다. '
                    'Seed 기간에 실제 국내 아파트 주방 평면 30개 이상을 신축·구축, 2·3·4Bay, 평형별로 분석해 Template 3~5개로 묶이는지 확인합니다. '
                    '표준 모듈 사용률이 40%에서 80%로 오르면 세대당 Kitchen Module 원가가 약 332만원에서 244만원으로 내려가도록 모델에 연동했습니다. M18에 60% 미만이면 이 Thesis를 재검토합니다.'))
    y = head(s, '10  Standardization', 'Kitchen Customization의 Productization',
             sub='투자자 질문: "집마다 다른데 결국 Custom Interior Business 아닌가?"  →  4단계 분류로 Custom을 Site Adjustment로 축소')
    steps = ['① Kitchen Layout\nClassification', '② Robot Architecture\nSelection', '③ Standard Module\n적용', '④ Site Adjustment\n(현장 조정만)']
    fills = [T['soft'], T['soft'], T['text'], T['accent_soft']]; cols = [T['text'], T['text'], 'FFFFFF', T['text']]
    flow(s, MX, y, CW, steps, h=0.7, gap=0.3, size=12, fills=fills, colors=cols)
    y2 = y + 0.95
    lw = 5.6
    text(s, MX, y2, lw, 0.3, 'Seed 평면 분석: 실제 국내 Apartment Kitchen 30개 이상', size=12, bold=True)
    kit.tag(s, MX, y2 + 0.36, 'TARGET')
    rows = [['표본', '신축 15 · 구축 15 / 2Bay · 3Bay · 4Bay / 59 · 74 · 84 · 101㎡+'],
            ['Geometry', 'Kitchen 형태 · Sink / 식세기 / IH 위치 · 키큰장 · 상부장'],
            ['치수', 'Aisle Width · 천장고 · 상부장 하단 높이 · 벽체 구조'],
            ['Robot', 'Home 후보 위치 · Reach Coverage · 동선 간섭'],
            ['산출', 'Layout Family 3~5개 · Template A/B/C · Coverage %']]
    table(s, MX, y2 + 0.65, lw, None, rows, col_w=[1.05, lw - 1.05], size=10, bold_first_col=True, label='plan30', max_h=2.3)
    rx = MX + lw + 0.35; rw = W - MX - rx
    text(s, rx, y2, rw, 0.3, 'Standardization KPI', size=12, bold=True); kit.tag(s, rx + 2.0, y2 + 0.05, 'TARGET')
    smr = inp('smr')
    krows = [['Kitchen Layout Family · Robot Architecture', '3~5개 · 2~3개'],
             ['Standard Module 사용률', f"{pct(smr[1])} (Y2) → {pct(smr[2])} (Y3) → {pct(smr[4])} (Y5)"],
             ['Design Reuse Ratio · Custom Component Ratio', '70% 이상 · 20% 이하 (M24)'],
             ['Design Lead Time', '5영업일 이하'], ['Installation Time (Robot Module)', '1일 · 2인 이하 (M24)'],
             ['Calibration Time', '2시간 이하 (M24)']]
    table(s, rx, y2 + 0.38, rw, ['KPI', '목표 (M24 / Y5)'], krows, col_w=[3.3, rw - 3.3], size=10, label='kpi', max_h=2.9)
    statement(s, MX, 6.15, CW, f"모델 연동: Standard Module 사용률 40% → 80% 시 Kitchen Module 원가 {B('kit_unit_cost')[0]:.0f} → {B('kit_unit_cost')[4]:.0f}만원/세대 (DERIVED)  |  Kill Criteria: M18 사용률 60% 미만 시 Productization Thesis 재검토",
              size=11.5)
    foot(s, 11)

# ---------------------------------------------------------------- 12 new vs remodel
def s12(prs):
    s = start(prs, 'channels', 12, '구축 = Validation Channel, 신축 = Scale Channel', q=[1, 5],
              visual='상하 2개 Swimlane. 구축 9단계 Flow + 역할(검증 항목), 신축 7단계 Flow + 역할(Scale). 하단 Timing 박스 (신축 계약→입주 2년 Lag, Backlog).',
              chart='Swimlane Flow 2개',
              note=('구축과 신축은 역할이 다릅니다. 구축은 이미 주방 리모델링을 하려는 고객에게 Robot-ready Kitchen을 함께 적용하는 방식입니다. '
                    '고객이 철거와 가구 시공을 어차피 하기 때문에 추가 Integration 비용이 작고, 가격·설치·사용성을 직접 검증할 수 있습니다. '
                    '신축은 건설사 설계 단계에서 Robot-ready Option을 넣는 방식으로 Project 단위 대량 공급이 가능합니다. '
                    '다만 Option 계약에서 입주까지 약 2년이 걸려 5년 재무계획에서 신축 매출은 Y5부터 반영했고, Y5 말 계약 Backlog는 400세대입니다.'))
    y = head(s, '11  신축 / 구축 적용방식', '구축 = Validation Channel, 신축 = Scale Channel',
             sub='구축: Kitchen Remodeling 시점에 적용 (초기 고객·가격·설치성 검증). 신축: 설계 단계부터 Robot-ready Option (B2B2C · Project 단위).')
    lanes = [('구축 Apartment', 'VALIDATION', ['리모델링 상담', '현장 실측', 'Layout 분류', 'Module 선택', 'Robot-ready 설계', '철거·가구 시공\n(Partner)', 'Robot 설치', 'Calibration', 'Safety Check'],
              '역할: 초기 고객 확보 · 가격 검증 · 설치성 검증 · 사용성 검증 · Layout Template 축적 · WTP 검증'),
             ('신축 Apartment', 'SCALE', ['Developer /\n건설사', 'Kitchen Design', 'ARKI Robot-ready\nSpec', 'Kitchen 가구 제작', '현장 설치', '입주: Robot 선택\n(구매 / Rental)', 'Robot-ready 입주 →\n향후 Attach'],
              '역할: 대량 공급 · B2B2C · Project 단위 확장 · Standard Option')]
    yy = y
    for i, (name, badge, steps, role) in enumerate(lanes):
        fill = T['text'] if i == 0 else T['accent']
        rect(s, MX, yy, 1.55, 1.55, fill=fill)
        text(s, MX + 0.1, yy + 0.2, 1.35, 0.6, name, size=12, bold=True, color='FFFFFF')
        text(s, MX + 0.1, yy + 0.95, 1.35, 0.3, badge, size=10, bold=True, color='FFFFFF' if i == 0 else T['text'])
        fx = MX + 1.75; fw = W - MX - fx
        n = len(steps); gap = 0.12; bw = (fw - gap * (n - 1)) / n
        for j, st in enumerate(steps):
            bx = fx + j * (bw + gap)
            f = T['accent_soft'] if ('Partner' in st) else T['soft']
            chip(s, bx, yy, bw, 0.85, st, fill=f, size=9.5 if n > 8 else 10, bold=True)
        text(s, fx, yy + 0.98, fw, 0.5, role, size=10.5, color=T['text2'])
        yy += 1.85
    bx = MX; by = yy + 0.05
    rect(s, bx, by, CW, 1.0, fill=T['soft'])
    proj = inp('projects'); bl = B('backlog')
    text(s, bx + 0.2, by + 0.1, CW - 0.4, 0.85,
         [[('Timing  ', {'bold': True, 'color': T['accent']}),
           (f"신축 Option 계약 → 입주·설치 약 2년 (ASSUMPTION). Base: Y3 {proj[2]}개 · Y4 {proj[3]}개 · Y5 {proj[4]}개 Project 계약 (TARGET) → 5년 내 설치는 Y5 {B('ni')[4]:.0f}세대뿐, Y5 말 Backlog {bl[4]:.0f}세대 (DERIVED).", {})],
          [('시사점  ', {'bold': True, 'color': T['accent']}),
           ('신축은 Scale Channel이지만 매출 인식이 늦음 → Seed·Series A 기간의 매출·검증은 구축 Remodeling이 담당.', {})]],
         size=11, space_after=4, anchor='m')
    foot(s, 12)

# ---------------------------------------------------------------- 13 robot-ready kitchen
def s13(prs):
    kc = B('kit_unit_cost')
    s = start(prs, 'robotready', 13, 'Robot-ready Kitchen: Robot 없이도 판매되는 독립 Product', q=[1, 5],
              visual='좌측 구성요소 11개 (아이콘 없이 2열 목록). 우측 Land & Expand 계단 Diagram (Robot-ready → Robot → Care/Consumables → Skill/Tool/Upgrade). 하단 가격·원가 KPI.',
              chart='Land & Expand 계단 Diagram',
              note=('Robot-ready Kitchen은 Robot을 같이 사지 않아도 판매되는 독립 제품입니다. 구조체에 정착된 Mount, Rail Interface, 전용 전원과 통신, 식세기 상향 Housing, Robot-friendly 수납이 포함됩니다. '
                    '신축에서는 이 Option만 먼저 판매할 수 있고, 입주 후 Robot 구매나 Rental을 붙입니다. Land and Expand 구조입니다. '
                    '구축 증분가는 450만원, 원가는 Y3 기준 277만원으로 가정했고, 신축 유상옵션이 분양가의 평균 9.7% 수준이라는 공개 사례가 참고값입니다.'))
    y = head(s, '12  Robot-ready Kitchen', 'Robot-ready Kitchen: Robot 없이도 판매되는 독립 Product',
             sub='Robot-ready 설치 = 미래 Robot Attach 가능 고객 확보 (Land & Expand)')
    comps = ['Robot Mount (구조체 정착)', 'Rail Interface', 'Dock · Robot Garage', '전용 전원 회로', '통신 (Ethernet / PoE)',
             'Vision 위치', 'Safety Sensor Interface', 'Tool Dock', 'Robot-friendly Storage (표준 Rack)', 'Service Access Panel',
             'Dishwasher Interface (상향 Housing)']
    lw = 5.4
    text(s, MX, y, lw, 0.3, '포함 요소', size=13, bold=True)
    for i, c in enumerate(comps):
        cx = MX + (i % 2) * (lw / 2); cy = y + 0.42 + (i // 2) * 0.5
        rect(s, cx, cy + 0.12, 0.1, 0.1, fill=T['accent'])
        text(s, cx + 0.2, cy, lw / 2 - 0.25, 0.46, c, size=10.5, anchor='m')
    rx = MX + lw + 0.4; rw = W - MX - rx
    text(s, rx, y, rw, 0.3, 'Land & Expand', size=13, bold=True)
    steps = [('LAND', 'Robot-ready Kitchen', '구축 증분 / 신축 Option'), ('EXPAND 1', 'Robot 구매 · Rental', '설치 시점 또는 입주 후'),
             ('EXPAND 2', 'Care · Consumables', '연 단위 반복'), ('EXPAND 3', 'Skill · Tool · Upgrade', 'V2 기능 · End-effector · 교체')]
    sw = (rw - 0.3) / 4
    for i, (a, b_, c) in enumerate(steps):
        sx = rx + i * (sw + 0.1); hgt = 1.0 + i * 0.5; sy = y + 0.42 + (2.5 - hgt)
        rect(s, sx, sy, sw, hgt, fill=T['accent'] if i == 0 else (T['text'] if i == 1 else T['soft']))
        colr = 'FFFFFF' if i < 2 else T['text']
        text(s, sx + 0.1, sy + 0.08, sw - 0.2, 0.25, a, size=9, bold=True, color=colr if i < 2 else T['accent'])
        text(s, sx + 0.1, sy + 0.33, sw - 0.2, 0.55, b_, size=11, bold=True, color=colr)
        text(s, sx + 0.1, y + 3.0, sw - 0.2, 0.5, c, size=9.5, color=T['text2'])
    by = y + 3.65
    ks = [(f"{mann(inp('p_rr'))}만원", '구축 증분가 (고객가)', 'ASSUMPTION'),
          (f"{kc[2]:.0f} → {kc[4]:.0f}만원", 'Kitchen Module 원가 Y3 → Y5', 'DERIVED'),
          (f"{mann(inp('p_rr_new'))}만원", '신축 Option 공급가 (원가 130만원)', 'ASSUMPTION'),
          ('9.7%', '신축 유상옵션 비용 / 분양가 (7개 단지 평균)', 'FACT'),
          (f"{pct(inp('later_attach'))}/년", 'Robot-ready Only 후속 Attach', 'ASSUMPTION')]
    kw = CW / 5
    for i, (v, l, tg) in enumerate(ks):
        kpi(s, MX + i * kw, by, kw - 0.15, v, l, tg, vsize=19, lsize=9.5)
    foot(s, 13)

# ---------------------------------------------------------------- 14 pricing
def s14(prs):
    n = N(); r3, r5, v = n['r3'], n['r5'], n['v']
    bom = inp('bom')
    s = start(prs, 'pricing', 14, '가격 가설: 원가 Floor · 시장 Reference · 가치 Anchor로 Range 설정', q=[2],
              visual='3열 (Cost Floor / Market Reference / Value Anchor) + 하단 가격가설 표 (구매·Rental)와 WTP Test Point, 핵심 Gap Statement.',
              chart='3열 비교 + 가격표',
              note=('가격은 "향후 검증"으로 두지 않고 세 방향에서 범위를 먼저 계산했습니다. 원가 기준으로는 Y3 BOM 1,150만원에서 목표 마진을 붙이면 Robot은 약 1,640만원, Rental은 월 31만원이 하한입니다. '
                    '시장 참고값으로 1X NEO는 2만 달러 또는 월 499달러입니다. 가치 기준으로는 Clean-up 시간 40분, 가사서비스 시간당 1.5만원, 자동화 비중 60%를 가정하면 월 약 18만원입니다. '
                    '즉 가사 대체 가치만으로는 원가 기반 Rental 가격을 정당화하기 어렵습니다. 그래서 Premium 주방 Amenity로서의 가치, V2 Task 확장, BOM 절감이 필요하고, WTP 검증이 Seed의 1순위입니다.'))
    y = head(s, '13  Pricing Hypothesis', '가격 가설: 원가 Floor · 시장 Reference · 가치 Anchor로 Range 설정',
             sub='Range를 먼저 계산하고 소비자 WTP로 검증하는 구조. 가격은 VAT 별도, Kitchen Remodeling 공사비는 별도 (시장가).')
    cw = (CW - 0.4) / 3
    blocks = [
        ('Cost Floor', 'DERIVED', [f"Robot BOM {bom[2]:,}만원 (Y3) / {bom[4]:,}만원 (Y5)",
                                   f"GM 30% 확보 Robot 가격: {bom[2] / 0.7:,.0f} / {bom[4] / 0.7:,.0f}만원",
                                   f"Rental 마진 20% 확보 월 요금: {r3['fee_at_20']:.1f} / {r5['fee_at_20']:.1f}만원",
                                   f"Robot-ready 원가 {B('kit_unit_cost')[2]:.0f}만원 → 증분가 450만원 (GM 약 {1 - B('kit_unit_cost')[2] / 450:.0%})"]),
        ('Market Reference', 'FACT', ['1X NEO: $20,000 또는 월 $499 (2026 출하)', 'Sunday Memo: 양산 시 $10k 미만 목표 (2026 베타)',
                                      'Moley Robotic Kitchen: Arm 포함 £248,000', '신축 유상옵션: 분양가의 평균 9.7%',
                                      '30평대 전체 리모델링 약 3,000만원 (한샘, 2019)']),
        ('Value Anchor', 'DERIVED', [f"Clean-up 40분/일 (ASSUMPTION) × 30일 = {v['hours']:.0f}시간/월",
                                     '가사서비스 1.5만원/h (FACT, 플랫폼 4시간 6만원대)', 'V1 자동화 비중 60% (ASSUMPTION)',
                                     f"→ 월 {v['value']:.0f}만원 (Range {v['lo']:.0f}~{v['hi']:.0f}만원)"])]
    for i, (t, tg, lines) in enumerate(blocks):
        bx = MX + i * (cw + 0.2)
        rect(s, bx, y, cw, 2.35, fill=T['soft'])
        text(s, bx + 0.18, y + 0.12, cw - 0.4, 0.3, t, size=13, bold=True)
        kit.tag(s, bx + cw - 1.1, y + 0.16, tg)
        text(s, bx + 0.18, y + 0.52, cw - 0.36, 1.8, lines, size=10, color=T['text2'], bullet='–', space_after=3)
    y2 = y + 2.55
    rows = [['구매 모델', 'Kitchen 공사비 (시장가, 별도)', f"Robot-ready {mann(inp('p_rr'))} + Robot {mann(inp('p_robot'))} + 설치 {mann(inp('p_comm'))} = ARKI {mann(inp('p_rr') + inp('p_robot') + inp('p_comm'))}만원",
             f"Robot 990 / 1,290 / 1,490 / 1,790만원", ttxt('ASSUMPTION')],
            ['Rental 모델', 'Kitchen 공사비 (시장가, 별도)', f"Robot-ready {mann(inp('p_rr'))} + 설치 {mann(inp('p_comm'))} + 월 {mann(inp('p_rent'))}만원 × 60개월 (Care Basic·Grip Kit 포함)",
             '월 19 / 25 / 29 / 33 / 39만원', ttxt('ASSUMPTION')]]
    table(s, MX, y2, CW, ['모델', '고객 기존 지출', 'ARKI 가격 가설 (Base)', 'WTP Test Point', 'Tag'], rows,
          col_w=[1.15, 2.2, 4.85, 2.6, 1.03], size=10, label='price', max_h=1.4)
    statement(s, MX, 6.05, CW, f"Gap: 가치 Anchor 월 {v['lo']:.0f}~{v['hi']:.0f}만원 < 원가 기반 Rental 월 {r5['fee_at_20']:.0f}~{r3['fee_at_20']:.0f}만원  →  V1 단일 Task의 가사 대체 가치만으로 가격 정당화 어려움. Premium Amenity 가치 · V2 Task 확장 · BOM 절감 필요 → WTP 검증이 Seed 1순위",
              size=11)
    foot(s, 14)

# ---------------------------------------------------------------- 15 household economics
def s15(prs):
    n = N(); h3, h5, r3, r5 = n['hh3'], n['hh5'], n['rt3'], n['rt5']
    s = start(prs, 'household', 15, 'Household Economics: 구축 Premium 1세대가 5년간 만드는 경제적 가치', q=[3, 5],
              visual='좌측: 1세대 5년 매출 vs 비용 Waterfall (가로 막대, Y3 원가). 우측: 구매/Rental × Y3/Y5 원가 비교표. 하단 해석 Statement.',
              chart='Waterfall (매출 항목 → 비용 항목 → Contribution)',
              note=(f"한 세대 기준 경제성입니다. 구축 Premium 주방에 Robot-ready Kitchen과 Robot을 구매로 설치하고 Care에 가입한 세대를 가정했습니다. "
                    f"5년 매출은 약 {h3['rev5']:,.0f}만원이고 이 중 설치 시점 매출이 {h3['y0']:,.0f}만원으로 {h3['y0'] / h3['rev5']:.0%}입니다. "
                    f"Y3 원가 수준에서는 5년 Contribution이 {h3['contrib5']:,.0f}만원으로 마진 {h3['cm5']:.0%}에 그칩니다. Robot BOM이 900만원까지 내려가는 Y5 원가에서는 {h5['contrib5']:,.0f}만원, {h5['cm5']:.0%}입니다. "
                    "따라서 세대 경제성을 결정하는 것은 소모품 수가 아니라 Robot 가격과 BOM입니다. Rental도 비슷한 Contribution을 만들지만 자산을 누가 보유하느냐가 핵심입니다."))
    y = head(s, '14  Household Economics', 'Household Economics: 구축 Premium 1세대가 5년간 만드는 경제적 가치',
             sub='구매 모델 · 직접판매 · Care 가입 세대 기준, Software·Tool은 구매율 반영 기대값 (만원). 모든 값 = ASSUMPTION 기반 DERIVED.')
    R, C = h3['R'], h3['C']
    items = [('Robot-ready 증분', R['kitchen'], 'r'), ('Robot', R['robot'], 'r'), ('설치·Calibration', R['comm'], 'r'),
             ('Care 5년', R['care'], 'r'), ('Consumables 5년', R['cons'], 'r'), ('Upgrade 기대값', R['sw'] + R['tool'], 'r'),
             ('5년 매출', h3['rev5'], 't'),
             ('Robot BOM', -C['robot'], 'c'), ('Kitchen Module', -C['kitchen'], 'c'), ('설치·물류', -(C['comm'] + C['log']), 'c'),
             ('Warranty', -C['warranty'], 'c'), ('Care 원가', -C['care'], 'c'), ('Consumables·Upgrade 원가', -(C['cons'] + C['sw'] + C['tool']), 'c'),
             ('획득비용 (CAC)', -C['channel'], 'c'), ('Contribution', h3['contrib5'], 'res')]
    lw = 6.3; lab_w = 1.95; bar_x = MX + lab_w + 0.1; bar_w = lw - lab_w - 0.75
    scale = bar_w / h3['rev5']; rh = 0.255; cum = 0.0
    text(s, MX, y - 0.02, lw, 0.28, 'Y3 원가 수준 · 구매 · 5년 (만원)', size=11, bold=True)
    for i, (lab, v, kind) in enumerate(items):
        ry = y + 0.32 + i * rh
        text(s, MX, ry, lab_w, rh, lab, size=9, color=T['text'] if kind in ('t', 'res') else T['text2'], align='r', anchor='m',
             bold=kind in ('t', 'res'))
        if kind == 'r':
            x0 = bar_x + cum * scale; rect(s, x0, ry + 0.05, v * scale, rh - 0.1, fill=T['text']); cum += v
        elif kind == 't':
            rect(s, bar_x, ry + 0.05, v * scale, rh - 0.1, fill='5C6169'); cum = v
        elif kind == 'c':
            cum += v; rect(s, bar_x + cum * scale, ry + 0.05, -v * scale, rh - 0.1, fill='C9CDD2')
        else:
            rect(s, bar_x, ry + 0.05, v * scale, rh - 0.1, fill=T['accent'])
        vx = bar_x + max(cum, 0) * scale + (abs(v) * scale if kind == 'c' else 0) + 0.05
        if kind in ('t', 'res'): vx = bar_x + v * scale + 0.05
        if kind == 'r': vx = bar_x + cum * scale + 0.05
        text(s, vx, ry, 0.75, rh, f"{v:,.0f}", size=8.5, bold=kind in ('t', 'res'), color=T['accent'] if kind == 'res' else T['text2'], anchor='m', check=False)
    rx = MX + lw + 0.35; rw = W - MX - rx
    rows = [['Year 0 매출', mann(h3['y0']), mann(h5['y0']), mann(r3['y0']), mann(r5['y0'])],
            ['5년 매출', mann(h3['rev5']), mann(h5['rev5']), mann(r3['rev5']), mann(r5['rev5'])],
            ['Recurring 매출 (5년)', mann(h3['recurring5']), mann(h5['recurring5']), mann(r3['R']['rental'] + r3['R']['cons']), mann(r5['R']['rental'] + r5['R']['cons'])],
            ['5년 매출총이익', mann(h3['gp5']), mann(h5['gp5']), mann(r3['gp5']), mann(r5['gp5'])],
            [('Lifetime Contribution', {'bold': True}), (mann(h3['contrib5']), {'bold': True}), (mann(h5['contrib5']), {'bold': True, 'color': T['accent']}),
             (mann(r3['contrib5']), {'bold': True}), (mann(r5['contrib5']), {'bold': True, 'color': T['accent']})],
            ['Contribution Margin', pct(h3['cm5'], 1), pct(h5['cm5'], 1), pct(r3['cm5'], 1), pct(r5['cm5'], 1)],
            ['Robot BOM 가정', mann(h3['bom']), mann(h5['bom']), mann(r3['bom']), mann(r5['bom'])]]
    table(s, rx, y + 0.3, rw, ['만원', '구매 Y3', '구매 Y5', 'Rental Y3', 'Rental Y5'], rows,
          col_w=[rw - 3.6, 0.9, 0.9, 0.9, 0.9], size=10, align=['l', 'r', 'r', 'r', 'r'], label='hh', max_h=3.2)
    text(s, rx, y + 3.45, rw, 0.9, ['Rental: Robot 자산 잔존가치 15% 회수, 금융비용 8% 반영 (ARKI 보유 가정)',
                                    'Partner 경유 시 Contribution 약 50만원 감소 (수수료 10%)'],
         size=9.5, color=T['text2'], bullet='–', space_after=2)
    statement(s, MX, 6.1, CW, f"세대 가치의 {h3['y0'] / h3['rev5']:.0%}는 설치 시점 매출 → 세대 경제성 = Robot ASP(WTP) × BOM이 결정. Recurring은 5년 {h3['recurring5']:,.0f}만원으로 보완 역할, 핵심 Value Driver 아님",
              size=11.5)
    foot(s, 15)

# ---------------------------------------------------------------- 16 business model & timeline
def s16(prs):
    a = {d['key']: d['vals']['B'] for d in M['inputs']}
    cons = M['cons']['rev']
    s = start(prs, 'bm', 16, 'Business Model: 설치 매출 → 반복 매출 → 확장 매출', q=[3, 5],
              visual='상단 3단 BM 블록 (A 초기 설치 / B 반복 / C 확장, 가격 가설 포함). 하단 1세대 Revenue Timeline (YEAR 0 ~ YEAR 4+) 막대 + Rental 3자 구조 Diagram.',
              chart='3단 BM + Revenue Timeline 막대',
              note=('수익모델은 세 단계입니다. 설치 시점에 Robot-ready Kitchen과 Robot Hardware 매출이 발생하고, 설치기반이 쌓이면서 Rental, Care, 소모품 같은 반복매출이 생깁니다. '
                    '이후 Software 기능, Tool, Robot 교체 같은 확장매출이 붙습니다. 한 세대 기준으로 설치 첫해 2,020만원, 이후 매년 약 73만원에서 93만원입니다. '
                    'Rental은 ARKI가 자산을 계속 보유하지 않도록 Scale 단계에서 렌탈·캐피탈 Partner가 자산 금융을 맡고, ARKI는 제품·Software·Care를 맡습니다.'))
    y = head(s, '15  Business Model', 'Business Model: 설치 매출 → 반복 매출 → 확장 매출',
             sub='핵심 Revenue Logic: 설치기반(Installed Base) 증가 → Recurring Revenue Base 증가. 모든 가격 = ASSUMPTION.')
    tiers = [('A. 초기 설치 매출', T['text'], 'FFFFFF', [f"Robot-ready Kitchen Build  {a['p_rr']}만원", f"Robot Hardware  {a['p_robot']:,}만원",
                                                   f"설치·Calibration  {a['p_comm']}만원"]),
             ('B. 반복 매출', T['accent'], 'FFFFFF', [f"Robot Rental  월 {a['p_rent']}만원 (60개월)", f"Care Basic  연 {a['p_care']}만원 (Plus 72만원)",
                                                 f"Consumables  연 {M['cons']['list_y']:.0f}만원 List (구매율 70%)"]),
             ('C. 확장 매출', T['soft'], T['text'], [f"Software Skill  {a['p_sw']}만원 (V2)", f"End-effector · Tool  {a['p_tool']}만원",
                                                  'Robot Upgrade · Replacement (5~7년)'])]
    tw = (CW - 0.4) / 3
    for i, (t, f, c, lines) in enumerate(tiers):
        bx = MX + i * (tw + 0.2)
        rect(s, bx, y, tw, 1.38, fill=f)
        text(s, bx + 0.18, y + 0.1, tw - 0.36, 0.3, t, size=13, bold=True, color=c)
        text(s, bx + 0.18, y + 0.45, tw - 0.36, 0.9, lines, size=10.5, color=c, bullet='–', space_after=1,
             bullet_color=c)
    y2 = y + 1.6
    text(s, MX, y2, 7.2, 0.3, 'Revenue Timeline — 구매 고객 1세대 (만원, 기대값)', size=12, bold=True)
    care = a['p_care']; yrs = [('YEAR 0', 'Kitchen · Robot 구매\n(또는 Rental Start)', a['p_rr'] + a['p_robot'] + a['p_comm']),
                              ('YEAR 1', 'Care · Consumables', care + cons),
                              ('YEAR 2', '+ Software Function', care + cons + a['sw_attach'] * a['p_sw']),
                              ('YEAR 3', '+ End-effector Upgrade', care + cons + a['tool_attach'] * a['p_tool']),
                              ('YEAR 4+', 'Robot Upgrade\nAdditional Tool · Skill', None)]
    bw = 1.3; base_y = y2 + 2.2; maxh = 1.55
    for i, (yl, d, v) in enumerate(yrs):
        bx = MX + i * (bw + 0.15)
        if v is not None:
            hh = maxh if i == 0 else max(0.12, maxh * v / 2020 * 6)
            rect(s, bx + 0.25, base_y - hh, bw - 0.5, hh, fill=T['text'] if i == 0 else T['accent'])
            text(s, bx, base_y - hh - 0.27, bw, 0.25, f"{v:,.0f}", size=10, bold=True, align='c', check=False)
        else:
            dashed_rect(s, bx + 0.25, base_y - 0.6, bw - 0.5, 0.6)
            text(s, bx, base_y - 0.87, bw, 0.25, '옵션', size=10, bold=True, align='c', color=T['muted'], check=False)
        text(s, bx, base_y + 0.05, bw, 0.25, yl, size=10, bold=True, align='c')
        text(s, bx, base_y + 0.3, bw, 0.45, d, size=8.5, color=T['text2'], align='c')
    text(s, MX, base_y + 0.8, 7.0, 0.36, 'YEAR 1~3 막대는 6배 확대 표시 (Year 0 대비 소액). YEAR 1~3 = Care 48 + Consumables 25.2 (+ 기대값). Robot Upgrade는 Base 재무 미반영.',
         size=8.5, color=T['muted'])
    rx = MX + 7.4; rw = W - MX - rx
    text(s, rx, y2, rw, 0.3, 'Rental 구조 (Scale 단계)', size=12, bold=True)
    nodes = [('ARKI', 'Product · Software · Care'), ('Rental / Capital Partner', 'Asset Financing (Robot 자산 보유)'), ('Customer', 'Monthly Payment')]
    for i, (t, d) in enumerate(nodes):
        ny = y2 + 0.4 + i * 0.86
        rect(s, rx, ny, rw, 0.64, fill=T['accent'] if i == 0 else T['soft'])
        text(s, rx + 0.18, ny + 0.04, rw - 0.36, 0.3, t, size=11.5, bold=True, color='FFFFFF' if i == 0 else T['text'])
        text(s, rx + 0.18, ny + 0.33, rw - 0.36, 0.28, d, size=9.5, color='FFFFFF' if i == 0 else T['text2'])
        if i < 2: arrow(s, rx + rw / 2, ny + 0.66, rx + rw / 2, ny + 0.84, color=T['muted'])
    text(s, rx, y2 + 3.0, rw, 0.6, f"Seed: ARKI 직접 Rental Pilot → Y4부터 Partner가 Robot을 ASP의 {pct(a['wholesale'])}에 매입, ARKI는 월 {a['partner_fee']:.0f}만원 Care·Grip 서비스료 (ASSUMPTION)",
         size=9.5, color=T['text2'])
    foot(s, 16)

# ---------------------------------------------------------------- 17 unit economics
def s17(prs):
    n = N(); r3, r5, c3, c5 = n['r3'], n['r5'], n['c3'], n['c5']
    h3 = M['household']['purchase_direct_Y3']; h5 = M['household']['purchase_direct_Y5']
    cons = M['cons']
    sc = M['sens_company']
    s = start(prs, 'unit', 17, 'Unit Economics: BOM과 Route Density가 Margin 결정', q=[3, 5],
              visual='4개 Unit Card (PURCHASE · RENTAL · CARE · CONSUMABLES) 각각 Y3/Y5 Contribution. 우측 Sensitivity Top 3 가로막대 (Y5 Contribution 영향).',
              chart='Unit Card 4개 + Tornado Top 3',
              note=('단위 경제성을 네 가지로 나눴습니다. 구매 모델의 설치 시점 Contribution은 Y3에 약 300만원, Y5에 600만원입니다. '
                    f"Rental은 월 33만원 기준 Y3 원가에서 Payback이 {r3['payback']:.0f}개월로 Rental Partner가 보통 요구하는 36개월을 넘습니다. BOM이 {r3['bom_max']:,.0f}만원 이하로 내려가야 Partner 구조가 성립합니다. "
                    f"Care는 Y3에 마진 {c3['margin']:.0%}로 Profit Center가 아니고, 방문 원가가 내려가는 Y5에 {c5['margin']:.0%}가 됩니다. "
                    '사업가치에 가장 큰 영향을 주는 변수는 고객 지불의사, Robot BOM, Partner 경유 물량 순서입니다.'))
    y = head(s, '16  Unit Economics', 'Unit Economics: BOM과 Route Density가 Margin 결정',
             sub='Base 가정. Y3 = Series A 직후 원가 수준, Y5 = 물량·표준화 반영 원가 수준 (만원). 모든 값 DERIVED (from ASSUMPTION).')
    y0c3 = h3['y0'] - (h3['C']['robot'] + h3['C']['kitchen'] + h3['C']['comm'] + h3['C']['log'] + h3['C']['warranty'] + h3['C']['channel'])
    y0c5 = h5['y0'] - (h5['C']['robot'] + h5['C']['kitchen'] + h5['C']['comm'] + h5['C']['log'] + h5['C']['warranty'] + h5['C']['channel'])
    cards = [('PURCHASE', '설치 시점 (Year 0)', [('고객가', f"{h3['y0']:,.0f}", f"{h5['y0']:,.0f}"), ('원가 (BOM·Module·설치·CAC 등)', f"−{h3['y0'] - y0c3:,.0f}", f"−{h5['y0'] - y0c5:,.0f}"),
                                             ('Contribution', f"{y0c3:,.0f}", f"{y0c5:,.0f}"), ('Margin', pct(y0c3 / h3['y0']), pct(y0c5 / h5['y0']))]),
             ('RENTAL', 'Robot 1대 · 월', [('월 요금', f"{r3['fee']:.1f}", f"{r5['fee']:.1f}"), ('감가·금융·Care·Grip·Reserve', f"−{r3['cost_m']:.1f}", f"−{r5['cost_m']:.1f}"),
                                          ('월 Contribution', f"{r3['contrib_m']:.1f}", f"{r5['contrib_m']:.1f}"), ('Payback (개월)', f"{r3['payback']:.0f}", f"{r5['payback']:.0f}")]),
             ('CARE', 'Robot 1대 · 년', [('Care Basic 요금', f"{c3['fee']:.0f}", f"{c5['fee']:.0f}"), ('방문·고장·Cloud 원가', f"−{c3['cost']:.1f}", f"−{c5['cost']:.1f}"),
                                       ('Contribution', f"{c3['contrib']:.1f}", f"{c5['contrib']:.1f}"), ('Margin', pct(c3['margin']), pct(c5['margin']))]),
             ('CONSUMABLES', 'Robot 1대 · 년', [('매출 (List × 70%)', f"{cons['rev']:.1f}", f"{cons['rev']:.1f}"), ('원가 (35%)', f"−{cons['cogs']:.1f}", f"−{cons['cogs']:.1f}"),
                                               ('Contribution', f"{cons['contrib']:.1f}", f"{cons['contrib']:.1f}"), ('Margin', pct(cons['margin']), pct(cons['margin']))])]
    lw = 7.9; cw = (lw - 0.2) / 2; ch = 1.92
    for i, (t, sub, rows) in enumerate(cards):
        cx = MX + (i % 2) * (cw + 0.2); cy = y + (i // 2) * (ch + 0.15)
        rect(s, cx, cy, cw, ch, fill=T['soft'])
        text(s, cx + 0.15, cy + 0.1, 1.8, 0.3, t, size=12, bold=True, color=T['accent'])
        text(s, cx + 1.85, cy + 0.12, cw - 2.0, 0.3, sub, size=9.5, color=T['text2'])
        text(s, cx + cw - 1.55, cy + 0.42, 0.7, 0.22, 'Y3', size=9, bold=True, color=T['muted'], align='r')
        text(s, cx + cw - 0.8, cy + 0.42, 0.65, 0.22, 'Y5', size=9, bold=True, color=T['muted'], align='r')
        for j, (lab, v3, v5) in enumerate(rows):
            ry = cy + 0.68 + j * 0.3
            bold = j == 2
            text(s, cx + 0.15, ry, cw - 1.75, 0.28, lab, size=9.5, bold=bold, anchor='m')
            text(s, cx + cw - 1.55, ry, 0.7, 0.28, v3, size=10, bold=bold, align='r', anchor='m')
            text(s, cx + cw - 0.8, ry, 0.65, 0.28, v5, size=10, bold=bold, align='r', anchor='m', color=T['accent'] if bold else T['text'])
    rx = MX + lw + 0.35; rw = W - MX - rx
    text(s, rx, y, rw, 0.3, 'Sensitivity Top 3 (Y5 Contribution)', size=12, bold=True)
    text(s, rx, y + 0.32, rw, 0.3, f"Base Y5 Contribution {eok(sc['base'])} · 불리 ↔ 유리 변화 (억원)", size=9.5, color=T['text2'])
    top = sc['items'][:3]; mx = max(max(abs(d['lo']), abs(d['hi'])) for d in top)
    cxm = rx + rw / 2; half = rw / 2 - 0.55
    for i, d in enumerate(top):
        ry = y + 0.8 + i * 1.0
        text(s, rx, ry, rw, 0.28, d['name'], size=10, bold=True)
        wl = abs(d['lo']) / mx * half; wh = abs(d['hi']) / mx * half
        rect(s, cxm - wl, ry + 0.34, wl, 0.3, fill='8C9198'); rect(s, cxm, ry + 0.34, wh, 0.3, fill=T['accent'])
        text(s, cxm - wl - 0.55, ry + 0.34, 0.52, 0.3, f"{d['lo'] / 10000:,.1f}", size=9, align='r', anchor='m', check=False)
        text(s, cxm + wh + 0.03, ry + 0.34, 0.6, 0.3, f"+{d['hi'] / 10000:,.1f}", size=9, anchor='m', check=False)
    vline(s, cxm, y + 1.05, 2.75, color=T['text'])
    text(s, rx, y + 3.85, rw, 0.4, '전체 10개 변수: A15. 신축 Option 선택률은 5년 내 영향 작음 (설치 Lag).', size=9, color=T['muted'])
    statement(s, MX, 6.15, CW, f"Rental Partner 구조 성립 조건 (DERIVED): Payback ≤ 36개월 → Robot BOM ≤ 약 {r3['bom_max']:,.0f}만원  |  Care Profit Center 조건: 방문원가 9만원 이하 + 원격진단으로 연 1.5회 이하 방문",
              size=11)
    foot(s, 17)

# ---------------------------------------------------------------- 18 market & beachhead
def s18(prs):
    mk = M['market']['B']
    s = start(prs, 'market', 18, 'Market: Premium · 적용가능 세대부터 Bottom-up', q=[1],
              visual='좌측 구축 Funnel (아파트 → Kitchen 교체 → Premium → 적용 가능 → SAM). 중앙 신축 Funnel. 우측 TAM/SAM/SOM 요약 + Beachhead 순서.',
              chart='Funnel 2개 + TAM/SAM/SOM 블록',
              note=('시장은 Top-down TAM이 아니라 세대 수부터 쌓았습니다. 아파트 약 1,328만호 중 연간 주방 교체 세대를 두 가지 방법으로 교차 추정하면 29만에서 30만 세대입니다. '
                    '이 중 Premium 10%, 그중 Robot-ready 적용 가능 60%를 가정하면 연 1.8만 세대, 금액으로 약 3,200억원이 구축 SAM입니다. '
                    '신축은 연 20만 세대 입주 중 Premium 단지 15%, Option 선택 10%로 연 3천 세대입니다. '
                    f"Base 계획의 Y5 매출 {mk['som']:.0f}억원은 SAM 세대의 약 2%입니다. Mass Market 진입은 가정하지 않았습니다."))
    y = head(s, '17  Market Sizing · Beachhead', 'Market: Premium · 적용가능 세대부터 Bottom-up',
             sub='과도한 TAM 배제. 세대 수 × 적용률 × 단가. 핵심 비율(Premium 10% · 적용 60% · Option 10%)은 ASSUMPTION → Seed 기간 검증.')
    def funnel(x, w, title, rows):
        text(s, x, y, w, 0.3, title, size=12, bold=True)
        for i, (v, lab, tg) in enumerate(rows):
            fy = y + 0.42 + i * 0.78
            ww = w * (1 - i * 0.06)
            last = i == len(rows) - 1
            rect(s, x, fy, ww, 0.68, fill=T['text'] if last else (T['soft'] if i % 2 == 0 else 'ECEDEF'))
            col = 'FFFFFF' if last else T['text']
            text(s, x + 0.12, fy + 0.03, ww - 1.2, 0.35, v, size=14, bold=True, color=col)
            text(s, x + 0.12, fy + 0.37, ww - 0.24, 0.28, lab, size=9, color=col if last else T['text2'])
            kit.tag(s, x + ww - 1.0, fy + 0.08, tg, size=7, h=0.18)
    fw = 3.85
    funnel(MX, fw, '구축 (연간)', [(f"{mk['apt'] / 100:,.0f}만호", '아파트 (2,018만 × 65.8%)', 'DERIVED'),
                                (f"{mk['rep'] / 10:,.0f}만 세대/년", f"Kitchen 교체 (교차검증 {mk['tri1'] / 10:.1f}·{mk['tri2'] / 10:.1f}만)", 'ASSUMPTION'),
                                (f"{mk['prem'] / 10:,.0f}만 세대", 'Premium 10%', 'ASSUMPTION'),
                                (f"{mk['fit'] / 10:,.1f}만 세대", 'Robot-ready 적용 가능 60%', 'ASSUMPTION'),
                                (f"{mk['sam_remodel']:,.0f}억원/년", f"구축 SAM · 단가 {mk['pkg_remodel']:,.0f}만원", 'DERIVED')])
    funnel(MX + fw + 0.3, fw, '신축 (연간)', [(f"{inp('a_new_supply') / 10:,.0f}만 세대/년", '아파트 입주 (23.6만·18.3만 평균)', 'DERIVED'),
                                            (f"{mk['new_prem'] / 10:,.0f}만 세대", 'Premium 단지 15%', 'ASSUMPTION'),
                                            (f"{mk['new_opt'] * 1000:,.0f}세대", 'Robot-ready Option 10%', 'ASSUMPTION'),
                                            (f"{mk['sam_new']:,.0f}억원/년", f"신축 SAM · 단가 {mk['pkg_new']:,.0f}만원", 'DERIVED')])
    rx = MX + 2 * fw + 0.6; rw = W - MX - rx
    blocks = [('TAM', f"{mk['tam'] / 10000:,.2f}조원/년", 'Premium 세대 (구축 3만 + 신축 3만) × 전체 패키지 2,020만원', 'DERIVED'),
              ('SAM', f"{mk['sam']:,.0f}억원/년", '적용 가능 · Option 선택 세대 × 기대 단가', 'DERIVED'),
              ('SOM', f"{mk['som']:,.0f}억원 (Y5)", f"Base Plan Y5 매출 · SAM 세대의 {mk['som_share_hh'] * 100:.1f}%", 'TARGET')]
    for i, (t, v, d, tg) in enumerate(blocks):
        by = y + i * 1.12
        rect(s, rx, by, rw, 1.0, fill=T['accent'] if i == 2 else T['soft'])
        c = 'FFFFFF' if i == 2 else T['text']
        text(s, rx + 0.15, by + 0.08, 0.7, 0.3, t, size=11, bold=True, color=c)
        text(s, rx + 0.85, by + 0.04, rw - 0.95, 0.4, v, size=16, bold=True, color=c)
        text(s, rx + 0.15, by + 0.5, rw - 0.3, 0.45, d, size=8.5, color=c if i == 2 else T['text2'])
    by = y + 3.45
    text(s, rx, by, rw, 0.3, 'Beachhead 순서', size=11, bold=True)
    text(s, rx, by + 0.32, rw, 1.2, ['① 구축 Premium Kitchen Remodeling', '② High-end 신축 Option', '③ Kitchen Furniture Partnership',
                                      '④ 건설사 Standard Option'], size=10, space_after=2)
    note_line(s, 'Recurring Pool (DERIVED): Installed Robot 1만 대당 Care·Consumables 연 약 69억원 (대당 연 69만원, 구매 60% · Rental 40% 가중). Mass Market 초기 진입 주장 없음.', y=6.5)
    foot(s, 18)

# ---------------------------------------------------------------- 19 GTM & revenue mix
def s19(prs):
    s = start(prs, 'gtm', 19, 'GTM: Direct는 학습, Scale은 Partner Distribution', q=[1, 5],
              visual='상단 Stage 1~5 계단 (시기·채널·Base 물량). 좌하 Revenue Mix 100% 누적 막대 (Y2~Y5 + 정상상태 DERIVED). 우하 KPI: Build 비중↓ / Robot+Recurring↑.',
              chart='Stage 계단 + 100% Stacked Column',
              note=('직접판매는 고객 학습과 제품 검증 목적입니다. Y2에 5세대 Home Pilot으로 시작하고, Y3부터 주방가구·인테리어 Partner를 통해 물량을 늘립니다. '
                    'Base에서 Y5 Partner 경유 Kitchen은 340세대로 직접판매 60세대의 5배 이상입니다. 신축은 Y3 계약, Y5 설치입니다. '
                    f"매출 구성에서 Kitchen Build와 설치 매출 비중은 Y5에 약 {B('build')[4] / B('rev')[4]:.0%}이고, 나머지는 Robot과 반복매출입니다. Interior 회사가 아니라 Robotics Product 회사로 가는지 보는 KPI입니다."))
    y = head(s, '18  GTM · Partner Distribution', 'GTM: Direct는 학습, Scale은 Partner Distribution',
             sub='초기 직접판매 = 고객학습 · Product Validation. Scale = Kitchen Furniture · Interior Partner · Construction Company · Certified Installer.')
    rd, rp, ni = inp('rd'), inp('rp'), B('ni')
    stages = [('Stage 1', 'Premium Remodeling\nDirect Pilot', f"Y2 {rd[1]}세대 → Y5 {rd[4]}세대"),
              ('Stage 2', 'Interior · Kitchen\nPartner', f"Y3 {rp[2]} → Y5 {rp[4]}세대"),
              ('Stage 3', 'Construction\nCompany', f"Y3 계약 → Y5 {ni[4]:.0f}세대 설치"),
              ('Stage 4', 'Certified Installation\nPartner', 'Y4~ 교육·인증'),
              ('Stage 5', 'Robot-ready Kitchen\nStandard', 'Y6~ (Series B 이후)')]
    sw = (CW - 0.4) / 5
    for i, (a, b_, c) in enumerate(stages):
        sx = MX + i * (sw + 0.1); sy = y + (4 - i) * 0.22
        f = T['text'] if i == 0 else (T['accent'] if i in (1, 2) else T['soft'])
        col = 'FFFFFF' if i < 3 else T['text']
        rect(s, sx, sy, sw, 1.55 - (4 - i) * 0.22 + 0.4, fill=f)
        text(s, sx + 0.12, sy + 0.08, sw - 0.24, 0.25, a, size=9, bold=True, color=col)
        text(s, sx + 0.12, sy + 0.32, sw - 0.24, 0.55, b_, size=11, bold=True, color=col)
        text(s, sx + 0.12, sy + 0.9, sw - 0.24, 0.3, c, size=9.5, color=col)
    y2 = y + 2.05
    text(s, MX, y2, 7.0, 0.3, 'Revenue Mix Evolution (Base, %)', size=12, bold=True)
    L = M['scenarios']['B']
    cats = ['Y2', 'Y3', 'Y4', 'Y5', '정상상태*']
    def sh(t, k): return L[k][t] / L['rev'][t] * 100 if L['rev'][t] else 0
    build = [sh(t, 'build') for t in (1, 2, 3, 4)]; robot = [sh(t, 'rev_robot') for t in (1, 2, 3, 4)]
    rec = [sh(t, 'recurring') for t in (1, 2, 3, 4)]; upg = [sh(t, 'rev_upg') for t in (1, 2, 3, 4)]
    st = M['steady']; tot = st['y0'] + 6 * st['arpu'] + 6 * st['upg']
    sb = (inp('p_rr') / 0.85 + inp('p_comm')) / tot * 100; sr = (st['y0'] - inp('p_rr') / 0.85 - inp('p_comm')) / tot * 100
    build.append(sb); robot.append(sr); rec.append(st['rec_share'] * 100); upg.append(st['upg_share'] * 100)
    column_chart(s, MX, y2 + 0.3, 6.9, 2.1, cats, [('Build', build), ('Robot', robot), ('Recurring', rec), ('Upgrade', upg)],
                 ['C9CDD2', '15171A', 'E2571B', 'F6C9B3'], stacked=True, vmax=100, fmt='0', label_colors=['15171A', 'FFFFFF', 'FFFFFF', '15171A'],
                 gap=55, size=9, legend=True, plot=(0.02, 0.12, 0.96, 0.76))
    text(s, MX, y2 + 2.72, 6.9, 0.3, '* 정상상태 (DERIVED): Installed Base = 연간 설치 × 6, Robot 교체주기 6.5년 · 교체율 30% 가정. Base 재무 5년 범위 밖.',
         size=8.5, color=T['muted'])
    rx = MX + 7.3; rw = W - MX - rx
    rect(s, rx, y2, rw, 3.05, fill=T['soft'])
    text(s, rx + 0.2, y2 + 0.15, rw - 0.4, 0.3, '공사업체가 되는 Risk 관리 KPI', size=12, bold=True)
    rows = [['Build 매출 비중', pct(L['build'][2] / L['rev'][2]), pct(L['build'][4] / L['rev'][4])],
            ['Robot + Recurring + Upgrade', pct(L['robot_recurring_share'][2]), pct(L['robot_recurring_share'][4])],
            ['Partner 경유 Kitchen 비중', pct(rp[2] / L['kitchens'][2]), pct(rp[4] / L['kitchens'][4])],
            ['Installed Robot (기말)', f"{L['base_end'][2]:.0f}대", f"{L['base_end'][4]:.0f}대"]]
    table(s, rx + 0.2, y2 + 0.55, rw - 0.4, ['KPI (Base)', 'Y3', 'Y5'], rows, col_w=[rw - 2.2, 0.9, 0.9], size=10,
          align=['l', 'r', 'r'], label='gtmkpi', max_h=2.0)
    text(s, rx + 0.2, y2 + 2.3, rw - 0.4, 0.7, '목표: Interior Company가 아닌 Robotics Product Company. 철거·가구·전기·배관은 Partner, ARKI는 Module·Calibration·Safety QA·Commissioning.',
         size=9.5, color=T['text2'])
    foot(s, 19)

# ---------------------------------------------------------------- 20 competition
def s20(prs):
    s = start(prs, 'competition', 20, '경쟁 구도: 모든 Player와 경쟁하지 않는 Integration Layer', q=[4, 5],
              visual='좌측 Category 경쟁표 (5행: 대표 사례·현재 상태·ARKI 차이). 우측 "대기업이 직접 하면?" 4개 Player별 관계 Diagram + ARKI Core.',
              chart='경쟁표 + 관계 Diagram',
              note=('경쟁은 Category로 봅니다. 가전사는 가전 내부를 자동화하고, 조리 Robot은 조리에 집중하며, Humanoid는 범용 이동형으로 접근합니다. '
                    '1X NEO는 2만 달러 또는 월 499달러에 2026년 출하를 발표했고, LG는 CES 2026에서 식세기를 비우는 CLOiD를 시연했습니다. 이 영역은 이미 큰 회사들이 움직이고 있습니다. '
                    'ARKI는 범용 Robot과 정면 경쟁하지 않고, 주방 공간과 Robot을 묶는 Integration Layer를 맡습니다. '
                    '삼성·LG는 기기 Interface Partner, 가구사는 Module과 Channel Partner, 건설사는 유통, Robot OEM은 공급사로 봅니다. 다만 대기업이 같은 Layer를 직접 할 위험은 남아 있습니다.'))
    y = head(s, '19  Competition', '경쟁 구도: 모든 Player와 경쟁하지 않는 Integration Layer',
             sub='Category 기준 비교. 사례는 공개 보도 기준 (FACT, A9 상세). 과장 금지: ARKI 우위는 현재 미검증.')
    rows = [['Kitchen Appliance', '식세기 · 인덕션 · 빌트인 가전', '가전 내부 공정 자동화', '가전 사이 이동 · 수납 담당'],
            ['Dedicated Cooking Robot', 'Moley (£248k, 천장 Rail 양팔) · Posha ($1,750)', '조리 특화 · 고가 또는 Countertop', 'Clean-up 우선 · 공동주택 Built-in'],
            ['Humanoid / Mobile', '1X NEO ($20k · 월 $499) · Sunday Memo (2026 베타) · LG CLOiD (CES 2026)', '범용 · 이동형 · 대규모 자본', '고정 Rail·Dock으로 Task 조건 고정 · 바닥 점유 0'],
            ['Industrial / Cobot Integration', 'UR · Doosan · Rainbow 등 + SI', '산업·상업 주방 검증된 Arm', '주거 공간·가구 Interface 표준'],
            ['Built-in Robotic Kitchen', 'Moley · Samsung Bot Chef (CES 2020 Concept)', '공간 일체형 시도 존재', '한국 공동주택 Template · 설치 Standard']]
    lw = 7.55
    table(s, MX, y, lw, ['Category', '대표 사례', '현재 접근', 'ARKI 차이 (가설)'], rows, col_w=[1.6, 2.55, 1.55, 1.85], size=9.5,
          label='comp', max_h=4.2)
    rx = MX + lw + 0.35; rw = W - MX - rx
    text(s, rx, y, rw, 0.3, '대기업이 직접 하면?', size=13, bold=True)
    rel = [('Samsung · LG (Appliance)', 'Device Interface Partner', '식세기 Door·Rack 연동 API'),
           ('Kitchen Furniture 기업', 'Module · Channel Partner', 'Robot-ready Module 공급'),
           ('Construction Company', 'Distribution', 'Robot-ready Option Spec'),
           ('Robot OEM', 'Supplier / Partner', 'Arm · Actuator 공급')]
    for i, (a, b_, c) in enumerate(rel):
        ry = y + 0.42 + i * 0.72
        rect(s, rx, ry, rw, 0.62, fill=T['soft'])
        text(s, rx + 0.12, ry + 0.04, rw * 0.55, 0.3, a, size=10, bold=True)
        text(s, rx + 0.12, ry + 0.32, rw * 0.55, 0.28, c, size=9, color=T['text2'])
        text(s, rx + rw * 0.57, ry, rw * 0.42, 0.62, b_, size=10.5, bold=True, color=T['accent'], anchor='m')
    cy = y + 3.4
    rect(s, rx, cy, rw, 1.12, fill=T['text'])
    text(s, rx + 0.15, cy + 0.08, rw - 0.3, 0.28, 'ARKI Core', size=11, bold=True, color=T['accent'])
    text(s, rx + 0.15, cy + 0.38, rw - 0.3, 0.72, 'Residential Robot Architecture · Kitchen Standard · Installation Standard · Software · Calibration · Care Network',
         size=10, color='FFFFFF')
    note_line(s, 'Risk: 대기업·가구사가 동일 Integration Layer를 직접 개발할 가능성 → 대응은 Template Library·설치 Data·Partner 계약 선점 (21장). 우위 여부는 미검증.', y=6.5)
    foot(s, 20)

# ---------------------------------------------------------------- 21 moat / IP / flywheel
def s21(prs):
    s = start(prs, 'moat', 21, 'Moat: Architecture · Template · 설치 Data · Installed Base', q=[5],
              visual='좌측 Moat 7 Layer 적층 (아래 Product Architecture → 위 Installed Base, 각 Layer 현재 상태). 중앙 Patent Family 후보 요약. 우측 Operational Flywheel 원형.',
              chart='Layer Stack + Flywheel',
              note=('Moat를 특허 개수나 AI 데이터만으로 설명하지 않습니다. 일곱 개 층으로 봅니다. 제품 구조, 주방 Template Library, 설치 Standard, Manipulation Skill, 특허와 Know-how, Care 데이터, 그리고 설치기반입니다. '
                    '현재는 모두 구축 전입니다. 특허 후보는 10개 Family로 정리했지만 선행기술조사 전이라 등록 가능성을 주장하지 않습니다. '
                    'Flywheel은 운영 측면입니다. 설치가 늘면 설치·고장 데이터가 쌓이고, Template이 개선되고, 설치시간과 Service 원가가 내려가 Partner가 늘어나는 구조입니다.'))
    y = head(s, '20  Moat · IP · Installed Base', 'Moat: Architecture · Template · 설치 Data · Installed Base',
             sub='특허 개수·AI Data만으로 설명하지 않음. 모든 Layer는 현재 구축 전 (TARGET). Patent는 후보 단계 — 선행기술조사 필요, 등록 가능성 주장 없음.')
    layers = ['L1  Product Architecture', 'L2  Kitchen Layout Template Library', 'L3  Installation Standard', 'L4  Manipulation Skill',
              'L5  Patent / Know-how', 'L6  Care / Service Data', 'L7  Installed Base']
    lw = 4.2
    for i, l in enumerate(reversed(layers)):
        ly = y + i * 0.6
        f = T['accent'] if i == 0 else (T['text'] if i == 6 else T['soft'])
        c = 'FFFFFF' if i in (0, 6) else T['text']
        rect(s, MX + i * 0.08, ly, lw - i * 0.16, 0.52, fill=f)
        text(s, MX + i * 0.08 + 0.15, ly, lw - 0.4, 0.52, l, size=11, bold=True, color=c, anchor='m')
    mx_ = MX + lw + 0.35; mw = 3.6
    text(s, mx_, y, mw, 0.3, 'Patent Family 후보 (A10)', size=12, bold=True)
    pats = ['주방가구 일체형 Rail · Dock · Storage 구조', 'Robot-ready Kitchen Interface Module', 'Fold / Deploy Robot Storage',
            'Human Zone / Robot Zone Safety Control', 'Kitchen End-effector', 'Food-contact Consumable Cartridge',
            'Installation Auto Calibration', 'Dishwasher Robot Interface', 'Robot Cleaning / Sanitizing Dock', 'Layout 기반 Robot Module Selection']
    text(s, mx_, y + 0.38, mw, 3.9, [f'{i + 1:02d}  {p}' for i, p in enumerate(pats)], size=9.5, space_after=2.5, color=T['text2'])
    kit.tag(s, mx_, y + 4.0, 'TBV')
    # flywheel
    fx = mx_ + mw + 0.3; fw = W - MX - fx
    text(s, fx, y, fw, 0.3, 'Installed Base Flywheel', size=12, bold=True)
    steps = ['Installed Kitchen ↑', 'Installation Data ↑', 'Failure Pattern 축적', 'Template 개선', 'Installation Time ↓',
             'Service Cost ↓', 'Partner 확대']
    import math
    cx = fx + fw / 2; cy = y + 2.25; r = 1.55
    for i, st in enumerate(steps):
        ang = -math.pi / 2 + i * 2 * math.pi / len(steps)
        bx = cx + r * math.cos(ang) - 0.75; by = cy + r * math.sin(ang) - 0.22
        chip(s, bx, by, 1.5, 0.44, st, fill=T['accent'] if i == 0 else T['soft'], color='FFFFFF' if i == 0 else T['text'], size=9)
    text(s, cx - 0.8, cy - 0.25, 1.6, 0.5, 'Operational\nFlywheel', size=10, bold=True, align='c', color=T['muted'])
    note_line(s, '차단 효과 가설: 동일 Hardware를 경쟁사가 확보해도 단지별 평면 Template · 설치 시간 Data · Partner 설치 표준은 설치 경험 없이 복제 어려움 (TO BE VALIDATED).', y=6.5)
    foot(s, 21)

# ---------------------------------------------------------------- 22 milestones & kill criteria
def s22(prs):
    s = start(prs, 'milestone', 22, '24개월 Investment Milestone과 Kill Criteria', q=[6],
              visual='4개 Phase 열 (M0-6 / M6-12 / M12-18 / M18-24): 상단 실행 항목, 중단 기업가치 Evidence, 하단 Kill Criteria (주황 테두리). 맨 아래 Seed 이전→이후 전환 띠.',
              chart='Phase Timeline + Kill Criteria',
              note=('Roadmap은 일정보다 기업가치가 올라가는 Evidence 중심으로 정리했습니다. 6개월에는 주거동선과 Robot Reach가 양립하는지, 9개월에는 Clean-up Task 신뢰성, 12개월에는 지불의사, '
                    '18개월에는 표준 모듈 재사용률, 24개월에는 유료 Pilot과 Partner를 확인합니다. 각 시점에 기준을 못 넘으면 구조를 바꾸거나 범위를 줄이거나 Scale 투자를 보류합니다. '
                    '투자자 입장에서는 돈이 끝까지 소진되기 전에 실패를 확인할 수 있는 구조입니다.'))
    y = head(s, '21  Roadmap · Milestone', '24개월 Investment Milestone과 Kill Criteria',
             sub='Roadmap이 아닌 기업가치 상승 Evidence 중심. 기준 미달 시 구조 변경 · 범위 축소 · Scale 보류. 모든 기준 = TARGET.')
    ph = [('M0 ~ M6', ['Layout Study (평면 30개)', '84㎡ 중심 Full-scale Mock-up', 'Robot Architecture 선정', 'Dish Handling Test'],
           'Reach × 동선 양립 확인', 'M6: 주거동선과 Robot Reach 양립 실패 → Architecture 변경'),
          ('M6 ~ M12', ['Kitchen Clean-up Demo', 'Dishwasher Integration', 'Robot-ready Storage · Template Study', 'BOM v1 · Consumer Research'],
           'Approved Task 3개 · Template 3개', 'M9: Clean-up 성공률 70% 미만 → Task Scope 축소\nM12: WTP 중앙값 < 목표가 60% → B2C 재검토'),
          ('M12 ~ M18', ['Real-home Pilot 3~5세대', 'Installation Process · Safety', 'Price · Rental · Care Economics', 'Design Partner'],
           '실제 주방 설치 · 설치시간 실측', 'M18: Standard Module 사용률 60% 미만 → Productization 재검토'),
          ('M18 ~ M24', ['Paid Pilot', 'Template Standardization', '설치비 · Service 원가 확정', 'Partner Pilot 협의'],
           'Series A Evidence Pack', 'M24: Paid Pilot · Partner 확보 실패 → Scale 투자 보류')]
    pw = (CW - 0.45) / 4
    for i, (t, items, ev, kill) in enumerate(ph):
        px = MX + i * (pw + 0.15)
        rect(s, px, y, pw, 0.42, fill=T['text']); text(s, px + 0.12, y, pw - 0.24, 0.42, t, size=12, bold=True, color='FFFFFF', anchor='m')
        text(s, px + 0.05, y + 0.52, pw - 0.1, 1.5, items, size=10, bullet='–', space_after=2)
        rect(s, px, y + 2.05, pw, 0.62, fill=T['accent_soft'])
        text(s, px + 0.12, y + 2.05, pw - 0.24, 0.62, [[('Evidence  ', {'size': 8.5, 'bold': True, 'color': T['accent']}), (ev, {'bold': True})]],
             size=10, anchor='m')
        rect(s, px, y + 2.8, pw, 1.0, line=T['accent'], lw=1.25)
        text(s, px + 0.12, y + 2.85, pw - 0.24, 0.92, kill, size=9.5, color=T['text'], anchor='m')
    text(s, MX, y + 2.85 - 0.0, 0.1, 0.1, '', size=8, check=False)
    by = y + 4.0
    rect(s, MX, by, 3.1, 0.75, fill=T['soft'])
    text(s, MX + 0.15, by, 2.9, 0.75, [[('Seed 이전  ', {'size': 9, 'color': T['muted'], 'bold': True}), ('Concept · Business Hypothesis', {'bold': True})]], size=11, anchor='m')
    arrow(s, MX + 3.15, by + 0.37, MX + 3.55, by + 0.37, color=T['accent'], lw=2)
    rect(s, MX + 3.6, by, CW - 3.6, 0.75, fill=T['text'])
    text(s, MX + 3.75, by, CW - 3.9, 0.75, 'Seed 이후: Working Product · Real Kitchen Installation · Template Library · Validated WTP / BOM / 설치비 / Service 원가 · Paid Pilot · Partner Validation · Repeatable Installation  →  Series A',
         size=10.5, bold=True, color='FFFFFF', anchor='m')
    foot(s, 22)

# ---------------------------------------------------------------- 23 team
def s23(prs):
    s = start(prs, 'team', 23, 'Founder / Team', q=[6],
              visual='좌측 Founder 평가 항목 7행 표 (모두 [Founder 정보 필요]). 우측 Seed 채용계획 (역할·시점) + 필요 Advisor.',
              chart='없음',
              note=('창업자 정보는 임의로 만들지 않았습니다. 투자 판단에서 가장 중요한 칸이 비어 있다는 점을 그대로 보여드립니다. '
                    '필요한 역량은 Robot Manipulation, 주방·건축 Integration, 그리고 고객·Partner 영업입니다. 이 세 가지를 Founding Team이 직접 갖추고 있는지가 Seed 판단의 첫 번째 질문이 됩니다.'))
    y = head(s, '22  Founder · Team', 'Founder / Team',
             sub='임의 생성 금지 원칙. 확인되지 않은 정보는 [Founder 정보 필요]로 표기. 투자 판단의 최우선 항목.')
    rows = [['Founder Background', '[Founder 정보 필요]'], ['Relevant Engineering Experience', '[Founder 정보 필요]'],
            ['Product Development Experience', '[Founder 정보 필요]'], ['Construction / Kitchen Understanding', '[Founder 정보 필요]'],
            ['Robot Experience', '[Founder 정보 필요]'], ['Customer / Partner Network', '[Founder 정보 필요]'],
            ['Full-time Commitment', '[Founder 정보 필요]']]
    lw = 5.9
    table(s, MX, y, lw, ['평가 항목', '내용'], [[a, (b_, {'color': T['accent'], 'bold': True})] for a, b_ in rows],
          col_w=[2.9, lw - 2.9], size=10.5, label='founder', max_h=3.6)
    rx = MX + lw + 0.4; rw = W - MX - rx
    text(s, rx, y, rw, 0.3, 'Seed 채용계획 (평균 인원 Y1 6명 → Y2 9명, ASSUMPTION)', size=12, bold=True)
    hires = [['Robotics Lead (Manipulation · Control)', 'M0'], ['Perception / ML Engineer', 'M0~M3'],
             ['Mechatronics (Rail · End-effector · Garage)', 'M0~M3'], ['Kitchen · Architecture Integration (설계·시공 표준)', 'M0'],
             ['Embedded · Electrical · Safety', 'M3~M6'], ['Field / Installation Engineer', 'M12'],
             ['BD · Customer Research (Partner)', 'M6']]
    table(s, rx, y + 0.38, rw, ['역할', '시점'], hires, col_w=[rw - 0.95, 0.95], size=10, label='hires', max_h=3.2)
    text(s, rx, y + 3.75, rw, 0.7, 'Advisor 필요: 주방가구 제조·시공 · 건설사 설계/유상옵션 · Robot 안전인증 (ISO 10218 / ISO 13482 / KC) · 렌탈 금융',
         size=10, color=T['text2'])
    statement(s, MX, 6.15, CW, 'Seed 판단 1순위: Robot Manipulation × 주방·건축 Integration × 고객·Partner 영업을 Founding Team이 직접 보유하는가', size=12)
    foot(s, 23)

# ---------------------------------------------------------------- 24 ask
def s24(prs):
    F = M['funds']; B5 = M['scenarios']['B']
    s = start(prs, 'ask', 24, 'Seed Ask: 20억원 + TIPS 연계, Commercial Risk 제거 자본', q=[6],
              visual='좌측 Use of Funds 표 (Draft vs 검증 수정안, 억원) + 부족분·대안. 우측 What Must Be True 7개 (짧은 문장) → Series A Evidence. 하단 Series A 규모 DERIVED.',
              chart='표 + 체크리스트',
              note=(f"요청 금액은 Seed 20억원입니다. 다만 실제 인건비와 Prototype, Mock-up 공간, 인증 비용을 반영해 24개월 예산을 다시 계산하면 약 {F['revised_total'] / 10000:.1f}억원이 필요합니다. "
                    f"20억원만으로는 약 {F['months_equity_only']:.0f}개월입니다. 그래서 TIPS R&D 최대 8억원 연계를 기본 구조로 제안하고, 선정되지 않으면 Seed 증액이나 18개월 시점 Bridge가 필요합니다. "
                    '이 자금으로 확인할 것은 오른쪽 일곱 가지 전제입니다. 24개월 후 이 증거가 있으면 Series A에서 Scale 자본을 요청합니다.'))
    y = head(s, '23  Seed Ask', 'Seed Ask: 20억원 + TIPS 연계, Commercial Risk 제거 자본',
             sub='Robot Kitchen 완성 X  →  Commercial Risk Reduction O. 사용안은 실제 인건비·Prototype·공간·인증 비용으로 재검증.')
    rows = []
    rev = dict(F['revised'])
    mapping = [('Core Development Team', 'Core Development Team'), ('Robot / Kitchen Prototype', 'Robot / Kitchen Prototype'),
               ('Mock-up / Installation Development', 'Mock-up / Installation Development'), ('Vision / Software / Data', 'Vision / Software / Data'),
               ('Pilot / Customer Validation', 'Pilot / Customer Validation'), ('Safety / Certification / IP', 'Safety / Certification / IP'),
               ('Operations / Contingency', None)]
    draft = dict(F['draft'])
    for dk, rk in mapping:
        rv = rev[rk] if rk else rev['Operations (G&A)'] + rev['Contingency (10%)']
        rows.append([dk, f"{draft[dk] / 10000:.1f}", f"{rv / 10000:.1f}"])
    rows.append([('합계 (24개월)', {'bold': True}), (f"{F['draft_total'] / 10000:.1f}", {'bold': True}), (f"{F['revised_total'] / 10000:.1f}", {'bold': True, 'color': T['accent']})])
    lw = 6.2
    table(s, MX, y, lw, ['억원', 'Draft', '수정안'], rows, col_w=[lw - 2.0, 1.0, 1.0], size=10, align=['l', 'r', 'r'], label='uof', max_h=3.3)
    text(s, MX, y + 3.3, lw, 1.3, [f"수정안 근거: 평균 인원 6→9명 × 인당 8,500만원, Mock-up 50평 + 2식, Pilot 5세대 손실 반영 (A16)",
                                  f"부족분 {F['gap_vs_seed'] / 10000:.1f}억원 · Seed 단독 Runway 약 {F['months_equity_only']:.0f}개월",
                                  'Plan A: TIPS R&D 최대 8억원 (선정 미확정) · Plan B: Seed 25억원 또는 M18 Bridge'],
         size=10, color=T['text2'], bullet='–', space_after=3)
    rx = MX + lw + 0.4; rw = W - MX - rx
    text(s, rx, y, rw, 0.3, 'What Must Be True  →  Series A Evidence', size=12, bold=True)
    wm = ['Remodeling 고객이 Robot Integration Premium을 지불', '주요 Kitchen Layout이 소수 Template으로 분류',
          'Single Robot Architecture가 반복 설치 가능', 'Robot + Installation GM이 물량과 함께 개선',
          'Care + Consumables가 실제 반복매출 형성', 'Partner Distribution이 Direct보다 빠르게 Scale',
          'Service Cost가 Recurring Revenue를 초과하지 않음']
    for i, w_ in enumerate(wm):
        ry = y + 0.42 + i * 0.5
        rect(s, rx, ry + 0.06, 0.32, 0.32, line=T['accent'], lw=1.25)
        text(s, rx, ry + 0.06, 0.32, 0.32, str(i + 1), size=10, bold=True, color=T['accent'], align='c', anchor='m')
        text(s, rx + 0.45, ry, rw - 0.45, 0.45, w_, size=10.5, anchor='m')
    statement(s, MX, 6.1, CW, f"Series A 규모 (DERIVED): Base Y3~Y4 영업손실 약 {-(B5['op'][2] + B5['op'][3]) / 10000:.0f}억원 + Buffer → 80~100억원. 손익분기 연 약 {M['breakeven_kitchens']:,.0f}세대 (Y5 단가·원가 기준, Y6 이후)",
              size=11.5)
    foot(s, 24)

MAIN = [s01, s02, s03, s04, s05, s06, s07, s08, s09, s10, s11, s12, s13, s14, s15, s16, s17, s18, s19, s20, s21, s22, s23, s24]
