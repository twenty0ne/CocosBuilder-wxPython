import wx
import wx.lib.buttons

class PanelTool(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1, style=wx.BORDER_RAISED, size=(1150, 50), pos=(0, 0))
        
        # zoom
        wx.StaticText(self, -1, "Zoom", pos=(60,30))
        
        self.btnZoomIn = wx.BitmapButton(self, -1, wx.Bitmap("images/TB_zoomIn.png", wx.BITMAP_TYPE_PNG), size=(45,30), pos=(5,4))
        self.Bind(wx.EVT_BUTTON, self.onClickBtnZoomIn, self.btnZoomIn)
        
        self.btnActualSize = wx.BitmapButton(self, -1, wx.Bitmap("images/TB_actualSize.png", wx.BITMAP_TYPE_PNG), size=(45,30), pos=(50,4))
        self.Bind(wx.EVT_BUTTON, self.onClickBtnActualSize, self.btnActualSize)
        
        self.btnZoomOut = wx.BitmapButton(self, -1, wx.Bitmap("images/TB_zoomOut.png", wx.BITMAP_TYPE_PNG), size=(45,30), pos=(95,4))
        self.Bind(wx.EVT_BUTTON, self.onClickBtnZoomOut, self.btnZoomOut)
        
        # view
        wx.StaticText(self, -1, "View", pos=(220,30))
        
        self.btnLeftPanel = wx.lib.buttons.GenBitmapToggleButton(self, -1, wx.Bitmap("images/TB_leftPanel.png", wx.BITMAP_TYPE_PNG), size=(45,30), pos=(180,4))
        self.btnLeftPanel.SetValue(True)
        self.Bind(wx.EVT_BUTTON, self.onClickBtnLeftPanel, self.btnLeftPanel)
        
        self.btnBottomPanel = wx.lib.buttons.GenBitmapToggleButton(self, -1, wx.Bitmap("images/TB_bottomPanel.png", wx.BITMAP_TYPE_PNG), size=(45,30), pos=(220,4))
        self.btnBottomPanel.SetValue(True)
        self.Bind(wx.EVT_BUTTON, self.onClickBtnBottomPanel, self.btnBottomPanel)
        
        self.btnRightPanel = wx.lib.buttons.GenBitmapToggleButton(self, -1, wx.Bitmap("images/TB_rightPanel.png", wx.BITMAP_TYPE_PNG), size=(45,30), pos=(260,4))
        self.btnRightPanel.SetValue(True)
        self.Bind(wx.EVT_BUTTON, self.onClickBtnRightPanel, self.btnRightPanel)
        
    def onClickBtnZoomIn(self, event):
        pass
    
    def onClickBtnActualSize(self, event):
        pass
    
    def onClickBtnZoomOut(self, event):
        pass
    
    def onClickBtnLeftPanel(self, event):
        btn = event.GetEventObject()
    
    def onClickBtnBottomPanel(self, event):
        pass
    
    def onClickBtnRightPanel(self, event):
        pass
    
        
        
        
        