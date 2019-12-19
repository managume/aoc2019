# Adviento de Código 2019

## Día 3: Cables Cruzados

### Parte 1

La asistencia gravitatoria fue exitosa, y vas de camino hacia la estación de reabastecimiento de Venus. Durante la vuelta de regreso a la Tierra, el sistema de gestión de combustible no fue completamente instalado, por lo que es nuestra siguiente prioridad en la lista.

Al abrir el panel frontal se ve un revoltijo de cables. Concretamente, **dos cables** están conectados a un puerto central y se extienden hacia el exterior en una cuadrícula. Traza el camino que toma cada cable al salir del puerto central, un cable por línea de texto (tu entrada del puzles).
Los cables se tuercen y giran, pero ocasionalmente dos cables se cruzan. Para arreglar el circuito, necesitas **encontrar el punto de intersección mas cercano al puerto central**. Como los cables están en una cuadrícula, utiliza la [distancia de Manhattan](https://es.wikipedia.org/wiki/Geometr%C3%ADa_del_taxista) para su medida. Técnicamente los cables se cruzan en el puerto central, donde ambos empiezan, aunque este punto no cuenta, ni lo hace en el caso en que un cable se cruce con sí mismo.

Por ejemplo, si el primer camino del cable es *R8,U5,L5,D3*, entonces empieza por el puerto central (0), avanza hacia la derecha *8*, sube *5*, izquierda *5*, y finalmente baja *3*:

```sh
...........
...........
...........
....+----+.
....|....|.
....|....|.
....|....|.
.........|.
.o-------+.
...........
```

Entonces, si el camino que toma el segundo cable es *U7,R6,D4,L4*, avanza hacia arriab *7*, derecha *6*, abajo *4* e izquierda *4*:

```sh
...........
.+-----+...
.|.....|...
.|..+--X-+.
.|..|..|.|.
.|.-X--+.|.
.|..|....|.
.|.......|.
.o-------+.
...........
```

Estos cables se cruzan en dos puntos (marcados con *X*), pero el que está más abajo a la izquierda es el más cercano al puerto central: su distancia es *3 + 3 = 6*.

Aquí están unos pocos ejemplos más:


* Ejemplo 1:
  * Cable 1: ```R75,D30,R83,U83,L12,D49,R71,U7,L72```
  * Cable 2: ```U62,R66,U55,R34,D71,R55,D58,R83```
  * Distancia: ```159```
  
* Ejemplo 2:
  * Cable 1: ```R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51```
  * Cable 2: ```U98,R91,D20,R16,D67,R40,U7,R15,U6,R7```
  * Distancia: ```135```

### Parte 2
