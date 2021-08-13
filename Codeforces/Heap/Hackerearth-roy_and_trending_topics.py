import heapq

N = int(input())
class Topic:
    def __init__(self, ID, new_score, old_score):
        self.ID = ID
        self.new_score = new_score
        self.old_score = old_score
        self.score_diff = new_score - old_score
    def __lt__(self, other):
        return self.score_diff > other.score_diff or (self.score_diff == other.score_diff and self.ID > other.ID)

heap = []
for i in range(N):
    ID, Z, P, L, C, S = map(int, input().split())
    new_score = P*50 + L*5 + C*10 + S*20
    heapq.heappush(heap, Topic(ID, new_score, Z))

for i in range(5):
    topic = heapq.heappop(heap)
    print(topic.ID, topic.new_score)