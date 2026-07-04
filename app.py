import streamlit as st
import time
from datetime import datetime

# 페이지 설정
st.set_page_config(page_title="감성 시계", page_icon="⏰")

# 폰트 + 스타일
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Gaegu:wght@400;700&display=swap" rel="stylesheet">

<style>
.stApp {
    background: linear-gradient(135deg, #ffd6e8, #cdb4ff);
    font-family: 'Gaegu', cursive;
}

/* 글래스 카드 */
.card {
    background: rgba(255, 255, 255, 0.25);
    backdrop-filter: blur(15px);
    border-radius: 30px;
    padding: 60px 40px;
    text-align: center;
    box-shadow: 0 8px 30px rgba(0,0,0,0.15);
    width: 60%;
    margin: auto;
    margin-top: 10%;
    transition: 0.3s;
}

.card:hover {
    transform: translateY(-5px);
}

/* 시계 텍스트 */
.time {
    font-size: 80px;
    color: #ffffff;
    text-shadow: 0 0 10px rgba(255,255,255,0.8),
                 0 0 20px rgba(255,182,255,0.6);
    letter-spacing: 2px;
}

/* 서브 텍스트 */
.sub {
    font-size: 20px;
    color: rgba(255,255,255,0.8);
    margin-top: 10px;
}
</style>
""", unsafe_allow_html=True)


st.markdown("<div class='card'>", unsafe_allow_html=True)

placeholder = st.empty()

while True:
    now = datetime.now().strftime("%H:%M:%S")

    placeholder.markdown(f"""
        <div class='time'>{now}</div>
        <div class='sub'>오늘도 좋은 하루 보내요 🌷</div>
    """, unsafe_allow_html=True)

    time.sleep(1)
