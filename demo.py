import pandas as pd
import requests
import streamlit as st 

st.set_page_config(
    page_title="team6 demo",
    page_icon="🛒",
)

st.title('TEAM6 - IMAGE 100:1 DEMO')

if 'answer' not in st.session_state:
    st.session_state['answer'] = 1

if 'isCorrect' not in st.session_state:
    st.session_state['isCorrect'] = 'none'

quiz_num = st.slider('문제를 선택해주세요!', 1, 10)

if quiz_num:
    st.session_state['isCorrect'] = 'none'
    f = open(f"assets/{quiz_num}/q.txt", "r")
    lines = f.readlines()
    quiz_text = lines[0]
    answer = 1 #int(lines[1])
    
    st.subheader(f"Q: {quiz_text}")
    st.session_state['answer'] = answer 

#####################quiz display


col1, col2, col3 = st.columns(3)

with col1:
   st.subheader("1번")
   st.image(f"assets/{quiz_num}/1.png")

with col2:
   st.subheader("2번")
   st.image(f"assets/{quiz_num}/2.png")

with col3:
   st.subheader("3번")
   st.image(f"assets/{quiz_num}/3.png")


col4, col5, col6 = st.columns(3)

with col4:
    if st.button("1번!"):
        if st.session_state["answer"] == 1:
           st.session_state['isCorrect'] = "correct"
        else:
           st.session_state['isCorrect'] = "wrong"

with col5:
    if st.button("2번!"):
        if st.session_state["answer"] == 2:
           st.session_state['isCorrect'] = "correct"
        else:
           st.session_state['isCorrect'] = "wrong"
with col6:
    if st.button("3번!"):
        if st.session_state["answer"] == 3:
           st.session_state['isCorrect'] = "correct"
        else:
           st.session_state['isCorrect'] = "wrong"

if st.session_state['isCorrect'] != "none":
    if st.session_state['isCorrect'] == "correct":
        st.header("정답!!!")
    elif st.session_state['isCorrect'] == "wrong":
        st.header("오답 ㅜㅜ")
        
st.subheader("정답 추론") 
if st.button("추론 시작!"):
    # module run here
    answer = "정답은 ~~~ 입니다."
    st.subheader(f"분석 결과 : answer")
    