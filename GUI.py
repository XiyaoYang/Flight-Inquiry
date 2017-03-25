import wx
from Graph_mid import *
import sys


#Define menu item id
ID_ABOUT = 101 
ID_EXIT  = 110

g = Graph('/Users/youngsee/Documents/2016FALL/CEE505/Final/CEE505Final_Xiyao_Yang/src')

class MainWindow(wx.Frame):
    
    def __init__(self, parent, id, title='Flights Application'):
        wx.Frame.__init__(self, parent, id, title,size=(800,480))
        #Create a panel that fits in the frame
        self.panel = wx.Panel(self)
        #self.panel1 contains left side bar with buttons and comboboxes
        self.panel1 = wx.Panel(self.panel,-1,size=(200,480))
        #self.panel2 contains graph and text control boxe on the right side 
        self.panel2 = wx.Panel(self.panel,-1,size=(600,480))
        #self.panel3 is a child of self.panel2 to resize the graph
        self.panel3 = MyPanel(self.panel2,-1,size=(600,360))
        #Define two combo boxes to create dropdown menus of departure and arrival cities separately
        self.combo1 = wx.ComboBox(self.panel1,choices = g.getAirportCodes(),size = (100,25))
        self.combo2 = wx.ComboBox(self.panel1,choices = g.getAirportCodes(),size = (100,25))
        #Define a text control field with read-only limitation and minimum size
        self.text = wx.TextCtrl(self.panel2,style = wx.TE_MULTILINE|wx.TE_READONLY)
        self.text.SetMinSize((0,120))
              
        #Define a series of box sizers
        self.box1 = wx.BoxSizer(wx.VERTICAL)
        self.box2 = wx.BoxSizer(wx.VERTICAL)
        self.box = wx.BoxSizer(wx.HORIZONTAL)
        self.StartUI(id)
        
    
    def StartUI(self,id):
        
        #Define a series of box sizers in left side bar
        l1_line = wx.BoxSizer(wx.HORIZONTAL)
        l2_line = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer1 = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer2 = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer3 = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer4 = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer5 = wx.BoxSizer(wx.HORIZONTAL)
        
        #Define the text of departure/arrival and fill airport nodes in their drop down menus
        l1 = wx.StaticText(self.panel1, label = "Departure:")          
        l2 = wx.StaticText(self.panel1, label = "Destination:")      
        #Define a search shortest button in the middle and bind it with onSearchShortest method with event handler
        searchShortestBtn = wx.Button(self.panel1,id,'search shortest path', size = (150,20))
        self.Bind(wx.EVT_BUTTON, self.onSearchShortest, searchShortestBtn)   
        #Define a search all button in the middle and bind it with onSearchAll method with event handler
        searchAllBtn = wx.Button(self.panel1,id,'search all path', size = (150,20))
        self.Bind(wx.EVT_BUTTON, self.onSearchAll, searchAllBtn)       
        #Define a reset button in the middle and bind it with onReset method with event handler
        resetBtn = wx.Button(self.panel1,id,'Reset View', size = (150,20))
        self.Bind(wx.EVT_BUTTON, self.onReset, resetBtn)
        #Define a reverse button in the middle and bind it with onReverse method with event handler
        reverseBtn = wx.Button(self.panel1,id,'reverse direction', size = (150,20))
        self.Bind(wx.EVT_BUTTON, self.onReverse, reverseBtn)
        #Define a quit button in the middle and bind it with onExit method with event handler
        quitBtn = wx.Button(self.panel1,id,'Quit', size = (150,20))
        self.Bind(wx.EVT_BUTTON, self.OnExit, quitBtn)        
        #Define separators
        line1 = wx.StaticLine(self.panel1, 0, style=wx.LI_HORIZONTAL,size=(180,3))
        line2 = wx.StaticLine(self.panel1, 0, style=wx.LI_HORIZONTAL,size=(180,3))
        line3 = wx.StaticLine(self.panel1, 0, style=wx.LI_HORIZONTAL,size=(180,3))
        
        #Add above elements to their horizontal sizers 
        l1_line.Add(l1,0,wx.ALL,9)
        l1_line.Add(self.combo1,0,wx.ALL|wx.EXPAND,5)
        l2_line.Add(l2,0,wx.ALL,5)
        l2_line.Add(self.combo2,0,wx.ALL|wx.EXPAND,5)
        btnSizer1.Add(reverseBtn,0,wx.ALL|wx.EXPAND|wx.CENTER,10)
        btnSizer2.Add(searchShortestBtn,0,wx.ALL|wx.EXPAND|wx.CENTER,10)
        btnSizer3.Add(searchAllBtn,0,wx.ALL|wx.EXPAND|wx.CENTER,10)
        btnSizer4.Add(resetBtn,0,wx.ALL|wx.EXPAND|wx.CENTER,10)
        btnSizer5.Add(quitBtn,0,wx.ALL|wx.EXPAND|wx.CENTER,10)
        
        #Add above sizers to a vertical sizer and set the sizer to fit the main frame
        self.box1.Add(l1_line,0,wx.ALL)
        self.box1.Add(l2_line,0,wx.ALL)
        self.box1.Add(btnSizer1,0,wx.CENTER)
        self.box1.Add(line1,0,wx.CENTER)
        self.box1.Add(btnSizer2,0,wx.CENTER)
        self.box1.Add(btnSizer3,0,wx.CENTER)
        self.box1.Add(line2,0,wx.CENTER)
        self.box1.AddStretchSpacer()
        self.box1.Add(btnSizer4,0,wx.CENTER)
        self.box1.AddStretchSpacer()
        self.box1.Add(line3,0,wx.CENTER)
        self.box1.Add(btnSizer5,0,wx.CENTER)
        self.box2.Add(self.panel3,3,wx.LEFT|wx.RIGHT|wx.EXPAND,5)
        self.box2.Add(self.text,1,wx.LEFT|wx.RIGHT|wx.EXPAND,5)
        self.box.Add(self.panel1,0,wx.LEFT,2)
        self.box.Add(self.panel2,1,wx.RIGHT|wx.EXPAND,2)
        
        #Set sizers to panels
        self.panel1.SetSizer(self.box1)
        self.panel2.SetSizer(self.box2)
        self.panel.SetSizer(self.box)
        
        #Define a file menu which has an About dialog and a Quit feature
        filemenu = wx.Menu()
        filemenu.Append(ID_ABOUT, '&About', 'Information about this program' )
        filemenu.AppendSeparator()
        filemenu.Append(ID_EXIT, '&Exit', 'Terminate the program')
        
        #Add the file menu to a menu bar and add the menue bar to the frame content
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, '&File') 
        self.SetMenuBar(menuBar)  
        
        #Bind menu item ids to their seperate methods by event handlers
        wx.EVT_MENU(self, ID_ABOUT, self.OnAbout)  
        wx.EVT_MENU(self, ID_EXIT, self.OnExit)
        
        #Set the position of main frame to center and show the GUI
        self.Center()
        self.Show(True)
    

    def OnAbout(self, e):
        #Define the dialog of About and show the modal, finally detroy when finished
        d = wx.MessageDialog(self, "This Application presents\n"
                           "the shortest path between two airports\n"
                           "Author: Xiyao Yang\n"
                           "Release Datetime: 11/29/2016",
                           "About", wx.OK)
        d.ShowModal() 
        d.Destroy()        
    
    def OnExit(self, e):
        #Exit the application when click Quit
        self.Close(True)
    
    def onSearchShortest(self,e):
        #Refresh text control field to be blank
        self.text.SetValue('') 
        #Compare departure airport to desitination, if the same, return error message
        startID = self.combo1.GetValue()
        endID = self.combo2.GetValue()
        if  startID == endID:
            txt = 'Err: Departure is the same as Destination.'
        elif startID == 'IAH' or endID == 'IAH':
            txt = 'Warning: IAH has no flights.'
        else:
            #If not, get values of selected airports and find their shortest path using methods in Graph class
            output = g.findShortestPath(startID, endID)
            #Format output 
            txt1 = 'The shortest trip from '+startID+' to '+endID + ' takes a total time of '+output['totaltime']+'\n'
            txt2 = ''
            for i in range(len(output['time'])):
                txt2 = txt2 + ('On %s from %s at %s, to %s at %s') \
                % (output['flights'][i],output['airports'][i],output['time'][i][0],output['airports'][i+1],output['time'][i][1]) +'\n'
            txt = txt1+txt2
            
        #Redirect output to text control field
        redir=RedirectText(self.text)
        redir.write(txt)
        sys.stdout=redir
        
        #Bind paint event with OnPaintShortest function defined in MyPanel class, lambda helps convey more parameters into the function
        if startID != endID and startID != 'IAH' and endID != 'IAH':
            self.panel3.Bind(wx.EVT_PAINT, lambda e,s=startID,d=endID :self.panel3.OnPaintShortest(e,s,d))
        
        #Recall the paint event everytime the window is refreshed
        self.Refresh()
    
    def onSearchAll(self,e):
        #Refresh text control field to be blank
        self.text.SetValue('') 
        #Compare departure airport to desitination, if the same, return error message
        if  self.combo1.GetValue() == self.combo2.GetValue():
            txt = 'Err: Departure is the same as Destination.'
        else:
            #If not, get values of selected airports and find their shortest path using methods in Graph class
            output = g.findPathTotalTime(self.combo1.GetValue(), self.combo2.GetValue())
            #Format output 
            txt1 = 'Trips from '+self.combo1.GetValue()+' to '+self.combo2.GetValue()+' has %s options' % len(output)+'\n'
            txt2 = ''
            for i,trip in enumerate(output):
                txt2 = txt2 +'\n'+'Trip option %s takes a total time of %s' % (i+1, trip['totaltime'])
                for i in range(len(trip['time'])):
                    txt2 = txt2 + ('On %s from %s at %s, arrive at %s at %s') \
                        % (trip['flights'][i],trip['airports'][i],trip['time'][i][0],trip['airports'][i+1],trip['time'][i][1]) +'\n'
            txt = txt1+txt2

        #Redirect output to text control field
        redir=RedirectText(self.text)
        redir.write(txt)
        sys.stdout=redir
        self.panel3.Bind(wx.EVT_PAINT, self.panel3.OnPaintAll)
        self.Refresh()
        
        
    
    def onReverse(self,e):
        #Refresh text control field to be blank
        self.text.SetValue('') 
        #Change combo box values
        combo1 = self.combo2.GetValue()
        combo2 = self.combo1.GetValue()
        self.combo1.SetValue(combo1)
        self.combo2.SetValue(combo2)
        e.Skip()
        
    def onReset(self,e):
        #Reset text control filed to blank, comboboxes to first choices, frame size and position to default 
        self.text.SetValue('')
        self.combo1.SetSelection(0)
        self.combo2.SetSelection(0)
        self.SetSize((800,480))
        self.Center()
    
    

class MyPanel(wx.Panel):
    """ class MyPanel creates a panel to draw on, inherits wx.Panel """
    def __init__(self, parent, id, size):
        #create a panel
        wx.Panel.__init__(self, parent, id)
        self.SetBackgroundColour("white")
        
        #Bind paint event to draw the points of cities initially
        self.Bind(wx.EVT_PAINT, self.OnPaint)

    #Paint dots of cities in yellow pen and in the parent panel, coordinates of dots are adjusted by panel size
    def OnPaint(self,e):
        dc = wx.PaintDC(self)
        airports = g.getAirportCodes()
        Max = g.getMax()
        Min = g.getMin()
        Size = self.GetSize()
        c = min(((0.8*Size[0])/(Max[0]-Min[0])),((0.8*Size[1])/(Max[1]-Min[1])))
        x0 = (Size[0]-c*(Max[0]-Min[0]))/2
        y0 = (Size[1]-c*(Max[1]-Min[1]))/2
        for item in airports:
            pos = g.getPosition(item)
            dc.SetPen(wx.Pen('Yellow',10,wx.SOLID))
            x = c*(pos[0]-2600)+x0
            y = c*(4400-pos[1])+y0
            dc.DrawPoint(x,y)
            dc.DrawText(item,x,y) 
    
    #Paint all paths among cities
    def OnPaintAll(self,e):
        dc = wx.PaintDC(self)
        airports = g.getAirportCodes()
        Max = g.getMax()
        Min = g.getMin()
        Size = self.GetSize()
        c = min(((0.8*Size[0])/(Max[0]-Min[0])),((0.8*Size[1])/(Max[1]-Min[1])))
        x0 = (Size[0]-c*(Max[0]-Min[0]))/2
        y0 = (Size[1]-c*(Max[1]-Min[1]))/2
        for item in airports:
            pos = g.getPosition(item)
            dc.SetPen(wx.Pen('Yellow',10,wx.SOLID))
            x = c*(pos[0]-2600)+x0
            y = c*(4400-pos[1])+y0
            dc.DrawPoint(x,y)
            dc.DrawText(item,x,y) 
            flights = g.getAttached(item)
            for i,item2 in enumerate(flights):
                if (i%2) != 0:
                    i = -i
                else:
                    i = i+1
                pos2 = (c*(item2[2]-2600)+x0,c*(4400-item2[3])+y0)
                mid = ((pos2[0]+x)/2,(pos2[1]+y)/2)
                pos3 = (mid[0]+i*5,-(pos2[0]-x)/(pos2[1]-y)*(mid[0]+i*0.1-mid[0])+mid[1])
                dc.SetPen(wx.Pen('Blue',1))
                dc.DrawSpline([(x,y),pos3,pos2])
   
    #Paint the shortest path using red pen
    def OnPaintShortest(self,e,startID,endID):
        dc = wx.PaintDC(self)
        airports = g.getAirportCodes()
        Max = g.getMax()
        Min = g.getMin()
        Size = self.GetSize()
        c = min(((0.8*Size[0])/(Max[0]-Min[0])),((0.8*Size[1])/(Max[1]-Min[1])))
        x0 = (Size[0]-c*(Max[0]-Min[0]))/2
        y0 = (Size[1]-c*(Max[1]-Min[1]))/2
        for item in airports:
            pos = g.getPosition(item)
            dc.SetPen(wx.Pen('Yellow',10,wx.SOLID))
            x = c*(pos[0]-2600)+x0
            y = c*(4400-pos[1])+y0
            dc.DrawPoint(x,y)
            dc.DrawText(item,x,y) 
            flights = g.getAttached(item)
            for i,item2 in enumerate(flights):
                if (i%2) != 0:
                    i = -i
                else:
                    i = i+1
                pos2 = (c*(item2[2]-2600)+x0,c*(4400-item2[3])+y0)
                mid = ((pos2[0]+x)/2,(pos2[1]+y)/2)
                pos3 = (mid[0]+i*5,-(pos2[0]-x)/(pos2[1]-y)*(mid[0]+i*0.1-mid[0])+mid[1])
                dc.SetPen(wx.Pen('Blue',1))
                dc.DrawSpline([(x,y),pos3,pos2])
        
        airports = g.findShortestPath(startID,endID)
        for i,item in enumerate(airports['airports']):
            if i+1 < len(airports['airports']):
                pos1 = g.getPosition(airports['airports'][i])
                x1 = c*(pos1[0]-2600)+x0
                y1 = c*(4400-pos1[1])+y0
                
                pos2 = g.getPosition(airports['airports'][i+1])
                x2 = c*(pos2[0]-2600)+x0
                y2 = c*(4400-pos2[1])+y0
               
                mid = ((x2+x1)/2,(y2+y1)/2)
                pos3 = (mid[0]+1*5,-(x2-x1)/(y2-y1)*(mid[0]+1*0.1-mid[0])+mid[1])
                dc.SetPen(wx.Pen('Red',1))
                dc.DrawSpline([(x1,y1),pos3,(x2,y2)])
            
      
        
class RedirectText(object):
    #Define a class to redirect text to a wx.textctrl
    def __init__(self,aWxTextCtrl):
        self.out=aWxTextCtrl
 
    def write(self,string):
        self.out.WriteText(string)

# define an Application and loop it
app = wx.App()
win = MainWindow(None, -1)
app.MainLoop()
