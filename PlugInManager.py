from PlugInNode import PlugInNode
from NSBundle import *
import cocos

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
            pass
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
            node = cocos.text.Label("label")
        else:
            assert(0)
            
        return node
        
    def plugInNodeNamed(self, name):
        return self._plugInsNode[name]
        
thePlugIn = PlugInManager()
        