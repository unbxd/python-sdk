from search.response.Facet import Facet
from search.response.RangeFacetEntry import RangeFacetEntry

class RangeFacet(Facet):
    
    _gap = 0
    
    def __init__(self, facetName, params):
        super(RangeFacet, self).__init__(facetName, params)
        self._gap = float((params.get("values")).get("gap"))

    def generateEntries(self, values):
        super(RangeFacet, self).generateEntries(values);
        
        self._rangeFacetEntries = []
        for entry in self._facetEntries:
            fromVar = float(entry.getTerm())
            toVar = fromVar + self._gap;
            self._rangeFacetEntries.append(RangeFacetEntry(fromVar, toVar, entry.getCount()))

    def getRangeEntries(self):
        return self._rangeFacetEntries
