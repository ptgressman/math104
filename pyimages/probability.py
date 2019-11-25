import plots
from sympy import *



x = Symbol('x')
myPlot = plots.MyStandardPlot()

myPlot.yfillbetween([exp(-x**2),0],(x,-0.5,0.5),samples=400)
myPlot.ygraph(exp(-x**2),(x,-2,2),color=-1)
myPlot.xticks([])
myPlot.yticks([])
myPlot.yaxis("left")
myPlot.mathlabel(1.2,0.5,r'f(x)')
myPlot.mathlabel(-0.5,-0.14,'c')
myPlot.mathlabel(0.5,-0.14,'d')
myPlot.arrow(-0.95,-0.4,-0.9,0)
myPlot.arrow(0.95,-0.4,0.9,0)
myPlot.text(0,-0.4,r'possible values of $X$')
myPlot.canvas.text(-2.4,0.75,'likelihood',fontsize=12,rotation=90)
#myPlot.mathlabel(0.0,1.2,r'y=\sqrt{1+x^2}')

myPlot.ylim(-0.5,1.1)
#myPlot.resize()
myPlot.show()
myPlot.saveas('probability01.png')
myPlot.destroy()

quit()
