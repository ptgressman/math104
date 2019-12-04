import matplotlib as mpl
import matplotlib.pyplot as plt
import sympy  as sp
import numpy as np

material = {
'red800' : '#C62828','red500' : '#F44336','red100' : '#FFCDD2','red50'  : '#FFEBEE',
'orange800' : '#EF6C00','orange500' : '#FF9800','orange100' : '#FFCC80','orange50'  : '#FFF3E0',
'yellow800' : '#F9A825','yellow500' : '#FFEB3B','yellow100' : '#FFF9C4','yellow50'  : '#FFFDE7',
'green800'  : '#2E7D32','green500' : '#4CAF50','green100' : '#C8E6C9','green50' : '#E8F5E9',
'blue800' : '#1565C0','blue500' : '#2196F3','blue100' : '#BBDEFB','blue50'  : '#E3F2FD',
'deeppurple800' : '#4527A0','deeppurple500' : '#673AB7','deeppurple100' : '#D1C4E9','deeppurple50' : '#EDE7F6',
'gray800' : '#424242','gray500' : '#9E9E9E','gray100' : '#F5F5F5','gray50' : '#FAFAFA'}

mpl.rcParams['text.usetex'] = True

class MyStandardPlot(object):
    def resize(self):
        left, right = plt.xlim()
        bot, top = plt.ylim()
        height = (top - bot) / (right - left) * 4.0
        self.fig.set_size_inches(4.0,height)
    def disk(self,x,y,r):
        c = plt.Circle((x,y),r)
        self.canvas.add_artist(c)
    def arrow(self,x,y,dx,dy):
        dl = dx
        if (dl < 0):
            dl = - dl
        if (dy > dl):
            dl = dy
        elif (-dy > dl):
            dl = -dy
        plt.arrow(x,y,dx,dy,head_length=0.07*dl,head_width=0.07*dl)

    def destroy(self):
        self.fig.clear()
        plt.close(self.fig)
    def __init__(self):
        self.fig = plt.figure()
        self.canvas = plt.axes()
        self.canvas.spines['top'].set_visible(False)
        self.canvas.spines['right'].set_visible(False)
        self.canvas.spines['left'].set_position('zero')
        self.canvas.spines['bottom'].set_position('zero')
        plt.gca().set_aspect('equal',adjustable='box')
        plt.tight_layout(4.0)
        self.fig.set_size_inches(4.0,4.0)
    def plot(self,list1,list2,colorno = 0):
        if (colorno == -1):
            colorname = '#000000'
        if (colorno == 0):
            colorname = material['deeppurple500']
        if (colorno == 1):
            colorname = material['red500']
        if (colorno == 2):
            colorname = material['orange500']
        if (colorno == 3):
            colorname = material['yellow500']
        if (colorno == 4):
            colorname = material['green500']
        if (colorno == 5):
            colorname = material['blue500']
        self.canvas.plot(list1,list2,color=colorname)
    def thinplot(self,list1,list2,lw,colorno = 0):
        if (colorno == -1):
            colorname = '#000000'
        if (colorno == 0):
            colorname = material['deeppurple500']
        if (colorno == 1):
            colorname = material['red500']
        self.canvas.plot(list1,list2,color=colorname,linewidth=lw)
    def fill(self,list1,list2,colorno = 0):
        if (colorno == 0):
            colorname = material['deeppurple100']
        if (colorno == 1):
            colorname = material['red100']
        self.canvas.fill(list1,list2,color=colorname)
    def xaxis(self,descriptor='center'):
        # can be bottom,zero,center,top
        if descriptor == 'bottom':
            self.canvas.spines['bottom'].set_position(('axes',0))
            return
        elif descriptor == 'top':
            self.canvas.spines['bottom'].set_position(('axes',1))
            return
        self.canvas.spines['bottom'].set_position(descriptor)
    def yaxis(self,descriptor='center'):
        # can be left,zero,center,top
        if descriptor == 'left':
            self.canvas.spines['left'].set_position(('axes',0))
            return
        elif descriptor == 'right':
            self.canvas.spines['left'].set_position(('axes',1))
            return
        self.canvas.spines['left'].set_position(descriptor)
    def xticks(self,ticklist):
        rawticks = []
        ticknames = []
        for item in ticklist:
            rawticks.append(float(item))
            ticknames.append(r'$\displaystyle ' + sp.latex(item) + '$')
        plt.xticks(rawticks,ticknames)
    def yticks(self,ticklist):
        rawticks = []
        ticknames = []
        for item in ticklist:
            rawticks.append(float(item))
            ticknames.append(r'$\displaystyle ' + sp.latex(item) + '$')
        plt.yticks(rawticks,ticknames)
    def text(self,x,y,s,horizontal='center',vertical='center'):
        self.canvas.text(x,y,s,fontsize=12,ha=horizontal,va=vertical)
    def mathlabel(self,x,y,s,horizontal='center',vertical='center'):
        totext = r'$\displaystyle ' + s + '$'
        self.canvas.text(x,y,totext,fontsize=12,ha=horizontal,va=vertical)
    def xlim(self,x0,x1):
        plt.xlim(float(x0),float(x1))
    def ylim(self,y0,y1):
        plt.ylim(float(y0),float(y1))
    def saveas(self,filename):
        self.fig.savefig(filename,format='png',dpi=320,bbox_inches='tight',pad_inches=0)
    def show(self):
        plt.show()
    def ygraph(self,func,xdata,samples=100,color=0):
        x = np.linspace(float(xdata[1]),float(xdata[2]),samples)
        y = []
        for xval in x:
            try:
                y.append(float(func.subs(xdata[0],xval)))
            except:
                y.append(float(func))
        self.plot(x,y,color)
    def xgraph(self,func,xdata,samples=100,color=0):
        x = np.linspace(float(xdata[1]),float(xdata[2]),samples)
        y = []
        for xval in x:
            try:
                y.append(float(func.subs(xdata[0],xval)))
            except:
                y.append(float(func))
        self.plot(y,x,color)
    def slopefield(self,func,xdata,ydata,samples=21,length=-1,color=0):
        x = np.linspace(float(xdata[1]),float(xdata[2]),samples)
        y = np.linspace(float(ydata[1]),float(ydata[2]),samples)
        if length <= 0:
            length = (float(xdata[2]) - float(xdata[1]))/float(samples+5)
        for xval in x:
            for yval in y:
                try:
                    slope = float(func.subs(xdata[0],xval).subs(ydata[0],yval))
                except:
                    slope = float(func)
                dx = length / np.sqrt(1.0 + slope*slope)
                dy = dx * slope
                self.thinplot([xval - dx*0.5,xval+dx*0.5],[yval-0.5*dy,yval+0.5*dy],0.5,color)
    def yfillbetween(self,funcs,xdata,samples=100,color=0,closed=True,swap=False):
        x = np.linspace(float(xdata[1]),float(xdata[2]),samples)
        x1 = []
        x2 = []
        y1 = []
        y2 = []
        for xval in x:
            x1.append(xval)
            x2.append(xval)
            try:
                y1.append(float(funcs[0].subs(xdata[0],xval)))
            except:
                y1.append(float(funcs[0]))
            try:
                y2.append(float(funcs[1].subs(xdata[0],xval)))
            except:
                y2.append(float(funcs[1]))
        x2.reverse()
        y2.reverse()
        if swap:
            x3 = x1
            x1 = y1
            y1 = x3
            x3 = x2
            x2 = y2
            y2 = x3
        self.fill(x1+x2,y1+y2,color)
        if not closed:
            self.plot(x1,y1,color)
            self.plot(x2,y2,color)
        else:
            x2.append(x1[0])
            y2.append(y1[0])
            self.plot(x1+x2,y1+y2,color)
    def xfillbetween(self,funcs,xdata,samples=100,color=0,closed=True):
        return self.yfillbetween(funcs,xdata,samples,color,closed,swap=True)


if __name__ == '__main__':
    x = sp.Symbol('x')
    myPlot = MyStandardPlot()
    #myPlot.xlim(-3.3,3.3)
    #myPlot.ylim(-3.3,3.3)
    myPlot.yfillbetween([sp.cos(x)-1,sp.cos(x)],(x,-sp.pi,sp.pi),closed=False)
    myPlot.xticks([-sp.pi,sp.pi])
    myPlot.yticks([-1,1])
    #myPlot.xaxis('center')
    #myPlot.yaxis('center')
    myPlot.math(1.0,0.5,r'y = \cos x')
    myPlot.show()
    #myPlot.saveas('test.svg')
