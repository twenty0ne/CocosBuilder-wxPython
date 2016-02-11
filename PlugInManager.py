from PlugInNode import PlugInNode
from NSBundle import *
import cocos
import NodeInfo
import CCBReaderInternal

class PlugInManager:
    def __init__(self):
        self._plugInsNode = {}
        self._plugInsNodeNames = []
        self._plugInsNodeNamesCanBeRoot = []
    
    def loadPlugIns(self):
        plugInPaths = theNSBundle._plugInPaths
        
        for plugInPath in plugInPaths:
            plugIn = PlugInNode(plugInPath)
            if plugIn and not plugIn._isAbstract:
                self._plugInsNode[plugIn._nodeClassName] = plugIn
                self._plugInsNodeNames.append(plugIn._nodeClassName)
                
                if plugIn._canBeRoot:
                    self._plugInsNodeNamesCanBeRoot.append(plugIn._nodeClassName)
                    
                # TODO:@twenty0ne
                # Load icon
    
    def createDefaultNodeOfType(self, name):
        plugin = self.plugInNodeNamed(name)
        if not plugin:
            return None
        
        # TODO:@twenty0ne
        # CocosBuilder-Mac use NSClassFromString
        print "createDefaultNodeOfType - " + plugin._nodeEditorClassName
        node = None
        if plugin._nodeEditorClassName == "CCNode":
            node = cocos.cocosnode.CocosNode()
        elif plugin._nodeEditorClassName == "CCLayer":
            node = cocos.layer.Layer()
        elif plugin._nodeEditorClassName == "CCLayerGradient":
            # TODO:@twenty0ne
            node = cocos.layer.Layer()
        elif plugin._nodeEditorClassName == "CCBPMenu":
            # TODO:@twenty0ne
            node = cocos.menu.Menu("TITLE")
        elif plugin._nodeEditorClassName == "CCMenuItemImage":
            # TODO:@twenty0ne
            # image, callback need to update
            node = cocos.menu.ImageMenuItem("images/missing-texture.png", None)
        elif plugin._nodeEditorClassName == "CCLabelBMFont":
            # TODO:@twenty0ne
            node = cocos.text.Label("missing-label")
        elif plugin._nodeEditorClassName == "CCSprite":
            node = cocos.sprite.Sprite("images/missing-texture.png")
        elif plugin._nodeEditorClassName == "CCBPLabelTTF":
            # TODO:@twenty0ne
            node = cocos.text.Label("missing-label")
        else:
            assert(0)
            
        # 
        nodeInfo = NodeInfo.nodeInfoWithPlugIn(plugin)
        extraProps = nodeInfo._extraProps
        node._userObject = nodeInfo
        
        # Set default data
        plugInProps = plugin._nodeProperties
        for propInfo in plugInProps:
            defaultValue = propInfo.get("default")
            if defaultValue:
                name = propInfo.get("name")
                ntype = propInfo.get("type")
                if bool(propInfo.get("dontSetInEditor")):
                    extraProps[name] = defaultValue
                else:
                    # Set the property on the object
                    CCBReaderInternal.setProp(name, ntype, defaultValue, node, (0,0))
            
        return node
        
    def plugInNodeNamed(self, name):
        return self._plugInsNode[name]
        
thePlugIn = PlugInManager()
        