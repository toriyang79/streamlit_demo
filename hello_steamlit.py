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

df = pd.DataFrame(rng(0).standard_normal((20, 3)), columns=["a", "b", "c"])

st.area_chart(df)

with st.echo():
    st.write('This code will be printed')
    
st.subheader("_Streamlit_ is :blue[cool] :sunglasses:")
st.subheader("This is a subheader with a divider", divider="gray")
st.subheader("These subheaders have rotating dividers", divider=True)
st.subheader("One", divider=True)
st.subheader("Two", divider=True)
st.subheader("Three", divider=True)
st.subheader("Four", divider=True)