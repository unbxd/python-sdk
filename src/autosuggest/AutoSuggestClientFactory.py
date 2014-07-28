from autosuggest.AutoSuggestClient import AutoSuggestClient

class AutoSuggestClientFactory(object):

    @staticmethod
    def getAutoSuggestClient(siteKey, apiKey, secure):
        return AutoSuggestClient(siteKey, apiKey, secure)