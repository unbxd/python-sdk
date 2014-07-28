from search.SearchClient import SearchClient
class SearchClientFactory(object):

    @staticmethod
    def getSearchClient(siteKey, apiKey, secure):
        return SearchClient(siteKey, apiKey, secure)