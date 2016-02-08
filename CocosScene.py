import cocos
from cocos.layer import Layer
from RulersLayer import RulersLayer

class CocosScene(Layer):    
    def __init__(self):
        super(CocosScene, self).__init__()
        self._bgLayer = None
        self._stageBgLayer = None
        self._contentLayer = None
        self._rulerLayer = None
        
        self.setupEditorNodes()
    
    def setupEditorNodes(self):
        self._rulerLayer = RulersLayer()
        self.add(self._rulerLayer, z=6)
        
    def nextFrame(self):
        # Update rulers
        self._rulerLayer.updateWithSize([700,650],[0,0],1)
        
    def mouseEntered(self):
        print "mouseEntered"
        self._rulerLayer.mouseEntered()
    
    def mouseExited(self):
        print "mouseExited"
        self._rulerLayer.mouseExited()
        
    def mouseMoved(self, pos):
        print "mouseMoved"
        self._rulerLayer.updateMousePos(pos)
        