from pylab import *
import numpy as np

#Se definen los ejes coordenados
def Ejes():
    Ejex = np.zeros(40)
    Ejey = np.zeros(4)
    aux = np.arange(-20,20,1)
    plt.plot(Ejex, aux, "r-")
    plt.plot(aux, Ejex, "r-")
    xlabel('X')
    ylabel('Y')
    xlim(-10,10)
    ylim(-10,10)
    Text(1,0,'X')

Ejes()
fin= np.arange(-10,10, 0.1)
f = 5-2*fin
a2 = -10
texto1 = text(3.5, 6, r'$f(x)=5-2*X$', fontsize=16)
plt.fill_between(fin, f, a2,
                 facecolor="orange", 
                 color='blue',       
                 alpha=0.2)
#plt.xticks(aux)
#plt.yticks([-]
plt.grid()

show()

Ejes()

fin= np.arange(-10,11, 1)
f = np.array([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5])
a2 = -10
texto1 = text(3.5, 6, r'$y\leq5$', fontsize=16)
plt.fill_between(fin, f, a2,
                 facecolor="orange", 
                 color='blue',       
                 alpha=0.2)
plt.grid()

show()
