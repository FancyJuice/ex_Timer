import wx
from PIL import Image
class RoundedButton(wx.Panel):
    def __init__(self, parent, bitmap, size=(100, 30), radius=10):
        super().__init__(parent, size=size)
        self.bitmap = bitmap
        self.radius = radius
        self.SetMinSize(size)

        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_LEFT_DOWN, self.OnClick)

    def OnPaint(self, event):
        width, height = self.GetClientSize()
        dc = wx.BufferedPaintDC(self)
        gc = wx.GraphicsContext.Create(dc)

        # 创建一个圆角路径
        path = gc.CreatePath()
        path.AddRoundedRectangle(0, 0, width, height, self.radius)
        gc.SetPen(wx.TRANSPARENT_PEN)  # 透明边框

        # 使用图片作为填充
        brush = gc.CreateBrush(wx.Brush(self.bitmap))
        gc.SetBrush(brush)

        # 填充圆角矩形
        gc.FillPath(path)

    def OnClick(self, event):
        print("Button clicked!")

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title='Rounded Button with Image', size=(300, 200))

        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)

        img = Image.open("res/pic/bgp.jpg")
        imsize = (120, 70)
        img = img.resize(imsize, Image.ANTIALIAS)  # 指定目标尺寸并使用抗锯齿算法
        img = img.convert("RGB")  # 将图像转换为RGB模式，wx.Bitmap需要RGB图像
        # 创建 wx.StaticBitmap 控件，并将缩放后的图像转换为 wx.Bitmap
        bmp = self.pil_image_to_wx_bitmap(img)

        # 加载图片

        btn = RoundedButton(panel, bmp, size=(bmp.GetWidth(), bmp.GetHeight()))
        sizer.Add(btn, 0, wx.ALL | wx.CENTER, 10)

        panel.SetSizer(sizer)

    def pil_image_to_wx_bitmap(self, pil_image):
        width, height = pil_image.size
        image = wx.Image(width, height)
        image.SetData(pil_image.convert("RGB").tobytes())
        wx_bitmap = wx.Bitmap(image)
        return wx_bitmap

if __name__ == '__main__':
    app = wx.App(False)
    frame = MyFrame()
    frame.Show()
    app.MainLoop()
