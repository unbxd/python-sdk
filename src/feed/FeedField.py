class FeedField(object):
    value = None
    
    def __init__(self, name, dataType, multiValued, autoSuggest):
        self.name = name
        self.multiValued = multiValued
        self.dataType = dataType
        self.autoSuggest = autoSuggest

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def isMultiValued(self): 
        return self.multiValued

    def getDataType(self):
        return self.dataType

    def isAutoSuggest(self): 
        return self.autoSuggest
    
    def __str__(self):
        ret = "Feed File -> "
        ret += "Name: " + self.name 
        ret += ", AutoSuggest: " + str(self.autoSuggest) 
        ret += ", DataType: " + self.dataType 
        ret += ", MultiValued: " + str(self.multiValued)
        return ret