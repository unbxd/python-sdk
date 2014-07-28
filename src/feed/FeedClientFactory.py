from feed.FeedClient import FeedClient
class FeedClientFactory:
    
    @staticmethod
    def getFeedClient(siteKey, secretKey, secure):
        return FeedClient(siteKey, secretKey, secure)