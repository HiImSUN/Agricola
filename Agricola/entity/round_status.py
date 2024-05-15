"""
라운드 상태를 저장하는 클래스
"""


class RoundStatus:
    def __init__(self):
        self.put_basic = [False for i in range(15)]
        self.put_round = [False for i in range(14)]
        self.remain_workers = [0, 0, 0, 0]