class MedianFinder:

    def __init__(self):
        # maxHeap：左邊最大堆（用負數實現）
        self.maxHeap = []
        # minHeap：右邊最小堆
        self.minHeap = []

    def addNum(self, num: int) -> None:
        # 先加進 maxHeap（負值模擬最大堆）
        heapq.heappush(self.maxHeap, -num)

        # 將最大堆堆頂元素轉移到最小堆，保持順序性
        heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

        # 若 minHeap 比 maxHeap 多元素，調整回平衡（最多只差 1）
        if len(self.minHeap) > len(self.maxHeap):
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap):
            # 偶數個元素，取兩堆堆頂平均
            return (-self.maxHeap[0] + self.minHeap[0]) / 2.0
        else:
            # 奇數個，maxHeap 多一個，中位數為其堆頂
            return -self.maxHeap[0]
