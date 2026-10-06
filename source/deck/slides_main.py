# SoftHand Seed IR deck v3 - main slides: Kitchen Robotics Platform (light design, 14 slides).
# Rules: one message per slide, headline + big image/diagram + 1-3 messages, nothing unverified stated as fact.
import json, os
from pptx.enum.shapes import MSO_SHAPE
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

FOOT = 'SoftHand  |  주방 로봇 조작 플랫폼  |  Seed 투자 제안서'
def foot(s, page, note=None):
    footer(s, page, left=FOOT, note=note)


# ---------------------------------------------------------------- 01 vision (cover)
def s01(prs):
    s = new_slide(prs, '01 vision')
    ix = 5.85
    image(s, KIT('lx_hero.jpg'), ix, 0, W - ix, H, focus=(0.6, 0.5))
    text(s, MX, 0.62, 4.8, 0.26, '[회사명 입력 필요]', size=11, color=T['muted'])
    text(s, MX, 1.42, 4.9, 0.3, 'KITCHEN ROBOTICS PLATFORM', size=13, bold=True, color=T['accent'])
    text(s, MX, 1.86, 4.95, 1.66, '모든 주방에서\n일할 수 있는 로봇', size=42, bold=True, line=0.95, label='cover title')
    text(s, MX, 3.6, 4.95, 0.32, 'The Robot That Can Work in Any Kitchen', size=15, color=T['text2'], label='cover en')
    text(s, MX, 4.1, 4.95, 0.62, '사람이 사용하는 기존 주방과 도구를\n그대로 사용하는 Kitchen Robotics Platform', size=14, label='cover sub')
    rows = [('시장', '상업용 주방 + 가정용 주방', T['text']), ('제품', 'Powered by SoftHand + Kitchen Skills', T['text']),
            ('투자 요청', 'Seed 20억 원 · 24개월', T['accent'])]
    y = 5.02
    hline(s, MX, y, 4.85, color=T['text'], lw=1.0)
    for k, v, c in rows:
        text(s, MX, y + 0.13, 1.0, 0.26, k, size=11, color=T['muted'])
        text(s, MX + 1.0, y + 0.09, 3.85, 0.32, v, size=14.5, bold=True, color=c, label='cover row ' + k)
        y += 0.48
        hline(s, MX, y, 4.85)
    text(s, MX, H - 0.55, 4.8, 0.22, '2026. 10  ·  이미지: 콘셉트 렌더링', size=9, color=T['muted'], check=False)
    notes(s, '모든 주방에서 일할 수 있는 로봇. 주방을 로봇에 맞게 다시 만들지 않고, 로봇이 사람이 쓰던 주방·도구·가전을 그대로 쓰게 하는 '
             'Kitchen Robotics Platform. 상업용 주방과 가정용 주방이 모두 핵심 시장, 제품은 SoftHand + Kitchen Skills, Seed 20억 원 / 24개월.')


# ---------------------------------------------------------------- 02 problem
def s02(prs):
    s = new_slide(prs, '02 problem')
    y0 = header(s, 'PROBLEM', '현재 주방 자동화는 로봇보다 주방을 더 많이 바꿉니다',
                '메뉴와 작업이 바뀔 때마다 새 하드웨어와 엔지니어링이 다시 필요')
    items = ['전용 그리퍼', '전용 조리장비', '전용 투입장치', '전용 레이아웃', '작업별 통합']
    menus = ['메뉴 A', '메뉴 B', '메뉴 C', '새 메뉴']
    tw, gap, bh, bg = 1.62, 0.22, 0.56, 0.08
    ty = y0 + 0.35
    fills = [T['dark'], '4A4F57', '7D838B']
    for j, m in enumerate(menus):
        x = MX + j * (tw + gap)
        for i, it in enumerate(items):
            yy = ty + i * (bh + bg)
            if j == 3:
                dashed_rect(s, x, yy, tw, bh, color=T['accent'])
                text(s, x, yy, tw, bh, it, size=11.5, color=T['accent'], align='c', anchor='m', label=f'tower new {i}')
            else:
                chip(s, x, yy, tw, bh, it, fill=fills[j], color='FFFFFF', size=11.5, bold=j == 0, label=f'tower {j}{i}')
        text(s, x, ty + 5 * (bh + bg) + 0.06, tw, 0.3, m, size=13, bold=True, align='c',
             color=T['accent'] if j == 3 else T['text'], label='menu ' + m)
    cy = ty + 5 * (bh + bg) + 0.48
    tot = 4 * tw + 3 * gap
    text(s, MX, cy, tot, 0.28, '메뉴가 늘수록 같은 과정 반복 (개념도)', size=11, color=T['muted'], align='c')
    rx = MX + tot + 0.75; rw = W - MX - rx
    vline(s, rx - 0.38, y0 + 0.35, 3.75)
    text(s, rx, y0 + 0.18, rw, 1.3, '75%', size=72, bold=True, color=T['accent'], line=0.9, label='75')
    text(s, rx, y0 + 1.5, rw, 0.62, '로봇 도입 총비용(TCO) 중\n초기 셋업·재설계 비중', size=15, bold=True, label='75 cap')
    text(s, rx, y0 + 2.18, rw, 0.25, '출처: BCG (2026.4), 로봇 도입 전반 기준', size=10, color=T['muted'])
    text(s, rx, y0 + 2.75, rw, 1.0, ['로봇 가격보다 환경을 맞추는 비용이 큼', '메뉴·도구가 바뀌면 같은 비용 반복'],
         size=13, color=T['text2'], bullet='–', indent=0.22, space_after=6, label='75 take')
    foot(s, 2, note='개념도 · 전용 주방 자동화 사례는 10장·부록 A6')
    notes(s, '기존 주방 자동화는 메뉴·작업마다 전용 그리퍼, 전용 조리장비, 전용 투입장치, 전용 레이아웃, 작업별 통합을 새로 만듦. '
             '메뉴가 바뀌면 같은 과정 반복. BCG(2026.4): 로봇 도입 총소유비용의 약 75%가 초기 셋업과 재설계(로봇 도입 전반 기준, 주방 한정 수치 아님).')


# ---------------------------------------------------------------- 03 insight
def s03(prs):
    s = new_slide(prs, '03 insight')
    y0 = header(s, 'INSIGHT', '주방은 이미 사람 손에 맞춰 표준화되어 있습니다')
    iw, ih = 7.3, 4.95
    iy = y0 + 0.17
    image(s, KIT('lx_insight.jpg'), MX, iy, iw, ih, focus=(0.5, 0.5))
    rx = MX + iw + 0.5; rw = W - MX - rx
    text(s, rx, iy, rw, 0.28, '어느 주방에나 있는 사람용 인터페이스', size=12, bold=True, color=T['muted'])
    words = ['팬', '냄비', '집게', '국자', '칼', '용기', '손잡이', '노브', '버튼', '서랍', '냉장고', '가전']
    cw3 = rw / 3; gy = iy + 0.42; rh = 0.56
    for i, wd in enumerate(words):
        r, c = divmod(i, 3)
        x = rx + c * cw3; yy = gy + r * rh
        hline(s, x, yy, cw3 - 0.12, color=T['text'] if r == 0 else T['line'], lw=1.0 if r == 0 else 0.75)
        text(s, x, yy + 0.1, cw3 - 0.12, 0.38, wd, size=18, bold=True, label='w ' + wd)
    my = gy + 4 * rh + 0.14
    text(s, rx, my, rw, 0.62, ['상업용·가정용 주방 모두 같은 형태', '새 주방도 같은 인터페이스 = 설치 환경'],
         size=12.5, color=T['text2'], bullet='–', indent=0.22, space_after=4, label='ins msg')
    bh = 1.25; by = iy + ih - bh
    rect(s, rx, by, rw, bh, fill=T['dark'])
    text(s, rx + 0.28, by, rw - 0.5, bh,
         [[('주방을 로봇에 맞추는 대신,', {'color': T['on_dark']})],
          [('로봇에게 ', {'color': T['on_dark']}), ('사람처럼 도구를 사용하는 능력', {'color': T['accent']}), ('을 준다', {'color': T['on_dark']})]],
         size=15, bold=True, anchor='m', label='ins concl')
    foot(s, 3, note='사람용 조리도구·용기·수전·화구를 그대로 둔 주방 · 콘셉트 렌더링')
    notes(s, '주방은 이미 사람 손 기준으로 표준화: 팬·냄비·집게·국자·칼·용기·손잡이·노브·버튼·서랍·냉장고·가전. 상업용과 가정용 모두 같은 형태. '
             '주방을 로봇에 맞추는 대신 로봇에게 사람처럼 도구를 쓰는 능력을 주면, 기존 주방이 곧 설치 환경.')


# ---------------------------------------------------------------- 04 solution
def s04(prs):
    s = new_slide(prs, '04 solution')
    y0 = header(s, 'SOLUTION', 'SoftHand + Kitchen Skills: 사람용 도구를 그대로 쓰는 손', '로봇 팔에 장착하는 손(SoftHand)과 주방 조작 Skill, 기존 주방·도구·가전은 그대로')
    cy = y0 + 0.2; ch = 4.6
    rect(s, MX, cy, 2.75, ch, fill='EEF0F2')
    cutout(s, REN('product.png'), MX + 0.1, cy + 0.15, 2.55, ch - 0.3)
    sx = MX + 3.15; sw = 3.55
    items = [('Soft Contact', '잡을 때는 부드럽게', '다양한 형상과 도구에 적응'),
             ('Rigid Work', '사용할 때는 단단하게', '팬·손잡이·노브·레버의 힘과 반력을 버팀'),
             ('Force · Tactile Control', '느끼면서 제어', '힘과 미끄러짐을 감지하며 작업')]
    yy = cy
    for en, ko, d in items:
        hline(s, sx, yy, sw, color=T['text'], lw=1.0)
        text(s, sx, yy + 0.14, sw, 0.24, en, size=11, bold=True, color=T['accent'])
        text(s, sx, yy + 0.42, sw, 0.42, ko, size=20, bold=True, label='sol ' + ko)
        text(s, sx, yy + 0.88, sw, 0.5, d, size=12.5, color=T['text2'], label='sol d ' + ko)
        yy += 1.52
    kx = sx + sw + 0.45; kw = W - MX - kx
    text(s, kx, cy, kw, 0.26, 'KITCHEN ROBOTICS PLATFORM', size=11, bold=True, color=T['muted'])
    layers = [('Application', '상업용 주방 · 가정용 주방', 'soft'),
              ('Skill', ['집기 · 붓기 · 젓기 · 뒤집기 · 열기', '누르기 · 돌리기 · 썰기 · 담기'], 'dark'),
              ('Manipulation', '힘·촉각 제어 · 순응 · 가변 강성 · 실패 복구', 'dark'),
              ('Hardware', 'SoftHand', 'accent'),
              ('Robot', '로봇 팔 · 가정용 로봇 · 주방 로봇', 'soft')]
    ly = cy + 0.38; lh = 0.66; lg = 0.07
    for name, cont, kind in layers:
        fill = {'soft': T['soft'], 'dark': T['dark'], 'accent': T['accent']}[kind]
        fc = T['text'] if kind == 'soft' else 'FFFFFF'
        rect(s, kx, ly, kw, lh, fill=fill)
        text(s, kx + 0.18, ly, 1.4, lh, name, size=12, bold=True, color=fc, anchor='m', label='layer n ' + name)
        text(s, kx + 1.6, ly, kw - 1.75, lh, cont, size=15 if kind == 'accent' else 11.5, bold=kind == 'accent',
             color=T['text2'] if kind == 'soft' else 'FFFFFF', anchor='m', label='layer ' + name)
        ly += lh + lg
    ly += 0.06
    lx_ = kx
    for col, lab in [(T['dark'], 'SoftHand가 만드는 범위'), (T['soft'], '고객·파트너·기존 로봇')]:
        rect(s, lx_, ly + 0.06, 0.14, 0.14, fill=col, line=T['grey_bar'] if col == T['soft'] else None)
        text(s, lx_ + 0.22, ly, 2.2, 0.26, lab, size=10.5, color=T['text2'], label='legend ' + lab[:8])
        lx_ += 0.22 + text_w(lab, 10.5) + 0.4
    foot(s, 4, note='4지(손가락 3 + 대향 엄지) 콘셉트 · 구동·센서·하중 상세는 부록 A3 · 콘셉트 렌더링')
    notes(s, 'SoftHand는 세 문장으로 설명: 잡을 때는 부드럽게(형상·도구 적응), 사용할 때는 단단하게(팬·손잡이·노브·레버의 힘과 반력), '
             '느끼면서 제어(힘·미끄러짐 감지). 회사가 만드는 것은 손 하나가 아니라 Hardware + Manipulation + Skill 계층. '
             '로봇 팔과 주방 애플리케이션은 고객·파트너 영역.')


# ---------------------------------------------------------------- 05 workflow
def s05(prs):
    s = new_slide(prs, '05 workflow')
    y0 = header(s, 'KITCHEN WORKFLOW', 'One Hand. Many Tools. Many Tasks.',
                '핸드 하나로 재료 집기부터 플레이팅까지, 사람용 도구를 그대로 사용 (콘셉트)')
    steps = [('lx_pick', '재료 집기', '그릇의 재료'), ('lx_lid', '용기 열기', '뚜껑 손잡이'), ('lx_drop', '팬에 투입', '재료 넣기'),
             ('lx_tongs', '집게 사용', '사람용 집게'), ('lx_stir', '젓기', '사람용 국자'), ('lx_knob', '노브 조작', '화구 노브'),
             ('lx_plate', '플레이팅', '집게 · 접시')]
    gap = 0.2; pw = (CW - 3 * gap) / 4; ph = 1.58; rp = ph + 0.78
    for i, (f, a, b) in enumerate(steps):
        r, c = divmod(i, 4)
        x = MX + c * (pw + gap); y = y0 + 0.12 + r * rp
        image(s, KIT(f + '.jpg'), x, y, pw, ph, focus=(0.5, 0.5))
        text(s, x, y + ph + 0.1, pw, 0.3, [[(f'{i + 1}  ', {'color': T['accent']}), (a, {})]], size=14, bold=True, label='wf ' + a)
        text(s, x + 0.26, y + ph + 0.42, pw - 0.26, 0.26, b, size=11, color=T['text2'], label='wf d ' + a)
    x = MX + 3 * (pw + gap); y = y0 + 0.12 + rp
    rect(s, x, y, pw, ph + 0.66, fill=T['dark'])
    text(s, x + 0.25, y + 0.22, pw - 0.4, 1.8,
         [[('핸드 1개', {'size': 22})], [('사람용 도구 여러 개', {})], [('작업 7종', {})], [('툴 교체 최소화', {'color': T['accent']})]],
         size=15, bold=True, color=T['on_dark'], space_after=5, label='wf sum')
    text(s, x + 0.25, y + ph + 0.3, pw - 0.4, 0.26, '툴 교체 최소화는 목표 (미검증)', size=10, color=T['on_dark2'], label='wf sum note')
    foot(s, 5, note='콘셉트 렌더링 · Seed 기간 실제 주방 반복시험으로 단계별 완료율·사람 개입 시간 검증')
    notes(s, '실제 주방 작업 흐름: 재료 집기 → 용기 열기 → 팬에 투입 → 집게 사용 → 젓기 → 노브 조작 → 플레이팅. '
             '핸드 1개, 사람용 도구 여러 개, 작업 7종. 툴 교체 0회는 검증되지 않았으므로 "툴 교체 최소화"를 목표로 표기.')


# ---------------------------------------------------------------- 06 why now
def s06(prs):
    s = new_slide(prs, '06 why now')
    y0 = header(s, 'WHY NOW', "AI가 발전할수록 병목은 '손'으로 이동합니다",
                '주방은 가장 다양한 현실 조작 환경, 손과 Skill 계층의 가치가 커지는 시점')
    steps = [('AI · VLA 발전', '로봇이 할 일을 이해하기 시작'), ('인지·판단 향상', '보고 계획하는 능력 향상'),
             ('로봇 팔·컴퓨팅 상용화', '몸과 연산은 이미 보급'), ('현실 조작이 새 병목', '사람용 물체·도구·손잡이를 안정적으로 다루기'),
             ('주방 = 가장 다양한 조작 환경', '도구·형상·힘 조절, 모두 사람 손 기준'), ('손 · Skill 계층 가치 증가', 'SoftHand가 선점하려는 계층')]
    n = 6; gap = 0.1; sw = (CW - (n - 1) * gap) / n; base = 5.42; top0 = 3.55; rise = 0.25
    for i, (a, b) in enumerate(steps):
        x = MX + i * (sw + gap); top = top0 - i * rise
        kind = 'soft' if i < 3 else ('dark' if i < 5 else 'accent')
        fill = {'soft': 'ECEEF0', 'dark': T['dark'], 'accent': T['accent']}[kind]
        rect(s, x, top, sw, base - top, fill=fill)
        fc = T['text'] if kind == 'soft' else 'FFFFFF'
        fc2 = {'soft': T['text2'], 'dark': 'B9BEC5', 'accent': 'FFE6DA'}[kind]
        text(s, x + 0.15, top + 0.15, 0.6, 0.26, f'{i + 1:02d}', size=11, bold=True,
             color='FFFFFF' if kind == 'accent' else T['accent'])
        text(s, x + 0.15, top + 0.46, sw - 0.28, 0.62, a, size=14, bold=True, color=fc, label='step ' + a)
        text(s, x + 0.15, top + 1.1, sw - 0.28, 0.7, b, size=11, color=fc2, label='step d ' + a)
    by = base + 0.24
    text(s, MX, by, 6, 0.26, '주방이 어려운 조작 환경인 이유', size=12, bold=True, color=T['muted'])
    reasons = [('도구가 다양', '팬·냄비·집게·국자·칼·용기'), ('형상이 계속 바뀜', '재료·메뉴·용기마다 다름'),
               ('접촉·힘 조절 필요', '젓기·뒤집기·누르기·돌리기'), ('사람 손 기준 설계', '손잡이·노브·버튼·문')]
    rw4 = CW / 4
    for i, (a, b) in enumerate(reasons):
        x = MX + i * rw4
        if i: vline(s, x - 0.12, by + 0.4, 0.6)
        text(s, x, by + 0.36, rw4 - 0.25, 0.3, a, size=14, bold=True, label='why ' + a)
        text(s, x, by + 0.68, rw4 - 0.25, 0.28, b, size=11.5, color=T['text2'], label='why d ' + a)
    foot(s, 6, note='근거: AI·VLA, 로봇 보급, 손이 병목이라는 업계 발언과 사례는 부록 A7')
    notes(s, '투자 논리: AI·VLA 발전 → 로봇의 인지·판단 향상 → 로봇 팔과 컴퓨팅은 이미 상용화 → 현실 세계와 접촉하는 조작이 새 병목 → '
             '주방은 도구가 다양하고 형상이 바뀌고 힘 조절이 필요하며 모두 사람 손 기준이라 가장 다양한 조작 환경 → Kitchen Robotics가 커질수록 손과 Skill 계층의 가치 증가. '
             '"왜 Kitchen Robotics인가"가 아니라 "왜 지금 조작 계층인가"에 대한 답.')


# ---------------------------------------------------------------- 07 commercial + home
def s07(prs):
    s = new_slide(prs, '07 markets')
    y0 = header(s, 'MARKET', '하나의 조작 플랫폼, 두 개의 큰 시장', '상업용 주방과 가정용 주방을 같은 손과 Skill로 연결')
    iy = y0 + 0.15; ih = 2.3; cw_ = 4.6
    cols = [(MX, 'pro_wide.jpg', (0.5, 0.42), '상업용 주방', 'Commercial Kitchen', '식당 · 프랜차이즈 · 급식 · 호텔 · 케이터링 · 센트럴키친',
             ['인력 부족 · 인건비 · 반복 작업', '긴 가동시간 · 다메뉴 대응', '프랜차이즈 확산 · 운영 표준화']),
            (W - MX - cw_, 'lx_wide.jpg', (0.56, 0.5), '가정용 주방', 'Home Kitchen', '조리 · 식사 준비 · 재료 손질 · 가전 조작 · 수납 · 식기 정리',
             ['다양한 메뉴 · 물체 · 도구', '기존 가전 · 냉장고 · 수납 사용', '가사 부담 감소 · 가정용 로봇과 결합'])]
    for x, f, foc, ttl, en, seg, vals in cols:
        image(s, KIT(f), x, iy, cw_, ih, focus=foc)
        text(s, x, iy + ih + 0.14, cw_, 0.36, [[(ttl, {}), ('   ' + en, {'size': 11, 'bold': False, 'color': T['muted']})]],
             size=18, bold=True, label='mk ' + ttl)
        text(s, x, iy + ih + 0.56, cw_, 0.26, seg, size=11, color=T['text2'], label='mk seg ' + ttl)
        text(s, x, iy + ih + 0.92, cw_, 0.85, vals, size=12.5, bullet='•', indent=0.17, space_after=3, label='mk vals ' + ttl)
    cx = MX + cw_ + 0.35; cwc = W - MX - cw_ - 0.35 - cx
    text(s, cx, iy, cwc, 0.28, '공통 조작 Skill', size=12, bold=True, color=T['accent'], align='c')
    skills = [('집기', 'Pick'), ('열기', 'Open'), ('붓기', 'Pour'), ('젓기', 'Stir'), ('뒤집기', 'Flip'), ('돌리기', 'Turn'),
              ('누르기', 'Press'), ('썰기', 'Cut'), ('옮기기', 'Move'), ('담기', 'Plate')]
    yy = iy + 0.4
    for ko, en in skills:
        text(s, cx, yy, cwc, 0.3, [[(ko, {'bold': True}), ('  ' + en, {'size': 10.5, 'color': T['muted']})]], size=13.5, align='c', label='sk ' + ko)
        yy += 0.345
    am = iy + ih / 2
    arrow(s, cx + 0.02, am, MX + cw_ + 0.06, am, color=T['accent'], lw=1.5)
    arrow(s, cx + cwc - 0.02, am, W - MX - cw_ - 0.06, am, color=T['accent'], lw=1.5)
    by = 6.28
    rect(s, MX, by, CW, 0.62, fill=T['soft'])
    text(s, MX + 0.22, by, CW - 0.44, 0.62,
         [[('Seed 첫 실행 (검증 대상)   ', {'bold': True, 'color': T['accent']}),
           ('두 시장 공통 작업 중 집게·팬·용기·노브·버튼·문 반복 작업부터  ·  상업용 주방 유료 PoC + 가정용 주방 환경 벤치 검증', {})],
          [('PoC 대상 고객군 (가설)   ', {'bold': True, 'color': T['text']}),
           ('다메뉴 조리 라인을 운영하는 외식·급식·센트럴키친, 창업 후 90일 내 고객 인터뷰 30곳으로 검증', {})]],
         size=11, anchor='m', space_after=2, label='seed scope')
    foot(s, 7, note='조리·식당 서비스 인력 부족률, 코로나 이전 대비 약 2배 (2023, 부록 A8) · 콘셉트 렌더링')
    notes(s, '상업용과 가정용 모두 핵심 시장. 제품 요구조건은 다르지만 집기·열기·붓기·젓기·뒤집기·돌리기·누르기·썰기·옮기기·담기 같은 기본 조작은 공통. '
             '두 시장을 잇는 자산은 "사람이 주방에서 하는 기본 조작 Skill". 비전은 두 시장 전체, Seed 실행은 집게·팬·용기·노브·버튼·문 반복 작업으로 좁힘 '
             '(큰 목표 + 좁은 첫 실행). 실제 첫 적용처는 미확정이므로 검증 대상으로 표기.')


# ---------------------------------------------------------------- 08 customer economics
def s08(prs):
    s = new_slide(prs, '08 economics')
    y0 = header(s, 'CUSTOMER VALUE', '메뉴가 바뀌어도 다시 만들지 않는 자동화',
                '고객의 비교 기준: 핸드 가격이 아닌, 메뉴·작업이 바뀔 때마다 드는 하드웨어·주방 개조·통합 비용')
    lw_ = 1.55; gap = 0.3; n = 6; cw_ = (CW - lw_ - (n - 1) * gap) / n; chh = 0.66
    rows = [('기존 방식', T['text'], [('새 작업·메뉴', 'soft'), ('전용 하드웨어', 'dark'), ('툴링', 'dark'), ('주방 개조', 'dark'), ('통합', 'dark'), ('검증', 'soft')]),
            ('SoftHand', T['accent'], [('새 작업·메뉴', 'soft'), ('같은 핸드', 'accent'), ('기존 Skill 재사용', 'accent_soft'), ('필요한 Skill 추가', 'soft'), ('보정', 'soft'), ('검증', 'soft')])]
    y = y0 + 0.32
    for lab, lc, chips in rows:
        text(s, MX, y, lw_, chh, lab, size=16, bold=True, color=lc, anchor='m')
        for i, (t, k) in enumerate(chips):
            x = MX + lw_ + i * (cw_ + gap)
            fill = {'soft': T['soft'], 'dark': '3A3E44', 'accent': T['accent'], 'accent_soft': T['accent_soft']}[k]
            col = 'FFFFFF' if k in ('dark', 'accent') else (T['accent'] if k == 'accent_soft' else T['text'])
            chip(s, x, y, cw_, chh, t, fill=fill, color=col, size=12.5, label='flow ' + t)
            if i: arrow(s, x - gap + 0.06, y + chh / 2, x - 0.06, y + chh / 2, color=T['muted'], lw=1.0)
        y += chh + 0.36
    text(s, MX + lw_, y - 0.26, CW - lw_, 0.26, '엔지니어링·검증은 계속 필요, 줄어드는 폭을 고객 현장에서 측정', size=11, color=T['muted'])
    ky = y + 0.18
    hline(s, MX, ky, CW, color=T['text'], lw=1.0)
    text(s, MX, ky + 0.14, 4, 0.3, 'Seed PoC에서 측정할 지표', size=15, bold=True)
    text(s, MX + 3.3, ky + 0.18, 8.5, 0.26, '고객 기존 수치 대비 · 가상의 절감률·ROI는 제시하지 않음', size=11, color=T['muted'])
    kpis = ['인력 투입 시간', '자동화 CapEx', '메뉴 추가 비용', '통합 엔지니어링 시간', '메뉴 전환 시간', '로봇 가동률', '투자 회수기간']
    kw = CW / 7
    for i, k in enumerate(kpis):
        x = MX + i * kw
        if i: vline(s, x - 0.1, ky + 0.66, 0.95)
        xx = x + (0.04 if i else 0)
        text(s, xx, ky + 0.64, kw - 0.22, 0.6, k, size=14, bold=True, label='kpi ' + k)
        text(s, xx, ky + 1.3, kw - 0.22, 0.26, 'PoC에서 측정', size=11, color=T['accent'])
    foot(s, 8, note='감소 폭은 고객 기존 수치 확보 후 PoC 결과로 산정 · 유료 PoC 자체가 지불의사 검증')
    notes(s, '고객은 손을 사는 것이 아니라 메뉴가 바뀌어도 다시 만들지 않는 자동화를 산다. 기존 방식은 새 메뉴마다 전용 하드웨어·툴링·주방 개조·통합·검증, '
             'SoftHand는 같은 핸드에서 기존 Skill을 재사용하고 필요한 Skill만 추가. 실제 수치가 없으므로 절감률·ROI를 만들지 않고 PoC 측정 지표로 제시.')


# ---------------------------------------------------------------- 09 skill platform + data flywheel
def _flywheel(s, cx, cy, R, nodes, hi=2, nw=1.62, nh=0.56):
    import math
    rect(s, cx - R, cy - R, 2 * R, 2 * R, line=T['grey_bar'], lw=1.5, shape=MSO_SHAPE.OVAL)
    n = len(nodes)
    for i in range(n):
        th = math.radians(-90 + (i + 0.5) * 360 / n)
        tx, ty = cx + R * math.cos(th), cy + R * math.sin(th)
        tri = rect(s, tx - 0.09, ty - 0.08, 0.18, 0.16, fill=T['muted'], shape=MSO_SHAPE.ISOSCELES_TRIANGLE)
        tri.rotation = math.degrees(th) + 180
    for i, nd in enumerate(nodes):
        th = math.radians(-90 + i * 360 / n)
        nx, ny = cx + R * math.cos(th), cy + R * math.sin(th)
        ours = i == hi
        rect(s, nx - nw / 2, ny - nh / 2, nw, nh, fill=T['accent'] if ours else 'FFFFFF', line=None if ours else T['text'], lw=1.0)
        text(s, nx - nw / 2 + 0.06, ny - nh / 2, nw - 0.12, nh, nd, size=12, bold=True, color='FFFFFF' if ours else T['text'],
             align='c', anchor='m', label='fw ' + nd)


def s09(prs):
    s = new_slide(prs, '09 skill platform')
    y0 = header(s, 'PLATFORM', '메뉴가 늘수록 장비가 아니라 Skill이 쌓입니다', 'From Hardware Expansion to Skill Expansion')
    lx = MX; lw = 6.3; y = y0 + 0.2
    text(s, lx, y, 3, 0.26, '기존 자동화', size=12, bold=True, color=T['muted'])
    pw = 0.86; aw = 0.3; pg = 0.2
    for i, m in enumerate('ABC'):
        x = lx + i * (2 * pw + aw + pg)
        chip(s, x, y + 0.34, pw, 0.42, f'메뉴 {m}', fill=T['soft'], size=11.5)
        arrow(s, x + pw + 0.04, y + 0.55, x + pw + aw - 0.04, y + 0.55)
        chip(s, x + pw + aw, y + 0.34, pw, 0.42, f'장비 {m}', fill='5A5F66', color='FFFFFF', size=11.5)
    y2 = y + 1.0
    text(s, lx, y2, 3, 0.26, 'SoftHand', size=12, bold=True, color=T['accent'])
    w1, w2 = 2.3, 1.5
    chip(s, lx, y2 + 0.34, w1, 0.42, '핸드 1개 + Kitchen Skills', fill=T['accent'], color='FFFFFF', size=11.5)
    arrow(s, lx + w1 + 0.05, y2 + 0.55, lx + w1 + 0.3, y2 + 0.55)
    chip(s, lx + w1 + 0.35, y2 + 0.34, w2, 0.42, '여러 레시피', fill=T['dark'], color='FFFFFF', size=11.5)
    arrow(s, lx + w1 + w2 + 0.4, y2 + 0.55, lx + w1 + w2 + 0.65, y2 + 0.55)
    chip(s, lx + w1 + w2 + 0.7, y2 + 0.34, w2, 0.42, '여러 주방', fill=T['dark'], color='FFFFFF', size=11.5)
    text(s, lx, y2 + 0.84, lw, 0.26, '집기 · 붓기 · 젓기 · 뒤집기 · 돌리기 · 담기의 조합 + 필요한 Skill 추가 (목표)', size=11, color=T['text2'], label='skill combo')
    iy = y2 + 1.36
    text(s, lx, iy, lw, 0.26, "같은 '집게 사용' Skill, 다른 주방", size=12, bold=True, color=T['muted'])
    iw = (lw - 0.2) / 2; ih = 1.72
    for i, (f, lab) in enumerate([('lx_tongs.jpg', '가정용 주방'), ('pro_tongs.jpg', '상업용 주방')]):
        x = lx + i * (iw + 0.2)
        image(s, KIT(f), x, iy + 0.34, iw, ih, focus=(0.5, 0.5))
        text(s, x, iy + 0.4 + ih, iw, 0.26, lab, size=11, color=T['text2'])
    fx = lx + lw + 0.55; fw = W - MX - fx
    text(s, fx, y, fw, 0.26, 'DATA FLYWHEEL  ·  향후 축적될 데이터 구조', size=12, bold=True, color=T['muted'])
    nodes = ['더 많은 주방', '더 많은 실제 작업', '조작·실패 데이터', '더 나은 Skill·복구', '더 많은 도구·레시피']
    cyc = y + 2.05
    _flywheel(s, fx + fw / 2, cyc, 1.42, nodes)
    text(s, fx + fw / 2 - 0.9, cyc - 0.3, 1.8, 0.6, '배치가 늘수록\nSkill이 좋아지는 구조', size=11, color=T['text2'], align='c', label='fw center')
    dy = cyc + 1.42 + 0.5
    text(s, fx, dy, fw, 0.26, '축적 대상: 실패 · 미끄러짐 · 위치 오차 · 재파지 · 힘 보정 · 복구 행동', size=11.5, bold=True, label='fw data')
    text(s, fx, dy + 0.32, fw, 0.26, '현재 보유 데이터 없음, Seed 기간 수집 시작 (목표)', size=11, color=T['accent'], label='fw now')
    foot(s, 9, note='콘셉트 렌더링 · 데이터 계획·권리 원칙은 부록 A12')
    notes(s, '기존 자동화는 메뉴 수만큼 장비가 늘어남. SoftHand는 같은 핸드에 Skill을 조합·추가해 여러 레시피와 여러 주방으로 확장하는 구조를 목표. '
             'From Hardware Expansion to Skill Expansion. 배치가 늘수록 실패·미끄러짐·위치 오차·재파지·힘 보정·복구 데이터가 쌓여 Skill이 좋아지는 구조. '
             '현재 보유 데이터는 없으며 "향후 축적될 데이터 구조"로 표기.')


# ---------------------------------------------------------------- 10 competition + moat
def s10(prs):
    s = new_slide(prs, '10 competition')
    y0 = header(s, 'COMPETITION · MOAT', '경쟁자는 다른 로봇 손이 아니라, 작업마다 새로 만드는 전용 자동화')
    cats = [('전용 주방 자동화', '예: 로봇 전용 주방, 튀김·패티·치킨 조리 로봇', '강점', '특정 메뉴·작업에 최적화, 높은 반복성 가능',
             '한계', '다른 메뉴·주방으로 확장 어려움'),
            ('전통 그리퍼 · EOAT', '예: 평행·진공·맞춤 그리퍼', '강점', '산업용 집기·놓기에 강함',
             '한계', '사람용 도구·다양한 주방 조작부에 한계 가능'),
            ('SoftHand + Kitchen Skills', '기존 사람용 주방·도구를 그대로 사용', '목표', '여러 작업을 하나의 조작 구조로 수행',
             '과제', '실제 주방 검증 전, 우위는 미검증')]
    gap = 0.34; cw_ = (CW - 2 * gap) / 3; ty = y0 + 0.32
    for i, (nm, ex, l1, v1, l2, v2) in enumerate(cats):
        x = MX + i * (cw_ + gap); ours = i == 2
        if ours: rect(s, x - 0.16, ty - 0.16, cw_ + 0.32, 2.42, fill=T['accent_soft'])
        text(s, x, ty, cw_, 0.36, nm, size=17, bold=True, color=T['accent'] if ours else T['text'], label='cat ' + nm)
        text(s, x, ty + 0.42, cw_, 0.26, ex, size=11.5, color=T['text2'], label='cat ex ' + nm)
        hline(s, x, ty + 0.82, cw_, color=T['text'], lw=1.0)
        for j, (l, v) in enumerate([(l1, v1), (l2, v2)]):
            yy = ty + 0.94 + j * 0.62
            text(s, x, yy, 0.6, 0.26, l, size=11, color=T['muted'])
            text(s, x + 0.6, yy - 0.02, cw_ - 0.6, 0.56, v, size=13, label=f'cat {nm} {l}')
            if j == 0: hline(s, x, yy + 0.52, cw_)
    my = ty + 2.5
    text(s, MX, my, CW, 0.3, [[('SOFTHAND MOAT   ', {'color': T['accent']}),
                               ('해자는 Hand 하나가 아니라 Hand + Skill + Runtime + Data의 누적 구조', {})]], size=14, bold=True, label='moat title')
    moat = [('Hardware', '주방용 Soft-Rigid 조작', '설계 목표'), ('Skill Library', '반복 사용 가능한 조작 Skill', '구축 목표'),
            ('Recovery Data', '실패와 복구 데이터', '향후 축적'), ('Cross-Robot Runtime', '다른 로봇에서 Skill 재사용', '검증 예정'),
            ('Installed Base', '다양한 주방의 실제 작업 경험', '장기 목표')]
    n = 5; ag = 0.3; bw = (CW - (n - 1) * ag) / n; by = my + 0.45; bh = 1.4
    for i, (a, b, st) in enumerate(moat):
        x = MX + i * (bw + ag)
        rect(s, x, by, bw, bh, fill=T['dark'])
        text(s, x + 0.18, by + 0.12, bw - 0.3, 0.56, a, size=13.5, bold=True, color='FFFFFF', label='moat ' + a)
        text(s, x + 0.18, by + 0.68, bw - 0.3, 0.46, b, size=11, color='B9BEC5', label='moat d ' + a)
        text(s, x + 0.18, by + bh - 0.34, bw - 0.3, 0.24, st, size=10.5, bold=True, color=T['accent'])
        if i: arrow(s, x - ag + 0.05, by + bh / 2, x - 0.05, by + bh / 2, color=T['text'], lw=1.25)
    foot(s, 10, note='공개 정보 기반 정성 비교, 독립 비교시험 아님 · 회사별 사례·출처는 부록 A6')
    notes(s, '가장 큰 경쟁자는 다른 로봇 손이 아니라 작업마다 새 전용 자동화를 만드는 방식. 전용 주방 자동화(예: Moley 로봇 주방, Miso Flippy, 에니아이 알파그릴, '
             '로보아르테)는 특정 메뉴에 강하지만 다른 메뉴·주방 확장이 어려움. 그리퍼·EOAT는 산업용 집기에 강하지만 사람용 도구 조작에 한계 가능. '
             '다른 핸드 회사가 들어오면? 해자는 Hand + Skill Library + Recovery Data + Cross-Robot Runtime + Installed Base의 누적. 모두 현재 목표 단계.')


# ---------------------------------------------------------------- 11 business model + base case / scale triggers
def s11(prs):
    s = new_slide(prs, '11 business model')
    B = M['base']
    y0 = header(s, 'BUSINESS MODEL', '하드웨어로 검증하고, Skill·Runtime 반복매출로 확장합니다')
    stages = [('1 · 핵심 시장', '상업용 + 가정용 주방', '식당 · 프랜차이즈 · 급식 · 호텔\n가정 조리 · 식사 준비 · 가전 조작',
               '초기', '유료 PoC · 하드웨어 · 통합'),
              ('2 · 제품 확장', '도구 · Skill · 레시피', '더 많은 도구 · 더 많은 Skill\n더 많은 레시피 · 더 많은 주방',
               '중기', 'SoftHand · Kitchen Skill 패키지 · Runtime · 유지보수'),
              ('3 · 유통 확장', '파트너 · OEM 채널', '직접 B2B · 주방 자동화 파트너\n로봇 OEM · 가전 OEM · 스마트홈',
               '중기~장기', '파트너 판매 · OEM · 라이선스'),
              ('4 · 장기 Scale 채널', 'Built-in 보급 (B2B2C)', '건설사 · 디벨로퍼 · 호텔\n시니어 주거 · 주거 플랫폼',
               '장기', '내장 Runtime · Built-in 파트너십')]
    gap = 0.3; cw_ = (CW - 3 * gap) / 4; ty = y0 + 0.24
    for i, (st, nm, mk, when, rv) in enumerate(stages):
        x = MX + i * (cw_ + gap)
        text(s, x, ty, cw_, 0.26, st, size=11.5, bold=True, color=T['accent'])
        text(s, x, ty + 0.3, cw_, 0.36, nm, size=16, bold=True, label='bm ' + nm)
        hline(s, x, ty + 0.74, cw_, color=T['text'], lw=1.0)
        text(s, x, ty + 0.84, cw_, 0.5, mk, size=11.5, color=T['text2'], label='bm mk ' + nm)
        hline(s, x, ty + 1.42, cw_)
        text(s, x, ty + 1.52, cw_, 0.24, when + ' 매출', size=10.5, bold=True, color=T['muted'])
        text(s, x, ty + 1.78, cw_, 0.5, rv, size=12, bold=True, label='bm rv ' + nm)
        if i < 3: arrow(s, x + cw_ + 0.04, ty + 0.13, x + cw_ + gap - 0.06, ty + 0.13, color=T['accent'])
    fy = 4.62; fh = 2.22
    lw2 = 5.7
    rect(s, MX, fy, lw2, fh, fill=T['soft'])
    text(s, MX + 0.25, fy + 0.16, lw2 - 0.5, 0.3, [[('Base Case  ', {}), ('하방', {'color': T['accent']})]], size=15, bold=True)
    text(s, MX + 0.25, fy + 0.52, 2.3, 0.5, '기존 계획 기반\n대규모 주방·OEM 매출 제외', size=11, color=T['text2'], label='base desc')
    text(s, MX + 0.25, fy + 1.16, 2.3, 0.5, f'{B["rev"][4]:.1f}억 원', size=24, bold=True, label='base y5')
    text(s, MX + 0.25, fy + 1.66, 2.3, 0.26, '5년차 매출 (가정)', size=11, color=T['text2'])
    cx, cyy, cww, chh = MX + 2.55, fy + 0.25, lw2 - 2.75, fh - 0.4
    plot = (0.02, 0.12, 0.96, 0.72); vmax = 52
    column_chart(s, cx, cyy, cww, chh, ['1년', '2년', '3년', '4년', '5년'], [('매출', B['rev'])], [T['grey_bar']], vmax=vmax,
                 show_labels=False, gap=45, plot=plot, size=10)
    px, py, pw, ph = plot
    for i, v in enumerate(B['rev']):
        ccx = cx + cww * (px + pw * (i + 0.5) / 5)
        top = cyy + chh * (py + ph * (1 - v / vmax))
        text(s, ccx - 0.4, top - 0.27, 0.8, 0.24, f'{v:.1f}', size=10, bold=i == 4, align='c', check=False)
    rx = MX + lw2 + 0.3; rw = W - MX - rx
    rect(s, rx, fy, rw, fh, fill=T['dark'])
    text(s, rx + 0.28, fy + 0.16, rw - 0.5, 0.3, [[('Scale Triggers  ', {'color': T['on_dark']}), ('상방 · 수치 미산정', {'color': T['accent']})]],
         size=15, bold=True)
    trig = ['주방 제품 검증', 'Skill 재사용', '로봇 OEM 채택', '가전사 파트너십', '가정용 주방 확장', 'Built-in 채널']
    tw3 = (rw - 0.56) / 3
    for i, t in enumerate(trig):
        r, c = divmod(i, 3)
        x = rx + 0.28 + c * tw3; yy = fy + 0.7 + r * 0.72
        hline(s, x, yy, tw3 - 0.2, color='3A3E44')
        text(s, x, yy + 0.1, 0.35, 0.3, f'{i + 1}', size=13, bold=True, color=T['accent'])
        text(s, x + 0.32, yy + 0.1, tw3 - 0.55, 0.56, t, size=13, bold=True, color=T['on_dark'], label='trig ' + t)
    foot(s, 11, note='건설사는 핵심 시장이 아닌 장기 채널 (부록 A13) · Base Case 손익·민감도 부록 A10 · 상방 매출은 산정하지 않음')
    notes(s, f'초기에는 유료 PoC·하드웨어·통합으로 검증하고, 고객이 늘수록 Kitchen Skill 패키지·Runtime·유지보수 반복매출 비중을 높임(Base Case 재사용 매출 비중 '
             f'5년차 {B["reuse_share"][4] * 100:.0f}%, 가정). 장기에는 로봇·가전 OEM, 라이선스, 내장 Runtime, Built-in 파트너십. 건설사는 핵심 시장이 아닌 장기 B2B2C 채널. '
             f'Base Case(5년차 {B["rev"][4]:.1f}억 원)는 기존 계획 기반으로 대규모 주방·OEM 매출을 제외한 하방, Scale Triggers가 상방이며 상방 수치는 만들지 않음.')


# ---------------------------------------------------------------- 12 seed validation plan (what we need to prove)
def s12(prs):
    s = new_slide(prs, '12 validation')
    y0 = header(s, 'SEED VALIDATION PLAN', '20억 원 · 24개월로 증명할 3가지',
                '로봇 핸드 아이디어를 반복 판매 가능한 Kitchen Robotics Platform으로 증명')
    by = y0 + 0.2; bh = 1.42; ag = 0.42
    w1, w2 = 2.45, 3.55; w3 = CW - w1 - w2 - 2 * ag
    x1 = MX; x2 = x1 + w1 + ag; x3 = x2 + w2 + ag
    rect(s, x1, by, w1, bh, fill=T['soft'])
    text(s, x1 + 0.22, by + 0.16, w1 - 0.4, 0.26, 'TODAY', size=11, bold=True, color=T['muted'])
    text(s, x1 + 0.22, by + 0.46, w1 - 0.4, 0.9, ['콘셉트', '기술 구조', '초기 설계'], size=13.5, bold=True, space_after=2, label='today')
    rect(s, x2, by, w2, bh, fill=T['accent'])
    text(s, x2 + 0.22, by + 0.16, w2 - 0.4, 0.26, 'SEED', size=11, bold=True, color='FFE6DA')
    text(s, x2 + 0.22, by + 0.42, w2 - 0.4, 0.42, '20억 원 · 24개월', size=21, bold=True, color='FFFFFF', label='seed amt')
    text(s, x2 + 0.22, by + 0.88, w2 - 0.4, 0.5, '인력 9.6 · 시제품·내구 2.7 · 시험 셀·주방 PoC 2.8\nSW·품질·IP 1.7 · 운영 1.5 · 예비비 1.7 (억 원)',
         size=10, color='FFFFFF', label='seed uof')
    rect(s, x3, by, w3, bh, fill=T['dark'])
    text(s, x3 + 0.22, by + 0.16, w3 - 0.4, 0.26, 'VALUE INFLECTION  ·  24개월 목표', size=11, bold=True, color=T['accent'])
    vi = ['실제 주방 시제품', '실제 주방 조작', '유료 PoC', '재구매 고객', '재사용 Kitchen Skill', '로봇 2종 검증', '양산 가능 설계', 'Series A 준비']
    hw = (w3 - 0.44) / 2
    for i, v in enumerate(vi):
        c, r = divmod(i, 4)
        text(s, x3 + 0.22 + c * hw, by + 0.46 + r * 0.235, hw - 0.1, 0.24, v, size=11.5, bold=True, color=T['on_dark'], label='vi ' + v)
    arrow(s, x1 + w1 + 0.05, by + bh / 2, x2 - 0.05, by + bh / 2, color=T['text'], lw=1.5)
    arrow(s, x2 + w2 + 0.05, by + bh / 2, x3 - 0.05, by + bh / 2, color=T['text'], lw=1.5)
    text(s, MX, by + bh + 0.08, CW, 0.26, [[('왜 지금 Seed인가   ', {'bold': True, 'color': T['accent']}),
                                            ('아직 위험한 단계이지만, 세 가지 가설이 검증되면 가치 상승 폭이 가장 큰 시점', {})]],
         size=11.5, color=T['text2'], label='seed timing')
    py = by + bh + 0.46
    proofs = [('실제 주방에서 일한다', [('검증', '검증 대상 6종 작업 실제 주방 반복시험'), ('목표', '승인 작업 완료율 95%+ · 내구 30만 회'), ('점검', 'M6 벤치 → M12 현장')]),
              ('고객이 돈을 낸다', [('검증', '고객 기존 수치 대비 KPI 측정'), ('목표', '유료 PoC 5건 · 재구매 2곳 · 공동개발 고객 3곳'), ('점검', 'M12 첫 유료 PoC → M24 재구매')]),
              ('Skill이 재사용된다', [('검증', '다른 메뉴·주방·로봇에 같은 Skill 적용'), ('목표', '로봇 2종 · 상업용/가정용 환경 공통 Skill'), ('점검', 'M12 재사용률 측정 → M24 이식 검증')])]
    gap = 0.34; pcw = (CW - 2 * gap) / 3
    for i, (t, rows) in enumerate(proofs):
        x = MX + i * (pcw + gap)
        text(s, x, py - 0.04, 0.5, 0.55, str(i + 1), size=30, bold=True, color=T['accent'], line=0.9)
        text(s, x + 0.5, py + 0.04, pcw - 0.5, 0.42, t, size=18, bold=True, label='proof ' + t)
        hline(s, x, py + 0.58, pcw, color=T['text'], lw=1.0)
        yy = py + 0.68
        for lab, val in rows:
            text(s, x, yy, 0.5, 0.24, lab, size=10.5, color=T['muted'])
            hh = text_h(val, 11.5, pcw - 0.52)
            text(s, x + 0.52, yy - 0.01, pcw - 0.52, hh + 0.02, val, size=11.5, label=f'proof {i} {lab}')
            yy += max(hh, 0.24) + 0.1
    ey = 6.34
    rect(s, MX, ey, CW, 0.5, fill=T['soft'])
    ev = '○ 시제품   ○ 도구 조작 시험   ○ 주방 시험   ○ 고객 인터뷰   ○ 주방 운영사·SI 논의   ○ LOI   ○ 공동개발   ○ 특허 검토'
    text(s, MX + 0.22, ey, CW - 0.44, 0.5, [[('현재 확보된 증거   ', {'bold': True, 'color': T['text']}), (ev + '   ', {}),
                                              ('[확보 항목 ● 표시 · 정보 입력 필요]', {'color': T['accent']})]],
         size=10.5, color=T['text2'], anchor='m', label='evidence')
    foot(s, 12, note='모든 목표는 계획이며 실적 아님 · 증거 확보 시 이 장을 Proof 중심으로 바꿔 앞쪽에 배치 · 단계별 점검 기준 부록 A2')
    notes(s, '20억 원으로 회사가 무엇으로 바뀌는가: 오늘은 콘셉트·기술 구조·초기 설계, 24개월 뒤 목표는 실제 주방 시제품·실제 주방 조작·유료 PoC·재구매·재사용 Skill·'
             '로봇 2종 검증·양산 가능 설계·Series A 준비. 가장 중요한 세 가지 증명: 실제 주방에서 일한다, 고객이 돈을 낸다, 다른 메뉴·주방·로봇에서 Skill이 재사용된다. '
             '현재 확보된 증거는 확인되지 않아 빈 칸으로 두고, 확보 시 Proof를 로드맵보다 앞에 배치.')


# ---------------------------------------------------------------- 13 team
def s13(prs):
    s = new_slide(prs, '13 team')
    y0 = header(s, 'TEAM', '왜 우리가 이 문제를 풀 수 있는가', '창업자 2명 + 핵심 인력 6명 단계 채용')
    fx = MX; fw = 4.05
    for i, role in enumerate(['대표 · 사업/제품', 'CTO · 핸드 메카트로닉스']):
        yy = y0 + 0.25 + i * 1.55
        rect(s, fx, yy, 1.12, 1.3, fill=T['soft'])
        text(s, fx, yy + 0.5, 1.12, 0.3, '사진', size=11, color=T['muted'], align='c')
        text(s, fx + 1.34, yy, fw - 1.34, 0.36, '[이름 입력 필요]', size=17, bold=True)
        text(s, fx + 1.34, yy + 0.4, fw - 1.34, 0.28, role, size=12, bold=True, color=T['accent'])
        text(s, fx + 1.34, yy + 0.74, fw - 1.34, 0.56, '사업과 직접 연결되는 경력 한 줄\n[정보 입력 필요]', size=11.5, color=T['text2'], label='founder ' + role)
    hy = y0 + 3.3
    hline(s, fx, hy, fw, color=T['text'], lw=1.0)
    text(s, fx, hy + 0.12, fw, 0.28, 'Seed 채용 계획 (6명 단계 채용)', size=12, bold=True)
    text(s, fx, hy + 0.44, fw, 0.56, '기구·구동 · 제어·임베디드 · 로봇 SW·Skill\n현장 통합 · 비전·AI · 설계·품질', size=11.5, color=T['text2'], label='hire')
    rx = fx + fw + 0.55; rw = W - MX - rx
    rows = [('Problem Insight', '현장에서 문제를 직접 확인한 팀',
             '[창업자]가 [주방·자동화 현장]에서 [직접 겪은 문제]를 확인한 경험'),
            ('Build Capability', 'Hand · Robotics · Control · AI를 만들 수 있는 팀',
             '[핸드·로봇·제어·AI 개발 이력, 시제품·논문·특허 중 확인된 것]'),
            ('Market Access', '첫 주방 고객과 파트너에 닿을 수 있는 팀',
             '[외식·급식 운영사, 주방 설비·가전, 로봇 SI 등 실제 관계]')]
    yy = y0 + 0.25
    for i, (en, ans, ph_) in enumerate(rows):
        hline(s, rx, yy, rw, color=T['text'] if i == 0 else T['line'], lw=1.0 if i == 0 else 0.75)
        text(s, rx, yy + 0.14, rw, 0.26, en, size=11.5, bold=True, color=T['accent'])
        text(s, rx, yy + 0.44, rw, 0.36, ans, size=17, bold=True, label='team ' + en)
        text(s, rx, yy + 0.88, rw, 0.26, [[(ph_ + '  ', {}), ('[정보 입력 필요]', {'color': T['accent']})]], size=12,
             color=T['text2'], label='team ph ' + en)
        yy += 1.3
    hline(s, rx, yy, rw)
    text(s, MX, 6.5, CW, 0.26, [[('참여 조건   ', {'bold': True, 'color': T['text']}),
                                ('전업 참여 · 자기자본 투자 · 공동창업자 합류 · 현 직장 정리 계획  ', {}), ('[정보 입력 필요]', {'color': T['accent']})]],
         size=11, color=T['text2'], label='commit')
    foot(s, 13, note='없는 이력·성과는 만들지 않음 · 외부 제출 전 실제 정보로 교체')
    notes(s, '세 가지만 답함. Problem Insight: 왜 이 창업자가 이 문제를 발견했는가. Build Capability: 왜 이 팀이 Hand·Robotics·Control·AI를 만들 수 있는가. '
             'Market Access: 왜 첫 Kitchen 고객과 파트너를 확보할 수 있는가. 질문이 아닌 답을 보여주는 구조, 실제 정보가 없으므로 자리 표시만 유지.')


# ---------------------------------------------------------------- 14 seed ask + vision (closing)
def s14(prs):
    s = new_slide(prs, '14 closing', bg='17181B')
    image(s, KIT('lx_front.jpg'), 0, 0, W, H, focus=(0.5, 0.5))
    text(s, MX, 0.28, CW, 0.75, '모든 주방에서 일할 수 있는 로봇', size=36, bold=True, color='FFFFFF', align='c', label='cl title')
    text(s, MX, 0.98, CW, 0.3, 'The Robot That Can Work in Any Kitchen', size=14, color='B9BEC5', align='c', label='cl en')
    y = 5.66
    cols = [('상업용 주방 + 가정용 주방', 'FFFFFF'), ('SoftHand + Kitchen Skills', 'FFFFFF'), ('Seed 20억 원 · 24개월', T['accent'])]
    cw3 = CW / 3
    for i, (t, c) in enumerate(cols):
        if i: vline(s, MX + i * cw3, y + 0.04, 0.3, color='4A4F57')
        text(s, MX + i * cw3, y, cw3, 0.38, t, size=16, bold=True, color=c, align='c', label='cl col ' + t)
    text(s, MX, y + 0.56, CW, 0.34, '사람이 사용하는 주방을 바꾸지 않고, 로봇이 그 주방에서 일하게 만든다.', size=16, color='F3F3F1', align='c', label='cl msg')
    text(s, MX, y + 0.98, CW, 0.32, [[('전 세계 Kitchen Robotics의 표준 조작 플랫폼을 만든다', {'color': T['accent']}),
                                       ('   Building the Manipulation Standard for Kitchen Robotics', {'size': 11, 'bold': False, 'color': 'A9AEB5'})]],
         size=14, bold=True, align='c', label='cl vision')
    text(s, MX, H - 0.36, CW, 0.22, '[회사명 입력 필요]  ·  [대표자명 · 이메일 · 연락처 입력 필요]  ·  [라운드 진행 상황 · 투자 조건 입력 필요]  ·  이미지: 콘셉트 렌더링', size=9, color='8C9198', align='c', check=False)
    notes(s, '마지막 메시지. 모든 주방에서 일할 수 있는 로봇. 상업용 주방 + 가정용 주방, SoftHand + Kitchen Skills, Seed 20억 원 / 24개월. '
             '사람이 사용하는 주방을 바꾸지 않고 로봇이 그 주방에서 일하게 만든다. 전 세계 Kitchen Robotics의 표준 조작 플랫폼을 만든다.')


MAIN = [s01, s02, s03, s04, s05, s06, s07, s08, s09, s10, s11, s12, s13, s14]
