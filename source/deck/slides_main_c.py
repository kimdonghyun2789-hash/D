from deckkit import *
import json
from paths import RENDERS as A, ORIGINAL as O, MODEL_JSON
M = json.load(open(MODEL_JSON, encoding='utf-8'))
B = M['base']; SEEDP = M['seed']

# ================================================================ 11 GTM
def s11(prs):
    s = new_slide(prs, '11')
    header(s, '11', '시장 진입과 확장', 'SI를 통해 시장에 들어가고, OEM으로 확장한다', 'Integrator-led. OEM-scaled.')
    stages = [('1단계 · M0–M24 (SEED)', 'SI 주도 진입', [('채널', 'Robot SI · Design Partner · 유료 PoC'), ('매출', 'SoftHand 하드웨어 + 유료 PoC + 통합 엔지니어링 + Task Skill 패키지'), ('증명', 'Design Partner 3곳 → 유료 PoC 5건 → 반복 고객 2곳')], False),
              ('2단계 · Y3–Y5', '직판 + 파트너', [('채널', '검증된 Skill Pack을 SI 파트너 네트워크로 판매'), ('매출', '재사용 Skill 패키지 + Runtime · 유지보수 (+ 하드웨어)'), ('증명', f"재사용 매출 비중 ↑ · Base Case Y5 ₩{B['rev'][4]:.1f}억 (OEM · Kitchen 0원)")], False),
              ('3단계 · 확장 TRIGGER', 'OEM Design Win', [('채널', 'Robot OEM이 Hand · Runtime을 옵션 · 표준 모듈로 탑재'), ('매출', 'OEM 라이선스 + 내장 Runtime + 출하량 연동 로열티'), ('증명', 'OEM Design Win 1건')], True)]
    gap = 0.22; cw = (12.13 - 2 * gap) / 3; y0 = 1.95; ch = 2.62
    for i, (st, title, rows, hot) in enumerate(stages):
        x = 0.6 + i * (cw + gap)
        card(s, x, y0, cw, ch, fill=OR_FILL if hot else CARD, line=OR if hot else None, lw=1.25)
        text(s, x + 0.22, y0 + 0.16, cw - 0.4, 0.22, st, size=8.5, f='S', color=OR, spc=80)
        text(s, x + 0.22, y0 + 0.42, cw - 0.4, 0.38, title, size=17, f='K')
        yy = y0 + 0.95
        for lab, val in rows:
            text(s, x + 0.22, yy, 0.55, 0.24, lab, size=8.5, f='S', color=OR_LIGHT if hot else MUTED)
            text(s, x + 0.8, yy - 0.01, cw - 1.0, 0.56, val, size=10, color=TEXT if lab == '매출' else TEXT2, f='S' if lab == '매출' else 'R', ls=1.12)
            yy += 0.58
        if i < 2: tri(s, x + cw + 0.06, y0 + ch / 2 - 0.05, s=0.1, color=OR if i == 1 else MUTED)
    ys = y0 + ch + 0.12
    card(s, 0.6, ys, 12.13, 0.4, fill=CARD)
    text(s, 0.8, ys + 0.07, 11.8, 0.28, [[('OEM이 직접 만들면?  ', {'f': 'S', 'color': OR}), ('다수 산업용 · 협동로봇 OEM은 Arm · Controller에 집중하고 End-effector는 파트너 생태계에 의존 — 여러 브랜드에서 동작하는 Skill은 독립 Layer가 유리 → OEM은 경쟁자이자 채널 (A4)', {})]], size=9, color=TEXT2)
    # bottom left: OEM scale mechanism
    y1 = 5.2; wl = 7.6
    card(s, 0.6, y1, wl, 1.68)
    text(s, 0.82, y1 + 0.14, wl - 0.4, 0.26, [[('OEM Design Win = Scale Trigger', {'f': 'K', 'size': 12.5}), ('    고객 한 곳씩 영업  →  OEM 출하량에 실려 판매', {'size': 9.5, 'color': TEXT2})]], size=12.5)
    terms = ['대상 Robot 출하량', '옵션 채택률', '대당 Hand · Runtime 매출', 'OEM 매출']
    ops = ['×', '×', '=']
    tw = [1.75, 1.45, 1.75, 1.35]; x = 0.82; yy = y1 + 0.58
    for i, t in enumerate(terms):
        last = i == 3
        b = box(s, x, yy, tw[i], 0.5, fill=OR_FILL if last else CARD2, line=OR if last else LINE2, lw=1.0, r=0.06)
        box_text(b, t, size=9.5, f='S', color=OR if last else TEXT)
        text(s, x, yy + 0.56, tw[i], 0.36, '[OEM 협의 후 검증]', size=8, f='M', color=YEL, align='c')
        x += tw[i]
        if i < 3:
            text(s, x, yy + 0.08, 0.3, 0.32, ops[i], size=14, f='K', color=MUTED, align='c'); x += 0.3
    # bottom right: business model message
    xr = 0.6 + wl + 0.2; wr = 12.73 - xr
    card(s, xr, y1, wr, 1.68, fill=OR_FILL, line=OR, lw=1.25)
    text(s, xr + 0.2, y1 + 0.14, wr - 0.35, 0.26, 'Hardware First. Skills Next. OEM at Scale.', size=10.5, f='S', color=OR)
    text(s, xr + 0.2, y1 + 0.44, wr - 0.35, 0.62, ['초기에는 제품회사처럼 돈을 벌고,', '장기에는 Platform Economics로 확장한다'], size=12, f='K', ls=1.12)
    text(s, xr + 0.2, y1 + 1.08, wr - 0.35, 0.55, ['Integration 매출은 숨기지 않는다 — 장기 모델이 아니라', '시장 진입과 제품화 수단 · 가격 가정 A10 · Base Case A11'], size=8.5, color=TEXT2, ls=1.15)
    footer(s, '11')
    notes(s, "시장 진입은 SI가 이끕니다. Seed 기간에는 Robot SI와 Design Partner를 통해 Paid PoC로 들어가고, 매출은 Hand 하드웨어, 유료 PoC, 통합 엔지니어링, Task Skill 패키지입니다. 통합 매출을 숨기지 않겠습니다. 다만 이것은 장기 비즈니스 모델이 아니라 시장 진입과 제품화를 위한 수단입니다. "
             "검증된 Skill Pack이 쌓이면 SI 파트너 네트워크를 통해 판매하고, 매출은 재사용 Skill 패키지와 Runtime·Support로 이동합니다. "
             "결정적인 Scale Trigger는 OEM Design Win입니다. 로봇 OEM이 저희 Hand와 Runtime을 옵션이나 표준 모듈로 탑재하면, 고객 한 곳씩 영업하던 회사가 OEM 출하량에 따라 판매되는 회사로 바뀝니다. "
             "OEM 매출은 대상 로봇 출하량 곱하기 옵션 채택률 곱하기 Hand·Runtime 매출 구조이며, 각 숫자는 OEM 협의 후 검증하겠습니다. 현재 단계에서는 수백억, 수천억 같은 매출을 계산하지 않았습니다. "
             "OEM이 직접 만들지 않겠느냐는 질문에는, 다수 산업용·협동로봇 OEM은 Arm과 Controller에 집중하고 End-effector는 파트너 생태계에 의존한다는 점, 그리고 여러 브랜드에서 동작하는 Skill은 단일 OEM이 만들기 어렵다는 점에서 OEM은 경쟁자이면서 채널이라고 답하겠습니다.")

# ================================================================ 12 FACTORY vs KITCHEN
def s12(prs):
    s = new_slide(prs, '12')
    header(s, '12', '확장 전략', '공장이 사업성을, 주방이 기술의 확장성을 증명한다', 'Factory Proves the Business. Kitchen Proves the Vision.', tag='CONCEPT RENDERING')
    y0 = 1.95; w = 5.96; ih = 2.75
    # factory
    xf = 0.6
    card(s, xf, y0, w, 4.78)
    picture_cover(s, A + 'cell_overview.jpg', xf + 0.06, y0 + 0.06, w - 0.12, ih, name='Factory rendering', fx=0.55, fy=0.5)
    pill(s, xf + 0.2, y0 + 0.2, None, 0.26, '공장 · 첫 매출 시장', color=TEXT, line=OR, fill=OR_FILL, size=8.5)
    text(s, xf + 0.25, y0 + ih + 0.2, w - 0.5, 0.36, '사업성을 증명한다', size=16, f='K')
    text(s, xf + 0.25, y0 + ih + 0.62, w - 0.5, 0.3, 'Machine Tending · 유료 PoC · 반복 발주 · 측정 가능한 ROI', size=10.5, f='S', color=OR_LIGHT)
    text(s, xf + 0.25, y0 + ih + 0.98, w - 0.5, 0.82, ['반복 공정이라 Baseline 대비 개선을 숫자로 증명할 수 있고,', 'SI 채널과 구매 예산이 이미 존재한다', '→ Base Case 매출의 100%'], size=9.5, color=TEXT2, ls=1.18)
    # kitchen
    xk = 0.6 + w + 0.21
    card(s, xk, y0, w, 4.78)
    picture_cover(s, A + 'kitchen_bench.jpg', xk + 0.06, y0 + 0.06, w - 0.12, ih, name='Kitchen bench rendering', fx=0.45, fy=0.45)
    pill(s, xk + 0.2, y0 + 0.2, None, 0.26, '주방 · 기술 Demonstrator', color=TEXT, line=LINE2, fill=BG, size=8.5)
    text(s, xk + 0.25, y0 + ih + 0.2, w - 0.5, 0.36, '기술의 확장성을 증명한다', size=16, f='K')
    text(s, xk + 0.25, y0 + ih + 0.62, w - 0.5, 0.3, '사람을 위해 만든 환경을 Robot이 그대로 쓰는 궁극의 Demonstrator', size=10, f='S', color=TEXT)
    chips = ['문', '서랍', '손잡이', '노브', '팬', '냄비', '집게', '접시', '젖은 표면', '유연한 물체', '변하는 하중']
    x = xk + 0.25; yy = y0 + ih + 0.98; maxx = xk + w - 0.25
    for t in chips:
        cwid = text_width_in(t, 'S', 8, 0) + 0.22
        if x + cwid > maxx: x = xk + 0.25; yy += 0.3
        chip(s, x, yy, cwid, 0.24, t, size=8, fill=CARD3, color=TEXT2); x += cwid + 0.07
    text(s, xk + 0.25, yy + 0.36, w - 0.5, 0.5, [[('Seed 범위  ', {'f': 'S', 'color': OR_LIGHT}), ('단일 팔 · 벤치 스케일 Demo (손잡이 · 집게 · 팬 · 접시) · ₩0.3억', {})], [('Series A 이후  ', {'f': 'S', 'color': MUTED}), ('천장형 양팔 Full Kitchen — 미래 비전 (A14)', {})]], size=9, color=TEXT2, ls=1.18)
    text(s, 0.6, 6.82, 12.13, 0.2, '주력시장이 아닌 이유: 회수기간이 가동률에 민감하고 위생 · 안전 부담이 커 검증이 느리다 — Kitchen은 Base Case 매출 0원, Upside로 분리 (A11 · A14)', size=8.5, color=MUTED2)
    footer(s, '12')
    notes(s, "Robot Kitchen의 역할을 한 문장으로 정리하면, 공장이 사업성을 증명하고 주방이 기술의 확장성을 증명한다는 것입니다. "
             "첫 매출은 공장에서 나옵니다. 반복 공정이라 고객 Baseline 대비 개선을 숫자로 증명할 수 있고, SI 채널과 구매 예산이 이미 있습니다. Base Case 매출은 100% 공장에서 나옵니다. "
             "주방은 문, 서랍, 손잡이, 노브, 팬, 냄비, 집게, 접시, 젖은 표면, 유연한 물체, 변하는 하중이 한 공간에 모여 있는, 사람을 위해 만들어진 환경의 집약체입니다. 그래서 Human-designed Environment를 로봇이 그대로 사용하는 궁극적인 Technology Demonstrator입니다. "
             "다만 Seed 단계에서는 범위를 줄였습니다. 천장 레일 양팔 주방이 아니라, 이미 구매하는 로봇 한 대로 손잡이, 집게, 팬, 접시를 다루는 벤치 스케일 데모만 3천만원 예산으로 만듭니다. 천장형 양팔 Full Kitchen은 Series A 이후의 비전이며, 그 경우에도 로봇 대여나 공동개발 같은 실제 파트너 전제가 생긴 뒤에 진행합니다. "
             "주방을 주력 시장에 두지 않는 이유는 회수기간이 가동률에 크게 좌우되고 위생·안전 요구가 높아, 첫 매출 엔진으로는 검증 속도가 느리기 때문입니다.")

# ================================================================ 13 ROADMAP
def s13(prs):
    s = new_slide(prs, '13')
    header(s, '13', '24개월 로드맵', '24개월 안에 기술이 아니라 사업성을 증명한다', '24 Months to Commercial Proof.', tag='Seed 마일스톤')
    # timeline
    ty = 1.92
    line(s, 0.65, ty + 0.06, 12.68, ty + 0.06, color=LINE2, w=1.25)
    for i, m in enumerate(['M0', 'M6', 'M12', 'M18', 'M24']):
        x = 0.65 + i * (12.03 / 4)
        box(s, x - 0.06, ty, 0.12, 0.12, fill=OR if i == 4 else MUTED, shape='oval', name='tick')
        text(s, x - 0.3, ty - 0.24, 0.6, 0.2, m, size=8.5, f='S', color=TEXT2, align='c')
    phases = [('M0–M6', '기술이 되는가?', ['법인 설립 · 핵심 인력 합류', 'SoftHand-4 Alpha 시제품', '머신텐딩 대표 공정 시연', '고객 인터뷰 30곳', 'Design Partner 후보 확보', '반복실험 기록'], '기술 리스크'),
              ('M6–M12', '고객이 돈을 낼 이유가 있는가?', ['첫 유료 PoC', '고객 Baseline 확보', '엔지니어링 시간 측정', '툴링 비용 · 리드타임 측정', 'ToolSkill V1'], '고객 리스크'),
              ('M12–M18', '반복 가능한 제품이 되는가?', ['설계 동결 · BOM · 공급사', '내구성 · 제조원가 검증', '첫 반복 발주', '첫 재사용 Skill 패키지', '재사용률 측정 시작', '두 번째 Robot 플랫폼 통합'], '제품 · 원가 리스크'),
              ('M18–M24', '확장 가능한가?', ['유료 PoC 5건+', '반복 고객 2곳+', '재사용 Skill 다수 확보', 'Skill 이식성 · Robot 2종', '매출총이익률 검증', 'Series A 준비'], '확장 리스크')]
    gap = 0.2; cw = (12.13 - 3 * gap) / 4; y0 = 2.22; ch = 3.08
    for i, (per, q, items, risk) in enumerate(phases):
        x = 0.6 + i * (cw + gap); hot = i == 3
        card(s, x, y0, cw, ch, fill=OR_FILL if hot else CARD, line=OR if hot else None, lw=1.25)
        text(s, x + 0.2, y0 + 0.14, cw - 0.3, 0.22, per, size=9, f='S', color=OR, spc=60)
        text(s, x + 0.2, y0 + 0.38, cw - 0.35, 0.62, q, size=13.5, f='K', ls=1.08)
        yy = y0 + 1.0
        for it in items:
            dot(s, x + 0.22, yy + 0.08, 0.06, OR if hot else MUTED)
            text(s, x + 0.36, yy, cw - 0.5, 0.24, it, size=9.5, color=TEXT if hot else TEXT2)
            yy += 0.27
        line(s, x + 0.2, y0 + ch - 0.42, x + cw - 0.2, y0 + ch - 0.42, color='5A3A26' if hot else LINE, w=0.75)
        text(s, x + 0.2, y0 + ch - 0.34, cw - 0.3, 0.24, [[('해소하는 리스크  ', {'size': 8, 'color': MUTED}), (risk, {'f': 'S', 'color': OR if hot else TEXT})]], size=9.5)
    if True:
        x = 0.6 + 3 * (cw + gap)
        pill(s, None, y0 + 0.13, None, 0.22, '보조: 주방 벤치 Demo', right=x + cw - 0.15, size=7, spc=20, color=TEXT2, line=LINE2)
    # gates
    y1 = 5.45
    label(s, 0.6, y1, 6, 'Seed Gate — 통과하지 못하면 이렇게 결정한다', color=OR, size=9.5)
    gates = [('M6', '도구 토크 · 반복성 미확보', 'Hand 구조 재검토'), ('M12', '전환비용 개선에 지불의사 없음', '첫 시장 · Task 재정의'),
             ('M18', 'Skill 재사용률 낮음', 'Platform 가설 재검토'), ('M24', '반복 발주 없음', 'Series A 확장 보류')]
    for i, (m, cond, dec) in enumerate(gates):
        x = 0.6 + i * (cw + gap)
        card(s, x, y1 + 0.3, cw, 1.1, fill=CARD, line=LINE2, lw=0.75, dash=True)
        text(s, x + 0.18, y1 + 0.4, 0.6, 0.3, m, size=13, f='K', color=OR)
        text(s, x + 0.78, y1 + 0.42, cw - 0.9, 0.26, cond, size=9.5, f='S')
        text(s, x + 0.78, y1 + 0.72, cw - 0.9, 0.55, [[('→ ', {'color': OR}), (dec, {})]], size=9.5, color=TEXT2, ls=1.1)
    footer(s, '13')
    notes(s, "24개월 계획의 목표는 기술개발 완료가 아니라 사업성 증명입니다. 네 개의 질문에 순서대로 답합니다. "
             "첫 6개월은 기술이 되는가입니다. 법인 설립과 핵심 인력 합류, SoftHand-4 알파, 머신텐딩 대표 Sequence, 고객 인터뷰 30곳과 Design Partner 후보, 반복실험 로그를 만듭니다. "
             "6~12개월은 고객이 돈을 낼 이유가 있는가입니다. 첫 Paid PoC를 하고 고객 Baseline을 확보해 엔지니어링 시간, 툴링 비용, 리드타임을 측정합니다. "
             "12~18개월은 반복 가능한 제품이 되는가입니다. 설계 동결과 BOM, 공급사, 내구성과 제조원가, 첫 반복 주문, 첫 재사용 Skill 패키지, 재사용률 측정, 두 번째 로봇 플랫폼 통합입니다. "
             "마지막 6개월은 확장 가능한가입니다. Paid PoC 5건 이상, 반복 고객 2곳 이상, 여러 재사용 Skill, 두 플랫폼에서의 Skill 이식성, 매출총이익률을 검증하고 Series A를 준비합니다. 주방 데모는 핵심 마일스톤이 아니라 보조 데모입니다. "
             "그리고 실패 조건을 미리 정했습니다. 6개월에 토크와 반복성이 안 나오면 Hand 구조를 재검토하고, 12개월에 지불의사가 없으면 시장과 Task를 다시 정의하고, 18개월에 재사용률이 낮으면 Platform 가설을 재검토하고, 24개월에 반복 주문이 없으면 Series A 확장을 보류합니다. 투자금은 R&D 소비가 아니라 가설검증 자본입니다.")

# ================================================================ 14 TEAM
def s14(prs):
    s = new_slide(prs, '14')
    header(s, '14', 'Founding Team', '왜 이 팀이 이 문제를 해결할 수 있는가', 'Founder-Market Fit', tag='[정보 입력 필요] · 외부 제출 전 필수', tag_style='placeholder')
    y0 = 1.95
    # founder card
    card(s, 0.6, y0, 3.85, 4.6)
    box(s, 0.85, y0 + 0.25, 1.05, 1.05, fill=YEL_FILL, line=YEL, dash=True, shape='oval', name='Photo')
    text(s, 0.85, y0 + 0.62, 1.05, 0.3, 'PHOTO', size=8.5, f='S', color=YEL, align='c')
    text(s, 2.1, y0 + 0.36, 2.2, 0.22, 'FOUNDER / CEO', size=8.5, f='S', color=OR, spc=80)
    text(s, 2.1, y0 + 0.62, 2.2, 0.42, '[이름]', size=20, f='K', color=YEL)
    text(s, 0.85, y0 + 1.5, 3.4, 0.22, '사업과 직접 연결되는 경험만 기재', size=8.5, f='S', color=MUTED)
    cats = ['Robot', 'Automation', 'Manufacturing', 'AI', 'Mechanical', 'Field Integration', 'Customer Network']
    x = 0.85; yy = y0 + 1.78
    for t in cats:
        cwid = text_width_in(t, 'S', 8, 0) + 0.22
        if x + cwid > 4.25: x = 0.85; yy += 0.3
        chip(s, x, yy, cwid, 0.24, t, size=8, fill=CARD3, color=TEXT2); x += cwid + 0.07
    placeholder(s, 0.85, yy + 0.42, 3.35, 0.62, '[정보 입력 필요] 산업 경력 · 직무 · 기간', size=9)
    placeholder(s, 0.85, yy + 1.14, 3.35, 0.62, '[정보 입력 필요] Prototype · 연구실적 · 특허', size=9)
    # three questions
    xq = 4.65; wq = 4.6
    qs = [('Q1', '왜 이 Founder가 이 문제를 발견했는가?', '창업 계기 · 현장에서 직접 겪은 전환비용 문제'),
          ('Q2', '왜 이 Founder와 팀이 이 제품을 만들 수 있는가?', 'Hand 메카트로닉스 · 제어 · 현장 통합 역량의 근거'),
          ('Q3', '왜 이 팀이 첫 고객을 확보할 수 있는가?', '고객 Network · 첫 Design Partner 후보 · SI 관계')]
    yy = y0
    for q, t, hint in qs:
        card(s, xq, yy, wq, 1.45)
        text(s, xq + 0.2, yy + 0.14, 0.5, 0.3, q, size=13, f='K', color=OR)
        text(s, xq + 0.7, yy + 0.16, wq - 0.85, 0.3, t, size=11, f='K')
        placeholder(s, xq + 0.2, yy + 0.58, wq - 0.4, 0.68, f'[정보 입력 필요]  {hint}', size=9)
        yy += 1.58
    # commitment
    xc = 9.45; wc = 12.73 - xc
    card(s, xc, y0, wc, 4.6)
    label(s, xc + 0.2, y0 + 0.16, wc - 0.3, 'Founder Commitment', color=OR, size=9)
    items = ['Full-time 전념', '자기자본 투자', '공동창업자', 'Prototype 경험', '연구실적', '특허', '고객 네트워크', '첫 Design Partner 후보', '현재 직장 정리 계획']
    yy = y0 + 0.5
    for it in items:
        text(s, xc + 0.2, yy, wc - 1.2, 0.26, it, size=10, f='S', color=TEXT)
        b = box(s, xc + wc - 0.95, yy - 0.01, 0.75, 0.26, fill=YEL_FILL, line=YEL, dash=True, r=0.05, name='check')
        box_text(b, '[  ]', size=8.5, f='S', color=YEL)
        yy += 0.44
    # hiring plan
    y1 = 6.68
    text(s, 0.6, y1, 12.13, 0.3, [[('Seed 채용 계획  ', {'f': 'S', 'color': OR}), ('창업자 2 + 핵심 6명 단계 채용 — 기구·구동 · 제어·임베디드 · Robot SW·Skill · 현장 통합(FAE) · Vision·AI · DFM·품질   |   없는 정보는 만들지 않는다', {})]], size=9, color=TEXT2)
    footer(s, '14')
    notes(s, "Pre-seed 투자에서 가장 중요한 것은 Founder-Market Fit입니다. 이 장은 이력 나열이 아니라 세 가지 질문에 답해야 합니다. 왜 이 창업자가 이 문제를 발견했는가, 왜 이 창업자와 팀이 이 제품을 만들 수 있는가, 왜 이 팀이 첫 고객을 확보할 수 있는가입니다. "
             "[이 부분은 창업자의 실제 이력으로 채워야 합니다. Robot, Automation, Manufacturing, AI, 기구, 현장 통합, 고객 네트워크 중 사업과 직접 연결되는 경험만 고르고, 풀타임 여부, 자기자본 투자, 공동창업자, 프로토타입 경험, 연구실적, 특허, 고객 네트워크, 첫 Design Partner 후보, 현재 직장 정리 계획을 기재합니다. 정보가 없으면 만들지 않고 비워둡니다.] "
             "Seed 기간에는 창업자 2명과 기구·구동, 제어·임베디드, 로봇 소프트웨어·Skill, 현장 통합, 비전·AI, DFM·품질 엔지니어 6명을 단계적으로 채용합니다.")

# ================================================================ 15 ASK
def s15(prs):
    s = new_slide(prs, '15')
    header(s, '15', '투자 제안', '20억원으로 제품이 아니라 회사를 만든다', '₩2.0B to Build the Company.')
    y0 = 1.95
    # seed block
    b = box(s, 0.6, y0, 2.6, 2.3, fill=OR, r=0.1, name='Seed block')
    text(s, 0.6, y0 + 0.22, 2.6, 0.24, 'SEED', size=10, f='S', color='FFFFFF', spc=200, align='c')
    text(s, 0.6, y0 + 0.48, 2.6, 0.8, '₩2.0B', size=38, f='K', color='FFFFFF', align='c', ls=1.0)
    text(s, 0.6, y0 + 1.3, 2.6, 0.6, ['20억원 · 24개월', 'Company Creation Capital'], size=10, f='S', color='FFFFFF', align='c', ls=1.15)
    # runway structure
    xr = 3.4; wr = 4.3
    card(s, xr, y0, wr, 2.3)
    label(s, xr + 0.2, y0 + 0.14, wr - 0.3, '집행 구조 · 18 + 6개월', color=OR, size=9)
    rows = [('18개월 Core Runway', f"₩{SEEDP['core18']:.1f}억", 'M0~M18 · 설계 동결 · 첫 반복 발주까지'),
            ('6개월 Milestone Extension', f"₩{SEEDP['ext6']:.1f}억", 'M18 Gate 통과 시 집행'),
            ('예비비 · 운전자본', '₩1.7억', '매출 0원이어도 M24까지 집행 가능')]
    yy = y0 + 0.45
    for t, v, d in rows:
        text(s, xr + 0.2, yy, 2.6, 0.26, t, size=10.5, f='S')
        text(s, xr + wr - 1.2, yy, 1.0, 0.26, v, size=11, f='K', color=OR, align='r')
        text(s, xr + 0.2, yy + 0.26, wr - 0.4, 0.22, d, size=8.5, color=TEXT2)
        yy += 0.6
    # series A readiness
    xs = 7.9; ws = 12.73 - xs
    card(s, xs, y0, ws, 2.3, fill=OR_FILL, line=OR, lw=1.25)
    label(s, xs + 0.2, y0 + 0.14, ws - 0.3, '24개월 후 Series A를 받을 수 있는 숫자', color=OR, size=9)
    kp = [('유료 PoC', '5건+'), ('반복 고객', '2곳+'), ('승인 Task 완료율', '≥95%'), ('내구성', '30만 회'), ('Skill 이식성', 'Robot 2종'), ('재사용률', '상승 추세'), ('하드웨어 매출총이익률', 'BOM 검증'), ('Design Partner', '3곳')]
    colw = (ws - 0.4) / 2
    for i, (k, v) in enumerate(kp):
        cx = xs + 0.2 + (i % 2) * colw; cy = y0 + 0.44 + (i // 2) * 0.45
        text(s, cx, cy, colw - 0.1, 0.2, k, size=8.5, color=TEXT2)
        text(s, cx, cy + 0.18, colw - 0.1, 0.28, v, size=12, f='K', color=TEXT)
    # use of funds bar
    y1 = 4.5
    label(s, 0.6, y1, 8, '자금 사용 계획 · ₩20억 (24개월)', color=OR, size=9.5)
    uof = SEEDP['uof']
    names = {'핵심 인력 (8명 단계 채용)': '핵심 인력 8명', 'Prototype · 내구시험': 'Prototype · 내구시험', 'Robot 2종 · 시험 Cell': 'Robot 2종 · 시험 Cell', '고객 PoC · 현장통합(비청구)': '고객 PoC · 현장통합',
             'SW · AI · Data': 'SW · AI · Data', '제조 · 품질 · 안전 · IP': '제조 · 품질 · IP', 'Kitchen Bench Demo': 'Kitchen Bench Demo', '운영 (임차·법무·회계·보험·출장)': '운영', '예비비 · 운전자본': '예비비 · 운전자본'}
    cols = [OR, 'F3A574', 'E9E7E2', 'AEB3BB', '8A8F97', '737882', '4C5159', '3B3F45', '2E333B']
    vals = [v for _, v in uof]; tot = sum(vals); vals = [v * 20.0 / tot for v in vals]
    x = 0.6; bw = 12.13
    for (n, _), v, c in zip(uof, vals, cols):
        w = bw * v / 20.0
        box(s, x, y1 + 0.3, w - 0.02, 0.42, fill=c, shape='rect', name='uof ' + n)
        x += w
    for i, ((n, _), v, c) in enumerate(zip(uof, vals, cols)):
        cx = 0.6 + (i % 3) * 4.1; cy = y1 + 0.86 + (i // 3) * 0.3
        box(s, cx, cy + 0.06, 0.13, 0.13, fill=c, shape='rect', name='legend')
        text(s, cx + 0.22, cy, 3.8, 0.26, [[(names[n] + '  ', {'color': TEXT}), (f'{v:.1f}억 ({v/20*100:.1f}%)', {'color': TEXT2})]], size=9.5)
    text(s, 0.6, 6.45, 12.13, 0.45, [[('추가 재원 (미반영)  ', {'f': 'S', 'color': OR_LIGHT}), ('정부지원금 · 공동개발비는 확정 전이므로 기본 재원에서 제외   ·   ', {}), ('Valuation · 지분율  ', {'f': 'S', 'color': YEL}), ('[투자 조건 입력 필요]', {'color': YEL})],
                                    '인건비는 2026년 시장 수준 · 4대보험 · 퇴직충당 포함 (창업자 연 ₩5,000만, 엔지니어 연 ₩7,000만 기준) · 월별 계획과 손익계산서 연결은 Appendix A12'], size=9, color=TEXT2, ls=1.2)
    footer(s, '15')
    notes(s, f"요청 금액은 Seed 20억원입니다. 이 돈은 시제품 하나를 만드는 개발비가 아니라, 기술 컨셉을 회사로 만드는 자금입니다. "
             f"집행은 18개월 Core Runway와 6개월 Milestone Extension으로 나눴습니다. 18개월까지 약 {SEEDP['core18']:.1f}억원으로 설계 동결과 첫 반복 주문까지 가고, 18개월 Gate를 통과하면 나머지 6개월 {SEEDP['ext6']:.1f}억원을 집행합니다. 예비비 1.7억원은 매출이 0원이어도 24개월을 버틸 수 있게 하는 완충입니다. "
             f"인건비는 창업자 2명을 포함해 8명을 단계적으로 채용하는 기준으로 약 {SEEDP['pers_total']:.1f}억원, 전체의 48%입니다. 기존 계획의 개발인력 9억원은 시장 수준 연봉과 4대보험, 퇴직충당을 넣으면 빠듯해 현실적으로 다시 계산했습니다. "
             "정부지원금과 공동개발비는 확정되지 않았기 때문에 기본 재원에 넣지 않았습니다. 24개월 후 Series A를 받을 수 있는 숫자는 Paid PoC 5건 이상, 반복 고객 2곳 이상, 승인 Task 완료율 95% 이상, 내구성 30만 회, 두 개 로봇 플랫폼에서의 Skill 이식성, 재사용률 상승 추세, BOM 기반 하드웨어 마진입니다. 밸류에이션과 지분 조건은 협의하겠습니다.")

# ================================================================ 16 CLOSING
def s16(prs):
    s = new_slide(prs, '16')
    picture(s, O + '_bg_glow.png', 7.6, -0.6, w=6.6, name='decorative glow')
    picture_fit(s, A + 'closing.png', 9.55, 0.55, 3.3, 5.35, name='SoftHand-4 on cobot rendering')
    pill(s, None, 5.92, None, 0.26, 'CONCEPT RENDERING', right=12.73)
    text(s, 0.6, 0.62, 8, 0.26, 'FOUNDING & SEED INVESTMENT PROPOSAL', size=10.5, f='S', color=OR, spc=200)
    text(s, 0.6, 0.98, 8.6, 0.85, 'ONE HAND. MANY TOOLS.', size=42, f='K', ls=1.0)
    text(s, 0.6, 1.85, 8.6, 0.42, 'Physical AI의 Manipulation Layer로 확장한다', size=19, f='K', color=OR)
    steps = ['기존 생산설비에서 시작합니다', '하나의 Hand로 여러 Task를 수행하고', '고객 프로젝트를 재사용 가능한 Skill로 제품화하고', '동일 Skill을 여러 Robot에서 사용할 수 있음을 증명합니다', 'Robot OEM으로 확장해 Manipulation Layer가 됩니다']
    yy = 2.55
    for i, t in enumerate(steps):
        num_badge(s, 0.6, yy + 0.02, i + 1, d=0.3, size=9.5, fill=OR if i < 4 else CARD3, color='FFFFFF' if i < 4 else OR)
        text(s, 1.05, yy, 5.75, 0.34, t, size=13, f='S' if i < 4 else 'K', color=TEXT if i < 4 else OR_LIGHT)
        yy += 0.56
    # physical AI stack
    xs = 6.95; ws = 2.6; ys = 2.5
    text(s, xs, ys, ws, 0.46, ['보고 판단하는 로봇은 빠르게 발전했다.', '이제 실제 세상을 다루는 능력이 남았다.'], size=9, f='M', color=TEXT, ls=1.15)
    layers = [('BRAIN', 'AI / VLA', '빠르게 발전'), ('EYES', 'Vision / Edge Compute', '상용 수준'), ('BODY', 'Robot Arm / Cobot', '이미 대규모 보급'), ('HAND', '현실세계 Manipulation', '여전히 어려운 문제')]
    yy = ys + 0.6
    for i, (k, d, st) in enumerate(layers):
        hot = k == 'HAND'
        b = box(s, xs, yy, ws, 0.5, fill=OR_FILL if hot else CARD, line=OR if hot else None, lw=1.0, r=0.06)
        text(s, xs + 0.14, yy + 0.12, 0.7, 0.26, k, size=10, f='K', color=OR if hot else TEXT)
        text(s, xs + 0.85, yy + 0.05, ws - 0.95, 0.42, [d, [(st, {'color': OR_LIGHT if hot else MUTED, 'f': 'S' if hot else 'R'})]], size=8.5, color=TEXT, ls=1.05)
        yy += 0.58
    # bottom strip
    y1 = 6.2
    cells = [('SEED ASK', '₩2.0B', True), ('TIMELINE', '24 Months', False), ('PROVE', 'PRODUCT', False), ('PROVE', 'PAID CUSTOMER', False), ('PROVE', 'REPEATABILITY', False), ('PROVE', 'REUSABILITY', False)]
    ws_ = [1.75, 1.85, 1.9, 2.35, 2.25, 2.11]; x = 0.6
    for (k, v, hot), w in zip(cells, ws_):
        box(s, x, y1, w - 0.08, 0.66, fill=OR if hot else CARD, r=0.06, name='strip')
        text(s, x + 0.14, y1 + 0.08, w - 0.3, 0.2, k, size=7.5, f='S', color='FFFFFF' if hot else MUTED, spc=100)
        text(s, x + 0.14, y1 + 0.28, w - 0.3, 0.32, v, size=13.5, f='K', color='FFFFFF' if hot else TEXT)
        x += w
    placeholder(s, 0.6, 7.0, 4.2, 0.3, '[대표자명 · 이메일 · 연락처 입력 필요]', size=9)
    text(s, 11.53, 7.08, 1.2, 0.24, '16', size=9.5, f='S', color=MUTED2, align='r', name='Page number')
    notes(s, "정리하겠습니다. One Hand, Many Tools. 저희는 기존 생산설비에서 시작합니다. 하나의 Hand로 여러 Task를 수행하고, 고객 프로젝트를 재사용 가능한 Skill로 제품화하고, 같은 Skill을 여러 로봇에서 쓸 수 있음을 증명합니다. "
             "그 다음 로봇 OEM으로 확장해 Physical AI의 Manipulation Layer가 되는 것이 장기 목표입니다. 보고 판단하는 로봇의 두뇌와 눈, 몸은 빠르게 발전했지만, 실제 세상을 다루는 손은 여전히 가장 어려운 문제로 남아 있습니다. "
             "저희는 완성된 회사의 성장자금이 아니라 이 회사를 시작하기 위한 Seed 20억원을 요청드립니다. 24개월 안에 제품, 유료 고객, 반복 발주, 그리고 재사용성을 증명하겠습니다. 감사합니다.")
