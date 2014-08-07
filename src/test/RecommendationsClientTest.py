import unittest
from main.Unbxd import Unbxd

class RecommendationsClientTest(unittest.TestCase):

    def setUp(self):
        Unbxd.configure("demo-u1393483043451", 
                        "ae30782589df23780a9d98502388555f", 
                        "ae30782589df23780a9d98502388555f")

    def test(self):
        response = Unbxd.getRecommendationsClient()
        response = response.getMoreLikeThese("532062745e4016fd1c73b7a4", None)
        response = response.execute()
        
        self.assertIsNotNone(response)
        self.assertEquals(200, response.getStatusCode())
        self.assertEquals("OK", response.getMessage())
        self.assertEquals(6, response.getTotalResultsCount())
        self.assertEquals(6, response.getResults().getResultsCount())
        self.assertIsNotNone(response.getResults().getAt(0).getUniqueId())