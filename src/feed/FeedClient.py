import zipfile
import json
import requests  # @UnresolvedImport
import xml.etree.ElementTree as ET
import os

from feed.response.FeedResponse import FeedResponse
from feed.FeedField import FeedField
from feed.FeedFile import FeedFile
from feed.exceptions.FeedInputException import FeedInputException
from feed.exceptions.FeedUploadException import FeedUploadException
from collections import OrderedDict

class FeedClient:
    
    def __init__(self, siteKey, secretKey, secure):
        self.siteKey = siteKey
        self.secretKey = secretKey
        self.secure = secure
        
        self._fields = []
        self._addedDocs = {}
        self._updatedDocs = {}
        self._deletedDocs = []
        
        self._taxonomyNodes = []
        self._taxonomyMappings = {}
    
    def getFeedUrl(self):
        endPartOfUrl = "feed.unbxdapi.com/upload/v2/" + self.secretKey + "/" + self.siteKey
        return "https://" + endPartOfUrl if self.secure else "http://" + endPartOfUrl
    
    '''
        Adds schema for a field. Schema needs to be added only once.
        @param fieldName Name of the field. Following rules apply for field names.
                         <ul>
                             <li>Should be alphnumeric</li>
                             <li>Can contain hyphens and underscores</li>
                             <li>Can not start and end with -- or __</li>
                             <li>Can not start with numbers</li>
                         </ul>
        @param datatype Datatype of the field. Refer {@link DataType}
        @param multivalued True for allowing multiple values for each document
        @param autosuggest True to include field in autosuggest response
        @return this
    '''
    def addSchema(self, fieldName, datatype, multivalued = False, autosuggest = False):
        feedField = FeedField(fieldName, datatype, multivalued, autosuggest)
        self._fields.append(feedField)
        return self
    
    '''
        Adds a product to the field. If a product with the same uniqueId is 
        found to be already present the product will be overwritten.
        @param product
        @return this
    '''
    def addProduct(self, product):
        self._addedDocs[product.getUniqueId()] = product
        return self
    
    '''
        Adds a list of products to the field. If a product with the same 
        uniqueId is found to be already present the product will be overwritten.
        @param product
        @return this
    '''
    def addProducts(self, products):
        for product in products:
            self.addProduct(product)
        return self
    
    '''
       Add a variant to a product.
       @param parentUniqueId Unique Id of the parent product
       @param variantAttributes Attributes of the variant
       @return this
       @throws FeedInputException
    '''
    def addVariant(self, parentUniqueId, variantAttributes):
        if parentUniqueId not in self._addedDocs:
            raise FeedInputException("Parent product needs to be added")
        
        self._addedDocs[parentUniqueId].addAssociatedProduct(variantAttributes)
        
        return self

    '''
       Add a variants to a product.
       @param parentUniqueId Unique Id of the parent product
       @param variantAttributes Attributes of the variant
       @return this
       @throws FeedInputException
    '''
    def addVariants(self, parentUniqueId, variantAttributes):
        for variantAttribute in variantAttributes:
            self.addVariant(parentUniqueId, variantAttribute)
        
        return self

    '''
       Upserts a product.
       @param productDelta Delta of product attributes. uniqueId is mandatory
       @return this
    '''
    def updateProduct(self, productDelta):
        self._updatedDocs[productDelta.getUniqueId()] = productDelta
        
        return self

    '''
       Upserts products.
       @param productsDeltas Deltas of products attributes. uniqueId is mandatory
       @return this
    '''
    def updateProducts(self, productsDeltas):
        for product in productsDeltas:
            self.updateProduct(product)
        
        return self

    '''
       Deletes a product with given uniqueId
       @param uniqueId
       @return this
    '''
    def deleteProduct(self, uniqueId):
        self._deletedDocs.append(uniqueId)
        
        return self

    '''
       Deletes products with given uniqueIds
       @param uniqueIds
       @return this
    '''
    def deleteProducts(self, uniqueIds):
        self._deletedDocs.extend(uniqueIds)
        
        return self

    '''
       Adds a taxonomy node
       @param node
       @return this
    '''
    def addTaxonomyNode(self, node):
        self._taxonomyNodes.append(node)
        
        return self

    '''
       Add taxonomy nodes
       @param nodes
       @return
    '''
    def addTaxonomyNodes(self, nodes):
        self._taxonomyNodes.extend(nodes)
        
        return self

    '''
       Maps a uniqueId with taxonomy nodes
       @param uniqueId
       @param nodeIds List of taxnonomy node Id
       @return this
    '''
    def addTaxonomyMapping(self, uniqueId, nodeIds):
        self._taxonomyMappings[uniqueId] = nodeIds
        
        return self

    '''
       Maps uniqueIds with taxonomy nodes
       @param mappings Map of Unique Id -> List of taxonomy nodes Ids
       @return this
    '''
    def addTaxonomyMappings(self, mappings):
        self._taxonomyMappings.update(mappings)
        
        return self
    
    def zipIt(self, xmlFile):
        try:
            zip = xmlFile.name + ".zip"
            output = zipfile.ZipFile(zip, 'w')
            output.write(os.path.abspath(xmlFile.name))
            output.close()
            
            if os.path.exists(zip):
                return zip
            else:
                return False
        except Exception:
                return False
    
    '''
       Uploads the feed to Unbxd platform. The feed is zipped before being pushed.
       Please be realistic and don't push millions of products in a single call. 
       Try to confine it to a few thousands. 10K would be a good number.
      
       @param isFullImport If true it will clear the old feed entirely 
                           and upload new products. Please use with care.
       @return {@link FeedResponse}
       @throws FeedUploadException
    '''
    def push(self, isFullImport):
        doc = FeedFile(self._fields, self._addedDocs.values(), 
                       self._updatedDocs.values(), OrderedDict.fromkeys(self._deletedDocs).keys(), 
                       self._taxonomyNodes, self._taxonomyMappings).getDoc()
        try :
            
            ''' Write the xml to a file '''
            xmlFile = open("/var/tmp/" + self.siteKey + ".xml", "w")
            docDump = ET.tostring(doc)
            print docDump
            xmlFile.write(docDump)
            xmlFile.close()
            
            xmlFile = open("/var/tmp/" + self.siteKey + ".xml", "r")
            
            ''' Zip the file '''
            self.zipIt(xmlFile)
            
            ''' Create the url '''
            url = self.getFeedUrl()
            if isFullImport:
                url += "?fullimport=true"
            
            ''' Post '''
            fileObj = open("/var/tmp/" + self.siteKey + ".xml.zip", 'rb')
            f = {"archive": ("/var/tmp/" + self.siteKey + ".xml.zip", fileObj)}
            session = requests.session()
            response = session.post(url, files=f)
            
            if response.status_code == 200:
                try:
                    responseObject = json.loads(response.text)
                    return FeedResponse(responseObject)
                except Exception, e:
                    raise FeedUploadException(response.content)
            else:
                raise FeedUploadException(response.content)
        except Exception, e:
            raise FeedUploadException(e)
