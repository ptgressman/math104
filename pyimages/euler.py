import plots
from sympy import *



x = Symbol('x')
myPlot = plots.MyStandardPlot()

myPlot.ygraph(1-x/2,(x,0,1))
myPlot.disk(0,1,0.02)
myPlot.disk(1,0.5,0.02)
myPlot.xticks([0,1])
myPlot.yticks([0,1])
myPlot.yaxis("left")
myPlot.canvas.text(0.5,0.70,r'slope = $f(0,1)$',rotation=-26.575,ha='center',fontsize=12)


#myPlot.mathlabel(0.0,1.2,r'y=\sqrt{1+x^2}')


#myPlot.resize()
myPlot.show()
myPlot.saveas('euler01.png')
myPlot.destroy()


x = Symbol('x')
myPlot = plots.MyStandardPlot()

myPlot.ygraph(1-x/2,(x,0,1))
myPlot.ygraph(3/4-x/4,(x,1,2))
myPlot.disk(0,1,0.02)
myPlot.disk(1,0.5,0.02)
myPlot.disk(2,0.25,0.02)
myPlot.xticks([0,1,2])
myPlot.yticks([0,1])
myPlot.yaxis("left")
#myPlot.canvas.text(0.5,0.70,r'slope = $f(0,1)$',rotation=-26.575,ha='center',fontsize=12)


#myPlot.mathlabel(0.0,1.2,r'y=\sqrt{1+x^2}')


#myPlot.resize()
myPlot.show()
myPlot.saveas('euler02.png')
myPlot.destroy()

x = Symbol('x')
myPlot = plots.MyStandardPlot()

myPlot.ygraph(1-x/2,(x,0,1))
myPlot.ygraph(3/4-x/4,(x,1,2))
myPlot.ygraph(4/8-x/8,(x,2,3))
myPlot.disk(0,1,0.02)
myPlot.disk(1,0.5,0.02)
myPlot.disk(2,0.25,0.02)
myPlot.disk(3,0.125,0.02)
myPlot.xticks([0,1,2,3])
myPlot.yticks([0,1])
myPlot.yaxis("left")
#myPlot.canvas.text(0.5,0.70,r'slope = $f(0,1)$',rotation=-26.575,ha='center',fontsize=12)


#myPlot.mathlabel(0.0,1.2,r'y=\sqrt{1+x^2}')


#myPlot.resize()
myPlot.show()
myPlot.saveas('euler03.png')
myPlot.destroy()
