from sympy import *
import sympy
from sympy.plotting import plot
import numpy as np
sympy.init_printing(use_unicode=True)
x=Symbol('x')
#Ejemplos de funciones: ("2*sin(x)-((x**2)/10)") con x=2.5
funcion=input("Ingresala funcion: ")
numeroAct=float(input("Ingrese el valor inicial: "))

derivada1=diff(funcion,x)
derivada2=diff(funcion,x,2)
derivada1.expand
derivada2.expand
print("Funcion: ",funcion)
print("Primera derivada: ",derivada1)
print("Segunda derivada: ",derivada2)
iteraccion=0
error=100
numeroAnt=numeroAct
#numeroAct=-2
ndev1=derivada1.evalf(subs={x:numeroAct})
ndev2=sympy.sympify(derivada2).subs(x,numeroAct);

while error>1 and iteraccion<=10:
    ndev1=sympy.sympify(derivada1).subs(x,numeroAct);
    ndev2=sympy.sympify(derivada2).subs(x,numeroAct);
    numeroAnt=numeroAct   
    numeroAct=(numeroAct-(ndev1/ndev2))
    if numeroAnt==numeroAct:
        error=100        
    else:
        error=abs((numeroAnt-numeroAct)/numeroAnt)*100        
    print("Iteracion: ",iteraccion," Raiz: ",round(numeroAct,5), " El error es de: ",round(error,5))
    
    iteraccion+=1  

ejey=sympy.sympify(funcion).subs(x,numeroAct);
minOmax=(derivada2.evalf(subs={x:numeroAct}))
print('Las coordenadas del punto son: (',numeroAct,' , ',ejey,')')
if minOmax>=0:
    print("Es un valor  minimo")
else:
    print ('Es un valor maximo')

print('Las coordenadas del punto son: (',numeroAct,' , ',ejey,')')
grafica=plot(funcion,"x" ,autoscale=True );
print("Punto mas general")
#Metodo que nos retorna evaluacion de un numero en la función
def graf (v):
    return sympy.sympify(funcion).subs(x,v);
        
a=[]
b=[]
limiteI=round(numeroAct)-3
limiteS=round(numeroAct)+3
for i in np.linspace(int(limiteI),int(limiteS),100):
    a.append(i);
    b.append(graf(i));

import matplotlib;
from matplotlib import pyplot;

pyplot.plot(a,b, color='black');
pyplot.plot(numeroAct,ejey,'o', color='blue');
pyplot.axhline(0, color="black");
pyplot.axvline(0, color="black");
pyplot.show();