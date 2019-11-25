import plots
from sympy import *





x = Symbol('x')
myPlot = plots.MyStandardPlot()
for constant in [-1,Rational(-1,2),0,Rational(1,2),1]:
    myPlot.ygraph(x-x**3/3+constant,[x,-2,2])

myPlot.xgraph((1+0.5*exp(2*x))/(1-0.5*exp(2*x)),[x,-2,-0.20],color=1)
myPlot.xgraph((1+0.25*exp(2*x))/(1-0.25*exp(2*x)),[x,-2,0.15],color=1)
myPlot.xgraph((1+0.125*exp(2*x))/(1-0.125*exp(2*x)),[x,-2,0.48],color=1)
myPlot.xgraph((1+0.0625*exp(2*x))/(1-0.0625*exp(2*x)),[x,-2,0.8],color=1)
myPlot.xgraph((1+0.5*exp(2*x))/(1-0.5*exp(2*x)),[x,0.9,2],color=1)
myPlot.xgraph((1+1.0*exp(2*x))/(1-1.0*exp(2*x)),[x,0.55,2],color=1)
myPlot.xgraph((1+2.0*exp(2*x))/(1-2.0*exp(2*x)),[x,0.25,2],color=1)
myPlot.xgraph((1+4.0*exp(2*x))/(1-4.0*exp(2*x)),[x,-0.1,2],color=1)
myPlot.xgraph((1-0.5*exp(2*x))/(1+0.5*exp(2*x)),[x,-2,2],color=1)
myPlot.xgraph((1-0.25*exp(2*x))/(1+0.25*exp(2*x)),[x,-2,2],color=1)
myPlot.xgraph((1-0.125*exp(2*x))/(1+0.125*exp(2*x)),[x,-2,2],color=1)
myPlot.xgraph((1-0.0625*exp(2*x))/(1+0.0625*exp(2*x)),[x,-2,2],color=1)
myPlot.xgraph((1-exp(2*x))/(1+exp(2*x)),[x,-2,2],color=1)
myPlot.xgraph((1-2*exp(2*x))/(1+2*exp(2*x)),[x,-2,2],color=1)
myPlot.xgraph((1-4*exp(2*x))/(1+4*exp(2*x)),[x,-2,2],color=1)
myPlot.yaxis('left')
myPlot.xaxis('bottom')
myPlot.xticks([-2,-1,0,1,2])
myPlot.yticks([-2,-1,0,1,2])
#myPlot.mathlabel(0.35,0.9,r'y= \sqrt{\sin{x}}')
myPlot.show()
myPlot.saveas('ortho02.png')
myPlot.destroy()



x = Symbol('x')
myPlot = plots.MyStandardPlot()


for constant in [Rational(-8,1),Rational(-4,1),-2,-1,-Rational(1,2), Rational(-1,4),0, Rational(1,4),Rational(1,2), 1, 2,Rational(4,1),Rational(8,1)]:
    start = -2
    if (constant * exp(2) > 2):
        start = -ln(2/constant)
    if (constant * exp(2) < -2):
        start = -ln(-2/constant)
    myPlot.ygraph(constant * exp(-x),(x,start,2))

for constant in [-2,Rational(-3,2),-1,Rational(-1,2),0,Rational(1,2),1,Rational(3,2)]:
    start = -2
    if (Rational(2,1)+constant > 2):
        start = - sqrt(4 - 2*constant)
    myPlot.xgraph(x**2/2+constant,[x,start,-start],color=1)

#myPlot.yfillbetween([0,sqrt(sin(x))],(x,0,pi),samples=400)
#myPlot.ygraph(0,(x,0,pi),color=-1)
#myPlot.xticks([0,pi])
#myPlot.yticks([0,1])
myPlot.yaxis('left')
myPlot.xaxis('bottom')
myPlot.xticks([-2,-1,0,1,2])
myPlot.yticks([-2,-1,0,1,2])
#myPlot.mathlabel(0.35,0.9,r'y= \sqrt{\sin{x}}')
myPlot.show()
myPlot.saveas('ortho01.png')
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
myPlot.saveas('ortho01.png')
myPlot.destroy()
