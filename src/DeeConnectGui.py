import wx, sys, AudioReciever, AudioSender, pyaudio, socket, StreamFactory

def programExit(event):
    sys.exit()
def connect(event):
    #host = '10.120.36.193'
    host = ipText.GetValue()
    port = 8080
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        print 'connecting to ', host
        sock.connect((host, port))
        print 'Connected to:', host
    except Exception as ex:
        print ex
        
    stream = StreamFactory.makeInputStream()
    outStream = StreamFactory.makeOutputStream()
    CHUNK = 1024

    #startTime = time.time()
    #endTime = startTime + 3
    message = ""

    # Continuous audio stream:
    print 'starting audio stream'
    while True:
        data = stream.read(CHUNK)
        sock.send(data)
    print 'writing message'
        
app = wx.App(redirect=True)
mainWin = wx.Frame(None, title="Dee Audio McPingerDinger - Omega Crust Edition", size=(800,600))
panelAction = wx.Panel(mainWin)
connectButton = wx.Button(panelAction, label="Connect")
endButton = wx.Button(panelAction, label="Exit")
ipLabel = wx.StaticText(panelAction, label="Enter an IP to connect to: ")
ipText = wx.TextCtrl(panelAction)#| TE_RICH)



connectButton.Bind(wx.EVT_BUTTON, connect)
endButton.Bind(wx.EVT_BUTTON, programExit)






actionBox = wx.BoxSizer()
actionBox.Add(connectButton, proportion=0, flag=wx.LEFT, border=5)
actionBox.Add(ipLabel, proportion=0, flag=wx.LEFT, border=5)
actionBox.Add(ipText, proportion=0, flag=wx.LEFT, border=5)
actionBox.Add(endButton, proportion=0, flag=wx.LEFT, border=5)




vertBox = wx.BoxSizer(wx.VERTICAL)
vertBox.Add(actionBox, proportion=0, flag=wx.EXPAND | wx.ALL | wx.CENTER, border = 5)
vertBox.Add(ipLabel, proportion=0, flag=wx.LEFT, border=5)
vertBox.Add(ipText, proportion=0, flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border=5)

mainWin.CreateStatusBar()
panelAction.SetSizer(vertBox)
vertBox.Fit(mainWin)
mainWin.Show()
app.MainLoop()


