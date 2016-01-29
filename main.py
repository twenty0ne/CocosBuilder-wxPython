import os
import wx

class PanelLeft(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1, style=wx.RAISED_BORDER, size=(50, 500), pos=(0, 51))
        
class PanelRight(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1, style=wx.RAISED_BORDER, size=(50, 500), pos=(750, 51))

class PanelBottom(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1, style=wx.RAISED_BORDER, size=(800, 50), pos=(0, 550))

class PanelTool(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1, style=wx.RAISED_BORDER, size=(800, 50))
        
        wx.Button(self, -1, "ZoomIn")
        
class PanelMain(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1)

class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Main Frame", size=(800, 600))
        
        panelTool = PanelTool(self)
        panelLeft = PanelLeft(self)
        panelRight = PanelRight(self)
        panelBottom = PanelBottom(self)
        
        panelMain = PanelMain(self)
        
        # create menu
        menuFile = wx.Menu()
        
        submenuNew = wx.Menu()
        submenuNew.Append(-1, "Project")
        submenuNew.AppendSeparator()
        submenuNew.Append(-1, "Interface")
        
        menuFile.AppendMenu(-1, "New", submenuNew)
        menuFile.AppendSeparator()
        item = menuFile.Append(-1, "Open...\tCtrl-O")
        self.Bind(wx.EVT_MENU, self.OnMenuOpen, item)
        
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
        
    def OnMenuOpen(self, evt):
        dialog = wx.FileDialog(None, "Choose a file", os.getcwd(), "", "*.ccbpro", wx.OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            print dialog.GetPath()
        dialog.Destroy()

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = MainFrame()
    frame.Show()
    app.MainLoop()