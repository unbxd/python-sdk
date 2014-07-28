from search.response.SearchResults import SearchResults

class BucketResult(object):
    def __init__(self, params):
        self._totalResultsCount = int(params.get("numberOfProducts"));
        self._results = SearchResults(params.get("products"));

    '''
       @return Total number of results found.
    '''
    def getTotalResultsCount(self):
        return self._totalResultsCount;

    '''
       @return Results in self bucket. Refer :@link SearchResults
    '''
    def getResults(self):
        return self._results;

