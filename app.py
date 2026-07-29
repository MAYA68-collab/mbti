import streamlit as st

# 1. 웹 페이지 기본 설정
st.set_page_config(
    page_title="MBTI 꿈 탐색기 🧩",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. 데이터 정의

# MBTI별 직업 데이터
mbti_jobs = {
    "INTJ": {
        "title": "전략적인 용장 (INTJ) ♟️",
        "jobs": ["💻 소프트웨어 아키텍트", "📊 데이터 과학자", "💼 경영 컨설턴트"],
        "desc": "혼자 깊이 생각하고 치밀한 계획을 세워 문제를 해결하는 데 뛰어난 능력이 있어요!"
    },
    "INTP": {
        "title": "아이디어 창출가 (INTP) 🧪",
        "jobs": ["🖥️ 컴퓨터 프로그래머", "🔬 기초과학 연구원", "🎮 게임 메커닉 기획자"],
        "desc": "호기심이 풍부하고 원리와 이론을 파헤치는 창의적인 탐구자예요!"
    },
    "ENTJ": {
        "title": "대담한 지도자 (ENTJ) 🏛️",
        "jobs": ["🚀 스타트업 CEO", "⚖️ 전문 변호사", "📋 총괄 프로젝트 매니저(PM)"],
        "desc": "목표를 향해 팀을 이끌고 체계적으로 성과를 내는 능력이 탁월해요!"
    },
    "ENTP": {
        "title": "뜨거운 혁신가 (ENTP) 💡",
        "jobs": ["💡 벤처 창업가", "📈 마케팅 크리에이티브 디렉터", "🎬 방송/콘텐츠 PD"],
        "desc": "새로운 것에 끊임없이 도전하고 독창적인 아이디어로 세상을 놀라게 해요!"
    },
    "INFJ": {
        "title": "통찰력 있는 선구자 (INFJ) 🔮",
        "jobs": ["💬 청소년 심리상담사", "✍️ 문학 작가 / 스토리라이터", "🤝 사회복지 기획가"],
        "desc": "다른 사람의 마음을 깊이 이해하고 따뜻한 사회를 만드는 데 가치를 둬요!"
    },
    "INFP": {
        "title": "열정적인 중재자 (INFP) 🎨",
        "jobs": ["🎨 일러스트레이터 / 웹툰 작가", "🎥 미디어 크리에이터", "🗣️ 언어치료사"],
        "desc": "풍부한 감수성과 진정성 있는 표현력으로 세상과 소통하는 아티스트예요!"
    },
    "ENFJ": {
        "title": "정의로운 언변가 (ENFJ) 📢",
        "jobs": ["🏫 진로 진학 교사", "👥 인사(HR) 교육 전문가", "🎙️ 공인 아나운서"],
        "desc": "주변 사람들에게 선한 영향력을 주고 함께 성장하도록 돕는 리더예요!"
    },
    "ENFP": {
        "title": "재발랄한 활동가 (ENFP) 🎈",
        "jobs": ["📝 광고 카피라이터", "🎉 문화 이벤트 기획자", "✈️ 여행 에세이스트"],
        "desc": "열정과 상상력이 넘치며, 사람들에게 즐거움과 에너지를 전해줘요!"
    },
    "ISTJ": {
        "title": "청렴결백한 논리주의자 (ISTJ) 📐",
        "jobs": ["📊 공인회계사", "🏛️ 행정 공무원", "🗄️ 데이터베이스 관리자"],
        "desc": "책임감이 강하고 원칙을 지키며 완벽하게 일을 처리하는 신뢰의 아이콘이에요!"
    },
    "ISFJ": {
        "title": "용감한 수호자 (ISFJ) 🛡️",
        "jobs": ["🩺 전문 간호사", "🧸 유치원 교사", "📚 전문 사서"],
        "desc": "타인을 섬세하게 배려하고 세심한 주의력으로 주변을 묵묵히 지원해요!"
    },
    "ESTJ": {
        "title": "엄격한 관리자 (ESTJ) ⚖️",
        "jobs": ["👮 경찰관 / 수사관", "📉 금융 자산관리사", "🏨 호텔 총지배인"],
        "desc": "질서와 규칙을 바탕으로 조직을 효율적으로 관리하고 이끄는 실천가예요!"
    },
    "ESFJ": {
        "title": "사교적인 외교관 (ESFJ) 🤝",
        "jobs": ["✈️ 항공 승무원", "🍎 초등학교 교사", "🎤 행사 전문 MC"],
        "desc": "친절하고 협동심이 강하며, 타인과의 좋은 관계를 형성하는 데 달인이에요!"
    },
    "ISTP": {
        "title": "만능 재주꾼 (ISTP) 🛠️",
        "jobs": ["🔧 기계 메카트로닉스 엔지니어", "🏎️ 레이싱 카 정비사", "🚑 응급구조사"],
        "desc": "도구를 다루고 실질적인 문제를 순발력 있게 해결하는 데 능숙해요!"
    },
    "ISFP": {
        "title": "호기심 많은 예술가 (ISFP) 🖌️",
        "jobs": ["🖼️ UX/UI 디자이너", "🐾 수의사 테크니션", "📸 감성 사진작가"],
        "desc": "온화하고 예술적인 감각을 지녔으며 자신만의 표현 방식을 소중히 여겨요!"
    },
    "ESTP": {
        "title": "모험을 즐기는 사업가 (ESTP) ⚡",
        "jobs": ["⚽ 스포츠 코치 / 트레이너", "👨‍🚒 소방관", "🤝 현장 영업 전문가"],
        "desc": "에너지 넘치고 관찰력이 뛰어나며 직관적이고 빠르게 행동에 옮겨요!"
    },
    "ESFP": {
        "title": "자유로운 영혼의 연예인 (ESFP) 🌟",
        "jobs": ["🎭 연기자 / 뮤지컬 배우", "👗 패션 스타일리스트", "🗺️ 가이드 / 관광 기획자"],
        "desc": "유쾌하고 분위기를 밝게 만들며 사람들의 시선을 사로잡는 매력이 있어요!"
    }
}

# 한국인 MBTI 비율 데이터 (약 비율 %)
korea_mbti = {
    "ISTJ": 14.7, "ESTJ": 11.2, "ISTP": 9.8, "ISFJ": 8.4,
    "ISFP": 7.3,  "ESTP": 6.8,  "ENFP": 6.5, "ESFP": 6.1,
    "INFP": 5.8,  "ESFJ": 5.4,  "INTP": 4.3, "INFJ": 3.8,
    "ENFJ": 3.5,  "ENTP": 2.8,  "INTJ": 2.3, "ENTJ": 1.3
}

# 3. 메인 화면 헤더
st.title("🧩 MBTI 꿈 탐색기 🧭")
st.caption("청소년 여러분의 성격 유형을 바탕으로 가능성과 적성을 찾아가는 공간입니다 🌟")

# 4. 탭 메뉴 생성 (단일 페이지 내 섹션 구분)
tab1, tab2, tab3 = st.tabs(["🎯 유형별 직업 추천", "📊 MBTI 한국 & 세계 분포", "💡 MBTI 지표 해독기"])

# ==========================================
# TAB 1: MBTI 맞춤 직업 추천
# ==========================================
with tab1:
    st.subheader("🔍 나의 MBTI 유형을 선택해 보세요")
    
    mbti_list = list(mbti_jobs.keys())
    selected_mbti = st.selectbox(
        "드롭다운에서 MBTI를 골라주세요 👇",
        options=["선택하세요..."] + mbti_list,
        index=0
    )

    if selected_mbti != "선택하세요...":
        info = mbti_jobs[selected_mbti]
        
        st.markdown(f"### ✨ **{info['title']}**")
        st.write(f"*{info['desc']}*")
        st.write("")
        
        st.subheader("🎯 추천하는 대표 직업 3가지")
        
        cols = st.columns(3)
        for idx, job in enumerate(info["jobs"]):
            with cols[idx]:
                st.success(f"**{job}**")

        st.divider()
        
        # 한국 비율 매칭 정보
        kor_rank_list = sorted(korea_mbti.items(), key=lambda x: x[1], reverse=True)
        mbti_ranks = [item[0] for item in kor_rank_list]
        rank = mbti_ranks.index(selected_mbti) + 1
        pct = korea_mbti[selected_mbti]
        
        st.metric(
            label=f"🇰🇷 대한민국 내 [{selected_mbti}] 비율 및 순위",
            value=f"{pct}%",
            delta=f"16개 유형 중 {rank}위"
        )

        st.info(
            f"💡 **상담가의 한마디**\n\n"
            f"**{selected_mbti}** 유형은 한국인 중 **{rank}번째({pct}%)**로 자주 만날 수 있는 유형이에요.\n"
            f"MBTI는 여러분의 성향을 이해하는 징검다리일 뿐! 흥미와 가치관을 더해 나만의 멋진 진로를 그려보세요 💪"
        )
    else:
        st.warning("👆 위 드롭다운 목록에서 자신의 MBTI를 선택해주세요!")

# ==========================================
# TAB 2: MBTI 분포 및 통계
# ==========================================
with tab2:
    st.subheader("🇰🇷 대한민국 MBTI 유형 분포")
    st.write("우리나라 사람들은 어떤 MBTI 유형이 가장 많을까요? (일반 통계 기준)")
    
    # 한국 MBTI 차트
    st.bar_chart(korea_mbti)
    
    st.divider()
    
    st.subheader("🌍 나라별 MBTI 대표 특징 & 분포 경향")
    st.markdown("""
    - **🇰🇷 대한민국**: 규칙과 실용성을 중시하는 **ISTJ, ESTJ, ISTP** 비율이 비교적 높게 나타납니다.
    - **🇺🇸 미국**: 외향적이고 개성을 중시하는 **ENFP, ESFP, ESTP** 등 E(외향) 성향이 상대적으로 활발합니다.
    - **🇯🇵 일본**: 타인을 배려하고 조화를 중시하는 **ISFJ, INFJ** 등 내향/감정형 비율이 다수를 차지합니다.
    - **🇩🇪 독일**: 체계적이고 아날로그적 정확성을 선호하는 **ISTJ, INTJ** 비율이 안정적으로 높습니다.
    """)
    
    st.caption("※ MBTI 통계는 표본 조사 대상 및 시기에 따라 차이가 있을 수 있습니다.")

# ==========================================
# TAB 3: 추가 기능 - MBTI 4가지 지표 해독기
# ==========================================
with tab3:
    st.subheader("🧠 MBTI 4가지 알파벳 지표 이해하기")
    st.write("각 알파벳이 의미하는 바를 알면 나의 장점과 보완점을 더 깊이 알 수 있어요!")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🔋 에너지 방향")
        st.caption("**E (외향)**: 외부 세계와 사람과의 만남에서 에너지를 얻음")
        st.caption("**I (내향)**: 혼자만의 시간과 내면 깊은 생각에서 에너지를 얻음")
        
        st.markdown("### 🧠 정보 수집 (인식)")
        st.caption("**S (감각)**: 오감, 직접 체험, 구체적인 사실과 현상에 집중")
        st.caption("**N (직관)**: 영감, 가능성, 전체적인 나무보다 숲을 보는 통찰")

    with col2:
        st.markdown("### ⚖️ 판단 기준")
        st.caption("**T (사고)**: 논리, 원리원칙, 객관적인 사실 기반 판단")
        st.caption("**F (감정)**: 인간관계, 공감, 상황과 사람의 가치 기반 판단")
        
        st.markdown("### 🧭 생활 양식")
        st.caption("**J (판단)**: 체계적, 치밀한 계획, 확실한 기한과 정리정돈")
        st.caption("**P (인식)**: 자율적, 융통성, 유연한 상황 대응과 호기심")

    st.divider()
    
    st.success("🌟 **진로 상담 팁**: 내가 잘하는 것(적성)과 좋아하는 것(흥미)이 만나는 지점이 여러분의 진짜 꿈입니다!")

# 하단 공통 푸터
st.caption("---")
st.caption("💚 청소년 진로 및 고민 상담 | MBTI 꿈 탐색 프로젝트 🧠")