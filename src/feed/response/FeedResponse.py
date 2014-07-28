from feed.response.FeedFieldError import FeedFieldError
class FeedResponse(object):

    def __init__(self, response):
        self._statusCode = int(response.get("statusCode"))
        self._message = str(response.get("message"))
        self._uploadID = str(response.get("unbxdFileName"))
        self._unknownSchemaFields = response.get("unknownSchemaFields")
        
        if("fieldErrors" in response):
            fieldErrors = response.get("fieldErrors")
            self._fieldErrors = []
            for error in fieldErrors:
                self._fieldErrors.append(FeedFieldError(error))
        
        if(response.get("rowNum") is not None):
            self._rowNum = int(str(response.get("rowNum")))
        
        if(response.get("colNum") is not None):
            self._colNum = int(str(response.get("colNum")))

    def getStatusCode(self):
        return self._statusCode

    def getMessage(self):
        return self._message

    def getUploadID(self):
        return self._uploadID

    def getFieldErrors(self):
        return self._fieldErrors

    def getUnknownSchemaFields(self):
        return self._unknownSchemaFields

    def getRowNum(self):
        return self._rowNum

    def getColNum(self):
        return self._colNum
