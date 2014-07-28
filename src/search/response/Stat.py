class Stat(object):

    def __init__(self, params):
        self._min = float(params.get("min"))
        self._max = float(params.get("max"))
        self._count = float(params.get("count"))
        self._sum = float(params.get("sum"))
        self._mean = float(params.get("mean"))

    def getCount(self):
        return self._count

    def getMin(self):
        return self._min

    def getMax(self):
        return self._max

    def getSum(self):
        return self._sum

    def getMean(self):
        return self._mean