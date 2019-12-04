import plots
from sympy import *


deltay = 4 * pi /13
deltath = atan(exp(2*deltay))
x = Symbol('x')
myPlot = plots.MyStandardPlot()
myPlot.xlim(0,pi*2)
myPlot.ylim(0,2*pi+0.05)
for c in range(9):
   offset = c*deltay
   for cycle in [-1,0,1,2]:
       myPlot.ygraph(offset+ln(abs(cos(x))),(x,cycle*pi-deltath,cycle*pi+deltath),color=1,samples=100)
       myPlot.ygraph(offset+ln(abs(sin(x))),(x,(cycle+0.5)*pi-deltath,(cycle+0.5)*pi+deltath),color=1,samples=100)
# offset = 3
# myPlot.ygraph(offset+ln(abs(sin(x))),(x,pi/4,3*pi/4))
# myPlot.ygraph(offset+ln(abs(cos(x))),(x,3*pi/4,5*pi/4))
# myPlot.ygraph(offset+ln(abs(sin(x))),(x,5*pi/4,7*pi/4))
# myPlot.ygraph(offset+ln(abs(cos(x))),(x,7*pi/4,9*pi/4))
myPlot.xticks([0,2*pi])
myPlot.yticks([0,2*pi])
myPlot.yaxis('left')


myPlot.show()
myPlot.saveas('test.png')
myPlot.destroy()
