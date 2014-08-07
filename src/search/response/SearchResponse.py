from search.response.SearchResults import SearchResults
from search.response.BucketResults import BucketResults
from search.response.Facets import Facets
from search.response.Stats import Stats

class SearchResponse(object):

    _errorCode = 0
    _statusCode = 0
    _queryTime = 0
    _results = None
    
    def __init__(self, params):
        if "error" in params:
            error = params.get("error")
            self._errorCode = int(error.get("code"))
            self._message = str(error.get("msg"))
        else:
            self._message = "OK"
            
            metaData = params.get("searchMetaData")
            self._statusCode = int(metaData.get("status"))
            self._queryTime = int(metaData.get("queryTime"))
            
            if "response" in params:
                response = params.get("response")
                self._totalResultsCount = int(response.get("numberOfProducts"))
                self._results = SearchResults(response.get("products"))
            
            if "buckets" in params:
                response = params.get("buckets")
                self._totalResultsCount = str(response.get("totalProducts"))
                self._buckets = BucketResults(response)
            
            if "facets" in params:
                facets = params.get("facets")
                self._facets = Facets(facets)
            
            if "stats" in params:
                stats = params.get("stats")
                self._stats = Stats(stats)
            
            if "didYouMean" in params:
                self._spellCorrections = []
                dym = params.get("didYouMean")
                for suggestion in dym:
                    self._spellCorrections.append(str(suggestion.get("suggestion")))
    
    '''
       @return  Status Code. 200 if OK.
     '''
    def getStatusCode(self):
        return self._statusCode

    '''
       @return Error code in case of an error.
     '''
    def getErrorCode(self):
        return self._errorCode

    '''
       @return OK if successful. Error message otherwise
     '''
    def getMessage(self):
        return self._message

    '''
       @return Time taken to query results in milliseconds
     '''
    def getQueryTime(self):
        return self._queryTime

    '''
       @return Total number of results found.
     '''
    def getTotalResultsCount(self):
        return self._totalResultsCount

    '''
       @return Results. Refer :@link SearchResults
     '''
    def getResults(self):
        return self._results

    '''
       @return Facets. Refer :@link Facets
     '''
    def getFacets(self):
        return self._facets

    '''
       @return Stats. Refer :@link Stats
     '''
    def getStats(self):
        return self._stats

    '''
       @return List of spell corrections in the order of relevance
     '''
    def getSpellCorrections(self):
        return self._spellCorrections

    '''
       @return Bucketed Response. Refer :@link BucketResults
     '''
    def getBuckets(self):
        return self._buckets

