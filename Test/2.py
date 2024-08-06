import wx


class MainFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(550, 340))
        self.initUI()

    def initUI(self):
        self.panel = wx.Panel(self, -1)
        self.panel.SetBackgroundColour("blue")
        ix = 42
        wx.StaticText(self.panel, label="时间记录工具", pos=(ix, 22))

        # 创建位图按钮
        self.startmap_normal = wx.Bitmap("./res/pic/start.png", wx.BITMAP_TYPE_PNG)
        self.startmap_highlight = wx.Bitmap("./res/pic/start_highlight.png", wx.BITMAP_TYPE_PNG)

        width, height = 60, 30  # 设置按钮大小
        scaled_normal = self.scale_bitmap(self.startmap_normal, width, height)
        self.button = wx.BitmapButton(self.panel, wx.ID_ANY, scaled_normal, size=(width, height), pos=(ix, 52),
                                      style=wx.BORDER_SIMPLE)

        # 绑定事件
        self.button.Bind(wx.EVT_BUTTON, self.OnButtonClicked)
        self.button.Bind(wx.EVT_ENTER_WINDOW, self.OnMouseOver)
        self.button.Bind(wx.EVT_LEAVE_WINDOW, self.OnMouseLeave)

    def scale_bitmap(self, bitmap, width, height):
        image = bitmap.ConvertToImage()
        image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
        return wx.Bitmap(image)

    def OnButtonClicked(self, event):
        # 按钮点击时的行为
        print("Button clicked")

    def OnMouseOver(self, event):
        # 鼠标悬浮时切换到高亮图片
        scaled_highlight = self.scale_bitmap(self.startmap_highlight, 60, 30)
        self.button.SetBitmap(scaled_highlight)

    def OnMouseLeave(self, event):
        # 鼠标离开时切换回普通图片
        scaled_normal = self.scale_bitmap(self.startmap_normal, 60, 30)
        self.button.SetBitmap(scaled_normal)


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
