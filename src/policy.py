class Policy:
    def __init__(self):
        self.available_policies = ["FIFO", "LRU"]
    
    def get_policies(self):
        return self.available_policies