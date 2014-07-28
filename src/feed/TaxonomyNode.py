class TaxonomyNode(object):

    ''' 
       nodeId : Generally corresponds to Category id or brand id
       parentNodeIds : List of parents in the order of nearest first.
    '''
    def __init__(self, nodeId, nodeName, parentNodeIds):
        self.nodeId = nodeId
        self.nodeName = nodeName
        self.parentNodeIds = parentNodeIds

    def getNodeId(self):
        return self.nodeId

    def getNodeName(self):
        return self.nodeName

    '''
       @return List of parents in the order of nearest first
    '''
    def getParentNodeIds(self):
        return self.parentNodeIds
