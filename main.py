
import streamlit as st
import math

st.set_page_config(
    page_title="MBTI 포켓몬 도감",
    page_icon="⚡",
    layout="wide"
)

# ──────────────────────────────────────────────
# CSS
# ──────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;700;900&family=Press+Start+2P&display=swap');

html, body, [class*="css"] {
    font-family: 'Noto Sans KR', sans-serif;
    background-color: #0d0d1a;
    color: #e0e0e0;
}

/* 헤더 */
.hero {
    text-align: center;
    padding: 2.5rem 1rem 1rem 1rem;
    background: radial-gradient(ellipse at 50% 0%, rgba(245,166,35,0.15) 0%, transparent 70%);
    border-bottom: 1px solid rgba(255,255,255,0.06);
    margin-bottom: 2rem;
}
.hero-title {
    font-family: 'Press Start 2P', monospace;
    font-size: 1.6rem;
    color: #f8e71c;
    text-shadow: 3px 3px 0 #f5a623, 6px 6px 0 rgba(245,166,35,0.3);
    letter-spacing: 2px;
    margin-bottom: 0.8rem;
}
.hero-subtitle {
    color: #aaa;
    font-size: 0.95rem;
    font-weight: 300;
}

/* 카드 */
.card {
    background: linear-gradient(160deg, #14142b 0%, #0f2040 100%);
    border-radius: 18px;
    padding: 1.4rem 1.2rem;
    margin-bottom: 1rem;
    border: 1px solid rgba(255,255,255,0.07);
    text-align: center;
    position: relative;
    overflow: hidden;
    transition: box-shadow 0.25s, transform 0.25s;
}
.card::before {
    content: '';
    position: absolute;
    top: -40%;
    left: -40%;
    width: 180%;
    height: 180%;
    background: radial-gradient(ellipse at 50% 50%, rgba(245,166,35,0.06) 0%, transparent 65%);
    pointer-events: none;
}
.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 32px rgba(245,166,35,0.18);
    border-color: rgba(245,166,35,0.4);
}

/* MBTI 배지 */
.mbti-badge {
    display: inline-block;
    background: linear-gradient(135deg, #f5a623, #f8e71c);
    color: #1a1a2e;
    font-weight: 900;
    font-size: 1.1rem;
    border-radius: 8px;
    padding: 0.25rem 0.9rem;
    margin-bottom: 0.6rem;
    letter-spacing: 3px;
}

/* 포켓몬 이름 */
.pokemon-name-kr {
    color: #ffffff;
    font-size: 1.15rem;
    font-weight: 700;
    margin: 0.3rem 0 0.1rem 0;
}
.pokemon-name-en {
    color: #7788aa;
    font-size: 0.78rem;
    margin-bottom: 0.5rem;
}
.pokemon-number {
    color: #556;
    font-size: 0.72rem;
    margin-bottom: 0.3rem;
}

/* 타입 태그 */
.type-tag {
    display: inline-block;
    border-radius: 20px;
    padding: 0.18rem 0.65rem;
    font-size: 0.72rem;
    font-weight: 700;
    margin: 0.15rem;
    color: white;
    letter-spacing: 0.5px;
}

/* 성격 유형 이름 */
.trait-label {
    color: #f5a623;
    font-size: 0.78rem;
    font-weight: 700;
    margin: 0.5rem 0 0.3rem 0;
    text-transform: uppercase;
    letter-spacing: 1.5px;
}

/* 설명 */
.card-desc {
    color: #bbc;
    font-size: 0.8rem;
    line-height: 1.6;
    margin-top: 0.4rem;
}

/* 포켓몬 이미지 */
.pokemon-img {
    width: 110px;
    height: 110px;
    object-fit: contain;
    margin: 0.5rem auto;
    display: block;
    filter: drop-shadow(0 6px 16px rgba(245,166,35,0.25));
}

/* 그룹 헤더 */
.group-header {
    display: flex;
    align-items: center;
    gap: 0.7rem;
    margin: 2rem 0 1rem 0;
}
.group-line {
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, rgba(245,166,35,0.5), transparent);
}
.group-title-text {
    color: #f5a623;
    font-weight: 900;
    font-size: 1rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    white-space: nowrap;
}

/* 상세 카드 */
.detail-wrapper {
    background: linear-gradient(160deg, #14142b, #0f2040);
    border-radius: 20px;
    border: 1px solid rgba(245,166,35,0.25);
    padding: 2rem;
    margin-top: 1.5rem;
}
.detail-section-title {
    color: #f5a623;
    font-size: 0.8rem;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 0.6rem;
    border-bottom: 1px solid rgba(245,166,35,0.2);
    padding-bottom: 0.3rem;
}
.keyword-chip {
    display: inline-block;
    background: rgba(245,166,35,0.12);
    border: 1px solid rgba(245,166,35,0.3);
    color: #f5c842;
    border-radius: 20px;
    padding: 0.2rem 0.75rem;
    font-size: 0.78rem;
    margin: 0.2rem;
}
.strength-item {
    background: rgba(100,220,100,0.08);
    border-left: 3px solid #4caf50;
    padding: 0.35rem 0.75rem;
    border-radius: 0 8px 8px 0;
    margin-bottom: 0.4rem;
    font-size: 0.82rem;
    color: #cee;
}
.weakness-item {
    background: rgba(255,80,80,0.08);
    border-left: 3px solid #f44;
    padding: 0.35rem 0.75rem;
    border-radius: 0 8px 8px 0;
    margin-bottom: 0.4rem;
    font-size: 0.82rem;
    color: #fcc;
}
.compat-good {
    display: inline-block;
    background: rgba(80,200,120,0.15);
    border: 1px solid rgba(80,200,120,0.4);
    color: #7ef7a0;
    border-radius: 8px;
    padding: 0.3rem 0.8rem;
    font-size: 0.85rem;
    font-weight: 700;
    margin: 0.2rem;
}
.compat-bad {
    display: inline-block;
    background: rgba(255,80,80,0.12);
    border: 1px solid rgba(255,80,80,0.35);
    color: #ff9090;
    border-radius: 8px;
    padding: 0.3rem 0.8rem;
    font-size: 0.85rem;
    font-weight: 700;
    margin: 0.2rem;
}
.famous-chip {
    display: inline-block;
    background: rgba(100,150,255,0.12);
    border: 1px solid rgba(100,150,255,0.3);
    color: #aac4ff;
    border-radius: 8px;
    padding: 0.3rem 0.8rem;
    font-size: 0.8rem;
    margin: 0.2rem;
}

/* 스탯 바 */
.stat-row {
    display: flex;
    align-items: center;
    gap: 0.7rem;
    margin-bottom: 0.55rem;
}
.stat-label {
    width: 80px;
    font-size: 0.75rem;
    color: #99a;
    text-align: right;
    flex-shrink: 0;
}
.stat-bar-bg {
    flex: 1;
    height: 10px;
    background: rgba(255,255,255,0.07);
    border-radius: 99px;
    overflow: hidden;
}
.stat-bar-fill {
    height: 100%;
    border-radius: 99px;
    transition: width 0.6s ease;
}
.stat-val {
    width: 35px;
    font-size: 0.78rem;
    color: #dde;
    font-weight: 700;
    flex-shrink: 0;
}

/* 필터 바 */
.filter-bar {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 14px;
    padding: 1rem 1.5rem;
    margin-bottom: 1.5rem;
}

/* 통계 뱃지 */
.stat-badge {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 10px;
    padding: 0.5rem 1.2rem;
    text-align: center;
    font-size: 1.4rem;
    font-weight: 900;
    color: #f8e71c;
}
.stat-badge-label {
    font-size: 0.72rem;
    color: #888;
    font-weight: 400;
    display: block;
}

/* 탭 스타일 보정 */
.stTabs [data-baseweb="tab"] {
    color: #aaa;
}
.stTabs [aria-selected="true"] {
    color: #f5a623 !important;
}
</style>
""", unsafe_allow_html=True)

# ──────────────────────────────────────────────
# 데이터
# ──────────────────────────────────────────────
MBTI_POKEMON = {
    "INTJ": {
        "pokemon_kr": "뮤츠",
        "pokemon_en": "Mewtwo",
        "number": 150,
        "type": ["에스퍼"],
        "type_color": ["#9B59B6"],
        "trait": "전략가",
        "group": "NT - 분석가",
        "group_emoji": "🔬",
        "short_desc": "냉철한 지성과 독립적인 사고로 모든 것을 계획하고 실행한다.",
        "long_desc": (
            "INTJ는 '마스터마인드'라고도 불리는 유형으로, 세상을 체스판처럼 바라보며 "
            "모든 상황을 전략적으로 분석합니다. 뮤츠는 과학의 힘으로 탄생한 존재로, "
            "감정보다 논리를 우선시하며 자신만의 강력한 신념 체계를 가지고 있습니다. "
            "혼자서도 충분하며, 자신의 목표를 향해 타협 없이 나아가는 모습이 INTJ의 본질과 완벽히 일치합니다. "
            "겉으로는 차갑고 접근하기 어려워 보이지만, 내면에는 세상을 바꾸고자 하는 강렬한 열망이 있습니다."
        ),
        "keywords": ["전략적", "독립적", "완벽주의", "냉철함", "비전가", "결단력"],
        "strengths": [
            "장기적인 계획 수립과 실행력이 탁월",
            "복잡한 문제를 논리적으로 분해하는 능력",
            "높은 기준과 의지로 목표를 반드시 달성",
            "독립적으로 일하며 뛰어난 결과물 도출",
        ],
        "weaknesses": [
            "타인의 감정에 둔감하게 보일 수 있음",
            "완벽주의로 인한 과도한 자기비판",
            "유연성 부족 — 자신의 계획에 지나치게 집착",
            "집단 내에서 오만하다는 인상을 줄 수 있음",
        ],
        "compatibility_good": ["ENFP", "ENTP"],
        "compatibility_bad": ["ESFP", "ISFP"],
        "famous": ["엘론 머스크", "니체", "나폴레옹", "레오나르도 다빈치"],
        "stats": {"리더십": 85, "분석력": 98, "공감능력": 35, "창의력": 80, "행동력": 75, "사교성": 30},
    },
    "INTP": {
        "pokemon_kr": "포리곤",
        "pokemon_en": "Porygon",
        "number": 137,
        "type": ["노말"],
        "type_color": ["#8899AA"],
        "trait": "논리술사",
        "group": "NT - 분석가",
        "group_emoji": "🔬",
        "short_desc": "분석적이고 호기심 많은 디지털 존재. 데이터로 세상을 이해한다.",
        "long_desc": (
            "INTP는 인류 역사상 가장 위대한 철학자, 수학자, 과학자들을 배출한 유형입니다. "
            "포리곤은 완전히 인공적으로 프로그래밍된 최초의 포켓몬으로, 논리와 알고리즘으로 "
            "존재 자체가 구성된 독특한 존재입니다. INTP처럼 포리곤은 현실 세계보다 데이터와 "
            "이론의 세계에서 더 편안함을 느낍니다. 끊임없는 지적 탐구와 '왜?'라는 질문을 "
            "멈추지 않는 것이 이 유형의 본질입니다."
        ),
        "keywords": ["논리적", "호기심", "이론가", "객관적", "내향적", "분석적"],
        "strengths": [
            "복잡한 개념을 빠르게 이해하고 새로운 이론 구축",
            "편견 없이 객관적으로 모든 가능성 검토",
            "혁신적인 아이디어와 독창적 문제 해결 방식",
            "광범위한 지식 습득과 다양한 분야 간 연결",
        ],
        "weaknesses": [
            "생각은 많지만 실행으로 연결되지 않는 경향",
            "사회적 상황에서 어색함을 느낌",
            "완벽한 이론을 추구하다 현실적 마감을 놓침",
            "감정 표현이 서툴러 차갑게 보일 수 있음",
        ],
        "compatibility_good": ["ENTJ", "ESTJ"],
        "compatibility_bad": ["ESFJ", "ISFJ"],
        "famous": ["아인슈타인", "빌 게이츠", "소크라테스", "찰스 다윈"],
        "stats": {"리더십": 45, "분석력": 99, "공감능력": 40, "창의력": 90, "행동력": 40, "사교성": 35},
    },
    "ENTJ": {
        "pokemon_kr": "리자몽",
        "pokemon_en": "Charizard",
        "number": 6,
        "type": ["불꽃", "비행"],
        "type_color": ["#E74C3C", "#5DADE2"],
        "trait": "통솔자",
        "group": "NT - 분석가",
        "group_emoji": "🔬",
        "short_desc": "강한 리더십과 도전 정신. 한계를 뛰어넘는 것이 본능이다.",
        "long_desc": (
            "ENTJ는 타고난 리더입니다. 리자몽은 포켓몬 세계에서 가장 상징적인 강자로, "
            "인정받지 못하면 명령에 따르지 않는 강인한 자존심을 가졌습니다. "
            "ENTJ처럼 리자몽은 자신보다 약한 존재의 지시는 무시하지만, "
            "진정한 실력자 앞에서는 최고의 파트너가 됩니다. "
            "어떤 장애물도 불꽃으로 태워버리는 추진력과, 하늘을 날며 전체 판세를 조망하는 "
            "전략적 시야가 이 유형의 핵심입니다."
        ),
        "keywords": ["리더십", "카리스마", "목표지향", "결단력", "도전적", "추진력"],
        "strengths": [
            "조직과 사람을 이끄는 천부적인 리더십",
            "목표를 설정하고 반드시 달성하는 강한 의지",
            "비효율을 참지 못하고 즉각 개선하는 실행력",
            "큰 그림을 보며 전략적으로 자원을 배분",
        ],
        "weaknesses": [
            "권위적이고 독단적으로 보일 수 있음",
            "타인의 감정보다 결과를 우선시",
            "속도가 너무 빨라 팀원이 따라오지 못함",
            "휴식을 모르고 번아웃에 취약",
        ],
        "compatibility_good": ["INTP", "INFP"],
        "compatibility_bad": ["ISTP", "ESTP"],
        "famous": ["스티브 잡스", "마가렛 대처", "알렉산더 대왕", "잭 웰치"],
        "stats": {"리더십": 99, "분석력": 82, "공감능력": 45, "창의력": 75, "행동력": 97, "사교성": 80},
    },
    "ENTP": {
        "pokemon_kr": "개굴닌자",
        "pokemon_en": "Greninja",
        "number": 658,
        "type": ["물", "악"],
        "type_color": ["#3498DB", "#6C3483"],
        "trait": "변론가",
        "group": "NT - 분석가",
        "group_emoji": "🔬",
        "short_desc": "창의적이고 빠른 적응력. 어떤 상황에서도 새로운 전략을 찾아낸다.",
        "long_desc": (
            "ENTP는 토론을 즐기고 아이디어가 넘치는 혁신가입니다. 개굴닌자는 물과 악 타입을 "
            "결합한 독특한 포켓몬으로, 어떤 상황에도 유연하게 대응하며 상대의 허점을 "
            "순식간에 파고드는 능력을 가졌습니다. ENTP처럼 고정된 틀에 갇히는 것을 싫어하며, "
            "자신만의 독특한 방식으로 전투를 풀어나갑니다. "
            "배틀본드 특성으로 트레이너와의 깊은 유대를 형성하는 모습은 ENTP가 신뢰하는 "
            "사람과 나누는 지적 교감을 떠올리게 합니다."
        ),
        "keywords": ["창의적", "변론가", "적응력", "독창적", "도전적", "기민함"],
        "strengths": [
            "어떤 아이디어든 즉각적으로 발전시키는 창의력",
            "토론과 논쟁에서 빠른 사고와 유연한 반론",
            "새로운 가능성과 기회를 남들보다 먼저 발견",
            "틀에 박힌 생각을 깨는 혁신적 접근",
        ],
        "weaknesses": [
            "시작은 잘하지만 마무리를 못하는 경향",
            "논쟁을 위한 논쟁으로 관계가 틀어질 수 있음",
            "규칙과 루틴을 따르는 것을 매우 힘들어함",
            "집중력이 분산되어 프로젝트가 산발적",
        ],
        "compatibility_good": ["INFJ", "INTJ"],
        "compatibility_bad": ["ISFJ", "ESFJ"],
        "famous": ["레오나르도 다빈치", "벤자민 프랭클린", "마크 트웨인", "토마스 에디슨"],
        "stats": {"리더십": 72, "분석력": 88, "공감능력": 55, "창의력": 97, "행동력": 80, "사교성": 85},
    },
    "INFJ": {
        "pokemon_kr": "루기아",
        "pokemon_en": "Lugia",
        "number": 249,
        "type": ["에스퍼", "비행"],
        "type_color": ["#9B59B6", "#5DADE2"],
        "trait": "옹호자",
        "group": "NF - 외교관",
        "group_emoji": "🌿",
        "short_desc": "세상의 평화를 수호하는 깊은 통찰력과 신비로운 존재.",
        "long_desc": (
            "INFJ는 전체 인구의 1~3%에 불과한 가장 희귀한 성격 유형입니다. "
            "루기아는 '바다의 수호신'으로, 그 날갯짓 한 번이 40일간의 폭풍을 일으킬 정도의 "
            "강력한 힘을 가졌지만 늘 바다 깊은 곳에 홀로 잠들어 있습니다. "
            "강력한 힘을 가졌음에도 평화를 위해 그 힘을 숨기는 루기아의 모습은 "
            "이상을 위해 자신을 희생하고, 타인의 내면을 꿰뚫어 보는 INFJ의 모습과 "
            "완벽하게 겹쳐집니다."
        ),
        "keywords": ["통찰력", "이상주의", "공감", "신비로움", "헌신", "희귀함"],
        "strengths": [
            "사람의 감정과 동기를 꿰뚫어 보는 통찰력",
            "강한 도덕적 신념과 공익을 위한 헌신",
            "창의적이면서도 체계적으로 비전을 실현",
            "깊고 의미있는 인간 관계 형성",
        ],
        "weaknesses": [
            "너무 높은 이상으로 현실에 실망하기 쉬움",
            "개인 경계를 설정하지 못해 감정적으로 소진",
            "비판에 매우 민감하게 반응",
            "완벽주의로 인한 과부하",
        ],
        "compatibility_good": ["ENTP", "ENFP"],
        "compatibility_bad": ["ESTP", "ESFP"],
        "famous": ["마틴 루터 킹", "넬슨 만델라", "칼 융", "간디"],
        "stats": {"리더십": 65, "분석력": 80, "공감능력": 97, "창의력": 85, "행동력": 60, "사교성": 55},
    },
    "INFP": {
        "pokemon_kr": "이브이",
        "pokemon_en": "Eevee",
        "number": 133,
        "type": ["노말"],
        "type_color": ["#A0907A"],
        "trait": "중재자",
        "group": "NF - 외교관",
        "group_emoji": "🌿",
        "short_desc": "감성적이고 다양한 가능성을 지닌 순수한 영혼. 꿈을 따라 진화한다.",
        "long_desc": (
            "INFP는 진정성과 개인적 가치관을 가장 중요시하는 몽상가입니다. "
            "이브이는 8가지 방향으로 진화할 수 있는 독특한 잠재력을 가진 포켓몬으로, "
            "어느 환경에 놓이느냐에 따라 완전히 다른 모습으로 성장합니다. "
            "INFP처럼 이브이는 아직 자신의 정체성을 탐구하는 중이며, "
            "주변의 압박보다는 자신의 내면의 소리를 따라 나아갑니다. "
            "어떤 상태에서도 순수하고 사랑스러운 본질은 변하지 않습니다."
        ),
        "keywords": ["감성적", "이상주의", "진정성", "공감", "창의적", "자유로운"],
        "strengths": [
            "깊은 공감 능력과 타인의 감정을 세심히 헤아림",
            "강한 도덕적 나침반으로 흔들리지 않는 가치관",
            "예술, 글, 음악 등 창의적 표현에서 두각",
            "열린 마음으로 다양성을 수용하고 화합",
        ],
        "weaknesses": [
            "이상과 현실의 괴리에서 오는 깊은 실망감",
            "갈등 상황을 극도로 피하려 함",
            "자기비판이 심하고 감정 기복이 있음",
            "중요한 결정을 오래 미루는 경향",
        ],
        "compatibility_good": ["ENTJ", "ENFJ"],
        "compatibility_bad": ["ESTJ", "ISTJ"],
        "famous": ["셰익스피어", "JRR 톨킨", "커트 코베인", "오드리 헵번"],
        "stats": {"리더십": 40, "분석력": 60, "공감능력": 95, "창의력": 92, "행동력": 45, "사교성": 50},
    },
    "ENFJ": {
        "pokemon_kr": "피카츄",
        "pokemon_en": "Pikachu",
        "number": 25,
        "type": ["전기"],
        "type_color": ["#F1C40F"],
        "trait": "선도자",
        "group": "NF - 외교관",
        "group_emoji": "🌿",
        "short_desc": "팀의 상징이자 따뜻한 에너지. 사람과의 유대를 가장 중요시한다.",
        "long_desc": (
            "ENFJ는 타인의 성장을 자신의 기쁨으로 여기는 천생 멘토입니다. "
            "피카츄는 포켓몬 세계의 상징으로, 단순히 강해서가 아니라 "
            "트레이너 지우와의 깊은 유대와 모든 이에게 희망을 주는 존재감 때문에 "
            "특별합니다. ENFJ처럼 피카츄는 팀의 사기를 높이고, "
            "자신이 가진 에너지를 아낌없이 나눕니다. "
            "포켓볼에 들어가는 것을 거부할 만큼 강한 자기 정체성도 가지고 있습니다."
        ),
        "keywords": ["카리스마", "공감", "영감", "리더십", "따뜻함", "헌신"],
        "strengths": [
            "타인의 잠재력을 발견하고 이끌어내는 능력",
            "팀의 화합과 동기부여에 탁월한 재능",
            "뛰어난 대화 능력과 사람의 마음을 여는 공감",
            "자신의 비전으로 다른 사람들에게 영감을 줌",
        ],
        "weaknesses": [
            "타인의 기대를 너무 의식해 자신을 잃을 수 있음",
            "모든 사람을 만족시키려다 지쳐버림",
            "비판을 개인적으로 받아들여 상처를 크게 받음",
            "경계 설정에 어려움을 겪음",
        ],
        "compatibility_good": ["INFP", "ISFP"],
        "compatibility_bad": ["INTP", "ISTP"],
        "famous": ["버락 오바마", "오프라 윈프리", "마틴 루터 킹", "마야 안젤루"],
        "stats": {"리더십": 92, "분석력": 65, "공감능력": 98, "창의력": 78, "행동력": 85, "사교성": 96},
    },
    "ENFP": {
        "pokemon_kr": "뮤",
        "pokemon_en": "Mew",
        "number": 151,
        "type": ["에스퍼"],
        "type_color": ["#FF69B4"],
        "trait": "활동가",
        "group": "NF - 외교관",
        "group_emoji": "🌿",
        "short_desc": "자유롭고 호기심이 넘치며 장난기 가득한 무한한 가능성의 존재.",
        "long_desc": (
            "ENFP는 삶을 거대한 모험으로 바라보는 자유로운 영혼입니다. "
            "뮤는 모든 포켓몬의 DNA를 가진 전설적인 존재로, "
            "어떤 기술이든 배울 수 있는 무한한 가능성을 상징합니다. "
            "ENFP처럼 뮤는 장난기 가득하고 호기심이 넘치며, "
            "낯선 것을 두려워하지 않고 오히려 즐깁니다. "
            "고정된 틀 없이 자유롭게 떠돌지만, 마음 깊은 곳에는 "
            "연결과 의미를 향한 강렬한 열망이 있습니다."
        ),
        "keywords": ["자유로운", "열정적", "창의적", "공감", "즉흥적", "낙관적"],
        "strengths": [
            "전염성 있는 에너지와 열정으로 모두를 끌어당김",
            "새로운 아이디어와 가능성에 대한 무한한 상상력",
            "다양한 사람들과 빠르고 진심어린 연결 형성",
            "어떤 상황에서도 긍정적인 면을 발견하는 능력",
        ],
        "weaknesses": [
            "집중력 부족으로 많이 시작하고 적게 마침",
            "지나친 낙관주의로 현실적 장애물을 과소평가",
            "감정 기복이 크고 기분에 따라 생산성이 달라짐",
            "혼자 있는 시간이 부족하면 쉽게 소진",
        ],
        "compatibility_good": ["INTJ", "INFJ"],
        "compatibility_bad": ["ISTJ", "ESTJ"],
        "famous": ["로빈 윌리엄스", "엘렌 디제너러스", "윌 스미스", "롤드 달"],
        "stats": {"리더십": 70, "분석력": 62, "공감능력": 94, "창의력": 96, "행동력": 80, "사교성": 97},
    },
    "ISTJ": {
        "pokemon_kr": "거북왕",
        "pokemon_en": "Blastoise",
        "number": 9,
        "type": ["물"],
        "type_color": ["#2980B9"],
        "trait": "현실주의자",
        "group": "SJ - 관리자",
        "group_emoji": "🛡️",
        "short_desc": "강한 책임감과 안정감. 든든한 수비로 소중한 것을 지킨다.",
        "long_desc": (
            "ISTJ는 성실함과 신뢰성의 대명사입니다. 거북왕은 포켓몬 세계에서 "
            "가장 믿음직스러운 파트너 중 하나로, 강력한 껍데기로 자신과 동료를 보호하고 "
            "상황이 어떻든 흔들리지 않는 안정감을 줍니다. "
            "ISTJ처럼 거북왕은 화려함보다 실용성을, 즉흥보다 체계를 선호합니다. "
            "한번 맡은 역할은 끝까지 완수하며, 그 존재만으로도 팀 전체에 "
            "든든한 심리적 안전감을 제공합니다."
        ),
        "keywords": ["성실함", "신뢰성", "체계적", "책임감", "안정적", "규칙중시"],
        "strengths": [
            "한번 맡은 일은 반드시 완수하는 강한 책임감",
            "세부 사항에 대한 뛰어난 주의력과 정확성",
            "장기적으로 일관된 신뢰를 쌓는 능력",
            "체계적인 계획과 효율적인 실행",
        ],
        "weaknesses": [
            "변화와 새로운 방식에 저항감을 느낌",
            "규칙에 지나치게 집착해 융통성이 부족",
            "감정 표현이 어색하고 내면을 잘 드러내지 않음",
            "일 외의 즐거움을 찾는 데 어려움",
        ],
        "compatibility_good": ["ESFP", "ESTP"],
        "compatibility_bad": ["ENFP", "ENTP"],
        "famous": ["워런 버핏", "제프 베조스(초기)", "앙겔라 메르켈", "조지 워싱턴"],
        "stats": {"리더십": 65, "분석력": 82, "공감능력": 55, "창의력": 45, "행동력": 78, "사교성": 50},
    },
    "ISFJ": {
        "pokemon_kr": "치코리타",
        "pokemon_en": "Chikorita",
        "number": 152,
        "type": ["풀"],
        "type_color": ["#27AE60"],
        "trait": "수호자",
        "group": "SJ - 관리자",
        "group_emoji": "🛡️",
        "short_desc": "다정하고 헌신적인 성격. 주변 사람들을 세심하게 돌본다.",
        "long_desc": (
            "ISFJ는 조용히 세상을 지탱하는 '보이지 않는 기둥' 같은 존재입니다. "
            "치코리타는 목에 달린 잎사귀에서 달콤한 향기를 내뿜어 주변을 편안하게 만들며, "
            "전투형 포켓몬이 아님에도 끝까지 트레이너 곁을 지키는 충성스러움을 가졌습니다. "
            "ISFJ처럼 치코리타는 화려한 활약보다 꾸준한 헌신으로 주변 사람들에게 "
            "따뜻한 안식처가 되어줍니다. 기억력이 좋아 소중한 사람에 대한 작은 것도 잊지 않습니다."
        ),
        "keywords": ["헌신적", "배려심", "세심함", "충성스러움", "실용적", "겸손함"],
        "strengths": [
            "타인의 필요를 미리 알아차리고 세심하게 배려",
            "뛰어난 기억력으로 중요한 사람의 세부사항 기억",
            "신뢰와 안정적인 환경을 만드는 능력",
            "책임감 있고 꼼꼼하게 일을 완수",
        ],
        "weaknesses": [
            "자신의 필요보다 타인의 필요를 항상 우선",
            "'아니오'라고 말하는 것을 극도로 어려워함",
            "변화를 싫어하고 편안한 루틴에서 벗어나기 힘들어함",
            "인정받지 못할 때 소리 없이 상처받음",
        ],
        "compatibility_good": ["ESFP", "ESTP"],
        "compatibility_bad": ["ENTP", "ENTJ"],
        "famous": ["마더 테레사", "로사 파크스", "케이트 미들턴", "비욘세"],
        "stats": {"리더십": 45, "분석력": 60, "공감능력": 96, "창의력": 55, "행동력": 65, "사교성": 70},
    },
    "ESTJ": {
        "pokemon_kr": "강철톤",
        "pokemon_en": "Aggron",
        "number": 306,
        "type": ["강철", "바위"],
        "type_color": ["#7F8C8D", "#935116"],
        "trait": "경영자",
        "group": "SJ - 관리자",
        "group_emoji": "🛡️",
        "short_desc": "규율과 강한 의지, 조직력. 맡은 영역은 반드시 지켜낸다.",
        "long_desc": (
            "ESTJ는 질서와 전통을 수호하는 사회의 기둥입니다. "
            "강철톤은 자신의 산을 자신의 영역으로 선포하고 그 어떤 침범도 허용하지 않으며, "
            "광산에서 나온 강철과 바위를 조각해 자신의 뿔을 보수하는 독특한 습성을 가졌습니다. "
            "ESTJ처럼 강철톤은 규칙, 경계, 책임을 매우 중요하게 여기며 "
            "조직의 구조를 유지하는 데서 만족감을 얻습니다. "
            "강인한 외모와 달리 자신의 영역 내 약자를 보호하는 따뜻한 면도 있습니다."
        ),
        "keywords": ["조직력", "규율", "실용적", "결단력", "책임감", "직설적"],
        "strengths": [
            "복잡한 조직과 프로세스를 효율적으로 운영",
            "명확한 목표 설정과 흔들리지 않는 실행",
            "직접적인 소통으로 혼선을 줄이는 능력",
            "규칙과 시스템을 구축하고 유지하는 능력",
        ],
        "weaknesses": [
            "융통성이 부족하고 예외 상황에 경직됨",
            "감정보다 논리를 앞세워 냉정하게 보임",
            "전통에 집착해 혁신적인 아이디어를 거부",
            "타인의 의견을 충분히 듣기 전에 판단",
        ],
        "compatibility_good": ["ISFP", "ISTP"],
        "compatibility_bad": ["INFP", "ENFP"],
        "famous": ["헨리 포드", "미셸 오바마", "힐러리 클린턴", "존 D. 록펠러"],
        "stats": {"리더십": 93, "분석력": 78, "공감능력": 50, "창의력": 48, "행동력": 90, "사교성": 75},
    },
    "ESFJ": {
        "pokemon_kr": "잠만보",
        "pokemon_en": "Snorlax",
        "number": 143,
        "type": ["노말"],
        "type_color": ["#5D6D7E"],
        "trait": "집정관",
        "group": "SJ - 관리자",
        "group_emoji": "🛡️",
        "short_desc": "편안함을 주는 큰 존재감. 주변 모두가 쉴 수 있는 공간이 되어준다.",
        "long_desc": (
            "ESFJ는 커뮤니티의 중심이자 모두를 하나로 묶어주는 존재입니다. "
            "잠만보는 거대한 몸집으로 때로는 길을 막는 불편한 존재처럼 보이지만, "
            "그 품에 안기면 세상 가장 편안한 공간이 됩니다. "
            "ESFJ처럼 잠만보는 주변 사람들에게 안정과 풍요로움을 주며, "
            "필요할 때는 놀라운 힘을 발휘합니다. "
            "사람들과의 따뜻한 연결을 가장 중요시하며, 모두가 행복한 환경을 만드는 것에 "
            "큰 보람을 느낍니다."
        ),
        "keywords": ["사교적", "배려", "전통적", "충성스러움", "따뜻함", "책임감"],
        "strengths": [
            "집단의 화합과 유대를 만들어내는 탁월한 능력",
            "실질적인 도움으로 타인의 필요에 즉각 응답",
            "신뢰할 수 있고 헌신적인 관계 유지",
            "사람들을 하나로 모으고 행사를 주도하는 능력",
        ],
        "weaknesses": [
            "타인의 인정에 지나치게 의존",
            "갈등을 피하려다 중요한 문제를 방치",
            "비판을 개인적 공격으로 받아들임",
            "자신의 욕구를 억누르고 타인을 우선시",
        ],
        "compatibility_good": ["ISFP", "ISTP"],
        "compatibility_bad": ["INTP", "ENTP"],
        "famous": ["테일러 스위프트", "제니퍼 가너", "셀레나 고메즈", "빌 클린턴"],
        "stats": {"리더십": 70, "분석력": 55, "공감능력": 94, "창의력": 60, "행동력": 72, "사교성": 97},
    },
    "ISTP": {
        "pokemon_kr": "팬텀",
        "pokemon_en": "Gengar",
        "number": 94,
        "type": ["고스트", "독"],
        "type_color": ["#6C3483", "#8E44AD"],
        "trait": "장인",
        "group": "SP - 탐험가",
        "group_emoji": "⚡",
        "short_desc": "독립적이고 실용적이며 예측 불가능한 행동파. 혼자만의 방식이 있다.",
        "long_desc": (
            "ISTP는 말보다 행동으로 모든 것을 증명하는 과묵한 전문가입니다. "
            "팬텀은 항상 어딘가에서 지켜보다 예상치 못한 순간에 나타나는 "
            "예측 불가능한 포켓몬입니다. ISTP처럼 규칙에 얽매이지 않고 "
            "자신만의 방식으로 문제를 해결하며, 겉으로는 차갑게 보이지만 "
            "믿을 수 있는 사람에게는 믿기 어려울 만큼 충실합니다. "
            "독립성을 최우선으로 여기며, 위기 상황에서 가장 냉철하게 빛나는 유형입니다."
        ),
        "keywords": ["독립적", "실용적", "냉철함", "기술적", "모험적", "즉흥적"],
        "strengths": [
            "위기 상황에서 침착하게 문제를 해결하는 능력",
            "손과 머리를 함께 쓰는 실용적 기술 습득",
            "어떤 상황에서도 현실적이고 효율적인 접근",
            "독립적으로 일하며 높은 자율성 발휘",
        ],
        "weaknesses": [
            "감정 표현이 매우 부족해 냉담하게 보임",
            "장기 계획보다 즉각적인 해결을 선호",
            "규칙과 구조를 답답해하고 충동적인 결정",
            "관계에 깊이 관여하는 것을 불편해함",
        ],
        "compatibility_good": ["ESTJ", "ESFJ"],
        "compatibility_bad": ["ENFJ", "INFJ"],
        "famous": ["클린트 이스트우드", "미야자키 하야오", "브루스 리", "마이클 조던"],
        "stats": {"리더십": 50, "분석력": 85, "공감능력": 40, "창의력": 75, "행동력": 90, "사교성": 38},
    },
    "ISFP": {
        "pokemon_kr": "리아코",
        "pokemon_en": "Totodile",
        "number": 158,
        "type": ["물"],
        "type_color": ["#2471A3"],
        "trait": "모험가",
        "group": "SP - 탐험가",
        "group_emoji": "⚡",
        "short_desc": "자유로운 감성과 즉흥적인 활발함. 순간순간을 온몸으로 즐긴다.",
        "long_desc": (
            "ISFP는 현재 순간을 온전히 살아가는 자유로운 예술가입니다. "
            "리아코는 항상 신나게 춤추고 웃으며 어떤 상황에서도 긍정적인 에너지를 잃지 않는 "
            "포켓몬입니다. ISFP처럼 리아코는 규칙보다 자신의 감각과 즉흥성을 따르며, "
            "겉으로는 가볍게 보이지만 내면에는 깊은 감수성을 가지고 있습니다. "
            "아름다움을 알아보는 눈과 순간의 기쁨을 온몸으로 표현하는 능력이 "
            "이 유형의 가장 큰 매력입니다."
        ),
        "keywords": ["자유로운", "감성적", "현재중심", "따뜻함", "예술적", "즉흥적"],
        "strengths": [
            "현재 순간에 완전히 몰입하는 감각적 경험",
            "개방적이고 비판적이지 않은 따뜻한 태도",
            "예술과 미적 감각에서 두드러지는 창의성",
            "유연하게 새로운 경험을 받아들이는 적응력",
        ],
        "weaknesses": [
            "장기적인 계획 수립과 실행에 어려움",
            "갈등을 극도로 피해 문제가 해결되지 않음",
            "자신에 대한 과소평가와 낮은 자존감",
            "스트레스를 받으면 예측 불가능하게 반응",
        ],
        "compatibility_good": ["ESTJ", "ESFJ"],
        "compatibility_bad": ["INTJ", "ENTJ"],
        "famous": ["마이클 잭슨", "프리다 칼로", "케빈 코스트너", "브리트니 스피어스"],
        "stats": {"리더십": 40, "분석력": 55, "공감능력": 88, "창의력": 90, "행동력": 70, "사교성": 72},
    },
    "ESTP": {
        "pokemon_kr": "아케인",
        "pokemon_en": "Arcanine",
        "number": 59,
        "type": ["불꽃"],
        "type_color": ["#E67E22"],
        "trait": "사업가",
        "group": "SP - 탐험가",
        "group_emoji": "⚡",
        "short_desc": "행동파, 빠른 결단력과 카리스마. 불꽃처럼 돌진한다.",
        "long_desc": (
            "ESTP는 생각보다 행동이 앞서는 에너지 넘치는 실용주의자입니다. "
            "'전설의 포켓몬'이라고까지 불리는 아케인은 시속 240km로 달리며 "
            "한번 목표를 향해 달리기 시작하면 아무것도 멈출 수 없습니다. "
            "ESTP처럼 아케인은 멈춰서 계획을 세우는 것보다 "
            "일단 뛰어들어 상황에 맞게 대응하는 것을 선호합니다. "
            "카리스마 넘치는 외모와 불굴의 에너지로 어디서든 주목받는 존재입니다."
        ),
        "keywords": ["행동력", "카리스마", "현실적", "기민함", "사교적", "대담함"],
        "strengths": [
            "압박 상황에서 즉각적이고 효과적인 판단",
            "위기를 기회로 전환하는 탁월한 위기관리 능력",
            "에너지와 카리스마로 사람들을 자연스럽게 끌어당김",
            "직접 몸으로 부딪히며 빠르게 기술을 습득",
        ],
        "weaknesses": [
            "충동적인 결정으로 나중에 후회하는 경우가 많음",
            "규칙과 이론적 학습에 흥미를 잃음",
            "미래 계획보다 현재 자극에 집중",
            "타인의 감정보다 사실에 집중해 상처를 줌",
        ],
        "compatibility_good": ["ISFJ", "ISTJ"],
        "compatibility_bad": ["INFJ", "INTJ"],
        "famous": ["도널드 트럼프", "어니스트 헤밍웨이", "잭 니콜슨", "에디 머피"],
        "stats": {"리더십": 82, "분석력": 68, "공감능력": 55, "창의력": 72, "행동력": 98, "사교성": 90},
    },
    "ESFP": {
        "pokemon_kr": "야돈",
        "pokemon_en": "Slowpoke",
        "number": 79,
        "type": ["물", "에스퍼"],
        "type_color": ["#2980B9", "#AF7AC5"],
        "trait": "연예인",
        "group": "SP - 탐험가",
        "group_emoji": "⚡",
        "short_desc": "느긋하고 낙천적인 분위기 메이커. 주변을 편안하게 만드는 특별한 재능.",
        "long_desc": (
            "ESFP는 삶을 무대로, 자신을 주인공으로 여기는 타고난 엔터테이너입니다. "
            "야돈은 낚싯대 없이 꼬리를 물에 드리우고 멍하니 있는 것처럼 보이지만, "
            "그 느긋함과 독특한 매력으로 모두에게 사랑받는 포켓몬입니다. "
            "ESFP처럼 야돈은 서두르지 않고 현재를 즐기며, "
            "주변 모든 것에 호기심을 보이고 사람들을 편안하게 만드는 특별한 아우라가 있습니다. "
            "느리지만 절대 멈추지 않으며, 결국에는 자신만의 방식으로 목표에 도달합니다."
        ),
        "keywords": ["낙천적", "사교적", "즉흥적", "현재중심", "엔터테인먼트", "유머"],
        "strengths": [
            "어디서든 분위기를 밝게 만드는 천부적 재능",
            "현재를 즐기고 긍정적인 에너지 전파",
            "사람들과 빠르고 자연스럽게 친해지는 능력",
            "미적 감각과 창의적인 표현력",
        ],
        "weaknesses": [
            "장기 계획보다 현재 즐거움을 우선시",
            "지루하거나 반복적인 업무에 매우 취약",
            "갈등 상황에서 회피하거나 과도하게 반응",
            "심각한 주제에 집중하기 어려움",
        ],
        "compatibility_good": ["ISTJ", "ISFJ"],
        "compatibility_bad": ["INTJ", "INFJ"],
        "famous": ["마릴린 먼로", "엘튼 존", "저스틴 비버", "아리아나 그란데"],
        "stats": {"리더십": 60, "분석력": 45, "공감능력": 88, "창의력": 85, "행동력": 78, "사교성": 99},
    },
}

GROUPS = ["NT - 분석가", "NF - 외교관", "SJ - 관리자", "SP - 탐험가"]
GROUP_DESC = {
    "NT - 분석가": "🔬 논리와 분석으로 세상을 이해하는 전략가들",
    "NF - 외교관": "🌿 공감과 이상으로 세상을 변화시키려는 이상주의자들",
    "SJ - 관리자": "🛡️ 안정과 질서로 세상을 지탱하는 든든한 수호자들",
    "SP - 탐험가": "⚡ 자유와 행동으로 세상을 탐험하는 모험가들",
}

STAT_COLORS = {
    "리더십":  ("linear-gradient(90deg, #E74C3C, #FF6B6B)", "#FF6B6B"),
    "분석력":  ("linear-gradient(90deg, #3498DB, #5DADE2)", "#5DADE2"),
    "공감능력": ("linear-gradient(90deg, #27AE60, #58D68D)", "#58D68D"),
    "창의력":  ("linear-gradient(90deg, #9B59B6, #C39BD3)", "#C39BD3"),
    "행동력":  ("linear-gradient(90deg, #E67E22, #F0B27A)", "#F0B27A"),
    "사교성":  ("linear-gradient(90deg, #F1C40F, #F7DC6F)", "#F7DC6F"),
}

def get_pokemon_image_url(number):
    return f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{number}.png"

def render_stat_bars(stats: dict):
    html = ""
    for label, val in stats.items():
        gradient, _ = STAT_COLORS[label]
        pct = min(val, 100)
        html += f"""
        <div class="stat-row">
            <div class="stat-label">{label}</div>
            <div class="stat-bar-bg">
                <div class="stat-bar-fill" style="width:{pct}%; background:{gradient};"></div>
            </div>
            <div class="stat-val">{val}</div>
        </div>"""
    return html

def render_mini_card(mbti, data):
    type_tags = "".join([
        f'<span class="type-tag" style="background:{data["type_color"][j]}">{t}</span>'
        for j, t in enumerate(data["type"])
    ])
    img_url = get_pokemon_image_url(data["number"])
    return f"""
    <div class="card">
        <div class="mbti-badge">{mbti}</div>
        <img src="{img_url}" class="pokemon-img" alt="{data['pokemon_kr']}">
        <div class="pokemon-number">#{data['number']:03d}</div>
        <div class="pokemon-name-kr">{data['pokemon_kr']}</div>
        <div class="pokemon-name-en">{data['pokemon_en']}</div>
        {type_tags}
        <div class="trait-label">{data['trait']}</div>
        <div class="card-desc">{data['short_desc']}</div>
    </div>"""

# ──────────────────────────────────────────────
# 앱 시작
# ──────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="hero-title">⚡ MBTI POKÉDEX ⚡</div>
    <div class="hero-subtitle">16가지 MBTI 유형과 닮은 포켓몬을 찾아보세요</div>
</div>
""", unsafe_allow_html=True)

# ── 탭 ──
tab1, tab2, tab3 = st.tabs(["📖 전체 도감", "🎯 내 유형 찾기", "📊 유형 비교"])

# ══════════════════════════════
# TAB 1: 전체 도감
# ══════════════════════════════
with tab1:
    # 필터 바
    st.markdown('<div class="filter-bar">', unsafe_allow_html=True)
    fc1, fc2, fc3 = st.columns([1.2, 1.5, 1])
    with fc1:
        selected_group = st.selectbox("그룹 필터", ["전체 보기"] + GROUPS, label_visibility="visible")
    with fc2:
        search = st.text_input("검색", placeholder="INTJ, 피카츄, 전기...", label_visibility="visible")
    with fc3:
        cols_count = st.selectbox("열 수", [2, 3, 4], index=2, label_visibility="visible")
    st.markdown('</div>', unsafe_allow_html=True)

    # 필터링
    filtered = {
        k: v for k, v in MBTI_POKEMON.items()
        if (selected_group == "전체 보기" or v["group"] == selected_group)
        and (
            search.strip() == ""
            or search.upper() in k
            or search in v["pokemon_kr"]
            or search.lower() in v["pokemon_en"].lower()
            or any(search in t for t in v["type"])
            or search in v["trait"]
        )
    }

    if not filtered:
        st.warning("검색 결과가 없습니다.")
    else:
        display_groups = [selected_group] if selected_group != "전체 보기" else GROUPS
        for group in display_groups:
            group_items = {k: v for k, v in filtered.items() if v["group"] == group}
            if not group_items:
                continue

            # 그룹 헤더
            st.markdown(f"""
            <div class="group-header">
                <div class="group-title-text">{group}</div>
                <div class="group-line"></div>
                <div style="color:#666;font-size:0.78rem;">{GROUP_DESC[group]}</div>
            </div>""", unsafe_allow_html=True)

            cols = st.columns(cols_count)
            for i, (mbti, data) in enumerate(group_items.items()):
                with cols[i % cols_count]:
                    st.markdown(render_mini_card(mbti, data), unsafe_allow_html=True)

# ══════════════════════════════
# TAB 2: 내 유형 찾기
# ══════════════════════════════
with tab2:
    st.markdown("#### 나의 MBTI 유형을 선택하세요")
    selected_mbti = st.selectbox(
        "MBTI 선택",
        list(MBTI_POKEMON.keys()),
        format_func=lambda x: f"{x}  —  {MBTI_POKEMON[x]['trait']}  ({MBTI_POKEMON[x]['pokemon_kr']})",
        label_visibility="collapsed"
    )

    if selected_mbti:
        d = MBTI_POKEMON[selected_mbti]
        img_url = get_pokemon_image_url(d["number"])

        st.markdown('<div class="detail-wrapper">', unsafe_allow_html=True)

        # 상단: 이미지 + 기본 정보
        col_img, col_info = st.columns([1, 2])
        with col_img:
            st.image(img_url, width=220)
        with col_info:
            type_tags_html = "".join([
                f'<span class="type-tag" style="background:{d["type_color"][j]};font-size:0.9rem;padding:0.3rem 1rem;">{t}</span>'
                for j, t in enumerate(d["type"])
            ])
            st.markdown(f"""
            <div style="margin-bottom:0.3rem">
                <span style="background:linear-gradient(135deg,#f5a623,#f8e71c);color:#1a1a2e;
                font-weight:900;font-size:1.8rem;border-radius:10px;padding:0.2rem 1rem;
                letter-spacing:4px;">{selected_mbti}</span>
            </div>
            <div style="color:#f5a623;font-size:1rem;font-weight:700;margin:0.5rem 0;
                text-transform:uppercase;letter-spacing:2px;">{d['trait']}</div>
            <div style="color:#fff;font-size:1.5rem;font-weight:900;margin-bottom:0.2rem">
                {d['pokemon_kr']}
            </div>
            <div style="color:#7788aa;font-size:0.9rem;margin-bottom:0.7rem">
                #{d['number']:03d} {d['pokemon_en']}  ·  {d['group']}
            </div>
            {type_tags_html}
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # 키워드
        st.markdown('<div class="detail-section-title">🏷️ 핵심 키워드</div>', unsafe_allow_html=True)
        keywords_html = "".join([f'<span class="keyword-chip">{kw}</span>' for kw in d["keywords"]])
        st.markdown(keywords_html, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # 상세 설명
        st.markdown('<div class="detail-section-title">📖 상세 설명</div>', unsafe_allow_html=True)
        st.markdown(f'<div style="color:#ccc;font-size:0.9rem;line-height:1.8;padding:0.5rem 0">{d["long_desc"]}</div>', unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # 강점 / 약점
        col_s, col_w = st.columns(2)
        with col_s:
            st.markdown('<div class="detail-section-title">✅ 강점</div>', unsafe_allow_html=True)
            for s in d["strengths"]:
                st.markdown(f'<div class="strength-item">• {s}</div>', unsafe_allow_html=True)
        with col_w:
            st.markdown('<div class="detail-section-title">⚠️ 약점</div>', unsafe_allow_html=True)
            for w in d["weaknesses"]:
                st.markdown(f'<div class="weakness-item">• {w}</div>', unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # 스탯 바
        st.markdown('<div class="detail-section-title">📊 성격 스탯</div>', unsafe_allow_html=True)
        st.markdown(render_stat_bars(d["stats"]), unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # 궁합
        col_g, col_b = st.columns(2)
        with col_g:
            st.markdown('<div class="detail-section-title">💚 잘 맞는 유형</div>', unsafe_allow_html=True)
            good_html = "".join([
                f'<span class="compat-good">{m}  {MBTI_POKEMON[m]["pokemon_kr"]}</span>'
                for m in d["compatibility_good"]
            ])
            st.markdown(good_html, unsafe_allow_html=True)
        with col_b:
            st.markdown('<div class="detail-section-title">❤️‍🔥 조심해야 할 유형</div>', unsafe_allow_html=True)
            bad_html = "".join([
                f'<span class="compat-bad">{m}  {MBTI_POKEMON[m]["pokemon_kr"]}</span>'
                for m in d["compatibility_bad"]
            ])
            st.markdown(bad_html, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # 유명인
        st.markdown('<div class="detail-section-title">🌟 대표 유명인</div>', unsafe_allow_html=True)
        famous_html = "".join([f'<span class="famous-chip">{f}</span>' for f in d["famous"]])
        st.markdown(famous_html, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

# ══════════════════════════════
# TAB 3: 유형 비교
# ══════════════════════════════
with tab3:
    st.markdown("#### 두 유형을 선택해서 비교해보세요")
    cc1, cc2 = st.columns(2)
    with cc1:
        mbti_a = st.selectbox("유형 A", list(MBTI_POKEMON.keys()),
            format_func=lambda x: f"{x} — {MBTI_POKEMON[x]['pokemon_kr']}", key="cmp_a")
    with cc2:
        mbti_b = st.selectbox("유형 B", list(MBTI_POKEMON.keys()), index=1,
            format_func=lambda x: f"{x} — {MBTI_POKEMON[x]['pokemon_kr']}", key="cmp_b")

    da, db = MBTI_POKEMON[mbti_a], MBTI_POKEMON[mbti_b]

    st.markdown("<br>", unsafe_allow_html=True)

    col_a, col_vs, col_b = st.columns([5, 1, 5])
    with col_a:
        st.image(get_pokemon_image_url(da["number"]), width=160)
        st.markdown(f"### {mbti_a}  {da['pokemon_kr']}")
        st.markdown(f"*{da['trait']}*")
    with col_vs:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        st.markdown("## VS", unsafe_allow_html=False)
    with col_b:
        st.image(get_pokemon_image_url(db["number"]), width=160)
        st.markdown(f"### {mbti_b}  {db['pokemon_kr']}")
        st.markdown(f"*{db['trait']}*")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("#### 📊 스탯 비교")

    stat_keys = list(da["stats"].keys())
    for stat in stat_keys:
        val_a = da["stats"][stat]
        val_b = db["stats"][stat]
        gradient_a, color_a = STAT_COLORS[stat]
        gradient_b, _ = STAT_COLORS[stat]

        col1, col2, col3, col4, col5 = st.columns([1, 3, 1, 3, 1])
        with col1:
            st.markdown(f"<div style='text-align:right;color:#dde;font-size:0.85rem;font-weight:700;padding-top:4px'>{val_a}</div>", unsafe_allow_html=True)
        with col2:
            bar_a = f"""
            <div style="display:flex;align-items:center;justify-content:flex-end;height:22px;">
                <div style="width:{val_a}%;height:10px;background:{gradient_a};border-radius:99px;"></div>
            </div>"""
            st.markdown(bar_a, unsafe_allow_html=True)
        with col3:
            st.markdown(f"<div style='text-align:center;color:#888;font-size:0.72rem;padding-top:4px'>{stat}</div>", unsafe_allow_html=True)
        with col4:
            bar_b = f"""
            <div style="display:flex;align-items:center;height:22px;">
                <div style="width:{val_b}%;height:10px;background:{gradient_b};border-radius:99px;"></div>
            </div>"""
            st.markdown(bar_b, unsafe_allow_html=True)
        with col5:
            st.markdown(f"<div style='color:#dde;font-size:0.85rem;font-weight:700;padding-top:4px'>{val_b}</div>", unsafe_allow_html=True)

    # 궁합 체크
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("#### 💞 궁합 분석")
    is_good = mbti_b in da["compatibility_good"] or mbti_a in db["compatibility_good"]
    is_bad  = mbti_b in da["compatibility_bad"]  or mbti_a in db["compatibility_bad"]

    if is_good:
        st.success(f"✨ **{mbti_a} × {mbti_b}** 는 서로를 보완하는 최고의 궁합입니다! 서로의 부족한 점을 채워주며 강력한 시너지를 만들어냅니다.")
    elif is_bad:
        st.error(f"⚡ **{mbti_a} × {mbti_b}** 는 가치관 충돌이 생길 수 있는 관계입니다. 서로 이해하는 노력이 필요하지만, 그만큼 성장의 기회가 될 수 있습니다.")
    else:
        st.info(f"🤝 **{mbti_a} × {mbti_b}** 는 무난한 관계입니다. 서로의 차이를 인정하면 좋은 파트너가 될 수 있습니다.")

    # 공통점 / 차이점
    same_letters = [l for l in ["I/E", "N/S", "T/F", "J/P"]
                    if (mbti_a[i] == mbti_b[i]) for i, l in enumerate(["I/E","N/S","T/F","J/P"])]
    diff_letters = [l for i, l in enumerate(["I/E","N/S","T/F","J/P"]) if mbti_a[i] != mbti_b[i]]

    col_same, col_diff = st.columns(2)
    with col_same:
        st.markdown("**공통점**")
        if same_letters:
            for l in same_letters:
                idx = ["I/E","N/S","T/F","J/P"].index(l)
                letter = mbti_a[idx]
                meanings = {"I":"내향형","E":"외향형","N":"직관형","S":"감각형","T":"사고형","F":"감정형","J":"판단형","P":"인식형"}
                st.markdown(f"- 둘 다 **{letter}** ({meanings.get(letter,'')})")
        else:
            st.markdown("- 공통된 성향이 없습니다")
    with col_diff:
        st.markdown("**차이점**")
        for i, l in enumerate(["I/E","N/S","T/F","J/P"]):
            if mbti_a[i] != mbti_b[i]:
                meanings = {"I":"내향형","E":"외향형","N":"직관형","S":"감각형","T":"사고형","F":"감정형","J":"판단형","P":"인식형"}
                la, lb = mbti_a[i], mbti_b[i]
                st.markdown(f"- **{mbti_a}**: {la} ({meanings.get(la,'')})  vs  **{mbti_b}**: {lb} ({meanings.get(lb,'')})")

# ── 푸터 ──
st.markdown("---")
st.markdown(
    "<div style='text-align:center;color:#444;font-size:0.75rem;padding:0.5rem 0'>"
    "포켓몬 이미지 출처: PokeAPI · MBTI 설명은 재미와 교육 목적으로 작성되었습니다"
    "</div>",
    unsafe_allow_html=True
)
