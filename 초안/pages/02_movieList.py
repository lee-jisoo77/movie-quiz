import streamlit as st
import os

RESULT_DETAILS = {
    "Type 1": {
        "title": "미장센의 탐닉자",
        "image1": "assets/hawyang.jpg",
        "image2": "assets/grandhotel.jpg",
        "description": "당신은 시각적 황홀경을 즐기는 탐닉자입니다! 색감, 구도, 조명이 완벽한 영화를 찾고 계신다면 이런 영화를 추천합니다.",
        "recommend1": "<화양연화>",
        "explain1": "왕가위 감독의 1960년대 홍콩의 공기를 담은 탐미적인 연출과 금지된 사랑의 여운을 담은 예술 영화.",
        "recommend2": "<그랜드부다페스트호텔>",
        "explain2": "웨스 앤더슨 감독의 대칭적 구도와 파스텔톤의 화려한 색감이 돋보이는 시각적 향연과 유머가 가득한 모험극." 

    },
    "Type 2": {
        "title": "이성적인 설계자",
        "image1": "assets/insepsion.jpg",
        "image2": "assets/oldboy.jpg",
        "description": "당신은 치밀한 복선과 반전을 즐기는 브레인 감상자입니다. 감독의 의도를 간파할 때 쾌감을 느끼는 스타일이시군요!",
        "recommend1": "<인셉션>",
        "explain1": "크리스토퍼 놀란 감독의 꿈과 현실이 뒤섞이는 복잡한 구조와 충격적인 반전이 돋보이는 SF 액션 스릴러.",
        "recommend2": "<올드보이>",
        "explain2": "박찬욱 감독이 그린 15년 동안의 감금으로 시작하는 처절한 복수극, 한국 영화의 위상을 세계에 알린 강렬한 누아르."
    },
    "Type 3": {
        "title": "고독한 휴머니스트",
        "image1": "assets/greenbook.jpg",
        "image2": "assets/camome.jpg",
        "description": "인간의 본질과 슬픔을 사랑하는 따뜻한 영혼의 소유자입니다. 영화가 주는 긴 여운과 감정의 파도를 소중히 여기시네요.",
        "recommend1": "<그린북>",
        "explain1": "1960년대 미국, 인종차별이 심한 남부로 연주 여행을 떠난 두 남자의 특별하고 따뜻한 우정. 피터 패럴리 감독의 휴머니즘이 돋보이는 영화.",
        "recommend2": "<카모메 식당>",
        "explain2": "핀란드 헬싱키의 작은 일식당에서 일어나는 일상의 소소한 행복과 인간관계의 복잡함을 담은 따뜻한 스토리. 오기구아미 나오코 감독의 섬세한 연출이 돋보이는 영화."
    },	 
    "Type 4": {
        "title": "에너지 풀파워 모험가",
        "image1": "assets/avengers.jpg",
        "image2": "assets/hardwork.jpg",
        "description": "영화는 즐거워야 한다는 주의! 시원한 전개와 확실한 해피엔딩을 통해 일상의 스트레스를 날려버리는 분입니다.",
        "recommend1": "<어벤져스>",
        "explain1": "마블 시네마틱 유니버스의 히어로들이 모여 펼치는 화려한 액션이 가득한 블록버스터. 조스 웨던 감독의 유머와 스펙터클이 돋보이는 영화.",
        "recommend2": "<극한직업>",
        "explain2": "해체 위기의 마약반이 위장 창업한 치킨집이 맛집으로 등극하며 벌어지는 코믹 수사극. 이병헌 감독 특유의 코미디와 액션이 돋보이는 영화."
    },
    "Type 5": {
        "title": "아방가르드 큐레이터",
        "image1": "assets/memento.jpg",
        "image2": "assets/murder.jpg",
        "description": "남들이 찾지 않는 독특하고 실험적인 영화를 선호합니다. 영화의 상징적 의미를 해석하는 안목이 매우 뛰어나시네요!",
        "recommend1": "<메멘토>",
        "explain1": "크리스토퍼 놀란 감독의 10분마다 기억을 잃는 남자가 아내의 살인범을 쫓는 과정을 역순으로 구성한 혁신적 스릴러.",
        "recommend2": "<살인의 추억>",
        "explain2": "80년대 화성 연쇄 살인 사건을 배경으로, 투박한 형사들의 집념과 시대의 아픔을 담은 걸작. 봉준호 감독의 치밀한 서사와 강렬한 감정 연출이 돋보이는 영화."
    }
}

st.title("추천 영화 리스트 🎞️")

if res_key := st.session_state.user_info.get('quiz_results'):
    details = RESULT_DETAILS.get(res_key)
    if details:
        st.subheader(f"{st.session_state.user_info['user_name']}님은 {details['title']}입니다.")
        st.markdown(f"### {details['description']}")

        st.markdown(f"### {details['recommend1']}")
        st.image(details['image1'], width=300)  
        st.write(details['explain1'])

        st.markdown(f"### {details['recommend2']}")
        st.image(details['image2'], width=300)        
        st.write(details['explain2'])

else:
    st.warning("퀴즈를 풀고 오시면 본인에게 딱 맞는 결과를 먼저 확인하실 수 있어요!")

st.divider()

# 3. 탭 생성 (딕셔너리의 모든 항목을 순회하며 생성)
tab_titles = [RESULT_DETAILS[key]['title'] for key in RESULT_DETAILS]
tabs = st.tabs(tab_titles)

with tabs[0]:
    st.markdown(f"### {RESULT_DETAILS['Type 1']['description']}")
    st.markdown(f"### {RESULT_DETAILS['Type 1']['recommend1']}")
    st.image(RESULT_DETAILS['Type 1']['image1'], width=300)  
    st.write(RESULT_DETAILS['Type 1']['explain1'])
    st.markdown(f"### {RESULT_DETAILS['Type 1']['recommend2']}")
    st.image(RESULT_DETAILS['Type 1']['image2'], width=300)  
    st.write(RESULT_DETAILS['Type 1']['explain2'])

with tabs[1]:
    st.markdown(f"### {RESULT_DETAILS['Type 2']['description']}")
    st.markdown(f"### {RESULT_DETAILS['Type 2']['recommend1']}")
    st.image(RESULT_DETAILS['Type 2']['image1'], width=300)  
    st.write(RESULT_DETAILS['Type 2']['explain1'])
    st.markdown(f"### {RESULT_DETAILS['Type 2']['recommend2']}")
    st.image(RESULT_DETAILS['Type 2']['image2'], width=300)  
    st.write(RESULT_DETAILS['Type 2']['explain2'])  

with tabs[2]:
    st.markdown(f"### {RESULT_DETAILS['Type 3']['description']}")
    st.markdown(f"### {RESULT_DETAILS['Type 3']['recommend1']}")
    st.image(RESULT_DETAILS['Type 3']['image1'], width=300)  
    st.write(RESULT_DETAILS['Type 3']['explain1'])
    st.markdown(f"### {RESULT_DETAILS['Type 3']['recommend2']}")
    st.image(RESULT_DETAILS['Type 3']['image2'], width=300)  
    st.write(RESULT_DETAILS['Type 3']['explain2'])  

with tabs[3]:
    st.markdown(f"### {RESULT_DETAILS['Type 4']['description']}")
    st.markdown(f"### {RESULT_DETAILS['Type 4']['recommend1']}")
    st.image(RESULT_DETAILS['Type 4']['image1'], width=300)  
    st.write(RESULT_DETAILS['Type 4']['explain1'])
    st.markdown(f"### {RESULT_DETAILS['Type 4']['recommend2']}")
    st.image(RESULT_DETAILS['Type 4']['image2'], width=300)  
    st.write(RESULT_DETAILS['Type 4']['explain2'])

with tabs[4]:
    st.markdown(f"### {RESULT_DETAILS['Type 5']['description']}")
    st.markdown(f"### {RESULT_DETAILS['Type 5']['recommend1']}")
    st.image(RESULT_DETAILS['Type 5']['image1'], width=300)  
    st.write(RESULT_DETAILS['Type 5']['explain1'])
    st.markdown(f"### {RESULT_DETAILS['Type 5']['recommend2']}")
    st.image(RESULT_DETAILS['Type 5']['image2'], width=300)  
    st.write(RESULT_DETAILS['Type 5']['explain2'])  

