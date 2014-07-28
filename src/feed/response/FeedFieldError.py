class FeedFieldError(object):
    def __init__(self, params):
        self._fieldName = params.get("fieldName")
        self._fieldValue = params.get("fieldValue")
        self._dataType = params.get("dataType")
        self._multivalued = params.get("multiValue") == 'True'
        self._errorCode = int(params.get("errorCode"))
        self._message = params.get("message")

        if(params.get("rowNum") is not None):
            self._rowNum = int(params.get("rowNum"))

        if(params.get("colNum") is not None):
            self._colNum = int(params.get("colNum"))

    def getFieldName(self):
        return self._fieldName

    def getFieldValue(self):
        return self._fieldValue

    def getDataType(self):
        return self._dataType

    def isMultivalued(self):
        return self._multivalued

    def getErrorCode(self):
        return self._errorCode

    def getMessage(self):
        return self._message

    def getRowNum(self):
        return self._rowNum

    def getColNum(self):
        return self._colNum