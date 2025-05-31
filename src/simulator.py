from algorithms import fifo, lru
from PySide6.QtGui import QColor

class PageReplacementSimulator:
    def __init__(self):
        self.frame_count = 0
        self.reference_string = ""
        self.policy = ""
        self.frame_history = []  # 각 단계별 프레임 상태
        self.color_history = []  # 각 단계별 색상 정보
    
    def set_reference_string(self, ref_string):
        self.reference_string = ref_string.upper()
    
    def set_policy(self, policy_name):
        """사용할 정책을 설정"""
        valid_policies = ["FIFO", "LRU"]
        if policy_name in valid_policies:
            self.policy = policy_name
    
    def set_frame_count(self, count):
        self.frame_count = count
    
    def run_simulation(self):
        self.frame_history = []
        self.color_history = []
        if self.policy == "FIFO":
            frames = []
            frame_states = []
            color_states = []
            result_texts = []
            for idx, page in enumerate(self.reference_string):
                color_col = []
                if page in frames:
                    result_texts.append(f"Data {page} is hit\n")
                    action = 'hit'
                elif len(frames) < self.frame_count:
                    frames.append(page)
                    result_texts.append(f"Data {page} is page fault\n")
                    action = 'fault'
                else:
                    frames.pop(0)
                    frames.append(page)
                    result_texts.append(f"Data {page} migrates\n")
                    action = 'migrates'
                # 현재 프레임 상태 기록
                col = []
                for i in range(self.frame_count):
                    if i < len(frames):
                        col.append(frames[i])
                        # 색상 지정
                        if frames[i] == page:
                            if action == 'fault':
                                color_col.append(QColor("yellow"))
                            elif action == 'hit':
                                color_col.append(QColor("#8fd900"))
                            elif action == 'migrates':
                                color_col.append(QColor("violet"))
                            else:
                                color_col.append(QColor("white"))
                        else:
                            color_col.append(QColor("white"))
                    else:
                        col.append(None)
                        color_col.append(QColor("white"))
                frame_states.append(col)
                color_states.append(color_col)
            self.frame_history = frame_states
            self.color_history = color_states
            return {"frame_count": self.frame_count, "reference_string": self.reference_string, "policy": self.policy, "result": result_texts}
        elif self.policy == "LRU":
            # LRU는 기존대로 pass
            return {"frame_count": self.frame_count, "reference_string": self.reference_string, "policy": self.policy, "result": []}
        else:
            return {"frame_count": self.frame_count, "reference_string": self.reference_string, "policy": self.policy, "result": []} 