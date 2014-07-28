''' Client class for calling Search APIs '''
import urllib
import requests  # @UnresolvedImport
import json
import collections
from search.response.SearchResponse import SearchResponse
from search.exceptions.SearchException import SearchException

class SearchClient:

    __encoding = "UTF-8"
    categoryIds = None
    bucketField = None
    query = None
    
    def __init__(self, siteKey, apiKey, secure):
        self.siteKey = siteKey
        self.apiKey = apiKey
        self.secure = secure
        
        self.filters = {}
        self.sorts = collections.OrderedDict() # The map needs to be insertion ordered.
        
        self.pageNo = 1
        self.pageSize = 10

    def getSearchUrl(self):
        endPartOfUrl = self.siteKey + ".search.unbxdapi.com/" + self.apiKey + "/search?wt=json"
        return "https://" + endPartOfUrl if self.secure else "http://" + endPartOfUrl

    def getBrowseUrl(self):
        endPartOfUrl = self.siteKey + ".search.unbxdapi.com/" + self.apiKey + "/browse?wt=json"
        return "https://" + endPartOfUrl if self.secure else "http://" + endPartOfUrl

    '''
       Searches for a query and appends the query parameters in the call.
       @param query
       @param queryParams
       @return self
     '''
    def search(self, query, queryParams):
        self.query = query
        self.queryParams = queryParams
        return self

    '''
       Searches for a query, appends the query parameters in the call and responds with bucketed results.
       @param query
       @param bucketField Field on which buckets have to created.
       @param queryParams
       @return self
     '''
    def bucket(self, query, bucketField, queryParams):
        self.query = query
        self.queryParams = queryParams
        self.bucketField = bucketField
        return self

    '''
       Calls for browse query and fetches results for given nodeIds.
       Has to be used when one node has multiple parents. All the node ids will be ANDed
       @param nodeIds
       @param queryParams
       @return self
     '''
    def browse(self, nodeIdList, queryParams):
        if isinstance(nodeIdList, list):
            self.categoryIds = nodeIdList
        else:
            self.categoryIds = []
            self.categoryIds.append(nodeIdList)
        self.queryParams = queryParams
        return self

    '''
       Filters the results
       Values in the same fields are ORed and different fields are ANDed
       @param fieldName
       @param values
       @return self
     '''
    def addFilter(self, fieldName, values):
        self.filters[fieldName] = values
        return self

    '''
       Sorts the results on a field
       @param field
       @param sortDir
       @return self
     '''
    def addSort(self, field, sortDir = "DESC"):
        self.sorts[field] = sortDir
        return self

    '''
       @param pageNo
       @param pageSize
       @return self
     '''
    def setPage(self, pageNo, pageSize):
        self.pageNo = pageNo
        self.pageSize = pageSize
        return self

    def generateUrl(self):
        if self.query is not None and self.categoryIds is not None:
            raise SearchException("Can't set query and node id at the same time")
        
        try:
            sb = ""
            
            if self.query is not None:
                sb += self.getSearchUrl()
                sb += "&q=" + urllib.quote(self.query).encode(SearchClient.__encoding)
                
                if self.bucketField is not None:
                    sb += "&bucket.field=" + urllib.quote(self.bucketField).encode(SearchClient.__encoding)
            elif self.categoryIds is not None and len(self.categoryIds) > 0:
                sb += self.getBrowseUrl()
                sb += "&category-id=" + urllib.quote(",".join(self.categoryIds)).encode(SearchClient.__encoding)
                
            if self.queryParams is not None and len(self.queryParams) > 0:
                for key in self.queryParams:
                    sb += "&" + key + "=" + urllib.quote(self.queryParams.get(key)).encode(SearchClient.__encoding)
                    
            if self.filters is not None and len(self.filters) > 0:
                for key in self.filters:
                    value = self.filters.get(key)
                    sb += "&filter=" + urllib.quote(key + ":\"" + value + "\"").encode(SearchClient.__encoding)
                    
            if self.sorts is not None and len(self.sorts) > 0:
                sorts = []
                for key in self.sorts:
                    sorts.append(key + " " + self.sorts.get(key).lower())
                sb += "&sort=" + urllib.quote(",".join(sorts)).encode(SearchClient.__encoding)
                
            sb += "&pageNumber=" + str(self.pageNo)
            sb += "&rows=" + str(self.pageSize)
            
            return sb
        except Exception, e:
            raise SearchException(e)

    '''
       Executes search.
       @return {@link SearchResponse}
       @throws SearchException
     '''
    def execute(self):
        try:
            url = self.generateUrl()
            session = requests.session()
            response = session.get(url)
            if response.status_code == 200:
                responseObject = json.loads(response.text)
                return SearchResponse(responseObject)
            else:
                responseText = response.content
                raise SearchException(responseText)
        except Exception, e:
            raise SearchException(e)
