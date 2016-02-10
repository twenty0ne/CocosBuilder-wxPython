import biplist
from NSBundle import *

class PlugInNode:
    def __init__(self, plugInPath):
        # Load properties
        propsPath = plugInPath + "/CCBPProperties.plist"
        props = biplist.readPlist(propsPath)
        
        self._nodeClassName = props.get("className")
        self._nodeEditorClassName = props.get("editorClassName")
        
        self._nodeProperties = []
        self._nodePropertiesDict = {}
        
        self.loadPropertiesForBundle(plugInPath, self._nodeProperties)
        self.setupNodePropsDict()
        
        # Support for spriteFrame drop targets
        spriteFrameDrop = props.get("spriteFrameDrop")
        if spriteFrameDrop:
            self._dropTargetSpriteFrameClass = spriteFrameDrop.get("className")
            self._dropTargetSpriteFrameProperty = spriteFrameDrop.get("property")
            
        # Check if node type can be root node and which children are allowed
        self._canBeRoot = bool(props.get("canBeRootNode"))
        self._canHaveChildren = bool(props.get("canHaveChildren"))
        self._isAbstract = bool(props.get("isAbstract"))
        self._requireChildClass = props.get("requireChildClass")
        self._requireParentClass = props.get("requireParentClass")
        self._positionProperty = props.get("positionProperty")
    
    def loadPropertiesForBundle(self, plugInPath, arr):
        # TODO:@twenty0ne
        # repeat load plist
        propsPath = plugInPath + "/CCBPProperties.plist"
        props = biplist.readPlist(propsPath)
        
        inheritsFrom = props.get("inheritsFrom")
        if inheritsFrom:
            plugInPath = theNSBundle.getPlugInPath(inheritsFrom)
            assert plugInPath
        
        arr.extend(props.get("properties"))
        
        # Handle overridden properties
        overrides = props.get("propertiesOverridden")
        if overrides:
            for propInfo in overrides:
                propName = propInfo.get("name")
                
                # Find the old property
                for i in range(len(arr)):
                    oldPropInfo = arr[i]
                    if oldPropInfo.get("name") == propName:
                        arr[i] = propInfo
                        
    
    def setupNodePropsDict(self):
        # Transform the nodes info array to a dictionary for quicker lookups of properties
        for propInfo in self._nodeProperties:
            propName = propInfo.get("name")
            if propName:
                self._nodePropertiesDict[propName] = propInfo
                