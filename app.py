import streamlit as st
import pandas as pd

# 페이지 설정
st.set_page_config(
    page_title="영화 취향 찾기",
    page_icon="🍿",
    layout="wide",
)

# 세션 상태 초기화 
if 'user_info' not in st.session_state:
    st.session_state.user_info = {
        'logged_in': False,
        'user_name': '',
        'student_id': '2023321042',  # 본인 학번
        'my_name': '이지수',          # 본인 이름
        'quiz_results': None,
        'login_failed': False,
    }

# 홈 화면 함수 
def show_home():
    st.title('영화 취향 찾기 🎥')
    st.markdown('### 나의 인생영화 찾기')
    st.write("""
        영화 퀴즈를 통해 사용자가 평소 선호하는 연출 스타일이나 서사를 분석해
        '거장 감독'이나 '인생 영화'를 매칭해드립니다.
    """)

    st.divider()

    # 로그인 섹션 
    if not st.session_state.user_info['logged_in']:
        st.subheader("🔐 로그인")
        st.write("퀴즈를 시작하려면 이름을 입력해 로그인하세요.")

        with st.form("login_form"):
            name_input = st.text_input("사용자 이름을 입력하세요", placeholder="예: 홍길동")
            submitted = st.form_submit_button("로그인 ▶", use_container_width=True)

            if submitted:
                if name_input.strip():
                    # 로그인 성공
                    st.session_state.user_info['logged_in'] = True
                    st.session_state.user_info['user_name'] = name_input.strip()
                    st.session_state.user_info['login_failed'] = False
                    st.rerun()
                else:
                    # 로그인 실패
                    st.session_state.user_info['login_failed'] = True

        if st.session_state.user_info['login_failed']:
            st.error("❌ 로그인 실패: 이름을 입력해야 합니다.")

    else:
        # 로그인 성공 상태
        st.success(f"{st.session_state.user_info['user_name']}님, 로그인되었습니다!")
        st.write("사이드바의 **Quiz** 메뉴에서 퀴즈를 시작해보세요.")

        if st.button("🚪 로그아웃"):
            st.session_state.user_info['logged_in'] = False
            st.session_state.user_info['user_name'] = ''
            st.session_state.user_info['quiz_results'] = None
            st.rerun()

    st.divider()

    # 제출자 정보 
    st.write("**📋 과제 제출자 정보**")
    st.write(f"**학번:** {st.session_state.user_info['student_id']}")
    st.write(f"**이름:** {st.session_state.user_info['my_name']}")


# 페이지 네비게이션 설정 
home_page = st.Page(show_home, title="홈 화면", default=True)
movie_page = st.Page("pages/02_movieList.py", title="Movie")
quiz_page = st.Page("pages/01_Quiz.py", title="Quiz")

pg = st.navigation({
    "🍿": [home_page, movie_page, quiz_page]
})

pg.run()
