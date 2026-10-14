<!-- p. 160 -->

## Unidad 4: Lanzamiento Multiple - Limites de ILP - Multithreading
    Ya se está alcanzando el límite práctico del Instruction Level Parallelism (ILP). Las técnicas
clásicas de explotación de ILP han permitido reducir el CPI (Cycles Per Instruction) hasta valores
cercanos a uno; sin embargo, a partir de este punto resulta cada vez más difícil obtener mejoras
significativas adicionales.
    Si se desea continuar incrementando la performance de un procesador, es necesario recurrir a otras
formas de paralelismo. Antes de avanzar, resulta conveniente precisar qué se entiende por performance.
En general, esta se mide en términos de throughput (cantidad de instrucciones completadas por unidad
de tiempo) y depende de tres factores principales:

      La frecuencia de reloj.

      La cantidad total de instrucciones a ejecutar.

      El CPI (Cycles Per Instruction), determinado por la microarquitectura.

    El objetivo de diseño es reducir el CPI incluso a valores menores que uno, lo que implica
completar, en promedio, más de una instrucción por ciclo de reloj. Dado que el ILP explotable dentro
de un único hilo es limitado, la única forma de alcanzar un CPI menor que uno es mediante la ejecución
paralela de múltiples instrucciones independientes, ya sea a través de arquitecturas superescalares,
ejecución fuera de orden o, de manera más efectiva, explotando paralelismo a niveles superiores como
el Thread Level Parallelism (TLP) mediante procesadores multinúcleo y multihilo.
    En este contexto, el énfasis del diseño de procesadores modernos se desplaza desde la optimi-
zación del ILP hacia la explotación del paralelismo entre hilos y aplicaciones, permitiendo mejorar
el throughput total del sistema aun cuando el rendimiento monohilo se mantiene aproximadamente
constante.
    La frecuencia ya no puede incrementarse fácilmente debido a limitaciones físicas (consumo y disipa-
ción de calor), y la cantidad de instrucciones depende del software (fuera del alcance de esta materia).
Por lo tanto, la variable de interés es el CPI.
    Sin embargo, en arquitecturas escalares tradicionales, incluso con técnicas de ILP, sólo se puede
emitir una instrucción por ciclo en el mejor de los casos. Para ir más allá de ese límite, se requiere
introducir más de una instrucción por ciclo. Aquí aparecen los procesadores superescalares: mi-
croarquitecturas escalares que incorporan múltiples vías de emisión (multiple issue) para sostener la
ejecución paralela de instrucciones independientes.
    En esta sección se abordará rápidamente el concepto de superescalaridad, entendida como la capa-
cidad de un procesador de lanzar más de una instrucción por ciclo, con el objetivo de seguir reduciendo
el CPI y mejorar el throughput global.
    Objetivo: Obtener un CPI (Cycles Per Instruction) menor a 1. Por ejemplo, un CPI de 0.2 implica
que se ejecutan cinco instrucciones por ciclo, lo cual se lograría ejecutando instrucciones en paralelo,
es decir, lanzando y ejecutando múltiples instrucciones por ciclo.
    Recursos disponibles para lograr esto:

      Área de silicio disponible.

      Técnicas para resolver las dependencias de datos (planificación).

      Técnicas para resolver las dependencias de control (especulación).

<!-- p. 161 -->

### Alternativas para Lanzamiento Múltiple de Instrucciones
### Procesador Superescalar

       Procesador Superescalar con planificación estática: Ejecuta instrucciones en orden.

       Procesador Superescalar con planificación dinámica y especulación: Ejecuta instruc-
       ciones fuera de orden, aumentando el paralelismo de ejecución.

   Procesadores VLIW (Very Long Instruction Word): Agrupan múltiples instrucciones in-
dependientes en una sola palabra de instrucción, que se ejecutan en paralelo.
   Para seguir reduciendo el CPI y lanzar más de una instrucción por ciclo, necesitamos arquitecturas
más avanzadas. En este punto aparecen dos grandes alternativas:

       Procesadores Superescalares: son arquitecturas que duplican o multiplican parte de sus
       unidades funcionales (ALUs, unidades de acceso a memoria, etc.) para permitir emitir más de
       una instrucción por ciclo.

       Very Long Instruction Word (VLIW): arquitecturas donde el compilador genera instruc-
       ciones muy largas que empaquetan varias operaciones en paralelo, delegando la planificación al
       software en lugar del hardware.

   El diseño superescalar puede implementarse de distintas maneras:

   1. Superescalar estático: la planificación de instrucciones se realiza en tiempo de compilación.

   2. Superescalar dinámico sin especulación: el hardware decide en tiempo de ejecución qué
      instrucciones emitir, pero sin mecanismos especulativos.

   3. Superescalar dinámico con especulación: agrega técnicas de ejecución especulativa para
      aprovechar más paralelismo. En la práctica, este último suele ser más teórico que real, ya que
      implica una complejidad de hardware muy elevada.

     El problema de estas técnicas es que requieren más hardware: más unidades funcionales, más
señales de control y mayor consumo energético. Además, aparece la necesidad de mantener la cohe-
rencia cuando se trabaja con múltiples memorias o cachés. Aunque los registros pueden duplicarse
para soportar varias vías de ejecución, la memoria principal no se duplica; en cambio, cada procesador
o núcleo dispone de sus propios niveles de caché, lo que introduce el desafío de la coherencia de
memoria (problema central en sistemas multiprocesador y arquitecturas NUMA).
     En paralelo a estas técnicas, surge la constatación de que el ILP tiene límites claros: aun con emisión
múltiple, no siempre se logra alimentar al procesador con suficientes instrucciones independientes. Por
ello, se introduce un nuevo paradigma: el Thread Level Parallelism (TLP).
     El TLP busca aprovechar múltiples hilos de ejecución en lugar de depender únicamente de la
independencia entre instrucciones dentro de un solo hilo. Si un procesador superescalar no recibe su-
ficientes instrucciones de un programa secuencial, puede mantener sus unidades activas ejecutando
instrucciones provenientes de varios hilos distintos. Este enfoque conduce directamente a los procesa-
dores multithread y, en última instancia, a las arquitecturas multicore modernas.

4.2.    Procesador Superescalar
   En un procesador Superescalar de grado dos (lo que indica que se ejecutan dos instrucciones al
mismo tiempo) y de dos vías, se tienen dos pipelines en paralelo (de ahí el término ”de dos vías”).
Esto permite, en el mejor de los casos, ejecutar dos instrucciones simultáneamente, siempre que no

<!-- p. 162 -->

                                              Detección de
        Tipo           Forma del issue                             Planificación             Ejemplos
                                                 azares
    Superscalar                                                                          Embedded MIPS,
                            Dinámico               HW                   Estática
       estático                                                                              ARM
    Superscalar
                            Dinámico               HW                   Dinámica              Ninguno
      dinámico
    Superscalar                                                     Dinámica con            P4, Core2,
                            Dinámico               HW
    especulativo                                                    especulación         Power5, SparcVI
        VLIW                Estático          Básicamente SW          Estática           TI C6x, Itanium

existan dependencias entre las instrucciones. En este caso, dos instrucciones se buscan, decodifican y
ejecutan al mismo tiempo.

                                                         Para implementar este diseño, se deben duplicar los
                                                         recursos clave, incluyendo:

                                                               Puertas de bloque de registros.

                                                               Buses.

                                                               Puertas de memoria.

                                                               Control.

    En teoría, esto permitiría alcanzar un CPI ideal de 0.5, pero en la práctica, varios factores impiden
alcanzar este ideal:

      Saltos.

      Instrucciones LOAD.

      Dependencias Verdaderas (LDE).

   Para optimizar el rendimiento y acercarse al CPI ideal, se requiere:

      Una predicción de saltos sofisticada.

      Un manejo especial de las instrucciones LOAD, como cargas especulativas y técnicas de prebús-
      queda.

    El procesador superescalar genera una presión adicional sobre la memoria y un incremento en los
riesgos de ejecución. Para reducir esta complejidad, se pueden introducir limitaciones, como restringir
el acceso a memoria a una sola instrucción LOAD por ciclo, lo que reduce la presión sobre la memoria.

<!-- p. 163 -->

#### Superescalar Simple (Estático, ejecución de instrucciones en orden)
                                                                             El procesador superescalar
                                                                             simple utiliza un detector de
                                                                             azares para bloquear el lanza-
                                                                             miento simultáneo de ciertas
                                                                             instrucciones, asegurando una
                                                                             ejecución en orden. La regla
                                                                             de lanzamiento es que se
                                                                             pueden lanzar en paralelo una
                                                                             instrucción de punto flotante
                                                                             y una de cualquier otro tipo.

Búsqueda y Decodificación El procesador busca y decodifica dos instrucciones en paralelo, cada
una de 64 bits. La decodificación se realiza en secuencia, es decir, una instrucción se decodifica tras
otra. La segunda instrucción solo se lanzará si la primera ya ha sido lanzada y no existen conflictos
de recursos.

Unidades Funcionales Segmentadas El procesador cuenta con unidades funcionales segmentadas
para realizar operaciones simples, como sumas y restas, que pueden completarse en un ciclo de reloj.
Sin embargo, operaciones más complejas, como divisiones y raíces cuadradas, requieren múltiples ciclos
de reloj.

Banco de Registros Cuando se ejecutan instrucciones en paralelo, el banco de registros debe tener
puertas adicionales para permitir la lectura simultánea de los registros necesarios.

Lanzamiento de Instrucciones y Conflictos El lanzamiento de instrucciones se realiza de manera
simple, lo que implica que se busca ejecutar instrucciones evitando conflictos de recursos compartidos,
como unidades funcionales y registros. Sin embargo, existen posibles conflictos específicos con ins-
trucciones de carga (load), almacenamiento (store), o movimiento de datos entre registros de punto
flotante (FP).
    Para mitigar los conflictos de Dependencia Verdadera (LDE), se debe asegurar una distancia
adecuada entre las instrucciones, de manera que los datos necesarios estén disponibles antes de ser
requeridos.

Efecto de los Saltos y Conflictos de Dependencia El procesador también debe gestionar el
efecto de los saltos y el ”salto retardado”, ya que una de las instrucciones en ejecución podría estar en
la posición de delay slot en caso de un salto retardado. Esto puede provocar conflictos de dependencia
y penalizaciones en la ejecución debido a los saltos.

<!-- p. 164 -->

    En la Figura se muestra un loop desenrollado (loop unrolling), técnica que consiste en replicar
varias iteraciones del loop dentro de una única iteración, con el objetivo de aumentar el paralelismo y
aprovechar mejor las unidades funcionales disponibles.

Descripción del código
      Se realizan 5 LOADs consecutivos que cargan los datos desde memoria a registros de punto
      flotante (F 0, F 6, F 10, F 14, F 18).

      Luego se ejecutan 5 operaciones ADDD en punto flotante, cada una con los registros cargados
      y un operando común (F 2).

      Finalmente, se ejecutan 5 STOREs para escribir los resultados en memoria.

Características
   1. Los LOADs son instrucciones enteras, por lo que no ocupan las unidades funcionales de punto
      flotante, lo cual permite que se mezclen en el mismo ciclo con operaciones ADDD sin generar
      conflictos.

   2. El loop queda estructurado de forma fija: siempre se cargan 5, se suman 5 y se almacenan 5.

   3. El CPI efectivo resulta de aproximadamente 2.4 ciclos por instrucción, lo cual es una mejora
      respecto a la ejecución estrictamente escalar.

   4. La ventaja principal es que no se modifica el código original del programa: el compilador
      aplica el desenrollado y reordenamiento, pero el programa fuente se mantiene.

Limitaciones
      Existe bloqueo en el lanzamiento: las instrucciones están organizadas de forma fija y no se
      pueden reordenar dinámicamente en tiempo de ejecución.

<!-- p. 165 -->

      La planificación es estática, realizada por el compilador. Esto implica que el rendimiento pue-
      de degradarse si cambian las condiciones en ejecución (fallos de caché, dependencias inesperadas,
      etc.).

      En arquitecturas VLIW, cada instrucción es de longitud fija: por ejemplo, se definen 2 vías
      para FP, 2 vías para entero y 1 vía para LOAD/STORE. Cuando el compilador no puede llenar
      todas las posiciones, completa con NOPs. De esta manera, el código mantiene siempre la misma
      longitud de instrucción, aunque haya huecos.

      En un procesador superescalar, el hardware decide dinámicamente cuántas instrucciones emitir
      por ciclo, y si no encuentra suficientes, simplemente lanza menos.

      En VLIW, en cambio, el compilador debe armar las instrucciones compuestas de antemano. Si
      no hay suficiente paralelismo, completa con NOPs, lo que hace que el código sea más predecible
      pero menos flexible.

   En resumen, este ejemplo muestra cómo el loop unrolling con 5 LOADs permite aprovechar
paralelismo a nivel de instrucción, pero también deja en evidencia las diferencias entre un enfoque
superescalar dinámico y uno VLIW estático.

#### Ventajas y Desventajas del Superescalar Simple
    Las instrucciones que se encuentran en el mismo renglón se ejecutan en paralelo en un procesador
superescalar simple. Algunas instrucciones, sin embargo, se ejecutan solas en un ciclo, como si la
instrucción que debería acompañarlas fuera una NOP, debido a la espera para que los operandos de las
instrucciones siguientes estén listos, evitando dependencias.
    En comparación, antes de implementar el superescalar, una iteración requería aproximadamente 12
ciclos. Con el superescalar y ejecución en paralelo, se reduce a un promedio de 2.4 ciclos por iteración,
aunque se agrega una iteración adicional para optimizar el rendimiento.

Ventajas

      No es necesario modificar el código fuente, lo que permite mantener la compatibilidad de los
      archivos binarios.

      No existen riesgos en la ejecución, debido a la estructura de ejecución en orden.

Desventajas

      Mezcla de instrucciones enteras y de punto flotante: Se alcanza un CPI de 0.5 solo si el programa
      contiene un 50 % de instrucciones FP y un 50 % de instrucciones enteras.

      Bloqueos en el lanzamiento: Al inicio, el sistema solo utilizará uno de los pipelines hasta que los
      operandos de las instrucciones de punto flotante estén disponibles.

      Planificación fija: No se adapta dinámicamente a cambios en tiempo de ejecución, como fallos
      en caché.

      Replanificación de código: Para maximizar la eficiencia en nuevas implementaciones, es necesario
      reordenar las instrucciones.

<!-- p. 166 -->

### Procesadores VLIW (Very Long Instruction Word)

    Cada instrucción en un procesador VLIW incluye una operación por ALU, lo cual genera instruc-
ciones de muchos bits. El análisis de dependencias se realiza en tiempo de compilación para determinar
cuántas operaciones se pueden incluir en un slot de instrucción sin crear problemas.

       Todas las operaciones en una instrucción se ejecutan en paralelo.

       Este método es eficiente cuando el software contiene muchas operaciones con pocas dependencias,
       como en el caso de los paquetes IA64 o los procesadores Transmeta con arquitectura “Molecula”.

       Si existen dependencias entre operaciones, se deben insertar instrucciones NOP, lo que crea slots
       vacíos y puede disminuir la eficiencia.
                                                                                   Código Original:
#### Ejemplo de Procesador VLIW
                                                                                       LD   F0, 0(R1)
   Este ejemplo muestra cómo un procesador VLIW puede ejecutar va-                     ADDD F4, F0, F2
   rias operaciones en paralelo mediante técnicas de Loop Unrolling y Re-              SD   0(R1), F4
   nombrado de Registros. Estas técnicas permiten crear una secuencia de               SUBI R1, R1, #8
   operaciones sin dependencias, ideal para procesadores VLIW.                         BNEZ R1, LOOP

   Para este caso, la dependencia en el registro F4 se resuelve con el renombrado de registros, lo que
permite un mayor paralelismo. Aplicando estas técnicas, el código modificado queda:

Código Modificado (Aplicando Loop Unrolling y Renombrado de Registros):
    LD   F0, 0(R1)
    LD   F6, -8(R1)
    LD   F10, -16(R1)
    LD   F14, -24(R1)
    ADDD F4, F0, F2
    ADDD F8, F6, F2
    ADDD F12, F10, F2
    ADDD F16, F14, F2
    SD   0(R1), F4
    SD   -8(R1), F8
    SD   -16(R1), F12

<!-- p. 167 -->

     SD   -24(R1), F16
     SUBI R1, R1, #32
     BNEZ R1, LOOP

   Para ejecutar estas operaciones en paralelo en un procesador VLIW se necesita:

      Capacidad de acceder a múltiples direcciones de memoria de forma simultánea (instrucciones
      LD).

      Más registros que en el código original para evitar dependencias en las instrucciones de punto
      flotante ADDD.

      Al menos un buffer para almacenar resultados temporales de las instrucciones SD.

#### Latencia y Mejora de Rendimiento
Latencia del Código Original: En el código original, la latencia se presenta de la siguiente manera:
- Se debe esperar un ciclo por la dependencia entre las instrucciones LD y ADDD. - Se deben esperar
dos ciclos por la dependencia entre las instrucciones ADDD y SD.
    Como resultado, la ejecución del bucle en el código original implica un mayor tiempo de espera
debido a estas dependencias.

Rendimiento del Código Modificado: Con el código modificado, se logra ejecutar 4 iteraciones
(ya que hay 4 instrucciones LD, 4 ADDD y 4 SD) en 14 ciclos, lo que resulta en 3.5 ciclos por iteración.
Esto representa una mejora significativa en comparación con el código original.

Ejecución Paralela con VLIW: Mediante el uso de VLIW, se logra ejecutar 7 iteraciones (ya
que hay 7 instrucciones LD, 7 ADDD y 7 SD) en 9 ciclos, lo que equivale a 1.3 ciclos por iteración.
Esta mejora es notable en términos de eficiencia de ejecución.

Ocupación de Slots: Durante estos 9 ciclos, se tienen 5 operaciones posibles por instrucción,
lo que da un total de 45 slots. En estos 45 slots se realizaron 23 operaciones, resultando en una
ocupación menor al 50 % en cuanto a la capacidad de cómputo paralelo. Solo en el tercer ciclo se
ocupan todas las operaciones disponibles en paralelo.

Requerimientos de Registros: Es importante señalar que se requirió de muchos registros para
lograr esta ejecución eficiente y paralela.

<!-- p. 168 -->

#### Ventajas y Desventajas de VLIW

      Hardware muy simple.

      No detecta dependencias.

      Lógica de lanzamiento simple.

      Puede explotar el paralelismo a lo largo de todo el programa.

Desventajas:

      Planificación estática, lo que lo hace muy sensible a fallos de caché.

      Necesita desenrollado de bucles muy agresivo.

      El bloque de registros es muy complejo en términos de área y tiempo de acceso, ya que tiene
      múltiples puertas para leer múltiples registros a la vez.

      Cuando hay dependencias, se generan muchas NOP, lo que resulta en:

         • Poca densidad de código (definida como código efectivo dividido por la cantidad de slots).

      La capacidad y el ancho de banda de la caché de instrucciones debe ser mayor, ya que se deben
      buscar múltiples instrucciones al mismo tiempo.

      Compilador muy complejo, que debe buscar dependencias, realizar loop unrolling, llenar los slots
      con operaciones o NOP según corresponda, etc.

      Incompatibilidad de binarios: para distintas arquitecturas VLIW (o incluso para distintos com-
      piladores del mismo código fuente), la asignación de instrucciones a los slots y las dependencias
      entre las instrucciones pueden variar, generando binarios incompatibles.

      Todas las operaciones dentro de una instrucción VLIW se ejecutan de manera síncrona; es
      decir, todas las operaciones contenidas en una instrucción deben completarse antes de pasar a la
      siguiente. Esta sincronización rígida puede presentar desafíos en situaciones de exclusión mutua.

Nota: Para este procesador también se puede utilizar la ejecución con predicados.

#### Ejemplo: Arquitectura EPIC (Explicitly Parallel Instruction Computing)
    La arquitectura EPIC (Explicitly Parallel Instruction Computing) fue desarrollada por Intel y
Hewlett-Packard (HP) para los procesadores IA-64 (Itanium). Es una evolución de la arquitectura
VLIW, donde la responsabilidad de encontrar y explotar el paralelismo recae en el compilador, y no
en el hardware.
    En EPIC, las instrucciones no son emitidas de una en una, sino en paquetes de 128 bits, que
incluyen varias operaciones paralelas más información de control de dependencias.

<!-- p. 169 -->

Estructura del paquete

      Cada paquete tiene 128 bits.

      En su interior se incluyen hasta 3 operaciones, de 41 bits cada una, más un campo de control
      llamado TMP (Template).

      Cada operación contiene:

        • Código de operación (Ope).
        • Tres registros de entrada/salida (operaciones de 3 operandos).
        • Un bit de predicado, que determina si la instrucción se ejecuta o no.

      El campo TMP define cómo están organizadas las instrucciones y codifica las dependencias entre
      ellas (indica los stop bits que marcan los límites entre grupos de instrucciones independientes).

Características destacadas

      Registros: 128 registros enteros de 64 bits y 128 registros de punto flotante de 82 bits.

      Predicación: hasta 64 registros de predicado de 1 bit, lo que permite ejecutar instrucciones
      condicionalmente sin necesidad de ramas.

      Cargas especulativas: permiten adelantar accesos a memoria antes de que se confirme si
      realmente son necesarios, reduciendo stalls.

      Instrucciones de verificación de carga: validan si las cargas especulativas fueron correctas.

      Hardware de chequeo de memoria: detecta dependencias de memoria para asegurar la
      consistencia.

Implementaciones

      Itanium (2001): primera implementación, con capacidad de ejecutar hasta 6 operaciones por
      ciclo, 10 etapas de pipeline, 800 MHz.

      Itanium 2 (2005): segunda generación, con mejoras en el pipeline (8 etapas), 6 operaciones
      por ciclo, hasta 1.66 GHz.

<!-- p. 170 -->

Resumen EPIC se diferencia de VLIW en que agrega mecanismos adicionales para mejorar el pa-
ralelismo y el rendimiento:

      Introducción de bits de parada (stop bits) para indicar límites claros entre grupos de instrucciones
      dependientes.

      Soporte de cargas especulativas y verificación para mejorar el uso de memoria.

      Gran cantidad de registros y ejecución predicada para reducir dependencias y ramas.

    En conclusión, EPIC es una evolución de VLIW que mantiene la idea de empaquetar múltiples
instrucciones en palabras largas, pero introduce mejoras que permiten mayor flexibilidad y eficiencia
en la ejecución paralela.

#### Superescalar con Planificación Dinámica (Fuera de orden)
    La arquitectura superescalar con planificación dinámica permite ejecutar instrucciones en paralelo
y fuera de orden para mejorar el rendimiento. Básicamente, es el procesador superescalar más el
algoritmo de Tomasulo modificado para finalización en orden.

Características:

      Estaciones de reserva separadas para registros de enteros y registros de punto flotante (PF).

      Se lanzan en el mismo ciclo dos instrucciones en orden (ciclo de lanzamiento: partir en dos
      subciclos).

      Solo instrucciones load para PF causan dependencias entre instrucciones enteras y PF.

      Reemplazo de buffer de carga con cola: se utiliza una cola en lugar de un buffer de carga conven-
      cional, lo que permite realizar las lecturas de datos de manera ordenada y evita la especulación
      de lectura (LDE) que podría generar problemas de dependencia de datos.

Ejecución:

      Ejecución Load: Check dirección en cola de escritura para evitar LDE.

      Ejecución Store: Check dirección en cola de lecturas para evitar EDL.

#### Especulación para Mayor Paralelismo en Procesadores Superescalares con Planificación Dinámica (Unidades Multiples + Tomasulo)
   Para obtener un mayor paralelismo, el procesador superescalar con planificación dinámica utiliza
una predicción de saltos agresiva, lo cual permite la especulación en la ejecución de instrucciones.

Especulación La especulación permite lanzar instrucciones dependientes de una predicción de salto
sin consecuencias negativas. En caso de que la predicción sea incorrecta, el procesador realiza un ”undo”
a nivel de hardware:

      HW ”undo”: Si la predicción resulta incorrecta, el hardware permite revertir la ejecución.

      Tratamiento de excepciones: Las excepciones se gestionan correctamente mediante un ROB
      (Reorder Buffer).

<!-- p. 171 -->

      Resolución de saltos: Una instrucción deja de estar en estado de especulación cuando su
      condición de salto se resuelve; en este punto, la instrucción entra en la fase de commit.

    El procesador realiza ejecución fuera de orden, pero asegura una finalización en orden de las
instrucciones, lo que garantiza la coherencia en los resultados.

#### Características
      Orden de ejecución dinámico: El procesador determina el orden de ejecución en el momento
      del lanzamiento. La planificación considera latencias variables, como los fallos de caché, para
      optimizar el rendimiento de la ejecución.

      Compatibilidad binaria: Es compatible con la ejecución de binarios existentes; sin embargo, el
      rendimiento mejora significativamente al recompilar el código para optimizar el aprovechamiento
      de las capacidades del procesador.

      Complejidad de hardware: Este tipo de procesador es muy complejo en cuanto a diseño de
      hardware, debido a la necesidad de gestionar tanto la planificación dinámica como la especulación
      y el manejo de excepciones en ejecución.

      Programa estático: Se inicia con un programa estático, es decir, un conjunto fijo de instruc-
      ciones ya cargadas en memoria.

      Búsqueda de instrucciones y predicción de saltos: El procesador busca las instrucciones
      en memoria e implementa la predicción de saltos para anticipar el flujo de ejecución, generando
      un flujo dinámico de instrucciones.

      Decodificación y renombramiento de registros: Las instrucciones se decodifican y, para
      evitar conflictos en el uso de registros, se realiza el renombramiento de registros. Este proceso
      asegura que los registros estén listos para cada instrucción sin interferencias de dependencias.

      Carga en estaciones de reserva: Las instrucciones renombradas se cargan en las estaciones
      de reserva, desde donde estarán listas para ser emitidas.

<!-- p. 172 -->

      Emisión y ejecución: Las instrucciones se emiten desde las estaciones de reserva y son ejecu-
      tadas por las unidades funcionales correspondientes.

      Escritura ordenada en el ROB: Una vez completada la ejecución, las instrucciones pasan al
      ROB (Reorder Buffer), que se encarga de gestionar el reordenamiento de resultados y asegurar
      que la escritura se realice en el orden correcto.

      Reordenamiento y finalización: Finalmente, el procesador realiza el reordenamiento necesa-
      rio y la escritura de resultados en orden, completando la ejecución de cada instrucción.

#### Pipeline del Alpha EV7 (2003)
   El Alpha 21364 (EV7) representa la culminación de la familia Alpha, integrando un pipeline
avanzado que combina el modelo clásico de 5 etapas (IF, ID, EX, MEM, WB) con técnicas dinámicas
de emisión múltiple basadas en el algoritmo de Tomasulo.

Figura 127: Pipeline del Alpha EV7 (2003), evolución del modelo IF–ID–EX–MEM–WB con Tomasulo.

      El EV7 podía emitir hasta 4 instrucciones por ciclo.

      Basado en Tomasulo, con renombre de registros, colas de emisión y ejecución fuera de orden.

      Maneja simultáneamente enteros, punto flotante y accesos a memoria con mecanismos de cohe-
      rencia y jerarquía de caché.

Etapas del pipeline

   1. Fetch (IF):

           Se obtienen hasta 4 instrucciones por ciclo desde la L1 Instruction Cache (64 KB, 2-way).
           Incluye branch predictors sofisticados y un generador de direcciones de siguiente línea
           para mantener el flujo de instrucciones.

<!-- p. 173 -->

   2. Map (ID/Rename):

              Las instrucciones se renombran a través de mapas de registros separados para enteros y
              punto flotante.
              Se resuelven dependencias falsas (WAR/WAW) mediante renombre dinámico.

   3. Issue Queue (Estaciones de Reserva – Tomasulo):

              Existen colas separadas: entera (20 entradas) y punto flotante (15 entradas).
              Aquí las instrucciones esperan a que sus operandos estén listos para poder ser emitidas.

   4. Register Read (REG):

              Acceso a los archivos de registros: 80 enteros y 72 de punto flotante.
              Este paso concreta la lectura de operandos ya disponibles o recibidos vía CDB (Common
              Data Bus).

   5. Execute (EX):

              Varias unidades funcionales enteras en paralelo.
              Unidades de coma flotante dedicadas: FP ADD/Div/Sqrt y FP MUL.
              Soporta ejecución fuera de orden con hasta 80 instrucciones en vuelo, más 32 loads y 32
              stores.

   6. Memory Access (MEM):

              Acceso a la L1 Data Cache (64 KB, 2-way).
              Interfaz con la L2 Cache unificada de 1.75 MB (7-way).
              Manejo de misses con buffers dedicados (Victim Buffer y Miss Address).

   7. Write Back (WB):

              Resultados se escriben en el archivo de registros o se transmiten a través del CDB hacia las
              colas de emisión que dependan de esos valores.

### Ejemplo ejecución para superescalar
                                                                 Operaciones en coma flotante: 3 ciclos de
                                                                 latencia

                                                                 Operaciones enteras: 1 ciclo de latencia

                                                                 Operaciones segmentadas

                                                                 Una unidad de cada tipo

                                                                 Saltos efectivos en etapa Decode (D)
   Ejecución escalar con una unidad entera y una de PF

       LD       R10, @y[0]                     ; direccion inicial del vector y a R10
       LD       R11, @u[0]                     ; Idem u
       LD       R12, @x[0]                     ; Idem x
       LD       R13, N                         ; numero de componentes a R13

<!-- p. 174 -->

     loop: LD F1, 0(R10)                 ; elemento de y a F1
           LD F2, 0(R11)                 ; elemento de u a F2
           LD F3, 0(R12)                 ; elemento de x a F3
           MULD F4, F1, F2               ; q = u * y
           MULD F5, F2, F3               ; u * x
           ADDI R11, R11, #8             ; actualiza puntero de u
           ADDD F6, F4, F3               ; y = x + q
           SUBD F7, F4, F5               ; x = q - u * x
           SD   0(R10), F6               ; almacena y
           ADDI R10, R10, #8             ; actualiza puntero de y
           SD   0(R12), F7               ; almacena x
           SUBI R13, R13, #1             ; actualiza N
           BNE loop                      ; salta a loop si R13 != 0
           ADDI R12, R12, #8             ; delay slot actualiza puntero de x

   Debido al orden de las instrucciones, no hubo mucho conflicto y el CPI es bueno. Superescalar
de 4 vías: Ejecución en orden.

<!-- p. 175 -->

 • Superescalar de 4 vías
 • Ejecución fuera de orden
 • Predicción de saltos

   Se observa que las instrucciones 6, 10, 12, 13 y 14 se ejecutan fuera de orden. Estas ins-
trucciones, al no presentar dependencias críticas y utilizar unidades funcionales de enteros, pueden
adelantarse respecto del orden original del programa.

### Límites de ILP
  El lanzamiento múltiple (ILP) permite mejorar el rendimiento sin modificar el modelo de progra-
mación. En los últimos años, el ancho superescalar de los diseños se ha mantenido igual que en 1995.

<!-- p. 176 -->

No obstante, el gap entre el rendimiento máximo teórico y el rendimiento real obtenido ha aumentado.

       ¿Es necesario desarrollar nuevos mecanismos de hardware o software para mejorar el apro-
       vechamiento de ILP?

   Actualmente, la tecnología Single Instruction Multiple Data (SIMD) se explota ampliamente
en extensiones multimedia de procesadores como:

       Intel MMX, SSE, SSE2, SSE3, SSE4

       Motorola Altivec

       SPARC, SGI, HP

   Al trabajar con vectores, SIMD permite alcanzar un speedup de aproximadamente diez veces sin
gran esfuerzo.

### ¿Cuánto ILP hay en las aplicaciones?
    La cuestión principal es si, con cierto hardware disponible en una arquitectura, es posible explotar
todo el ILP de una aplicación específica para esa arquitectura.
    Supongamos un procesador superescalar con ejecución fuera de orden, especulación y recursos
ilimitados:

       Infinitos registros para renombrado

       Predicción de saltos perfecta (sin predicciones incorrectas)

       Cachés perfectas (sin fallos de caché)

       Lanzamiento de instrucciones sin limitaciones

       Desambiguación de memoria perfecta

          ¿Hasta qué punto un procesador real se
          puede aproximar al ILP explotado por
          este procesador ideal?

   Para comparar los procesadores reales con este pro-
   cesador ideal, es esencial analizar los límites de ILP
   explotables en el software (benchmarks) evaluado
   en estos procesadores. A continuación, se analizará
   el impacto de las características del procesador en
   el IPC alcanzado, siendo estas características:

       Cantidad de instrucciones lanzadas por ciclo.

       Ventana de Instrucciones: Número de instrucciones que un procesador puede manejar en
       ejecución simultáneamente.

       Cantidad de registros para renombrado.

       Predicción de saltos.

<!-- p. 177 -->

       Caché: Tamaño, organización y políticas de reemplazo. Se busca minimizar los cache miss.
       Análisis de Memory Alias: Capacidad del procesador para determinar si dos o más accesos
       a memoria corresponden a la misma ubicación de memoria. Si se puede asegurar que no existe
       aliasing de memoria, el procesador puede maximizar el paralelismo reordenando y ejecutando
       los accesos de memoria en paralelo de manera segura.

   Luego de analizar el impacto de las distintas características para diferentes benchmarks (deter-
minando que las características realizables logran un IPC cercano al IPC ideal), se concluye que el
procesador a construir debería tener la siguiente configuración:

                            Característica                   Nuevo Modelo
                     Instrucciones lanzadas por ciclo       64 (sin restricciones)
                        Ventana de instrucciones        Infinito vs. 256, 128, 32, 16
                       Registros para renombrado               64 Int + 64 FP
                           Predicción de saltos                    1K 2-bit
                                  Caché                            Perfecto
                        Análisis de Memory Alias         Desambiguación por HW

                               Cuadro 6: Configuración del Procesador

### Thread Level Parallelism y Multithreading
#### ¿Cómo superar los límites de ILP?
   Existen varias estrategias para superar los límites del ILP:

<!-- p. 178 -->

       Mejorar compiladores e ISA: Los compiladores pueden optimizar el código para aprovechar
       mejor el paralelismo a nivel de instrucciones. Además, se pueden diseñar nuevas Instruction Set
       Architectures (ISA) que faciliten la ejecución paralela.

       Eliminar riesgos en la memoria: Los riesgos de escritura después de carga (ELD) y escritura
       después de escritura (EDE) pueden limitar el paralelismo. Se pueden implementar técnicas como
       el reordenamiento de instrucciones o el uso de buffers de registro para mitigar estos riesgos.

       Eliminar riesgos en registros y memoria mediante la predicción: Los riesgos de lectura
       después de escritura (LDE) pueden evitarse mediante técnicas de predicción de dependencias.
       Esto implica anticipar las dependencias de datos y tomar decisiones especulativas para mantener
       el flujo de instrucciones sin interrupciones.

       Explorar otros tipos de paralelismo: Además del paralelismo a nivel de instrucciones, se
       pueden buscar otros tipos de paralelismo, como el paralelismo a nivel de hilos (Thread Level
       Parallelism, TLP). Esto implica ejecutar múltiples hilos de forma concurrente para aprovechar
       aún más la capacidad de procesamiento.

   Una alternativa es buscar paralelismo a nivel de threads (TLP), ya que muchas aplicaciones (como
bases de datos y códigos científicos) se beneficiarían de esto. Además, para realizar múltiples tareas,
podemos utilizar los threads que componen un programa, evitando el cambio entre múltiples progra-
mas. Esto permite aprovechar mejor la CPU, ya que es mucho menos costoso cambiar de thread en
lugar de programa.

### Thread

Figura 128: Hilos dentro de un mismo proceso: comparten code, globals y heap, pero cada hilo posee
su propio stack y contexto (registros/PC).

<!-- p. 179 -->

    Un thread (hilo) es la unidad de ejecución dentro de un proceso. A diferencia de los procesos,
los threads de un mismo proceso comparten el mismo espacio de direcciones (code, globals, heap,
etc.), pero cada hilo mantiene su estado de ejecución propio: contador de programa (PC),
registros y su pila (stack) para llamadas y variables locales.
    Esta organización hace que crear y conmutar entre threads suela ser más liviano que entre pro-
cesos, pero requiere sincronización para acceder a datos compartidos.
    Existen mecanismos para explotar paralelismo a nivel de threads tanto en software (planificación
del SO sobre uno o más cores) como en hardware (p. ej., fine-grained multithreading y SMT ).
    Objetivo de TLP: Utilizar múltiples flujos de instrucciones para mejorar el throughput de compu-
tadoras que ejecutan muchos programas diferentes, reduciendo el tiempo de ejecución de un programa
multithreaded.
    Data Level Parallelism (DLP): Consiste en explotar paralelismo aplicando la misma operación
a múltiples elementos de datos en forma simultánea. Es el tipo de paralelismo característico del modelo
SIMD (Single Instruction, Multiple Data), donde una sola instrucción opera sobre un vector de valores
(por ejemplo, sumar varios enteros o flotantes en un único paso).
    En procesadores actuales se implementa mediante extensiones multimedia (p. ej. SSE/AVX en
x86, NEON en ARM), que utilizan registros anchos para empaquetar varios datos y procesarlos en
paralelo (SIMD “corto”). En arquitecturas vectoriales clásicas, en cambio, el hardware trabaja con
vectores de mayor longitud y amortiza mejor el costo de control, siendo muy eficiente para bucles con
muchos datos.
    El DLP es especialmente útil en aplicaciones como procesamiento de imágenes y audio, álgebra
lineal, simulaciones numéricas y machine learning, donde predominan bucles del estilo for con ope-
raciones elementales repetidas. Su rendimiento depende de factores como el ancho SIMD (cuántos
elementos se procesan por instrucción), la alineación y disposición de memoria, y la capacidad
del compilador (o del programador) para vectorizar el código. (ver Anexo 7, pág. 243)

### Diferencias entre ILP y TLP
       Instruction Level Parallelism (ILP): Explota el paralelismo implícito dentro de un segmento
       de código lineal o un bucle (en BB).

       Thread Level Parallelism (TLP): Representa el uso de múltiples threads que son inherente-
       mente paralelos.

       Eficiencia: TLP puede ser más eficaz en cuanto a costo comparado con ILP.

### ¿Por qué Multithreading?
    Cuando se trabaja con un solo thread, se pueden desperdiciar tiempo y recursos de hardware,
especialmente cuando se producen fallos en la caché y se requiere esperar a que se complete el acceso
a memoria. El multithreading permite aprovechar este tiempo desperdiciado al ejecutar otros threads
disponibles mientras se espera por el acceso a memoria.
    Observando la ocupación de un procesador superescalar de tres vías en el tiempo, se pueden ver
muchos slots libres debido a las dependencias:

                      Característica                Descripción
                           ILP         Paralelismo dentro de código lineal/bucle
                          TLP           Paralelismo mediante múltiples threads
                        Eficiencia           TLP puede ser más rentable

<!-- p. 180 -->

    En cuanto a memoria, las CPUs no se ven limitadas por la capacidad de los distintos tipos de
memoria (caché, flash, RAM, disco, etc.), sino por la velocidad de acceso a las mismas. Estas tienen
escalas de rendimiento muy distintas, donde el acceso a la memoria puede convertirse en un cuello de
botella para el procesador.

                                                    Utilizando la técnica de multithreading es posi-
                                                    ble aprovechar el tiempo que se desperdicia con un
                                                    solo thread cuando se produce un fallo de caché.
                                                    Al ocurrir esto, el procesador puede ejecutar otros
                                                    threads que estén disponibles, en lugar de esperar
                                                    a que se complete el acceso a memoria. Esto per-
                                                    mite optimizar el uso de los recursos de hardware
                                                    y reducir el tiempo total de ejecución.
   En la figura se ilustra un procesador superescalar de 3 vías (hasta 3 instrucciones por ciclo).
Los cuadrados NO rojos representan slots libres que no se pueden ocupar debido a dependencias
(entre instrucciones) y a stalls por accesos a memoria (p. ej., latencias y fallos de caché), lo que
denota una pérdida de rendimiento al desaprovechar capacidad de ejecución disponible.

### Multithreading
                                                                El multithreading es una técnica que
                                                                permite que múltiples threads compartan
                                                                unidades funcionales de un único proce-
                                                                sador de manera solapada. Para permi-
                                                                tir esto, el procesador debe ser capaz de
                                                                mantener el estado de cada thread me-
                                                                diante la replicación de estructuras, co-
                                                                mo:
      Una copia separada del banco de registros.
      Una copia separada del Contador de Programa (PC), entre otras.

    Para implementar el multithreading, el hardware debe estar preparado para realizar cambios de
thread de forma rápida. Con esta técnica se logra incrementar el trabajo procesado por unidad de
tiempo. Si los threads corresponden a la misma tarea, se reduce el tiempo de ejecución total.

### Límites del Multithreading
    Aunque el multithreading incrementa la cantidad de trabajo procesado por unidad de tiempo, no
es una técnica ideal y pueden producirse pérdidas de rendimiento. Por ejemplo, un programa puede ver
incrementado su tiempo de ejecución individual, aun cuando el número total de programas ejecutados
por unidad de tiempo aumente.

### Conmutación de Threads
   Existen dos tipos de conmutación entre threads:

      Conmutación de grano fino: el procesador alterna de thread en cada ciclo, típicamente
      siguiendo una política round-robin entre los threads listos (saltando los que estén bloqueados).
      Conmutación de grano grueso: Cuando un thread debe detenerse (por ejemplo, en caso de
      un fallo de caché).

<!-- p. 181 -->

#### Multithreading de Grano Fino
    En el multithreading de grano fino, la conmutación entre threads se produce después de cada
instrucción, generando una ejecución intercalada de los diversos threads. Esta política suele aplicarse
mediante un esquema round-robin, ignorando aquellos threads bloqueados (es decir, no considerados
en la conmutación).
    La CPU debe ser capaz de conmutar de thread cada ciclo.

      Ventaja: Puede ocultar stalls de alta y baja latencia, ya que cuando un thread está bloqueado,
      los otros threads pueden utilizar los recursos.

      Desventaja: Retarda la ejecución de cada thread individual, ya que un thread sin stall es
      retrasado debido al reparto de recursos (ciclos) entre threads.

   Ejemplo: Procesadores Niagara y Niagara 2 de SUN.

#### Multithreading de Grano Grueso
    El multithreading de grano grueso conmutará entre threads solo en caso de largos stalls, como
fallos en la caché L2.

      Ventajas:

          • No requiere una conmutación rápida entre threads.
          • No introduce retrasos innecesarios en cada thread, ya que la conmutación solo ocurre cuando
            un thread no puede avanzar.

      Desventajas:

          • No elimina stalls cortos.
          • La conmutación es costosa en términos de ciclos de reloj.
          • Al lanzar instrucciones de un nuevo thread, el pipeline debe vaciarse y luego ser llenado
            nuevamente antes de que las instrucciones comiencen a completarse.

    Debido a esta secuencia de vaciado y llenado del pipeline, los sistemas de multithreading de grano
grueso son efectivos para reducir la penalización de detenciones largas, cuando el tiempo de rellenado
del pipeline es insignificante comparado con el tiempo de detención.

#### Simultaneous Multithreading (SMT)
   Existe una variante del multithreading de grano fino que permite a un procesador superescalar
explotar Instruction Level Parallelism (ILP) y multithreading de manera combinada y eficiente. Esta
técnica se conoce como Simultaneous Multithreading (SMT).

<!-- p. 182 -->

Figura 129: En la figura se muestran distintas formas de aprovechar las vías de ejecución en un
procesador superescalar de 4 vías. Cada cuadrado representa una vía de emisión en un ciclo
de reloj. Los cuadrados en blanco son idle slots, es decir, vías desaprovechadas. En grano fino se
observa una alta conmutación de threads (cambio frecuente, típicamente ciclo a ciclo). En SMT
(Simultaneous Multithreading) se combinan instrucciones de distintos threads en el mismo ciclo para
ocupar más vías, apoyándose en ejecución fuera de orden (p. ej., Tomasulo) y un Reorder Buffer
(ROB) para mantener commit en orden. Finalmente, el multiprocesamiento se representa como
dos procesadores (cores) independientes superescalares de 2 vías cada uno, ejecutando threads
en paralelo.

Superscalar (ILP) El primer esquema (más a la izquierda) corresponde a un procesador supers-
calar de 4 vías. Esto significa que puede emitir hasta 4 instrucciones por ciclo. Sin embargo, debido
a las limitaciones del ILP de un único hilo, no siempre hay suficientes instrucciones independientes
para llenar los 4 cuadrados. En el ejemplo, el Thread 1 (verde) logra ocupar 2 vías en un ciclo, luego
solo 1, luego 2, luego 3. . . hasta que aparece un stall. El resto de los cuadrados quedan blancos (idle),
lo que representa hardware desaprovechado.

Multithreading de Grano Fino Aquí el procesador alterna entre hilos en cada ciclo: ciclo 1 ejecuta
Thread 1 (verde), ciclo 2 ejecuta Thread 2 (rojo), ciclo 3 ejecuta Thread 3 (amarillo), etc. La ventaja
es que se llenan más cuadrados de colores (menos blancos), ya que cuando un hilo está esperando,
otro se ejecuta.

Multithreading de Grano Grueso El procesador ejecuta un hilo hasta que ocurre un evento largo
(por ejemplo, fallo de caché). Entonces cambia a otro hilo. Esto reduce cambios frecuentes de hilo,
pero si el hilo activo tiene poca ILP, muchos cuadrados siguen quedando blancos.

<!-- p. 183 -->

Simultaneous Multithreading (SMT) En SMT, varios hilos pueden emitir instrucciones en el
mismo ciclo. Así, si el Thread 1 solo logra ocupar 2 vías, otro hilo puede llenar los cuadrados restantes.
El resultado es que aparecen muchos más cuadrados de colores mezclados y muchos menos cuadra-
dos blancos. Por eso, SMT es la mejor opción: aprovecha tanto ILP como TLP al mismo tiempo,
maximizando la ocupación de las 4 vías.

Multiprocesamiento En este caso, cada hilo corre en un procesador físico distinto. Todos los
cuadrados de colores corresponden a hilos ejecutándose en paralelo en diferentes núcleos. No hay
blancos, pero el costo de hardware es mayor.

Conclusión

      Los cuadrados de colores representan instrucciones de distintos hilos.

      Los cuadrados blancos son ciclos perdidos (idle slots).

      El superscalar depende solo de un hilo y deja muchos blancos.

      El multithreading ayuda, pero SMT es claramente superior: menos idle slots, más cuadrados
      de colores, mejor aprovechamiento del procesador.

    La técnica de Simultaneous Multithreading (SMT) aprovecha que los procesadores superes-
calares modernos suelen tener más unidades funcionales disponibles para uso paralelo que las que un
único thread puede utilizar.

      Planificación dinámica y renombrado de registros: Gracias a estas técnicas, múltiples
      instrucciones de threads independientes pueden ejecutarse sin preocuparse por problemas de
      dependencia, explotando Instruction Level Parallelism (ILP) y Thread Level Parallelism (TLP)
      simultáneamente.

      Soporte de hardware en procesadores superescalares fuera de orden: Los procesadores
      modernos integran mecanismos para ejecutar más de un thread, como:

        • Gran número de registros físicos: Permiten mapear los registros arquitectónicos de
          diferentes threads.
        • Renombrado de registros: Proporciona identificadores únicos para los operandos de
          cada instrucción, permitiendo mezclar instrucciones de diferentes threads sin confundir sus
          operandos. Esto asegura que las instrucciones de un thread no interfieran con las de otro.
        • Ejecución fuera de orden: Permite utilizar los recursos del procesador de forma eficaz,
          manteniendo solo una tabla de renombrado y un valor de PC por cada thread.
        • Commit independiente: Logrado mediante un Reorder Buffer (ROB) por cada thread.
          Los ROB pueden implementarse de forma:
              ◦ Lógica: Usando un puntero para el head y el tail de cada thread, creando múltiples
                listas enlazadas independientes.
              ◦ Física: Añadiendo un bit a cada registro del ROB para identificar el thread al que
                pertenece.
        • Manejo de memoria: Para evitar conflictos, puede ser necesario implementar una Trans-
          lation Lookaside Buffer (TLB) por cada thread.

<!-- p. 184 -->

      Ejecución concurrente de múltiples threads: Los threads pueden pertenecer al mismo o
      a diferentes procesos, y el sistema operativo percibe el procesador como un Symmetric Multi-
      Processing (SMP), es decir, como si hubiese múltiples procesadores. Así, el sistema operativo
      asigna instrucciones a cada thread de manera equivalente a distribuir tareas en múltiples proce-
      sadores.

### Conclusiones sobre el Límite de ILP
   Límites de la explotación del ILP e implicancias de aumentar el ancho de emisión de
instrucciones en un procesador:

      Doblar el ancho de emisión: El ancho de emisión representa la cantidad de instrucciones
      que un procesador puede emitir en un solo ciclo de reloj. Incrementar este ancho requiere que el
      procesador:

<!-- p. 185 -->

        • Tenga un mayor acceso a la memoria caché de datos.
        • Mejore la predicción y resolución de saltos condicionales.
        • Acceda y renombre un mayor número de registros.
        • Busque un mayor número de instrucciones en la caché de instrucciones.

      Estas mejoras incrementan la complejidad de diseño y aumentan significativamente el consumo
      de energía.

      Relación entre rendimiento y consumo de energía: La mayoría de las técnicas para au-
      mentar el rendimiento de un procesador también incrementan su consumo de energía, ya que
      requieren recursos adicionales (circuitos, transistores, unidades de ejecución, etc.). Sin embar-
      go, una técnica se considera eficiente en energía si el aumento en rendimiento es superior al
      incremento en consumo energético.

      Baja eficiencia en términos de energía: Las técnicas de emisión múltiple, que permiten
      emitir y ejecutar varias instrucciones en paralelo, son generalmente poco eficientes desde el
      punto de vista energético. A medida que el ancho de emisión aumenta, es difícil lograr mejoras
      significativas en rendimiento sin un consumo de energía desproporcionadamente alto.

   En resumen, las conclusiones destacan que:

      Intentar duplicar el ancho de emisión de instrucciones en un procesador conlleva un aumento
      considerable en la complejidad de diseño y el consumo de energía.

      La mayoría de las técnicas de mejora de rendimiento incrementan también el consumo de energía.

      Las técnicas de emisión múltiple son poco eficientes energéticamente, lo que subraya los desafíos
      y limitaciones de explotar al máximo el Instruction Level Parallelism (ILP) en procesadores.

<!-- p. 186 -->

                                                                           Figura 130: Resumen conceptual de la Unidad N°5: Jerarquía de Memoria
