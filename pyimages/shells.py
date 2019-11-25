import plots
from sympy import *



x = Symbol('x')
myPlot = plots.MyStandardPlot()

myPlot.yfillbetween([-1+x+sqrt(1+x**2),sqrt(1+x**2)],(x,-1,1),samples=400)
myPlot.xgraph(1,(x,-2+sqrt(2),sqrt(2)),color=-1)
myPlot.xticks([-1,0,1])
myPlot.yticks([0,1])
myPlot.yaxis('left')
myPlot.mathlabel(0.2,-0.4,r'y=-1+x+\sqrt{1+x^2}')
myPlot.mathlabel(0.0,1.2,r'y=\sqrt{1+x^2}')


#myPlot.resize()
myPlot.show()
myPlot.saveas('shell04.png')
myPlot.destroy()

quit()


x = Symbol('x')
myPlot = plots.MyStandardPlot()

myPlot.yfillbetween([sqrt(1-x**2),1],(x,0,1),samples=400)
myPlot.xgraph(0,(x,0,1),color=-1)
myPlot.xticks([0,1])
myPlot.yticks([0,1])
myPlot.yaxis('left')
myPlot.xlim(-0.005,1.05)
myPlot.ylim(0,1.05)
myPlot.mathlabel(0.6,0.55,r'y=\sqrt{1-x^2}')


#myPlot.resize()
myPlot.show()
myPlot.saveas('shell03.png')
myPlot.destroy()

quit()

x = Symbol('x')
myPlot = plots.MyStandardPlot()

myPlot.xfillbetween([sqrt(x),x+sqrt(x)],(x,0,1),samples=400)
myPlot.ygraph(1,(x,0,2),color=-1)
myPlot.xticks([0,2])
myPlot.yticks([0,1])
myPlot.yaxis('left')
myPlot.mathlabel(0.6,0.75,r'x=\sqrt{y}')
myPlot.mathlabel(1.5,0.45,r'x=y+\sqrt{y}')
myPlot.xlim(0,2.1)


#myPlot.resize()
myPlot.show()
myPlot.saveas('shell02.png')
myPlot.destroy()

quit()

x = Symbol('x')
myPlot = plots.MyStandardPlot()

myPlot.yfillbetween([-sqrt(1-x**2),sqrt(1-x**2)],(x,0,1),samples=400)
myPlot.xgraph(0,(x,-1,1),color=-1)
myPlot.xticks([0,1])
myPlot.yticks([-1,0,1])
myPlot.yaxis('left')
myPlot.mathlabel(0.9,0.95,r'y= \sqrt{1-x^2}')
myPlot.mathlabel(0.9,-0.95,r'y= -\sqrt{1-x^2}')
myPlot.xlim(-0.1,1.3)

myPlot.resize()
myPlot.show()
myPlot.saveas('shell01.png')
myPlot.destroy()
