import wx

app = wx.App()
frame = wx.Frame(None, title="StaticText换行示例", size=(300, 200))
panel = wx.Panel(frame)

long_text = "这是一个很长很长很长很长很长的文本，用于演示StaticText的换行问题。"
# static_text = wx.StaticText(panel, label=long_text, size=(240, -1))
# static_text.Wrap(200)
wx.StaticText(panel, label=long_text, pos=(20, 20), size=(240, 300), style=wx.ALIGN_LEFT | wx.EXPAND)

# sizer = wx.BoxSizer(wx.VERTICAL)
# sizer.Add(static_text, 0, wx.ALL, 10)
# panel.SetSizer(sizer)

frame.Show()
app.MainLoop()
