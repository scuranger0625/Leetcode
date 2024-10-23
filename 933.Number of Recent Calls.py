class RecentCounter:
    def __init__(self):
        self.queue = [0] * 10000  # 固定大小的陣列
        self.start = 0           # 隊頭指標
        self.end = 0             # 隊尾指標

    def ping(self, t: int) -> int:
        # 將新請求加入環狀隊列
        self.queue[self.end] = t
        self.end = (self.end + 1) % 10000
        
        # 移除不在3000毫秒範圍內的請求
        while self.queue[self.start] < t - 3000:
            self.start = (self.start + 1) % 10000
        
        # 返回在範圍內的請求數
        return (self.end - self.start + 10000) % 10000
