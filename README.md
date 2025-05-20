//ejerciciomiercoles//

Resolución de laberintos usando el algoritmo A* (A-Star) en Python. Proyecto de Estructura de Datos para encontrar el camino óptimo evitando obstáculos.
# Resolución de laberintos con el algoritmo A*

Este proyecto lo realicé como trabajo extra para la materia de Estructura de Datos.  
Mi nombre es Diego Rojas y mi código universitario es 35295.

El objetivo del trabajo fue implementar el algoritmo A* en Python para resolver un laberinto representado en forma de matriz.  
Este algoritmo permite encontrar el camino más corto entre dos puntos, evitando los obstáculos que hay en el camino.

 //Cómo funciona//

El laberinto se representa como una matriz de números:
- El número 0 representa espacios libres donde se puede pasar.
- El número 1 representa obstáculos o paredes que no se pueden cruzar.

El programa busca el camino más corto desde la esquina superior izquierda hasta la esquina inferior derecha.

El algoritmo A* funciona evaluando el costo de llegar a un punto y una estimación de cuánto falta para llegar al destino. Con eso, decide cuál es el camino más eficiente.

//Cómo ejecutar el código//

Solo necesitas tener Python 3 instalado. Luego puedes ejecutar el programa con:

