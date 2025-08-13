# hello_streamlit.py
import streamlit as st
import pandas as pd
from numpy.random import default_rng as rng

# 제목 추가
st.title("🎉 내 첫 번째 Streamlit 앱!")

# 텍스트 추가
st.write("안녕하세요! Streamlit으로 만든 웹 애플리케이션입니다.")

# 버튼 추가
if st.button("클릭해보세요!"):
    st.success("버튼이 클릭되었습니다! 🎊")

st.caption("안녕하세요. 텍스트입니다.")
st.caption("A caption with _italics_ :blue[colors] and emojis :sunglasses:")

st.badge("New")
st.badge("Success", icon=":material/check:", color="green")

st.markdown(
    ":violet-badge[:material/star: Favorite] :orange-badge[⚠️ Needs review] :gray-badge[Deprecated]"
)

st.title("🐦 프롬프트 트위터 v1.1")  # 버전 추가
st.markdown("**유용한 LLM 프롬프트를 공유하는 공간입니다** ✨")  # 이모지 추가
