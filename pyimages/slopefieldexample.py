import plots
from sympy import *


x,y = symbols('x,y')
myPlot = plots.MyStandardPlot()
myPlot.slopefield(-x*y,[x,-2,2],[y,-2,2],samples=25)
myPlot.ygraph(2*exp(-x*x/2),[x,-2,2],samples=100,color=1)
myPlot.ygraph(-2*x/1.5*exp(-x*x/2),[x,-2,2],samples=100,color=2)
myPlot.ygraph(2*exp(-x*x/2-x-1.5),[x,-2,2],samples=100,color=3)
myPlot.xticks([-2,-1,0,1,2])
myPlot.yticks([-2,-1,0,1,2])
myPlot.ylim(-2.1,2.35)
myPlot.xlim(-2.05,2.05)
myPlot.yaxis('left')
myPlot.xaxis('bottom')
myPlot.mathlabel(0.0,2.2,r"y' = - x y")
myPlot.disk(-1.5,0.65,0.05)
myPlot.text(-1.65,0.65,'A')
myPlot.disk(-1.5,0.0,0.05)
myPlot.text(-1.65,0.0,'B')
myPlot.disk(-1.5,-0.65,0.05)
myPlot.text(-1.65,-0.65,'C')

myPlot.disk(1.5,0.65,0.05)
myPlot.text(1.65,0.65,'D')
myPlot.disk(1.5,0.0,0.05)
myPlot.text(1.65,0.0,'E')
myPlot.disk(1.5,-0.65,0.05)
myPlot.text(1.65,-0.65,'F')


myPlot.show()
myPlot.saveas('slopeX01.png')
myPlot.destroy()


quit()
