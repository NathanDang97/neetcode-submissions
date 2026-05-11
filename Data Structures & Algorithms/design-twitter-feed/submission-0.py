class Twitter:

    # solution using sorting 
    def __init__(self):
        self.news_feed = defaultdict(list)
        self.follow_set = defaultdict(set)
        self.timestamp = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.news_feed[userId].append((self.timestamp, tweetId))
        self.timestamp += 1        

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = self.news_feed[userId][:]
        for followeeId in self.follow_set[userId]:
            feed.extend(self.news_feed[followeeId])

        feed.sort(key=lambda x: -x[0])
        return [tweetId for _, tweetId in feed[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follow_set[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follow_set[followerId].discard(followeeId)
        
