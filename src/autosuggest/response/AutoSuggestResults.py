from autosuggest.response.AutoSuggestResultSection import AutoSuggestResultSection
class AutoSuggestResults(object):

    def __init__(self, params):
        self._resultSections = {}
        for result in params:
            type = result.get("doctype")
            if type not in self._resultSections:
                self._resultSections[type] = AutoSuggestResultSection(type)
            
            self._resultSections[type].addResult(result)

    '''
       @return Get response in sections. 
     '''
    def getResultSections(self):
        return self._resultSections

    '''
       @return Get suggestions in buckets
     '''
    def getBuckets(self):
        return self._resultSections.get("IN_FIELD")

    '''
       @return Get Popular products
     '''
    def getPopularProducts(self):
        return self._resultSections.get("POPULAR_PRODUCTS")

    '''
       @return Get suggestions based on keyword
     '''
    def getKeywordSuggestions(self):
        return self._resultSections.get("KEYWORD_SUGGESTION")

    '''
       @return Get Top Queries
     '''
    def getTopQueries(self):
        return self._resultSections.get("TOP_SEARCH_QUERIES")