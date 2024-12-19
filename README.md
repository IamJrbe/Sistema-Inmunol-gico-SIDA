[![Open in MATLAB Online](https://www.mathworks.com/images/responsive/global/open-in-matlab-online.svg)](https://matlab.mathworks.com/open/github/v1?repo=IamJrbe/Sistema-Inmunol-gico-SIDA)
# Sistema Inmunológico 

## Estudiantes
Fernandez Esquivel Hector Andres
Chaparro Zamora Alain Yahir
Banuelos Elias Andres Martin
Departamento de Ingeniería Eléctrica y Electrónica, Tecnológico Nacional de México/IT Tijuana, Blvd. Alberto Limón Padilla s/n, Tijuana, C.P. 22454, B.C., México. Email: l21212142@tectijuana.edu.mx; l21212147@tectijuana.edu.mx l21212153@tectijuana.edu.mx

## Asignaturas o departmento donde se puede usar la Actividad
Modelado de Sistemas Fisiológicos de Ingeniería Biomédica

## Información general
El modelizado de sistemas fisiológicos es una herramienta importante en Ingeniería Biomédica, permite comprender el funcionamiento del cuerpo humano, así como diseñar y evaluar terapias y dispositivos médicos; se define como el proceso de formular modelos matemáticos o computacionales que representan el comportamiento y la interacción de los sistemas biológicos y fisiológicos. Esta asignatura pretende aportar al perfil del Ingeniero Biomédico la capacidad de realizar investigación científica en el área de Biología de Sistemas con la finalidad de dirigir y participar en equipos de trabajo interdisciplinarios en contextos nacionales e internacionales, así como de proporcionar soluciones informáticas para resolver problemas en el campo de la Ingeniería Biomédica con ética profesional; lo anterior al proporcionar al estudiante bases sólidas para modelizar sistemas y diseñar controladores para la solución de problemas en las áreas de atención médica y del sector industrial médico. La construcción de analogías entre circuitos eléctricos y sistemas fisiológicos para la formulación de modelos matemáticos y el diseño de controladores mediante la experimentación in silico brindan herramientas de gran aplicación en el quehacer profesional del Ingeniero Biomédico.

La asignatura de Modelado de Sistemas Fisiológicos forma parte del plan de estudios de la carrera en Ingeniería Biomédica con la siguiente competencia general del curso: Utiliza las propiedades de los circuitos RLC para describir la dinámica de sistemas fisiológicos, obtener modelos matemáticos y aplicar el control clásico, esto con el objetivo de integrar los principios de la Ingeniería de Control, la Electrónica Analógica y las Ciencias de la Computación con la Anatomía y Fisiología del cuerpo humano para proporcionar descripciones cuantitativas y cualitativas de sistemas fisiológicos complejos con el objetivo de modelizar, analizar, controlar, ilustrar y predecir su dinámica tanto en el corto como en el largo plazo.

## Objetivo general
Diseñar un gemelo digital de un sistema fisiológico que permita identificar las diferencias entre un paciente afectado por una enfermedad (caso) y un individuo saludable (control) para desarrollar un protocolo de tratamiento mediante un sistema de control en lazo cerrado.

## Descripción detallada del sistema
El modelo desarrollado utiliza un circuito eléctrico tipo RLC para representar la dinámica del sistema inmunológico afectado por el SIDA, causado por el virus de inmunodeficiencia humana (VIH). Este virus ataca y debilita el sistema inmunológico al destruir las células T CD4+, esenciales para coordinar la respuesta inmune, dejando al cuerpo vulnerable frente a infecciones oportunistas y ciertos tipos de cáncer.

Componentes del Modelo:
Resistencias (R₁ y R₂): Simulan las pérdidas en la respuesta inmunitaria debido a inflamación crónica y daño celular, representando la dificultad para activar y mantener una respuesta efectiva.

Inductor (L): Representa la memoria inmunológica del sistema, que se ve comprometida en pacientes con SIDA debido a la destrucción de células T CD4+ y de memoria.

Capacitor (C): Modela la capacidad del sistema para almacenar recursos inmunitarios, como anticuerpos y citoquinas, que también se ven afectados por el daño a las células B.

Fuente de entrada (Vₑ): Simboliza un estímulo externo, como un patógeno o una infección, que activa la respuesta inmune.

Salida (Vₛ): Refleja la respuesta inmunológica generada, la cual es débil en individuos con SIDA debido a la incapacidad del sistema para responder adecuadamente.

Análisis Matemático:
El modelo se basa en la función de transferencia del circuito, permitiendo analizar la dinámica de las respuestas inmunológicas en individuos sanos y pacientes con SIDA. Las simulaciones realizadas con Python muestran las diferencias en la respuesta entre ambos casos, evidenciando la incapacidad del sistema inmunológico afectado para generar una respuesta eficaz frente a un estímulo externo.

Aplicaciones y Potencial Terapéutico:
Este enfoque facilita la visualización de las alteraciones funcionales en el sistema inmunológico debido al SIDA, proporcionando una base para explorar estrategias terapéuticas. Entre ellas se incluyen:

Fortalecer la memoria inmunológica (L).
Restaurar la producción de anticuerpos y citoquinas (C).
Mitigar la inflamación crónica (R₁ y R₂).

## Referencias principales
[1]“VIH y sida”, Who.int. [En línea]. Disponible en: https://www.who.int/es/news-room/fact-sheets/detail/hiv-aids. [Consultado: 06-dic-2024].

[2] "VIH/sida”, Medlineplus.gov. [En línea]. Disponible en: https://medlineplus.gov/spanish/ency/article/000594.htm. [Consultado: 06-dic-2024].

[3] H. Niu and Z. Geng, "Stabilization of an underactuated AUV with physical damping on SE(3) via SIDA method," en *2016 35th Chinese Control Conference (CCC)*, Chengdu, China, 2016, pp. 9856-9861. DOI: 10.1109/CHICC.2016.7553196.
