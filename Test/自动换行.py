# import wx
#
#
# class MainFrame(wx.Frame):
#     def __init__(self, parent, id, title):
#         wx.Frame.__init__(self, parent, id, title, size=(400, 200))
#         self.initUI()
#
#     def initUI(self):
#         panel = wx.Panel(self)
#
#         # 创建带自动换行的多行文本控件
#         text = "这是一个带自动换行的文本标签。" * 20
#         wrap_text = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.VSCROLL)
#         wrap_text.SetValue(text)
#
#         sizer = wx.BoxSizer(wx.VERTICAL)
#         sizer.Add(wrap_text, 1, wx.EXPAND | wx.ALL, 20)
#         panel.SetSizer(sizer)
#
#
# app = wx.App(False)
# frame = MainFrame(None, wx.ID_ANY, "自动换行示例")
# frame.Show()
# app.MainLoop()


import wx

app = wx.App(False)
frame = wx.Frame(None, wx.ID_ANY, "Sizer 示例", size=(400, 300))

panel = wx.Panel(frame)

# 创建一个垂直的BoxSizer
sizer = wx.BoxSizer(wx.VERTICAL)

# 添加控件到sizer中
text = wx.StaticText(panel, label="这是一个文本标签")
sizer.Add(text, 0, wx.ALIGN_CENTER | wx.ALL, 10)  # 控制文本标签的尺寸和位置

button = wx.Button(panel, wx.ID_ANY, "按钮")
sizer.Add(button, 0, wx.ALIGN_CENTER | wx.ALL, 10)  # 控制按钮的尺寸和位置

# 设置panel的sizer
panel.SetSizer(sizer)

frame.Show()
app.MainLoop()
