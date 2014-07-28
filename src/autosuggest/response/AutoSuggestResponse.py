from autosuggest.response.AutoSuggestResults import AutoSuggestResults

class AutoSuggestResponse:
    _errorCode = 0
    _results = None
    
    def __init__(self, params):
        if "error" in params:
            error = params.get("error")
            self._errorCode = int(error.get("code"))
            self._message = str(error.get("msg"))
        else :
            self._message = "OK"

            metaData = params.get("searchMetaData")

            self._statusCode = int(metaData.get("status"))
            self._queryTime = int(metaData.get("queryTime"))

            if "response" in params:
                response = params.get("response")
                self._totalResultsCount = int(response.get("numberOfProducts"))
                self._results = AutoSuggestResults(response.get("products"));

    '''
       @return Status Code. 200 if OK.
    '''
    def getStatusCode(self):
        return self._statusCode;

    '''
     @return Error code in case of an error.
    '''
    def getErrorCode(self):
        return self._errorCode;

    '''
     @return OK if successfull. Error message otherwise
    '''
    def getMessage(self):
        return self._message;

    '''
     @return Time taken to query results in milliseconds
    '''
    def getQueryTime(self):
        return self._queryTime;

    '''
     @return Total number of results found.
    '''
    def getTotalResultsCount(self):
        return self._totalResultsCount;

    '''
     @return Results. Refer :@link AutoSuggestResults
    '''
    def getResults(self):
        return self._results;
