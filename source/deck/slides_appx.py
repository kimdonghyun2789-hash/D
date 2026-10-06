# SoftHand Seed 투자유치 사업계획서 v5 (최종본) - appendix (table-first, evidence and detail behind the main plan).
# Detail follows the business plan (사업계획서, 2026-10-06); sources are listed in A15.
from kit import *
import kit
from slides_main import M, RAW, REN, ORI, KIT, FOOT, ph, eok

APPX_LIST = [
    ('A1', '작성 전제와 사실·가정 구분'), ('A2', '작업군별 개발 단계와 도구별 제어'), ('A3', '핸드 설계 상세'), ('A4', '비전 AI·데이터 상세'),
    ('A5', '적용 장면: 제조 반복 취급'), ('A6', '적용 장면: 주방 작업'), ('A7', '로봇 주방 설치·운영 상세'), ('A8', '경쟁 상세'),
    ('A9', '시장 근거 상세'), ('A10', '로봇 기술 동향'), ('A11', '가격·원가·판매 조건 가정'), ('A12', '5개년 재무 상세와 민감도'),
    ('A13', 'Seed 자금 사용 상세'), ('A14', '안전·위생·인증·지식재산'), ('A15', '출처'),
]
TOP = 2.0          # content top on appendix slides


def aheader(s, code, title, sub=None):
    text(s, MX, 0.55, 8, 0.28, f'부록 {code}', size=11, bold=True, color=T['accent'])
    text(s, MX, 0.9, CW, 0.52, title, size=24, bold=True, line=0.95, label='atitle ' + code)
    if sub: text(s, MX, 1.46, CW, 0.3, sub, size=13, color=T['text2'], label='asub ' + code)


def afoot(s, code, note=None):
    footer(s, code, left=FOOT, note=note)


def bullets(s, x, y, w, items, size=12, gap=4, label='bullets', color=None):
    paras = [ph(it) if '[' in it else it for it in items]
    hh = text_h(items, size, w - 0.18, space_after=gap)
    text(s, x, y, w, hh + 0.05, paras, size=size, bullet='•', indent=0.18, space_after=gap, color=color or T['text2'], label=label)
    return hh


def block_title(s, x, y, w, t, color=None):
    text(s, x, y, w, 0.3, t, size=13, bold=True, color=color or T['text'])
    hline(s, x, y + 0.36, w, color=T['text'], lw=1.0)
    return y + 0.48


B_ = lambda t: (t, {'bold': True})
ACC = lambda t: (t, {'bold': True, 'color': T['accent']})


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
            y += 0.56
            hline(s, x, y - 0.12, 3.6)
    footer(s, 'A', left=FOOT)


# ---------------------------------------------------------------- A1 facts vs assumptions
def a01(prs):
    s = new_slide(prs, 'A1')
    aheader(s, 'A1', '작성 전제와 사실·가정 구분', '확인된 사실, 계획, 가정, 장기 확장 가능성, 확보가 필요한 자료를 구분해 표기')
    rows = [
        [B_('확인된 사실'), '사업계획서 초안(2026.10.6, 회사명 미정)과 개발 구상\n공개 자료 출처 확인: IFR, BCG, qbrobotics, Moley Robotics, YORI 연구(arXiv), ISO 10218-2:2025 등\n'
                         '법인·창업팀·특허·시제품·고객 계약·매출·보유 자금은 미확인', '회사 실적으로 표현하지 않음'],
        [B_('계획 (목표)'), '24개월 목표: 4지 제품 검증, 5지 알파, 로봇 주방 제한 메뉴 실증, 유료 실증 5건, 반복 발주 고객 2곳\n'
                          '12·24개월 성능 목표, 0~36개월 일정, 첫 90일 인터뷰 30곳, 핵심 인력 7명 단계 채용', '"목표", "계획"'],
        [B_('가정'), '가격·원가: 핸드 1,500/800만 원, 주방 셀 2억/1.4억 원, SW 계약 300/90만 원, 실증 총이익률 40%\n'
                   '5개년 판매량·매출·손익, 초기 접근시장 75억·60억 원, 고객 투자회수 예시, Seed 사용 계획', '"가정", "제안"'],
        [B_('장기 확장 가능성'), '5지 핸드 고도화와 휴머노이드 적용, 프리미엄 가정용 주방, 임대·RaaS, 레시피 실행 소프트웨어 확대', '"장기 가능성"\n기준 시나리오 미반영'],
        [B_('확보 필요 자료'), '법인·주주·핵심 인력 이력, 특허 소유권, 무편집 시험 영상·원시 로그, BOM·공급사 견적·수율\n'
                         '유료 실증 계약·고객 기준 성능, 월별 현금흐름, 시험·인증 범위, 고객 운영비·절감시간', '[정보 입력 필요]\n투자 실사 전 확보'],
    ]
    table(s, MX, TOP + 0.05, CW, ['구분', '현재 내용', '표기 원칙'], rows, col_w=[2.0, 7.43, 2.4], size=11.5, pad=0.08, max_h=4.3, label='A1 table')
    footnote(s, '이미지: 본 자료의 핸드·로봇 이미지는 모두 자체 콘셉트 렌더링이며 실제 시험 장면이 아님. 실물 확보 시 시제품 사진 → 시험 영상 → 고객 현장 순으로 교체')
    afoot(s, 'A1', note='사업계획서 작성 전제: 가격·사양·일정·투자금·시장 산정·매출 전망은 투자 검토용 제안·가정')


# ---------------------------------------------------------------- A2 task stages & per-tool control
def a02(prs):
    s = new_slide(prs, 'A2')
    aheader(s, 'A2', '작업군별 개발 단계와 도구별 제어', '승인된 도구 모델부터 등록하고 손잡이 위치·허용 하중을 관리')
    lw = 7.3
    rows = [[B_('식기·용기 정렬·적층'), ACC('1단계'), '파손·끼임 방지, 젖은 표면 미끄러짐, 적층 안정성'],
            [B_('드라이버·스패너'), '2단계', '저토크 작업부터 시작, 반력·토크 검증'],
            [B_('플라이어·집게'), '2~3단계', '손잡이를 유지하면서 개폐하는 다지 제어'],
            [B_('프라이팬·냄비'), '2~3단계', '내용물 포함 질량·모멘트, 고온 손잡이, 양손 분담'],
            [B_('오븐'), '3단계', '문·손잡이 조작, 트레이 취급, 열·끼임 관리'],
            [B_('나이프·해머'), '후속 단계', '절단·충격 특성, 파지 이탈 검증 후 제한 작업'],
            [B_('동적 물체·유연체'), '병행 기술개발', '속도 범위·형상 변화·가림 조건별 성능 분리 평가']]
    table(s, MX, TOP + 0.05, lw, ['작업군', '개발 순서', '검증 과제'], rows, col_w=[2.0, 1.4, 3.9], size=11.5, pad=0.085, max_h=4.6, label='A2 table')
    rx = MX + lw + 0.45; rw = W - MX - rx
    y = block_title(s, rx, TOP + 0.05, rw, '도구별 제어 핵심')
    y += bullets(s, rx, y, rw, ['드라이버: 축 정렬·누름 힘·회전 토크', '스패너: 면접촉 유지·재파지', '플라이어: 손잡이 개폐력', '팬·냄비: 수평 유지와 쏟아짐 방지',
                               '해머: 충격 전달 구조의 피로·도구 이탈', '나이프: 절삭 저항·날 위치·작업물 고정'], size=11, gap=2, label='A2 ctrl') + 0.25
    y = block_title(s, rx, y, rw, '설계 원칙')
    bullets(s, rx, y, rw, ['공통 제어기·통신·손목 장착 구조 유지\n제조용·주방용 접촉부 분리', '하나의 재질·손가락 사양으로 모든 용도를\n충족한다는 가정은 두지 않음',
                           '탈착식 슬리브·거치대 사용 시\n보조장치 없는 시험 결과와 구분 제시'], size=11, gap=3, label='A2 rule')
    afoot(s, 'A2', note='칼·해머는 차폐·접근 제한·독립 인터록 충족 후 제한 작업으로만 활성화')


# ---------------------------------------------------------------- A3 hand engineering detail
def a03(prs):
    s = new_slide(prs, 'A3')
    aheader(s, 'A3', '핸드 설계 상세: 구동·하중·접촉부', '구동 방식은 미확정, 3개월 이내 비교 시험으로 선정 · 특허 가능성은 선행기술 조사 후 판단')
    lw = 7.3
    text(s, MX, TOP + 0.02, lw, 0.3, '구동 방식 비교 시험 (0~3개월)', size=13, bold=True)
    rows = [[B_('전동 텐던'), '기준 후보', '공통 평가 항목으로 측정'],
            [B_('소형 유압'), '비교 후보', '채택 시 호스 굽힘 수명, 누설 감지·격리 추가 검증'],
            [B_('공압'), '비교 후보', '공통 평가 항목으로 측정']]
    h1 = table(s, MX, TOP + 0.4, lw, ['후보', '위치', '검증 내용'], rows, col_w=[1.6, 1.3, 4.4], size=11.5, pad=0.08, label='A3 drive')
    text(s, MX, TOP + 0.5 + h1, lw, 0.3, '공통 평가 항목: 손 무게, 유지력, 응답, 누설, 소음, 소비전력, 정비비', size=11, color=T['text2'], label='A3 crit')
    y = block_title(s, MX, TOP + 1.0 + h1, lw, '접촉부: 용도별 분리')
    rows2 = [[B_('주방용'), '세척성·오염 관리·방수·내열성 우선, 식품용 별도 재질 선정'],
             [B_('제조용'), '내마모·토크 유지·정비성 우선'],
             [B_('공통'), '교체형 패드·외피, 미끄럼·마모·세척·재질 적합성 시험']]
    table(s, MX, y - 0.1, lw, None, rows2, col_w=[1.3, lw - 1.3], size=11.5, pad=0.07, label='A3 contact')
    rx = MX + lw + 0.45; rw = W - MX - rx
    y = block_title(s, rx, TOP + 0.02, rw, '하중 설계 (계산 예)')
    y += bullets(s, rx, y, rw, ['3kg 냄비, 무게중심이 파지점에서 0.20m\n3 × 9.81 × 0.20 ≈ 5.9N·m (정적 모멘트)', '가속·충격을 더하면 요구치 증가\n큰 냄비는 양손 지지 또는 거치대 보조',
                               '손의 파지 하중 ≠ 로봇 팔 가반하중\n팔에는 손·어댑터·센서·도구·내용물 합산'], size=11, gap=3, label='A3 load') + 0.25
    y = block_title(s, rx, y, rw, '감각부·로봇 장착')
    bullets(s, rx, y, rw, ['손끝·손바닥 접촉센서, 관절·장력 센서\n손목 6축 힘·토크 센서', '젖음·열·오염 조건의 편차와 재교정 시험',
                           '플랜지 어댑터·공구중심점 교정·통신 드라이버\n대표 로봇 2개 플랫폼에서 통합 검증'], size=11, gap=3, label='A3 sense')
    afoot(s, 'A3', note='4지는 안정적 감싸쥐기와 비용, 5지는 재파지·정밀 조작 확장을 우선 · 엄지 대향·손가락 굽힘·제한적 벌림 동작 설계')


# ---------------------------------------------------------------- A4 vision / data detail
def a04(prs):
    s = new_slide(prs, 'A4')
    aheader(s, 'A4', '비전 AI·데이터 상세', '센서별 역할을 나누고 실패 유형까지 기록 · 수치는 목표이며 현재 보유 데이터 없음')
    lw = 7.3
    rows = [[B_('상부 RGB-D·손목 카메라'), '형상·도구 부위·배치 상태', '증기·금속 반사·기울어진 표면 오차 시험, 다른 시점 재관측'],
            [B_('촉각 (손끝·손바닥)'), '접촉·미끄러짐', '젖음·열·오염 조건 편차와 재교정'],
            [B_('손목 6축 힘·토크'), '반력·토크', '도구 토크·누름 힘 확인'],
            [B_('초음파'), '근거리 장애물·액면 (보조)', '정밀 자세·조리 온도 판단에는 사용하지 않음'],
            [B_('인덕션 출력 + 온도센서'), '가열 상태', '온도·시간·액량 감시']]
    table(s, MX, TOP + 0.05, lw, ['센서', '확인 대상', '한계·보완'], rows, col_w=[2.15, 2.0, 3.15], size=11, pad=0.08, max_h=3.4, label='A4 sensors')
    by = 5.0
    y = block_title(s, MX, by, lw, '성능 보고 방식')
    bullets(s, MX, y, lw, ['최초 시도 성공·재시도 포함 성공·작업 중단을 분리하고 시험 횟수·성공 건수·신뢰구간을 함께 보고',
                           '동적 파지는 추적 중지와 놓침도 실패로 집계, 미관측 물체 일반화는 별도 보고'], size=11, gap=3, label='A4 report')
    rx = MX + lw + 0.45; rw = W - MX - rx
    y = block_title(s, rx, TOP + 0.05, rw, '데이터 기록 항목 (시간 동기화)')
    y += bullets(s, rx, y, rw, ['객체 ID, 도구 기능부, 파지 방식, 관절·장력, 접촉력, 물체 속도, 조명·오염 조건, 결과와 실패 원인',
                               '초기 목표: 도구·용기 30종 이상, 시도 1만 회 이상 (수집량보다 실패 유형의 다양성)'], size=11, gap=3, label='A4 log') + 0.25
    y = block_title(s, rx, y, rw, '학습·검증 방식')
    y += bullets(s, rx, y, rw, ['사람 시연·원격조작으로 초기 정책, 현장 데이터 추가', '프레임 단위 무작위 분할 대신 물체 모델·작업 세션·현장 단위로 분리',
                               'VLA·모방학습은 고수준 작업 선택·동작 생성 후보, 힘·속도·안전 한계는 독립 제어 계층'], size=11, gap=3, label='A4 learn') + 0.25
    y = block_title(s, rx, y, rw, '데이터 권리')
    bullets(s, rx, y, rw, ['고객 현장 데이터의 수집·보관·학습·재사용 범위는 계약에서 분리 합의', '오픈소스 모델·라이브러리 상업 이용 조건은 출시 전 확인'],
            size=11, gap=3, label='A4 rights')
    afoot(s, 'A4')


# ---------------------------------------------------------------- A5 manufacturing scenes
def a05(prs):
    s = new_slide(prs, 'A5')
    aheader(s, 'A5', '적용 장면: 제조 반복 취급 (콘셉트 렌더링)', '초기 고객(로봇 SI·제조기업) 공정 예시 · 실제 적용 공정은 첫 90일 인터뷰로 확정 · 실제 시험 장면 아님')
    steps = [('s1_door', '문 열기'), ('s2_pick', '소재 집기'), ('s3_load', '기계에 넣기'), ('s4_press', '버튼 누르기'),
             ('s5_unload', '완성품 꺼내기'), ('s6_close', '문 닫기')]
    lw = 6.6; gap = 0.16; pw = (lw - 2 * gap) / 3; ph_ = 1.45
    for i, (f, a) in enumerate(steps):
        r, c = divmod(i, 3)
        x = MX + c * (pw + gap); y = TOP + 0.05 + r * (ph_ + 0.5)
        image(s, RAW(f + '_color.png'), x, y, pw, ph_, focus=(0.5, 0.5))
        text(s, x, y + ph_ + 0.08, pw, 0.28, [[(f'{i + 1}  ', {'color': T['accent']}), (a, {})]], size=12, bold=True, label='mt ' + a)
    text(s, MX, TOP + 2 * (ph_ + 0.5) + 0.05, lw, 0.26, '공작기계 소재 투입·배출 6단계 예시 (SoftHand-4 콘셉트 모델)', size=10, color=T['muted'])
    rx = MX + lw + 0.5; rw = W - MX - rx
    y = block_title(s, rx, TOP + 0.05, rw, '사업상 위치')
    y += bullets(s, rx, y, rw, ['반복 취급 공정을 가진 제조기업과 로봇 SI가\n초기 고객 (1~2년차)', '같은 핸드로 문·버튼·소재를 다루면\n작업별 그리퍼·지그 교체를 줄일 수 있는지 검증',
                               '0~3개월에 초기 적용 작업 3개 확정\n7~12개월 제조 실증'], size=11.5, gap=3, label='A5 a') + 0.25
    y = block_title(s, rx, y, rw, '검증 지표 (목표)')
    bullets(s, rx, y, rw, ['정적 파지 30종 98%, 정렬 오차 ±3mm (24개월)', '사이클타임·전환시간·성공률·총비용을\n전용 그리퍼와 동일 조건에서 비교',
                           '선정 고객의 총 사람 개입시간 30% 이상 감소'], size=11.5, gap=3, label='A5 b')
    afoot(s, 'A5', note='렌더링은 동일 SoftHand-4 콘셉트 모델 · 시제품 확보 시 실제 시험 영상으로 교체')


# ---------------------------------------------------------------- A6 kitchen scenes
def a06(prs):
    s = new_slide(prs, 'A6')
    aheader(s, 'A6', '적용 장면: 주방 작업 (콘셉트 렌더링)', '로봇 주방(3년차~) 작업 예시 · 레시피 확장 순서에 따라 단계별 검증 · 실제 시험 장면 아님')
    steps = [('lx_pick', '재료 집기', '1단계'), ('lx_lid', '용기 열기', '1단계'), ('lx_plate', '그릇에 담기', '1단계'), ('ck_wide', '양팔·LM 이동축 구성', '구성'),
             ('lx_drop', '팬에 투입', '2단계'), ('lx_tongs', '집게 사용', '2단계'), ('lx_stir', '저속 젓기', '2단계'), ('lx_knob', '인덕션 조절', '2단계')]
    gap = 0.2; pw = (CW - 3 * gap) / 4; ph_ = 1.62
    for i, (f, a, st) in enumerate(steps):
        r, c = divmod(i, 4)
        x = MX + c * (pw + gap); y = TOP + 0.05 + r * (ph_ + 0.55)
        image(s, KIT(f + '.jpg'), x, y, pw, ph_, focus=(0.5, 0.5) if f != 'ck_wide' else (0.55, 0.42), zoom=1.0 if f != 'ck_wide' else 1.25)
        text(s, x, y + ph_ + 0.08, pw, 0.3, [[(st + '  ', {'color': T['accent']}), (a, {})]], size=12, bold=True, label='scene ' + a)
    afoot(s, 'A6', note='단계: 레시피 확장 순서(1 비가열 취급, 2 저속 젓기 볶음·찜) · 팬 던지기·고속 칼질은 초기 범위에서 제외')


# ---------------------------------------------------------------- A7 ceiling kitchen installation & operation
def a07(prs):
    s = new_slide(prs, 'A7')
    aheader(s, 'A7', '로봇 주방 설치·운영 상세', '실제 구조는 가반하중·작업영역·건축 구조 검토 후 확정 · 주방 셀 판매는 3년차부터 (계획)')
    iw = 4.8; ih = 2.75
    image(s, KIT('ck_wide.jpg'), MX, TOP + 0.05, iw, ih, focus=(0.56, 0.42), zoom=1.2)
    text(s, MX, TOP + ih + 0.12, iw, 0.26, '천장 이동형 양팔 로봇 주방 콘셉트 (렌더링, 단일 공통 캐리지안)', size=10, color=T['muted'])
    y = block_title(s, MX, TOP + ih + 0.55, iw, '캐리지 구성 비교')
    table(s, MX, y - 0.1, iw, None, [[ACC('단일 공통 캐리지'), '우선 비교, 이동·충돌 제어 단순화'],
                                     [B_('독립 캐리지'), '후속 검토, 작업 범위는 넓지만\n팔·축 간 충돌과 케이블 간섭 증가']],
          col_w=[1.6, iw - 1.6], size=11, pad=0.06, label='A7 carriage')
    rx = MX + iw + 0.45; rw = W - MX - rx
    y = block_title(s, rx, TOP + 0.05, rw, '구조·설치 조건')
    y += bullets(s, rx, y, rw, ['LM 가이드는 안내 요소, 구동기·엔코더·브레이크·종단 스토퍼·케이블 관리장치 별도 필요',
                               '검토된 구조체 또는 독립 프레임에 고정 (천장 마감재에 직접 고정하지 않음), 역설치 허용 로봇 모델 선택',
                               '동하중·처짐·진동·낙하 방지·정전 시 보유 상태 검증', '상부 레일 윤활제·마모분이 조리구역에 떨어지지 않도록 커버·격리 구조'],
                size=11, gap=3, label='A7 install') + 0.22
    y = block_title(s, rx, y, rw, '운영 범위와 사람에게 남는 작업')
    y += bullets(s, rx, y, rw, ['레시피는 재료·중량·투입 순서·온도 범위·시간·완료 조건·예외 처리가 검증된 작업 절차로 관리',
                               '식재료 전처리, 카트리지 보충, 일일 세척 점검은 사람 작업으로 도입 제안서에 명시'], size=11, gap=3, label='A7 ops') + 0.22
    y = block_title(s, rx, y, rw, '견적 범위')
    bullets(s, rx, y, rw, ['셀 원가: 팔 2대·핸드 2개·레일/프레임·제어/안전·설치/시운전·기본 보증', '건축 보강·싱크대 전체 교체·급배수/전기 증설은 별도 견적'],
            size=11, gap=3, label='A7 quote')
    afoot(s, 'A7', note='경제성 검증: 재료 보충·전후 세척·복구를 포함한 사람 개입시간, 에너지·물 사용량 기록')


# ---------------------------------------------------------------- A8 competition detail
def a08(prs):
    s = new_slide(prs, 'A8')
    aheader(s, 'A8', '경쟁 상세: 핸드 · 그리퍼 · 로봇 주방 · 조리 자동화', '공개 정보 기반 정성 비교, 독립 비교시험 아님 · 회사명은 범주 예시이며 우열을 주장하지 않음')
    rows = [
        [B_('소프트·다지 핸드'), 'qbrobotics qb SoftHand Industry: 5지, 19자유도·1모터, 파워그립 2kg,\n핀치 0.6kg, IP65, 0.99kg (제조사 공개)\n'
                               'Shadow·Allegro·Tesollo 등 다지 핸드, Tesla·Figure 등은 손 자체 개발', '형상 적응\n고자유도', '도구 토크 유지, 부분 독립 조작,\n세척 교체부, 작업 완료율로 비교'],
        [B_('산업용 그리퍼·EOAT'), '평행·진공·적응형 그리퍼, 툴 체인저', '저가·고신뢰, 지정 공정 최적화', '범용성 이득이 비용·속도 손실보다 큰 다품종 작업에 집중'],
        [B_('로봇 주방 시스템'), 'Moley Robotics A-AiR: 이동 플랫폼 양손 로봇, 3자유도 갠트리, 비전,\n수전·오븐·블렌더 등 주방기기 연동 (공급사 소개, 2020 발표)',
         '통합 주방 제품', '천장 양팔 주방 자체의 신규성 주장 배제\n부품 플랫폼·국내 주방 통합·서비스성 검증'],
        [B_('조리 자동화 연구'), 'YORI (Noh 외, arXiv:2405.11094)\n모듈형 로봇 주방과 양팔 매니퓰레이터를 활용한 자율 조리', '연구 시연', '장시간 운영·정비·유료 고객\n경제성 입증'],
        [B_('전용 조리 장비'), '급식 사업장 공정별 조리로봇(삼성웰스토리), 패티 조리 로봇(에니아이),\n튀김 스테이션(Miso Robotics)', '지정 메뉴\n고처리량', '로봇 주방은 정해진 재료·도구·\n메뉴의 반복 업무에 집중'],
    ]
    table(s, MX, TOP - 0.05, CW, ['범주', '대표 사례 (공개 정보)', '특성', '본 사업의 대응'], rows, col_w=[1.85, 5.6, 1.5, 2.883], size=11, pad=0.08,
          max_h=4.9, label='A8 table')
    afoot(s, 'A8', note='출처: 부록 A15 · Moley 사진·로고는 사용하지 않음 (본 자료 이미지는 자체 콘셉트 렌더링)')


# ---------------------------------------------------------------- A9 market evidence
def a09(prs):
    s = new_slide(prs, 'A9')
    aheader(s, 'A9', '시장 근거 상세', '설치 기반과 수요 배경을 보여주는 공개 지표 · 당사 시장 규모와 매출로 전환하지 않음')
    rows = [
        [B_('로봇 설치 기반 (세계)'), '산업용 로봇 신규 설치 2024년 약 54.2만 대 → 2025년 60만 대 이상 (+11%)\n가동 대수 약 500만 대 (2025, +9%), 중국이 신규 설치의 59%', 'IFR World Robotics 2025·2026'],
        [B_('로봇 설치 기반 (국내)'), '2025년 신규 설치 약 3.0만 대 (−1%), 세계 4위 시장\n로봇 밀도 근로자 1만 명당 1,220대 (세계 1위, 2019년 이후 연평균 7% 증가)', 'IFR World Robotics 2026'],
        [B_('로봇 도입 비용 구조'), '기존 로봇 도입 총소유비용의 약 75%가 초기 셋업·재설계\n(작업 흐름 구성, 신제품 적응, 기존 공정 통합)', 'BCG (2026.4)'],
        [B_('주방 인력 (응용 제품 배경)'), '숙박·음식점업 사업체 861,863개, 종사자 2,293,381명 (2023)\n조리·식당 서비스 인력 부족률 코로나19 이전 대비 약 2배, 외식업체 952곳 중 27.6% 인력난 (2023)',
         '통계청 전국사업체조사 · 헤럴드경제 (2025.5)'],
        [B_('국내 조리로봇 도입 사례'), '부산교육청 학교 급식실 조리로봇 실증: 솥 앞 작업시간 평균 69% 감소 (2025)\n삼성웰스토리 급식 사업장 공정별 조리로봇 운영 (2023~)', '서울신문 (2025.12) · 인사이트코리아'],
        [B_('해외 외식 운영자'), '미국 외식 운영자 49%: 인력 대응 기술·자동화가 자기 업종에서 더 보편화될 것', 'NRA (Restaurant Dive, 2025)'],
        [B_('시장 규모 산정 원칙'), '검증되지 않은 시장 총액은 인용하지 않고 고객 후보 × 판매 단가의 상향식으로 산정 (본문 10장)', '사업계획서'],
    ]
    table(s, MX, TOP - 0.05, CW, ['구분', '내용', '출처'], rows, col_w=[2.3, 6.7, 2.833], size=11, pad=0.065, max_h=4.95, label='A9 table')
    afoot(s, 'A9', note='국내 주방 로봇 시장 규모는 공식 통계 부재로 미제시 · 국내 수요는 첫 90일 고객 인터뷰로 검증 예정')


# ---------------------------------------------------------------- A10 technology trends
def a10(prs):
    s = new_slide(prs, 'A10')
    aheader(s, 'A10', '로봇 기술 동향: 판단·시각·로봇 팔은 상용화, 손과 도구 조작은 과제', '각 수치는 출처 발표 기준이며 독립 검증 아님')
    rows = [
        [B_('판단 · AI 모델'), '빠르게 발전', 'Gemini Robotics 1.5 (2025.9) · NVIDIA Isaac GR00T N1.6 (2026.1) · Physical Intelligence 기업가치 56억 달러 (2025.11)'],
        [B_('시각 · 연산'), '상용 수준', 'NVIDIA Jetson AGX Thor: 2,070 FP4 TFLOPS, 이전 세대 대비 AI 연산 7.5배 (2025.8)'],
        [B_('로봇 팔·휴머노이드'), '대규모 보급', '산업용 로봇 가동 약 500만 대, 연 60만 대 이상 설치 (IFR, 2026.9) · Figure 기업가치 390억 달러 (2025.9)'],
        [ACC('손 · 도구 조작'), ACC('남은 과제'),
         '"The forearm and hand are more difficult than the entire rest of the robot." Elon Musk, Tesla 2025년 3분기 실적 발표 (2025.10)\n'
         'NVIDIA 레퍼런스 휴머노이드(2026.6) 외부 촉각 핸드 채택 · Figure 03 촉각 손끝 (3g 감지, 2025.10)'],
        [B_('자본 유입'), '—', '로보틱스 스타트업 투자 2025년 150억 달러 (사상 최대), 2026년 상반기 188억 달러 (Crunchbase News, 2026.6)'],
    ]
    table(s, MX, TOP + 0.05, CW, ['구분', '상태', '근거 (출처·시점)'], rows, col_w=[2.6, 1.45, 7.783], size=12, pad=0.09, max_h=3.9, label='A10 table')
    footnote(s, '해석: AI 모델·시각·로봇 팔이 상용화되면서 사람용 도구를 잡고 사용하는 손과 조작 소프트웨어가 남은 과제, 협동로봇·산업용 로봇·휴머노이드 모두 적용 대상')
    afoot(s, 'A10', note='출처: 부록 A15')


# ---------------------------------------------------------------- A11 pricing & sales terms
def a11(prs):
    s = new_slide(prs, 'A11')
    G = M['gm_unit']; R = M['roi']
    aheader(s, 'A11', '가격·원가·판매 조건 가정', '모두 부가세 제외 계획값 · 사업계획서 수치를 그대로 사용 · 가격 수용성은 유료 실증에서 검증')
    rows = [
        [B_('4지 중심 핸드 패키지 (평균)'), '1,500만 원', '800만 원', f'{G["hand"] * 100:.1f}%', '부품·조립·검사·초기 보증 충당'],
        [B_('주방 셀 1식'), '2억 원', '1억4,000만 원', f'{G["cell"] * 100:.1f}%', '팔 2대·핸드 2개·레일/프레임·제어/안전·설치/시운전·기본 보증'],
        [B_('소프트웨어 연간 계약'), '300만 원/계약', '90만 원/계약', f'{G["sw"] * 100:.1f}%', '원격 진단·기능 업데이트·기술지원, 필수 안전 기능은 구독과 무관'],
        [B_('유료 실증·개발'), '연 1.0~2.0억 원', '—', '40.0%', '실증 계약과 양산 발주 구분'],
    ]
    h = table(s, MX, TOP + 0.05, CW, ['제품', '판매가', '직접원가', '총이익률', '원가·계약 포함 범위'], rows, col_w=[2.75, 1.5, 1.5, 1.1, CW - 6.85],
              size=11.5, pad=0.085, align=['l', 'r', 'r', 'r', 'l'], label='A11 table')
    by = TOP + 0.4 + h
    hw = (CW - 0.5) / 2
    y = block_title(s, MX, by, hw, '판매 조건')
    bullets(s, MX, y, hw, ['고객 전환: 진단 → 유료 실증 계약 → 사전 합의된 성능·경제성 검수 → 구매·반복 발주', '의향서는 수주로 집계하지 않음, 실증 선수금·검수 기준 계약',
                           '주방 셀에 들어가는 핸드는 핸드 단품 매출에서 제외', '임대·RaaS는 실제 정비비·잔존가치 확보 후 금융 파트너와 검토'],
            size=11, gap=3, label='A11 terms')
    x2 = MX + hw + 0.5
    y = block_title(s, x2, by, hw, '고객 투자회수 산식 (주방 셀 예시)')
    bullets(s, x2, y, hw, ['연 순절감액 = 시간당 총 인건비 2만5천 원 × 하루 절감 시간 × 연 300일 − 연 추가 운영비 1,000만 원',
                           f'하루 6시간: {R[0]["saving"]:,.0f}만 원/년 → 2억 원 ÷ 연 순절감액 ≈ {R[0]["payback"]:.1f}년',
                           f'하루 10시간: {R[1]["saving"]:,.0f}만 원/년 → 약 {R[1]["payback"]:.1f}년 (금융·세금·잔존가치 제외)',
                           '프리미엄 가정용은 시간 편익·편의성·주방 차별화에 대한 지불 의사를 별도 검증'], size=11, gap=3, label='A11 roi')
    afoot(s, 'A11', note='비표준 요청은 별도 견적 · 초기 회사가 장비 금융과 유지보수 위험을 동시에 떠안지 않도록 설계')


# ---------------------------------------------------------------- A12 5-year detail
def a12(prs):
    s = new_slide(prs, 'A12')
    B = M['base']; A = M['assumptions']; S = M['sens']
    aheader(s, 'A12', '5개년 재무 상세와 민감도 (기준 시나리오)', '단위: 억 원 · 1년차 = 투자 집행 시작연도 · 사업계획서 산식과 수치를 그대로 재현')
    f = eok
    rows = [
        ['핸드 단품 판매 (대)'] + [str(v) for v in A['hands']],
        ['  매출 (대수 × 0.15)'] + [f(v) for v in B['rev_hand']],
        ['  매출총이익 (대당 0.07)'] + [f(v) for v in B['gp_hand']],
        ['주방 셀 판매 (대)'] + [str(v) for v in A['cells']],
        ['  매출 (셀 × 2.0)'] + [f(v) for v in B['rev_cell']],
        ['  매출총이익 (셀당 0.6)'] + [f(v) for v in B['gp_cell']],
        ['SW 유효 계약 (건)'] + [str(v) for v in A['sw']],
        ['  매출 (계약 × 0.03)'] + [f(v) for v in B['rev_sw']],
        ['  매출총이익 (계약당 0.021)'] + [f(v) for v in B['gp_sw']],
        ['유료 실증·개발 매출 (총이익률 40%)'] + [f(v) for v in B['rev_pilot']],
        [B_('총매출')] + [(f(v), {'bold': True}) for v in B['rev']],
        ['매출총이익 (이익률)'] + [f'{f(g)} ({m * 100:.0f}%)' for g, m in zip(B['gp'], B['gm'])],
        ['운영비'] + [f(v) for v in B['opex']],
        [B_('영업손익')] + [(f(v), {'bold': True, 'color': T['accent'] if v < 0 else T['text']}) for v in B['op']],
        ['누적 영업손익'] + [f(v) for v in B['cum_op']],
    ]
    lw = 7.9
    table(s, MX, TOP - 0.1, lw, ['항목', '1년차', '2년차', '3년차', '4년차', '5년차'], rows, col_w=[2.9] + [1.0] * 5, size=10, align=['l', 'r', 'r', 'r', 'r', 'r'],
          pad=0.03, max_h=5.0, label='A12 table')
    rx = MX + lw + 0.45; rw = W - MX - rx
    y = block_title(s, rx, TOP - 0.1, rw, '민감도 (동일 마진·운영비)')
    s3, s4 = S['y3_50'], S['y4_80']
    h1 = table(s, rx, y - 0.1, rw, None, [[B_('기준'), f'5년차 매출 {f(B["rev"][4])}억\n영업이익 {f(B["op"][4])}억'],
                                         [B_('3년차 50%'), f'매출 {f(s3["rev"])}억\n영업손실 {f(-s3["op"])}억'],
                                         [B_('4년차 80%'), f'총이익 {f(s4["gp"])}억 < 운영비 {A["opex"][3]:.0f}억\n영업손실 {f(-s4["op"])}억']],
               col_w=[1.25, rw - 1.25], size=10.5, pad=0.05, label='A12 sens')
    y = block_title(s, rx, y + h1 + 0.1, rw, '산정 기준')
    bullets(s, rx, y, rw, ['SW 계약 수: 당해 매출 인식 가능한 연간 계약 환산치', '운영비: 연구개발·영업·관리·감가상각 포함 계획값',
                           '단순 모델: 재고·설비·보증금·매출채권·세금 미반영', '1~2년차 누적 영업손실 14.49억 원\n18~24개월에 후속 자금 조달'], size=10.5, gap=2, label='A12 basis')
    afoot(s, 'A12', note='4년차 영업손실 0.38억 원은 사업계획서 민감도(총이익 19.62억 < 운영비 20억)의 차액')


# ---------------------------------------------------------------- A13 use of funds detail
def a13(prs):
    s = new_slide(prs, 'A13')
    B = M['base']; A = M['assumptions']; U = M['uof']; SEED = M['seed']
    aheader(s, 'A13', 'Seed 자금 사용 상세', '24개월 계획 현금 집행 한도 · 손익계산서 운영비와 일대일로 일치하지 않음')
    link = {'개발 인력': '핵심 인력 7명 단계 채용 (14장)', '시제품·시험 설비': '4지 알파·베타, 5지 알파, 내구 시험 (10만 → 30만 회)',
            'AI 데이터·연산': '도구·용기 30종 이상, 시도 1만 회 이상', '주방 통합 실증': '주방 양팔 통합, 메뉴 1종 → 3종 실증',
            '안전·품질·지식재산': '통합 위험 평가, 선행기술 조사, 출원 후보 검토', '운영·예비비': '공급 지연·재작업 대비'}
    rows = [[B_(k), f'{v:.1f}', f'{v / SEED * 100:.1f}%', d, link.get(k, '')] for k, v, d in U]
    rows.append([B_('합계'), (f'{sum(v for _, v, _ in U):.1f}', {'bold': True}), ('100%', {'bold': True}), '24개월 계획 현금 집행 한도', ''])
    h = table(s, MX, TOP + 0.05, CW, ['항목', '금액 (억 원)', '비중', '사용 목적', '관련 일정·목표 (사업계획서)'], rows, col_w=[2.0, 1.15, 0.85, 3.9, CW - 7.9],
              size=11, pad=0.075, align=['l', 'r', 'r', 'l', 'l'], label='A13 table')
    by = TOP + 0.4 + h
    hw = (CW - 0.5) / 2
    y = block_title(s, MX, by, hw, '현금 계획 원칙')
    bullets(s, MX, y, hw, ['장비 자산화·재고·매출 회수 시점을 반영한 월별 현금계획 [입력 필요]', '보조금은 미확정이므로 기본 조달재원에서 제외',
                           '월별 채용·인건비 계획 [입력 필요]'], size=11, gap=3, label='A13 cash')
    x2 = MX + hw + 0.5
    y = block_title(s, x2, by, hw, '손익과의 연결')
    bullets(s, x2, y, hw, [f'1~2년차 운영비 {A["opex"][0] + A["opex"][1]:.0f}억 원, 매출총이익 {B["gp"][0] + B["gp"][1]:.2f}억 원',
                           f'1~2년차 누적 영업손실 {eok(-B["cum_op"][1])}억 원, 재고·설비·매출채권 반영 시 현금 소요 증가', '18~24개월에 후속 자금 조달 필요'],
            size=11, gap=3, label='A13 link')
    afoot(s, 'A13', note='금액은 사업계획서 제안안 · 투자 실사 전 월별 현금계획으로 재작성')


# ---------------------------------------------------------------- A14 safety / hygiene / IP
def a14(prs):
    s = new_slide(prs, 'A14')
    aheader(s, 'A14', '안전·위생·인증·지식재산', '제품 검증 전에는 인증 취득·규제 적합·독자성을 주장하지 않음 · 표준은 적용 검토 대상')
    cw3 = (CW - 0.7) / 3
    cols = [('안전', ['협동로봇에 소프트 핸드를 달아도 전체 시스템이 자동으로 안전해지지 않음', '고온 조리도구·칼·중량물·이동축을 포함한 통합 위험 평가',
                     'ISO 10218-2:2025: 산업용 로봇 응용·로봇 셀 안전 요구사항', '가정용 주방에 같은 기준을 그대로 적용한다고 단정하지 않음, 판매국별 요구사항은 시험기관과 결정',
                     '천장·역설치: 브레이크·낙하 방지, 정전 시 보유 상태, 작업별 안전 정지 상태']),
            ('위생', ['IP 등급은 침수·고압 세척·내열·식품 위생 적합성을 모두 의미하지 않음', '주방용 접촉부: 식품접촉 적합성, 세척 후 잔류물·미생물 검증, 세척제 내성',
                     '오염/청결 동선 분리, 배수·비산수 관리, 세척기 연동', '상부 레일 윤활제·마모분 낙하 방지 커버·격리']),
            ('지식재산·영업비밀 (계획)', ['출원 후보: 엄지 대향·관절 순응/잠금 구조, 손끝 교체·밀봉 구조', '출원 후보: 미끄러짐과 반력에 따른 파지 재구성, 양팔·이동축 작업 분담 및 청결 구역 관리',
                                     '영업비밀 후보: 데이터 정제, 장력 보정,\n실패 복구 파라미터', '선행기술 조사와 권리범위 검토 전에는\n독자성·비침해·세계 최초를 주장하지 않음'])]
    for i, (t, items) in enumerate(cols):
        x = MX + i * (cw3 + 0.35)
        y = block_title(s, x, TOP + 0.05, cw3, t)
        bullets(s, x, y, cw3, items, size=12, gap=8, label='A14 ' + t)
    afoot(s, 'A14', note='현재 확인된 특허 출원 없음 · 예산: 안전·품질·지식재산 1.0억 원 (Seed 사용 계획)')


# ---------------------------------------------------------------- A15 sources
SOURCES = [
    ('S1', 'IFR, World Robotics 2025 보도자료 (2025-09)', 'ifr.org'),
    ('S2', 'IFR, World Robotics 2026 보도자료 (2026-09-24)', 'ifr.org'),
    ('S3', 'BCG, How Physical AI Is Reshaping Robotics Today (2026-04)', 'bcg.com'),
    ('S4', 'qbrobotics, qb SoftHand Industry 제품 사양', 'qbrobotics.com'),
    ('S5', 'Moley Robotics, A AiR kitchen', 'moley.com'),
    ('S6', 'Noh 외, YORI 자율 조리 시스템, arXiv:2405.11094', 'arxiv.org'),
    ('S7', 'ISO 10218-2:2025 (로봇 응용·셀 안전)', 'iso.org'),
    ('S8', '통계청, 2023년 전국사업체조사 결과 (2024-09-27)', 'kostat.go.kr'),
    ('S9', '헤럴드경제, 외식업계 인력난 (2025-05-10)', 'biz.heraldcorp.com'),
    ('S10', '서울신문, 부산 학교 급식실 조리 로봇 (2025-12-30)', 'seoul.co.kr'),
    ('S11', '인사이트코리아, 삼성웰스토리 급식 조리로봇', 'insightkorea.co.kr'),
    ('S12', 'Restaurant Dive, NRA 2025 labor market·tech', 'restaurantdive.com'),
    ('S13', 'AI타임스, 에니아이 햄버거 조리 로봇 (2025)', 'aitimes.com'),
    ('S14', 'The Robot Report, Miso Robotics Flippy', 'therobotreport.com'),
    ('S15', 'Tesla 2025년 3분기 실적 발표 녹취 (2025-10-22)', 'fool.com'),
    ('S16', 'NVIDIA, GR00T N1.6 · 레퍼런스 휴머노이드 (2026)', 'nvidia.com'),
    ('S17', 'CNBC, NVIDIA Jetson AGX Thor (2025-08-25)', 'cnbc.com'),
    ('S18', 'Google DeepMind, Gemini Robotics 1.5 (2025-09)', 'deepmind.google'),
    ('S19', 'Figure, Series C · Figure 03 (2025)', 'figure.ai'),
    ('S20', 'Bloomberg, Physical Intelligence 가치 평가 (2025-11)', 'bloomberg.com'),
    ('S21', 'Crunchbase News, 로보틱스 투자 (2026-06)', 'news.crunchbase.com'),
]
def a15(prs):
    s = new_slide(prs, 'A15')
    aheader(s, 'A15', '출처', '열람 기준 2026-10-06 · 가격·원가·성능·고객 수·일정·매출은 본 계획의 가정 (출처 수치 아님) · 전체 URL은 수정 보고서')
    half = (len(SOURCES) + 1) // 2; tw = (CW - 0.35) / 2
    for c in range(2):
        rows = [[(sid, {'bold': True, 'color': T['accent']}), t, (u, {'color': T['text2'], 'size': 9})] for sid, t, u in SOURCES[c * half:(c + 1) * half]]
        table(s, MX + c * (tw + 0.35), TOP + 0.02, tw, ['번호', '출처', '도메인'], rows, col_w=[0.55, tw - 0.55 - 1.65, 1.65], size=10, pad=0.045,
              max_h=4.85, label=f'A15 table {c}')
    afoot(s, 'A15', note='S1·S4~S7은 사업계획서 인용 출처 [1]~[5]와 같음 · 시장조사기관의 시장 총액 전망은 사용하지 않음')


APPX = [a00, a01, a02, a03, a04, a05, a06, a07, a08, a09, a10, a11, a12, a13, a14, a15]
