from search.response.BucketResult import BucketResult
class BucketResults(object):

    def __init__(self, params):
        self._numberOfBuckets = int(params.get("numberOfBuckets"))

        self._buckets = []
        self._bucketsMap = {}
        for bucketKey in params:
            if bucketKey == "totalProducts" or bucketKey == "numberOfBuckets":
                continue
            
            bucket = BucketResult(params.get(bucketKey))
            self._buckets.append(bucket)
            self._bucketsMap[bucketKey] = bucket

    '''
     @return Number of buckets in response
    '''
    def getNumberOfBuckets(self):
        return self._numberOfBuckets

    '''
      @param value
      @return Bucket for the field value
    '''
    def getBucket(self, value):
        return self._bucketsMap.get(value)

    '''
      @return List of {@link BucketResult}
    '''
    def getBuckets(self):
        return self._buckets
