class FeedProduct:
    
    ''' Unique Id of the product. Generally corresponds to the SKU. '''
    
    '''
       @param uniqueId
       @param attributes
    '''
    def __init__(self, uniqueId, attributes):
        if attributes is None:
            attributes = {}
        attributes["uniqueId"] = uniqueId
        
        self._attributes = attributes
        self._associatedDocuments = []
        self.uniqueId = uniqueId

    '''
       @return Unique Id of the product
    '''
    def getUniqueId(self):
        return self.uniqueId

    '''
       @return Product Attributes
    '''
    def getAttributes(self):
        return self._attributes

    '''
       @return get list of associated products
    '''
    def getAssociatedProducts(self):
        return self._associatedDocuments

    '''
       adds the associated product to the list.
    '''
    def addAssociatedProduct(self, product):
        self._associatedDocuments.append(product)

    '''
       @param key
       @return Attribute of the product
    '''
    def get(self, key):
        return self._attributes[key]

    def __str__(self):
        ret = "Attributes : " + str(self._attributes) 
        ret += ", Associated Documents : " + str(self._associatedDocuments) 
        ret += ", UniqueId" + str(self.uniqueId)
        return ret
