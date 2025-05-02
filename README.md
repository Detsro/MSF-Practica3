[![Open in MATLAB Online](https://www.mathworks.com/images/responsive/global/open-in-matlab-online.svg)](https://matlab.mathworks.com/open/github/v1?repo=Detsro/MSF-Practica3)
# MSF-Practica3
Modelado de Sistemas Fisiológicos. Práctica 3: Sistema Cardiovascular [Meraz18210139]

## Autor
Mauricio Jesús Meraz Galeana

Ingeniería Biomédica, Departamento de Ingeniería Eléctrica y Electrónica, Tecnológico Nacional de México/IT Tijuana. Blvd. Alberto Limón Padilla s/n, Tijuana, C.P. 22454, B.C., México. Email: mauricio.meraz18@tectijuana.edu.mx

## Objetivos general
El modelo de Windkessel de cuatro elementos contiene dos elementos din·micos. Por lo tanto, se
necesitan dos estados para describir la din·mica. El vector de estados se conforma por las variables FL (t)
denotando el áujo a travÈs de la inercia arterial total, y la variable Pp (t) representando la presiÛn sobre la
distensibilidad arterial. Entonces, asumiendo Pa (t) como la presiÛn arterial de entrada, y en consecuencia
a Fa (t) como el áujo hacia la aorta o arteria pulmonar.
## Actividades

1. Calcular analÌticamente la funciÛn de transferencia del sistema cardiovascular.
2. Determinar el error en estado estacionario y la estabilidad del sistema en lazo abierto.
3. Construir el diagrama de bloques como se indica en el diagrama 5.8.
4. DiseÒar el controlador con Simulink utilizando el bloque PID Controller y la herramienta Tune para
sintonizar los valores Ûptimos para cada una de las ganancias kP , kI y kD.
5. Ilustrar el cambio de la presiÛn sobre la distensibilidad arterial [Pp (t)] en respuesta a la presiÛn
arterial de entrada Pa (t). Utilice la funciÛn de entrada Uniform Random Number con la siguiente
conÖguracion: min = 0:2 V; max = 1 V; seed = 106; Sample time = 0:5:
6. Determinar la respuesta a la funciÛn en el intervalo t 2 [0; 15] (segundos) en Python, Simulink y
Multisim en lazo abierto y en lazo cerrado con el control
7. Elaborar el diagrama biolÛgico del sistema con BioRender.com.
8. Discutir los resultados obtenidos en la experimentaciÛn in silico y elaborar el reporte de la pr·ctica.

## Docente
Dr. Paul A. Valle

Posgrado en Ciencias de la Ingeniería [PCI] y Departamento de Ingeniería Eléctrica y Electrónica [DIEE], Tecnológico Nacional de México/IT Tijuana. Blvd. Alberto Limón Padilla s/n, Tijuana, C.P. 22454, B.C., México. Email: paul.valle@tectijuana.edu.mx

## Lecturas
[1] Paul. A. Valle, Syllabus para la asignatura de Modelado de Sistemas Fisiológicos, Tecnológico Nacional de México/IT Tijuana, Tijuana, B.C., México, 2025. Permalink: https://www.dropbox.com/scl/fi/4gl55ccrjm9yulvziikxs/Modelado-de-Sistemas-Fisiologicos.pdf

[2] M. C. Khoo, Physiological Control Systems Analysis Simulation, and Estimation, 2nd ed. Piscataway, New Jersey, USA: IEEE Press, 2018.
