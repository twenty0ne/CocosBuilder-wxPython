import wx

class PanelProperty(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1, style=wx.BORDER_RAISED, size=(250, 650), pos=(900, 53))