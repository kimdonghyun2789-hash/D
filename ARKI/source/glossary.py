# Plain-Korean glossary applied to appendix (legacy) slide text: consulting English -> words used in Korean IR / 사업계획서.
# Longest phrases first; word boundaries so product names (Care Basic, BOM, Rail ...) and codes stay intact.
import re

GLOSS = [
    ('What Must Be True', '투자 전제'), ('Kill Criteria', '중단 기준'), ('Kill · 대응', '중단 기준 · 대응'), ('Kill', '중단'),
    ('Validation Channel', '검증 시장'), ('Scale Channel', '확장 시장'), ('VALIDATION', '검증'), ('SCALE', '확장'),
    ('Land & Expand', '설치 후 추가 판매'), ('Integration Layer', '공간 · 로봇 통합 영역'),
    ('Installed Base Flywheel', '설치 기반 선순환'), ('Installed Base', '설치 기반'), ('Operational\nFlywheel', '운영\n선순환'), ('Flywheel', '선순환'),
    ('Moat', '진입장벽'), ('Evidence Pack', '증빙 자료'), ('CURRENT EVIDENCE', '현재 보유 근거'), ('SEED TARGET', 'Seed 목표'),
    ('Investment Proof', '투자 근거'), ('Investment Scorecard', '투자 평가표'), ('Investment Milestone', '투자 마일스톤'),
    ('Red-Team Q&A', '예상 질문과 답'), ('VC Red-Team Q&A', '예상 질문과 답'), ('Red-Team', '반론 검토'),
    ('Productization', '제품화'), ('Standardization', '표준화'), ('Site Adjustment', '현장 조정'),
    ('Standard Module', '표준 모듈'), ('Kitchen Layout Template Library', '주방 표준안 라이브러리'), ('Template Library', '표준안 라이브러리'),
    ('Kitchen Layout Family', '주방 유형'), ('Layout Family', '주방 유형'), ('Kitchen Layout', '주방 배치'), ('Kitchen Geometry', '주방 형태'),
    ('Robot Installation Architecture', '로봇 설치 방식'), ('Robot Architecture', '로봇 설치 방식'), ('Installation Architecture', '설치 방식'),
    ('Installation Standard', '설치 표준'), ('Installation Data', '설치 데이터'),
    ('Robot Working Zone', '로봇 작업 영역'), ('Human Working Zone', '사람 작업 영역'), ('Human Zone', '사람 작업 영역'), ('Robot Zone', '로봇 작업 영역'),
    ('No-go', '진입 금지'), ('Robot Reach', '로봇 도달 범위'), ('Robot Home', '로봇 보관함'),
    ('Paid Pilot', '유료 실증'), ('Home Pilot', '가정 실증'), ('Partner Pilot', '파트너 실증'), ('Real-home Pilot', '실제 가정 실증'),
    ('Customer Validation', '고객 검증'), ('Consumer Research', '소비자 조사'), ('Consumer Interview', '소비자 인터뷰'),
    ('Household Economics', '세대당 경제성'), ('Unit Economics', '단위 경제성'), ('Lifetime Contribution', '5년 기여이익'),
    ('Recurring Revenue', '반복 매출'), ('Revenue Timeline', '매출 시점'), ('Revenue Mix', '매출 구성'),
    ('Value Anchor', '가치 기준가'), ('Cost Floor', '원가 기준 하한'), ('Market Reference', '시장 참고가'),
    ('Partner Distribution', '파트너 유통'), ('Go-to-Market', '사업화 전략'), ('Beachhead', '첫 시장'),
    ('Use of Funds', '자금 사용 계획'), ('Seed Ask', '투자 요청'), ('Risk Register', '리스크 관리표'),
    ('Approved Task', '승인된 작업'), ('Task Success Rate', '작업 성공률'), ('Mock-up', '목업'),
    ('Robot-ready Kitchen', 'Robot-ready 주방'), ('Concept Layout', '콘셉트 배치'), ('Concept Model', '콘셉트 모델'),
]
# escape + word-ish boundaries (ASCII letters only; Hangul next to a term is fine)
_PAT = [(re.compile(r'(?<![A-Za-z])' + re.escape(a) + r'(?![A-Za-z])'), b) for a, b in GLOSS]

_PAIR = {'이': '가', '가': '이', '은': '는', '는': '은', '을': '를', '를': '을', '과': '와', '와': '과'}

def _jong(ch):
    o = ord(ch) - 0xAC00
    return None if not (0 <= o < 11172) else o % 28      # 0 = no final consonant, 8 = ㄹ

def _fix_particle(word, rest):
    """Adjust the particle right after a replaced Korean word (이/가, 은/는, 을/를, 과/와, 으로/로)."""
    if not rest or not word: return rest
    j = _jong(word[-1])
    if j is None: return rest
    end = len(rest) == 1 or not ('가' <= rest[1] <= '힣')
    if rest.startswith('으로') and (j == 0 or j == 8): return '로' + rest[2:]
    if rest.startswith('로') and not rest.startswith('로봇') and j not in (0, 8): return '으로' + rest[1:]
    c = rest[0]
    if c in _PAIR and end:
        want_cons = j != 0
        if (c in '이은을과') != want_cons: return _PAIR[c] + rest[1:]
    return rest

def plain(t):
    for p, b in _PAT:
        out = []; last = 0
        for m in p.finditer(t):
            out.append(t[last:m.start()]); out.append(b); last = m.end()
            rest = _fix_particle(b, t[last:last + 3])
            out.append(rest); last += 3 if len(t) >= last + 3 else len(t) - last
        out.append(t[last:]); t = ''.join(out)
    return t
