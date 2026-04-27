import streamlit as st
import time
import os


# 캐싱 기능
@st.cache_data
def load_quiz_questions():
    return [
        {"q": "1. 영화를 선택할 때 가장 먼저 보는 것은?", "a": "예고편의 압도적인 영상미와 색감", "b": "줄거리 요약의 탄탄한 구성"},
        {"q": "2. 가장 선호하는 연출 스타일은?", "a": "한 장면만 봐도 화보 같은 '미장센'", "b": "대사 한마디가 가슴에 박히는 '각본'"},
        {"q": "3. 영화 속 배경이 당신에게 주는 의미는?", "a": "환상적인 세계관을 보여주는 시각적 장치", "b": "인물의 심리를 대변하는 상징적 장소"},
        {"q": "4. 영화가 끝난 뒤 가장 선호하는 감정은?", "a": "가슴이 뻥 뚫리는 시원함", "b": "가슴 한구석이 아릿해지는 긴 여운"},
        {"q": "5. 주인공의 운명에 대해 당신의 선택은?", "a": "결국 행복해지는 해피엔딩", "b": "현실적인 고통이 담긴 비극"},
        {"q": "6. 눈물 흘리는 영화에 대해 어떻게 생각하나요?", "a": "기분 전환이 필요한데 슬픈 건 피곤해", "b": "슬픔을 통해 정화되는 카타르시스가 좋아"},
        {"q": "7. 영화 중반부, 당신은 어떤 상태인가요?", "a": "화면 속 분위기에 흠뻑 취해 감상한다", "b": "결말이 어떨지 끊임없이 추리한다"},
        {"q": "8. 뒤통수를 때리는 '역대급 반전'에 대해 어떻게 느끼나요?", "a": "적당한 흐름이 좋다", "b": "예측하지 못한 결말일수록 짜릿하다"},
        {"q": "9. 설명되지 않은 '열린 결말'을 만났을 때 당신은?", "a": "찝찝하다, 결론을 내줬으면 좋겠다", "b": "나만의 해석을 덧붙이는 재미가 있다"},
        {"q": "10. 주말에 혼자 영화를 본다면 어떤 장르를?", "a": "화려한 액션이나 블록버스터", "b": "철학적 메시지가 담긴 예술 영화"},
        {"q": "11. 영화의 음악(OST)이 당신에게 미치는 영향은?", "a": "웅장한 사운드가 전율을 줘야 한다", "b": "인물 사이의 고요함도 음악처럼 느껴진다"},
        {"q": "12. 내가 좋아하는 영화를 남들에게 추천할 때 기준은?", "a": "시간 순삭! 정말 재밌어", "b": "보고 나면 인생에 대해 생각하게 될 거야"},
        {"q": "13. 영화의 속도감(호흡) 중 선호하는 것은?", "a": "쉴 틈 없이 몰아치는 빠른 전개", "b": "느리지만 섬세하게 따라가는 전개"},
        {"q": "14. 당신이 생각하는 최고의 명장면은?", "a": "잊을 수 없는 거대한 스케일", "b": "두 인물의 섬세한 눈빛 교환"},
        {"q": "15. 인생 영화를 다시 볼 때 당신은 어떤 부분을 보나요?", "a": "처음 봤을 때의 그 짜릿한 쾌감", "b": "예전에 놓쳤던 숨겨진 복선과 상징"}
    ]

# 결과 상세 데이터 딕셔너리
RESULT_DETAILS = {
    "Type 1": {
        "title": "미장센의 탐닉자",
        "image": "assets/미장센.png",
        "description": "당신은 시각적 황홀경을 즐기는 탐닉자입니다! 색감, 구도, 조명이 완벽한 영화를 볼 때 가장 큰 행복을 느끼시네요.",
        "recommend": "추천 영화: <화양연화>, <그랜드부다페스트호텔>"
    },
    "Type 2": {
        "title": "이성적인 설계자",
        "image": "assets/설계자.png",
        "description": "당신은 치밀한 복선과 반전을 즐기는 브레인 감상자입니다. 감독의 의도를 간파할 때 쾌감을 느끼는 스타일이시군요!",
        "recommend": "추천 영화: <인셉션>, <올드보이>"
    },
    "Type 3": {
        "title": "고독한 휴머니스트",
        "image": "assets/휴머니스트.png",
        "description": "인간의 본질과 슬픔을 사랑하는 따뜻한 영혼의 소유자입니다. 영화가 주는 긴 여운과 감정의 파도를 소중히 여기시네요.",
        "recommend": "추천 영화: <그린북>, <카모메 식당>"
    },
    "Type 4": {
        "title": "에너지 풀파워 모험가",
        "image": "assets/모험가.png",
        "description": "영화는 즐거워야 한다는 주의! 시원한 전개와 확실한 해피엔딩을 통해 일상의 스트레스를 날려버리는 분입니다.",
        "recommend": "추천 영화: <어벤져스>, <극한직업>"
    },
    "Type 5": {
        "title": "아방가르드 큐레이터",
        "image": "assets/큐레이터.png",
        "description": "남들이 찾지 않는 독특하고 실험적인 영화를 선호합니다. 영화의 상징적 의미를 해석하는 안목이 매우 뛰어나시네요!",
        "recommend": "추천 영화: <더 랍스터>, <기생충>"
    }
}

# 세션 상태 초기화
if 'current_step' not in st.session_state:
    st.session_state.current_step = 0
if 'temp_answers' not in st.session_state:
    st.session_state.temp_answers = [None] * 15

# --- UI 시작 ---
st.title("🍿 시네마틱 페르소나 테스트")

# CASE 1: 로그인 안 된 경우
if not st.session_state.user_info['logged_in']:
    st.subheader("테스트를 시작하기 전, 이름을 알려주세요!")
    name_input = st.text_input("사용자 이름")
    if st.button("테스트 시작하기 ▶"):
        if name_input.strip():
            st.session_state.user_info['user_name'] = name_input.strip()
            st.session_state.user_info['logged_in'] = True
            st.session_state.current_step = 0
            st.session_state.temp_answers = [None] * 15
            st.rerun()
        else:
            st.warning("⚠️ 이름을 입력해주세요.")

# CASE 2: 퀴즈 진행
else:
    # ✅ 캐싱된 퀴즈 데이터 로드 (두 번째 호출부터는 캐시에서 즉시 반환)
    questions = load_quiz_questions()
    total_q = len(questions)

    st.info(f"👤 {st.session_state.user_info['user_name']}님, 환영합니다!")

    if st.session_state.current_step < total_q:
        step = st.session_state.current_step
        st.progress((step + 1) / total_q)
        st.write(f"**질문 {step + 1} / {total_q}**")

        item = questions[step]
        st.subheader(item['q'])
        st.write("가장 마음이 가는 선택지를 클릭하세요.")

        if st.button(f"🅰️ {item['a']}", use_container_width=True, key=f"btn_a_{step}"):
            st.session_state.temp_answers[step] = 1
            st.session_state.current_step += 1
            st.rerun()

        if st.button(f"🅱️ {item['b']}", use_container_width=True, key=f"btn_b_{step}"):
            st.session_state.temp_answers[step] = 2
            st.session_state.current_step += 1
            st.rerun()

        st.write("")
        if step > 0:
            if st.button("⬅️ 이전 질문으로", type="secondary"):
                st.session_state.current_step -= 1
                st.rerun()

    # 결과 화면
    else:
        st.balloons()
        total_score = sum(st.session_state.temp_answers)

        if total_score <= 17: res_key = "Type 4"
        elif total_score <= 21: res_key = "Type 1"
        elif total_score <= 25: res_key = "Type 3"
        elif total_score <= 28: res_key = "Type 2"
        else: res_key = "Type 5"

        st.session_state.user_info['quiz_results'] = res_key

        st.success("🎉 당신의 취향은 바로...")
        st.markdown(f"### {st.session_state.user_info['user_name']}님의 시네마틱 페르소나는...")
        st.markdown(f"## **✨ {RESULT_DETAILS[res_key]['title']}**")

        img_path = RESULT_DETAILS[res_key]['image']
        if os.path.exists(img_path):
            st.image(img_path, width=250)

        st.write(RESULT_DETAILS[res_key]['description'])
        st.info(RESULT_DETAILS[res_key]['recommend'])

        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔄 다시 테스트하기", use_container_width=True):
                st.session_state.current_step = 0
                st.session_state.temp_answers = [None] * 15
                st.rerun()
        with col2:
            if st.button("🎬 추천 영화 보러가기", use_container_width=True):
                st.switch_page("pages/02_movieList.py")

st.write('더 많은 추천 영화 리스트는 사이드바의 "Movie" 페이지에서 확인하세요!')

import os
