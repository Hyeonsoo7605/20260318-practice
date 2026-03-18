import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Streamlit Elements Demo", layout="wide")

st.title("🎨 Streamlit 기본 요소 데모")
st.markdown("Streamlit에서 지원하는 주요 UI 요소를 한 곳에서 확인할 수 있는 예제 페이지입니다.")

st.header("1. 텍스트 & 마크다운")
st.write("일반 텍스트")
st.markdown("**강조된 텍스트**와 _기울임_ 및 [링크](https://streamlit.io)")
st.code("print('Hello Streamlit')", language='python')

st.header("2. 데이터 표현")

df = pd.DataFrame({
    "이름": ["철수", "영희", "민수", "지영"],
    "나이": [25, 30, 22, 28],
    "점수": [88, 92, 75, 85],
})
st.dataframe(df)
st.table(df)

st.subheader("3. 차트")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.line_chart(chart_data)
st.bar_chart(chart_data)

st.subheader("4. 위젯")
name = st.text_input("이름 입력")
age = st.number_input("나이", min_value=0, max_value=120, value=20)
color = st.selectbox("선호 색상", ["빨강", "초록", "파랑"])
agree = st.checkbox("동의합니다")
option = st.radio("옵션 선택", ["옵션 A", "옵션 B", "옵션 C"])

if st.button("전송"):
    st.success(f"{name}님, 선택된 값: 나이={age}, 색상={color}, 동의={agree}, 옵션={option}")

st.subheader("5. 레이아웃")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("온도", "20°C", "-1°C")
with col2:
    st.metric("습도", "60%", "+2%")
with col3:
    st.metric("속도", "15km/h", "+3km/h")

with st.expander("숨김 영역(Expander)"):
    st.write("이 공간은 접을 수 있는 영역입니다.")

st.subheader("6. 진척도 및 상태")
progress = st.progress(0)
status_text = st.empty()
for i in range(101):
    progress.progress(i)
    status_text.text(f"진행률: {i}%")

st.header("7. 탭")
with st.tabs(["Tab 1", "Tab 2", "Tab 3"])[0]:
    st.write("첫번째 탭 내용")
with st.tabs(["Tab 1", "Tab 2", "Tab 3"])[1]:
    st.write("두번째 탭 내용")
with st.tabs(["Tab 1", "Tab 2", "Tab 3"])[2]:
    st.write("세번째 탭 내용")

st.sidebar.title("사이드바")
st.sidebar.write("사이드바에 추가 정보나 필터를 넣을 수 있습니다.")
sidebar_slider = st.sidebar.slider("사이드바 슬라이더", 0, 100, 50)
st.sidebar.write(f"선택된 값: {sidebar_slider}")
