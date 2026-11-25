"""
post
follow unfollow
view 10 most recent

users and tweets have IDs
"""
class Twitter:

    def __init__(self):
        self.time = 0
        self.user_posts = defaultdict(list)
        self.user_followers = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_posts[userId].append((self.time, tweetId))
        self.time += 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        feed = self.user_posts[userId][:]
        for followeeId in self.user_followers[userId]:
            feed.extend(self.user_posts[followeeId])
        
        feed.sort(key=lambda x: -x[0])
        return [tweetId for _, tweetId in feed[:10]]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.user_followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.user_followers[followerId].discard(followeeId)
