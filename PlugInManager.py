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
        node = None
        if plugin._nodeEditorClassName == "CCNode":
            pass
        elif plugin._nodeEditorClassName == "CCLayer":
            node = cocos.layer.Layer()
        else:
            assert(0)
            
        return node
        
    def plugInNodeNamed(self, name):
        return self._plugInsNode[name]
        
thePlugIn = PlugInManager()
        