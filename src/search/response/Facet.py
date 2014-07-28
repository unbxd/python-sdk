from search.response.FacetEntry import FacetEntry

class Facet(object):
    def __init__(self, facetName, params):
        self.name = facetName
        self._type = params.get("type")
        
        if isinstance(params.get("values"), dict):
            map = params.get("values")
            self.generateEntries(map.get("counts"))
        else:
            self.generateEntries(params.get("values"))

    '''
       @return Facet name
     '''
    def getName(self):
        return self.name

    '''
       @return Type of facet
     '''
    def getType(self):
        return self._type

    def generateEntries(self, values):
        self._facetEntries = []
        term = None
        
        for i in range(0, len(values)):
            if(i % 2 == 0):
                term = str(values[i])
            else:
                count = int(values[i])
                self._facetEntries.append(FacetEntry(term, count))

    '''
       @return List of :@link FacetEntry
     '''
    def getEntries(self):
        return self._facetEntries
    
    