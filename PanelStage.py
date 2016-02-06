import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), './cocos/'))

import wx
import PygletWX
import cocos
import pyglet

# TODO:@twenty0ne
# wx.Panel replace pyglet.window
class PanelStage(PygletWX.PygletGLPanel):
    
    # for window
    fullscreen = False
    width = 650
    height = 650    
    
    def __init__(self, parent, id=wx.ID_ANY):
        PygletWX.PygletGLPanel.__init__(self, parent, -1, style=wx.BORDER_RAISED, size=(650, 650), pos=(250, 53))
        self.SetBackgroundColour("gray")
        #self.draw_objects()
        #self.canvas.Bind(wx.EVT_LEFT_DOWN, self.canvas_RightClicked)
        
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.onTimer, self.timer)
        # 1 / 60 second
        self.timer.Start(17)
 
    def canvas_RightClicked(self, event):
        """Creates the context menu if necessary, then displays it"""
        if self._contextMenu is None:
            self._createContextMenu()
        #self._contextMenu.Check(self._drawmode, True)
        self.canvas.PopupMenu(self._contextMenu, event.GetPosition())
        
    def create_objects(self):
        '''create opengl objects when opengl is initialized'''
        # hello world
        cocos.director.director.init(window=self, autoscale=False)
        
        layer = cocos.layer.Layer()       
        
        sprite = cocos.sprite.Sprite('test/grossini.png')
        #sprite.position = 0,0
        #sprite.scale = 2
        layer.add(sprite)
        sprite.do( cocos.actions.interval_actions.MoveBy( (200,0), duration=0.5 ) )
        
        #label = cocos.text.Label('Hello world', font_name='Times New Roman', font_size=32, anchor_x='center', anchor_y='center')
        #label.position = 320,240
        #layer.add(label)
        
        #self.image = pyglet.image.load('images/btn-move.png')
        
        self.scene = cocos.scene.Scene(layer) 
        cocos.director.director.run(self.scene)         
        
 
    def draw_objects(self):
        print "draw_objects"
        """Draws the objects on the canvas"""
        if not self.GLinitialized:
            return
 
        # clear the screen
        pyglet.gl.glClearColor(0.93, 0.93, 0.93, 1)
        pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT | pyglet.gl.GL_DEPTH_BUFFER_BIT)   
        
        
        #pyglet.gl.glPushMatrix()
        #self.scene.visit()
        #self._label.visit()
        #pyglet.gl.glPopMatrix()
        cocos.director.director.on_draw()
        
        #pyglet.gl.glBegin(pyglet.gl.GL_QUADS)
        #pyglet.gl.glVertex3f(0, 0, 0)
        #pyglet.gl.glVertex3f(0.1, 0.2, 0.3)
        #pyglet.gl.glVertex3f(0.1, 0.2, 0.3)
        #pyglet.gl.glEnd()    
        
        #self.image.blit(0, 0, 0)
        
    # pyglet.window
    def push_handlers(self, *args, **kwargs):
        pass
    
    def remove_handlers(self, *args, **kwargs):
        pass
    
    def set_fullscreen(self, fullscreen=True, screen=None, mode=None,
                           width=None, height=None):    
        pass
    
    def clear(self):
        pass
    
    def switch_to(self):
        pass
    
    def on_resize(self, width, height):
        pass
    
    def onTimer(self, evt):
        pyglet.clock.tick()
        self.OnDraw()
    