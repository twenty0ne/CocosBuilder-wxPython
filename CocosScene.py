#import sys
#import os
#sys.path.append(os.path.join(os.path.dirname(__file__), 'cocos/'))

import pyglet
import cocos
from cocos.layer import Layer,ColorLayer
from RulersLayer import RulersLayer

#
kCCBBorderDevice = 0
kCCBBorderTransparent = 1
kCCBBorderOpaque = 2
kCCBBorderNone = 3

#
kCCBAlignHorizontalCenter = 0
kCCBAlignVerticalCenter = 1
kCCBAlignLeft = 2
kCCBAlignRight = 3


class CocosScene(Layer):
    def __init__(self):
        super(CocosScene, self).__init__()
        self._bgLayer = None
        self._stageBgLayer = None
        self._contentLayer = None
        self._rulerLayer = None
        self._borderLayer = None
        self._rootNode = None
        self._borderDevice = None
        self._stageBorderType = 0
        
        self.setupEditorNodes()
    
    def setupEditorNodes(self):
        # TODO:@twenty0ne
        self._rulerLayer = RulersLayer()
        self.add(self._rulerLayer, z=6)
        
        # Border layer
        self._borderLayer = Layer()
        self.add(self._borderLayer, z=1)
        
        self._borderDevice = cocos.sprite.Sprite("images/missing-texture.png")
        self._borderLayer.add(self._borderDevice, z=1)
        
        # Gray background
        self._bgLayer = ColorLayer(128,128,128,255,width=4096,height=4096)
        self._bgLayer.position = 0,0
        self._bgLayer.anchor = 0,0
        self.add(self._bgLayer, z=-1)
        
        # Black content layer
        self._stageBgLayer = ColorLayer(0,0,0,255,width=0,height=0)
        self._stageBgLayer.anchor = 0.5,0.5
        # TODO:@twenty0ne
        # stageBgLayer.ignoreAnchorPointForPosition = NO
        self.add(self._stageBgLayer, z=0)
        
        self._contentLayer = Layer()
        self.add(self._contentLayer)
        
    def nextFrame(self):
        # Setup border layer
        bounds = 
        
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
        
    def setStageBorder(self, ntype):
        self._borderDevice.visible = False
        
        if self._stageBgLayer.width == 0 or self._stageBgLayer.height == 0:
            ntype = kCCBBorderNone
            self._stageBgLayer.visible = False
        else:
            self._stageBgLayer.visible = True
            
        if ntype == kCCBBorderDevice:
            deviceTexture = None
            rotateDevice = True
            
            if rotateDevice:
                self._borderDevice.rotation = 90
            else:
                self._borderDevice.rotation = 0
            deviceTexture = pyglet.resource.image("images/frame-iphone.png")
            self._borderDevice.image = deviceTexture
            self._borderDevice.visible = True
            
        self._stageBorderType = ntype
    
theCocosScene = None