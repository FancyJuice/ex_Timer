import wx


class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(350, 500))

        self.InitUI()
        self.Centre()

    def InitUI(self):

        panel = wx.Panel(self)
        sizer1 = wx.GridBagSizer(4, 4)

        # text = wx.StaticText(panel, label="Rename To")
        # sizer.Add(text, pos=(0, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=5)
        info = "这是一个带自动换行的文本标签。" * 40
        tc = wx.TextCtrl(panel, style=wx.TE_READONLY | wx.TE_MULTILINE | wx.VSCROLL)
        tc.SetValue(info)
        sizer1.Add(tc, pos=(1, 0), span=(2, 3),
                  flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=25)

        sizer1.AddGrowableCol(1)
        sizer1.AddGrowableRow(2)
        buttonOk = wx.Button(panel, wx.ID_OK)
        # sizer1.Add(buttonOk, pos=(3, 1), flag=wx.ALIGN_CENTER | wx.BOTTOM, border=10)
        # sp = wx.StaticText(panel)
        # sizer.Add(sp, pos=(3, 2), flag=wx.EXPAND)
        box = wx.BoxSizer(wx.VERTICAL)
        box.Add(sizer1, proportion=1, flag=wx.EXPAND | wx.TOP | wx.BOTTOM, border=10)
        box.Add(buttonOk, flag=wx.ALIGN_CENTER | wx.BOTTOM, border=10)
        panel.SetSizer(box)


def main():

    app = wx.App()
    ex = Example(None, title='Rename')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()