"""
Proyecto Modelado - Sistema Inmunologico

Departamento de Ingeniería Eléctrica y Electrónica, Ingeniería Biomédica
Tecnológico Nacional de México [TecNM - Tijuana]
Blvd. Alberto Limón Padilla s/n, C.P. 22454, Tijuana, B.C., México

Nombre del alumno: Andres Martin Bañuelos Elias; Alain Yahir Chaparro Zamora ; Hector Andres Fernandez Esquivel
Número de control: 21212142; 21212147; 21212153
Correo institucional:l21212142@tectijuana.edu.mx;l21212147@tectijuana.edu.mx; l21212153@tectijuana.edu.mx

Asignatura: Modelado de Sistemas Fisiológicos
Docente: Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx
"""
# Instalar librerias en consola
#!pip install control
#!pip install slycot

# Librerías para cálculo numérico y generación de gráficas
import numpy as np
import math as m
import matplotlib.pyplot as plt
import control as ctrl

# Datos de la simulación
x0, t0, tF, dt, w, h = 0, 0, 0.1, 1E-6, 6, 3
N = round((tF-t0)/dt) + 1 
t = np.linspace(t0, tF, N)
u1 = np.ones(N) #Escalon unitario

#Componentes del control
R1 = 10
R2 = 10
L  = 5E-3
C  = 50E-6
numControl = (1)
denControl = (C*L, C*R2, 1)
sysControl = ctrl.tf(numControl, denControl)
print(sysControl)

# Componentes del caso
R1 = 1
R2 = 1
L  = 10E-3
C  = 100E-6
numCaso = (1)
denCaso = (C*L, C*R2, 1)
sysCaso = ctrl.tf(numCaso, denCaso)
print(sysCaso)

# Componentes del controlador
Rr = 1432.9
Re = 21.185
Cr = 1E-6
Ce = 1.0703E-5
numPID = [Rr*Re*Cr*Ce, Re*Ce+Rr*Cr, 1]
denPID = [Re*Cr, 0]
PID = ctrl.tf(numPID, denPID)
print(PID)

# Sistema de control en lazo cerrado control
X = ctrl.series(PID,sysCaso)
sysPID = ctrl.feedback(X,1,sign = -1)
print(sysPID)
Tratamiento = ctrl.series(sysControl, sysPID)

def plotsignals(u, sysControl, sysCaso, Tratamiento):
    fig = plt.figure()  
    ts, pControl = ctrl.forced_response(sysControl, t, u1, x0)
    plt.plot(t, pControl, '-', color=[0,0,1], label='$Vs_{Control}(t)$')
    
    ts, pCaso = ctrl.forced_response(sysCaso, t, u1, x0)
    plt.plot(t, pCaso, '-', color=[1, 0.7450, 0.9330], label='$Vs_{Caso}(t)$')
    
    ts, ptrat = ctrl.forced_response(Tratamiento, t, u1, x0)
    plt.plot(t, ptrat, '--', color=[0,1,0], label='$Vs_{Tratamiento}(t)$')
    
    plt.grid(False)

    plt.xlim(0, 0.1)
    plt.xticks(np.arange(0, 0.11, 0.01))
    plt.ylim(0, 2)
    plt.yticks(np.arange(0, 2.1, 0.25))
    
    plt.xlabel('$t$ $[s]$', fontsize=11)
    plt.ylabel('$V_e(t)$ $[V]$', fontsize=11)
    plt.legend(bbox_to_anchor=(0.5, -0.3), loc='center', ncol=4, fontsize=8, frameon=False)
    fig.set_size_inches(w, h)  
    fig.tight_layout()
    plt.show()

    namepng = 'python_' + 'Inmunologico' + '.png'
    namepdf = 'python_' + 'Inmunologico' + '.pdf'
    fig.savefig(namepng, dpi=600, bbox_inches='tight')
    fig.savefig(namepdf, bbox_inches='tight')
    return fig 

plotsignals(u1, sysControl, sysCaso, Tratamiento)