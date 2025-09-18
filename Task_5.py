class RecentCounter:
    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        self.requests.append(t)
        while self.requests[0] < t - 3000:
            self.requests.pop(0)
        return len(self.requests)

recentCounter = RecentCounter()
print(recentCounter.ping(1))     # 1
print(recentCounter.ping(100))   # 2
print(recentCounter.ping(135))  # 3
print(recentCounter.ping(150))  # 3
print(recentCounter.ping(3001))  # 3
print(recentCounter.ping(3002))  # 3