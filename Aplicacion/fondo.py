from tkinter import *
from tkinter import messagebox
import numpy as np
from cvxopt import glpk
from cvxopt.base import matrix as m

#propiedad raiz de la ventana
raiz =Tk()
#variable que contendrá el número de variables 
nvaria = StringVar()
#variable que contendrá el número de restricciones 
nrest = StringVar()
#variables que contendran los datos de los cuadros de texto
cvari = StringVar() #contendrá los coeficientes de la función objetivo
crest = StringVar()  #contendrá los coeficientes de las variables
cind = StringVar() #variable que contendrá los coeficientes independientes de las restricciones



#funciones

#ventana que muestra el resultado del problema
def mostrar_solu(sol, c):
    raiz.withdraw
    v_sol=Toplevel()
    #se ponen el icono de la aplicación
    v_sol.iconbitmap("bitmap.ico")
    Label(v_sol, text="Función:").grid(row=0,column=0, padx=10,pady=10,columnspan=10)
    if sol[0]=='optimal':
        Label(v_sol, text='El valor óptimo es {0}'.format((-c.T*sol[1])[0])).grid(row=2,column=0, padx=10,pady=10,columnspan=10)
        Label(v_sol, text='Los valores óptimos de las variables son: {0}'.format(sol[1])).grid(row=3,column=0, padx=10,pady=10,columnspan=10)
    else:
        sin_sol=Label(v_sol, text='El problema no devolvió una solución óptima. El estado del solucionador fue {0}'.format(sol[0]))
        sin_sol.grid(row=2,column=0, padx=10,pady=10,columnspan=10)
    

#solucionador del problema
def solucionar(c,G,h):
    sol = glpk.ilp(c, G.T, h, I=set([0,1, 2]))
    #valores de las varibles
    print('Los valores óptimos de las variables son: {0}n'.format(sol[1]))
    if sol[0]=='optimal':
        #valor de la función objetivo
        print('El valor óptimo es {0}'.format((-c.T*sol[1])[0]))
        # El valor óptimo debemos transponerlo y cambiarle el signo, estamos maximizando.
    else:
        print('El problema no devolvió una solución óptima. El estado del solucionador fue {0}'.format(sol[0]))
        #Obtiene los datos de los campos y soluciona el sistema
    return sol

#cambia de signo los valores de lista
def cambiar_signo(lista):
    for i in range(len(lista)): 
        lista[i]= lista[i]*-1
    return lista

#función que se ejecuta cuando se envian los primeros datos
def enviarDatos():
    #se obtienen los datos de los cuadros de textos
    nvaria=cvariables.get()  
    nrest=crestricciones.get()
    #sentencias que revisan si se obtuvieron datos y que sean numericos
    if nvaria!="":
        #se abre la segunda ventana 
        abrirVentana2(int(nvaria), int(nrest))
    else:
        #se muestra un mensaje de error al usuario
        messagebox.showwarning("Error", "alguno de los datos son nulos")

#segunda ventana para entrar las variables
def abrirVentana2(variables, restricciones ):   

    def getDatos():
        #coeficientes de la función objetivo sin tratar
        c_sfo = []
        #coeficientes independientes
        c_sinp = []

        c_sres = [[]]
        #se obtienen los coeficientes de la función objetivo
        print("coeficientes de la función objetivo")
        for ii in range(len(c_fo)):
            c_sfo.append(int(c_fo[ii].get()))
        print("coeficientes independientes:")
        for ii in range(len(c_ind)):         
            c_sinp.append(int(c_ind[ii].get()))
        print("coeficientes de las restricciones")
        for ii in range(len(c_res)):
            c_aux = []
            for jj in range(len(c_res[ii])):
                c_aux.append(int(c_res[ii][jj].get()))   
            c_sres.append(c_aux)
        #quita un espacio sin utilizar
        c_sres = c_sres[1:][::]
        #se invierten los signos de los coeficientes de la función objetivo
        c_sfo=cambiar_signo(c_sfo)
        #se definen las variables para mandarlas a la función que soluciona el problema
        c = m(c_sfo,tc='d')
        G = m(c_sres, tc='d')
        h = m(c_sinp,tc='d')
        mostrar_solu(solucionar(c,G,h), c)
        edatos.destroy()

    #Se crea una nueva ventana encima de la principal
    raiz.withdraw
    #se sobrepone a la ventana principal
    edatos=Toplevel()
    rgeneral=""
    #se le pone un icono a la ventana
    edatos.iconbitmap("bitmap.ico")
    Label(edatos, text="Función:").grid(row=0,column=0, padx=10,pady=10,columnspan=restricciones+3)
    #lista con los coeficientes de la función objetivo
    c_fo = []

    #se ponen los cuadros de texto para ingresar la función objetivo
    for i in range(variables):
        # cuadros de entrada de datos
        c_fo.append(Entry(edatos))
        c_fo[i].grid(row=1, column=(i*2),padx=10,pady=10)
        #variable que le da formato a las variables para luego ponerlas en la ventana
        aux="X"+str(i+1)
        rgeneral+=aux+","
        #etiquetas de cada una de las variables
        textovariables= Label(edatos,text=aux)
        textovariables.grid(row=1, column=((i*2)+1),pady=10)
    
    #titulo "restricciones" en la ventana
    Label(edatos, text="Restricciones:").grid(row=2,column=0, padx=10,pady=10,columnspan=restricciones+3)

    #lista de los coeficientes de las restricciones
    c_res = [[]]
    
    #lista de los coeficientes independientes de las restricciones
    c_ind = []

    #Creador de la plantilla de las restricciones
    for i in range(restricciones):
        c_aux = []
        for j in range(variables):
            #crea los cuadros donde se entra el texto, se define inmediatamente su posición con grid
            #vari = (Entry(edatos)).grid(row=3+i, column=(j*2),padx=10,pady=10)
            c_aux.append(Entry(edatos))        
            c_aux[j].grid(row=3+i, column=(j*2),padx=10,pady=10)
            aux="X"+str(j+1)
            #crea los cuadros donde se presenta las varaibles numeradas, se define inmediatamente su posición con grid
            textovariables= Label(edatos,text=aux).grid(row=3+i, column=((j*2)+1),pady=10)
            textovariables= Label(edatos,text="≤").grid(row=3+i, column=((j*2)+3),pady=10, padx=5)

        c_res.append(c_aux)
        c_ind.append(Entry(edatos))
        c_ind[i].grid(row=3+i, column=(variables*2+4),pady=10)

    c_res = c_res[1:][::]
    rgeneral+="≥ 0"
    Label(edatos, text=rgeneral).grid(row=restricciones+3,column=0, padx=10,pady=10,columnspan=restricciones+3)
    #botón de envio
    botonEnvio=Button(edatos, text="siguiente",command=getDatos)
    botonEnvio.grid(row=4+restricciones, column=0,pady=10, columnspan=restricciones+3)
    botonEnvio.config(justify="center",font=("SansSerif",12), cursor="hand2")
 

raiz.title("Aplicación programación entera pura")

raiz.iconbitmap("bitmap.ico")

raiz.config(bg="gray")

pframe=Frame()
pframe.pack()
pframe.config(bg="gray")
pframe.config(width="650", height="350")

#labels texto plano
labelVariables= Label(pframe, text="Ingrese el número de variables del problema",fg="white", font=("SansSerif",16),bg="gray")
labelRestricciones= Label(pframe, text="Ingrese el número de restricciones del problema", fg="white", font=("SansSerif",16),bg="gray")

labelVariables.grid(row=0,column=0,padx=20,pady=20)
labelRestricciones.grid(row=1, column=0, padx=20,pady=20)
#Labels entradas

cvariables = Entry(pframe)
cvariables.grid(row=0,column=1,padx=20,pady=20)
cvariables.config(justify="center",font=("SansSerif",16))

crestricciones=Entry(pframe)
crestricciones.grid(row=1,column=1,padx=20,pady=20)
crestricciones.config(justify="center",font=("SansSerif",16))

#botones

botonEnvio=Button(pframe, text="siguiente",command=enviarDatos)
botonEnvio.grid(row=2, column=0,padx=20,pady=20, columnspan=2)
botonEnvio.config(justify="center",font=("SansSerif",14), cursor="hand2")



raiz.mainloop()
