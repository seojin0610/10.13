import streamlit as st

st.set_page_config(
    page_title="MBTI 포켓몬 단짝 찾기",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

POKEMON_MBTI_DATA = {
    "INTJ": {
        "name_kr": "뮤츠",
        "name_en": "Mewtwo",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/150.png",
        "type": "에스퍼 (Psychic)",
        "traits": "냉철한 분석력, 완벽주의, 압도적인 지능",
        "reasons": [
            "치밀한 전략을 세우고 홀로 깊게 사고하는 INTJ의 냉철함과 닮았습니다.",
            "타인의 시선에 휘둘리지 않고 자신만의 독보적인 영역을 구축합니다.",
            "압도적인 지능과 독립성으로 어떤 문제든 명쾌하게 해결합니다."
        ]
    },
    "INTP": {
        "name_kr": "후딘",
        "name_en": "Alakazam",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/65.png",
        "type": "에스퍼 (Psychic)",
        "traits": "IQ 5000의 박학다식, 아이디어 파공, 원리 탐구",
        "reasons": [
            "호기심이 넘치고 이론적 문제 해결을 좋아하는 INTP와 지적 호흡이 잘 맞습니다.",
            "끊임없이 지식을 탐구하며 독창적인 관점으로 세상을 분석합니다.",
            "말없이 서로의 생각과 지적 탐구를 깊이 존중해주는 단짝이 됩니다."
        ]
    },
    "ENTJ": {
        "name_kr": "리자몽",
        "name_en": "Charizard",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/6.png",
        "type": "불꽃 / 비행 (Fire / Flying)",
        "traits": "강인한 리더십, 불같은 승부욕, 리더의 카리스마",
        "reasons": [
            "목표를 향해 거침없이 돌진하는 ENTJ의 리더십과 야망을 지지해줍니다.",
            "어려운 난관이 닥쳐도 특유의 카리스마와 열정으로 함께 돌파합니다.",
            "서로에게 강력한 동기부여를 주며 최고의 목표를 향해 나아갑니다."
        ]
    },
    "ENTP": {
        "name_kr": "팬텀",
        "name_en": "Gengar",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/94.png",
        "type": "고스트 / 독 (Ghost / Poison)",
        "traits": "장난기 가득한 창의력, 임기응변, 유쾌한 에너자이저",
        "reasons": [
            "새롭고 독창적인 아이디어가 샘솟는 ENTP에게 최고의 유쾌한 파트너입니다.",
            "고정관념을 깨부수며 매일매일 지루할 틈 없는 신선한 모험을 선사합니다.",
            "어떤 뜻밖의 상황에서도 뛰어난 임기응변으로 함께 위기를 즐겁게 넘어섭니다."
        ]
    },
    "INFJ": {
        "name_kr": "가디안",
        "name_en": "Gardevoir",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/282.png",
        "type": "에스퍼 / 페어리 (Psychic / Fairy)",
        "traits": "깊은 공감 능력, 헌신, 신비로운 직관력",
        "reasons": [
            "타인의 감정을 누구보다 깊이 이해하고 따뜻하게 보살피는 INFJ와 어울립니다.",
            "말하지 않아도 마음을 읽고 굳건한 신뢰와 신비로운 안식처가 되어줍니다.",
            "소중한 가치와 사람을 지키기 위해 끝까지 헌신하는 진실된 단짝입니다."
        ]
    },
    "INFP": {
        "name_kr": "이브이",
        "name_en": "Eevee",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/133.png",
        "type": "노멀 (Normal)",
        "traits": "무한한 가능성, 순수한 감수성, 풍부한 상상력",
        "reasons": [
            "다양한 가능성을 내포하고 순수한 풍부한 감성을 가진 INFP의 마음을 매료시킵니다.",
            "어떤 형태의 성장도 포용해주는 따뜻하고 유연한 성품을 지녔습니다.",
            "서로의 꿈과 풍부한 상상력을 조용히 응원하며 든든한 버팀목이 됩니다."
        ]
    },
    "ENFJ": {
        "name_kr": "망나뇽",
        "name_en": "Dragonite",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/149.png",
        "type": "드래곤 / 비행 (Dragon / Flying)",
        "traits": "온화한 영웅, 친절함, 타인을 돕는 헌신",
        "reasons": [
            "주변 사람들을 챙기고 선한 영향력을 퍼뜨리는 ENFJ의 성품과 똑 닮았습니다.",
            "넓은 바다처럼 온화한 마음으로 사람들을 응원하고 품어줍니다.",
            "위기 상황에서는 누구보다 강력하게 친구를 지키는 따뜻한 수호자입니다."
        ]
    },
    "ENFP": {
        "name_kr": "피카츄",
        "name_en": "Pikachu",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png",
        "type": "전기 (Electric)",
        "traits": "톡톡 튀는 에너자이저, 친화력, 밝은 긍정왕",
        "reasons": [
            "언제나 열정적이고 에너지가 넘쳐나는 ENFP에게 짜릿한 활력을 선사합니다.",
            "어디서나 금세 친구가 되는 인싸 매력과 밝은 시너지를 냅니다.",
            "일상 속 작은 순간도 밝은 웃음과 긍정 에너지로 채워주는 빛나는 단짝입니다."
        ]
    },
    "ISTJ": {
        "name_kr": "거북왕",
        "name_en": "Blastoise",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/9.png",
        "type": "물 (Water)",
        "traits": "묵묵한 책임감, 신뢰성, 흔들리지 않는 든든함",
        "reasons": [
            "주어진 책임을 완벽하게 완수하고 원칙을 지키는 ISTJ의 신뢰감과 잘 맞습니다.",
            "어떤 풍파에도 흔들리지 않는 묵묵하고 단단한 방어막이 되어줍니다.",
            "철저한 준비성과 꼼꼼함으로 일상을 차분하고 안정적으로 이끌어줍니다."
        ]
    },
    "ISFJ": {
        "name_kr": "이상해씨",
        "name_en": "Bulbasaur",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/1.png",
        "type": "풀 / 독 (Grass / Poison)",
        "traits": "차분한 조력자, 배려심, 든든한 세심함",
        "reasons": [
            "주변을 세심하게 배려하고 온화한 안식처를 주는 ISFJ의 따뜻함과 어울립니다.",
            "변함없는 모습으로 곁을 지키며 묵묵히 도움을 주는 충직한 소울메이트입니다.",
            "작은 것 하나까지 기억하고 챙겨주는 깊은 성실함을 공유합니다."
        ]
    },
    "ESTJ": {
        "name_kr": "윈디",
        "name_en": "Arcanine",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/59.png",
        "type": "불꽃 (Fire)",
        "traits": "위풍당당함, 규칙 준수, 체계적인 리더십",
        "reasons": [
            "체계적이고 정의로우며 용맹함을 갖춘 ESTJ의 성향과 호흡이 잘 맞습니다.",
            "당당한 모습으로 조직과 팀을 단결시키고 효율적으로 이끕니다.",
            "신의와 약속을 목숨처럼 여기는 강한 책임감으로 정상을 향해 나아갑니다."
        ]
    },
    "ESFJ": {
        "name_kr": "해피너스",
        "name_en": "Blissey",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/242.png",
        "type": "노멀 (Normal)",
        "traits": "사랑과 치유의 마술사, 친화력, 세심한 케어",
        "reasons": [
            "모두에게 행복과 치유의 에너지를 건네는 ESFJ의 따뜻함에 딱 맞춰집니다.",
            "타인의 기쁨과 슬픔에 깊이 공감하고 정성껏 마음을 보듬어줍니다.",
            "화기애애한 분위기를 만들고 보람찬 일상을 함께 만드는 친근한 단짝입니다."
        ]
    },
    "ISTP": {
        "name_kr": "루카리오",
        "name_en": "Lucario",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/448.png",
        "type": "격투 / 강철 (Fighting / Steel)",
        "traits": "냉철한 파동 탐지, 문제 해결사, 침착한 해결력",
        "reasons": [
            "상황을 냉철하게 직관하고 정밀하게 문제를 해결하는 ISTP와 닮았습니다.",
            "불필요한 감정 소비 없이 깔끔하고 군더더기 없는 도전을 함께합니다.",
            "서로의 영역을 존중하면서도 결정적인 순간 강력한 합을 맞추는 단짝입니다."
        ]
    },
    "ISFP": {
        "name_kr": "잠만보",
        "name_en": "Snorlax",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/143.png",
        "type": "노멀 (Normal)",
        "traits": "유유자적, 마이페이스, 평화로운 힐링",
        "reasons": [
            "여유를 즐기고 평화로운 삶을 추구하는 ISFP에게 편안한 안식을 선사합니다.",
            "남들의 시선보다 현재 moment와 평화로움을 최우선으로 아낍니다.",
            "함께 있는 것만으로도 도심 속 스트레스가 사르르 녹아내리는 힐링 친구입니다."
        ]
    },
    "ESTP": {
        "name_kr": "괴력몬",
        "name_en": "Machamp",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/68.png",
        "type": "격투 (Fighting)",
        "traits": "액션파 에너자이저, 실전 중심, 에너제틱",
        "reasons": [
            "말보다 행동이 먼저 나가는 역동적인 ESTP와 화끈한 에너지를 자랑합니다.",
            "어떤 액티비티나 스릴 넘치는 현장도 거침없이 도전하고 즐깁니다.",
            "거침없는 솔직함과 넘치는 행동력으로 함께 매 순간 최선을 다해 달립니다."
        ]
    },
    "ESFP": {
        "name_kr": "푸린",
        "name_en": "Jigglypuff",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/39.png",
        "type": "노멀 / 페어리 (Normal / Fairy)",
        "traits": "무대 위의 주인공, 스타성, 사랑스러운 분위기 메이커",
        "reasons": [
            "주목받는 것을 즐기고 사람들에게 즐거움을 전하는 ESFP의 매력과 부합합니다.",
            "풍부한 표현력과 특유의 넘치는 텐션으로 어디서든 인기를 끌어모읍니다.",
            "함께 있는 모든 순간을 흥겨운 축제 무대로 만드는 러블리 파트너입니다."
        ]
    }
}

st.markdown("""
    <style>
    /* Dark & Vibrant Yellow Base Theme Override */
    .stApp {
        background-color: #0d0d0d;
        color: #f5f5f5;
        font-family: 'Pretendard', 'Noto Sans KR', sans-serif;
    }
    
    /* Title Styling */
    .main-title {
        font-size: 2.8rem;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(135deg, #ffe600 0%, #ffaa00 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
    }
    
    .sub-title {
        text-align: center;
        font-size: 1.2rem;
        color: #e6e6e6;
        font-weight: 500;
        margin-bottom: 2rem;
    }

    /* Container Glassmorphism Card */
    .pokemon-card {
        background: rgba(26, 26, 26, 0.95);
        border: 2px solid #ffe600;
        border-radius: 20px;
        padding: 25px;
        box-shadow: 0 10px 30px rgba(255, 230, 0, 0.25);
        margin-top: 15px;
    }

    /* Pokemon Name Header */
    .pokemon-header {
        font-size: 2.2rem;
        font-weight: 800;
        color: #ffe600;
        text-align: center;
        margin-bottom: 5px;
    }

    .pokemon-subname {
        font-size: 1.2rem;
        color: #aaaaaa;
        text-align: center;
        margin-bottom: 20px;
    }

    /* Badges */
    .type-badge {
        display: inline-block;
        background-color: #ffe600;
        color: #000000;
        font-weight: 800;
        padding: 6px 18px;
        border-radius: 20px;
        font-size: 1.05rem;
        margin-bottom: 15px;
    }

    .trait-box {
        background-color: #1a1a1a;
        border-left: 4px solid #ffe600;
        padding: 12px 16px;
        border-radius: 6px;
        font-size: 1.1rem;
        color: #ffffff;
        margin-bottom: 20px;
    }

    /* Reason List */
    .reason-list {
        font-size: 1.15rem;
        line-height: 1.8;
        color: #f0f0f0;
    }

    /* Customizing Streamlit Selectbox Label */
    label[data-testid="stWidgetLabel"] {
        color: #ffe600 !important;
        font-size: 1.3rem !important;
        font-weight: 700 !important;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>⚡ MBTI 포켓몬 단짝 찾기 ⚡</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>당신의 성격 유형(MBTI)에 가장 잘 어울리는 단짝 포켓몬을 만나보세요!</p>", unsafe_allow_html=True)

mbti_list = list(POKEMON_MBTI_DATA.keys())
selected_mbti = st.selectbox(
    "👉 당신의 MBTI 유형을 선택해 주세요:",
    options=["선택하세요..."] + mbti_list,
    index=0
)

if selected_mbti != "선택하세요...":
    # Trigger celebratory balloons/snow effects
    st.balloons()
    st.snow()

    data = POKEMON_MBTI_DATA[selected_mbti]

    st.markdown("---")

    # Main Card Layout
    col1, col2 = st.columns([1, 1], gap="medium")

    with col1:
        st.image(data["image"], use_container_width=True, caption=f"공식 일러스트: {data['name_kr']}")

    with col2:
        st.markdown(f"<div class='pokemon-header'>{data['name_kr']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='pokemon-subname'>({data['name_en']})</div>", unsafe_allow_html=True)
        
        st.markdown(f"**⚡ 포켓몬 타입:** <span class='type-badge'>{data['type']}</span>", unsafe_allow_html=True)
        
        st.markdown(f"<div class='trait-box'><b>💡 주요 특징:</b> {data['traits']}</div>", unsafe_allow_html=True)

    # Detailed Compatibility Reasons Section
    st.markdown("<h3 style='color: #ffe600; font-size: 1.5rem; margin-top: 20px;'>🤝 어울리는 이유</h3>", unsafe_allow_html=True)
    
    reasons_html = "<div class='reason-list'><ul>"
    for reason in data["reasons"]:
        reasons_html += f"<li style='margin-bottom: 8px;'>{reason}</li>"
    reasons_html += "</ul></div>"
    
    st.markdown(reasons_html, unsafe_allow_html=True)

    st.success(f"🎉 축하합니다! {selected_mbti} 유형인 당신의 최상의 모험 파트너는 **{data['name_kr']}** 입니다!")

else:
    st.info("💡 위 드롭다운 메뉴에서 MBTI 유형을 선택하면 단짝 포켓몬이 등장합니다!")
```

