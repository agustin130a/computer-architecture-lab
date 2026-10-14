<!-- p. 187 -->

## Unidad 5: Jerarquia de Memoria
     Para mantener la CPU funcionando de manera óptima, es necesario asegurar un flujo constante
de datos e instrucciones mediante el acceso a memoria. Si bien el ancho de banda de las memorias ha
crecido a razón de un 9 % anual (hasta 1999), la demanda de la CPU sobre la memoria ha aumentado a
una tasa considerablemente mayor (50 % anual hasta 1999). Esto genera una brecha significativa entre
el rendimiento de la CPU en términos de velocidad y la velocidad con la cual se puede suministrar
el flujo de datos e instrucciones. Contar con más memoria permite un mayor uso de datos, pero el
desafío es que la velocidad óptima de memoria debería igualar la velocidad del procesador para evitar
tiempos de espera en la transferencia de operandos y almacenamiento de resultados. Además, el costo
de la memoria debe ser razonable para que el sistema sea económicamente accesible. La demanda de
anchura de banda con memoria crece.

### Características de la Memoria
     Los puntos fundamentales relacionados con la memoria incluyen: Cantidad, Velocidad y Coste
     Las siguientes observaciones son generalmente válidas:
       A menor tiempo de acceso, mayor coste.
       A mayor capacidad, mayor coste.
       A mayor capacidad, menor velocidad.

#### Solución
    Para cumplir con los requerimientos de capacidad, velocidad y costo, es fundamental implementar
una estructura de memoria que aproveche la cercanía de referencias. Esta estrategia permite una com-
binación de diferentes tipos de memoria que optimiza el rendimiento total, acercándolo al rendimiento
de la memoria más rápida.

### Jerarquía de Memoria
    La jerarquía de memoria se refiere a la organización piramidal de los distintos niveles de memoria
en los sistemas informáticos. Su objetivo es obtener el rendimiento de una memoria de alta velocidad
al costo de una memoria de baja velocidad, basándose en el principio de cercanía de referencias.

<!-- p. 188 -->

   Un computador típico está formado por diversos
   niveles de memoria organizados de manera jerár-
   quica:

          Nivel 0: Registros de la CPU.

          Nivel 1: Memoria caché.

          Nivel 2: Memoria principal.

          Nivel 3: Memoria secundaria. Disco duro
          (con el mecanismo de memoria virtual).

          Nivel 4: Cintas magnéticas. Son las más len-
          tas y de mayor capacidad.

   El coste de todo el sistema de memoria suele exce-
   der al coste de la CPU, por lo que resulta funda-
   mental optimizar su uso.

#### Propiedades de la Jerarquía de Memoria
   El principio de cercanía en la jerarquía de memoria incluye los siguientes conceptos clave:
      Localidad Espacial: Si en un momento se hace referencia a una posición específica de memoria,
      es probable que esa misma posición sea referenciada nuevamente en el futuro cercano. Esto se
      logra almacenando una copia de los datos en la caché, permitiendo un acceso más rápido.
      Localidad Temporal: Cuando se accede a una localización de memoria en un momento dado, es
      probable que las localizaciones cercanas sean referenciadas poco después. Este concepto permite
      estimar las posiciones cercanas y optimizar su acceso.
      Localidad Secuencial: Las direcciones de memoria utilizadas suelen ser contiguas, ya que las
      instrucciones se ejecutan de forma secuencial.
   Además, la jerarquía de memoria sigue dos propiedades fundamentales:
      Inclusión: Cualquier información contenida en el nivel de memoria Mi debe estar presente
      también en los niveles Mi+1 , Mi+2 , etc.
      Coherencia: Las copias de la misma información en diferentes niveles de memoria deben man-
      tenerse coherentes. Esto se asegura mediante políticas de actualización, como Write Through y
      Write Back.

#### Gestión de la Jerarquía de Memoria
   La gestión de la jerarquía de memoria debe perseguir los si-
   guientes objetivos:

          Optimizar el uso de la memoria.

          Crear la ilusión de una memoria con un tiempo de ac-
          ceso similar al del nivel de memoria más rápido y un
          costo por bit similar al nivel más económico.

<!-- p. 189 -->

    La gestión de la jerarquía de memoria se realiza de manera dinámica, es decir, en tiempo de
ejecución, y abarca únicamente algunos niveles: el nivel de caché (nivel 1), la memoria principal (nivel
2) y la memoria secundaria (nivel 4).
    Nota: El nivel 0 (registros) es asignado por el compilador en tiempo de compilación, mientras que
el nivel 4 (cintas y CD-ROMs) se destina a copias de seguridad.

#### Gestión de la Memoria Caché
    La memoria caché controla la transferencia de información entre la memoria caché y la memoria
principal. Este proceso es generalmente realizado por un hardware específico, la Unidad de Gestión de
Memoria (MMU, por sus siglas en inglés).

#### Gestión de la Memoria Virtual
  La memoria virtual controla la transferencia de información entre la memoria secundaria y la
memoria principal. Esta gestión es realizada en parte por el sistema operativo y en parte por la MMU.

### Terminología
       Bloque: Es la unidad mínima de transferencia de datos entre dos niveles de la jerarquía de
       memoria.

       Acierto (hit): Ocurre cuando el dato solicitado se encuentra en el nivel de memoria “i”.
       Conceptos asociados a los aciertos:

         • Tasa de aciertos (hit ratio): Es el porcentaje de aciertos en el nivel “i” y se calcula como
           el cociente entre los aciertos en i y los accesos totales a i.
         • Tiempo de acierto: Es la suma del tiempo de acceso al nivel “i” y el tiempo de detección
           de un acierto.

       Fallo (miss): Ocurre cuando el dato solicitado no se encuentra en el nivel “i” y debe buscarse
       en el nivel “i + 1”.
       Conceptos asociados a los fallos:

         • Tasa de fallos (miss ratio): Es el porcentaje de fallos en el nivel “i” y se calcula como
           1 − Tasa de aciertos.
         • Tiempo de penalización por fallo: Es la suma del tiempo necesario para sustituir un
           bloque del nivel “i” y el tiempo de acceso al dato. El tiempo de penalización por fallo es
           mayor que el tiempo de acierto.

#### Políticas de Emplazamiento en Memoria Caché
    Dado que la memoria principal es mucho mayor que la memoria caché, es necesario decidir en qué
marco de caché se ubicará un bloque. La elección de una política de emplazamiento afecta directamente
la organización de la memoria caché.
    Emplazamiento (de bloques de caché): Es la regla que determina en qué línea o conjunto
de la caché puede ubicarse (mapearse) un bloque traído desde memoria principal. Según el tipo de
caché, el emplazamiento puede ser: directo (cada bloque va a una única línea), asociativo por
conjuntos (puede ir a cualquiera de las líneas dentro de un conjunto) o totalmente asociativo
(puede ir a cualquier línea de la caché). El emplazamiento influye en los conflictos y en la tasa de
misses.

<!-- p. 190 -->

#### Emplazamiento Directo (Caché Directa)
                                                        donde:
   En la caché directa, cada bloque de memoria prin-         M B: Número de marco en la caché.
   cipal ocupa siempre el mismo marco de la caché.
   Este marco se determina con la expresión:                 B: Número de bloque de la memoria princi-
                                                             pal.
                     MB = B    mód M                        M : Número de marcos en la memoria caché
                                                             (tamaño de la caché).

Ejemplo Supongamos una memoria principal de 16 bytes y una caché de 4 bytes. En este caso, un
acceso a la caché requiere dos tiempos: uno para determinar si el dato se encuentra en caché y otro
para el acceso propiamente dicho (tiempo de acceso y tiempo de detección de acierto).

                                                        No es posible almacenar los 16 bytes de memoria
                                                        en los 4 bytes de caché, por lo que se almacena el
                                                        primer elemento de cada grupo de 4 bytes. Esto
                                                        implica que:

                                                             La posición 0 de la caché almacena los datos
                                                             de las posiciones de memoria 0, 4, 8, etc.

                                                             En general, se guarda cualquier posición de
                                                             memoria cuyos dos bits menos significativos
                                                             de la dirección sean ceros (los dos bits más
                                                             significativos indican el número de grupo, y
                                                             los menos significativos se usan para identifi-
                                                             car el byte dentro del grupo).

                                                             Dirección <1:0> ⇒ Índice de Caché.

Condiciones de Carga en Caché La información se lleva a la caché cuando se intenta acceder a
alguno de los bytes de un grupo y dicho byte no se encuentra en la caché.

Localización de Información en la Caché Consideremos una caché directa de 1 KB, con bloques
de 32 bytes. Para una caché de 2N direcciones, partimos de una dirección de memoria de 32 bits.
   La caché está dividida en N bloques (marcos) de 32 bytes cada uno, y cada uno de estos marcos
hace referencia a uno de los grupos de bloques en los que está dividida la memoria principal. El índice
de caché hace referencia a uno de los bloques dentro de la caché.

      Los M bits menos significativos de la dirección seleccionan el byte dentro del bloque (siendo el
      tamaño del bloque 2M ).

      Cada bloque en la caché tiene un tag asociado, que indica cuál de los bloques de la memoria
      principal está copiado en el bloque de caché al que se está haciendo referencia.

      Cada bloque tiene un bit de validez (Valid bit) que indica si el dato está actualizado.

    Los (32 − N ) bits más significativos de la dirección de memoria corresponden al tag. Este tag se
compara con el tag almacenado en la caché para determinar si el bloque de memoria al que se refiere
la dirección se encuentra en caché (hit) o no (miss).

<!-- p. 191 -->

   De esta manera, la caché contiene las partes de la memoria principal que se están utilizando en el
momento, simplificando el acceso a la memoria. No es necesario recorrer toda la caché; en su lugar, se
accede directamente al bloque correspondiente y se determina, mediante el tag, si el dato es el deseado
o no.

Alta tasa de fallos por aliasing En esta arquitectura de caché directa, se produce un problema
significativo debido a que muchos bloques compiten por el mismo marco en la caché, generando una
alta tasa de fallos o misses. Este problema, conocido como aliasing, ocurre porque múltiples direcciones
de memoria tienen el mismo índice de caché y, por lo tanto, ocuparían el mismo bloque en la caché.
Esto resulta en un miss cada vez que se intenta acceder a un dato diferente dentro del mismo grupo
de bloques de la memoria principal.

### Memoria Asociativa por Conjuntos (N-way Asociativa)
    Para reducir el problema de aliasing, se emplea la memoria N-way asociativa, que utiliza N bancos
de caché (cada uno con su propio bloque, tag y bit de validez), operando en paralelo. Generalmente,
se utilizan 2, 4, 8, etc., bancos de caché.

Ejemplo: Caché 2-way Asociativa            En una caché 2-way asociativa, el funcionamiento es el si-
guiente:

       El índice de caché selecciona un conjunto dentro de la caché.

       Los dos tags en el conjunto de bancos de caché se comparan en paralelo.

       El dato se selecciona en función de los resultados de la comparación de los tags.

<!-- p. 192 -->

#### Cache Directa vs Cache Asociativa por Conjuntos

                       Caché Directa vs Caché Asociativa por Conjuntos
              Parámetro                  Caché Directa              Asociativa por Conjuntos
          Número requerido de
                                                 1                                N
            comparadores
                                                                    Se tiene un retardo extra al
                                                                    acceder a los datos debido a
                Retardo                          -
                                                                      que deben pasar por un
                                                                            multiplexor.
                                       El bloque de caché es
                                     accesible antes del hit, se
         ¿Cuándo es accesible el                                    El dato llega después del hit
                                     puede asumir un acierto,
                dato?                                                        del acceso.
                                       continuar y hacer una
                                   recuperación en caso de fallo.

### Caché Totalmente Asociativa (Fully Associative Cache)
    Una caché totalmente asociativa permite almacenar un dato en cualquier posición libre de la caché.
En este tipo de caché, el tag corresponde a la dirección completa de 32 bits de la memoria. Sin embargo,
el inconveniente principal de esta organización es que, al buscar un dato, se debe recorrer la tabla de
tags de la caché, que no está ordenada, para encontrar el dato requerido. Esta búsqueda puede ser
lenta si se compara cada tag de forma secuencial, o muy costosa en términos de hardware si se realiza
una comparación en paralelo de todos los tags.
    Este método de almacenamiento es útil cuando la caché es de tamaño muy reducido (por ejemplo,
de 4 u 8 entradas).

Ventajas

       Baja tasa de fallos, ya que cada bloque se puede ubicar en cualquier marco disponible.

<!-- p. 193 -->

Desventajas

       Alta complejidad de hardware.

       Directorio grande debido a las etiquetas largas.

       Necesidad de algoritmos de reemplazo, que añaden sobrecarga de memoria.

   Si la asociatividad de una caché es baja, un bloque de memoria (RAM) tiene muy pocas
   ubicaciones posibles dentro de la caché. En el caso extremo de una caché mapeo directo
   (1-vía), cada bloque de RAM tiene una única ubicación posible (una sola línea) en la caché,
   lo que aumenta la probabilidad de misses por conflicto.

### Consideraciones de Diseño de una Memoria Caché
    Una memoria caché es una memoria pequeña y rápida situada entre el procesador y la memoria
principal. Su función principal es almacenar una copia de la porción de información actualmente en
uso de la memoria, con el objetivo de disminuir el tiempo de acceso.

### Estructura de la Caché
       Memoria Principal (Mp): Constituida por 2n palabras direccionables, divididas en nB bloques
       de tamaño fijo.

       Memoria Caché (Mc): Compuesta por nM marcos de bloque (donde nM ≪ nB).

       Directorio en la Caché: Indica qué subconjunto de los nB bloques de la memoria principal
       reside actualmente en los nM marcos de bloque en la caché.

### Políticas de Reemplazo
   Cuando se intenta acceder a una palabra que no se encuentra en la caché (fallo de escritura), es
necesario trasladar todo el bloque de información correspondiente desde la memoria principal a la

<!-- p. 194 -->

memoria caché. Si existe espacio en la caché, se sigue la política de emplazamiento. Sin embargo, si
no hay espacio disponible, se debe determinar qué bloque eliminar para introducir el nuevo, aplicando
así una política de reemplazo. Estas políticas deben cumplir los siguientes requisitos:

       Implementarse completamente en hardware, ya que la implementación en software es muy lenta.
       La caché busca acercar la velocidad de trabajo de la memoria a la del procesador.

       Realizar la selección en el ciclo de memoria principal, mientras se trae el nuevo bloque.

       Intentar seleccionar un bloque que no sea necesario en el futuro, aunque esto es difícil debido a
       la imprevisibilidad del comportamiento de los programas.

    El espacio de reemplazo es el conjunto de bloques candidatos a ser reemplazados. Su alcance
depende de la política de emplazamiento utilizada. En el caso de caché de emplazamiento directo,
cada bloque tiene un marco asignado de forma fija. En una caché asociativa, el espacio de reemplazo
incluye toda la caché, mientras que en una caché asociativa por conjuntos, el espacio de reemplazo
es limitado a los marcos del conjunto específico. La política de reemplazo elegida debe minimizar la
cantidad de fallos y ser viable en términos de complejidad de implementación.

### Reemplazo Aleatorio
    En esta política, el bloque a reemplazar se elige de forma aleatoria. Este método es fácil de im-
plementar en hardware y permite tiempos de acceso bajos. Sin embargo, tiene una tasa de fallos
relativamente alta en comparación con otras políticas de reemplazo.

### Reemplazo FIFO (First-In, First-Out)
    Esta política reemplaza el bloque en el espacio de reemplazo que ha estado más tiempo cargado
en la caché. Es simple de implementar y sigue una estrategia lineal.

### Menos Recientemente Usado (LRU)
    La política LRU reemplaza el bloque menos recientemente usado. Es sencilla de implementar para
conjuntos asociativos de dos bloques, pero cuando el número de bloques es mayor, se utilizan contadores
llamados registros de edad en lugar de un único bit.

### Menos Frecuentemente Usado (LFU)
   Esta política reemplaza el bloque que ha sido menos referenciado en el espacio de reemplazo. Para
implementar LFU, se emplean registros contadores que registran la cantidad de veces que cada bloque
ha sido referenciado.

### Políticas de Actualización
### Write Through o Escritura Directa
    En esta política, cada escritura actualiza tanto la caché como la memoria principal. En los fallos
de lectura, el bloque de caché a reemplazar siempre es sobrescrito, independientemente de si ha sido
modificado o no, lo que asegura la coherencia. Cuando se necesita vaciar la caché o modificar un dato,
no se requiere acceso adicional a la memoria principal, ya que los datos en esta ya están actualizados.
Solo se necesita un bit de control, el de validez.
    Ventajas:

<!-- p. 195 -->

      Nunca hay inconsistencia, lo cual permite que los fallos de lectura sean más rápidos al no requerir
      escrituras en el nivel inferior.

      Es más sencilla de diseñar y de manejar debido a su control simple.

   Desventajas:

      Tiene bajo rendimiento en escritura, ya que cada actualización en la caché implica un acceso a
      la memoria principal.

      Genera una alta demanda en el bus (requiere mayor ancho de banda).

    Para mejorar su rendimiento, se puede utilizar un buffer de escritura que almacena temporalmente
los datos mientras esperan ser escritos en la memoria principal.

### Write Back o Post Escritura
   En la política Write Back, sólo se actualiza la caché durante una escritura. Antes de eliminar un
dato de la caché, este se transfiere a la memoria principal si ha sido modificado. Los bits de control
necesarios son:

      V (Validez): Indica si el dato está presente en la caché.

      D (Dirty o Sucio): Indica si el dato ha sido modificado desde la última vez que se accedió a
      él. Si el dato está marcado como sucio, debe ser escrito en la memoria principal antes de ser
      reemplazado; si no, se puede eliminar sin actualización adicional.

   Ventajas:

      El procesador puede escribir palabras individuales a la velocidad de la caché.

      Múltiples escrituras en un bloque requieren sólo una actualización en el nivel inferior de la
      jerarquía, reduciendo el tráfico entre la caché y la memoria principal.

      Utiliza menor ancho de banda y permite una mejor tolerancia a la alta latencia de la memoria,
      ya que no requiere accesos constantes a la memoria principal.

   Desventajas:

      Requiere hardware más costoso.

      Puede generar inconsistencias en el sistema de memoria.

### Rendimiento
#### Rendimiento de la Caché
   Teniendo en cuenta el CPI, el reloj del sistema, las instrucciones y el acceso a datos en memoria
considerando los casos de miss:

                   Tiempo CPU = (Ciclos CPU + Ciclos de espera de memoria) × Tc
   donde los Ciclos de espera de memoria se calculan como:

Ciclos de espera de memoria = Accesos a memoria × Tasa de fallos × Tiempo de penalización de fallo

<!-- p. 196 -->

    Al multiplicar y dividir por el número de instrucciones, podemos expresar el tiempo de CPU de la
siguiente manera:

Tiempo CPU = N° de instr × (CPI + accesos por instr × Tasa de fallos × Penalización de fallo) × Tc

   La fórmula simplificada para el tiempo de CPU es:

                                                  ma
                                                                 
                               CPUtime = IC CPI +    MRMP Tc
                                                   i
   Donde:

      IC: Número de instrucciones.

      CPI: Ciclos por instrucción.

      ma : Acceso a memoria.

      i: Instrucción.

      MR: Miss rate (tasa de fallos).

      MP: Miss penalty (penalización por fallo).

### Mejorar el Rendimiento de la Caché
   Para optimizar el rendimiento de la caché, se pueden aplicar las siguientes estrategias:

#### Reducir la Tasa de Fallos de la Caché (MR)

      Reducir la Penalización por Fallos.

      Reducir el Tiempo de Acceso a la Caché.

5.16.1.    Reducir la Tasa de Fallos de la Caché (MR)
   Existen diferentes tipos de fallos en la caché que afectan su rendimiento:

      Fallos Iniciales: Ocurren siempre en la primera búsqueda en la caché, ya que esta se encuentra
      vacía.

      Fallos por Capacidad: Suceden debido al tamaño limitado de la caché y a la propiedad de
      localidad temporal.

      Fallos por Conflicto: Aparecen cuando dos bloques intentan ocupar el mismo espacio debido
      a la política de emplazamiento utilizada.

<!-- p. 197 -->

#### Cambiar la Asociatividad
    Aumentar la asociatividad de la caché puede reducir la tasa de fallos de conflicto, ya que se
contará con más marcos. Sin embargo, el tiempo de acceso a los datos y el coste de hardware se ven
incrementados debido a que hay que agregar más entradas al multiplexor que buscará los datos.
    A medida que aumenta la capacidad de la caché, la asociatividad (1-way, 2-way, etc.) pierde
influencia en la tasa de fallos, ya que para los distintos tipos de caché, esta tasa converge a medida que
la capacidad aumenta. Esto quiere decir que para una caché de gran tamaño no tiene sentido colocar
una caché totalmente asociativa, mientras que para una caché pequeña, aumentar la asociatividad sí
va a producir una mejora considerable.

#### Cambiar el Tamaño del Bloque
    El tamaño de bloque en la memoria caché se refiere a la cantidad de palabras contiguas que se
almacenan juntas en un solo bloque de caché. El tamaño mínimo de bloque es de una palabra, y
el tamaño máximo es el de la memoria caché (en este caso, la caché almacenaría un solo valor que
ocuparía la totalidad de la caché).
    Si el tamaño es de una sola palabra o de unas pocas palabras, es probable que sucedan muchos
fallos de memoria debido a la propiedad de localidad espacial (es probable que se necesite traer a caché
las palabras cercanas al bloque). Si el bloque es de unas cuantas palabras, la tasa de fallos se reducirá
por el mismo motivo (las palabras cercanas ya se encontrarán en memoria).
    Si el tamaño del bloque aumenta de manera excesiva, aumentará la tasa de fallos y también el
tiempo de penalización por fallo. Esto se debe a que, cuando se busque un bloque demasiado grande,
este contendrá datos que no necesariamente se encuentran en la localidad del bloque ya cargado. Por
ende, será necesario cambiar tanto el bloque que ya estaba en caché como el bloque recientemente
cargado para que haya proximidad espacial entre los datos de la caché.

   El efecto del tamaño del bloque es mayor para cachés de menor tamaño (y viceversa). Se debe
entonces encontrar un tamaño óptimo para el bloque.

<!-- p. 198 -->

#### Cambiar el Algoritmo de Reemplazo

   El algoritmo de reemplazo utilizado tie-
   ne un impacto significativo en la tasa de
   fallos de capacidad. Las diferencias entre
   algoritmos, como el Least Recently Used
   (LRU) y el reemplazo Aleatorio, tienden
   a disminuir a medida que aumenta el ta-
   maño de la caché.

#### Caché Víctima (CV)

                                  La caché víctima es una pequeña caché totalmente asociativa que se co-
                                  loca junto a la caché principal en la jerarquía de memoria. Su propósito
                                  es reducir la tasa de fallos de la caché principal.
                                  Cuando se produce un fallo en la caché principal (Mc), es decir, cuando
                                  el dato buscado no se encuentra en la caché, se verifica si el bloque
                                  deseado está presente en la caché víctima. Si el bloque se encuentra en
                                  la caché víctima, se realiza un intercambio entre el bloque de la caché
                                  principal y el bloque de la caché víctima (esto permite buscar el bloque
                                  en la caché víctima en lugar de en la memoria principal Mp, lo cual es
                                  más rápido).
                                  La caché víctima es especialmente útil para cachés pequeñas de empla-
                                  zamiento directo. En una caché de 4 KB con una memoria víctima de
                                  cuatro entradas, es posible reducir entre el 20 % y el 95 % de los fallos.
                                  Cuanto menor es la memoria caché principal, más efectiva resulta la
                                  caché víctima.

<!-- p. 199 -->

#### Caché Pseudo Asociativa

    Es un tipo de memoria caché que combina características de las cachés de emplazamiento directo
y las cachés totalmente asociativas.
    Al igual que en las cachés de emplazamiento directo, la caché pseudo asociativa se divide en marcos,
que corresponden a grupos de bloques de la memoria principal. Cada marco tiene una etiqueta que
se compara con la etiqueta contenida en la dirección solicitada para determinar si el dato deseado
se encuentra en el marco. Dentro de la caché, el índice del conjunto se utiliza para referenciar los
diferentes marcos y el desplazamiento se utiliza para referenciar los bytes dentro del marco.
    Si hay un acierto, se accede al dato correspondiente en ese bloque. Sin embargo, si hay un fallo, el
comportamiento es diferente al de las cachés de emplazamiento directo:
    En una caché pseudo asociativa se utiliza toda la capacidad de la caché para reubicar algunos
bloques extra en marcos que no corresponden al grupo de dichos bloques en memoria principal. Luego,
ante un fallo, en lugar de buscar el dato en memoria principal, se busca en estos marcos que contienen
bloques extra (pseudo conjuntos). El marco en el que se busca es el correspondiente al índice de
conjunto pero con el bit más significativo invertido. Esto permite que un bloque de memoria principal
se pueda ubicar en dos marcos de memoria caché (pseudo asociativa de dos vías).

#### Caché con Prebúsqueda
   La caché con prebúsqueda se basa en ocultar la latencia de un fallo de caché anticipando las
búsquedas en memoria antes de que el procesador demande el dato que no se encuentra en caché.
Esto se logra solapando el acceso a memoria con instrucciones independientes (que no tengan acceso
a memoria) anteriores a la instrucción que requiere el dato. Dado que en esta anticipación no se
involucran registros, esto no genera riesgos. Sin embargo, existe la posibilidad de que se realicen
búsquedas innecesarias. Existen dos formas de implementar la prebúsqueda:

<!-- p. 200 -->

Prebúsqueda por Software El compilador introduce instrucciones especiales de prebúsqueda. La
eficiencia depende del compilador y del tipo de programa (funciona bien para bucles, patrones de
acceso a arrays simples y aplicaciones de cálculo, pero no para aplicaciones con instrucciones enteras
que presentan un amplio reuso de la caché). La prebúsqueda puede tener como destino la caché o un
buffer de prebúsqueda.
      Las instrucciones de prebúsqueda no generan excepciones.
      Es una forma de especulación.
      La introducción de nuevas instrucciones implica un overhead.
      Mientras más búsquedas se realicen, más se ocupará la memoria.

Prebúsqueda por Hardware La prebúsqueda secuencial permite anticipar un bloque adicional de
memoria. Puede implementarse de las siguientes maneras:
      Prebúsqueda sobre Fallo: Se prebusca el bloque b + 1 si el acceso al bloque b produce un
      fallo.
      Prebúsqueda Marcada: Se incluye un tag en cada bloque. Si un bloque marcado es buscado
      o prebuscado, el siguiente se prebusca. Esta técnica sigue bien la localidad espacial.
      Prebúsqueda Adaptativa: El grado de prebúsqueda (número de bloques prebuscados) se
      ajusta en función del comportamiento.
      Prebúsqueda con ”Stride” Arbitrario: Anticipa los datos prebuscando bloques en la caché
      siguiendo un patrón de saltos específico en las direcciones de memoria. En lugar de prebuscar
      bloques adyacentes, se prebuscan bloques en la caché utilizando un patrón de acceso conocido
      como ”stride” o paso. Por ejemplo, se pueden prebuscar bloques con un salto de dos o tres
      direcciones. Esta estrategia es útil cuando se detecta un patrón regular de acceso con saltos
      constantes en las direcciones de memoria.

#### Optimizar en Tiempo de Compilación
   Durante la compilación, pueden realizarse modificaciones en el código que aumenten la localidad
espacial y/o temporal y reduzcan la tasa de fallos de la caché. Existen varias técnicas que el compilador
puede aplicar sobre el código para mejorar el rendimiento de la caché:
      Fusión de arrays: Mejora la localidad espacial para disminuir los fallos. Consiste en colocar
      las mismas posiciones de diferentes arrays en posiciones contiguas de memoria.

<!-- p. 201 -->

      Fusión de bucles: Mejora la localidad temporal para disminuir los fallos. Fusiona los bucles
      que usen los mismos arrays para aprovechar los datos que se encuentran en caché antes de
      desecharlos.

      Intercambio de bucles: Mejora la localidad espacial para disminuir los fallos por conflictos.
      Depende de cómo el lenguaje almacene los datos. Por ejemplo, en el lenguaje C, las matrices se
      almacenan por filas, por lo que se debe variar en el bucle interno la columna.

      Alargamiento de arrays: Mejora la localidad espacial para disminuir los fallos. Evita que en
      cada iteración del bucle se compita por el mismo marco de bloque.

<!-- p. 202 -->

    Descomposición en bloques: Disminuye la tasa de fallos por capacidad mejorando la localidad
temporal. Para ilustrar su funcionamiento, se puede utilizar como ejemplo una multiplicación de ma-
trices. En lugar de operar sobre una fila o columna completa, se trabaja en sub-bloques, maximizando
los accesos a datos ya cargados antes de que sean desechados.
    Ejemplo: Multiplicación de matrices C = A × B. Sin descomposición en bloques se tiene:

void matrixMultiplication(int** A, int** B, int** C, int N) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            for (int k = 0; k < N; k++) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }
}

   Si las matrices son lo suficientemente grandes, es posible que no quepan todos sus elementos en la
memoria caché. Esto genera fallos por capacidad cada vez que se necesita acceder a un elemento de la
matriz que no está en caché, lo cual sucede frecuentemente debido a que la multiplicación de matrices
implica acceder a múltiples elementos de diferentes filas y columnas que pueden estar dispersos en
memoria.
   Aplicando descomposición en bloques:

void matrixMultiplication(int** A, int** B, int** C, int N, int blockSize) {
    for (int i = 0; i < N; i += blockSize) {
        for (int j = 0; j < N; j += blockSize) {
            for (int k = 0; k < N; k += blockSize) {
                // Realizar multiplicación en bloques
                for (int ii = i; ii < i + blockSize; ii++) {
                    for (int jj = j; jj < j + blockSize; jj++) {
                        for (int kk = k; kk < k + blockSize; kk++) {
                            C[ii][jj] += A[ii][kk] * B[kk][jj];
                        }
                    }
                }
            }
        }
    }
}

    La matriz de tamaño N × N se divide en bloques más pequeños de tamaño blockSize. Al dividir
las matrices en bloques, se mejora la localidad temporal ya que se trabajará con un conjunto más

<!-- p. 203 -->

pequeño de datos en cada iteración del bucle interno. Este conjunto más pequeño de datos podrá
alojarse en la caché, reduciendo los fallos de capacidad.

### Reducir la Penalización de los Fallos de Caché
#### Dar Prioridad a las Lecturas sobre las Escrituras
    Pueden darse casos en que las lecturas quedan a la espera de escrituras con una penalización en
tiempo mayor. Esta estrategia se basa en detener las lecturas solo cuando existe un conflicto directo
con una escritura pendiente.
    En la estrategia de escritura directa (write-through) en la caché, suele usarse un buffer intermedio:
cuando se realiza una escritura en la caché, los datos modificados se almacenan inicialmente en un
buffer intermedio antes de ser escritos en la memoria principal. Mientras los datos modificados están
en el buffer, existe la posibilidad de que una lectura intente acceder a la misma ubicación de memoria
o a una ubicación superpuesta que está pendiente de ser escrita en la memoria principal. Esto puede
resultar en una penalización significativa en el rendimiento.
    Para evitar esta penalización, se priorizan las lecturas cuando no hay conflicto. Esto significa que,
si no hay un conflicto directo entre una lectura y una escritura pendiente en el buffer, se da prioridad
a la lectura. En lugar de esperar a que se vacíe el buffer, se realiza la lectura directamente desde la
memoria principal.
    Cuando se utiliza la estrategia de post-escritura (write-back):

      Buffer para bloque sucio: los bloques modificados (bloques sucios) se almacenan en un buffer
      intermedio antes de escribirse en la memoria principal. Esto permite agrupar y optimizar las
      operaciones de escritura para minimizar el acceso frecuente a la memoria principal. Los bloques
      sucios permanecen en el buffer hasta que sea necesario reemplazarlos por nuevos bloques o hasta
      que se realice una escritura posterior.

      Cuando ocurre un fallo de lectura y se necesita reemplazar un bloque en la caché, primero se
      debe leer el bloque solicitado desde la memoria principal. Esto asegura que los datos requeridos
      estén disponibles antes de realizar cualquier operación de escritura correspondiente. Después de
      leer el bloque de memoria principal, se realiza cualquier operación de escritura necesaria en caso
      de que el bloque modificado (bloque sucio) deba ser reemplazado.

    Las operaciones de escritura pueden ser más costosas que las operaciones de lectura en términos
de tiempo de acceso y recursos requeridos. De esta manera, las lecturas no deben esperar por las
escrituras.

#### Reemplazamiento de Subbloques
    Cuando se debe descartar un bloque de caché debido a un fallo, quizás no es necesario quitar toda
la información del mismo. Por esto, se divide el bloque en subbloques y se reemplazan solo los que
sean necesarios en lugar de reemplazar el bloque completo.

<!-- p. 204 -->

    La idea detrás del reemplazo de subbloques es aprovechar la localidad de los datos y minimizar
el almacenamiento de etiquetas (tags). La localidad se refiere a la propiedad de que los datos accedidos
recientemente y sus datos vecinos tienen más probabilidades de ser accedidos nuevamente en un futuro
cercano. Al dividir el bloque en subbloques más pequeños, se puede identificar y reemplazar solo los
subbloques que se consideran menos relevantes o que tienen menor probabilidad de ser accedidos
nuevamente en comparación con otros subbloques. Esto permite una mejor utilización de la caché y
reduce el costo de reemplazo de bloques completos.

### Envío Directo de la Palabra Solicitada al Procesador
    Hasta el momento, se ha supuesto que cuando se produce un fallo de lectura es necesario enviar
todo el bloque de información desde el nivel inferior de la jerarquía a la memoria caché. Esto hace que
la espera sea elevada, sobre todo para bloques de gran tamaño. Este problema se puede evitar con
el envío directo de la palabra solicitada al procesador. Actualmente, existen dos técnicas que
implementan esta política:

      Carga Anticipada (Early Restart): consiste en reanudar la ejecución del proceso tan pronto
      como llegue la palabra solicitada, sin esperar la llegada completa del bloque. Se ahorra tiempo,
      ya que la ejecución del proceso y la transferencia del resto del bloque continúan en paralelo.

      Primero la palabra solicitada (Critical Word First): organiza la memoria para que la
      palabra solicitada sea siempre la primera en llegar a la memoria caché. El resto del bloque se
      carga en caché en los siguientes ciclos.

    La eficiencia de esta técnica depende del tamaño del bloque; es especialmente útil con bloques
grandes (para bloques pequeños, la ganancia es muy pequeña).
    Sin embargo, esta técnica tiene un inconveniente relacionado con la localidad espacial: debido a
que solo se envía directamente la palabra solicitada y no el bloque completo, puede ocurrir que se
necesite acceder a la siguiente palabra del bloque en un momento cercano. En ese caso, habrá una
penalización adicional, ya que se requerirá acceder nuevamente a la memoria principal para obtener
esa siguiente palabra.

### Caché Sin Bloqueo (Non-blocking o Lockup-free)
    Aprovechando la propiedad de una CPU para ejecutar instrucciones fuera de orden (Tomasulo),
la estrategia consiste en no detener la ejecución ante un fallo de caché. En lugar de esto, se siguen
ejecutando otras instrucciones hasta que el dato se traiga de memoria. Para esto, se utilizan memorias
caché no bloqueantes. Diferentes diseños permiten soportar múltiples fallos simultáneos.

<!-- p. 205 -->

   Los beneficios de esta técnica dependen de la planificación de las instrucciones. La implementación
de una caché sin bloqueo requiere una interfaz de memoria más compleja, que puede incluir múltiples
bancos de memoria. Esto permite la recuperación simultánea de datos de diferentes bloques de caché
y una mayor eficiencia en la gestión de los fallos de caché.

#### Implementación
    Para una operación de carga sin bloqueo (por ejemplo, LD R1, dir), existe un registro específico
designado para almacenar temporalmente el dato solicitado durante la operación. El objetivo es realizar
un seguimiento de la petición y controlar adecuadamente la función de carga. Para lograr esto, se
necesita la siguiente información esencial para el control de la función:

      Dirección del bloque que produce el fallo.

      Entrada de la caché para el bloque.

      Ítem en el bloque que produce el fallo.

      Registro donde se almacena el dato: En el proceso de carga sin bloqueo, el dato solicitado
      se almacena en un registro designado, actuando como un destino temporal hasta que se complete
      la operación de carga y esté disponible para su uso por el procesador.

<!-- p. 206 -->

#### Caché Multinivel (L2, L3, ...)
    Una técnica para reducir la penalización por fallos de caché es la implementación de múltiples
niveles de caché, como la caché L1, L2, L3, y así sucesivamente. Cada nivel de caché se encuentra a
una distancia mayor del procesador, lo que implica tiempos de acceso ligeramente más largos que la
caché anterior, pero aún mucho más rápidos que acceder a la memoria principal. A medida que se
incrementa el nivel de caché, su tamaño también tiende a ser mayor que el nivel anterior.
    Cuando ocurre un fallo en el nivel L1 de caché, en lugar de buscar el dato directamente en la
memoria principal, se busca en el nivel L2 de caché, lo cual tiene una penalización de tiempo mucho
menor. Esto permite aprovechar la jerarquía de caché para reducir la penalidad por fallos y mejorar
el rendimiento del sistema.
    La eficiencia de los niveles de caché se puede calcular considerando los tiempos de acceso y las
tasas de fallos de cada nivel. La métrica utilizada es el Tiempo Medio de Acceso a Memoria (TAMA),
que es el tiempo esperado para acceder a un dato en caché. Se calcula considerando los tiempos de
acceso y las tasas de fallos de cada nivel de caché.

Definiciones:

      Tabla de fallos local (MissRateLi): Se refiere a los fallos en un nivel específico de caché
      divididos por el número total de accesos a ese nivel. Para L2, Miss RateL2 sería la cantidad de
      fallos que se dieron en L2 dividido la cantidad de accesos a L2.

      Tasa de fallos Global: Se refiere a los fallos en un nivel específico de caché divididos por el
      número total de accesos a memoria generados por el procesador. La tasa de fallos global es una
      métrica importante para evaluar el rendimiento y la eficiencia del sistema de caché.

      Tiempo de Acceso (HitTimeLi): Se refiere al tiempo necesario para acceder exitosamente a
      un dato en el respectivo nivel (i) de caché.

Obtener TAMA:

                           TAMA = HitTimeL1 + MissRateL1 × Miss PenaltyL1                            (12)

                     Miss PenaltyL1 = HitTimeL2 + MissRateL2 × Miss PenaltyL2                        (13)
      TAMA = HitTimeL1 + Miss RateL1 × (HitTimeL2 + MissRateL2 × Miss PenaltyL2)                     (14)

<!-- p. 207 -->

   Conclusiones: La caché L1 tiene un impacto di-
   recto en el procesador, ya que proporciona acceso
   rápido a los datos dentro del ciclo del procesador.
   La caché L2 influye en la penalización por fallos de
   la caché L1. Si la caché L1 experimenta un fallo y
   se debe buscar el dato en la caché L2, la presencia
   de la caché L2 permite reducir el tiempo medio de
   acceso en comparación con tener que acceder direc-
   tamente a la memoria principal.

#### Reducir el Tiempo de Acceso a la Caché (Aciertos)
Caches Simples y Pequeñas Una caché pequeña se puede integrar junto al procesador, lo que
evita la penalización en tiempo que se produce al tener que acceder a la memoria externa.
    Una caché simple se caracteriza por tener un grado de asociatividad pequeño, lo que significa
que cada bloque de memoria tiene una única ubicación posible en la caché. Esto permite acelerar la
comparación de las etiquetas de los bloques y, por lo tanto, reducir el tiempo necesario para encontrar
un acierto en la caché.
    Al tener una caché pequeña y simple, es más factible su incorporación en el chip de la CPU,
eliminando la necesidad de conexiones externas y reduciendo aún más el tiempo de acceso. Cuanto
más pequeño y simple sea el hardware de la caché, más rápido será su rendimiento.

#### Caché de Direcciones Virtuales
    El tiempo de acierto de la memoria caché es uno de los parámetros que más influyen en el ren-
dimiento de un sistema computador, ya que determina el tiempo de ciclo. Esta técnica tiene como
objetivo evitar la espera en la Translation Lookaside Buffer (TLB), responsable de traducir las direc-
ciones virtuales a direcciones físicas de memoria, lo cual reduce el tiempo de acierto.

Recordatorio:

<!-- p. 208 -->

      Una dirección virtual es un valor utilizado internamente por el procesador y el sistema opera-
      tivo para direccionar los datos. En lugar de trabajar con direcciones físicas, los procesos utilizan
      el mecanismo de memoria virtual, lo que permite:

          • Que el tamaño de la memoria utilizada por un proceso pueda ser mayor que la memoria
            física disponible, trayendo datos a la memoria principal o a la caché solo cuando se los
            necesita.
          • Que se garantice que los procesos no interfieran con otros procesos en el sistema.

      Una dirección física es la ubicación real de los datos en la memoria física del sistema. Las
      direcciones virtuales son traducidas por el hardware y el sistema operativo a direcciones físicas
      en el momento de acceder a la memoria.

   Utilizando una caché de direcciones virtuales, se accede a la caché mediante la dirección virtual en
lugar de la dirección física, permitiendo un acceso más rápido y evitando la necesidad de realizar una
traducción en la TLB. Sin embargo, esto plantea algunos desafíos:

      Cambio de contexto: Es necesario borrar la caché cuando ocurre un cambio de contexto, ya
      que los datos almacenados están asociados a direcciones virtuales específicas y podrían no ser
      válidos para el nuevo proceso. Si no se realiza el borrado, podrían producirse falsos aciertos y la
      caché podría devolver datos incorrectos.

      Problema de sinónimos: Dos direcciones virtuales diferentes pueden apuntar a la misma direc-
      ción física de memoria, lo que genera conflictos y problemas al buscar los datos correspondientes.

    Una solución para estos problemas es asignar a cada bloque de caché un identificador de proceso,
que se compara con el del proceso que solicita los datos, garantizando que los datos en caché sean
válidos y pertenezcan al proceso correcto.

Modos de uso de la memoria virtual en caché:

      Direccionamiento virtual parcial: También llamado solapamiento.

      Direccionamiento virtual total: Prácticamente no se utiliza.

#### Direccionamiento Virtual Parcial (Solapamiento)
   Cuando se utiliza una caché física, se emplean direcciones físicas ya traducidas por el mecanismo
de memoria virtual. Este proceso de traducción puede ser más rápido si se realiza simultáneamente
con la búsqueda del bloque en la caché.
   La dirección virtual se divide en dos partes:

      Página virtual: Debe pasar por el mecanismo de traducción y actúa como la etiqueta que
      verifica si el marco de memoria virtual contiene el dato del bloque solicitado.

      Desplazamiento: Se utiliza directamente en la dirección física y en la dirección de caché. Se
      compone del índice de caché (para seleccionar el marco dentro de la caché) y la palabra (que
      referencia un elemento dentro del marco).

    Si se establecen restricciones en el tamaño del desplazamiento y el número de página, se puede
realizar el acceso en paralelo:

      Mientras se traduce la dirección de la página mediante la tabla de páginas.

<!-- p. 209 -->

      Se utiliza el desplazamiento de la dirección virtual para seleccionar el conjunto y la palabra de
      la dirección de caché.

    El desplazamiento de la dirección virtual, que no se modifica durante la traducción, se puede
descomponer en el campo conjunto (cache index) y palabra. Con estos datos se puede acceder al dato
correspondiente en la caché y luego, cuando se conoce la dirección real (es decir, se comprueba la
etiqueta), se decide qué hacer:

      Si en la traducción se produce un acierto, se acepta el dato seleccionado en la caché.

      En caso de fallo, se descarta el dato seleccionado y se lee el dato auténtico.

La principal limitación de esta alternativa es que la caché no puede ser mayor que el tamaño de la
página virtual. Un modo de aumentar el tamaño máximo de la caché es aumentar la asociatividad.

#### Direccionamiento Virtual Total
    Este direccionamiento prácticamente no se utiliza. En él se suprime el paso de traducción, ya que
se utilizan las páginas proporcionadas por la dirección virtual como ”tag” de la dirección de caché.
Lógicamente, en estos casos los tamaños de la dirección virtual y la caché deben coincidir.
    El problema es que, dado que pueden existir procesos diferentes con la misma dirección virtual,
podría ocurrir que la misma dirección virtual tenga diferentes direcciones físicas. La solución sería
vaciar la caché cada vez que se produce un cambio de contexto. Sin embargo, esto implica una pérdida
de tiempo y una degradación en el rendimiento. Otra solución es aumentar el tamaño del ”tag” de la
dirección de caché añadiéndole un identificador de proceso (PID). Si el sistema operativo asigna este
”tag” al proceso, no se necesitaría vaciar la caché cada vez que se carga otro proceso.
    En esta alternativa surge lo que se conoce como el ”problema de sinónimos o alias”. Este problema
aparece cuando varios procesos comparten información, ya que puede existir el mismo dato en dife-
rentes bloques de caché, cada uno de ellos asociado a un proceso diferente. Esto causa un problema
de coherencia en la caché, ya que cuando un proceso actualiza un dato, el resto de los procesos no se
percata de ello. La solución es evitar que existan varias copias del mismo dato mediante la detección
de sinónimos en el momento en que se produzca.

<!-- p. 210 -->

    Cuando la dirección virtual se traduce a dirección física a través del TLB, es fácil evitar que
existan sinónimos simplemente asignando la misma dirección física a diferentes direcciones virtuales.
Sin embargo, esto no es posible si la caché utiliza directamente la dirección virtual. La única solución
es realizar la traducción física en paralelo al acceso a la caché.

#### Segmentación de Escrituras
    La escritura habitualmente toma más tiempo que la lectura, ya que no se puede realizar en paralelo
la comprobación de la etiqueta y la escritura del dato, pues existe el riesgo de acceder al dato incorrecto.
Una técnica que puede evitar este problema es la segmentación de la escritura.
    Como primera medida, se separan los datos y las etiquetas para que puedan ser accedidos de
manera independiente.
    Normalmente, en una escritura en caché, se compara la etiqueta del marco indicado por el cache
index con la etiqueta de la dirección de escritura. Cuando se utiliza la segmentación de escrituras,
se escribe el dato durante la comparación, pero en lugar de escribir directamente sobre la caché, se
utiliza un buffer de escritura retrasada (Delayed Write Buffer).
    La escritura se segmenta en dos etapas:

      En la primera, mientras se comprueba la etiqueta, se guarda el dato y la dirección de la caché
      sobre la cual se escribirá en el buffer de escritura retrasada.

      En la siguiente fase, si la escritura ha sido un acierto, se escribe en la caché (utilizando la
      dirección y el dato de la escritura anterior, provenientes del buffer de escritura retrasada).

### La Memoria Principal
   La memoria principal es el siguiente nivel en la jerarquía de memoria después de la memoria
caché. Su función es satisfacer los pedidos de datos de la memoria caché y servir como interfaz de
entrada/salida. Las medidas de rendimiento de la memoria principal son:

      Latencia: Es el tiempo que demora la memoria en realizar una operación. Afecta a la penaliza-
      ción por fallos de la caché. Este tiempo está compuesto por:

          • Tiempo de acceso: tiempo entre la petición y la llegada del dato.
          • Tiempo de ciclo: tiempo entre peticiones sucesivas.

<!-- p. 211 -->

      Ancho de banda: Es la cantidad máxima de datos que se pueden transferir desde y hacia la
      memoria en un período de tiempo determinado. Representa la capacidad de la memoria para
      manejar el flujo de datos entre el procesador y la memoria. Es un requerimiento para sistemas
      multiprocesadores y para la entrada/salida. El uso de memorias caché de segundo nivel hace que
      el ancho de banda sea también un requisito para las memorias caché (el ancho de banda de la
      memoria principal afecta a la penalización de fallo de bloques grandes L2). De hecho, el tamaño
      de bloque para una caché se determina según el ancho de banda de la memoria principal.

   Existen dos tecnologías para la fabricación de memoria:

#### Tecnología DRAM (Dynamic Random Access Memory)
    En este tipo de memorias, para posibilitar el aumento en la capacidad, se utiliza un único transistor
para almacenar un bit de información. Al ser solo un transistor, una lectura del bit destruye la
información; por lo tanto, debe ser escrita nuevamente. A esta operación se la conoce como refresco y
debe realizarse frecuentemente (la DRAM necesita ser refrescada periódicamente). El refresco es una
de las razones por las cuales el tiempo de ciclo de una DRAM es mucho más largo que su tiempo de
acceso.
    Debido a la gran capacidad de estas memorias, resulta muy costoso producir un empaquetado con
todos los puertos necesarios para direccionarlas. Para solucionar esto, se realiza un multiplexado de
las líneas de dirección. La memoria se organiza como una matriz de direcciones y la dirección se divide
en dos partes:

      Una mitad para especificar el acceso a una columna (CAS - Column Access Strobe)

      La otra mitad para indicar la fila (RAS - Row Access Strobe)

   Ejemplo: Esquema de organización de una DRAM de 64 Mb:

<!-- p. 212 -->

#### Tecnología SRAM (Static Random Access Memory)
    En las SRAM, el refresco no es necesario (ya que cuentan con entre 4 y 6 transistores por bit), por
esta razón, el tiempo de acceso es muy cercano al tiempo de ciclo.
    Las memorias SRAM son utilizadas por su velocidad, mientras que en las DRAM, el objetivo es
reducir el costo por bit. Las memorias DRAM suelen ser de 4 a 8 veces más grandes que las SRAM.
A su vez, las SRAM son hasta 16 veces más rápidas que las DRAM, pero su costo es de 8 a 16 veces
mayor.

#### Incremento del Ancho de Banda
    Aunque tanto la latencia como el ancho de banda son medidas de rendimiento importantes para
la memoria principal, es mucho más simple y económico incrementar el ancho de banda.
    Una técnica para aumentar el ancho de banda consiste en recuperar más de una palabra en cada
ciclo, manteniendo la misma latencia. La desventaja de este sistema es que incrementa el costo del
bus.
    Ejemplo: Suponiendo una memoria DRAM con una palabra de 32 bits (4 Bytes) que demora:

      1 ciclo en enviar la dirección

      10 ciclos en el acceso

      1 ciclo en enviar el dato

   La mejora en rendimiento al recuperar bloques de cuatro palabras en lugar de una resulta:

   En lugar de aumentar el ancho de la caché o del bus, se puede emplear la técnica de memoria
entrelazada.

#### Memoria Entrelazada
    Los chips de memoria se pueden organizar en bancos para leer o escribir múltiples palabras a la
vez en lugar de una sola palabra. Estos bancos tienen el ancho de una palabra, de modo que el ancho

<!-- p. 213 -->

del bus y de la caché no necesitan modificarse. Sin embargo, al enviar direcciones a varios bancos
simultáneamente, es posible leer todos los bancos al mismo tiempo, incrementando el rendimiento sin
modificar la infraestructura del bus.

    En este ejemplo, en el que se accede a 4 palabras a la vez en lugar de a una, el banco 0 (MO) tiene
todas las palabras cuya dirección módulo 4 es 0, el banco 1 tiene todas las palabras cuya dirección
módulo 4 es 1 y así sucesivamente. Esta correspondencia se denomina factor de enlazado y estos bancos
de memoria están enlazados a nivel de palabra. Esto optimiza los accesos secuenciales a memoria.
    La motivación original de los bancos de memoria fue entrelazar accesos secuenciales. Una razón
adicional es permitir múltiples accesos independientes, como las memorias caché que no se bloquean
cuando se están accediendo. Para esto, cada banco necesita una interfaz con el sistema (cada uno tiene
su controlador, bus de direcciones, bus de datos, etc).
    A su vez, existe:

      Entrelazamiento de nivel bajo: Se refiere a la organización de los bancos a nivel de palabra,
      permitiendo la transferencia simultánea de varias palabras a través de diferentes bancos.

      Entrelazamiento de nivel alto: Implica la organización de los bancos en unidades mayores
      que las palabras, como bloques de memoria, para acceder simultáneamente a datos de mayor
      tamaño.

      Entrelazamiento mixto: Combinación de entrelazamiento de nivel bajo y alto, lo que permite
      optimizar el acceso tanto a nivel de palabra como a nivel de bloque de memoria.

<!-- p. 214 -->

                                                                                    Figura 131: Resumen conceptual de la Unidad N°6: Coherencia, Consistencia y Sincronización
