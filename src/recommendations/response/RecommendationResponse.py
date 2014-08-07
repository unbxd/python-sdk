from recommendations.response.RecommendationResults import RecommendationResults
class RecommendationResponse:

    def __init__(self, params):
        if params.get("error") is not None:
            self.error = params.get("error")
            self._errorCode = int(self.error.get("code"))
            self._message = str(self.error.get("message"))
        else:
            self._message = "OK"
            
            self._statusCode = int(params.get("status"))
            self._queryTime = int(params.get("queryTime"))
            
            self._totalResultsCount = int(params.get("count"))
            
            if "Recommendations" in params:
                self._results = RecommendationResults(params.get("Recommendations"))

    '''
       @return Status Code. 200 if OK.
    '''
    def getStatusCode(self):
        return self._statusCode

    '''
       @return Error code in case of an error.
    '''
    def getErrorCode(self):
        return self._errorCode

    '''
       @return OK if successfull. Error message otherwise
    '''
    def getMessage(self):
        return self._message

    '''
       @return Time taken to query results in milliseconds
    '''
    def getQueryTime(self):
        return self._queryTime

    '''
       @return Number of results in the response.
    '''
    def getTotalResultsCount(self):
        return self._totalResultsCount

    '''
       @return Results. Refer :@link RecommendationResults
    '''
    def getResults(self):
        return self._results
