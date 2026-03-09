from collections import defaultdict
import heapq

class Twitter:
    def __init__(self):
        self.count = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        min_heap = []

        self.following[userId].add(userId)
        
        for followeeId in self.following[userId]:
            if followeeId in self.tweets:
                index = len(self.tweets[followeeId]) - 1
                count, tweetId = self.tweets[followeeId][index]
                heapq.heappush(min_heap, [count, tweetId, followeeId, index - 1])

        while min_heap and len(res) < 10:
            count, tweetId, followeeId, idx = heapq.heappop(min_heap)
            res.append(tweetId)
            if idx >= 0:
                count, tweetId = self.tweets[followeeId][idx]
                heapq.heappush(min_heap, [count, tweetId, followeeId, idx - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId] and followerId != followeeId:
            self.following[followerId].remove(followeeId)