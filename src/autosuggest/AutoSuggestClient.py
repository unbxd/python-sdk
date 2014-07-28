# Client class for calling AutoSuggest APIs
from autosuggest.exceptions.AutoSuggestException import AutoSuggestException
import urllib
import json
import requests  # @UnresolvedImport
from autosuggest.response.AutoSuggestResponse import AutoSuggestResponse

class AutoSuggestClient:
    __encoding = "UTF-8";
    
    def __init__(self, siteKey, apiKey, secure):
        self.siteKey = siteKey;
        self.apiKey = apiKey;
        self.secure = secure;

        self.inFieldsCount = -1;
        self.popularProductsCount = -1;
        self.keywordSuggestionsCount = -1;
        self.topQueriesCount = -1;

    def getAutoSuggestUrl(self):
        endPartOfUrl = self.siteKey + ".search.unbxdapi.com/" + self.apiKey + "/autosuggest?wt=json"
        return "https://" + endPartOfUrl if self.secure else "http://" + endPartOfUrl

    '''
       Gets autosuggest results for query
       @param query
       @return self
     '''
    def autosuggest(self, query):
        self.query = query
        return self

    '''
       Sets number of in_fields to be returned in results
       @param inFieldsCount
       @return self
     '''
    def setInFieldsCount(self, inFieldsCount):
        self.inFieldsCount = inFieldsCount
        return self

    '''
       Sets number of popular products to be returned in results
       @param popularProductsCount
       @return self
     '''
    def setPopularProductsCount(self, popularProductsCount):
        self.popularProductsCount = popularProductsCount
        return self

    '''
       Sets number of keyword suggestions to be returned in results
       @param keywordSuggestionsCount
       @return self
     '''
    def setKeywordSuggestionsCount(self, keywordSuggestionsCount):
        self.keywordSuggestionsCount = keywordSuggestionsCount;
        return self;

    '''
       Sets number of popular queries to be returned in results
       @param topQueriesCount
       @return self
     '''
    def setTopQueriesCount(self, topQueriesCount):
        self.topQueriesCount = topQueriesCount;
        return self;

    def generateUrl(self):
        try:
            sb = ""
            
            if self.query is not None:
                sb += self.getAutoSuggestUrl()
                sb += "&q=" + urllib.quote(self.query).encode(AutoSuggestClient.__encoding)
            
            if self.inFieldsCount != -1:
                sb += "&inFields.count=" + urllib.quote(str(self.inFieldsCount) + "").encode(AutoSuggestClient.__encoding)
            
            if self.popularProductsCount != -1:
                sb += "&popularProducts.count=" + urllib.quote(str(self.popularProductsCount) + "").encode(AutoSuggestClient.__encoding)
            
            if self.keywordSuggestionsCount != -1:
                sb += "&keywordSuggestions.count=" + urllib.quote(str(self.keywordSuggestionsCount) + "").encode(AutoSuggestClient.__encoding)
            
            if self.topQueriesCount != -1:
                sb += "&topQueries.count=" + urllib.quote(str(self.topQueriesCount) + "").encode(AutoSuggestClient.__encoding)
            
            return sb
        except Exception, e:
            raise AutoSuggestException(e)

    '''
       Executes Auto Suggest Query.
     '''
    def execute(self): 
        try:
            url = self.generateUrl()
            session = requests.session()
            response = session.get(url)
            if response.status_code == 200:
                responseObject = json.loads(response.text)
                return AutoSuggestResponse(responseObject)
            else:
                responseText = response.content
                raise AutoSuggestException(responseText)
        except Exception, e:
            raise AutoSuggestException(e)
