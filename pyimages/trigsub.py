import plots
from sympy import *


x = Symbol('x')
myPlot = plots.MyStandardPlot()

myPlot.canvas.axis('off')
myPlot.yfillbetween([0,x],(x,0,1),samples=2)

myPlot.xticks([])
myPlot.yticks([])

myPlot.mathlabel(1.12,0.5,r'\sqrt{x^2-3}')
myPlot.mathlabel(0.35,0.5,r'x')
myPlot.mathlabel(0.5,-0.06,r'\sqrt{3}')
myPlot.mathlabel(0.1,0.04,r'\theta')
myPlot.plot([0.95,0.95,1],[0,0.05,0.05])


#myPlot.mathlabel(0.0,1.2,r'y=\sqrt{1+x^2}')

#myPlot.resize()
myPlot.show()
myPlot.saveas('trigsub03.png')
myPlot.destroy()

quit()

x = Symbol('x')
myPlot = plots.MyStandardPlot()

myPlot.canvas.axis('off')
myPlot.yfillbetween([0,x],(x,0,1),samples=2)

myPlot.xticks([])
myPlot.yticks([])

myPlot.mathlabel(1.05,0.5,r'x')
myPlot.mathlabel(0.35,0.5,r'\sqrt{x^2+5}')
myPlot.mathlabel(0.5,-0.06,r'\sqrt{5}')
myPlot.mathlabel(0.1,0.04,r'\theta')
myPlot.plot([0.95,0.95,1],[0,0.05,0.05])


#myPlot.mathlabel(0.0,1.2,r'y=\sqrt{1+x^2}')

#myPlot.resize()
myPlot.show()
myPlot.saveas('trigsub02.png')
myPlot.destroy()

quit()


x = Symbol('x')
myPlot = plots.MyStandardPlot()

myPlot.canvas.axis('off')
myPlot.yfillbetween([0,x],(x,0,1),samples=2)

myPlot.xticks([])
myPlot.yticks([])

myPlot.mathlabel(1.05,0.5,r'x')
myPlot.mathlabel(0.45,0.5,'3')
myPlot.mathlabel(0.5,-0.06,r'\sqrt{9-x^2}')
myPlot.mathlabel(0.1,0.04,r'\theta')
myPlot.plot([0.95,0.95,1],[0,0.05,0.05])


#myPlot.mathlabel(0.0,1.2,r'y=\sqrt{1+x^2}')

#myPlot.resize()
myPlot.show()
myPlot.saveas('trigsub01.png')
myPlot.destroy()
