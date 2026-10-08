# MH Robotics — Seed + TIPS IR model (single source of truth for the deck, the xlsx and the docs)
# Units: 만원 (KRW 10,000) unless a unit says otherwise.
# Year Y1 = M1~M12 (Seed + TIPS 1차년도), Y2 = M13~M24 (TIPS 2차년도), Y3 = 후속 투자 (Series A) 이후.
# Every input carries a tag: FACT / DERIVED / ASSUMPTION / TARGET.
#   python3 MH/source/model.py   -> MH/source/model.json (+ sanity asserts)
import json, os, copy

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'model.json')
SC = ('C', 'B', 'U')
SCN = {'C': 'Conservative', 'B': 'Base', 'U': 'Upside'}
YEARS = ['Y1', 'Y2', 'Y3', 'Y4', 'Y5']
N = 5

# ---------------------------------------------------------------- 24개월 팀 계획 (ASSUMPTION)
# (key, 역할, 시작 월, 인당 연 인건비(4대보험·퇴직급여 포함), FTE 비율, TIPS 과제 참여율, 구분, Lean 포함, Lean 시작 월)
# Founder 2인은 TIPS 요건 (대표 포함 창업팀 2인 이상) 기준의 자리이며 실제 인물 정보는 비워 둔다.
TEAM = [
    ('F1', '대표 · 사업 총괄 [Founder 정보 필요]', 1, 6000, 1.0, 0.5, 'founder', True, None),
    ('F2', '공동창업자 · 기술 총괄 [Founder 정보 필요]', 1, 6000, 1.0, 0.6, 'founder', True, None),
    ('E1', 'Manipulation · 제어 리드', 1, 9600, 1.0, 0.5, 'rnd', True, None),
    ('E2', 'Perception · ML 리드', 2, 9600, 1.0, 0.5, 'rnd', True, None),
    ('E3', 'Hand · 기구 리드 (메카트로닉스)', 2, 9600, 1.0, 0.6, 'rnd', True, None),
    ('E4', '임베디드 · 전기 · 안전', 4, 7800, 1.0, 0.5, 'rnd', True, None),
    ('E5', 'Robot SW · 통합 (Motion · Skill)', 6, 7800, 1.0, 0.5, 'rnd', True, None),
    ('B1', '제품 · 사업개발 (고객 검증 · 파트너)', 7, 7200, 1.0, 0.0, 'biz', True, None),
    ('E6', 'Hand 센싱 (Grip Force · Slip)', 10, 7800, 1.0, 0.5, 'rnd', False, None),
    ('O1', '경영지원 (재무 · 과제 관리, 0.5 FTE)', 10, 5400, 0.5, 0.0, 'ops', True, None),
    ('E7', '시험 · 신뢰성 (Test · QA)', 13, 7800, 1.0, 0.4, 'rnd', True, 19),
    ('S1', '설치 · Commissioning 엔지니어', 13, 6600, 1.0, 0.0, 'field', True, None),
    ('E8', 'Skill · Data 엔지니어', 16, 7800, 1.0, 0.4, 'rnd', False, None),
    ('S2', '현장 서비스 Technician', 19, 5400, 1.0, 0.0, 'field', False, None),
]
TEAM_KIND = {'founder': 'Founder', 'rnd': 'R&D', 'biz': '사업', 'ops': '경영지원', 'field': '현장'}

# 인건비 외 24개월 지출 (ASSUMPTION, 만원): key, 구분 (Spec 33 항목), 내용, Base(Y1, Y2), Lean(Y1, Y2), TIPS 과제 편성 비율 (Y1, Y2), TIPS 비목
COSTS = [
    ('robot_hw', 'Robot Hardware', 'R&D 로봇 셀 (Arm · Vision · Compute) Y1 3식 + Y2 1식', (4800, 1600), (4800, 0), (0.8, 0.8), '연구재료비'),
    ('hand_proto', 'Hand Prototype', '상용 Gripper 비교군 구매 · 자체 Hand v1~v3 가공 · 센서 · Pad 금형', (6000, 4000), (5000, 3000), (0.9, 0.9), '연구재료비'),
    ('mockup', 'Kitchen Mock-up', '실물 크기 목업 3종 (Remodeling · ㄱ자 · Retrofit) · 식기세척기 3모델 · 재구성', (5000, 2500), (4000, 1000), (0.8, 0.8), '연구재료비'),
    ('swdata', 'Software · Data', 'GPU · Cloud · Annotation · SW License', (2500, 3000), (2000, 2000), (0.8, 0.8), '연구활동비'),
    ('pilot', 'Pilot', '가정 실증 운영 (설치 파트너 · 보험 · 모니터링). 실증 하드웨어는 원가로 별도', (0, 3500), (0, 2500), (0.0, 0.0), '-'),
    ('custval', 'Customer · Partner', '고객 인터뷰 · 정리 시간 기록 · WTP 조사 (n≥300) · 예약금 Test · 파트너 개발 · 전시', (2000, 4000), (1500, 2500), (0.0, 0.0), '-'),
    ('cert', 'Certification', '안전 Gap 분석 (IEC 63682 초안 · ISO 13482) · EMC/전기안전 사전시험 · 식품접촉 소재 시험', (1500, 4500), (1500, 2000), (1.0, 0.45), '연구활동비'),
    ('ip', 'IP', '선행기술조사 · 국내 출원 5건 · PCT 1건', (1500, 3000), (1200, 1800), (0.8, 0.8), '연구활동비'),
    ('space', 'Space', '실험실 · 목업 공간 (약 50평) 임차 · 관리', (4800, 4800), (3600, 3600), (0.0, 0.0), '간접비 일부'),
    ('ga', 'Operating', '법무 · 회계 · 보험 · 사무 · 출장 · 채용', (4000, 5000), (3500, 4000), (0.0, 0.0), '간접비 일부'),
]
CONTINGENCY = 0.10        # 인건비 외 지출의 10% 예비비 (ASSUMPTION)
ALLOW_RATE = 0.05         # 연구수당 = TIPS 과제 현금 인건비의 5% (ASSUMPTION, 상한 내)
BUFFER_MONTHS = 3         # M24 시점 Series A 협상 기간 Buffer (Y2 월평균 지출 × 3)


def team_plan(scope='base'):
    out = []
    for key, role, m0, cost, frac, part, kind, lean, lean_m0 in TEAM:
        if scope == 'lean' and not lean:
            continue
        st = (lean_m0 or m0) if scope == 'lean' else m0
        pm1 = max(0, 12 - (st - 1)) if st <= 12 else 0
        pm2 = 12 if st <= 13 else max(0, 24 - (st - 1))
        c1, c2 = cost * frac * pm1 / 12, cost * frac * pm2 / 12
        out.append(dict(key=key, role=role, start=st, loaded=cost, frac=frac, part=part, kind=kind,
                        pm=[pm1 * frac, pm2 * frac], cost=[c1, c2]))
    return out


def budget24(scope='base'):
    """24개월 Bottom-up 예산. 5개년 모델 Y1~Y2 Opex의 원천."""
    tm = team_plan(scope)
    people = [sum(m['cost'][t] for m in tm) for t in (0, 1)]
    fte = [sum(m['pm'][t] for m in tm) / 12 for t in (0, 1)]
    k = 3 if scope == 'base' else 4
    lines = [dict(key=c[0], cat=c[1], item=c[2], y=list(c[k]), tips_share=list(c[5]), tips_cat=c[6]) for c in COSTS]
    other = [sum(l['y'][t] for l in lines) for t in (0, 1)]
    cont = [CONTINGENCY * other[t] for t in (0, 1)]
    # TIPS 과제 (Base만 편성표 작성). 인건비 현금 = R&D 인원 × 참여율, 현물 = Founder × 참여율
    tips_cash_pay = [sum(m['cost'][t] * m['part'] for m in tm if m['kind'] == 'rnd') for t in (0, 1)]
    allow = [ALLOW_RATE * tips_cash_pay[t] for t in (0, 1)]
    return dict(scope=scope, team=tm, people=people, fte=fte, lines=lines, other=other, contingency=cont,
                allow=allow, tips_cash_pay=tips_cash_pay,
                heads_m24=sum(1 for m in tm if m['pm'][1] > 0 and m['frac'] >= 1) + sum(m['frac'] for m in tm if m['frac'] < 1),
                opex=[people[t] + other[t] + cont[t] + allow[t] for t in (0, 1)])


BUD = {'base': budget24('base'), 'lean': budget24('lean')}

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

# --- market (FACT = public statistics; see docs/07 for URLs)
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
inp('a_replace_cycle', 'market', 'Kitchen 교체주기 (노후 아파트)', '년', 'ASSUMPTION', 22, '교차검증용 가정. 견적 · 인터뷰로 검증')
inp('a_txn_apt_share', 'market', '매매거래 중 아파트 비중', '%', 'ASSUMPTION', 0.70, '부동산원 월별 아파트 거래 비중 확인 필요')
inp('a_txn_kitchen_rate', 'market', '매수 후 Kitchen 교체율', '%', 'ASSUMPTION', 0.40, '인터뷰 · 인테리어 Partner 자료로 검증')
inp('a_aging_nontxn', 'market', '비거래 노후 교체 세대', '천/년', 'ASSUMPTION', 100, '교차검증용 가정')
inp('a_kitchen_replace', 'market', '연간 Kitchen 교체 세대 (아파트)', '천/년', 'ASSUMPTION', 300, '두 방식 교차검증 (29만 · 30만) 후 30만으로 설정')
inp('a_premium_share', 'market', 'Premium Kitchen 비중 (교체 세대 중)', '%', 'ASSUMPTION', 0.10, '주방 예산 2,000만원 이상 가정. 견적 수집으로 검증')
inp('a_fit_rate', 'market', 'Remodeling 적용 가능률 (구조 · 전원 · 평면)', '%', 'ASSUMPTION', 0.60, '평면 30개 분석으로 검증')
inp('a_prem_stock', 'market', 'Premium 세대 비중 (아파트 재고 기준)', '%', 'ASSUMPTION', 0.10, 'Retrofit 대상. 소득 · 주택가격 기준 정의 필요')
inp('a_dw_premium', 'market', 'Premium 세대 식기세척기 보유율', '%', 'ASSUMPTION', 0.60, '공식 보급률 통계 확인 안 됨 (2019~20 업계 추정 10%대 초반 · 전체 가구) → TO BE VALIDATED')
inp('a_retro_fit', 'market', 'Retrofit 호환률 (주방 형태 · 식세기 위치 · 상부장)', '%', 'ASSUMPTION', 0.40, '가설. 확보 평면 5종 (Remodeling 기본 배치 수용 1 · 미수용 3 · 미검토 1)으로는 판단 불가 → 평면 30개 · 상담 주방 실측으로 검증')
inp('a_retro_conv', 'market', 'Retrofit 연간 전환율 (호환 세대 중, 제품 성숙 후)', '%', 'ASSUMPTION', 0.005, '가설. Phase 2 시작 전 검증')
inp('a_new_supply', 'market', '연간 신규 아파트 입주 (평균)', '천/년', 'ASSUMPTION', 200, '2025 실적 23.6만 · 2026 예정 18.3만 (평균 21.0만) → 보수적으로 20만')
inp('a_premium_project', 'market', 'Premium 단지 비중 (신축)', '%', 'ASSUMPTION', 0.15, '브랜드 · 분양가 기준 정의 필요')

# --- value anchor
inp('f_helper_rate', 'value', '가사서비스 시간당 요금 (플랫폼 4시간 59,900~64,900원)', '만원/h', 'FACT', 1.5,
    '가사서비스 플랫폼 공개 요금 (2025, 보도 · 앱 정보)')
inp('a_cleanup_min', 'value', '식사 후 정리 시간 (식기 이동 · 식세기 · 수납, 일)', '분/일', 'ASSUMPTION', 40, 'Time-diary(n=30)로 검증')
inp('a_auto_share', 'value', 'CLEAN 자동화 가능 비중', '%', 'ASSUMPTION', 0.60, '식기 이동 · 식세기 적재/인출 · 수납만. 행주 · 싱크 세척 제외')
inp('fx', 'value', '환율 (Benchmark 환산용)', '원/USD', 'ASSUMPTION', 1400, '부품 Benchmark 환산 전용')

# --- prices (VAT 별도, 고객가)
inp('p_rr', 'price', 'Interface · Integration — Remodeling (Robot Home · Rail · 식세기 Interface · Storage Dock)', '만원/세대', 'ASSUMPTION',
    {'C': 400, 'B': 450, 'U': 450}, '주방 공사비 위 증분. 시스템에어컨 유상옵션(500~1,000만원) 대비 하단')
inp('p_rr_new', 'price', 'Interface Option — New-build (설계 반영, MH 공급가)', '만원/세대', 'ASSUMPTION', {'C': 200, 'B': 220, 'U': 220},
    '건설사 · 가구사 마진 별도. 분양 고객가 약 300만원 가정')
inp('p_rt_if', 'price', 'Interface Kit — Retrofit (Compact Mount · Dock · Vision Reference · Drop Zone)', '만원/세대', 'ASSUMPTION', 150,
    '기존 주방 유지. 최소 시공')
inp('p_robot', 'price', 'Robot System ASP (Arm · Adaptive Hand · Vision · Safety · Controller)', '만원/대', 'ASSUMPTION',
    {'C': 1290, 'B': 1490, 'U': 1490}, 'Upside는 가격 인상 없음. WTP 검증 대상 1순위')
inp('p_comm', 'price', 'Installation · Calibration · Safety Check (Remodeling · New-build)', '만원/대', 'ASSUMPTION', 80, '')
inp('p_comm_rt', 'price', 'Installation · Calibration (Retrofit, 현장 Calibration 비중 큼)', '만원/대', 'ASSUMPTION', 120, '')
inp('p_rent', 'price', 'Robot Rental 월 요금 (Care Basic · Grip Kit 포함, 60개월)', '만원/월', 'ASSUMPTION', {'C': 29, 'B': 33, 'U': 33},
    '원가 Build-up (감가 · 금융 · Care · Grip · Reserve) + 마진')
inp('rent_months', 'price', 'Rental 계약기간', '개월', 'ASSUMPTION', 60, '')
inp('p_care', 'price', 'Care Basic 연 요금 (구매 고객)', '만원/년', 'ASSUMPTION', {'C': 42, 'B': 48, 'U': 48},
    '정기 안전점검 · Calibration · 원격진단 · SW Update · A/S 공임')
inp('p_care_plus', 'price', 'Care Plus 연 요금 (Kit 정기교체 포함)', '만원/년', 'ASSUMPTION', 72, '옵션 상품. 재무 Base에는 미반영')
inp('p_grip', 'price', 'Grip Kit (Finger Pad · Food-contact Tip · Suction Seal)', '만원/Kit', 'ASSUMPTION', 4.5, '분기 교체 가정')
inp('n_grip', 'price', 'Grip Kit 교체 횟수', '회/년', 'ASSUMPTION', 4, 'Pad 마모율 · 교체주기 검증 대상 (KPI: Pad 수명)')
inp('p_clean', 'price', 'Cleaning Kit (Brush · Wiper · Cleaning Pad)', '만원/Kit', 'ASSUMPTION', 2.5, '')
inp('n_clean', 'price', 'Cleaning Kit 교체 횟수', '회/년', 'ASSUMPTION', 4, '')
inp('p_protect', 'price', 'Protection Kit (Sensor Cover · Sleeve · Seal)', '만원/Kit', 'ASSUMPTION', 4.0, '')
inp('n_protect', 'price', 'Protection Kit 교체 횟수', '회/년', 'ASSUMPTION', 2, '')
inp('cons_attach', 'price', 'Consumables 구매율', '%', 'ASSUMPTION', {'C': 0.55, 'B': 0.70, 'U': 0.70}, '')
inp('care_attach', 'price', 'Care 가입률 (구매 고객)', '%', 'ASSUMPTION', {'C': 0.55, 'B': 0.70, 'U': 0.70}, '')
inp('p_sw', 'price', 'ASSIST Skill Pack (설치 다음 해)', '만원', 'ASSUMPTION', 60, 'ASSIST 기능 (재료 이동 · 투입 보조 등) 출시 전제')
inp('sw_attach', 'price', 'ASSIST Skill 구매율', '%', 'ASSUMPTION', {'C': 0.10, 'B': 0.20, 'U': 0.20}, '')
inp('p_tool', 'price', 'Tool · End-effector 추가 (설치 2년 후)', '만원', 'ASSUMPTION', 80, 'FUTURE CONCEPT 제품')
inp('tool_attach', 'price', 'Tool 구매율', '%', 'ASSUMPTION', {'C': 0.15, 'B': 0.25, 'U': 0.25}, '')
inp('wholesale', 'price', 'Rental Partner 공급가율 (Robot ASP 대비)', '%', 'ASSUMPTION', 0.88, 'Y4부터 Rental Partner가 자산 보유')
inp('partner_fee', 'price', 'Rental Partner → MH Care · Grip 서비스료', '만원/월', 'ASSUMPTION', 6.0, '')
inp('realization', 'price', '가격 실현율 (Y2 Pilot 할인)', '%', 'ASSUMPTION',
    {'C': [1, 0.3, 1, 1, 1], 'B': [1, 0.5, 1, 1, 1], 'U': [1, 0.6, 1, 1, 1]}, 'Pilot은 할인 유료')

# --- costs
inp('kit_std_cost', 'cost', 'Interface Kit 원가 — Remodeling (표준부품 100% 기준)', '만원/세대', 'ASSUMPTION', 200,
    'Robot Home (Dock) · Rail Interface · 식세기 상향 하우징 · 전원/통신 · Storage Dock')
inp('custom_factor', 'cost', 'Custom 부품 원가 배수', 'x', 'ASSUMPTION', 1.6, '')
inp('design_cost', 'cost', 'Site 설계 · 조정 원가 (100% Custom 시)', '만원/세대', 'ASSUMPTION', 100, '')
inp('smr', 'cost', 'Interface 표준부품 사용률', '%', 'TARGET',
    {'C': [0.40, 0.45, 0.55, 0.62, 0.65], 'B': [0.40, 0.50, 0.65, 0.75, 0.80], 'U': [0.40, 0.55, 0.70, 0.80, 0.85]},
    'M24 65% 이상 목표 (M18 60% 미만이면 Interface 설계 재검토)')
inp('kit_new_cost', 'cost', 'Interface Option 원가 — New-build (공장 생산)', '만원/세대', 'ASSUMPTION', {'C': 145, 'B': 130, 'U': 120}, '')
inp('rt_kit_cost', 'cost', 'Interface Kit 원가 — Retrofit', '만원/세대', 'ASSUMPTION', 70, 'Compact Mount · Dock · Vision Reference')
inp('bom', 'cost', 'Robot System BOM (Adaptive Hand 포함)', '만원/대', 'ASSUMPTION',
    {'C': [1680, 1580, 1330, 1210, 1100], 'B': [1680, 1520, 1180, 1030, 915], 'U': [1680, 1460, 1100, 950, 820]},
    'BOM 구성 Benchmark 기반 (부록). 수량 · 국산화 · 자체 Hand 원가 하락 가정')
inp('comm_cost', 'cost', 'Installation · Calibration 원가 — Remodeling · New-build (MH 인력)', '만원/대', 'ASSUMPTION',
    {'C': [120, 100, 75, 62, 55], 'B': [120, 90, 60, 45, 38], 'U': [120, 85, 52, 38, 30]}, 'Calibration 시간 KPI와 연동')
inp('comm_cost_rt', 'cost', 'Installation · Calibration 원가 — Retrofit (MH 인력)', '만원/대', 'ASSUMPTION',
    {'C': [160, 140, 110, 95, 85], 'B': [160, 130, 95, 75, 62], 'U': [160, 120, 85, 65, 52]}, '현장 Calibration 비중 큼')
inp('logistics', 'cost', '물류 (세대당)', '만원/세대', 'ASSUMPTION', 25, '')
inp('warranty', 'cost', 'Warranty Reserve (Robot 매출 대비)', '%', 'ASSUMPTION', {'C': 0.05, 'B': 0.04, 'U': 0.035}, '1년 무상 A/S')
inp('visits', 'cost', '정기 방문 횟수', '회/년', 'ASSUMPTION',
    {'C': [2, 2, 2, 2, 2], 'B': [2, 2, 2, 1.5, 1.5], 'U': [2, 2, 1.5, 1.2, 1.0]}, '원격진단 고도화로 감소')
inp('visit_cost', 'cost', '방문 1회 원가 (인건비 · 이동)', '만원/회', 'ASSUMPTION',
    {'C': [15, 14, 12.5, 11, 10], 'B': [15, 13, 11, 9, 8], 'U': [15, 12, 10, 8, 7]},
    '참고: 제조사 출장비 2.8만원 (소비자 부과분, 2026)과 별개인 실제 원가. Route Density로 하락')
inp('corrective', 'cost', '고장 방문 (Failure Rate)', '회/대·년', 'ASSUMPTION', {'C': 0.9, 'B': 0.6, 'U': 0.5}, '')
inp('corr_cost', 'cost', '고장 방문 1회 원가 (소부품 포함)', '만원/회', 'ASSUMPTION', 18, '')
inp('cloud', 'cost', 'Cloud · Software 운영비', '만원/대·년', 'ASSUMPTION', 4, '')
inp('cons_cogs', 'cost', 'Consumables 원가율 (물류 포함)', '%', 'ASSUMPTION', {'C': 0.40, 'B': 0.35, 'U': 0.32}, '')
inp('sw_cogs', 'cost', 'Skill 원가율', '%', 'ASSUMPTION', 0.10, '')
inp('tool_cogs', 'cost', 'Tool 원가율', '%', 'ASSUMPTION', 0.45, '')
inp('partner_margin', 'cost', 'Kitchen · Interior · 설치 Partner 수수료 (Partner 경유 판매)', '%', 'ASSUMPTION',
    {'C': 0.12, 'B': 0.10, 'U': 0.09}, '')
inp('cac', 'cost', '직접판매 획득비용 (상담 · 설계 · Demo)', '만원/세대', 'ASSUMPTION', {'C': 180, 'B': 150, 'U': 140}, '')
inp('bd_new', 'cost', '신축 Project 수주비용 (Spec · 견본주택)', '만원/Project', 'ASSUMPTION', 2000, '')
inp('residual', 'cost', 'Rental 자산 잔존가치 (60개월 후)', '%', 'ASSUMPTION', 0.15, 'Refurbish 재배치')
inp('fin_rate', 'cost', 'Rental 자산 금융비용', '%/년', 'ASSUMPTION', 0.08, '캐피탈 조달금리 + Spread 가정')
inp('payback_hurdle', 'cost', 'Rental Partner 요구 Payback', '개월', 'ASSUMPTION', 36, '렌탈 · 캐피탈사 협의로 검증')

# --- volumes
inp('rd', 'volume', 'Remodeling — MH 직접 판매 (시공은 파트너)', '세대', 'TARGET',
    {'C': [0, 3, 20, 35, 40], 'B': [0, 3, 30, 50, 60], 'U': [0, 3, 35, 60, 70]}, 'Y2 = 가정 실증 3세대 (유료 목표, 할인)')
inp('rp', 'volume', 'Remodeling — 주방 · 인테리어 Partner 경유', '세대', 'TARGET',
    {'C': [0, 0, 10, 60, 150], 'B': [0, 0, 20, 130, 340], 'U': [0, 0, 30, 220, 600]}, 'Kitchen 가구 · 인테리어 Partner')
inp('rt', 'volume', 'Existing Kitchen Retrofit (호환 주방, Partner 설치)', '세대', 'TARGET',
    {'C': [0, 0, 0, 10, 40], 'B': [0, 0, 0, 20, 80], 'U': [0, 0, 0, 30, 120]}, 'Phase 2. Y4 시작')
inp('attach', 'volume', 'Robot Attach Rate (Remodeling, 설치 시점)', '%', 'ASSUMPTION',
    {'C': [1, 1, 0.75, 0.75, 0.75], 'B': [1, 1, 0.85, 0.85, 0.85], 'U': [1, 1, 0.85, 0.85, 0.85]}, '나머지는 Interface 선설치 (Robot 후설치)')
inp('later_attach', 'volume', 'Interface 선설치 세대의 연간 Robot 후설치', '%/년', 'ASSUMPTION', {'C': 0.05, 'B': 0.10, 'U': 0.12}, '')
inp('rental_share', 'volume', 'Rental 선택 비중', '%', 'ASSUMPTION',
    {'C': [0, 0.3, 0.3, 0.35, 0.35], 'B': [0, 0.3, 0.3, 0.4, 0.4], 'U': [0, 0.3, 0.3, 0.45, 0.45]}, '')
inp('partner_rental', 'volume', 'Rental 자산 보유 주체 (0 = MH Pilot, 1 = Rental Partner)', 'flag', 'ASSUMPTION', [0, 0, 0, 1, 1], '')
inp('projects', 'volume', '신축 Interface Option 계약 Project', '개', 'TARGET',
    {'C': [0, 0, 0, 1, 2], 'B': [0, 0, 1, 2, 3], 'U': [0, 0, 2, 3, 4]}, '계약 2년 후 입주 · 설치')
inp('hh_project', 'volume', 'Project당 세대수', '세대', 'ASSUMPTION', 800, '')
inp('option_rate', 'volume', '신축 Interface Option 선택률', '%', 'ASSUMPTION', {'C': 0.06, 'B': 0.10, 'U': 0.12}, '')
inp('new_attach', 'volume', '신축 입주 시 Robot Attach', '%', 'ASSUMPTION', {'C': 0.15, 'B': 0.25, 'U': 0.30}, '')

# --- opex (same plan in all scenarios). Y1~Y2 = 24개월 Bottom-up 예산 (BUD['base']), Y3~Y5 = Series A 이후 가정
_b = BUD['base']
_cl = {l['key']: l['y'] for l in _b['lines']}
inp('fte', 'opex', '평균 인원 (FTE)', '명', 'ASSUMPTION', [_b['fte'][0], _b['fte'][1], 20, 32, 42],
    'Y1~Y2 = 팀 계획 (Budget_24M, Founder 2 + 신규 채용) · Y3부터 Series A 전제')
inp('loaded', 'opex', '인당 연 인건비 (4대보험 · 퇴직급여 포함, 평균)', '만원/년', 'ASSUMPTION',
    [_b['people'][0] / _b['fte'][0], _b['people'][1] / _b['fte'][1], 8500, 8500, 8500],
    'Y1~Y2 = 팀 계획 가중평균 · Y3~ 평균 연봉 약 7,100만원 × 1.2')
inp('robot_hw', 'opex', 'Robot Hardware (R&D 로봇 셀)', '만원', 'ASSUMPTION', _cl['robot_hw'] + [12000, 14000, 16000], '')
inp('hand_proto', 'opex', 'Hand Prototype (비교군 · 자체 Hand v1~v3)', '만원', 'ASSUMPTION', _cl['hand_proto'] + [10000, 12000, 14000], '')
inp('mockup', 'opex', 'Kitchen Mock-up (실물 크기 3종)', '만원', 'ASSUMPTION', _cl['mockup'] + [8000, 9000, 10000], '')
inp('swdata', 'opex', 'Software · Data (GPU · Cloud · Annotation)', '만원', 'ASSUMPTION', _cl['swdata'] + [10000, 15000, 20000], '')
inp('pilot', 'opex', 'Pilot 운영 (실증 하드웨어 제외)', '만원', 'ASSUMPTION', _cl['pilot'] + [5000, 5000, 5000], '')
inp('custval', 'opex', 'Customer Validation · Partner · Marketing', '만원', 'ASSUMPTION', _cl['custval'] + [30000, 50000, 70000], '')
inp('cert', 'opex', 'Safety · Certification', '만원', 'ASSUMPTION', _cl['cert'] + [15000, 6000, 5000], 'Y3 본인증')
inp('ip', 'opex', 'IP (선행기술조사 · 출원)', '만원', 'ASSUMPTION', _cl['ip'] + [5000, 4000, 5000], '')
inp('space', 'opex', 'Space (실험실 · 목업 공간)', '만원', 'ASSUMPTION', _cl['space'] + [10000, 12000, 15000], '')
inp('ga', 'opex', 'Operating · G&A (법무 · 회계 · 보험 · 사무)', '만원', 'ASSUMPTION', _cl['ga'] + [30000, 40000, 50000], '')
inp('contingency', 'opex', '예비비 (인건비 외 지출의 10%, Y1~Y2)', '만원', 'DERIVED',
    [_b['contingency'][0], _b['contingency'][1], 0, 0, 0], '24개월 계획의 하드웨어 · 일정 Risk 대비')
inp('rnd_allow', 'opex', '연구수당 (TIPS 과제 현금 인건비 × 5%)', '만원', 'DERIVED',
    [_b['allow'][0], _b['allow'][1], 0, 0, 0], 'TIPS 선정 시')
OTHER_KEYS = ('robot_hw', 'hand_proto', 'mockup', 'swdata', 'pilot', 'custval', 'cert', 'ip', 'space', 'ga',
              'contingency', 'rnd_allow')

# --- funding. 규정 값 = 2026 TIPS 공고 (sources.json), 선정은 미확정
inp('tips', 'funding', 'TIPS R&D 정부지원금 (일반 트랙 최대)', '만원', 'FACT', 80000,
    '중소벤처기업부 공고 제2026-40호 (2026.1.26) 팁스 창업기업 지원계획. 선정 미확정')
inp('tips_months', 'funding', 'TIPS R&D 기간 (최대)', '개월', 'FACT', 24, '공고 제2026-40호')
inp('tips_gov_ratio', 'funding', '정부지원연구개발비 비율 상한 (총 연구개발비 대비)', '%', 'FACT', 0.75,
    '공고 제2026-40호 (사본 · 운용사 정리 기준: 정부 75% 이내, 기관부담 25% 이상)')
inp('tips_cash_ratio', 'funding', '기관부담연구개발비 중 현금 최소 비율', '%', 'FACT', 0.10, '공고 제2026-40호 (사본 · 운용사 정리 기준)')
inp('op_invest_min', 'funding', 'TIPS 운영사 선투자 요건 (수도권)', '만원', 'FACT', 20000, '2026: 수도권 2억원 이상 · 비수도권 1억원 이상')
inp('biz_link', 'funding', '비R&D 연계 (창업사업화 · 해외마케팅) 각 최대 (선정 뒤 별도 신청, 기본안 미반영)', '만원', 'FACT', 15000,
    '공고 제2026-40호: 각 10개월 최대 1.5억원, 합산 3억원, 정부 70% 이내')

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

def cons_lists(a):
    cons_y = a['p_grip'] * a['n_grip'] + a['p_clean'] * a['n_clean'] + a['p_protect'] * a['n_protect']
    cons_y_rent = a['p_clean'] * a['n_clean'] + a['p_protect'] * a['n_protect']
    return cons_y, cons_y_rent, a['p_grip'] * a['n_grip']

def care_cost(a, t):
    return yr(a['visits'], t) * yr(a['visit_cost'], t) + a['corrective'] * a['corr_cost'] + a['cloud']

def kit_cost(a, t):
    smr = yr(a['smr'], t)
    return a['kit_std_cost'] * (smr + a['custom_factor'] * (1 - smr)) + a['design_cost'] * (1 - smr)

# ---------------------------------------------------------------- 5-year engine
def run(s, ov=None):
    a = V(s, ov)
    L = {k: [0.0] * N for k in (
        'rd', 'rp', 'rt', 'ni', 'kitchens', 'pl_remodel', 'later', 'pl_new', 'pl', 'rpl', 'pp', 'drpl', 'prpl', 'pool',
        'pb_end', 'pb_avg', 'dr_end', 'dr_avg', 'pr_end', 'pr_avg', 'base_end',
        'rev_kitchen', 'rev_comm', 'rev_robot', 'rev_rental', 'rev_care', 'rev_cons', 'rev_upg', 'rev',
        'c_kitchen', 'c_log', 'c_robot', 'c_comm', 'c_warranty', 'c_dep', 'c_care', 'c_cons', 'c_upg', 'cogs', 'gp',
        'ch_partner', 'ch_cac', 'ch_bd', 'contrib', 'op_people', 'op_other', 'opex', 'op', 'capex', 'cash', 'cum_cash',
        'backlog', 'kit_unit_cost', 'care_unit_cost')}
    cons_y, cons_y_rent, grip_y = cons_lists(a)
    cum_capex_prev = 0.0
    for t in range(N):
        real = yr(a['realization'], t); att = yr(a['attach'], t)
        rd, rp, rt = yr(a['rd'], t), yr(a['rp'], t), yr(a['rt'], t)
        ni = (a['projects'][t - 2] * a['hh_project'] * a['option_rate']) if t >= 2 else 0.0
        pool_prev = L['pool'][t - 1] if t else 0.0
        later = pool_prev * a['later_attach']
        pl_remodel = (rd + rp) * att
        pl_new = ni * a['new_attach']
        pl = pl_remodel + pl_new + later + rt
        rs = yr(a['rental_share'], t); pf = yr(a['partner_rental'], t)
        rpl = pl * rs; pp = pl - rpl; drpl = rpl * (1 - pf); prpl = rpl * pf
        pool = pool_prev + (rd + rp) * (1 - att) + ni * (1 - a['new_attach']) - later
        g = lambda k: L[k][t - 1] if t else 0.0
        pb_end = g('pb_end') + pp; pb_avg = g('pb_end') + pp / 2
        dr_end = g('dr_end') + drpl; dr_avg = g('dr_end') + drpl / 2
        pr_end = g('pr_end') + prpl; pr_avg = g('pr_end') + prpl / 2
        # revenue — INSTALL (Interface · Installation · Robot) / OPERATE (Rental · Care · Consumables) / EXPAND (Skill · Tool)
        rev_kitchen = (rd + rp) * a['p_rr'] * real + ni * a['p_rr_new'] + rt * a['p_rt_if'] * real
        rev_comm = (pl - rt) * a['p_comm'] * real + rt * a['p_comm_rt'] * real
        rev_robot = pp * a['p_robot'] * real + prpl * a['p_robot'] * a['wholesale']
        rev_rental = dr_avg * a['p_rent'] * 12
        rev_care = pb_avg * a['care_attach'] * a['p_care'] + pr_avg * a['partner_fee'] * 12
        rev_cons = pb_avg * a['cons_attach'] * cons_y + (dr_avg + pr_avg) * a['cons_attach'] * cons_y_rent
        pl1 = L['pl'][t - 1] if t >= 1 else 0.0; pl2 = L['pl'][t - 2] if t >= 2 else 0.0
        rev_upg = pl1 * a['sw_attach'] * a['p_sw'] + pl2 * a['tool_attach'] * a['p_tool']
        rev = rev_kitchen + rev_comm + rev_robot + rev_rental + rev_care + rev_cons + rev_upg
        # cogs
        kit_unit = kit_cost(a, t)
        bom = yr(a['bom'], t)
        c_kitchen = (rd + rp) * kit_unit + ni * a['kit_new_cost'] + rt * a['rt_kit_cost']
        c_log = (rd + rp + ni + rt) * a['logistics']
        c_robot = (pp + prpl) * bom
        c_comm = (pl - rt) * yr(a['comm_cost'], t) + rt * yr(a['comm_cost_rt'], t)
        c_warranty = a['warranty'] * rev_robot
        capex = drpl * bom
        c_dep = cum_capex_prev * (1 - a['residual']) / 5 + capex * (1 - a['residual']) / 5 * 0.5
        care_unit = care_cost(a, t)
        c_care = (pb_avg * a['care_attach'] + dr_avg + pr_avg) * care_unit
        c_cons = rev_cons * a['cons_cogs'] + (dr_avg + pr_avg) * grip_y * a['cons_cogs']
        c_upg = pl1 * a['sw_attach'] * a['p_sw'] * a['sw_cogs'] + pl2 * a['tool_attach'] * a['p_tool'] * a['tool_cogs']
        cogs = c_kitchen + c_log + c_robot + c_comm + c_warranty + c_dep + c_care + c_cons + c_upg
        gp = rev - cogs
        ch_partner = a['partner_margin'] * (rp * (a['p_rr'] * real + att * (a['p_robot'] + a['p_comm']) * real)
                                            + rt * (a['p_rt_if'] + a['p_robot'] + a['p_comm_rt']) * real)
        ch_cac = rd * a['cac']
        ch_bd = a['projects'][t] * a['bd_new']
        contrib = gp - ch_partner - ch_cac - ch_bd
        op_people = yr(a['fte'], t) * yr(a['loaded'], t)
        op_other = sum(yr(a[k], t) for k in OTHER_KEYS)
        opex = op_people + op_other
        op = contrib - opex
        cash = op + c_dep - capex
        backlog = (a['projects'][t] + (a['projects'][t - 1] if t >= 1 else 0)) * a['hh_project'] * a['option_rate']
        for k, v in dict(rd=rd, rp=rp, rt=rt, ni=ni, kitchens=rd + rp + ni + rt, pl_remodel=pl_remodel, later=later,
                         pl_new=pl_new, pl=pl, rpl=rpl, pp=pp, drpl=drpl, prpl=prpl, pool=pool, pb_end=pb_end,
                         pb_avg=pb_avg, dr_end=dr_end, dr_avg=dr_avg, pr_end=pr_end, pr_avg=pr_avg,
                         base_end=pb_end + dr_end + pr_end,
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
    # layer mix: INSTALL / OPERATE / EXPAND
    L['install'] = [L['rev_kitchen'][t] + L['rev_comm'][t] + L['rev_robot'][t] for t in range(N)]
    L['build'] = [L['rev_kitchen'][t] + L['rev_comm'][t] for t in range(N)]
    L['recurring'] = [L['rev_rental'][t] + L['rev_care'][t] + L['rev_cons'][t] for t in range(N)]
    L['expand'] = list(L['rev_upg'])
    L['gm'] = [L['gp'][t] / L['rev'][t] if L['rev'][t] else 0 for t in range(N)]
    L['robot_recurring_share'] = [(L['rev_robot'][t] + L['recurring'][t] + L['rev_upg'][t]) / L['rev'][t] if L['rev'][t] else 0
                                  for t in range(N)]
    L['oe_share'] = [(L['recurring'][t] + L['rev_upg'][t]) / L['rev'][t] if L['rev'][t] else 0 for t in range(N)]
    L['min_cum_cash'] = min(L['cum_cash'])
    return L

# ---------------------------------------------------------------- household / unit economics (Base)
CHANNELS = {'remodel': 'Remodeling', 'retrofit': 'Existing Retrofit', 'newbuild': 'New-build'}

def household(s='B', t=2, channel='direct', mode='purchase', ov=None, install='remodel'):
    """One representative household, 5 years, expected values, cost level of year index t.
    install: remodel | retrofit | newbuild.  channel: direct | partner (remodel); retrofit = partner; newbuild = B2B2C."""
    a = V(s, ov)
    bom = yr(a['bom'], t)
    care_unit = care_cost(a, t)
    cons_y, cons_y_rent, grip_y = cons_lists(a)
    R = {}; C = {}
    if install == 'remodel':
        R['kitchen'] = a['p_rr']; R['comm'] = a['p_comm']
        C['kitchen'] = kit_cost(a, t); C['comm'] = yr(a['comm_cost'], t)
    elif install == 'retrofit':
        R['kitchen'] = a['p_rt_if']; R['comm'] = a['p_comm_rt']
        C['kitchen'] = a['rt_kit_cost']; C['comm'] = yr(a['comm_cost_rt'], t)
    else:
        R['kitchen'] = a['p_rr_new']; R['comm'] = a['p_comm']
        C['kitchen'] = a['kit_new_cost']; C['comm'] = yr(a['comm_cost'], t)
    C['log'] = a['logistics']
    R['sw'] = a['sw_attach'] * a['p_sw']; R['tool'] = a['tool_attach'] * a['p_tool']
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
    if install == 'newbuild':
        C['channel'] = a['bd_new'] / (a['hh_project'] * a['option_rate'])      # Project 수주비용 / Option 세대
    elif install == 'retrofit' or channel == 'partner':
        C['channel'] = a['partner_margin'] * (R['kitchen'] + a['p_robot'] + R['comm'])
    else:
        C['channel'] = a['cac']
    rev5 = sum(R.values()); cost5 = sum(C.values())
    gp5 = rev5 - (cost5 - C['channel'])
    install_rev = R['kitchen'] + R['comm'] + R.get('robot', 0)
    operate_rev = R.get('rental', 0) + R.get('care', 0) + R['cons']
    expand_rev = R['sw'] + R['tool']
    service_cost = C['care'] + C['cons'] + C['warranty']
    return dict(R=R, C=C, y0=y0, rev5=rev5, cost5=cost5, gp5=gp5, contrib5=rev5 - cost5,
                gm5=gp5 / rev5, cm5=(rev5 - cost5) / rev5, recurring5=operate_rev,
                layers=dict(install=install_rev, operate=operate_rev, expand=expand_rev),
                service_cost5=service_cost, kit_unit=C['kitchen'], care_unit=care_unit, bom=bom,
                install=install, channel=channel, mode=mode)

def rental_econ(s='B', t=2, ov=None):
    a = V(s, ov); bom = yr(a['bom'], t)
    care_unit = care_cost(a, t)
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
    a = V(s); cu = care_cost(a, t)
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

# ---------------------------------------------------------------- market (Bottom-up, 4 segments)
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
    # ② Retrofit: 재고 기준 호환 세대 pool × 연간 전환율
    retro_pool = apt * a['a_prem_stock'] * a['a_dw_premium'] * a['a_retro_fit']    # 천세대 (재고)
    retro_annual = retro_pool * a['a_retro_conv']                                   # 천세대/년
    pkg_retro = a['p_rt_if'] + a['p_robot'] + a['p_comm_rt']
    # ③ New-build
    new_prem = a['a_new_supply'] * a['a_premium_project']
    new_opt = new_prem * a['option_rate']
    pkg_new = a['p_rr_new'] + a['new_attach'] * (a['p_robot'] + a['p_comm'])
    tam = (prem + new_prem) * pkg_full / 10        # 억원  (천세대 × 만원 → 천만원 → /10 = 억원)
    sam_remodel = fit * pkg_remodel / 10
    sam_retro = retro_annual * pkg_retro / 10
    sam_new = new_opt * pkg_new / 10
    sam = sam_remodel + sam_retro + sam_new
    L = run(s)
    som = L['rev'][4] / 10000                       # 억원 (Y5 plan)
    som_hh = L['kitchens'][4]
    # ④ Recurring: Installed Base × ARPU (구매 고객 Care · Consumables 기대값, Rental 고객은 별도)
    cons_y, cons_y_rent, _ = cons_lists(a)
    arpu = a['care_attach'] * a['p_care'] + a['cons_attach'] * cons_y
    arpu_rent = a['p_rent'] * 12 + a['cons_attach'] * cons_y_rent
    return dict(apt=apt, tri1=tri1, tri2=tri2, rep=rep, prem=prem, fit=fit, pkg_remodel=pkg_remodel, pkg_full=pkg_full,
                retro_pool=retro_pool, retro_annual=retro_annual, pkg_retro=pkg_retro, sam_retro=sam_retro,
                new_prem=new_prem, new_opt=new_opt, pkg_new=pkg_new, tam=tam, sam_remodel=sam_remodel, sam_new=sam_new,
                sam=sam, som=som, som_hh=som_hh,
                som_share_hh=som_hh / ((fit + retro_annual + new_opt) * 1000),
                arpu=arpu, arpu_rent=arpu_rent, base_y5=L['base_end'][4], recurring_y5=L['recurring'][4] / 10000,
                recurring_per_1000=arpu * 1000 / 10000, kitchen_pool=rep + a['a_new_supply'])

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
        ('Interface 가격 ±20%', {'p_rr': lambda v: v * 0.8}, {'p_rr': lambda v: v * 1.2}),
        ('직접판매 획득비용 ±50%', {'cac': lambda v: v * 1.5}, {'cac': lambda v: v * 0.5}),
        ('Care 요금 ±20%', {'p_care': lambda v: v * 0.8}, {'p_care': lambda v: v * 1.2}),
        ('Care 방문 원가 ±30%', {'visit_cost': lambda v: [x * 1.3 for x in v]}, {'visit_cost': lambda v: [x * 0.7 for x in v]}),
        ('Interface 표준부품 사용률 -15pp/+15pp', {'smr': lambda v: [x - 0.15 for x in v]}, {'smr': lambda v: [x + 0.15 for x in v]}),
        ('설치 · Calibration 원가 ±50%', {'comm_cost': lambda v: [x * 1.5 for x in v]}, {'comm_cost': lambda v: [x * 0.5 for x in v]}),
        ('Failure Rate 1.2 ↔ 0.3회', {'corrective': 1.2, 'warranty': 0.06}, {'corrective': 0.3, 'warranty': 0.025}),
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
        ('Customer WTP (Robot ASP · Interface ±20%)', {'p_robot': lambda v: v * 0.8, 'p_rr': lambda v: v * 0.8},
         {'p_robot': lambda v: v * 1.2, 'p_rr': lambda v: v * 1.2}),
        ('Robot BOM ±20%', {'bom': lambda v: [x * 1.2 for x in v]}, {'bom': lambda v: [x * 0.8 for x in v]}),
        ('Partner 경유 Remodeling ±30%', {'rp': lambda v: [x * 0.7 for x in v]}, {'rp': lambda v: [x * 1.3 for x in v]}),
        ('Robot Attach Rate 65% ↔ 95%', {'attach': lambda v: [1, 1, .65, .65, .65]}, {'attach': lambda v: [1, 1, .95, .95, .95]}),
        ('Interface 표준부품 사용률 -15pp/+10pp', {'smr': lambda v: [x - 0.15 for x in v]}, {'smr': lambda v: [min(x + 0.10, 0.95) for x in v]}),
        ('설치 · Calibration 원가 ±50%', {'comm_cost': lambda v: [x * 1.5 for x in v], 'comm_cost_rt': lambda v: [x * 1.5 for x in v]},
         {'comm_cost': lambda v: [x * 0.5 for x in v], 'comm_cost_rt': lambda v: [x * 0.5 for x in v]}),
        ('Care 방문 원가 ±30%', {'visit_cost': lambda v: [x * 1.3 for x in v]}, {'visit_cost': lambda v: [x * 0.7 for x in v]}),
        ('Failure Rate 1.2 ↔ 0.3회', {'corrective': 1.2, 'warranty': 0.06}, {'corrective': 0.3, 'warranty': 0.025}),
        ('Retrofit 물량 0 ↔ 2배', {'rt': lambda v: [0] * 5}, {'rt': lambda v: [x * 2 for x in v]}),
        ('신축 Option 선택률 5% ↔ 15%', {'option_rate': 0.05}, {'option_rate': 0.15}),
        ('Rental 비중 60% ↔ 20%', {'rental_share': lambda v: [0, .3, .3, .6, .6]}, {'rental_share': lambda v: [0, .3, .3, .2, .2]}),
    ]
    out = []
    for name, lo, hi in items:
        out.append(dict(name=name, lo=run('B', lo)['contrib'][4] - base, hi=run('B', hi)['contrib'][4] - base))
    out.sort(key=lambda d: -(abs(d['lo']) + abs(d['hi'])))
    return dict(base=base, items=out)

# ---------------------------------------------------------------- 24개월 자금 계획: TIPS 과제 편성 · 재원 · Seed 범위
TIPS_CATS = ('인건비 (현금)', '인건비 (현물)', '연구재료비', '연구활동비', '연구수당', '간접비')

def tips_project(bud):
    """TIPS 과제 편성 (Base). 총 연구개발비 = 정부지원 최대 ÷ 정부 비율 상한. 간접비 = 연차 총액 − 직접비."""
    a = V('B')
    tm = bud['team']
    rows = []
    cash = [sum(m['cost'][t] * m['part'] for m in tm if m['kind'] == 'rnd') for t in (0, 1)]
    inkind = [sum(m['cost'][t] * m['part'] for m in tm if m['kind'] == 'founder') for t in (0, 1)]
    n_rnd = sum(1 for m in tm if m['kind'] == 'rnd')
    rows.append(('인건비 (현금)', f'R&D 인원 {n_rnd}명 × 참여율 40~60%', cash[0], cash[1], '현금'))
    rows.append(('인건비 (현물)', 'Founder 2인 × 참여율 50~60%', inkind[0], inkind[1], '현물'))
    for cat in ('연구재료비', '연구활동비'):
        ls = [l for l in bud['lines'] if l['tips_cat'] == cat]
        y = [sum(l['y'][t] * l['tips_share'][t] for l in ls) for t in (0, 1)]
        rows.append((cat, ' · '.join(l['cat'] for l in ls), y[0], y[1], '현금'))
    rows.append(('연구수당', '현금 인건비 × 5%', bud['allow'][0], bud['allow'][1], '현금'))
    direct = [sum(r[2 + t] for r in rows) for t in (0, 1)]
    total = a['tips'] / a['tips_gov_ratio']
    yt = [total * direct[t] / sum(direct) for t in (0, 1)]          # 간접비율 연차 동일
    rows.append(('간접비', '직접비 비례 (공간 · 관리비 일부 충당)', yt[0] - direct[0], yt[1] - direct[1], '현금'))
    inkind_t = sum(inkind)
    private = total - a['tips']; private_cash = private - inkind_t
    assert private_cash >= a['tips_cash_ratio'] * private - 1e-6, ('cash share of 기관부담', private_cash)
    assert all(r[2] >= 0 and r[3] >= 0 for r in rows), rows
    gov_y = [yt[t] * a['tips_gov_ratio'] for t in (0, 1)]
    cash_direct = sum(direct) - inkind_t
    return dict(rows=[dict(cat=r[0], item=r[1], y1=r[2], y2=r[3], kind=r[4], total=r[2] + r[3]) for r in rows],
                year_total=yt, total=total, gov=a['tips'], gov_y=gov_y, private=private, private_cash=private_cash,
                inkind=inkind_t, indirect=total - sum(direct), indirect_rate=(total - sum(direct)) / cash_direct,
                months=a['tips_months'])

def funding_plan():
    """24개월 사용처 (Spec 33 항목) · 재원 · Seed 범위 (Base / Lean / TIPS 미선정)."""
    a = V('B'); L = run('B')
    bud = BUD['base']; lean = BUD['lean']
    TP = tips_project(bud)
    # 실증 · 판매 관련 순비용 = 회사 지출 − Opex (실증 매출총손실 · 획득비용 · Rental 자산 − 감가)
    spend = [-L['cash'][0], -L['cash'][1]]
    pilot_net = [spend[t] - L['opex'][t] for t in (0, 1)]
    uses = []
    uses.append(dict(cat='인건비', item=f"팀 {len(bud['team'])}명 (Founder 2 + 신규 {len(bud['team']) - 2}) · 평균 {bud['fte'][0]:.1f} → {bud['fte'][1]:.1f} FTE",
                     y=list(bud['people']), tips=[TP['rows'][0]['y1'] + TP['rows'][1]['y1'], TP['rows'][0]['y2'] + TP['rows'][1]['y2']]))
    uses.append(dict(cat='연구수당', item='TIPS 과제 현금 인건비 × 5%', y=list(bud['allow']), tips=list(bud['allow'])))
    for l in bud['lines']:
        tp = [l['y'][t] * l['tips_share'][t] for t in (0, 1)]
        uses.append(dict(cat=l['cat'], item=l['item'], y=list(l['y']), tips=tp))
    uses.append(dict(cat='예비비', item='인건비 외 지출의 10%', y=list(bud['contingency']), tips=[0, 0]))
    uses.append(dict(cat='실증 순비용', item='실증 3세대 하드웨어 · 설치 원가 − 실증 매출 (50% 할인) · Rental 자산', y=pilot_net, tips=[0, 0]))
    # 간접비는 Space · Operating 사용처를 일부 충당
    ind = [TP['rows'][-1]['y1'], TP['rows'][-1]['y2']]
    for u in uses:
        if u['cat'] == 'Space':
            u['tips'] = [min(u['y'][t], ind[t]) for t in (0, 1)]
    rest = [ind[t] - next(u for u in uses if u['cat'] == 'Space')['tips'][t] for t in (0, 1)]
    for u in uses:
        if u['cat'] == 'Operating':
            u['tips'] = [min(u['y'][t], rest[t]) for t in (0, 1)]
    tot_y = [sum(u['y'][t] for u in uses) for t in (0, 1)]
    assert all(abs(tot_y[t] - spend[t]) < 1e-6 for t in (0, 1)), (tot_y, spend)
    tips_in_uses = sum(sum(u['tips']) for u in uses)
    assert abs(tips_in_uses - TP['total']) < 1e-6, (tips_in_uses, TP['total'])
    spend_total = sum(spend)
    buffer = BUFFER_MONTHS * spend[1] / 12
    seed_base = spend_total - a['tips'] + buffer
    # Lean: 팀 축소 · 목업/실증/인증 축소. 실증 순비용은 Base와 동일 가정
    lean_spend = [lean['opex'][t] + pilot_net[t] for t in (0, 1)]
    lean_buffer = BUFFER_MONTHS * lean_spend[1] / 12
    seed_lean = sum(lean_spend) - a['tips'] + lean_buffer
    # TIPS 미선정: 연구수당 없음, Lean 범위를 Seed 단독으로
    no_tips = [lean_spend[t] - lean['allow'][t] for t in (0, 1)]
    seed_no_tips = sum(no_tips) + BUFFER_MONTHS * no_tips[1] / 12
    # runway: 월 지출 연도 내 균등, 정부지원은 연차 초 지급 가정
    def runway(seed, sp, gov):
        avail = lambda m: seed + gov[0] + (gov[1] if m > 12 else 0)
        used = lambda m: sp[0] * min(m, 12) / 12 + (sp[1] * (m - 12) / 12 if m > 12 else 0)
        for k in range(1, 361):
            m = k / 10
            if used(m) > avail(m) + 1e-6:
                return m - 0.1
        return 36.0
    seed_round = lambda v: round(v / 10000)      # 억원 반올림
    return dict(uses=uses, spend=spend, spend_total=spend_total, pilot_net=pilot_net, tips=TP, buffer=buffer,
                buffer_months=BUFFER_MONTHS,
                seed_base=seed_base, seed_lean=seed_lean, seed_no_tips=seed_no_tips,
                seed_range=[seed_round(seed_lean), seed_round(seed_base)],
                lean_spend=lean_spend, lean_total=sum(lean_spend), no_tips_spend=no_tips,
                company_need=spend_total - a['tips'], tips_gov=a['tips'],
                runway_base=runway(seed_base, spend, TP['gov_y']),
                op_invest_min=a['op_invest_min'], biz_link=a['biz_link'],
                team=bud['team'], team_lean=lean['team'], fte=bud['fte'], fte_lean=lean['fte'],
                heads_m24=bud['heads_m24'], heads_m24_lean=lean['heads_m24'], people=bud['people'],
                lean_people=lean['people'], lean_other=lean['other'])

# ---------------------------------------------------------------- BOM breakdown (ASSUMPTION, 만원/대) — sums equal Base bom Y1 / Y3 / Y5
BOM_BREAKDOWN = [  # (item, pilot(Y1), Y3, Y5, basis)
    ('6축 Arm (가반 3~5kg, Controller 포함)', 950, 600, 450, 'FAIRINO FR5 $6,999 · xArm 6 $8,399 · UR3e $23k~33k 공개가 → OEM · 국산 Partner'),
    ('Adaptive Hand (손가락 2~3 · 교체형 Pad · 힘/미끄럼 감지 · Quick Changer)', 200, 120, 85, 'Robotiq 2F-85 약 $5,825 (2026 판매가) · Inspire RH56 $4,500~9,899 대비 자체 설계 목표가'),
    ('Rail · Carriage · Servo (Remodeling · New-build, 2.4~3.6m)', 180, 150, 120, 'Belt 구동 7축 Rail. Retrofit은 Compact Mount'),
    ('Vision (Depth Camera 2대 + Mount)', 110, 80, 60, 'Orbbec Gemini 335 $384~400 · RealSense D405 $514'),
    ('Compute (Edge GPU)', 100, 80, 70, 'Edge AI Module 가정'),
    ('Safety (Zone Sensor · Safety Controller)', 70, 60, 50, 'ToF/Radar Zone Sensor + Safety Relay 가정'),
    ('Robot Home (Dock) · Harness · Enclosure', 70, 50, 45, ''),
    ('조립 · 시험 (Pilot은 Opex 인건비 처리)', 0, 40, 35, ''),
]

def partner_irr(s='B', months=None):
    """Rental Partner IRR: buys robot at ASP × wholesale, receives (rent − MH service fee) monthly, residual at end."""
    a = V(s); m = months or a['rent_months']
    price = a['p_robot'] * a['wholesale']; inflow = a['p_rent'] - a['partner_fee']; resid = price * a['residual']
    def npv(r):
        return -price + sum(inflow / (1 + r) ** k for k in range(1, m + 1)) + resid / (1 + r) ** m
    lo, hi = 0.0, 0.1
    for _ in range(200):
        mid = (lo + hi) / 2
        if npv(mid) > 0: lo = mid
        else: hi = mid
    return dict(price=price, inflow=inflow, resid=resid, irr_m=lo, irr_y=(1 + lo) ** 12 - 1,
                payback=price / inflow, hurdle=a['payback_hurdle'])     # 단순 회수기간 (개월) vs 요구 Payback

# ---------------------------------------------------------------- 기술 KPI → 경제성 연결 (DERIVED targets)
def kpi_links():
    """R&D KPI가 Unit Economics 가정과 맞물리는 값 (KPI 목표의 근거)."""
    a = V('B')
    s1 = next(m for m in TEAM if m[0] == 'S1')
    hour = s1[3] / (12 * 20.9 * 8)                    # 설치 엔지니어 시간당 원가 (만원/h)
    inst_h = [yr(a['comm_cost'], t) / hour for t in range(N)]
    inst_h_rt = [yr(a['comm_cost_rt'], t) / hour for t in range(N)]
    visit_h = [yr(a['visit_cost'], t) / hour for t in range(N)]
    grasps_day = 20 * 2 * 1.5                         # 식기 20개 × (적재 + 인출) × 하루 1.5회
    pad_life = grasps_day * 365 / a['n_grip']
    return dict(hour=hour, inst_h=inst_h, inst_h_rt=inst_h_rt, visit_h=visit_h, grasps_day=grasps_day, pad_life=pad_life,
                care_unit=[care_cost(a, t) for t in range(N)], bom=list(a['bom']))

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
        hh[f'retrofit_purchase_{lab}'] = household('B', t, 'partner', 'purchase', install='retrofit')
        hh[f'newbuild_purchase_{lab}'] = household('B', t, 'b2b', 'purchase', install='newbuild')
    M['household'] = hh
    M['rental'] = {lab: rental_econ('B', t) for t, lab in ((2, 'Y3'), (4, 'Y5'))}
    M['rental_C'] = {lab: rental_econ('C', t) for t, lab in ((2, 'Y3'), (4, 'Y5'))}
    M['care'] = {lab: care_econ('B', t) for t, lab in ((2, 'Y3'), (4, 'Y5'))}
    M['cons'] = cons_econ('B')
    M['market'] = {s: market(s) for s in SC}
    M['value'] = value_anchor('B')
    M['sens_household'] = sens_household()
    M['sens_company'] = sens_company()
    M['funding'] = funding_plan()
    M['tips'] = M['funding']['tips']
    M['kpi_links'] = kpi_links()
    M['bom_breakdown'] = BOM_BREAKDOWN
    bb = V('B')['bom']
    for col, t in ((1, 0), (2, 2), (3, 4)):
        assert abs(sum(r[col] for r in BOM_BREAKDOWN) - bb[t]) < 1e-9, ('BOM breakdown', col)
    M['partner_irr'] = {s: partner_irr(s) for s in SC}
    # break-even installs (Y5 Base contribution per install vs Y5 opex)
    B = M['scenarios']['B']
    cpk = B['contrib'][4] / B['kitchens'][4]
    M['breakeven_kitchens'] = B['opex'][4] / cpk
    M['contrib_per_kitchen_y5'] = cpk
    # Series A 이후 (Y3~Y5) 누적 현금 소요 — 후속 라운드 규모 참고 (DERIVED)
    M['post_seed_burn'] = dict(y3=-B['cash'][2], y4=-B['cash'][3], y3_y4=-(B['cash'][2] + B['cash'][3]),
                               min_cum=B['min_cum_cash'])
    M['team_kind'] = TEAM_KIND
    # sanity checks
    for s in SC:
        L = M['scenarios'][s]
        for t in range(N):
            parts = sum(L[k][t] for k in ('rev_kitchen', 'rev_comm', 'rev_robot', 'rev_rental', 'rev_care', 'rev_cons', 'rev_upg'))
            assert abs(parts - L['rev'][t]) < 1e-6
            assert abs(L['pl'][t] - L['rpl'][t] - L['pp'][t]) < 1e-9
            assert L['pool'][t] >= -1e-9
    assert M['scenarios']['C']['rev'][4] < M['scenarios']['B']['rev'][4] < M['scenarios']['U']['rev'][4]
    F = M['funding']
    assert F['seed_lean'] < F['seed_base'] < F['seed_no_tips'] + 1e9
    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump(M, f, ensure_ascii=False, indent=1)
    return M

if __name__ == '__main__':
    M = main()
    for s in SC:
        L = M['scenarios'][s]
        print(SCN[s], 'rev(억)', [round(x / 10000, 1) for x in L['rev']], 'GP%', [round(x * 100) for x in L['gm']],
              'contrib(억)', [round(x / 10000, 1) for x in L['contrib']], 'OP(억)', [round(x / 10000, 1) for x in L['op']],
              'installs', [round(x) for x in L['kitchens']], 'robots', [round(x) for x in L['pl']],
              'base', round(L['base_end'][4]), 'cumcash(억)', round(L['min_cum_cash'] / 10000, 1),
              'OE share', [round(x * 100) for x in L['oe_share']])
    for k, h in M['household'].items():
        print(k, 'y0', round(h['y0']), 'rev5', round(h['rev5']), 'gp5', round(h['gp5']), 'contrib5', round(h['contrib5']),
              'cm', round(h['cm5'] * 100, 1), 'layers', {kk: round(v) for kk, v in h['layers'].items()})
    print('rental', {k: (round(v['contrib_m'], 2), round(v['payback'], 1), round(v['bom_max']), round(v['fee_at_20'], 1)) for k, v in M['rental'].items()})
    print('care', {k: (round(v['cost'], 1), round(v['margin'] * 100)) for k, v in M['care'].items()})
    print('market', {k: round(v, 1) if isinstance(v, float) else v for k, v in M['market']['B'].items()})
    print('sens hh', round(M['sens_household']['base']), [(d['name'], round(d['lo']), round(d['hi'])) for d in M['sens_household']['items']])
    print('sens co', round(M['sens_company']['base']), [(d['name'], round(d['lo']), round(d['hi'])) for d in M['sens_company']['items']])
    F = M['funding']; TP = F['tips']
    print('team fte', [round(x, 2) for x in F['fte']], 'people', [round(x) for x in F['people']], 'heads M24', F['heads_m24'],
          '| lean fte', [round(x, 2) for x in F['fte_lean']], 'lean people', [round(x) for x in F['lean_people']])
    for u in F['uses']:
        print('  use', u['cat'], [round(x) for x in u['y']], 'tips', [round(x) for x in u['tips']])
    print('spend', [round(x) for x in F['spend']], round(F['spend_total']), 'buffer', round(F['buffer']),
          'seed base', round(F['seed_base']), 'lean', round(F['seed_lean']), 'no tips', round(F['seed_no_tips']),
          'range(억)', F['seed_range'], 'runway', F['runway_base'])
    print('tips rows', [(r['cat'], round(r['y1']), round(r['y2']), r['kind']) for r in TP['rows']], 'total', round(TP['total']),
          'cash', round(TP['private_cash']), 'inkind', round(TP['inkind']), 'indirect', round(TP['indirect_rate'] * 100, 1))
    print('kpi links', {k: (v if not isinstance(v, list) else [round(x, 1) for x in v]) for k, v in M['kpi_links'].items()})
    print('post seed burn', {k: round(v) for k, v in M['post_seed_burn'].items()})
    print('breakeven installs', round(M['breakeven_kitchens']), 'cpk', round(M['contrib_per_kitchen_y5']))
    print('partner irr', {k: round(v['irr_y'] * 100, 1) for k, v in M['partner_irr'].items()})
