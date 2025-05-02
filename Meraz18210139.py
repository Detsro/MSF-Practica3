"""
Práctica 2: Sistema Cardiovascular

Departamento de Ingeniería Eléctrica y Electrónica, Ingeniería Biomédica  
Tecnológico Nacional de México [TecNM - Tijuana]  
Blvd. Alberto Limón Padilla s/n, C.P. 22454, Tijuana, B.C., México  

Nombre del alumno: Mauricio Jesus Meraz Galeana  
Número de control: 18210139  
Correo institucional: mauricio.meraz18@tectijuana.edu.mx  

Asignatura: Modelado de Sistemas Fisiológicos  
Docente: Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx
"""

# Librerías necesarias
import numpy as np
import math
import matplotlib.pyplot as plt
import control

# Parámetros generales
x0, t0, tF, dt, w, h = 0, 0, 10, 1E-3, 10, 5
N = round((tF - t0) / dt) + 1
t = np.linspace(t0, tF, N)
u = np.sin(2 * math.pi * 95 / 60 * t) + 0.8  # Señal de entrada

# Función de transferencia del sistema cardiovascular
def cardio(R, L, C, Z):
    num = [L * R, R * Z]
    den = [C * L * R * Z, L * R + L * Z, R * Z]
    sys = control.tf(num, den)
    return sys

# Casos cardiovasculares
# Normotenso
Zs, Cs, Rs, Ls = 0.033, 1.500, 0.950, 0.010
sysS = cardio(Rs, Ls, Cs, Zs)

# Hipotenso
Zh, Ch, Rh, Lh = 0.020, 0.250, 0.6, 0.005
sysE = cardio(Rh, Lh, Ch, Zh)

# Hipertenso
Za, Ca, Ra, La = 0.050, 2.500, 1.4, 0.020
sysA = cardio(Ra, La, Ca, Za)

# Gráfica en lazo abierto
def plotsignals(u, sysS, sysE, sysA, signal):
    fig = plt.figure()
    _, Vs = control.forced_response(sysS, t, u, x0)
    plt.plot(t, Vs, '-', color=[0.3, 0.5, 0.2], label='$P_A(t): Normotenso$')

    _, Ve = control.forced_response(sysE, t, u, x0)
    plt.plot(t, Ve, ':', color=[0.5, 0.05, 0.05], label='$P_A(t): Hipotenso$')

    _, Va = control.forced_response(sysA, t, u, x0)
    plt.plot(t, Va, ':', linewidth=0.5, color=[0.1, 0.1, 0.6], label='$P_A(t): Hipertenso$')

    plt.grid(False)
    plt.xlim(0, 10)
    plt.ylim(-0.5, 2)
    plt.xticks(np.arange(0, 11, 1))
    plt.yticks(np.arange(-0.5, 2.1, 0.25))
    plt.xlabel('$t$ [s]')
    plt.ylabel('$PA(t)$ [V]')
    plt.title('Normotenso')
    plt.legend(bbox_to_anchor=(0.5, -0.23), loc='center', ncol=4, fontsize=8, frameon=False)
    plt.show()
    fig.set_size_inches(w, h)
    fig.tight_layout()
    fig.savefig(f'lazo_abierto_{signal}.png', dpi=600, bbox_inches='tight')
    fig.savefig(f'lazo_abierto_{signal}.pdf', dpi=600, bbox_inches='tight')

# Ejecutar la gráfica de lazo abierto
plotsignals(u, sysS, sysE, sysA, 'respuesta')

# Tratamiento: Hipotenso con PID
Cr = 1E-6
Re = 2413.8
Rr = 0.53877
numPID_h = [Rr * Cr, 1]
denPID_h = [Re * Cr, 0]
PID_h = control.tf(numPID_h, denPID_h)

X_h = control.series(PID_h, sysE)
sysPID_h = control.feedback(X_h, 1, sign=-1)

fig_h = plt.figure()
plt.plot(t, u, '-', linewidth=0.5, color=[0.95, 0.65, 0.15], label='$P_a(t)$')
_, Ve = control.forced_response(sysE, t, u, x0)
plt.plot(t, Ve, '-', linewidth=0.5, color=[0.2, 0.2, 0.6], label='$P_p(t): Hipotenso$')
_, pid_h = control.forced_response(sysPID_h, t, u, x0)
plt.plot(t, pid_h, ':', linewidth=2, color=[0.5, 0.05, 0.05], label='$P_p(t): Tratamiento$')
plt.grid(True)
plt.xlim(0, 10)
plt.xticks(np.arange(0, 11, 1))
plt.ylim(-0.5, 2)
plt.xlabel('$t$ [s]')
plt.ylabel('$V(t)$ [V]')
plt.title('Tratamiento: Hipotenso')
plt.legend(bbox_to_anchor=(0.5, -0.23), loc='center', ncol=3)
plt.show()
fig_h.set_size_inches(w, h)
fig_h.tight_layout()
fig_h.savefig('Tratamiento_hipotenso.png', dpi=600, bbox_inches='tight')
fig_h.savefig('Tratamiento_hipotenso.pdf', dpi=600, bbox_inches='tight')

# Tratamiento: Hipertenso con PID
Cr = 1E-6
Re = 2419.4
Rr = 0.80639 
numPID_a = [Rr * Cr, 1]
denPID_a = [Re * Cr, 0]
PID_a = control.tf(numPID_a, denPID_a)

X_a = control.series(PID_a, sysA)
sysPID_a = control.feedback(X_a, 1, sign=-1)

fig_a = plt.figure()
plt.plot(t, u, '-', linewidth=0.5, color=[0.95, 0.65, 0.15], label='$P_a(t)$')
_, Va = control.forced_response(sysA, t, u, x0)
plt.plot(t, Va, '-', linewidth=0.5, color=[0, 0.25, 0.4], label='$P_p(t): Hipertenso$')
_, pid_a = control.forced_response(sysPID_a, t, u, x0)
plt.plot(t, pid_a, ':', linewidth=2, color=[0.5, 0.05, 0.05], label='$P_p(t): Tratamiento$')
plt.grid(True)
plt.xlim(0, 10)
plt.xticks(np.arange(0, 11, 1))
plt.ylim(-0.5, 2)
plt.xlabel('$t$ [s]')
plt.ylabel('$V(t)$ [V]')
plt.title('Tratamiento: Hipertenso')
plt.legend(bbox_to_anchor=(0.5, -0.23), loc='center', ncol=3)
plt.show()
fig_a.set_size_inches(w, h)
fig_a.tight_layout()
fig_a.savefig('Tratamiento_hipertenso.png', dpi=600, bbox_inches='tight')
fig_a.savefig('Tratamiento_hipertenso.pdf', dpi=600, bbox_inches='tight')
