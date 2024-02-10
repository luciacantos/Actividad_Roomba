# Actividad_Roomba

Link repositorio: https://github.com/luciacantos/Actividad_Roomba

Le proponemos realizar un proyecto que consiste en la escritura de un script Python que permite a un robot aspirador calcular la superficie de una habitación y estimar el tiempo de limpieza.

Imaginemos que la habitación que hay que limpiar contiene un mueble debajo del cual no puede meterse el robot y que tiene las siguientes características:

PLANO DE LA HABITACIÓN

![Plano habitación.](https://github.com/luciacantos/Actividad_Roomba/assets/114728382/8085ab45-a740-4bf8-940f-d4b6b0f00195)


VISTA 3D DE LA HABITACIÓN

![Plano habitación 3D.](https://github.com/luciacantos/Actividad_Roomba/assets/114728382/e3bb4ee1-e62b-4179-bb8b-688862fbf721)


Una de las formas posibles de calcular la superficie que debe limpiar el robot consiste en fragmentar la superficie total en zonas utilizables:


| ZONAS | LARGO (cm) | ANCHO (cm) |
| ------------- | ------------- | ------------- |
| Zona 1 |  500  |  150 |
| Zona 2 |  480  |  101 |
| Zona 3 |  309  |  480 |
| Zona 4 |  90   |  220 |

Una vez fragmentada, es fácil calcular la superficie total que hay que limpiar añadiendo las superficies de cada zona. Estas superficies se calculan multiplicando el largo por el ancho en cada una de ellas.

ZONAS UTILIZABLES POR EL ROBOT ASPIRADOR

![Zonas utilizables.](https://github.com/luciacantos/Actividad_Roomba/assets/114728382/ce9011ee-a472-4adf-bd33-1018216005f5)



