import wx, sys, AudioReciever, AudioSender, pyaudio, socket, StreamFactory

def programExit(event):
    sys.exit()
def startListening(event):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    # Socket setup
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('', 8080))
    sock.listen(5)
    print "Client running on ",sock.getsockname()
    #allsocks = [listener]

    # Main:
    outStream = StreamFactory.makeOutputStream()
    conn, addr = sock.accept()
    print 'New connection from ', addr
    data = conn.recv(1024)

    #a = 1
    while data != '':
        outStream.write(data)
        data = conn.recv(1024)
        #a = a+1
        #print "Packy: ", a
        
    print "all done"
    
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
listenButton = wx.Button(panelAction, label="Listen")
endButton = wx.Button(panelAction, label="Exit")
ipLabel = wx.StaticText(panelAction, label="Enter an IP to connect to: ")
ipText = wx.TextCtrl(panelAction)#| TE_RICH)



listenButton.Bind(wx.EVT_BUTTON, startListening)
connectButton.Bind(wx.EVT_BUTTON, connect)
#listenButton.Bind(wx.EVT_BUTTON, printSomethingElse)
#connectButton.Bind(wx.EVT_BUTTON, printSomething)
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


