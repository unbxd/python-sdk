from xml.etree.ElementTree import Element, SubElement
from xml.sax.saxutils import escape
import types

class FeedFile(object):
    def __init__(self, fields, addedDocs, updatedDocs, 
                 deletedDocs, taxonomyNodes, taxonomyMappings): 
        try:
            self.feed = Element('feed')
            
            if len(fields) > 0 or len(addedDocs) > 0 or len(updatedDocs) > 0 or len(deletedDocs) > 0:
                catalog = SubElement(self.feed, 'catalog')
                
                if len(fields) > 0:
                    self.writeSchema(fields, catalog)
                
                if len(addedDocs) > 0:
                    addNode = SubElement(catalog, "add")
                    self.writeAdd(addedDocs, addNode)
                
                if len(updatedDocs) > 0:
                    updateNode = SubElement(catalog, "update")
                    self.writeUpdate(updatedDocs, updateNode)
                
                if len(deletedDocs) > 0:
                    deleteNode = SubElement(catalog, "delete")
                    self.writeDelete(deletedDocs, deleteNode)
                
            if len(taxonomyNodes) > 0 or len(taxonomyMappings) > 0:
                taxonomy = SubElement(self.feed, "taxonomy")
                
                if len(taxonomyNodes) > 0:
                    self.writeTree(taxonomyNodes, taxonomy);
                
                if len(taxonomyMappings) > 0:
                    self.writeMapping(taxonomyMappings, taxonomy)
        except Exception, e:
            e.args
    
    def writeSchema(self, fields, parent):
        for field in fields:
            schema = SubElement(parent, 'schema')
            
            fieldName = SubElement(schema, "fieldName")
            fieldName.text = field.getName()
            
            dataType = SubElement(schema, "dataType")
            dataType.text = field.getDataType().lower()
            
            multiValued = SubElement(schema, "multiValued")
            multiValued.text = str(field.isMultiValued()).lower()
            
            autoSuggest = SubElement(schema, "autoSuggest")
            if field.isAutoSuggest() == True:
                autoSuggest.text = 'true'
            else :
                autoSuggest.text = 'false'

    def writeAttribute(self, items, field, o, associated):
        if type(o) is types.DictType:
            values = o
        else:
            values = []
            values.append(o)
        
        for value in values:
            if value is None: 
                continue;
            
            if associated == True:
                associated = "Associated"
            else:
                associated = ""
            
            e = SubElement(items, field + associated)
            
            value = str(value)
            value = value.replace("[\u0000-\u001f]", "")
            
            value = escape(value); 
            e.text = value

    def writeAdd(self, addedDocs, parent):
        for product in addedDocs:
            items = SubElement(parent, "items")
            
            for field in product.getAttributes():
                self.writeAttribute(items, field, product.get(field), False);
            
            if product.getAssociatedProducts() is not None and len(product.getAssociatedProducts()) > 0:
                for associatedProduct in product.getAssociatedProducts():
                    associatedItems = SubElement(items, "associatedProducts")
                    for field in associatedProduct:
                        self.writeAttribute(associatedItems, field, associatedProduct.get(field), True);
    
    def writeUpdate(self, updatedDocs, parent):
        for product in updatedDocs:
            items = SubElement(parent, "items")
            
            for field in product.getAttributes():
                self.writeAttribute(items, field, product.get(field), False)
            
            parent.appendChild(items);

    def writeDelete(self, deletedDocs, parent):
        for uniqueId in deletedDocs:
            items = SubElement(parent, "items")
            
            e = SubElement(items, "uniqueId")
            e.text = uniqueId

    def writeTree(self, nodes, parent):
        for node in nodes:
            tree = SubElement(parent, "tree")
            
            nodeId = SubElement(tree, "nodeId")
            nodeId.text = node.getNodeId()
            
            nodeName = SubElement(tree, "nodeName");
            nodeName.text = node.getNodeName()
            
            if node.getParentNodeIds() is not None :
                for parentNodeIdValue in node.getParentNodeIds():
                    parentNodeId = SubElement(tree, "parentNodeId")
                    parentNodeId.text = parentNodeIdValue
    
    def writeMapping(self, taxonomyMappings, parent):
        for uniqueId in taxonomyMappings:
            mapping = SubElement(parent, "mapping")
            
            uniqueIdNode = SubElement(mapping, "uniqueId")
            uniqueIdNode.text = uniqueId
            
            for nodeIdValue in taxonomyMappings[uniqueId]:
                nodeId = SubElement(mapping, "nodeId")
                nodeId.text = nodeIdValue

    def getDoc(self):
        return self.feed;