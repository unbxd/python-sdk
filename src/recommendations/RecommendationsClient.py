import urllib
import requests  # @UnresolvedImport
import json

from recommendations.exceptions.RecommendationsException import RecommendationsException
from recommendations.response.RecommendationResponse import RecommendationResponse

class RecommendationsClient:
    __encoding = "UTF-8"
    ip = None

    def __init__(self, siteKey, apiKey, secure):
        self.siteKey = siteKey
        self.apiKey = apiKey
        self.secure = secure

    def getRecommendationUrl(self):
        endPartOfUrl = "apac-recommendations.unbxdapi.com/v1.0/" + self.apiKey + "/" + self.siteKey + "/"
        return "https://" + endPartOfUrl if self.secure else "http://" + endPartOfUrl

    '''
       Get Recently viewed items for the user : uid
       @param uid value of the cookie : "unbxd.userId"
       @return self
    '''
    def getRecentlyViewed(self, uid):
        self._boxType = "RECENTLY_VIEWED"
        self.uid = uid
        
        return self

    '''
       Get products recommended for user : uid
       @param uid value of the cookie : "unbxd.userId"
       @param ip IP address if the user for localization of results
       @return self
    '''
    def getRecommendedForYou(self, uid, ip):
        self._boxType = "RECOMMENDED_FOR_YOU"
        self.uid = uid
        self.ip = ip
        return self

    '''
       Get More products like product : uniqueId
       @param uniqueId Unique Id of the product
       @param uid value of the cookie : "unbxd.userId"
       @return self
    '''
    def getMoreLikeThese(self, uniqueId, uid):
        self._boxType = "MORE_LIKE_THESE"
        self.uid = uid
        self.uniqueId = uniqueId
        return self

    '''
       Get products which were also viewed by users who viewed the product : uniqueId
       @param uniqueId Unique Id of the product
       @param uid value of the cookie : "unbxd.userId"
       @return self
    '''
    def getAlsoViewed(self, uniqueId, uid):
        self._boxType = "ALSO_VIEWED"
        self.uid = uid
        self.uniqueId = uniqueId
        return self

    '''
      Get products which were also bought by users who bought the product : uniqueId
      @param uniqueId Unique Id of the product
      @param uid value of the cookie : "unbxd.userId"
      @return self
    '''
    def getAlsoBought(self, uniqueId, uid):
        self._boxType = "ALSO_BOUGHT"
        self.uid = uid
        self.uniqueId = uniqueId
        return self

    '''
      Get Top Selling products
      @param uid value of the cookie : "unbxd.userId"
      @param ip IP address if the user for localization of results
      @return self
    '''
    def getTopSellers(self, uid, ip):
        self._boxType = "TOP_SELLERS"
        self.uid = uid
        self.ip = ip
        return self

    '''
      Get Top Selling products within self category
      @param category name of the category
      @param uid value of the cookie : "unbxd.userId"
      @param ip IP address if the user for localization of results
      @return self
    '''
    def getCategoryTopSellers(self, category, uid, ip):
        self._boxType = "CATEGORY_TOP_SELLERS"
        self.uid = uid
        self.ip = ip
        self.category = category
        return self

    '''
      Get Top Selling products within self brand
      @param brand name of the brand
      @param uid value of the cookie : "unbxd.userId"
      @param ip IP address if the user for localization of results
      @return self
    '''
    def getBrandTopSellers(self, brand, uid, ip):
        self._boxType = "BRAND_TOP_SELLERS"
        self.uid = uid
        self.ip = ip
        self.brand = brand
        return self

    '''
      Get Top Selling products among products similar to self product
      @param uniqueId Unique Id of the product
      @param uid value of the cookie : "unbxd.userId"
      @param ip IP address if the user for localization of results
      @return self
    '''
    def getPDPTopSellers(self, uniqueId, uid, ip):
        self._boxType = "PDP_TOP_SELLERS"
        self.uid = uid
        self.ip = ip
        self.uniqueId = uniqueId
        return self

    '''
      Get recommendations based on the products added in cart by the user : uid
      @param uid value of the cookie : "unbxd.userId"
      @param ip IP address if the user for localization of results
      @return self
    '''
    def getCartRecommendations(self, uid, ip):
        self._boxType = "CART_RECOMMEND"
        self.uid = uid
        self.ip = ip
        return self

    def generateUrl(self):
        try:
            sb = ""
            
            if self._boxType is not None:
                sb += self.getRecommendationUrl()
                
                if self._boxType == "ALSO_VIEWED":
                    sb += "also-viewed/" + urllib.quote(self.uniqueId).encode(RecommendationsClient.__encoding) + "?format=json"
                elif self._boxType == "ALSO_BOUGHT":
                    sb += "also-bought/" + urllib.quote(self.uniqueId).encode(RecommendationsClient.__encoding) + "?format=json"
                elif self._boxType == "RECENTLY_VIEWED":
                    sb += "recently-viewed/" + urllib.quote(self.uid).encode(RecommendationsClient.__encoding) + "?format=json"
                elif self._boxType == "RECOMMENDED_FOR_YOU":
                    sb += "recommend/" + urllib.quote(self.uid).encode(RecommendationsClient.__encoding) + "?format=json"
                elif self._boxType == "MORE_LIKE_THESE":
                    sb += "more-like-these/" + urllib.quote(self.uniqueId).encode(RecommendationsClient.__encoding) + "?format=json"
                elif self._boxType == "TOP_SELLERS":
                    sb += "top-sellers/" + "?format=json"
                elif self._boxType == "CATEGORY_TOP_SELLERS":
                    sb += "category-top-sellers/" + urllib.quote(self.category).encode(RecommendationsClient.__encoding) + "?format=json"
                elif self._boxType == "BRAND_TOP_SELLERS":
                    sb += "brand-top-sellers/" + urllib.quote(self.brand).encode(RecommendationsClient.__encoding) + "?format=json"
                elif self._boxType == "PDP_TOP_SELLERS":
                    sb += "pdp-top-sellers/" + urllib.quote(self.uniqueId).encode(RecommendationsClient.__encoding) + "?format=json"
                elif self._boxType == "CART_RECOMMEND":
                    sb += "cart-recommend/" + urllib.quote(self.uid).encode(RecommendationsClient.__encoding) + "?format=json"
                
                if self.uid is not None:
                    sb += "&uid=" + urllib.quote(self.uid).encode(RecommendationsClient.__encoding)
                
                if self.ip is not None:
                    sb += "&ip=" + urllib.quote(self.ip).encode(RecommendationsClient.__encoding)
            else:
                raise RecommendationsException("Couldn't determine which recommendation widget to call.")
            
            return sb
        except Exception, e:
            raise RecommendationsException(e)

    '''
       Executes a recommendations call
       @return {@link RecommendationResponse}
       @throws RecommendationsException
    '''
    def execute(self): 
        try:
            url = self.generateUrl()
            session = requests.session()
            response = session.get(url)
            if response.status_code == 200:
                responseObject = json.loads(response.text)
                return RecommendationResponse(responseObject)
            else:
                responseText = response.content
                raise RecommendationsException(responseText)
        except Exception, e:
            raise RecommendationsException(e)

