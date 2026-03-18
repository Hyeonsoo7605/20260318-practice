import streamlit as st

st.set_page_config(page_title="자기소개 페이지", layout="centered")

st.title("👋 안녕하세요! 자기소개 페이지입니다")

st.subheader("기본 정보")
st.write("- 이름: 홍길동")
st.write("- 직업: 데이터 분석가")
st.write("- 이메일: honggildong@example.com")

st.subheader("소개")
st.markdown("안녕하세요! 저는 **데이터 분석과 머신러닝**을 사랑하는 개발자입니다.\n\n여러 프로젝트에서 시각화, 리스트릭트, 예측 모델을 구축해왔습니다.")

st.subheader("주요 기술")
st.write("- Python (Pandas, NumPy, Scikit-learn)")
st.write("- Streamlit, Dash")
st.write("- SQL, AWS")

st.subheader("관심사")
with st.expander("클릭해서 열기"):
    st.write("데이터 시각화, AI 도구 개발, 생산성 향상 자동화")

st.subheader("간단한 인터랙션")
name = st.text_input("이름을 입력하세요", "홍길동")
message = st.text_area("자기소개 한 줄", "Streamlit으로 만든 간단한 웹 앱에 오신 것을 환영합니다!")

if st.button("제출"):
    st.success(f"{name}님의 자기소개: {message}")

st.sidebar.header("프로필 요약")
st.sidebar.write("- 5년 경력 데이터 분석가")
st.sidebar.write("- 관심 기술: 머신러닝 / 데이터 시각화")
st.sidebar.write("- 개인 프로젝트: 추천 시스템, 자연어 처리")

