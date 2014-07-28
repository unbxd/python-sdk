from recommendations.RecommendationsClient import RecommendationsClient

class RecommendationsClientFactory(object):
    @staticmethod
    def getRecommendationsClient(siteKey, apiKey, secure):
        return RecommendationsClient(siteKey, apiKey, secure);
