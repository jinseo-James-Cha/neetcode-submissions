from collections import defaultdict
class Twitter:

    def __init__(self):
        self.post_list = []
        self.follow_list = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.follow_list:
            self.follow_list[userId].add(userId)
        
        self.post_list.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.follow_list:
            return []

        user_and_followers = self.follow_list[userId]
        feeds = []
        for user_id, tweet_id in self.post_list[::-1]:
            if user_id in user_and_followers:
                feeds.append(tweet_id)
            
            if len(feeds) == 10:
                break
        return feeds


    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_list[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
            
        if followerId not in self.follow_list:
            return
        
        if followeeId in self.follow_list[followerId]:
            self.follow_list[followerId].remove(followeeId)

