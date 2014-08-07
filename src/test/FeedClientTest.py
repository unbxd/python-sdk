import unittest
from main.Unbxd import Unbxd
from feed.FeedProduct import FeedProduct
from feed.TaxonomyNode import TaxonomyNode

class FeedClientTest(unittest.TestCase):

    def setUp(self):
        Unbxd.configure("sdk_test-u1404981344388", 
                        "149abee9a65f0d135cd07c90308c54d4", 
                        "149abee9a65f0d135cd07c90308c54d4")

    def test_product_upload(self):
        product = {}
        product["title"] = "phodu joote"
        product["some-field"] = "test-field-value"
        product["brand"] = "Adidas"
        product["category"] = "Sports Shoes"
        product["price"] = 1100
        
        variant = {}
        variant["gender"] = "male"
        
        response = Unbxd.getFeedClient()
        response = response.addSchema("some-field", "TEXT")
        response = response.addSchema("genderAssociated", "TEXT", True, True)
        response = response.addProduct(FeedProduct("testsku", product))
        response = response.addProduct(FeedProduct("testsku2", product))
        response = response.addVariant("testsku2", variant)
        response = response.push(False)
        
        self.assertIsNotNone(response)
        self.assertEquals(200, response.getStatusCode())
        self.assertIsNotNone(response.getMessage())
        self.assertIsNotNone(response.getUploadID())
        self.assertEquals(0, len(response.getUnknownSchemaFields()))
        self.assertEquals(0, len(response.getFieldErrors()))
        
    def atest_product_upload_should_fail_unknown_fields(self):
        product = {}
        product["title"] = "phodu joote"
        product["some-unknown-field"] = "test-field-value"
        product["brand"] = "Adidas"
        product["category"] = "Sports Shoes"
        product["price"] = 1100
        
        response = Unbxd.getFeedClient()
        response = response.addProduct(FeedProduct("testsku3", product))
        response = response.push(False)
        
        self.assertIsNotNone(response)
        self.assertEquals(602, response.getStatusCode())
        self.assertIsNotNone(response.getMessage())
        self.assertIsNotNone(response.getUploadID())
        self.assertEquals(1, len(response.getUnknownSchemaFields()))
        self.assertEquals("some-unknown-field", response.getUnknownSchemaFields()[0])
        self.assertEquals(0, len(response.getFieldErrors()))

    def test_product_upload_should_fail_field_error(self):
        product = {}
        product["title"] = "phodu joote"
        product["brand"] = "Adidas"
        product["category"] = "Sports Shoes"
        product["price"] = "1100abc"
        
        response = Unbxd.getFeedClient()
        response = response.addProduct(FeedProduct("testsku3", product))
        response = response.push(False)
        
        self.assertIsNotNone(response)
        self.assertEquals(401, response.getStatusCode())
        self.assertIsNotNone(response.getMessage())
        self.assertIsNotNone(response.getUploadID())
        self.assertEquals(0, len(response.getUnknownSchemaFields()))
        self.assertEquals(1, len(response.getFieldErrors()))
        self.assertEquals("price", response.getFieldErrors()[0].getFieldName())
        self.assertEquals("1100abc", response.getFieldErrors()[0].getFieldValue())
        self.assertEquals("DECIMAL".lower(), response.getFieldErrors()[0].getDataType())
        self.assertIsNotNone(response.getFieldErrors()[0].getMessage())
        self.assertEquals(402, response.getFieldErrors()[0].getErrorCode())
        self.assertNotEquals(0, response.getFieldErrors()[0].getRowNum())
        self.assertNotEquals(0, response.getFieldErrors()[0].getColNum())

    def test_taxonomy_upload(self):
        response = Unbxd.getFeedClient()
        response = response.addTaxonomyNode(TaxonomyNode("1", "Men", None))
        response = response.addTaxonomyNode(TaxonomyNode("2", "Shoes", ["1"]))
        response = response.addTaxonomyMapping("testsku2", ["1", "2"])
        response = response.push(False)
        self.assertIsNotNone(response)
        self.assertEquals(200, response.getStatusCode())
        self.assertIsNotNone(response.getMessage())
        self.assertIsNotNone(response.getUploadID())
        self.assertEquals(0, len(response.getUnknownSchemaFields()))
        self.assertEquals(0, len(response.getFieldErrors()))
