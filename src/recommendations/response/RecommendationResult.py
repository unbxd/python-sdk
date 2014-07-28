class RecommendationResult:
    def __init__(self, params):
        self._attributes = params
        self._uniqueId = str(self._attributes.get("uniqueId"))

    '''
      @return Attributes of the product
    '''
    def getAttributes(self):
        return self._attributes

    '''
      @return Unique Id of the product
    '''
    def getUniqueId(self):
        return self._uniqueId

    '''
      @param fieldName
      @return Attribute of the product for given field name
    '''
    def getAttribute(self, fieldName):
        return self._attributes.get(fieldName)
