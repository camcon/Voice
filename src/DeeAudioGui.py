import wx, sys, AudioReciever, AudioSender

def programExit(event):
    sys.exit()

app = wx.App(redirect=True)
mainWin = wx.Frame(None, title="Dee Audio McPingerDinger - Omega Crust Edition", size=(800,600))
panelAction = wx.Panel(mainWin)
connectButton = wx.Button(panelAction, label="Connect")
listenButton = wx.Button(panelAction, label="Listen")
endButton = wx.Button(panelAction, label="Exit")
ipLabel = wx.StaticText(panelAction, label="Enter an IP to connect to: ")
ipText = wx.TextCtrl(panelAction)#| TE_RICH)



listenButton.Bind(wx.EVT_BUTTON, AudioReciever.startListening())
connectButton.Bind(wx.EVT_BUTTON, AudioSender.connect(ipText.GetValue()))
endButton.Bind(wx.EVT_BUTTON, programExit)






actionBox = wx.BoxSizer()
actionBox.Add(connectButton, proportion=0, flag=wx.LEFT, border=5)
actionBox.Add(listenButton, proportion=0, flag=wx.LEFT, border=5)
actionBox.Add(ipLabel, proportion=0, flag=wx.LEFT, border=5)
actionBox.Add(ipText, proportion=0, flag=wx.LEFT, border=5)
actionBox.Add(endButton, proportion=0, flag=wx.LEFT, border=5)




vertBox = wx.BoxSizer(wx.VERTICAL)
vertBox.Add(actionBox, proportion=0, flag=wx.EXPAND | wx.ALL | wx.CENTER, border = 5)
#actionBox.Add(ipLabel, proportion=0, flag=wx.LEFT, border=5)
vertBox.Add(ipLabel, proportion=0, flag=wx.LEFT, border=5)
vertBox.Add(ipText, proportion=0, flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border=5)

mainWin.CreateStatusBar()
panelAction.SetSizer(vertBox)
#mainWin.SetMinSize((1130,320))
vertBox.Fit(mainWin)
mainWin.Show()
app.MainLoop()


