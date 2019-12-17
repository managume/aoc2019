# Adviento de Código 2019

## Día 2: Alarma de Programa 1202

### Primera parte

En mitad de maniobra de [asistencia gravitatoria](https://es.wikipedia.org/wiki/Asistencia_gravitatoria), tu ordenador de abordo suelta un pitido debido a una "[alarma de programa 1202](https://www.hq.nasa.gov/alsj/a11/a11.landing.html#1023832)". En la radio, un elfo ya te está explicando cómo manejar la situación: "No te preocupes, esto es perfectamente norma--" El ordenador de abordo [arde en llamas](https://es.wikipedia.org/wiki/Halt_and_Catch_Fire).

Notificad a los elfos que el [humo mágico](https://en.wikipedia.org/wiki/Magic_smoke) del ordenador parece haberse disipado. "Ese ordenador ejecutaba programas **Intcode** como el programa de asistencia gravitatoria que estaba funcionando ¡Seguramente hay suficientes piezas de repuesto para construir un nuevo ordenador Intcode!"

Un programa Intcode es una lista de [enteros]() separados por comas (como 1,0,0,3,99). Para ejecutar uno, empieza por el primer entero (llamado posición 0). Aquí, encontrarás un **opcode** - 1, 2 o 99. El opcode indica qué hacer; por ejemplo, 99 significa que el programa ha terminado y debería parar inmediatamente. Encontrarse un opcode desconocido significa que algo ha ido mal.

Opcode 1 **suma** dos número leidos desde dos posiciones y almacena el resultado en una tercera posición. Los tres enteros **inmediatamente después** del opcode que te dicta esas tres posiciones - los dos primeros indican las **posiciones** desde donde deberías leer los valores de entrada, y el tercero indica la **posición** en donde la salida debería ser almacenada.

Por ejemplo, si tu ordenador Intcode encuentra los valores 1,10,20,30, debería leer los valores de las posiciones 10 y 20, sumar dichos valores, y entonces sobrescribir el valor en la posición 30 con el resultado de la suma.

Opcode 2 funciona exactamente como el opcode 1, excepto que **multiplica** los dos valores de entrada en vez de sumarlos. De nuevo, los tres enteros después del opcode indican **donde** están los valores de entrada y de salida, no sus valores.

Una vez hayas procesado un opcode correctamente, **avanza al siguiente** adelantando 4 posiciones.

Por ejemplo, supón que tienes el siguiente programa:

1,9,10,3,2,3,11,0,99,30,40,50

Con el propósito de ilustrarlo, aquí esta el mismo programa dividido en diferentes líneas.

1,9,10,3,
2,3,11,0,
99,
30,40,50

El primero de los cuatro enteros, 1,9,10,3, son las posiciones 0, 1, 2 y 3. Juntas, representan el primer opcode (1, suma), las posiciones de dos valores de entradas (9 y 10), y la posición del valor de salida (3). Para manejar este opcode, primero necesitas acceder a los valores en las posiciones de entrada: la posición 9 contiene el valor 30, y la posición 10 contiene el valor 40. Suma dichos números para conseguir un resultado de 70. Entonces, almacena este valor en la posición de salida; aquí, la posición de salida (3) está **en** la posición 3, por lo que sobrescribe el mismo.

1,9,10,**70**,
2,3,11,0,
99,
30,40,50

Avanza 4 posiciones para alcanzar el siguiente opcode, 2. Este opcode funciona como el anterior, pero multiplica en vez de sumar. Los valores de entrada están en las posiciones 3 y 11; estas posiciones contienen los valores 70 y 50 respectivamente. Multiplicando estos valores se tiene como resultado 3500; este valor es almacenado en la posición 0.

**3500**,9,10,70,
2,3,11,0,
99,
30,40,50

Avanzando 4 posiciones más llegas al opcode 99, deteniendo el programa.

Aquí están los estados iniciales y finales de unos pocos mas programas:

1,0,0,0,99 pasa a ser **2**,0,0,0,99 (1 + 1 = 2).
2,3,0,3,99 pasa a ser 2,3,0,**6**,99 (3 * 2 = 6).
2,4,4,5,99,0 pasa a ser 2,4,4,5,99,**9801** (99 * 99 = 9801).
1,1,1,4,99,5,6,0,99 pasa a ser **30**,1,1,4,2,5,6,0,99.

Una vez tengas un ordenador funcionando, el primer paso es restaurar el programa de asistencia gravitacional (la entrada del puzles) al estado de "alarma de programa 1202" que tuvo antes de que el último ordenador se prendiera fuego. Para hacer esto, **antes de ejecutar el programa**, reemplaza la posición 1 con el valor 12 y reemplaza la posición 2 con el valor 2. ¿**Qué valor hay en la posición 0** tras detenerse el programa?

### Segunda parte

"¡Bien, el nuevo ordenador parece estar funcionando correctamente! **Tenlo a mano** durante esta misión, probablemente lo usarás otra vez. Los ordenadores Intcode reales soportan muchas más instrucciones que el tuyo, pero te haremos saber cuales son, si las necesitas"

"Además, tu prioridad actual debe ser completar tu asistencia gravitatoria alrededor de la Luna. Para que esta misión sea un éxito, debemos acordar una terminología para las partes que ya has construido.!

Los programas Intcode son dados como una lista de enteros; estos valores son usados como el estado inicial de la **memoria** de la computadora. Cuando ejecutas un programa Intcode, asegúrate de empezar inicializando la memoria con los valores del programa. Una posición en memoria es conocida como **dirección** (por ejemplo, el primer valor en memoria está en la "dirección 0").

Opcodes (como *1*, *2*, o *99*) marcan el inicio de una **instrucción**. Los valores usados inmediatamente despues de un opcode, si hay alguno, son conocidos como **parámetros** de instrucción. Por ejemplo, en la instrucción *1,2*,*3*,*4*, *1* es el opcode; *2*,*3* y *4* son los parámetros. La instrucción *99* contiene únicamente un opcode, sin parámetros.

La dirección de la instrucción actual se llama **instrucción puntero**; empieza por *0*. Después de que una instrucción finalice, el puntero de instrucción incrementa el **número de valores en la instrucción**; hasta que añadas más instrucciones al computador, este es siempre *4* (*1* opcode + *3* parámetros) para las instrucciones de suma y producto. (La instrucción de interrupción incrementaría en 1 el puntero de instrucción, pero interrumpe el programa en su lugar).

"Vista la terminología, estamos listo para proceder. Para completar la asistencia gravitatoria, necesitas **determinar que par de valores de entrada producen la salida *19690720*.**"

Los valores de entrada todavía deben de ser provisto al programa reemplazando los valores en las direcciones *1* y *2*, justo como antes. En este programa, el valor situado en la dirección *1* se llama **nombre**, y el valor situado en la dirección *2* se llama **verbo**. Cada uno de los dos valores de entrada estarán entre *0* y *99*, inclusive.

Una vez el programa se haya detenido, su valor de salida estará disponible en la dirección *0*, al igual que antes. Cada vez que intentes un par de valores de entrada, asegúrate primero de **reiniciar los valores de la memoria del computador en el programa** (tus valores de entradas del puzles) - en otras palabras, no reutilices memoria de un intento anterior.

Encuentra el valor de entrada nombre y verbo que causan que el programa produzca el valor de salida *19690720*. **¿Qué da 100 * nombre + verbo?** (Por ejemplo, *si nombre=12* y *verbo=2*, la respuesta sería *1202*)