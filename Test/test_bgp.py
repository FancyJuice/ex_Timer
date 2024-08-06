import wx
from PIL import Image

class MyPanel(wx.Panel):
    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent, id)
        try:
            image_file = "./res/pic/bgp.jpg"

            img = Image.open(image_file)
            imsize = (300, 200)
            img = img.resize(imsize, Image.ANTIALIAS)  # 指定目标尺寸并使用抗锯齿算法
            img = img.convert("RGB")  # 将图像转换为RGB模式，wx.Bitmap需要RGB图像

            # 创建 wx.StaticBitmap 控件，并将缩放后的图像转换为 wx.Bitmap
            to_bmp_image = self.pil_image_to_wx_bitmap(img)

            # to_bmp_image = wx.Image(image_file, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
            self.bitmap = wx.StaticBitmap(self, -1, to_bmp_image, (0, 0))
            image_width = to_bmp_image.GetWidth()
            image_height = to_bmp_image.GetHeight()
            set_title = '%s %d x %d' % (image_file, to_bmp_image.GetWidth(), to_bmp_image.GetHeight())
            parent.SetTitle(set_title)
        except IOError:
            print('Image file %s not found' % image_file)
            raise SystemExit
        # 创建一个按钮
        self.button = wx.Button(self.bitmap, -1, label='启动', pos=(102, 125))


    def pil_image_to_wx_bitmap(self, pil_image):
        width, height = pil_image.size
        image = wx.Image(width, height)
        image.SetData(pil_image.convert("RGB").tobytes())
        wx_bitmap = wx.Bitmap(image)
        return wx_bitmap


if __name__ == '__main__':
    app = wx.App()
    frame = wx.Frame(None, -1, '登陆窗口', size=(300, 200))
    my_panel = MyPanel(frame, -1)
    frame.Show()
    app.MainLoop()