# SoftHand Seed 투자유치 사업계획서 v4 - main slides (14).
# Business-plan format: numbered sections, plain Korean statements, tables and numbers first,
# one product image only, every unverified item marked 목표 / 가정 / 검증 예정 / [입력 필요].
import json, os
from kit import *
import kit

from paths import RAW as _RAW, RENDERS as _RENDERS, ORIGINAL as _ORIGINAL, MODEL_JSON as _MODEL
PATHS = dict(raw=_RAW, renders=_RENDERS, original=_ORIGINAL, model=_MODEL)
def RAW(n): return os.path.join(PATHS['raw'], n)
def REN(n): return os.path.join(PATHS['renders'], n)
def ORI(n): return os.path.join(PATHS['original'], n)
def KIT(n): return os.path.join(PATHS['renders'], 'kitchen', n)

M = {}
def load_model():
    M.update(json.load(open(PATHS['model'], encoding='utf-8')))

FOOT = '[회사명 입력 필요]  |  투자유치 사업계획서 (Seed)'
IN = '[입력 필요]'


def foot(s, page, note=None):
    footer(s, page, left=FOOT, note=note)


def bp_header(s, no, section, title, lead=None):
    """Business-plan header: numbered section label, one-line statement title, optional lead, rule. Returns content top."""
    text(s, MX, 0.48, 6, 0.26, f'{no:02d}   {section}', size=11, bold=True, color=T['accent'])
    text(s, MX, 0.78, CW, 0.5, title, size=24, bold=True, label='title ' + section)
    y = 1.36
    if lead:
        text(s, MX, y, CW, 0.28, lead, size=13, color=T['text2'], label='lead ' + section)
        y += 0.38
    hline(s, MX, y, CW, color=T['text'], lw=1.0)
    return y + 0.24


def ph(t):
    """Runs: plain text with [입력 필요] style placeholders in accent."""
    out = []
    while '[' in t:
        i = t.index('['); j = t.index(']', i) + 1
        if i: out.append((t[:i], {}))
        out.append((t[i:j], {'color': T['accent']}))
        t = t[j:]
    if t: out.append((t, {}))
    return out


def kv_table(s, x, y, w, rows, kw=1.3, size=11.5, pad=0.075, label='kv', max_h=None):
    """Two-column label/value table with a top rule."""
    hline(s, x, y, w, color=T['text'], lw=1.0)
    return table(s, x, y, w, None, [[(k, {'bold': True}), v] for k, v in rows], col_w=[kw, w - kw], size=size, pad=pad,
                 label=label, max_h=max_h)


# ---------------------------------------------------------------- 01 cover
def s01(prs):
    s = new_slide(prs, '01 cover')
    text(s, MX, 0.7, 8, 0.3, '[회사명 입력 필요]', size=13, bold=True, color=T['accent'])
    text(s, MX, 1.95, CW, 0.32, '투자유치 사업계획서 (Seed)', size=14, bold=True, color=T['text2'])
    text(s, MX, 2.45, CW, 1.45, '주방 조리 자동화용 로봇 핸드\nSoftHand 개발 및 사업화', size=36, bold=True, line=0.98, label='cover title')
    text(s, MX, 3.98, CW, 0.32, '사람용 조리도구와 가전을 그대로 사용하는 로봇 핸드와 주방 작업 소프트웨어', size=15, color=T['text2'], label='cover sub')
    y = 4.85
    hline(s, MX, y, CW, color=T['text'], lw=1.0)
    items = [('투자 유치 금액', '20억 원 (Seed)'), ('자금 사용 기간', '24개월'), ('1차 목표 시장', '급식·외식 상업용 주방'), ('작성일', '2026년 10월')]
    cw4 = CW / 4
    for i, (k, v) in enumerate(items):
        x = MX + i * cw4 + (0.2 if i else 0)
        if i: vline(s, MX + i * cw4, y + 0.22, 0.7)
        text(s, x, y + 0.2, cw4 - 0.35, 0.26, k, size=11, color=T['muted'])
        text(s, x, y + 0.5, cw4 - 0.35, 0.4, v, size=17, bold=True, color=T['accent'] if i == 0 else T['text'], label='cover ' + k)
    hline(s, MX, y + 1.15, CW)
    text(s, MX, H - 0.78, CW, 0.26, [ph('대표자 [입력 필요]  ·  이메일·연락처 [입력 필요]')], size=11, color=T['muted'], check=False)
    text(s, MX, H - 0.5, CW, 0.22, '본 자료의 매출·성능·일정은 계획 및 가정이며 실적이 아님', size=9, color=T['muted'], check=False)
    notes(s, '주방 조리 자동화용 로봇 핸드 SoftHand 개발 및 사업화. Seed 20억 원, 24개월. 1차 목표 시장은 급식·외식 상업용 주방.')


# ---------------------------------------------------------------- 02 overview
def s02(prs):
    s = new_slide(prs, '02 overview')
    B = M['base']
    y0 = bp_header(s, 1, '사업 개요', '급식·외식 주방의 반복 조리 작업을 자동화하는 로봇 핸드 사업')
    lw = 4.3
    text(s, MX, y0, lw, 0.28, '회사 현황', size=13, bold=True)
    rows = [('회사명', ph('[입력 필요]')), ('대표자', ph('[입력 필요]')), ('설립', ph('[설립일 또는 예정일 입력 필요]')),
            ('소재지', ph('[입력 필요]')), ('인원', '창업자 2명, 24개월 내 6명 단계 채용 계획'), ('사업 분야', '로봇 핸드 · 주방 자동화 소프트웨어'),
            ('개발 단계', '콘셉트·기술 구조·초기 설계\n(시제품 개발 전)'), ('지식재산', ph('확인된 출원 없음 [보유 시 입력]'))]
    kv_table(s, MX, y0 + 0.38, lw, rows, kw=1.15, label='company')
    rx = MX + lw + 0.45; rw = W - MX - rx
    text(s, rx, y0, rw, 0.28, '사업 요약', size=13, bold=True)
    rows2 = [('해결할 문제', '주방 조리 인력 부족, 메뉴·공정마다 전용 장비가 필요한 기존 조리 자동화'),
             ('제품', '사람용 조리도구·가전을 그대로 쓰는 로봇 핸드(SoftHand) + 주방 작업 소프트웨어'),
             ('1차 목표 고객', '단체급식·센트럴키친·프랜차이즈 주방 (가설, 고객 인터뷰 30곳으로 검증 예정)'),
             ('수익 구조', '유료 실증(PoC) → 핸드 판매 → 작업 소프트웨어·유지보수 반복 매출'),
             ('투자 요청', [('Seed 20억 원', {'bold': True, 'color': T['accent']}), (', 24개월 운영 (매출 없이도 운영 가능한 규모)', {})]),
             ('24개월 목표', '유료 PoC 5건 · 재구매 고객 2곳 · 공동개발 고객 3곳 · 로봇 2종 호환 · 양산 설계 확정'),
             ('5년차 계획', f'매출 {B["rev"][4]:.1f}억 원, 영업손익 손익분기 근접 (기본 계획, 가정)'),
             ('장기 방향', '상업용·가정용 주방에서 사람용 도구를 쓰는 범용 로봇 조작 기술')]
    kv_table(s, rx, y0 + 0.38, rw, rows2, kw=1.45, label='summary')
    foot(s, 2)
    notes(s, '회사 현황은 확인된 정보가 없어 자리만 둠. 사업 요약: 문제(인력 부족·전용 장비), 제품(로봇 핸드 + 작업 소프트웨어), 1차 고객(가설), '
             '수익 구조, 투자 요청, 24개월 목표, 5년차 계획(기본 계획).')


# ---------------------------------------------------------------- 03 problem
def s03(prs):
    s = new_slide(prs, '03 problem')
    y0 = bp_header(s, 2, '문제 인식', '조리 인력은 부족하고, 기존 조리 자동화는 공정마다 전용 장비가 필요')
    lw = 3.95
    text(s, MX, y0, lw, 0.28, '주방 인력 현황', size=13, bold=True)
    stats = [('229만 명', '숙박·음식점업 종사자 (사업체 86.2만 개, 2023)'),
             ('약 2배', '조리·식당 서비스 인력 부족률, 코로나19 이전 대비 (2023)'),
             ('27.6%', '인력난을 겪는 외식업체 비율 (952곳 조사, 2023)'),
             ('49%', '인력 대응 자동화가 더 보편화될 것이라는 미국 외식 운영자 (2025)')]
    y = y0 + 0.38
    for i, (n, d) in enumerate(stats):
        hline(s, MX, y, lw, color=T['text'] if i == 0 else T['line'], lw=1.0 if i == 0 else 0.75)
        text(s, MX, y + 0.1, 1.45, 0.46, n, size=22, bold=True, color=T['accent'] if i == 1 else T['text'], label='stat ' + n)
        text(s, MX + 1.5, y + 0.12, lw - 1.5, 0.5, d, size=11.5, color=T['text2'], label='stat d ' + n)
        y += 0.86
    hline(s, MX, y, lw)
    rx = MX + lw + 0.5; rw = W - MX - rx
    text(s, rx, y0, rw, 0.28, '기존 조리 자동화 방식', size=13, bold=True)
    rows = [[('공정별 전용\n조리로봇', {'bold': True}), '삼성웰스토리: 국·탕, 볶음, 면·튀김 로봇을 공정별로 배치\n부산교육청: 학교 급식실 튀김·볶음·국 조리로봇 실증 (2025)',
             '공정·메뉴 수만큼\n장비·공간 증가'],
            [('메뉴 전용 장비', {'bold': True}), '패티 조리 로봇, 시간당 200장 이상 (에니아이 알파그릴)\n튀김 스테이션 전용 로봇 (Miso Robotics Flippy)', '다른 메뉴·작업에\n사용 어려움'],
            [('로봇 전용 주방', {'bold': True}), '천장 레일 양팔 로봇 + 전용 조리도구 (Moley Robotics)\n구성별 약 13.4만~34만 달러 (2021 보도)', '주방 전체 재설계\n높은 초기 비용']]
    h = table(s, rx, y0 + 0.38, rw, ['방식', '사례 (공개 정보)', '도입 시 부담'], rows, col_w=[1.45, rw - 1.45 - 1.75, 1.75], size=11, pad=0.08, label='auto table')
    by = y0 + 0.38 + h + 0.25
    rect(s, rx, by, rw, 0.98, fill=T['soft'])
    text(s, rx + 0.22, by, rw - 0.44, 0.98,
         [[('공통점  ', {'bold': True, 'color': T['text']}), ('로봇에 맞춰 장비·도구·주방을 바꾸는 방식, 메뉴·공정이 늘수록 장비·공간·통합 비용 증가', {})],
          [('참고  ', {'bold': True, 'color': T['text']}), ('로봇 도입 총비용의 약 75%가 초기 셋업·재설계 (BCG, 2026, 로봇 도입 전반 기준)', {})]],
         size=11.5, color=T['text2'], anchor='m', space_after=4, label='problem box')
    foot(s, 3, note='출처: 통계청 전국사업체조사(2023), 헤럴드경제(2025.5), Restaurant Dive(2025), 각 사 공개 자료 · 부록 A17')
    notes(s, '수요: 숙박·음식점업 종사자 229만 명(2023), 조리·식당 서비스 인력 부족률 코로나 이전 대비 약 2배, 외식업체 27.6% 인력난, 미국 외식 운영자 49% 자동화 확대 예상. '
             '공급: 지금의 조리 자동화는 공정·메뉴별 전용 장비 또는 로봇 전용 주방 방식이라 메뉴·공정이 늘수록 장비와 공간이 함께 증가.')


# ---------------------------------------------------------------- 04 solution
def s04(prs):
    s = new_slide(prs, '04 solution')
    y0 = bp_header(s, 3, '해결 방안', '기존 조리도구와 가전을 그대로 쓰는 로봇 핸드와 작업 소프트웨어')
    iw, ih = 2.45, 3.55
    rect(s, MX, y0, iw, ih, fill='EEF0F2')
    cutout(s, REN('product.png'), MX + 0.1, y0 + 0.12, iw - 0.2, ih - 0.24)
    text(s, MX, y0 + ih + 0.06, iw, 0.26, 'SoftHand 콘셉트 설계안 (렌더링)', size=9.5, color=T['muted'])
    rx = MX + iw + 0.45; rw = W - MX - rx
    text(s, rx, y0, rw, 0.28, '제품 구성', size=13, bold=True)
    rows = [[('SoftHand 로봇 핸드', {'bold': True}), '손가락 3개 + 대향 엄지, 부드러운 접촉면 + 하중 지지 골격, 힘·미끄러짐 감지, 기존 협동로봇에 장착', '하드웨어 판매', '1,500만 원'],
            [('주방 작업 소프트웨어', {'bold': True}), '재료 집기·뚜껑 열기·집게·국자 사용·노브 조작·플레이팅 등 작업 단위 패키지', '작업 패키지', '핸드당 300만 원'],
            [('제어 SW·유지보수', {'bold': True}), '힘·촉각 제어, 보정, 업데이트, 교체형 접촉부 공급', '연간 계약', '핸드당 연 150만 원'],
            [('유료 실증 (PoC)', {'bold': True}), '고객 주방 8~12주 적용, 고객 기존 수치 대비 측정', '프로젝트', '건당 5,000만 원']]
    h = table(s, rx, y0 + 0.38, rw, ['구성', '내용', '판매 형태', '가격 (가정)'], rows, col_w=[1.95, rw - 1.95 - 1.2 - 1.55, 1.2, 1.55],
              size=11, pad=0.075, align=['l', 'l', 'l', 'r'], label='product table')
    by = y0 + 0.38 + h + 0.3
    text(s, rx, by, rw, 0.28, '고객 입장에서 달라지는 점 (PoC에서 검증 예정)', size=13, bold=True)
    hline(s, rx, by + 0.36, rw, color=T['text'], lw=1.0)
    gains = [('주방 유지', '기존 레이아웃·조리도구·가전을 그대로 사용, 전용 장비·주방 개조 최소화'),
             ('메뉴 추가', '공정·메뉴가 늘 때 장비 대신 작업 소프트웨어를 추가 (목표)'),
             ('로봇 호환', '고객이 가진 협동로봇에 장착, 로봇 2종 호환 검증 (목표)')]
    gw = rw / 3
    for i, (a, b) in enumerate(gains):
        x = rx + i * gw
        text(s, x, by + 0.48, gw - 0.25, 0.3, a, size=13, bold=True, label='gain ' + a)
        text(s, x, by + 0.8, gw - 0.25, 0.62, b, size=11, color=T['text2'], label='gain d ' + a)
    foot(s, 4, note='가격은 기존 계획의 가정 (부록 A10) · 핸드 상세 설계는 부록 A3 · 적용 장면 콘셉트는 부록 A5')
    notes(s, '제품은 로봇 핸드 하드웨어, 주방 작업 소프트웨어, 제어 소프트웨어·유지보수, 유료 실증으로 구성. 가격은 기존 계획의 가정. '
             '고객 가치(주방 유지, 메뉴 추가 시 소프트웨어 추가, 로봇 호환)는 PoC에서 검증할 목표.')


# ---------------------------------------------------------------- 05 technology & development status
def s05(prs):
    s = new_slide(prs, '05 technology')
    y0 = bp_header(s, 4, '기술 및 개발 현황', '핵심 기술 4가지, 24개월 안에 시제품에서 양산 설계까지')
    rows = [[('순응·강성 전환 구조', {'bold': True}), '잡을 때는 부드럽게, 도구를 쓸 때는 단단하게 (탄성 요소·장력 제어·잠금 기구)', '콘셉트 설계', '알파 시제품 검증 (M6), 설계 확정 (M18)'],
            [('힘·촉각 기반 조작 제어', {'bold': True}), '손끝 접촉·미끄러짐 감지, 손목 6축 힘센서로 반력·토크 제어', '구조 설계', '승인 작업 완료율 95% 이상'],
            [('주방 작업 소프트웨어', {'bold': True}), '집기·열기·젓기 등 작업 단위로 표준화, 다른 메뉴·주방·로봇에 재사용', '구조 설계', '검증 대상 6종 작업, 로봇 2종 호환'],
            [('교체형 위생 접촉부', {'bold': True}), '세척·교체 가능한 패드·외피, 식품 접촉 재질 적용', '콘셉트', '재질 시험, 교체 주기 확정']]
    h = table(s, MX, y0, CW, ['핵심 기술', '내용', '현재 상태', '24개월 목표'], rows, col_w=[2.6, 5.1, 1.45, 2.68], size=11.5, pad=0.085, label='tech table')
    by = y0 + h + 0.35
    cw2 = (CW - 0.5) / 2
    text(s, MX, by, cw2, 0.28, '목표 사양 (24개월, 목표)', size=13, bold=True)
    specs = [('핸드 하중', '2kg (동일 조건 원통 물체)'), ('승인 작업 완료율', '95% 이상 (최초 시도·재시도 분리 보고)'), ('내구성', '반복 개폐 30만 회 (양산 목표 100만 회)'),
             ('로봇 호환', '협동로봇 2종에서 같은 작업 소프트웨어 사용')]
    kv_table(s, MX, by + 0.38, cw2, specs, kw=1.7, size=11.5, pad=0.07, label='specs')
    x2 = MX + cw2 + 0.5
    text(s, x2, by, cw2, 0.28, '개발 현황과 지식재산', size=13, bold=True)
    st = [('현재 단계', '콘셉트·기술 구조·초기 설계, 시제품·시험 데이터 없음'),
          ('구동 방식', '전동 텐던 기준, 소형 유압·공압과 비교 후 결정 (창업 후 3개월)'),
          ('지식재산', ph('확인된 출원 없음, 선행기술 조사 후 출원 [보유 시 입력]')),
          ('검증 방식', '반복 시험 횟수·성공 건수·신뢰구간 공개, 무편집 영상')]
    kv_table(s, x2, by + 0.38, cw2, st, kw=1.3, size=11.5, pad=0.07, label='status')
    foot(s, 5, note='모든 사양은 목표이며 실적 아님 · 구동·센서·하중 상세는 부록 A3, 시험 방법은 부록 A4')
    notes(s, '핵심 기술: 순응·강성 전환 구조, 힘·촉각 기반 제어, 주방 작업 소프트웨어, 교체형 위생 접촉부. 현재는 콘셉트·설계 단계로 시제품·시험 데이터 없음. '
             '24개월 목표: 하중 2kg, 승인 작업 완료율 95%, 내구 30만 회, 로봇 2종 호환.')


# ---------------------------------------------------------------- 06 market
def s06(prs):
    s = new_slide(prs, '06 market')
    B = M['base']; A = M['assumptions']
    y0 = bp_header(s, 5, '시장 분석', '국내 급식·외식 주방에서 조리 로봇 도입이 시작되는 단계')
    lw = 3.7
    text(s, MX, y0, lw, 0.28, '글로벌 식품 로봇 시장 (억 달러)', size=12.5, bold=True)
    cy = y0 + 0.4; chh = 2.35; plot = (0.08, 0.14, 0.84, 0.72); vmax = 80
    column_chart(s, MX, cy, lw, chh, ['2023', '2030 전망'], [('시장', [18.1, 68.1])], [T['grey_bar']], vmax=vmax, show_labels=False,
                 gap=80, plot=plot, size=11)
    px, py, pw, ph_ = plot
    for i, v in enumerate([18.1, 68.1]):
        ccx = MX + lw * (px + pw * (i + 0.5) / 2); top = cy + chh * (py + ph_ * (1 - v / vmax))
        text(s, ccx - 0.6, top - 0.32, 1.2, 0.28, f'{v:.1f}', size=13, bold=True, align='c', check=False)
    text(s, MX, cy + chh + 0.36, lw, 0.5, '연평균 20.6% 성장 전망 (Grand View Research)\n식품 제조·포장 포함, 주방만의 수치 아님', size=10.5, color=T['text2'], label='mkt cap')
    hline(s, MX, cy + chh + 1.0, lw, color=T['text'], lw=1.0)
    text(s, MX, cy + chh + 1.1, lw, 0.6, [[('국내 숙박·음식점업  ', {'bold': True, 'color': T['text']})], [('사업체 86.2만 개 · 종사자 229만 명 (2023, 통계청)', {})]],
         size=11.5, color=T['text2'], label='domestic')
    rx = MX + lw + 0.5; rw = W - MX - rx
    text(s, rx, y0, rw, 0.28, '국내 도입 사례 (공개 정보)', size=12.5, bold=True)
    rows = [[('학교 급식', {'bold': True}), '부산교육청, 서비스로봇 실증사업으로 3개교에 다기능 조리로봇 도입 (2025)\n솥 앞 작업시간 평균 69%, 근력 작업 72% 감소'],
            [('급식 위탁', {'bold': True}), '삼성웰스토리, 산업체 사업장에 국·볶음·면·튀김 조리로봇 운영 (2023~)'],
            [('외식', {'bold': True}), '버거 패티(에니아이), 치킨(로보아르테, Series A 75억 원) 조리 로봇 매장 적용']]
    h1 = table(s, rx, y0 + 0.38, rw, None, rows, col_w=[1.25, rw - 1.25], size=11, pad=0.075, label='cases')
    hline(s, rx, y0 + 0.38, rw, color=T['text'], lw=1.0)
    ty = y0 + 0.38 + h1 + 0.3
    text(s, rx, ty, rw, 0.28, '당사 목표 시장 단계', size=12.5, bold=True)
    rows2 = [[('1차 · Seed', {'bold': True, 'color': T['accent']}), '단체급식·센트럴키친·프랜차이즈 주방의 반복 조리 보조 (가설)'],
             [('2차 · 3~5년차', {'bold': True}), '외식 매장 주방 확대, 주방설비 업체·로봇 SI 파트너 판매'],
             [('3차 · 장기', {'bold': True}), '가정용 주방 (가전·가정용 로봇 기업 협력), 빌트인 주방 (장기 확장 가능성)']]
    h2 = table(s, rx, ty + 0.38, rw, None, rows2, col_w=[1.55, rw - 1.55], size=11, pad=0.075, label='stages')
    hline(s, rx, ty + 0.38, rw, color=T['text'], lw=1.0)
    text(s, rx, ty + 0.5 + h2, rw, 0.3,
         [[('당사 5년차 목표 (기본 계획)  ', {'bold': True, 'color': T['text']}),
           (f'신규 핸드 {int(B["hands_new"][4])}대 · 누적 설치 {int(B["installed_end"][4])}대 · 매출 {B["rev"][4]:.1f}억 원', {})]],
         size=11.5, color=T['text2'], label='som')
    foot(s, 6, note='조사기관별 전망 편차 큼 (2030년 49.7억~68.1억 달러) · 국내 주방 로봇 시장 규모는 공식 통계 부재로 미제시 · 부록 A8')
    notes(s, '글로벌 식품 로봇 시장 18.1억 달러(2023) → 68.1억 달러(2030 전망, Grand View Research, 식품 제조·포장 포함). 국내 숙박·음식점업 사업체 86.2만 개, 종사자 229만 명(2023). '
             '국내에서는 학교 급식(부산교육청 실증, 솥 앞 작업시간 69% 감소), 급식 위탁(삼성웰스토리), 외식(에니아이·로보아르테)에서 조리 로봇 도입이 시작. '
             '당사 목표 시장은 1차 급식·센트럴키친·프랜차이즈(가설), 2차 외식 매장·파트너 판매, 3차 가정용·빌트인(장기).')


# ---------------------------------------------------------------- 07 competition
def s07(prs):
    s = new_slide(prs, '07 competition')
    y0 = bp_header(s, 6, '경쟁 분석', '경쟁 제품은 메뉴·공정 전용 장비, 당사는 범용 핸드로 차별화')
    rows = [[('전용 조리 장비·로봇 (국내)', {'bold': True}), '에니아이 알파그릴, 급식용 국·볶음·튀김 조리로봇', '메뉴·공정 전용', '높은 처리량, 상용 운영 중', '메뉴·공정 추가 시 장비 추가'],
            [('로봇 전용 주방 (해외)', {'bold': True}), 'Moley Robotics', '천장 레일 양팔 + 전용 조리도구', '다양한 요리 시연', '주방 재설계, 약 13.4만~34만 달러'],
            [('스테이션 로봇 (해외)', {'bold': True}), 'Miso Robotics Flippy', '튀김 스테이션 전용', '외식 매장 확산', '튀김 외 작업 어려움'],
            [('밀 조립 로봇 (해외)', {'bold': True}), 'Chef Robotics (Series A 4,310만 달러)', '식품 공장 조립 라인', '공장 대량 생산', '매장 주방 조리 작업과 다름'],
            [('산업용 그리퍼', {'bold': True}), '평행·진공·적응형 그리퍼', '범용 집기', '저가·고신뢰', '사람용 도구·노브 조작 제한'],
            [('당사 SoftHand', {'bold': True, 'color': T['accent']}), '로봇 핸드 + 주방 작업 소프트웨어', '기존 조리도구 사용', '여러 공정을 핸드 하나로 (목표)', '속도·내구·위생 검증 필요']]
    h = table(s, MX, y0, CW, ['구분', '대표 사례', '방식', '강점', '한계'], rows, col_w=[2.45, 3.0, 2.1, 2.2, 2.08], size=11, pad=0.075, label='comp table')
    by = y0 + h + 0.3
    text(s, MX, by, CW, 0.28, '당사 차별화 요소 (모두 검증 예정)', size=13, bold=True)
    hline(s, MX, by + 0.36, CW, color=T['text'], lw=1.0)
    diffs = [('기존 도구 사용', '사람용 집게·국자·팬·노브를 그대로 사용'), ('공정 통합', '핸드 하나로 여러 공정 처리, 툴 교체 최소화'),
             ('소프트웨어 확장', '메뉴 추가 시 작업 소프트웨어 추가'), ('로봇 무관', '고객 보유 협동로봇에 장착, 로봇 2종 호환')]
    dw = CW / 4
    for i, (a, b) in enumerate(diffs):
        x = MX + i * dw
        text(s, x, by + 0.48, dw - 0.25, 0.3, a, size=13, bold=True, label='diff ' + a)
        text(s, x, by + 0.8, dw - 0.25, 0.5, b, size=11, color=T['text2'], label='diff d ' + a)
    foot(s, 7, note='공개 정보 기반 정성 비교, 독립 비교시험 아님 · 우열을 주장하지 않음 · 상세 부록 A7')
    notes(s, '현재 상용 조리 자동화는 대부분 메뉴·공정 전용 장비. 해외에는 로봇 전용 주방(Moley), 튀김 스테이션(Miso), 식품 공장 조립(Chef Robotics). '
             '당사는 사람용 도구를 그대로 쓰는 범용 핸드와 작업 소프트웨어로 차별화하되, 처리 속도·내구·위생은 검증 과제.')


# ---------------------------------------------------------------- 08 go-to-market
def s08(prs):
    s = new_slide(prs, '08 gtm')
    y0 = bp_header(s, 7, '사업화 전략', '급식·센트럴키친 유료 실증으로 시작해 파트너 판매로 확대')
    rows = [[('1단계 실증', {'bold': True, 'color': T['accent']}), 'M0~M12', '단체급식·센트럴키친 (가설)', '고객 인터뷰 30곳 → 유료 PoC (8~12주)', '첫 유료 PoC (M12)'],
            [('2단계 첫 판매', {'bold': True}), 'M12~M24', 'PoC 고객·공동개발 고객', '핸드 + 작업 소프트웨어 판매', '유료 PoC 5건, 재구매 2곳'],
            [('3단계 확대', {'bold': True}), '3~5년차', '프랜차이즈·급식 위탁사·외식 매장', '직판 + 주방설비 업체·로봇 SI 파트너', '5년차 신규 200대'],
            [('장기', {'bold': True}), '5년차 이후', '가정용 주방, 로봇·가전 기업', '라이선스·제품 탑재 협력', '장기 가능성']]
    lw = 8.0
    h = table(s, MX, y0, lw, ['단계', '기간', '고객', '방식', '목표'], rows, col_w=[1.35, 1.0, 1.95, 2.15, 1.55], size=11, pad=0.085, label='gtm table')
    rx = MX + lw + 0.45; rw = W - MX - rx
    blocks = [('판매 채널', ['직판 (초기 고객·공동개발 고객)', '주방설비 업체·로봇 SI 파트너 (3년차~)', '정부 실증사업 참여 검토 (예: 서비스로봇 실증사업)']),
              ('가격 정책 (가정)', ['핸드 1,500만 원, 파트너 경유 1,200만 원', '작업 소프트웨어 핸드당 300만 원', '제어 SW·유지보수 연 150만 원', '유료 PoC 건당 5,000만 원']),
              ('초기 영업 활동', ['창업 후 90일 내 고객 인터뷰 30곳', '공동개발 고객 3곳 확보 (목표)', '비표준 요청은 별도 견적, 표준 작업 위주 수주'])]
    y = y0
    for t_, items in blocks:
        text(s, rx, y, rw, 0.28, t_, size=13, bold=True)
        hline(s, rx, y + 0.36, rw, color=T['text'], lw=1.0)
        hh = text_h(items, 11, rw - 0.18, space_after=3)
        text(s, rx, y + 0.46, rw, hh + 0.05, items, size=11, bullet='•', indent=0.18, space_after=3, color=T['text2'], label='gtm ' + t_)
        y += 0.46 + hh + 0.32
    foot(s, 8, note='1차 고객군은 가설이며 실제 고객·계약 없음 · 고객 인터뷰 결과로 확정')
    notes(s, '1단계: 고객 인터뷰 30곳 후 단체급식·센트럴키친에서 유료 PoC. 2단계: PoC·공동개발 고객 대상 첫 판매. 3단계: 직판 + 주방설비 업체·로봇 SI 파트너. '
             '장기: 가정용 주방·로봇·가전 기업 협력. 가격은 기존 계획의 가정. 고객군은 가설.')


# ---------------------------------------------------------------- 09 revenue model
def s09(prs):
    s = new_slide(prs, '09 revenue model')
    B = M['base']
    y0 = bp_header(s, 8, '수익 모델', '하드웨어 판매로 시작해 소프트웨어·유지보수 반복 매출로 전환')
    lw = 6.2
    rows = [[('유료 실증·통합', {'bold': True}), '건당 5,000만 원 / 4,000만 원', '40%', '초기'],
            [('핸드 하드웨어', {'bold': True}), '1,500만 원 (파트너 1,200만 원)', '원가 950 → 750만 원', '초기~'],
            [('작업 소프트웨어', {'bold': True}), '핸드당 300만 원, 1.0 → 1.6개', '85%', '초기~'],
            [('제어 SW·유지보수', {'bold': True}), '설치 핸드당 연 150만 원', '70%', '중기~'],
            [('라이선스·제품 탑재', {'bold': True}), ph('출하량 연동 [협의 후 검증]'), '—', '장기']]
    h = table(s, MX, y0, lw, ['매출원', '과금 (가정)', '매출총이익률 (가정)', '시점'], rows, col_w=[1.9, 2.3, 1.2, 0.8], size=11, pad=0.085,
              label='rev table')
    text(s, MX, y0 + h + 0.25, lw, 0.85, [[('반복 매출 비중 (기본 계획)  ', {'bold': True, 'color': T['text']}),
                                           (f'1년차 0% → 3년차 {B["reuse_share"][2] * 100:.0f}% → 5년차 {B["reuse_share"][4] * 100:.0f}%', {'color': T['accent'], 'bold': True})],
                                          [('정의  ', {'bold': True, 'color': T['text']}), ('고객별 엔지니어링(실증·통합)을 제외한 하드웨어·소프트웨어·유지보수·파트너 매출', {})]],
         size=11.5, color=T['text2'], space_after=4, label='reuse')
    rx = MX + lw + 0.5; rw = W - MX - rx
    text(s, rx, y0, rw, 0.28, '매출 구성 계획 (억 원, 기본 계획)', size=12.5, bold=True)
    series = [('실증·통합', B['poc_int']), ('하드웨어 직판', B['hw']), ('파트너 판매', B['partner']), ('작업 소프트웨어', B['skill']), ('제어 SW·유지보수', B['runtime'])]
    cols = [T['grey_bar'], '4A4F57', '8C9198', T['accent'], 'F2A27E']
    lg_y = y0 + 0.36; lx_ = rx
    for (nm, _), c in zip(series, cols):
        rect(s, lx_, lg_y + 0.07, 0.12, 0.12, fill=c)
        text(s, lx_ + 0.17, lg_y, 1.6, 0.25, nm, size=9.5, color=T['text2'], check=False)
        lx_ += 0.17 + text_w(nm, 9.5) + 0.22
    cy = y0 + 0.72; chh = 4.1; plot = (0.02, 0.08, 0.96, 0.82); vmax = 50
    column_chart(s, rx, cy, rw, chh, ['1년', '2년', '3년', '4년', '5년'], series, cols, stacked=True, vmax=vmax, show_labels=False, gap=55, plot=plot, size=11)
    px, py, pw, ph_ = plot
    for i, tot in enumerate(B['rev']):
        ccx = rx + rw * (px + pw * (i + 0.5) / 5); top = cy + chh * (py + ph_ * (1 - tot / vmax))
        text(s, ccx - 0.6, top - 0.3, 1.2, 0.26, f'{tot:.1f}', size=11.5, bold=True, align='c', check=False)
    foot(s, 9, note='모든 가격·원가·마진은 검증 전 가정 · 상세 부록 A10 · 라이선스·제품 탑재 매출은 기본 계획에 미반영')
    notes(s, '초기 매출은 유료 실증·통합과 핸드 판매, 설치 대수가 늘면서 작업 소프트웨어·유지보수·파트너 판매 비중이 커지는 구조. '
             f'반복 매출 비중 5년차 {B["reuse_share"][4] * 100:.0f}%(기본 계획). 라이선스·제품 탑재는 장기이며 수치 미반영.')


# ---------------------------------------------------------------- 10 financial plan
def s10(prs):
    s = new_slide(prs, '10 financials')
    B = M['base']
    y0 = bp_header(s, 9, '매출·손익 계획', '5개년 매출·손익 계획 (기본 계획)', '대규모 주방 체인·로봇 OEM·가정용 매출을 제외한 보수적 계획, 모든 수치는 가정')
    f = lambda v: f'{v:.1f}'.replace('-', '−')
    lw = 7.0
    rows = [['매출액'] + [f(v) for v in B['rev']],
            ['매출총이익'] + [f(v) for v in B['gp']],
            ['매출총이익률'] + [f'{v * 100:.0f}%' for v in B['gm']],
            ['운영비'] + [f(v) for v in B['opex']],
            [('영업손익', {'bold': True})] + [(f(v), {'bold': True, 'color': T['accent'] if v < 0 else T['text']}) for v in B['op']],
            ['신규 핸드 (대)'] + [str(int(v)) for v in B['hands_new']],
            ['누적 설치 (대)'] + [str(int(v)) for v in B['installed_end']]]
    h = table(s, MX, y0, lw, ['구분 (억 원)', '1년차', '2년차', '3년차', '4년차', '5년차'], rows, col_w=[1.75] + [1.05] * 5, size=11.5,
              align=['l', 'r', 'r', 'r', 'r', 'r'], pad=0.075, label='pl table')
    cum = []; c = 0
    for v in B['op']: c += v; cum.append(c)
    fy = y0 + h + 0.3
    text(s, MX, fy, lw, 0.28, '자금 흐름 (억 원, 기본 계획)', size=12.5, bold=True)
    frows = [['누적 영업손익'] + [f(v) for v in cum], ['조달 재원', 'Seed', 'Seed', '시리즈 A', '시리즈 A', '시리즈 A']]
    table(s, MX, fy + 0.36, lw, None, frows, col_w=[1.75] + [1.05] * 5, size=11.5, align=['l', 'r', 'r', 'r', 'r', 'r'], pad=0.075, label='cash')
    hline(s, MX, fy + 0.36, lw, color=T['text'], lw=1.0)
    y12 = -(B['op'][0] + B['op'][1]); y35 = -(B['op'][2] + B['op'][3] + B['op'][4])
    text(s, MX, fy + 1.2, lw, 0.6,
         [[('1·2년차 영업손실 ', {}), (f'{y12:.1f}억 원', {'bold': True, 'color': T['text']}), ('은 Seed로 충당, 3~5년차 영업손실 ', {}),
           (f'{y35:.1f}억 원', {'bold': True, 'color': T['text']}), ('은 시리즈 A로 조달 계획', {})]],
         size=11.5, color=T['text2'], label='cash note')
    rx = MX + lw + 0.5; rw = W - MX - rx
    blocks = [('주요 가정', ['핸드 1,500만 원 (원가 950 → 750만 원)', '작업 소프트웨어 300만 원, 유지보수 연 150만 원', '유료 PoC 1·4·5·6·6건 (연도별)',
                         '운영비 1·2년차 = Seed 집행 계획, 3~5년차 평균 14·19·23명']),
              ('민감도 (5년차)', ['판매량 −30%: 매출 31.4억, 영업손익 −7.1억', '파트너 채널 1년 지연: 매출 32.3억, 영업손익 −6.4억', '판매량 −50%: 매출 22.4억, 영업손익 −11.9억']),
              ('미반영 상승 요인', ['대규모 급식·외식 체인 반복 도입', '로봇·가전 기업 제품 탑재·라이선스', '가정용 주방 확대 (수치 미산정)'])]
    y = y0
    for t_, items in blocks:
        text(s, rx, y, rw, 0.28, t_, size=12.5, bold=True)
        hline(s, rx, y + 0.35, rw, color=T['text'], lw=1.0)
        hh = text_h(items, 11, rw - 0.18, space_after=2)
        text(s, rx, y + 0.44, rw, hh + 0.05, items, size=11, bullet='•', indent=0.18, space_after=2, color=T['text2'], label='fin ' + t_)
        y += 0.44 + hh + 0.26
    foot(s, 10, note='상세 손익·산정 기준은 부록 A11 · 3~5년차 누적 영업손실 약 17.1억 원은 후속 투자로 조달 계획')
    notes(s, f'기본 계획: 매출 {B["rev"][0]:.1f} → {B["rev"][4]:.1f}억 원(5년차), 영업손익 5년차 손익분기 근접. 대규모 체인·OEM·가정용 매출은 제외. '
             '민감도: 판매량 −30% 시 5년차 매출 31.4억·영업손익 −7.1억. 3~5년차 영업손실은 시리즈 A로 조달.')


# ---------------------------------------------------------------- 11 schedule
def s11(prs):
    s = new_slide(prs, '11 schedule')
    y0 = bp_header(s, 10, '추진 일정', '24개월 4단계 추진, 단계별 점검 후 다음 자금 집행')
    lw = 3.3; qn = 8; qw = (CW - lw) / qn; rh = 0.31
    phases = [('기술 검증', 'M0~M6'), ('고객 검증', 'M6~M12'), ('제품 검증', 'M12~M18'), ('확장 검증', 'M18~M24')]
    for i, (a, b) in enumerate(phases):
        x = MX + lw + i * 2 * qw
        rect(s, x + 0.02, y0, 2 * qw - 0.04, 0.3, fill=T['dark'] if i == 3 else '4A4F57')
        text(s, x + 0.02, y0, 2 * qw - 0.04, 0.3, f'{a}  {b}', size=10.5, bold=True, color='FFFFFF', align='c', anchor='m', label='ph ' + a)
    hy = y0 + 0.36
    for q in range(qn):
        text(s, MX + lw + q * qw, hy, qw, 0.24, f'{q + 1}분기', size=9.5, color=T['muted'], align='c', check=False)
    hline(s, MX, hy + 0.28, CW, color=T['text'], lw=1.0)
    tasks = [('법인 설립·핵심 인력 채용', 0, 5), ('구동 방식 비교·알파 시제품', 0, 2), ('고객 인터뷰 30곳', 0, 1), ('주방 작업 소프트웨어 V1 (6종)', 1, 4),
             ('유료 실증 (PoC) 1건 → 5건', 3, 8), ('설계 확정·BOM·공급사', 4, 6), ('내구 시험 (30만 회 목표)', 4, 7), ('로봇 B 통합·이식 검증', 4, 8),
             ('가정용 주방 환경 벤치 검증', 6, 8), ('재구매·첫 판매', 6, 8), ('시리즈 A 준비', 5, 8)]
    y = hy + 0.36
    for i, (t_, a, b) in enumerate(tasks):
        text(s, MX, y, lw - 0.15, rh, t_, size=10.5, anchor='m', label='task ' + t_)
        for q in range(qn):
            x = MX + lw + q * qw
            rect(s, x + 0.02, y + 0.06, qw - 0.04, rh - 0.12, fill=(T['accent'] if a <= q < b else 'F1F2F4'))
        y += rh
    hline(s, MX, y + 0.04, CW)
    gy = y + 0.14
    text(s, MX, gy, lw - 0.15, 0.5, '점검 시점 (미달 시 결정)', size=10.5, bold=True, anchor='m')
    gates = [('M6', '토크·반복성 미확보 → 핸드 구조 재검토'), ('M12', '지불의사 없음 → 고객군·작업 재정의'), ('M18', '재사용률 낮음 → 제품 구조 재검토'),
             ('M24', '재구매 없음 → 시리즈 A 확장 보류')]
    for i, (m, d) in enumerate(gates):
        x = MX + lw + i * 2 * qw
        text(s, x + 0.05, gy, 2 * qw - 0.1, 0.5, [[(m + '  ', {'bold': True, 'color': T['accent']}), (d, {})]], size=9.5, color=T['text2'], label='gate ' + m)
    foot(s, 11, note='분기는 투자 집행일 기준 · 단계별 점검 기준 상세는 부록 A2')
    notes(s, '24개월을 기술 검증(M0~M6), 고객 검증(M6~M12), 제품 검증(M12~M18), 확장 검증(M18~M24)으로 나누고, 각 점검 시점에 미달하면 범위 축소 또는 방향 전환 후 다음 자금 집행.')


# ---------------------------------------------------------------- 12 use of funds
def s12(prs):
    s = new_slide(prs, '12 use of funds')
    SP = M['seed']
    y0 = bp_header(s, 11, '자금 소요 및 사용 계획', 'Seed 20억 원으로 24개월 운영, 매출 없이도 운영 가능')
    names = {'핵심 인력 (8명 단계 채용)': ('인건비 (8명 단계 채용)', '창업자 2명 + 엔지니어 6명, 4대보험·퇴직충당 포함'),
             'Prototype · 내구시험': ('시제품·내구 시험', '알파·베타 시제품, 반복 내구 시험'),
             'Robot 2종 · 시험 Cell': ('로봇 2종·시험 설비', '협동로봇 2종, 주방·산업 시험 셀'),
             '고객 PoC · 현장통합(비청구)': ('실증·현장 통합', '고객 주방 실증 중 비청구 비용'),
             'SW · AI · Data': ('소프트웨어·데이터', '작업 소프트웨어, 데이터 수집 장비'),
             '제조 · 품질 · 안전 · IP': ('제조·품질·안전·지재권', 'BOM·공급사, 위생·안전 검토, 특허 출원'),
             'Kitchen Bench Demo': ('가정용 환경 벤치', '가정용 주방 환경 재현 검증'),
             '운영 (임차·법무·회계·보험·출장)': ('운영비', '임차·법무·회계·보험·출장'),
             '예비비 · 운전자본': ('예비비·운전자본', '24개월 후 잔존 (매출 없을 때)')}
    lw = 7.6
    rows = []
    for k, v in SP['uof']:
        nm, d = names.get(k, (k, ''))
        rows.append([(nm, {'bold': True}), d, f'{v:.1f}', f'{v / 20 * 100:.0f}%'])
    rows.append([('합계', {'bold': True}), '', (f'{SP["uof_total"]:.1f}', {'bold': True}), ('100%', {'bold': True})])
    h = table(s, MX, y0, lw, ['항목', '내용', '금액 (억 원)', '비중'], rows, col_w=[2.2, 3.4, 1.2, 0.8], size=11, align=['l', 'l', 'r', 'r'], pad=0.06,
              label='uof table')
    rx = MX + lw + 0.5; rw = W - MX - rx
    cont = SP['uof'][-1][1]
    blocks = [('집행 구조', [f'18개월 핵심 운영 {SP["core18"]:.1f}억 원 (설계 확정·첫 재구매까지)', f'6개월 연장 {SP["ext6"]:.1f}억 원 (M18 점검 통과 시 집행)',
                          f'예비비·운전자본 {cont:.1f}억 원']),
              ('손익 연결', [f'운영비 1년차 {SP["opex_y1"]:.1f}억 + 2년차 {SP["opex_y2"]:.1f}억 = {SP["opex_y1"] + SP["opex_y2"]:.1f}억 원', '매출원가는 매출로 충당, 정부지원금·공동개발비 미반영']),
              ('후속 투자', ['시리즈 A: M15부터 준비, M24 전후 유치 목표', '3~5년차 누적 영업손실 약 17.1억 원 (기본 계획)', ph('시리즈 A 목표 규모 [입력 필요]')])]
    y = y0
    for t_, items in blocks:
        text(s, rx, y, rw, 0.28, t_, size=12.5, bold=True)
        hline(s, rx, y + 0.35, rw, color=T['text'], lw=1.0)
        paras = [ph(it) if '[' in it else it for it in items]
        hh = text_h(items, 11, rw - 0.18, space_after=2)
        text(s, rx, y + 0.44, rw, hh + 0.05, paras, size=11, bullet='•', indent=0.18, space_after=2, color=T['text2'], label='use ' + t_)
        y += 0.44 + hh + 0.28
    foot(s, 12, note='인건비 기준: 창업자 연 5,000만 원, 엔지니어 연 7,000만 원 + 15% · 채용 일정은 13장, 상세 부록 A12')
    notes(s, f'Seed 20억 원: 인건비 {SP["uof"][0][1]:.1f}억, 시제품·내구 시험 2.7억, 로봇 2종·시험 설비 1.3억, 실증·현장 통합 1.2억, 소프트웨어·데이터 0.6억, '
             f'제조·품질·안전·지재권 1.1억, 가정용 환경 벤치 0.3억, 운영비 1.5억, 예비비 {cont:.1f}억. 18개월 핵심 운영 + 6개월 연장 구조. 매출이 없어도 24개월 운영.')


# ---------------------------------------------------------------- 13 organization
def s13(prs):
    s = new_slide(prs, '13 team')
    y0 = bp_header(s, 12, '조직 및 인력', '창업자 2명과 핵심 인력 6명으로 구성')
    text(s, MX, y0, CW, 0.28, '창업자', size=13, bold=True)
    frows = [[('대표 · 사업/제품', {'bold': True}), ph('[성명 입력 필요]'), ph('[주방·자동화 관련 경력, 기간 입력 필요]'), ph('[창업 계기·현장에서 확인한 문제 입력 필요]')],
             [('CTO · 핸드 메카트로닉스', {'bold': True}), ph('[성명 입력 필요]'), ph('[핸드·로봇·제어 개발 이력, 시제품·논문·특허 입력 필요]'), ph('[핸드·제어 개발 역량 근거 입력 필요]')]]
    h1 = table(s, MX, y0 + 0.38, CW, ['역할', '성명', '주요 경력', '이 사업과의 연결'], frows, col_w=[2.3, 1.8, 4.1, 3.63], size=11, pad=0.085, label='founders')
    hy = y0 + 0.38 + h1 + 0.3
    lw = 7.2
    text(s, MX, hy, lw, 0.28, '핵심 인력 채용 계획 (6명)', size=13, bold=True)
    roles = {'기구·구동 엔지니어': '손가락·구동부 설계, 시제품 제작', '제어·임베디드 엔지니어': '힘·촉각 제어, 보드·펌웨어', 'Robot SW · Skill 엔지니어': '작업 소프트웨어, 로봇 연동',
             '현장 통합(FAE) 엔지니어': '고객 주방 설치·실증 운영', 'Vision · 조작 AI 엔지니어': '물체 인식, 작업 학습', 'DFM · 품질 엔지니어': '양산 설계, 품질·위생 검증'}
    kname = {'Robot SW · Skill 엔지니어': '로봇 SW·작업 소프트웨어', '현장 통합(FAE) 엔지니어': '현장 통합 엔지니어', 'Vision · 조작 AI 엔지니어': '비전·조작 AI 엔지니어',
             'DFM · 품질 엔지니어': '설계·품질 엔지니어'}
    hr = [[(kname.get(r, r), {'bold': True}), f'M{st}', roles.get(r, '')] for r, st, _ in M['hires'] if r in roles]
    table(s, MX, hy + 0.38, lw, ['직무', '합류', '주요 업무'], hr, col_w=[2.6, 0.8, 3.8], size=11, pad=0.06, label='hires')
    rx = MX + lw + 0.5; rw = W - MX - rx
    text(s, rx, hy, rw, 0.28, '창업팀 역량 요약', size=13, bold=True)
    caps = [('문제 이해', '[현장에서 문제를 확인한 경험 입력 필요]'), ('개발 역량', '[핸드·로봇·제어·AI 개발 역량 입력 필요]'),
            ('고객 접근', '[외식·급식·주방설비·로봇 SI 관계 입력 필요]'), ('참여 조건', '[전업 참여·자기자본 투자·공동창업 계약 입력 필요]')]
    kv_table(s, rx, hy + 0.38, rw, [(a, ph(b)) for a, b in caps], kw=1.15, size=11, pad=0.07, label='caps')
    foot(s, 13, note='확인되지 않은 이력·성과는 기재하지 않음 · 외부 제출 전 실제 정보로 교체')
    notes(s, '창업자 2명(대표, CTO)과 6명 단계 채용. 창업자 경력·역량은 확인되지 않아 자리만 둠. 채용 순서: 기구·구동(M2), 제어·임베디드(M3), 로봇 SW(M5), '
             '현장 통합(M8), 비전·AI(M10), 설계·품질(M13).')


# ---------------------------------------------------------------- 14 investment proposal
def s14(prs):
    s = new_slide(prs, '14 proposal')
    y0 = bp_header(s, 13, '투자 제안', 'Seed 20억 원 투자 제안')
    lw = 4.2
    text(s, MX, y0, lw, 0.28, '투자 조건', size=13, bold=True)
    terms = [('투자 금액', [('20억 원', {'bold': True, 'color': T['accent']})]), ('투자 형태', ph('[보통주·상환전환우선주 등 입력 필요]')),
             ('기업가치', ph('[투자 전 기업가치 입력 필요]')), ('지분율', ph('[입력 필요]')), ('자금 사용 기간', '24개월 (18개월 + 6개월 연장)'),
             ('라운드 현황', ph('[참여 투자자·진행 상황 입력 필요]'))]
    kv_table(s, MX, y0 + 0.38, lw, terms, kw=1.35, size=11.5, pad=0.075, label='terms')
    mx_ = MX + lw + 0.45; mw = 3.8
    text(s, mx_, y0, mw, 0.28, '투자 후 24개월 목표', size=13, bold=True)
    goals = [('유료 PoC', '5건 이상'), ('재구매 고객', '2곳 이상'), ('공동개발 고객', '3곳'), ('승인 작업 완료율', '95% 이상'), ('내구성', '30만 회'),
             ('로봇 호환', '2종'), ('양산 설계', '설계 확정·BOM')]
    hline(s, mx_, y0 + 0.38, mw, color=T['text'], lw=1.0)
    table(s, mx_, y0 + 0.38, mw, None, [[k, (v, {'bold': True, 'align': 'r'})] for k, v in goals], col_w=[mw - 1.5, 1.5], size=11.5, pad=0.065, label='goals')
    rx = mx_ + mw + 0.45; rw = W - MX - rx
    blocks = [('투자 의미', ['콘셉트 단계에서 실제 주방 실증·첫 판매까지 가는 자금', '세 가지 검증: 실제 주방 작동, 고객 지불, 작업 소프트웨어 재사용']),
              ('후속 투자', ['시리즈 A: 24개월 목표 달성 후 유치 계획', ph('목표 규모 [입력 필요]')]),
              ('회수 방안 (장기 가능성)', ['로봇·주방설비·가전 기업의 전략적 인수', '기술특례 상장 (확정된 논의 없음)'])]
    y = y0
    for t_, items in blocks:
        text(s, rx, y, rw, 0.28, t_, size=13, bold=True)
        hline(s, rx, y + 0.35, rw, color=T['text'], lw=1.0)
        plain = [''.join(r[0] for r in it) if isinstance(it, list) else it for it in items]
        hh = text_h(plain, 11, rw - 0.18, space_after=2)
        text(s, rx, y + 0.44, rw, hh + 0.05, items, size=11, bullet='•', indent=0.18, space_after=2, color=T['text2'], label='prop ' + t_)
        y += 0.44 + hh + 0.26
    by = 6.2
    rect(s, MX, by, CW, 0.62, fill=T['soft'])
    text(s, MX + 0.25, by, CW - 0.5, 0.62, [[('연락처   ', {'bold': True, 'color': T['text']})] + ph('대표자 [입력 필요]  ·  이메일 [입력 필요]  ·  전화 [입력 필요]')],
         size=11.5, color=T['text2'], anchor='m', label='contact')
    foot(s, 14, note='목표는 계획이며 실적 아님 · 단계별 점검 기준 부록 A2 · 사실·가정 구분 부록 A1')
    notes(s, 'Seed 20억 원, 24개월. 투자 조건·라운드 현황은 입력 필요. 24개월 목표: 유료 PoC 5건, 재구매 2곳, 공동개발 3곳, 완료율 95%, 내구 30만 회, 로봇 2종, 양산 설계. '
             '후속 투자는 시리즈 A, 회수는 전략적 인수·기술특례 상장 가능성(확정 논의 없음).')


MAIN = [s01, s02, s03, s04, s05, s06, s07, s08, s09, s10, s11, s12, s13, s14]
