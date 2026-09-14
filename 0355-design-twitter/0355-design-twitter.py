from collections import defaultdict

class Twitter:

    def __init__(self):
        self.time = 0
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.time, tweetId])
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:

        users = [userId] + list(self.following[userId])

        fyp = []

        for x in users:
            fyp.extend(self.tweets[x])

        fyp = sorted(fyp, key= lambda x: x[0], reverse= True)

        ans = []

        for x in fyp:
            ans.append(x[1])

        return ans[:10]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)