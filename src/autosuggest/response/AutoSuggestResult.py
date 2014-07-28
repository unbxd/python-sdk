class AutoSuggestResult(object):
    def __init__(self, params):
        self._attributes = params;

    '''
       @return Attributes of the product
     '''
    def getAttributes(self):
        return self._attributes;

    '''
       @param fieldName
       @return Attribute of the product for given field name
     '''
    def getAttribute(self, fieldName):
        return self._attributes.get(fieldName)

    '''
       @return Get Suggestion
     '''
    def getSuggestion(self):
        return str(self.getAttribute("autosuggest"))