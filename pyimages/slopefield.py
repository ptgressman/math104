import plots
from sympy import *



x,y = symbols('x,y')
myPlot = plots.MyStandardPlot()

for c in [0.5,0.667,1.0,2.0,8.0,0.25,0.01,-20,-5]:
    myPlot.ygraph(1/(c+x**2),[x,-1.55,1.55])
myPlot.ygraph(1/(-1.5+x**2),[x,-sqrt(0.5),sqrt(0.5)])
myPlot.ygraph(1/(-2+x**2),[x,-1,1])
myPlot.ygraph(1/(-3+x**2),[x,-sqrt(2),sqrt(2)])
myPlot.ygraph(1/(-0.4+x**2),[x,0.9,1.55])
myPlot.ygraph(1/(-0.4+x**2),[x,-1.55,-0.9])
for c in [0.01,0.05,0.15,0.4,0.75,1.0,1.25,1.5,1.75,2]:
    myPlot.xgraph(c*exp(2*y**3/3),[y,-1,2.1],color=1)
    myPlot.xgraph(-c*exp(2*y**3/3),[y,-1,2.1],color=1)
myPlot.xlim(-1.55,1.55)
myPlot.ylim(-1,2.1)
myPlot.xticks([-1,0,1])
myPlot.yticks([-1,0,1])
myPlot.yaxis('left')
myPlot.xaxis('bottom')
myPlot.show()
myPlot.saveas('orthoX02.png')
myPlot.destroy()
quit()

x,y = symbols('x,y')
myPlot = plots.MyStandardPlot()

for x0 in [0.25,0.375,0.5,0.625,0.75,0.875,1.0]:
    myPlot.ygraph(sqrt(x0**4-x**4),[x,-x0,x0],samples=400)
    myPlot.ygraph(-sqrt(x0**4-x**4),[x,-x0,x0],samples=400)
for c in [0,0.333,0.667,1,1.333,2,5.0,5000.0]:
    if c <= 1:
        range = 1
    else:
        range = sqrt(1.0/ln(c))/2.0
    if range > 1.0:
        range = 1.0
    myPlot.ygraph(c*exp(-1/(4*x**2)),[x,0.1,range],color=1)
    myPlot.ygraph(-c*exp(-1/(4*x**2)),[x,0.1,range],color=1)
    myPlot.ygraph(c*exp(-1/(4*x**2)),[x,-range,-0.1],color=1)
    myPlot.ygraph(-c*exp(-1/(4*x**2)),[x,-range,0.1],color=1)
myPlot.xticks([-1,0,1])
myPlot.yticks([-1,0,1])
myPlot.yaxis('left')
myPlot.xaxis('bottom')
myPlot.show()
myPlot.saveas('orthoX01.png')
myPlot.destroy()
quit()

x,y = symbols('x,y')
myPlot = plots.MyStandardPlot()
myPlot.slopefield(x**3-3*x*(y**2),[x,-2,2],[y,-2,2],samples=25)
myPlot.xticks([-2,-1,0,1,2])
myPlot.yticks([-2,-1,0,1,2])
myPlot.ylim(-2.1,2.35)
myPlot.yaxis('left')
myPlot.xaxis('bottom')
myPlot.mathlabel(0.0,2.2,r"y' = x^3 - 3 x y^2")
myPlot.disk(-1,0.625,0.04)
myPlot.text(-1.15,0.625,'A')
myPlot.disk(1.5,0.875,0.04)
myPlot.text(1.65,0.875,'C')
myPlot.disk(1.5,0.125,0.04)
myPlot.text(1.65,0.125,'E')
myPlot.disk(1.5,0.5,0.04)
myPlot.text(1.65,0.5,'D')
myPlot.disk(1.5,1.25,0.04)
myPlot.text(1.65,1.25,'B')
myPlot.disk(1.5,-0.25,0.04)
myPlot.text(1.65,-0.25,'F')

myPlot.show()
myPlot.saveas('connect02.png')
myPlot.destroy()


quit()

x,y = symbols('x,y')
myPlot = plots.MyStandardPlot()
myPlot.slopefield(2*y * (1-y),[x,-1,2],[y,-1,2],samples=25)
myPlot.xticks([-1,0,1,2])
myPlot.yticks([-1,0,1,2])
myPlot.yaxis('left')
myPlot.xaxis('bottom')
myPlot.mathlabel(0.5,2.2,r"y' = 2y(1-y)")
myPlot.disk(-0.5,0.125,0.04)
myPlot.text(-0.65,0.125,'A')
myPlot.disk(1.0,0.875,0.04)
myPlot.text(1.15,0.875,'C')
myPlot.disk(1.0,0.125,0.04)
myPlot.text(1.15,0.125,'E')
myPlot.disk(1.0,0.5,0.04)
myPlot.text(1.15,0.5,'D')
myPlot.disk(1.0,1.125,0.04)
myPlot.text(1.15,1.125,'B')
myPlot.disk(1.0,-0.125,0.04)
myPlot.text(1.15,-0.125,'F')

myPlot.show()
myPlot.saveas('connect01.png')
myPlot.destroy()


quit()

def multifield(whichone):
    x,y = symbols('x,y')
    myPlot = plots.MyStandardPlot()

    myPlot.ygraph(0.5*exp(x*x/2),[x,-1,1],color=1)
    myPlot.ygraph(0.25*exp(-x*x/2),[x,-1,1],color=2)
    myPlot.ygraph(x,[x,-1,1],color=3)
    myPlot.ygraph(-sqrt(0.25**2-x**2),[x,-0.25,0.25],color=4)
    myPlot.ygraph(-sqrt(0.5**2+x**2),[x,-0.9,0.9],color=5)

    myPlot.text(0.95,0.70,'A')
    myPlot.text(0.88,0.95,'C')
    myPlot.text(0.95,0.22,'B')
    myPlot.text(0.92,-0.95,'E')
    myPlot.text(0.32,0,'D')
    if whichone == 4:
        myPlot.slopefield(x*y,[x,-1,1],[y,-1,1],samples=25)
    elif whichone == 2:
        myPlot.slopefield(-x*y,[x,-1,1],[y,-1,1],samples=25)
    elif whichone == 3:
        myPlot.slopefield(x-y+1,[x,-1,1],[y,-1,1],samples=25)
    elif whichone == 1:
        myPlot.slopefield(-x/sqrt(0.5**2+x**2),[x,-1,1],[y,-1,1],samples=25)

    myPlot.xticks([-1,0,1])
    myPlot.yticks([-1,0,1])
    myPlot.yaxis('left')
    myPlot.xaxis('bottom')


#    myPlot.show()
    myPlot.saveas('slope' + str(whichone).zfill(2) +'.png')
    myPlot.destroy()

for index in range(4):
    multifield(index+1)

quit()
