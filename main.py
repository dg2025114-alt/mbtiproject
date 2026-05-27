
import streamlit as st

st.set_page_config(
    page_title="MBTI 포켓몬 도감",
    page_icon="⚡",
    layout="wide"
)

# CSS 스타일
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700;900&display=swap');

    html, body, [class*="css"] {
        font-family: 'Noto Sans KR', sans-serif;
    }

    .main { background-color: #1a1a2e; }

    .title {
        text-align: center;
        font-size: 3rem;
        font-weight: 900;
        background: linear-gradient(135deg, #f5a623, #f8e71c, #ff6b6b);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
    }

    .subtitle {
        text-align: center;
        color: #aaa;
        font-size: 1rem;
        margin-bottom: 2rem;
    }

    .card {
        background: linear-gradient(145deg, #16213e, #0f3460);
        border-radius: 20px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        border: 1px solid rgba(255,255,255,0.08);
        transition: transform 0.2s;
        text-align: center;
    }

    .card:hover {
        transform: translateY(-4px);
        border-color: rgba(245,166,35,0.5);
    }

    .mbti-badge {
        display: inline-block;
        background: linear-gradient(135deg, #f5a623, #f8e71c);
        color: #1a1a2e;
        font-weight: 900;
        font-size: 1.4rem;
        border-radius: 10px;
        padding: 0.2rem 0.8rem;
        margin-bottom: 0.5rem;
        letter-spacing: 2px;
    }

    .pokemon-name {
        color: #ffffff;
        font-size: 1.1rem;
        font-weight: 700;
        margin: 0.3rem 0;
    }

    .pokemon-eng {
        color: #888;
        font-size: 0.85rem;
        margin-bottom: 0.5rem;
    }

    .type-tag {
        display: inline-block;
        border-radius: 20px;
        padding: 0.15rem 0.6rem;
        font-size: 0.75rem;
        font-weight: 700;
        margin: 0.2rem;
        color: white;
    }

    .desc {
        color: #ccc;
        font-size: 0.82rem;
        line-height: 1.5;
        margin-top: 0.6rem;
    }

    .pokemon-img {
        width: 100px;
        height: 100px;
        object-fit: contain;
        margin: 0.5rem auto;
        display: block;
        filter: drop-shadow(0 4px 12px rgba(245,166,35,0.3));
    }

    .filter-section {
        background: #16213e;
        border-radius: 15px;
        padding: 1rem 1.5rem;
        margin-bottom: 2rem;
        border: 1px solid rgba(255,255,255,0.06);
    }

    .group-title {
        color: #f5a623;
        font-weight: 900;
        font-size: 1.2rem;
        margin: 1.5rem 0 0.5rem 0;
        border-left: 4px solid #f5a623;
        padding-left: 0.7rem;
    }
</style>
""", unsafe_allow_html=True)

# 포켓몬 데이터
MBTI_POKEMON = {
    "INTJ": {
        "pokemon_kr": "뮤츠",
        "pokemon_en": "Mewtwo",
        "number": 150,
        "type": ["에스퍼"],
        "type_color": ["#F95587"],
        "trait": "전략가",
        "desc": "냉철한 지성과 독립적인 사고로 모든 것을 계획하고 실행한다.",
        "group": "NT - 분석가"
    },
    "INTP": {
        "pokemon_kr": "포리곤",
        "pokemon_en": "Porygon",
        "number": 137,
        "type": ["노말"],
        "type_color": ["#A8A878"],
        "trait": "논리술사",
        "desc": "분석적이고 호기심 많은 디지털 존재. 데이터로 세상을 이해한다.",
        "group": "NT - 분석가"
    },
    "ENTJ": {
        "pokemon_kr": "리자몽",
        "pokemon_en": "Charizard",
        "number": 6,
        "type": ["불꽃", "비행"],
        "type_color": ["#F08030", "#98D8D8"],
        "trait": "통솔자",
        "desc": "강한 리더십과 도전 정신. 한계를 뛰어넘는 것이 본능이다.",
        "group": "NT - 분석가"
    },
    "ENTP": {
        "pokemon_kr": "개굴닌자",
        "pokemon_en": "Greninja",
        "number": 658,
        "type": ["물", "악"],
        "type_color": ["#6890F0", "#705848"],
        "trait": "변론가",
        "desc": "창의적이고 빠른 적응력. 어떤 상황에서도 새로운 전략을 찾아낸다.",
        "group": "NT - 분석가"
    },
    "INFJ": {
        "pokemon_kr": "루기아",
        "pokemon_en": "Lugia",
        "number": 249,
        "type": ["에스퍼", "비행"],
        "type_color": ["#F95587", "#98D8D8"],
        "trait": "옹호자",
        "desc": "세상의 평화를 수호하는 깊은 통찰력과 신비로운 존재.",
        "group": "NF - 외교관"
    },
    "INFP": {
        "pokemon_kr": "이브이",
        "pokemon_en": "Eevee",
        "number": 133,
        "type": ["노말"],
        "type_color": ["#A8A878"],
        "trait": "중재자",
        "desc": "감성적이고 다양한 가능성을 지닌 순수한 영혼. 꿈을 따라 진화한다.",
        "group": "NF - 외교관"
    },
    "ENFJ": {
        "pokemon_kr": "피카츄",
        "pokemon_en": "Pikachu",
        "number": 25,
        "type": ["전기"],
        "type_color": ["#F8D030"],
        "trait": "선도자",
        "desc": "팀의 상징이자 따뜻한 에너지. 사람과의 유대를 가장 중요시한다.",
        "group": "NF - 외교관"
    },
    "ENFP": {
        "pokemon_kr": "뮤",
        "pokemon_en": "Mew",
        "number": 151,
        "type": ["에스퍼"],
        "type_color": ["#F95587"],
        "trait": "활동가",
        "desc": "자유롭고 호기심이 넘치며 장난기 가득한 무한한 가능성의 존재.",
        "group": "NF - 외교관"
    },
    "ISTJ": {
        "pokemon_kr": "거북왕",
        "pokemon_en": "Blastoise",
        "number": 9,
        "type": ["물"],
        "type_color": ["#6890F0"],
        "trait": "현실주의자",
        "desc": "강한 책임감과 안정감. 든든한 수비로 소중한 것을 지킨다.",
        "group": "SJ - 관리자"
    },
    "ISFJ": {
        "pokemon_kr": "치코리타",
        "pokemon_en": "Chikorita",
        "number": 152,
        "type": ["풀"],
        "type_color": ["#78C850"],
        "trait": "수호자",
        "desc": "다정하고 헌신적인 성격. 주변 사람들을 세심하게 돌본다.",
        "group": "SJ - 관리자"
    },
    "ESTJ": {
        "pokemon_kr": "강철톤",
        "pokemon_en": "Aggron",
        "number": 306,
        "type": ["강철", "바위"],
        "type_color": ["#B8B8D0", "#B8A038"],
        "trait": "경영자",
        "desc": "규율과 강한 의지, 조직력. 맡은 영역은 반드시 지켜낸다.",
        "group": "SJ - 관리자"
    },
    "ESFJ": {
        "pokemon_kr": "잠만보",
        "pokemon_en": "Snorlax",
        "number": 143,
        "type": ["노말"],
        "type_color": ["#A8A878"],
        "trait": "집정관",
        "desc": "편안함을 주는 큰 존재감. 주변 모두가 쉴 수 있는 공간이 되어준다.",
        "group": "SJ - 관리자"
    },
    "ISTP": {
        "pokemon_kr": "팬텀",
        "pokemon_en": "Gengar",
        "number": 94,
        "type": ["고스트", "독"],
        "type_color": ["#705898", "#A040A0"],
        "trait": "장인",
        "desc": "독립적이고 실용적이며 예측 불가능한 행동파. 혼자만의 방식이 있다.",
        "group": "SP - 탐험가"
    },
    "ISFP": {
        "pokemon_kr": "리아코",
        "pokemon_en": "Totodile",
        "number": 158,
        "type": ["물"],
        "type_color": ["#6890F0"],
        "trait": "모험가",
        "desc": "자유로운 감성과 즉흥적인 활발함. 순간순간을 온몸으로 즐긴다.",
        "group": "SP - 탐험가"
    },
    "ESTP": {
        "pokemon_kr": "아케이도스",
        "pokemon_en": "Arcanine",
        "number": 59,
        "type": ["불꽃"],
        "type_color": ["#F08030"],
        "trait": "사업가",
        "desc": "행동파, 빠른 결단력과 카리스마. 불꽃처럼 돌진한다.",
        "group": "SP - 탐험가"
    },
    "ESFP": {
        "pokemon_kr": "야돈",
        "pokemon_en": "Slowpoke",
        "number": 79,
        "type": ["물", "에스퍼"],
        "type_color": ["#6890F0", "#F95587"],
        "trait": "연예인",
        "desc": "느긋하고 낙천적인 분위기 메이커. 주변을 편안하게 만드는 특별한 재능.",
        "group": "SP - 탐험가"
    },
}

GROUPS = ["NT - 분석가", "NF - 외교관", "SJ - 관리자", "SP - 탐험가"]

def get_pokemon_image_url(number):
    return f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{number}.png"

# 헤더
st.markdown('<div class="title">⚡ MBTI 포켓몬 도감 ⚡</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">당신의 MBTI 유형과 닮은 포켓몬을 찾아보세요!</div>', unsafe_allow_html=True)

# 필터
with st.container():
    st.markdown('<div class="filter-section">', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 2])
    with col1:
        selected_group = st.selectbox(
            "🔍 그룹 필터",
            ["전체 보기"] + GROUPS,
            label_visibility="collapsed"
        )
    with col2:
        search = st.text_input("포켓몬 또는 MBTI 검색", placeholder="예: INTJ, 피카츄, 전기...", label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)

# 필터링
filtered = {
    k: v for k, v in MBTI_POKEMON.items()
    if (selected_group == "전체 보기" or v["group"] == selected_group)
    and (
        search == ""
        or search.upper() in k
        or search in v["pokemon_kr"]
        or search.lower() in v["pokemon_en"].lower()
        or any(search in t for t in v["type"])
    )
}

# 그룹별 출력
display_groups = [selected_group] if selected_group != "전체 보기" else GROUPS

for group in display_groups:
    group_items = {k: v for k, v in filtered.items() if v["group"] == group}
    if not group_items:
        continue

    st.markdown(f'<div class="group-title">🏷️ {group}</div>', unsafe_allow_html=True)

    cols = st.columns(4)
    for i, (mbti, data) in enumerate(group_items.items()):
        with cols[i % 4]:
            # 타입 태그 HTML
            type_tags = "".join([
                f'<span class="type-tag" style="background:{data["type_color"][j]}">{t}</span>'
                for j, t in enumerate(data["type"])
            ])

            img_url = get_pokemon_image_url(data["number"])

            st.markdown(f"""
            <div class="card">
                <div class="mbti-badge">{mbti}</div>
                <img src="{img_url}" class="pokemon-img" alt="{data['pokemon_kr']}">
                <div class="pokemon-name">{data['pokemon_kr']}</div>
                <div class="pokemon-eng">#{data['number']:03d} {data['pokemon_en']}</div>
                {type_tags}
                <div style="color:#f5a623; font-size:0.8rem; font-weight:700; margin-top:0.4rem">{data['trait']}</div>
                <div class="desc">{data['desc']}</div>
            </div>
            """, unsafe_allow_html=True)

# 내 MBTI 찾기
st.markdown("---")
st.markdown("### 🎯 내 MBTI로 바로 찾기")
mbti_options = list(MBTI_POKEMON.keys())
selected_mbti = st.selectbox("MBTI를 선택하세요", mbti_options)

if selected_mbti:
    data = MBTI_POKEMON[selected_mbti]
    c1, c2 = st.columns([1, 2])
    with c1:
        st.image(get_pokemon_image_url(data["number"]), width=180)
    with c2:
        st.markdown(f"## {selected_mbti} — {data['pokemon_kr']}")
        st.markdown(f"**#{data['number']:03d} {data['pokemon_en']}** | {data['trait']}")
        st.markdown(f"**타입:** {' / '.join(data['type'])}")
        st.markdown(f"**그룹:** {data['group']}")
        st.info(data['desc'])
