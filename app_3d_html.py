##### app_3d_html.py
import streamlit as st
from pathlib import Path

st.set_page_config(page_title="대전 3D 표고면", layout="wide")

##### HTML 파일 경로 (레포와 같은 폴더에 있으면 그대로 둡니다)
HTML_PATH = Path("3d_elevation_surface.html")

##### 높이(px)와 스크롤 여부를 조절할 수 있게 옵션 제공
st.title("대전시 지표면 3D 시각화 (HTML 임베드)")
height = st.sidebar.number_input("표시 높이(px)", min_value=400, max_value=2000, value=900, step=50)
scrolling = st.sidebar.checkbox("스크롤 허용", value=True)

if not HTML_PATH.exists():
    st.error(f"HTML 파일을 찾지 못했습니다: {HTML_PATH.resolve()}")
else:
    html_str = HTML_PATH.read_text(encoding="utf-8", errors="ignore")
    st.components.v1.html(html_str, height=height, scrolling=scrolling)
