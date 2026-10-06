# SoftHand Seed IR deck v2 - appendix (light design, 개조식 copy, table-first).
from kit import *
import kit
from slides_main import M, RAW, REN, ORI

APPX_LIST = [
    ('A1', '주요 가정과 근거 수준'), ('A2', '단계별 점검 기준'), ('A3', '경쟁사 상세·로봇 제조사 분석'), ('A4', '피지컬 AI 흐름'),
    ('A5', '시장 근거'), ('A6', '핸드 설계 상세'), ('A7', '성능 지표와 시험 방법'), ('A8', '스크루드라이버 기술 데모'),
    ('A9', '수익 모델 가정'), ('A10', '5개년 손익 상세'), ('A11', '자금 사용 상세'), ('A12', '데이터 축적 계획'),
    ('A13', '주방 데모 범위'), ('A14', '안전·인증·IP'), ('A15', '주요 위험과 대응'), ('A16', '출처'),
]
TOP = 2.0          # content top on appendix slides
BOTTOM = 6.9       # content bottom (footer starts below)


def aheader(s, code, title, sub=None):
    text(s, MX, 0.55, 8, 0.28, f'부록 {code}', size=11, bold=True, color=T['accent'])
    text(s, MX, 0.9, CW, 0.52, title, size=26, bold=True, line=0.95, label='atitle ' + code)
    if sub: text(s, MX, 1.48, CW, 0.3, sub, size=13, color=T['text2'], label='asub ' + code)


def afoot(s, code, note=None):
    footer(s, code, note=note)


def bullets(s, x, y, w, items, size=12, gap=4, label='bullets', color=None):
    hh = text_h(items, size, w - 0.18, space_after=gap)
    text(s, x, y, w, hh + 0.05, items, size=size, bullet='•', indent=0.18, space_after=gap, color=color or T['text2'], label=label)
    return hh


def block_title(s, x, y, w, t, color=None):
    text(s, x, y, w, 0.3, t, size=13, bold=True, color=color or T['text'])
    hline(s, x, y + 0.36, w, color=T['text'], lw=1.0)
    return y + 0.48


# ---------------------------------------------------------------- A0 divider
def a00(prs):
    s = new_slide(prs, 'A0 divider')
    text(s, MX, 0.9, 6, 0.9, '부록', size=40, bold=True)
    text(s, MX, 1.85, 6, 0.6, '본문의 근거와 상세 계획', size=16, color=T['text2'])
    half = (len(APPX_LIST) + 1) // 2
    for col in range(2):
        x = MX + 4.4 + col * 4.0
        y = 0.95
        for code, t in APPX_LIST[col * half:(col + 1) * half]:
            text(s, x, y, 0.65, 0.3, code, size=13, bold=True, color=T['accent'])
            text(s, x + 0.65, y, 3.2, 0.3, t, size=13, label='toc ' + code)
            y += 0.5
            hline(s, x, y - 0.1, 3.6)
    footer(s, 'A')


# ---------------------------------------------------------------- A1 evidence
def a01(prs):
    s = new_slide(prs, 'A1')
    aheader(s, 'A1', '주요 가정과 근거 수준', '확인된 사실, 계획, 가정, 확보가 필요한 자료를 구분해 표기')
    rows = [
        [('확인된 사실', {'bold': True}), '사업 아이디어·기술 구상·IR 초안 (2026.10)\n외부 시장 자료(IFR·BCG) 출처 확인\n법인·창업팀·특허·시제품·고객 계약·매출·보유 자금은 미확인',
         '회사 실적으로 표현하지 않음\n창업·Seed 제안서로 표기'],
        [('계획', {'bold': True}), 'SoftHand-4 V1, 머신텐딩 스킬 팩, 공동개발 고객 3곳, 유료 PoC 5건, 로봇 2종\n고객 인터뷰 30곳, 24개월 로드맵, 단계별 점검 기준',
         '"목표", "계획"으로 표기'],
        [('가정', {'bold': True}), '핸드 1,500만 원 (원가 950만 → 750만 원), 스킬 300만 원, 런타임 연 150만 원\n유료 PoC 5,000만 원, 기본 시나리오 매출·손익, 성능 목표치',
         '"가정", "경영 계획"으로 표기'],
        [('확보 필요 자료', {'bold': True}), '창업자·핵심 인력 이력, 시제품·무편집 시험 영상, 특허·FTO\n고객 인터뷰·LOI·공동개발 고객, 유료 PoC, BOM, 고객 기존 수치, 동일 조건 비교시험',
         '[정보 입력 필요] 표기\n투자 실사 전 확보'],
    ]
    table(s, MX, TOP + 0.05, CW, ['구분', '현재 내용', '표기 원칙'], rows, col_w=[2.0, 6.83, 3.0], size=12, pad=0.09,
          max_h=3.9, label='A1 table')
    footnote(s, '이미지: 모든 SoftHand 이미지는 같은 SoftHand-4 콘셉트 모델(4지·대향 엄지·그라파이트 손바닥·주황 패드·흰색 손목 모듈)로 통일. '
                '실물 확보 시 시제품 사진, 시험 영상, 고객 현장, CAD 순으로 교체')
    afoot(s, 'A1')


# ---------------------------------------------------------------- A2 gates
def a02(prs):
    s = new_slide(prs, 'A2')
    aheader(s, 'A2', '단계별 점검 기준', '실패 조건과 결정을 먼저 정하고 자금을 단계별로 집행')
    rows = [
        [('M6', {'bold': True, 'color': T['accent']}), '기술: 핸드 하나로 대표 공정 수행', '대표 작업 5종 반복 시연\n목표 토크·반복성 기록 공개', '핸드 구조 재검토\n(구동 방식·골격·잠금)', '후속 채용 보류\n시제품 예산 재배분'],
        [('M12', {'bold': True, 'color': T['accent']}), '고객: 전환 비용 개선에 비용 지불', '유료 PoC 1건 이상\n고객 기존 수치 확보, 지불의사 확인', '첫 시장·작업 재정의\n(다른 공정·다른 고객군)', '6개월 연장 자금 집행 재검토'],
        [('M18', {'bold': True, 'color': T['accent']}), '제품: 반복 판매·스킬 재사용', '설계 확정, 첫 재구매\n재사용률 측정 시작, 로봇 B 통합', '플랫폼 가설 재검토\n제품 + 서비스 모델 검토', 'Series A 착수 시점 조정'],
        [('M24', {'bold': True, 'color': T['accent']}), '확장: 재구매·스킬 이식성', '재구매 고객 2곳 이상\n로봇 2종 호환, 매출총이익률 검증', 'Series A 확장 보류\n축소 운영·브리지 검토', 'Series A 규모·시점 결정'],
    ]
    table(s, MX, TOP + 0.05, CW, ['시점', '검증 가설', '통과 기준 (목표)', '미달 시 결정', '자금 영향'], rows,
          col_w=[0.85, 2.85, 3.13, 2.75, 2.25], size=12, pad=0.09, max_h=3.6, label='A2 table')
    by = 5.85
    hline(s, MX, by, CW, color=T['text'], lw=1.0)
    bullets(s, MX, by + 0.15, CW, ['점검은 이사회·투자자와 분기별 지표 리뷰로 판단, 미달 시 범위 축소 또는 방향 전환을 결정한 뒤 다음 단계 자금 집행 (18개월 + 6개월 구조와 연동)',
                                    '시험 결과는 시험 횟수·성공 건수·최초 시도와 재시도 분리·신뢰구간으로 보고, 데모 영상이 아닌 기록으로 판단'], size=12, label='A2 notes')
    afoot(s, 'A2')


# ---------------------------------------------------------------- A3 competition detail
def a03(prs):
    s = new_slide(prs, 'A3')
    aheader(s, 'A3', '경쟁사 상세·로봇 제조사 분석', '공개 정보 기반 정성 비교, 독립 비교시험 아님 (Seed 기간 동일 조건 비교시험으로 검증)')
    rows = [
        [('전통 그리퍼·EOAT', {'bold': True}), '평행·진공·맞춤 EOAT (예: SCHUNK 등)', '정밀·저가·고신뢰', '작업마다 교체, 사람용 장치 조작은 설비 개조'],
        [('적응형 그리퍼', {'bold': True}), 'Robotiq Adaptive Gripper', '다양한 형상 파지, 통합 용이', '문·레버 조작과 공구 토크 제한'],
        [('소프트 핸드', {'bold': True}), 'qb SoftHand Industry (5지·1모터·파워그립 2kg, 제조사 공개)', '형상 적응, 안전한 접촉', '공구 토크·강성 전환 제한'],
        [('다지 로봇 핸드', {'bold': True}), 'Shadow · Allegro · Tesollo DG-5F-S · Sharpa Wave · Tesla·Figure 자체 개발', '고자유도, 복잡한 조작', '비용·복잡도·내구성, 연구·휴머노이드 중심'],
        [('전용 설비', {'bold': True}), '전용 체결 툴, 전용 조리 설비 (예: Moley형 로봇 주방)', '특정 작업 최적', '범용성 없음, 설비 투자 큼'],
        [('SoftHand-4 (목표)', {'bold': True, 'color': T['accent']}), '사람용 장치 조작 + 재사용 스킬', '—', '미검증, Seed 기간 비교시험 대상'],
    ]
    h1 = table(s, MX, TOP - 0.05, CW, ['범주', '대표 사례 (공개 정보)', '강점', '머신텐딩 관점 한계'], rows,
               col_w=[1.85, 4.9, 2.0, 3.08], size=11, pad=0.05, max_h=3.0, label='A3 table')
    oy = TOP - 0.05 + h1 + 0.22
    text(s, MX, oy, CW, 0.3, '로봇 제조사(OEM)가 직접 만든다면', size=13, bold=True)
    table(s, MX, oy + 0.34, CW, None, [
        [('관찰', {'bold': True}), 'Tesla·Figure는 휴머노이드 손 내재화, 다수 산업용·협동로봇 제조사는 EOAT 파트너 생태계 의존, NVIDIA 레퍼런스 휴머노이드(2026.6)도 외부 촉각 핸드 채택'],
        [('해석', {'bold': True}), '로봇 제조사는 경쟁자이자 판매 채널, 단일 제조사는 여러 브랜드에서 쓰는 스킬을 만들기 어려움'],
        [('대응', {'bold': True}), '로봇 무관 통합, 로봇 2종 이식성 검증, OEM 파트너십 우선 (확장 계기 = OEM 채택)'],
    ], col_w=[0.8, CW - 0.8], size=11, pad=0.05, max_h=1.2, label='A3 oem')
    afoot(s, 'A3', note='출처: 제조사 공개 사양·보도자료 (A16: S5·S13·S14·S15) · 회사명은 범주 예시이며 성능 우열을 주장하지 않음')


# ---------------------------------------------------------------- A4 physical AI
def a04(prs):
    s = new_slide(prs, 'A4')
    aheader(s, 'A4', '피지컬 AI 흐름: 두뇌·눈·몸은 상용화, 남은 병목은 손', '본문 08 "왜 지금인가"의 근거, 각 수치는 출처 발표 기준이며 독립 검증 아님')
    rows = [
        [('두뇌 · AI·VLA', {'bold': True}), '빠르게 발전', 'Gemini Robotics 1.5 (2025.9) · NVIDIA Isaac GR00T N1.6 (2026.1) · Physical Intelligence 기업가치 56억 달러 (2025.11)'],
        [('눈 · 비전·엣지', {'bold': True}), '상용 수준', 'NVIDIA Jetson AGX Thor: 2,070 FP4 TFLOPS, 이전 세대 대비 AI 연산 7.5배 (2025.8)'],
        [('몸 · 로봇 팔·휴머노이드', {'bold': True}), '대규모 보급', '산업용 로봇 가동 약 500만 대, 연 60만 대 이상 설치 (IFR, 2026.9) · Figure 기업가치 390억 달러 (2025.9)'],
        [('손 · 현실 세계 조작', {'bold': True, 'color': T['accent']}), ('아직 병목', {'bold': True, 'color': T['accent']}),
         '"The forearm and hand are more difficult than the entire rest of the robot." Elon Musk, Tesla 2025년 3분기 실적 발표 (2025.10)\n'
         'NVIDIA 레퍼런스 휴머노이드(2026.6) 외부 촉각 핸드 채택 · Figure 03 촉각 손끝 (3g 감지, 2025.10)'],
        [('자본 유입', {'bold': True}), '—', '로보틱스 스타트업 투자 2025년 150억 달러 (사상 최대), 2026년 상반기 188억 달러 (Crunchbase News, 2026.6)'],
    ]
    table(s, MX, TOP + 0.05, CW, ['단계', '상태', '근거 (출처·시점)'], rows, col_w=[2.6, 1.45, 7.78], size=12, pad=0.09, max_h=3.9, label='A4 table')
    footnote(s, '해석: 두뇌·눈·몸이 상용화되면서 사람용 설비를 다루는 조작 계층이 병목. 장기 비전의 근거이며, 회사의 첫 매출 근거는 기존 설비의 자동화 전환 비용 (본문 03)')
    afoot(s, 'A4', note='출처: A16 S4~S11')


# ---------------------------------------------------------------- A5 market evidence
def a05(prs):
    s = new_slide(prs, 'A5')
    aheader(s, 'A5', '시장 근거', '첫 시장은 설치 기반, 장기 상한은 로봇 제조사 출하량 (OEM 매출은 계산하지 않음)')
    text(s, MX, TOP + 0.05, 4.6, 0.3, '연간 산업용 로봇 신규 설치 (천 대, IFR)', size=12, bold=True, color=T['muted'])
    column_chart(s, MX, TOP + 0.45, 4.6, 3.1, ['2024', '2025', '2026F', '2029F'], [('설치', [542, 603, 655, 806])], [T['grey_bar']],
                 stacked=False, vmax=950, fmt='0', gap=60, plot=(0.03, 0.1, 0.94, 0.78), size=12)
    text(s, MX, TOP + 3.85, 4.6, 0.6, '가동 중 산업용 로봇 약 500만 대 (2025년 말)\n한국 로봇 밀도 1,220대 / 직원 1만 명 (세계 1위)', size=12, color=T['text2'], label='A5 cap')
    rx = MX + 5.1; rw = W - MX - rx
    rows = [
        [('첫 시장', {'bold': True}), '국내 다품종 머신텐딩\n(로봇 SI·제조사)', '국내 연 약 3만 대 설치\n로봇 밀도 세계 1위', '구매의향 미검증\n고객 인터뷰 30곳'],
        [('확장', {'bold': True}), '글로벌 산업용·협동로봇 설치 기반', '가동 약 500만 대\n2025년 60만 대+ (+11%)\n2029F 80.6만 대', '기존 설비 개조 수요'],
        [('상한', {'bold': True}), '로봇 제조사 출하량\n휴머노이드·피지컬 AI', 'OEM 채택 시 출하량 연동 (본문 10 공식)\n휴머노이드 전망은 기관별 편차 큼', '매출 수치 미산정'],
    ]
    table(s, rx, TOP + 0.05, rw, ['단계', '정의', '규모 근거', '성격'], rows, col_w=[0.85, 1.95, 2.35, rw - 5.15], size=11.5, pad=0.08,
          max_h=3.6, label='A5 table')
    footnote(s, 'EOAT 시장 추정치는 조사기관별 편차가 커 시장 규모 근거로 사용하지 않음 · 휴머노이드 전망 예: Goldman Sachs 2035년 648만 대 (2026.8, Investing.com 보도)')
    afoot(s, 'A5', note='출처: IFR World Robotics 2026 (2026.9), IFR 로봇 밀도 (2026.4)')


# ---------------------------------------------------------------- A6 hand engineering
def a06(prs):
    s = new_slide(prs, 'A6')
    aheader(s, 'A6', '핸드 설계 상세: 구동·하중·센싱', '구동 방식은 미확정, 창업 후 3개월 내 비교시험으로 선정 (M6 점검과 연동)')
    lw = 7.9
    rows = [
        [('구성 (4지)', {'bold': True}), '손가락 3 + 대향 엄지, 문·집기·레버·버튼 수행 최소 구성', '5지 대비 부품 수·비용·내구성·제어 복잡도 (5지는 Series A 이후)'],
        [('구동부', {'bold': True}), '전동 텐던을 기준 후보로 소형 유압·공압과 비교', '손 무게·유지력·응답·누설·소음·소비전력·정비비'],
        [('가변 순응성', {'bold': True}), '탄성 요소·장력 제어, 필요 시 잠금 기구', '접촉 충격 완화와 조작 토크 유지의 균형'],
        [('감각부', {'bold': True}), '손끝·손바닥 접촉센서, 관절·장력 센서, 손목 6축 힘·토크 센서', '절삭유·분진·오염 조건 편차와 재교정'],
        [('접촉부', {'bold': True}), '교체형 패드·외피, 용도별 재질 분리 (제조: 내마모·내유, 주방: 세척·내열)', '미끄럼·마모·세척·재질 적합성 시험'],
        [('로봇 장착', {'bold': True}), '공통 손목 모듈·플랜지 어댑터·TCP 보정·통신 드라이버', '로봇 2종 실제 통합, 이식성 측정'],
    ]
    table(s, MX, TOP + 0.05, lw, ['기술 요소', '개발 내용', '검증 기준'], rows, col_w=[1.4, 3.45, 3.05], size=11.5, pad=0.08, max_h=4.6, label='A6 table')
    rx = MX + lw + 0.45; rw = W - MX - rx
    y = block_title(s, rx, TOP + 0.05, rw, '하중 설계 예시 (머신텐딩)')
    y += bullets(s, rx, y, rw, ['소재 1.5kg, 파지점에서 무게중심 0.10m', '정적 모멘트 약 1.5 N·m (가속·충격 시 증가)', '문 개방력·레버 조작 토크는 설비별 기존 수치 측정 후 사양 확정',
                               '손의 파지 하중 ≠ 로봇 팔 가반하중 (손·어댑터·소재 합산)'], size=11.5, label='A6 load') + 0.3
    y = block_title(s, rx, y, rw, '제어 구조')
    bullets(s, rx, y, rw, ['비전: 형상·장치 위치·배치 상태', '촉각: 접촉·미끄러짐', '손목 힘센서: 반력·토크', 'VLA·모방학습은 상위 작업 선택에 활용, 힘·속도·안전 한계는 독립 제어 계층에서 보장'],
            size=11.5, label='A6 ctrl')
    afoot(s, 'A6', note='공통 제어기·통신·손목 모듈은 유지하고 접촉부만 용도별로 분리')


# ---------------------------------------------------------------- A7 performance
def a07(prs):
    s = new_slide(prs, 'A7')
    aheader(s, 'A7', '성능 지표와 시험 방법', '파지 성공률이 아닌 작업 완료 기준 · 모든 수치는 목표이며 실적 아님')
    rows = [
        [('대표 공정 완료율 (6단계)', {'bold': True}), '단계별 반복 시연', '승인 작업 95% 이상', '최초 시도·재시도·중단 분리 보고, 신뢰구간'],
        [('소재 집기·투입 (등록 소재)', {'bold': True}), '10종, 95% 이상', '20종, 98% 이상', '종별 100회, 낙하 없이 투입 완료'],
        [('문·레버·버튼 조작', {'bold': True}), '대표 설비 2종', '설비 4종, 완료율 95% 이상', '조작력·작업 시간 함께 보고'],
        [('핸드 하중', {'bold': True}), '원통 소재 1kg', '동일 조건 2kg', '자세·속도·모멘트 한계 명시'],
        [('내구성', {'bold': True}), '반복 개폐 10만 회', '30만 회 (양산 목표 100만 회)', '하중·패드 교체 주기·힘 저하율 명시'],
        [('스킬 이식성', {'bold': True}), '로봇 A 기준 기록', '로봇 B 재사용 검증', '추가 엔지니어링 시간·완료율·재사용 모듈 비중'],
        [('재사용률', {'bold': True}), '측정 체계 수립', 'M12부터 측정, 상승 추세', '신규 고객 적용 시 그대로 쓴 모듈 비중'],
        [('사람 개입·전환 시간', {'bold': True}), '공정별 고객 기존 수치 확보', '기존 수치 대비 감소 (PoC 측정)', '재료 보충·복구 포함, 임의 목표치 없음'],
        [('연구 트랙 (점검 제외)', {'bold': True, 'color': T['muted']}), '스크루드라이버 저토크 체결 데모', '유연체·주방 벤치 데모', 'Seed 성공 조건이 아닌 기술 트랙'],
    ]
    table(s, MX, TOP + 0.05, CW, ['지표', '12개월 목표', '24개월 목표', '시험 정의'], rows, col_w=[2.85, 2.55, 2.85, 3.58], size=11.5, pad=0.065,
          max_h=4.4, label='A7 table')
    afoot(s, 'A7', note='시험 횟수·성공 건수·신뢰구간 공개, 편집 없는 시험 영상 제공 · 감소율 목표는 고객 기존 수치 확보 후 설정')


# ---------------------------------------------------------------- A8 screwdriver
def a08(prs):
    s = new_slide(prs, 'A8')
    aheader(s, 'A8', '스크루드라이버 기술 데모', '시각적으로 좋은 작업이지만 핵심 상용 작업은 아님, 기술 트랙으로 분리')
    rect(s, MX, TOP + 0.05, 5.2, 4.4, fill='EEF0F2')
    cutout(s, REN('screwdriver.png'), MX + 0.2, TOP + 0.25, 4.8, 4.0)
    text(s, MX, TOP + 4.55, 5.2, 0.25, '저토크 체결 데모 · 콘셉트 렌더링', size=10, color=T['muted'])
    rx = MX + 5.7; rw = W - MX - rx
    y = block_title(s, rx, TOP + 0.05, rw, '이 데모로 확인하는 것')
    y += bullets(s, rx, y, rw, ['공구 토크 전달 (일할 때는 단단하게)', '대향 엄지 파지 안정성', '작업 순간 강성 전환 (검증 예정)'], size=12.5, label='A8 a') + 0.3
    y = block_title(s, rx, y, rw, '핵심 상용 작업이 아닌 이유')
    y += bullets(s, rx, y, rw, ['로봇 손목에 전용 전동 드라이버를 다는 편이 더 싸고 빠르고 정밀', '핸드로 얻는 설비·엔드이펙터 절감 효과가 작음'], size=12.5, label='A8 b') + 0.3
    y = block_title(s, rx, y, rw, '의미가 생기는 경우')
    bullets(s, rx, y, rw, ['한 셀에서 체결이 가끔만 필요해 툴 체인저 추가가 과한 경우', '사람용 공구를 그대로 써야 하는 서비스·주방 환경 (집게 등은 주방 벤치 데모)'], size=12.5, label='A8 c')
    afoot(s, 'A8')


# ---------------------------------------------------------------- A9 revenue model assumptions
def a09(prs):
    s = new_slide(prs, 'A9')
    aheader(s, 'A9', '수익 모델 가정', '모든 가격·원가·마진은 검증 전 가정')
    rows = [
        [('초기 (Seed)', {'bold': True}), '유료 PoC', '건당 5,000만 원 (8~12주, 대여 핸드 포함)', '40%', '지불의사 검증·고객 기존 수치 확보'],
        [('초기', {'bold': True}), '통합 엔지니어링', '프로젝트당 4,000만 원', '40%', '진입 수단, 비중 축소 목표'],
        [('초기~중기', {'bold': True}), 'SoftHand 하드웨어', '핸드 패키지 1,500만 원 (직판)\n1,200만 원 (SI 파트너 순매출)', '원가 950만 → 750만 원', 'BOM·공급사 확정 후 재산정 (M18)'],
        [('초기~중기', {'bold': True}), '작업 스킬 패키지', '핸드당 300만 원 (파트너 240만 원)\n핸드당 1.0 → 1.6개', '85%', '승인 작업 단위 판매'],
        [('중기', {'bold': True}), '런타임·유지보수', '설치 핸드당 연 150만 원', '70%', '설치 기반 반복 매출'],
        [('장기', {'bold': True}), 'OEM 라이선스·내장 런타임·로열티', '출하량 연동 [OEM 협의 후 검증]', '—', '기본 시나리오 미반영 (확장 계기)'],
    ]
    table(s, MX, TOP + 0.05, CW, ['단계', '매출원', '과금 단위·가정 가격', '매출총이익률 가정', '역할'], rows,
          col_w=[1.35, 2.55, 3.6, 1.95, 2.38], size=12, pad=0.085, max_h=4.0, label='A9 table')
    footnote(s, '통합 매출은 숨기지 않되 장기 모델이 아닌 진입·제품화 수단으로 정의 · 주방 셀 판매는 기본 시나리오에서 제외 · 확정 표현이던 "스킬 연간 구독·소프트웨어 마진 70%"는 단계별 가정으로 전환')
    afoot(s, 'A9')


# ---------------------------------------------------------------- A10 P&L detail
def a10(prs):
    s = new_slide(prs, 'A10')
    B = M['base']; A = M['assumptions']
    aheader(s, 'A10', '5개년 손익 상세 (기본 시나리오)', '단위: 억 원 · 1년차 = 투자 집행 첫해 · 주방·OEM 매출 0원 (상승 요인으로 분리)')
    f = lambda v: f'{v:.1f}'.replace('-', '−')
    inst = []
    tot = 0
    for d, p in zip(A['hand_direct'], A['hand_partner']): tot += d + p; inst.append(str(tot))
    rows = [
        ['유료 PoC / 통합 (건)'] + [f'{a} / {b}' for a, b in zip(A['poc_n'], A['int_n'])],
        ['신규 핸드 (대) 직판 / 파트너'] + [f'{a} / {b}' for a, b in zip(A['hand_direct'], A['hand_partner'])],
        ['설치 핸드 누적 (대)'] + inst,
        ['매출: 유료 PoC·통합'] + [f(v) for v in B['poc_int']],
        ['매출: SoftHand 하드웨어'] + [f(v) for v in B['hw']],
        ['매출: 작업 스킬'] + [f(v) for v in B['skill']],
        ['매출: 런타임·유지보수'] + [f(v) for v in B['runtime']],
        ['매출: 파트너 판매 (하드웨어+스킬)'] + [f(v) for v in B['partner']],
        [('총매출', {'bold': True})] + [(f(v), {'bold': True}) for v in B['rev']],
        ['매출총이익 (이익률)'] + [f'{f(g)} ({m * 100:.0f}%)' for g, m in zip(B['gp'], B['gm'])],
        ['운영비'] + [f(v) for v in B['opex']],
        [('영업손익', {'bold': True})] + [(f(v), {'bold': True}) for v in B['op']],
        [('재사용 매출 비중', {'bold': True})] + [(f'{v * 100:.0f}%', {'bold': True, 'color': T['accent']}) for v in B['reuse_share']],
    ]
    lw = 7.75
    table(s, MX, TOP + 0.02, lw, ['항목', '1년', '2년', '3년', '4년', '5년'], rows, col_w=[2.75] + [1.0] * 5, size=11,
          align=['l', 'r', 'r', 'r', 'r', 'r'], pad=0.045, max_h=4.85, label='A10 table')
    rx = MX + lw + 0.45; rw = W - MX - rx
    y = block_title(s, rx, TOP + 0.02, rw, '민감도 (5년차)')
    h1 = table(s, rx, y, rw, None, [[('판매량 −30% (3~5년차)', {'bold': True}), '매출 31.4억\n영업손익 −7.1억'],
                                    [('핸드 원가 절감 지연', {'bold': True}), '영업손익 −3.1억'],
                                    [('SI 파트너 채널 1년 지연', {'bold': True}), '매출 32.3억\n영업손익 −6.4억'],
                                    [('판매량 −50%', {'bold': True}), '매출 22.4억\n영업손익 −11.9억']],
               col_w=[2.05, rw - 2.05], size=11, pad=0.06, label='A10 sens')
    y = block_title(s, rx, y + h1 + 0.25, rw, '산정 기준')
    bullets(s, rx, y, rw, ['운영비 1·2년차 = Seed 24개월 집행 계획 (A11)', '3~5년차 = 평균 인원 14·19·23명 × 1인 연 0.72~0.76억 + 비인건비 4.5~6.2억',
                           '매출원가 = PoC·통합 60%, 핸드 원가, 스킬 15%, 런타임 30%', '미반영 상승 요인: 주방 파트너 공동 제품화, OEM 채택'], size=11, label='A10 basis')
    afoot(s, 'A10')


# ---------------------------------------------------------------- A11 use of funds detail
def a11(prs):
    s = new_slide(prs, 'A11')
    SP = M['seed']
    aheader(s, 'A11', 'Seed 20억 원 집행 계획과 손익 연결', '18개월 핵심 운영 + 6개월 연장 · 정부지원금·공동개발비 미반영')
    roles = {'대표 · 사업/제품 (Founder)': '대표 · 사업/제품', 'CTO · Hand 메카트로닉스 (Co-founder)': 'CTO · 핸드 메카트로닉스', '기구·구동 엔지니어': '기구·구동 엔지니어',
             '제어·임베디드 엔지니어': '제어·임베디드 엔지니어', 'Robot SW · Skill 엔지니어': '로봇 SW·스킬 엔지니어', '현장 통합(FAE) 엔지니어': '현장 통합 엔지니어',
             'Vision · 조작 AI 엔지니어': '비전·조작 AI 엔지니어', 'DFM · 품질 엔지니어': '설계·품질 엔지니어'}
    hr = []; tot = 0
    for role, start, mc in M['hires']:
        c = mc * (24 - start + 1); tot += c
        hr.append([roles.get(role, role), f'M{start}', f'{c:.2f}억'])
    hr.append([('합계 · 8명', {'bold': True}), '', (f'{tot:.1f}억', {'bold': True})])
    lw = 5.2
    text(s, MX, TOP + 0.02, lw, 0.3, '핵심 인력 채용 계획', size=13, bold=True)
    h1 = table(s, MX, TOP + 0.4, lw, ['역할', '합류', '24개월 인건비'], hr, col_w=[2.75, 0.9, 1.55], size=11, align=['l', 'c', 'r'], pad=0.05,
               max_h=3.6, label='A11 hires')
    text(s, MX, TOP + 0.5 + h1, lw, 0.5, '창업자 연 5,000만 원, 엔지니어 연 7,000만 원 + 4대보험·퇴직충당 15%', size=10.5, color=T['muted'], label='A11 basis')
    rx = MX + lw + 0.5; rw = W - MX - rx
    names = {'핵심 인력 (8명 단계 채용)': '핵심 인력 8명', 'Prototype · 내구시험': '시제품·내구시험', 'Robot 2종 · 시험 Cell': '로봇 2종·시험 셀',
             '고객 PoC · 현장통합(비청구)': '고객 PoC·현장 통합 (비청구)', 'SW · AI · Data': 'SW·AI·데이터', '제조 · 품질 · 안전 · IP': '제조·품질·안전·IP',
             'Kitchen Bench Demo': '주방 벤치 데모', '운영 (임차·법무·회계·보험·출장)': '운영 (임차·법무·회계·보험·출장)', '예비비 · 운전자본': '예비비·운전자본'}
    rows = [[names.get(k, k), f'{v:.1f}억', f'{v / 20 * 100:.0f}%'] for k, v in SP['uof']]
    rows.append([('합계', {'bold': True}), (f'{SP["uof_total"]:.1f}억', {'bold': True}), ('100%', {'bold': True})])
    text(s, rx, TOP + 0.02, rw, 0.3, '자금 사용 계획', size=13, bold=True)
    h2 = table(s, rx, TOP + 0.4, rw, ['항목', '금액', '비중'], rows, col_w=[rw - 2.2, 1.2, 1.0], size=11, align=['l', 'r', 'r'], pad=0.045,
               max_h=3.6, label='A11 uof')
    opex = SP['opex_y1'] + SP['opex_y2']
    text(s, rx, TOP + 0.55 + h2, rw, 0.8,
         [[('손익 연결  ', {'bold': True, 'color': T['text']}), (f'운영비(예비비 제외) 1년차 {SP["opex_y1"]:.1f}억 + 2년차 {SP["opex_y2"]:.1f}억 = {opex:.1f}억', {})],
          [('집행 구조  ', {'bold': True, 'color': T['text']}), (f'18개월 핵심 운영 {SP["core18"]:.1f}억 + 6개월 연장 {SP["ext6"]:.1f}억 + 예비비 {SP["uof"][-1][1]:.1f}억', {})]],
         size=11, color=T['text2'], space_after=3, label='A11 link')
    afoot(s, 'A11', note='기존 "개발 인력 9.0억"은 같은 채용 범위에서 과소 추정 → 9.6억으로 재산정')


# ---------------------------------------------------------------- A12 data
def a12(prs):
    s = new_slide(prs, 'A12')
    aheader(s, 'A12', '데이터 축적 계획', '현재 보유 데이터 없음 · 제품화 구조(본문 09)가 먼저, 데이터는 그 위에 쌓이는 보조 경쟁력')
    steps = ['더 많은 배치', '더 많은 실제 작업', '실패·복구 데이터', '더 나은 스킬', '더 높은 완료율']
    sw = CW / 5; y = TOP + 0.15
    hline(s, MX, y + 0.05, CW, color=T['text'], lw=1.25)
    for i, st in enumerate(steps):
        x = MX + i * sw
        dot(s, x + 0.05, y + 0.05, d=0.12, fill=T['accent'] if i == 2 else T['text'])
        text(s, x, y + 0.22, sw - 0.2, 0.3, st, size=14, bold=True, color=T['accent'] if i == 2 else T['text'], label='d ' + st)
    cy = y + 0.95; cw3 = (CW - 0.6) / 3
    cols = [('Seed 데이터 계획 (목표)', ['도구·부품·설비 장치 30종 이상', '시도 1만 회 이상, 시간 동기화', '실패 원인 라벨링·복구 기록', '물체·세션·현장 단위 분리 검증']),
            ('데이터 권리', ['고객 데이터의 수집·학습·재사용 범위를 계약으로 분리 합의', '고객 고유 공정 정보는 고객 자산으로 보호', '스킬 개선용 일반화 데이터만 회사 자산']),
            ('함께 쌓이는 역량', ['소프트-리지드 하이브리드, 교체형 접촉부, 강성 전환', '힘·미끄러짐 기반 장치 조작 제어', 'SI 현장 통합·PoC 운영 경험'])]
    for i, (t, items) in enumerate(cols):
        x = MX + i * (cw3 + 0.3)
        yy = block_title(s, x, cy, cw3, t)
        bullets(s, x, yy, cw3, items, size=12, label='A12 ' + t)
    footnote(s, '목표는 성공 영상이 아닌 "어떤 상황에서 실패했고 어떻게 복구했는가"의 축적 · 데이터 경쟁력은 제품화 구조와 스킬 이식성 검증 이후에 강조')
    afoot(s, 'A12')


# ---------------------------------------------------------------- A13 kitchen
def a13(prs):
    s = new_slide(prs, 'A13')
    aheader(s, 'A13', '주방 데모 범위', '주방은 첫 매출 시장이 아닌 기술 확장성 데모 · 기본 시나리오 매출 0원')
    lw = 6.9
    rows = [
        [('형태', {'bold': True}), '단일 팔·벤치 규모 데모', '천장 레일·양팔 풀 키친'],
        [('대표 작업', {'bold': True}), '손잡이·집게·팬·접시', '재료 투입·세척·가열·배식·수납'],
        [('하드웨어', {'bold': True}), '기존 로봇 활용 (추가 구매 없음)', '로봇 팔 대여·파트너 하드웨어·공동개발 전제'],
        [('예산', {'bold': True}), '0.3억 원 (기존 0.5억에서 축소)', '파트너 확보 후 별도 산정'],
        [('전제 조건', {'bold': True}), '없음', '실제 파트너·공동개발 계약 (현재 미확보)'],
    ]
    h1 = table(s, MX, TOP + 0.05, lw, ['구분', 'Seed (M18~M24)', 'Series A 이후 (미래 비전)'], rows, col_w=[1.25, 2.6, 3.05], size=11.5, pad=0.07,
               max_h=2.6, label='A13 table')
    y = block_title(s, MX, TOP + h1 + 0.35, lw, '고객 경제성 예시 (가정)')
    bullets(s, MX, y, lw, ['셀 투자 2억 원, 인건비 시간당 2.5만 원, 연 300일, 추가 운영비 연 1,000만 원',
                           '하루 6시간 절감: 연 순절감 3,500만 원, 단순 회수 약 5.7년',
                           '하루 10시간 절감: 연 순절감 6,500만 원, 단순 회수 약 3.1년',
                           '회수기간이 가동률에 민감, 초기 매출원으로 두지 않음 (금융·세금·잔존가치 제외)'], size=11.5, label='A13 roi')
    rx = MX + lw + 0.45; rw = W - MX - rx
    image(s, ORI('hero05_ceiling_dual_arm_kitchen.png'), rx, TOP + 0.05, rw, rw * 9 / 16, focus=(0.5, 0.5))
    text(s, rx, TOP + 0.15 + rw * 9 / 16, rw, 0.45, '미래 비전 · 콘셉트 렌더링\n천장형 양팔 주방은 Series A 이후, 실제 파트너 확보 후 진행', size=10.5, color=T['muted'], label='A13 cap')
    yy = block_title(s, rx, TOP + 0.75 + rw * 9 / 16, rw, '하중·안전')
    bullets(s, rx, yy, rw, ['3kg 냄비, 무게중심 0.20m: 정적 모멘트 약 5.9 N·m, 큰 냄비는 양손·거치대 보조',
                            '고온 도구·칼·튀김: 차폐·접근 제한·독립 인터록 충족 전 기능 비활성'], size=11.5, label='A13 safety')
    afoot(s, 'A13')


# ---------------------------------------------------------------- A14 safety / IP
def a14(prs):
    s = new_slide(prs, 'A14')
    aheader(s, 'A14', '안전·인증·IP', '인증·권리 확보 전에는 적합성·독자성·세계 최초를 주장하지 않음')
    cw2 = (CW - 0.6) / 2
    y = block_title(s, MX, TOP + 0.05, cw2, '안전 (머신텐딩 셀)')
    bullets(s, MX, y, cw2, ['소프트 핸드를 달아도 셀 전체가 자동으로 안전해지지 않음, 설비·공구·소재·이동 범위를 포함한 통합 위험성 평가',
                            '적용 검토: ISO 10218-2:2025 (산업용 로봇 응용·로봇 셀 안전)',
                            '로봇이 설비 문을 열어도 설비 안전 인터록은 우회하지 않음, 사람 작업자와 같은 조건으로 운전',
                            '절삭유·분진 환경의 접촉부 재질·센서 신뢰성 별도 검증',
                            '주방 확장 시 식품 접촉·세척·내열 요구는 판매국별 시험기관과 결정 (IP 등급 ≠ 위생 적합성)'], size=12, gap=6, label='A14 safety')
    x2 = MX + cw2 + 0.6
    y = block_title(s, x2, TOP + 0.05, cw2, 'IP·영업비밀 (계획)')
    bullets(s, x2, y, cw2, ['출원 후보: 대향 엄지·관절 순응과 잠금 구조·교체형 손끝·밀봉 구조',
                            '출원 후보: 사람용 장치 조작을 위한 핸드-스킬 구조, 로봇 독립 작업 스킬 표현, 보정 이식 방법',
                            '영업비밀 후보: 데이터 정제·장력 보정·실패 복구 파라미터',
                            '원칙: 선행기술 조사·권리범위 검토(FTO) 후 출원, 그 전에는 비침해·독자성 주장 금지',
                            '오픈소스 모델·라이브러리 상업 이용 조건 출시 전 확인'], size=12, gap=6, label='A14 ip')
    afoot(s, 'A14', note='현재 특허 출원 없음 · 예산: 제조·품질·안전·IP 1.1억 원')


# ---------------------------------------------------------------- A15 risks
def a15(prs):
    s = new_slide(prs, 'A15')
    aheader(s, 'A15', '주요 위험과 대응')
    rows = [
        [('순응성과 강성 충돌', {'bold': True}), '레버·문 조작 시 처짐·미끄러짐', '골격·잠금 비교시험, 작업 토크별 출시 제한, M6 점검'],
        [('과도한 맞춤 개발 (SI화)', {'bold': True}), '낮은 마진, 확장 불가', '승인 작업 목록, 비표준 요청 별도 견적, 재사용률 지표, M18 점검'],
        [('스킬 이식성 실패', {'bold': True}), '플랫폼 가설 약화', '로봇 독립 작업 표현, 보정 도구, 로봇 2종 검증'],
        [('지불의사 부족', {'bold': True}), '매출 지연, 첫 시장 오판', '유료 PoC 선수금, 기존 수치 측정 계약, M12 점검'],
        [('긴 영업 주기·후속 조달', {'bold': True}), '운전자금 부족', '18 + 6개월 집행, 예비비, Series A 조기 착수 (M15~)'],
        [('설비 안전·인터록', {'bold': True}), '도입 지연', '통합 위험성 평가, 설비 인터록 유지, ISO 10218-2 검토'],
        [('로봇 제조사 내재화', {'bold': True}), 'OEM 채널 축소', '로봇 무관 통합, 여러 브랜드용 스킬, OEM 파트너십 우선'],
        [('창업팀 구성 지연', {'bold': True}), '일정·실행력 저하', '공동창업자·핵심 2인 합류를 Seed 클로징 조건으로 설정'],
        [('접촉부 마모·오염', {'bold': True}), '유지비 증가', '교체형 패드, 교체 주기 명시, 내구시험 (30만 회 목표)'],
    ]
    table(s, MX, 1.65, CW, ['주요 위험', '사업 영향', '대응·판정'], rows, col_w=[3.1, 3.2, 5.53], size=12, pad=0.08, max_h=5.2, label='A15 table')
    afoot(s, 'A15')


# ---------------------------------------------------------------- A16 sources
SOURCES = [
    ('S1', 'IFR, World Robotics 2026 보도자료 (2026-09-24)', 'ifr.org/ifr-press-releases/news/five-million-robots-now-operate-in-factories-globally'),
    ('S2', 'IFR, Robot Density: 한국 1,220대 / 직원 1만 명 (2026-04-08)', 'ifr.org (press release)'),
    ('S3', 'BCG, How Physical AI Is Reshaping Robotics Today (2026-04)', 'bcg.com/publications/2026/how-physical-ai-is-reshaping-robotics-today'),
    ('S4', 'Tesla 2025년 3분기 실적 발표 녹취, The Motley Fool (2025-10-22)', 'fool.com/earnings/call-transcripts/2025/10/22/tesla-tsla-q3-2025-earnings-call-transcript/'),
    ('S5', 'NVIDIA, Isaac GR00T Reference Humanoid Robot 발표 (2026-06-01)', 'investor.nvidia.com'),
    ('S6', 'NVIDIA, CES 2026 Physical AI 모델 발표, GR00T N1.6 (2026-01-05)', 'nvidianews.nvidia.com'),
    ('S7', 'CNBC, NVIDIA Jetson AGX Thor 출시 (2025-08-25)', 'cnbc.com/2025/08/25/nvidias-thor-t5000-robot-brain-chip.html'),
    ('S8', 'Google DeepMind, Gemini Robotics 1.5 (2025-09)', 'deepmind.google/blog/gemini-robotics-15-brings-ai-agents-into-the-physical-world/'),
    ('S9', 'Figure, Series C (2025-09) · Figure 03 공개 (2025-10-09)', 'figure.ai/news'),
    ('S10', 'Bloomberg, Physical Intelligence $5.6B 가치 평가 (2025-11-20)', 'bloomberg.com'),
    ('S11', 'Crunchbase News, Robotics startup funding record (2026-06-22)', 'news.crunchbase.com/robotics/startup-venture-funding-surges-2026-data/'),
    ('S12', 'Investing.com, Goldman Sachs 휴머노이드 전망 (2026-08-31)', 'investing.com'),
    ('S13', 'qbrobotics, qb SoftHand Industry 제품 사양 (제조사 공개)', 'qbrobotics.com/product/qb-softhand-industry/'),
    ('S14', 'Robotics & Automation News, Tesollo DG-5F-S (2026-03-13)', 'roboticsandautomationnews.com'),
    ('S15', 'Moley Robotics, A-AiR kitchen (공급사 소개)', 'moley.com/a-air-kitchen/'),
    ('S16', 'ISO 10218-2:2025, Industrial robot applications and robot cells', 'iso.org/standard/73934.html'),
]
def a16(prs):
    s = new_slide(prs, 'A16')
    aheader(s, 'A16', '출처', '열람 기준 2026-10-06 · 가격·원가·성능·고객 수·일정·매출은 출처 수치가 아닌 본 계획의 가정')
    rows = [[(sid, {'bold': True, 'color': T['accent']}), t, (u, {'color': T['text2'], 'size': 9.5})] for sid, t, u in SOURCES]
    table(s, MX, TOP + 0.02, CW, ['번호', '출처', '링크'], rows, col_w=[0.6, 5.15, 6.08], size=10, pad=0.035, max_h=4.85, label='A16 table')
    afoot(s, 'A16')


APPX = [a00, a01, a02, a03, a04, a05, a06, a07, a08, a09, a10, a11, a12, a13, a14, a15, a16]
