import wx
import time
from utils import csv_fun as C
from utils import timefun as T
from utils import txtfun as TF

from utils.fpath import *


def show_exit_projs(self):
    s = C.show_pros(file_path)
    text = wx.StaticText(self, label=s, pos=(20, 60))
    text.Wrap(300)  # 设置最大宽度为 200 像素，超过宽度将自动换行


def button_icon(self, pic):
    img_path = os.path.join(pic_path, pic)
    icon = wx.Icon(img_path, type=wx.BITMAP_TYPE_PNG)
    self.SetIcon(icon)


class ShowInfo(wx.Dialog):
    def __init__(self, parent, id, info, title):
        super(ShowInfo, self).__init__(parent, id, title, size=(300, 200))
        self.app = wx.GetApp()
        self.panel = self.app.frame
        self.Center()
        button_icon(self, "show.png")

        vbox = wx.BoxSizer(wx.VERTICAL)
        tc1 = wx.TextCtrl(self, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.VSCROLL)
        tc1.SetValue(info)
        vbox.Add((-1, 10))
        vbox.Add(tc1, proportion=1, flag=wx.EXPAND | wx.RIGHT | wx.LEFT, border=20)
        vbox.Add((-1, 20))
        buttonok = wx.Button(self, wx.ID_OK)
        vbox.Add(buttonok, flag=wx.ALIGN_CENTER | wx.BOTTOM, border=15)

        self.SetSizer(vbox)


class StaDialog(wx.Dialog):
    def __init__(self, parent, id):
        super(StaDialog, self).__init__(parent, id, "开始（项目专用）", size=(350, 250))
        self.app = wx.GetApp()
        self.panel = self.app.frame

        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(self, label="所要进行的项目名称：")
        hbox1.Add(st1, flag=wx.LEFT | wx.ALIGN_CENTER_VERTICAL, border=20)
        self.proj = wx.TextCtrl(self)
        hbox1.Add(self.proj, flag=wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, border=8)

        vbox.Add((-1, 24))
        vbox.Add(hbox1, flag=wx.EXPAND)
        vbox.Add((-1, 24))
        info1, info2 = C.show_projs()
        st4 = wx.StaticText(self, label=info1)
        st5 = wx.StaticText(self, label=info2)
        st5.Wrap(280)
        vbox.Add(st4, flag=wx.LEFT, border=20)
        vbox.Add((-1, 4))
        vbox.Add(st5, flag=wx.LEFT, border=28)
        self.submit = wx.Button(self, label="开始计时")
        vbox.Add((-1, 30))
        vbox.Add(self.submit, flag=wx.ALIGN_CENTER)

        self.SetSizer(vbox)

        self.Bind(wx.EVT_BUTTON, self.OnClick, self.submit)
        self.Bind(wx.EVT_CHAR_HOOK, self.OnChar)
        # 图标
        button_icon(self, "我的流程.png")
        self.Center()
    def OnClick(self, event):
        proj = self.proj.GetValue()
        info = C.change_info(file_path, proj)
        dlg = TimDialog(None, 1, info, proj)
        self.Close()
        dlg.ShowModal()
        dlg.Destroy()

    def OnChar(self, event):
        keycode = event.GetKeyCode()
        if keycode == wx.WXK_RETURN or keycode == wx.WXK_NUMPAD_ENTER:
            self.OnClick(event)
        else:
            event.Skip()


class TimDialog(wx.Dialog):
    def __init__(self, parent, id, info, proj):
        super(TimDialog, self).__init__(parent, id, "计时开始", size=(350, 200))
        _, self.begin_t = TF.da_hour()
        self.start_time = time.time()
        self.proj = proj
        self.app = wx.GetApp()
        self.panel = self.app.frame

        intro = wx.StaticText(self, label=info)
        self.submit_btn = wx.Button(self, label="结束计时")
        self.elapsed_time_label = wx.StaticText(self, label="", size=(300, -1), style=wx.ALIGN_CENTER)

        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.update_elapsed_time, self.timer)
        self.timer.Start(1000)  # 每1000毫秒（1秒）更新一次

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add((-1, 24))
        vbox.Add(intro, flag=wx.LEFT, border=20)
        vbox.Add((-1, 24))

        vbox.Add(self.elapsed_time_label, proportion=1, flag=wx.ALIGN_CENTER)
        vbox.Add((-1, 24))
        vbox.Add(self.submit_btn, flag=wx.ALIGN_CENTER | wx.BOTTOM, border=20)

        self.SetSizer(vbox)

        self.Bind(wx.EVT_BUTTON, self.OnClick, self.submit_btn)
        self.Bind(wx.EVT_CHAR_HOOK, self.OnChar)

        # 图标
        button_icon(self, "日程安排.png")
        self.Center()
        # self.setPosition()

    def setPosition(self):
        # 获取屏幕尺寸
        screen_width, screen_height = wx.DisplaySize()
        # 获取对话框尺寸
        dialog_width, dialog_height = self.GetSize()

        # 计算对话框在屏幕右上角的位置
        x = screen_width - dialog_width
        y = 0
        # 设置对话框位置
        self.SetPosition((x, y))

    def update_elapsed_time(self, event):
        current_time = time.time()
        elapsed_time = current_time - self.start_time
        formatted_time = T.time_s2(elapsed_time)
        self.elapsed_time_label.SetLabel(f"计时中：{formatted_time}")

    def OnClick(self, event):
        self.timer.Stop()
        self.end_time = time.time()  # 记录结束时间
        TF.setlog(self.proj, self.begin_t)
        elapsed_time = self.end_time - self.start_time
        s = "您此次花费的的时间为: " + T.time_s2(elapsed_time)
        C.change_3(file_path, self.proj, elapsed_time)
        dlg = ResDialog(None, 2, s)
        self.Close()
        dlg.ShowModal()
        dlg.Destroy()

    def OnChar(self, event):
        keycode = event.GetKeyCode()
        if keycode == wx.WXK_RETURN or keycode == wx.WXK_NUMPAD_ENTER:
            self.OnClick(event)
        else:
            event.Skip()





class DelDialog(wx.Dialog):
    def __init__(self, parent, id):
        super(DelDialog, self).__init__(parent, id, "删除记录", size=(350, 250))
        self.app = wx.GetApp()
        self.panel = self.app.frame

        # 图标
        button_icon(self, "历史数据.png")
        self.Center()

        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(self, label="所要删除的项目名称：")
        hbox1.Add(st1, flag=wx.LEFT | wx.ALIGN_CENTER_VERTICAL, border=20)
        self.tc1 = wx.TextCtrl(self)
        hbox1.Add(self.tc1, flag=wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, border=8)

        vbox.Add((-1, 24))
        vbox.Add(hbox1, flag=wx.EXPAND)
        vbox.Add((-1, 24))
        info1, info2 = C.show_projs()
        st4 = wx.StaticText(self, label=info1)
        st5 = wx.StaticText(self, label=info2)
        st5.Wrap(280)
        vbox.Add(st4, flag=wx.LEFT, border=20)
        vbox.Add((-1, 4))
        vbox.Add(st5, flag=wx.LEFT, border=28)
        self.submit = wx.Button(self, label="提交")
        vbox.Add((-1, 30))
        vbox.Add(self.submit, flag=wx.ALIGN_CENTER)

        self.SetSizer(vbox)

        self.Bind(wx.EVT_BUTTON, self.OnClick, self.submit)
        self.Bind(wx.EVT_CHAR_HOOK, self.OnChar)



    def OnClick(self, event):
        proj = self.tc1.GetValue()
        C.del_2(file_path, proj)
        info = C.show_info(file_path)
        dlg = RecDialog(None, -1, info, "项目记录")
        self.Close()
        dlg.ShowModal()
        dlg.Destroy()

    def OnChar(self, event):
        keycode = event.GetKeyCode()
        if keycode == wx.WXK_RETURN or keycode == wx.WXK_NUMPAD_ENTER:
            self.OnClick(event)
        else:
            event.Skip()


class AddDialog(wx.Dialog):
    """添加项目对话框"""
    def __init__(self, parent, id):
        super(AddDialog, self).__init__(parent, id, "添加项目记录", size=(350, 250))
        self.app = wx.GetApp()
        self.panel = self.app.frame

        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(self, label="添加的项目名称：")
        hbox1.Add(st1, flag=wx.LEFT | wx.ALIGN_CENTER_VERTICAL, border=10)
        self.tc1 = wx.TextCtrl(self)
        hbox1.Add(self.tc1, proportion=1, flag=wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, border=8)
        st2 = wx.StaticText(self, label="时间：")
        hbox1.Add(st2, flag=wx.ALIGN_CENTER_VERTICAL)
        self.tc2 = wx.TextCtrl(self)
        hbox1.Add(self.tc2, proportion=1, flag=wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, border=8)
        st3 = wx.StaticText(self, label="H")
        hbox1.Add(st3, flag=wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, border=10)
        vbox.Add((-1, 24))
        vbox.Add(hbox1, flag=wx.EXPAND)
        vbox.Add((-1, 24))

        info1, info2 = C.show_projs()
        st4 = wx.StaticText(self, label=info1)
        st5 = wx.StaticText(self, label=info2)
        st5.Wrap(280)
        vbox.Add(st4, flag=wx.LEFT, border=20)
        vbox.Add((-1, 4))
        vbox.Add(st5, flag=wx.LEFT, border=28)
        self.submit = wx.Button(self, label="提交")
        vbox.Add((-1, 30))
        vbox.Add(self.submit, flag=wx.ALIGN_CENTER)

        self.SetSizer(vbox)

        self.Bind(wx.EVT_BUTTON, self.OnClick, self.submit)
        self.Bind(wx.EVT_CHAR_HOOK, self.OnChar)

        # 图标
        button_icon(self, "Targets.png")

        self.Center()

    def OnClick(self, event):
        proj = self.tc1.GetValue()
        t = self.tc2.GetValue()
        if t == "":
            return
        C.add_1(file_path, proj, t)
        # dlg = ShowDialog(None, -1)

        info = C.show_info(file_path)
        dlg = RecDialog(None, -1, info, "项目记录")

        self.Close()
        dlg.ShowModal()
        dlg.Destroy()


    def OnChar(self, event):
        keycode = event.GetKeyCode()
        if keycode == wx.WXK_RETURN or keycode == wx.WXK_NUMPAD_ENTER:
            if self.tc2.GetValue() is not None:
                self.OnClick(event)
        else:
            event.Skip()


class RecDialog(wx.Dialog):
    """显示当日记录对话框"""
    def __init__(self, parent, id, info, name):
        super(RecDialog, self).__init__(parent, id, name, size=(350, 500))
        self.app = wx.GetApp()
        self.panel = self.app.frame

        # 图标
        button_icon(self, "饭团.png")

        self.Center()
        sizer1 = wx.GridBagSizer(4, 4)
        tc = wx.TextCtrl(self, style=wx.TE_READONLY | wx.TE_MULTILINE | wx.VSCROLL)
        tc.SetValue(info)
        sizer1.Add(tc, pos=(0, 0), span=(2, 3),
                   flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=25)

        sizer1.AddGrowableCol(1)
        sizer1.AddGrowableRow(1)
        buttonOk = wx.Button(self, wx.ID_OK)
        box = wx.BoxSizer(wx.VERTICAL)
        box.Add(sizer1, proportion=1, flag=wx.EXPAND | wx.TOP | wx.BOTTOM, border=15)
        box.Add((-1, 10))
        box.Add(buttonOk, flag=wx.ALIGN_CENTER | wx.BOTTOM, border=20)
        self.SetSizer(box)


class RecDialog2(wx.Dialog):
    """显示当日记录对话框"""
    def __init__(self, parent, id, info, name):
        super(RecDialog2, self).__init__(parent, id, name, size=(350, 500))
        self.app = wx.GetApp()
        self.panel = self.app.frame

        # 图标
        button_icon(self, "饭团.png")

        self.Center()
        sizer1 = wx.GridBagSizer(4, 4)
        tc = wx.TextCtrl(self, style=wx.TE_READONLY | wx.TE_MULTILINE | wx.VSCROLL)
        tc.SetValue(info)
        sizer1.Add(tc, pos=(0, 0), span=(2, 3),
                   flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=25)

        sizer1.AddGrowableCol(1)
        sizer1.AddGrowableRow(1)
        buttonOk = wx.Button(self, wx.ID_OK)
        buttonPic = wx.Button(self, label="PIC")  # 新增的 PIC 按钮
        buttonPic.Bind(wx.EVT_BUTTON, self.on_pic_button)  # 绑定按钮事件处理函数
        box = wx.BoxSizer(wx.VERTICAL)
        box.Add(sizer1, proportion=1, flag=wx.EXPAND | wx.TOP | wx.BOTTOM, border=15)
        box.Add((-1, 10))

        # 创建一个水平的 BoxSizer 来包含确认按钮和 PIC 按钮
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(buttonOk, flag=wx.ALIGN_CENTER | wx.RIGHT, border=10)
        hbox.Add(buttonPic, flag=wx.ALIGN_CENTER)
        box.Add(hbox, flag=wx.ALIGN_CENTER | wx.BOTTOM, border=20)

        self.SetSizer(box)
        self.pic_frame = None  # 用于存储图片窗口的引用

    def on_pic_button(self, event):
        if self.pic_frame is not None and self.pic_frame.IsShown():
            # 如果图片窗口已经打开并且可见，则关闭它
            self.pic_frame.Close()
            self.pic_frame = None  # 重置图片窗口引用
        else:
            # 否则，显示本地图片
            img = wx.Image(RP_Path, wx.BITMAP_TYPE_ANY)
            frame_size = (img.GetWidth()+20, img.GetHeight()+40)  # 调整窗口大小为图片大小加上一些边距
            self.pic_frame = wx.Frame(None, title="项目时间图示", size=frame_size)
            button_icon(self.pic_frame, "饭团.png")
            panel = wx.Panel(self.pic_frame)
            bmp = wx.Bitmap(img)
            wx.StaticBitmap(panel, -1, bmp, (0, 0))

            screen_size = wx.GetDisplaySize()
            window_size = self.GetSize()
            f_size = self.pic_frame.GetSize()
            x = (screen_size.width - window_size.width - 2 * f_size.width) // 2
            y = (screen_size.height - window_size.height) // 2

            # 设置窗口位置
            self.pic_frame.SetPosition((x, y))
            self.pic_frame.Show()


class DayDialog(wx.Dialog):
    """添加日常记录对话框"""
    def __init__(self, parent, id):
        super(DayDialog, self).__init__(parent, id, "开始日常", size=(350, 250))
        self.app = wx.GetApp()
        self.panel = self.app.frame
        wx.StaticText(self, label="所要进行的活动名称", pos=(20, 24))

        self.proj = wx.TextCtrl(self, pos=(145, 20))
        self.submit_btn = wx.Button(self, label="开始计时", pos=(135, 140))
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.submit_btn)
        self.Bind(wx.EVT_CHAR_HOOK, self.OnChar)

        # 图标
        button_icon(self, "我的流程.png")

        self.Center()
    def OnClick(self, event):
        proj = self.proj.GetValue()
        info = C.change_info(file_path, proj)
        dlg = DtimDialog(None, 1, info, proj)
        self.Close()
        dlg.ShowModal()
        dlg.Destroy()

    def OnChar(self, event):
        keycode = event.GetKeyCode()
        if keycode == wx.WXK_RETURN or keycode == wx.WXK_NUMPAD_ENTER:
            self.OnClick(event)
        else:
            event.Skip()


class DtimDialog(wx.Dialog):
    """日程记录计时对话框"""
    def __init__(self, parent, id, info, proj):
        super(DtimDialog, self).__init__(parent, id, "计时开始", size=(350, 200))
        _, self.begin_t = TF.da_hour()
        self.start_time = time.time()
        self.proj = proj
        self.app = wx.GetApp()
        self.panel = self.app.frame

        wx.StaticText(self, label=info, pos=(20, 24), size=(300, -1))
        self.elapsed_time_label = wx.StaticText(self, label="", pos=(20, 60), size=(300, -1))
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.update_elapsed_time, self.timer)
        self.timer.Start(1000)  # 每1000毫秒（1秒）更新一次


        self.submit_btn = wx.Button(self, label="结束计时", pos=(135, 110))
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.submit_btn)
        self.Bind(wx.EVT_CHAR_HOOK, self.OnChar)

        # 图标
        button_icon(self, "日程安排.png")
        self.setPosition()
        # self.Center()

    def setPosition(self):
        # 获取屏幕尺寸
        screen_width, screen_height = wx.DisplaySize()

        # 获取对话框尺寸
        dialog_width, dialog_height = self.GetSize()

        # 计算对话框在屏幕右上角的位置
        x = screen_width - dialog_width
        y = 0

        # 设置对话框位置
        self.SetPosition((x, y))
    def update_elapsed_time(self, event):
        current_time = time.time()
        elapsed_time = current_time - self.start_time
        formatted_time = T.time_s2(elapsed_time)
        self.elapsed_time_label.SetLabel(f"计时中：{formatted_time}")

    def OnClick(self, event):
        self.timer.Stop()
        self.end_time = time.time()  # 记录结束时间
        TF.setlog(self.proj, self.begin_t)  # 记录至日常记录中

        elapsed_time = self.end_time - self.start_time
        s = "您此次花费的的时间为: " + T.time_s2(elapsed_time)
        dlg = ResDialog(None, 2, s)
        self.Close()
        dlg.ShowModal()
        dlg.Destroy()

    def OnChar(self, event):
        keycode = event.GetKeyCode()
        if keycode == wx.WXK_RETURN or keycode == wx.WXK_NUMPAD_ENTER:
            self.OnClick(event)
        else:
            event.Skip()


class ResDialog(wx.Dialog):
    """生成时间记录显示"""
    def __init__(self, parent, id, info):
        super(ResDialog, self).__init__(parent, id, "时间记录", size=(350, 200))
        self.app = wx.GetApp()
        self.panel = self.app.frame

        tx = wx.StaticText(self, label=info, size=(300, 20), style=wx.ALIGN_CENTER)
        button_ok = wx.Button(self, wx.ID_OK)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add((-1, 50))
        vbox.Add(tx, proportion=1, flag=wx.ALIGN_CENTER)
        vbox.Add(button_ok, flag=wx.ALIGN_CENTER | wx.BOTTOM, border=20)
        self.SetSizer(vbox)

        # 图标
        button_icon(self, "生成报告.png")
        self.Center()


# class TransparentText(wx.StaticText):
#     #继承了wx.Statictext的类，并对相应的方法进行重写;
#     def __init__(self, parent, id=wx.ID_ANY, label='', pos=wx.DefaultPosition, size=(240, 300),
#                  style=wx.TRANSPARENT_WINDOW | wx.ALIGN_LEFT | wx.EXPAND):
#         wx.StaticText.__init__(self, parent, id, label=label, pos=pos, size=size, style=style)
#         # font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD)
#         # self.SetFont(font)
#         self.SetForegroundColour('white')
#         self.Bind(wx.EVT_PAINT, self.on_paint)
#         self.Bind(wx.EVT_ERASE_BACKGROUND, lambda event: None)
#         self.Bind(wx.EVT_SIZE, self.on_size)
#
#     def on_paint(self, event):#重写on_paint可以对控件进行重写重新构造形状
#         bdc = wx.PaintDC(self)
#         dc = wx.GCDC(bdc)
#         font_face = self.GetFont()
#         font_color = self.GetForegroundColour()
#         dc.SetFont(font_face)
#         dc.SetTextForeground(font_color)
#         dc.DrawText(self.GetLabel(), 0, 0)
#
#     def on_size(self, event):
#         self.Refresh()
#         event.Skip()

class TransparentText(wx.StaticText):
    def __init__(self, parent, id=wx.ID_ANY, label='', pos=wx.DefaultPosition, size=wx.DefaultSize,
                 style=wx.TRANSPARENT_WINDOW | wx.ALIGN_LEFT | wx.EXPAND):
        wx.StaticText.__init__(self, parent, id, label=label, pos=pos, size=size, style=style)
        self.SetForegroundColour('white')
        self.text_lines = []
        self.UpdateText(label)
        self.Bind(wx.EVT_ERASE_BACKGROUND, lambda event: None)
        self.Bind(wx.EVT_SIZE, self.on_size)
        self.Bind(wx.EVT_PAINT, self.on_paint)

    def UpdateText(self, text):
        self.text_lines = [text[i:i + 20] for i in range(0, len(text), 20)]
        for i in range(len(self.text_lines)):
            if self.text_lines[i][0] in {"，", "。", "！", "？", ",", ".", "!", "?"}:
                self.text_lines[i-1] += self.text_lines[i][0]
                self.text_lines[i] = self.text_lines[i][1:]
        self.Refresh()

    def on_paint(self, event):
        bdc = wx.PaintDC(self)
        dc = wx.GCDC(bdc)
        font_face = self.GetFont()
        font_color = self.GetForegroundColour()
        dc.SetFont(font_face)
        dc.SetTextForeground(font_color)

        y = 0
        for line in self.text_lines:
            dc.DrawText(line, 0, y+3)
            y += dc.GetCharHeight()

    def on_size(self, event):
        self.Refresh()
        event.Skip()
