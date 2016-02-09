kCCBFileFormatVersion = 4

def deserializeColor3(val):
    pass
def nodeGraphFromDictionary(doc, parentSize):
    # TODO:@twenty0ne
    
    props = doc.get("properties")
    baseClass = doc.get("baseClass")
    children = doc.get("children")
    
    # Create the node
    node = 

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
    elif fileVersion > kCCBFileFormatVersion:
        print "WARNING! Trying to load file made with a newer version of CocosBuilder"
        return None
    
    return nodeGraphFromDictionary(nodeGraph, parentSize)

def setProp(name, type, serializedValue, node, parentSize):
    pass