import numpy as np
from cvxopt import glpk
from cvxopt.base import matrix as m

c = m([-80000, -76000, -55000],tc='d')
G = m([ [13 ,15, 7],[12 ,10, 9],[0 ,12, 4] ], tc='d')
h = m([2000 ,1500 ,1200],tc='d')
sol = glpk.ilp(c, G.T, h, I=set([0,1, 2]))
print('Los valores óptimos de las variables son: {0}n'.format(sol[1]))
if sol[0]=='optimal':
    print('El valor óptimo es {0}'.format((-c.T*sol[1])[0]))
# El valor óptimo debemos transponerlo y cambiarle el signo, estamos maximizando.
 
else:
    print('El problema no devolvió una solución óptima. El estado del solucionador fue {0}'.format(sol[0]))

#[-1 ,0 ,0],[0 ,-1, 0],[0, 0 , 1]


