<!-- p. 45 -->

## Unidad 2: Aspectos Básicos de la Segmentación
    Los lenguajes de las computadoras son bastante similares debido a la similitud de los conjuntos de
instrucciones. Esto se produce porque todas las computadoras están construidas a partir de tecnologías
de hardware basadas en principios similares y porque hay unas pocas operaciones básicas que todas
las computadoras deben proporcionar.
    Además, los diseñadores de computadoras tienen un objetivo común: encontrar un lenguaje que
facilite la construcción del hardware y el compilador, maximizando el rendimiento y minimizando el
costo y la energía.
    Entonces, las consideraciones decisivas en la selección de un conjunto de instrucciones son: la
simplicidad del equipo y la claridad de su aplicación a los problemas realmente importantes junto con
la velocidad de su manejo de esos problemas. Hay dos tipos de microprocesadores:
       Los microprocesadores RISC (Reduced Instruction Set Computer): Las instrucciones son
       de tamaño fijo, hay un set reducido y solamente las instrucciones LD y ST acceden a memoria.
       Disponen de muchos registros de propósito general y posibilita la segmentación y el paralelismo
       reduciendo los accesos a memoria.
       Los microprocesadores CISC (Complex Instruction Set Computer): Comprenden un set de
       instrucciones amplio y complejo, muchas de las cuales pueden acceder a memoria. Esto dificulta
       el paralelismo. Muchos procesadores CISC actuales dividen una instrucción compleja CISC en
       varias instrucciones simples de tipo RISC (microinstrucciones).

### Arquitectura MIPS-DLX
    El MIPS es una familia de microprocesadores que utiliza RISC. DLX es un tipo de arquitectura
MIPS que usa instrucciones de 32 bits. Las instrucciones DLX se pueden separar en tres tipos: tipo
R, tipo I y tipo J.
       Tipo R son instrucciones de registro puras, con un operando y tres registros contenidos en la
       palabra de 32 bits.
       Tipo I son similares, pero solo incluyen un registro y usan los otros 16 bits para almacenar
       valores inmediatos. Por último, las de
       Tipo J son saltos, conteniendo un operando y una dirección de 26 bits.
                                                                             op: Identificador de instruc-
                                                                             ción.

                                                                             Identificador de Registros.

                                                                                • rs: Id registro fuente.
                                                                                • rt: Id registro destino
                                                                                  (para tipo LOAD).
                                                                                • rd: Id registro destino.

                                                                             shamt: Cantidad de despla-
                                                                             zamiento.

                                                                             inmediato: Operando inme-
                                                                             diato.
                       Figura 23: Instrucciones DLX.
                                                                             direccion: Destino de salto.

<!-- p. 46 -->

                 Figura 24: Ilustración de los cinco modos de direccionamiento MIPS.

                                                           Operaciones LOAD y STORE
                                                                LOAD (Carga): Lee datos y los carga
                                                                en los registros del procesador.

                                                                STORE (Almacenar): Escribe datos
                                                                desde un registro en una ubicación de
                                                                memoria.

               Figura 25: Set Instrucciones MPIS

   La siguiente instrucción INTEL x86

   add r1, [r2+r3*4+60]                  // x86 (NOT MIPS) example

    El MIPS sólo permite un modo de direccionamiento bastante simple: para especificar una dirección
se puede utilizar una constante y un registro.

<!-- p. 47 -->

   Puede traducirse como
   slli r3, r3, 2             //      r3 := r3 << 2 (i.e. r3 := r3 * 4)
   add r2, r2, r3             //      r2 := r2 + r3
   lw r4, 60(r2)              //      r4 := memory[60 + r2]
   add r1, r1, r4             //      r1 := r1 + r4

   El procesador DLX tiene 32 registros (r0 , r1 , r2 ,..., r31), cada uno de los cuales tiene 32 bits de
longitud. Sin embargo, dos de estos registros están reservados para fines especiales:

      r0 siempre contiene cero. Se puede utilizar como operando de origen siempre que se necesite cero
      y los almacenamientos en él no tienen ningún efecto.

      r31 está reservado para ser utilizado por algunas instrucciones DLX (ej: JAL).

    DLX también tiene un PC (contador de programa) de 32 bits. Siempre se comienza buscando en
memoria la instrucción en la posición del PC y poniéndola en IR (registro de instrucción). Luego, se
incrementa el PC en 4 bytes. Luego, se lee el banco de registros (posiciones rs y rt) y se las escribe
en A y B respectivamente. Pueden darse cuatro cosas:

Operación Tipo R
    En una operación tipo R, se realiza una operación aritmético-lógica entre los registros A y B. El
resultado del cálculo se guarda en ALUout. Luego, el resultado se almacena en el banco de registros en
el registro indicado por rd (es decir, RW). En este caso:

      Los registros rs y rt se encuentran en RA y RB, respectivamente.

      El registro rd se encuentra en RW.

Operación Tipo I: LW (Load Literal)
    Para la instrucción LW (load literal), se calcula la dirección de memoria a partir del registro A y
el valor inmediato. El resultado de este cálculo se guarda en ALUout. Luego, se busca el dato en la
memoria en la dirección obtenida y se guarda en MDR, indicando que es un dato y no una instrucción.
Finalmente, se almacena el dato en el banco de registros en el registro indicado por rt. En este caso:

      El registro rs y el inmediato se utilizan para calcular la posición de memoria.

      El registro rt es el registro donde se guarda el dato.

Operación Tipo I: SW (Store Literal)
    Para la instrucción SW (store literal), se calcula la posición de memoria utilizando los datos en A
y el inmediato, y el resultado se coloca en ALUout. Luego, se accede a la memoria y se guarda el dato
que está en B en la posición calculada. En este caso:

      El registro rs y el inmediato se utilizan para calcular la posición de memoria.

      El registro rt contiene el valor que se desea almacenar en memoria.

<!-- p. 48 -->

Operación Tipo I: BEQ (Branch If Equal)
    Para la instrucción BEQ (branch if equal), se realiza un salto solo si A = B. Se lleva a cabo la
resta entre A y B. Si el resultado es 0 (es decir, Z = 1), se incrementa el PC en el valor del inmediato
multiplicado por 4 bytes. En este caso:

      El registro rs contiene A.

      El registro rt contiene B.

      El inmediato es el desplazamiento que se suma al PC para realizar el salto.

                                   Figura 26: Modelo 1: Ruta de datos.

     Señal          Descripción de la Señal de Control
     PCWrite        Actualiza el contador de programa (PC) con la dirección de la siguiente instrucción.
     Iord           Lee una instrucción de la memoria. Vemos si metemos otra inst (0) o la inst de salto (1)
     MemWrite       Escribe datos en la memoria.
     IRWrite        Carga la instrucción actual en el registro de instrucciones (IR).
     RegDst         Selecciona el registro de destino (RD o RS) para almacenar el resultado de una operación.
     RegWrite       Habilita la escritura en el banco de registros.
     AWrite         Escribe datos en el registro A.
     ALUSrcA        Selecciona la primera entrada de la Unidad Aritmética Lógica (ALU).
     ALUop          Especifica la operación que debe realizar la ALU.
     OutWrite       Escribe datos en la salida del procesador.
     MDRWrite       Escribe los datos del registro de datos de memoria (MDR) en la memoria.
     MemtoReg       Determina si los datos que se devolverán a un registro provienen de memoria o de ALU.
     BWrite         Escribe datos en el registro B.
     ALUSrcB        Selecciona la segunda entrada de la Unidad Aritmética Lógica (ALU).
     MemRead        Lee datos de la memoria.

<!-- p. 49 -->

   Las señales de control en los procesadores MPIS (Multiprocessor Instruction Set) se utilizan para
coordinar y controlar las operaciones internas del procesador.

#### Maquina de Estado del Controlador antes definido

      Búsqueda de instrucción (Instruction Fetch): En esta etapa, se busca la instrucción en la
      memoria. Esto se representa con la instrucción: IR ← Memoria(PC) donde PC es el contador de
      programa que apunta a la instrucción actual. Luego, el contador de programa se incrementa en
      4 para apuntar a la siguiente instrucción: PC ← PC + 4

      Decodificación y lectura de registros (Decode/Register Fetch): En esta etapa, se leen
      los registros fuente dependiendo del tipo de instrucción. Si la instrucción es de tipo R o I, se
      leerán los registros rs y rt: A ← BR(rs), B ← BR(rt).
      También se decodifica el tipo de operación para dirigir el flujo de control.

      Ejecución (Execution):

         • Para las instrucciones de tipo R (aritméticas o lógicas), se realiza la operación indicada por
           el campo funct: ALUout ← A funct B
         • Para las instrucciones de carga (lw) y almacenamiento (sw), se calcula la dirección de
           memoria sumando el valor del registro A con la extensión del inmediato: ALUout ← A +
           SignExt(immed)
         • Para las instrucciones de rama condicional (beq), se resta A de B y se comprueba si el
           resultado es cero: A − B

      Acceso a memoria (Memory Access):

         • Para las instrucciones de carga (lw), se accede a la memoria y se almacena el valor en un
           registro temporal: MDR ← Memoria(ALUout)
         • Para las instrucciones de almacenamiento (sw), el valor de B se escribe en la dirección de
           memoria calculada: Memoria(ALUout) ← B

      Escritura de resultados (Write-back):

<!-- p. 50 -->

         • Para las instrucciones de tipo R, el resultado de la ALU se escribe en el registro de destino:
           BR(rd) ← ALUout
         • Para las instrucciones de carga (lw), el valor cargado desde la memoria se escribe en el
           registro de destino: BR(rt) ← MDR

#### Etapas de una instrucción

                                  Figura 27: Etapas de la instrucción.

   1. Búsqueda de instrucción (Instruction Fetch IF) Se accede a la memoria de instrucciones
      con el valor indicado por el contador de programa (PC) y se obtiene la instrucción a ejecutar.
      El PC se actualiza con el valor de la siguiente dirección de instrucción.

   2. Decodificación de Instrucción (Instruction Decode ID) Se decodifica la instrucción y se
      accede a los registros implicados en ella. Se analizan los valores de los registros para posibles
      saltos (branches). Si es necesario, se realiza la extensión de signo del valor de offset. Además, se
      calcula la posible dirección de salto considerando el offset que se debería incrementar al PC.

   3. Ejecución de Instrucción (Execution EX) En este ciclo, la Unidad Aritmético-Lógica (ALU)
      realiza las operaciones necesarias con los operandos determinados en el ciclo anterior. Si es
      requerido, se calcula la dirección efectiva para acceder a la memoria.

   4. Acceso a Memoria (Memory Access MEM) Con la dirección efectiva calculada en el ciclo
      anterior, se accede a la memoria para realizar una operación de lectura (load) o escritura (store).

   5. Escritura (Write-back WB) Se escribe el resultado de la operación ejecutada en el registro
      correspondiente.

                                        Figura 28: Etapas de R.

<!-- p. 51 -->

                           Figura 29: Etapas de LOAD.

                           Figura 30: Etapas de STORE.

                            Figura 31: Etapas de BEQ.

<!-- p. 52 -->

#### Etapas de Instrucciones en Monociclo/Multiciclo/Segmentado
   1. Procesador Monociclo:

           En un procesador monociclo, todos los pasos necesarios para ejecutar una instrucción se
           completan en un solo ciclo de reloj.
           Desventaja: El ciclo debe durar tanto como la instrucción más larga, que en este caso es de
           45 ns. Esto provoca un desaprovechamiento del tiempo del procesador en las instrucciones
           más cortas.

   2. Procesador Multiciclo:

           En un procesador multiciclo, las instrucciones se dividen en etapas, y cada etapa se completa
           en un ciclo de reloj, que es más corto (10 ns).
           Ventaja: Se reduce el desperdicio del procesador, ya que las instrucciones más largas toman
           más ciclos y las más cortas, menos.
           Desventaja: El ciclo debe durar lo que dure la etapa más larga (10 ns), lo que implica que
           algunas etapas más rápidas desperdiciarán tiempo de procesador. Además, una instrucción
           de 5 etapas tardará 50 ns, mientras que en el monociclo solo se tardaba 45 ns.

   3. Procesador Segmentado (Pipeline):

           En un procesador segmentado, el procesador se divide en varias etapas, de modo que cada
           una de estas siempre está procesando una parte de una instrucción.
           Ventaja: Luego de los primeros 5 ciclos, se completa una instrucción por ciclo de reloj (10
           ns), optimizando el uso del procesador.

                                    Figura 32: Sistema monociclo.

                                    Figura 33: Sistema multiciclo.

<!-- p. 53 -->

    Mientras se completa una etapa de una instrucción, el hardware destinado a las otras cuatro
etapas queda ocioso. La segmentación consiste en usar ese hardware para trabajar en las etapas de
instrucciones siguientes, de manera que hay una ganancia en tiempo debida al trabajo en paralelo.

                           Figura 34: Paralelismo ideal en un sistema segmentado.
Nota: A partir del ciclo 5 el CPI es 1. Durante los primeros ciclos el CPI es mayor debido al llenado
del pipeline. Si no se presentan riesgos ni stalls, el CPI se mantiene en 1 indefinidamente, logrando el
                                          máximo rendimiento.

       Procesador Monociclo: Tiempo total = 45 ns × 100 inst = 4500 ns
       Procesador Multiciclo: Tiempo total = 10 ns × 4,6 CPI × 100 inst = 4600 ns
       Procesador Segmentado (Pipeline): Tiempo total = 10 ns × (100 + 4) inst = 1040 ns

    En un caso ideal, la segmentación puede aumentar la velocidad de ejecución hasta 4 veces en
comparación con otros métodos. Sin embargo, más adelante se demostrará que esta mejora es, en
realidad, difícil de alcanzar en la práctica.

### Pipelining o Segmentación
    La segmentación permite ejecutar varias instrucciones en un mismo ciclo (cada una en
una etapa diferente).Es una técnica de implementación de microprocesadores que permite que
múltiples instrucciones se solapen en la ejecución. Explota el paralelismo entre las instrucciones de un
flujo secuencial. A diferencia de otras técnicas para incrementar la velocidad del procesador, tiene la
ventaja sustancial de ser fundamentalmente invisible al programador. Se aprovecha el paralelismo en
las acciones necesarias para ejecutar una instrucción.
    El throughput de un pipeline se determina por cuán a menudo una instrucción abandona el pipeline.
Dado que las etapas de un pipeline son secuenciales, todas deben estar listas para poder avanzar al
mismo tiempo. El tiempo que se requiere para que una instrucción pase de una etapa del pipeline a la
siguiente se conoce como ciclo de procesador. El tiempo de duración de este ciclo estará determinado
por la etapa más lenta. Por ello, el objetivo del diseñador de un pipeline debe ser balancear las cargas
de cada etapa para equilibrar los tiempos.
    CASO IDEAL: Si todas las etapas estuvieran perfectamente balanceada, el tiempo por instruc-
cion en el pipeline es:

                                                      Tiempo por instrucción SIN pipeline
            Tiempo por instrucción CON pipeline =
                                                               Cantidad de etapas
    Consideremos el siguiente ejemplo para ilustrar el rendimiento de un pipeline: El tiempo por
instrucción sin pipeline es de 100 ns y el pipeline está dividido en 5 etapas.

<!-- p. 54 -->

    Sustituyendo los valores: Tiempo por instrucción CON pipeline = 1005 ns = 20 ns Por lo tanto, el
tiempo por instrucción utilizando el pipeline es de 20 ns.
    El speedup teórico, si el pipeline está perfectamente balanceado, sería igual a la cantidad de etapas:
    Speedup teórico = 5 ← Este valor puede disminuir en la práctica debido a factores como el balanceo
imperfecto entre etapas.
   Conflicto entre instrucciones Tipo R y LOAD

   Las instrucciones LOAD constan de 5 fases de ejecución: IF (Instruction Fetch), ID (Instruction
   Decode), EX (Execute), MEM (Memory Access) y WB (Write Back).
   Las instrucciones tipo R tienen 4 fases: IF (Instruction Fetch), ID (Instruction Decode), EXE
   (Execute) y WB (Write Back), ya que no acceden a la memoria de datos, omitiendo la etapa
   de MEM.
   Para evitar inconsistencias en la segmentación del pipeline y posibles conflictos entre las distintas
   etapas de las instrucciones, se añade una etapa adicional de MEM en las instrucciones tipo
   R. Esta etapa no realiza ninguna operación, pero garantiza que todas las instrucciones pasen
   por el mismo número de etapas, asegurando la correcta sincronización del pipeline y evitando
   conflictos.

### Limitaciones prácticas del Pipelining
   En la práctica, el pipelining no solo mejora el rendimiento al aumentar el throughput, sino que
también introduce ciertas limitaciones:

       Cada etapa del pipeline debe durar lo mismo que la etapa más lenta. En este ejemplo, aunque
       algunas etapas requieren menos tiempo, todas se ajustan al ciclo de 200 ps, que corresponde a
       la etapa de mayor duración.

       En las etapas de ID (Instruction Decode) y WB (Write Back) se produce una parti-
       cularidad: la lectura de registros (ID) ocurre en un flanco del reloj, mientras que la escritura
       (WB) ocurre en el otro flanco. Esto implica que se desperdicia medio ciclo, ya que ambas
       operaciones no pueden superponerse exactamente.

   En la Figura 35 se muestra la ejecución secuencial (arriba) frente a la ejecución con pipelining
(abajo), considerando estas limitaciones y los ciclos de reloj.

#### Problemas en Sistemas Segmentados
    Para asegurar que las instrucciones dentro del pipeline no intenten utilizar los mismos recursos al
mismo tiempo y no interfieran entre ellas, las etapas del pipeline se separan con registros de segmen-
tación (también conocidos como latches o flip-flops). Estos registros cumplen las siguientes funciones:

       Los registros de segmentación se encuentran entre cada etapa del pipeline.

       Al final de cada ciclo de reloj, los resultados de una etapa se almacenan en estos registros.

       La etapa siguiente utiliza los resultados almacenados como entradas.

       Los registros tienen nombres que corresponden a las dos etapas que separan. Por ejemplo, el
       registro de segmentación entre las etapas IF (Instruction Fetch) e ID (Instruction Decode) se
       llama IF/ID.

<!-- p. 55 -->

Figura 35: Comparación entre ejecución secuencial (arriba) y con pipeline (abajo), considerando que
todas las etapas se ajustan al tiempo de la etapa más larga y que en ID/WB se desaprovecha medio
ciclo por los flancos de reloj.

                           Figura 36: Registros de segmentación entre las etapas.

   La segmentación puede enfrentar varios riesgos que dificultan la ejecución eficiente de instrucciones.

<!-- p. 56 -->

Estos riesgos impiden que se inicie la ejecución de una nueva instrucción en cada ciclo. Los tipos de
riesgos incluyen:

       Riesgos Estructurales: Ocurren cuando dos instrucciones intentan utilizar el mismo recurso
       en el mismo ciclo.

       Riesgos de Datos:Se presentan cuando se intenta utilizar un dato antes de que esté completa-
       mente preparado, afectando el mantenimiento del orden estricto de lecturas y escrituras.

       Riesgos de Control: Surgen al intentar tomar una decisión sobre una condición que aún no
       ha sido evaluada.

   Los riesgos deben ser detectados y resueltos para asegurar una ejecución eficiente en sistemas
segmentados.

### Riegos en la Segmentación
#### Riesgo Estructural

   Una instrucción en curso no puede ejecutarse en
   el ciclo de reloj previsto debido a que el hardwa-
   re no admite la combinación de instrucciones que
   se intentan ejecutar en ese ciclo. Esto ocurre, por
   ejemplo, cuando dos instrucciones intentan utilizar
   el mismo recurso simultáneamente en el mismo ci-
   clo (Memoria, ALU o Registros).
                                                                     Figura 37: Riesgos estructurales.

Figura 38: Problema: Como tanto las instrucciones como los datos se almacenan en una única memoria
(con un solo puerto de lectura) en lugar de en dos memorias separadas, no es posible leer una instrucción
y leer un dato.

<!-- p. 57 -->

   Solución a los Riegos estructurales

         Memoria:

            1. Se utiliza una memoria para las instrucciones y otra para los datos, de manera que
               se puedan leer datos e instrucciones al mismo tiempo.

         Registros:

            1. Se emplean dos puertos de lectura en el banco de registros para poder leer dos
               registros simultáneamente.
            2. Se divide el ciclo de reloj en dos: medio ciclo para la escritura y medio ciclo para la
               lectura, de forma que se pueda leer y escribir un registro en el mismo ciclo (la lectura
               ocurre en el flanco ascendente y la escritura en el flanco descendente) (Ver figura a
               continuación).

         ALU: Sumador Agregado.

                                   Figura 39: Solución Registros (2).

   Analizando todos estos problemas, obtenemos el segundo esquema del diseño. Este diseño tiene
como objetivo evitar riesgos estructurales. Las correcciones realizadas son las siguientes:

      No es posible utilizar la ALU para actualizar el PC y, al mismo tiempo, actualizar la dirección
      para acceder al dato. Por lo tanto, se agrega un sumador en la etapa de ejecución (EX), el cual
      se encargará de actualizar el PC.

      Se separa la memoria en memoria de instrucciones (etapa de búsqueda de instrucciones, IF) y
      memoria de datos (etapa de acceso a la memoria, MEM).

<!-- p. 58 -->

                     Figura 40: Modelo 2: Ruta de Datos SIN Riegos Estructurales.

Figura 41: Modelo 2: Ruta de Datos SIN Riegos Estructurales (SIMPLIFICADO): Cada paso de la
instrucción se puede situar en el camino de datos de izquierda a derecha. Las únicas excepciones a
esta regla son la actualización del registro PC y el paso final de escritura de resultados, mostrados en
color. En este último caso, el resultado de la ALU o de la memoria de datos se envía hacia la izquierda
para ser escritos en el banco de registros. (Aunque normalmente se utilizan las líneas de color para
representar líneas de control, en este caso representan líneas de datos.).

<!-- p. 59 -->

Explicación Señales de control con modulo de Control Principal en el Modelo 2
      Selección de PC: Se requiere una señal de control para indicarle al multiplexor de la primera
      etapa qué valor asignar al PC para ejecutar la siguiente instrucción. Este valor puede ser el
      anterior incrementado en 4 bytes o la dirección obtenida por el segundo sumador, en caso de que
      se produzca un salto. Para esto, se utiliza una compuerta AND, cuyas entradas son branch (será
      1 si la operación es de tipo salto) y el flag zero (será 1 si A y B son iguales). Cuando ambas
      señales sean 1, el multiplexor tomará la salida del segundo sumador; en caso contrario, tomará
      la salida del primer sumador.

                                Figura 42: Modelo 2: Selección de PC.

      Control de ALU: Para determinar qué operación debe realizar la ALU, se analiza el campo
      function de la instrucción (los 6 bits menos significativos) y dos bits del control principal ALUop,
      obtenidos del código de operación (OP) de la instrucción. Los dos bits de ALUop indican el tipo
      de instrucción (R, LW, SW o BEQ). Si es de tipo R, se examina el campo function para definir
      la operación. Por ejemplo, si la instrucción tiene un código de operación 100011 (LW), entonces
      ALUop será 00 y el campo funct no será relevante. En cambio, si el código de operación es 000100
      (BEQ), ALUop será 01, y el valor de ALUctr será 110, como si se tratara de una resta.

Figura 43: Modelo 2: El control de la ALU se determina por ALUop (que depende del tipo de instruc-
ción) y el campo de función en las instrucciones de tipo-R.

      Selección del registro destino: En las instrucciones de tipo R, el registro destino es rd (bits
      15-11), mientras que en las instrucciones de tipo I, el registro destino es rt (bits 20-16). Para
      seleccionar el registro destino, se utiliza una señal de control regdest en la etapa de ejecución
      que se encarga de esta tarea.

<!-- p. 60 -->

                               Figura 44: Modelo 2: Control principal.

      Las señales de control que se obtienen de la instrucción en la etapa ID pueden ser requeridas
      en etapas posteriores, por lo que se transmiten a través del pipeline mediante registros. De esta
      manera, para una misma señal de control, existen múltiples variantes según la etapa en la que
      se encuentren. Ejemplo: Write_Reg_ID, Write_Reg_EX, Write_Reg_MEM, Write_Reg_WB.

                                                        Observe que cuatro de las nueve líneas de control
                                                        se usan en la etapa EX, mientras que las cinco
                                                        restantes pasan al registro de segmentación EX/-
                                                        MEM, que ha sido extendido para poder almace-
                                                        nar las líneas de control. Tres se usan durante la
                                                        etapa MEM, y las dos últimas se pasan al registro
                                                        MEM/WB para ser usadas en la etapa WB.

         Figura 45: Modelo 2: Control principal.

#### Riesgos de Datos
    Provienen de dependencias de datos entre instrucciones (una instrucción necesita como dato el
resultado de una instrucción anterior). Es decir, se intenta utilizar un dato que todavía no está pre-
parado.
    Los riesgos de datos ocurren cuando, debido a la
    segmentación, el orden de lectura de los operandos      #       Ejemplo         Riesgo
    y la escritura de resultados se modifica respecto al            ADD   r1,r2,r3  r1 se lee antes de
                                                            LDE
    especificado por el programa. Se produce un riesgo              ADD r4,r1,r2 que lo escriba
    si existe dependencia entre instrucciones que se eje-           ADD r1,r4,r3 r4 se escribe antes de
                                                            EDL
    cutan concurrentemente. Dependiendo del tipo de                 ADD r4,r1,r2 que lo lea
    segmentación, el riesgo puede ocurrir o no. Existen             ADD r4,r2,r3 Si la 2ª instrucción
                                                            EDE
    tres tipos diferentes de riesgos de datos:                      ADD r4,r1,r2 ocurre primero

      Lectura después de escritura (LDE): Se produce un riesgo si un registro se lee antes de que
      se complete la escritura de dicho registro por una instrucción anterior.

<!-- p. 61 -->

      Escritura después de lectura (EDL) o antidependencia: Se produce un riesgo si un registro
      se escribe antes de que se complete la lectura de dicho registro por una instrucción anterior. Este
      tipo de riesgo aparece únicamente en arquitecturas con ejecución fuera de orden.

      Escritura después de escritura (EDE) o dependencia de salida: Se produce un riesgo si
      un registro se escribe antes de que se complete la escritura de dicho registro por una instrucción
      anterior. Al igual que la antidependencia, solo resulta problemático en ejecución fuera de
      orden.

   Teorema de Riego de Datos

   Considere dos instrucciones i y j, donde i precede a j. Definimos el Dominio (D) como
   los operandos de la instrucción y el Rango (R) como el resultado de la instrucción. Los
   riesgos de datos se identifican según las siguientes intersecciones: Riesgo de Lectura Después
   de Escritura (EDL) (WAR) ocurre si D(i) ∩ R(j) ̸= ∅, indicando que los operandos de i
   interfieren con el resultado de j; Riesgo de Lectura Después de Escritura (LDE) (RAW)
   ocurre si R(i) ∩ D(j) ̸= ∅, indicando que el resultado de i interfiera con los operandos de j; y
   Riesgo de Escritura Después de Escritura (EDE) (WAW) ocurre si R(i) ∩ R(j) ̸= ∅,
   indicando que el resultado de i interfiera con el resultado de j.
   Consideración de No Riesgo ocurre si D(i) ∩ D(j) ̸= ∅, indicando que no hay interferencia
   entre los operandos de i y j;

   En una asignación, como por ejemplo a = b + c, el dominio corresponde a los operandos (en este
caso, b y c, que están en la derecha de la ecuación), mientras que el rango es el resultado (en este
caso, a, que está en la izquierda de la ecuación).
    Los problemas de (EDL) y (EDE) se solucionan debido a que la etapa de escritura (WB) es siempre
la última etapa en la ejecución de una instrucción. Esto asegura que la escritura del resultado ocurra
en un ciclo de reloj posterior, y no de manera simultánea con otras operaciones, evitando así conflictos
en el acceso a registros.
   La estructura presentada en la figura 40, es vulnerable a los riesgos de Datos antes enunciados.

Concatenación de Instrucciones con Riesgo de Datos
   Consideremos el siguiente orden de ejecución del programa (en instrucciones):

     SUB r2, r1, r3 → AND r12, r2, r5 → OR r13, r6, r2 → ADD r14, r2, r2 → SW r15, 100(r2)

    En este caso, el valor del registro r2 solo se actualizará al finalizar la etapa de WB (Write Back).
Por lo tanto, cualquier ciclo anterior a esta etapa tendrá versiones desactualizadas de r2, lo que
provoca problemas de acarreo. Las instrucciones AND r12, r2, r5 ; OR r13, r6, r2 y ADD r14,
r2, r2 utilizarán valores incorrectos de r2, y solo en la instrucción siguiente a la ADD se refleja el
valor actualizado en ese momento. Sin embargo, este valor ya será incorrecto, ya que las instrucciones
anteriores no ejecutaron correctamente debido a la desactualización del registro.Todo esto se refleja
en la siguiente figura:

<!-- p. 62 -->

                Figura 46: Concatenación de Instrucciones con Riesgo de Datos (LDE).

    SOLUCIÓN? El forwarding: El problema surge en el ciclo 5, cuando el dato está disponible,
pero aún no ha sido actualizado en el banco de registros (etapa WB). Para solucionar esto, se puede
emplear un cortocircuito que envíe el resultado directamente desde la primera ALU (en la etapa EX)
hacia las siguientes ALUs de las otras instrucciones. Esto se logra añadiendo un multiplexor adicional,
que permitirá seleccionar entre el dato del banco de registros o el dato recién calculado en la etapa
EX, de modo que las instrucciones posteriores utilicen el valor actualizado antes de que se complete el
ciclo de escritura en WB.
    La solución principal para resolver los riesgos de datos es que no es necesario esperar a que una
instrucción se complete por completo antes de intentar resolver dichos riesgos. En una instrucción, tan
pronto como la ALU produce un resultado, este puede ser utilizado por la siguiente instrucción, si es
necesario. Esto se representa en la siguiente figura:

Figura 47: Cortocircuito. Enviar el dato a las etapas que lo necesitan, cuanto esta listo. Se pueden
ejecutar todas las instrucciones sin problemas

<!-- p. 63 -->

    Este enfoque se denomina anticipación de resultados (forwarding) o realimentación (bypas-
sing), y consiste en el uso de hardware adicional que permite anticipar el dato buscado mediante los
recursos internos del procesador. Así, el resultado calculado por la ALU se redirige directamente a las
instrucciones que lo requieran, evitando retrasos en la ejecución debidos a la espera de actualización
del banco de registros.

¿Cómo implementar el forwarding?
   Para implementar la anticipación de resultados, se añaden dos multiplexores a la entrada de la
ALU junto con un control adecuado para detectar dependencias de datos y anticipar los resultados
cuando sea necesario.
   El primer multiplexor recibe tres posibles entradas:

      El registro A proveniente de la etapa anterior.

      El resultado de la instrucción anterior a la salida de la ALU.

      El resultado de la instrucción anterior de la anterior a la salida de la memoria.

    El segundo multiplexor recibe estas mismas señales, pero en relación con el registro B. La selección
de las entradas adecuadas de los multiplexores se gestiona mediante una Unidad de Cortocircuito,
que decide cuál entrada utilizar.
    La Unidad de Cortocircuito es esencial para gestionar los riesgos de datos, especialmente en
instrucciones de tipo R. Si ocurre un riesgo de lectura después de escritura (LDE), se debe
cortocircuitar la salida de la ALU (de la primera instrucción) con la entrada de la ALU (de la segunda
instrucción).

                             Figura 48: Implementación del cortocircuito.

<!-- p. 64 -->

   Por otro lado, en situaciones de Load-Use Hazard, cuando una instrucción LW es seguida por
una instrucción de tipo R, es necesario cortocircuitar la salida de la memoria (de la instrucción LW)
con la entrada de la ALU (de la segunda instrucción).
   Para realizar este control, la Unidad de Cortocircuito necesita la siguiente información, que se
almacena en los registros de segmento hasta la etapa EX:
      El registro que se escribe en la instrucción anterior (rd en el tipo R, y rt en el tipo I).
      Los registros que se leen en la nueva instrucción (rs y rt).
      La señal de control Write_Reg, que indica si la instrucción va a escribir en un registro (es decir,
      si es de tipo R o tipo I como LW).
    Como se puede observar, incluso adelantando el resultado mediante la anticipación de resultados
(forwarding), existe una dependencia hacia atrás en el tiempo entre la primera y la segunda instrucción.
    En el caso de la instrucción LW r1, 0(r2), el valor de r1 no estará disponible hasta la cuarta etapa
(MEM), ya que el dato se obtiene de la memoria. Sin embargo, la segunda instrucción, que depende de
ese dato, lo necesitará en su segunda etapa (EX).
    Este tipo de dependencia no puede ser resuelto por la Unidad de Cortocircuito, ya que el dato
aún no ha sido recuperado de la memoria cuando la segunda instrucción lo requiere. Como resultado,
la segunda instrucción deberá esperar un ciclo de reloj antes de poder continuar su ejecución. Esta
espera se conoce como stall o burbuja, y es necesaria para evitar la lectura de datos incorrectos.
   Nota:
   Introducir una burbuja no es lo mismo que una instrucción NOP. Una instrucción NOP se
   traslada a través de todas las etapas del pipeline, resultando en que no se haga nada en cada
   una de ellas. Introducir una burbuja en cambio consiste en que una etapa no haga nada durante
   un ciclo para que las otras puedan producir los resultados que necesita la instrucción siguiente
   a tiempo.

Figura 49: Caso del Load: No se puede resolver con el cortocircuito. La instrucción dependiente del
Load debe esperar un ciclo. Como la dependencia entre la carga y la instrucción siguiente (and) va
hacia atrás en el tiempo, este riesgo no puede ser resuelto mediante la anticipación de datos. Por tanto,
esta combinación debe resultar en un bloqueo generado por la unidad de detección de riesgos.

<!-- p. 65 -->

Solución para Riegos de Datos
    Además de una unidad de anticipación de datos, es necesaria una Unidad de Detección de
Riesgos (Hazard Detection Unit) para evitar conflictos en el pipeline. Esta unidad debe operar du-
rante la etapa ID, de manera que pueda insertar un bloqueo entre una instrucción de tipo load y la
instrucción que dependa de su resultado.
    El control para la detección de riesgos en el caso de una instrucción load se realiza evaluando las
siguientes condiciones:

   1. La señal de control memRead de la instrucción anterior.

   2. El registro rt de la instrucción anterior, que indica dónde se almacena el resultado de la instruc-
      ción load.

   3. Los registros rs y rt de la instrucción actual (en la etapa ID).

   ¿Bloquear el pipeline por un ciclo?

   Si se cumple la condición: Mem_Read_EX && ((rt_EX == rs_ID) || (rt_EX == rt_ID))) entonces
   se debe bloquear el pipeline por un ciclo.

    La primera parte de la condición comprueba si la instrucción anterior es una carga (load), ya que
es la única instrucción que lee de memoria. Las siguientes partes verifican si el registro destino (rt) de
la carga en la etapa EX coincide con cualquiera de los dos registros fuente de la instrucción actual en
ID. Si la condición se cumple, la instrucción actual se bloquea por un ciclo.

    Manejo del bloqueo en el pipeline: Cuando la instrucción en la etapa ID se bloquea, también
debe bloquearse la instrucción en la etapa IF, ya que de no hacerlo, se perdería la instrucción que
se está recuperando de memoria. Para bloquear estas dos instrucciones, es necesario impedir que
cambien los valores del contador de programa (PC) y el registro de segmentación IF/ID. Si estos
valores no cambian, la instrucción en la etapa IF seguirá leyendo de memoria usando el mismo valor
de PC, y los registros en la etapa ID se volverán a leer utilizando los mismos campos de instrucción en
el registro IF/ID.
    En cuanto a la mitad posterior del pipeline (a partir de la etapa EX), lo que se hace es ejecutar
instrucciones que no tienen efecto (nop). Esto se logra poniendo a 0 los campos de control de las etapas
EX, MEM y WB en el registro de segmentación ID/EX. Estos valores de control se propagan hacia adelante
en cada ciclo con el efecto deseado: si los valores de control son todos 0, no se escribirá en memoria ni
en registros.
    La señal Stall activada en 1 detiene el avance del PC, IF/ID e ID/EX, permitiendo que el pipeline
se sincronice adecuadamente.

                             Figura 50: Manejo del bloqueo en el pipeline.

<!-- p. 66 -->

    Este caso corresponde a un hazard de tipo load-use, ya que el dato cargado por LW recién está
disponible al final de la etapa MEM, mientras que la SUB lo requiere al inicio de la etapa EX en el ciclo
siguiente.
    Incluso aplicando técnicas de forwarding, este riesgo persiste y requiere la inserción de al menos
un ciclo de burbuja o la reordenación de instrucciones independientes para evitar el conflicto.

                      Figura 51: Modelo 3: Ruta de Datos SIN Riesgos de Datos.

#### Riesgos de Control
    Surgen de la necesidad de tomar decisiones en cuanto a realizar o no realizar saltos, basadas en los
resultados de una instrucción, mientras otras instrucciones se están ejecutando en el pipeline. Estos
riesgos se presentan específicamente en las instrucciones de salto condicional (branch).
    Cuando se lee una instrucción de salto condicional desde la memoria de programa, se desconoce
cuál será la siguiente instrucción a ejecutar, debido a que:
      El salto puede producirse o no en función de la comparación de los operandos de la instrucción.
      Esta información no está disponible de forma inmediata en la siguiente etapa de IF del pipeline.

      En caso de que el salto ocurra, la dirección efectiva del salto (la dirección en memoria de
      programa donde debe leerse la siguiente instrucción) también debe calcularse usando el offset
      de la instrucción, lo cual tampoco está disponible durante la etapa de IF.
    Esto implica que se debe detener el pipeline durante tres ciclos para asegurar la ejecución en
el orden correcto, lo cual representa una pérdida significativa de rendimiento (incluso mayor que la
pérdida provocada por los riesgos de datos). Para realizar un salto, es necesario:
      Tener la dirección de salto calculada

      Conocer si se cumple la condición para saltar

<!-- p. 67 -->

   El riesgo surge porque:
      En la ruta de datos que hemos analizado, ambos datos se calculan durante la ejecución.
      Si el salto es válido, la dirección del salto se carga en el PC durante la etapa de Memoria (Mem).

Manejo de los Riesgos de Control
    OPCIÓN I: Una opción para manejar los riesgos de control es bloquear o detener el pipeline
(stall) hasta que se conozca cuál será la siguiente instrucción que se debe leer en la memoria durante
la etapa de IF. En otras palabras, se debe bloquear el pipeline hasta que se haya calculado la dirección
de salto y se haya tomado la decisión de si el salto debe realizarse o no.
    Como la dirección efectiva del salto (el nuevo valor para el PC) se obtiene al final de la etapa MEM,
esto implica detener el pipeline durante tres ciclos de reloj.

                           Figura 52: detener el pipeline durante tres ciclos de reloj.
    Sin embargo, este proceso es demasiado lento, lo que contradice el objetivo de incrementar el
throughput mediante la segmentación. Tres ciclos de reloj por salto representan un tiempo excesivo
perdido. Por lo tanto, es crucial reducir la penalización por saltos (es decir, la cantidad de ciclos en
los que se detiene el pipeline). Esto se puede lograr de las siguientes maneras:

Obtener la Comparación de Operandos y la Dirección de Destino con Anticipación
    OPCIÓN II (Branch Delay Slot): No es necesario que la comparación de los operandos, para
tomar la decisión de salto, se realice en la ALU durante la etapa EX. Si se añade un comparador en
la etapa ID, el resultado estaría disponible dos ciclos antes, lo que permitiría reducir la detención del
pipeline (introducción de una burbuja) a solo un ciclo.

<!-- p. 68 -->

Figura 53: En vez de meter 3 burbujas (perder 3 ciclos). Calculo antes la evaluación y condición. Sólo
hay que esperar un ciclo para saber la instrucción que sigue a la de salto.

   De manera similar, se puede agregar hardware para calcular
   la dirección de destino en la etapa ID. Dado que en el registro
   IF/ID ya se dispone del valor del PC y del campo inmediato,
   basta con incorporar un sumador en la etapa ID para realizar
   este cálculo.

                       Figura 54: Implementar la solución II (Branch Delay Slot)

OPCIÓN III : Predicciones de Saltos
 Riesgos de Control según los Tipos de Saltos
Condicionales / Incondicionales
      Condicionales:

        • Se necesita predecir tanto la decisión como el objetivo del salto (la dirección a la que se
          debe saltar).
        • La dirección real sólo se conoce después de ejecutar la instrucción.
        • Una predicción incorrecta provoca un vaciado total del cauce (flush), descartando las ins-
          trucciones que se están buscando y decodificando en ese momento. Esto se logra poniendo
          las señales de control a cero en las etapas IF, ID y EX.
        • Condicionales directos (70 % de todos los saltos):
              ◦ Son muy frecuentes.
              ◦ La penalización por una predicción incorrecta de la dirección es alta (vaciado completo).
              ◦ Es crucial predecir correctamente la dirección del salto condicional.
              ◦ Dependen de los flags de estado: overflow, signo, cero, paridad, acarreo, auxiliar.
              ◦ La dirección objetivo se conoce en la etapa de descodificación.

<!-- p. 69 -->

              ◦ Es relativa al puntero de instrucción de la instrucción de salto.
        • Condicionales indirectos:
              ◦ Muchas arquitecturas no los implementan.

      Incondicionales:

        • Sólo se necesita predecir el objetivo del salto.
        • Incondicionales directos:
              ◦ Se efectúan siempre.
              ◦ La dirección objetivo se conoce en la etapa de descodificación.
              ◦ Son menos frecuentes y la penalización por redirección errónea es baja (vaciado parcial).
              ◦ Una predicción incorrecta tiene menor importancia.
        • Incondicionales indirectos:
              ◦ La dirección objetivo es el valor de un registro, por lo que se conoce en la etapa de
                ejecución.
              ◦ Los returns son saltos incondicionales indirectos.
              ◦ Las calls también pueden ser incondicionales indirectos.
              ◦ Son poco frecuentes, pero la penalización por predicción errónea es alta (vaciado com-
                pleto).
              ◦ A veces es importante predecirlos correctamente.

      Directos:

        • El objetivo del salto está especificado dentro de la instrucción (como un valor inmediato).
        • La dirección objetivo real se conoce después de la etapa de descodificación.
        • Una predicción incorrecta origina un vaciado parcial del cauce (flush).

      Indirectos:

        • La dirección objetivo debe ser calculada.
        • La dirección objetivo real se conoce después de la etapa de ejecución.
        • Una predicción incorrecta provoca el vaciado total del cauce (flush).

Salto Retardado
    Otro esquema de manejo de saltos consiste en retardar el salto una instrucción. Esto implica que,
después de la instrucción de salto, se genera un ciclo de retardo (delay slot), en el cual generalmente
se ejecuta la instrucción siguiente al salto, independientemente de si el salto se realiza o no. De esta
manera, se consigue el tiempo necesario para obtener el resultado de la decisión del salto.
    Nota: La instrucción en el delay slot no debe tener dependencia alguna con la instrucción de salto.
Es responsabilidad del compilador buscar instrucciones válidas y útiles para rellenar estos delay slots.
Si no se encuentran instrucciones útiles, se utilizan NOP (penalización de un ciclo).
    Existen tres tipos de decisiones que el compilador puede tomar para rellenar el delay slot:

   1. Rellenar con alguna instrucción independiente anterior al salto. Esta es la mejor opción.

   2. Rellenar con alguna instrucción ubicada en el destino del salto (suponer salto tomado). Útil en
      bucles.

<!-- p. 70 -->

   3. Rellenar con alguna instrucción que siga al salto (suponer que el salto no fue tomado). Útil en
      condiciones IF-ELSE.

Figura 55: Instrucción NO dependiente de salto. Si es posible encontrarla, 0 ciclos de penalización.
Caso contrario, 1 ciclo de penalización.

                                     Figura 56: Tipos de Saltos.

Predicciones de Saltos y Tipos
      Para disminuir el efecto sobre las prestaciones debido a los riesgos de control, se utiliza la
      predicción de saltos.
      En la etapa IF (Instruction Fetch), es necesario predecir tanto la dirección como el objetivo del
      salto.

<!-- p. 71 -->

      La predicción puede ser:

         • Estática: Siempre se predice si el salto será efectuado o no. Si la predicción es falsa, la
           instrucción siguiente se aborta (se cambia por NOP)
         • Dinámica: La predicción se basa en la historia previa del salto.

Predicción Estática
   Se tiene una predicción de salto siempre tomado o una predicción de salto nunca tomado. La
complejidad de esta propuesta radica en saber determinar cuándo la predicción falla y qué se debe
hacer para revertir los cambios.
   Si se elige una predicción de salto nunca tomado, se continúa la búsqueda de la siguiente instrucción
como si la instrucción de salto no tuviera nada en especial. Luego, si la etapa ID determina que la
predicción falló, es decir, que el salto debería haberse tomado, se debe convertir la instrucción buscada
en una NOP (Flush) y realizar la búsqueda de la instrucción indicada por el salto.
   Por el contrario, si se predice que el salto siempre es tomado, como no se puede conocer la dirección
de salto antes de la etapa ID, no se tienen ventajas y se genera la misma situación que con las
detenciones del pipeline.
   En este esquema, el compilador puede mejorar el rendimiento organizando el código de manera
que la decisión más frecuente coincida con la decisión implementada en el hardware.

                           Figura 57: Predicción estática, salto NUNCA tomado.

#### Predicción Dinámica
    Con pipelines más profundos (mayor número de etapas), la penalización en ciclos de reloj por
fallos en la predicción de saltos es mayor. Esto significa que la predicción estática ya no es suficiente
para obtener buenas prestaciones en el pipeline. Para mejorar el rendimiento, es posible predecir el
comportamiento de los saltos en tiempo de ejecución, utilizando la información generada durante la
ejecución del programa. Esta técnica se denomina predicción dinámica de saltos.

      Una estrategia común consiste en observar si el salto fue tomado la última vez que se ejecutó
      la instrucción. Si fue tomado, se busca la siguiente instrucción en la misma dirección que la vez
      anterior.

      Para implementar esta estrategia, se puede utilizar un búfer de predicción de saltos o una
      tabla de historia de saltos. Estas estructuras son memorias pequeñas indexadas con la parte
      menos significativa de la dirección de la instrucción de salto. Cada entrada contiene un bit que
      indica si el salto ha sido recientemente tomado o no.

      Aunque no se sabe con certeza si la predicción es correcta, la predicción se realiza como una
      apuesta basada en la historia previa del salto.

   Funcionamiento del Búfer de Predicción de Saltos:

<!-- p. 72 -->

      Al predicir que un salto será tomado, la búsqueda de la siguiente instrucción se inicia en la
      dirección predicha.

      Si la predicción resulta incorrecta (es decir, si el salto no fue tomado como se esperaba), las
      instrucciones predichas incorrectamente son descartadas (vaciamiento de cauce, o flush).

      El bit de predicción en el búfer se invierte y se guarda nuevamente en la tabla para futuras
      predicciones.

   Consideraciones:

      Los saltos tienden a ser consistentes, especialmente en el caso de bucles, condiciones de error o
      el tratamiento de casos límite.

      La idea central de la predicción dinámica es predecir si un salto será efectuado o no en función
      de su historia previa.

      Una vez que el salto es descodificado, la búsqueda continúa por uno de sus posibles caminos.

      En caso de una predicción incorrecta, es necesario vaciar las instrucciones del camino incorrecto
      y seguir por el camino correcto, lo que impacta negativamente en las prestaciones.

      El impacto de los errores de predicción depende de la profundidad de la segmentación del pipeline
      y de la frecuencia de las instrucciones de salto.

                     Figura 58: Modelo 4: Ruta de Datos SIN Riesgos de Control.

<!-- p. 73 -->

Pérdida de Rendimiento y Cálculo del CPI
    El CPI ideal (Ciclos por Instrucción) es de 1, lo que representa un pipeline funcionando sin
interrupciones. Sin embargo, cuando el pipeline se detiene debido a instrucciones de salto, se producen
pérdidas de rendimiento. Estas pérdidas se reflejan en un aumento del CPI real, que se calcula
sumando la penalización media por instrucción debido a los saltos.

      En un programa típico, aproximadamente el 30 % de las instrucciones son saltos. Cada salto
      introduce una penalización en el pipeline.

      El CPI real puede expresarse como:

                           CP Ireal = CP Iideal +       Penalizacióninstr × Frecuenciainstr                  (5)
                                                    X

      Para las instrucciones de salto, esto se traduce en:

                                          CP Ireal = 1 + (1 × 0,3) = 1,3                                     (6)

      Esto significa que, en promedio, cada instrucción en el programa sufre una penalización de 0.3
      ciclos debido a los saltos.

      Costo de los Saltos: Con un 30 % de instrucciones de salto, la penalización media por instruc-
      ción es de 1 ciclo por salto multiplicado por su frecuencia de aparición, es decir:

                              Penalización media por instrucción = 1 × 0,3 = 0,3                             (7)

Cálculo del Speedup
    El speedup es una medida utilizada para evaluar la eficiencia de la segmentación del pipeline. Se
define como la relación entre el tiempo de ejecución de un programa sin segmentación y el tiempo de
ejecución del mismo programa con segmentación.

                                              Tiempo sin segmentación
                                  Speedup =                                                                  (8)
                                              Tiempo con segmentación
  Sustituyendo los valores, el cálculo del speedup para un pipeline segmentado con 5 etapas y un
CPI real de 1.3 se obtiene con la siguiente fórmula:

                                    Número de Instrucciones × Número de Etapas
                       Speedup =                                                                             (9)
                                         Número de Instrucciones × CP I
   Dando como resultado:
                                          Speedup =          = 3,84                                         (10)
                                                         1,3

Impacto en el Rendimiento con los Riesgos de Control
    El impacto de las instrucciones de salto genera una pérdida de rendimiento del 24 % con respecto
al caso ideal:
                                     Speedup real     3,84
                                                    =      = 0,76                               (11)
                                     Speedup ideal     5
    En caso de implementar técnicas como el salto retardado, la pérdida de rendimiento es conside-
rablemente menor, ya que se permite ejecutar una instrucción en el delay slot, mitigando el impacto
del salto en el pipeline.

<!-- p. 74 -->

   Resumen del Procesador Segmentado

         Todas las instrucciones tienen igual duración.

         Rendimiento ideal: se ejecuta una instrucción por ciclo, con un CPI = 1.

         Los riesgos estructurales y de datos (EDE y EDL) se resuelven por construcción.

         Los riesgos de tipo LDE en las instrucciones tipo-R se solucionan mediante cortocircui-
         to.

         Los riesgos LDE en instrucciones de load implican paradas del procesador. Aquí el com-
         pilador ayuda planificando las instrucciones.

         Los riesgos de control, como las paradas y los saltos retardados, se resuelven con la ayuda
         del compilador.

   Importante: Las instrucciones comienzan y terminan en orden.

       Instrucciones con diferentes duraciones:

        • ¿Qué ocurre si las instrucciones tienen diferentes duraciones?
        • Esto es particularmente relevante en las instrucciones de aritmética en punto flotante.

### El control y los Salto Asíncronos
    Una de las partes más problemáticas del control en un procesador es la implementación de excep-
ciones e interrupciones. Ambas hacen referencia a eventos que, al igual que los saltos, alteran el flujo
normal de ejecución de las instrucciones.
    Las interrupciones y excepciones se crearon para manejar eventos inesperados que afectan la eje-
cución del programa. A continuación se detalla la diferencia entre ellas según la convención del MIPS:

       Excepciones:

        • Se refiere a cualquier cambio inesperado del flujo de control, sin distinguir si la causa es
          interna o externa.
        • Son sincrónicas y se producen debido a causas internas como desbordamiento aritmético,
          errores de acceso a memoria (fallos de página), o violaciones de protección.
        • Se deben manejar al instante, cortando la ejecución de la instrucción actual y guardando el
          contexto del programa al momento de la excepción. Luego, se puede recuperar el contexto
          y continuar desde el punto del fallo.

       Interrupciones:

        • Se refiere a eventos externos que interrumpen el flujo de ejecución del programa, como
          solicitudes de dispositivos de entrada/salida (E/S).
        • Son asíncronas y pueden ocurrir entre instrucciones.
        • Cuando ocurren, se vacía el pipeline y se introducen instrucciones NOP. El PC se almacena
          con la dirección de la interrupción.

<!-- p. 75 -->

Características y Manejo
      Síncronas vs Asíncronas:

         • Las excepciones son síncronas, ya que ocurren en sincronía con la ejecución de instrucciones.
         • Las interrupciones son asíncronas, ya que ocurren independientemente de la ejecución del
           programa.

      Solicitadas vs Generadas por el Programa:

         • Las interrupciones externas son solicitadas por dispositivos externos.
         • Las excepciones (o trampas) son generadas por el propio programa o el procesador en
           respuesta a errores internos.

      Manejo de Excepciones:

         • Las excepciones deben ser manejadas cuidadosamente para evitar la pérdida de datos.
         • Un ejemplo es el fallo de página, que puede ocurrir en medio de una instrucción y debe ser
           tratado de manera que permita recomenzar la ejecución correctamente.
         • Para las excepciones, se introduce una instrucción de trap en la etapa IF, se anulan las
           escrituras de la instrucción que causó la excepción y se guardan las instrucciones siguientes
           hasta la etapa MEM. Luego, se pasa a la rutina de gestión de excepciones.
         • Se requiere que todas las instrucciones anteriores a la excepción se completen correctamente,
           la instrucción que produjo la excepción debe ser tratada, y las instrucciones siguientes deben
           considerarse como si no hubieran comenzado.

#### Excepciones en el MPIS-DLX

            Figura 59: Maquina de Estado del Controlador antes definido CON INT/EXC.

<!-- p. 76 -->

      IF (Instruction Fetch): Fallo de página de instrucción, acceso no alineado, violación de pro-
      tección.

      ID (Instruction Decode): Instrucción ilegal.

      EX (Execution): Excepción aritmética.

      MEM (Memory Access): Fallo de página de datos, acceso no alineado, violación de protección.

      WB (Write Back): Ninguna.

   En los estados 0, 1 y 7, se involucra el manejo de excepciones de la siguiente manera:

      Se guarda en el PC el valor de la instrucción anterior que no ha terminado de ejecutarse.

      Se coloca en el PC la dirección de la rutina de excepción.

      Se almacena la causa de la excepción.

      Interrupciones:

        • Se debe esperar a que se termine de ejecutar la instrucción actual.
        • Una vez finalizada la instrucción, se guarda el PC con la dirección de la siguiente instrucción
          a ejecutar.
        • Se transfiere el control a la rutina de interrupción.

    NOTA: Si las excepciones no se consideran adecuadamente durante el diseño de la unidad de
control, intentar incorporarlas posteriormente a una implementación compleja puede reducir signifi-
cativamente el rendimiento y complicar el diseño.

Flujo de manejo de excepciones en un pipeline
   El proceso completo que sigue el procesador y el sistema operativo cuando ocurre una excepción
puede resumirse en los siguientes pasos:

   1. Detección de la excepción: El pipeline detecta la instrucción con fallo.

   2. Inserción de instrucción de trap: Se fuerza la inserción de una instrucción especial de trap
      en la próxima etapa IF.

   3. Bloqueo de escrituras: Hasta que el trap sea tomado, se desactivan todas las escrituras de la
      instrucción con fallo y de todas las posteriores en el pipeline. Esto se logra colocando ceros en
      los registros intermedios (pipeline latches).

   4. Guardar la dirección de la instrucción responsable: La dirección de la instrucción que
      causó la excepción se almacena en el EPC (Exception Program Counter).

   5. Transferencia de control: El control del procesador se transfiere a una dirección específica
      del sistema operativo encargada de manejar excepciones.

   6. Acción del sistema operativo: La rutina de excepción del sistema operativo toma control y
      puede:

           Proveer un servicio al programa de usuario.

<!-- p. 77 -->

           Responder al error (ej. un desbordamiento) con una acción predefinida.
           Parar la ejecución del programa.
           Mostrar un mensaje de error.

   7. Guardar estado adicional: El sistema operativo guarda inmediatamente el valor del PC de
      la instrucción con fallo, para asegurar un retorno correcto.

   8. Resolución de la excepción: Dependiendo de la acción tomada:

           Finalizar el programa, si la excepción es irrecuperable.
           Continuar la ejecución del programa, usando el valor almacenado en el EPC para
           retomar la ejecución en el punto correcto.

   Para que el sistema operativo trate correctamente una excepción, necesita saber tanto la instrucción
que la causó como la razón por la cual se produjo. Existen dos métodos principales para comunicar la
causa de una excepción:

      Registro de Causa (MIPS): En la arquitectura MIPS, se utiliza un registro de estado llamado
      registro de causa (cause register), que contiene un campo que indica la razón de la excepción.

      Interrupciones vectorizadas: En este método, la dirección a la que se transfiere el control
      está determinada por la causa de la excepción. Por ejemplo:

       Tipo de excepción           Dirección del vector de excepciones (en hexadecimal)
      Instrucción no definida                           8000 0000 nex
     Desbordamiento aritmético                          8000 0180 nex

              Cuadro 1: Interrupciones vectorizadas: Tabla de excepciones y sus vectores

    El sistema operativo conoce la razón de la excepción según la dirección donde se inicia el manejo
de la misma. Estas direcciones están separadas por 32 bytes (u 8 instrucciones). El sistema operativo
debe:

      Guardar la causa de la excepción: Se almacena la causa de la excepción y se ejecuta algún
      proceso relacionado con ella.

      Vectorización de excepciones: En caso de que las excepciones estén vectorizadas, la dirección
      de inicio del manejo depende de la causa. Si no están vectorizadas, todas las excepciones usan un
      único punto de entrada, y el sistema operativo descodifica el registro de estado para identificar
      la causa.

      Añadir registros y señales: Se pueden agregar algunos registros adicionales y señales de
      control a la implementación básica para manejar las excepciones.

   En sistemas con pipeline, las interrupciones y excepciones pueden ser:

      Síncronas o asíncronas:

        • Síncronas: Se sabe en qué momento de la instrucción ocurren.
        • Asíncronas: No se conoce exactamente cuándo se producirán.

<!-- p. 78 -->

      Solicitadas o generadas:

        • Solicitadas por el programa: Por ejemplo, desbordamiento aritmético.
        • Generadas dentro del programa: Fallos internos en la ejecución.

      Dentro de las instrucciones o entre ellas:

        • Las excepciones pueden ocurrir durante la ejecución de una instrucción.
        • También pueden ocurrir entre dos instrucciones.

   El solapamiento en la ejecución de instrucciones en un pipeline complica la determinación de si
una instrucción puede cambiar el estado de la máquina sin riesgos. En un pipeline con varias etapas,
cualquier instrucción puede provocar una excepción en una etapa diferente. Ejemplo:

      Fallos de página: Ocurren en medio de una instrucción y deben ser recomenzables. Ante un
      fallo de página:

        • Se introduce una instrucción trap en la etapa de IF.
        • Se anulan las escrituras tanto de la instrucción que generó el fallo como de las posteriores,
          que deben esperar hasta que se resuelva el fallo de página.
        • Se guarda el valor de PC de la instrucción que produjo el fallo (debe conservarse hasta la
          etapa de MEM) y se pasa a la rutina de gestión de la excepción.
        • Una vez resuelta la excepción, se utiliza el valor guardado del PC para retomar la ejecución
          desde donde se interrumpió.

   Cuando ocurre una interrupción externa (por ejemplo, de entrada/salida), se deben seguir estos
pasos:

      Cargar el PC: Se carga el PC con la dirección del handler de la interrupción.

      Vaciar el pipeline: Se vacía el pipeline e ingresan instrucciones nop (stall), para garantizar
      que no se produzcan excepciones mientras la interrupción es manejada.

      Guardar el PC: Se guarda el valor del PC con la dirección de la siguiente instrucción a ejecutar,
      para poder retornar al punto correcto una vez manejada la interrupción.

      Es importante vaciar el pipeline antes de manejar la interrupción, ya que las instrucciones pos-
      teriores podrían generar excepciones. Si se retoma la ejecución después de la interrupción, estas
      excepciones no existirían en el estado recuperado, lo cual podría generar inconsistencias.

    Una vez que se ha manejado la excepción, el sistema operativo debe continuar o finalizar la ejecución
del programa. Si se decide continuar, el sistema debe recuperar el estado previo a la excepción y
recomenzar la ejecución desde el punto adecuado. Esto implica:

      Resolver la excepción: El sistema maneja la excepción y, dependiendo de la causa, decide la
      acción a seguir.

      Recuperar el estado previo: El sistema recupera el estado del pipeline antes de que ocurriera
      la excepción.

      Reiniciar la ejecución: Se reinicia la ejecución desde el punto donde ocurrió la excepción.

<!-- p. 79 -->

   Una excepción se considera precisa si:

      Todas las instrucciones anteriores a la excepción han sido completadas.

      Las instrucciones que causan la excepción y las posteriores se comportan como si no hubieran
      empezado.

    El que un procesador tenga excepciones precisas hace referencia a que se garantiza que todas las
instrucciones anteriores a la instrucción que generó la excepción se hayan completado y que todos los
cambios realizados por estas instrucciones se hayan reflejado en el estado arquitectónico (registro de
estado, registros de propósito general, registros de punto flotante, etc). En cambio, la instrucción que
genera la excepción y las siguientes comienzan de nuevo una vez resuelta la excepción.

Figura 60: Manejo de excepciones en el pipeline. Suponiendo que las X marcan los lugares donde
surgen las excepciones, siempre se atiende primero la excepción de la instrucción más vieja. Aunque
temporalmente aparezcan excepciones en las etapas ID o IF de instrucciones más nuevas, primero se
debe atender la excepción ocurrida en la etapa MEM de la primera instrucción. Al llegar a la etapa WB
de esa instrucción, se chequea el vector de excepciones (ejemplo: 0001), donde el bit en 1 indica
que la excepción ocurrió en la etapa MEM.

    El problema de las excepciones en un pipeline es que estas pueden ocurrir fuera de orden. Por
ejemplo, es posible que la segunda o tercera excepción se produzcan antes que la primera debido a
la naturaleza paralela de las etapas del pipeline. Para resolver este problema, se utiliza un vector de
estado asociado a cada instrucción.

Vector de Estado para Excepciones
   Este vector de estado consta de un bit por cada etapa del pipeline donde puede producirse una
excepción. Cuando una excepción ocurre en una etapa específica para una instrucción:

      Se marca el bit correspondiente en el vector de estado de esa instrucción.

      Se impide la escritura en los registros o en la memoria, de manera que los resultados de la
      instrucción con excepción no se almacenen.

  El vector se verifica al final de la etapa MEM (inicio de la etapa WB), y las excepciones se
manejan en el orden en que llegan a la etapa WB, asegurando un control preciso de las mismas.

<!-- p. 80 -->

Ejemplo de Excepciones en Pipeline Segmentado
    En una implementación segmentada, las excepciones se manejan como cualquier otro riesgo de
control. Por ejemplo, supongamos que ocurre un desbordamiento aritmético en una instrucción de
suma: add r1, r2, r1
    Para manejar esta excepción, utilizaremos un esquema similar al utilizado para los saltos tomados.
Sin embargo, en este caso, la excepción provoca que se desactiven las señales de control. Para eliminar
las instrucciones que han entrado en el pipeline tras la instrucción con excepción, se procede de la
siguiente manera:

      Se elimina la instrucción en la etapa IF transformándola en una nop.
      En la etapa ID, se utiliza el multiplexor que ya existe, el cual es usado para poner a cero las
      señales de control en caso de bloqueos. Para ello, se añade una nueva señal de control llamada
      ID.Flush, que se combina con la lógica de bloqueo de la unidad de detección de riesgos para
      eliminar la instrucción en la etapa ID.
      En la etapa EX, se añade una señal llamada EX.Flush que activa nuevos multiplexores, los
      cuales ponen a cero las líneas de control de la etapa.

    Para comenzar la búsqueda de instrucciones desde la posición 8000 0180 hex (que es la locali-
zación de la excepción en caso de un desbordamiento aritmético), se agrega una nueva entrada al
multiplexor del PC que envía esta dirección al PC.
    El último paso en el manejo de la excepción es guardar el PC de la instrucción que causó la
excepción en el registro de excepción del PC (EPC). Se guarda la dirección de la instrucción con un
desplazamiento de 4 (PC+4), por lo que la rutina de manejo de la excepción debe restar 4 al valor
guardado antes de reanudar la ejecución del programa.

                              Figura 61: Ruta de datos y Excepciones.

<!-- p. 81 -->

    El desbordamiento se detecta durante la etapa de ejecución (EX), en el ciclo 6 del pipeline. En
este punto, se guarda la dirección de la instrucción que sigue a la operación add en el registro EPC
(en este caso, 4C + 4 = 50hex). Cerca del final de este ciclo, se activan todas las señales de vaciado
(Flush), desactivando las líneas de control de la instrucción add, impidiendo que sus resultados se
propaguen hacia las etapas posteriores.
    En el ciclo 7, el pipeline contiene burbujas en lugar de instrucciones válidas. Esto se debe a que
las instrucciones posteriores a add han sido vaciadas del pipeline como resultado de la excepción.
Al mismo tiempo, se comienza la búsqueda de la primera instrucción de la rutina de manejo de
excepciones, localizada en la dirección 8000 0180 hex. En este ejemplo, la primera instrucción de la
rutina es sw $25, 1000($0).
    Es importante destacar que las instrucciones and y or, que estaban en el pipeline antes de la
instrucción add, completan su ejecución normalmente, ya que no están involucradas en el desborda-
miento. A pesar de no mostrarse explícitamente, la señal de desbordamiento de la ALU es una entrada
en la unidad de control, lo que activa el vaciado del pipeline.
    Un problema importante a destacar es que, si no se para la ejecución de la instrucción en la mitad,
el programador no podrá observar el valor que contenía el registro (r1) antes de que se sobrescriba. En
este ejemplo, el registro destino de la instrucción add es (r1), por lo que el valor anterior se perderá.
Para evitar esto, la detección cuidadosa del desbordamiento en la etapa EX permite que la señal
EX.Flush impida que el resultado de add sea escrito en la etapa WB.
    Muchas excepciones requieren que la instrucción que causó la excepción finalice como si se hubiera
ejecutado de forma normal. La forma más sencilla de lograr esto es vaciar el pipeline, manejar la
excepción y luego reiniciar la ejecución de la instrucción desde el principio. De esta manera, el sistema
garantiza que la excepción se maneja correctamente y que el flujo de control del programa se restablece
adecuadamente.

### Operaciones Multiciclo
   Para mejorar el rendimiento de la uni-
   dad de ejecución, es común agregar hard-
   ware adicional especializado para ciertos
   tipos de operaciones, como unidades es-
   pecíficas para operaciones en punto flo-
   tante y operaciones con enteros. Estas
   unidades están diseñadas para ejecutar
   instrucciones especializadas más eficien-
   temente, aunque algunas de estas opera-
   ciones pueden requerir más de un ciclo de
   ejecución. Un caso típico de este tipo de
   optimización es la inclusión de unidades
                                                  Figura 62: EX está dividida en varias subunidades.
   para operaciones de punto flotante.

       Riesgos Estructurales: La adición de unidades especializadas puede generar conflictos cuando
       varias instrucciones compiten por los mismos recursos de hardware al mismo tiempo. Esto ocurre
       cuando una única unidad de hardware no es suficiente para ejecutar todas las instrucciones de
       un mismo tipo que se encuentran en diferentes etapas del pipeline.

       Mayor Penalización en los Riesgos LDE (Load-Data Hazard): Algunas instrucciones
       pueden tardar más en la etapa de ejecución (EX), especialmente aquellas relacionadas con el
       punto flotante. Esto introduce latencias adicionales en el pipeline, y puede aumentar la penali-
       zación de los riesgos LDE, ya que otras instrucciones que dependen de los resultados de estas

<!-- p. 82 -->

      operaciones quedarán a la espera por más tiempo.

      Finalización Fuera de Orden: La ejecución de operaciones en diferentes unidades especiali-
      zadas puede causar que las instrucciones finalicen fuera de orden, lo que complica la consistencia
      de los datos y el control de excepciones. En arquitecturas segmentadas, esto puede generar pro-
      blemas al tratar de mantener el orden correcto de finalización de las instrucciones, especialmente
      si no se maneja adecuadamente el vaciado del pipeline o las excepciones.

      Solapamiento de Operaciones Enteras y de Punto Flotante: Las operaciones enteras y
      de punto flotante pueden solaparse, lo que es beneficioso para mejorar el rendimiento, siempre y
      cuando los operandos de estas instrucciones sean independientes. En caso de dependencia entre
      operandos, se deben manejar correctamente los riesgos para evitar errores en el cálculo y la
      ejecución.

   La adición de unidades especializadas en la unidad de ejecución requiere una planificación cuidadosa
para evitar que estos problemas afecten negativamente el rendimiento general del sistema.

    Para realizar las operaciones correspondientes, se utilizarán tantos ciclos de reloj (ya sea para
uso o para iniciación) como etapas tenga el hardware destinado a esa operación. Por ejemplo, una
multiplicación en punto flotante puede demorar 7 ciclos, mientras que una división en punto flotante
podría requerir hasta 24 ciclos. Cabe destacar que el hardware de la división funciona de manera
diferente, ya que no suele estar segmentado en un pipeline. Esto significa que no es posible reutilizar
parte del hardware que ya ha resuelto algunas etapas de un cálculo para iniciar el siguiente, como sí
se hace en un pipeline.
    Esta diferencia en la duración de las operaciones implica que el orden de finalización de las ins-
trucciones puede variar. Si una operación B, que requiere menos ciclos de reloj, es precedida por una
operación A, que requiere más ciclos, es probable que B termine antes que A. Este riesgo de cambio
en el orden de ejecución requiere la intervención del procesador, ya que podría ser necesario parar su
operación temporalmente para manejar este cambio.
    La detección del cambio de orden en la ejecución de instrucciones puede requerir que el procesador
almacene los resultados en un buffer y los ordene antes de continuar, o que espere a que todas las
operaciones anteriores finalicen antes de proceder con las siguientes etapas (como la etapa de MEM).
Esto garantiza que las instrucciones se completen en el orden correcto y que no haya inconsistencias
en los datos.

<!-- p. 83 -->

#### Riesgos

Figura 63: Riesgo de LDE: La gran duración de algunas instrucciones implica más ciclos de detención
en el pipeline para garantizar un resultado correcto. Es necesario evitar situaciones como las de este
ejemplo mediante una planificación más cuidadosa de las instrucciones.

                               Figura 64: Finalización fuera de orden.

                       Figura 65: Riesgo EDE (Escritura después de Ejecución).

   Cuando las instrucciones terminan en un orden distinto al de su lanzamiento, pueden surgir diversos
problemas:

      Conflictos por escritura simultánea en registros: Si varias instrucciones intentan escribir
      en el mismo registro al mismo tiempo, se produce un conflicto, ya que no es posible que un
      mismo registro sea escrito simultáneamente por dos instrucciones diferentes, aunque se disponga
      de múltiples puertos en el banco de registros.

<!-- p. 84 -->

      Aparición de riesgos EDE (Escritura Después de Ejecución): Este tipo de riesgo, tam-
      bién conocido como Write After Write (WAW), ocurre cuando una instrucción sobrescribe los
      resultados de una instrucción anterior antes de que esta última haya completado su ejecución.
      Por ejemplo, si la instrucción LD F2 escribe en el registro F2 antes que la instrucción ADDD F2,
      F4, F2, la instrucción ADDD no funcionará correctamente, ya que su operando ha sido sobrescrito.

      Problemas con las excepciones: Cuando las instrucciones terminan en un orden diferente al
      esperado, puede cambiar el orden en que ocurren las excepciones, lo que complica su manejo.

    El riesgo EDE, o WAW (Write After Write), se produce cuando una instrucción sobrescribe un
registro antes de que una instrucción previa que también escribe en ese registro haya completado su
ejecución. Esto puede ocurrir, por ejemplo, cuando la instrucción LD F2 sobrescribe el valor de F2
antes de que la instrucción ADDD F2, F4, F2 lo haga, inutilizando el resultado de la operación de
suma.
    Riesgo LDE: Este riesgo surge cuando una instrucción intenta leer un valor de un registro antes de
que la instrucción que debía escribir en dicho registro haya completado su operación. En el ejemplo
anterior, si la instrucción ADDD intenta leer el valor de F2 antes de que la instrucción LD F2 haya
completado la escritura, se producirá un riesgo LDE, lo que puede generar resultados incorrectos en
el cálculo.
    Riesgo ELD: Este riesgo, también conocido como WAR (Write After Read), aparece cuando una
instrucción de escritura depende de los datos leídos por una instrucción previa. Sin embargo, en un
pipeline correctamente diseñado, las escrituras en los registros se realizan en orden durante la etapa
de escritura, lo que impide que se produzcan riesgos WAR.
    Para tratar los riesgos EDE (Write After Write), también conocidos como WAW, se pueden aplicar
las siguientes estrategias:

      Detener la instrucción que produce el riesgo: En el caso de que una instrucción LD esté
      escribiendo en F2 mientras que una instrucción ADDD está en proceso de ejecución, se puede
      detener la ejecución de LD hasta que ADDD haya completado su ejecución. De esta manera, se
      evita que la escritura en F2 por parte de la instrucción LD interfiera con la instrucción ADDD.

      Eliminar la escritura de la primera instrucción: Alternativamente, se puede optar por
      eliminar la escritura en F2 realizada por la instrucción ADDD. Esto evita que la instrucción LD lea
      un valor incorrecto de F2 debido a la escritura pendiente de la instrucción ADDD.

   Las operaciones que requieren múltiples ciclos de reloj, como operaciones de punto flotante, pueden
complicar el manejo de conflictos y riesgos. Para abordar estos problemas:

      Detección de conflictos en la etapa ID: Se debe detectar en la etapa de decodificación de
      instrucciones y lectura de registros (ID) si hay conflictos potenciales. Si una instrucción necesita
      escribir registros en el mismo ciclo que una instrucción ya emitida, la primera se detiene un ciclo.
      Esto evita la escritura simultánea en el mismo registro por diferentes instrucciones.

      Uso de un registro de desplazamiento: Implementar un registro de desplazamiento puede
      ayudar a indicar cuándo las instrucciones ya lanzadas podrán usar el bloque de registros. Este
      registro ayuda a gestionar el orden y el acceso a los registros de manera eficiente.

      Establecimiento de prioridades de acceso: Es necesario establecer prioridades de acceso
      a los recursos. Dar mayor prioridad a las unidades con mayor latencia permite gestionar mejor
      los conflictos y evitar que las instrucciones se bloqueen mutuamente. Se puede implementar una
      lógica de chequeo de detenciones en dos puntos para manejar estos conflictos.

<!-- p. 85 -->

### MPIS R4000 - Segmentación de 8 etapas

                           Figura 66: MPIS R4000 - Segmentación de 8 etapas .

       IF (Instruction Fetch): Es la primera mitad de la etapa de búsqueda de instrucción. Durante
       esta etapa, se inicia el acceso a la caché de instrucciones para obtener la instrucción siguiente.
       Además, se actualiza el contador de programa (PC) para apuntar a la siguiente instrucción en
       memoria.

       IS (Instruction Supply): Es la segunda mitad de la etapa de búsqueda de instrucción. Aquí
       se completa el acceso a la caché de instrucciones y se obtiene la instrucción correspondiente al
       PC actualizado en la etapa IF.

       Reg/Dec (Registro/Decodificación): En esta etapa, se verifica si la instrucción tiene un
       acierto en la caché de instrucciones. Además, se realiza la decodificación de la instrucción y la
       búsqueda de los registros necesarios para su ejecución. También se realizan comprobaciones de
       riesgos, como los riesgos de datos y control.

       EX (Ejecución): Durante esta etapa, se lleva a cabo la ejecución real de la instrucción. Se
       realizan operaciones como el cálculo en la ALU (Unidad Aritmético-Lógica), el cálculo de la
       dirección efectiva de la memoria, la evaluación de condiciones de salto y el cálculo del destino de
       salto. Esta etapa puede llevar varios ciclos de reloj, especialmente para instrucciones complejas.

       DF (Data Fetch): Esta etapa marca el inicio de la búsqueda de datos. Aquí se inicia el acceso
       a la memoria de datos para obtener los operandos necesarios para la instrucción en ejecución.

       DS (Data Supply): Es la segunda mitad de la etapa de búsqueda de datos. Durante esta
       etapa, se completa el acceso a la memoria de datos y se obtienen los operandos necesarios para
       la instrucción.

       TC (Tag Check): En esta etapa, se realizan comprobaciones de etiquetas y se determina si hay
       un acierto en la caché de datos. Esto implica verificar si los datos requeridos están disponibles
       en la caché de datos o si es necesario acceder a la memoria principal.

       WB (Write Back): Es la última etapa del ciclo de ejecución de una instrucción. Aquí se realiza
       la escritura de los resultados de la instrucción en los registros correspondientes. Los datos están
       disponibles al final de la etapa DS, aunque aún no se ha verificado si hay un acierto en la caché
       de datos.

<!-- p. 86 -->

Más Penalización en Cargas y en Saltos

                                                         En el caso de los saltos (instrucciones de salto
                                                         condicional o incondicional), se presenta una
                                                         penalización de tres ciclos de latencia. Esto se
                                                         debe a que la condición de salto se evalúa en la
                                                         etapa EX (Ejecución) y se toma una decisión
                                                         sobre la dirección de salto. Durante estos tres
                                                         ciclos, el procesador debe esperar para conocer
                                                         la dirección correcta a la que saltar.

                                                         Salto retardado de un ciclo y dos ciclos de
                                                         “predict not-taken”.
   Figura 67: Dos ciclos de latencia en los Load con
   cortocircuito.

                                                         (*) (**) (***) → Las instrucciones que siguen
                                                         al salto continúan su ejecución de forma nor-
                                                         mal y se abortan en caso de que el salto se
                                                         tome.

Operaciones de Punto Flotante
    El MIPS R4000 cuenta con tres unidades funcionales que funcionan en paralelo: un divisor, un
multiplicador y un sumador de punto flotante. Las diferentes operaciones se realizan mediante estas
unidades, y la duración de las operaciones varía entre 2 ciclos (negación) y 112 ciclos (raíz cuadrada).
    Las unidades funcionales de punto flotante están segmentadas en un total de 8 estados. Cada etapa
está especializada para una parte específica de la operación. A continuación se describen las etapas y
sus correspondientes unidades:

              Etapas         Unidad        Descripción
                A           FP adder       Etapa de suma de mantisas
                D           FP divider     Etapa de división
                E          FP multiplier   Etapa de test de excepciones
                M          FP multiplier   Primera etapa del multiplicador
                N          FP multiplier   Segunda etapa del multiplicador
                R           FP adder       Etapa de redondeo
                S           FP adder       Etapa de desplazamiento
                U               -          Etapa de desempaquetado

                    Cuadro 2: Etapas de las Unidades Funcionales del MIPS R4000

<!-- p. 87 -->

Comportamiento de Las unidades de PF (Punto Flotante)

     Instr PF         1     2        3        4         5      6       7                   8
   Add, Subtract      U    S+A      A+R      R+S
      Multiply        U    E+M       M        M         M      N     N+A              R
       Divide         U     A        R       D28        ...   D+A    D+R      D+R, D+A, D+R, A, R
    Square root       U     E     (A+R)108    .         ...    A      R
      Negate          U     S
   Absolute value     U     S
    FP compare        U     A           R

                           Cuadro 3: Comportamiento de las unidades de PF

                                        Latencia    Intervalo de inicialización
                       Add, Subtract       4                     3
                         Multiply          8                     4
                          Divide           36                   35
                        Square root       112                  111
                          Negate           2                     1
                       Absolute value      2                     1
                        FP compare         3                     2

Rendimiento

                                                                                     Load stalls (1 o 2 ci-
                                                                                     clos)

                                                                                     Saltos (2 ciclos + slots
                                                                                     no rellenos)

                                                                                     FP stalls (resultados):
                                                                                     riesgo de LDE (latencia)

                                                                                     FP stalls (estructura-
                                                                                     les): hardware de pun-
                                                                                     to flotante (Hw FP) muy
                                                                                     escaso (paralelismo)
            Figura 68: No se alcanza el rendimiento ideal CPI = 1.

   RECORDAR: Una instrucción termina cuando se ejecuta su operación WB (Write
   Back)

<!-- p. 88 -->

                                                                        Figura 69: Resumen conceptual de la Unidad N°3: ILP (Paralelismo a Nivel de Instrucción).
