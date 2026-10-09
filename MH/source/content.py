# Shared qualitative content for the MH deck appendix and the docs (single source, Korean).
# Numbers come from model.json via M; text here never invents customers, partners, contracts or founder facts.
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
M = json.load(open(os.path.join(HERE, 'model.json'), encoding='utf-8'))
F = M['funding']; TP = F['tips']; KL = M['kpi_links']; MK = M['market']['B']
H3 = M['household']['purchase_direct_Y3']; H5 = M['household']['purchase_direct_Y5']
A = {d['key']: d['vals']['B'] for d in M['inputs']}

# ---------------------------------------------------------------- technical KPI (Spec 22)
# group, name, definition, benchmark (with source), M6, M12, M18, M24, basis of the target, tag
KPI = [
    ('Manipulation', 'Task Success Rate (CLEAN)', '식기 1개를 사람 개입 없이 집기 → 식세기 적재 (또는 꺼내기 → 수납)까지 끝낸 비율',
     'Voysey 2021 식세기 적재 58.7% (실험실 · one-shot) · Dobb-E 81% (단순 가사 · 10가구) · TidyBot 85% [S36~S38]',
     'Baseline 측정', '≥ 80% (목업)', '≥ 85% (주방 3종)', '≥ 90% (실거주 3세대)',
     '식사 1회 식기 20개 기준 사람 개입 ≤ 2건 = 90%. 공개 연구보다 높은 목표 = 환경 Interface 효과를 확인하는 지표', 'TARGET'),
    ('Manipulation', 'Object Coverage', '30종 한국 식기 · 도구 세트 중 Tool 교체 없이 파지 가능한 종류',
     '공개 Benchmark 없음 (자체 세트 정의)', '상용 Gripper Baseline', '≥ 24/30', '≥ 26/30', '≥ 27/30',
     'Buy vs Build 판정: 상용 Gripper 대비 +15%p 이상이면 자체 Hand 채택', 'TARGET'),
    ('Manipulation', 'Human Intervention Rate', '식세기 1회분 (식기 20개)당 사람 개입 횟수', '-', '측정', '≤ 4회', '≤ 3회', '≤ 2회',
     'Task Success Rate와 같은 기준의 사용자 체감 지표', 'TARGET'),
    ('Manipulation', 'Failure Recovery Rate', '감지된 실패 (미끄러짐 · 기울어짐 · 적재 실패) 중 자율 복구 비율', '공개 Benchmark 없음', '-', 'Baseline 측정',
     'M12 결과로 설정', 'M18 설정값 달성', 'M12 측정값으로 목표 설정', 'TARGET'),
    ('Manipulation', 'Cycle Time', '식기 1개 적재 평균 시간', '사람 약 3~5초/개 (참고, 측정 필요)', '측정', '측정', '≤ 40초/개', '≤ 30초/개',
     '식기 20개를 10분 안에 적재 → 식후 사람이 없는 시간에 끝남', 'TARGET'),
    ('Manipulation', 'Grip Stability', '파지 중 낙하 · 미끄러짐 발생률', '-', '측정', '≤ 1/200회', '≤ 1/500회', '≤ 1/1,000회',
     f"Pad 1세트 수명 (약 {KL['pad_life']:,.0f}회) 동안 낙하 ≤ 5회", 'TARGET'),
    ('Manipulation', 'Slip Detection', '낙하 전 미끄럼 감지율', 'GelSight 기반 실시간 감지 99% (일상 물체 10종 · 실험실) [S44]', '-', '≥ 90%', '≥ 93%', '≥ 95%',
     '연구 수준보다 낮게 시작 (젖은 표면 · 저가 센서 조건)', 'TARGET'),
    ('Manipulation', 'Hand Durability (Pad 수명)', 'Pad 교체 전 파지 횟수 (가속 시험)', '-', '-', '시험 설계', '가속 시험', f"≥ {KL['pad_life']:,.0f}회",
     f"Grip Kit 분기 교체 가정 × 하루 {KL['grasps_day']:.0f}회 파지 (식기 20개 × 적재 · 꺼내기 × 1.5회)", 'DERIVED'),
    ('Application', 'Calibration Time', '새 주방에서 현장 Calibration 완료 시간', '-', '-', '≤ 8시간 (목업)', '≤ 4시간 (주방 3종)', '≤ 4시간 (가정)',
     f"설치 · Calibration 원가 Y3 {A['comm_cost'][2]}만원 = 약 {KL['inst_h'][2]:.0f}인시 (2인 1일) 안에 설치까지 끝내야 함", 'DERIVED'),
    ('Application', 'Site Programming Time', '주방별 Custom 코드 · 티칭 시간', '-', '-', '측정', 'Custom 코드 0 · 티칭 ≤ 1시간', '동일',
     'Template Skill만 써야 반복 설치 가능', 'TARGET'),
    ('Application', 'Installation Time', 'Robot 설치 + Calibration + Safety Check (Interface 시공 제외)', '-', '-', '-', '측정',
     'Remodeling 2인 1일 · Retrofit 2인 2일 이내', f"설치 원가 가정과 연동 (Remodeling 약 {KL['inst_h'][2]:.0f}인시 · Retrofit 약 {KL['inst_h_rt'][2]:.0f}인시, Y3)", 'DERIVED'),
    ('Application', 'Kitchen Compatibility', '분석 평면 · 상담 주방 중 적용 가능 비율', '확보 평면 5종: 기본 배치 가능 1 · 불가 3 · 미검토 1 (DERIVED)', '평면 30개 분석', '-', '상담 주방 실측', '-',
     f"가정 Remodeling {A['a_fit_rate'] * 100:.0f}% · Retrofit {A['a_retro_fit'] * 100:.0f}%를 실측으로 대체", 'ASSUMPTION'),
    ('Application', 'Task Transferability', '타 주방 설치 후 성공률 하락 (같은 Skill)', '-', '-', '-', '≤ 10%p (주방 3종)', '≤ 10%p (가정)',
     'Platform 반복 적용의 핵심 증거', 'TARGET'),
    ('Business', 'Robot BOM', 'Robot System 1대 원가 (Adaptive Hand 포함)', '공개가 Benchmark (부록 B6)', f"{A['bom'][0]:,}만원 (시제품)", '-', '100대/년 견적',
     f"견적 ≤ {A['bom'][2]:,}만원 (Y3 가정)", 'Robot ASP 1,490만원에서 Hardware 마진 확보 (민감도 2순위)', 'ASSUMPTION'),
    ('Business', 'Installation Cost', '세대당 설치 · Calibration 실비', '-', '-', '-', '목업 기준', f"실측 ≤ {A['comm_cost'][1]}만원 (Y2 가정)", '실거주 3세대 실측', 'ASSUMPTION'),
    ('Business', 'Service Cost', '고장 방문 (A/S) 1회 원가 · 연 발생 횟수', '-', '-', '-', '-', f"실측 (가정 연 {A['corrective']['B'] if isinstance(A['corrective'], dict) else A['corrective']}회)",
     '고장 횟수 민감도 (연 1.2회 시 세대당 5년 −84만원)', 'ASSUMPTION'),
    ('Business', 'Care Cost', '정기 방문 · 원격진단 · Cloud 연 원가', '-', '-', '-', '-', f"실측 ≤ {KL['care_unit'][1]:.1f}만원/대·년",
     f"Care 요금 {A['p_care']}만원/년 대비 마진", 'ASSUMPTION'),
    ('Business', 'WTP', '시스템 1,490만원 이상 지불 의향 비율 (Premium 리모델링 상담 고객)', '-', '인터뷰 50명 (정성)', '-', 'n ≥ 300 조사 · 예약금 테스트', '-',
     '판정 기준 ≥ 30% (가설). 15% 미만이면 가격 · 구성 재설계', 'TARGET'),
    ('Business', 'Pilot Conversion', '실거주 3세대 실증 중 유료 전환', '-', '-', '-', '실증 착수', '≥ 2세대', '실증 50% 할인 → 정가 전환 의향', 'TARGET'),
    ('Business', 'Consumables Cost', 'Grip Kit 원가율 (물류 포함)', 'Robotiq Fingertip $175~195 (참고) [S16]', '-', '-', '견적', f"≤ {A['cons_cogs'] * 100:.0f}%", '소모품 마진 가정 검증', 'ASSUMPTION'),
]

# ---------------------------------------------------------------- Hand test plan (B1): item, content, tag
HAND_TEST = [
    ('시험 물체 (30종)', '접시 대 · 중 · 소 (도자기 · 멜라민) · 밥공기 · 국그릇 · 면기 · 컵 · 머그 · 유리잔 · 물병 · 수저 · 젓가락 · 냄비뚜껑 (유리 · 금속) · 집게 · 국자 · 뒤집개 · 보관용기 (유리 · Plastic) · 쟁반 · 도마 (소)', 'TARGET (세트 정의)'),
    ('조건', '건조 / 젖은 표면 · 세제 잔여 · 식기 겹침 · 식세기 랙 (하단 · 상단 · 수저통) · 수납 서랍 · 상부장', 'TARGET'),
    ('비교군 (Buy)', 'Robotiq 2F-85 (약 $5,825) · 저가 전동 Parallel Gripper · Suction Cup (식품용 실리콘) · Soft Finger (Fin-ray형)', 'FACT (가격)'),
    ('자체 Hand (Build)', 'v1 (M4): 2+1 손가락 부족구동 + 교체형 Pad · v2 (M10): Edge Lip · 미끄럼 감지 · v3 (M18): 내구 · 위생 · 원가', 'CONCEPT'),
    ('측정 지표', '종류별 성공률 · Tool 교체 횟수 · 파손 · 낙하 · 미끄럼 감지 · Cycle Time · Pad 마모 · 세척 후 성능 · 단가', 'TARGET'),
    ('판정 (M6)', 'Coverage +15%p 이상 또는 Tool 교체 횟수 50% 감소 → 자체 Hand 채택 · 아니면 상용 Gripper + 교체형 Pad (Buy)', 'TARGET'),
    ('식품 접촉 규격', '식품위생법 "기구" · 「기구 및 용기 · 포장의 기준 및 규격」 고무제 (실리콘) 재질 · 용출 · 해외: FDA 21 CFR 177.2600 · EU 1935/2004 (수출 시)', 'FACT [S48]'),
    ('연구 참고', 'GelSight 기반 실시간 미끄럼 감지 99% (일상 물체 10종 · 실험실) · 식세기 적재 연구 58.7% (트레이 25개)', 'FACT [S36 · S44]'),
]

# ---------------------------------------------------------------- safety · certification path (B5): item, content, tag, source
SAFETY = [
    ('협동 운전 기준', 'ISO 10218-1/-2:2025 (2025.2 발행): ISO/TS 15066 요구 통합 · 감속 기능 250mm/s 이하 · 손 · 손가락 준정적 접촉력 140N (부속서 M)', 'FACT', '[S28 · S39]'),
    ('가정용 로봇 안전', 'IEC 63682 (구 IEC 60335-2-123) Robots for household and similar use: 2026 CDV 단계 (발행 전)', 'FACT', '[S47]'),
    ('개인 서비스 로봇', 'ISO 13482 개정 FDIS (2025.7) · 국내 ISO 13482 인증 사례 (유진로봇 AMR)', 'FACT', '[S31 · S47]'),
    ('전기 · EMC', 'KC 전기용품 안전 · 전자파 적합성 (가정용) — 적용 범위 사전상담 필요', 'TBV', '-'),
    ('식품 접촉', '「기구 및 용기 · 포장의 기준 및 규격」 고무제 규격 (ASSIST · COOK 단계 필수)', 'FACT', '[S48]'),
    ('MH 안전 원칙', '사람 위로 운반 금지 · Zone 진입 시 감속 · 정지 · 저가반하중 Arm · 쿡탑 구역 진입 금지 · 고장 시 Robot Home 자동 복귀 · 로봇 없이 일반 주방 사용 가능', 'CONCEPT', '-'),
    ('일정', 'M4 위험성평가 · M9 인증기관 사전상담 · M12 안전 기능 시험 · M18 사전시험 (전기 · EMC) · Series A 이후 본인증', 'TARGET', '-'),
]

# ---------------------------------------------------------------- component benchmark (B6): name, USD (FACT), 만원 at FX (ASSUMPTION)
FX = 1400
def _mw(*usd):
    return ' / '.join('~'.join(f"{u * FX / 1e4:,.0f}" for u in (x if isinstance(x, tuple) else (x,))) for x in usd)
BENCH = [
    ('UR3e (3kg)', '$23k~33k', _mw((23000, 33000))), ('Doosan E0509 (5kg)', '약 $22k', _mw(22000)),
    ('UFACTORY xArm 6 (5kg)', '$8,399', _mw(8399)), ('FAIRINO FR5 (5kg)', '$6,999', _mw(6999)),
    ('Robotiq 2F-85 (2026 판매가)', '약 $5,825', _mw(5825)), ('Inspire RH56 계열 (Dexterous)', '$4,500~9,899', _mw((4500, 9899))),
    ('Robotiq Fingertip', '$175~195', _mw((175, 195))), ('Orbbec Gemini 335 / RealSense D405', '$384~400 / $514', _mw((384, 400), 514)),
]

# ---------------------------------------------------------------- housing statistics (C1): item, value, tag, source / formula
HOUSING = [
    ('총주택 (2025.11.1)', '2,018.1만호', 'FACT', '국가데이터처 2025 인구주택총조사 (2026.7.28) [S1]'),
    ('아파트 비중', '65.8%', 'FACT', '2025 인구주택총조사 [S1]'),
    ('아파트 수', f"약 {MK['apt'] / 10:,.0f}만호", 'DERIVED', '총주택 2,018.1만 × 65.8%'),
    ('준공 20년 이상 / 30년 이상 주택 비중', '56.0% / 30.6%', 'FACT', '2025 인구주택총조사 [S1]'),
    ('아파트 수 · 20년 이상 아파트 (2023)', '1,263만호 · 639만호 (50.7%)', 'FACT', '2023 주택총조사 인용 보도 [S2]'),
    ('주택 준공 · 인허가 · 착공 (2025)', '34.2만 · 38.0만 · 27.3만호', 'FACT', '국토부 2025.12 주택통계 [S3]'),
    ('아파트 입주 2025 / 2026 예정', '23만6,263 / 18만3,124가구', 'FACT', '부동산114 REPS [S5]'),
    ('주택 매매거래 (2025)', '72.6만호 (10년 평균 88.5만)', 'FACT', 'KB주택시장리뷰 (부동산원 자료) [S6]'),
    ('무급 가사노동 가치 (2024)', '582.4조원 · 가정관리 459.5조원 (78.9%) · 1인당 132분/일', 'FACT', '국가데이터처 가계생산 위성계정 (2026.4) [S40]'),
    ('연간 주방 교체 교차검증 ① / ②', f"{MK['tri1'] / 10:.1f}만 / {MK['tri2'] / 10:.1f}만", 'DERIVED', '20년+ 아파트 ÷ 22년 · 매매 × 70% × 40% + 10만 (ASSUMPTION)'),
    ('연간 주방 교체 (설정값)', '30만 세대/년', 'ASSUMPTION', '①·② 범위 → 견적 · Partner Data로 보정'),
]

# ---------------------------------------------------------------- remodeling · rental · care references (C2): item, value, tag, note
REFS = [
    ('국내 리모델링 시장 (건축물 전체)', '2025 37조원 → 2030 44조원 (전망)', 'FACT', '한국건설산업연구원 · 주택 주방 단독 아님 [S7]'),
    ('프리미엄 주방 동향', '수입 · 고가 맞춤 약 90% · 키친바흐 +17% · 밀레 연계 +173%', 'FACT', '한샘 발표 인용 보도 [S9]'),
    ('한샘 리하우스 매출', '2025 1Q 1,147억원 (−4.3%)', 'FACT', '분기 실적 [S10]'),
    ('신축 유상옵션 / 분양가', '평균 9.7% (분양가상한제 7개 단지)', 'FACT', '보도 · 옵션 선택 문화 [S11]'),
    ('코웨이 (렌탈 · 방문관리)', '2025 매출 4조9,636억 · 영업이익 8,787억 · 국내 계정 748만 (2026 1Q)', 'FACT', '실적 보도 [S12]'),
    ('LG 가전 구독 · Care', '2025 구독 매출 2조원+ · 케어매니저 약 4,000명 · LH 5,400세대 · 재건축 약 7,000세대 선택지', 'FACT', '실적 · 보도 [S41]'),
    ('가전 A/S 출장비 (소비자 부과)', '2.8만원 (삼성 · LG, 2026)', 'FACT', 'MH 방문 원가와 다름 [S13]'),
    ('식기세척기 보급률', '10%대 초반 (2019~2020 업계 추정, 전체 가구)', 'TBV', '최신 공식 통계 없음 → 조사 [S30]'),
    ('주방 단독 교체 가격: 일반 / Premium', '600~1,500만원 / 2,000~4,000만원', 'ASSUMPTION', '공식 자료 없음 → 견적 20건 (M6)'),
]

# ---------------------------------------------------------------- received floor plans (B2): plan, type, size (mm), kitchen form, 3D status, base layout fit
PLANS = [
    ('구축 2Bay A', '구축 · 계단실형 (코어 포함)', '12,390 × 11,670', 'ㄱ자 (싱크대 벽 3,255mm + 쿡탑 벽)', '완료 · 원도면 중첩 확인', '가능: 일자 3,150mm · 간섭 없음 (B4)'),
    ('구축 2Bay B', '구축 · 전면 발코니', '10,940 × 8,500', 'ㄱ자 (싱크대 벽 약 2.6m + 쿡탑 벽) · 거실 일체형', '완료', '불가 · 냉장고 위치 변경 시 약 3.3m'),
    ('신축 2Bay', '신축 · 탑상형', '15,120 × 10,730', 'ㄱ자 + 아일랜드', '미착수', '미검토'),
    ('신축 3Bay', '신축 · 판상형', '12,400 × 10,550', 'ㄷ자 (싱크대 벽 약 2.6m + 쿡탑 벽)', '완료', '불가 · Compact Mount 검토'),
    ('신축 4Bay', '신축 · 판상형', '14,700 × 9,780', 'ㄷ자 (싱크대 벽 약 2.8m + 쿡탑 벽)', '완료', '불가 · Compact Mount 검토'),
]

# ---------------------------------------------------------------- R&D work packages (Spec 21)
WP = [
    ('WP1', 'Adaptive Kitchen Robot Hand', 'M1~M24', '주방 식기 · 도구 30종을 Tool 교체 없이 하나의 손으로',
     ['상용 Gripper 비교군 (M1~M6) · Hand v1 (M4) · v2 (M10) · v3 (M18)', '교체형 Food-contact Module · Grip Force · Slip Detection', '내구 · 위생 시험 (세척 · 열 · 세제)'],
     'Hand v3 · 30종 파지 Data · 내구 시험 결과', 'Object Coverage · Grip Stability · Slip Detection · Pad 수명', 'Hand · 기구 리드 · Hand 센싱 · Manipulation 리드'),
    ('WP2', 'Kitchen Manipulation Skill', 'M3~M24', 'CLEAN Skill을 Template으로 만들어 주방마다 재사용',
     ['Pick · Place · Insert (식세기 랙) · Remove · Open/Close', 'Failure Detection · Recovery', 'Skill Template · 공개 범용 모델 (π0 계열) Fine-tune 검토'],
     'CLEAN Skill Library v1', 'Task Success · Intervention · Recovery · Cycle Time', 'Manipulation 리드 · Robot SW · Skill/Data'),
    ('WP3', 'Kitchen Perception / Calibration', 'M2~M24', '새 주방에서 4시간 내 같은 Skill 실행',
     ['식기 30종 인식 Dataset', 'Kitchen Mapping · Coordinate Calibration (Dock · 가전 기준점)', 'Appliance / Storage Position Mapping · Task Parameter'],
     'Calibration Tool · 현장 절차서', 'Calibration Time · Task Transferability', 'Perception 리드 · Skill/Data'),
    ('WP4', 'Minimal Environment Interface', 'M3~M22', '필요한 곳에만 표준 Interface',
     ['Robot Home (보관 · 펼침) · Tool Dock · 수납 Dock', '식세기 Interface (랙 · 문) · Vision 기준점', 'Retrofit Compact Mount · 설치 표준'],
     'Interface 표준 v1 · 설치 표준서', 'Installation Time · Compatibility · 표준부품 사용률', '임베디드 · 전기 · 안전 · Hand 리드 · 설치 엔지니어'),
    ('WP5', 'Human-Robot Safety', 'M4~M24', '사람 곁 주방에서 안전 기준 충족',
     ['Zone 감시 · 감속 · 정지 · 충돌 감지 · 비상정지 · Robot Home 자동 복귀', '위험성평가 · 표준 Gap (ISO 10218-2:2025 · IEC 63682 초안 · ISO 13482)', '전기안전 · EMC 사전시험'],
     'Safety Architecture · 사전시험 결과', '감속 250mm/s · 접촉력 기준 충족 · 사전시험 통과', '임베디드 · 전기 · 안전 · 시험 · 신뢰성'),
    ('WP6', 'Integrated CLEAN 실증', 'M9~M24', '목업 → 주방 3종 → 실거주 3세대로 끝까지 검증',
     ['1:1 목업 CLEAN (M9~M12)', '주방 3종 적용 시험 (M13~M18)', '실거주 3세대 실증 · 연속 운전 신뢰성 (M19~M24)'],
     '실증 보고서 · BOM · 설치 · Service 원가 실측', 'Task Success (가정 ≥ 90%) · Pilot Conversion', '시험 · 신뢰성 · 설치 엔지니어 · 사업개발'),
]

# ---------------------------------------------------------------- gates (24M)
GATES = [
    ('M6', 'Hand v1 vs 상용 Gripper (30종) · Robot Architecture 확정 · 평면 30개 분석 · 인터뷰 50명',
     'Coverage +15%p 또는 Tool 교체 횟수 50% 감소', '상용 Gripper + 교체형 Pad로 전환 (Buy) · WP1 예산 재배분'),
    ('M12', '목업 CLEAN 전 과정 · 식기 성공률 · 안전 기능 · 특허 출원 2건',
     '식기 성공률 ≥ 80% · Safety 기능 동작', '적재 단계로 범위 축소 · Interface 보강 후 재시험'),
    ('M18', '주방 3종 적용 시험 · Calibration 시간 · WTP n ≥ 300 · 예약금 테스트 · 인증 사전상담',
     '하락 ≤ 10%p · Calibration ≤ 4시간 · WTP ≥ 30% (1,490만원)', 'Retrofit 보류 · Remodeling 집중 / 가격 · 구성 재설계'),
    ('M24', '실거주 3세대 실증 · 유료 전환 · BOM · 설치 · Service 원가 실측 · Partner 조건 · 출원 5건',
     '가정 ≥ 90% · 유료 전환 ≥ 2세대 · 원가가 가정 범위 안', 'Bridge 또는 범위 축소 후 재검증 (Series A 연기)'),
]

# ---------------------------------------------------------------- IP families (Spec 23)
# area, family, business importance, differentiation, prior-art risk (refs), priority, timing
IP = [
    ('Robot Hand', 'Replaceable Food-contact Module (교체형 Pad · Tip, 마모 표시, 위생 결합 구조)', '상 (소모품 · 위생)', '중', '중~상 (Schmalz OFG 마모부품 · Robotiq Fingertip) [S43 · S16]', 1, 'M6~M9'),
    ('Robot Hand', 'Adaptive Finger Mechanism (얇은 Edge 집기 + 감싸쥐기 겸용, Edge Lip)', '상', '중', '상 (Dishcare US 11,731,282 Tapered Finger · 부족구동 Gripper 일반) [S49]', 2, 'M9~M12'),
    ('Robot Hand', 'Compliance / Stiffness (젖은 유리 · 도자기 대응 가변 강성)', '중', '중', '중~상', 3, 'M15'),
    ('Robot Hand', 'Tool Interface (국자 · 집게 · 뚜껑 Tool 결합 · Dock)', '중', '중', '상 (EP 3,881,977 교체형 End piece · Tool Changer 일반) [S50]', 3, 'M18'),
    ('Manipulation', 'Kitchen Object Handling (식세기 랙 형상 기반 식기 배치 계획)', '상', '중', '상 (Dishcraft US 10,507,584) [S49]', 2, 'M12'),
    ('Manipulation', 'Failure Recovery (적재 실패 · 기울어짐 감지 후 다시 놓기)', '중', '중', '중', 3, 'M15'),
    ('Calibration', 'Kitchen Mapping (가전 · 수납 Registry + Template)', '상', '중', '중 (Minimanipulation · Instrumented Environment US 10,518,409) [S50]', 2, 'M12'),
    ('Calibration', 'Task Coordinate Calibration (Robot Home · 가전 기준점 기반 좌표 보정)', '상', '중~상 (가설)', '중', 1, 'M6~M9'),
    ('Interface', 'Robot Mount / Robot Home (보관 · 펼침 경로 · Rail 결합)', '상', '중', '상 (주방 벽 Rail Arm US 7,751,938 외 · 수납장 로봇 US 12,275,130) [S50]', 2, 'M9'),
    ('Interface', 'Tool Dock · Storage Dock', '중', '하~중', '중', 3, 'M18'),
    ('Interface', 'Appliance Interface (식세기 랙 · 문의 Robot 대응 구조 · 연동)', '상', '중', '중 (US 2023/0165427 식세기 맞춤 Routine) [S49]', 2, 'M12'),
    ('Safety', 'Human / Robot Zone Control (주방 평면 기반 Zone · 감속 · Robot Home 자동 복귀)', '중', '중', '중~상 (협동로봇 일반 기술)', 3, 'M18'),
]
IP_PLAN = '24개월 국내 출원 5건 (1순위 2건 M6~M9 · 2순위 3건 M12~M18) + PCT 1건 (M18, 1순위 중 1건) · M3 선행기술조사 (KIPRIS · USPTO · EPO · Google Patents) · 청구항 변리사 검토 · 등록 가능성 미정'

# ---------------------------------------------------------------- risk register
RISKS = [
    ('기술', '자체 Hand가 상용 Gripper보다 낫지 않음', 'M6 30종 비교', 'Buy 전환 · 교체형 Pad · Skill에 집중', 'M6 열위 → 자체 Hand 중단'),
    ('기술', '주방이 바뀌면 성능 급락 (Calibration 과다)', 'M18 주방 3종 적용 시험', 'Interface 보강 · Remodeling 채널 집중', 'Calibration > 8시간 → Retrofit 보류'),
    ('시장', 'CLEAN 가치에 비해 가격이 높음 (WTP 부족)', 'M18 n ≥ 300 · 예약금', 'Rental 중심 · 구성 · 가격 재설계 · ASSIST 묶음', 'WTP < 15% → Seed 범위 재편'),
    ('사업', '설치 · A/S 원가 과다', 'M24 실거주 3세대 실측', '원격진단 · Partner 교육 · 설치 표준', '설치 > 2인 2일 → 채널 재검토'),
    ('안전 · 인증', '가정용 로봇 기준 불확실 (IEC 63682 발행 전)', 'M9 인증기관 사전상담 · M18 사전시험', '저속 · Zone 분리 · 사람 감지 시 정지 · 표준 Gap 관리', '인증 경로 미확정 → 판매 보류'),
    ('경쟁', '가전사 · Humanoid의 빠른 진입', '분기 Monitoring', 'Interface · Skill 협력 Position · 가구사 · 건설사 Partner', '-'),
    ('자금', 'TIPS 미선정', '운영사 IR · 분기 접수', f"Lean 범위 · 비R&D 과제 · 일정 연장 (TIPS 없이 Seed 약 {F['seed_no_tips'] / 10000:.1f}억원)", '-'),
    ('팀', 'Founder 공백 · 핵심 리드 채용 지연', 'M3 리드 3명 채용', '리드 3명 우선 · 지분 보상', 'M6 리드 미충원 → 일정 재편'),
    ('IP', '선행특허 충돌 (식기 로봇 · 주방 Rail)', 'M3 예비 FTO', '회피 설계 · 좁은 청구', '-'),
    ('위생', '식품접촉 소재 규격', 'M12 소재 시험', '규격 실리콘 · 교체형 구조', '-'),
]

# ---------------------------------------------------------------- 20 investor questions + defense (Spec 34)
QA = [
    ('왜 Kitchen인가?',
     '동작이 적고 반복되며 (Pick · Place · Insert · Remove), 작업영역이 정해져 있고 (싱크 · 식세기 · 수납), 다룰 식기 종류가 한정돼 있어 기술 검증이 가능함. 매일 쓰고 주방 리모델링 · 입주라는 구매 계기가 있어 사업 검증도 가능. CLEAN → COOK 확장 경로.',
     '가정관리 무급노동 459.5조원 (2024, FACT) · 연 주방 교체 약 30만 (ASSUMPTION)', '지불의사 미검증 → M18 WTP', '03'),
    ('왜 Robot Arm인가?',
     '식세기 랙 · 서랍 · 상부장 작업은 위치 · 자세 제어가 필요해 6축 Arm이 맞음. 전용 기계는 식기 · 주방마다 재설계, 이동형은 하단 작업 · 가격 · 안전 부담. Arm은 Skill · Tool로 ASSIST · COOK 확장.',
     'FAIRINO FR5 $6,999 · xArm 6 $8,399 (FACT) → BOM 하락 경로', f"Pilot BOM 중 Arm {M['bom_breakdown'][0][1]}만원 → OEM · 국산 Partner 필요", '08 · B6'),
    ('기존 Appliance로 해결 불가능한가?',
     '식세기는 세척만 하고 넣기 · 꺼내기 · 수납은 가전 밖의 일. 가전 개선은 사람 작업을 줄일 뿐 이동 · 적재는 남음. MH는 가전과 경쟁하지 않고 가전 사이를 잇는 Appliance Interface를 만듦.',
     '-', '가전사가 로봇을 내장할 가능성 → Q15', '02'),
    ('CLEAN만으로 고객이 돈을 내는가?',
     f"아직 모름 (핵심 미검증 가설). 가치 Anchor: 식후 정리 40분/일 × 가사서비스 1.5만원/h × 자동화 60% ≈ 월 {M['value']['value']:.0f}만원 vs Rental 월 {A['p_rent']['B'] if isinstance(A['p_rent'], dict) else A['p_rent']}만원 → Gap 존재. 그래서 Premium Remodeling 고객부터, CLEAN은 Platform 검증용, ASSIST 확장 · 위생 · 편의 가치를 묶어 WTP 조사.",
     '가사서비스 요금 1.5만원/h (FACT) · 정리 40분 (ASSUMPTION)', '가치 Gap 명시 · WTP n ≥ 300 + 예약금 (M18)', '03 · 11'),
    ('COOK까지 기술적으로 연결 가능한가?',
     '같은 Arm · Hand · Calibration · Safety를 쓰고, 추가 항목은 Skill · Tool · 식품접촉 규격 · 열/액체 안전. 24개월 범위는 CLEAN, ASSIST가 중간 단계, COOK은 장기 R&D (FUTURE). 공개 범용 모델 (π0.5) 발전이 Skill 확장 속도를 높일 수 있음.',
     'openpi π0 · π0.5 공개 (FACT) [S46]', '조리 안전 · 위생 규격 부담 큼', '09'),
    ('상용 Gripper를 쓰면 안 되는가? 왜 자체 Hand인가?',
     '처음엔 상용 Gripper로 시작해 비교 기준을 잡고 M6에 30종 식기로 비교. 자체 Hand 가설: 얇은 접시 Edge + 컵 · 그릇 감싸쥐기를 Tool 교체 없이, 젖은 표면 미끄럼 감지, 교체형 식품접촉 Pad (위생 · 소모품), 목표 원가. 우위가 없으면 Buy로 전환 (중단 기준).',
     f"Robotiq 2F-85 약 $5,825 (FACT) vs 자체 Hand 원가 가정 Pilot {M['bom_breakdown'][1][1]}만원 → Y5 {M['bom_breakdown'][1][3]}만원", '자체 개발 비용 · 기간', '06'),
    ('주방마다 다른데 실제 적용 가능한가?',
     f"모든 주방이 아니라 호환 주방부터. 적용률 Remodeling {A['a_fit_rate'] * 100:.0f}% · Retrofit {A['a_retro_fit'] * 100:.0f}% (가정) → 평면 30개 분석 (M6). Calibration (Mapping · 기준점 · Template)으로 타 주방 적용, M18 주방 3종 하락 ≤ 10%p · ≤ 4시간.",
     '확보 평면 5종 중 3종 기본 배치 불가 · 1종 미검토 (DERIVED)', '표본 작음', '04 · 07'),
    ('환경 Integration이 과도한 공사를 요구하지 않는가?',
     f"Remodeling은 주방 공사와 동시에 진행 (Interface 증분 {A['p_rr']['B'] if isinstance(A['p_rr'], dict) else A['p_rr']}만원 = Premium 주방 2,000~4,000만원의 약 11~23%). Retrofit은 Compact Mount · Dock만 ({A['p_rt_if']}만원). New-build는 설계 단계 반영. 인테리어 시공은 Partner.",
     'Premium 주방 가격대는 ASSUMPTION (견적 20건으로 검증)', 'Retrofit 호환률 미검증', '10'),
    ('결국 Interior Company 아닌가?',
     f"아님. Remodeling 세대당 5년 매출 {H3['rev5']:,.0f}만원 중 Interface는 {H3['R']['kitchen']:,.0f}만원 (약 {H3['R']['kitchen'] / H3['rev5'] * 100:.0f}%), 나머지는 Robot · Care · 소모품 · Skill. 시공은 Partner, MH Core는 Robot · Hand · Skill · Calibration · Interface 표준 · Safety · 시운전.",
     f"설치 원가 목표 {A['comm_cost'][1]} → {A['comm_cost'][4]}만원 (ASSUMPTION)", '초기 Remodeling 채널 의존', '10 · 13'),
    ('A/S 비용이 너무 크지 않은가?',
     f"Care 원가 Build-up (Y3): 방문 2회 × {A['visit_cost'][2]:g}만원 + 고장 {M['care']['Y3']['corrective'] / 18:.1f}회 × 18만원 + Cloud 4만원 = 연 {KL['care_unit'][2]:.1f}만원 vs Care 요금 48만원 → 마진 {M['care']['Y3']['margin'] * 100:.0f}% (Y3) → {M['care']['Y5']['margin'] * 100:.0f}% (Y5, 원격진단 · 동선 밀도). 고장 1.2회/년 (Warranty 6% 동반) 시 세대당 5년 −84만원",
     'ASSUMPTION (실측 없음)', 'M24 실거주 3세대 실측 필요', '14 · D3'),
    ('Rental이 자본집약적이지 않은가?',
     f"Pilot만 MH 직접 보유, Y4부터 Rental · Capital Partner가 자산 보유 (ASP의 88%에 매입, MH 서비스료 월 6만원, Partner IRR 약 {M['partner_irr']['B']['irr_y'] * 100:.1f}%). MH B/S 부담 지양. 단, Partner 단순 회수기간 약 {M['partner_irr']['B']['payback']:.0f}개월 > 요구 {M['partner_irr']['B']['hurdle']}개월 (가정) → 매입가율 · 서비스료 · 기간 협의 (M24)",
     '코웨이 국내 렌탈 계정 748만 (2026 1Q) · LG 가전 구독 매출 2조원+ (2025) (FACT)', 'Partner 조건 미확인 → M24', '11 · D3'),
    ('Care에 고객이 돈을 내는가?',
     'Care는 소프트웨어 구독이 아니라 고가 로봇의 안전 · 성능 유지 계약 (정기점검 · Calibration · 원격진단 · A/S). 가전 구독의 정기관리 수요가 선례. 가입률 70%는 가정이며 실증에서 확인.',
     'LG 케어매니저 약 4,000명 · 정기관리 포함 구독 (FACT) [S41]', '가입률 미검증', '11'),
    ('Consumables가 실제 필요한가?',
     '억지 Lock-in이 아니라 식품 · 식기 접촉 Pad · Seal의 마모 · 위생 교체. 교체주기는 Pad 수명 시험 (M18~M24)으로 확정. 구매 고객 기대 매출은 연 약 25만원으로 비중이 작음.',
     '식품위생법 "기구" · 고무제 규격 (FACT) [S48]', '교체주기 미검증', '06 · 11'),
    ('Humanoid가 발전하면?',
     '위협이자 기회. 공개 범용 모델은 MH Manipulation Layer에 활용 가능. Humanoid도 주방에서는 하단 작업 · 위생 · 안전 · 가격 ($20,000 · 월 $499) 제약이 있음. MH의 Interface · Skill · Calibration 자산은 다른 Robot Platform에도 적용 가능 (Interface 표준 제공자 Position).',
     '1X NEO 가격 · Figure 식세기 시연 · LG CLOiD 2028 목표 (FACT)', 'Humanoid 가격 급락 시 가격 압박', '15'),
    ('Samsung / LG / Kitchen Furniture Company가 직접 하면?',
     '가능성 있음 (LG CLOiD 2028 상용화 목표). 대응: 가전사 · 가구사는 Partner · 채널 후보 (Appliance Interface · 주방 시공), MH는 설치 · Calibration Know-how와 Installed Base Data로 차별화, 좁은 IP (Food-contact Module · 기준점 Calibration).',
     '한샘 등 가구사의 로봇 협업 보도 없음 (2026) [S51]', '대기업 진입 시 채널 협상력 약함', '15'),
    ('Robot OEM과 무엇이 다른가?',
     'OEM은 Arm을 파는 회사, MH는 Arm을 사서 Hand · Skill · Calibration · Interface · Safety · Care로 주방 System을 만드는 회사. OEM은 공급 Partner이자 BOM 하락 경로.',
     '-', '핵심 부품 OEM 의존', '08'),
    ('실제 핵심 IP는 무엇인가?',
     '1순위: 교체형 Food-contact Module, Task Coordinate Calibration (Dock · 가전 기준점). 2순위: Robot Home · Appliance Interface · 식기 Handling. 식기 로봇 · 주방 Rail 선행특허가 있어 넓은 청구는 어렵고 구체 구조 · 방법 청구를 목표. 실제 방어력은 Data · 절차 · Installed Base.',
     'US 11,731,282 · US 10,507,584 · US 7,751,938 등 (FACT, 청구항 미검토)', 'IP 단독 방어력 약함 · 등록 미정', '15 · E1'),
    ('20억원 전후 Seed가 필요하다면 왜 그 규모인가?',
     f"Bottom-up: 24개월 지출 {F['spend_total'] / 10000:.2f}억원 (인건비 {sum(F['people']) / 10000:.1f}억원 · 24개월 차 약 {F['heads_m24']:.0f}명) − TIPS 8억원 + 3개월 Buffer {F['buffer'] / 10000:.2f}억원 = {F['seed_base'] / 10000:.2f}억원 (≈ {F['seed_base'] / 10000:.0f}억원). Lean (팀 · 범위 축소, 지출 {F['lean_total'] / 10000:.1f}억원) {F['seed_lean'] / 10000:.1f}억원. TIPS 미선정 시 Lean 범위 {F['seed_no_tips'] / 10000:.1f}억원",
     'TIPS 규정 (FACT) · 비용 (ASSUMPTION)', '인건비 · 채용 속도 가정', '18 · A6 · A7'),
    ('24개월 뒤 어떤 Evidence가 있어야 후속투자가 가능한가?',
     '실거주 3세대 CLEAN ≥ 90% · 유료 전환 ≥ 2세대 · 주방 3종 적용 하락 ≤ 10%p · Calibration ≤ 4시간 · BOM · 설치 · Service 원가 실측 · WTP n ≥ 300 (1,490만원 ≥ 30%) · Partner 조건 (리모델링 1 · 렌탈/캐피탈 1) · 출원 5건.',
     'TARGET', '실증 3세대는 표본이 작음', '16 · 18'),
    ('Founder가 왜 적합한가?',
     '[Founder 정보 필요] — 현재 답할 수 없음. 필요한 역량은 로봇 조작 (Hand · Skill), 주방 · 건축 시공 (Interface · 시공 Partner), 고객 · 파트너 영업의 세 축. 이 칸이 채워지기 전에는 투자 판단 불가.',
     '없음', '가장 큰 공백', '17'),
]

# what the investment committee is really testing with each question (docs 16), same order as QA
QA_INTENT = [
    '첫 적용 공간이 기술 · 사업 검증 순서로 합리적인지 (유행 · 감성 선택이 아닌지)',
    'Form Factor가 작업범위 · 원가 · 안전에 맞는지 (이동형 · 전용기계 대비)',
    '가전사의 기능 개선만으로 대체될 위험',
    '첫 Workflow의 지불의사와 가치 Gap',
    '확장 Story가 실제 기술 경로인지, 과장인지',
    '자체 Hand 개발이 시간 · 자금 낭비가 될 위험 (Buy vs Build)',
    '반복 설치 가능성 = Scale의 전제',
    '고객 공사 부담 · 판매 마찰',
    '매출 구성 · 마진 구조 · 밸류에이션 Multiple (시공업 vs 제품회사)',
    '서비스 원가가 Unit Economics를 무너뜨릴 위험',
    'Balance Sheet 부담과 추가 자금 소요',
    '반복매출의 실체 (가입 동기)',
    '억지 Lock-in 여부와 소모품 매출의 신뢰성',
    '기술 진부화 위험과 MH 자산의 잔존 가치',
    '대기업 진입 · 채널 종속 위험',
    'MH가 가치사슬에서 차지하는 위치와 부가가치',
    '방어력 · FTO (침해) 위험',
    '금액 근거 · 자금 효율 · 희석 규모',
    'Milestone 정의와 Series A 준비도',
    'Founder-Market Fit (팀이 이 문제를 풀 수 있는가)',
]
assert len(QA_INTENT) == len(QA)
# spec 34 lists 21 questions; QA[5] answers two of them ("상용 Gripper를 쓰면 안 되는가?" + "왜 자체 Hand가 필요한가?")
QA_SPEC_MERGED = {5: ['상용 Gripper를 쓰면 안 되는가?', '왜 자체 Hand가 필요한가?']}

# ---------------------------------------------------------------- evidence gaps + founder inputs
EVIDENCE = [
    ('Founder · 핵심 팀', '없음 (자리만 정의)', '이력 · 역할 · 지분 · 전업 · 리드 3명 채용', 'Founder 자료 · 채용', '즉시 ~ M3'),
    ('고객 Pain (정리 시간)', '가정 40분/일', '30세대 시간일지 조사', '자체 조사', 'M3'),
    ('WTP · 구매 행동', '없음', '인터뷰 50명 → 조사 n ≥ 300 · 예약금 테스트', '리모델링 상담 · 온라인 패널', 'M6 (정성) · M18'),
    ('Hand 성능', '없음', '상용 Gripper 대비 30종 비교', 'WP1 시험', 'M6'),
    ('CLEAN 성공률', '없음', '목업 ≥ 80% → 가정 ≥ 90%', 'WP6', 'M12 · M24'),
    ('타 주방 적용 · Calibration 시간', '없음', '주방 3종 · ≤ 4시간', 'WP3 · WP6', 'M18'),
    ('평면 호환률', '확보 5종 (1종 가능)', '평면 30개 분석', '입주자모집공고 평면 · 동의 실측', 'M6'),
    ('BOM', '공개가 기반 추정', '100대/년 견적', '부품사 · OEM 견적', 'M18'),
    ('설치 · A/S 원가', '가정', '실거주 3세대 실측', 'WP6', 'M24'),
    ('Partner', '없음 (계약 · LOI 없음)', '리모델링 시공 1 · 렌탈/캐피탈 1 조건', '협의', 'M18 ~ M24'),
    ('인증 경로', '미확정', '인증기관 사전상담 · 사전시험', 'WP5', 'M9 · M18'),
    ('IP', '출원 0건', '선행기술조사 · 출원 5건 + PCT 1건', '변리사', 'M3 · M24'),
    ('시장 기초 통계', '식세기 보급률 · 주방 교체 수 공식 통계 없음', '소비자 조사 · 견적 20건', '자체 조사', 'M6'),
]
FOUNDER_INPUTS = [
    ('신원 · 경력', '이름 · 학력 · 경력 (연도별) · 현재 소속'),
    ('역할 · 지분', '대표 / CTO 등 역할, 지분 · 베스팅 (TIPS: 창업팀 2인 이상 60% 이상)'),
    ('전업 여부', '전업 시점 · 겸직 여부'),
    ('Why This Problem', '이 문제를 택한 이유 · 개인 경험 · 문제 인식 근거'),
    ('Relevant Engineering Experience', '로봇 · 기구 · 제어 · 비전 · 하드웨어 양산 경험'),
    ('Hardware / Product Development', '개발 · 출시한 제품 · 프로젝트 (역할 · 성과)'),
    ('Robot · Mechanical · AI Capability', '논문 · 특허 · 코드 · 수상 등 증빙'),
    ('Construction · Kitchen · Manufacturing', '주방 · 건축 시공 · 제조 경험 (Interface · 설치 표준에 직결)'),
    ('Customer / Partner Network', '리모델링 · 가구사 · 건설사 · 렌탈사 접점 (실명 · 관계 수준, 없으면 "없음")'),
    ('IP · 권리귀속', '보유 특허 · 전 직장 / 연구실 IP 충돌 · 경업금지'),
    ('법인 정보', '설립일 · 소재지 (수도권 여부 = 운영사 투자 요건) · 업력 · 상호 MH Robotics 상표 검색'),
    ('투자 · 과제 이력', '기존 투자 · 정부과제 · 자본금'),
    ('운영사 접촉', 'TIPS 운영사 접촉 현황 (없으면 "없음")'),
    ('채용 Pool', '리드 3명 (Manipulation · Perception · Hand) 후보 여부'),
]

# ---------------------------------------------------------------- competitors detail
COMP = [
    ('1X NEO', 'Humanoid (가정)', '가사 전반 · 원격조작 학습', '$20,000 또는 월 $499 · 2026년 말 첫 배송 목표 (확인 안 됨)', '이동 · 범용 손 · 설치 불필요', 'S19'),
    ('Figure (Helix 02)', 'Humanoid', '식세기 꺼내기 → 수납 → 적재 약 4분 연속 시연 (회사 발표)', '가격 · 출시 미공개', '범용 VLA 모델 학습', 'S45'),
    ('Sunday Robotics Memo', '이동형 가정 로봇', '식세기 적재 · 테이블 정리 시연', 'Beta 2026년 말 · 양산 $10k 미만 목표', '집안 이동 · 학습 Data', 'S20'),
    ('LG CLOiD', 'Humanoid형 홈로봇', '식세기 비우기 · 빨래 등 시연 (CES 2026)', '2026 실증 · 2028 상용화 목표 · 가격 미공개', '가전 연계 · 팔 범위 무릎 높이 이상 (보도)', 'S21'),
    ('Samsung', '가전 · 로봇', 'Bot Handy (2021 Concept) · 2026 AI 가전 중심', '출시 확인 안 됨', '가전 내부 자동화', 'S22'),
    ('Moley Robotic Kitchen', '로봇 주방', '천장 Rail 양팔 조리', '£248,000 (Arm 포함, 2021)', '전용 주방 · 조리 중심', 'S23'),
    ('Posha', '조리대 조리 로봇', '자동 조리', '$1,750 + 월 $15', '조리 전용 기기', 'S24'),
    ('Tesla Optimus', 'Humanoid', '가정용 목표', '소비자 목표가 $20k~30k (양산 시)', '범용', 'S25'),
    ('UR · Doosan + Robotiq', '협동로봇 + Gripper', '부품 (산업용)', 'UR3e $23k~33k · E0509 약 $22k · 2F-85 약 $5,825', 'SI 업체 맞춤', 'S15 · S42'),
    ('한샘 · 리바트', '주방가구', '키친바흐 × 가게나우 빌트인 협업', '로봇 협업 보도 없음 (2026)', '주방 시공 · 수납', 'S51'),
]

# ---------------------------------------------------------------- investment memo verdict
VERDICT = 'MEET'
VERDICT_WHY = [
    ('INVEST가 아닌 이유', ['Founder · 팀 정보가 없음 (가장 큰 공백)', '기술 Baseline (Hand · CLEAN 성공률) 측정값 없음', '고객 지불의사 · 구매 행동 증거 없음',
                         'BOM · 설치 · Care 원가가 모두 가정', '가전사 · Humanoid 진입 속도가 빠름']),
    ('WATCH · PASS가 아닌 이유', ['문제 정의와 접근 (Hand + Skill + Calibration + Interface)이 일관되고 측정 가능한 Gate로 쪼개져 있음',
                              'Bottom-up 자금 계획 · TIPS 레버리지 · 역할 분리 (기술 vs 사업 검증)',
                              '검증 채널 (Remodeling) → Scale 채널 (신축) 순서와 Partner 구조가 현실적',
                              'FACT / ASSUMPTION / TARGET 구분이 엄격해 실사 비용이 낮음']),
]
CHANGE_EVIDENCE = [
    ('Founder · 핵심 팀', '로봇 조작 · Hand 개발 실적과 주방 · 건축 시공 실적을 가진 2인 이상 전업 Founding Team (지분 · 역할 확정)'),
    ('기술 Baseline (M3 이내)', '상용 Arm + Gripper로 30종 식기 파지 · 식세기 적재 영상과 성공률 Data'),
    ('고객 행동', 'Premium 리모델링 고객 10세대 이상 예약금 또는 유료 실증 의향서 (2,020만원 또는 월 33만원 조건)'),
    ('설치 경제성', '서로 다른 주방 2종에서 Calibration · 설치 1일 이내 (목업 가능)'),
    ('Partner', '리모델링 시공 Partner 1곳 + 렌탈 · 캐피탈 Partner 1곳의 조건부 협력 의사 (조건 명시)'),
]
SCORE = [  # 항목, 현재 (1~5), M24 목표, 근거
    ('팀', 1, 4, 'Founder 정보 없음'),
    ('문제 · 고객 Pain', 3, 4, '공식 통계 (가사노동 가치) 있음 · 정리 시간은 가정'),
    ('기술 · 차별성', 2, 4, '접근은 일관 · 측정값 없음 · 선행특허 다수'),
    ('시장', 3, 4, 'Bottom-up 산식 공개 · 비율은 가정'),
    ('BM · Unit Economics', 3, 4, '구조 명확 · Hardware 마진 얇음 · 원가 가정'),
    ('경쟁 · IP', 2, 3, '대기업 · Humanoid · 선행특허'),
    ('실행 계획', 4, 4, 'WP · Gate · 중단 기준 구체'),
    ('자금 계획', 4, 4, 'Bottom-up · TIPS 역할 분리'),
]

# ---------------------------------------------------------------- price hypothesis (floor / reference / anchor)
RC = M['rental']['Y3']
PRICE = [
    ('Robot System', f"{A['p_robot']['B'] if isinstance(A['p_robot'], dict) else A['p_robot']:,}만원",
     f"BOM Y3 {A['bom'][2]:,} → Y5 {A['bom'][4]:,}만원 (Hardware 마진 {(1 - A['bom'][2] / 1490) * 100:.0f}% → {(1 - A['bom'][4] / 1490) * 100:.0f}%)",
     '1X NEO $20,000 (약 2,800만원) · Sunday Memo 목표 $10k 미만 · UR3e $23k~33k', f"가사 대체 월 약 {M['value']['value']:.0f}만원 × 60개월 ≈ {M['value']['value'] * 60:,.0f}만원"),
    ('Interface · Integration (Remodeling)', f"{A['p_rr']['B'] if isinstance(A['p_rr'], dict) else A['p_rr']}만원", f"Kit 원가 Y3 약 {H3['C']['kitchen']:,.0f}만원 (표준부품 65%)",
     'Premium 주방 2,000~4,000만원의 11~23% (ASSUMPTION) · 신축 유상옵션 분양가 대비 9.7% (FACT)', '주방 공사와 동시 시공 → 별도 공사 회피'),
    ('Installation · Calibration', f"{A['p_comm']}만원 (Retrofit {A['p_comm_rt']})", f"원가 Y3 {A['comm_cost'][2]}만원 (약 {KL['inst_h'][2]:.0f}인시)", '가전 출장비 2.8만원 (소비자 부과, 비교 불가) [S13]', '-'),
    ('Rental', f"월 {A['p_rent']['B'] if isinstance(A['p_rent'], dict) else A['p_rent']}만원 (60개월)", f"월 원가 Y3 {RC['cost_m']:.1f}만원 (마진 20% 요금 {RC['fee_at_20']:.1f}만원)", '1X NEO 월 $499 (약 70만원)', f"가사 대체 월 약 {M['value']['value']:.0f}만원 → Gap"),
    ('Care', f"연 {A['p_care']['B'] if isinstance(A['p_care'], dict) else A['p_care']}만원", f"원가 Y3 {M['care']['Y3']['cost']:.1f} → Y5 {M['care']['Y5']['cost']:.1f}만원", 'LG 구독 정기관리 포함 (가격 구조 비공개)', '안전 · 성능 유지'),
    ('Consumables', f"연 {M['cons']['list_y']:.0f}만원 (정가)", f"원가율 {A['cons_cogs']['B'] * 100 if isinstance(A['cons_cogs'], dict) else A['cons_cogs'] * 100:.0f}%", 'Robotiq Fingertip $175~195 · 식품용 실리콘 컵 £7~20', '위생 · 마모 교체'),
]

# ---------------------------------------------------------------- market validation plan
MKT_VALID = [
    ('연 주방 교체 30만 세대', 'ASSUMPTION (교차검증 29.0만 · 30.3만)', '견적 20건 · 인테리어 Partner 인터뷰 · 부동산원 아파트 거래 비중', 'M6'),
    ('Premium 비중 10%', 'ASSUMPTION', '견적 분포 (주방 2,000만원 이상)', 'M6'),
    ('Remodeling 적용 가능률 60%', 'ASSUMPTION', '평면 30개 분석 · 상담 주방 실측', 'M6'),
    ('Premium 재고 10% · 식세기 60% · 호환 40% · 전환 0.5%/년', 'ASSUMPTION / TBV', '소비자 조사 n ≥ 300 · 평면 분석', 'M18'),
    ('신축 Premium 단지 15% · Option 10% · 입주 시 로봇 구매 25%', 'ASSUMPTION', '건설사 · 분양 옵션 사례 조사', 'M18'),
    ('Care 가입 70% · 소모품 구매 70%', 'ASSUMPTION', '실증 3세대 · Pilot 가입 · 교체 Data', 'M24'),
]
