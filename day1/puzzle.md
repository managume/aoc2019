# Adviento de Código 2019

## Día 1: La Tiranía de la Ecuación del Cohete

### Primera parte

¡Papa Noel se ha quedado varado en los límites del Sistema Solar mientras entregaba regalos a otros planetas! Para calcular de manera precisa su posición en el espacio, alinear con seguridad su motor de curvatura, y retornar a la Tierra a tiempo de salvar la Navidad, necesita que le hagas llegar las medidas de cincuenta estrellas.

Reúne estrellas resolviendo puzles. Cada día se abrirán dos puzles en el calendario de adviento; el segundo puzles se desbloqueará una vez completes el primero. Cada puzles te garantiza una estrella ¡Buena suerte!

Los elfos están preparados para subirte a una nave espacial y lanzarte.

Entre las opciones de Ir o No Ir, los elfos están decididos por la opción de 'Ir' siempre que haya combustible suficiente. Todavía no han determinado la cantidad de combustible necesario.

El combustible necesario para el lanzamiento de un módulo se basa en su masa. Específicamente, para encontrar el combustible requerido para un módulo, tomar su masa, dividirla por 3, redondearla a la baja, y restarle 2.

Por ejemplo:
* Para una masa de ```12```, dividir entre ```3``` y redondea a la baja para llegar a ```4```, luego resta ```2``` para tener como resultado ```2```.
* Para una masa de ```14```, dividir entre ```3``` y redondea a la baja para llegar a ```4```, luego resta ```2```, por lo que el combustible necesario será de ```2```.  
* Para una masa de ```1969```, el combustible necesario será de ```654```.
* Para una masa de ```100756```, el combustible necesario será de ```33583```.

El contador de combustible necesita saber el total de combustible necesario. Para dar con ello, calcula individualmente la cantidad de combustible que necesita la masa de cada módulo ([ver archivo de entradas del puzles](input.txt)) , entonces se suman todos los valores de combustible.

### Segunda parte

Durante la segunda votación, el elfo al cargo de la doble verificación de Ecuación del Cohete para la secuencia de lanzamiento. Aparentemente, has olvidado incluir una carga adicional de combustible para contrarrestar la masa del combustible añadido.

El combustible también necesita una carga de combustible como si se tratara de un módulo más. Toma su masa, divide entre 3, redondea a la baja y réstale 2. Sin embargo,esa carga de combustible **también** necesitará su propia cantidad de combustible y **ese** combustible, necesitará más combustible y así sucesivamente. Cualquier masa que necesite una carga de **combustible negativa** debe ser tratada como si necesitara **cero combustible**; la masa restante de combustible, si la hubiera, se la dejamos para el mundo de los sueños y fantasías, donde no hay masa y queda fuera del cálculo.

Así, para la masa de cada módulo, se calcula su combustible y se añade al total. Entonces, tratamos la cantidad de combustible que acabamos de calcular como una nueva entrada de masa y repetimos el proceso, continuando hasta que la cantidad requerida de combustible sea cero o negativa. Por ejemplo:

* Un módulo de masa ```14``` necesita una carga de combustible de ```2```. Esta cantidad de combustible no necesita más combustible (2 dividido entre 3 y redondeado a la baja da 0, que requeriría combustible negativo), por lo tanto el total de combustible que necesita sigue siendo ```2```.
* Primero, un módulo de masa ```1969``` necesita una carga de combustible de ```654```. Ahora, esta cantidad de combustible necesita una carga más de combustible de ```216``` (654 / 3 - 2). La carga de ```216``` necesitará ```70``` más de combustible, que a su vez necesitará ```21``` y esta necesitará ```5```. Esta última cantidad no necesita de más combustible. Por lo que el total de carga de combustible que necesitamos para nuestro módulo de masa ```1969``` es ```654 + 216 + 70 + 21 + 5 = 966```.
* La carga de combustible que necesitamos para un módulo de masa ```100756``` y su propia carga de combustible es de: ```33583 + 11162 + 3728 + 1240 + 411 + 135 + 43 + 12 + 2 = 50346```

¿**Cuál es la suma de la carga de combustible requerida** por todos los módulos de nuestra nave espacial, teniendo también en cuenta la masa de combustible añadida? (Calcular las cantidades de combustibles requeridas para cada módulo por separado y luego sumarlas al final.)

Pese a que no tiene cambios, puedes [volver a acceder al archivo de entradas del puzles](input.txt).