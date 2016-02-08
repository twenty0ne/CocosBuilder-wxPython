import os
import wx
from App import *
from PanelResource import *
from PanelTool import *
from PanelProperty import *
from PanelStage import *

class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "CocosBuilder", size=(1150, 700))
        
        # panel = wx.Panel(self)
        # panel
        panelStage = PanelStage(self)
        panelResource = PanelResource(self)
        panelProperty = PanelProperty(self)
        panelTool = PanelTool(self)
                
        # create menu
        menuFile = wx.Menu()
        
        submenuNew = wx.Menu()
        submenuNew.Append(-1, "Project")
        submenuNew.AppendSeparator()
        submenuNew.Append(-1, "Interface")
        
        menuFile.AppendMenu(-1, "New", submenuNew)
        menuFile.AppendSeparator()
        item = menuFile.Append(-1, "Open...\tCtrl-O")
        self.Bind(wx.EVT_MENU, self.onMenuOpen, item)
        
        menuEdit = wx.Menu()
        
        menuBar = wx.MenuBar()
        menuBar.Append(menuFile, "File")
        menuBar.Append(menuEdit, "Edit")
        self.SetMenuBar(menuBar)
        
        # create toolbar
        # toolbar = self.CreateToolBar()
        # toolbar.AddSimpleTool(-1, wx.Bitmap("images/TB_zoomIn.png", wx.BITMAP_TYPE_PNG), "New")
        # toolbar.AddTool(-1, wx.Button())
        # toolbar.AddToolItem(wx.Button(toolbar, -1, "Hello"))
        # toolbar.Realize()
        
        # panelToolbar = wx.Panel(self)
        # wx.Button(panelToolbar, -1, "Hello")
        
        # theApp.openProject("/Users/Tom/Desktop/mygit/CocosBuilder-wxPython/test/ccb3project.ccbproj")
        
    def onMenuOpen(self, evt):
        dialog = wx.FileDialog(None, "Choose a file", os.getcwd(), "", "*.ccbproj", wx.OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            print dialog.GetPath()
        dialog.Destroy()

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = MainFrame()
    #test pygletwx
    """
    frame = wx.Frame(None, -1, "CocosBuilder", size=(1150, 700))
    panel = PygletWX.EditorGLPanel(frame)
    panel.ChangeImage(pyglet.image.load("images/btn-move.png"))
    """
    frame.Show()
    app.MainLoop()