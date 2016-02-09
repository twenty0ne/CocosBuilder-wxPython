from PlugInNode import PlugInNode

class PlugInManager:
    def __init__(self):
        self._plugInsNode = {}
        self._plugInsNodeNames = []
        self._plugInsNodeNamesCanBeRoot = []
    
    def loadPlugIns(self):

        
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
        pass
        
    def plugInNodeNamed(self, name):
        pass
        
thePlugIn = PlugInManager()
        