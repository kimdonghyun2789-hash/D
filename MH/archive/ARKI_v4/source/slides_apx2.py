# Appendix v2: v1 main + appendix slides kept in full and re-coded A~F (common.APX mode), plus new slides:
# index, B5 reference-geometry review, B6~B8 84㎡ 2/3/4Bay concept-model detail.
from common import *
import os, json
from common import M
import common
import slides_legacy as L
import slides_appx as AX
import slides_main as SM

TG = ttxt

# ---------------------------------------------------------------- index
INDEX = [
    ('A', '투자 판단 요약', [('A1', '투자 판단 6개 질문과 현재 답'), ('A2', '투자 근거: 현재 vs 계획'), ('A3', '투자 전제 7가지'),
                             ('A4', '투자 평가표 · 판단 (WATCH)')]),
    ('B', '제품 · 표준화', [('B1', '기존 로봇 추가형 vs Robot-ready 비교'), ('B2', 'ARKI 주방 시스템 구성'), ('B3', 'V1 설거지 정리 상세'),
                            ('B4', '배치 기준 · 설치 방식'), ('B5', '받은 평면 5종 · 진행 상태'),
                            ('B6', '구축 2Bay A: 원래 평면 → ARKI 적용'), ('B7', '콘셉트 배치 Case A~D'),
                            ('B8', '적용환경: Bay vs 주방 형태'), ('B9', '제품화 상세 · KPI'), ('B10', '평면 30개 분석 계획'),
                            ('B11', 'Robot-ready 주방 독립 판매'), ('B12', '로봇 도달 범위 · 단면 치수'), ('B13', '안전 · 인증'),
                            ('B14', '설치: 구조체 정착 · 전원 · 통신')]),
    ('C', '시장 · 사업화', [('C1', '주택 통계'), ('C2', '주방 리모델링 시장 · 가격'), ('C3', '시장 규모 상세'), ('C4', '구축 / 신축 적용 흐름'),
                           ('C5', '사업화 전략 · 매출 구성'), ('C6', '경쟁 구도 · 대기업 대응'), ('C7', '경쟁사 상세'), ('C8', '고객 검증 · 기술 KPI')]),
    ('D', '경제성 · 재무', [('D1', '가격 가설 (원가 · 시장 · 가치)'), ('D2', '세대당 경제성'), ('D3', '수익 모델 · 매출 시점'), ('D4', '단위 경제성 · 민감도'),
                           ('D5', '부품 비교 · BOM'), ('D6', '세대당 경제성 상세'), ('D7', '렌탈 모델'), ('D8', '관리 서비스 · 소모품'),
                           ('D9', '5개년 재무 모델 (3개 시나리오)'), ('D10', '민감도 분석'), ('D11', 'TIPS 기간 자금 계획 상세')]),
    ('E', '진입장벽 · 리스크 · Q&A', [('E1', '진입장벽 · 특허 · 설치 기반'), ('E2', '특허 후보 10건'), ('E3', '마일스톤 · 중단 기준'),
                                     ('E4', '리스크 관리표'), ('E5~E6', '예상 질문과 답 25개')]),
    ('F', '참고', [('F1', '수치 표기 원칙 (Tag)'), ('F2', '출처')]),
]

def idx(prs):
    s = start(prs, 'APX', 'Index', 'Appendix 목차', visual='3열 목차 (A~F Section · Code · 제목)', chart='없음',
              note='부록은 본문 19쪽의 근거, 계산, 검증 계획입니다. A는 투자 판단 요약, B는 제품과 표준화, C는 시장과 GTM, D는 경제성, E는 Moat와 Risk, F는 Tag 원칙과 출처입니다.')
    y = head(s, 'APPENDIX', 'Appendix 목차', sub='본문 수치의 근거 · 계산 · 검증 계획. 이전 판 본문 · 부록 유지 (재배치). 재무 수식 모델: ARKI_Robotics_Financial_Model.xlsx')
    cols = [INDEX[0:2], INDEX[2:4], INDEX[4:6]]
    cw = (CW - 0.6) / 3
    for ci, secs in enumerate(cols):
        cx = MX + ci * (cw + 0.3); yy = y
        for key, name, items in secs:
            rect(s, cx, yy, cw, 0.32, fill=T['text'])
            text(s, cx + 0.12, yy, cw - 0.24, 0.32, f'{key}   {name}', size=10.5, bold=True, color='FFFFFF', anchor='m')
            yy += 0.36
            for code, t in items:
                text(s, cx + 0.05, yy, 0.62, 0.22, code, size=9, bold=True, anchor='m')
                text(s, cx + 0.68, yy, cw - 0.7, 0.22, t, size=9, color=T['text2'], anchor='m')
                yy += 0.2
            yy += 0.12
        assert yy < H - 0.55, ('index column too long', ci, yy)
    foot(s, 'Index')


# ---------------------------------------------------------------- B5 received plans: classification + status
def b05(prs):
    rows = [['구축 2Bay A', '구축 · 계단실형 (코어 포함)', '12,390 × 11,670', 'ㄱ자 (윗벽 3,255mm + 옆벽)', '완료 · 원본과 겹쳐 확인', '완료 · 표준 한 줄 3,150mm · 충돌검사 0cm (본문, B6)'],
            ['구축 2Bay B', '구축 · 전면 발코니', '10,940 × 8,500', 'ㄱ자 (싱크 줄 약 2.6m + 아랫벽) · 거실과 개방', '완료 · 원본과 겹쳐 확인', '미적용 · 냉장고 이전 시 약 3.3m'],
            ['신축 2Bay', '신축 · 탑상형', '15,120 × 10,730', '옆벽 + 윗벽 + 아일랜드형 카운터', '미착수', '미적용'],
            ['신축 3Bay', '신축 · 판상형', '12,400 × 10,550', '윗벽 싱크 줄 약 2.6m + 옆벽 쿡탑 + 반도형', '완료 · 원본과 겹쳐 확인', '미적용 · 표준 한 줄보다 짧음'],
            ['신축 4Bay', '신축 · 판상형', '14,700 × 9,780', '윗벽 싱크 줄 약 2.8m + 옆벽 쿡탑 + 반도형', '완료 · 원본과 겹쳐 확인', '미적용 · 표준 한 줄보다 짧음']]
    table_slide(prs, 'B5', 'B5', 'APPENDIX B5', '받은 평면 5종: 분류와 진행 상태',
                ['평면', '구분', '크기 (치수선, mm)', '주방 형태', '디지털화 (3D)', 'ARKI 적용'], rows,
                [1.25, 1.95, 1.55, 2.95, 1.75, 2.38], size=9.5,
                sub='받은 도면 5종 (구축 2Bay 대표 2종 + 신축 2 · 3 · 4Bay). 단지명은 표기하지 않음. 치수선 기준으로 디지털화한 뒤 원본 위에 겹쳐 벽 · 문 · 창 위치를 확인. 본문 그림은 대표 평면 1종 (구축 2Bay A)만 사용.',
                visual='5행 표 (평면 · 구분 · 크기 · 주방 형태 · 디지털화 상태 · ARKI 적용 상태)',
                note=('받은 평면 다섯 종의 분류와 진행 상태입니다. 신축 2Bay를 뺀 네 종은 치수선 기준으로 3D 모델을 만들고 원본 도면 위에 벽, 문, 창 위치를 겹쳐 확인했습니다. '
                      '그중 구축 2Bay A에는 표준 한 줄 3,150밀리미터를 배치하고 작업 자세와 보관, 이동 경로까지 충돌검사를 마쳤습니다. '
                      '나머지 세 종은 싱크 줄이 약 2.6~2.8미터로 표준 한 줄보다 짧습니다. 그래서 짧은 벽용 한 줄을 따로 만드는 일을 TIPS 1차년도 평면 분석 과제에 넣었습니다.'),
                takeaway='5종 모두 싱크와 조리기구가 다른 벽 → "싱크 벽 = 로봇 구역 / 조리기구 = 로봇 금지" 원칙과 맞음. 다만 싱크 줄 3종이 2.6~2.8m → 짧은 벽용 한 줄 필요 (5종 표본 · TO BE VALIDATED)')


# ---------------------------------------------------------------- B6 old2a: as drawn -> ARKI (verified)
def b06n(prs):
    V = json.load(open(os.path.join(SM.RD, 'plan_old2a_verify.json'), encoding='utf-8'))['ik']['verify']
    s = start(prs, 'B6', 'B6', '구축 2Bay A: 원래 평면 → ARKI 적용',
              visual='왼쪽: 받은 평면을 치수 그대로 옮긴 평면도 (원래 ㄱ자 주방). 오른쪽: 같은 평면에 ARKI 한 줄 + 인덕션 이동. 아래: 바뀐 점 · 충돌검사 결과.',
              chart='평면도 2장 + 표',
              note=('본문 6쪽 평면의 상세입니다. 왼쪽은 받은 도면을 치수선 기준으로 그대로 옮긴 원래 평면, 오른쪽은 ARKI를 넣은 평면입니다. '
                    '원래 주방은 윗벽과 왼쪽 벽을 쓰는 ㄱ자였고, ARKI 적용 후에는 윗벽 전체를 ARKI 한 줄로 쓰고 인덕션을 왼쪽 벽 아래쪽으로 옮겼습니다. '
                    '보관함 문은 왼쪽 벽 때문에 90도까지만 열리며, 이 조건에서 보관, 전개, 이동 경로를 다시 검사했습니다.'))
    y = head(s, 'APPENDIX B6', '구축 2Bay A: 원래 평면 → ARKI 적용',
             sub='받은 도면 (12,390 × 11,670mm, 코어 포함)을 치수선 기준으로 3D화 · 왼쪽 원래 주방, 오른쪽 ARKI 적용 (CONCEPT)')
    ph = 3.55; pw = ph * (1400 / 1320)
    for i, (nm, lab) in enumerate([('plan_old2a_top_orig', '원래 평면 (ㄱ자 주방)'), ('plan_old2a_top_arki', 'ARKI 적용 (윗벽 한 줄 + 인덕션 옆벽)')]):
        x = MX + i * (pw + 0.3)
        SM.render(s, nm, x, y, pw, ph, bg=(255, 255, 255))
        text(s, x, y + ph + 0.04, pw, 0.24, lab, size=9.5, bold=True, check=False)
    rx = MX + 2 * pw + 0.65; rw = W - MX - rx
    rows = [['주방 윗벽', '3,255mm (왼쪽 벽 ~ 침실2 문)'], ['ARKI 한 줄', '3,150mm (보관함 45 · 내려놓는 곳 70 · 싱크 80 · 서랍 60 · 식세기 60cm)'],
            ['싱크 중심 이동', '약 21cm'], ['인덕션', '왼쪽 벽 아래쪽 (4,400~6,110mm 구간)'], ['보관함 문', '최대 90° (왼쪽 벽)'],
            ['충돌검사', f"보관 {V['park']:.0f}cm · 전개 경로 {V['path']:.0f}cm · 레일 이동 {V['transit']:.0f}cm 관통 (가구 {V['obstacles']}개 상자)"]]
    table(s, rx, y, rw, ['항목', '값'], rows, col_w=[1.15, rw - 1.15], size=9.5, label='B6')
    foot(s, 'B6')


# ---------------------------------------------------------------- B7 old2b: as drawn (3D)
def b07n(prs):
    s = start(prs, 'B7', 'B7', '구축 2Bay B: 받은 평면 3D',
              visual='왼쪽: 받은 평면을 치수 그대로 옮긴 평면도. 오른쪽: 같은 평면의 3D (벽 높이 110cm에서 자름). 아래: ARKI 적용 검토 사항.',
              chart='평면도 + 3D',
              note=('두 번째 구축 2Bay 평면입니다. 전면 발코니가 있는 구형 2Bay이고, 주방은 침실 벽을 등진 싱크 줄과 아랫벽 쿡탑 줄로 된 ㄱ자이며 거실과 트여 있습니다. '
                    '치수선 기준으로 3D를 만들고 원본과 겹쳐 확인했습니다. ARKI를 넣으려면 싱크 줄 끝의 냉장고 위치와 코너 처리를 정해야 해서 검토 중입니다.'))
    y = head(s, 'APPENDIX B7', '구축 2Bay B: 받은 평면 3D',
             sub='받은 도면 (10,940 × 8,500mm)을 치수선 기준으로 3D화 · 원본 위에 겹쳐 벽 · 문 · 창 위치 확인 · ARKI 적용은 검토 중')
    ph = 3.7; pw = ph * (1400 / 1100)
    SM.render(s, 'plan_old2b_top_orig', MX, y, pw, ph, bg=(255, 255, 255))
    rh = ph; rw = min(W - MX - (MX + pw + 0.3), rh * (1600 / 1200))
    SM.render(s, 'plan_old2b_unit', W - MX - rw, y, rw, rh, bg=(255, 255, 255))
    text(s, MX, y + ph + 0.12, CW, 0.8, ['검토 사항: 싱크 줄 (침실3 벽, 약 2.6m) 끝 냉장고 이전 여부 · ㄱ자 코너에서 식기세척기 문 · 보관함 문이 쿡탑 줄과 겹치지 않는 배치',
                                         '후보: 싱크 줄을 냉장고 자리까지 늘려 약 3.3m 확보 → ARKI 한 줄 (보관함은 거실 쪽 끝, 식기세척기는 코너에서 떨어뜨림)'],
         size=10, color=T['text2'], bullet='–', space_after=3)
    foot(s, 'B7')


# ---------------------------------------------------------------- B6~B8 84㎡ concept-model detail
APT_DETAIL = {
    '2': ('B8', '(참고) 이전 84㎡ 2Bay 콘셉트 모델', [
        ('세대 Envelope', '약 7.8 × 10.9 m (전용 약 84㎡ 가정) · 판상형 2Bay', 'CONCEPT'),
        ('주방 위치', '후면 측부 · 식당 · 거실과 전후 배치 (구축형)', 'CONCEPT'),
        ('Kitchen Geometry', 'ㄱ자: Sink Run 약 2.6 m + Cooktop Run 약 1.8 m + 키큰장 0.6 m', 'CONCEPT'),
        ('Robot Architecture', 'Dock / Fold-out: 키큰장 상단 Robot Home + Swing Plate', 'CONCEPT'),
        ('Robot Working Zone', 'Sink 우측 ~ 키큰장 (약 1.2 m) · 식세기 상향', 'ASSUMPTION'),
        ('Human Zone · No-go', 'ㄱ자 내측 통로 = Human · Cooktop Run = No-go', 'ASSUMPTION'),
        ('핵심 설계 변수', 'Run이 짧아 Rail 대신 고정 Dock · 식세기와 Robot Home을 한 키큰장에 수직 배치', 'ASSUMPTION'),
        ('검증 항목', '키큰장 폭 600 확보 · Swing 반경 ↔ 상부장 간섭 · Sink ↔ 식세기 거리 ≤ Reach', 'TBV')]),
    '3': ('B9', '(참고) 이전 84㎡ 3Bay 콘셉트 모델', [
        ('세대 Envelope', '약 10.2 × 8.3 m (전용 약 84㎡ 가정) · 전면 침실 · 거실 · 침실', 'CONCEPT'),
        ('주방 위치', '후면 중앙 · 거실과 전후 배치 · 다용도실 인접', 'CONCEPT'),
        ('Kitchen Geometry', '일자 Sink Run 3.6 m (Robot Home 0.44 + Counter 2.56 + 식세기 · 수납 0.6) + ㄱ자 Cooktop Run 1.8 m', 'CONCEPT'),
        ('Robot Architecture', 'Rail: 상부장 하단 Rail 약 2.9 m + 키큰장 2개 (Garage · 식세기/수납)', 'CONCEPT'),
        ('Robot Working Zone', 'Sink Run Counter 전체 (약 2.56 m)', 'ASSUMPTION'),
        ('Human Zone · No-go', 'Sink Run 앞 통로 + Cooktop Run = Human · Cooktop = No-go', 'ASSUMPTION'),
        ('핵심 설계 변수', '후면 창 (다용도실 방향) 위치 → Rail 고정면 (상부장 하단 vs 천장 Bulkhead) · 상부장 하단 높이', 'ASSUMPTION'),
        ('검증 항목', '상부장 하단 약 1,450 mm · 통로 900~1,200 mm · 후면 창 위치 (B14)', 'TBV')]),
    '4': ('B10', '(참고) 이전 84㎡ 4Bay 콘셉트 모델', [
        ('세대 Envelope', '약 11.4 × 7.4 m (전용 약 84㎡ 가정) · 전면 4실', 'CONCEPT'),
        ('주방 위치', '후면 중앙 · Open Kitchen (거실과 연결)', 'CONCEPT'),
        ('Kitchen Geometry', '벽면 일자 Run 약 3.6 m + Island 약 2.2 m (IH · 착석)', 'CONCEPT'),
        ('Robot Architecture', 'Wall-side Rail + Human Island (Island에는 Robot 미진입)', 'CONCEPT'),
        ('Robot Working Zone', '벽면 Run Counter (Sink · 식세기 · 수납)', 'ASSUMPTION'),
        ('Human Zone · No-go', 'Island · 통로 = Human · Island 상판 (IH · 착석) = No-go', 'ASSUMPTION'),
        ('핵심 설계 변수', 'Island ↔ 벽면 통로 폭 · 운반 경로가 통로 위로 나가지 않도록 Reach 제한', 'ASSUMPTION'),
        ('검증 항목', '통로 1,000~1,200 mm · Island 위치 · 착석 위치 ↔ Robot Reach 이격', 'TBV')]),
}

def _apt_detail(prs, t):
    code, title, rows = APT_DETAIL[t]
    s = start(prs, code, code, title, visual='좌측 주방 3D 투시도 (번호 ①~⑥ + Zone 표시) · 우측 상단 세대 Axonometric · 우측 Concept Parameter 표 8행',
              chart='3D Concept Model + Parameter 표',
              note=(f'{title.split(":")[0]}의 상세입니다. 왼쪽은 주방 투시도, 오른쪽 위는 세대 전체입니다. 표의 치수와 배치는 Concept 가정이며, '
                    '특정 단지 평면이 아닙니다. 마지막 행의 검증 항목을 평면 30개 분석과 Full-scale Mock-up에서 확인합니다.'))
    y = head(s, f'APPENDIX {code}', title,
             sub='Representative Korean 84㎡ Apartment Concept Model · 국내 대표 84㎡ 공동주택 유형 기반 Concept Model (특정 단지 아님). 치수 = Concept 가정.')
    lw = 5.7; lh = lw / (1500 / 1125)
    at = SM.render(s, f'apt{t}_kitchen', MX, y, lw, lh, border=True)
    for j, (k, _) in enumerate(SM.MARKS):
        mx_, my_ = at(k); SM.marker(s, mx_, my_, j + 1, d=0.24, size=9)
    lgy = y + lh + 0.1; x = MX
    for j, (_, lab) in enumerate(SM.MARKS):
        SM.marker(s, x + 0.1, lgy + 0.11, j + 1, d=0.2, size=7.5, ring=False)
        tw = kit.text_w(lab, 9) + 0.1
        text(s, x + 0.25, lgy, tw, 0.22, lab, size=9, anchor='m', check=False); x += 0.25 + tw + 0.06
    lgy2 = lgy + 0.3; x = MX
    for kind, lab in [('robot', 'Robot Working Zone'), ('reach', 'Robot Reach'), ('human', 'Human Zone'), ('nogo', 'No-go')]:
        SM.swatch(s, x, lgy2 + 0.01, kind)
        tw = kit.text_w(lab, 9) + 0.1
        text(s, x + 0.42, lgy2, tw, 0.22, lab, size=9, anchor='m', check=False); x += 0.42 + tw + 0.14
    uw = 1.75; uh = uw / (1500 / 1125); ux = MX + 0.08; uy = y + lh - uh - 0.08
    SM.render(s, f'apt{t}_unit', ux, uy, uw, uh, border=True)
    text(s, ux, uy + 0.03, uw, 0.2, '세대 전체 (주황 외곽 = 주방 · 식당)', size=7, color=T['muted'], align='c', check=False)
    rx = MX + lw + 0.35; rw = W - MX - rx
    trs = [[a, b_, TG(tg)] for a, b_, tg in rows]
    table(s, rx, y, rw, ['항목', 'Concept 값 · 설명', 'Tag'], trs, col_w=[1.3, rw - 2.45, 1.15], size=9.5, label=code,
          max_h=H - y - 0.62)
    foot(s, code)

def b08(prs): _apt_detail(prs, '2')
def b09(prs): _apt_detail(prs, '3')
def b10(prs): _apt_detail(prs, '4')


# ---------------------------------------------------------------- order (A~F)
ORDER = [idx,
         L.s02, L.s03, AX.a18, AX.a22,                                                    # A
         L.s05, L.s07, L.s08, L.s09, b05, b06n, L.s10, L.s06, L.s11, AX.a05, L.s13,         # B1~B11
         AX.a06, AX.a07, AX.a08,                                                           # B12~B14
         AX.a02, AX.a03, L.s18, L.s12, L.s19, L.s20, AX.a09, AX.a17,                       # C
         L.s14, L.s15, L.s16, L.s17, AX.a04, AX.a11, AX.a12, AX.a13, AX.a14, AX.a15, AX.a16,  # D
         L.s21, AX.a10, L.s22, AX.a19, AX.a20, AX.a21,                                    # E
         AX.a01, AX.a23]                                                                   # F

def build(prs):
    common.APX['on'] = True
    try:
        for f in ORDER:
            f(prs)
    finally:
        common.APX['on'] = False; kit.XFORM['fn'] = None
