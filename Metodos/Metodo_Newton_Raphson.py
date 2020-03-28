
#Nombre: Metodo de Newton para maximos y minimos.
#Autor: Didier Alejandro Martinez
#Github: Caiel3

from sympy import *
import sympy
from sympy.plotting import plot
import numpy as np
import matplotlib;
from matplotlib import pyplot;

sympy.init_printing(use_unicode=True)
x=Symbol('x')
#Ejemplos de funciones: ("2*sin(x)-((x**2)/10)") con x=2.5
funcion=input("Ingresala funcion: ")
numeroAct=float(input("Ingrese el valor inicial: "))

derivada1=diff(funcion,x)
derivada2=diff(funcion,x,2)
derivada1.expand
derivada2.expand
#Mostramos la informacion de la función para el metodo.
print("Funcion: ",funcion)
print("Primera derivada: ",derivada1)
print("Segunda derivada: ",derivada2)

iteraccion=0
error=100
numeroAnt=numeroAct
ndev1=derivada1.evalf(subs={x:numeroAct})
ndev2=sympy.sympify(derivada2).subs(x,numeroAct);
# Realizamos la interaciones del metodo
while error>1 and iteraccion<=10:
    ndev1=sympy.sympify(derivada1).subs(x,numeroAct);
    ndev2=sympy.sympify(derivada2).subs(x,numeroAct);
    numeroAnt=numeroAct   
    numeroAct=(numeroAct-(ndev1/ndev2))
    if numeroAnt==numeroAct:
        error=100        
    else:
        error=abs((numeroAnt-numeroAct)/numeroAnt)*100        
    print("Iteracion: ",iteraccion," Raiz: ",round(numeroAct,5), " El error es de: ",round(error,5),"%")
    
    iteraccion+=1  

#Evaluamos para encontar el punto y si este es maximo o minimo
ejey=sympy.sympify(funcion).subs(x,numeroAct);
minOmax=(derivada2.evalf(subs={x:numeroAct}))

#Comprovamos si es un valor minimo o maximo
print('Las coordenadas del punto son: (',numeroAct,' , ',ejey,')')
if minOmax>=0:
    print("Es un valor  minimo")
else:
    print ('Es un valor maximo')



#Metodo que nos retorna evaluacion de un numero en la función
def graf (v):
    return sympy.sympify(funcion).subs(x,v);
        
a=[]
b=[]
limiteI=round(numeroAct)-3
limiteS=round(numeroAct)+3
#GRAFICAMOS
#Generamos los valores para graficar
for i in np.linspace(int(limiteI),int(limiteS),100):
    a.append(i);
    b.append(graf(i));


# Completamos el nombre de la funcion
funcion='Grafica: '+funcion+' Punto: ('+str(numeroAct)+','+str(ejey)+')'
pyplot.plot(a,b, color='black');
pyplot.plot(numeroAct,ejey,'o', color='blue');
pyplot.axhline(0, color="black");
pyplot.axvline(0, color="black");
pyplot.title(str(funcion))
pyplot.show();