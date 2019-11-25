import plots
from sympy import *



x = Symbol('x')
myPlot = plots.MyStandardPlot()

myPlot.yfillbetween([0,sqrt(sin(x))],(x,0,pi),samples=400)
myPlot.ygraph(0,(x,0,pi),color=-1)
myPlot.xticks([0,pi])
myPlot.yticks([0,1])
myPlot.yaxis('left')
myPlot.mathlabel(0.35,0.9,r'y= \sqrt{\sin{x}}')
myPlot.show()
myPlot.saveas('disksin.png')
myPlot.destroy()
print integrate(pi*(sin(x)),(x,0,pi))

quit()

x = Symbol('x')
myPlot = plots.MyStandardPlot()

myPlot.yfillbetween([x**2/4,x/2],(x,0,2),samples=400)
myPlot.xgraph(0,(x,0,1),color=-1)
myPlot.xticks([0,2])
myPlot.yticks([0,1])
myPlot.yaxis('left')
myPlot.mathlabel(0.65,0.5,r'\displaystyle y= \frac{1}{2} x')
myPlot.mathlabel(1.75,0.5,r'\displaystyle y= \frac{1}{4} x^2')

myPlot.show()
myPlot.saveas('washer1.png')
myPlot.destroy()
