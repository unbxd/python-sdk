from search.response.Stat import Stat

class Stats(object):
    def __init__(self, params):
        self._stats = {}
        for field in params:
            if params.get(field) is not None:
                self._stats[field] = Stat(params.get(field))

    '''
       @return Map of Field --> {@link Stat}
     '''
    def getStats(self):
        return self._stats

    '''
       @param fieldName
       @return Stat for the field name
     '''
    def getStat(self, fieldName):
        return self._stats.get(fieldName)