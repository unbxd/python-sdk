from search.response.SearchResult import SearchResult

class SearchResults(object):

    def __init__(self, products):
        self._resultsCount = len(products)
        self._results = []
        for product in products:
            self._results.append(SearchResult(product))

    '''
       @return Number of results
    '''
    def getResultsCount(self):
        return self._resultsCount

    def getAt(self, i):
        if i >= self._resultsCount:
            return None
        return self._results[i]

    '''
       @return List of products. Refer :@link SearchResult
    '''
    def getResults(self):
        return self._results