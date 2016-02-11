#import sys
#import os
#sys.path.append(os.path.join(os.path.dirname(__file__), 'cocos/'))

import cocos
from cocos.layer import Layer,ColorLayer
from RulersLayer import RulersLayer

class CocosScene(Layer):
    def __init__(self):
        super(CocosScene, self).__init__()
        self._bgLayer = None
        self._stageBgLayer = None
        self._contentLayer = None
        self._rulerLayer = None
        self._rootNode = None
        
        self.setupEditorNodes()
    
    def setupEditorNodes(self):
        # TODO:@twenty0ne
        self._rulerLayer = RulersLayer()
        self.add(self._rulerLayer, z=6)
        
        # Black content layer
        self._stageBgLayer = ColorLayer(0,0,0,255,width=0,height=0)
        self._stageBgLayer.anchor = 0.5,0.5
        # TODO:@twenty0ne
        # stageBgLayer.ignoreAnchorPointForPosition = NO
        self.add(self._stageBgLayer, z=0)
        
        self._contentLayer = Layer()
        self.add(self._contentLayer)
        
    def nextFrame(self):
        # Update rulers
        self._rulerLayer.updateWithSize([700,650],[0,0],1)
        
    def mouseEntered(self):
        # print "mouseEntered"
        self._rulerLayer.mouseEntered()
    
    def mouseExited(self):
        # print "mouseExited"
        self._rulerLayer.mouseExited()
        
    def mouseMoved(self, pos):
        # print "mouseMoved"
        self._rulerLayer.updateMousePos(pos)
        
    def replaceRootNodeWith(self, node):
        if self._rootNode:
            self._contentLayer.remove(self._rootNode)
        self._rootNode = node
        
        if not node:
            return        
        self._contentLayer.add(node)
    
theCocosScene = None