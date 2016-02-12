import PositionPropertySetter
import TexturePropertySetter
import PlugInManager

kCCBFileFormatVersion = 4
kCCBUseRegularFile = "Use regular file"

def deserializePoint(val):
    return (val[0],val[1])

def deserializeColor3(val):
    pass
def nodeGraphFromDictionary(doc, parentSize):
    # TODO:@twenty0ne
    
    props = doc.get("properties")
    baseClass = doc.get("baseClass")
    children = doc.get("children")
    
    # Create the node
    node = PlugInManager.thePlugIn.createDefaultNodeOfType(baseClass)
    if not node:
        print "WARNING! Plug-in missing for " + baseClass
        return None
    
    # TODO:@twenty0ne
    # Fetch info and extra properties
    nodeInfo = node._userObject
    extraProps = nodeInfo._extraProps
    plugIn = nodeInfo._plugIn
    
    # Flash skew compatibility
    # TODO:@twenty0ne
    # if bool(doc.get("usesFlashSkew")):
    #    node
    
    # Set properties for the node
    for propInfo in props:
        ntype = propInfo.get("type")
        name = propInfo.get("name")
        serializedValue = propInfo.get("value")
        
        # Check for renamings
        # TODO:@twenty0ne
        
        if plugIn.dontSetInEditorProperty(name):
            extraProps[name] = serializedValue
        else:
            setProp(name, ntype, serializedValue, node, parentSize)
            
        baseValue = propInfo.get("baseValue")
        # if baseValue:
        # TODO:@twenty0ne
        
    # Set extra properties for code connections
    customClass = doc.get("customClass", "")
    memberVarName = doc.get("memberVarAssignmentName", "")
    memberVarType = int(doc.get("memberVarAssignmentType"))
    
    extraProps["customClass"] = customClass
    extraProps["memberVarAssignmentName"] = memberVarName
    extraProps["memberVarAssignmentType"] = memberVarType
    
    # TODO:@twenty0ne
    # JS code connections
        
    # Children load
    # TODO:@twenty0ne
    # contentSize = node.contentSize
    # TODO:@twenty0ne
    if baseClass == "CCMenu":
        childlist = []
        for childdoc in children:
            child = nodeGraphFromDictionary(childdoc, (100,100))
            childlist.append(child)           
        node.create_menu(childlist)
    else:
        for childdoc in children:
            child = nodeGraphFromDictionary(childdoc, (100,100))
            node.add(child)        
    
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

def setProp(name, ntype, serializedValue, node, parentSize):
    # Fetch info and extra properties
    nodeInfo = node._userObject
    extraProps = nodeInfo._extraProps
    
    if ntype == "Position":
        x = serializedValue[0]
        y = serializedValue[1]
        posType = 0
        if len(serializedValue) == 3:
            posType = serializedValue[2]
        PositionPropertySetter.setPosition((x,y), posType, node, name, parentSize)
    elif ntype == "Point" or ntype == "PointLock":
        pt = deserializePoint(serializedValue)
        # TODO:@twenty0ne
    elif ntype == "Size":
        w = serializedValue[0]
        h = serializedValue[1]
        size = (w, h)
        sizeType = 0
        if len(serializedValue) == 3:
            sizeType = serializedValue[2]
        PositionPropertySetter.setSize(size, sizeType, node, name, parentSize)
    elif ntype == "Scale" or ntype == "ScaleLock":
        x = float(serializedValue[0])
        y = float(serializedValue[1])
        scaleType = 0
        if len(serializedValue) >= 3:
            extraProps[name+"Lock"] = serializedValue[2]
        if len(serializedValue) == 4:
            scaleType = int(serializedValue[3])
        #PositionPropertySetter.setScaledX
        node.scale_x = x
        node.scale_y = y
    elif ntype == "FontTTF":
        pass
    elif ntype == "SpriteFrame":
        spriteSheetFile = serializedValue[0]
        spriteFile = serializedValue[1]
        if not spriteSheetFile or spriteSheetFile == "":
            spriteSheetFile = kCCBUseRegularFile
        extraProps[name+"Sheet"] = spriteSheetFile
        extraProps[name] = spriteFile
        TexturePropertySetter.setSpriteFrameForNode(node, name, spriteFile, spriteSheetFile)
    elif ntype == "Check":
        # TODO:@twenty0ne
        pass
    elif ntype == "Color3":
        # TODO:@twenty0ne
        pass
    elif ntype == "Text" or ntype == "String":
        text = serializedValue
        if not text:
            text = ""
        node.element.text = text
    elif ntype == "Byte" or ntype == "Blendmode" or \
         ntype == "Block" or ntype == "FntFile" or \
         ntype == "Degrees" or ntype == "FloatScale" or ntype == "IntegerLabeled":
        pass
    else:
        assert(0)
        