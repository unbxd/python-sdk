from recommendations.response.RecommendationResult import RecommendationResult
class RecommendationResults:

    def __init__(self, params):
        self._resultsCount = len(params)
        
        self._results = []
        for result in params:
            self._results.append(RecommendationResult(result))

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
       @return List of products. Refer :@link RecommendationResult}
    '''
    def getResults(self):
        return self._results