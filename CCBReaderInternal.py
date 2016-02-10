from PlugInManager import thePlugIn

kCCBFileFormatVersion = 4

def deserializeColor3(val):
    pass
def nodeGraphFromDictionary(doc, parentSize):
    # TODO:@twenty0ne
    
    props = doc.get("properties")
    baseClass = doc.get("baseClass")
    children = doc.get("children")
    
    # Create the node
    node = thePlugIn.createDefaultNodeOfType(baseClass)
    if not node:
        print "WARNING! Plug-in missing for " + baseClass
        return None
    
    # TODO:@twenty0ne
    # Fetch info and extra properties
    
    # Set properties for the node
    for propInfo in props:
        ntype = propInfo.get("type")
        name = propInfo.get("name")
        serializedValue = propInfo.get("value")
        
        # Check for renamings
        # TODO:@twenty0ne
        
    
    return node

def nodeGraphFromDocumentDictionary(doc, parentSize):
    if not doc:
        print "WARNING! Trying to load invalid file type (dict is null)"
        return None
    
    # Load file metadata
    fileType = doc.get("fileType")
    fileVersion = int(doc.get("fileVersion"))
    if not fileType or fileType != "CocosBuilder":
        print "WARNING! Trying to load invalid file type " + fileType
        return None
    
    nodeGraph = doc.get("nodeGraph")
    if fileVersion <= 2:
        # Use legacy reader
        # assetsPath = 
        # TODO:@twenty0ne
        assert(0)
        pass
    elif fileVersion > kCCBFileFormatVersion:
        print "WARNING! Trying to load file made with a newer version of CocosBuilder"
        return None
    
    return nodeGraphFromDictionary(nodeGraph, parentSize)

def setProp(name, type, serializedValue, node, parentSize):
    pass