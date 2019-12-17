# Adviento de Código 2019

## Día 4: Contenedor Seguro

### Parte 1

Has llegado al depósito de combustible de Venus solamente para descubrir que está protegido con una contraseña. Los elfos habían escrito la contraseña en una nota adhesiva, pero alguien la tiró.

Sin embargo, recuerdan algunos datos clave sobre la contraseña:

- Es un número de seis dígitos.
- El valor está incluido en el rango de número que aparecen en la entrada del puzles.
- Dos dígitos adyacentes son iguales (como 22 en 122345)
- Yendo de izquierda a derecha, los dígitos **nunca disminuyen**; solamente aumentan o permanecen iguales (como 111123 o 135679).


Aparte de las reglas de rango, las siguientes también son ciertas:

- ```111111``` cumple con la condición  (doble 11, nunca disminuye)
- ```223550``` no cumple la condición (un dígito disminuye ```50```)
- ```123789``` no cumple la condición (no hay doble dígito)

¿**Cuántas contraseñas diferentes** hay en el rango dado en el problema que cumplen los criterios anteriores?

El rango de entrada que se proporciona es ```307237-769058```.

## Part 2

Un elfo acaba de recordar un detalle importante: los dos dígitos adyacentes coincidentes **no forman parte de un grupo mayor de dígitos adyacentes**.

Dada esta nueva condición, pero ignorando la regla de rango, lo siguiente es verdadero:

- ```112233``` cumple la condición porque los dígitos nunca disminuyen y todos los dígitos repetidos tienen la misma longitud.
- ```123444``` no cumple la condición (la repetición ```44``` es parte de un grupo mayor ```444```).
- ```111122``` cumple la condición (a pesar de que el ```1``` esté repetido más de dos veces, el número contiene un doble ```22```).

¿**Cuántas contraseñas diferentes** hay en el rango dado en el problema que cumplen los criterios anteriores?

El rango de entrada que se proporciona es ```307237-769058```.