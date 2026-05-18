class Twitter:

    # solution using max heap
    def __init__(self):
        self.news_feed = defaultdict(list)
        self.follow_set = defaultdict(set)
        self.timestamp = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.news_feed[userId].append((self.timestamp, tweetId))
        self.timestamp += 1        

    def getNewsFeed(self, userId: int) -> List[int]:
        max_heap = []
        feed = []

        # to make sure the user can see their own tweets on their feed
        self.follow_set[userId].add(userId)

        # for each followee, push their most recent tweets into a max heap
        for followeeId in self.follow_set[userId]:
            if followeeId in self.news_feed:
                index = len(self.news_feed[followeeId]) - 1
                timestamp, tweetId = self.news_feed[followeeId][index]
                heapq.heappush_max(max_heap, (timestamp, tweetId, followeeId, index - 1))

        # construct the news feed
        while max_heap and len(feed) < 10:
            # add the most recent tweet
            timestamp, tweetId, followeeId, index = heapq.heappop_max(max_heap)
            feed.append(tweetId)

            # if the followee has older tweets, push the next one into the heap
            if index >= 0:
                timestamp, tweetId = self.news_feed[followeeId][index]
                heapq.heappush_max(max_heap, (timestamp, tweetId, followeeId, index - 1))

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follow_set[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follow_set[followerId].discard(followeeId)
        
