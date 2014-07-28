class SearchResult(object):

    def __init__(self, product):
        self._attributes = product
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
