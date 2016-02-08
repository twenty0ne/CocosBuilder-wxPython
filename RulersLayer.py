import cocos
from cocos.layer import Layer
from cocos.sprite import Sprite
from cocos.cocosnode import CocosNode
from cocos.text import Label

class RulersLayer(Layer):
    def __init__(self):
        super(RulersLayer, self).__init__()
        
        self._kCCBRulerWidth = 15
        
        self._stageOrigin = [0,0]
        self._winSize = [0,0]
        self._zoom = 1.0
        
        # TODO:@twenty0ne
        # CCScale9Sprite
        bgVertical = Sprite('images/ruler-bg-vertical.png')
        # TODO:@twenty0ne
        # notice image_anchor, anchor, transform_anchor difference
        bgVertical.image_anchor = 0,0
        self.add(bgVertical)
        self._bgVertical = bgVertical
        
        bgHorizontal = Sprite('images/ruler-bg-horizontal.png')
        bgHorizontal.image_anchor = 0,0
        self.add(bgHorizontal, z=2)
        self._bgHorizontal = bgHorizontal
        
        marksVertical = CocosNode()
        self.add(marksVertical, z=1)
        self._marksVertical = marksVertical
        
        marksHorizontal = CocosNode()
        self.add(marksHorizontal, z=3)
        self._marksHorizontal = marksHorizontal
        
        mouseMarkVertical = Sprite('images/ruler-guide.png')
        mouseMarkVertical.image_anchor = 0,0.5
        mouseMarkVertical.visible = False
        self.add(mouseMarkVertical, z=4)
        self._mouseMarkVertical = mouseMarkVertical
        
        mouseMarkHorizontal = Sprite('images/ruler-guide.png')
        mouseMarkHorizontal.rotation = -90
        mouseMarkHorizontal.image_anchor = 0,0.5
        mouseMarkHorizontal.visible = False
        self.add(mouseMarkHorizontal, z=4)
        self._mouseMarkHorizontal = mouseMarkHorizontal
        
        xyBg = Sprite('images/ruler-xy.png')
        xyBg.image_anchor = 0,0
        xyBg.position = 0,0
        self.add(xyBg, z=5)
        
        lblX = Label("0", position=(40,3), color=(0,0,0,255), font_size=8, anchor_x="right")
        #lblX.anchor = 1,0
        #lblX.position = 47,3
        lblX.visible = False
        self.add(lblX, z=6)
        self._lblX = lblX
        
        lblY = Label("0", position=(90,3), color=(0,0,0,255), font_size=8, anchor_x="right")
        #lblY.anchor = 1,0
        #lblY.position = 97,3
        lblY.visible = False
        self.add(lblY, z=6)
        self._lblY = lblY
        
    def updateWithSize(self, ws, so, zm):
        self._stageOrigin[0] = int(self._stageOrigin[0])
        self._stageOrigin[1] = int(self._stageOrigin[1])
        
        if self._winSize == ws and self._stageOrigin == so and self._zoom == zm:
            return
        
        self._winSize = ws
        self._stageOrigin = so
        self._zoom = zm
        
        # TODO:@twenty0ne
        # CCScale9Sprite.preferedSize
        # Resize backrounds
        self._bgHorizontal.scale_x = self._winSize[0]/self._bgHorizontal.width
        self._bgHorizontal.scale_y = self._kCCBRulerWidth/self._bgHorizontal.height
        
        self._bgVertical.scale_x = self._kCCBRulerWidth/self._bgVertical.width
        self._bgVertical.scale_y = self._winSize[1]/self._bgVertical.height
        
        # Add marks and numbers
        for obj in self._marksVertical.get_children():
            self._marksVertical.remove(obj)
        for obj in self._marksHorizontal.get_children():
            self._marksHorizontal.remove(obj)
            
        # Vertical marks
        y = int(so[1]) - (int(so[1])/10)*10
        while y < ws[1]:
            yDist = abs(y - int(self._stageOrigin[1]))
            
            mark = None
            addLabel = False
            if yDist == 0:
                mark = Sprite("images/ruler-mark-origin.png")
                addLabel = True
            elif yDist%50 == 0:
                mark = Sprite("images/ruler-mark-major.png")
                addLabel = True
            else:
                mark = Sprite("images/ruler-mark-minor.png")
            mark.image_anchor = 0,0.5
            mark.position = 0,y
            self._marksVertical.add(mark)
            
            if addLabel:
                displayDist = yDist / self._zoom
                strDist = str(displayDist)
                strLen = len(strDist)
                for i in range(0, strLen):
                    lbl = Label(strDist[i], color=(0,0,0,255), font_size=8)
                    lbl.anchor = 0,0
                    lbl.position = 2,(y+1+10*(strLen-i-1))
                    self._marksVertical.add(lbl)
            
            y = y + 10
            
        # Horizontal marks
        x = int(so[0]) - (int(so[0])/10)*10
        while x < ws[0]:
            xDist = abs(x - int(self._stageOrigin[0]))
            
            mark = None
            addLabel = False
            if xDist == 0:
                mark = Sprite("images/ruler-mark-origin.png")
                addLabel = True
            elif xDist%50 == 0:
                mark = Sprite("images/ruler-mark-major.png")
                addLabel = True
            else:
                mark = Sprite("images/ruler-mark-minor.png")
            mark.image_anchor = 0,0.5
            mark.position = x,0
            mark.rotation = -90
            self._marksHorizontal.add(mark)
            
            if addLabel:
                displayDist = xDist / self._zoom
                lbl = Label(str(displayDist), color=(0,0,0,255), font_size=8)
                lbl.anchor = 0,0
                lbl.position = x+1,1
                self._marksHorizontal.add(lbl)
            
            x = x + 10
            
        
    def updateMousePos(self, pos):
        self._mouseMarkHorizontal.position = (pos[0],0)
        self._mouseMarkVertical.position = (0,pos[1])
        
        # TODO:@twenty0ne
        # change label text use .element.text
        self._lblX.element.text = str(pos[0])
        self._lblY.element.text = str(pos[1])
        
    def mouseEntered(self):
        self._mouseMarkHorizontal.visible = True
        self._mouseMarkVertical.visible = True
        self._lblX.visible = True
        self._lblY.visible = True
        
    def mouseExited(self):
        self._mouseMarkHorizontal.visible = False
        self._mouseMarkVertical.visible = False
        self._lblX.visible = False
        self._lblY.visible = False        
        
    
        
        
        
        