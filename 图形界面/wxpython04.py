import wx

class MyFrame(wx.Frame):
    def __init__(self,parent,fid,title):
        wx.Frame.__init__(self,parent,fid,title,size=(300,200))
        panel = wx.Panel(self)
        self.title = wx.StaticText(panel,label='用户登陆')
        self.user_label = wx.StaticText(panel, label='账号')
        self.user_input = wx.TextCtrl(panel,style=wx.TE_LEFT)
        self.pswd_label = wx.StaticText(panel, label='密码')
        self.pswd_input = wx.TextCtrl(panel, style=wx.TE_PASSWORD)
        self.bt_submit = wx.Button(panel, label='确定')
        self.bt_reset = wx.Button(panel, label='取消')

        self.bt_submit.Bind(wx.EVT_BUTTON,self.bt_submit_click)

        layout_u = wx.BoxSizer(wx.HORIZONTAL)
        layout_u.Add(self.user_label,proportion=0,flag=wx.ALL,border=10)
        layout_u.Add(self.user_input, proportion=1, flag=wx.ALL, border=10)

        layout_p = wx.BoxSizer(wx.HORIZONTAL)
        layout_p.Add(self.pswd_label, proportion=0, flag=wx.ALL, border=10)
        layout_p.Add(self.pswd_input, proportion=1, flag=wx.ALL, border=10)

        layout_b = wx.BoxSizer(wx.HORIZONTAL)
        layout_b.Add(self.bt_submit, proportion=0, flag=wx.ALIGN_LEFT, border=10)
        layout_b.Add(self.bt_reset, proportion=0, flag=wx.ALIGN_CENTER, border=10)

        layout_t = wx.BoxSizer(wx.VERTICAL)
        layout_t.Add(self.title,proportion=0,flag=wx.ALIGN_CENTER|wx.TOP,border=20)
        layout_t.Add(layout_u,proportion=0,flag=wx.EXPAND|wx.RIGHT,border=10)
        layout_t.Add(layout_p,proportion=0,flag=wx.EXPAND|wx.RIGHT,border=10)
        layout_t.Add(layout_b,proportion=0,flag=wx.ALIGN_CENTER,border=20)

        panel.SetSizer(layout_t)

    def bt_submit_click(self,EVENT):
        if self.user_input.GetValue() == '' or self.pswd_input.GetValue() == '':
            wx.MessageBox('请输入用户名，密码')
        elif self.user_input.GetValue() == 'wxpython' and self.pswd_input.GetValue() == '123456':
            wx.MessageBox('登陆成功')
        else:
            wx.MessageBox('用户名或密码不正确')
if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(None,0,'小麦布局')
    frame.Show()
    app.MainLoop()

