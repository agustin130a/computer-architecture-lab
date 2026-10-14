<!-- p. 215 -->

## Unidad 6: Multiprocesadores - Coherencia, Consistencia y Sincronización
### Multiprocesadores
    Se denomina multiprocesador a un computador que cuenta con dos o más microprocesadores
(CPUs). Gracias a esto, el multiprocesador puede ejecutar simultáneamente varios hilos pertenecientes
a un mismo proceso o bien a procesos diferentes.
    Los ordenadores multiprocesador presentan problemas de diseño que no se encuentran en ordena-
dores monoprocesador. Estos problemas derivan del hecho de que dos programas pueden ejecutarse
simultáneamente y, potencialmente, pueden interferirse entre sí (en lo que se refiere a las lecturas y
escrituras en memoria).

### Jerarquía de Memoria Extendida
     Existen tres tipos de arquitecturas que resuelven estos problemas:

       Arquitectura NUMA (Nonuniform Memory Access): En esta arquitectura, cada proce-
       sador tiene acceso y control exclusivo a una parte de la memoria. Cada CPU tiene una caché
       y una RAM privadas. Existe una red de interconexión para las CPUs, lo que implica que la
       latencia de acceso a memoria puede variar dependiendo de la ubicación del bloque de memoria.
       Para un CPU, acceder a su propia caché será más rápido que acceder a las cachés de otros CPUs,
       ya que esto requiere pasar por la red.

       Arquitectura SMP (Symmetric Multiprocessors) o UMA (Uniform Memory Ac-
       cess): En esta arquitectura, todos los procesadores comparten toda la memoria. Cada CPU
       tiene su propia caché privada y están interconectadas mediante una red de interconexión. En
       este caso, cada CPU tiene acceso igualitario a la memoria compartida, y el tiempo de acceso es
       el mismo independientemente de la ubicación de la memoria.

       Sistemas de caché compartida: Una primera implementación consiste en una caché com-
       partida. Este caso no existe en la vida real y es a modo ilustrativo. Se cuenta con una caché
       L1 compartida por n CPUs, los cuales están conectados mediante un switch de n entradas que
       permite conmutar entre la CPU solicitante, la caché y la memoria principal.

       Caché de bus compartido: En este caso, cada CPU tiene su propia caché privada y están
       interconectadas mediante un bus de E/S que también las conecta a la memoria principal.

<!-- p. 216 -->

    La arquitectura SMP O UMA, debe lidiar con el problema de la coherencia de caché. Cada mi-
croprocesador cuenta con su propia memoria cache local. De manera que cuando un microprocesador
escribe en una dirección de memoria, lo hace únicamente sobre su copia local en caché. Si otro micro-
procesador tiene almacenada la misma dirección de memoria en su caché, resultará que trabaja con
una copia obsoleta del dato almacenado.

### Datos Privados y Compartidos en Arquitecturas de Memoria Compartida
    En una arquitectura con memoria compartida, existen dos tipos de datos: datos privados y datos
compartidos. Los datos privados son utilizados exclusivamente por un único procesador, mientras
que los datos compartidos son utilizados por varios procesadores, generalmente para propósitos de
sincronización.
    Los sistemas de computación poseen una jerarquía de memoria que incluye memorias caché rápidas.
Estas cachés son útiles para reducir el ancho de banda de la memoria y para ocultar la latencia de los
accesos a la memoria principal, ya que cada CPU tiene su propia caché privada.
    Cuando los datos privados son copiados en las memorias caché, se obtienen todos los beneficios
mencionados, y dado que ningún otro procesador necesita acceder a estos datos, el comportamiento
es idéntico al de un sistema uniprocesador.
    En el caso de los datos compartidos, al copiarlos en las cachés de los procesadores que los utilizan, se
logra ocultar la latencia de acceso a la memoria, permitiendo que los procesadores accedan rápidamente
a estos datos desde la caché en lugar de esperar que se lean de la memoria principal. Esto mejora el
rendimiento general del sistema y reduce la necesidad de ancho de banda de memoria. Además, copiar
los datos compartidos en las cachés de los procesadores que los necesitan reduce la competición entre

<!-- p. 217 -->

procesadores cuando intentan acceder simultáneamente a la memoria para leer un dato compartido,
mejorando así la eficiencia del sistema.
   A pesar de estas ventajas, copiar a la caché datos compartidos genera el problema de coherencia
de caché.

### El Problema de la Coherencia de Caché
   Informalmente, se dice que un sistema de memoria es coherente si al leer cualquier dato, se
devuelve el valor más actualizado del mismo (el último valor escrito para ese dato). Esta definición de
#### Coherencia

       Coherencia: Define qué valor debe ser retornado en una lectura.

       Consistencia: Define cuándo un valor que fue escrito por un procesador puede ser leído por el
       mismo u otros procesadores.

6.4.1.    Coherencia
    Un sistema de memoria es coherente si, para el resultado de cualquier ejecución del programa
sobre una posición de memoria U, es posible construir una ordenación secuencial consistente con los
resultados de la ejecución. Esto significa que el valor devuelto por una operación de load solicitada
por cualquier procesador es igual al valor almacenado por el último store realizado sobre esa posición,
independientemente del procesador que realizó esta operación.
    En esta definición se observan dos componentes esenciales:

       Propagación: Las escrituras realizadas deben ser visibles para todos los procesadores.

       Serialización de escrituras: Todas las escrituras realizadas sobre una posición de memoria
       deben observarse en el mismo orden por todos los procesadores.

   El modelo de consistencia de memoria implica conocer exactamente cuando un valor que fue escrito
por un procesador puede ser leído por los demás procesadores.

### Modelo Intuitivo de Memoria
#### Programa Secuencial
    En un programa secuencial, las posiciones de memoria se utilizan para comunicar valores entre
diferentes puntos del programa. Cuando se lee una posición, se espera recibir el último valor escrito
en ella. Esto parece no presentar problemas, ya que no existen múltiples procesadores accediendo a la
memoria simultáneamente. Sin embargo, en uniprocesadores pueden surgir problemas de coherencia
cuando otro dispositivo (que no sea el procesador) intenta leer o escribir en la memoria usando el
DMA:

       Si un dispositivo DMA escribe en memoria, el procesador puede seguir viendo valores antiguos
       en la caché, ya que aún no refleja los datos nuevos escritos por el DMA.

       Si un dispositivo DMA lee la memoria, puede leer un valor antiguo si se utiliza write-back, ya
       que el dispositivo aún no ve los valores nuevos escritos por el procesador.

<!-- p. 218 -->

#### Espacio de Direcciones Compartido en Sistemas con un Único Procesador (Multiprogramación)
    Cuando se lee una posición, se obtiene el último valor escrito en ella, independientemente del
proceso (o hilo) que realizó la última escritura sobre dicha posición. Las cachés no interfieren en el uso
de múltiples procesos (o hilos) en un procesador, ya que todos ellos acceden a la memoria a través de
la misma jerarquía de memoria.

#### Multiprocesadores de Memoria Compartida
    Objetivo: Es deseable que el resultado de ejecutar un programa con varios hilos sea el mismo,
independientemente de si estos hilos se ejecutan en paralelo (en un multiprocesador) o de forma
entrelazada (en un uniprocesador multiprogramado).
    Problema: Cuando dos o más procesos acceden a la memoria a través de cachés diferentes, existe
el riesgo de que obtengan valores inconsistentes.

### Soluciones de Grano Grueso
   Dado que las operaciones de E/S son mucho menos frecuentes que los accesos a memoria, se pueden
considerar las siguientes soluciones:

       Evitar utilizar la caché: Los segmentos de memoria involucrados en las operaciones de E/S
       se marcan como No-Cacheables o bien se utilizan operaciones de load/store no-cacheables.

       Sacar las páginas de la caché antes de la E/S: Las páginas de memoria involucradas
       en cualquier operación de E/S son eliminadas de la caché (flush) previamente por el sistema
       operativo. Para esto se debería tener una instrucción o macro para actualizar la memoria.

       Usar la caché para E/S: El tráfico de E/S pasa por todos los niveles de la jerarquía de
       memoria. Este método tiene la desventaja de que el contenido de la caché puede corromperse
       con datos que no son de interés inmediato para el procesador, además de que la caché puede
       ralentizarse debido a que el dispositivo de E/S accede constantemente a la caché sin necesidad
       de requerir los datos actualizados.

    En multiprocesadores, la lectura o escritura de variables compartidas es un evento frecuente, por
lo que no es práctico deshabilitar la caché para datos compartidos ni invocar al sistema operativo
cada vez que se referencia a una variable compartida (por lo que ninguna de las tres alternativas
anteriores es viable). Los microprocesadores actuales incluyen mecanismos integrados para soportar
la coherencia.

### Políticas o Protocolos para Mantener la Coherencia
#### Invalidación en Escritura / Coherencia Dinámica
    Cuando se escribe en un bloque, se invalidan todas las demás copias (esquema de múltiples lectores,
un solo escritor). Las escrituras consecutivas en el mismo bloque (no necesariamente en la misma
palabra) efectuadas desde el mismo procesador se realizan localmente, sin necesidad de replicar la
escritura. Solo se requiere una transacción en caso de múltiples escrituras al mismo dato.

       En un fallo de lectura:

         • Con write-through, la memoria siempre está actualizada.

<!-- p. 219 -->

         • Con write-back, se produce una búsqueda (snoop) en las cachés remotas para encontrar el
           valor más reciente. La caché que contiene este valor lo proporciona al solicitante y a la
           memoria principal.

#### Actualización en Escritura
    Cuando se escribe en un bloque, todas las copias se actualizan (esto es típico cuando se utiliza write-
through y hay pocos procesadores). Si hay escrituras consecutivas en la misma palabra, se requieren
múltiples actualizaciones (write merge).
      En caso de fallo de lectura, simplemente se busca el dato solicitado en la memoria principal, que
      siempre está actualizada.

#### Protocolos según la Red de Interconexión
   Las memorias caché coherentes ofrecen las siguientes ventajas para los datos compartidos:
      Migración: Un dato puede ser movido a una caché local y utilizado allí de manera transparente,
      lo cual reduce la latencia de acceso al dato y disminuye el ancho de banda requerido para la
      memoria compartida.

      Replicación: Un dato puede ser leído simultáneamente por varios procesadores al mantener
      una copia en la caché local de cada uno. La replicación disminuye la latencia de acceso y reduce
      la competencia entre procesadores por leer un dato compartido.
    Para mantener la coherencia en un sistema con cachés, existen protocolos que realizan un segui-
miento del uso de los datos compartidos, evitando incoherencias. Los protocolos para invalidación o
actualización dependen de la red de interconexión. Si la red permite un broadcast eficiente, las opera-
ciones de invalidación o actualización pueden enviarse simultáneamente a todos los controladores.

#### Protocolo Snoopy (buses): Observación del Bus
   Cada controlador de caché está observando los eventos que ocurren en el bus y toma decisiones en
consecuencia. Un controlador de caché envía eventos al bus en función de las repeticiones de acceso a
memoria que recibe el procesador. De esta manera, se envían órdenes de invalidación o actualización
simultáneamente a todos los demás controladores.
      Cada caché que tiene una copia de un bloque de memoria también tiene una copia del estado de
      uso compartido del bloque. No existe un estado centralizado.

      Todas las cachés son accesibles mediante algún medio de broadcast, como un bus, y todos los
      controladores de caché monitorean o espían (snoop) el medio para determinar si tienen o no una
      copia del valor que se está pidiendo en el bus.

      Si la red de conexión no permite broadcast o no es eficiente, la invalidación o la actualización se
      envía únicamente a aquellas cachés que tienen una copia del bloque.

#### Protocolos Basados en Directorios
    Se utiliza un directorio (centralizado o distribuido) con una entrada por cada bloque, en la que se
indica en qué cachés existe copia y en qué estado se encuentra esta.
      Existe una ubicación centralizada, llamada directorio, que almacena el estado de uso compartido
      de todos los bloques.

<!-- p. 220 -->

       La implementación de este tipo de protocolo es más compleja que en los protocolos snoopy, pero
       permite una mayor escalabilidad hacia grandes cantidades de procesadores.

### Políticas de Asignación
#### Write Allocate (write on miss)
    Cuando un procesador realiza una escritura a una dirección de memoria determinada, se verifica
si la dirección se encuentra en la caché. Si está presente en la caché (hit), la escritura se realiza
directamente en la caché. Si no se encuentra (write miss), en lugar de descartar la escritura o escribir
directamente en la memoria principal, la caché trae el bloque completo de memoria que contiene la
dirección de escritura solicitada desde la memoria principal a la caché. Luego, la escritura se realiza
en la caché y el bloque se marca como modificado. La política de actualización write back utiliza write
allocate con la esperanza de que las siguientes operaciones de escritura (o incluso de lectura) sean
sobre ese bloque de memoria que ahora se encuentra en caché.

#### No Write Allocate (Write Around o Sin asignación de Escritura)
    Cuando se produce un fallo de caché en una operación de escritura, en lugar de traer el bloque com-
pleto de memoria a la caché y luego realizar la escritura, la escritura se omite y se realiza directamente
en la memoria principal.

       En el caso de write through, se utiliza no write allocate porque el que las siguientes escrituras
       sean sobre un bloque recientemente traído a caché no provee ninguna ventaja, ya que de todas
       formas esas escrituras deben hacerse también sobre memoria principal.

### Protocolos Snoopy
    Para el uso de estos protocolos, no se debe realizar ninguna modificación en el hardware de la
memoria ni de las cachés; solo se debe ampliar la funcionalidad del controlador de memoria caché. En
este tipo de protocolos, cada bloque de memoria tiene asociado un estado. Los cambios de estado se
realizan cuando en el bus se observa una transacción relevante (o ante operaciones load o store).
    El Arbitraje del Bus Impone un Orden: Las transacciones del bus son visibles en el mismo
orden por todos los controladores de caché. La comprobación de bus se realiza con las mismas etiquetas
con las que se ejecutan las peticiones del procesador. Dentro de los protocolos snoopy, existen dos tipos
de políticas:

       Invalidación en Escritura: Al escribir en un bloque, todas las demás copias son invalidadas,
       permitiendo múltiples lectores pero un único escritor. La reacción frente a fallos de lectura
       depende de la política de actualización:

         • Write-through: La memoria está siempre actualizada. Así, ante un fallo de lectura, se busca
           directamente en la memoria.
         • Write-back: La memoria se actualiza solo cuando el bloque debe ser removido de la caché;
           por ello, al producirse un fallo de lectura, se debe buscar en las cachés para encontrar el
           valor correcto.

       Actualización en Escritura: Al escribir en un bloque, todas las copias se actualizan. Se
       utiliza escritura directa (write-through). Si ocurre un fallo de lectura, se busca en la memoria,
       que siempre está actualizada.

<!-- p. 221 -->

#### Protocolo Snoopy de dos Estados
    Este protocolo se aplica a un único nivel de caché (para escritura directa, non-allocate). Aunque
solo los bloques residentes en memoria caché tienen un bit de validez, se considera que el estado de
los bloques no residentes en caché es inválido.

   Diagrama de Estados del Protocolo:

          Estados posibles: Válido (V) - Inválido (I).

          El estado inicial de todos los bloques es Invá-
          lido.

   Convenio de representación: Cada transición
   es disparada por la observación de un evento en el
   procesador o el bus.

          Eventos del Procesador:

            • PrRd (Lectura)
            • PrWr (Escritura)

          Eventos del Bus:

            • BUS_Rd (Lectura)
            • BUS_Wr (Escritura)

   Transiciones del Diagrama de Estados:

      T3: Partiendo del estado Inválido, si un procesador realiza una escritura (PrWr), se escribe el
      dato en memoria sin actualizar la caché (el estado sigue siendo Inválido). Se envía un mensaje
      al bus indicando la escritura (BUS_Wr).

      T2: Si se realiza una lectura (PrRd) desde un estado Inválido (fallo de lectura), se busca el dato
      en memoria y se actualiza la caché, cambiando al estado Válido. Se envía un mensaje al bus
      indicando la lectura (BUS_Rd).

      T1a: Si se realiza una lectura (PrRd) y el estado es Válido, es un acierto (no se accede a memoria
      ni se cambia el estado). No se envía ningún mensaje al bus.

      T1b: Si se realiza una escritura (PrWr) en un estado Válido, se actualizan tanto la memoria prin-
      cipal como la caché, manteniendo el estado como Válido. Se envía un mensaje al bus indicando
      la escritura sobre la caché (BUS_Wr).

    T4: Supongamos que en un procesador A ocurrió la transición T1b y que en otro procesador B,
el estado respecto de un dato era ”Válido” cuando esto sucedió. El procesador B observa en el bus el
mensaje BUS_Wr, lo cual indica que la caché del procesador B ya no tiene la última actualización del
dato en cuestión, por lo que el estado pasa a ser ”Inválido”. No se envía ningún mensaje al bus (–).
    El protocolo Snoopy provee coherencia a la caché porque:

      Garantiza la propagación de escrituras: Todos los controladores espían el bus, asegurando
      así que todas las actualizaciones de escritura se propagan.

<!-- p. 222 -->

      Garantiza la serialización de escrituras: Dado que el bus es atómico (una transacción a la
      vez) y que el arbitraje de bus define el orden de las escrituras a todas las posiciones de memoria,
      las escrituras en memoria suceden de una en una y en orden.
    Con estas características, las operaciones se realizan en orden y el valor devuelto por la última
lectura es el último valor escrito.

   Las transacciones del bus asociadas con escrituras segmentan los flujos individuales de cada pro-
grama. Entre dos transacciones de escritura, el orden de las lecturas en los distintos procesadores
no está restringido. Entre escrituras, cada programa realiza sus lecturas de acuerdo con el orden del
programa.

    El mayor defecto de este protocolo es que utiliza escritura directa (write-through). Este tipo de
política requiere un alto ancho de banda con la memoria. Por ejemplo, supongamos un procesador de

<!-- p. 223 -->

2000 MHz, con CP I = 1, y un 15 % de ”operaciones store” de 8 bytes cada uno. Esto implica que se
realizarían 300 millones de ”operaciones store” por segundo por procesador, lo cual significa un ancho
de banda de 2400 MB/s por cada procesador. Con lo cual un bus de memoria de 10 GB/s solo podría
soportar 4 procesadores sin saturarse.
    La solución al problema del ancho de banda en los protocolos Snoopy es utilizar una política
de post-escritura (write-back). Sin embargo, esto generaría una complicación para la propagación y
serialización. Para lidiar con estas situaciones, se debe adoptar un esquema de tres estados. Para una
caché con write-back (y, por lo tanto, write-allocate), los estados serían: Inválido, Válido o Compartido,
y Modificado.

### Protocolo MSI: Invalidación de tres Estados
    El protocolo MSI también es un protocolo de invalidación en la escritura, que cuenta con tres
estados:

      I (Inválido o no presente)

      S (Válido o Compartido): El bloque está presente en la caché y no ha sido modificado. La
      memoria está actualizada. Otras cachés adicionales pueden tener copia.

      M (Modificado o Dirty): Sólo hay una caché con copia válida (la copia de la memoria prin-
      cipal está desactualizada). La exclusividad implica que la caché puede modificar el bloque sin
      notificárselo a otros.

   En cuanto a los eventos que generan transiciones entre estados, se tienen los siguientes:

      Peticiones del procesador:

        • PrRd: Petición de lectura.
        • PrWr: Petición de escritura.

      Transacciones del Bus:

        • BusRd (Lecturas por parte de otros procesadores): El controlador de la caché pone
          la dirección en el bus y pide una copia que no piensa modificar. El sistema de memoria
          (posiblemente otra caché) proporciona el dato. Esta transacción se genera por un PrRd
          que falla en la caché, y el procesador espera como resultado de esta transacción el dato
          solicitado.
        • BusWB (equivalente a Flush) - Post-escrituras: El controlador de la caché pone la
          dirección y el contenido para el bloque de memoria en el bus. La memoria principal se
          actualiza con el último contenido. Esta transacción la genera el controlador de la caché en
          una post-escritura.
        • Replace: Se va a quitar el bloque de caché para traer otro de la memoria principal.
        • BusRdx (Lectura con Exclusividad): Trae el dato desde la memoria a la caché con
          intención de modificarlo, y el resto de las cachés invalidan su copia. La genera el controlador
          cuando recibe PrWr y el estado era ”Inválido” o ”Compartido”. El controlador de la caché
          pone la dirección en el bus y pide una copia exclusiva que planea modificar. El sistema de
          memoria (o posiblemente otra caché) proporciona el dato. Todas las demás cachés necesitan
          ser invalidadas. Esta transacción se genera por un PrWr a un bloque que no está en la caché
          o está en estado ”Compartido”. Una vez la caché obtiene la copia exclusiva, la escritura se
          realiza en la caché.

<!-- p. 224 -->

      Nueva respuesta del controlador de caché:
          • Flush: Volcar el bloque de caché al bus.
    Otro concepto necesario para soportar los protocolos de post-escritura es que junto con el cambio
de estado de cada bloque en la caché, el controlador de la caché puede intervenir en las transacciones
del bus y poner el contenido del bloque referenciado en el bus, en vez de permitir que la memoria pro-
porcione el dato. El controlador de la caché también puede iniciar nuevas transacciones, proporcionar
datos para las post-escrituras o recoger datos proporcionados por el sistema de memoria.

#### Diagrama de Transición de Estados de una Caché con Post-Escritura

   T1: Si el estado es I (Inválido) (inicial-
   mente lo es para todos los bloques de ca-
   ché), y el procesador realiza una escritura
   (PrWr), se produce un fallo de escritura
   (debido a que el dato no está en caché).
   Se trae el dato de memoria a caché y se lo
   modifica, siendo este procesador el único
   que posee la versión actualizada del da-
   to (el estado pasa a ser M o Dirty). Se
   envía un mensaje al bus indicando que
   se realizó una lectura con exclusividad
   (BusRdX), de manera que para todas
   las demás cachés, al observar este men-
   saje en el bus (BusRdX), se invalidará
   el dato (si lo tienen).

      T2: Partiendo del estado I (Inválido), si un procesador realiza una lectura, se producirá un fallo
      de lectura ya que el dato no se encontraba en caché. Se traerá el dato desde la memoria principal
      y el estado pasará a S (Válido). Se envía un mensaje al bus indicando que se realizó una lectura.
      T3: Partiendo del estado S (Válido) (se cuenta con el dato actualizado en caché), si un procesador
      realiza una escritura (PrWr), el estado pasará a ser M (Modified), y se enviará un mensaje por
      el bus indicando que el dato ha sido leído con la intención de modificarlo (BusRdX). Para
      todas las demás cachés, al observar este mensaje en el bus (BusRdX), se invalidará el dato (si
      lo tienen).
      T4: Partiendo del estado M (Dirty) (el procesador en cuestión es el único que tiene el dato
      actualizado, pues fue este quien lo modificó por última vez), si se lee (PrRd) o escribe (PrWr)
      el dato por parte de este mismo procesador, el estado seguirá siendo M y no hay necesidad de
      enviar mensajes por el bus.
      T5: Partiendo del estado M (Dirty), si el bloque de caché debe reemplazarse por otro (Replace),
      el estado pasará a ser inválido y se envía el mensaje Flush (se vuelca el dato en el bus para
      actualizarlo en memoria principal). Lo mismo sucede si, estando en el estado M, se recibe la señal
      BusRdX; esto indica que otro procesador necesita leer el dato con la intención de modificarlo.
      T6: Partiendo del estado M (Dirty), si se observa una señal BusRd en el bus (otra caché necesita
      el dato que este procesador ha modificado), se envía un mensaje Flush al bus (se vuelca el dato
      en el bus para actualizarlo en memoria principal) y el estado pasa a ser S (Válido).

<!-- p. 225 -->

      T7: Partiendo del estado S (Válido), si se observa en el bus una señal BusRdX (otro procesador
      necesita leer el dato para modificarlo) o si se debe quitar el bloque de caché para traer otro
      (Replace), el estado pasa a ser I (Inválido) y no es necesario enviar mensajes por el bus.

      T8: Partiendo del estado S (Válido), si el procesador en cuestión realiza una lectura de este dato
      (PrRd) o si se observa en el bus el mensaje BusRd (otro procesador realiza una lectura sin
      intención de modificarlo), el estado seguirá siendo S (Válido) y no es necesario enviar mensajes
      por el bus.

#### Ejemplos

<!-- p. 226 -->

#### Problema del Protocolo MSI
    El protocolo MSI no es eficiente para aplicaciones secuenciales. Estas aplicaciones suelen realizar
lecturas y modificaciones sobre algún dato que está en la memoria. Durante una operación de lectura-
modificación del dato, incluso si un par procesador-caché no comparte el dato con ningún otro par, el
protocolo requiere dos transacciones de bus:

      Una al leer: BusRd (transición de I a S).
      Otra al modificar: BusRdX (transición de S a M).

   Para mejorar esta situación, se utiliza un protocolo de cuatro estados.

#### Protocolo MESI: Invalidación de Cuatro Estados
    El protocolo MESI introduce un cuarto estado al esquema de coherencia de caché, añadiendo el
estado E (Exclusivo). Los estados del protocolo son: M (Modificado), E (Exclusivo), S (Compartido)
y I (Inválido).
    La semántica de estos estados es similar al protocolo MSI, con la introducción del estado E, el
cual indica que una caché posee la única copia de cierto bloque de datos, sin que este bloque haya sido
modificado. Esto significa que el bloque de datos está presente solo en la memoria principal y en esta
caché. A continuación se detallan las características principales del estado E:

      Exclusividad: La existencia del estado E reduce el tráfico en el bus, ya que permite una
      transición del estado E (Exclusivo) al estado M (Modificado) sin necesidad de realizar ninguna
      transacción en el bus.
      Sin Pertenencia: Aunque el bloque se encuentra en el estado E, la memoria tiene una copia
      válida del bloque. En este estado, el controlador de caché no está obligado a proporcionar el
      bloque en respuesta a una transacción de lectura para ese bloque, a diferencia del estado M en
      el protocolo MSI.

<!-- p. 227 -->

#### Nueva Señal en el Protocolo MESI
   Para soportar el estado E, se introduce la señal S (Share). Partiendo del estado I, cuando se realiza
una lectura que falla (ya que el estado era I), se envía uno de los siguientes mensajes al bus:

      S (Share): Cuando un procesador realiza una lectura desde el estado I (Inválido), consulta a
      las demás cachés si alguna tiene una copia del dato. Si al menos una caché posee el dato, se
      envía la señal S por el bus, en cuyo caso el bloque pasa al estado S (Shared).

      S (Share negado): Si ninguna otra caché tiene una copia del dato solicitado, no se envía la
      señal S (es decir, se niega el compartir). En este caso, el bloque pasa al estado E (Exclusive).

   Así, las transiciones posibles incluyen:

      PrRd(S): Corresponde a un fallo de lectura en el que al menos otra caché tiene una copia del
      dato solicitado.

      PrRd(S negado): Corresponde a un fallo de lectura en el que ninguna caché tiene una copia
      del dato solicitado, permitiendo la transición al estado E.

#### Diagrama de Estados

#### Transiciones del Protocolo MESI
    A continuación se detallan las transiciones del protocolo MESI entre los estados de la caché para
distintos tipos de operaciones de lectura y escritura.

      T1: Cuando un procesador realiza una lectura (PrRd) desde el estado I (Inválido), consulta a
      las demás cachés si alguna tiene una copia de este dato. Si alguna lo tiene, se envía la señal S
      por el bus, y el estado del bloque en la caché del procesador solicitante pasa a S (Shared). El
      dato se copia a la caché del procesador que realizó la lectura.

<!-- p. 228 -->

      T2: En la misma situación anterior, si ninguna caché tiene una copia del dato solicitado, no se
      envía la señal S por el bus, y el estado del bloque para el procesador solicitante cambia a E
      (Exclusive). El dato se copia a la caché del procesador que realizó la lectura.

      T3: Partiendo del estado I (Inválido), si un procesador intenta escribir un dato (PrWr), se
      produce un fallo de escritura debido a que el dato no está en caché. El estado cambia a M
      (Modificado o Dirty), el dato se copia desde la memoria principal a la caché de este procesador
      y se envía el mensaje BusRdX (lectura con exclusividad), indicando que se lee el dato con
      intención de modificarlo, por lo que todas las demás cachés deberán invalidar sus copias del
      dato.

      T4: Partiendo del estado S (Shared o Válido Compartido), si un procesador realiza una escritura
      (PrWr), el estado cambia a M (Modificado o Dirty). Se envía el mensaje BusRdX (lectura
      con exclusividad) para indicar que el dato será modificado, lo cual provoca que las demás cachés
      invaliden sus copias del dato.

      T5: Partiendo del estado M (Modificado o Dirty), el procesador en cuestión es el único que
      tiene la copia actualizada del dato. Por lo tanto, si realiza una escritura (PrWr) o una lectura
      (PrRd) sobre el dato, no cambia el estado ni se envía ningún mensaje por el bus.

      T6: Partiendo del estado E (Exclusive), si el procesador realiza una escritura (PrWr), el estado
      cambia a M (Modificado o Dirty), pero al ser el único par procesador/caché que tiene una copia
      del dato, no es necesario enviar ningún mensaje por el bus.

      T7: Partiendo del estado E (Exclusive), si el procesador realiza una lectura (PrRd), el estado
      no cambia ni es necesario enviar ningún mensaje por el bus.

      T8: Partiendo del estado S (Shared o Válido Compartido), ante una lectura por parte del
      procesador en cuestión (PrRd) o de algún otro (mensaje BusRd), el estado no cambia ni es
      necesario enviar ningún mensaje por el bus.

      T9: Partiendo del estado S (Shared o Válido Compartido), si se observa en el bus el mensaje
      BusRdX, se debe invalidar el dato, pues otro procesador va a modificarlo (el estado pasa a ser
      Inválido). No es necesario enviar ningún mensaje por el bus.

      T10: Partiendo del estado E (Exclusive), si se observa en el bus el mensaje BusRd (otro pro-
      cesador va a leer el dato), el estado pasa a ser S (Shared o Válido Compartido) y se envía un
      mensaje Flush al bus (se vuelca el dato en el bus para actualizarlo en memoria principal).

      T11: Partiendo del estado M (Modificado o Dirty), si se observa en el bus el mensaje BusRd (otro
      procesador va a leer el dato), el estado pasa a ser S (Shared o Válido Compartido) y se envía
      un mensaje Flush al bus (se vuelca el dato en el bus para actualizarlo en memoria principal).

      T12: Partiendo del estado E (Exclusive), si se observa en el bus el mensaje BusRdX, se debe
      invalidar el dato, pues otro procesador va a modificarlo (el estado pasa a ser Inválido). No es
      necesario enviar ningún mensaje por el bus.

      T13: Partiendo del estado M (Modificado o Dirty), si se observa en el bus el mensaje BusRdX, se
      debe invalidar el dato, pues otro procesador va a modificarlo (el estado pasa a ser Inválido). Sin
      embargo, partir del estado M (Modified o Dirty) indica que esta es la única copia actualizada del
      dato, por lo que se envía un mensaje Flush al bus (se vuelca el dato en el bus para actualizarlo
      en memoria principal).

<!-- p. 229 -->

### Carreras (Races) entre Escrituras
    Las carreras ocurren cuando dos entidades intentan escribir en la misma posición. No puede mo-
dificarse la caché hasta que se tenga el bus. Otro procesador podría tomar el bus antes y escribir el
mismo bloque en su caché.
    Por este motivo, se deben seguir los siguientes dos pasos:

   1. Arbitrar el bus: Los diferentes procesadores compiten por el control del bus en un proceso de
      arbitraje para determinar qué procesador obtiene el derecho a utilizar el bus.

<!-- p. 230 -->

   2. Poner el fallo sobre el bus y completar la operación o las transiciones partidas en
      el bus: Las transiciones sobre el bus no son atómicas. Puede haber varias transiciones para el
      mismo bloque en marcha al mismo tiempo, lo que debe resolverse.

    Los diferentes procesadores deben acceder al bus para obtener datos y direcciones. Además, los
procesadores ”espían” el bus de manera que, si la dirección en el bus coincide con algún ”tag”, se debe
invalidar o actualizar el bloque en la memoria caché asociada al procesador en cuestión.
    Consultar la coincidencia del tag interfiere con el uso de la caché por la CPU. La solución a este
problema es duplicar los tags. El bus serializa las escrituras (actúa como si fuera un semáforo); solo
un procesador realiza la operación con memoria.

### Consistencia de Memoria
    La coherencia implica que las escrituras sobre una posición se hacen visibles a todos los lectores en
el mismo orden, pero no dice nada sobre el orden con el que se hacen visibles las escrituras a diferentes
posiciones de memoria.
    Ejemplo: Considérense 2 procesos, P1 y P2, ejecutándose en diferentes procesadores. Sea el código:

                                        P1 :    A = 1;    B = 2;
                                       P2 :    print B;   print A;
    La intuición nos hace esperar que, si print B imprime un 2, entonces print A tiene que imprimir
un 1. Las instrucciones 2a y 2b leen diferentes direcciones de memoria, y la coherencia no dice nada
sobre el orden en que las escrituras de P1 sobre esas variables se hacen visibles a P2.
    Si P1 ejecuta la instrucción 1a y continúa con 1b, sin asegurarse antes de que P2 haya completado
la invalidación de A en su caché local, podría ocurrir que el resultado de print B fuera 2 y el de print
A fuera 0 (P2 lee A de su caché local).
    Es necesario un modelo de ordenación que los programadores puedan usar para razonar acerca de
la corrección de los programas.

### Modelo de Consistencia de Memoria para un espacio de direcciones compartido
    Especifica las restricciones en el orden en el que las operaciones de memoria (emitidas por un único
o por diferentes procesos) deben hacerse visibles a los procesadores. Incluye operaciones a las mismas
o a diferentes posiciones de memoria. La consistencia incluye la coherencia.
    Consistencia: El modelo de consistencia de memoria implica conocer exactamente cuándo un
valor que fue escrito por un procesador puede ser leído por los demás procesadores.
    Este es un contrato entre el programador y el diseñador del sistema. Los programadores se basan
en el modelo de consistencia para razonar acerca de los posibles resultados (corrección de los pro-
gramas). Para el diseñador del compilador o del hardware, el modelo impone limitaciones a posibles
reordenaciones (optimizaciones).

### Consistencia Secuencial
   Objetivo: Que el resultado de ejecutar un programa que usa varios procesos (threads) sea el
mismo independientemente de si los procesos se ejecutan en paralelo (multiprocesadores) o de forma
entrelazada (uniprocesador multiprogramado).
   Un multiprocesador es secuencialmente consistente si el resultado de la ejecución de cualquier
programa es el mismo que se obtendría si:

<!-- p. 231 -->

   1. Las operaciones de todos los procesadores se ejecutasen según algún orden secuencial.

   2. Las operaciones de cada procesador individual ocurren en el orden especificado por el programa.

    Esta es una abstracción para el programador del subsistema de memoria bajo el modelo de consis-
tencia secuencial: parece que los procesadores comparten una única memoria (aunque realmente esta
se halle distribuida entre los procesadores, cada uno con su caché).

### Consistencia Secuencial
   Para satisfacer la consistencia secuencial, tenemos dos restricciones:

   1. Orden del programa: Las operaciones de memoria de un proceso deben hacerse visibles, tanto
      a sí mismo como a los demás procesos, en el orden del programa.

   2. Atomicidad: Antes de emitirse la siguiente operación de memoria, es necesario que la operación
      en curso se haya completado (hecho visible) a todos los procesos. Es decir, antes de que un nuevo
      valor sea visible, la anterior escritura tiene que ser visible para todos los procesadores.

    La atomicidad de las escrituras es la clave que garantiza que antes de que un nuevo valor sea
visible, la anterior escritura tiene que ser visible para todos los procesadores.

### Ejemplo
   P1:
                                      (1a) A = 1;    (1b) B = 2;
P2:
                                     (2a) print B;   (2b) print A;
Valor inicial de A y B = 0.
   Resultados posibles bajo Consistencia Secuencial:

      Orden de operaciones 2a, 2b, 1a, 1b produce (A, B) = (0, 0).

      Orden de operaciones 1a, 2a, 1b, 2b produce (A, B) = (1, 0).

      Orden de operaciones 1a, 1b, 2a, 2b produce (A, B) = (1, 2).

<!-- p. 232 -->

    El resultado (A, B) = (0, 2) no es posible ya que:
    A = 0 implica 2b → 1a, lo que implica 2a → 1b. Sin embargo, B = 2 implica 1b → 2a. Esto genera
una contradicción en el orden de operaciones para lograr el resultado de A y B.
    Para la ejecución 1b → 1a → 2b → 2a se obtiene el resultado (1, 2). Aunque este no es el orden
del programa, (A, B) = (1, 2) es uno de los resultados posibles bajo consistencia secuencial, por lo que
este orden de operaciones es posible.
    Entonces, no es realmente importante en qué orden se emitan de hecho las operaciones a la memoria
o incluso cuándo se completen. Lo que importa es que parezcan completarse en un orden que no viole
la consistencia secuencial.

### Condiciones Suficientes para la Consistencia Secuencial
   1. (Condición Local) Todo proceso emite las peticiones a memoria en el orden especificado por
      el programa.

   2. (Condición Local) Después de emitir una operación de escritura, el proceso que la emitió
      espera antes de emitir su siguiente operación a que se haya completado dicha escritura.

   3. (Condición Global) Después de emitir una operación de lectura, el proceso que la emitió
      espera antes de emitir su siguiente operación a que se haya completado:

        a) Dicha lectura.
        b) La escritura que generó el valor devuelto por la lectura (no sólo debe haberse completado
           con respecto al proceso que realiza la lectura sino también con respecto a todos los procesos).

### Coherencia de Caché Basada en Directorio
    Recordatorio: La arquitectura NUMA (Nonuniform Memory Access), donde cada procesador
tiene acceso y control exclusivo a una parte de la memoria. Cada CPU tiene una caché privada y una
RAM privada también. En este escenario existe una red de interconexión para las CPUs. La latencia
de acceso a memoria puede variar dependiendo de la ubicación del bloque de memoria. Para un CPU
acceder a su caché será más rápido que acceder a las caches de otros CPU, ya que para esto se suma
el tiempo de pasar por la red. Cada procesador ve un espacio global de direcciones físicas compartido.
    Los accesos locales o remotos los maneja el Asistente de Comunicaciones del nodo. El procesador
y el controlador de caché no perciben si un fallo de caché se resuelve en su memoria local o es preciso
acudir a un nodo remoto de la red. Se tiene el problema de la coherencia de caches (al igual que en
Snoopy). Sin embargo, no hay un mecanismo para observar las transacciones de memoria (no hay bus,
hay una red) de otros nodos.
    Una solución: Llevar a la caché solo datos locales (T3E).
    Otra alternativa es utilizar un directorio que mantiene información sobre el estado y localización
en cachés de cada bloque de memoria. Este directorio podría ser un ”cuello de botella”, por lo que se
distribuye el directorio por los nodos.

### Protocolo de Directorio
   Se pueden utilizar un esquema similar a snoopy (por ejemplo con 3 estados: MSI), pero los cambios
de estado son provocados por mensajes a través de la red.
   Estados de un bloque en la caché de un procesador P:

   1. M (Exclusivo o Modificado): La caché de P tiene la única copia válida del bloque. La memoria
      principal no está actualizada.

<!-- p. 233 -->

   2. S (Shared o Compartido): La caché de P tiene una copia del bloque. Puede haber más copias
      en otras cachés. La memoria principal está actualizada.

   3. I (Inválido): El bloque no está en la caché de P.

   El directorio permite determinar para cada bloque de memoria:

   1. Si el bloque no se encuentra copiado en la caché de ningún procesador.

   2. Si existe una o varias copias del bloque sin modificar (clean, memoria principal actualizada) en
      los procesadores. Registra la lista de procesadores que tienen esas copias.

   3. Si un procesador (y uno solo) tiene una copia modificada del bloque (dirty, memoria principal
      no actualizada) y cuál es ese procesador.

   Posible implementación: 1 bit por procesador (indica presencia/ausencia del bloque) en el
procesador + 1 bit clean/dirty.
   Tres tipos de procesadores implicados en una transacción:

   1. Peticionario (local): El procesador que inicia la petición.

   2. Home: El procesador donde reside la zona de memoria que contiene la dirección solicitada.

   3. Remoto: Procesador cuya caché contiene copias válidas de la dirección solicitada en estado S o
      M. (Si el estado es M, sólo puede haber uno: Owner).

#### Ejemplos

<!-- p. 234 -->

### Organización del Directorio
    Los primeros esquemas de directorio aparecieron en los mainframes de IBM. La memoria (cen-
tralizada) mantenía copia de las etiquetas (tags) almacenadas en cada una de las cachés (Directorio
Centralizado).

### Esquema Plano
   El origen de la información de directorio para un bloque se encuentra en un lugar fijo (nodo
home/origen), que viene determinado directamente por la dirección del bloque (hashing).

      Ante un fallo de caché, se envía una transacción de red directamente al nodo origen para consultar
      el directorio.
   Esquema Plano Basado en Memoria
   La información de directorio acerca de un deter-
   minado bloque está almacenada en el nodo origen
   (home) de dicho bloque.

   Esquema Plano Basado en Caché
   La información de directorio acerca de un determi-
   nado bloque no está totalmente almacenada en el
   nodo origen, sino distribuida.

<!-- p. 235 -->

### Directorio Plano Basado en Memoria (Definiciones)
      Nodo Peticionario (local): Contiene el procesador que emite una petición del bloque.

      Nodo Origen (home): Nodo en cuya porción de memoria principal se encuentra el bloque
      (contiene el directorio).

      Nodo Sucio (dirty): Tiene una copia del bloque en su caché en estado modificado.

      Nodo Exclusivo (exclusive): Tiene una copia del bloque en estado exclusivo (única copia de
      caché válida y el bloque está actualizado en memoria).

      Nodo Propietario (owner): Nodo que mantiene en la actualidad la copia válida de un bloque
      y debe suplir los datos cuando sean necesarios (puede ser un nodo Sucio o un nodo Origen).

#### Funcionamiento

### Rendimiento y Sobrecarga
#### Rendimiento en las Escrituras (mensajes de invalidación)
      Número de mensajes (BW): Proporcional al número de nodos que comparten el bloque.

<!-- p. 236 -->

      Número de mensajes en el camino crítico (Latencia): La identidad de todos ellos está
      disponible en el nodo origen, por lo que los mensajes de invalidación se pueden enviar en paralelo.

### Sobrecarga de Almacenamiento
   Se refiere a la cantidad de memoria adicional que se requiere para mantener el directorio, que es
una estructura que realiza el seguimiento de qué bloques de memoria están presentes en qué cachés.

                   M = número total de bloques de memoria presentes en el sistema.
                   Nproc = Número de procesadores o nodos presentes en el sistema.

                                               Número de entradas en el directorio
                                                                                     !
            Sobrecarga de directorio ( %) =                                              × 100
                                                              M
   Para un tamaño de línea de 4 bytes:

      4 nodos: Sobrecarga del directorio 12.5 %

      25 nodos: Sobrecarga del directorio 50 %

      1024 nodos: Sobrecarga del directorio 200 %

### Soluciones
      Utilizar nodos multiprocesador (solo 1 bit por nodo). Ejemplo: 25 procesadores, 4 procesadores
      por nodo, línea de 128 B: Sobrecarga: 0.25 %

      En lugar de almacenar 1 bit por nodo en cada entrada del directorio, se almacenan un deter-
      minado número de punteros a los nodos que comparten dicho bloque (reducción de anchura del
### Directorio Plano Basado en Caché

      Organizar el directorio como una caché, en lugar de tener una entrada por cada bloque (reducción
      de altura del directorio).

6.26.    Directorio Plano Basado en Caché

   Existe una memoria principal, origen de cada bloque.

<!-- p. 237 -->

   1. La entrada del directorio en el nodo origen tiene:

           Un puntero al primer nodo (nodo cabecera) que tiene copia de dicho bloque.
           Bits de estado.
           El resto de los nodos con copia se encuentran unidos mediante una lista enlazada distribuida
           (IEEE 159-1992 Scalable Coherent Interface (SCI): doblemente enlazada).

   2. Fallo de lectura:

           El nodo peticionario envía una petición al nodo origen del bloque para determinar la iden-
           tidad del nodo cabecera.
           El nodo origen responde con la identidad del nodo cabecera.
           El nodo peticionario envía solicitud al nodo cabecera para que lo inserte a la cabeza de la
           lista (convirtiéndose en el nuevo nodo cabecera), lo cual incrementa la latencia.
           Los datos son enviados por:
             • El nodo origen, si tiene copia.
             • El nodo cabecera en caso contrario (siempre tiene la última copia).

   3. Eliminación (Reemplazamiento) e inserción en la lista:

           Añade bastante complejidad al protocolo: es necesario coordinarse con el nodo anterior y
           posterior en la lista (que podría estar intentando reemplazar el mismo bloque).

   4. Escritura:

           El nodo peticionario puede encontrarse ya en la lista de nodos que comparten el bloque.
           Se recorre el resto de la lista para invalidar las sucesivas copias.
           Los acuses de recibo de las invalidaciones se envían al nodo que realiza la escritura.

   5. Rendimiento en las escrituras (mensajes de invalidación):

           Número de mensajes (BW): proporcional al número de nodos que comparten el bloque
           (semejante a los esquemas basados en memoria), pero distribuidos.
           Número de mensajes en el camino crítico (latencia): también proporcional al número de
           nodos que comparten el bloque (los mensajes se serializan).

   6. Ventajas respecto a los esquemas basados en memoria:

           Menor sobrecarga de directorio.
           Punteros al nodo cabecera: proporcional al número de bloques de memoria de la máquina.
           Punteros siguiente y anterior: proporcional al número de bloques de caché en la máquina
           (mucho menor que el número de bloques de memoria).
           El trabajo realizado por los controladores para enviar las invalidaciones no está centralizado
           en el nodo origen, sino distribuido entre los nodos que comparten el bloque.
           La lista enlazada guarda el orden en el que se han realizado los accesos.

<!-- p. 238 -->

Sincronización: Introducción
   Necesidad: Garantizar acceso seguro de un proceso a variables compartidas.

      Problema presente incluso en uniprocesadores con multiprogramación (exclusión mutua, seccio-
      nes críticas).

      Aspectos relevantes:

        • Primitiva de hardware básica: una instrucción no interrumpible (operación atómica)
          que lee y actualiza una cierta posición de memoria (cerrojo).
        • Las operaciones de sincronización a nivel de usuario (rutinas de software de sincronización)
          se construyen usando esta primitiva de hardware.
        • En sistemas MPP, las operaciones de sincronización pueden convertirse en el cuello de
          botella del sistema.

   Competencia entre procesos: Un conjunto de procesos compiten por leer y modificar el cerrojo
(adquisición del cerrojo).
      En contraste con el caso uniprocesador, todos estos procesos pueden ejecutarse simultáneamente
      en distintos procesadores.

      Cada procesador puede leer el cerrojo desde su caché local sin generar tráfico en el bus.

      Sin embargo, al escribir genera tráfico en el sistema de comunicaciones (invalidaciones), incluso
      si el intento de modificar el cerrojo es fallido porque el cerrojo ya ha sido adquirido por otro
      procesador.

      El procesador puede permanecer en un bucle generando tráfico inútil en el bus hasta que logra
      adquirir el cerrojo.

Sincronización: Primitivas de Hardware Básicas
    Intercambio (atomic exchange): Intercambia el valor de un registro y una posición de memoria
(cerrojo).
      Convenciones de interpretación:

        • 0 ⇒ el cerrojo está libre.
        • 1 ⇒ el cerrojo está bloqueado y no es accesible.

<!-- p. 239 -->

      Si dos procesadores intentan ejecutar la operación Exchange a la vez, el mecanismo de seria-
      lización de escrituras garantiza que uno de los dos obtendrá un 0 en el registro y el otro un
      1.

   Otras primitivas:

      Test-and-set: Comprueba el valor de una variable y si está en cero, la pone a 1.

      Fetch-and-increment: Incrementa el valor de una variable en memoria.

Operaciones Atómicas en Multiprocesadores
      Requiere una lectura y escritura en una sola instrucción no interrumpible.

      Complica la implementación de coherencia: el hardware no permite otra operación entre la lectura
      y escritura y debe evitar el interbloqueo.

Sincronización con un Par de Operaciones
      Load Linked (LL): Lee una dirección de memoria y guarda en un registro especial (link register)
      la dirección leída.

        • Si ocurre una interrupción (cambio de contexto) o si el bloque de caché que contiene la
          dirección es invalidado por una escritura, el link register se borra.

      Store Conditional (SC): Almacena el contenido de un registro R en una dirección de memoria
      si coincide con la dirección almacenada en el link register. En caso contrario, no se realiza el
      almacenamiento.

        • Si el almacenamiento tuvo éxito, devuelve R = 1; en caso contrario, R = 0. Analizando
          el valor retornado por SC, se puede deducir si el par se ejecutó como si las instrucciones
          fueran atómicas.

Implementación de Otras Primitivas con LL+SC
   Intercambio:

tryExchange:
    LL R2, 0(R1)            ; load linked
    SC R3, 0(R1)            ; store conditional
    BEQZ R3, try            ; branch if store fails
    MOV R4, R2              ; success: put load value in R4

   Fetch-and-increment:

try:
    LL R2, 0(R1)            ; load linked
    DADDUI R3, R2, 1        ; increment
    SC R3, 0(R1)            ; store conditional
    BEQZ R3, try            ; branch if store fails

    Nota: Entre LL y SC puede haber operaciones sobre registros; esto puede generar problemas si no
es el caso.

<!-- p. 240 -->

Spin Lock
   Un spin lock es un bucle en el que un proceso permanece intentando conseguir un cerrojo hasta
que lo consigue.

Implementación Simple sin Coherencia de Caché
   Para implementar un spin lock sin coherencia de caché, se puede mantener las variables del cerrojo
en memoria. Supongamos que la variable cerrojo está en M [0 + (R1)]:

DADDUI R2, R0, 1           ; R2 = 1
lockit:
EXCH R2, 0(R1)             ; intercambio atómico
BNEZ R2, lockit            ; ¿ya bloqueado?

      Los accesos a memoria implican tráfico en el sistema de comunicaciones, lo cual se convierte en
      un cuello de botella cuando varios procesadores compiten por el cerrojo.

      Incluso con un sistema con coherencia de caché, la situación no mejora mucho. Varios procesa-
      dores ejecutando EXCH pueden generar fallos de escritura e invalidaciones.

Implementación con Coherencia de Caché
    Una forma de mejorar el spin lock en un sistema con coherencia de caché es realizar una consulta
preliminar del cerrojo antes de hacer el intercambio atómico (esquema test-and-exchange).

      Un procesador permanece leyendo su copia local mientras detecta que el cerrojo está bloqueado.

      Cuando en su caché el cerrojo aparece libre, ejecuta un EXCH y compite con otros procesadores
      que estén haciendo el mismo spin lock.

      El procesador ganador verá un 0 en el registro de la instrucción EXCH, mientras que los demás
      verán un 1.

      Esto evita invalidaciones inútiles cuando un procesador está ejecutando repetidamente el bucle
      de espera.

lockit:
    LD R2, 0(R1)               ; carga preliminar del cerrojo
    BNEZ R2, lockit            ; si no está disponible, espera
    DADDUI R2, R0, 1           ; R2 = 1
    EXCH R2, 0(R1)             ; intercambio atómico
    BNEZ R2, lockit            ; si el cerrojo no estaba en 0, espera

      Cuando el procesador ganador libera el cerrojo (escribiendo un 0), la carrera entre los procesa-
      dores ”perdedores” comienza de nuevo.

<!-- p. 241 -->

Ejemplo: Uso del Código Anterior con 3 Procesadores
    A continuación, se muestra un ejemplo de ejecución del código anterior con tres procesadores (P 0,
P 1 y P 2) y el estado de coherencia del cerrojo en cada paso.

Implementación de Spin Lock usando LL+SC
   El siguiente código muestra la implementación de un spin lock utilizando las instrucciones LL
(Load Linked) y SC (Store Conditional) para evitar el uso de una instrucción atómica de lectura-
modificación-escritura.

lockit:
    LL R2, 0(R1)             ; Cargar el cerrojo en R2, sin generar tráfico si el
                             ; cerrojo está en caché local.
     BNEZ R2, lockit         ; Si R2 != 0, el cerrojo esta ocupado, sigue
                             ; esperando (spin).
     DADDUI R2, R0, 1        ; Si el cerrojo estaba libre (R2 = 0), pon R2 = 1 (indica
                             ; que el cerrojo se va a bloquear).
     SC R2, 0(R1)            ; Intenta almacenar R2 (1) en el cerrojo. Solo lo hará si
                             ; no ha habido una escritura en la memoria entre el LL y el SC.
     BEQZ R2, lockit         ; Si SC falló (R2 = 0), significa que el cerrojo fue modificado
                             ; por otro procesador, entonces intenta de nuevo.

Explicación de cada paso:
   1. LL R2, 0(R1): La instrucción LL (Load Linked) carga el valor del cerrojo desde la dirección
      de memoria R1 a R2. Esta instrucción marca la dirección de memoria como ”vinculada”, lo que

<!-- p. 242 -->

      significa que el procesador espera que cualquier escritura posterior en esa dirección cause una
      invalidación en su caché si otra escritura ocurre antes de que se complete el SC. Esta instrucción
      no genera tráfico en el sistema de comunicaciones, siempre y cuando la variable del cerrojo esté
      en la caché local.

   2. BNEZ R2, lockit: Si R2 no es igual a cero (lo que significa que el cerrojo está ocupado), el
      procesador entra en un bucle de espera (”spin”) e intenta leer nuevamente la variable de cerrojo
      hasta que se libere.

   3. DADDUI R2, R0, 1: Si el cerrojo estaba libre (R2 = 0), se pone el valor de R2 a 1, indicando que
      el cerrojo está ahora bloqueado.

   4. SC R2, 0(R1): La instrucción SC (Store Conditional) intenta almacenar el valor de R2 (que es
      1, indicando que el cerrojo está bloqueado) en la misma dirección de memoria R1. El almacena-
      miento solo se realiza si no ha habido ninguna escritura en la memoria entre la ejecución del LL
      y el SC. Si otra escritura modificó el valor del cerrojo en este intervalo (por ejemplo, debido a
      una interrupción o escritura de otro procesador), el SC falla.

   5. BEQZ R2, lockit: Si el SC falla (es decir, R2 = 0), significa que el cerrojo fue modificado por
      otro procesador entre el LL y el SC, por lo que el procesador intenta de nuevo.
