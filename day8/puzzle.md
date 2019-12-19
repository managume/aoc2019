# Adviento de Código 2019

## Día 8: Formato de Imagen Espacial

### Parte 1

Los ánimos se levantan cuando los elfos se dan cuenta de tienes la oportunidad de reiniciar uno de sus Mars rovers, así que sienten curiosidad por saber si pasarías una breve estancia en Marte. Aterriza tu nave cerca del rover.

Cuando alcanzas el rover, ¡descubres que ya está en el proceso de reinicio! Está esperando que alguien meta la clave de la [BIOS](https://en.wikipedia.org/wiki/BIOS). El elfo responsable del rover toma una foto de la contraseña (entrada del puzle) y te la envía vía la Red de Envío Digital

Desafortunadamente, las imágenes enviadas por la Red de Envío Digital no están codificadas con ninguna codificación normal. En vez de ello, están codificadas con un formato especial de Imagen Espacial. Ninguno de los elfos parece recordar por qué está así. Te envían las instrucciones para decodificarlo.

Las imágenes son enviadas como una serie de digitos en el que cada uno representa el color de un único píxel. Los dígitos rellenan cada file de la imagen de izquierda a derecha, luego bajan a la siguiente fila, rellenando las filas de arriba a abajo hasta que cada píxel de la imagen está relleno.

Cada imagen consiste en una serie de **capas** de idéntico tamaño que están rellenas de esta manera. Así, el primer dígito corresponde con el píxel situado en la esquina superior izquierda de la primera capa, el segundo dígito se corresponde con el píxel a la derecha del anterior de la misma capa, y así sucesivamente hasta el último dígito, que se corresponde con el píxel de la esquina inferior derecha de la última capa.

Por ejemplo, dada una imagen de `3` píxeles de ancho y `2` píxeles de alto, los datos de la imagen `123456789012` corresponden a las siguientes capas de imagen: 

```
Capa 1: 123
        456

Capa 2: 789
        012
```
La imagen que recibes es de **`25` píxeles de ancho y `6` píxeles de alto**.

Para asegurarse de que la imagen no ha sido corrompida durante la transmisión, los elfos quieren que encuentres la capa que contiene el **menor número de dígitos `0`**. En esa capa, ¿cuál es el **número de dígitos `1` multiplicados por el número de dígitos `2`**?

### Parte 2