# SoftHand Seed 투자유치 사업계획서 v4 - appendix (table-first, Korean terms, evidence and detail behind the main plan).
from kit import *
import kit
from slides_main import M, RAW, REN, ORI, KIT, FOOT, ph

APPX_LIST = [
    ('A1', '사실·가정 구분'), ('A2', '단계별 점검 기준'), ('A3', 'SoftHand 설계 상세'), ('A4', '성능 지표와 시험 방법'),
    ('A5', '적용 장면 (콘셉트)'), ('A6', '산업 검증 트랙 (머신텐딩)'), ('A7', '경쟁사 상세'), ('A8', '시장 근거 상세'),
    ('A9', '로봇 기술 동향'), ('A10', '수익 모델 가정'), ('A11', '5개년 손익 상세'), ('A12', '인건비·자금 사용 상세'),
    ('A13', '데이터 축적 계획'), ('A14', '장기 확장 경로'), ('A15', '안전·위생·인증·지재권'), ('A16', '위험 요인과 대응'),
    ('A17', '출처'),
]
TOP = 2.0          # content top on appendix slides


def aheader(s, code, title, sub=None):
    text(s, MX, 0.55, 8, 0.28, f'부록 {code}', size=11, bold=True, color=T['accent'])
    text(s, MX, 0.9, CW, 0.52, title, size=24, bold=True, line=0.95, label='atitle ' + code)
    if sub: text(s, MX, 1.46, CW, 0.3, sub, size=13, color=T['text2'], label='asub ' + code)


def afoot(s, code, note=None):
    footer(s, code, left=FOOT, note=note)


def bullets(s, x, y, w, items, size=12, gap=4, label='bullets', color=None):
    hh = text_h(items, size, w - 0.18, space_after=gap)
    text(s, x, y, w, hh + 0.05, items, size=size, bullet='•', indent=0.18, space_after=gap, color=color or T['text2'], label=label)
    return hh


def block_title(s, x, y, w, t, color=None):
    text(s, x, y, w, 0.3, t, size=13, bold=True, color=color or T['text'])
    hline(s, x, y + 0.36, w, color=T['text'], lw=1.0)
    return y + 0.48


B_ = lambda t: (t, {'bold': True})


# ---------------------------------------------------------------- A0 divider
def a00(prs):
    s = new_slide(prs, 'A0 divider')
    text(s, MX, 0.9, 4, 0.9, '부록', size=40, bold=True)
    text(s, MX, 1.85, 3.7, 0.9, '본문의 근거와 상세 계획', size=16, color=T['text2'])
    half = (len(APPX_LIST) + 1) // 2
    for col in range(2):
        x = MX + 4.4 + col * 4.0
        y = 0.95
        for code, t in APPX_LIST[col * half:(col + 1) * half]:
            text(s, x, y, 0.65, 0.3, code, size=13, bold=True, color=T['accent'])
            text(s, x + 0.65, y, 3.2, 0.3, t, size=13, label='toc ' + code)
            y += 0.5
            hline(s, x, y - 0.1, 3.6)
    footer(s, 'A', left=FOOT)


# ---------------------------------------------------------------- A1 evidence
def a01(prs):
    s = new_slide(prs, 'A1')
    aheader(s, 'A1', '사실·가정 구분', '확인된 사실, 계획, 가정, 장기 가능성, 확보가 필요한 자료를 구분해 표기')
    rows = [
        [B_('확인된 사실'), '사업 아이디어·기술 구상·사업계획서 초안 (2026.10)\n외부 공개 자료(통계청·IFR·BCG·외식업 인력·NRA·조리 로봇 사례) 출처 확인\n법인·창업팀·특허·시제품·고객 계약·매출·보유 자금은 미확인',
         '회사 실적으로 표현하지 않음'],
        [B_('계획 (목표)'), 'SoftHand-4 V1, 주방 작업 소프트웨어 (검증 대상 6종 작업), 공동개발 고객 3곳, 유료 PoC 5건, 재구매 2곳\n로봇 2종, 고객 인터뷰 30곳, 24개월 추진 일정, 단계별 점검 기준',
         '"목표", "계획"'],
        [B_('가정'), '핸드 1,500만 원 (원가 950만 → 750만 원), 작업 소프트웨어 300만 원, 유지보수 연 150만 원, 유료 PoC 5,000만 원\n5개년 매출·손익 (기본 계획), 성능 목표치 (기존 머신텐딩 기준 수치를 주방 작업에 적용)',
         '"가정"'],
        [B_('장기 가능성'), '가정용 주방 확대, 로봇·가전 기업 제품 탑재, 라이선스, 빌트인 주방 (건설사·디벨로퍼), 데이터 축적',
         '"장기 가능성"\n수치 미산정'],
        [B_('확보 필요 자료'), '창업자·핵심 인력 이력, 시제품·무편집 시험 영상, 특허·FTO\n고객 인터뷰·LOI·공동개발 고객, 유료 PoC, BOM, 고객 기존 수치, 동일 조건 비교시험',
         '[정보 입력 필요]\n투자 실사 전 확보'],
    ]
    table(s, MX, TOP + 0.05, CW, ['구분', '현재 내용', '표기 원칙'], rows, col_w=[2.0, 7.43, 2.4], size=11.5, pad=0.08, max_h=4.3, label='A1 table')
    footnote(s, '이미지: SoftHand 이미지는 모두 같은 SoftHand-4 콘셉트 모델의 렌더링이며 실제 시험 장면이 아님. 실물 확보 시 시제품 사진 → 시험 영상 → 고객 현장 순으로 교체')
    afoot(s, 'A1')


# ---------------------------------------------------------------- A2 gates
def a02(prs):
    s = new_slide(prs, 'A2')
    aheader(s, 'A2', '단계별 점검 기준', '실패 조건과 결정을 먼저 정하고 자금을 단계별로 집행 · 모든 기준은 목표')
    acc = lambda t: (t, {'bold': True, 'color': T['accent']})
    rows = [
        [acc('M6'), '기술: 핸드 하나로 검증 대상 작업 수행', '검증 대상 6종 작업 벤치 반복 시연\n목표 토크·반복성 기록 공개', '핸드 구조 재검토\n(구동 방식·골격·잠금)', '후속 채용 보류\n시제품 예산 재배분'],
        [acc('M12'), '고객: 주방 고객이 비용 지불', '유료 PoC 1건 이상\n고객 기존 수치 확보, 지불의사 확인', '1차 고객군·작업 재정의\n(다른 작업·다른 주방 유형)', '6개월 연장 자금 집행 재검토'],
        [acc('M18'), '제품: 반복 판매·작업 소프트웨어 재사용', '설계 확정, 첫 재구매\n재사용률 측정 시작, 로봇 B 통합', '제품 구조 재검토\n제품 + 서비스 모델 검토', '시리즈 A 착수 시점 조정'],
        [acc('M24'), '확장: 재구매·이식성', '재구매 고객 2곳 이상, 로봇 2종 호환\n상업용·가정용 환경 공통 작업\n매출총이익률 검증', '시리즈 A 확장 보류\n축소 운영·브리지 검토', '시리즈 A 규모·시점 결정'],
    ]
    table(s, MX, TOP + 0.05, CW, ['시점', '검증 가설', '통과 기준 (목표)', '미달 시 결정', '자금 영향'], rows,
          col_w=[0.85, 2.85, 3.38, 2.6, 2.15], size=12, pad=0.09, max_h=3.75, label='A2 table')
    by = 5.85
    hline(s, MX, by, CW, color=T['text'], lw=1.0)
    bullets(s, MX, by + 0.15, CW, ['점검은 이사회·투자자와 분기별 지표 리뷰로 판단, 미달 시 범위 축소 또는 방향 전환을 결정한 뒤 다음 단계 자금 집행 (18개월 + 6개월 구조와 연동)',
                                    '시험 결과는 횟수·성공 건수·재시도 분리·신뢰구간으로 보고, 산업 검증 트랙(A6)은 토크·반복성·내구성 확인에 활용'],
            size=11.5, label='A2 notes')
    afoot(s, 'A2')


# ---------------------------------------------------------------- A3 SoftHand engineering
def a03(prs):
    s = new_slide(prs, 'A3')
    aheader(s, 'A3', 'SoftHand 설계 상세: 구성·구동·센싱·하중', '구동 방식은 미확정, 창업 후 3개월 내 비교시험으로 선정 (M6 점검 연동)')
    lw = 7.9
    rows = [
        [B_('구성 (4지)'), '손가락 3 + 대향 엄지, 도구·손잡이·노브·버튼을 다루는 최소 구성', '5지 대비 부품 수·비용·내구성·제어 복잡도 (5지는 시리즈 A 이후)'],
        [B_('구동부'), '전동 텐던을 기준 후보로 소형 유압·공압과 비교', '손 무게·유지력·응답·누설·소음·소비전력·정비비'],
        [B_('가변 순응성'), '탄성 요소·장력 제어, 필요 시 잠금 기구 (가변 강성)', '접촉 충격 완화와 조작 토크 유지의 균형'],
        [B_('감각부'), '손끝·손바닥 접촉센서, 관절·장력 센서, 손목 6축 힘·토크 센서', '물·기름·열·오염 조건 편차와 재교정'],
        [B_('접촉부'), '교체형 패드·외피, 용도별 재질 분리 (주방: 세척·내열·식품 접촉 / 산업: 내마모·내유)', '미끄럼·마모·세척·재질 적합성 시험'],
        [B_('로봇 장착'), '공통 손목 모듈·플랜지 어댑터·TCP 보정·통신 드라이버', '로봇 2종 실제 통합, 이식성 측정'],
    ]
    table(s, MX, TOP + 0.05, lw, ['기술 요소', '개발 내용', '검증 기준'], rows, col_w=[1.35, 3.55, 3.0], size=11.5, pad=0.075, max_h=4.6, label='A3 table')
    rx = MX + lw + 0.45; rw = W - MX - rx
    y = block_title(s, rx, TOP + 0.05, rw, '하중 설계 예시 (계산 예)')
    y += bullets(s, rx, y, rw, ['3kg 냄비, 무게중심 0.20m: 정적 모멘트 약 5.9 N·m (가속·충격 시 증가), 큰 냄비는 양손·거치대 보조',
                               '산업 예: 소재 1.5kg, 무게중심 0.10m에서 약 1.5 N·m',
                               '팬 손잡이·노브 조작 토크는 대상 도구·가전 실측 후 사양 확정',
                               '손의 파지 하중 ≠ 로봇 팔 가반하중 (손·어댑터·도구 합산)'], size=11, label='A3 load') + 0.25
    y = block_title(s, rx, y, rw, '제어 구조')
    bullets(s, rx, y, rw, ['비전: 도구·용기·조작부 위치와 상태', '촉각: 접촉·미끄러짐 / 손목 힘센서: 반력·토크',
                           '학습 기반 모델은 상위 작업 선택에 활용, 힘·속도·안전 한계는 독립 제어 계층에서 보장'], size=11, label='A3 ctrl')
    afoot(s, 'A3', note='공통 제어기·손목 모듈은 유지하고 접촉부만 용도별로 분리')


# ---------------------------------------------------------------- A4 performance
def a04(prs):
    s = new_slide(prs, 'A4')
    aheader(s, 'A4', '성능 지표와 시험 방법', '파지 성공률이 아닌 작업 완료 기준 · 모든 수치는 목표이며 실적 아님')
    rows = [
        [B_('검증 대상 작업 완료율\n(집게·팬·용기·노브·버튼·문)'), '작업별 벤치 반복 시연', '승인 작업 95% 이상', '최초 시도·재시도·중단 분리 보고, 신뢰구간'],
        [B_('등록 물체 집기·투입 (재료·용기·도구)'), '10종, 95% 이상', '20종, 98% 이상', '종별 100회, 낙하 없이 투입 완료'],
        [B_('문·노브·버튼 조작 (가전·조작부)'), '대표 가전 2종', '4종, 완료율 95% 이상', '조작력·작업 시간 함께 보고'],
        [B_('핸드 하중'), '원통 물체 1kg', '동일 조건 2kg', '자세·속도·모멘트 한계 명시'],
        [B_('내구성'), '반복 개폐 10만 회', '30만 회 (양산 목표 100만 회)', '하중·패드 교체 주기·힘 저하율 명시'],
        [B_('로봇 이식성'), '로봇 A 기준 기록', '로봇 B 재사용 검증', '추가 엔지니어링 시간·완료율·재사용 모듈 비중'],
        [B_('재사용률'), '측정 체계 수립', 'M12부터 측정, 상승 추세', '신규 고객 적용 시 그대로 쓴 모듈 비중'],
        [B_('사람 개입·메뉴 전환 시간'), '고객 기존 수치 확보', '기존 수치 대비 감소 (PoC 측정)', '재료 보충·복구 포함, 임의 목표치 없음'],
        [('연구 트랙 (점검 제외)', {'bold': True, 'color': T['muted']}), '스크루드라이버 저토크 체결 데모', '썰기·유연체 등 고난도 작업', 'Seed 성공 조건이 아닌 기술 트랙'],
    ]
    table(s, MX, TOP + 0.05, CW, ['지표', '12개월 목표', '24개월 목표', '시험 정의'], rows, col_w=[3.15, 2.45, 2.75, 3.48], size=11.5, pad=0.055,
          max_h=4.6, label='A4 table')
    afoot(s, 'A4', note='수치는 기존 계획(머신텐딩 기준)을 주방 작업에 그대로 적용 · 속도·위생·온도 지표는 PoC 설계 시 추가')


# ---------------------------------------------------------------- A5 application scenes (concept renders)
def a05(prs):
    s = new_slide(prs, 'A5')
    aheader(s, 'A5', '적용 장면 (콘셉트 렌더링)', '검증 대상 주방 작업을 하나의 핸드로 수행하는 장면 예시 · 실제 시험 장면 아님')
    steps = [('lx_pick', '재료 집기'), ('lx_lid', '용기 열기'), ('lx_drop', '팬에 투입'), ('lx_tongs', '집게 사용'),
             ('lx_stir', '국자로 젓기'), ('lx_knob', '노브 조작'), ('lx_plate', '플레이팅'), ('pro_tongs', '상업용 주방 라인 (집게)')]
    gap = 0.2; pw = (CW - 3 * gap) / 4; ph_ = 1.62
    for i, (f, a) in enumerate(steps):
        r, c = divmod(i, 4)
        x = MX + c * (pw + gap); y = TOP + 0.05 + r * (ph_ + 0.55)
        image(s, KIT(f + '.jpg'), x, y, pw, ph_, focus=(0.5, 0.5))
        text(s, x, y + ph_ + 0.08, pw, 0.3, [[(f'{i + 1}  ', {'color': T['accent']}), (a, {})]], size=12, bold=True, label='scene ' + a)
    afoot(s, 'A5', note='1~7 가정·프리미엄 주방, 8 상업용 주방 · 툴 교체 최소화는 목표이며 미검증')


# ---------------------------------------------------------------- A6 industrial validation track
def a06(prs):
    s = new_slide(prs, 'A6')
    aheader(s, 'A6', '산업 검증 트랙: 머신텐딩', '주 시장이 아닌 시험장 · 높은 반복 조건에서 핸드의 기본 성능을 검증')
    steps = [('s1_door', '문 열기'), ('s2_pick', '소재 집기'), ('s3_load', '기계에 넣기'), ('s4_press', '버튼 누르기'),
             ('s5_unload', '완성품 꺼내기'), ('s6_close', '문 닫기')]
    lw = 6.6; gap = 0.16; pw = (lw - 2 * gap) / 3; ph_ = 1.45
    for i, (f, a) in enumerate(steps):
        r, c = divmod(i, 3)
        x = MX + c * (pw + gap); y = TOP + 0.05 + r * (ph_ + 0.5)
        image(s, RAW(f + '_color.png'), x, y, pw, ph_, focus=(0.5, 0.5))
        text(s, x, y + ph_ + 0.08, pw, 0.28, [[(f'{i + 1}  ', {'color': T['accent']}), (a, {})]], size=12, bold=True, label='mt ' + a)
    text(s, MX, TOP + 2 * (ph_ + 0.5) + 0.05, lw, 0.26, '공작기계 소재 투입·배출 6단계 (콘셉트 렌더링)', size=10, color=T['muted'])
    rx = MX + lw + 0.5; rw = W - MX - rx
    y = block_title(s, rx, TOP + 0.05, rw, '역할')
    y += bullets(s, rx, y, rw, ['파지·문 개폐·버튼·레버·노브·토크·반복성·산업 내구성을 높은 반복 조건에서 시험',
                               '같은 핸드·제어 소프트웨어·기본 조작(열기·집기·누르기·돌리기)을 주방 작업 개발에 재사용'], size=11.5, label='A6 a') + 0.25
    y = block_title(s, rx, y, rw, '사업상 위치')
    y += bullets(s, rx, y, rw, ['기존 계획의 산업 PoC·판매는 5개년 기본 계획에 포함 (주방·산업 비중은 PoC 후 재산정)',
                               '스크루드라이버 저토크 체결은 상용 작업이 아닌 기술 데모 (연구 트랙)'], size=11.5, label='A6 b') + 0.25
    y = block_title(s, rx, y, rw, '이전 사업계획 대비')
    bullets(s, rx, y, rw, ['첫 시장이던 머신텐딩을 검증 트랙으로 조정, 내용은 보존'], size=11.5, label='A6 c')
    afoot(s, 'A6')


# ---------------------------------------------------------------- A7 competition detail
def a07(prs):
    s = new_slide(prs, 'A7')
    aheader(s, 'A7', '경쟁사 상세: 전용 자동화 · 그리퍼 · 다른 핸드', '공개 정보 기반 정성 비교, 독립 비교시험 아님 · 회사명은 범주 예시이며 우열을 주장하지 않음')
    rows = [
        [B_('전용 조리 자동화'),
         'Moley Robotics: 천장 레일 양팔 로봇 주방·전용 조리도구 (약 13.4만~34만 달러, 2021)\n'
         'Miso Robotics Flippy: 튀김 스테이션 전용 로봇\n에니아이 알파그릴: 패티 조리 시간당 200장 이상, 국내 버거 브랜드 공급\n'
         '로보아르테: 협동로봇 1대 치킨 조리 (Series A 75억 원, 2022)\n삼성웰스토리: 급식 사업장 국·볶음·면·튀김 조리로봇 (2023~)\n'
         'Chef Robotics: 식품 공장 밀 조립 (Series A 4,310만 달러, 2025)',
         '특정 메뉴·작업 최적화\n상용 운영 사례', '새 메뉴·공정마다 추가 장비·설비·통합'],
        [B_('산업용 그리퍼 · EOAT'), '평행·진공·맞춤 EOAT, Robotiq 적응형 그리퍼 등', '저가·고신뢰·통합 용이', '사람용 도구·손잡이·노브 조작 제한, 툴 체인저 필요'],
        [B_('소프트·다지 핸드'), 'qb SoftHand Industry · Shadow · Allegro · Tesollo · Sharpa · Tesla·Figure 자체 개발', '형상 적응·고자유도',
         '토크·강성 전환 제한 또는 비용·내구성, 연구·휴머노이드 중심'],
        [('당사 SoftHand (목표)', {'bold': True, 'color': T['accent']}), '사람용 주방 도구 조작 + 재사용 작업 소프트웨어', '—', '미검증, Seed 기간 동일 조건 비교시험'],
    ]
    h1 = table(s, MX, TOP - 0.08, CW, ['범주', '대표 사례 (공개 정보)', '강점', '주방 확장 관점 한계'], rows,
               col_w=[1.75, 6.45, 1.6, 2.03], size=10.5, pad=0.045, max_h=3.6, label='A7 table')
    oy = TOP - 0.08 + h1 + 0.16
    text(s, MX, oy, CW, 0.3, '로봇·가전 기업이 직접 만든다면', size=12.5, bold=True)
    table(s, MX, oy + 0.32, CW, None, [
        [B_('관찰'), 'Tesla·Figure는 손 내재화, 다수 로봇 제조사는 그리퍼 파트너 의존, NVIDIA 레퍼런스 휴머노이드(2026.6)는 외부 촉각 핸드 채택'],
        [B_('해석'), '로봇·가전 기업은 경쟁자이자 판매 채널, 단일 기업은 여러 브랜드에서 쓰는 작업 소프트웨어를 만들기 어려움'],
        [B_('대응'), '로봇 무관 통합, 로봇 2종 이식성 검증, 로봇·가전 기업 협력 우선'],
    ], col_w=[0.8, CW - 0.8], size=10.5, pad=0.045, max_h=1.2, label='A7 oem')
    afoot(s, 'A7', note='출처: 부록 A17 · Moley 사진은 저작권 확인 전 사용하지 않음 (본 자료 이미지는 자체 콘셉트 렌더링)')


# ---------------------------------------------------------------- A8 market evidence
def a08(prs):
    s = new_slide(prs, 'A8')
    aheader(s, 'A8', '시장 근거 상세', '공식 통계와 공개 보도 기준 · 시장조사기관 전망은 편차가 커서 범위로 표기')
    rows = [
        [B_('국내 주방 규모'), '숙박·음식점업 사업체 861,863개, 종사자 2,293,381명 (2023, 전년 대비 +0.4%, +3.5%)', '통계청 전국사업체조사 (2024.9 잠정)'],
        [B_('주방 인력'), '조리·식당 서비스 인력 부족률, 2023년 코로나19 이전 대비 약 2배\n외식업체 952곳 중 27.6% 인력난 응답 (2023)', '한국외식산업연구원·고용노동부 자료 (헤럴드경제, 2025.5)'],
        [B_('학교 급식 실증'), '부산교육청, 서비스로봇 실증사업으로 3개교에 튀김·볶음·국 조리로봇 도입 (2025)\n솥 앞 작업시간 평균 69%, 근력 작업 횟수 72% 감소, 확대 도입 긍정 응답 90% 이상', '서울신문 등 (2025.12)'],
        [B_('급식 위탁'), '삼성웰스토리, 2023년 조리로봇 코너 도입, 국·탕·볶음·면·튀김 조리로봇을 공정별 배치', '인사이트코리아 등 보도'],
        [B_('해외 운영자'), '미국 외식 운영자 49%: 인력 대응 기술·자동화가 2025년 자기 업종에서 더 보편화', 'NRA (Restaurant Dive, 2025)'],
        [B_('시장 전망'), '글로벌 식품 로봇 18.1억 달러 (2023) → 68.1억 달러 (2030), 연 20.6%\n다른 기관 2030년 전망 49.7억 달러 (식품 제조·포장 포함 광의)', 'Grand View Research · The Business Research Company'],
        [B_('투자 사례'), 'Chef Robotics Series A 4,310만 달러 (2025, 지분 2,060만 + 장비 금융 2,250만 달러)\n로보아르테 Series A 75억 원 (2022)', 'AgFunderNews · 파이낸셜뉴스'],
        [B_('로봇 보급'), '산업용 로봇 가동 약 500만 대, 2025년 신규 60만 대 이상 · 한국 로봇 밀도 1,220대/직원 1만 명', 'IFR (2026)'],
    ]
    table(s, MX, TOP - 0.05, CW, ['구분', '내용', '출처'], rows, col_w=[1.6, 7.0, 3.23], size=10.5, pad=0.055, max_h=4.95, label='A8 table')
    afoot(s, 'A8', note='국내 주방 로봇 시장 규모는 공식 통계 부재로 미제시 · 국내 수요는 고객 인터뷰 30곳으로 검증 예정')


# ---------------------------------------------------------------- A9 technology trends
def a09(prs):
    s = new_slide(prs, 'A9')
    aheader(s, 'A9', '로봇 기술 동향: 판단·시각·로봇 팔은 상용화, 현실 조작은 과제', '각 수치는 출처 발표 기준이며 독립 검증 아님')
    rows = [
        [B_('판단 · AI 모델'), '빠르게 발전', 'Gemini Robotics 1.5 (2025.9) · NVIDIA Isaac GR00T N1.6 (2026.1) · Physical Intelligence 기업가치 56억 달러 (2025.11)'],
        [B_('시각 · 연산'), '상용 수준', 'NVIDIA Jetson AGX Thor: 2,070 FP4 TFLOPS, 이전 세대 대비 AI 연산 7.5배 (2025.8)'],
        [B_('로봇 팔·휴머노이드'), '대규모 보급', '산업용 로봇 가동 약 500만 대, 연 60만 대 이상 설치 (IFR, 2026.9) · Figure 기업가치 390억 달러 (2025.9)'],
        [('손 · 현실 세계 조작', {'bold': True, 'color': T['accent']}), ('남은 과제', {'bold': True, 'color': T['accent']}),
         '"The forearm and hand are more difficult than the entire rest of the robot." Elon Musk, Tesla 2025년 3분기 실적 발표 (2025.10)\n'
         'NVIDIA 레퍼런스 휴머노이드(2026.6) 외부 촉각 핸드 채택 · Figure 03 촉각 손끝 (3g 감지, 2025.10)'],
        [B_('자본 유입'), '—', '로보틱스 스타트업 투자 2025년 150억 달러 (사상 최대), 2026년 상반기 188억 달러 (Crunchbase News, 2026.6)'],
    ]
    table(s, MX, TOP + 0.05, CW, ['구분', '상태', '근거 (출처·시점)'], rows, col_w=[2.6, 1.45, 7.78], size=12, pad=0.09, max_h=3.9, label='A9 table')
    footnote(s, '해석: AI 모델·시각·로봇 팔이 상용화되면서 사람용 물체·도구·조작부를 다루는 손과 조작 소프트웨어가 남은 과제, 주방은 도구·형상·힘 조절이 가장 다양한 환경')
    afoot(s, 'A9', note='출처: 부록 A17')


# ---------------------------------------------------------------- A10 revenue model assumptions
def a10(prs):
    s = new_slide(prs, 'A10')
    aheader(s, 'A10', '수익 모델 가정', '모든 가격·원가·마진은 검증 전 가정 · 기존 계획의 수치를 그대로 유지')
    rows = [
        [B_('초기 (Seed)'), '유료 PoC (주방 중심, 산업 검증 트랙 포함)', '건당 5,000만 원 (8~12주, 대여 핸드 포함)', '40%', '지불의사 검증·고객 기존 수치 확보'],
        [B_('초기'), '통합 엔지니어링', '프로젝트당 4,000만 원', '40%', '진입 수단, 비중 축소 목표'],
        [B_('초기~중기'), 'SoftHand 하드웨어', '핸드 패키지 1,500만 원 (직판)\n1,200만 원 (파트너 순매출)', '원가 950만 → 750만 원', 'BOM·공급사 확정 후 재산정 (M18)'],
        [B_('초기~중기'), '주방 작업 소프트웨어', '핸드당 300만 원 (파트너 240만 원)\n핸드당 1.0 → 1.6개', '85%', '작업 단위 판매'],
        [B_('중기'), '제어 SW·유지보수', '설치 핸드당 연 150만 원', '70%', '설치 기반 반복 매출'],
        [B_('장기'), '로봇·가전 기업 제품 탑재, 라이선스, 빌트인 협력', ph('출하량·설치량 연동 [협의 후 검증]'), '—', '기본 계획 미반영 (추가 성장 요인)'],
    ]
    table(s, MX, TOP + 0.05, CW, ['단계', '매출원', '과금 단위·가정 가격', '매출총이익률 가정', '역할'], rows,
          col_w=[1.3, 2.9, 3.4, 1.85, 2.38], size=12, pad=0.08, max_h=4.1, label='A10 table')
    footnote(s, '주방 고객의 가격 수용성은 유료 PoC에서 검증 · 통합 매출은 장기 모델이 아닌 진입·제품화 수단')
    afoot(s, 'A10')


# ---------------------------------------------------------------- A11 P&L detail
def a11(prs):
    s = new_slide(prs, 'A11')
    B = M['base']; A = M['assumptions']
    aheader(s, 'A11', '5개년 손익 상세 (기본 계획)', '단위: 억 원 · 대규모 주방 체인·로봇 OEM·가정용 매출 제외 · 1년차 = 투자 집행 첫해')
    f = lambda v: f'{v:.1f}'.replace('-', '−')
    inst = []; tot = 0
    for d, p in zip(A['hand_direct'], A['hand_partner']): tot += d + p; inst.append(str(tot))
    rows = [
        ['유료 PoC / 통합 (건)'] + [f'{a} / {b}' for a, b in zip(A['poc_n'], A['int_n'])],
        ['신규 핸드 (대) 직판 / 파트너'] + [f'{a} / {b}' for a, b in zip(A['hand_direct'], A['hand_partner'])],
        ['설치 핸드 누적 (대)'] + inst,
        ['매출: 유료 PoC·통합'] + [f(v) for v in B['poc_int']],
        ['매출: SoftHand 하드웨어'] + [f(v) for v in B['hw']],
        ['매출: 작업 소프트웨어'] + [f(v) for v in B['skill']],
        ['매출: 제어 SW·유지보수'] + [f(v) for v in B['runtime']],
        ['매출: 파트너 판매 (하드웨어+SW)'] + [f(v) for v in B['partner']],
        [B_('총매출')] + [(f(v), {'bold': True}) for v in B['rev']],
        ['매출총이익 (이익률)'] + [f'{f(g)} ({m * 100:.0f}%)' for g, m in zip(B['gp'], B['gm'])],
        ['운영비'] + [f(v) for v in B['opex']],
        [B_('영업손익')] + [(f(v), {'bold': True}) for v in B['op']],
        [B_('반복 매출 비중')] + [(f'{v * 100:.0f}%', {'bold': True, 'color': T['accent']}) for v in B['reuse_share']],
    ]
    lw = 7.75
    table(s, MX, TOP + 0.02, lw, ['항목', '1년', '2년', '3년', '4년', '5년'], rows, col_w=[2.75] + [1.0] * 5, size=11,
          align=['l', 'r', 'r', 'r', 'r', 'r'], pad=0.045, max_h=4.85, label='A11 table')
    rx = MX + lw + 0.45; rw = W - MX - rx
    y = block_title(s, rx, TOP + 0.02, rw, '민감도 (5년차)')
    h1 = table(s, rx, y, rw, None, [[B_('판매량 −30% (3~5년차)'), '매출 31.4억\n영업손익 −7.1억'],
                                    [B_('핸드 원가 절감 지연'), '영업손익 −3.1억'],
                                    [B_('파트너 채널 1년 지연'), '매출 32.3억\n영업손익 −6.4억'],
                                    [B_('판매량 −50%'), '매출 22.4억\n영업손익 −11.9억']],
               col_w=[2.05, rw - 2.05], size=11, pad=0.06, label='A11 sens')
    y = block_title(s, rx, y + h1 + 0.25, rw, '산정 기준')
    bullets(s, rx, y, rw, ['운영비 1·2년차 = Seed 24개월 집행 계획 (A12)', '3~5년차 = 평균 인원 14·19·23명 × 1인 연 0.72~0.76억 + 비인건비 4.5~6.2억',
                           '매출원은 분야 무관 가정, 주방·산업 비중은 PoC 후 재산정', '미반영 상승 요인은 본문 10장'], size=11, label='A11 basis')
    afoot(s, 'A11')


# ---------------------------------------------------------------- A12 personnel & use of funds detail
def a12(prs):
    s = new_slide(prs, 'A12')
    SP = M['seed']
    aheader(s, 'A12', '인건비·자금 사용 상세', '18개월 핵심 운영 + 6개월 연장 · 정부지원금·공동개발비 미반영')
    roles = {'대표 · 사업/제품 (Founder)': '대표 · 사업/제품', 'CTO · Hand 메카트로닉스 (Co-founder)': 'CTO · 핸드 메카트로닉스', '기구·구동 엔지니어': '기구·구동 엔지니어',
             '제어·임베디드 엔지니어': '제어·임베디드 엔지니어', 'Robot SW · Skill 엔지니어': '로봇 SW·작업 소프트웨어', '현장 통합(FAE) 엔지니어': '현장 통합 엔지니어',
             'Vision · 조작 AI 엔지니어': '비전·조작 AI 엔지니어', 'DFM · 품질 엔지니어': '설계·품질 엔지니어'}
    hr = []; tot = 0
    for role, start, mc in M['hires']:
        c = mc * (24 - start + 1); tot += c
        hr.append([roles.get(role, role), f'M{start}', f'{c:.2f}억'])
    hr.append([B_('합계 · 8명'), '', (f'{tot:.1f}억', {'bold': True})])
    lw = 5.2
    text(s, MX, TOP + 0.02, lw, 0.3, '핵심 인력 채용 계획', size=13, bold=True)
    h1 = table(s, MX, TOP + 0.4, lw, ['역할', '합류', '24개월 인건비'], hr, col_w=[2.75, 0.9, 1.55], size=11, align=['l', 'c', 'r'], pad=0.05,
               max_h=3.6, label='A12 hires')
    text(s, MX, TOP + 0.5 + h1, lw, 0.5, '창업자 연 5,000만 원, 엔지니어 연 7,000만 원 + 4대보험·퇴직충당 15%', size=10.5, color=T['muted'], label='A12 basis')
    rx = MX + lw + 0.5; rw = W - MX - rx
    names = {'핵심 인력 (8명 단계 채용)': '인건비 (8명)', 'Prototype · 내구시험': '시제품·내구 시험', 'Robot 2종 · 시험 Cell': '로봇 2종·주방/산업 시험 설비',
             '고객 PoC · 현장통합(비청구)': '실증·현장 통합 (비청구)', 'SW · AI · Data': '소프트웨어·데이터', '제조 · 품질 · 안전 · IP': '제조·품질·안전·지재권',
             'Kitchen Bench Demo': '가정용 환경 벤치', '운영 (임차·법무·회계·보험·출장)': '운영 (임차·법무·회계·보험·출장)', '예비비 · 운전자본': '예비비·운전자본'}
    rows = [[names.get(k, k), f'{v:.1f}억', f'{v / 20 * 100:.0f}%'] for k, v in SP['uof']]
    rows.append([B_('합계'), (f'{SP["uof_total"]:.1f}억', {'bold': True}), ('100%', {'bold': True})])
    text(s, rx, TOP + 0.02, rw, 0.3, '자금 사용 계획', size=13, bold=True)
    h2 = table(s, rx, TOP + 0.4, rw, ['항목', '금액', '비중'], rows, col_w=[rw - 2.2, 1.2, 1.0], size=11, align=['l', 'r', 'r'], pad=0.045,
               max_h=3.6, label='A12 uof')
    opex = SP['opex_y1'] + SP['opex_y2']
    text(s, rx, TOP + 0.55 + h2, rw, 0.8,
         [[('손익 연결  ', {'bold': True, 'color': T['text']}), (f'운영비(예비비 제외) 1년차 {SP["opex_y1"]:.1f}억 + 2년차 {SP["opex_y2"]:.1f}억 = {opex:.1f}억', {})],
          [('집행 구조  ', {'bold': True, 'color': T['text']}), (f'18개월 핵심 운영 {SP["core18"]:.1f}억 + 6개월 연장 {SP["ext6"]:.1f}억 + 예비비 {SP["uof"][-1][1]:.1f}억', {})]],
         size=11, color=T['text2'], space_after=3, label='A12 link')
    afoot(s, 'A12', note='매출이 없어도 24개월 운영, 예비비 잔존')


# ---------------------------------------------------------------- A13 data
def a13(prs):
    s = new_slide(prs, 'A13')
    aheader(s, 'A13', '데이터 축적 계획', '현재 보유 데이터 없음 · 설치 대수가 늘면 실제 주방 작업 데이터가 쌓이는 구조 (계획)')
    rows = [
        [B_('Seed 수집 계획 (목표)'), '도구·용기·조작부 30종 이상, 시도 1만 회 이상, 영상·촉각·힘·관절 시간 동기화\n실패 원인 라벨링: 미끄러짐·위치 오차·재파지·힘 보정·복구 행동\n물체·세션·주방 단위로 나눠 검증'],
        [B_('활용'), '작업 소프트웨어 개선, 실패 복구 기능, 새 도구·메뉴 적용 시간 단축 (목표)'],
        [B_('데이터 권리'), '고객 데이터의 수집·학습·재사용 범위를 계약으로 분리 합의\n고객 레시피·운영 정보는 고객 자산으로 보호, 작업 개선용 일반화 데이터만 회사 자산\n가정용은 영상·개인정보 최소 수집 원칙'],
        [B_('함께 쌓이는 역량'), '소프트-리지드 하이브리드 구조, 교체형 접촉부, 강성 전환\n힘·미끄러짐 기반 도구·조작부 제어, 주방 현장 통합·PoC 운영 경험'],
    ]
    table(s, MX, TOP + 0.05, CW, ['구분', '내용'], rows, col_w=[2.6, CW - 2.6], size=12, pad=0.09, max_h=4.5, label='A13 table')
    footnote(s, '목표는 성공 영상이 아닌 "어떤 상황에서 실패했고 어떻게 복구했는가"의 기록 · 데이터는 작업 소프트웨어 재사용과 이식성 검증 이후에 강조')
    afoot(s, 'A13')


# ---------------------------------------------------------------- A14 long-term expansion path
def a14(prs):
    s = new_slide(prs, 'A14')
    aheader(s, 'A14', '장기 확장 경로: 단독 구매에서 기본 탑재로', '건설사는 핵심 시장이 아닌 장기 유통·탑재 채널 · 현재 확인된 협업 없음 · 기본 계획 미반영')
    rows = [
        [B_('단독형'), '별도로 구매해 설치하는 주방 로봇 (협동로봇 + SoftHand)', '상업용 주방 · 가정', 'Seed~중기'],
        [B_('가전 연동형'), '오븐·인덕션·냉장고 등 가전과 연동해 작업', '가전 기업 · 스마트홈 플랫폼', '장기'],
        [B_('빌트인형'), '주방 설계 단계부터 로봇 설치 공간·전원·통신을 반영', '건설사 · 디벨로퍼 · 호텔 · 시니어 주거', '장기'],
    ]
    lw = 7.4
    h = table(s, MX, TOP + 0.05, lw, ['단계', '형태', '협력 대상', '시기'], rows, col_w=[1.3, 3.1, 2.0, 1.0], size=11.5, pad=0.09, label='A14 table')
    y = block_title(s, MX, TOP + 0.4 + h, lw, '활용 공간 (장기 가능성)')
    text(s, MX, y, lw, 0.3, '아파트 · 프리미엄 레지던스 · 시니어 주거 · 호텔 · 서비스드 레지던스', size=12.5, label='A14 spaces')
    rx = MX + lw + 0.45; rw = W - MX - rx
    image(s, KIT('lx_wide.jpg'), rx, TOP + 0.1, rw, rw * 0.62, focus=(0.5, 0.5))
    text(s, rx, TOP + 0.18 + rw * 0.62, rw, 0.26, '빌트인 주방 콘셉트 렌더링 (장기 가능성)', size=10, color=T['muted'])
    afoot(s, 'A14', note='관련 네트워크·협의가 있다면 실제 정보로 기재, 없으면 가능성으로만 유지')


# ---------------------------------------------------------------- A15 safety / hygiene / IP
def a15(prs):
    s = new_slide(prs, 'A15')
    aheader(s, 'A15', '안전·위생·인증·지재권', '인증·권리 확보 전에는 적합성·독자성을 주장하지 않음 · 표준은 적용 검토 대상')
    cw3 = (CW - 0.7) / 3
    cols = [('안전 (주방·산업)', ['소프트 핸드를 달아도 셀 전체가 자동으로 안전해지지 않음, 칼·고온·사람 근접을 포함한 통합 위험성 평가',
                                 '상업용 주방·산업 셀: ISO 10218-2:2025 (로봇 응용·셀 안전) 적용 검토',
                                 '가정용: ISO 13482 (개인 돌봄 로봇 안전) 등 적용 검토, 사람 근접 시 속도·힘 제한',
                                 '고온 도구·칼·튀김: 차폐·접근 제한·독립 인터록 충족 전 기능 비활성']),
            ('위생 (주방)', ['식품 접촉 재질: 국내 「기구 및 용기·포장의 기준 및 규격」(식약처), 해외 NSF/ANSI 51 등 판매국 기준을 시험기관과 결정',
                           '교체형 접촉부·외피, 세척·건조 절차, 밀봉 구조', '방수·방진 등급(IP) ≠ 위생 적합성', '가전·설비 안전 인터록은 우회하지 않음']),
            ('지재권·영업비밀 (계획)', ['출원 후보: 대향 엄지·관절 순응과 잠금 구조, 교체형 위생 손끝, 밀봉 구조',
                                    '출원 후보: 사람용 도구 조작을 위한 핸드-작업 소프트웨어 구조, 로봇 독립 작업 표현, 보정 이식 방법',
                                    '영업비밀 후보: 데이터 정제·장력 보정·실패 복구 파라미터',
                                    '원칙: 선행기술 조사·FTO 후 출원, 그 전에는 비침해·독자성 주장 금지'])]
    for i, (t, items) in enumerate(cols):
        x = MX + i * (cw3 + 0.35)
        y = block_title(s, x, TOP + 0.05, cw3, t)
        bullets(s, x, y, cw3, items, size=11.5, gap=6, label='A15 ' + t)
    afoot(s, 'A15', note='현재 확인된 특허 출원 없음 · 예산: 제조·품질·안전·지재권 1.1억 원')


# ---------------------------------------------------------------- A16 risks
def a16(prs):
    s = new_slide(prs, 'A16')
    aheader(s, 'A16', '위험 요인과 대응')
    rows = [
        [B_('순응성과 강성 충돌'), '팬·노브·문 조작 시 처짐·미끄러짐', '골격·잠금 비교시험, 작업 토크별 출시 제한, M6 점검'],
        [B_('위생·세척·열'), '세척 불가·오염 시 주방 도입 불가', '교체형 위생 접촉부·밀봉 구조, 식품 접촉 재질 시험'],
        [B_('속도·처리량'), '사람·전용 장비 대비 느리면 경제성 약화', '반복 보조 작업부터, PoC에서 처리량·가동률 측정'],
        [B_('시장 범위 과대'), '상업용·가정용·산업 동시 추진으로 실행 분산', 'Seed는 검증 대상 6종 작업 집중, 가정용은 벤치 검증'],
        [B_('과도한 맞춤 개발'), '낮은 마진, 확장 불가', '표준 작업 목록, 비표준 요청 별도 견적, 재사용률 지표, M18 점검'],
        [B_('로봇 이식성 실패'), '작업 소프트웨어 재사용 가설 약화', '로봇 독립 작업 표현, 보정 도구, 로봇 2종 검증'],
        [B_('지불의사 부족'), '매출 지연, 1차 고객군 오판', '유료 PoC 선수금, 기존 수치 측정 계약, M12 점검'],
        [B_('안전 (칼·고온·사람 근접)'), '사고·도입 지연', '통합 위험성 평가, 기능 제한, 독립 인터록'],
        [B_('로봇·가전 기업 내재화'), '협력 채널 축소', '로봇 무관 통합, 여러 브랜드용 작업 소프트웨어, 협력 우선'],
        [B_('긴 영업 주기·후속 조달'), '운전자금 부족', '18 + 6개월 집행, 예비비, 시리즈 A 조기 착수 (M15~)'],
        [B_('창업팀 구성 지연'), '일정·실행력 저하', '공동창업자·핵심 2인 합류를 Seed 클로징 조건으로 설정'],
    ]
    table(s, MX, 1.65, CW, ['위험 요인', '사업 영향', '대응'], rows, col_w=[3.1, 3.4, 5.33], size=11.5, pad=0.065, max_h=5.25, label='A16 table')
    afoot(s, 'A16')


# ---------------------------------------------------------------- A17 sources
SOURCES = [
    ('S1', '통계청, 2023년 전국사업체조사 결과 (잠정, 2024-09-27)', 'kostat.go.kr'),
    ('S2', '헤럴드경제, 외식업계 인력난 (2025-05-10)', 'biz.heraldcorp.com'),
    ('S3', 'Restaurant Dive, NRA 2025 labor market·tech', 'restaurantdive.com'),
    ('S4', '서울신문, 부산 학교 급식실 조리 로봇 (2025-12-30)', 'seoul.co.kr'),
    ('S5', '인사이트코리아, 삼성웰스토리 급식 조리로봇', 'insightkorea.co.kr'),
    ('S6', 'AI타임스, 에니아이 햄버거 조리 로봇 (2025)', 'aitimes.com'),
    ('S7', '파이낸셜뉴스, 로보아르테 75억 시리즈A (2022-05-12)', 'fnnews.com'),
    ('S8', 'New Atlas, Moley robotic kitchen (2021)', 'newatlas.com'),
    ('S9', 'The Robot Report, Miso Robotics Flippy', 'therobotreport.com'),
    ('S10', 'AgFunderNews, Chef Robotics $43m Series A (2025)', 'agfundernews.com'),
    ('S11', 'Grand View Research, Food Robotics Market', 'grandviewresearch.com'),
    ('S12', 'The Business Research Company, Food Robotics', 'thebusinessresearchcompany.com'),
    ('S13', 'BCG, How Physical AI Is Reshaping Robotics Today (2026-04)', 'bcg.com'),
    ('S14', 'IFR, World Robotics 2026 · Robot Density (2026)', 'ifr.org'),
    ('S15', 'Tesla 2025년 3분기 실적 발표 녹취 (2025-10-22)', 'fool.com'),
    ('S16', 'NVIDIA, GR00T N1.6 · 레퍼런스 휴머노이드 (2026)', 'nvidia.com'),
    ('S17', 'CNBC, NVIDIA Jetson AGX Thor (2025-08-25)', 'cnbc.com'),
    ('S18', 'Google DeepMind, Gemini Robotics 1.5 (2025-09)', 'deepmind.google'),
    ('S19', 'Figure, Series C · Figure 03 (2025)', 'figure.ai'),
    ('S20', 'Bloomberg, Physical Intelligence 가치 평가 (2025-11)', 'bloomberg.com'),
    ('S21', 'Crunchbase News, Robotics startup funding (2026-06)', 'news.crunchbase.com'),
    ('S22', 'qbrobotics, qb SoftHand Industry', 'qbrobotics.com'),
    ('S23', 'Robotics & Automation News, Tesollo DG-5F-S (2026-03)', 'roboticsandautomationnews.com'),
    ('S24', 'ISO 10218-2:2025 · ISO 13482:2014', 'iso.org'),
]
def a17(prs):
    s = new_slide(prs, 'A17')
    aheader(s, 'A17', '출처', '열람 기준 2026-10-06 · 가격·원가·성능·고객 수·일정·매출은 출처 수치가 아닌 본 계획의 가정 · 전체 URL은 수정 보고서')
    half = (len(SOURCES) + 1) // 2; tw = (CW - 0.35) / 2
    for c in range(2):
        rows = [[(sid, {'bold': True, 'color': T['accent']}), t, (u, {'color': T['text2'], 'size': 8.5})] for sid, t, u in SOURCES[c * half:(c + 1) * half]]
        table(s, MX + c * (tw + 0.35), TOP + 0.02, tw, ['번호', '출처', '도메인'], rows, col_w=[0.5, tw - 0.5 - 1.75, 1.75], size=9.5, pad=0.035,
              max_h=4.85, label=f'A17 table {c}')
    afoot(s, 'A17')


APPX = [a00, a01, a02, a03, a04, a05, a06, a07, a08, a09, a10, a11, a12, a13, a14, a15, a16, a17]
