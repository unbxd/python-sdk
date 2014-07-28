import unittest
from main.Unbxd import Unbxd

class SearchClientTest(unittest.TestCase):

    def setUp(self):
        Unbxd.configure("demo-u1393483043451", 
                        "ae30782589df23780a9d98502388555f", 
                        "ae30782589df23780a9d98502388555f");

    def test_search(self):
        queryParams = {}
        queryParams["fl"] = "uniqueId"
        queryParams["stats"] = "price";
        
        response = Unbxd.getSearchClient()
        response = response.search("*", queryParams)
        response = response.addFilter("color_fq","black")
        response = response.addFilter("Brand_fq", "Ralph Lauren")
        response = response.addSort("price", "ASC")
        response = response.setPage(2, 5)
        response = response.execute();
        
        self.assertIsNotNone(response);
        self.assertEquals(0, response.getStatusCode());
        self.assertNotEquals(0, response.getQueryTime());
        self.assertEquals(0, response.getErrorCode());
        self.assertEquals("OK", response.getMessage());
        self.assertNotEquals(0, response.getTotalResultsCount());
        self.assertEquals(5, response.getResults().getResultsCount());
        self.assertEquals(1, len(response.getResults().getAt(0).getAttributes()));
        self.assertIsNotNone(response.getResults().getAt(0).getAttributes().get("uniqueId"));
        self.assertIsNotNone(response.getStats());
        self.assertIsNotNone(response.getStats().getStat("price").getMin());
        
    def test_browse(self):
        queryParams = {}
        queryParams["fl"] = "uniqueId"
        queryParams["stats"] = "price"
        
        response = Unbxd.getSearchClient()
        response = response.browse("1", queryParams)
        response = response.addFilter("color_fq","black")
        response = response.addFilter("Brand_fq", "Ralph Lauren")
        response = response.addSort("price", "ASC")
        response = response.setPage(2, 5)
        response = response.execute();
        
        self.assertIsNotNone(response);
        self.assertEquals(0, response.getStatusCode());
        self.assertNotEquals(0, response.getQueryTime());
        self.assertEquals(0, response.getErrorCode());
        self.assertEquals("OK", response.getMessage());
        self.assertNotEquals(0, response.getTotalResultsCount());
        self.assertEquals(5, response.getResults().getResultsCount());
        self.assertEquals(1, len(response.getResults().getAt(0).getAttributes()));
        self.assertIsNotNone(response.getResults().getAt(0).getAttributes().get("uniqueId"));
        self.assertIsNotNone(response.getStats());
        self.assertIsNotNone(response.getStats().getStat("price").getMin());

    def test_bucket(self):
        queryParams = {}
        queryParams["fl"] = "uniqueId"
        queryParams["stats"] = "price"
        
        response = Unbxd.getSearchClient()
        response = response.bucket("*", "category", queryParams)
        response = response.addFilter("color_fq","black")
        response = response.addFilter("Brand_fq", "Ralph Lauren")
        response = response.addSort("price", "ASC")
        response = response.setPage(2, 5)
        response = response.execute();
        
        self.assertIsNotNone(response);
        self.assertEquals(0, response.getStatusCode());
        self.assertNotEquals(0, response.getQueryTime());
        self.assertEquals(0, response.getErrorCode());
        self.assertEquals("OK", response.getMessage());
        self.assertNotEquals(0, response.getTotalResultsCount());
        self.assertIsNone(response.getResults());
        self.assertEquals(5, response.getBuckets().getNumberOfBuckets());
        self.assertNotEquals(0, response.getBuckets().getBuckets()[0].getTotalResultsCount());
        self.assertEquals(1, len(response.getBuckets().getBuckets()[0].getResults().getAt(0).getAttributes()));
        self.assertIsNotNone(response.getBuckets().getBuckets()[0].getResults().getAt(0).getAttributes().get("uniqueId"));
        self.assertIsNotNone(response.getStats());
        self.assertIsNotNone(response.getStats().getStat("price").getMin());

if __name__ == '__main__':
    unittest.main()