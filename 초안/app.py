import streamlit as st
import pandas as pd
import numpy as np

# 페이지 설정
st.set_page_config(
    page_title="영화 취향 찾기",
    page_icon="🍿",
    layout="wide",

)
def show_home():
     #제목과 소개
    st.title('영화 취향 찾기🎥')
    st.markdown('### 나의 인생영화 찾기')

    st.write("""
        영화 퀴즈를 통해 사용자가 평소 선호하는 연출 스타일이나 서사를 분석해 '거장 감독'이나 '인생 영화'를 매칭해드립니다.
        """)

    # 과제 조건: 첫 화면에 학번과 이름 표시
    st.write("사이드바의 메뉴를 이용해 퀴즈를 시작해 주세요!")

    st.divider()

    st.write("과제 제출자 정보")
    st.write(f"**학번:** {st.session_state.user_info['student_id']}")
    st.write(f"**이름:** {st.session_state.user_info['my_name']}")

# 1. 세션 상태 초기화 (지수님의 코드 원리)
if 'user_info' not in st.session_state:
    st.session_state.user_info = {
        'logged_in': False,
        'user_name': '',
        'student_id': '2023321042', # 본인 학번
        'my_name': '이지수',      # 본인 이름
        'quiz_results': []
        }

# 1. 각 페이지 설정 (파일명은 그대로, title만 변경)
# st.Page("파일경로", title="사이드바에 뜰 이름")
home_page = st.Page(show_home, title="홈 화면", default=True)
login_page = st.Page("pages/02_movieList.py", title="Movie")
quiz_page = st.Page("pages/01_Quiz.py", title="Quiz")

# 2. 내비게이션 구성 (사이드바 메뉴 그룹화도 가능합니다)
pg = st.navigation({
    "🍿": [home_page,login_page, quiz_page]
})

# 3. 실행 (이 코드가 있어야 화면이 나타납니다)
pg.run()