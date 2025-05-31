import sys
from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QComboBox, QLineEdit, QSpinBox, QTextEdit, QApplication, QScrollArea)
from PySide6.QtCore import Qt
from style import (
    BUTTON_STYLE, LABEL_STYLE, BLACK_LABEL_STYLE, COMBOBOX_STYLE, LINEEDIT_STYLE, SPINBOX_STYLE,
    SIM_LABEL_STYLE, TEXT_EDIT_STYLE, GRAPH_LABEL_STYLE, GRAPH_INFO_LABEL_STYLE,
    WINDOW_TITLE, WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_X, WINDOW_Y
)
from policy import Policy
from random_generator import RandomGenerator
from simulator import PageReplacementSimulator
from simulation_view import SimulationView
import matplotlib.pyplot as plt
from PySide6.QtGui import QPixmap
from io import BytesIO

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(WINDOW_TITLE)
        self.setGeometry(WINDOW_X, WINDOW_Y, WINDOW_WIDTH, WINDOW_HEIGHT)

        # Initialize components
        self.policy_manager = Policy()
        self.random_generator = RandomGenerator()
        self.simulator = PageReplacementSimulator()

        # 상단 입력부
        top_layout = QHBoxLayout()
        policy_label = QLabel("Policy:")
        policy_label.setStyleSheet(BLACK_LABEL_STYLE)
        self.policy_combo = QComboBox()
        self.policy_combo.addItems(self.policy_manager.get_policies())
        self.policy_combo.setStyleSheet(COMBOBOX_STYLE)
        ref_label = QLabel("Reference String:")
        ref_label.setStyleSheet(BLACK_LABEL_STYLE)
        self.ref_input = QLineEdit()
        self.ref_input.setMaxLength(12)
        self.ref_input.setStyleSheet(LINEEDIT_STYLE)
        frame_label = QLabel("#Frame:")
        frame_label.setStyleSheet(BLACK_LABEL_STYLE)
        self.frame_spin = QSpinBox()
        self.frame_spin.setRange(1, 7)
        self.frame_spin.setValue(4)
        self.frame_spin.setStyleSheet(SPINBOX_STYLE)
        random_btn = QPushButton("Random")
        random_btn.setStyleSheet(BUTTON_STYLE)
        random_btn.clicked.connect(self.generate_random_string)
        run_btn = QPushButton("Run")
        run_btn.setStyleSheet(BUTTON_STYLE)
        run_btn.clicked.connect(self.run_simulation)
        top_layout.addWidget(policy_label)
        top_layout.addWidget(self.policy_combo)
        top_layout.addWidget(ref_label)
        top_layout.addWidget(self.ref_input)
        top_layout.addWidget(frame_label)
        top_layout.addWidget(self.frame_spin)
        top_layout.addWidget(random_btn)
        top_layout.addWidget(run_btn)

        # 중앙/하단 레이아웃
        main_layout = QHBoxLayout()
        self.sim_view = SimulationView()
        right_layout = QVBoxLayout()
        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        self.text_edit.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.text_edit.setStyleSheet(TEXT_EDIT_STYLE)
        self.text_edit.setFixedHeight(150)
        self.text_edit.setFixedWidth(200)
        self.graph_label = QLabel()
        self.graph_label.setAlignment(Qt.AlignCenter)
        self.graph_label.setStyleSheet(GRAPH_LABEL_STYLE)
        self.graph_label.setFixedHeight(150)
        self.graph_label.setFixedWidth(200)
        self.graph_info_label = QLabel()
        self.graph_info_label.setAlignment(Qt.AlignCenter)
        self.graph_info_label.setStyleSheet(GRAPH_INFO_LABEL_STYLE)
        right_layout.addWidget(self.text_edit)
        right_layout.addWidget(self.graph_label)
        right_layout.addWidget(self.graph_info_label)
        main_layout.addWidget(self.sim_view, 2)
        main_layout.addLayout(right_layout, 1)

        # 전체 레이아웃
        layout = QVBoxLayout()
        layout.addLayout(top_layout)
        layout.addLayout(main_layout)
        self.setLayout(layout)

    def generate_random_string(self):
        random_string = self.random_generator.generate_string()
        self.ref_input.setText(random_string)

    def run_simulation(self):
        self.simulator.set_policy(self.policy_combo.currentText())
        self.simulator.set_frame_count(self.frame_spin.value())
        self.simulator.set_reference_string(self.ref_input.text())
        result_dict = self.simulator.run_simulation()
        result = result_dict.get('result', [])
        if isinstance(result, list):
            self.text_edit.setText(''.join(result))
        else:
            self.text_edit.setText(str(result))
        # 그래프 그리기
        if isinstance(result, list):
            fault_count = sum('page fault' in line for line in result)
            migrates_count = sum('migrates' in line for line in result)
            hit_count = sum('hit' in line for line in result)
            total_faults = fault_count + migrates_count
            total_hits = hit_count
            sizes = [total_faults, total_hits]
            colors = ['#ff9999','#8fd9b6']
            fig, ax = plt.subplots(figsize=(2,2))
            ax.pie(sizes, labels=None, colors=colors, autopct='%1.1f%%', startangle=90)
            ax.axis('equal')
            buf = BytesIO()
            plt.savefig(buf, format='png', bbox_inches='tight', transparent=True)
            plt.close(fig)
            buf.seek(0)
            qpixmap = QPixmap()
            qpixmap.loadFromData(buf.getvalue())
            self.graph_label.setPixmap(qpixmap)
            self.graph_info_label.setText(f"faults : {total_faults}개, hits : {total_hits}개")
        else:
            self.graph_label.clear()
            self.graph_info_label.clear()
        # 시뮬레이션 프레임 및 색상 정보 생성
        ref_str = self.ref_input.text()
        frame_count = self.frame_spin.value()
        if hasattr(self.simulator, 'frame_history') and hasattr(self.simulator, 'color_history'):
            frames = self.simulator.frame_history
            colors = self.simulator.color_history
        else:
            frames = [[None]*frame_count for _ in ref_str]
            colors = [[QColor("white")]*frame_count for _ in ref_str]
        self.sim_view.set_simulation_data(ref_str, frames, colors) 