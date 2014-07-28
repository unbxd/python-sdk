from autosuggest.response.AutoSuggestResult import AutoSuggestResult

class AutoSuggestResultSection(object):

    _resultsCount = 0
    
    def __init__(self, type):
        self._type = type
        self._results = []

    def addResult(self, params):
        self._results.append(AutoSuggestResult(params))
        self._resultsCount = self._resultsCount + 1

    '''
       @return :@link AutoSuggestType
     '''
    def getType(self):
        return self._type

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
       @return List of Auto suggest results. Refer :@link AutoSuggestResult
     '''
    def getResults(self):
        return self._results