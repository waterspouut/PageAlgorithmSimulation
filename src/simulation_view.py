from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QColor, QPen, QFont
from PySide6.QtCore import Qt

class SimulationView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.reference_string = ""
        self.frames = []  # 2D 리스트: [step][frame]
        self.colors = []  # 2D 리스트: [step][frame] (QColor)
        self.square_size = 40  # px
        self.col_gap = self.square_size // 4
        self.setMinimumHeight(300)
        self.setMinimumWidth(600)
        self.setMaximumHeight(400)
        self.setMaximumWidth(1000)

    def set_simulation_data(self, reference_string, frames, colors):
        self.reference_string = reference_string
        self.frames = frames
        self.colors = colors
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), Qt.black)
        font = QFont("맑은 고딕", 16)
        painter.setFont(font)
        label_height = self.square_size // 2
        label_y = 20  # 기존 값 유지
        frame_top_y = label_y + label_height + (label_height // 4)  # 문자와 프레임 사이 간격 추가
        # 각 열(단계)마다
        for col, ch in enumerate(self.reference_string):
            x = 20 + col * (self.square_size + self.col_gap)
            # 문자 중앙정렬, 프레임과 간격을 두고 아래쪽에 정렬
            painter.setPen(Qt.white)
            painter.drawText(x, label_y, self.square_size, label_height, Qt.AlignHCenter | Qt.AlignBottom, ch)
            # 프레임 세로로
            if col < len(self.frames):
                for row, value in enumerate(self.frames[col]):
                    y = frame_top_y + row * self.square_size
                    painter.setPen(QPen(Qt.white, 2))
                    painter.drawRect(x, y, self.square_size, self.square_size)
                    if value:
                        painter.setPen(QPen(self.colors[col][row]))
                        painter.drawText(x, y, self.square_size, self.square_size, Qt.AlignCenter, str(value)) 