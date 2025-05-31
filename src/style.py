# style.py
# GUI 디자인(색상, 폰트, 크기 등) 관련 설정만 저장

# 색상
PRIMARY_COLOR = "#ff9900"
SECONDARY_COLOR = "#cccccc"
BACKGROUND_COLOR = "#222222"
TEXT_COLOR = "#ffffff"
BUTTON_COLOR = "#ff9900"
BUTTON_TEXT_COLOR = "#ffffff"
BORDER_COLOR = "#888"

# 폰트
FONT_FAMILY = "맑은 고딕, Malgun Gothic, Arial, sans-serif"
FONT_SIZE_LARGE = 24
FONT_SIZE_MEDIUM = 18
FONT_SIZE_SMALL = 15
FONT_SIZE_GRAPH_INFO = 13

# 버튼 스타일
BUTTON_STYLE = f"""
    QPushButton {{
        background-color: {BUTTON_COLOR};
        color: {BUTTON_TEXT_COLOR};
        border-radius: 6px;
        padding: 6px 16px;
        font-family: {FONT_FAMILY};
        font-size: {FONT_SIZE_SMALL}px;
    }}
    QPushButton:hover {{
        background-color: #ffa733;
    }}
"""

# 라벨 스타일
LABEL_STYLE = f"color: {TEXT_COLOR}; font-family: {FONT_FAMILY}; font-size: {FONT_SIZE_MEDIUM}px;"

# 콤보박스 스타일
COMBOBOX_STYLE = f"font-family: {FONT_FAMILY}; font-size: {FONT_SIZE_SMALL}px;"

# 입력창 스타일
LINEEDIT_STYLE = f"font-family: {FONT_FAMILY}; font-size: {FONT_SIZE_SMALL}px;"

# 스핀박스 스타일
SPINBOX_STYLE = f"font-family: {FONT_FAMILY}; font-size: {FONT_SIZE_SMALL}px;"

# 스타일
SIM_LABEL_STYLE = f"background-color: black; color: white; font-size: {FONT_SIZE_SMALL}px; border: 2px solid {BORDER_COLOR}; font-family: {FONT_FAMILY};"
TEXT_EDIT_STYLE = f"background-color: {SECONDARY_COLOR}; font-size: {FONT_SIZE_SMALL}px; border: 2px solid {BORDER_COLOR}; font-family: {FONT_FAMILY};"
GRAPH_LABEL_STYLE = f"background-color: {SECONDARY_COLOR}; font-size: {FONT_SIZE_SMALL}px; border: 2px solid {BORDER_COLOR}; font-family: {FONT_FAMILY};"
GRAPH_INFO_LABEL_STYLE = f"background-color: {SECONDARY_COLOR}; font-size: {FONT_SIZE_GRAPH_INFO}px; border: 2px solid {BORDER_COLOR}; font-family: {FONT_FAMILY};"

# 윈도우 설정
WINDOW_TITLE = "Page Replacement Algorithm Simulator"
WINDOW_WIDTH = 850
WINDOW_HEIGHT = 420
WINDOW_X = 100
WINDOW_Y = 100

BLACK_LABEL_STYLE = f"color: #000000; font-family: {FONT_FAMILY}; font-size: {FONT_SIZE_MEDIUM}px;" 