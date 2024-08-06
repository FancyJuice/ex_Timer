import wx

app = wx.App(False)
frame = wx.Frame(None, wx.ID_ANY, "调整位图按钮大小示例")

# 加载位图
bitmap = wx.Bitmap("./res/pic/按钮BG.png", wx.BITMAP_TYPE_PNG)

# 将位图转换为图像
image = bitmap.ConvertToImage()

# 缩放图像，这里将图像缩放为新的尺寸（width, height）
width, height = 100, 50  # 设置新的按钮大小
image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)

# 将图像转换回位图
bitmap = wx.Bitmap(image)

# 创建位图按钮，并将缩放后的位图应用于按钮
button = wx.BitmapButton(frame, wx.ID_ANY, bitmap, size=(100, 50), style=wx.BORDER_SIMPLE)
button.SetBackgroundColour(wx.Colour(100, 100, 100))  # 设置按钮背景颜色

button.SetLabel("你好")

frame.Show()
app.MainLoop()
