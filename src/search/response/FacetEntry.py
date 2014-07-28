class FacetEntry(object):
    def __init__(self, count, term = None):
        self.count = count
        self.term = term

    def getTerm(self):
        return self.term;

    def getCount(self):
        return self.count;
