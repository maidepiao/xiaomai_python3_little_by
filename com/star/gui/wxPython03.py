import wx

app = wx.App()

frame = wx.Frame(parent=None,title='小麦GUI',pos=(500,300),size=(500,300))
panel = wx.Panel(frame)

title = wx.StaticText(panel,label='欢迎登陆',pos=(200,50))
font = wx.Font(16,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL)
title.SetFont(font)

user = wx.StaticText(panel,label='账号',pos=(100,90))
user_input = wx.TextCtrl(panel,pos=(150,90),size=(100,25))
pswd = wx.StaticText(panel,label='密码',pos=(100,150))
pswd_input = wx.TextCtrl(panel,pos=(150,150),size=(100,25))

wx.Button(panel,label='确定',pos=(150,200))
wx.Button(panel,label='取消',pos=(250,200))


frame.Show()
app.MainLoop()