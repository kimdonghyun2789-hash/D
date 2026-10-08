# ARKI Robotics — TIPS IR model (single source of truth for the deck, the xlsx and the docs)
# Units: 만원 (KRW 10,000) unless a unit says otherwise.  Year Y1 = TIPS 과제 M1~M12, Y2 = M13~M24, Y3 = 후속 투자 이후.
# Every input carries a tag: FACT / DERIVED / ASSUMPTION / TARGET.
#   python3 ARKI/source/model.py   -> ARKI/source/model.json (+ sanity asserts)
import json, os, copy

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'model.json')
SC = ('C', 'B', 'U')
SCN = {'C': 'Conservative', 'B': 'Base', 'U': 'Upside'}
YEARS = ['Y1', 'Y2', 'Y3', 'Y4', 'Y5']
N = 5

# ---------------------------------------------------------------- inputs
INPUTS = []          # ordered list (drives the xlsx Inputs sheets and the tag register)
IDX = {}

def inp(key, group, desc, unit, tag, val, src=''):
    """val: scalar | list[5] (same in all scenarios) | dict{C,B,U} of scalar or list[5]."""
    vals = val if isinstance(val, dict) else {s: val for s in SC}
    vals = {s: (list(v) if isinstance(v, list) else v) for s, v in vals.items()}
    d = dict(key=key, group=group, desc=desc, unit=unit, tag=tag, vals=vals,
             yearly=isinstance(vals['B'], list), src=src)
    INPUTS.append(d); IDX[key] = d

# --- market (FACT = public statistics; see docs/03 for URLs)
inp('m_housing_total', 'market', '총주택 (2025.11.1 기준)', '천호', 'FACT', 20181,
    '국가데이터처, 2025 인구주택총조사 등록센서스 결과 (2026.7.28 발표)')
inp('m_apt_share', 'market', '아파트 비중 (총주택 대비)', '%', 'FACT', 0.658, '국가데이터처, 2025 인구주택총조사')
inp('m_house_20y_share', 'market', '준공 20년 이상 주택 비중', '%', 'FACT', 0.560, '국가데이터처, 2025 인구주택총조사')
inp('m_house_30y_share', 'market', '준공 30년 이상 주택 비중', '%', 'FACT', 0.306, '국가데이터처, 2025 인구주택총조사')
inp('m_apt_2023', 'market', '아파트 수 (2023)', '천호', 'FACT', 12630, '통계청, 2023 주택총조사 (보도 인용)')
inp('m_apt_20y_2023', 'market', '준공 20년 이상 아파트 (2023)', '천호', 'FACT', 6390, '통계청, 2023 주택총조사 (보도 인용)')
inp('m_txn_2025', 'market', '주택 매매거래 (2025, 전체 주택)', '천호', 'FACT', 726, 'KB주택시장리뷰 2026.2 (한국부동산원 자료)')
inp('m_completion_2025', 'market', '주택 준공 (2025 연간, 전체 주택)', '천호', 'FACT', 342.4, '국토교통부, 2025년 12월 주택통계')
inp('m_movein_2025', 'market', '아파트 입주 (2025)', '천호', 'FACT', 236.3, '부동산114 REPS')
inp('m_movein_2026e', 'market', '아파트 입주 예정 (2026)', '천호', 'FACT', 183.1, '부동산114 REPS (예정 물량)')
inp('a_replace_cycle', 'market', 'Kitchen 교체주기 (노후 아파트)', '년', 'ASSUMPTION', 22, '교차검증용 가정. Seed 기간 견적·인터뷰로 검증')
inp('a_txn_apt_share', 'market', '매매거래 중 아파트 비중', '%', 'ASSUMPTION', 0.70, '부동산원 월별 아파트 거래 비중 확인 필요')
inp('a_txn_kitchen_rate', 'market', '매수 후 Kitchen 교체율', '%', 'ASSUMPTION', 0.40, '인터뷰·인테리어 Partner 자료로 검증')
inp('a_aging_nontxn', 'market', '비거래 노후 교체 세대', '천/년', 'ASSUMPTION', 100, '교차검증용 가정')
inp('a_kitchen_replace', 'market', '연간 Kitchen 교체 세대 (아파트)', '천/년', 'ASSUMPTION', 300, '두 방식 교차검증(29만·30만) 후 30만으로 설정')
inp('a_premium_share', 'market', 'Premium Kitchen 비중', '%', 'ASSUMPTION', 0.10, '주방 예산 2,000만원 이상 가정. 견적 수집으로 검증')
inp('a_fit_rate', 'market', 'Robot-ready 적용 가능률 (구조·전원·평면)', '%', 'ASSUMPTION', 0.60, '평면 30개 분석으로 검증')
inp('a_new_supply', 'market', '연간 신규 아파트 입주 (평균)', '천/년', 'DERIVED', 200, '2025 실적 23.6만·2026 예정 18.3만 → 20만')
inp('a_premium_project', 'market', 'Premium 단지 비중 (신축)', '%', 'ASSUMPTION', 0.15, '브랜드·분양가 기준 정의 필요')

# --- value anchor
inp('f_helper_rate', 'value', '가사서비스 시간당 요금 (플랫폼 4시간 59,900~64,900원)', '만원/h', 'FACT', 1.5,
    '가사서비스 플랫폼 공개 요금 (2025, 보도·앱 정보)')
inp('a_cleanup_min', 'value', 'Clean-up 시간 (식사 후 정리, 일)', '분/일', 'ASSUMPTION', 40, 'Time-diary(n=30)로 검증')
inp('a_auto_share', 'value', 'V1 자동화 가능 비중', '%', 'ASSUMPTION', 0.60, '식기 이동·식세기·수납만. 행주·싱크 세척 제외')
inp('fx', 'value', '환율 (Benchmark 환산용)', '원/USD', 'ASSUMPTION', 1400, '부품 Benchmark 환산 전용')

# --- prices (VAT 별도, 고객가)
inp('p_rr', 'price', 'Robot-ready Kitchen 증분가 (구축)', '만원/세대', 'ASSUMPTION', {'C': 400, 'B': 450, 'U': 450},
    '기존 Kitchen 공사비 위 증분. 시스템에어컨 유상옵션(500~1,000만원) 대비 하단')
inp('p_rr_new', 'price', 'Robot-ready Option 공급가 (신축, ARKI 매출)', '만원/세대', 'ASSUMPTION', {'C': 200, 'B': 220, 'U': 220},
    '건설사·가구사 마진 별도. 분양 고객가 약 300만원 가정')
inp('p_robot', 'price', 'Robot Module ASP (구매)', '만원/대', 'ASSUMPTION', {'C': 1290, 'B': 1490, 'U': 1490},
    'Upside는 가격 인상 없음. WTP 검증 대상 1순위')
inp('p_comm', 'price', '설치·Calibration·Safety Check', '만원/대', 'ASSUMPTION', 80, '')
inp('p_rent', 'price', 'Robot Rental 월 요금 (Care Basic·Grip Kit 포함, 60개월)', '만원/월', 'ASSUMPTION', {'C': 29, 'B': 33, 'U': 33},
    '원가 Build-up(감가·금융·Care·Grip·Reserve)+마진')
inp('rent_months', 'price', 'Rental 계약기간', '개월', 'ASSUMPTION', 60, '')
inp('p_care', 'price', 'Care Basic 연 요금 (구매 고객)', '만원/년', 'ASSUMPTION', {'C': 42, 'B': 48, 'U': 48},
    '정기점검·Calibration·원격진단·SW Update·A/S 공임')
inp('p_care_plus', 'price', 'Care Plus 연 요금 (Kit 정기교체 포함)', '만원/년', 'ASSUMPTION', 72, '옵션 상품. 재무 Base에는 미반영')
inp('p_grip', 'price', 'Grip Kit (Finger Pad·Food-contact Tip·Suction Cup)', '만원/Kit', 'ASSUMPTION', 4.5, '분기 교체 가정')
inp('n_grip', 'price', 'Grip Kit 교체 횟수', '회/년', 'ASSUMPTION', 4, 'Replacement Cycle 검증 대상')
inp('p_clean', 'price', 'Cleaning Kit (Brush·Wiper·Cleaning Pad)', '만원/Kit', 'ASSUMPTION', 2.5, '')
inp('n_clean', 'price', 'Cleaning Kit 교체 횟수', '회/년', 'ASSUMPTION', 4, '')
inp('p_protect', 'price', 'Protection Kit (Sensor Cover·Sleeve·Seal)', '만원/Kit', 'ASSUMPTION', 4.0, '')
inp('n_protect', 'price', 'Protection Kit 교체 횟수', '회/년', 'ASSUMPTION', 2, '')
inp('cons_attach', 'price', 'Consumables 구매율', '%', 'ASSUMPTION', {'C': 0.55, 'B': 0.70, 'U': 0.70}, '')
inp('care_attach', 'price', 'Care 가입률 (구매 고객)', '%', 'ASSUMPTION', {'C': 0.55, 'B': 0.70, 'U': 0.70}, '')
inp('p_sw', 'price', 'Software Skill Pack (설치 다음 해)', '만원', 'ASSUMPTION', 60, 'V2 기능 (재료 투입 보조 등) 출시 전제')
inp('sw_attach', 'price', 'Software Skill 구매율', '%', 'ASSUMPTION', {'C': 0.10, 'B': 0.20, 'U': 0.20}, '')
inp('p_tool', 'price', 'End-effector / Tool 추가 (설치 2년 후)', '만원', 'ASSUMPTION', 80, 'FUTURE CONCEPT 제품')
inp('tool_attach', 'price', 'Tool 구매율', '%', 'ASSUMPTION', {'C': 0.15, 'B': 0.25, 'U': 0.25}, '')
inp('wholesale', 'price', 'Rental Partner 공급가율 (Robot ASP 대비)', '%', 'ASSUMPTION', 0.88, 'Y4부터 Rental Partner가 자산 보유')
inp('partner_fee', 'price', 'Rental Partner → ARKI Care·Grip 서비스료', '만원/월', 'ASSUMPTION', 6.0, '')
inp('realization', 'price', '가격 실현율 (Y2 Pilot 할인)', '%', 'ASSUMPTION',
    {'C': [1, 0.3, 1, 1, 1], 'B': [1, 0.5, 1, 1, 1], 'U': [1, 0.6, 1, 1, 1]}, 'Pilot은 할인 유료')

# --- costs
inp('kit_std_cost', 'cost', 'Kitchen Module 원가 (100% 표준부품 기준)', '만원/세대', 'ASSUMPTION', 200,
    '하부 보강 프레임·Rail Interface·식세기 상향 하우징·Robot Garage·전원/통신·수납 Rack')
inp('custom_factor', 'cost', 'Custom 부품 원가 배수', 'x', 'ASSUMPTION', 1.6, '')
inp('design_cost', 'cost', 'Design·Site Adjustment 원가 (100% Custom 시)', '만원/세대', 'ASSUMPTION', 100, '')
inp('smr', 'cost', 'Standard Module 사용률', '%', 'TARGET',
    {'C': [0.40, 0.45, 0.55, 0.62, 0.65], 'B': [0.40, 0.50, 0.65, 0.75, 0.80], 'U': [0.40, 0.55, 0.70, 0.80, 0.85]},
    'Seed 종료 시 65% 이상 (Kill Criteria: M18 60% 미만)')
inp('kit_new_cost', 'cost', 'Robot-ready Option 원가 (신축, 공장 생산)', '만원/세대', 'ASSUMPTION', {'C': 145, 'B': 130, 'U': 120}, '')
inp('bom', 'cost', 'Robot Module BOM', '만원/대', 'ASSUMPTION',
    {'C': [1600, 1500, 1300, 1180, 1080], 'B': [1600, 1450, 1150, 1000, 900], 'U': [1600, 1400, 1080, 920, 800]},
    'A4 부품 Benchmark 기반. 수량·국산화·전용 Arm으로 하락 가정')
inp('comm_cost', 'cost', '설치·Calibration 원가 (ARKI 인력)', '만원/대', 'ASSUMPTION',
    {'C': [120, 100, 75, 62, 55], 'B': [120, 90, 60, 45, 38], 'U': [120, 85, 52, 38, 30]}, '설치시간 TARGET과 연동')
inp('logistics', 'cost', '물류 (프로젝트당)', '만원/세대', 'ASSUMPTION', 25, '')
inp('warranty', 'cost', 'Warranty Reserve (Robot 매출 대비)', '%', 'ASSUMPTION', {'C': 0.05, 'B': 0.04, 'U': 0.035}, '1년 무상 A/S')
inp('visits', 'cost', '정기 방문 횟수', '회/년', 'ASSUMPTION',
    {'C': [2, 2, 2, 2, 2], 'B': [2, 2, 2, 1.5, 1.5], 'U': [2, 2, 1.5, 1.2, 1.0]}, '원격진단 고도화로 감소')
inp('visit_cost', 'cost', '방문 1회 원가 (인건비·이동)', '만원/회', 'ASSUMPTION',
    {'C': [15, 14, 12.5, 11, 10], 'B': [15, 13, 11, 9, 8], 'U': [15, 12, 10, 8, 7]},
    '참고: 제조사 출장비 2.8만원(소비자 부과분, 2026)과 별개인 실제 원가. Route Density로 하락')
inp('corrective', 'cost', '고장 방문 (Failure Rate)', '회/대·년', 'ASSUMPTION', {'C': 0.9, 'B': 0.6, 'U': 0.5}, '')
inp('corr_cost', 'cost', '고장 방문 1회 원가 (소부품 포함)', '만원/회', 'ASSUMPTION', 18, '')
inp('cloud', 'cost', 'Cloud·Software 운영비', '만원/대·년', 'ASSUMPTION', 4, '')
inp('cons_cogs', 'cost', 'Consumables 원가율 (물류 포함)', '%', 'ASSUMPTION', {'C': 0.40, 'B': 0.35, 'U': 0.32}, '')
inp('sw_cogs', 'cost', 'Software 원가율', '%', 'ASSUMPTION', 0.10, '')
inp('tool_cogs', 'cost', 'Tool 원가율', '%', 'ASSUMPTION', 0.45, '')
inp('partner_margin', 'cost', 'Kitchen·Interior Partner 수수료 (Partner 경유 패키지)', '%', 'ASSUMPTION',
    {'C': 0.12, 'B': 0.10, 'U': 0.09}, '')
inp('cac', 'cost', '직접판매 획득비용 (상담·설계·Demo)', '만원/세대', 'ASSUMPTION', {'C': 180, 'B': 150, 'U': 140}, '')
inp('bd_new', 'cost', '신축 Project 수주비용 (Spec·견본주택)', '만원/Project', 'ASSUMPTION', 2000, '')
inp('residual', 'cost', 'Rental 자산 잔존가치 (60개월 후)', '%', 'ASSUMPTION', 0.15, 'Refurbish 재배치')
inp('fin_rate', 'cost', 'Rental 자산 금융비용', '%/년', 'ASSUMPTION', 0.08, '캐피탈 조달금리+Spread 가정')
inp('payback_hurdle', 'cost', 'Rental Partner 요구 Payback', '개월', 'ASSUMPTION', 36, '렌탈·캐피탈사 협의로 검증')

# --- volumes
inp('rd', 'volume', '구축 직접판매 Kitchen', '세대', 'TARGET',
    {'C': [0, 3, 20, 35, 40], 'B': [0, 3, 30, 50, 60], 'U': [0, 3, 35, 60, 70]}, 'Y2 = 가정 실증 3세대 (TIPS 과제, 유료 목표)')
inp('rp', 'volume', '구축 Partner 경유 Kitchen', '세대', 'TARGET',
    {'C': [0, 0, 10, 60, 150], 'B': [0, 0, 20, 130, 340], 'U': [0, 0, 30, 220, 600]}, 'Kitchen 가구·인테리어 Partner')
inp('attach', 'volume', 'Robot Attach Rate (구축, 설치 시점)', '%', 'ASSUMPTION',
    {'C': [1, 1, 0.75, 0.75, 0.75], 'B': [1, 1, 0.85, 0.85, 0.85], 'U': [1, 1, 0.85, 0.85, 0.85]}, '나머지는 Robot-ready Only')
inp('later_attach', 'volume', 'Robot-ready Only 세대의 연간 후속 Attach', '%/년', 'ASSUMPTION', {'C': 0.05, 'B': 0.10, 'U': 0.12}, '')
inp('rental_share', 'volume', 'Rental 선택 비중', '%', 'ASSUMPTION',
    {'C': [0, 0.3, 0.3, 0.35, 0.35], 'B': [0, 0.3, 0.3, 0.4, 0.4], 'U': [0, 0.3, 0.3, 0.45, 0.45]}, '')
inp('partner_rental', 'volume', 'Rental 자산 보유 주체 (0 = ARKI Pilot, 1 = Rental Partner)', 'flag', 'ASSUMPTION', [0, 0, 0, 1, 1], '')
inp('projects', 'volume', '신축 Robot-ready Option 계약 Project', '개', 'TARGET',
    {'C': [0, 0, 0, 1, 2], 'B': [0, 0, 1, 2, 3], 'U': [0, 0, 2, 3, 4]}, '계약 2년 후 입주·설치')
inp('hh_project', 'volume', 'Project당 세대수', '세대', 'ASSUMPTION', 800, '')
inp('option_rate', 'volume', '신축 Robot-ready Option 선택률', '%', 'ASSUMPTION', {'C': 0.06, 'B': 0.10, 'U': 0.12}, '')
inp('new_attach', 'volume', '신축 입주 시 Robot Attach', '%', 'ASSUMPTION', {'C': 0.15, 'B': 0.25, 'U': 0.30}, '')

# --- fixed opex (same plan in all scenarios)
inp('fte', 'opex', '평균 인원', '명', 'ASSUMPTION', [4.4, 7, 20, 32, 42],
    'Y1~Y2 = TIPS 기간 (대표 + 신규 연구원 4명 → Y2 실증 엔지니어 · 사업개발 추가, TIPS_TEAM). Y3부터 후속 투자 전제')
inp('loaded', 'opex', '인당 연 인건비 (4대보험·퇴직급여 포함)', '만원/년', 'ASSUMPTION', 8500, '평균 연봉 약 7,100만원 × 1.2')
inp('proto', 'opex', 'Robot·Kitchen Prototype (H/W)', '만원', 'ASSUMPTION', [12000, 4000, 30000, 35000, 40000],
    'Y1 시제품 1차 2식 + 실물 크기 목업 주방 2식 · Y2 2차 개선 부품 (실증 3세대 하드웨어는 원가에 반영)')
inp('swdata', 'opex', 'Vision·Software·Data (GPU·Cloud·Annotation)', '만원', 'ASSUMPTION', [2000, 3000, 10000, 15000, 20000], '')
inp('space', 'opex', 'Full-scale Mock-up·공간', '만원', 'ASSUMPTION', [6000, 4000, 10000, 12000, 15000], 'Y1~Y2: 목업 공간 약 30평 임차 + 목업 시공')
inp('cert_ip', 'opex', 'Safety·Certification·IP', '만원', 'ASSUMPTION', [2500, 6000, 20000, 10000, 10000],
    'Y1 선행기술조사 · 특허 출원 2건 / Y2 공인시험 · 안전 사전시험 · 특허 3건 / Y3 본인증')
inp('research', 'opex', 'Pilot·Customer Validation', '만원', 'ASSUMPTION', [2000, 3500, 5000, 5000, 5000],
    'Y1 인터뷰 50명 · 정리 시간 기록 30세대 / Y2 지불의사 조사 n≥300 · 실증 가정 지원')
inp('mkt', 'opex', 'Marketing·Partner Enablement', '만원', 'ASSUMPTION', [0, 1000, 30000, 50000, 70000], '')
inp('ga', 'opex', 'G&A (법무·회계·보험·사무)', '만원', 'ASSUMPTION', [5000, 6000, 30000, 40000, 50000], '')

# --- funding (TIPS 기간 24개월). 규정 값 = 2026 TIPS 공고 (sources.json), 선정은 미확정
inp('tips', 'funding', 'TIPS R&D 정부지원금 (일반 트랙 최대)', '만원', 'FACT', 80000, '중소벤처기업부 공고 제2026-40호 (2026.1.26) 팁스 창업기업 지원계획. 선정 미확정')
inp('tips_months', 'funding', 'TIPS R&D 기간 (최대)', '개월', 'FACT', 24, '공고 제2026-40호')
inp('tips_gov_ratio', 'funding', '정부지원연구개발비 비율 상한 (총 연구개발비 대비)', '%', 'FACT', 0.75, '공고 제2026-40호 (사본 · 운용사 정리 기준: 정부 75% 이내, 기관부담 25% 이상)')
inp('tips_cash_ratio', 'funding', '기관부담연구개발비 중 현금 최소 비율', '%', 'FACT', 0.10, '공고 제2026-40호 (사본 · 운용사 정리 기준)')
inp('op_invest', 'funding', '운영사 투자 (요청액, TIPS 추천 전제)', '만원', 'ASSUMPTION', 30000, '요건: 수도권 2억원 이상 · 비수도권 1억원 이상 (2026). 조건 (형태 · 기업가치 · 지분)은 협의')
inp('followon', 'funding', '후속 투자 (M12 목표, 공동투자 · Pre-A)', '만원', 'TARGET', 50000, 'M9 · M12 점검 결과 기반')
inp('biz_link', 'funding', '비R&D 연계 (창업사업화 · 해외마케팅) 각 최대 (선정 뒤 별도 신청, 기본안 미반영)', '만원', 'FACT', 15000, '공고 제2026-40호: 각 10개월 최대 1.5억원, 합산 3억원, 정부 70% 이내')

# ---------------------------------------------------------------- helpers
def V(s, ov=None):
    """Scenario value lookup with optional overrides {key: value or callable(old)->new}."""
    ov = ov or {}
    out = {}
    for d in INPUTS:
        v = copy.deepcopy(d['vals'][s])
        if d['key'] in ov:
            o = ov[d['key']]
            v = o(v) if callable(o) else o
        out[d['key']] = v
    return out

def yr(v, t):
    return v[t] if isinstance(v, list) else v

# ---------------------------------------------------------------- 5-year engine
def run(s, ov=None):
    a = V(s, ov)
    L = {k: [0.0] * N for k in (
        'rd', 'rp', 'ni', 'kitchens', 'pl_remodel', 'later', 'pl_new', 'pl', 'rpl', 'pp', 'drpl', 'prpl', 'pool',
        'pb_end', 'pb_avg', 'dr_end', 'dr_avg', 'pr_end', 'pr_avg', 'base_end',
        'rev_kitchen', 'rev_comm', 'rev_robot', 'rev_rental', 'rev_care', 'rev_cons', 'rev_upg', 'rev',
        'c_kitchen', 'c_log', 'c_robot', 'c_comm', 'c_warranty', 'c_dep', 'c_care', 'c_cons', 'c_upg', 'cogs', 'gp',
        'ch_partner', 'ch_cac', 'ch_bd', 'contrib', 'op_people', 'op_other', 'opex', 'op', 'capex', 'cash', 'cum_cash',
        'backlog', 'kit_unit_cost', 'care_unit_cost')}
    cons_y = a['p_grip'] * a['n_grip'] + a['p_clean'] * a['n_clean'] + a['p_protect'] * a['n_protect']
    cons_y_rent = a['p_clean'] * a['n_clean'] + a['p_protect'] * a['n_protect']
    grip_y = a['p_grip'] * a['n_grip']
    cum_capex_prev = 0.0
    for t in range(N):
        real = yr(a['realization'], t); att = yr(a['attach'], t); smr = yr(a['smr'], t)
        rd, rp = yr(a['rd'], t), yr(a['rp'], t)
        ni = (a['projects'][t - 2] * a['hh_project'] * a['option_rate']) if t >= 2 else 0.0
        pool_prev = L['pool'][t - 1] if t else 0.0
        later = pool_prev * a['later_attach']
        pl_remodel = (rd + rp) * att
        pl_new = ni * a['new_attach']
        pl = pl_remodel + pl_new + later
        rs = yr(a['rental_share'], t); pf = yr(a['partner_rental'], t)
        rpl = pl * rs; pp = pl - rpl; drpl = rpl * (1 - pf); prpl = rpl * pf
        pool = pool_prev + (rd + rp) * (1 - att) + ni * (1 - a['new_attach']) - later
        g = lambda k: L[k][t - 1] if t else 0.0
        pb_end = g('pb_end') + pp; pb_avg = g('pb_end') + pp / 2
        dr_end = g('dr_end') + drpl; dr_avg = g('dr_end') + drpl / 2
        pr_end = g('pr_end') + prpl; pr_avg = g('pr_end') + prpl / 2
        # revenue
        rev_kitchen = (rd + rp) * a['p_rr'] * real + ni * a['p_rr_new']
        rev_comm = pl * a['p_comm'] * real
        rev_robot = pp * a['p_robot'] * real + prpl * a['p_robot'] * a['wholesale']
        rev_rental = dr_avg * a['p_rent'] * 12
        rev_care = pb_avg * a['care_attach'] * a['p_care'] + pr_avg * a['partner_fee'] * 12
        rev_cons = pb_avg * a['cons_attach'] * cons_y + (dr_avg + pr_avg) * a['cons_attach'] * cons_y_rent
        pl1 = L['pl'][t - 1] if t >= 1 else 0.0; pl2 = L['pl'][t - 2] if t >= 2 else 0.0
        rev_upg = pl1 * a['sw_attach'] * a['p_sw'] + pl2 * a['tool_attach'] * a['p_tool']
        rev = rev_kitchen + rev_comm + rev_robot + rev_rental + rev_care + rev_cons + rev_upg
        # cogs
        kit_unit = a['kit_std_cost'] * (smr + a['custom_factor'] * (1 - smr)) + a['design_cost'] * (1 - smr)
        bom = yr(a['bom'], t)
        c_kitchen = (rd + rp) * kit_unit + ni * a['kit_new_cost']
        c_log = (rd + rp + ni) * a['logistics']
        c_robot = (pp + prpl) * bom
        c_comm = pl * yr(a['comm_cost'], t)
        c_warranty = a['warranty'] * rev_robot
        capex = drpl * bom
        c_dep = cum_capex_prev * (1 - a['residual']) / 5 + capex * (1 - a['residual']) / 5 * 0.5
        care_unit = yr(a['visits'], t) * yr(a['visit_cost'], t) + a['corrective'] * a['corr_cost'] + a['cloud']
        c_care = (pb_avg * a['care_attach'] + dr_avg + pr_avg) * care_unit
        c_cons = rev_cons * a['cons_cogs'] + (dr_avg + pr_avg) * grip_y * a['cons_cogs']
        c_upg = pl1 * a['sw_attach'] * a['p_sw'] * a['sw_cogs'] + pl2 * a['tool_attach'] * a['p_tool'] * a['tool_cogs']
        cogs = c_kitchen + c_log + c_robot + c_comm + c_warranty + c_dep + c_care + c_cons + c_upg
        gp = rev - cogs
        ch_partner = a['partner_margin'] * rp * (a['p_rr'] * real + att * (a['p_robot'] + a['p_comm']) * real)
        ch_cac = rd * a['cac']
        ch_bd = a['projects'][t] * a['bd_new']
        contrib = gp - ch_partner - ch_cac - ch_bd
        op_people = yr(a['fte'], t) * a['loaded']
        op_other = sum(yr(a[k], t) for k in ('proto', 'swdata', 'space', 'cert_ip', 'research', 'mkt', 'ga'))
        opex = op_people + op_other
        op = contrib - opex
        cash = op + c_dep - capex
        backlog = (a['projects'][t] + (a['projects'][t - 1] if t >= 1 else 0)) * a['hh_project'] * a['option_rate']
        for k, v in dict(rd=rd, rp=rp, ni=ni, kitchens=rd + rp + ni, pl_remodel=pl_remodel, later=later, pl_new=pl_new,
                         pl=pl, rpl=rpl, pp=pp, drpl=drpl, prpl=prpl, pool=pool, pb_end=pb_end, pb_avg=pb_avg,
                         dr_end=dr_end, dr_avg=dr_avg, pr_end=pr_end, pr_avg=pr_avg, base_end=pb_end + dr_end + pr_end,
                         rev_kitchen=rev_kitchen, rev_comm=rev_comm, rev_robot=rev_robot, rev_rental=rev_rental,
                         rev_care=rev_care, rev_cons=rev_cons, rev_upg=rev_upg, rev=rev, c_kitchen=c_kitchen,
                         c_log=c_log, c_robot=c_robot, c_comm=c_comm, c_warranty=c_warranty, c_dep=c_dep,
                         c_care=c_care, c_cons=c_cons, c_upg=c_upg, cogs=cogs, gp=gp, ch_partner=ch_partner,
                         ch_cac=ch_cac, ch_bd=ch_bd, contrib=contrib, op_people=op_people, op_other=op_other,
                         opex=opex, op=op, capex=capex, cash=cash, backlog=backlog, kit_unit_cost=kit_unit,
                         care_unit_cost=care_unit).items():
            L[k][t] = v
        L['cum_cash'][t] = (L['cum_cash'][t - 1] if t else 0) + cash
        cum_capex_prev += capex
    # derived shares
    L['build'] = [L['rev_kitchen'][t] + L['rev_comm'][t] for t in range(N)]
    L['recurring'] = [L['rev_rental'][t] + L['rev_care'][t] + L['rev_cons'][t] for t in range(N)]
    L['gm'] = [L['gp'][t] / L['rev'][t] if L['rev'][t] else 0 for t in range(N)]
    L['robot_recurring_share'] = [(L['rev_robot'][t] + L['recurring'][t] + L['rev_upg'][t]) / L['rev'][t] if L['rev'][t] else 0
                                  for t in range(N)]
    L['min_cum_cash'] = min(L['cum_cash'])
    return L

# ---------------------------------------------------------------- household / unit economics (Base)
def household(s='B', t=2, channel='direct', mode='purchase', ov=None):
    """One representative 구축 Premium household, 5 years, expected values, cost level of year index t."""
    a = V(s, ov)
    smr = yr(a['smr'], t); bom = yr(a['bom'], t)
    kit_unit = a['kit_std_cost'] * (smr + a['custom_factor'] * (1 - smr)) + a['design_cost'] * (1 - smr)
    care_unit = yr(a['visits'], t) * yr(a['visit_cost'], t) + a['corrective'] * a['corr_cost'] + a['cloud']
    cons_y = a['p_grip'] * a['n_grip'] + a['p_clean'] * a['n_clean'] + a['p_protect'] * a['n_protect']
    cons_y_rent = a['p_clean'] * a['n_clean'] + a['p_protect'] * a['n_protect']
    grip_y = a['p_grip'] * a['n_grip']
    R = {}; C = {}
    R['kitchen'] = a['p_rr']; R['comm'] = a['p_comm']
    R['sw'] = a['sw_attach'] * a['p_sw']; R['tool'] = a['tool_attach'] * a['p_tool']
    C['kitchen'] = kit_unit; C['comm'] = yr(a['comm_cost'], t); C['log'] = a['logistics']
    C['sw'] = R['sw'] * a['sw_cogs']; C['tool'] = R['tool'] * a['tool_cogs']
    if mode == 'purchase':
        R['robot'] = a['p_robot']; R['care'] = 5 * a['p_care']          # Care 가입 세대 기준
        R['cons'] = 5 * a['cons_attach'] * cons_y
        C['robot'] = bom; C['warranty'] = a['warranty'] * a['p_robot']
        C['care'] = 5 * care_unit; C['cons'] = R['cons'] * a['cons_cogs']
    else:
        R['rental'] = a['p_rent'] * a['rent_months']
        R['cons'] = 5 * a['cons_attach'] * cons_y_rent
        C['robot'] = bom * (1 - a['residual'])                              # 순 감가 (잔존가치 회수)
        C['finance'] = bom * (1 + a['residual']) / 2 * a['fin_rate'] * 5
        C['warranty'] = a['warranty'] * bom
        C['care'] = 5 * care_unit; C['cons'] = (R['cons'] + 5 * grip_y) * a['cons_cogs']
    y0 = R['kitchen'] + R['comm'] + R.get('robot', 0)
    if channel == 'direct':
        C['channel'] = a['cac']
    else:
        C['channel'] = a['partner_margin'] * (a['p_rr'] + a['p_robot'] + a['p_comm'])
    rev5 = sum(R.values()); cost5 = sum(C.values())
    gp5 = rev5 - (cost5 - C['channel'])
    return dict(R=R, C=C, y0=y0, rev5=rev5, cost5=cost5, gp5=gp5, contrib5=rev5 - cost5,
                gm5=gp5 / rev5, cm5=(rev5 - cost5) / rev5, recurring5=rev5 - y0 - R['sw'] - R['tool'],
                kit_unit=kit_unit, care_unit=care_unit, bom=bom)

def rental_econ(s='B', t=2, ov=None):
    a = V(s, ov); bom = yr(a['bom'], t)
    care_unit = yr(a['visits'], t) * yr(a['visit_cost'], t) + a['corrective'] * a['corr_cost'] + a['cloud']
    m = a['rent_months']
    lines = dict(dep=bom * (1 - a['residual']) / m,
                 fin=bom * (1 + a['residual']) / 2 * a['fin_rate'] / 12,
                 care=care_unit / 12,
                 grip=a['p_grip'] * a['n_grip'] * a['cons_cogs'] / 12,
                 reserve=a['warranty'] * bom / m)
    cost_m = sum(lines.values())
    fee = a['p_rent']
    op_cash_m = fee - lines['care'] - lines['grip']
    payback = bom / op_cash_m
    bom_max = a['payback_hurdle'] * op_cash_m
    return dict(lines=lines, cost_m=cost_m, fee=fee, contrib_m=fee - cost_m, margin=(fee - cost_m) / fee,
                fee_at_20=cost_m / 0.8, payback=payback, bom_max=bom_max, bom=bom)

def care_econ(s='B', t=2):
    a = V(s); cu = yr(a['visits'], t) * yr(a['visit_cost'], t) + a['corrective'] * a['corr_cost'] + a['cloud']
    return dict(fee=a['p_care'], visits=yr(a['visits'], t) * yr(a['visit_cost'], t),
                corrective=a['corrective'] * a['corr_cost'], cloud=a['cloud'], cost=cu,
                contrib=a['p_care'] - cu, margin=(a['p_care'] - cu) / a['p_care'])

def cons_econ(s='B'):
    a = V(s)
    kits = [('Grip Kit', a['p_grip'], a['n_grip']), ('Cleaning Kit', a['p_clean'], a['n_clean']),
            ('Protection Kit', a['p_protect'], a['n_protect'])]
    list_y = sum(p * n for _, p, n in kits)
    rev = list_y * a['cons_attach']
    return dict(kits=kits, list_y=list_y, rev=rev, cogs=rev * a['cons_cogs'], contrib=rev * (1 - a['cons_cogs']),
                margin=1 - a['cons_cogs'], attach=a['cons_attach'])

# ---------------------------------------------------------------- market
def market(s='B'):
    a = V(s)
    apt = a['m_housing_total'] * a['m_apt_share']                                   # 천호
    tri1 = a['m_apt_20y_2023'] / a['a_replace_cycle']
    tri2 = a['m_txn_2025'] * a['a_txn_apt_share'] * a['a_txn_kitchen_rate'] + a['a_aging_nontxn']
    rep = a['a_kitchen_replace']
    prem = rep * a['a_premium_share']
    fit = prem * a['a_fit_rate']
    att = yr(a['attach'], 4)
    pkg_remodel = a['p_rr'] + att * (a['p_robot'] + a['p_comm'])                     # 만원/세대
    pkg_full = a['p_rr'] + a['p_robot'] + a['p_comm']
    new_prem = a['a_new_supply'] * a['a_premium_project']
    new_opt = new_prem * a['option_rate']
    pkg_new = a['p_rr_new'] + a['new_attach'] * (a['p_robot'] + a['p_comm'])
    tam = (prem + new_prem) * pkg_full / 10        # 억원  (천세대 × 만원 → 천만원 → /10 = 억원)
    sam_remodel = fit * pkg_remodel / 10
    sam_new = new_opt * pkg_new / 10
    sam = sam_remodel + sam_new
    som = run(s)['rev'][4] / 10000                  # 억원 (Y5 plan)
    som_hh = run(s)['kitchens'][4]
    return dict(apt=apt, tri1=tri1, tri2=tri2, rep=rep, prem=prem, fit=fit, pkg_remodel=pkg_remodel, pkg_full=pkg_full,
                new_prem=new_prem, new_opt=new_opt, pkg_new=pkg_new, tam=tam, sam_remodel=sam_remodel, sam_new=sam_new,
                sam=sam, som=som, som_hh=som_hh, som_share_hh=som_hh / ((fit + new_opt) * 1000),
                kitchen_pool=rep + a['a_new_supply'])

def value_anchor(s='B'):
    a = V(s)
    hours = a['a_cleanup_min'] / 60 * 30
    v = hours * a['f_helper_rate'] * a['a_auto_share']
    lo = 30 / 60 * 30 * a['f_helper_rate'] * 0.5
    hi = 45 / 60 * 30 * a['f_helper_rate'] * 0.7
    return dict(hours=hours, value=v, lo=lo, hi=hi)

# ---------------------------------------------------------------- sensitivity
def sens_household():
    base = household('B', 2)['contrib5']
    items = [
        ('Robot ASP (WTP) ±20%', {'p_robot': lambda v: v * 0.8}, {'p_robot': lambda v: v * 1.2}),
        ('Robot BOM ±20%', {'bom': lambda v: [x * 1.2 for x in v]}, {'bom': lambda v: [x * 0.8 for x in v]}),
        ('Robot-ready 증분가 ±20%', {'p_rr': lambda v: v * 0.8}, {'p_rr': lambda v: v * 1.2}),
        ('직접판매 획득비용 ±50%', {'cac': lambda v: v * 1.5}, {'cac': lambda v: v * 0.5}),
        ('Care 요금 ±20%', {'p_care': lambda v: v * 0.8}, {'p_care': lambda v: v * 1.2}),
        ('방문 원가 ±30%', {'visit_cost': lambda v: [x * 1.3 for x in v]}, {'visit_cost': lambda v: [x * 0.7 for x in v]}),
        ('Standard Module 사용률 -15pp/+15pp', {'smr': lambda v: [x - 0.15 for x in v]}, {'smr': lambda v: [x + 0.15 for x in v]}),
        ('설치 원가 ±50%', {'comm_cost': lambda v: [x * 1.5 for x in v]}, {'comm_cost': lambda v: [x * 0.5 for x in v]}),
        ('Failure Rate 0.3 ↔ 1.2회', {'corrective': 1.2, 'warranty': 0.06}, {'corrective': 0.3, 'warranty': 0.025}),
        ('Consumables 구매율 50% ↔ 90%', {'cons_attach': 0.5}, {'cons_attach': 0.9}),
    ]
    out = []
    for name, lo, hi in items:
        out.append(dict(name=name, lo=household('B', 2, ov=lo)['contrib5'] - base,
                        hi=household('B', 2, ov=hi)['contrib5'] - base))
    out.sort(key=lambda d: -(abs(d['lo']) + abs(d['hi'])))
    return dict(base=base, items=out)

def sens_company():
    """Y5 Contribution (GP − 채널비용) change, Base."""
    base = run('B')['contrib'][4]
    items = [
        ('Customer WTP (Robot ASP·증분가 ±20%)', {'p_robot': lambda v: v * 0.8, 'p_rr': lambda v: v * 0.8},
         {'p_robot': lambda v: v * 1.2, 'p_rr': lambda v: v * 1.2}),
        ('Robot BOM ±20%', {'bom': lambda v: [x * 1.2 for x in v]}, {'bom': lambda v: [x * 0.8 for x in v]}),
        ('Partner 경유 Kitchen ±30%', {'rp': lambda v: [x * 0.7 for x in v]}, {'rp': lambda v: [x * 1.3 for x in v]}),
        ('Robot Attach Rate 65% ↔ 95%', {'attach': lambda v: [1, 1, .65, .65, .65]}, {'attach': lambda v: [1, 1, .95, .95, .95]}),
        ('Standard Module 사용률 -15pp/+10pp', {'smr': lambda v: [x - 0.15 for x in v]}, {'smr': lambda v: [min(x + 0.10, 0.95) for x in v]}),
        ('설치 원가 ±50%', {'comm_cost': lambda v: [x * 1.5 for x in v]}, {'comm_cost': lambda v: [x * 0.5 for x in v]}),
        ('Service 원가 (방문) ±30%', {'visit_cost': lambda v: [x * 1.3 for x in v]}, {'visit_cost': lambda v: [x * 0.7 for x in v]}),
        ('Failure Rate 0.3 ↔ 1.2회', {'corrective': 1.2, 'warranty': 0.06}, {'corrective': 0.3, 'warranty': 0.025}),
        ('신축 Option 선택률 5% ↔ 15%', {'option_rate': 0.05}, {'option_rate': 0.15}),
        ('Rental 비중 20% ↔ 60%', {'rental_share': lambda v: [0, .3, .3, .6, .6]}, {'rental_share': lambda v: [0, .3, .3, .2, .2]}),
    ]
    out = []
    for name, lo, hi in items:
        out.append(dict(name=name, lo=run('B', lo)['contrib'][4] - base, hi=run('B', hi)['contrib'][4] - base))
    out.sort(key=lambda d: -(abs(d['lo']) + abs(d['hi'])))
    return dict(base=base, items=out)

# ---------------------------------------------------------------- TIPS 기간 (24개월) 자금 계획
# 팀 (ASSUMPTION): (역할, 시작 월, 인건비 구분, TIPS 과제 참여율). 대표 외 인원은 모두 신규 채용 계획 (Founder 정보 미제공).
TIPS_TEAM = [('대표 (과제책임자)', 1, '현물', 0.5), ('로봇 제어 · 조작 연구원', 1, '현금', 0.8), ('비전 · ML 연구원', 2, '현금', 0.8),
             ('메카트로닉스 · 기구 연구원', 2, '현금', 0.8), ('임베디드 · 전기 · 안전 연구원', 6, '현금', 0.8),
             ('설치 · 실증 엔지니어', 13, '현금', 0.5), ('사업개발 · 고객 조사', 13, '과제 외', 0.0)]
# R&D 과제 예산 중 인건비 외 비목 (ASSUMPTION, 만원): (비목, 내용, Y1, Y2)
TIPS_OTHER = [('연구재료비', '시제품 1차 2식 · 실물 크기 목업 주방 2식 (Y1) / 실증용 하드웨어 · 2차 개선 부품 (Y2)', 12000, 6500),
              ('연구활동비', '외주 가공 · SW · 연구실 운영 · 특허 2건 (Y1) / 공인시험 · 안전 사전시험 · 특허 3건 (Y2)', 6000, 9200),
              ('연구수당', '참여 연구원 (인건비 대비 약 5%)', 1400, 1800)]
TIPS_Y1 = 50000                  # R&D 과제 1차년도 총액 (ASSUMPTION); 2차년도 = 총액 − 1차년도, 간접비 = 연차 총액 − 직접비

def tips_plan():
    a = V('B'); L = run('B')
    mo = a['loaded'] / 12
    pm = []                       # person-months per member and year
    for role, m0, kind, part in TIPS_TEAM:
        y1 = max(0, 12 - (m0 - 1)) if m0 <= 12 else 0
        y2 = 12 if m0 <= 13 else max(0, 24 - (m0 - 1))
        pm.append((role, m0, kind, part, y1, y2))
    fte = [sum(p[4] for p in pm) / 12, sum(p[5] for p in pm) / 12]
    assert abs(round(fte[0], 1) - a['fte'][0]) < 1e-9 and abs(fte[1] - a['fte'][1]) < 1e-9, ('TIPS team vs fte', fte)
    pay = lambda kind, t: sum(p[4 + t] * p[3] * mo for p in pm if p[2] == kind)
    rows = [('인건비', f"신규 연구원 {sum(1 for p in pm if p[2] == '현금')}명 (참여율 50~80%)", pay('현금', 0), pay('현금', 1), '현금'),
            ('인건비', '대표 (과제책임자, 참여율 50%)', pay('현물', 0), pay('현물', 1), '현물')]
    rows += [(c, d, y1, y2, '현금') for c, d, y1, y2 in TIPS_OTHER]
    direct = [sum(r[2 + t] for r in rows) for t in (0, 1)]
    total = a['tips'] / a['tips_gov_ratio']          # 정부지원금 최대를 쓰는 총 연구개발비
    year_total = (TIPS_Y1, total - TIPS_Y1)
    rows.append(('간접비', '연구개발 지원 · 성과활용 (직접비 대비)', year_total[0] - direct[0], year_total[1] - direct[1], '현금'))
    inkind = sum(r[2] + r[3] for r in rows if r[4] == '현물')
    private = total - a['tips']; private_cash = private - inkind
    assert private_cash >= a['tips_cash_ratio'] * private - 1e-6, ('cash share of 기관부담', private_cash)
    assert all(r[2] >= 0 and r[3] >= 0 for r in rows)
    gov_y = [year_total[t] * a['tips_gov_ratio'] for t in (0, 1)]
    spend = [-L['cash'][0], -L['cash'][1]]           # 회사 전체 지출 (실증 매출 차감 후, TIPS 과제 외 비용 포함)
    spend_total = sum(spend)
    srcs = [('TIPS R&D 정부지원금', a['tips'], 'FACT'), ('운영사 투자 (요청)', a['op_invest'], 'ASSUMPTION'),
            ('후속 투자 (M12 목표)', a['followon'], 'TARGET')]
    src_total = sum(v for _, v, _ in srcs)
    # runway without the follow-on round: monthly burn flat within a year, grant paid at the start of each year
    avail = lambda m: a['op_invest'] + gov_y[0] + (gov_y[1] if m > 12 else 0)
    used = lambda m: spend[0] * min(m, 12) / 12 + (spend[1] * (m - 12) / 12 if m > 12 else 0)
    runway = 24.0
    for k in range(1, 241):
        m = k / 10
        if used(m) > avail(m) + 1e-6:
            runway = m - 0.1; break
    # what the R&D budget covers inside the company spend (for the uses chart)
    people = sum(r[2] + r[3] for r in rows if r[0] in ('인건비', '연구수당'))
    return dict(team=[dict(role=p[0], start=p[1], kind=p[2], part=p[3], pm_y1=p[4], pm_y2=p[5]) for p in pm], fte=fte,
                rows=[dict(cat=r[0], item=r[1], y1=r[2], y2=r[3], kind=r[4], total=r[2] + r[3]) for r in rows],
                year_total=list(year_total), total=total, gov=a['tips'], gov_y=gov_y, private=private, private_cash=private_cash,
                inkind=inkind, indirect_rate=(total - sum(direct)) / sum(direct), people_rnd=people,
                spend=spend, spend_total=spend_total, non_rnd=spend_total - total, company_need=spend_total - a['tips'],
                sources=[dict(name=n, value=v, tag=t) for n, v, t in srcs], src_total=src_total, buffer=src_total - spend_total,
                runway_no_followon=runway, biz_link=a['biz_link'], months=a['tips_months'])


# ---------------------------------------------------------------- BOM breakdown (ASSUMPTION, 만원/대) — sums equal Base bom Y1 / Y3 / Y5
BOM_BREAKDOWN = [  # (item, pilot(Y1), Y3, Y5, basis)
    ('6축 Arm (가반 3~5kg, Controller 포함)', 950, 600, 450, 'FAIRINO FR5 $6,999 · xArm 6 $8,399 공개가 → OEM·국산 Partner·전용 Arm'),
    ('Linear Rail · Carriage · Servo (2.4~3.6m)', 180, 150, 120, 'Belt 구동 7축 Rail. 소형 KK Module $73~245는 참고만'),
    ('End-effector Set (Gripper + Suction + Tool Changer)', 120, 90, 70, 'Robotiq 2F-85 $4,999 대비 저가 전동 Gripper + 자체 Finger'),
    ('Vision (Depth Camera 2대 + Mount)', 110, 80, 60, 'Orbbec Gemini 335 $384~400 · RealSense D405 $514'),
    ('Compute (Edge GPU)', 100, 80, 70, 'Edge AI Module 가정'),
    ('Safety (Zone Sensor·Safety Controller)', 70, 60, 50, 'ToF/Radar Zone Sensor + Safety Relay 가정'),
    ('Garage Door · Harness · Enclosure', 70, 50, 45, ''),
    ('조립·시험 (Pilot은 Opex 인건비 처리)', 0, 40, 35, ''),
]

def partner_irr(s='B', months=None):
    """Rental Partner IRR: buys robot at ASP × wholesale, receives (rent − ARKI service fee) monthly, residual at end."""
    a = V(s); m = months or a['rent_months']
    price = a['p_robot'] * a['wholesale']; inflow = a['p_rent'] - a['partner_fee']; resid = price * a['residual']
    def npv(r):
        return -price + sum(inflow / (1 + r) ** k for k in range(1, m + 1)) + resid / (1 + r) ** m
    lo, hi = 0.0, 0.1
    for _ in range(200):
        mid = (lo + hi) / 2
        if npv(mid) > 0: lo = mid
        else: hi = mid
    return dict(price=price, inflow=inflow, resid=resid, irr_m=lo, irr_y=(1 + lo) ** 12 - 1)

# ---------------------------------------------------------------- export
def main():
    M = {'inputs': INPUTS, 'scenarios': {}, 'years': YEARS}
    for s in SC:
        M['scenarios'][s] = run(s)
    hh = {}
    for t, lab in ((2, 'Y3'), (4, 'Y5')):
        for mode in ('purchase', 'rental'):
            for ch in ('direct', 'partner'):
                hh[f'{mode}_{ch}_{lab}'] = household('B', t, ch, mode)
    M['household'] = hh
    M['rental'] = {lab: rental_econ('B', t) for t, lab in ((2, 'Y3'), (4, 'Y5'))}
    M['rental_C'] = {lab: rental_econ('C', t) for t, lab in ((2, 'Y3'), (4, 'Y5'))}
    M['care'] = {lab: care_econ('B', t) for t, lab in ((2, 'Y3'), (4, 'Y5'))}
    M['cons'] = cons_econ('B')
    M['market'] = {s: market(s) for s in SC}
    M['value'] = value_anchor('B')
    M['sens_household'] = sens_household()
    M['sens_company'] = sens_company()
    M['tips'] = tips_plan()
    M['bom_breakdown'] = BOM_BREAKDOWN
    bb = V('B')['bom']
    for col, t in ((1, 0), (2, 2), (3, 4)):
        assert abs(sum(r[col] for r in BOM_BREAKDOWN) - bb[t]) < 1e-9, ('BOM breakdown', col)
    M['partner_irr'] = {s: partner_irr(s) for s in SC}
    # break-even kitchens (Y5 Base contribution per kitchen vs Y5 opex)
    B = M['scenarios']['B']
    cpk = B['contrib'][4] / B['kitchens'][4]
    M['breakeven_kitchens'] = B['opex'][4] / cpk
    M['contrib_per_kitchen_y5'] = cpk
    # steady-state recurring share (DERIVED illustration: installed base = 6 × annual placements)
    a = V('B'); rs = 0.4
    cons_y = a['p_grip'] * a['n_grip'] + a['p_clean'] * a['n_clean'] + a['p_protect'] * a['n_protect']
    cons_y_rent = a['p_clean'] * a['n_clean'] + a['p_protect'] * a['n_protect']
    arpu = (1 - rs) * (a['care_attach'] * a['p_care'] + a['cons_attach'] * cons_y) + rs * (a['partner_fee'] * 12 + a['cons_attach'] * cons_y_rent)
    y0 = a['p_rr'] / 0.85 + (1 - rs) * a['p_robot'] + rs * a['p_robot'] * a['wholesale'] + a['p_comm']
    upg = a['p_robot'] * 0.30 / 6.5
    M['steady'] = dict(arpu=arpu, y0=y0, upg=upg, base_mult=6,
                       rec_share=6 * arpu / (y0 + 6 * arpu + 6 * upg), upg_share=6 * upg / (y0 + 6 * arpu + 6 * upg))
    # sanity checks
    for s in SC:
        L = M['scenarios'][s]
        for t in range(N):
            parts = sum(L[k][t] for k in ('rev_kitchen', 'rev_comm', 'rev_robot', 'rev_rental', 'rev_care', 'rev_cons', 'rev_upg'))
            assert abs(parts - L['rev'][t]) < 1e-6
            assert abs(L['pl'][t] - L['rpl'][t] - L['pp'][t]) < 1e-9
            assert L['pool'][t] >= -1e-9
    assert M['scenarios']['C']['rev'][4] < M['scenarios']['B']['rev'][4] < M['scenarios']['U']['rev'][4]
    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump(M, f, ensure_ascii=False, indent=1)
    return M

if __name__ == '__main__':
    M = main()
    for s in SC:
        L = M['scenarios'][s]
        print(SCN[s], 'rev(억)', [round(x / 10000, 1) for x in L['rev']], 'GP%', [round(x * 100) for x in L['gm']],
              'contrib(억)', [round(x / 10000, 1) for x in L['contrib']], 'OP(억)', [round(x / 10000, 1) for x in L['op']],
              'kitchens', [round(x) for x in L['kitchens']], 'robots', [round(x) for x in L['pl']],
              'base', round(L['base_end'][4]), 'cumcash(억)', round(L['min_cum_cash'] / 10000, 1))
    for k, h in M['household'].items():
        print(k, 'y0', round(h['y0']), 'rev5', round(h['rev5']), 'gp5', round(h['gp5']), 'contrib5', round(h['contrib5']),
              'cm', round(h['cm5'] * 100, 1))
    print('rental', {k: (round(v['contrib_m'], 2), round(v['payback'], 1), round(v['bom_max']), round(v['fee_at_20'], 1)) for k, v in M['rental'].items()})
    print('care', {k: (round(v['cost'], 1), round(v['margin'] * 100)) for k, v in M['care'].items()})
    print('cons', M['cons']['rev'], M['cons']['contrib'])
    print('market', {k: round(v, 1) if isinstance(v, float) else v for k, v in M['market']['B'].items()})
    print('value', M['value'])
    print('sens hh', M['sens_household']['base'], [(d['name'], round(d['lo']), round(d['hi'])) for d in M['sens_household']['items']])
    print('sens co', round(M['sens_company']['base']), [(d['name'], round(d['lo']), round(d['hi'])) for d in M['sens_company']['items']])
    TP = M['tips']
    print('tips rows', [(r['cat'], round(r['y1']), round(r['y2']), r['kind']) for r in TP['rows']], 'total', TP['total'], 'cash', round(TP['private_cash']), 'inkind', round(TP['inkind']), 'indirect', round(TP['indirect_rate'] * 100, 1))
    print('tips spend', [round(x) for x in TP['spend']], round(TP['spend_total']), 'need', round(TP['company_need']), 'sources', TP['src_total'], 'buffer', round(TP['buffer']), 'runway w/o follow-on', TP['runway_no_followon'], 'fte', TP['fte'])
    print('breakeven kitchens', round(M['breakeven_kitchens']), 'cpk', round(M['contrib_per_kitchen_y5']))
    print('steady', M['steady'])
    print('partner irr', {k: round(v['irr_y'] * 100, 1) for k, v in M['partner_irr'].items()})
