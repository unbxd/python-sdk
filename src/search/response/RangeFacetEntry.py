from search.response.FacetEntry import FacetEntry
class RangeFacetEntry(FacetEntry):
    def __init__(self, fromVar, toVar, count):
        super(RangeFacetEntry, self).__init__(count);
        self.fromVar = fromVar;
        self.toVar = toVar;
    
    def getFrom(self):
        return self.fromVar
    
    def getTo(self):
        return self.toVar;