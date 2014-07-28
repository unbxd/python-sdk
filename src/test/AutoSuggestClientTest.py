import unittest
from main.Unbxd import Unbxd

class AutoSuggestClientTest(unittest.TestCase):
    
    def setUp(self):
        Unbxd.configure("autosuggesttest-u1405357792247", 
                        "7db139ac885f6516fb276520668daf83", 
                        "7db139ac885f6516fb276520668daf83");

    def test_autosuggest(self): 
        response = Unbxd.getAutoSuggestClient()
        response = response.autosuggest("sh")
        response = response.setInFieldsCount(3)
        response = response.setKeywordSuggestionsCount(5)
        response = response.setPopularProductsCount(10)
        response = response.setTopQueriesCount(4)
        response = response.execute()
        
        self.assertIsNotNone(response);
        self.assertEquals(0, response.getStatusCode());
        self.assertNotEquals(0, response.getQueryTime());
        self.assertEquals(0, response.getErrorCode());
        self.assertEquals("OK", response.getMessage());
        self.assertNotEquals(0, response.getTotalResultsCount());