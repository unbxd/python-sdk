from search.response.Facet import Facet
from search.response.RangeFacet import RangeFacet

class Facets(object):
    def __init__(self, params):
        self._facets = []
        self._facetsMap = {}
        
        for field in params:
            facetParams = params.get(field)
            type = facetParams.get("type")
            
            if type == "facet_fields": 
                facet = Facet(field, facetParams) 
            else:
                facet = RangeFacet(field, facetParams)
            self._facets.append(facet)
            self._facetsMap[field] = facet

    '''
       @return List of {@link Facet
    '''
    def getFacets(self):
        return self._facets

    '''
       @return Map of field --> {@link Facet
    '''
    def getFacetsAsMap(self):
        return self._facetsMap

    '''
       @param facetName
       @return Facet for given field name
    '''
    def getFacet(self, facetName):
        return self._facetsMap.get(facetName)

