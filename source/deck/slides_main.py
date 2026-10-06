# SoftHand Seed 투자유치 사업계획서 v5 (최종본) - main slides (17).
# Content, numbers and business order follow the business plan (사업계획서, 2026-10-06): hand + tool-use control software
# for robot SI / manufacturing first, ceiling dual-arm kitchen as the application product from year 3.
# Business-plan format: numbered sections, plain Korean statements, tables and numbers first, two concept images only,
# every unverified item marked 목표 / 가정 / 검증 예정 / [입력 필요].
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
PITCH = ('저희는 로봇이 사람이 쓰는 도구를 잡고 실제 작업까지 수행하도록 하는 소프트 로봇핸드와 제어 소프트웨어를 개발합니다. '
         '초기에는 4지 핸드를 기존 로봇에 부착하여 반복 취급과 제한된 도구 작업을 검증하고, 이를 5지 핸드와 천장 이동형 양팔 로봇 주방으로 확장합니다. '
         'Seed 20억원을 통해 24개월 내 제품 성능과 유료 고객의 경제성을 입증하고 반복 판매 기반을 확보하고자 합니다.')


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


def block(s, x, y, w, title, items, size=11, gap=2, tsize=12.5, label=None, bullet='•'):
    """Block title + rule + bulleted lines. Items: str (with optional [..] placeholder) or run lists. Returns bottom y."""
    text(s, x, y, w, 0.28, title, size=tsize, bold=True)
    hline(s, x, y + 0.35, w, color=T['text'], lw=1.0)
    paras = [ph(it) if isinstance(it, str) and '[' in it else it for it in items]
    plain = [''.join(r[0] for r in it) if isinstance(it, list) else it for it in items]
    ind = 0.18 if bullet else 0
    hh = text_h(plain, size, w - ind, space_after=gap)
    text(s, x, y + 0.44, w, hh + 0.05, paras, size=size, bullet=bullet, indent=ind or 0.2, space_after=gap, color=T['text2'],
         label=label or 'block ' + title)
    return y + 0.44 + hh + 0.05


def eok(v, d=2):
    return f'{v:.{d}f}'.replace('-', '−')


B_ = lambda t: (t, {'bold': True})


# ---------------------------------------------------------------- cover
def s01(prs):
    s = new_slide(prs, '01 cover')
    text(s, MX, 0.7, 8, 0.3, '[회사명 입력 필요]', size=13, bold=True, color=T['accent'])
    text(s, MX, 1.95, CW, 0.32, '투자유치 사업계획서 (Seed)', size=14, bold=True, color=T['text2'])
    text(s, MX, 2.45, CW, 1.45, '사람용 도구를 잡고 사용하는\n소프트 로봇핸드 개발 및 사업화', size=36, bold=True, line=0.98, label='cover title')
    text(s, MX, 3.98, CW, 0.32, '4지·5지 소프트 로봇핸드와 도구 사용 제어 소프트웨어, 천장 이동형 양팔 로봇 주방으로 확장', size=15,
         color=T['text2'], label='cover sub')
    y = 4.85
    hline(s, MX, y, CW, color=T['text'], lw=1.0)
    items = [('투자 유치 금액', '20억 원 (Seed)'), ('자금 사용 기간', '24개월'), ('초기 고객', '로봇 SI·제조기업'), ('작성일', '2026년 10월 6일')]
    cw4 = CW / 4
    for i, (k, v) in enumerate(items):
        x = MX + i * cw4 + (0.2 if i else 0)
        if i: vline(s, MX + i * cw4, y + 0.22, 0.7)
        text(s, x, y + 0.2, cw4 - 0.35, 0.26, k, size=11, color=T['muted'])
        text(s, x, y + 0.5, cw4 - 0.35, 0.4, v, size=17, bold=True, color=T['accent'] if i == 0 else T['text'], label='cover ' + k)
    hline(s, MX, y + 1.15, CW)
    text(s, MX, H - 0.78, CW, 0.26, [ph('대표자 [입력 필요]  ·  이메일·연락처 [입력 필요]')], size=11, color=T['muted'], check=False)
    text(s, MX, H - 0.5, CW, 0.22, '본 자료의 가격·사양·일정·시장 산정·매출은 투자 검토용 제안·가정이며 실적이나 확정 수주가 아님', size=9,
         color=T['muted'], check=False)
    notes(s, '사람용 도구를 잡고 사용하는 소프트 로봇핸드 개발 및 사업화. Seed 20억 원, 24개월. 초기 고객은 로봇 SI와 반복 취급 공정을 가진 제조기업, '
             '로봇 주방은 3년차 이후 응용 제품.')


# ---------------------------------------------------------------- 01 summary
def s02(prs):
    s = new_slide(prs, '02 summary')
    B = M['base']
    y0 = bp_header(s, 1, '투자 제안 요약', '핸드·제어 소프트웨어로 시작해 로봇 주방으로 확장하는 사업')
    lw = 4.3
    text(s, MX, y0, lw, 0.28, '회사 현황', size=13, bold=True)
    rows = [('회사명', ph('[입력 필요]')), ('대표자', ph('[입력 필요]')), ('설립', ph('[설립일 또는 예정일 입력 필요]')),
            ('소재지', ph('[입력 필요]')), ('핵심 인력', '7명 단계 채용 계획\n(사업·제품 1, 기구/구동 2, 제어 1, AI 2, 통합 1)'),
            ('사업 분야', '소프트 로봇핸드, 도구 사용 제어 소프트웨어, 로봇 주방'),
            ('개발 단계', ph('개발 구상·계획 단계, 시제품·시험 데이터 미확인 [보유 시 입력]')), ('지식재산', ph('확인된 출원 없음 [보유 시 입력]'))]
    kv_table(s, MX, y0 + 0.38, lw, rows, kw=1.15, size=11, label='company')
    rx = MX + lw + 0.45; rw = W - MX - rx
    text(s, rx, y0, rw, 0.28, '사업 요약', size=13, bold=True)
    rows2 = [('핵심 가치', '도구마다 전용 그리퍼를 바꾸는 부담을 줄이고, 형상이 다른 물체 취급과 도구 사용을 하나의 핸드·제어 플랫폼으로 확대'),
             ('초기 제품', '4지 핸드(SoftHand-4), 로봇 장착 어댑터, 비전·촉각 제어 SDK, 제한된 도구 작업 패키지'),
             ('초기 고객', '로봇 시스템통합(SI) 업체, 반복 취급 공정 보유 제조기업 → 유료 실증 후 주방 제조사·상업 주방 운영사와 공동 제품화'),
             ('확장 제품', '5지 정밀 조작 핸드(SoftHand-5), 천장 이동형 양팔 로봇 주방, 검증된 레시피 실행 소프트웨어'),
             ('투자 요청', [('Seed 20억 원', {'bold': True, 'color': T['accent']}), (' · 24개월 개발·유료 실증 · 기업가치·지분율 협의', {})]),
             ('24개월 목표', '4지 제품 검증, 5지 알파 시제품, 로봇 주방 제한 메뉴 실증\n유료 실증 5건, 반복 발주 고객 2곳'),
             ('5년차 계획', f'매출 {B["rev"][4]:.0f}억 원, 영업이익 {eok(B["op"][4])}억 원 (핸드 350대·주방 셀 25대, 기준 시나리오·가정)'),
             ('후속 투자', '성능 시험·고객 경제성·반복 발주 확인 후 양산·주방 상품화 자금 조달 (18~24개월 시점)')]
    kv_table(s, rx, y0 + 0.38, rw, rows2, kw=1.3, size=11, label='summary')
    foot(s, 2, note='작성 전제: 법인·창업팀·특허·시제품·고객 계약·매출·보유 자금 미확인, 가격·일정·매출은 제안·가정 (부록 A1)')
    notes(s, '대표자 발표 문안: ' + PITCH)


# ---------------------------------------------------------------- 02 customer problem
def s03(prs):
    s = new_slide(prs, '03 problem')
    y0 = bp_header(s, 2, '고객 문제와 사업 기회', '다품종 작업의 그리퍼 교체·재설정 부담과 사람용 도구 조작의 한계')
    lw = 7.3
    text(s, MX, y0, lw, 0.28, '고객별 문제와 제공 가치', size=13, bold=True)
    rows = [[B_('제조업체·로봇 SI'), '다품종 작업마다 그리퍼·지그 변경, 작업 전환 시 재설정 부담', '공통 핸드와 작업별 소프트웨어로 교체·재설정 시간 절감'],
            [B_('로봇 OEM·연구기관'), '사람용 도구 조작에 필요한 손·센서·제어 통합 부담', '검증된 핸드 모듈과 API, 시험 데이터 제공'],
            [B_('상업 주방 운영사'), '반복 취급·투입·정리 업무와 작업자 편차', '정해진 재료·도구·메뉴에서 반복 업무 자동화'],
            [B_('고급 주방 제조사'), '기존 주방 설비의 기능 차별화와 신제품 필요', '수납형 로봇 모듈과 조리 소프트웨어 공동 개발']]
    h = table(s, MX, y0 + 0.38, lw, ['고객', '현장 문제', '제공 가치'], rows, col_w=[1.7, 2.8, 2.8], size=11, pad=0.07, label='customer table')
    by = y0 + 0.38 + h + 0.3
    paras = [[('도구를 잡는 것과 사용하는 것의 차이', {'bold': True, 'color': T['text'], 'size': 12})],
             [('손잡이 파지에 더해 작업점 위치, 반력·토크, 미끄러짐, 손목 자세, 작업 완료 판정이 필요', {})],
             [('드라이버 회전 토크, 플라이어 손잡이 개폐, 프라이팬 무게중심 변화는 각각 별도의 동작·힘 제어', {})],
             [('투자 지표  ', {'bold': True, 'color': T['accent']}), ('실제 작업 성공률과 사람 개입 시간 (파지 영상만으로 판단하지 않음)', {})]]
    th = text_h(paras, 11.5, lw - 0.44, space_after=4)
    rect(s, MX, by, lw, th + 0.4, fill=T['soft'])
    text(s, MX + 0.22, by + 0.18, lw - 0.44, th + 0.05, paras, size=11.5, color=T['text2'], space_after=4, label='tool use box')
    rx = MX + lw + 0.5; rw = W - MX - rx
    text(s, rx, y0, rw, 0.28, '근거 지표 (공개 자료)', size=13, bold=True)
    stats = [('75%', '기존 로봇 도입 총소유비용 중\n초기 셋업·재설계 비중 (BCG, 2026)'),
             ('60만 대+', '2025년 세계 산업용 로봇 신규 설치\n(2024년 약 54.2만 대, IFR)'),
             ('3.0만 대', '2025년 국내 산업용 로봇 신규 설치\n세계 4위 시장 (IFR)'),
             ('1,220대', '한국 제조업 근로자 1만 명당 로봇 수\n세계 1위 (IFR, 2026)')]
    y = y0 + 0.38
    for i, (n, d) in enumerate(stats):
        hline(s, rx, y, rw, color=T['text'] if i == 0 else T['line'], lw=1.0 if i == 0 else 0.75)
        text(s, rx, y + 0.12, 1.3, 0.42, n, size=19, bold=True, color=T['accent'] if i == 0 else T['text'], label='stat ' + n)
        text(s, rx + 1.35, y + 0.12, rw - 1.35, 0.5, [d], size=10.5, color=T['text2'], label='stat d ' + n)
        y += 0.8
    hline(s, rx, y, rw)
    text(s, rx, y + 0.12, rw, 0.5, ['설치 기반을 보여주는 참고 지표, 당사 시장 규모와 다름', '시장 규모는 10장에서 상향식으로 산정'],
         size=10, color=T['muted'], label='stat note')
    foot(s, 3, note='출처: BCG(2026.4), IFR World Robotics 2025·2026 · 부록 A9·A15')
    notes(s, '고객 문제: 제조·SI는 작업마다 그리퍼·지그 교체와 재설정, 로봇 OEM은 손·센서·제어 통합, 주방 운영사는 반복 취급과 작업자 편차, 주방 제조사는 차별화. '
             '근거: 기존 로봇 도입 총소유비용의 약 75%가 초기 셋업·재설계(BCG). 산업용 로봇 설치 2025년 60만 대 이상, 한국 3.0만 대·로봇 밀도 1,220대(IFR). '
             '도구 사용은 파지 이상의 제어가 필요하므로 투자 지표는 작업 성공률과 사람 개입 시간.')


# ---------------------------------------------------------------- 03 products
def s04(prs):
    s = new_slide(prs, '04 products')
    y0 = bp_header(s, 3, '제품 구성과 사업 범위', '초기 제품은 4지 핸드와 제어 SDK, 5지 핸드와 로봇 주방은 확장 제품')
    iw, ih = 2.2, 2.75
    rect(s, MX, y0, iw, ih, fill='EEF0F2')
    cutout(s, REN('product.png'), MX + 0.1, y0 + 0.12, iw - 0.2, ih - 0.24)
    rx = MX + iw + 0.35; rw = W - MX - rx
    rows = [[B_('SoftHand-4'), '엄지 대향 기능을 포함한 4지 구조, 교체형 접촉 패드, 촉각·힘 제어, 로봇 장착 어댑터', '로봇 SI·제조업체\n핸드 판매·설치비', ('초기 제품', {'bold': True, 'color': T['accent']})],
            [B_('ToolSkill SDK'), '도구·손잡이 인식, 파지 계획, 힘·토크 제한, 실패 복구, 로그, 제한된 도구 작업 패키지', 'OEM·SI\n연간 소프트웨어·지원 계약', ('초기 제품', {'bold': True, 'color': T['accent']})],
            [B_('SoftHand-5'), '5지 구조, 선택 관절 독립 구동, 양손 협조와 세밀한 조작', '로봇 OEM·고급 조작 수요\n핸드·개발 키트', '확장\n(24개월 알파)'],
            [B_('Ceiling Kitchen'), 'LM 이동축, 역설치 양팔 로봇, 핸드, 센서, 인덕션·세척·수납 연동', '주방 제조사·상업 주방\n공동개발·시스템 판매', '확장\n(3년차~ 판매)']]
    h = table(s, rx, y0, rw, ['제품 (가칭)', '핵심 구성', '초기 구매자 · 수익', '사업 단계'], rows, col_w=[1.6, 3.85, 2.3, rw - 7.75],
              size=11, pad=0.07, label='product table')
    by = max(y0 + ih, y0 + h) + 0.28
    text(s, MX, by, CW, 0.28, '작업군별 개발 순서 (승인된 도구 모델부터 등록, 손잡이 위치·허용 하중 관리)', size=13, bold=True)
    st = [('1단계', '식기·용기 정렬·적층', '파손·끼임 방지, 젖은 표면 미끄러짐, 적층 안정성'),
          ('2단계', '드라이버·스패너', '저토크 작업부터, 반력·토크 검증'),
          ('2~3단계', '플라이어·집게\n프라이팬·냄비', '손잡이 유지 개폐, 내용물 질량·모멘트, 양손 분담'),
          ('3단계', '오븐', '문·손잡이 조작, 트레이 취급, 열·끼임 관리'),
          ('후속 단계', '나이프·해머', '절단·충격 특성, 파지 이탈 검증 후 제한 작업'),
          ('병행 기술개발', '동적 물체·유연체', '속도·형상 변화·가림 조건별 분리 평가')]
    cw6 = CW / 6
    rows2 = [[(b, {'bold': True}) for _, b, _ in st], [(c, {'color': T['text2'], 'size': 10}) for _, _, c in st]]
    table(s, MX, by + 0.38, CW, [a for a, _, _ in st], rows2, col_w=[cw6] * 6, size=11, pad=0.06, label='stage table', header_color=T['accent'])
    foot(s, 4, note='제조용·주방용 접촉부는 분리, 공통 제어기·통신·손목 장착 구조는 유지 · 이미지는 콘셉트 렌더링 · 상세 부록 A2')
    notes(s, '초기 제품: SoftHand-4(4지 핸드)와 ToolSkill SDK(도구 사용 제어 소프트웨어)를 로봇 SI·제조업체에 판매. 확장 제품: SoftHand-5(24개월 알파), '
             'Ceiling Kitchen(3년차부터 주방 제조사·상업 주방과 공동 판매). 작업군은 식기·용기 정렬부터 시작해 저토크 공구, 집게·팬, 오븐 순으로 확대하고 칼·해머는 후속 단계.')


# ---------------------------------------------------------------- 04 hand technology
def s05(prs):
    s = new_slide(prs, '05 hand tech')
    y0 = bp_header(s, 4, '소프트 핸드 핵심 기술', '소프트 접촉면과 하중 지지 골격을 결합한 하이브리드 핸드',
                   '도구를 감싸는 순응성과 작업 반력을 견디는 강성을 함께 확보 · 구동 방식은 3개월 내 비교 시험으로 결정')
    lw = 7.4
    rows = [[B_('구동부'), '전동 텐던을 기준 후보로 소형 유압·공압과 비교', '손 무게, 유지력, 응답, 누설, 소음, 소비전력, 정비비'],
            [B_('가변 순응성'), '탄성요소·장력 제어, 필요 시 잠금기구', '접촉 충격 완화와 도구 토크 유지의 균형'],
            [B_('감각부'), '손끝·손바닥 접촉센서, 관절·장력 센서, 손목 6축 힘·토크 센서', '젖음·열·오염 조건의 편차와 재교정'],
            [B_('접촉부'), '교체형 패드·외피, 식품용 별도 재질 선정', '미끄럼·마모·세척·재질 적합성 시험'],
            [B_('로봇 장착'), '플랜지 어댑터, 공구중심점 교정, 통신 드라이버', '대표 로봇 2개 플랫폼에서 실제 통합 검증']]
    h = table(s, MX, y0, lw, ['기술 요소', '개발 내용', '검증 기준'], rows, col_w=[1.35, 3.25, 2.8], size=11, pad=0.08, label='tech table')
    block(s, MX, y0 + h + 0.3, lw, '구조 설계 방향', ['엄지 대향, 손가락 굽힘, 제한적인 벌림 동작 설계',
                                                 '4지: 안정적인 감싸쥐기와 비용 우선 · 5지: 재파지와 정밀 조작 확장 우선'], size=11, label='structure')
    rx = MX + lw + 0.45; rw = W - MX - rx
    y = block(s, rx, y0, rw, '하중 설계', ['손의 파지 하중과 로봇 팔 가반하중은 별도로 설계',
                                          '팔 가반하중: 손·어댑터·센서·도구·내용물의\n질량과 무게중심을 합산',
                                          '예: 3kg 냄비, 무게중심이 파지점에서 0.20m\n→ 정적 모멘트 약 5.9N·m',
                                          '가속·충격 시 요구치 증가, 큰 냄비는 양손 지지\n또는 거치대 보조'], size=11, label='load')
    block(s, rx, y + 0.22, rw, '도구별 제어 요구', ['드라이버: 축 정렬·누름 힘·회전 토크', '스패너: 면접촉 유지·재파지', '플라이어: 손잡이 개폐력',
                                                 '팬·냄비: 수평 유지, 쏟아짐 방지', '해머·나이프: 피로·이탈, 절삭 저항·날 위치 별도 검증'], size=11, label='tool ctrl')
    foot(s, 5, note='유압 채택 시 호스 굽힘 수명·누설 감지·격리 포함 · 특허 가능성은 선행기술 조사 후 판단 · 상세 부록 A3')
    notes(s, '탄성 외피·패드와 경량 관절 골격을 결합한 하이브리드 구조. 구동부는 전동 텐던을 기준 후보로 유압·공압과 3개월 내 비교 시험. '
             '감각부는 손끝·손바닥 접촉, 관절·장력, 손목 6축 힘·토크. 하중 예시: 3kg 냄비, 0.20m에서 정적 모멘트 약 5.9N·m.')


# ---------------------------------------------------------------- 05 vision AI
def s06(prs):
    s = new_slide(prs, '06 vision')
    y0 = bp_header(s, 5, '비전 AI와 촉각·힘 제어', '인식부터 작업 결과 확인까지 하나의 제어 흐름으로 개발')
    text(s, MX, y0, CW, 0.28, '제어 흐름', size=13, bold=True)
    steps = ['상부 RGB-D·손목 카메라', '객체 분할·도구 기능 부위 인식', '위치·자세 또는 변형 상태 추정', '이동 예측', '파지 후보와 작업 계획',
             '촉각·힘 기반 접촉 제어', '작업 결과 확인', '재파지·재시도·정지']
    cw8 = CW / 8
    h0 = table(s, MX, y0 + 0.38, CW, [str(i + 1) for i in range(8)], [[(t, {}) for t in steps]], col_w=[cw8] * 8, size=10.5, pad=0.06,
               label='pipeline', header_color=T['accent'])
    ty = y0 + 0.38 + h0 + 0.3
    lw = 7.4
    text(s, MX, ty, lw, 0.28, '조작 기술과 실패 대응', size=13, bold=True)
    rows = [[B_('강체·도구 인식'), '손잡이·날·회전축·작업점 구분, 6-DoF 자세 추정', '반사·가림 시 다른 시점 재관측'],
            [B_('동적 물체 추적'), '영상 시간동기화, 속도 추정, 지연 반영 도달점 예측', '신뢰도 저하·속도 초과 시 추적 중단 또는 재계획'],
            [B_('비정형 유연체'), '변형 키포인트·윤곽·점군 추적, 장력·변형 제한', '단일 강체 자세로 단순화하지 않고 상태 재추정'],
            [B_('정렬·적층'), '목표면 상대 위치, 접촉 탐색, 무게중심·안정성 평가', '불안정 적층 감지 후 내려놓기·재배치'],
            [B_('양팔 협조'), '공유 작업 좌표, 충돌 회피, 역할 배정, 하중 분담', '한 팔 이상 감지 시 양팔·이동축 연계 정지']]
    table(s, MX, ty + 0.38, lw, ['기술', '구현 방향', '실패 대응'], rows, col_w=[1.45, 3.15, 2.8], size=10.5, pad=0.06, label='vision table')
    rx = MX + lw + 0.45; rw = W - MX - rx
    y = block(s, rx, ty, rw, '센서 역할', ['비전: 형상·도구 부위·배치 상태', '촉각: 접촉·미끄러짐 · 손목 센서: 반력', '초음파: 근거리 장애물·액면 보조 수단',
                                          '가열 상태: 인덕션 출력 정보 + 별도 온도센서'], size=11, label='sensors')
    block(s, rx, y + 0.2, rw, '학습 데이터 계획 (목표)', ['도구·용기 30종 이상, 시도 1만 회 이상, 실패 유형의 다양성 중시',
                                                        '물체·작업 세션·현장 단위로 학습·검증·시험 분리',
                                                        'VLA·모방학습은 고수준 작업 선택에 한정, 힘·속도·안전 한계는 독립 제어 계층'], size=11, label='data')
    foot(s, 6, note='초음파는 정밀 자세·조리 온도 판단을 대신하지 않음 · 증기·금속 반사·기울어진 표면에서 센서별 오차 시험 · 부록 A4')
    notes(s, '상부 RGB-D·손목 카메라 → 분할·기능 부위 인식 → 자세·변형 추정 → 이동 예측 → 파지·작업 계획 → 촉각·힘 접촉 제어 → 결과 확인 → 재파지·재시도·정지. '
             '데이터는 도구·용기 30종 이상, 시도 1만 회 이상, 물체·세션·현장 단위로 분리 검증. VLA·모방학습은 고수준 선택에 한정.')


# ---------------------------------------------------------------- 06 ceiling kitchen
def s07(prs):
    s = new_slide(prs, '07 kitchen')
    y0 = bp_header(s, 6, '천장 이동형 양팔 로봇 주방', '로봇 주방은 3년차부터 주방 제조사와 공동 판매하는 응용 제품',
                   '싱크대 상부 구조 프레임의 LM 이동축에 협동로봇 2대를 역설치, 각 팔의 핸드가 세척·준비·가열·플레이팅·수납 구역을 연결')
    iw = 5.0; ih = iw * 9 / 16
    image(s, KIT('ck_front.jpg'), MX, y0, iw, ih, focus=(0.5, 0.47), zoom=1.32)
    block(s, MX, y0 + ih + 0.22, iw, '시스템 구성 (검토안)', ['LM 가이드와 구동기·엔코더·브레이크·종단 스토퍼·케이블 관리장치',
                                                          '두 팔을 단일 공통 캐리지에 장착하는 안 우선 비교, 독립 캐리지는 후속 검토',
                                                          '검토된 구조체 또는 독립 프레임에 고정, 역설치 허용 로봇 모델 선택'], size=10.5, label='ck system')
    rx = MX + iw + 0.45; rw = W - MX - rx
    rows = [[B_('재료 준비'), '계량·전처리된 재료 카트리지 인식·투입', '재료 ID, 유통·보관 조건, 투입량 확인'],
            [B_('싱크·세척'), '식기 투입·꺼내기, 예비 헹굼·솔질, 정렬', '오염/청결 동선 분리, 배수, 비산수, 세척기 연동'],
            [B_('가열'), '인덕션 조절, 젓기, 뚜껑 조작', '온도·시간·액량 감시, 고온 작업 접근 제한'],
            [B_('배식·수납'), '정해진 그릇에 담기, 적층·보관', '파손·누락 확인, 적층 높이 제한'],
            [B_('대기·정비'), '로봇 수납, 외피 교체·세척, 수동 사용 전환', '잔열·구동 상태 확인, 서비스 접근 공간']]
    h = table(s, rx, y0, rw, ['구역', '작업', '설계 사항'], rows, col_w=[1.1, 2.5, rw - 3.6], size=10.5, pad=0.06, label='zones')
    ry = y0 + h + 0.25
    text(s, rx, ry, rw, 0.28, '레시피 확장 순서', size=12.5, bold=True)
    rec = [[('1단계', {'bold': True, 'color': T['accent']}), '비가열 식기·재료 용기 취급'], [B_('2단계'), '준비 재료를 사용한 저속 젓기 중심 볶음·찜'],
           [B_('3단계'), '메뉴·용기 다양화, 오븐 조작'], [B_('4단계'), '전용 밀폐·차폐 설비를 갖춘 튀김']]
    hline(s, rx, ry + 0.36, rw, color=T['text'], lw=1.0)
    table(s, rx, ry + 0.36, rw, None, rec, col_w=[1.1, rw - 1.1], size=10.5, pad=0.045, label='recipes')
    foot(s, 7, note='팬 던지기·고속 칼질은 초기 조리 방식에서 제외 · 레시피는 검증된 작업 절차로 관리 · 이미지는 콘셉트 렌더링 · 부록 A7')
    notes(s, 'Ceiling Kitchen: 싱크대 상부 구조 프레임에 LM 가이드·구동 이동축, 협동로봇 2대 역설치. 단일 공통 캐리지안 우선. 구역: 재료 준비, 싱크·세척, 가열, 배식·수납, 대기·정비. '
             '레시피는 비가열 취급 → 저속 젓기 볶음·찜 → 메뉴·용기 다양화·오븐 → 밀폐·차폐 설비 튀김 순. 판매는 3년차부터 주방 제조사와 표준 설치 모델 공동 판매.')


# ---------------------------------------------------------------- 07 performance targets
def s08(prs):
    s = new_slide(prs, '08 performance')
    y0 = bp_header(s, 7, '성능 목표와 검증 계획', '작업 완료율과 사람 개입 시간 중심의 12·24개월 성능 목표',
                   '제안 목표이며 실적 아님 · 시제품 시험 후 하중·속도·재질·환경 조건과 함께 확정')
    rows = [[B_('정적 파지'), '등록 물체 20종, 95% 이상', '30종 이상, 98% 이상', '종별 100회, 낙하 없이 이송·배치 완료'],
            [B_('동적 파지'), '0.1m/s 이하에서 90% 이상', '0.3m/s 이하에서 95% 이상', '무작위 초기위치, 전 시도 포함'],
            [B_('유연체 취급'), '지정 샘플 3종, 90% 이상', '천·포장재 등 5종, 95% 이상', '찢김·과변형 없는 완료'],
            [B_('정렬 오차'), '등록 강체 ±5mm', '등록 강체 ±3mm', '손에서 놓은 후 측정, 유연체 별도 기준'],
            [B_('감지→제어 갱신'), 'p95 200ms 이하', 'p95 100ms 이하', '촬영부터 제어 명령까지 측정'],
            [B_('도구 작업'), '저토크 작업 2종', '저토크 3종, 완료율 95% 이상', '토크·작업 시간 동시 보고'],
            [B_('핸드 하중'), '건조 원통 손잡이 1kg', '동일 조건 2kg', '특정 자세·속도·모멘트 한계 명시'],
            [B_('내구성'), '반복 개폐 10만 회', '30만 회 (양산 시 100만 회 지향)', '하중·교체주기·힘 저하율 명시'],
            [B_('주방 실증'), '비가열 취급 시연', '메뉴 3종, 무개입 완료율 90% 이상', '메뉴별 100회 반복'],
            [B_('경제성'), '공정별 기준 시간 확보', ('총 사람 개입시간 30% 이상 감소', {'bold': True, 'color': T['accent']}), '선정 고객의 기준 시간 대비 검증']]
    h = table(s, MX, y0, CW, ['지표', '12개월 목표', '24개월 목표', '시험 정의'], rows, col_w=[1.95, 2.75, 3.25, CW - 7.95], size=10.5, pad=0.045,
              label='perf table')
    by = y0 + h + 0.22
    hw = (CW - 0.5) / 2
    block(s, MX, by, hw, '성능 보고 방식', ['최초 시도 성공·재시도 포함 성공·작업 중단 분리 보고',
                                            '시험 횟수·성공 건수·신뢰구간 공개, 추적 중지·놓침도 실패',
                                            '주방: 보충·세척·복구를 포함한 사람 개입시간, 에너지·물 사용량'], size=10.5, gap=1, label='report')
    block(s, MX + hw + 0.5, by, hw, '출시 게이트', ['유료 실증은 고객과 합의한 제한된 운영 범위에서만 진행',
                                                  '낙하·과열·의도치 않은 동작은 개선 완료까지 해당 기능 출시 보류',
                                                  '소수 시험의 무사고를 안전성 입증으로 주장하지 않음'], size=10.5, gap=1, label='gate')
    foot(s, 8, note='단일 파지 성공률을 전체 조리 성공률로 제시하지 않음 · 시험 정의 상세 부록 A4')
    notes(s, '12개월·24개월 성능 목표(제안). 정적 파지 20종 95% → 30종 98%, 동적 파지 0.1m/s 90% → 0.3m/s 95%, 감지→제어 p95 200ms → 100ms, '
             '핸드 하중 1kg → 2kg, 내구 10만 → 30만 회, 주방 메뉴 3종 무개입 90%, 선정 고객 사람 개입시간 30% 감소. 중대 이상은 개선 완료까지 출시 보류.')


# ---------------------------------------------------------------- 08 competition
def s09(prs):
    s = new_slide(prs, '09 competition')
    y0 = bp_header(s, 8, '경쟁·차별화·지식재산', '차별화 요소는 동일 조건 비교 시험과 고객 평가로 검증')
    rows = [[B_('qbrobotics\nqb SoftHand Industry'), '제조사 공개 사양: 5지, 19자유도·1모터, 파워그립 2kg, IP65',
             '다지 형태보다 도구 토크 유지·부분 독립 조작·세척 교체부·작업 완료율로 비교'],
            [B_('Moley Robotics\nA-AiR'), '이동 플랫폼 양손 로봇, 3자유도 갠트리, 비전, 수전·오븐 등 주방기기 연동 (공급사 소개)',
             '천장 양팔 주방 자체의 신규성은 주장하지 않음\n부품 플랫폼·국내 주방 통합·서비스성 검증'],
            [B_('YORI 연구 (2024)'), '모듈형 주방과 양팔 조작을 활용한 자율 조리 연구', '연구 시연 이후 장시간 운영·정비·유료 고객 경제성 입증'],
            [B_('전용 그리퍼·전용 조리기'), '지정 공정에 최적화한 대안', '범용성 이득이 비용·속도 손실보다 큰 다품종 작업에 집중']]
    h = table(s, MX, y0, CW, ['비교 대상', '확인된 내용 (공개 자료)', '본 사업의 대응'], rows, col_w=[2.35, 4.55, CW - 6.9], size=11.5, pad=0.1,
              label='comp table')
    by = y0 + h + 0.4
    c1, c2 = 4.0, 3.75; c3 = CW - c1 - c2 - 0.8
    block(s, MX, by, c1, '차별화 가설 (모두 검증 대상)', ['① 감싸쥐기와 토크 유지를 함께 하는 하이브리드 핸드', '② 비전·촉각·힘 제어를 결합한 작업별 스킬',
                                                         '③ 현장에서 교체·세척하는 주방 접촉 모듈', '④ 로봇 제조사별 장착·제어 연결',
                                                         '⑤ 실패와 복구를 포함한 실사용 데이터'], size=11, gap=3, bullet=None, label='hyp')
    block(s, MX + c1 + 0.4, by, c2, '특허·영업비밀 (계획)', ['출원 후보: 엄지 대향·관절 잠금, 손끝 교체·밀봉,\n파지 재구성, 양팔·이동축 작업 분담',
                                                             '선행기술 조사 전 독자성·비침해·세계 최초\n주장 안 함', '영업비밀 후보: 데이터 정제, 장력 보정,\n실패 복구 파라미터'],
          size=11, gap=3, label='ip')
    block(s, MX + c1 + c2 + 0.8, by, c3, '비교 실험·데이터 권리', ['전용 그리퍼와 동일 조건 비교\n(사이클타임·전환시간·성공률·총비용)',
                                                               '고객 데이터의 학습·재사용 범위는\n계약에서 분리 합의', '오픈소스 상업 이용 조건 출시 전 확인'],
          size=11, gap=3, label='test')
    foot(s, 9, note='출처: qbrobotics 제품 사양, Moley Robotics A-AiR 소개, arXiv:2405.11094 · 독립 비교시험 아님 · 상세 부록 A8')
    notes(s, 'qb SoftHand Industry(5지, 19자유도·1모터, 파워그립 2kg, IP65), Moley A-AiR(이동 플랫폼 양손 로봇·갠트리·주방기기 연동), YORI 연구, 전용 그리퍼·조리기와 비교. '
             '천장 양팔 주방 자체의 신규성은 주장하지 않음. 차별화 가설 5가지는 동일 조건 비교 시험과 고객 평가로 검증.')


# ---------------------------------------------------------------- 09 go-to-market
def s10(prs):
    s = new_slide(prs, '10 gtm')
    A = M['assumptions']
    y0 = bp_header(s, 9, '시장 진입 전략', '비가열 취급·정렬·저하중 도구 작업으로 진입해 SI 반복 판매로 확대')
    lw = 6.75
    text(s, MX, y0, lw, 0.28, '연차별 판매 순서', size=13, bold=True)
    rows = [[('1년차', {'bold': True, 'color': T['accent']}), '유료 실증·기술개발 계약', '로봇 SI·제조기업', f'실증·개발 매출 {A["pilot"][0]:.1f}억 원'],
            [B_('2년차'), 'SI를 통한 핸드 반복 판매\nSW 연간 계약', '로봇 SI·제조기업', f'핸드 {A["hands"][1]}대, SW {A["sw"][1]}건'],
            [B_('3년차~'), '주방 제조사와 표준 설치\n모델 공동 판매', '주방 제조사\n상업 주방 운영사', f'주방 셀 {A["cells"][2]}대\n(5년차 {A["cells"][4]}대)'],
            [B_('장기'), '임대·RaaS (정비비·잔존가치\n확보 후 금융 파트너와 검토)', '—', '기준 시나리오 미반영']]
    h = table(s, MX, y0 + 0.38, lw, ['시기', '판매 방식', '대상 고객', '재무 계획 반영'], rows, col_w=[0.85, 2.45, 1.65, 1.8], size=11, pad=0.07,
              label='sales order')
    cy = y0 + 0.38 + h + 0.3
    text(s, MX, cy, lw, 0.28, '고객 전환 절차', size=13, bold=True)
    conv = ['진단', '유료 실증 계약', '성능·경제성 검수', '구매·반복 발주']
    cw4 = lw / 4
    hc = table(s, MX, cy + 0.38, lw, [f'{i + 1}단계' for i in range(4)], [[(c, {'bold': True}) for c in conv]], col_w=[cw4] * 4, size=11, pad=0.07,
               label='conversion', header_color=T['accent'])
    text(s, MX, cy + 0.38 + hc + 0.12, lw, 0.5, ['검수 기준은 실증 계약 전에 고객과 합의, 실증 계약과 양산 발주는 구분', '의향서는 수주로 집계하지 않음, 임대는 장비 금융·유지보수 위험 때문에 후순위'],
         size=10, color=T['muted'], label='conv note')
    rx = MX + lw + 0.5; rw = W - MX - rx
    y = block(s, rx, y0, rw, '최초 진입시장', ['비가열 상태의 표준 용기·도구 취급, 정렬, 간단한 저하중 도구 작업',
                                              '불특정 가정의 모든 작업은 첫 제품 범위에서 제외',
                                              '공통 손·제어 기술의 반복 판매 가능성을 먼저 검증한 뒤 설치·서비스 역량이 큰 주방 제품으로 확장'], size=11, label='entry')
    ty = y + 0.22
    text(s, rx, ty, rw, 0.28, '첫 90일 고객 검증 (활동 목표)', size=12.5, bold=True)
    rows2 = [[B_('로봇 SI'), ('10곳', {'align': 'r'})], [B_('제조 사용자'), ('10곳', {'align': 'r'})], [B_('주방 제조·운영사'), ('10곳', {'align': 'r'})],
             [('유료 실증 가능 고객 선정', {'bold': True, 'color': T['accent']}), ('5곳', {'bold': True, 'color': T['accent'], 'align': 'r'})]]
    hline(s, rx, ty + 0.36, rw, color=T['text'], lw=1.0)
    h2 = table(s, rx, ty + 0.36, rw, None, rows2, col_w=[rw - 1.2, 1.2], size=11, pad=0.05, label='interviews')
    text(s, rx, ty + 0.46 + h2, rw, 0.62, '확보 자료: 실제 물체·작업 영상·사이클타임·전환시간·오류비용·도입예산 · 인터뷰 수는 활동 목표이며 고객 확보 실적 아님',
         size=10, color=T['muted'], label='interview note')
    foot(s, 10, note='판매 순서는 사업계획서 기준 · 로봇 주방은 핸드·제어 플랫폼의 반복 판매 검증 후 3년차부터 추진')
    notes(s, '최초 진입: 비가열 표준 용기·도구 취급, 정렬, 저하중 도구 작업. 1년차 유료 실증·기술개발 계약, 2년차 SI를 통한 핸드 반복 판매, '
             '3년차부터 주방 제조사와 표준 설치 모델 공동 판매. 첫 90일 로봇 SI·제조·주방 각 10곳 인터뷰 후 유료 실증 가능 고객 5곳 선정.')


# ---------------------------------------------------------------- 10 market size, pricing, customer economics
def s11(prs):
    s = new_slide(prs, '11 market')
    SAM = M['sam']; R = M['roi']; G = M['gm_unit']
    y0 = bp_header(s, 10, '시장 규모·가격·고객 경제성', '시장 규모는 고객 후보와 판매 단가를 곱하는 상향식으로 산정',
                   '검증되지 않은 시장 총액은 제시하지 않음 · 모든 수치는 계획용 가정이며 구매 의향 미검증')
    lw = 6.4
    text(s, MX, y0, lw, 0.28, '초기 접근시장 (가정)', size=13, bold=True)
    rows = [[B_('핸드'), '후보 100곳 × 잠재 5대 × 1,500만 원', [(f'{SAM["hand"]:.0f}억 원', {'bold': True, 'color': T['accent']}), (', 일회성 장비 기회', {})]],
            [B_('주방'), '후보 30곳 × 1셀 × 2억 원', [(f'{SAM["cell"]:.0f}억 원', {'bold': True}), (', 별도 응용시장', {})]],
            [B_('중복 처리'), '주방 셀 1식에 자사 핸드 2대 포함', '핸드 시장과 단순 합산하지 않음'],
            [B_('획득 목표'), '5년차 핸드 단품 350대, 주방 셀 25대', '판매 실행 목표, 시장 점유율 예측 아님']]
    h = table(s, MX, y0 + 0.38, lw, ['구분', '가정식', '금액·해석'], rows, col_w=[1.15, 2.75, 2.5], size=11, pad=0.07, label='sam table')
    block(s, MX, y0 + 0.38 + h + 0.3, lw, '원가 포함 범위와 별도 견적', ['핸드: 부품·조립·검사·초기 보증 충당',
                                                                    '주방 셀: 팔 2대·핸드 2개·레일/프레임·제어/안전·설치/시운전·기본 보증',
                                                                    '건축 보강·싱크대 전체 교체·급배수/전기 증설은 별도 견적',
                                                                    'SW 계약: 원격 진단·업데이트·기술지원, 필수 안전 기능은 구독과 무관'], size=11, gap=3, label='cost scope')
    rx = MX + lw + 0.5; rw = W - MX - rx
    text(s, rx, y0, rw, 0.28, '가격·직접원가 (가정, 부가세 제외)', size=13, bold=True)
    prow = [[B_('4지 중심 핸드 패키지'), '1,500만 원', '800만 원', f'{G["hand"] * 100:.1f}%'],
            [B_('주방 셀 1식'), '2억 원', '1.4억 원', f'{G["cell"] * 100:.1f}%'],
            [B_('SW 연간 계약'), '300만 원', '90만 원', f'{G["sw"] * 100:.1f}%'],
            [B_('유료 실증·개발'), '연 1~2억 원', '—', '40.0%']]
    h2 = table(s, rx, y0 + 0.38, rw, ['제품', '판매가', '직접원가', '총이익률'], prow, col_w=[rw - 3.3, 1.15, 1.1, 1.05], size=11, pad=0.05,
               align=['l', 'r', 'r', 'r'], label='price table')
    ry = y0 + 0.38 + h2 + 0.25
    text(s, rx, ry, rw, 0.28, '고객 투자회수 예시 (주방 셀, 가정)', size=13, bold=True)
    text(s, rx, ry + 0.36, rw, 0.45, ['투자비 2억 원, 시간당 총 인건비 2만5천 원, 연 300일,\n연 추가 운영비 1,000만 원'], size=10.5, color=T['text2'],
         label='roi basis')
    rr = [[f'하루 {x["hours"]}시간 절감', f'{x["saving"]:,.0f}만 원', (f'약 {x["payback"]:.1f}년', {'bold': True})] for x in R]
    h3 = table(s, rx, ry + 0.84, rw, ['사람 업무 절감', '연 순절감액', '단순 회수기간'], rr, col_w=[rw - 3.0, 1.5, 1.5], size=11, pad=0.06,
               align=['l', 'r', 'r'], label='roi table')
    text(s, rx, ry + 0.94 + h3, rw, 0.45, ['금융·세금·잔존가치 제외, 가동률이 높은 상업 시설에서 먼저 검증', '사람을 완전히 대체하는 인원수로 절감액을 계산하지 않음'],
         size=10, color=T['muted'], label='roi note')
    foot(s, 11, note='5년차 목표(핸드 350대·셀 25대)는 판매 실행 목표 · 프리미엄 가정용은 지불 의사 별도 검증 · 부록 A11')
    notes(s, f'초기 접근시장(가정): 핸드 100곳 × 5대 × 1,500만 원 = {SAM["hand"]:.0f}억 원, 주방 30곳 × 2억 원 = {SAM["cell"]:.0f}억 원, 단순 합산하지 않음. '
             '가격·원가: 핸드 1,500/800만 원(46.7%), 주방 셀 2억/1.4억 원(30%), SW 300/90만 원(70%). '
             f'고객 투자회수: 하루 6시간 절감 시 약 {R[0]["payback"]:.1f}년, 10시간 절감 시 약 {R[1]["payback"]:.1f}년.')


# ---------------------------------------------------------------- 11 five-year plan
def s12(prs):
    s = new_slide(prs, '12 financials')
    B = M['base']; A = M['assumptions']; S = M['sens']
    y0 = bp_header(s, 11, '5개년 재무 계획', f'5년차 매출 {B["rev"][4]:.0f}억 원, 영업이익 {eok(B["op"][4])}억 원 (기준 시나리오, 가정)',
                   '투자 집행 시작연도를 1년차로 정의 · 핸드 단품·주방 셀·SW 계약·유료 실증 매출의 단순 모델')
    lw = 7.3
    neg = lambda v: (eok(v), {'bold': True, 'color': T['accent'] if v < 0 else T['text']})
    rows = [['핸드 단품 판매 (대)'] + [str(v) for v in A['hands']],
            ['주방 셀 판매 (대)'] + [str(v) for v in A['cells']],
            ['SW 유효 계약 (건)'] + [str(v) for v in A['sw']],
            ['유료 실증·개발 매출'] + [eok(v) for v in A['pilot']],
            [B_('총매출')] + [(eok(v), {'bold': True}) for v in B['rev']],
            ['매출총이익'] + [eok(v) for v in B['gp']],
            ['운영비'] + [eok(v) for v in B['opex']],
            [B_('영업손익')] + [neg(v) for v in B['op']],
            ['누적 영업손익'] + [eok(v) for v in B['cum_op']]]
    h = table(s, MX, y0, lw, ['구분 (억 원)', '1년차', '2년차', '3년차', '4년차', '5년차'], rows, col_w=[2.0] + [1.06] * 5, size=11,
              align=['l', 'r', 'r', 'r', 'r', 'r'], pad=0.042, label='pl table')
    by = y0 + h + 0.2
    hw = (lw - 0.4) / 2
    s3, s4 = S['y3_50'], S['y4_80']
    block(s, MX, by, hw, '민감도 (사업계획서 기준)', [f'3년차 판매·계약·실증 50%\n→ 매출 {eok(s3["rev"])}억, 영업손실 {eok(-s3["op"])}억',
                                                       f'4년차 전 부문 매출 80%\n→ 총이익 {eok(s4["gp"])}억 < 운영비 {A["opex"][3]:.0f}억',
                                                       '손익분기는 제품 구성과 실제 원가에 민감'], size=10.5, gap=2, label='sens')
    block(s, MX + hw + 0.4, by, hw, '자금 수요', [f'1~2년차 누적 영업손실 {eok(-B["cum_op"][1])}억 원',
                                                '재고·설비·보증금·매출채권·세금\n반영 시 현금 소요 증가',
                                                'Seed로 5개년 전체를 조달하지 않음\n18~24개월에 후속 자금 조달 필요'], size=10.5, gap=2, label='cash need')
    rx = MX + lw + 0.5; rw = W - MX - rx
    text(s, rx, y0, rw, 0.28, '매출 구성 (억 원)', size=12.5, bold=True)
    series = [('핸드 단품', B['rev_hand']), ('주방 셀', B['rev_cell']), ('소프트웨어', B['rev_sw']), ('실증·개발', B['rev_pilot'])]
    cols = [T['accent'], '4A4F57', '8C9198', T['grey_bar']]
    lg_y = y0 + 0.36; lx_ = rx
    for (nm, _), c in zip(series, cols):
        rect(s, lx_, lg_y + 0.07, 0.12, 0.12, fill=c)
        text(s, lx_ + 0.17, lg_y, 1.4, 0.25, nm, size=9.5, color=T['text2'], check=False)
        lx_ += 0.17 + text_w(nm, 9.5) + 0.2
    cy = y0 + 0.72; chh = 3.95; plot = (0.02, 0.1, 0.96, 0.8); vmax = 125
    column_chart(s, rx, cy, rw, chh, ['1년차', '2년차', '3년차', '4년차', '5년차'], series, cols, stacked=True, vmax=vmax, show_labels=False,
                 gap=55, plot=plot, size=10.5)
    px, py, pw, ph_ = plot
    for i, tot in enumerate(B['rev']):
        ccx = rx + rw * (px + pw * (i + 0.5) / 5); top = cy + chh * (py + ph_ * (1 - tot / vmax))
        text(s, ccx - 0.6, top - 0.29, 1.2, 0.26, f'{tot:.1f}', size=11, bold=True, align='c', check=False)
    foot(s, 12, note='산식·부문별 매출총이익 부록 A12 · 모든 수치는 사업계획서 기준 시나리오의 계획값이며 실적 아님')
    notes(s, f'기준 시나리오: 매출 {B["rev"][0]:.1f} → {B["rev"][4]:.1f}억 원, 영업손익 {eok(B["op"][0])} → {eok(B["op"][4])}억 원, 4년차 흑자 전환(계획). '
             f'1~2년차 누적 영업손실 {eok(-B["cum_op"][1])}억 원. 민감도: 3년차 50% 시 영업손실 {eok(-s3["op"])}억 원, 4년차 80% 시 총이익이 운영비에 못 미침. '
             '18~24개월에 후속 자금 조달 필요.')


# ---------------------------------------------------------------- 12 schedule
def s13(prs):
    s = new_slide(prs, '13 schedule')
    y0 = bp_header(s, 12, '개발 일정', '36개월 6단계 개발, 단계 통과 조건을 충족하면 다음 단계로 진행')
    cx0 = MX; cw_p = 1.2; tx = cx0 + cw_p + 0.1; tw = 3.2; ox = tx + tw + 0.45; ow = 3.75; gx = ox + ow + 0.2; gw = W - MX - gx
    rh = 0.53
    text(s, cx0, y0, cw_p, 0.26, '기간', size=11, bold=True)
    text(s, ox, y0, ow, 0.26, '핵심 산출물', size=11, bold=True)
    text(s, gx, y0, gw, 0.26, '단계 통과 조건', size=11, bold=True)
    for m in range(0, 37, 6):
        xx = tx + tw * m / 36
        text(s, xx - 0.25, y0, 0.5, 0.26, str(m), size=10, color=T['muted'], align='c', check=False)
    hy = y0 + 0.36
    hline(s, MX, hy, CW, color=T['text'], lw=1.0)
    rect(s, tx, hy + 0.02, tw * 24 / 36, rh * 6 - 0.04, fill=T['accent_soft'])
    phases = [('0~3개월', 0, 3, '고객 인터뷰, 요구사항, 구동 비교, 선행기술 조사', '구동 구조 선정, 초기 적용 작업 3개 확정'),
              ('4~6개월', 3, 6, '4지 알파, 센서·파지 제어, 비가열 작업 데모', '물체 10종 반복 파지, 원시 시험 로그 확보'),
              ('7~12개월', 6, 12, '4지 베타, 비전 추적, 제조 실증, 주방 기구 검토', '12개월 목표 검증, 유료 실증 계약'),
              ('13~18개월', 12, 18, '주방 양팔 통합, 젖은 식기 취급, 메뉴 1종', '낙하·정전·열·세척 관련 검증 후 제한 운전'),
              ('19~24개월', 18, 24, '4지 제품 검증, 5지 알파, 메뉴 3종', '유료 실증 누적 5건, 반복 발주 2곳 목표'),
              ('25~36개월', 24, 36, '5지 고도화, 표준 주방 셀, 제조·서비스 체계', '후속 투자·고객 검수 충족 시 출시 확대')]
    y = hy
    for i, (p, a, b, out, gate) in enumerate(phases):
        text(s, cx0, y + 0.06, cw_p, rh - 0.1, p, size=11, bold=True, anchor='m', label='ph ' + p)
        rect(s, tx + tw * a / 36 + 0.02, y + 0.17, tw * (b - a) / 36 - 0.04, rh - 0.34, fill=T['accent'] if b <= 24 else '8C9198')
        text(s, ox, y + 0.06, ow, rh - 0.1, out, size=10.5, anchor='m', label='out ' + p)
        text(s, gx, y + 0.06, gw, rh - 0.1, gate, size=10.5, color=T['text2'], anchor='m', label='gate ' + p)
        y += rh
        hline(s, MX, y, CW, color=T['line'])
    text(s, tx, y + 0.06, tw, 0.24, '눈금: 투자 집행 후 개월 · 음영: Seed 자금 사용 기간 (24개월)', size=9, color=T['muted'], check=False)
    gy = y + 0.42
    text(s, MX, gy, CW, 0.28, '24개월 목표 (투자 제안 기준)', size=13, bold=True)
    hline(s, MX, gy + 0.36, CW, color=T['text'], lw=1.0)
    goals = [('4지 핸드', '제품 검증'), ('5지 핸드', '알파 시제품'), ('로봇 주방', '제한 메뉴 3종 실증'), ('유료 실증', '누적 5건'), ('반복 발주 고객', '2곳')]
    gw5 = CW / 5
    for i, (a, b) in enumerate(goals):
        x = MX + i * gw5
        if i: vline(s, x, gy + 0.5, 0.62)
        text(s, x + (0.15 if i else 0), gy + 0.47, gw5 - 0.25, 0.26, a, size=10.5, color=T['muted'])
        text(s, x + (0.15 if i else 0), gy + 0.74, gw5 - 0.25, 0.36, b, size=14, bold=True, label='goal ' + a)
    foot(s, 13, note='기간은 투자 집행일 기준 · 성능 목표와 출시 게이트는 07장 · 단계 통과 조건 미충족 시 해당 기능 출시 보류')
    notes(s, '0~3개월 고객 인터뷰·구동 비교, 4~6개월 4지 알파, 7~12개월 4지 베타·제조 실증·유료 실증 계약, 13~18개월 주방 양팔 통합·메뉴 1종, '
             '19~24개월 4지 제품 검증·5지 알파·메뉴 3종, 25~36개월 5지 고도화·표준 주방 셀. 24개월 목표: 유료 실증 누적 5건, 반복 발주 2곳.')


# ---------------------------------------------------------------- 13 use of funds
def s14(prs):
    s = new_slide(prs, '14 use of funds')
    B = M['base']; A = M['assumptions']; U = M['uof']; SEED = M['seed']
    y0 = bp_header(s, 13, 'Seed 자금 사용 계획', 'Seed 20억 원은 24개월 개발·유료 실증의 현금 집행 한도')
    lw = 7.4
    rows = [[B_(k), d, f'{v:.1f}', f'{v / SEED * 100:.1f}%'] for k, v, d in U]
    rows.append([B_('합계'), '24개월 계획 현금 집행 한도', (f'{sum(v for _, v, _ in U):.1f}', {'bold': True}), ('100%', {'bold': True})])
    h = table(s, MX, y0, lw, ['항목', '사용 목적', '금액 (억 원)', '비중'], rows, col_w=[1.95, 3.45, 1.15, 0.85], size=11, align=['l', 'l', 'r', 'r'],
              pad=0.065, label='uof table')
    by = y0 + h + 0.35
    text(s, MX, by, lw, 0.28, '구성 비중', size=12.5, bold=True)
    x = MX; bw = lw; yb = by + 0.4
    cols = [T['accent'], '4A4F57', '8C9198', 'A9AEB5', 'C9CDD2', 'DDE0E3']
    for (k, v, _), c in zip(U, cols):
        ww = bw * v / SEED
        rect(s, x, yb, ww - 0.02, 0.42, fill=c)
        text(s, x, yb, ww - 0.02, 0.42, f'{v:.1f}', size=10.5, bold=True, color='FFFFFF' if c in (T['accent'], '4A4F57', '8C9198') else T['text'],
             align='c', anchor='m', check=False)
        x += ww
    lx_ = MX; ly = yb + 0.52
    for (k, v, _), c in zip(U, cols):
        rect(s, lx_, ly + 0.07, 0.12, 0.12, fill=c)
        text(s, lx_ + 0.17, ly, 1.8, 0.25, k, size=9.5, color=T['text2'], check=False)
        lx_ += 0.17 + text_w(k, 9.5) + 0.22
    rx = MX + lw + 0.5; rw = W - MX - rx
    y = block(s, rx, y0, rw, '집행 원칙', ['자금 사용표는 현금 집행 예산, 손익계산서 운영비와 일대일로 일치하지 않음',
                                          '장비 자산화·재고·매출 회수 시점을 반영한 월별 현금계획은 투자 실사 전 작성',
                                          '보조금은 미확정이므로 기본 조달재원에서 제외', '개발 인력 10억 원: 7명 단계 채용 기준', '월별 채용·인건비 계획 [입력 필요]'],
              size=11, label='uof rules')
    block(s, rx, y + 0.22, rw, '손익 연결과 후속 자금', [f'1~2년차 운영비 {A["opex"][0] + A["opex"][1]:.0f}억 원, 매출총이익 {B["gp"][0] + B["gp"][1]:.2f}억 원',
                                                     f'1~2년차 누적 영업손실 {eok(-B["cum_op"][1])}억 원', '18~24개월에 후속 자금 조달 필요',
                                                     '후속 투자 목표 규모 [입력 필요]'], size=11, label='uof link')
    foot(s, 14, note='금액은 사업계획서 제안안 · 항목별 상세 부록 A13')
    notes(s, 'Seed 20억 원: 개발 인력 10.0억, 시제품·시험 설비 3.5억, AI 데이터·연산 1.5억, 주방 통합 실증 2.0억, 안전·품질·지식재산 1.0억, 운영·예비비 2.0억. '
             '현금 집행 예산이며 손익 운영비와 일대일로 일치하지 않음. 1~2년차 누적 영업손실 14.49억 원, 18~24개월에 후속 조달.')


# ---------------------------------------------------------------- 14 organization
def s15(prs):
    s = new_slide(prs, '15 team')
    y0 = bp_header(s, 14, '조직 및 인력', '핵심 인력 7명 단계 채용, 안전·위생·특허·주방 설계는 외부 협력')
    text(s, MX, y0, CW, 0.28, '창업자 (확인 자료로 보완 필요)', size=13, bold=True)
    frows = [[B_('대표 · 사업·제품 책임자'), ph('[성명 입력 필요]'), ph('[핸드·로봇·제조 자동화 관련 경력, 기간 입력 필요]'), ph('[창업 계기, 확인한 고객 문제 입력 필요]')],
             [B_('공동창업자'), ph('[여부·성명 입력 필요]'), ph('[보유 기술·장비·연구 이력 입력 필요]'), ph('[역할·지분·전업 참여 조건 입력 필요]')]]
    h1 = table(s, MX, y0 + 0.38, CW, ['역할', '성명', '주요 경력·보유 기술', '이 사업과의 연결'], frows, col_w=[2.3, 2.1, 4.0, CW - 8.4], size=11,
               pad=0.07, label='founders')
    hy = y0 + 0.38 + h1 + 0.3
    lw = 8.4
    text(s, MX, hy, lw, 0.28, '초기 핵심 역할 7명 (단계 채용 전제)', size=13, bold=True)
    hr = [[B_('사업·제품 책임자'), '1', '고객 인터뷰·유료 실증 계약, 제품 범위·가격, 파트너', '첫 90일 검증, 유료 실증 5건'],
          [B_('핸드 기구/구동'), '2', '손가락 골격·엄지 대향 구조, 구동 비교 시험, 교체형 접촉부, 내구 시험', '4지 알파·베타, 5지 알파'],
          [B_('제어·임베디드'), '1', '촉각·관절/장력·손목 힘 센서, 파지·힘 제어, 로봇 통신 드라이버', '감지→제어 p95 100ms'],
          [B_('비전·조작 AI'), '2', '도구 기능 부위 인식, 자세·동적 추적, 데이터 수집·학습·검증', '도구·용기 30종, 시도 1만 회'],
          [B_('시스템 통합'), '1', '로봇 2개 플랫폼 장착·교정, 제조 실증, 주방 양팔·LM축 통합', '제조 실증, 주방 메뉴 3종']]
    table(s, MX, hy + 0.38, lw, ['역할', '인원', '주요 업무', '연계 목표'], hr, col_w=[1.75, 0.6, 3.85, 2.2], size=10.5, pad=0.055,
          align=['l', 'c', 'l', 'l'], label='roles')
    rx = MX + lw + 0.45; rw = W - MX - rx
    y = block(s, rx, hy, rw, '외부 협력', ['안전: 통합 위험성 평가, 시험기관', '위생: 식품접촉 재질·세척 검증', '특허: 선행기술 조사·출원', '주방 설계: 주방 제조사·설치'],
              size=10.5, gap=1, label='partners')
    block(s, rx, y + 0.2, rw, '채용 계획', ['단계 채용, 월별 일정 [입력 필요]', '인건비 예산: Seed 개발 인력 10억 원'], size=10.5, gap=1, label='hiring')
    foot(s, 15, note='역할별 업무·연계 목표는 사업계획서의 개발 계획 기준 · 확인되지 않은 이력·성과는 기재하지 않음')
    notes(s, '초기 핵심 역할 7명: 사업·제품 책임자 1, 핸드 기구/구동 2, 제어·임베디드 1, 비전·조작 AI 2, 시스템 통합 1. 단계 채용 전제. '
             '안전·위생·특허·주방 설계는 외부 전문기관과 협력. 창업자 경력·공동창업자·보유 기술은 확인 자료로 보완 필요.')


# ---------------------------------------------------------------- 15 risks & due diligence
def s16(prs):
    s = new_slide(prs, '16 risks')
    y0 = bp_header(s, 15, '제품화 위험과 투자 검증 항목', '주요 위험 7가지와 투자 실사 전에 확보할 증거 8가지')
    lw = 7.75
    rows = [[B_('순응성과 강성 충돌'), '잘 잡아도 도구가 회전하거나 처짐', '손가락 골격·잠금·양손 지지 비교, 작업 토크별 출시 제한'],
            [B_('반사·증기·가림'), '추적 실패·오파지', '다시점 센서, 신뢰도 기준, 접촉 기반 재확인'],
            [B_('젖음·기름·열·세제'), '미끄러짐·외피 열화·오염', '소재 시험·교체 기준·세척 접근성 검증'],
            [B_('천장·역설치·정전'), '낙하·파손·재료 유출', '구조 검토, 브레이크·낙하 방지, 작업별 안전 정지 상태 설계'],
            [B_('칼·해머·튀김'), '절상·충격·화상 위험', '차폐·접근 제한·독립 인터록 충족 후 기능 활성화'],
            [B_('과도한 맞춤 개발'), '낮은 마진·서비스 비용 증가', '승인 도구·메뉴, 주방 설치 표준화, 비표준 요청 별도 견적'],
            [B_('긴 영업주기·후속 조달'), '운전자금 부족', '실증 선수금·검수 기준 계약, 단계 채용, 후속 투자 조기 착수']]
    h = table(s, MX, y0, lw, ['주요 위험', '사업 영향', '대응·판정'], rows, col_w=[1.95, 2.2, 3.6], size=11, pad=0.085, label='risk table')
    ky = y0 + h + 0.3
    kp = [[('투자 가치의 핵심  ', {'bold': True, 'color': T['text']}), ('승인된 도구와 작업 범위를 넓히면서 같은 핸드·제어 플랫폼을 반복 판매할 수 있는지', {})],
          [('실행 전략  ', {'bold': True, 'color': T['text']}), ('제조용 모듈 매출과 주방용 시스템 확장을 단계적으로 연결', {})]]
    kh = text_h(kp, 11, lw - 0.44, space_after=4)
    rect(s, MX, ky, lw, kh + 0.36, fill=T['soft'])
    text(s, MX + 0.22, ky + 0.16, lw - 0.44, kh + 0.05, kp, size=11, color=T['text2'], space_after=4, label='thesis box')
    rx = MX + lw + 0.45; rw = W - MX - rx
    ev = ['① 법인·주주·핵심 인력 이력', '② 기존 연구·특허의 소유권과 이전 가능성', '③ 시제품 무편집 시험 영상과 원시 로그', '④ BOM·공급사 견적·제조 수율',
          '⑤ 유료 실증 계약과 고객 기준 성능', '⑥ 월별 현금흐름·후속 투자 계획', '⑦ 시험·인증 범위와 견적', '⑧ 고객의 실제 운영비·절감시간']
    y = block(s, rx, y0, rw, '투자 실사 전 확보할 증거', ev, size=10.5, gap=2, bullet=None, label='evidence')
    text(s, rx, y + 0.08, rw, 0.3, [ph('현재 상태: 확보된 자료 없음 [확보 시 입력]')], size=10.5, color=T['text2'], label='evidence status')
    block(s, rx, y + 0.55, rw, '안전·위생 검토 범위', ['ISO 10218-2:2025(로봇 응용·셀 안전) 기준\n고온 도구·칼·중량물·이동축 통합 위험 평가',
                                                     'IP 등급 ≠ 식품 위생 적합성\n식품접촉 재질·세척 잔류물·미생물 별도 검증'], size=10.5, gap=2, label='safety')
    foot(s, 16, note='제품 검증 전 인증 취득·규제 적합을 주장하지 않음 · 가정용 주방 적용 기준은 시험기관과 별도 결정 · 상세 부록 A14')
    notes(s, '주요 위험: 순응성·강성 충돌, 반사·증기·가림, 젖음·기름·열·세제, 천장·역설치·정전, 칼·해머·튀김, 과도한 맞춤 개발, 긴 영업주기·후속 조달. '
             '투자 실사 전 증거 8가지: 법인·인력, 특허 소유권, 무편집 시험 영상·로그, BOM·견적·수율, 유료 실증 계약, 월별 현금흐름, 인증 범위, 고객 운영비·절감시간.')


# ---------------------------------------------------------------- 16 investment proposal
def s17(prs):
    s = new_slide(prs, '17 proposal')
    y0 = bp_header(s, 16, '투자 제안', 'Seed 20억 원으로 24개월 내 제품 성능과 유료 고객 경제성 입증')
    lw = 4.2
    text(s, MX, y0, lw, 0.28, '투자 조건', size=13, bold=True)
    terms = [('투자 금액', [('20억 원 (Seed)', {'bold': True, 'color': T['accent']})]), ('투자 형태', ph('[보통주·상환전환우선주 등 입력 필요]')),
             ('기업가치·지분율', ph('협의 [입력 필요]')), ('자금 사용 기간', '24개월 (개발·유료 실증)'), ('라운드 현황', ph('[참여 투자자·진행 상황 입력 필요]')),
             ('후속 투자', ph('18~24개월 착수, 규모 [입력 필요]'))]
    kv_table(s, MX, y0 + 0.38, lw, terms, kw=1.45, size=11, pad=0.07, label='terms')
    mx_ = MX + lw + 0.45; mw = 3.9
    text(s, mx_, y0, mw, 0.28, '24개월 목표 (검증 지표)', size=13, bold=True)
    goals = [('4지 핸드', '제품 검증'), ('5지 핸드', '알파 시제품'), ('로봇 주방', '제한 메뉴 3종 실증'), ('유료 실증', '누적 5건'), ('반복 발주 고객', '2곳'),
             ('정적 파지', '30종, 98% 이상'), ('사람 개입시간', '30% 이상 감소')]
    hline(s, mx_, y0 + 0.38, mw, color=T['text'], lw=1.0)
    table(s, mx_, y0 + 0.38, mw, None, [[k, (v, {'bold': True, 'align': 'r'})] for k, v in goals], col_w=[mw - 1.9, 1.9], size=11, pad=0.06, label='goals')
    rx = mx_ + mw + 0.45; rw = W - MX - rx
    y = block(s, rx, y0, rw, '후속 투자 조건', ['성능 시험·고객 경제성·반복 발주 확인 후 양산·주방 상품화 자금 조달'], size=11, label='follow-on')
    y = block(s, rx, y + 0.2, rw, '투자 판단의 핵심', ['승인된 도구·작업 범위를 넓히면서 같은 핸드·제어 플랫폼을 반복 판매할 수 있는지',
                                                     '제조용 모듈 매출에서 주방 시스템으로 단계적 확장'], size=11, label='thesis')
    block(s, rx, y + 0.2, rw, '회수 방안 (장기 가능성)', ['로봇·주방설비 기업의 전략적 인수, 기술특례 상장 (확정된 논의 없음)'], size=11, label='exit')
    by = 6.15
    rect(s, MX, by, CW, 0.62, fill=T['soft'])
    text(s, MX + 0.25, by, CW - 0.5, 0.62, [[('연락처   ', {'bold': True, 'color': T['text']})] + ph('대표자 [입력 필요]  ·  이메일 [입력 필요]  ·  전화 [입력 필요]')],
         size=11.5, color=T['text2'], anchor='m', label='contact')
    foot(s, 17, note='목표는 계획이며 실적 아님 · 사실·가정 구분 부록 A1')
    notes(s, '대표자 발표 문안: ' + PITCH + ' 투자 조건(형태·기업가치·지분율·라운드)은 입력 필요.')


MAIN = [s01, s02, s03, s04, s05, s06, s07, s08, s09, s10, s11, s12, s13, s14, s15, s16, s17]
