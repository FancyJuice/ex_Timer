import wx

class MainFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(550, 340))
        self.initUI()

    def initUI(self):
        self.panel = wx.Panel(self, -1)
        ix = 42
        wx.StaticText(self.panel, label="时间记录工具", pos=(ix, 22))

        # 创建位图按钮
        startmap = wx.Bitmap("./res/pic/start.png", wx.BITMAP_TYPE_PNG)
        width, height = 60, 30  # 设置按钮大小
        startmap = self.scale_bitmap(startmap, width, height)
        self.button = wx.BitmapButton(self.panel, wx.ID_ANY, startmap, size=(width, height), pos=(ix, 52), style=wx.BORDER_SIMPLE)

        # 自定义绘制按钮上的文本（背景透明）

    def scale_bitmap(self, bitmap, width, height):
        image = bitmap.ConvertToImage()
        image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
        return wx.Bitmap(image)

class App(wx.App):
    def __init__(self):
        super(self.__class__, self).__init__()

    def OnInit(self):
        self.title = "计时工具 v."
        self.frame = MainFrame(None, -1, self.title)
        self.frame.Show(True)
        return True

app = App()
app.MainLoop()
