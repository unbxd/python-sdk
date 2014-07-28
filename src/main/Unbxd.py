from main.ConfigException import ConfigException
from feed.FeedClientFactory import FeedClientFactory
from search.SearchClientFactory import SearchClientFactory
from autosuggest.AutoSuggestClientFactory import AutoSuggestClientFactory
from recommendations.RecommendationsClientFactory import RecommendationsClientFactory

class Unbxd(object):
    ''' 
        Class to configure and retrieve clients. 
    '''
    
    secure = False
    _configured = False
    
    ''' 
        Configure Unbxd Client. This method should be called while initializing you application.
        If you don't know the configuration details please get in touch with support@unbxd.com
        
        @param siteKey The Unique Identifier for Site created on Unbxd Platform
        @param apiKey API key for calling read APIs
        @param secretKey API key for calling Feed APIs 
        @param secure True to use HTTPS while making REST API calls,
                      Default is false.
    '''
    @staticmethod
    def configure(siteKey, apiKey, secretKey, secure = None):
        Unbxd.siteKey = siteKey
        Unbxd.apiKey = apiKey
        Unbxd.secretKey = secretKey
        Unbxd._configured = True
        
        if (secure is not None):
            Unbxd.secure = secure
    
    '''
        Should return a new Feed Client
    '''
    @staticmethod
    def getFeedClient():
        if Unbxd._configured is False:
            raise ConfigException("Please configure first with Unbxd.configure()")
        return FeedClientFactory().getFeedClient(Unbxd.siteKey, Unbxd.secretKey, Unbxd.secure)
    
    '''
       Should return a new Search Client
    '''
    @staticmethod
    def getSearchClient():
        if Unbxd._configured is False:
            raise ConfigException("Please configure first with Unbxd.configure()")
        return SearchClientFactory.getSearchClient(Unbxd.siteKey, Unbxd.apiKey, Unbxd.secure)

    '''
       Should return a new Autosuggest Client
    '''
    @staticmethod
    def getAutoSuggestClient():
        if Unbxd._configured is False:
            raise ConfigException("Please configure first with Unbxd.configure()")
        return AutoSuggestClientFactory.getAutoSuggestClient(Unbxd.siteKey, Unbxd.apiKey, Unbxd.secure)

    '''
       Should return a new Recommendations Client
       @return {@link RecommendationsClient}
       @throws ConfigException
    '''
    @staticmethod
    def getRecommendationsClient():
        if Unbxd._configured is False:
            raise ConfigException("Please configure first with Unbxd.configure()")
        return RecommendationsClientFactory.getRecommendationsClient(Unbxd.siteKey, Unbxd.apiKey, Unbxd.secure)

