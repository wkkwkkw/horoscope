import streamlit as st
import random
from datetime import datetime
import pytz

# 페이지 설정 (귀여운 아이콘과 제목)
st.set_page_config(page_title="뽀쟉 오늘의 운세", page_icon="🐾", layout="centered")

# 귀여운 폰트와 파스텔톤 UI를 위한 커스텀 CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Jua&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Jua', sans-serif;
    }

    /* 제목 색상 변경 */
    h1, h2, h3 {
        color: #FF8BA7 !important;
    }

    /* 버튼 스타일 변경 (둥글고 귀엽게) */
    .stButton>button {
        background-color: #FFC6C7;
        color: #4A4A4A;
        border-radius: 30px;
        border: 2px dashed #FF8BA7;
        font-size: 20px;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #FF8BA7;
        color: white;
        border: 2px solid #FF8BA7;
        transform: scale(1.05);
    }

    /* 선택 박스 라벨 색상 */
    .stSelectbox label {
        color: #FF8BA7;
        font-size: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# 한국 시간 기준 오늘 날짜 구하기
korea_tz = pytz.timezone('Asia/Seoul')
today = datetime.now(korea_tz)
date_str = today.strftime("%Y%m%d")

# 헤더 부분
st.markdown("<h1 style='text-align: center;'>🐾 뽀쟉뽀쟉 오늘의 운세 🐾</h1>", unsafe_allow_html=True)
st.markdown(
    f"<p style='text-align: center; color: #8C8C8C; font-size: 18px;'>{today.strftime('%Y년 %m월 %d일')}, 오늘 하루는 어떨까요? 몽글몽글한 마음으로 확인해봐요! 🌷</p>",
    unsafe_allow_html=True)

# 12지신 띠 목록 (더 귀여운 동물 이모지로)
zodiac_signs = [
    "🐭 찎찎 쥐띠", "🐮 음메 소띠", "🐯 어흥 호랑이띠", "🐰 깡총 토끼띠",
    "🐲 크앙 용띠", "🐍 스르륵 뱀띠", "🐴 다그닥 말띠", "🐑 메에 양띠",
    "🐵 우끼끼 원숭이띠", "🐔 꼬끼오 닭띠", "🐶 멍멍 개띠", "🐷 꿀꿀 돼지띠"
]

st.write("---")
# 띠 선택
selected_zodiac = st.selectbox("✨ 나의 귀여운 띠를 골라주세요!", zodiac_signs)

# 귀여운 말투의 운세 데이터 풀
general_fortunes = [
    "오늘은 운수대통! 맛있는 간식을 먹게 될지도 몰라요 츄베릅 😋🍰",
    "이불 밖은 위험해요! 오늘은 무리하지 말고 뒹굴뒹굴 쉬어가는 건 어떨까요? 🛌💤",
    "우와! 생각지도 못한 깜짝 선물이 찾아올 수 있는 반짝반짝한 하루예요 ✨🎁",
    "조금 뾰로통해질 수 있는 날이에요. 달콤한 초콜릿으로 기분을 달래보아요 🍫🥺",
    "활기찬 하루! 밀려있던 일들이 호다닥 끝날 거예요. 최고최고! 👍🚀",
    "오늘은 주변 사람들에게 예쁜 말을 건네보아요. 행운이 두 배로 돌아올 거예요 💌💕"
]

love_fortunes = [
    "두근두근! 심장이 콩닥거리는 기분 좋은 만남이 기다려요 🥰",
    "가까운 사람과 도란도란 이야기를 나누기 딱 좋은 날이에요 ☕️💬",
    "오늘은 내가 먼저 찡긋! 윙크하며 인사해보는 건 어때요? 😉💖",
    "작은 오해가 생길 수 있어요. '미안해'라는 마법의 단어를 기억해요 🥺🪄"
]

wealth_fortunes = [
    "길 가다가 백 원이라도 주울 수 있는 날! 럭키비키잖아? 🍀💰",
    "텅~장 주의보! 귀여운 쓰레기를 사고 싶어도 오늘은 꾹 참아보아요 🛒❌",
    "지갑이 빵빵해질 기운이 스멀스멀~ 기분 좋은 소식이 들려올 거예요 💸🐷",
    "오늘은 차곡차곡 저금통에 밥을 주는 날이에요 짤랑짤랑 🪙🏦"
]

colors = ["딸기우유 핑크 🍓", "하늘하늘 소라색 ☁️", "병아리 노란색 🐥", "청포도 초록색 🍇", "보송보송 하얀색 ☁️", "라벤더 보라색 💜", "오렌지 귤색 🍊"]

st.write("")  # 여백

# 운세 보기 버튼
if st.button("🔮 두구두구... 오늘의 운세 보기! 🔮", use_container_width=True):
    # 날짜와 띠를 조합하여 시드 고정
    seed_value = date_str + selected_zodiac
    random.seed(seed_value)

    # 랜덤 운세 추출
    general = random.choice(general_fortunes)
    love = random.choice(love_fortunes)
    wealth = random.choice(wealth_fortunes)
    lucky_number = random.randint(1, 99)
    lucky_color = random.choice(colors)

    # 로딩 애니메이션 같은 효과 (실제로는 바로 나옴)
    st.toast("운세 요정이 별가루를 뿌리는 중... ✨")

    # 결과 출력
    st.divider()
    st.markdown(f"<h3 style='text-align: center;'>🎊 {selected_zodiac}의 운세 도착! 🎊</h3>", unsafe_allow_html=True)

    # 귀여운 알림창으로 표시
    st.info(f"🌈 **오늘의 총운:**\n\n {general}", icon="🌟")
    st.error(f"💘 **오늘의 애정운:**\n\n {love}", icon="💖")
    st.success(f"🍯 **오늘의 재물운:**\n\n {wealth}", icon="🪙")

    # 행운의 요소
    st.write("---")
    st.markdown("<h4 style='text-align: center; color: #FF8BA7;'>🍀 당신을 지켜줄 행운의 아이템 🍀</h4>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <div style="background-color: #FFF0F5; padding: 20px; border-radius: 20px; text-align: center; border: 2px dashed #FFB6C1;">
            <div style="font-size: 20px;">🎲 행운의 숫자</div>
            <div style="font-size: 40px; color: #FF69B4; font-weight: bold;">{lucky_number}</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div style="background-color: #F0F8FF; padding: 20px; border-radius: 20px; text-align: center; border: 2px dashed #87CEFA;">
            <div style="font-size: 20px;">🎨 행운의 색깔</div>
            <div style="font-size: 30px; color: #4682B4; font-weight: bold; margin-top: 10px;">{lucky_color}</div>
        </div>
        """, unsafe_allow_html=True)

    st.balloons()  # 축하 풍선 이펙트!