import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog


#página guia para la aplición:
#https://stephendata.science.blog/2020/02/07/programacion-lineal-con-python/

#Problemas tomados de:
# F. Hillier and G. Lieberman, (2010), Introducción a la investigación de operaciones.
# .México, D.F. McGraw-Hill Novena edición p.71-74

#3.1-5 Maximizar

#   Z = 2 X1 + X2

#sujeta a

#          X2 <= 10
# 2 X1 + 5 X2 <= 60
#   X1 +   X2 <= 18
# 3 X1 +   X2 <= 44

c = np.array ([-2.0, -1.0])
A = np.array ([[0,1],[2,5],[1,1],[3,1]])
b = np.array ([10,60,18,44])

res = linprog(c, A, b, method = "revised simplex")
print (res)


#3.4-8 Minimizar
# Z = 40 X1 + 50 X2

#sujeto a:

#  2X1 + 3 X2 >= 30
#   X1 +   X2 >= 12
#  2X1 +   X2 >= 20


cost = np.array ([40.0 , 50.0])
restric = np.array ([[-2,-3],[-1,-1],[-2,-1]])
coLibres = np.array ([-30,-12,-20])

sol = linprog (cost, restric, coLibres, method = "revised simplex")
print (sol)


#función que grafica la región solución
def plot_constructor(c,A,b,limites,zz):
    N = A.shape[0]
    print("Number of contraints inequalities: ", N)
    plt.figure()
    plt.title("Cost:  z = "+ " + ".join([str(x)+" x"+str(i+1) for i,x in enumerate(c)]))
    X = np.linspace(0,15)
    for i in range(0,N):
        c_txt = " + ".join([str(x)+" x"+str(i+1) for i,x in enumerate(A[i,:])]) + " <= " + str(b[i])
        plt.plot(X, -X*(A[i,0]/A[i,1]) + b[i]/A[i,1] ,label = c_txt ) 
 
    for j in range(zz[0],zz[1], zz[2]):
        c_txt = "z = " + str(j)
        plt.plot(X, -X*(c[0]/c[1]) + (j/c[1]), "--" ,label = c_txt ) 
         
    res = linprog(c, A, b, method="revised simplex")
    plt.plot(res.x[0],res.x[1],"ro", label="Solucion")
     
    plt.xlim(0,limites[0])
    plt.ylim(0,limites[1])
    plt.legend()
    plt.grid()
    plt.show()


#gráfica del problema de maximización
plot_constructor(c,A,b,[20,20],[-30,0,5])

plot_constructor(cost, restric, coLibres, [20,20], [300,1000,100])

