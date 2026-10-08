# Appendix slides (A0 ~ A23). Mostly table-led; every number carries a Number Tag.
from common import *
from common import M
import drawings as DR

APX = []
def apx(f):
    APX.append(f); return f

def P(code):          # page label for appendix
    return code

TG = ttxt

# ---------------------------------------------------------------- A0 index
@apx
def a00(prs):
    s = start(prs, 'A0', 'A0', 'Appendix 목차', visual='2열 목차', chart='없음',
              note='부록은 본문 숫자의 근거와 계산 과정을 담습니다. 각 부록 번호는 본문에서 참조한 위치입니다.')
    y = head(s, 'APPENDIX', 'Appendix 목차', sub='본문 수치의 근거 · 계산 · 검증 계획. 재무 수식 모델: ARKI_Robotics_Financial_Model.xlsx')
    items = ['A1  Number Tag 원칙과 구분표', 'A2  Housing Data', 'A3  Kitchen Remodeling 시장 · 가격 Reference',
             'A4  Robot Component Benchmark · BOM', 'A5  Kitchen Geometry · 평면 30개 분석 계획', 'A6  Robot Reach · 단면 치수',
             'A7  Safety Architecture · Certification', 'A8  설치 Architecture (구조체 정착 · 전원 · 통신)', 'A9  Competition 상세',
             'A10  IP / Patent Portfolio', 'A11  Household Unit Economics 상세', 'A12  Rental Model',
             'A13  Care · Consumables Model', 'A14  5-Year Financial Model (3 Scenario)', 'A15  Sensitivity Analysis',
             'A16  Seed Use of Funds 검증', 'A17  Customer Validation · 기술 KPI', 'A18  What Must Be True',
             'A19  Risk Register', 'A20~21  VC Red-Team Q&A', 'A22  Investment Scorecard · 판단', 'A23  Sources']
    half = (len(items) + 1) // 2
    for i, it in enumerate(items):
        cx = MX + (i // half) * (CW / 2); cy = y + (i % half) * 0.43
        text(s, cx, cy, CW / 2 - 0.3, 0.38, it, size=12, anchor='m')
        hline(s, cx, cy + 0.41, CW / 2 - 0.3)
    foot(s, 'A0')

# ---------------------------------------------------------------- A1 tags
@apx
def a01(prs):
    cnt = {}
    for d in M['inputs']:
        cnt[d['tag']] = cnt.get(d['tag'], 0) + 1
    rows = [[TG('FACT'), '공식 통계 또는 공개자료로 확인된 값', '총주택 2,018만호 · 아파트 65.8% · 2025 준공 34.2만호 · 1X NEO $20,000', f"{cnt.get('FACT', 0)}개 입력"],
            [TG('DERIVED'), 'FACT를 ARKI가 계산한 값', '아파트 약 1,328만호 · 교체 세대 교차검증 29.0만·30.3만 · 가치 Anchor 월 18만원', '계산 시트 전부'],
            [TG('ASSUMPTION'), '현재 사업가설 (검증 전)', 'Robot ASP 1,490만원 · BOM · Rental 월 33만원 · Premium 10% · 적용률 60%', f"{cnt.get('ASSUMPTION', 0)}개 입력"],
            [TG('TARGET'), 'Seed 기간 또는 이후 목표', '평면 30개 · Template 3~5 · Standard Module 65% · 설치 1일 · Paid Pilot', f"{cnt.get('TARGET', 0)}개 입력 + KPI"],
            [TG('CONCEPT'), '실물 없는 설계 개념', 'Concept Layout A~D · 단면 · Robot Module 구성', '도면·Diagram'],
            [TG('TBV'), '검증 방법이 정해진 미확인 사실', '식세기 보급률 · 벽식 단지 평면 반복성 · Founder 정보', '본문 각주'],
            [TG('FUTURE'), '현재 존재하지 않는 제품', 'V2 ASSIST · V3 COOK · End-effector Tool 확장', 'Roadmap']]
    table_slide(prs, 'A1', 'A1', 'APPENDIX A1', 'Number Tag 원칙과 구분표', ['Tag', '정의', '대표 예시', '적용 범위'], rows,
                [1.45, 3.0, 5.6, 1.78], sub='모든 주요 숫자와 미검증 내용을 7개 Tag로 구분. 전체 입력 목록·Tag·출처: xlsx Inputs 시트, docs/04_Number_Tag_Register.md',
                size=10.5, takeaway='금지: 가상 고객 · 가상 계약 · 가상 LOI · 가상 Partner · 가상 매출 · 근거 없는 점유율 · "최초" · Patent 등록 확정 표현',
                note='본 자료의 모든 숫자는 일곱 가지 Tag 중 하나를 갖습니다. 사실과 가설이 섞이지 않도록 입력 단계부터 Tag를 붙였고, 엑셀 모델의 Inputs 시트에서 전체 목록을 확인할 수 있습니다.')

# ---------------------------------------------------------------- A2 housing
@apx
def a02(prs):
    mk = M['market']['B']
    rows = [['총주택 (2025.11.1)', '2,018.1만호', TG('FACT'), '국가데이터처 2025 인구주택총조사 (2026.7.28)'],
            ['아파트 비중 / 아파트 수', '65.8% / 약 1,328만호', TG('FACT'), '비중 FACT, 호수는 2,018.1만 × 65.8% (DERIVED)'],
            ['준공 20년 이상 / 30년 이상 주택 비중', '56.0% / 30.6%', TG('FACT'), '2025 인구주택총조사'],
            ['아파트 수 · 20년 이상 아파트 (2023)', '1,263만호 · 639만호 (50.7%)', TG('FACT'), '2023 주택총조사 인용 보도'],
            ['주택 준공 (2025)', '34만2,399호 (−17.8%)', TG('FACT'), '국토부 2025.12 주택통계'],
            ['주택 인허가 · 착공 · 공동주택 분양 (2025)', '37만9,834 · 27만2,685 · 19만8,373호', TG('FACT'), '국토부 2025.12 주택통계'],
            ['아파트 인허가 (2025)', '34만6,773가구', TG('FACT'), '국토부 주택통계 인용 보도'],
            ['아파트 입주 2025 / 2026 예정', '23만6,263 / 18만3,124가구', TG('FACT'), '부동산114 REPS'],
            ['주택 매매거래 (2025)', '72.6만호 (10년 평균 88.5만)', TG('FACT'), 'KB주택시장리뷰 (부동산원 자료)'],
            ['연간 Kitchen 교체 세대 교차검증 ①', f"{mk['tri1'] / 10:.1f}만", TG('DERIVED'), '20년+ 아파트 639만 ÷ 교체주기 22년 (ASSUMPTION)'],
            ['연간 Kitchen 교체 세대 교차검증 ②', f"{mk['tri2'] / 10:.1f}만", TG('DERIVED'), '매매 72.6만 × 아파트 70% × 교체율 40% + 비거래 10만 (ASSUMPTION)'],
            ['연간 Kitchen 교체 세대 (설정값)', '30만 세대/년', TG('ASSUMPTION'), '①·② 교차검증 범위 → Seed 기간 Partner 판매 Data로 보정']]
    table_slide(prs, 'A2', 'A2', 'APPENDIX A2', 'Housing Data', ['항목', '값', 'Tag', '출처 / 산식'], rows,
                [3.35, 2.85, 1.25, 4.38], sub='공식 통계는 검색 시점(2026-10-07) 보도 인용 → 외부 제출 전 원문 (국가데이터처·국토부 보도자료) 대조 필요', size=10,
                note='주택 통계는 국가데이터처 2025 인구주택총조사와 국토부 2025년 12월 주택통계를 기준으로 했습니다. 주방 교체 세대 수는 공식 통계가 없어 두 가지 방법으로 교차 추정하고 가정값으로 표시했습니다.')

# ---------------------------------------------------------------- A3 kitchen market
@apx
def a03(prs):
    rows = [['국내 리모델링 시장 (건축물 전체, 비주거 포함)', '2025년 37조원 → 2030년 44조원 (전망)', TG('FACT'), '한국건설산업연구원 전망치 · 주택 Kitchen 단독 규모 아님'],
            ['한샘 리하우스 부문 매출', '2025 1Q 1,147억원 (−4.3%)', TG('FACT'), '분기 실적 보도'],
            ['프리미엄 Kitchen 시장 구성', '약 90%가 수입 · 고가 맞춤', TG('FACT'), '한샘 발표 인용 보도 (2025.7)'],
            ['키친바흐 · 밀레 연계 부엌 매출', '+17% (2025.6 기준) · +173% (2024 대비)', TG('FACT'), '회사 발표 인용 보도 — 빌트인 가전 통합 수요 신호'],
            ['30평대 전체 리모델링 (스타일패키지)', '평당 100만원대 → 약 3,000만원', TG('FACT'), '2019 보도 · 가격 시점 오래됨'],
            ['신축 유상옵션 비용 / 분양가', '평균 9.7% (분양가상한제 7개 단지)', TG('FACT'), '보도 · 옵션 선택 문화 근거'],
            ['식기세척기 보급률', '10%대 초반 (2019~2020 업계 추정)', TG('TBV'), '최신 공식 통계 확인 안 됨 → 소비자 조사로 확인'],
            ['Kitchen 단독 교체 가격대: 일반', '600~1,500만원', TG('ASSUMPTION'), '공식 자료 없음 → 90일 내 견적 20건 수집 (TBV)'],
            ['Kitchen 단독 교체 가격대: Premium', '2,000~4,000만원 (빌트인 가전 포함 시 상향)', TG('ASSUMPTION'), 'Beachhead 정의 기준 · 견적으로 검증'],
            ['Robot-ready 증분가 / Kitchen 공사비', '450만원 / Premium 2,000~4,000만원 → 11~23%', TG('DERIVED'), '증분 부담률 = WTP 조사 핵심 문항']]
    table_slide(prs, 'A3', 'A3', 'APPENDIX A3', 'Kitchen Remodeling 시장 · 가격 Reference', ['항목', '값', 'Tag', '비고'], rows,
                [3.4, 3.6, 1.25, 3.58], sub='Kitchen 단독 Remodeling 가격의 공식 통계 부재 → 가격가설은 ASSUMPTION, Seed 첫 90일 견적 수집으로 대체', size=10,
                takeaway='Premium Kitchen + 빌트인 가전 통합 수요는 공개 실적으로 확인 (FACT). 단, Robot Integration Premium 지불 여부는 별개 → WTP 조사 필요',
                note='Kitchen 단독 리모델링 가격은 공식 통계가 없습니다. 그래서 일반과 Premium 가격대는 가정으로 표시했고, 첫 90일 안에 한샘, 리바트, 지역 업체 견적 20건을 모아 대체합니다. 빌트인 가전과 주방가구를 통합하려는 수요는 한샘 실적에서 확인됩니다.')

# ---------------------------------------------------------------- A4 component benchmark & BOM
@apx
def a04(prs):
    fx = 1400
    s = start(prs, 'A4', 'A4', 'Robot Component Benchmark · BOM', visual='좌측 공개가 Benchmark 표 (USD→원화 환산), 우측 BOM Pilot/Y3/Y5 표 (ASSUMPTION, 합계는 재무모델과 일치).',
              chart='표 2개',
              note='Robot BOM은 공개가 부품을 기준으로 추정했습니다. Pilot 단계는 1,600만원, Series A 이후 1,150만원, Y5에 900만원으로 내려간다고 가정했습니다. 가장 큰 항목은 Arm이며, Y5 450만원은 OEM Partner나 전용 Arm 개발이 필요한 공격적 가정입니다.')
    y = head(s, 'APPENDIX A4', 'Robot Component Benchmark · BOM',
             sub='Benchmark = 공개 판매가 (FACT, 환율 1,400원/USD ASSUMPTION). BOM = ASSUMPTION, 재무모델 Base BOM과 합계 일치 (model.py assert).')
    bm = [['UR3e (3kg)', '$23k~33k', f"{23000 * fx / 1e4:,.0f}~{33000 * fx / 1e4:,.0f}", '유통가'],
          ['Doosan E0509 (5kg)', '약 $22k', f"{22000 * fx / 1e4:,.0f}", 'Aggregator'],
          ['UFACTORY xArm 6 (5kg, 700mm)', '$8,399', f"{8399 * fx / 1e4:,.0f}", 'RobotShop'],
          ['FAIRINO FR5 (5kg, 922mm)', '$6,999', f"{6999 * fx / 1e4:,.0f}", '판매가'],
          ['UFACTORY Lite 6 (0.6kg)', '$4,482 (Kit)', f"{4482 * fx / 1e4:,.0f}", '가반 부족'],
          ['Robotiq 2F-85 / OnRobot RG2', '$4,999 / 약 $3,200', f"{4999 * fx / 1e4:,.0f} / {3200 * fx / 1e4:,.0f}", '판매가'],
          ['Robotiq Fingertip', '$175~195', f"{175 * fx / 1e4:,.0f}~{195 * fx / 1e4:,.0f}", 'Consumable 참고'],
          ['Orbbec Gemini 335 / RealSense D405', '$384~400 / $514', f"{384 * fx / 1e4:,.0f} / {514 * fx / 1e4:,.0f}", '판매가'],
          ['Piab Food-grade Cup', '£7~20', '1~4', 'FDA 21 CFR 177.2600']]
    lw = 6.0
    table(s, MX, y, lw, ['Benchmark (FACT)', 'USD', '만원', '비고'], bm, col_w=[2.45, 1.35, 1.05, 1.15], size=9.5,
          align=['l', 'r', 'r', 'l'], label='bench', max_h=4.4)
    rx = MX + lw + 0.3; rw = W - MX - rx
    rows = [[r[0], f"{r[1]:,}", f"{r[2]:,}", f"{r[3]:,}"] for r in M['bom_breakdown']]
    tot = [sum(r[i] for r in M['bom_breakdown']) for i in (1, 2, 3)]
    rows.append([('합계 (재무모델 BOM)', {'bold': True}), (f"{tot[0]:,}", {'bold': True}), (f"{tot[1]:,}", {'bold': True}), (f"{tot[2]:,}", {'bold': True, 'color': T['accent']})])
    table(s, rx, y, rw, ['BOM (ASSUMPTION, 만원/대)', 'Pilot', 'Y3', 'Y5'], rows, col_w=[rw - 2.25, 0.75, 0.75, 0.75], size=9.5,
          align=['l', 'r', 'r', 'r'], label='bom', max_h=4.4)
    statement(s, MX, 6.05, CW, 'BOM 하락 경로 = 수량 + Arm OEM Partner (국산·중국산 Cobot) + 전용 경량 Arm (Series A 이후). Y5 Arm 450만원은 공격적 가정 → Sensitivity 2순위 변수 (A15)',
              size=11)
    foot(s, 'A4')

# ---------------------------------------------------------------- A5 geometry / 30 plans
@apx
def a05(prs):
    s = start(prs, 'A5', 'A5', 'Kitchen Geometry · 평면 30개 분석 계획', visual='좌측 표본 설계 Matrix (신축/구축 × Bay × 평형). 우측 분석 항목과 산출물, 자료 확보 방법.',
              chart='Matrix 표',
              note='평면 분석은 Seed 첫 3개월의 핵심 과업입니다. 신축 15개, 구축 15개를 평형과 Bay 구성별로 골고루 뽑고, 공개 분양 평면과 동의를 받은 실측을 함께 씁니다. 결과물은 Layout Family, Template, Coverage 비율입니다.')
    y = head(s, 'APPENDIX A5', 'Kitchen Geometry · 평면 30개 분석 계획',
             sub='표본 = TARGET. 자료: 입주자모집공고 평면 (공개) + 리모델링 상담 고객 동의 실측. 특정 단지 도면은 공개 자료 범위에서만 사용.')
    hdr = ['구분', '59㎡', '74㎡', '84㎡', '101㎡+', '계']
    rows = [['구축 2Bay', '3', '1', '2', '—', '6'], ['구축 3Bay', '2', '2', '3', '1', '8'], ['구축 4Bay', '—', '—', '1', '—', '1'],
            ['신축 3Bay', '2', '2', '3', '1', '8'], ['신축 4Bay', '1', '1', '3', '2', '7'],
            [('합계', {'bold': True}), ('8', {'bold': True}), ('6', {'bold': True}), ('12', {'bold': True}), ('4', {'bold': True}), ('30', {'bold': True, 'color': T['accent']})]]
    lw = 5.3
    table(s, MX, y, lw, hdr, rows, col_w=[1.4, 0.75, 0.75, 0.75, 0.9, 0.75], size=10.5, align=['l', 'c', 'c', 'c', 'c', 'c'], label='matrix', max_h=2.6)
    kit.tag(s, MX, y + 2.55, 'TARGET')
    text(s, MX, y + 2.85, lw, 1.2, ['84㎡ 비중 확대: 국민평형 · Mock-up 기준', '구축은 1990~2000년대 준공 판상형 중심 (교체 수요)',
                                     '신축은 4Bay · 대면형 · Island 포함'], size=10, color=T['text2'], bullet='–', space_after=2)
    rx = MX + lw + 0.35; rw = W - MX - rx
    items = [['Kitchen Geometry', '일자 / 11자 / ㄱ자 / ㄷ자 / Island · 대면형'],
             ['설비 위치', 'Sink · 식세기 · IH · 냉장고 · 키큰장 · 상부장'],
             ['치수', 'Run 길이 · Aisle Width · 상부장 하단 높이 · 천장고'],
             ['구조 제약', '벽체 구조 (RC 벽식 / 조적 / 경량) · 배관 Shaft · 창호'],
             ['Robot', 'Home 후보 · Reach Coverage (Sink·식세기·수납) · 동선 간섭'],
             ['산출', 'Layout Family 3~5 · Template A/B/C · Template별 Coverage % · Site Adjustment 항목']]
    table(s, rx, y, rw, ['분석 항목', '내용'], items, col_w=[1.55, rw - 1.55], size=10, bold_first_col=True, label='items', max_h=3.2)
    statement(s, MX, 5.95, CW, '성공 기준 (TARGET): 상위 3개 Template이 표본의 70% 이상 Cover · Template당 Site Adjustment 항목 5개 이하  |  실패 시: Architecture 수 확대 또는 Beachhead 평형 축소',
              size=11)
    foot(s, 'A5')

# ---------------------------------------------------------------- A6 reach / section
@apx
def a06(prs):
    s = start(prs, 'A6', 'A6', 'Robot Reach · 단면 치수', visual='좌측 Kitchen 단면 CONCEPT (Counter 850 · 상부장 1,450~2,250 · Rail · 역설치 Arm Reach R700 · Human Zone). 우측 핵심 치수 표 (FACT/ASSUMPTION/TBV).',
              chart='단면 Diagram + 치수표',
              note='상부장 하단 Rail에 매단 Arm의 Reach를 700mm로 가정하면 작업대 상판과 Sink 바닥까지는 닿지만, 바닥 근처 식세기 하단 Rack까지는 어렵습니다. 그래서 식세기를 키큰장 안에 허리 높이로 올리는 것이 핵심 설계 규칙입니다. 치수는 업계 통상값이며 실측으로 검증합니다.')
    y = head(s, 'APPENDIX A6', 'Robot Reach · 단면 치수',
             sub='CONCEPT 단면. 치수는 국내 Kitchen 통상 치수 기반 개념값 → 평면 30개 실측으로 검증 (TBV).')
    DR.section(s, MX + 0.75, y + 0.1, 4.8, 4.2, detail=True)
    kit.tag(s, MX, y + 4.45, 'CONCEPT')
    rx = MX + 6.0; rw = W - MX - rx
    rows = [['작업대 높이', '850mm (통상)', TG('TBV')], ['상부장 하단 / 상단', '1,450 / 2,250mm', TG('TBV')], ['천장고 (구축)', '약 2,300~2,400mm', TG('TBV')],
            ['통로 (11자형 Aisle)', '900~1,200mm', TG('TBV')], ['Arm Reach (5kg급)', '700mm (xArm 6) · 922mm (FR5)', TG('FACT')],
            ['가반하중 요구 (EE 포함)', '1.5kg 이상 (접시·국그릇)', TG('ASSUMPTION')], ['식세기 Rack 높이 (상향 배치)', '약 450~1,050mm', TG('ASSUMPTION')],
            ['Sink 바닥 깊이', '상판 −200~250mm', TG('TBV')], ['Robot 통로 위 운반', '금지 (사람 존재 시)', TG('ASSUMPTION')]]
    table(s, rx, y, rw, ['항목', '값', 'Tag'], rows, col_w=[2.3, rw - 3.45, 1.15], size=10, label='dims', max_h=3.9)
    statement(s, rx, 5.75, rw, '바닥형 식세기 하단 Rack (약 150~300mm)은 역설치 Arm Reach 밖 → 식세기 상향 배치 또는 Z축 Lift 필요', size=10.5)
    foot(s, 'A6')

# ---------------------------------------------------------------- A7 safety
@apx
def a07(prs):
    s = start(prs, 'A7', 'A7', 'Safety Architecture · Certification', visual='좌측 Safety 기능 표 (Zone·Speed·Force·Payload·Fail-safe). 우측 적용 표준·인증 표 (단계별).',
              chart='표 2개',
              note='머리 위 Robot의 안전은 투자자가 반드시 묻는 질문입니다. 원칙은 사람이 있는 Zone 위로 물건을 운반하지 않고, 사람이 Robot Zone에 들어오면 즉시 정지하며, 가반하중과 속도를 낮게 제한하는 것입니다. 2025년 개정된 ISO 10218에 협동 안전 요구사항이 통합되었고, 가정용은 ISO 13482와 KC 전기안전, 전자파, 식품용 기구 기준을 함께 봐야 합니다. 본인증은 Series A 단계로 계획했습니다.')
    y = head(s, 'APPENDIX A7', 'Safety Architecture · Certification',
             sub='원칙: 사람 위 운반 금지 · Zone 진입 시 정지 · 저속 · 저가반 · 고장 시 일반 Kitchen. 인증 경로는 전문기관 사전상담으로 확정 (TBV).')
    lw = 6.1
    rows = [['Zone 분리', 'Robot / Human / No-go Zone 고정 · Rail 이동범위 기계적 Stopper'],
            ['Zone 감시', 'ToF·Radar Zone Sensor → Human 진입 시 Safety-rated Monitored Stop'],
            ['속도·힘 제한', 'Human 근접 시 저속 · PFL (Power & Force Limiting)'],
            ['Payload 제한', 'V1 운반 1.5kg 이하 · 칼·뜨거운 용기 제외'],
            ['낙하 대응', 'Grip Loss 감지 · 통로 위 운반 금지 · Counter 위 저고도 이동'],
            ['Fail-safe', '정전·고장 시 Garage 복귀 또는 정지 · 수동 해제 · 일반 Kitchen 사용 유지'],
            ['접근 제어', 'Child Lock · Garage Door Interlock · 원격 정지']]
    table(s, MX, y, lw, ['기능', 'Concept 설계'], rows, col_w=[1.4, lw - 1.4], size=10, bold_first_col=True, label='safety', max_h=3.9)
    kit.tag(s, MX, y + 3.45, 'CONCEPT')
    rx = MX + lw + 0.3; rw = W - MX - rx
    std = [['ISO 10218-1/-2:2025', '로봇·Robot 응용 안전. TS 15066 협동 요구 통합 (2025.2)', 'Seed: 설계 기준'],
           ['ISO 13482', 'Personal Care Robot 안전 (국내 인증 사례 존재)', 'A: 적용성 검토'],
           ['IEC 60335-1 / KC', '가정용 전기기기 안전 · 전기용품안전관리법', 'A: 본인증'],
           ['KC 전자파 (EMC)', '전파법 적합성평가', 'A: 본인증'],
           ['ISO 13849-1', '안전기능 PL (목표 PL d, ASSUMPTION)', 'Seed: 설계'],
           ['식품용 기구 기준', '식품접촉 Tip·Pad 재질 (식약처 기준 및 규격)', 'Seed: 재질 선정']]
    table(s, rx, y, rw, ['표준 · 인증', '내용', '시점'], std, col_w=[1.55, rw - 2.75, 1.2], size=9.5, label='std', max_h=3.9)
    statement(s, MX, 5.95, CW, 'Seed 범위: Risk Assessment · 설계 기준 적용 · 예비시험 (비용 ASSUMPTION 0.7억원 내외)  |  본인증: Series A (A16). 인증기간이 Launch 일정 Risk',
              size=11)
    foot(s, 'A7')

# ---------------------------------------------------------------- A8 installation
@apx
def a08(prs):
    s = start(prs, 'A8', 'A8', '설치 Architecture: 구조체 정착 · 전원 · 통신', visual='좌측 Load Path Diagram (Arm → Carriage → Rail → 보강 Frame → Anchor → RC 벽체). 우측 설치 검토 표 (구조·전기·통신·설비) + 설치 순서.',
              chart='Load Path Flow + 표',
              note='Rail형 설치에서 Robot 하중은 상부장이 아니라 보강 Frame을 거쳐 구조체로 전달되어야 합니다. 동하중과 반복하중을 고려해 Anchor를 설계하고, 구축은 벽체가 철근콘크리트인지, 조적이나 경량벽인지 실측 단계에서 확인합니다. 이 검토 절차 자체가 설치 Standard이자 Partner 교육 내용입니다.')
    y = head(s, 'APPENDIX A8', '설치 Architecture: 구조체 정착 · 전원 · 통신',
             sub='Robot 하중은 가구가 아닌 구조체로 전달. 구축은 벽체 유형 실측 확인이 설치 가능 여부의 1차 Gate (Robot-ready 적용 가능률 60% 가정의 근거 항목).')
    steps = ['Arm · Payload\n(동하중 포함)', 'Carriage\n· Rail', '보강 Steel\nFrame', 'Post-installed\nAnchor', 'RC 벽체 ·\n슬래브']
    flow(s, MX, y, CW, steps, h=0.75, gap=0.3, size=11, fills=[T['soft'], T['soft'], T['text'], T['text'], T['accent_soft']],
         colors=[T['text'], T['text'], 'FFFFFF', 'FFFFFF', T['text']])
    rows = [['구조', '설계하중 = (Arm + Carriage + Payload) × 동적계수 · 피로 (반복 이동)', '콘크리트용 앵커 설계기준 (KDS 14 20 54) · ACI 318 Ch.17 참조', TG('ASSUMPTION')],
            ['벽체 유형', 'RC 벽식 → 직접 정착 / 조적·경량벽 → 바닥·천장 지지 Frame 또는 Dock Type 전환', '실측 단계 판정 · 내력벽 손상 금지', TG('TBV')],
            ['처짐·진동', 'Rail 처짐 · 공진 → 위치정밀도 · 소음 영향', 'Mock-up 계측 (가속도·변위)', TG('TARGET')],
            ['전기', '전용 회로 · 누전차단 · Garage 내 전원', '전기설비규정 (KEC) 기준 시공 (Partner)', TG('CONCEPT')],
            ['통신', '유선 Ethernet / PoE + Wi-Fi 보조 · 원격진단', '세대 내 통신 단자 위치', TG('CONCEPT')],
            ['설비', '식세기 상향 Housing 급·배수 · 환기', '배관 Partner 시공', TG('CONCEPT')]]
    table(s, MX, y + 1.0, CW, ['검토', '내용', '기준 · 방법', 'Tag'], rows, col_w=[1.2, 5.3, 4.1, 1.23], size=10, bold_first_col=True,
          label='install', max_h=3.2)
    statement(s, MX, 6.0, CW, '설치 순서 (TARGET): 실측 · 벽체 판정 → Partner 철거·가구·전기 → ARKI Frame·Rail → Robot 장착 → Auto Calibration → Safety Check → 인수  |  Robot Module 설치 1일 · 2인 (M24)',
              size=10.5)
    foot(s, 'A8')

# ---------------------------------------------------------------- A9 competition detail
@apx
def a09(prs):
    rows = [['1X NEO', 'Humanoid', '$20,000 또는 월 $499 (최소 6개월) · 2026 출하', '원격조종 학습 병행 · 범용 가사', TG('FACT')],
            ['Sunday Robotics Memo', 'Wheeled Mobile', '2026 베타 약 50가구 · 양산 $10k 미만 목표', '식세기 적재·테이블 정리 시연', TG('FACT')],
            ['LG CLOiD', 'Wheeled Humanoid', 'CES 2026 공개 · 가격 미공개', '식세기 비우기·세탁 시연 · LG 가전 연동', TG('FACT')],
            ['Figure 03', 'Humanoid', '가격 미공개 (RaaS 언급)', '가사 시연 (빨래·설거지)', TG('FACT')],
            ['Tesla Optimus', 'Humanoid', '소비자 목표 $20~30k · 2027 전후', '범용', TG('FACT')],
            ['Samsung Bot Handy', 'Mobile Manipulator', 'CES 2021 Concept · 출시 미공개', '식기 정리 시연', TG('FACT')],
            ['Moley', 'Built-in Robotic Kitchen', 'Arm 포함 £248,000 / 제외 £128~140k', '천장 Rail 양팔 · 조리', TG('FACT')],
            ['Samsung Bot Chef', 'Built-in (Concept)', 'CES 2020 Concept', '상부장 하단 Rail 양팔 조리 시연', TG('FACT')],
            ['Posha', 'Countertop Cooking', '$1,750 (선주문 $1,500) + 월 $15', '자동 투입·젓기 조리기', TG('FACT')],
            ['국내 Food-tech (로보아르테 · 웨이브 등)', 'Commercial Cobot', '상업 주방 · 매장 자동화', '가정용 아님', TG('FACT')],
            ['ARKI', 'Built-in Kitchen Integration', 'Concept 단계 · 실적 없음', 'Clean-up · 공동주택 Template · 설치 Standard', TG('CONCEPT')]]
    table_slide(prs, 'A9', 'A9', 'APPENDIX A9', 'Competition 상세', ['Player', 'Category', '가격 · 상태', '접근', 'Tag'], rows,
                [2.6, 1.95, 3.35, 2.75, 1.18], sub='공개 보도 기준 (A23 Sources). 성능 비교는 공개 Data 부재로 하지 않음. "최초 · 압도적" 주장 없음.', size=9.5,
                takeaway='시사점: 범용 Mobile·Humanoid가 월 $499 수준 구독가를 제시 → ARKI는 고정 설치형의 신뢰성 · 바닥 점유 0 · Kitchen 일체 디자인 · 설치·A/S로 차별화해야 함 (미검증)',
                note='가정용 Robot 시장은 2025년 이후 빠르게 움직이고 있습니다. 1X는 월 499달러 구독을 내놓았고, Sunday와 LG는 식기세척기 작업을 시연했습니다. ARKI가 같은 가격대에서 선택받으려면 고정 설치형의 신뢰성, 바닥을 차지하지 않는 점, 주방과 일체화된 디자인, 설치와 A/S가 실제로 더 낫다는 것을 증명해야 합니다.')

# ---------------------------------------------------------------- A10 IP
@apx
def a10(prs):
    rows = [['1', '주방가구 일체형 Robot Rail · Dock · Storage', '상부장 하단 Rail + Garage 일체 구조 · 하중 전달', '높음 (모든 Rail형)', '높음 — 천장 Rail 로봇주방 (Moley) · Under-cabinet Rail (Bot Chef)'],
            ['2', 'Robot-ready Kitchen Interface Module', '표준 Mount · 전원 · 통신 · Sensor Interface 규격', '높음 (Land 상품)', '중간 — 가구 Interface · 가전 Built-in 규격'],
            ['3', 'Fold / Deploy Robot Storage', '키큰장 내 수납·전개 기구', '중간 (Compact)', '중간 — 가전 Lift · 수납형 Robot'],
            ['4', 'Human / Robot Zone Safety Control', '주방 Zone Map 기반 정지·감속 Logic', '높음', '높음 — 산업 SSM · 협동 Robot 안전'],
            ['5', 'Kitchen End-effector', '식기 형상 (밥공기·국그릇) 대응 Gripper·Suction', '중간', '중간 — 식품 Gripper'],
            ['6', 'Food-contact Consumable Cartridge', '교체형 Tip · Pad 체결 구조 · 교체주기 인식', '중간 (반복매출)', '중간 — 교체형 Gripper Pad'],
            ['7', 'Installation Auto Calibration', '설치 후 Target 기반 자동 좌표 보정', '높음 (설치시간)', '중간 — Robot Calibration 일반'],
            ['8', 'Dishwasher Robot Interface', 'Door · Rack 위치 표준 · 상향 Housing 연동', '높음', '중간 — 가전사 Robot 연동 특허 가능성'],
            ['9', 'Robot Cleaning / Sanitizing Dock', 'Garage 내 EE 세척·건조', '중간 (위생)', '낮음~중간'],
            ['10', 'Layout 기반 Robot Module Selection', '평면 분류 → Architecture·Module 자동 선택 Software', '중간 (표준화)', '낮음~중간 — 설계 자동화 SW']]
    table_slide(prs, 'A10', 'A10', 'APPENDIX A10', 'IP / Patent Portfolio 후보 (10 Family)', ['#', 'Family', 'Protectable Core', 'Business Relevance', 'Prior Art Risk (선행기술조사 필요)'], rows,
                [0.35, 2.75, 3.3, 1.65, 3.78], sub='등록 가능성 주장 없음. M3까지 선행기술조사 (KIPRIS · USPTO · EPO) → TIPS 24개월 출원 5건 우선순위 결정. 전체 = TBV',
                size=9.5, takeaway='출원 우선순위 가설: ② Interface Module · ⑦ Auto Calibration · ⑧ Dishwasher Interface — 사업 핵심이면서 선행 위험이 상대적으로 낮을 것으로 추정 (TBV)',
                note='특허 후보 열 개를 사업 관련성과 선행기술 위험으로 정리했습니다. Rail 일체형 구조는 Moley나 삼성 Bot Chef 같은 선례가 있어 선행기술 위험이 높습니다. 표준 Interface, 자동 Calibration, 식기세척기 Interface가 사업 핵심이면서 상대적으로 위험이 낮을 것으로 보지만, 모두 선행기술조사 후 판단합니다.')

# ---------------------------------------------------------------- A11 household detail
@apx
def a11(prs):
    h = M['household']; k3, k5, r3, r5 = h['purchase_direct_Y3'], h['purchase_direct_Y5'], h['rental_direct_Y3'], h['rental_direct_Y5']
    def r(lab, f, bold=False):
        vals = [f(x) for x in (k3, k5, r3, r5)]
        cell = lambda v: (f"{v:,.0f}" if isinstance(v, (int, float)) else v, {'bold': bold})
        return [(lab, {'bold': bold})] + [cell(v) for v in vals]
    g = lambda d, k: d.get(k, 0)
    rows = [r('Robot-ready Kitchen 증분', lambda d: g(d['R'], 'kitchen')), r('설치·Calibration', lambda d: g(d['R'], 'comm')),
            r('Robot (구매)', lambda d: g(d['R'], 'robot')), r('Rental 60개월', lambda d: g(d['R'], 'rental')),
            r('Care Basic 5년', lambda d: g(d['R'], 'care')), r('Consumables 5년', lambda d: g(d['R'], 'cons')),
            r('Software · Tool (기대값)', lambda d: g(d['R'], 'sw') + g(d['R'], 'tool')), r('5년 매출', lambda d: d['rev5'], True),
            r('Kitchen Module 원가', lambda d: g(d['C'], 'kitchen')), r('Robot BOM (Rental: 순감가)', lambda d: g(d['C'], 'robot')),
            r('Rental 금융비용', lambda d: g(d['C'], 'finance')), r('설치·물류·Warranty', lambda d: g(d['C'], 'comm') + g(d['C'], 'log') + g(d['C'], 'warranty')),
            r('Care 원가 5년', lambda d: g(d['C'], 'care')), r('Consumables·Upgrade 원가', lambda d: g(d['C'], 'cons') + g(d['C'], 'sw') + g(d['C'], 'tool')),
            r('획득비용 (CAC)', lambda d: g(d['C'], 'channel')), r('Lifetime Contribution', lambda d: d['contrib5'], True),
            r('Contribution Margin', lambda d: f"{d['cm5'] * 100:.1f}%", True)]
    table_slide(prs, 'A11', 'A11', 'APPENDIX A11', 'Household Unit Economics 상세 (1세대 · 5년 · 만원)', ['항목', '구매 Y3', '구매 Y5', 'Rental Y3', 'Rental Y5'], rows,
                [4.4, 1.85, 1.85, 1.85, 1.88], sub='구축 Premium · 직접판매 · Base. Y3/Y5 = 해당 연도 원가 수준을 5년 적용. 전부 DERIVED (from ASSUMPTION). xlsx Household 시트와 동일.',
                size=9, align=['l', 'r', 'r', 'r', 'r'], pad=0.025,
                note='한 세대 경제성의 상세 계산입니다. 구매 모델은 Robot 매출이 대부분이고, Rental 모델은 같은 Robot을 60개월 동안 회수합니다. Rental은 잔존가치를 15% 회수한다고 보고 순감가와 금융비용을 원가로 넣었습니다.')

# ---------------------------------------------------------------- A12 rental
@apx
def a12(prs):
    r3, r5 = M['rental']['Y3'], M['rental']['Y5']; pi = M['partner_irr']['B']; c3 = M['rental_C']['Y3']
    s = start(prs, 'A12', 'A12', 'Rental Model: 월 요금 Build-up · Payback · Partner 구조', visual='좌측 월 원가 Build-up 표 (Y3/Y5). 우측 Partner 구조 경제성 (매입가·월 순유입·IRR) + Seed/Scale 단계 구분.',
              chart='표 + 구조 Diagram',
              note=(f"Rental 요금은 원가에서 출발했습니다. Y3 원가 수준에서 감가, 금융, Care, Grip, Reserve를 합치면 월 {r3['cost_m']:.1f}만원이고 33만원 요금에서 마진은 {r3['margin']:.0%}입니다. "
                    f"Payback은 {r3['payback']:.0f}개월로 36개월을 넘어서, Y3 원가로는 렌탈사가 자산을 사기 어렵습니다. Y5 원가에서는 {r5['payback']:.0f}개월입니다. "
                    f"Partner가 ASP의 88%에 Robot을 사고 월 27만원을 받으면 연 IRR이 약 {pi['irr_y']:.0%}로 계산되지만, 고객 연체와 중도해지는 반영하지 않았습니다."))
    y = head(s, 'APPENDIX A12', 'Rental Model: 월 요금 Build-up · Payback · Partner 구조',
             sub='Rental = 초기부담 감소 수단. ARKI의 장기 자산보유 지양 → Seed는 직접 Pilot, Scale은 Rental / Capital Partner. 전부 DERIVED (from ASSUMPTION).')
    L = r3['lines']; L5 = r5['lines']
    rows = [['감가 (BOM × 85% ÷ 60)', f"{L['dep']:.1f}", f"{L5['dep']:.1f}"], ['금융비용 (평균잔액 × 8% ÷ 12)', f"{L['fin']:.1f}", f"{L5['fin']:.1f}"],
            ['Care 원가 ÷ 12', f"{L['care']:.1f}", f"{L5['care']:.1f}"], ['Grip Kit 원가 ÷ 12', f"{L['grip']:.1f}", f"{L5['grip']:.1f}"],
            ['Failure Reserve (BOM × 4% ÷ 60)', f"{L['reserve']:.1f}", f"{L5['reserve']:.1f}"],
            [('월 원가', {'bold': True}), (f"{r3['cost_m']:.1f}", {'bold': True}), (f"{r5['cost_m']:.1f}", {'bold': True})],
            ['월 요금 (가정)', f"{r3['fee']:.1f}", f"{r5['fee']:.1f}"],
            [('월 Contribution · Margin', {'bold': True}), (f"{r3['contrib_m']:.1f} · {r3['margin']:.0%}", {'bold': True}), (f"{r5['contrib_m']:.1f} · {r5['margin']:.0%}", {'bold': True, 'color': T['accent']})],
            ['마진 20% 확보 요금', f"{r3['fee_at_20']:.1f}", f"{r5['fee_at_20']:.1f}"],
            [('Payback (개월)', {'bold': True}), (f"{r3['payback']:.0f}", {'bold': True, 'color': T['accent']}), (f"{r5['payback']:.0f}", {'bold': True})],
            ['36개월 Payback 최대 BOM', f"{r3['bom_max']:,.0f}", f"{r5['bom_max']:,.0f}"]]
    lw = 6.2
    table(s, MX, y, lw, ['만원 / 월 (Robot 1대)', 'Y3 원가', 'Y5 원가'], rows, col_w=[lw - 2.2, 1.1, 1.1], size=10, align=['l', 'r', 'r'], label='rent', max_h=4.3)
    rx = MX + lw + 0.35; rw = W - MX - rx
    rect(s, rx, y, rw, 2.1, fill=T['soft'])
    text(s, rx + 0.2, y + 0.12, rw - 0.4, 0.3, 'Rental Partner 경제성 (Base, Y4~)', size=12, bold=True)
    text(s, rx + 0.2, y + 0.5, rw - 0.4, 1.55, [f"Robot 매입가: ASP × 88% = {pi['price']:,.0f}만원", f"월 순유입: 요금 33 − ARKI 서비스료 6 = {pi['inflow']:.0f}만원 × 60개월",
                                                  f"잔존가치 15% = {pi['resid']:,.0f}만원 → 연 IRR 약 {pi['irr_y'] * 100:.1f}% (연체·해지 미반영)",
                                                  f"Conservative (월 29만원): IRR 약 {M['partner_irr']['C']['irr_y'] * 100:.1f}%"],
         size=10, color=T['text2'], bullet='–', space_after=3)
    kit.tag(s, rx + rw - 1.0, y + 0.15, 'DERIVED')
    rows2 = [['Seed (Y1~Y3)', 'ARKI 직접 Rental Pilot (소량) · 자산 = Opex·Capex', '요금·해지율·A/S 실측'],
             ['Scale (Y4~)', 'Rental / Capital Partner가 자산 보유 · ARKI는 Product·Software·Care', 'ARKI Balance Sheet 경량화']]
    table(s, rx, y + 2.3, rw, ['단계', '구조', '목적'], rows2, col_w=[1.15, rw - 2.85, 1.7], size=9.5, label='rent2', max_h=1.6)
    statement(s, MX, 6.0, CW, f"결론: Rental은 Y3 원가에서 Payback {r3['payback']:.0f}개월로 Partner 허들(36개월) 미달 → BOM ≤ {r3['bom_max']:,.0f}만원 달성 전까지 Rental은 Pilot 규모로 제한. Conservative 요금(월 29만원) 시 Y3 Payback {c3['payback']:.0f}개월",
              size=10.5)
    foot(s, 'A12')

# ---------------------------------------------------------------- A13 care & consumables
@apx
def a13(prs):
    c3, c5 = M['care']['Y3'], M['care']['Y5']; cons = M['cons']
    s = start(prs, 'A13', 'A13', 'Care · Consumables Model', visual='좌측 Care 원가 구조 표 (Y3/Y5) + 포함 서비스. 우측 Consumables Kit 표 (구성·가격·교체주기·연 매출·원가) + 검증 KPI.',
              chart='표 2개',
              note=(f"Care는 단순 Software 구독이 아니라 Robot 수명주기 유지보수 계약입니다. 연 48만원에 정기점검 2회, Calibration, 원격진단, Update, A/S 공임을 포함합니다. "
                    f"Y3에는 방문 원가 때문에 마진이 {c3['margin']:.0%}이고, 원격진단으로 방문을 줄이고 지역 밀도가 올라가는 Y5에 {c5['margin']:.0%}가 됩니다. "
                    '소모품은 억지 Lock-in이 아니라 위생과 Grip 성능, 식품접촉부 교체 관점에서 설계합니다. 교체주기는 실측 전 가정입니다.'))
    y = head(s, 'APPENDIX A13', 'Care · Consumables Model',
             sub='Care = Robot Lifecycle Maintenance Contract (Software 구독 아님). Consumables = 위생 · 마모 · Grip 성능 · 식품접촉부 교체 · 안전 유지 목적.')
    lw = 5.5
    rows = [['Care Basic 연 요금', f"{c3['fee']:.0f}", f"{c5['fee']:.0f}", TG('ASSUMPTION')],
            ['정기 방문 (횟수 × 원가)', f"{c3['visits']:.1f}", f"{c5['visits']:.1f}", TG('ASSUMPTION')],
            ['고장 방문 (0.6회 × 18만원)', f"{c3['corrective']:.1f}", f"{c5['corrective']:.1f}", TG('ASSUMPTION')],
            ['Cloud · Software', f"{c3['cloud']:.1f}", f"{c5['cloud']:.1f}", TG('ASSUMPTION')],
            [('Care Contribution · Margin', {'bold': True}), (f"{c3['contrib']:.1f} · {c3['margin']:.0%}", {'bold': True}), (f"{c5['contrib']:.1f} · {c5['margin']:.0%}", {'bold': True, 'color': T['accent']}), TG('DERIVED')]]
    table(s, MX, y, lw, ['Care (만원/대·년)', 'Y3', 'Y5', 'Tag'], rows, col_w=[2.6, 0.95, 0.95, 1.0], size=10, align=['l', 'r', 'r', 'l'], label='care', max_h=2.7)
    text(s, MX, y + 2.75, lw, 1.3, ['포함: 정기 안전점검 · Calibration · Remote Diagnosis · Joint / Rail / Vision 상태 · Consumables Check · Software Update · A/S',
                                    '참고: 가전 A/S 출장비 2.8만원 (삼성·LG 2026, 소비자 부과분, FACT) ≠ ARKI 실제 방문 원가',
                                    'Care Plus 연 72만원 = Kit 정기교체 포함 (Base 재무 미반영)'], size=9, color=T['text2'], bullet='–', space_after=2)
    rx = MX + lw + 0.3; rw = W - MX - rx
    kits = [['Grip Kit', 'Finger Pad · Food-contact Tip · Suction Cup', '4.5', '분기', '18.0'],
            ['Cleaning Kit', 'Brush · Wiper · Cleaning Pad', '2.5', '분기', '10.0'],
            ['Protection Kit', 'Sensor Cover · Sleeve · Seal', '4.0', '반기', '8.0'],
            [('합계 (List)', {'bold': True}), '', '', '', (f"{cons['list_y']:.1f}", {'bold': True})],
            [('구매율 70% 적용 매출 · 원가 35%', {'bold': True}), '', '', '', (f"{cons['rev']:.1f} · {cons['cogs']:.1f}", {'bold': True, 'color': T['accent']})]]
    table(s, rx, y, rw, ['Kit', '구성', '만원', '주기', '연 List'], kits, col_w=[1.2, rw - 3.45, 0.7, 0.65, 0.9], size=9.5,
          align=['l', 'l', 'r', 'c', 'r'], label='kits', max_h=2.4)
    kit.tag(s, rx, y + 2.3, 'ASSUMPTION')
    text(s, rx, y + 2.6, rw, 1.2, ['검증 KPI: Replacement Cycle · Cost per Kit · 연 Consumables 매출/Robot · Gross Margin · Care Attach Rate',
                                   '부품 원가 참고: Robotiq Fingertip $175~195, Food-grade Cup £7~20 (FACT) → 자체 설계로 원가 35% 목표'],
         size=9.5, color=T['text2'], bullet='–', space_after=3)
    statement(s, MX, 5.95, CW, 'Care는 Y3에 Profit Center 아님 (Margin 23%) → 원격진단으로 방문 1.5회 이하 · Route Density로 방문원가 9만원 이하 달성 시 Y5 Margin 44% (TARGET 경로)',
              size=10.5)
    foot(s, 'A13')

# ---------------------------------------------------------------- A14 financial model
@apx
def a14(prs):
    S = M['scenarios']
    s = start(prs, 'A14', 'A14', '5-Year Financial Model (3 Scenario)', visual='상단 Base 손익 상세 표 (Y1~Y5, 억원). 하단 Conservative / Upside 요약 표 + 매출 Column Chart.',
              chart='표 + 3-Scenario 매출 Column',
              note=(f"Base에서 매출은 Y3 {S['B']['rev'][2] / 1e4:.1f}억원, Y5 {S['B']['rev'][4] / 1e4:.1f}억원이고, 5년 내내 영업적자입니다. Hardware 회사의 일반적인 경로이며 Y5 영업손실은 {-S['B']['op'][4] / 1e4:.0f}억원입니다. "
                    f"Conservative는 지불의사와 BOM 하락이 약해 Y5 Contribution이 거의 0으로, Scale 투자를 보류해야 하는 시나리오입니다. Upside는 가격을 올리지 않고 Partner 물량, 표준화, 설치원가로만 차이를 두었습니다."))
    y = head(s, 'APPENDIX A14', '5-Year Financial Model (3 Scenario)',
             sub='Bottom-up Driver: Kitchen · Robot · Robot-ready Only · Rental · Care / Consumables Installed Base · Upgrade. 억원. 상세 수식: xlsx FM 시트. 전부 DERIVED (from ASSUMPTION · TARGET).')
    L = S['B']; e = lambda v: f"{v / 1e4:,.1f}"
    def row(lab, k, bold=False, f=e):
        return [(lab, {'bold': bold})] + [(f(L[k][t]), {'bold': bold}) for t in range(5)]
    rows = [row('Kitchen Build + 설치', 'build'), row('Robot Hardware', 'rev_robot'), row('Rental + Care + Consumables', 'recurring'),
            row('Upgrade', 'rev_upg'), row('매출', 'rev', True), row('매출총이익', 'gp'),
            [('매출총이익률', {})] + [(f"{L['gm'][t] * 100:.0f}%" if L['rev'][t] else '—', {}) for t in range(5)],
            row('Contribution (채널비용 후)', 'contrib'), row('Opex', 'opex'), row('영업이익 (근사)', 'op', True),
            [('Kitchen · Robot 설치', {})] + [(f"{L['kitchens'][t]:.0f} · {L['pl'][t]:.0f}", {}) for t in range(5)],
            [('Installed Robot (기말)', {})] + [(f"{L['base_end'][t]:.0f}", {}) for t in range(5)]]
    lw = 7.4
    table(s, MX, y, lw, ['Base (억원)'] + M['years'], rows, col_w=[2.4] + [1.0] * 5, size=9, align=['l'] + ['r'] * 5, label='fm', max_h=3.95, pad=0.04)
    rx = MX + lw + 0.3; rw = W - MX - rx
    cats = M['years']
    column_chart(s, rx, y, rw, 2.2, cats, [('Conservative', [v / 1e4 for v in S['C']['rev']]), ('Base', [v / 1e4 for v in S['B']['rev']]),
                                           ('Upside', [v / 1e4 for v in S['U']['rev']])],
                 ['C9CDD2', '15171A', 'E2571B'], fmt='0', gap=60, size=8, legend=True, plot=(0.02, 0.14, 0.96, 0.72), show_labels=False)
    srows = []
    for sc in ('C', 'B', 'U'):
        Ls = S[sc]
        srows.append([{'C': 'Conservative', 'B': 'Base', 'U': 'Upside'}[sc], e(Ls['rev'][4]), e(Ls['contrib'][4]), e(Ls['op'][4]), e(Ls['min_cum_cash'])])
    table(s, rx, y + 2.4, rw, ['Y5 (억원)', '매출', 'Contrib.', '영업이익', '누적현금'], srows, col_w=[1.15, 0.7, 0.75, 0.75, rw - 3.35], size=9,
          align=['l', 'r', 'r', 'r', 'r'], label='scn', max_h=1.5)
    text(s, rx, y + 3.65, rw, 0.4, '누적현금 = 5년 누적 영업현금흐름 최저점 (투자유치 전, Rental 자산 포함)', size=8.5, color=T['muted'])
    statement(s, MX, 6.0, CW, f"Upside = 가격 동일, Partner 물량 · 표준화 · 설치원가 · Installed Base 차이. Conservative = WTP·BOM 하락 미달 → Y5 Contribution ≈ 0 → Scale 투자 보류 시나리오 (Kill Criteria M24)",
              size=10.5)
    foot(s, 'A14')

# ---------------------------------------------------------------- A15 sensitivity
@apx
def a15(prs):
    sh, sc = M['sens_household'], M['sens_company']
    s = start(prs, 'A15', 'A15', 'Sensitivity Analysis', visual='좌우 Tornado 2개: (좌) 세대 5년 Contribution, (우) 회사 Y5 Contribution. Top 3 변수 강조.',
              chart='Tornado Chart 2개',
              note=('두 기준으로 민감도를 봤습니다. 세대 기준으로는 Robot 가격, Robot BOM, Robot-ready 증분가 순서이고, 회사 기준으로는 고객 지불의사, BOM, Partner 경유 물량 순서입니다. '
                    '즉 Top 3 Critical Variable은 Customer WTP, Robot BOM, Partner Distribution입니다. 신축 Option 선택률은 5년 안에는 영향이 작은데, 계약에서 설치까지 2년 시차가 있기 때문입니다.'))
    y = head(s, 'APPENDIX A15', 'Sensitivity Analysis',
             sub='Top 3 Critical Variable = Customer WTP · Robot BOM · Partner Distribution. 회색 = 불리, 주황 = 유리. 전부 DERIVED.')
    def tornado(x, w, title, base_txt, items, unit_div, unit):
        text(s, x, y, w, 0.3, title, size=12, bold=True)
        text(s, x, y + 0.32, w, 0.28, base_txt, size=9.5, color=T['text2'])
        mx = max(max(abs(d['lo']), abs(d['hi'])) for d in items)
        lab_w = 2.45; cx = x + lab_w + (w - lab_w) / 2; half = (w - lab_w) / 2 - 0.5
        rh = 0.36
        for i, d in enumerate(items):
            ry = y + 0.75 + i * rh
            text(s, x, ry, lab_w - 0.1, rh, d['name'], size=8.5, align='r', anchor='m', bold=i < 3, color=T['text'] if i < 3 else T['text2'])
            wl = abs(d['lo']) / mx * half; wh = abs(d['hi']) / mx * half
            rect(s, cx - wl, ry + 0.08, wl, rh - 0.16, fill='8C9198'); rect(s, cx, ry + 0.08, wh, rh - 0.16, fill=T['accent'] if i < 3 else 'F6C9B3')
            text(s, cx - wl - 0.5, ry, 0.47, rh, f"{d['lo'] / unit_div:,.{1 if unit == '억' else 0}f}", size=8, align='r', anchor='m', check=False)
            text(s, cx + wh + 0.03, ry, 0.55, rh, f"+{d['hi'] / unit_div:,.{1 if unit == '억' else 0}f}", size=8, anchor='m', check=False)
        vline(s, cx, y + 0.72, len(items) * rh + 0.06, color=T['text'])
    hw = (CW - 0.4) / 2
    tornado(MX, hw, '세대 5년 Lifetime Contribution (구매·Y3 원가)', f"Base {sh['base']:,.0f}만원 · 변화 (만원)", sh['items'], 1, '만')
    tornado(MX + hw + 0.4, hw, '회사 Y5 Contribution (Base)', f"Base {sc['base'] / 1e4:,.1f}억원 · 변화 (억원)", sc['items'], 1e4, '억')
    note_line(s, 'Robot Attach Rate · Standard Module 사용률 · Failure Rate는 중위권. Rental 비중은 P&L보다 현금(자산) 영향이 큼 (A12). 회사 기준 민감도는 model.py 산출 (xlsx Sensitivity 하단 정적 표).', y=6.45)
    foot(s, 'A15')

# ---------------------------------------------------------------- A16 TIPS-period funding detail
@apx
def a16(prs):
    TP = M['tips']; a = {d['key']: d['vals']['B'] for d in M['inputs']}; L = M['scenarios']['B']
    two = lambda k: [a[k][0], a[k][1]]
    ppl = [a['fte'][t] * a['loaded'] for t in (0, 1)]
    lines = [('인건비', ppl, f"평균 {a['fte'][0]:.1f}명 · {a['fte'][1]:.0f}명 × 연 {a['loaded']:,}만원 (4대보험 · 퇴직급여 포함)"),
             ('시제품 (로봇 · 주방)', two('proto'), '1차 2식 + 목업 주방 2식 (Y1) · 2차 개선 부품 (Y2)'),
             ('목업 공간', two('space'), '약 30평 임차 + 목업 시공'),
             ('비전 · SW · 데이터', two('swdata'), 'GPU · 클라우드 · 데이터 라벨링'),
             ('안전 · 시험 · 특허', two('cert_ip'), '선행기술조사 · 출원 5건 · 공인기관 사전시험'),
             ('관리비', two('ga'), '법무 · 회계 · 보험 · 사무')]
    known = [sum(v[t] for _, v, _ in lines) for t in (0, 1)]
    lines.append(('고객 검증 · 실증', [TP['spend'][t] - known[t] for t in (0, 1)], f"인터뷰 · 지불의사 조사 · 가정 실증 {a['rd'][1]}세대 (실증 매출 차감)"))
    s = start(prs, 'A16', 'A16', 'TIPS 기간 자금 계획 상세 (24개월)', visual='좌측 회사 전체 지출 표 (Y1 · Y2 · 합계, 근거). 우측: 재원 · TIPS 과제 예산과의 관계 · 후속 투자 없을 때.',
              chart='표',
              note=(f"TIPS 24개월 동안 회사 전체 지출은 약 {TP['spend_total'] / 1e4:.1f}억원입니다. 이 중 {TP['total'] / 1e4:.0f}억원이 TIPS 과제 예산이고, 나머지는 과제에 넣지 않는 인건비 일부와 관리비, 고객 조사 비용입니다. "
                    f"재원은 TIPS 정부지원 {TP['gov'] / 1e4:.0f}억원, 운영사 투자 {a['op_invest'] / 1e4:.0f}억원, 12개월 점검 뒤 후속 투자 {a['followon'] / 1e4:.0f}억원입니다. 후속 투자가 없으면 약 {TP['runway_no_followon']:.0f}개월까지 가능합니다."))
    y = head(s, 'APPENDIX A16', 'TIPS 기간 자금 계획 상세 (24개월)',
             sub='회사 전체 지출 = 재무모델 Base Y1 + Y2 (xlsx TIPS_Budget 시트 연동). TIPS 과제 예산은 이 지출의 일부. 모든 값 ASSUMPTION · DERIVED.')
    rows = [[lab, f"{v[0] / 1e4:.2f}", f"{v[1] / 1e4:.2f}", f"{(v[0] + v[1]) / 1e4:.2f}", why] for lab, v, why in lines]
    rows.append([('합계', {'bold': True}), (f"{TP['spend'][0] / 1e4:.2f}", {'bold': True}), (f"{TP['spend'][1] / 1e4:.2f}", {'bold': True}),
                 (f"{TP['spend_total'] / 1e4:.2f}", {'bold': True, 'color': T['accent']}), ''])
    lw = 8.0
    table(s, MX, y, lw, ['억원', 'Y1', 'Y2', '합계', '근거'], rows, col_w=[1.75, 0.6, 0.6, 0.7, lw - 3.65], size=9.5, align=['l', 'r', 'r', 'r', 'l'], label='tipsuof', max_h=4.0)
    rx = MX + lw + 0.3; rw = W - MX - rx
    rect(s, rx, y, rw, 4.0, fill=T['soft'])
    text(s, rx + 0.18, y + 0.12, rw - 0.36, 0.3, '재원과 판단', size=12, bold=True)
    text(s, rx + 0.18, y + 0.5, rw - 0.36, 3.45, [f"재원: TIPS {TP['gov'] / 1e4:.0f} + 운영사 {a['op_invest'] / 1e4:.0f} + 후속 {a['followon'] / 1e4:.0f} = {TP['src_total'] / 1e4:.0f}억원 (여유 {TP['buffer'] / 1e4:.1f}억원)",
                                                 f"TIPS 과제 예산 {TP['total'] / 1e4:.0f}억원 (정부 {TP['gov'] / 1e4:.0f} · 민간 {TP['private'] / 1e4:.0f}) ⊂ 회사 전체 지출 {TP['spend_total'] / 1e4:.1f}억원",
                                                 f"후속 투자 없을 때: 약 {TP['runway_no_followon']:.0f}개월 → 2차 시제품 · 실증 범위 축소",
                                                 f"창업사업화 연계 최대 {TP['biz_link'] / 1e4:.0f}억원 (선정 뒤 별도 신청)은 미반영",
                                                 '절감 옵션: 로봇 팔 구매형 시제품 · 목업 공간 공유 · 채용 3개월 순연 (일정 위험 증가)'],
         size=9.5, color=T['text2'], bullet='–', space_after=4)
    statement(s, MX, 6.0, CW, f"결론: TIPS 단계는 기술 검증 (시제품 · 목업 · 가정 실증 · 공인시험)까지. 판매 · 파트너 확장과 본인증은 후속 투자 (3년차~)로 넘김",
              size=10.5)
    foot(s, 'A16')

# ---------------------------------------------------------------- A17 validation & tech KPI
@apx
def a17(prs):
    s = start(prs, 'A17', 'A17', 'Customer Validation · 기술 KPI', visual='좌측 고객검증 설계 표 (방법·표본·확인항목·시점). 우측 기술 KPI 표 (M12 Mock-up / M24 Real Home TARGET).',
              chart='표 2개',
              note=('고객 검증은 인터뷰만으로 끝내지 않습니다. 시간 일지로 Pain의 크기를 재고, Van Westendorp와 Gabor-Granger로 가격 구간을, Conjoint로 구매와 Rental, 기능, 노출 디자인의 상대 가치를 봅니다. '
                    '마지막으로 환불 가능한 예약금으로 실제 행동을 확인합니다. 기술 KPI는 현재 수치가 없어 목표만 제시했습니다.'))
    y = head(s, 'APPENDIX A17', 'Customer Validation · 기술 KPI',
             sub='현재 측정값 없음 → 모두 TARGET. 고객검증은 "말"이 아닌 "행동"(예약금·유료 Pilot)으로 종결.')
    lw = 6.3
    rows = [['Time-diary', '30세대 · 7일', 'Clean-up 빈도·시간 · Pain', 'M0~M3'],
            ['Interview', '50명 (Premium 상담 30 · 최근 시공 10 · 신축 계약 10)', 'Pain · 수용성 · 안전·소음·디자인 우려 · 구매 vs Rental', 'M1~M4'],
            ['PSM + Gabor-Granger', 'n≥300 (Panel)', 'Robot 가격 · Rental 월 요금 · Care 요금 Range', 'M4~M6'],
            ['Choice-based Conjoint', 'n≥300', '가격 × Task 범위 × 노출/은폐 × 소음 × 설치일수 × Care', 'M6~M9'],
            ['Smoke Test', 'Mock-up Demo 방문자', '환불가능 예약금 전환율', 'M9~M12'],
            ['Paid Pilot', '3세대 (TIPS 가정 실증)', '실제 결제 · 사용 Log · 해지 의향', 'M13~M24']]
    table(s, MX, y, lw, ['방법', '표본', '확인 항목', '시점'], rows, col_w=[1.4, 1.8, lw - 4.0, 0.8], size=9, label='cv', max_h=4.2)
    rx = MX + lw + 0.3; rw = W - MX - rx
    import slides_main as SMK        # same KPI list as the main-deck TIPS goal slide (single source)
    kp = [[k['name'].split('\n')[0] + (f" ({k['unit']})" if k['unit'] else ''), k['y1'], k['goal']] for k in SMK.TIPS['kpi'] if k['name'][:4] != '표준 한']
    kp += [['그립 실패 자동 복구율 (%)', '50', '70'], ['소음 (1m, dB(A))', '측정', '55 이하']]
    table(s, rx, y, rw, ['기술 KPI (TARGET)', '1차년도 (목업)', '최종 (가정 실증)'], kp, col_w=[rw - 2.5, 1.2, 1.3], size=9, label='tkpi', max_h=4.2)
    statement(s, MX, 6.0, CW, 'Kill 연동: M9 성공률 70% 미만 → Task Scope 축소 (Unloading·Storage 우선)  |  M12 WTP 중앙값이 목표가의 60% 미만 → B2C 재검토 (신축 B2B2C·Rental 중심)',
              size=10.5)
    foot(s, 'A17')

# ---------------------------------------------------------------- A18 WMBT
@apx
def a18(prs):
    rows = [['1  Remodeling 고객이 Robot Integration Premium 지불', '없음 (가격 가설만)', 'PSM·Conjoint · 예약금 · Paid Pilot', 'WTP 중앙값 < 목표가 60% (M12)'],
            ['2  주요 Kitchen Layout이 소수 Template으로 분류', '없음 (통상 치수 Concept)', '평면 30개 · Template Coverage', '상위 3개 Template Cover < 70%'],
            ['3  Single Robot Architecture 반복 설치', '없음', 'Mock-up 2식 · Home Pilot 설치시간', '세대별 Custom 설계 필요 · 설치 > 2일'],
            ['4  Robot + Installation GM 개선', '부품 공개가 기반 BOM 추정', 'BOM v2 견적 · 설치원가 실측', 'Y3 BOM > 1,300만원 전망'],
            ['5  Care + Consumables 반복매출 형성', '없음', 'Pilot 세대 Care 가입 · Kit 교체주기', 'Care 가입 < 40% · 교체주기 > 2배'],
            ['6  Partner Distribution이 Direct보다 빠르게 Scale', '없음 (가상 Partner 미기재)', 'Partner Pilot 시공 · 수수료 조건', 'M24 Partner Pilot 0건'],
            ['7  Service Cost ≤ Recurring Revenue', '없음', '방문원가·고장률 실측', '방문 원가 > Care 요금 (Y3 원가 기준)']]
    table_slide(prs, 'A18', 'A18', 'APPENDIX A18', 'What Must Be True', ['전제', '현재 Evidence', '향후 검증 (Seed)', 'Failure Condition'], rows,
                [4.05, 2.35, 2.8, 2.63], sub='7개 전제가 모두 성립해야 Built-in Residential Robotics Platform으로 Scale 가능. 현재 Evidence는 전부 "없음" 또는 추정.', size=9.5,
                takeaway='Seed 투자 = 7개 전제를 24개월 안에 확인하는 Option 매입. 1·2·4번이 Series A 판단의 핵심 (Sensitivity Top 변수와 일치)',
                note='Seed 투자는 이 일곱 가지 전제를 확인하는 옵션을 사는 것입니다. 현재 Evidence는 모두 없거나 추정 단계이고, 각 전제마다 실패로 판정할 조건을 미리 정했습니다. 특히 지불의사, Template 분류, Robot 원가 개선이 Series A 판단의 핵심입니다.')

# ---------------------------------------------------------------- A19 risk register
@apx
def a19(prs):
    rows = [['Apartment Fit', '동선·Reach 양립 · 벽체 구조 · 천장고', 'Mock-up · 평면 30개 · 벽체 판정', 'M6 Architecture 변경'],
            ['Technology', 'Clean-up 신뢰성 · 한식 식기 다양성', '성공률 · 개입 · Recovery 측정', 'M9 Scope 축소'],
            ['Standardization', 'Custom 설계 비중 과다', 'Standard Module 사용률 · Reuse', 'M18 Thesis 재검토'],
            ['Customer WTP', 'Robot Premium 지불 거부', 'PSM · Conjoint · 예약금', 'M12 B2C 재검토'],
            ['Installation Economics', '설치시간 · 현장 변수', '설치·Calibration 시간 실측', 'M18 원가 기준 미달 시 Template 재설계'],
            ['Rental Economics', 'Payback > 36개월', 'BOM 절감 · 요금 Test', 'BOM > 1,060만원 시 Rental Pilot 한정'],
            ['Service Economics', '방문원가 > Care 요금', '방문·고장 실측 · 원격진단', 'Care 요금·구성 재설계'],
            ['Channel', 'Partner 확보 실패 · 공사업체화', 'Partner Pilot · 역할 분담 계약', 'M24 Scale 보류'],
            ['Safety · 인증', '머리 위 작업 사고 · 인증 지연', 'Risk Assessment · 예비시험', '사고 0 · 인증 일정 Series A 계획 반영'],
            ['Competition', '대기업·Humanoid 저가 구독', 'Template·설치 Data · Partner 선점', '차별화 미입증 시 B2B Module 공급으로 전환 검토']]
    table_slide(prs, 'A19', 'A19', 'APPENDIX A19', 'Risk Register: Risk → 투자 후 Evidence → Kill Criteria', ['Risk', '내용', '투자 후 Evidence', 'Kill · 대응'], rows,
                [2.1, 3.3, 3.25, 3.18], sub='Seed Capital의 목적 = Commercial Risk Reduction. 각 Risk를 측정 가능한 Evidence와 판단 시점에 연결.', size=9.5,
                note='리스크마다 투자 후 어떤 증거로 줄일지, 실패하면 무엇을 할지를 연결했습니다. 기술 리스크만이 아니라 공간, 표준화, 가격, 설치·렌탈·서비스 경제성, 채널, 안전, 경쟁까지 포함했습니다.')

# ---------------------------------------------------------------- A20/A21 red-team
def qa():
    Bm = M['scenarios']['B']
    bs = Bm['build'][4] / Bm['rev'][4]
    return [
    ('왜 Robot Arm인가?', '식기 형상·위치가 매번 다름 → 고정 기구로 불가. 단, Arm 범위는 Rail·Dock으로 제한해 범용성보다 신뢰성 우선 (09장).'),
    ('기존 Appliance로 해결 불가능한가?', '가전은 내부 공정만 자동화. 식탁→식세기→수납 이동은 가전 경계 밖 (04장). 가전사 확장 가능성은 Risk로 인정.'),
    ('왜 Kitchen Clean-up인가?', '매 식사 반복 · 열·칼 위험 없음 · 식세기·수납이라는 고정 끝점 → 표준화 용이. 체감가치는 Cooking보다 낮음 (08장).'),
    ('돈을 낼 만큼의 Pain인가?', '미검증. 가치 Anchor 월 11~24만원 < 원가 기반 Rental 24~31만원 → Gap 존재. Time-diary·WTP로 M12 판정 (14장).'),
    ('Robot 가격은 얼마인가?', '가설 1,490만원 (Test 990~1,790). Y3 BOM 1,150만원 → GM 23% (A4·A11).'),
    ('Remodeling 포함 총 고객비용은?', 'Kitchen 공사비 (Premium 2,000~4,000만원, ASSUMPTION) + ARKI 2,020만원. 증분 부담 큼 → Rental·신축 Option 병행 (14장).'),
    ('Rental은 얼마여야 하는가?', '원가 기반 마진 20% 요금: Y3 31만원 · Y5 24만원. 가설 33만원. Partner Payback 36개월 위해 BOM ≤ 1,060만원 (A12).'),
    ('Care는 왜 필요한가?', 'Calibration·Rail·Vision 점검과 위생 관리가 안전·성능 유지 조건. Software 구독 아님 (A13).'),
    ('Consumables는 실제로 얼마나?', '가설 연 36만원 List, 구매율 70% → 25만원. 교체주기 미실측 (A13).'),
    ('Robot 고장 시 Kitchen 사용 가능한가?', '설계 Requirement: Garage 복귀·수동 해제·일반 Kitchen 기능 유지 (09장 #07, A7).'),
    ('머리 위 Robot은 안전한가?', '사람 위 운반 금지 · Zone 진입 정지 · 1.5kg 이하 · ISO 10218:2025 · 13482 검토. 인증은 Series A (A7).'),
    ('집마다 다른데 표준화 가능한가?', '가설. 4단계 분류 + 평면 30개로 M12 판정, Standard Module 60% 미만 시 재검토 (11장).'),
    ('Bay보다 Geometry가 중요한가?', 'Robot 설치는 주방 Run·설비 위치·Aisle이 결정, Bay는 거실·침실 배치 변수 (06장).'),
    ('공사업체가 되는 것 아닌가?', f'철거·가구·전기·배관 = Partner. ARKI = Module·Calibration·Safety QA. KPI: Build 비중 Y5 {bs:.0%} (19장).'),
    ('왜 구축부터인가?', '이미 철거·시공하는 고객 → 추가 Integration 비용 최소 · 가격·설치 직접 검증 · 신축은 2년 Lag (12장).'),
    ('왜 신축이 Scale Channel인가?', 'Project당 수백 세대 · 설계 단계 표준 Spec · 유상옵션 관행 (분양가 9.7%). 단, 매출 인식 지연 (12장).'),
    ('건설사가 직접 하면?', '건설사는 Robot·SW·A/S 운영 역량보다 유통 역할. ARKI Spec을 Option으로 채택하는 Distribution 관계 (20장).'),
    ('Kitchen Furniture 회사가 직접 하면?', '가장 현실적 위협. Module·Channel Partner로 협력하되 Template·설치 Data·Calibration SW로 차별 (미검증).'),
    ('Robot OEM이 직접 하면?', 'OEM은 Arm 판매가 목적, 주거 설치·A/S·가구 Interface는 비핵심 → Supplier 관계 (20장).'),
    ('Rental Asset 부담은?', 'Seed는 소량 Pilot만 ARKI 보유. Y4부터 Rental Partner가 자산 보유, Partner IRR 약 13% (연체 미반영, A12).'),
    ('A/S 비용은?', 'Y3 Robot당 연 36.8만원 (방문 2회 × 11만원 + 고장 0.6회) → Y5 26.8만원 (A13).'),
    ('Care가 Profit Center가 될 수 있는가?', 'Y3 Margin 23% → 아님. 방문 1.5회 이하·원가 9만원 이하에서 Y5 44%. Route Density 의존.'),
    ('20억원이 충분한가?', '아니오. 24개월 수정안 약 25.8억원 → TIPS 8억 연계 또는 25억원 / M18 Bridge (A16).'),
    ('24개월 후 Series A Evidence는?', 'Paid Pilot · WTP · BOM ≤ 1,150만원 경로 · Template 3개 70% Cover · 설치 1일 · Partner Pilot (22장).'),
    ('Founder가 왜 적합한가?', '[Founder 정보 필요] — 현재 답할 수 없음. 투자 판단 1순위 공백 (23장).'),
    ]

@apx
def a20(prs):
    rows = [[str(i + 1), q, a] for i, (q, a) in enumerate(qa()[:13])]
    table_slide(prs, 'A20', 'A20', 'APPENDIX A20', 'VC Red-Team Q&A (1/2)', ['#', '질문', '답 (근거 위치)'], rows, [0.35, 3.0, 8.48],
                sub='Seed 심사역 관점 재검토. 답이 약한 항목은 본문 수정 반영 (가치 Gap · Rental Payback · Seed 부족분 · Founder 공백 명시).', size=9,
                note='심사역이 반드시 물을 질문에 대한 답입니다. 답이 약한 항목은 숨기지 않고 본문에 반영했습니다. 대표적으로 가치 기준 가격과 원가 기반 가격의 차이, Rental Payback, Seed 부족분, Founder 정보 공백입니다.')

@apx
def a21(prs):
    rows = [[str(i + 14), q, a] for i, (q, a) in enumerate(qa()[13:])]
    table_slide(prs, 'A21', 'A21', 'APPENDIX A21', 'VC Red-Team Q&A (2/2)', ['#', '질문', '답 (근거 위치)'], rows, [0.35, 3.0, 8.48],
                sub='약한 답: 4 (Pain) · 6 (총 고객비용) · 18 (가구사 직접 진입) · 23 (자금) · 25 (Founder) → Investment Memo의 Reasons Not to Invest', size=9,
                note='약한 답이 다섯 개 있습니다. Pain의 크기, 총 고객비용, 가구사의 직접 진입, Seed 금액, 그리고 Founder입니다. 이 다섯 개가 Investment Memo의 투자하지 않을 이유와 그대로 연결됩니다.')

# ---------------------------------------------------------------- A22 scorecard
def score():
    Bm = M['scenarios']['B']
    rs = Bm['recurring'][4] / Bm['rev'][4]
    return [('Market', 3, 4, '공식 통계로 Stock·공급 확인. SAM 비율(Premium·적용·Option)은 가정'),
         ('Product', 2, 4, 'Concept 정의 명확. 실물·Mock-up 없음'),
         ('Technology', 2, 4, 'Cobot·Vision 부품은 상용. 가정 주방 Clean-up 신뢰성 미검증'),
         ('Customer Demand', 1, 4, 'Interview·WTP·예약 없음. 가치 Anchor < 원가 Gap'),
         ('Standardization', 1, 4, '평면 분석 없음. 분류 체계만 존재'),
         ('Unit Economics', 2, 3, f"Y3 세대 CM {M['household']['purchase_direct_Y3']['cm5']:.0%} · Y5 {M['household']['purchase_direct_Y5']['cm5']:.0%} (가정). BOM 의존"),
         ('Recurring Revenue', 2, 3, f"구조 설계됨. 비중 Y5 {rs:.0%} · 정상상태 약 {M['steady']['rec_share']:.0%}"),
         ('Distribution', 1, 3, 'Partner 접촉 없음. Partner 역할·수수료 구조만 설계'),
         ('Team', 1, None, '[Founder 정보 필요] — 평가 불가'),
         ('Capital Efficiency', 2, 3, f"TIPS 24개월 지출 약 {M['tips']['spend_total'] / 1e4:.1f}억 · 후속 투자 없으면 약 {M['tips']['runway_no_followon']:.0f}개월. 5년 누적 현금소요 약 {-Bm['min_cum_cash'] / 1e4:.0f}억 (Base)")]

@apx
def a22(prs):
    s = start(prs, 'A22', 'A22', 'Investment Scorecard · Seed 판단', visual='좌측 10개 항목 Scorecard 표 (현재/24개월 Target 점수 막대 + 핵심 Evidence). 우측 판단 박스 WATCH + INVEST 전환 조건 5개.',
              chart='Scorecard Bar + 판단 박스',
              note=('실제 Seed 심사역 관점의 점수표입니다. 시장과 접근 방식은 구조가 분명하지만, 고객 수요, 표준화, 유통, 팀은 현재 증거가 없습니다. '
                    '그래서 판단은 WATCH입니다. 다섯 가지 증거가 확보되면 INVEST로 바뀔 수 있습니다. Founder 적합성, 실제 크기 Mock-up 시연, 실명 고객의 예약금이나 유료 Pilot 의향, 평면 30개 분석 결과, 실재하는 Partner 협력 합의입니다.'))
    y = head(s, 'APPENDIX A22', 'Investment Scorecard · Seed 판단',
             sub='점수 1~5 (5 = 강한 Evidence). 현재 = 2026.10 · Target = M24. 본 판단은 자료 작성자의 Red-Team 의견.')
    lw = 7.7
    hdr_y = y
    text(s, MX, hdr_y, 1.7, 0.28, '항목', size=9.5, bold=True); text(s, MX + 1.75, hdr_y, 1.6, 0.28, '현재 → Target', size=9.5, bold=True)
    text(s, MX + 3.45, hdr_y, lw - 3.45, 0.28, '핵심 Evidence', size=9.5, bold=True)
    hline(s, MX, hdr_y + 0.3, lw, color=T['text'])
    SCORE = score()
    for i, (k, cur, tgt, ev) in enumerate(SCORE):
        ry = hdr_y + 0.36 + i * 0.37
        text(s, MX, ry, 1.7, 0.36, k, size=10, bold=True, anchor='m')
        for j in range(5):
            bx = MX + 1.75 + j * 0.3
            f = T['text'] if j < cur else (T['accent_soft'] if (tgt and j < tgt) else T['soft'])
            rect(s, bx, ry + 0.1, 0.24, 0.18, fill=f)
        text(s, MX + 3.3, ry, 0.15, 0.36, '', size=8, check=False)
        text(s, MX + 3.45, ry, lw - 3.45, 0.36, ev, size=9, color=T['text2'], anchor='m')
        hline(s, MX, ry + 0.36, lw)
    text(s, MX, hdr_y + 4.08, lw, 0.3, '■ 현재 점수   ■ 24개월 Target 증분 (연주황)   Team은 정보 부재로 Target 미설정', size=8.5, color=T['muted'])
    tot_c = sum(c for _, c, _, _ in SCORE); tot_t = sum((t or c) for _, c, t, _ in SCORE)
    rx = MX + lw + 0.3; rw = W - MX - rx
    rect(s, rx, y, rw, 0.95, fill=T['text'])
    text(s, rx + 0.2, y + 0.06, rw - 0.4, 0.3, '운영사 관점 판단 (작성자 의견)', size=10, bold=True, color='A9AEB5')
    text(s, rx + 0.2, y + 0.33, rw - 0.4, 0.55, 'WATCH', size=26, bold=True, color=T['accent'])
    text(s, rx + 1.9, y + 0.42, rw - 2.1, 0.45, f"현재 {tot_c}/50 → Target {tot_t}/50", size=10, color='FFFFFF')
    text(s, rx, y + 1.1, rw, 0.3, 'INVEST 전환 조건 (최대 5개)', size=11.5, bold=True)
    conds = ['Founder: Robot Manipulation × 주방·건축 Integration 역량 보유 Full-time 2인 이상',
             'Mock-up: 실제 크기 주방에서 식기 → 식세기 Loading 연속 시연 (영상 + 성공률 Log)',
             'WTP 신호: Premium 상담 고객 30명 Interview + 실명 예약금 또는 유료 Pilot 의향 3건 이상',
             '표준화 신호: 실제 평면 30개 중 상위 3개 Template이 70% 이상 Cover',
             'Channel 신호: 주방가구·Interior 사업자 1곳과 Pilot 시공 협력 합의 (실재)']
    for i, c in enumerate(conds):
        cy = y + 1.42 + i * 0.55
        text(s, rx, cy, 0.3, 0.5, str(i + 1), size=12, bold=True, color=T['accent'], anchor='m')
        text(s, rx + 0.32, cy, rw - 0.32, 0.55, c, size=9.5, anchor='m')
    statement(s, MX, 6.25, CW, '판단 근거: 진입 방식(구축 Validation → 신축 Scale)·Kill Criteria·BM 구조는 명확. 그러나 Founder·고객·표준화·Channel Evidence가 모두 공백 → 현 시점 투자 · TIPS 추천 근거 부족 (WATCH)',
              size=10.5)
    foot(s, 'A22')

# ---------------------------------------------------------------- A23 sources
import re as _re
def _srclabel(src):
    head_ = src.split('http')[0].rstrip(' :,—-')
    if head_.endswith('보도'): head_ = head_[:-2].rstrip(' —-')
    doms = _re.findall(r'https?://(?:www\.|m\.)?([^/\s,]+)', src)
    dom = ', '.join(dict.fromkeys(doms[:2]))
    return (head_ + ' · ' if head_ else '') + dom
def _src_slide(prs, code, items, part):
    s = start(prs, code, code, 'Sources', visual='출처 목록 2열', chart='없음',
              note='출처는 검색 시점의 보도와 공개 자료입니다. 외부 제출 전에는 국가데이터처와 국토교통부 보도자료 원문으로 다시 확인해야 합니다.')
    y = head(s, f'APPENDIX {code}', 'Sources', sub='조회일 2026-10-07 · 검색 결과 기준. 외부 제출 전 원문 대조 필요. 전체 URL: docs/03_Market_Data_and_Sources.md · xlsx Sources 시트')
    hw = (CW - 0.3) / 2; half = (len(items) + 1) // 2
    for col in range(2):
        chunk = items[col * half:(col + 1) * half]
        lines = [f"[{d['id']}] {d['item']} — {_srclabel(d['source'])}" for d in chunk]
        text(s, MX + col * (hw + 0.3), y, hw, 5.0, lines, size=8.5, color=T['text2'], space_after=4)
    foot(s, code)

@apx
def a23(prs):
    _src_slide(prs, 'A23', M['src'], 'FACT 출처')

APPX = APX
