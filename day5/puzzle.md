# Adviento de Código 2019

## Día 5: Soleado con Probabilidad de Asteroides

### Parte 1

Estás empezando a sudar mientras la nave se dirige hacia Mercurio. Los elfos te sugieren que hagas funcionar el aire acondicionado actualizando tu ordenador de abordo para que soporte la Terminal de Supervisión de Temperatura Ambiente.

La Terminal de Supervisión de Temperatura Ambiente (TeSTA) empieza ejecutando un **programa de diagnóstico** (tus valores de entrada del puzle). El programa de diagnóstico de TeSTA ejecutará en [tu computador Intcode ya existente](../day2/puzzle.md) después de algunas modificaciones:

**Primero**, necesitarás añadir **dos nuevas instrucciones**:

- Opcode `3` toma un único entero como entrada y lo almacena en la posición dada por su único parámetro. Por ejemplo, la instrucción `3,50` tomaría un valor de entrada y lo almacenaría en la posición `50`.

- Opcode `4` devuelve el valor almancenado en la dirección que indica su único parámetro. Por ejempo, la instrucción `4,50` devolvería el valor almacenado en la posición `50`.

Los programas que utilicen estas instrucciones vendrán con la documentación que explica lo que debe conectarse a la entrada y salida. El programa `3,0,4,0,99` devuelve lo que recibe como entrada y luego se detiene.

**Segundo**, necesitarás añadir compatibilidad con los ***modos de parámetro**_

Cada parámetro de una instrucción se maneja en base a su modo de parámetro. Ahora mismo, tu ordenado de abordo entiende el modo de parámetro 0, **modo posición**, esto hace que el parámetro se interprete como una **posición** - si el parámetro es `50`, su valor es **el valor almacenado en la dirección 50 de memoria***. Hasta ahora, todos los parámetros han estado en modo posición.

Ahora, tu ordenador de abordo también necesitará majeras parámetros en modo `1`, **modo inmediato**. En el modo inmediato, un parámetro es interpretado como un valor - si el parámetro es `50`, su valor es simplemente `50`.

Los modos de parámetro se almacenan en el mismo valor que el opcode de la instrucción. El opcode es un número de dos dígitos compuesto únicamente por unidades y decenas de dígitos, esto es, el opcode son los dos número más a la derecha del primer valor de una instrucción. Los módos de parámetro son dígitos individuales, uno por parámetro, leído el opcode de derecha a izquierda: el primer modo de parámetro es el dígito situado en la centena, el segundo modo de parámetro es el dígito situado en la unidad de mil, el tercer modo de parámetro es el dígito situado en la decena de mil, y así sucesivamente. Cualquier modo que falte es `0`.

Por ejemplo, considera el programa `1002,4,3,4,33`.

La primera instrucción, `1002,4,3,4`, es una instrucción **múltiple** - los dos dígitos situados más a la derecha del primer valor, `02`, indican el opcode `2`, multiplicación. Entonces, yendo de derecha a izquierda, los modos de parámetros son `0` (dígito en la centena), `1` (dígito en la unidad de mil), y `0` (dígito en la decena de mil, no presente, por lo que es `0`):

```
ABCDE
 1002

DE - opcode de dos dígitos, 02 == opcode 2
 C - modo del 1er parámetro,  0 == modo posición
 B - modo del 2do parámetro,  1 == modo inmediato
 A - modo del 3er parámetro,  0 == modo posición,
                                  omitido por ser un cero a la izquierda
```
Esta instrucción multiplica sus primeros dos parámetros. El primer parámetro, `4` en modo posición, funciona como antes - su valor es el valor almacenado en la dirección de memoria `4` (33). El segundo parámetro, `3` en modo inmediato, simplemente tiene el valor `3`. El resultado de la operación, `33 * 3 = 99`, es escrito de acuerdo al tercer parámetro, `4` en modo posición, que también funciona como lo hacía anteriormente - `99` es escrito en la dirección de memoria `4`.

Finalmente, algunas notas a tener en cuenta:

- Es importante recordar que el puntero de instrucción debe incrementarse por el número de valores que hay en la instrucción despúes de que esta finalice. Porque con las nuevas instrucciones, esta cantidad ya no es siempre `4`.

- Los enteros puedes senr negativos: `1101,100,-1,4,0` es un programa válido (recupera `100 + -1` y guarda el resultado en la posición de memoria `4`).

El programa de diagnóstica TeSTA empezará solicitando al usuario el ID del sistema a verificar, ejecutando una instrucción de entrada - introduce el valor `1`, el ID de la unidad de aire acondicionado de la nave. 

Entonces realizará una series de pruebas de diagnóstico confirmando que varias partes del computador Intcode, como los modos de parámetro, funcionan correctamente. Para cada prueba, ejecutará una instrucción de **salida** indicando cómo de cerca ha estado el resultado de la prueba del valor que se esperaba, donde `0` significa que la prueba fue satisfactoria. Los valores de salida diferentes a cero significan que una función no se está ejecutando correctamente; verifica las instrucciones ejecutadas tras lanzar la instrucción de salida para comprobar cual falló.

Por último, el programa devolverá un **código de diagnóstico** y se detendrá. Este valor de salida no es un error; un valor de saluda seguido inmendiatamente por una detención significa que el programa ha terminado. Si todos los valores de salida son ceros exceptuando el del código de diagnóstico, signifa que el programa se ejecutó exitosamente.

Después de introducir el valor 1 a la instrucción de entrada y pasar todas las pruebas ¿**Qué código de diagnóstivo devuelve el programa**?

### Parte 2