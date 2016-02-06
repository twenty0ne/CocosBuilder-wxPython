import wx

class PanelResource(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1, style=wx.BORDER_RAISED, size=(250, 650), pos=(0, 53))
        
        treeCtrl = wx.TreeCtrl(self, -1, style=wx.TR_DEFAULT_STYLE|wx.TR_FULL_ROW_HIGHLIGHT|wx.TR_HIDE_ROOT, size=(250,650))
        idRoot = treeCtrl.AddRoot('PATH')
        treeCtrl.AppendItem(idRoot, 'T2')
        treeCtrl.AppendItem(idRoot, 'T3')
        treeCtrl.ExpandAll()
    