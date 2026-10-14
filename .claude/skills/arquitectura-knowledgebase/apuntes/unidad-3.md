<!-- p. 89 -->

## Unidad 3: ILP (Paralelismo a Nivel de Instrucción)

¿A dónde llegamos?
   Segmentamos el procesador. Aparecieron riesgos (estructurales, de datos y de control) y estuvimos
trabajando para mitigarlos:

      Riesgos de control: duplicábamos hardware, dividíamos memorias.

      Usábamos la mitad del ciclo para escribir los registros y la otra mitad para leer.

      Riesgos de datos: hacíamos cortocircuito (forwarding). En el caso de LOAD teníamos que meter
      una burbuja.

      Riesgos de control: poníamos una ALU para calcular la dirección antes y perdíamos un
      ciclo.

¿Qué vamos a ver ahora?
   En esta unidad (y la que sigue) veremos técnicas para seguir explotando el ILP. ILP es el
paralelismo a través de unidades de instrucción. La idea es sacarle provecho a la segmentación.

¿Cuándo le saco provecho?
      Cuando tengo siempre lleno el pipeline.

      Cuando no tengo que estar parándolo y vaciándolo por los saltos.

      Cuando no tengo dependencias por LOAD que me obliguen a meter burbujas todo el tiempo.

    Eso aumenta el CPI. Nos interesa tener el CPI ideal (1), y lo vamos perdiendo por los saltos
y por los riesgos de datos. Ahora vamos a ver técnicas para explotar al máximo el ILP.
    La segmentación mejora la productividad del procesador, pero no reduce el tiempo de ejecución
inherente o la latencia de las instrucciones. Para algunas instrucciones, la latencia es comparable a la
de la estrategia de ciclo único. Esto puede expresarse como:

               Latencia de Instrucción = Tiempo de ejecución inherente por instrucción
    La segmentación reduce la duración del ciclo de reloj en un camino de datos de ciclo único. Aunque
mejora el rendimiento general (throughput), no tiene un impacto significativo en la latencia de las
instrucciones:

                      Ciclo de Reloj Segmentado < Ciclo de Reloj de Ciclo Único
                                  Latencia ≈ Latencia en Ciclo Único
    La ejecución múltiple de instrucciones añade hardware adicional al camino de datos, lo que permite
iniciar varias instrucciones en cada ciclo de reloj. Sin embargo, esto aumenta la latencia efectiva debido
a la complejidad añadida:

                                                    Número de Ciclos
                                   CPI efectivo =
                                                     Instrucciones

<!-- p. 90 -->

    La ejecución múltiple se enfoca principalmente en la reducción del CPI, a diferencia de la segmen-
tación, que se centra en la reducción de la duración del ciclo de reloj.
    Mientras que la segmentación se enfoca en reducir la duración del ciclo de reloj, la ejecución
múltiple busca reducir los ciclos por instrucción (CPI ):

                           Objetivo de Segmentación: mı́n(Ciclo de Reloj)
                              Objetivo de Ejecución Múltiple: mı́n(CPI)

   Objetivo

   Ejecutar el mayor número posible de instrucciones por ciclo.

   El problema reside en que el CPI real es la penalización por saltos:

              CPI real = CPI ideal + Penalización media por instrucción ← CPI real >1
    Por ello se intenta explotar el ILP.
    El paralelismo a nivel de instrucciones es una técnica que permite ejecutar múltiples instrucciones
en forma simultánea dentro de un procesador, aprovechando la disponibilidad de recursos y reduciendo
el tiempo de ejecución. Esto se logra al identificar dependencias entre instrucciones y organizarlas en
grupos que pueden ejecutarse de manera independiente y en paralelo.

¿Por qué se considera que el CPI ideal es 1?
    Supongamos que tienes una secuencia de instrucciones. En el primer ciclo, inicias la primera ins-
trucción (en IF), en el segundo ciclo inicias la segunda instrucción (en IF) mientras la primera está en
ID, y así sucesivamente. En un sistema ideal, después del primer ciclo, podrás completar una instruc-
ción en cada ciclo de reloj. Esto significa que, en promedio, estás completando una instrucción por
ciclo.

### Bloque Básico (BB)
    Es un conjunto de instrucciones sin saltos entre ellas. El tamaño promedio de un bloque básico es
de cuatro instrucciones. Como un bloque básico tiene instrucciones fuertemente dependientes entre sí,
para obtener una mejora considerable es aconsejable intercalar las instrucciones de múltiples bloques
básicos, ya que estas serán independientes.

### Tipos de mecanismos para explotar ILP
    Explotar ILP significa diseñar estrategias de ejecución que permiten que las instrucciones indepen-
dientes se ejecuten en paralelo, aumentando el rendimiento y la eficiencia del procesador. Esto puede
lograrse con técnicas basadas en HW o en SW.
    Existen dos enfoques principales:
       Técnicas estáticas: se aplican en tiempo de compilación (las realiza el compilador). Ventaja:
       no agregan consumo ni complejidad de hardware. Desventaja: suelen ser menos eficientes porque
       no pueden adaptarse a lo que ocurre en runtime (por ejemplo, un fallo de caché en un momento
       específico).
       Técnicas dinámicas: las implementa el hardware en runtime (el propio procesador). Suelen
       ser más costosas en potencia, consumo y complejidad del chip (más hardware y lógica), pero se
       adaptan a lo que sucede en ejecución.

<!-- p. 91 -->

#### Mecanismos Basados en Hardware
   Estos mecanismos se activan en tiempo de ejecución (dinámicos). Ejemplos incluyen procesadores
como Pentium, AMD e IBM.

      A diferencia de los mecanismos de software, los mecanismos basados en hardware tienen acceso
      a toda la información disponible en el momento de la ejecución, lo que permite tomar decisiones
      con mayor precisión.

      Un método basado en software, por ejemplo, no puede prever detalles como la ocurrencia de un
      fallo de página o misscache.

      El código es independiente de la ejecución. Repito cada vez que ejecuto.

      Resolver el ILP mediante hardware tiene implicancias en términos de consumo de energía y costo
      del procesador.

#### Mecanismos Basados en Software
    Estos mecanismos se activan en tiempo de compilación (estáticos). Un ejemplo de procesador que
utiliza este enfoque es el Itanium.

      Para ser efectivos, estos mecanismos deben conocer las dependencias entre instrucciones del
      programa. Las dependencias de memoria, en particular, son difíciles de determinar.

      Una técnica para explotar ILP por software, diseñada para un procesador A, no necesariamente
      funcionará bien en otro procesador B, lo cual es un problema cuando se trata de aplicaciones
      para procesadores de propósito general.

      Sin embargo, en aplicaciones particulares donde el hardware no cambia (por ejemplo, en sistemas
      embebidos que siempre ejecutan el mismo programa), esta opción puede ser más apropiada.
      Repito cada vez que compilo.

Aspecto                        Descripción de Compilación
Definición                     Proceso de traducir el código fuente a lenguaje de máquina.
Tiempo                         Ocurre antes de la ejecución.
Dependencias                   Resuelve dependencias de instrucciones, pero no tiene información de ejecución.
Mecanismos Basados en HW       No se aplican en este contexto.
Mecanismos Basados en SW       Se activan en tiempo de compilación, pero pueden ser menos efectivos.

Aspecto                          Descripción de Ejecución
Definición                       Proceso en el que el sistema operativo ejecuta el código compilado.
Tiempo                           Ocurre en tiempo de ejecución.
Información Accesible            Accede a información dinámica y toma decisiones en tiempo real.
Mecanismos Basados en HW         Se activan en tiempo de ejecución, optimizando decisiones en tiempo real.
Mecanismos Basados en SW         No se aplican en este contexto, ya que dependen de la compilación.

<!-- p. 92 -->

### Técnicas para Explotar ILP
#### Técnicas Dinámicas Basadas en Hardware
   Las técnicas dinámicas basadas en hardware permiten mejorar el rendimiento del procesador me-
diante la detección y resolución de riesgos en tiempo de ejecución, sin depender exclusivamente del
compilador. Estas técnicas incrementan el paralelismo efectivo y reducen el CPI observado.

   1. Planificación Dinámica: Utiliza hardware especializado para detectar dependencias entre ins-
      trucciones y reordenarlas dinámicamente durante la ejecución. En lugar de detener el pipeline
      ante la presencia de riesgos de datos, el procesador identifica instrucciones independientes y las
      ejecuta fuera de orden, manteniendo un flujo continuo de ejecución.

                           Planificación dinámica → mı́n(Paradas por riesgos de datos)

   2. Predicción Dinámica de Saltos: Permite al procesador anticipar el resultado de una instruc-
      ción de control antes de que la condición sea evaluada. Mediante el uso de historial de ejecución
      y estructuras de predicción, se reducen las paradas asociadas a riesgos de control.

                    Predicción dinámica de saltos → mı́n(Paradas por riesgos de control)

   3. Lanzamiento Múltiple de Instrucciones por Ciclo: Consiste en la capacidad del hardware
      para emitir y ejecutar múltiples instrucciones independientes en un mismo ciclo de reloj. Esta
      técnica, característica de los procesadores superescalares, permite explotar el paralelismo a nivel
      de instrucción y reducir el CPI ideal.
                                                   Número total de ciclos
                                CPI ideal =
                                              Número de instrucciones ejecutadas

                              Lanzamiento múltiple → máx(Instrucciones por ciclo)

   4. Especulación: Permite ejecutar instrucciones de manera anticipada, asumiendo ciertos resul-
      tados para dependencias de datos o decisiones de control. Si la especulación resulta correcta,
      se mejora el rendimiento; en caso contrario, el procesador revierte los efectos especulativos y
      restablece el estado arquitectónico correcto.
                                            
                                            Correcta:     mı́n(Paradas por riesgos)
                           Especulación →
                                            Incorrecta:   Revertir efectos y reejecutar

   5. Desambiguación Dinámica de Memoria: Permite al procesador determinar en tiempo de
      ejecución si múltiples accesos a memoria son independientes. Mediante técnicas de seguimiento
      de dependencias, aliasing y especulación, se priorizan lecturas y se posponen escrituras cuando
      es seguro hacerlo, reduciendo las paradas causadas por riesgos de datos en memoria.

          Desambiguación dinámica de memoria → mı́n(Paradas por riesgos de datos en memoria)

<!-- p. 93 -->

#### Técnicas Estáticas Basadas en Software
   1. Desenrollado de Bucles o Loop Unrolling: Consiste en duplicar o triplicar segmentos del
      cuerpo del bucle, reduciendo así la cantidad de iteraciones necesarias y eliminando las instruc-
      ciones de salto y las comprobaciones de límites en cada iteración. Esto permite una ejecución
      más eficiente y reduce las paradas por riesgos de control.

                           Desenrollado de Bucles → mı́n(Paradas por riesgos de control)

   2. Planificación por el Compilador o Compiler Scheduling: El compilador reorganiza las
      instrucciones del programa para favorecer el paralelismo y la ejecución eficiente en el hardware
      del procesador. Este proceso implica analizar las dependencias de datos y control, reorganizando
      las instrucciones para minimizar los riesgos y maximizar la ejecución en paralelo.

                        Planificación por el Compilador → máx(Paralelismo en ejecución)

   3. Software Pipelining: Consiste en dividir un bucle en una serie de iteraciones superpuestas.
      En lugar de esperar a que una iteración se complete antes de comenzar la siguiente, el software
      pipelining aprovecha el paralelismo temporal iniciando múltiples iteraciones en diferentes etapas
      del bucle. Esto reduce las paradas por riesgos de datos.

                              Software Pipelining → mı́n(Paradas por riesgos de datos)

   4. Predicción Estática y Especulación por Compilador: El compilador realiza suposiciones
      anticipadas sobre el flujo de las instrucciones y optimiza su ejecución en consecuencia. La pre-
      dicción estática implica que el compilador hace estimaciones basadas en el análisis del código
      fuente sin ejecutar el programa, mientras que la especulación por compilador permite ejecutar
      instrucciones de manera especulativa, basándose en las suposiciones del compilador acerca de
      las dependencias de datos y control.
                                                              
                                                              Correcta:   mı́n(Paradas por riesgos)
              Predicción Estática y Especulación →
                                                              Incorrecta: Reintentar ejecución correcta

                              Cuadro 4: Resumen de Técnicas para Explotar ILP

Técnica                                                Descripción
Técnicas Dinámicas Basadas en HW
1. Planificación Dinámica                              Reorganiza instrucciones para evitar riesgos de datos.
2. Predicción Dinámica de Saltos                       Toma decisiones anticipadas sobre saltos, minimizando paradas.
3. Lanzamiento Múltiple de Instrucciones por Ciclo     Ejecuta varias instrucciones en paralelo en un ciclo.
4. Especulación                                        Ejecuta instrucciones conjeturales; deshace efectos si es incorrecto.
5. Desambiguación Dinámica de Memoria                  Resuelve conflictos de acceso a memoria.
Técnicas Estáticas Basadas en SW
1. Desenrollado de Bucles                              Duplica segmentos de bucles, reduciendo iteraciones y paradas.
2. Planificación por el Compilador                     Reorganiza instrucciones para maximizar paralelismo.
3. Software Pipelining                                 Inicia múltiples iteraciones superpuestas del bucle.
4. Predicción Estática y Especulación por Compilador   Suposiciones sobre el flujo de instrucciones; reintentar si es incorrecto.

<!-- p. 94 -->

### Dependencias (HW y Recursos)
    Para obtener el máximo paralelismo, es crítico determinar las dependencias entre instrucciones.
Las dependencias son propias de los programas y determinan el orden del cálculo de los resultados,
imponiendo un límite al paralelismo que es posible obtener. La presencia de una dependencia indica
la posibilidad de un riesgo, pero el riesgo de que este aparezca y la posible parada depende de las
características de la segmentación en el procesador.
    El problema de las dependencias nace de los recursos compartidos (tanto hardware como datos).
Se debe determinar cuáles dependencias existen y a qué recursos afectan.

Tipos de Dependencias
   1. Dependencia de datos: La instrucción j depende del resultado provisto por la instrucción i.

           Dependencia verdadera (LDE): Ocurre cuando la instrucción i produce un resultado
           que la instrucción j necesita.
                                          NOTA:

                   i : LD F 0, 0(R1);         • F0, F1 , F2 , ... , Fn son registros.
                j : ADDD F 4, F 0, F 2        • ADDD instrucción aritmética para la suma de números
                                                de coma flotante de precisión doble.
   2. Dependencia de nombre:

           Antidependencia (WAR o EDL): La instrucción j escribe registros o memoria antes
           que la instrucción i. Estas instrucciones son dependientes y no se puede alterar el orden de
           su ejecución.
                                    i : ADDD F 4, F 0, F 2; j : LD F 0, −8(R1)

           Dependencia de salida (EDE o WAW): Las instrucciones i y j escriben el mismo
           registro o posición de memoria. Estas instrucciones también son dependientes.

                                   i : ADDD F 4, F 0, F 2;   j : SUBD F 4, F 3, F 2

    En las dependencias de datos, los mecanismos de ejecución deben asegurar que el resultado sea el
mismo que si la ejecución fuera secuencial. Es decir, se debe explotar todo el paralelismo posible sin
alterar el resultado de la ejecución.
    Las dependencias de nombre ocurren cuando una instrucción depende del resultado de otra instruc-
ción que aún no ha producido dicho resultado. En lugar de esperar a que la instrucción dependiente
tenga acceso al resultado, se pueden utilizar registros adicionales o nombres para almacenar y com-
partir temporalmente los valores necesarios. Esto permite que la instrucción dependiente obtenga el
resultado de un registro diferente, evitando así la dependencia directa con la instrucción original y
permitiendo una ejecución paralela.

#### Dependencias de Control
    Las dependencias de control se refieren a las relaciones de dependencia entre las instrucciones de un
programa que involucran la ejecución condicional o el cambio en el flujo de control. Estas dependencias
aseguran que el orden y la coherencia del programa se mantengan correctamente. Cada instrucción
depende de un conjunto de saltos y cambios en el flujo de ejecución que deben respetarse para preservar
el orden y la coherencia del programa.

<!-- p. 95 -->

         if P1 (
                    S1;
                                                Las dependencias de control pueden violarse, es decir, se pue-
                          );
                                                den ejecutar instrucciones no debidas siempre y cuando esto
                               if P2 (
                                                no modifique el resultado correcto del programa. El compor-
                                         S2;
                                                tamiento de las excepciones y el flujo de datos (cómo los datos
                                            )
                                                se transmiten desde una instrucción a otra) también deben
                                                preservarse.
   S1 depende de P1; S2 depende de P2

#### Dependencias de Control y Excepciones
   El comportamiento de las excepciones se debe preservar. Cualquier cambio en el orden de ejecución
no debe modificar cómo las excepciones son atendidas durante la ejecución.

               DADDU R2, R3, R4                 La instrucción LW podría generar un fallo de página, por lo
               BEQZ R2, L1                      que, aunque no tenga dependencias directas con la instruc-
               LW    R1, 0(R2)                  ción anterior, no se puede cambiar su posición antes de la
         L1:                                    instrucción BEQZ, ya que esto podría alterar la forma en que
                                                se atienden las excepciones.

#### Dependencias de Control y Flujo de Datos
   El flujo de datos entre instrucciones productoras y consumidoras de datos debe mantenerse ade-
cuadamente.
               DADDU R1, R2, R3
               BEQZ R4, L1                      La instrucción OR utiliza el valor resultante de la instrucción
               DSUBU R1, R5, R6                 DADDU o DSUBU, dependiendo del resultado de un salto condi-
         L1:                                    cional. Es crucial preservar este flujo de datos para asegurar
               OR     R7, R1, R8                que los cálculos se realicen correctamente.

### Consideraciones en la Gestión de Dependencias para la Explotación de ILP
   El compilador se concentra en las dependencias del programa, no en los riesgos de un “pipeline”
determinado.

       Dependencias de Datos: Es fácil determinar las dependencias entre registros, pero resulta más
       complicado cuando se trata de direcciones de memoria. Por ejemplo, puede ser difícil determinar
       si los datos obtenidos de las direcciones 100(R4) y 20(R6) son iguales, o si los datos obtenidos
       de 20(R6) en una iteración son los mismos que en otra iteración diferente.
       Para permitir la reordenación de las instrucciones load y store, el compilador debe conocer
       estas dependencias entre instrucciones. Para evitar dependencias de nombre, es posible usar más
       registros en el procesador, lo que proporciona más opciones para asignar nombres a los datos y
       reducir dichas dependencias.

       Dependencias de Control: En términos generales:

         • Una instrucción dependiente de un salto no puede moverse antes del salto.
         • Una instrucción no dependiente de un salto no puede moverse después del salto.

<!-- p. 96 -->

      Esto garantiza que se mantenga el orden correcto de las instrucciones con respecto a los saltos
      condicionales.
      Las dependencias de control afectan el orden de las excepciones y el flujo de datos. Para abordar
      este problema, se requiere una solución combinada de hardware y software, en la cual tanto el
      procesador como el compilador colaboran para asegurar el manejo adecuado de las excepciones
      y del flujo de datos.

#### Ejemplo: Bucle Simple

   Consideremos el siguiente bucle simple:

   for (i = 1000; i > 0; i--)                          |    Sumo una contante
       x[i] = x[i] + s;                                |    al vector x[i]

   En ensamblador (asumiendo que el registro R1 ya contiene el valor 1000), el código sería:

Loop:
     LD         F0, 0(R1)              ; Cargar el elemento del array (F0 = x[i])
     ADDD       F4, F0, F2             ; Sumar el escalar en F2 (F4 = x[i] + s)
     SD         F4, 0(R1)              ; Guardar el resultado (x[i] = F4)
     SUBI       R1, R1, #8             ; Decrementar el puntero en 8 bytes, doble palabra
     BNEZ       R1, Loop               ; Saltar si R1 != 0

    La ejecución de estas instrucciones en el procesador tendría el siguiente flujo, asumiendo que el
procesador tiene una latencia de uso de 3 ciclos para operaciones de punto flotante y de 1 ciclo para
instrucciones de enteros:

         Ejecución en el procesador:

         Instrucción              | Ciclo   |
         ------------------------------------
         LD F0, 0(R1)             | 1       |
         Espera                   | 2       |
         ------------------------------------
         ADDD F4, F0, F2          | 3       |              Por lo tanto, el bucle demora 10 ciclos para
         Espera                   | 4       |              completarse (una instrucción cada dos ciclos,
         Espera                   | 5       |              lo que implica un CPI = 0.5). Esto puede
         ------------------------------------              mejorarse explotando el paralelismo a nivel de
         SD 0(R1), F4             | 6       |              instrucciones (ILP).
         ------------------------------------
         SUBI R1, R1, #8          | 7       |
         Espera                   | 8       |
         ------------------------------------
         BNEZ R1, Loop            | 9       |
         Espera                   | 10      |
         ------------------------------------

<!-- p. 97 -->

#### Planificación de Instrucciones (Reordenamiento)
    El siguiente ejemplo muestra cómo se pueden reordenar las instrucciones del bucle para ocultar
latencias y optimizar la ejecución (cambiamos el orden pero mantemenos el mismo resultado):

         Loop:
             LD   F0, 0(R1)                 ; Cargar elemento del array (F0 = x[i])
             SUBI R1, R1, #8                ; Decrementar el puntero en 8 bytes (i--)
             ADDD F4, F0, F2                ; Sumar el escalar en F2 (F4 = x[i] + s)
             BNEZ R1, Loop                  ; Saltar si R1 != 0
             SD   0(R1), F4                 ; Guardar el resultado (x[i] = F4)

    Con el reordenamiento de las instrucciones, se logra ejecutar el bucle en 6 ciclos, con una instrucción
completada por ciclo. Esto representa una mejora respecto a la versión original, que tardaba 9 ciclos.
    Además, se observan 2 ciclos de overhead debido al salto, pero el reordenamiento permite eliminar
las esperas por dependencias y aprovechar mejor el slot del salto (salto retardado), lo que reduce la
cantidad total de ciclos en los que se ejecuta el código.

#### Loop Unrolling (Desenrollado)
    Para exponer más paralelismo y eliminar saltos, el bucle se desenrolla 4 veces, como se muestra
a continuación:
   Loop:
       LD   F0, 0(R1)                  ; Cargar elemento del array (F0 = x[i])
       ADDD F4, F0, F2                 ; Sumar el escalar en F2 (F4 = x[i] + s)
       SD   0(R1), F4                  ; Guardar el resultado (x[i] = F4)

         LD   F6, -8(R1)               ; Cargar el siguiente elemento (x[i-1])
         ADDD F8, F6, F2               ; Sumar el escalar en F2 (F8 = x[i-1] + s)
         SD   -8(R1), F8               ; Guardar el resultado (x[i-1] = F8)

         LD   F10, -16(R1)             ; Cargar el siguiente elemento (x[i-2])
         ADDD F12, F10, F2             ; Sumar el escalar en F2 (F12 = x[i-2] + s)
         SD   -16(R1), F12             ; Guardar el resultado (x[i-2] = F12)

         LD   F14, -24(R1)             ; Cargar el siguiente elemento (x[i-3])
         ADDD F16, F14, F2             ; Sumar el escalar en F2 (F16 = x[i-3] + s)
         SD   -24(R1), F16             ; Guardar el resultado (x[i-3] = F16)

         SUBI R1, R1, #32              ; Decrementar el puntero en 32 bytes
         BNEZ R1, Loop                 ; Saltar si R1 != 0

      Expone más paralelismo y elimina saltos:
         • En esta versión desenrollada, se elimina un total de 3 saltos y 3 decrementos en cada
           iteración.
         • Las dependencias de datos permanecen y siguen existiendo ciertas paradas.
         • Se requieren más registros; el renombrado de registros por parte del compilador evita
           conflictos.

<!-- p. 98 -->

      Optimización mediante reordenamiento:

         • En lugar de decrementar el puntero por 8 bytes tras cada iteración, se usan desplaza-
           mientos negativos (-8, -16, -24, -32) directamente en LD/SD.
         • Esto reduce evaluaciones repetidas del puntero y minimiza saltos.

      Desenrollo y planificación:

         • Desenrosco y planifico: primero los 4 LOAD, luego los 4 ADD, y después los 4 STORE.
         • En vez de restar 8 cada vez, resto 32 al final: en lugar de i + 1, hago i + 4.
         • Si el for original tenía 100 iteraciones, ahora pasa a 25.

      Efecto en rendimiento:

         • Se pasa de ∼ 8 ciclos por iteración a ∼ 3,5 ciclos por iteración.

      Limitaciones:

         • Presión sobre registros: no puedo desenrollar las 100 iteraciones porque no tengo 100
           registros; tengo 32 y uso 2 por iteración.
         • Aumento del tamaño de código: al desenrollar hay más instrucciones; crece el binario
           y la presión de registros.

#### Desenrollado + Planificación

         Loop:
             LD     F0, 0(R1)              ; F0 = x[i]
             LD     F6, -8(R1)             ; F6 = x[i-1]
             LD     F10, -16(R1)           ; F10 = x[i-2]
             LD     F14, -24(R1)           ; F14 = x[i-3]

              ADDD F4, F0, F2              ; F4 = F0 + s = x[i] + s
              ADDD F8, F6, F2              ; F8 = F6 + s = x[i-1] + s
              ADDD F12, F10, F2            ; F12 = F10 + s = x[i-2] + s
              ADDD F16, F14, F2            ; F16 = F14 + s = x[i-3] + s

              SD    0(R1), F4              ; x[i] = F4 = x[i] + s
              SD    -8(R1), F8             ; x[i-1] = F8 = x[i-1] + s
              SD    -16(R1), F12           ; x[i-2] = F12 = x[i-2] + s
              SD    -24(R1), F16           ; x[i-3] = F16 = x[i-3] + s

              SUBI R1, R1, #32             ; Decrementar R1 en 32 bytes
              BNEZ R1, Loop                ; Saltar si R1 != 0

      Optimización del tiempo de ejecución: El tiempo de ejecución del bucle se ha reducido a
      3.5 ciclos por iteración gracias al desenrollado y la planificación de instrucciones.

      Uso de más registros: Se han utilizado más registros, que son un recurso limitado en el
      procesador. Esto no puede evitarse en este tipo de optimizaciones.

<!-- p. 99 -->

      Impacto en programas más largos: Aunque el programa original es corto y no se ve afectado,
      en programas más largos, aumentar el tamaño para explotar ILP podría provocar fallos en la
      memoria de instrucciones, lo que afectaría negativamente el tiempo de ejecución.

      Planificación del compilador:El compilador juega un papel crucial al planificar las instruc-
      ciones para minimizar riesgos y eliminar paradas en el pipeline.

   RESUMEN: Mas Registros = codigo mas largo pero mas corto en tiempo.

#### Software Pipelining
    A diferencia del loop unrolling, el software pipeline no elimina saltos: la cantidad de saltos es
la misma. Lo que busca es eliminar dependencias de datos (los stalls).

      Si las iteraciones de un bucle son independientes, se pueden tomar instrucciones de diferentes
      iteraciones para aumentar el ILP (Paralelismo a Nivel de Instrucción).

      Las instrucciones se reorganizan de manera que cada una pertenezca a una iteración distinta.

      Ventajas:

         • Evita dependencias entre instrucciones, eliminando la necesidad de insertar paradas en el
           pipeline.
         • No aumenta la longitud del programa.
         • No se requieren registros adicionales, lo que optimiza el uso de recursos del procesador.

      Desventajas:

         • No disminuye la cantidad de saltos del bucle original.
         • Introduce un overhead temporal al inicio, debido a la necesidad de ”llenar el pipeline”.
         • Se genera otro overhead al final, ya que es necesario ”vaciar el pipeline”.

      Para implementar el software pipelining, el bucle se desenrolla n veces, siendo n el número de
      iteraciones independientes.

      Posteriormente, se ejecuta una instrucción de cada iteración, logrando una sucesión de instruc-
      ciones independientes.

      Finalmente, se modifica el puntero y se realizan los saltos para que las instrucciones se ejecuten
      para todas las n iteraciones.

<!-- p. 100 -->

                                                                     En lugar de esperar a que se com-
                                                                     plete una iteración completa del bu-
                                                                     cle antes de comenzar la siguiente
                                                                     iteración, en este ejemplo la segun-
                                                                     da iteración comienza solo después
                                                                     de que A se complete la sección de
                                                                     la primera iteración. En otras pala-
                                                                     bras, la segunda iteración comien-
                                                                     za solo después de que se complete
                                                                     una parte de la primera iteración.
                                                                     Siempre que se pueda preservar la
                                                                     exactitud, la iteración i+1 puede co-
                                                                     menzar antes de que finalice la ite-
                                                                     ración i. Esto generalmente permite
                                                                     una utilización mucho mayor de los
                                                                     recursos de la máquina de la que se
                                                                     podría lograr con otras técnicas de
                     Figura 70: Software Pipelining.
                                                                     programación.
   La idea es partir del mismo loop con stalls y hacer un paso intermedio:

      Desenrollar 3 veces (iteraciones I0 , I1 , I2 ).

      Tomar una instrucción de cada iteración y armar un nuevo loop con ese trío. De este modo,
      por ser de iteraciones distintas, no dependen entre sí: el ADD no depende del LD, y el STORE
      no depende del ADD.

      Usar registros distintos para cada iteración.

   Para que funcione, hace falta un setup y un “tier load” (pasos antes y después):

      Antes de entrar al kernel, ejecutar la primera de la segunda iteración y las dos primeras de
      la tercera iteración.

      Luego se itera con el trío independiente (una instrucción por iteración).

  El resultado es que la cantidad de saltos se mantiene, pero no aparecen los stalls en el
medio.

<!-- p. 101 -->

   He desarrollado cada instrucción y tengo
   registros distintos. Aunque los saltos son
   equivalentes, he eliminado la dependen-
   cia de los datos.

   Ejecución SW Pipelined (suposi-
   ción R1=1000)

   Nota: En el código con software pipeli-
   ning falta una parte al inicio (llenado del
   pipeline) y una parte al final (vaciado del
   pipeline).

                                                   Figura 71: Ejecución SW Pipelined (R1=1000).

   Loop Unrolling                                        Software Pipelining

          Maximiza la distancia resultado-uso.               Minimiza las dependencias en el cuerpo del
                                                             bucle, al hacer que las instrucciones de di-
          Menor tamaño del código, ya que elimina            ferentes iteraciones se ejecuten en paralelo.
          la necesidad de instrucciones de salto adi-
          cionales en cada iteración.                        No reduce el número de saltos, ya que los
                                                             saltos condicionales aún están presentes en
          Llenado y vaciado del pipeline solo una vez,       el código.
          al inicio y al final del bucle.
                                                             Necesita manejo especial para el llenado y
          Ventajas:                                          vaciado del pipeline, tanto al inicio como al
            • Reducción en el número de saltos, ya           final del bucle.
              que estos se eliminan o se reducen sig-        Ventajas:
              nificativamente.
            • Incrementa el paralelismo dentro del             • No incrementa el tamaño del código
              bucle al ejecutar múltiples operaciones            significativamente, ya que no se aña-
              en paralelo.                                       den iteraciones adicionales.
                                                               • Puede manejar bucles con dependen-
          Desventajas:                                           cias entre instrucciones de manera más
            • Incremento en el tamaño del código                 eficiente.
              debido a la expansión del bucle.               Desventajas:
            • Necesidad de incluir iteraciones adi-
              cionales, lo que puede llevar a un uso           • Overhead asociado con el llenado y va-
              más intensivo de los registros.                    ciado del pipeline, que ocurre al inicio
                                                                 y al final del bucle.
            • Puede ejercer presión adicional sobre
              el uso de registros debido a la necesi-          • Puede haber un mayor costo en la ges-
              dad de almacenar múltiples resultados              tión de las dependencias entre instruc-
              intermedios.                                       ciones de diferentes iteraciones.

<!-- p. 102 -->

   Planificación estática: Una limitación de las técnicas de segmentación estática es que las ins-
trucciones se emiten en el mismo orden en que aparecen en el programa.

### Planificación Dinámica
    Las técnicas dinámicas son implementadas por hardware (no en tiempo de compilación). Requie-
ren agregar más componentes, lógica y combinacionales, con impacto en consumo y costo de diseño;
suelen rendir mejor que las técnicas estáticas.
    La planificación dinámica consiste, esencialmente, en la ejecución fuera de orden: ejecutar
instrucciones independientes apenas están listas. Si tengo LOAD → ADD → STORE → (otra instrucción
independiente), el compilador podría reordenar, pero con hardware dinámico el programa puede venir
“tal cual” y, en runtime, se ejecuta lo que ya está listo. Esto implica terminación fuera de orden.
¿Es un problema? Por las excepciones puede serlo; si no, no debería afectar el resultado.
    A nivel de etapas, se divide la decodificación en issue/decode y read operands; luego viene la
ejecución. Este enfoque se basa en el algoritmo de Tomasulo (IBM - 1967). No todos los procesadores
lo implementan: en embebidos suele evitarse por consumo, complejidad y costo (por ejemplo, en un
celular no conviene sacrificar batería).
    Con planificación dinámica, el hardware reorganiza la ejecución para reducir detenciones, man-
teniendo el pipeline y la consistencia del estado de procesador y memoria. Los riesgos estructura-
les se verifican al decodificar; así, aun respetando el orden del programa, las instrucciones comienzan
cuando sus operandos están disponibles. El procesador segmentado ejecuta fuera de orden y, en
consecuencia, termina fuera de orden.
    Es especialmente útil con múltiples unidades funcionales. Es clave diferenciar entre distribuir
instrucciones a unidades distintas y el momento en que comienzan a ejecutarse.
    A diferencia de la planificación estática (el compilador lanza instrucciones sin poder resolver en
ejecución todas las dependencias), en la dinámica el procesador modifica la secuencia en tiempo
de ejecución, resolviendo dependencias sin cambiar el resultado final. Las instrucciones se ejecutan
según la disponibilidad de datos y recursos, aprovechando el ILP cuando no hay dependencias.
    Al encargarse el hardware, esta técnica sirve para distintos códigos y dependencias descono-
cidas en compilación (por ejemplo, posiciones de memoria que dependen de literales). El compilador
se simplifica, pero el costo está en la complejidad del hardware.
   Ejemplo - Consideremos las siguientes instrucciones:
                                            Si estas instrucciones se ejecutan en orden,
       DIVD   F0, F2, F4         ; S1
                                            la etapa ID bloquea la ejecución en S2 hasta
       ADDD   F10, F0, F8        ; S2
                                            que se resuelva la dependencia (F0 disponible)
       SUBD   F12, F8, F14       ; S3
                                            y S3 tampoco puede ejecutarse hasta que esto
                                            suceda.

   Una solución consiste en dividir la etapa ID en dos etapas diferenciadas:

        Issue: Decodifica y chequea riesgos estructurales (chequea si están disponibles las unidades para
        hacer las operaciones).

<!-- p. 103 -->

      Lectura de operandos: Chequea disponibilidad de operandos. Debe implementarse para per-
      mitir el flujo de instrucciones. Está listo F2 y F4? si, bueno puedo seguir...

Ejecución de un fragmento de código sin planificación y con planificación dinámica

                                               Consideremos las siguientes latencias para las operacio-
       i1:        MULTD F0, F2, F6
                                               nes:
       i2:        ADDD F4, F0, F2
       i3:        ADDD F8, F2, F6                    Latencia de la unidad de multiplicación: 5 ciclos.
       i4:        SUBD F10, F6, F2
                                                     Latencia de la unidad de suma: 2 ciclos.

    En un sistema sin planificación, el procesador retiene el control hasta que finaliza la ejecución de
cada instrucción y obtiene el resultado de la primera operación (FO). Solo en ese momento se inicia la
ejecución del resto de las instrucciones. Para completar las cuatro instrucciones, se requieren 13 ciclos
de reloj.
    En un sistema con planificación dinámica, el proceso es más eficiente, ya que el sistema lanza las
instrucciones de manera continua, gestionando las dependencias entre ellas. Por ejemplo, cuando la
instrucción II3 tiene una dependencia con la instrucción I1, el sistema lo detecta automáticamente.
Sin embargo, las instrucciones I3 e I4 pueden avanzar sin problemas, ya que no dependen de I1 ni de
I2. Esto permite optimizar el uso del procesador y mejorar el rendimiento.

    Al haber una ejecución fuera de orden, las instrucciones finalizan también fuera de orden. La fina-
lización fuera de orden (que es una característica de la planificación dinámica) genera complicaciones
con respecto al manejo de excepciones. El comportamiento de excepciones debe ser preservado en el
sentido de que las excepciones deben ser generadas como serían si el programa se ejecutara en orden.
Se dice que la planificación dinámica puede generar excepciones imprecisas.

<!-- p. 104 -->

Excepciones Imprecisas
   Una excepción es imprecisa si al momento de generarse el estado del procesador no es el mismo
que tendría si las instrucciones hubieran sido ejecutadas en orden. Pueden ocurrir por dos situaciones:

      El pipeline ya ha completado instrucciones que son posteriores en el orden secuencial del pro-
      grama a la instrucción que genera la excepción.

      El pipeline aún no ha completado instrucciones que son anteriores a la que genera la excepción.

#### Algoritmo de Tomasulo (por Robert Tomasulo 1967)
                                  El algoritmo de Tomasulo es un método para manejar las dependencias
                                  de datos y mejorar la ejecución fuera de orden en procesadores. Es-
                                  te algoritmo detecta cuando los operandos para una instrucción están
                                  disponibles, reduciendo así los riesgos de dependencia de datos (EDE
                                  y EDL). También utiliza el renombrado de registros para eliminar los
                                  riesgos de dependencia de datos entre instrucciones.
    Figura 72: Robert Tomasulo.
   El algoritmo de Tomasulo resuelve tres tipos de riesgos:
          Riesgos de Dependencia de Datos en el
          tiempo de ejecución (LDE).                    Aplicación y Extensión
          Riesgos de Dependencia de Datos en el         El algoritmo se aplica principalmente a la unidad
          tiempo de decodificación de instrucciones     de operaciones de punto flotante. Sin embargo,
          (EDE).                                        es fácil extenderlo a las unidades de operaciones
                                                        con enteros, ya que el concepto de renombrado de
          Riesgos de Dependencia de Datos en el
                                                        registros y buffers de reserva también es aplicable
          tiempo de lectura de operandos (EDL).
                                                        a estas unidades.
   Para lograr esto, el algoritmo emplea:                     Unidad de Operaciones de Punto Flo-
          Renombrado de Registros: Se utilizan                tante: Utiliza el algoritmo para gestionar
          registros renombrados para evitar conflic-          las instrucciones que realizan cálculos com-
          tos entre instrucciones que escriben en el          plejos.
          mismo registro.                                     Unidad de Operaciones Enteras: Ex-
          Buffer de Reordenamiento: Permite                   tiende el algoritmo para manejar instruc-
          que las instrucciones sean ejecutadas fue-          ciones aritméticas y lógicas con enteros.
          ra de orden y luego se reordenan antes de     Casi todos los procesadores modernos utilizan
          escribir los resultados.                      mecanismos basados en el algoritmo de Tomasulo
          Buffer de Reserva: Cada unidad fun-           debido a su eficacia en la reducción de riesgos de
          cional mantiene un buffer para almacenar      dependencia de datos y su capacidad para mejo-
          las instrucciones que están esperando a sus   rar el rendimiento del procesador.
          operandos.

Estructura de un Procesador que utiliza el Algoritmo de Tomasulo
      Cola de operaciones de punto flotante: Se tiene una cola de instrucciones FIFO (ingresan
      en orden, salen en orden).

<!-- p. 105 -->

      Registros de Punto Flotante: Se disponen de cuatro registros FP a disposición del pro-
      gramador, los cuales forman parte de la arquitectura definida. Estos registros se utilizan para
      almacenar datos de punto flotante, empleados en operaciones aritméticas y lógicas. Cada registro
      tiene dos campos:

        • V: Indica el valor almacenado en el registro.
        • Q: Indica si el registro va a ser modificado por alguna operación. Si no hay ninguna ope-
          ración que modifique el registro, el valor de Q será cero. En caso contrario, Q tendrá una
          etiqueta (TAG), que es el nombre del resultado producido por la operación. Esta etiqueta
          está asociada al ID del slot de la estación de reserva que se encarga de dicha operación.

      El uso de etiquetas es parte del mecanismo conocido como Renombramiento de Registros.

     Figura 73: Estructura de un Procesador que utiliza el Algoritmo de Tomasulo (alternativa).

            Nota: A lo largo de este capítulo se utilizará la Figura 74 como esquema de referencia. Para reducir
            el tamaño de las imágenes intermedias no se muestran las conexiones entre los bloques.

      Unidades Funcionales de Punto Flotante: Se tienen las siguientes unidades funcionales:

        • Sumador FP: Para realizar sumas y restas.
        • Multiplicador FP: Para multiplicaciones y divisiones.

      Estaciones de Reserva: Las estaciones de reserva son estructuras que almacenan información
      sobre las instrucciones y sus operandos. Existen distintos tipos de estaciones de reserva para
      diferentes propósitos: Tres estaciones ADD. Seis estaciones LOAD. Dos estaciones MULT.
      Tres estaciones STORE.

<!-- p. 106 -->

                                                                                                                                                                               Apuntes Teóricos - Arquitectura de Computadoras
                                     Figura 74: Estructura de un Procesador que utiliza el Algoritmo de Tomasulo. Esta es la representación preferida en el presente apunte.

<!-- p. 107 -->

      Estaciones de Reserva para Instrucciones ADD y MULT: Las estaciones de reserva para
      instrucciones ADD y MULT están asociadas a la unidad funcional correspondiente. El conjunto
      de estas estaciones de reserva y su unidad funcional asociada se denomina unidad de ejecución.
      Cada slot de esta estructura contiene los siguientes campos:

        • Op: Indica el tipo de operación que se realizará en el slot de la estación de reserva.
        • Vi y Vk: Almacenan los valores de los operandos fuente necesarios para realizar la opera-
          ción. Estos valores pueden provenir de registros o de la estación de reserva, o del banco de
          registros.
        • Qj y Qk: Se utilizan como etiquetas para rastrear el estado de disponibilidad de los ope-
          randos fuente. Si Qj o Qk contienen un valor distinto de cero, significa que el operando
          correspondiente aún no está disponible y que la etiqueta apunta a la estación de reserva que
          está generando dicho operando. Cuando Qj o Qk son iguales a cero, indica que el operando
          correspondiente está disponible y la instrucción puede proceder con su ejecución.
        • Busy: Indica si el slot de la estación de reserva está ocupado o libre. Si está libre, puede
          ser utilizado por una nueva instrucción.

      Buffers de Carga y Buffers de Almacenamiento: Las estaciones de reserva para las ins-
      trucciones LOAD y STORE se denominan Load Buffers y Store Buffers, respectivamente.
      Estas estaciones están asociadas a la unidad de memoria (de datos). Cada slot de estos buffers
      incluye campos específicos para la dirección de memoria y el estado de disponibilidad del dato
      en memoria asociado a dicha entrada:

      Campos para Load Buffers

        • Dir: Dirección de memoria desde la cual se debe cargar el dato.
        • Valor: Después de que se completa la operación de carga, el valor correspondiente se
          almacena en este campo.
        • Busy: Indica si el slot de la estación de reserva está ocupado o libre.

      Campos para Store Buffers

        • Qi: Este campo representa una etiqueta que indica la estación de reserva LOAD asociada
          que proporciona el valor a almacenar en la memoria. La instrucción STORE necesita el
          valor almacenado en una estación de reserva LOAD antes de que pueda ejecutarse.
        • Dir: Almacena la dirección de memoria donde se almacenará el dato. Indica la ubicación
          en la memoria principal donde se guardará el valor.
        • Vi: Contiene el valor que se va a almacenar en la memoria. La instrucción STORE toma
          este valor y lo guarda en la dirección de memoria especificada por el campo Dir.
        • Busy: Similar a las estaciones de reserva LOAD, este campo indica si el slot de la estación
          de reserva STORE está ocupado o libre.

      Las instrucciones permanecen en las estaciones de reserva hasta que todos sus operandos estén
      disponibles y puedan ser emitidas para su ejecución.

      Common Data Bus (CDB): El Common Data Bus (CDB) es una vía de comunicación entre
      los componentes del sistema, con múltiples usos:

<!-- p. 108 -->

         • Envío de operandos: Cuando una instrucción necesita acceder a sus operandos, estos
           se transmiten a través del CDB desde el banco de registros a las estaciones de reserva
           asociadas.
         • Transferencia de resultados: Cuando una unidad funcional completa la ejecución y su
           resultado es necesario para otra instrucción, el resultado se transmite directamente desde la
           unidad funcional a la estación de reserva específica que está trabajando con esa instrucción.
         • Coordinación de accesos a memoria: Cuando se emite una instrucción de carga o
           almacenamiento, la dirección de memoria y los datos a leer o escribir se envían a través del
           CDB.
         • Actualización de registros: El CDB se utiliza para actualizar los registros adecuados
           después de recibir los resultados de las unidades funcionales. Cuando un resultado se trans-
           mite a través del CDB, se almacena en el registro correspondiente en el banco de registros.
           Esto asegura que los datos actualizados estén disponibles para las instrucciones posteriores
           que puedan necesitarlos.

      Debido a sus múltiples usos, este bus se convierte en un cuello de botella, ya que cada una de
      estas operaciones requiere que el bus esté disponible.

#### Etapas del Algoritmo de Tomasulo
Issue (Emisión de la instrucción) Se comienza por extraer una instrucción de la cola de instruc-
ciones. Si hay un slot libre en la estación de reserva correspondiente a la operación de la instrucción,
se envía la operación junto con los valores de los operandos a dicho slot y se actualiza el campo Busy,
indicando que el slot está ocupado.

      Si un operando está disponible, se guarda en el campo correspondiente y la etiqueta Q será cero,
      indicando que el operando está listo.

      Si un operando no está disponible, la etiqueta Q indicará el ID del slot de la estación de reserva
      que generará el operando solicitado, y el campo V estará vacío.

    Si no hay un slot libre en la estación de reserva para la unidad funcional requerida, existe un riesgo
estructural, y se detiene la alimentación de instrucciones hasta que quede libre algún slot.

Ejecución Una vez que los datos de la instrucción se encuentran en la estación de reserva, el com-
portamiento dependerá de la disponibilidad de los operandos:

      Si algún operando no está disponible (se cuenta con la etiqueta Q correspondiente), se monitorea
      el Common Data Bus (CDB) hasta que el dato aparezca acompañado de la misma etiqueta, es
      decir, hasta que los operandos estén listos. Cuando esto ocurre, el dato se guarda en el campo
      correspondiente del operando en el slot de la estación de reserva.

      Cuando todos los operandos de la instrucción asociada al slot están listos, se comienza su ejecu-
      ción.

    Esto soluciona riesgos de Load Data Execution (LDE), ya que no se comenzará a ejecutar la ins-
trucción hasta que todos los operandos estén listos. Si varias instrucciones están listas al mismo tiempo
y utilizan módulos distintos (por ejemplo, suma y multiplicación), pueden ejecutarse simultáneamente.

<!-- p. 109 -->

Escritura de Resultados Cuando un resultado está listo, el Common Data Bus (CDB) llevará el
dato al registro correspondiente, así como a las estaciones de reserva que lo necesiten. Las etiquetas
Q que apuntaban al ID de quien produjo este resultado se actualizan, indicando que el operando está
listo.
    Además, el slot de la estación de reserva asociado a ese resultado se marca como disponible, de
manera que pueda ser utilizado para otra instrucción.
    No se chequean riesgos de Execution Data Execution (EDE) ni de Execution Data Load (EDL), ya
que son eliminados por el Renombramiento de Registros.

   ER: ESTACIÓN DE RESERVA

#### Ejemplo 1 TOMASULO: Ejecución de Secuencia

               Figura 75: Ciclo i – Issue: se reserva la estación y se renombran registros.

               Figura 76: Ciclo n – Primer operando listo: llega el valor de Y por CDB.

<!-- p. 110 -->

          Figura 77: Ciclo m – Operandos listos: se resuelven Y y Z, la ALU puede ejecutar.

             Figura 78: Ciclo W – Writeback: resultado escrito en F 0, estación liberada.

#### Ejemplo 2 TOMASULO

         Código                              Supuestos
         LD       F6 , 34(R2)                      Operation latencies: load/store 2 cycles,
         LD       F2 , 45(R3)
         MULTI    F0 , F2    ,F4                   Add/sub 2 cycles,
         SUBD     F8 , F6    ,F2
         DIVD     F10 , F0   ,F6                   Mult 10 cycles,
         ADD      F6 , F8    ,F2                   Divide 40 cycles

          El Issue ocurre cuando la instrucción abandona la cola FIFO de instrucciones (simboli-
          zada en gris en los diagramas).

          En la estación de reserva, los campos Qj y Qk indican qué instrucción está produciendo
          el valor de Vj o Vk .

          Cuando ambos Qj y Qk son iguales a 0, significa que los operandos ya están disponibles
          y la instrucción puede comenzar su ejecución.

<!-- p. 111 -->

Solución → Inicia en el ciclo 0

                              Figura 79: Ciclo 1 – Estado inicial del ejemplo.

                           Figura 80: Ciclo 2 – Se disparan las primeras cargas.

                           Figura 81: Ciclo 3 – Inicio de la instrucción MULTD.

<!-- p. 112 -->

                           Figura 82: Ciclo 4 – SUBD entra en estación de suma.

                           Figura 83: Ciclo 5 – Se preparan DIVD y dependencias.

                           Figura 84: Ciclo 6 – ADDD queda esperando operandos.

<!-- p. 113 -->

                    Figura 85: Ciclo 7 – Ejecución en paralelo de varias estaciones.

                    Figura 86: Ciclo 8 – Resultados parciales se propagan por CDB.

               Figura 87: Ciclo 13 – Resolución de dependencias entre SUBD y ADDD.

<!-- p. 114 -->

                           Figura 88: Ciclo 16 – Se actualizan registros destino.

                              Figura 89: Ciclo 57 – Estado final del ejemplo.

   La tabla 90 demuestra claramente que la ejecución fue fuera de orden. Aunque las instruc-
   ciones se emitieron en secuencia (LD, LD, MULT, SUBD, DIVD, ADDD), el orden de finalización y
   escritura de resultados difirió:

         SUBD (emitida cuarta) completó y escribió en el ciclo 8, antes que la MULT (emitida tercera)
         que recién terminó en el ciclo 16.

         ADDD (última en emitirse) finalizó y escribió en el ciclo 11, bastante antes que la DIVD, que
         terminó en el ciclo 57.

   Esto confirma que el procesador con el algoritmo de Tomasulo permite out-of-order execu-
   tion, resolviendo dependencias dinámicamente y maximizando el uso de las unidades funciona-
   les.

<!-- p. 115 -->

Figura 90: Tabla de estados de las instrucciones mostrando Issue, Execution complete y Write
Result.

#### Ejemplo 3 TOMASULO: Renombrado Dinámico en un Loop Unrolling
    Se mostrará un caso en el que los resultados de las unidades funcionales no se guardan en registros si
no que una vez que se produce el resultado, pasan directamente a la estación de reserva correspondiente,
pues una instrucción posterior debe modificar los mismos registros antes de que la primera operación
se complete:

         Loop Example                                Multiply toma 4 ciclos.

         Loop:    LD    F0 , 0(R1)                   La primera carga (miss L1 cache) toma 8 ciclos.
                  MULTD F4 , F0    , F2
                                                     La segunda carga (hit en L1 cache) toma 1 ciclo.
                  SD    F4 , 0(R1)
                  SUBI R1 , R1     , #8              Mostramos los ciclos para SUBI y BNEZ.
                  BNEZ R1 , Loop
                                                     En realidad, las instrucciones enteras están ade-
                                                     lante de las instrucciones de punto flotante.

Solución (Mostramos 2 iteraciones)

                                           Figura 91: Ciclo 2

<!-- p. 116 -->

                           Figura 92: Ciclo 3

                           Figura 93: Ciclo 4

                           Figura 94: Ciclo 5

<!-- p. 117 -->

                           Figura 95: Ciclo 6

                           Figura 96: Ciclo 7

                           Figura 97: Ciclo 8

<!-- p. 118 -->

                            Figura 98: Ciclo 9

                           Figura 99: Ciclo 10

                           Figura 100: Ciclo 11

<!-- p. 119 -->

                           Figura 101: Ciclo 12

                           Figura 102: Ciclo 13

                           Figura 103: Ciclo 14

<!-- p. 120 -->

                           Figura 104: Ciclo 15

                           Figura 105: Ciclo 16

                           Figura 106: Ciclo 17

<!-- p. 121 -->

                           Figura 107: Ciclo 18

                           Figura 108: Ciclo 19

                           Figura 109: Ciclo 20

<!-- p. 122 -->

                  ITER       Instruction           j    k    Issue     Comp      Result
                    1        LD F0, 0(R1)         F0     0     1         9        10
                    1      MULTD F4, F0, F2       F4    F0     2        14        15
                    1        SD F4, 0(R1)         F4     0     3        18        19
                    2        LD F0, 0(R1)         F0     0     6        10        11
                    2      MULTD F4, F0, F2       F4    F0     7        15        16
                    2        SD F4, 0(R1)         F4     0     8        19        20

         Cuadro 5: Estado de las instrucciones con sus ciclos de emisión, ejecución y escritura.

#### Nomenclatura TOMASULO
      Instrucción aritmética: D ← OP (S1, S2)
      Instrucción aritmética que realiza la operación OP sobre el contenido de los registros S1 y S2,
      y deposita el resultado en el registro D.

      Instrucción Load: D ← Mem[Dirección]
      Carga en el registro D el contenido de la posición de memoria Dirección.

      Instrucción Store: Mem[Dirección] ← S
      Almacena el contenido del registro S en la posición de memoria Dirección.

      Estación de reserva x: ER(x)(Busy, OP, Qj, Vj, Qk, Vk)

      Registro x: Reg(x)(Qi, Vi)

      Load Buffer x: LB(x)(Busy, Dir)

      Store Buffer x: SB(x)(Busy, Dir, Qi, Vi)

Descripción de los Campos
      ER(x): Este slot de la estación de reserva generará el resultado x.

      ER(x).Busy: Indica si el slot de la estación de reserva está ocupado o no.

      ER(x).OP: Operación a realizar en ese slot de la estación de reserva.

      ER(x).Qj: Etiqueta que indica 0 si el operando j está disponible. En caso contrario, indica el
      nombre del resultado esperado o el ID del slot de la estación de reserva que lo genera.

      ER(x).Vj: Valor del operando j (o nada si el operando no está disponible).

      ER(x).Qk y ER(x).Vk: Ídem para el operando k.

      Reg(x): Registro x.

      Reg(x).Qi: Indica si el valor del registro está disponible (Qi = 0). En caso contrario, indica el
      nombre del resultado esperado o el ID del slot de la estación de reserva que lo genera.

      Reg(x).Vi: Valor del registro x (o nada si el valor no está disponible).

      LB(x): Trae el valor x de la memoria.

      LB(x).Dir: Dirección de la memoria en donde se encuentra el valor x.

<!-- p. 123 -->

      LB(x).Busy: Indica si el slot del Load Buffer está ocupado o libre.

      SB(x): Se almacena el valor x en la memoria.

      SB(x).Vi: Valor de x.

      SB(x).Dir: Dirección donde se debe almacenar el valor x.

      SB(x).Qi: Indica si el valor x está disponible (Qi = 0). En caso contrario, indica el nombre del
      resultado esperado o el ID del slot de la estación de reserva que lo genera.

      SB(x).Busy: Indica si el slot del Store Buffer está ocupado o libre.

    Esta nomenclatura se utiliza para explicar las fases del algoritmo de Tomasulo en cada tipo de
instrucción.

                                  Figura 110: Fase Issue (Emisión).

<!-- p. 124 -->

                           Figura 111: Fase Ejecución.

                           Figura 112: Fase Escritura.

<!-- p. 125 -->

#### Ventajas y Desventajas de Tomasulo

       Elimina cuellos de botella en los registros, ya que los datos se copian y los registros quedan libres
       para su uso.

       Evita riesgos de Execution Data Load (EDL) y Execution Data Execution (EDE), a diferencia
       de los enfoques estáticos.

       Permite el unrolling en hardware, facilitando la ejecución eficiente de bucles.

       No está limitado a bloques básicos, ya que no habría dependencias de saltos.

Desventajas

       Complejidad: En cada estación de reserva (ER), es necesario comparar y acceder tanto en lectura
       como en escritura a los mismos buses.

       Genera muchas cargas de registros, lo que puede impactar en el rendimiento.

       El Common Data Bus (CDB) limita el rendimiento al ser un recurso compartido por las diferentes
       unidades.

       Excepciones imprecisas: Las instrucciones pueden no ejecutarse en el orden programado, dificul-
       tando el manejo preciso de excepciones.

### Tratamiento de Dependencias de Control
Reducir la penalidad de saltos implica determinar rápidamente si se tomará el salto o no.
   En un programa, aproximadamente 5/6 de los saltos son tomados y solo 1/6 no lo son. Esto
surge de la siguiente clasificación:

       Saltos incondicionales: siempre tomados (≈ 33 %).

       Saltos condicionales de bucle: tomados casi siempre (salvo la última iteración, ≈ 33 %).

       Otros condicionales: tomados en promedio el 50 % de las veces (≈ 16,6 % tomados y 16,6 %
       no tomados).

Problemas en el pipeline         Cada salto genera dos dificultades principales:

   1. Incertidumbre del flujo: hasta resolver la condición, el procesador no sabe qué instrucción
      cargar a continuación en el pipeline.

   2. Cálculo de la dirección: en caso de tomarse el salto, se debe calcular la nueva dirección de
      destino, lo que introduce demoras.

<!-- p. 126 -->

Impacto

      Cada 7–8 instrucciones, en promedio, aparece un salto.

      Esto provoca stalls en el pipeline, aumentando el CPI (Cycles Per Instruction).

      En el mejor de los casos, implica al menos un ciclo de burbuja; en el peor, vaciar el pipeline y
      cargar la nueva dirección.

Figura 113: Clasificación y frecuencia de saltos en un programa típico. En promedio, un sexto de los
saltos no se toman.

Importancia de la predicción de saltos: Es fundamental predecir correctamente los saltos, ya
que una predicción precisa promete una ejecución continua del programa. Si la predicción falla, se
pierden ciclos de reloj, lo que impacta negativamente en el rendimiento.

<!-- p. 127 -->

Figura 114: La Frecuencia de los saltos depende del tipo de programa. Además, el comportamiento
depende del tipo de programa.

#### Predicción de Saltos
   La solución al problema de los saltos en el pipeline combina dos técnicas clave:

Predicción (Branch Prediction)

      Consiste en adivinar si un salto será tomado o no tomado.

      Permite continuar cargando instrucciones en el pipeline sin esperar a conocer el resultado real
      de la condición.

      Ejemplo: asumir siempre “tomado” o siempre “no tomado”, o utilizar algoritmos más avanzados
      basados en el historial de ejecución.

Especulación (Speculative Execution)

      Es la acción de ejecutar provisionalmente las instrucciones del camino predicho.

      Estas instrucciones solo se confirman cuando se resuelve la condición del salto.

      Si la predicción fue correcta, se gana tiempo porque el pipeline no se detuvo.

      Si la predicción fue incorrecta, se deben descartar las instrucciones especulativas y retomar el
      camino correcto, con el costo de perder ciclos.

Resumen

      Predicción: elegir el camino probable (tomado o no tomado).

      Especulación: ejecutar ese camino elegido de forma provisional.

Impacto Cuando la predicción acierta, el procesador evita stalls en el pipeline y reduce el CPI.
Cuando falla, se penaliza el rendimiento porque deben descartarse las instrucciones mal especuladas
y recargar el flujo correcto.

Idea Básica: Cuando se detecta una instrucción de salto condicional sin resolver, se debe predecir
el camino del salto:

      Se supone o predice el camino del salto: tomado (Taken) o no tomado (Untaken).

      Si se predice que el salto será tomado, también se predice la dirección de destino del salto.

      La ejecución continúa de forma especulativa a lo largo del camino supuesto.

Cuando se resuelve la condición del salto:

      Si la predicción fue correcta: La ejecución se confirma y continúa normalmente.

      Si la predicción fue incorrecta (fallo de predicción o misprediction): Se descartan todas las ins-
      trucciones ejecutadas especulativamente y se reanuda la ejecución a lo largo del camino correcto.

<!-- p. 128 -->

Problemas a Resolver ante Instrucciones de Salto:

      Predicción del salto: Predecir si el salto se tomará o no:

        • UNTAKEN (No Tomado): Predecir que el salto no se tomará.
        • TAKEN (Tomado): Predecir la dirección de destino del salto en caso de que se tome,
          minimizando el retardo.

Penalización por Saltos:

      Si la predicción de salto tomado es correcta, la penalización será de solo un ciclo (suponiendo
      que no se está utilizando salto retardado).

      Si la predicción de salto no tomado es correcta, no habrá penalización, es decir, el retardo será
      de 0 ciclos.

      Si la predicción es incorrecta (ya sea de salto tomado o no tomado), se necesitarán al menos dos
      ciclos para vaciar el pipeline y retomar la ejecución correcta.

Figura 115: Predecir la dirección de la instrucción destino del salto con un retardo (para saltos
tomados)

<!-- p. 129 -->

    Para predecir la dirección del salto de manera eficiente, es necesario detectarlo lo más pronto
posible. Cuando se realiza un salto “I”, se puede guardar la dirección de destino de dicho salto. Así,
cuando se vuelva a ejecutar el mismo salto “I”, se accederá a esta dirección previamente almacenada
en lugar de calcularla nuevamente. Para esto se utiliza:

### Branch Target Address Cache (BTAC)
    La BTAC es una memoria caché que almacena la dirección de destino de los últimos saltos tomados,
evitando recalcular la dirección en cada instrucción de salto.

Funcionamiento        Cuando se accede a una instrucción de salto:

       Se consulta en paralelo la BTAC utilizando como índice la dirección de la instrucción de salto.

       Si la instrucción está presente en la BTAC y el salto se predice como tomado, la dirección de
       destino se lee directamente desde la BTAC y se utiliza en el pipeline.

       Si no está presente o el salto se predice como no tomado, se continúa con la secuencia normal
       de ejecución (P C + 4).

                  Figura 116: Esquema de la Branch Target Address Cache (BTAC).

Qué no hace la BTAC La BTAC no decide si el salto será tomado o no; sólo provee la dirección
destino si hay hit. La decisión taken/not taken proviene de un predictor de dirección (p. ej., BHT
con contadores saturantes de 1 o 2 bits, o reglas estáticas).

Selección de la siguiente dirección (etapa IF) En la etapa de Fetch se consulta en paralelo la
BTAC con el PC actual:
                               
                               BTAC[PC].target     si pred_taken=1 y BTAC-hit,
                   next_PC =
                               PC + 4              si pred_taken=0 o BTAC-miss.

Operativamente, un MUX selecciona entre PC+4 y el target entregado por la BTAC, controlado por
la predicción.

<!-- p. 130 -->

Actualización de la BTAC

      Cuando se resuelve la instrucción de salto y se confirma que fue tomado:

         • Si ya estaba en la BTAC, se actualiza la dirección destino.
         • Si no estaba, se inserta una nueva entrada.

      Si el salto no fue tomado y estaba en la BTAC, la entrada se elimina.

Consideraciones de diseño

      No es posible iterar secuencialmente sobre todas las entradas para encontrar coincidencias, ya
      que sería demasiado costoso en ciclos.

      Buscar en paralelo en todas las posiciones implicaría un alto consumo de hardware y energía.

      Por ello, se usan estructuras de tipo caché asociativa (similar a las memorias caché de datos
      e instrucciones).

Llamadas y retornos (returns) Los retornos cambian de destino en cada invocación; por eso se
usa un Return Address Stack (RAS):

      Al ejecutar una call se empuja PC+4.

      Al ejecutar return se saca la dirección de retorno predicha.

La BTAC por sí sola no predice bien los return por su variabilidad.

Nomenclatura En la literatura se usan BTAC/BTB casi como sinónimos: ambos almacenan el
target. Algunos BTB también incluyen bits de predicción; aquí distinguimos: BTAC = target, BHT
= dirección (taken/not).

Predicción estática en embebidos En varios ARM Cortex-R/M y entornos embebidos se usa
por simplicidad la regla “siempre no tomado” (o backward taken / forward not taken). Ventaja:
no hay que calcular destino si acierta; desventaja: estadísticamente conviene “tomado” pero requiere
BTAC/BTB para no pagar el cálculo del destino.

Resumen

      Dos piezas: predictor de dirección (BHT) + predictor de destino (BTAC/BTB).

      Si acierta: se evitan stalls; si falla: flush de especulación y penalidad.

   Existen distintos tipos de memoria caché para almacenar y acceder a las direcciones de destino
de los saltos en la BTAC (acceso directo, totalmente asociativa y asociativa por conjuntos). Cada
una de estas opciones tiene sus propias ventajas y desventajas en términos de costo, complejidad y
rendimiento (ver unidad 5).

#### Clasificación de Técnicas de Predicción de Saltos
   La predicción de saltos puede clasificarse en dos categorías: estática y dinámica. Estas se dife-
rencian en el momento en que se realiza la predicción y presentan ventajas e inconvenientes distintos.

<!-- p. 131 -->

#### Predicción Estática
rante la ejecución. En algunas implementaciones, puede incrementar considerablemente la longitud
del ejecutable, llegando hasta un 30 % de aumento. Aunque esta técnica tiene una menor precisión
en comparación con la predicción dinámica, ofrece la ventaja de no requerir una mayor inversión en
hardware.
    Existen diversas técnicas de predicción estática de saltos. Las más sencillas se basan en las propie-
dades estáticas de los saltos, como su código de operación o su dirección destino, mientras que las más
complejas utilizan profiling, es decir, realizan ejecuciones previas para obtener medidas que permitan
deducir estáticamente el comportamiento del salto.

Predicción Dinámica: Se lleva a cabo en tiempo de ejecución, lo que permite adaptarse al compor-
tamiento real de los saltos durante la ejecución del programa. Esto proporciona una mayor precisión
en la predicción, pero a costa de un mayor costo de hardware.
    Las técnicas de predicción dinámica utilizan información histórica:

      Local: Basada en el comportamiento de los saltos en una dirección específica.

      Global: Basada en el comportamiento de todos los saltos en el programa.

      Combinada: Utiliza una mezcla de ambas fuentes de información.

                      Figura 117: Clasificación de técnicas de predicción de saltos.

3.8.2.   Predicción Estática
Predicción Estática Fija Esta técnica implica predecir todos los saltos como siempre tomados o
siempre no tomados. Si se predice que el salto siempre será tomado, se obtendrá un mayor número
de aciertos de predicción (aproximadamente el 75 % de los saltos condicionales son tomados). Sin
embargo, esto conlleva un mayor costo de hardware, ya que se requiere almacenar las direcciones de
destino de los saltos. Por otro lado, si se predice que el salto nunca será tomado, se tendrá un menor
número de aciertos de predicción (solo el 25 % de los saltos condicionales son no tomados), pero con
un menor costo de hardware.

Predicción Estática Basada en la Dirección Esta técnica utiliza la dirección del salto para hacer
la predicción. Los saltos hacia atrás, que suelen corresponder a bucles, se predicen como tomados, ya
que generalmente se repiten múltiples veces. Por otro lado, los saltos hacia adelante, que suelen estar
asociados a estructuras if-then-else, se predicen como no tomados. Esta técnica funcionará bien en

<!-- p. 132 -->

programas con muchos bucles, pero puede comportarse de manera deficiente en programas con pocos
bucles y muchas estructuras if-then-else.

Predicción Estática Basada en el Código de Operación En esta técnica, se utiliza el código de
operación (opcode) de la instrucción de salto para realizar la predicción. Se establecen reglas basadas
en estudios que muestran que, para distintos códigos de operación, la probabilidad de que un salto
sea tomado o no es diferente. Lee y Smith realizaron un estudio del comportamiento de los saltos
según su código de operación para el IBM 370, observando que para ciertos códigos de operación la
probabilidad de que un salto sea tomado es bastante alta (del orden del 80 %-90 %).

Predicción Estática Dirigida por el Compilador En esta técnica, el compilador proporciona
información al hardware sobre la predicción de saltos. Existen diferentes enfoques:

      Predicción basada en el tipo de construcción: El compilador predice si el salto será tomado
      o no en función del tipo de construcción de control, como if, for o while.

      Predicción basada en profiling: El compilador realiza ejecuciones previas del programa y
      utiliza la información recopilada sobre el comportamiento de las instrucciones de salto para
      hacer la predicción.

      Predicción especificada por el programador: El programador indica al compilador si el
      salto debe predecirse como tomado o no mediante directivas específicas en el código fuente. Se
      puede añadir un bit de predicción al opcode de la instrucción para indicar la predicción.

#### Predicción Dinámica

Figura 118: La predicción dinámica se realiza observando el comportamiento de las instrucciones de
salto en las ultimas ejecuciones (local o globalmente).

Predictor de un Bit
   El predictor de 1 bit utiliza un único bit de historia para cada instrucción de salto. Este bit
almacena el resultado de la última ejecución del salto:

      Si fue tomado, se predice que volverá a ser tomado.

      Si fue no tomado, se predice que volverá a ser no tomado.

<!-- p. 133 -->

   En otras palabras, este predictor recuerda únicamente el último estado, y asume que el
comportamiento se repetirá.
        Implementado como una máquina de dos estados:

             • Estado 0: No tomado.
             • Estado 1: Tomado.

          Se utiliza un contador saturado de 1 bit.
                                                                     Figura 119: Máquina de estados del
          La predicción es directamente el valor de ese bit.         predictor de 1 bit.

      Tras ejecutar el salto, el bit se actualiza según el resultado real:

         • Si fue tomado: el bit se pone en 1.
         • Si no fue tomado: el bit se pone en 0.

Limitaciones

      Solo captura el resultado de la última ejecución del salto.

      Produce dos predicciones incorrectas en los cambios de comportamiento:

         • Cuando un bucle finaliza (última iteración).
         • Cuando se alterna entre tomado y no tomado.

      Es especialmente ineficiente en bucles anidados o patrones alternantes (T, NT, T, NT, ...),
      donde el historial de un solo bit no refleja el verdadero comportamiento.

Eficiencia

      En bucles simples de muchas iteraciones es muy efectivo: Por ejemplo, en un bucle de 1000
      iteraciones, acertará en 999 casos y fallará solo en 2.

      En cambio, en bucles anidados o saltos con comportamiento irregular, su desempeño se degrada
      drásticamente, llegando a fallar en la mitad de las predicciones.

Resumen El predictor de un bit es la forma más simple de predicción dinámica: bajo costo de hard-
ware, razonablemente efectivo para bucles simples, pero insuficiente para escenarios más complejos.
Estos problemas motivan el uso de contadores de 2 bits, que reducen el impacto de los cambios
ocasionales en el comportamiento del salto.

#### Predictor de Dos Bits (Bimodal)
   Este predictor utiliza dos bits de predicción por cada instrucción de salto, reflejando el comporta-
miento de las últimas dos ejecuciones de ese salto.

Predicción:

      Un salto que se toma repetidamente se predice como Taken.

      Un salto que no se toma repetidamente se predice como Not Taken.

      Si un salto toma una dirección inusual una sola vez, el predictor mantiene la predicción usual.

<!-- p. 134 -->

Funcionamiento:

      Máquina de cuatro estados:
      Registro de historia: Contador saturado de 2 bits.
      Predicción: Se basa en el bit más significativo del registro de historia.

Comportamiento:
      Bucle simple: Inicialmente, el predictor necesita ajustarse, lo que genera predicciones erróneas.
      Sin embargo, una vez que el patrón de ejecución se establece, el predictor aprende a predecir
      correctamente el salto como Taken en las siguientes iteraciones, aumentando el porcentaje de
      aciertos.
      Bucle dentro de otro bucle: Se producen aproximadamente un 50 % menos de predicciones
      erróneas en comparación con el predictor de 1 bit.
    Este predictor es más efectivo al correlacionar mejor debido a la mayor memoria, aunque su costo
es más alto, ya que requiere dos bits de almacenamiento por cada instrucción de salto que está siendo
rastreada en la ventana de la caché (una tabla o matriz donde se almacenan los registros asociados a
las instrucciones de salto que están siendo rastreadas por el predictor).

Ejemplo: for(1000)
      Predictor de 1 bit:
        • Arranca prediciendo Not Taken.
        • Falla la primera vez (porque en realidad el salto es Taken).
        • Aprende y predice Taken en todas las siguientes iteraciones.
        • Falla nuevamente en la última vez (cuando el salto ya no se toma).
      ⇒ Total: 2 fallos (independientemente del tamaño del bucle).
      Predictor de 2 bits:
        • Arranca en Fuertemente no tomado (00).
        • Falla la primera vez y avanza al estado Débilmente no tomado (01).
        • Vuelve a fallar y pasa a Débilmente tomado (10).
        • Acierta en todas las siguientes iteraciones mientras se mantiene en Tomado.
        • Al salir del bucle falla una vez más.
      ⇒ Total: 3 fallos (independientemente del tamaño del bucle).

<!-- p. 135 -->

Ejemplo: for(1000){ for(1000)} (bucles anidados)

      Predictor de 1 bit:

         • Cada vez que termina el bucle interno, el predictor falla 2 veces (una al salir y otra al
           reingresar en la siguiente vuelta).
         • Con 1000 iteraciones del bucle externo, esto produce ∼ 2000 fallos adicionales.
         • A esto se suman los 2 fallos del bucle externo.

      ⇒ Total: 2002 fallos.

      Predictor de 2 bits:

         • En el primer paso de aprendizaje, comete 3 errores (igual que en el caso simple).
         • Luego, al salir y volver a entrar al bucle interno, no cambia inmediatamente de estado
           gracias a los 2 bits: mantiene la predicción de Taken.
         • Esto significa que las reentradas del bucle interno casi no generan fallos adicionales.
         • Solo falla en las salidas definitivas de cada bucle.

      ⇒ Total: ∼ 1003 fallos, es decir, aproximadamente la mitad que el predictor de 1 bit.

#### Implementación
    Las dos estrategias más comunes para almacenar la información sobre las ejecuciones anteriores
de instrucciones de salto son:

 Buffer de Destino de Saltos BTB (Branch Target Buffer)
  Añade bits de predicción a las entradas de la BTAC. La BTAC con bits de predicción se denomina
BTB, que es una estructura que almacena en cada entrada:

                                   BTB = BTAC + bits de predicción

      Un tag con la instrucción de salto.

      La dirección de destino del último salto tomado (BTA = Branch Target Buffer).

      Los bits de predicción de ese salto.

<!-- p. 136 -->

   Actualización de la BTB: Los campos de la BTB se actualizan después de ejecutar el salto,
según:

      Si el salto fue tomado o no ⇒ Actualizar bits de predicción.
      La dirección de destino del salto ⇒ Actualizar la BTA.

Predicción Implícita (sin bits de predicción)
   Aplicable con un solo bit de predicción.

      Si la instrucción de salto está en la BTB ⇒ el salto se predice como tomado.
      Si la instrucción de salto no está en la BTB ⇒ el salto se predice como no tomado.

    Ejemplos: MC 68060: 256 x 2 bit, Pentium: 256 x 2 bit, R8000: 1K x 1 bit, PM1: 1K x 2 bit,
Pentium II: 512 x 2 bit, Pentium 4: 4K x 2 bits
    Desventaja: Sólo se puede predecir aquellas instrucciones de salto que están en la BTB. Si la
dirección de la instrucción de salto no está presente en la BTB, no se puede realizar una predicción
válida.

Tabla de Historia de Saltos BHT (Branch Table History)
   La Tabla de Historia de Saltos (BHT) mantiene un registro del historial de comportamiento
de saltos en el programa. Cada entrada en la tabla corresponde a una dirección de instrucción y
almacena información sobre si el salto en esa dirección ha sido tomado o no en ejecuciones anteriores.
   Dependiendo de la implementación, la BHT puede utilizar diferentes esquemas de almacenamiento.
Generalmente existen dos tablas:

<!-- p. 137 -->

      La BTAC (Branch Target Address Cache) almacena la dirección de destino de los últimos
      saltos tomados.

      La BHT (Branch History Table) almacena los bits de predicción de todas las instrucciones
      de salto condicional. Para cada salto, la BHT guarda información sobre si fue tomado o no en
      ejecuciones anteriores.

    Ventaja: Puede hacer predicciones para instrucciones que no están en la BTAC, ya que la BHT
tiene una mayor capacidad de almacenamiento, almacenando información para todas las instrucciones
de salto del programa, independientemente de si están presentes en la BTAC.
    Desventaja: Aumenta el hardware necesario (dos tablas asociativas).

Acceso a la BHT
    La BHT se accede utilizando los bits menos significativos de la dirección del salto. En lugar de
utilizar etiquetas (tags) para identificar las entradas en la tabla, se utiliza una dirección parcial, lo que
reduce el costo del hardware. Sin embargo, este enfoque puede tener un impacto en el rendimiento, ya
que el comportamiento de las entradas puede degradarse debido a la falta de etiquetas distintivas.

Asociativa por conjuntos
    Una opción para reducir el costo de hardware de la BHT es implementarla como una tabla asocia-
tiva por conjuntos. En este enfoque, las tablas asociativas se reducen en tamaño, lo que resulta en un
mayor costo. Sin embargo, esto permite mantener un comportamiento similar a una implementación
de tablas más grandes para un costo de hardware dado.
    Ejemplos: Gmicro 100: 256 x 1 bit, PowerPC 604: 512 x 2 bit, R10000: 512 x 2 bit, PowerPC 620:
2K x 2 bit, PA 8000: 256 x 3 bit, Alpha 21164A: 2K x 2 bit, AMD64: 16K x 2 bits

<!-- p. 138 -->

Comportamiento de los Predictores Dinámicos
    Prácticamente no hay mejora al aumentar la cantidad de entradas, por lo que es inútil seguir
aumentando el número de entradas. Para algunos programas (ej. programas con enteros), hay dema-
siados fallos. Esto se debe a que el método de predicción no es asertivo, ya que la predicción se basa
únicamente en dónde se produce el salto.

Otras Formas de Predicción (Predictores Correlacionados ⇒ Historia Global)
Patrones Repetitivos
   1. Muchas instrucciones de salto ejecutan patrones repetitivos.

    Idea: Los saltos no son siempre independientes, sino que siguen un patrón. El comportamiento
de los últimos n saltos de una misma instrucción de salto afecta la predicción actual. En este caso se
guarda un registro con la historia reciente de ese salto y se usa como índice para decidir la predicción.

                Figura 120: Ejemplo de predicción repetitiva basada en historia local.

Predicción basada en historia LOCAL

      La historia se guarda de manera local a un solo salto, no a otros.

      No es una máquina de estados tradicional de 1 o 2 bits, sino un registro que guarda explícitamente
      el comportamiento de las últimas n ejecuciones (ej: 3 últimos resultados).

      Cada patrón registrado se asocia a una predicción.

                           Historia (últimos 3 saltos)   Predicción siguiente
                                       111                  0 (No Tomado)
                                       011                    1 (Tomado)
                                       101                    1 (Tomado)
                                       110                    1 (Tomado)

Ejemplo: Si los últimos cuatro saltos fueron: T, T, T, NT, entonces el predictor local registra ese
patrón y decide la predicción para la siguiente ejecución en función de la entrada correspondiente en
la tabla.
    De esta forma, si el comportamiento del salto es repetitivo (por ejemplo, siempre Tomado, Tomado,
No Tomado), el predictor es capaz de aprender esa secuencia y anticipar correctamente el resultado.

Predictores Globales
   Muchas instrucciones de salto dependen del comportamiento de otros saltos recientes (historia
global).

<!-- p. 139 -->

   Si conocemos el comportamiento de la última ejecución de b1, podemos predecir el comportamiento
de b2 en la siguiente ejecución. Esto se conoce como Predicción basada en historia GLOBAL.

Comportamiento del predictor de un bit (estado inicial: ”not taken”, NT)
    Caso 1: d = 0, 1, 2, . . .

                      Valor de d       d ̸= 0?   b1    d antes de b2      d ̸= 1?    b2
                          0               no     NT          1               no      NT
                          1               sí      T          1               no      NT
                          2               sí      T          2               sí       T

   Conclusión: Si b1 no se toma, entonces b2 tampoco se toma. Esto indica una correlación entre
saltos.

Caso 2: d = 2, 0, 2, 0, . . .
   Este es un peor caso para los predictores locales. La variable d alterna permanentemente entre
dos valores, lo que provoca que el predictor de un bit nunca logre estabilizarse y falle en cada intento.

Ejecución paso a paso
           d   Pred. b1          Resultado   Nuevo b1       Pred. b2    Resultado      Nuevo b2
           2     NT                  T          T             NT            T             T
           0      T                 NT         NT              T           NT            NT
           2     NT                  T          T             NT            T             T
           0      T                 NT         NT              T           NT            NT

Análisis
      El predictor de un bit (b1) arranca en Not Taken.

      Cada salto contradice la predicción previa, forzando a actualizar el bit en la dirección opuesta.

      Como el patrón alterna constantemente (2 → 0 → 2 → 0), el predictor nunca converge: falla en
      todas las iteraciones.

Conclusión Este ejemplo muestra que el predictor de un bit se vuelve completamente ineficaz
ante patrones alternados, generando fallos de predicción en el 100 % de los saltos. En este tipo
de flujo, los predictores locales de 1 bit no son útiles, ya que no logran capturar la regularidad del
comportamiento.

<!-- p. 140 -->

Solución
Predictor de dos niveles (1,1)
   En este esquema, para cada salto existen 21 = 2 predictores de 1 bit. El comportamiento del
último salto (m = 1) determina cuál predictor se usa.

Idea general

       Se tiene una historia global/local de los últimos m saltos.

       Según esa historia, se elige cuál de los 2m predictores utilizar.

       Cada predictor tiene n bits de saturación.

Caso (1,1)

       m = 1: se consideran solo los últimos 1 salto.

       n = 1: cada predictor es de un solo bit (Taken / Not Taken).

       Por lo tanto, hay dos predictores de 1 bit, no un predictor de 2 bits.

 Bits de predicción        Predicción si el último salto fue NT            Predicción si el último salto fue T
       NT/NT                                NT                                             NT
        NT/T                                NT                                              T
        T/NT                                 T                                             NT
         T/T                                 T                                              T

Interpretación

       El predictor de dos niveles (m, n) mantiene una tabla de historia de m bits.

       Esa historia selecciona uno de los 2m predictores de n bits.

       En el caso (1, 1), hay dos predictores de 1 bit: uno se utiliza cuando el último salto fue NT, y el
       otro cuando fue T.

Ejemplo: Tamaño de un predictor (2,2)
    Un predictor de dos niveles con m = 2 y n = 2, con 4k entradas: 4 × 2 × 4K = 32Kb
    En el siguiente análisis, en la segunda columna se tienen los dos predictores (para una instrucción
de salto). El primer predictor de un bit se utiliza cuando el último salto no fue tomado, y el segundo
predictor se usa cuando el último salto sí fue tomado.

### Análisis de Predicciones
    En el siguiente análisis, en la segunda columna se tienen los dos predictores (para una instrucción
de salto). El primer predictor de un bit se utiliza cuando el último salto no fue tomado, y el segundo
se utiliza cuando el último salto sí fue tomado. Luego:

<!-- p. 141 -->

Caso 2: d=2, 0, 2, 0,...
   Sólo se predice mal la 1ª iteración (d=2).

 d=?     Predicción b1      b1    Nueva predicción b1         Predicción b2       b2    Nueva predicción b2
  2         NT/NT            T          T/NT                     NT/NT            T           NT/T
  0          T/NT           NT          T/NT                      NT/T            NT          NT/T
  2          T/NT            T          T/NT                      NT/T            T           NT/T
  0          T/NT           NT          T/NT                      NT/T            NT          NT/T

    Las columnas 2, 3 y 4 hacen referencia a una instrucción de salto, y las últimas tres a la segunda
instrucción. Cuando llega una instrucción de salto (b1), se debe seleccionar un predictor de los dos
para tomar la predicción. Esto se hace en base al último salto: si el mismo no fue tomado, se elige el
primer predictor, si lo fue, se elige el segundo. En el caso de que la predicción falle, se debe actualizar
el predictor que falló.

Descripción del Caso
    Primera iteración: Se supone al principio NT/NT (que no va a tomarse). Entonces, como el último
salto ”no fue tomado”, se elige el primer predictor (NT), pero es una predicción errónea, ya que debe
tomarse. Se actualiza el predictor que falló, quedando T/NT.
    Cuando viene la instrucción b2, dado que el último salto sí se tomó, se elige el segundo predictor
(NT), pero nuevamente falla y debe tomarse el salto, por lo que se actualiza a NT/T.
    Así sucesivamente, veremos que para este caso, solo se falló en las dos primeras predicciones (debido
a que inicialmente todo se asume como NT). Después de eso, las predicciones siempre aciertan.

### Predictor de Dos Niveles (2,2) con 16 Entradas
    Existen 22 = 4 predictores, cada uno con 2 bits de historia global de saltos. Los bits de predicción
se definen de la siguiente manera:

      0 ⇒ Not Taken (NT)

      1 ⇒ Taken (T)

    Cada columna representa un predictor basado en los 2 bits de historia global de saltos, es decir, el
comportamiento de los dos saltos anteriores. La predicción para el siguiente salto se obtiene a partir
de la combinación del penúltimo y último salto.
    Por ejemplo:

      Si el penúltimo salto no fue tomado (0) y el último sí fue tomado (1), la predicción será la de la
      segunda columna (01), que inicialmente predice NT/T.

      Si los dos últimos saltos fueron tomados (historia 11), se utilizará la última columna, que ini-
      cialmente predice T/T.

<!-- p. 142 -->

Figura 121: 2-bits de historia Global de saltos (2 Saltos anteriores) (Ejemplo: 01 = “not taken” Y
“taken”).

   Cuando una predicción falla, se actualiza el predictor correspondiente. Por ejemplo:

      Si la historia es 01 y la predicción es NT/T, pero el salto no fue tomado, se actualizaría el
      predictor a NT/NT.

      Si la historia es 11 y el salto no fue tomado, se actualiza el predictor de T/T a T/NT.

    Este mecanismo permite ajustar las predicciones en función del comportamiento observado de los
saltos.

Predictores Híbridos
    Los predictores estudiados tienen cada uno sus ventajas e inconvenientes. Combinando el uso de
distintos predictores y aplicando uno u otro según convenga, se pueden obtener predicciones mucho
más correctas.
    La idea de los predictores híbridos es utilizar más de un predictor, generalmente uno local y
uno global, y elegir dinámicamente el más acertado en cada momento. A medida que se ejecuta la
instrucción de salto, ambos predictores se mantienen activos y un mecanismo de selección determina
cuál de ellos se está desempeñando mejor. De esta forma, el sistema puede cambiar de predictor según
cuál resulte más asertivo en la ejecución real.

                Predictor híbrido =       (Predictores globales) +       (Predictores locales)
                                      X                              X

<!-- p. 143 -->

Implementación del Mecanismo de Selección
   Para combinar dos predictores, P1 y P2, se utiliza una tabla de contadores saturados de dos bits
indexada por la dirección de la instrucción de saltos. Habrá una tabla (llamada Juez) que almacena
un contador de dos bits para cada dirección de instrucción de salto. Cada contador representa el estado
de predicción para esa dirección de salto en particular. Los cuatro posibles estados son:

      00 ⇒ P1 fuertemente tomado.
      01 ⇒ P1 débilmente tomado.
      10 ⇒ P2 débilmente tomado.
      11 ⇒ P2 fuertemente tomado.

    Para seleccionar el predictor se utiliza el MSB (bit más significativo) del contador (00, 01 ⇒ P1,
10, 11 ⇒ P2). Luego, se utiliza una lógica para actualizar el valor del contador:

                             P1        P2      Actualización del Contador
                            Fallo     Fallo           Cont no varía
                            Fallo    Acierto             Cont +1
                           Acierto    Fallo              Cont -1
                           Acierto   Acierto          Cont no varía

      Si P2 acierta más que P1 ⇒ Contador aumenta.
      Si P1 acierta más que P2 ⇒ Contador disminuye.

Bit más significativo del contador:

      0 ⇒ Predictor P1 seleccionado.
      1 ⇒ Predictor P2 seleccionado.

<!-- p. 144 -->

Ejemplo
   El Predictor Competitivo (Tournament Predictor) combina dos tipos de predictores:

      Predictor Local: Predice un salto en función del comportamiento previo de ese mismo salto
      (considera las últimas 10 ejecuciones del salto).

      Predictor Global: Predice un salto en función del comportamiento de los últimos 12 saltos
      ejecutados.

    El Juez decide cuál de las dos predicciones se aplica, seleccionando el predictor que manifieste el
mejor comportamiento.
    Actualización: Al resolver cada salto, se actualizan los predictores en función de su acierto o
fallo. Si los dos predictores hicieron una predicción distinta, se actualiza el juez para que favorezca al
que acertó.
    .Este mecanismo es clave para la ejecución especulativa en arquitecturas como el 21264 (hasta 80
instrucciones en la ventana). Tasas de predicción correcta en benchmarks: 90-100 %.

Asertividad de los Distintos Predictores Dinámicos
    La ventaja del predictor híbrido es su capacidad de seleccionar el predictor correcto para un
determinado salto. Esto es muy importante para programas enteros.
    Un predictor híbrido selecciona el global casi un 40 % de las veces para SPEC integer (opera-
ciones enteras) y menos del 15 % de las veces para SPEC FP (operaciones de punto flotante).
    Esto coincide con el estudio hecho previamente, que llegaba a la conclusión de que los predictores
globales son efectivos para las operaciones con enteros, pero no para operaciones de punto flotante,
en las que funcionan mejor los predictores locales.

<!-- p. 145 -->

Predicción de los Retornos
    La precisión de los predictores con los retornos es muy baja, pues la dirección de retorno cambia
mucho en función de la llamada.
    Solución: Pila de direcciones de retorno (8 a 16 entradas).
    Esta pila, a menudo conocida como Return Address Stack (RAS), es una estructura de datos
utilizada para almacenar las direcciones de retorno de las llamadas a funciones.
    Cuando se realiza una llamada a una función, la dirección de retorno se guarda en la pila de
direcciones de retorno en lugar de almacenarse en registros o en otros lugares tradicionales. Cuando se
produce una instrucción de retorno, el procesador consulta la cima de la pila de direcciones de retorno
y recupera la dirección almacenada en esa entrada. Luego, el flujo de ejecución se dirige a la dirección
recuperada.
    Mientras más entradas tenga la pila, mejor será la predicción:

#### Detección de Instrucciones de Salto
    Para poder aplicar los métodos de predicción de salto anteriormente vistos, se necesita saber si la
instrucción es de tipo salto. El problema radica en que la instrucción de salto es reconocida cuando
finaliza la etapa 2 (decodificación). Esta situación implica varios ciclos de retardo por cada instrucción
de salto. Hay tres formas de mejorar esto:

<!-- p. 146 -->

Figura 122: Detección temprana de instrucciones de control en el pipeline. Al finalizar la etapa D
(Decode), el procesador ya conoce el tipo de instrucción. Si la instrucción corresponde a un salto, se
activa el mecanismo de predicción para determinar el flujo de ejecución y evitar penalizaciones por
riesgos de control.

      Detección en paralelo con la decodificación: Mediante un decodificador de saltos dedicado
      es capaz de detectar las instrucciones de salto antes de que finalice la etapa de decodificación.

      Detección después de la etapa fetch: La instrucción se reconoce antes de que sea decodificada
      mientras está en el buffer de instrucciones.

      Detección durante la etapa fetch: La instrucción es detectada al mismo tiempo que se lee
      la caché de instrucciones.

#### Recuperación de Fallo de Predicción
    En caso de que la predicción falle, se debe recuperar el procesador y deshacer los cambios con un
retardo mínimo. Esto se realiza en dos pasos:

   1. Descarte de resultados: Los resultados de las instrucciones especulativas (las que estamos
      ejecutando pero aún no sabemos si saltará o no) se almacenan en registros temporales (registros
      de renombramiento o buffer de renombramiento) y no modifican los contenidos de los registros
      ni de la memoria. Si la predicción fue correcta, se pasan los resultados de los registros temporales
      a los definitivos o a la memoria. Caso contrario, se descartan los resultados.

   2. Reanudación de la ejecución por el camino correcto: El procesador debe guardar la
      dirección del camino alternativo. Si la predicción fue ”no tomado”, el procesador debe calcular
      y almacenar la dirección de destino del salto por si acaso. Si la predicción fue ”tomado”, debe
      guardar la dirección siguiente al salto.

#### Reducción de Retardos en la Recuperación de Fallos
   El procesador puede guardar, no solo la dirección del camino alternativo, sino prebuscar y alma-
cenar algunas instrucciones de este camino:

      Si la predicción fue ”Taken”:

          • El procesador almacena la dirección del camino secuencial.
          • El procesador prebusca y almacena las primeras instrucciones secuenciales.

<!-- p. 147 -->

      Si la predicción fue ”Not taken”:

          • El procesador calcula y almacena la dirección destino del salto.
          • El procesador prebusca y almacena las primeras instrucciones del destino del salto.

   Si bien esto reduce los retardos en la recuperación, pueden generarse fallos de caché (cache miss)
que producirían otro retardo.

Otras Alternativas
Ejecución Condicional de Instrucciones
    Idea básica: Eliminar parcialmente los saltos condicionales mediante el uso de instrucciones de
ejecución condicional.

      Una instrucción de ejecución condicional está formada por:

          • Una condición
          • Una operación
          • Ejecución condicional:
              ◦ Si la condición es cierta: la instrucción se ejecuta.
              ◦ Si la condición es falsa: la instrucción se comporta como un NOP.

    Ejemplo:

     BNEZ R1, L                              |
     MOV R2, R3                              | ==>   CMOVZ R2, R3, R1
L                                            |

   Ventaja: Reduce la necesidad de saltos simples, evitando calcular direcciones de salto adicionales.
   Desventaja: Estas instrucciones deben evaluarse siempre, por lo que consumen tiempo incluso
cuando la condición es falsa. En promedio, resultan más lentas que las instrucciones incondicionales.
   Ejemplos de arquitecturas: Alpha, HP-PA, MIPS, SPARC.

#### Ejecución con Predicados
    Este enfoque, conocido también como ejecución predicada, no tuvo gran éxito masivo, aunque
muchos procesadores implementaron algún tipo de instrucciones condicionales (por ejemplo, el CMOV
en x86). La ventaja principal es simplificar el flujo eliminando saltos, pero la contrapartida es que la
instrucción condicional es más compleja: debe incluir tanto la operación como la condición, aumentando
la lógica interna.
    En arquitecturas RISCV, este tipo de instrucción puede coexistir siempre que no se viole la res-
tricción del tamaño fijo de las instrucciones. Por ejemplo, en RISCV podría implementarse siempre
que se mantenga el formato estándar de tres registros (rs1, rs2, rd), reservando uno de los campos
para la condición.
    Idea básica:

      Transformar todas las instrucciones en condicionales.

      Una instrucción de ejecución condicional está formada por:

          • Una parte de condición, denominada predicado o guarda.

<!-- p. 148 -->

        • Una parte de operación.

   Ejecución predicada:

      Si la condición es cierta: La instrucción se ejecuta.

      Si la condición es falsa: La instrucción se comporta como un NOP.

                                         Figura 123: Ejemplo.

pred_It p1(U), p2(U), a, 10;
significa: ¿Es ’’a’’ < 10? Si es verdadero ejecutar ’’p2(U)’’ y de lo contrario
ejecutar ’’p1(U)’’.

pred_gt p3(U), p4(U), b, 20;
significa: ¿Es ’’b’’ > 20? Si es verdadero ejecutar ’’p4(U)’’ y de lo contrario
ejecutar ’’p3(U)’’.

    El resultado de la condición o predicado se almacena en los llamados registros de predicado. Si el
predicado es verdadero, se almacena un valor de 1 en el registro de predicado correspondiente; si es
falso, se almacena un valor de 0.
    Esta alternativa no ha sido muy utilizada.

### Especulación
   La predicción de saltos introduce especulación: habrá instrucciones cuya ejecución depende de
una predicción. Existen entonces dos tipos de instrucciones en el procesador:

      Independientes: no dependen del salto y se ejecutan siempre de manera normal.

      Dependientes: su ejecución depende del acierto o fallo en la predicción del salto.

    La pregunta es: ¿cómo se implementa esta distinción en un modelo de ejecución con finalización
fuera de orden?
    La especulación consiste en ejecutar provisoriamente el camino elegido por la predicción. Las
instrucciones que dependen de un branch se ejecutan de manera especulativa, pero en un modelo fuera
de orden como Tomasulo, tal como está, no es suficiente. ¿Por qué? Porque la ejecución fuera de orden
permite finalizar instrucciones antes de tiempo, y si la predicción resulta incorrecta, no hay forma de
“deshacer” los resultados ya aplicados.

<!-- p. 149 -->

#### Algoritmo de Tomasulo con Especulación
    La especulación consiste en ejecutar instrucciones cuyo resultado depende de la predicción de un
salto. En el algoritmo de Tomasulo clásico esto no es posible de manera segura, porque la ejecución
fuera de orden permite que instrucciones especulativas finalicen antes de tiempo, sin posibilidad de
“deshacer” sus efectos si la predicción falla.

Solución: Se modifica el algoritmo de Tomasulo para forzar la finalización en orden. Para ello
se agrega una etapa extra llamada commit, junto con un buffer de reordenamiento (ROB, Re-Order
Buffer).

      Una instrucción termina realmente cuando escribe en un registro o en memoria.

      Con el ROB, los resultados de instrucciones ejecutadas (incluso fuera de orden) se almacenan
      primero en este buffer.

      Solo cuando la instrucción alcanza la etapa de commit, sus resultados se escriben efectivamente
      en los registros o memoria, respetando el orden del programa.

Funciones del ROB:

      Almacena resultados de instrucciones cuya ejecución ha finalizado pero que aún no actualizaron
      registros o memoria.

      Permite manejar instrucciones especulativas: si la predicción fue incorrecta, las entradas espe-
      culativas en el ROB se descartan sin modificar el estado arquitectónico.

      Facilita el paso de operandos entre instrucciones especulativas con dependencias de datos (ej.
      LDE, Load Data Dependency).

Fuentes de operandos en Tomasulo con especulación:

      Registros: cuando la instrucción previa ya finalizó y escribió su resultado.

      ROB: cuando la instrucción previa ya ejecutó, pero su resultado aún no fue comiteado.

      CDB (Common Data Bus): cuando la instrucción previa está transmitiendo su resultado en
      la fase de escritura.

    El algoritmo de Tomasulo con especulación introduce un ROB y una etapa de commit, lo que
permite ejecutar instrucciones fuera de orden pero finalizar en orden, garantizando la corrección del
estado del procesador incluso en presencia de predicciones de salto erróneas.
    Cada entrada del ROB tiene 4 campos:

      Tipo de instrucción: Indica si la instrucción es de salto (no hay que guardar ningún resultado
      en ningún destino), store (el destino es la memoria) o Aritmética/Load (el destino es un registro).

      Destino: Número de registro (en instrucciones aritméticas y load) o dirección de memoria
      (store).

      Valor: Resultado de la ejecución de la instrucción. Este valor es guardado hasta que se actualiza
      el registro o la posición de memoria de destino.

<!-- p. 150 -->

      Listo: Indica si la instrucción ha completado la ejecución y el resultado está disponible en el
      campo ”valor”.

                       Figura 124: Algoritmo de TOMASULO con especulación.

              Figura 125: Vista alternativa del algoritmo de Tomasulo con especulación.

<!-- p. 151 -->

#### Estados del algoritmo de Tomasulo Especulativo
   1. Issue: Se toma una instrucción de la cola para ejecutarla.

            Requiere que exista una estación de reserva libre y una entrada libre en el ROB.
            Los operandos pueden obtenerse desde el banco de registros, desde el ROB o desde el
            Common Data Bus (CDB).

   2. Ejecución: Cuando todos los operandos están disponibles, la instrucción se ejecuta en la unidad
      funcional correspondiente.

   3. Escritura de resultados: Al finalizar la ejecución, los resultados se difunden por el CDB hacia:

            Otras estaciones de reserva que los necesiten.
            La entrada correspondiente en el ROB.

      Importante: en esta etapa no se escriben registros ni memoria directamente.

   4. Commit: Una instrucción se retira del ROB cuando:

            Se encuentra en la cabecera del ROB (instrucción más antigua, modelo FIFO).
            Su resultado ya está listo.

      En ese momento, el resultado se escribe en el banco de registros o en memoria de manera
      ordenada.

Campos típicos de una entrada en el ROB:

      Tipo de instrucción: salto, store, aritmética/lógica, etc.

      Destino: número de registro o dirección de memoria a actualizar.

      Valor: resultado calculado.

      Flag de estado: indica si la instrucción ya finalizó su ejecución.

Funcionamiento del ROB:

      Las instrucciones entran al ROB en orden de emisión.

      Dos punteros controlan su operación:

          • Puntero de escritura (verde): indica dónde se inserta la nueva instrucción.
          • Puntero de lectura (rojo): marca la instrucción más antigua que debe finalizar primero.

      El ROB funciona como una cola FIFO: siempre se inserta por el verde y se retira por el rojo,
      garantizando finalización en orden.

<!-- p. 152 -->

    La instrucción LOAD ocupa una estación de reserva y se asigna a la entrada ROB1. Antes el destino
era directamente el registro F0, ahora es el ROB quien escribirá en F0. El valor aún no está disponible,
pero cualquier instrucción que dependa de F0 sabrá que su resultado llegará desde ROB1, formando
una cadena de punteros. Por ejemplo, ADDD F10, F4, F0 usará como fuente el valor que producirá
ROB1.

<!-- p. 157 -->

#### Riesgos a través de la Memoria
    Los riesgos EDE y EDL ya no aparecen, ya que la actualización de la memoria se realiza en orden:
todas las instrucciones load y store previas habrán finalizado antes de que otra instrucción requiera
sus datos.
    El riesgo LDE sí puede producirse cuando un load accede a una dirección A y existe en el ROB
un store previo que aún no escribió su resultado en esa misma dirección.
    Mecanismo de prevención:
      Un load no accede a memoria si en el ROB hay un store previo con la misma dirección.

      Tampoco accede si todavía no se calculó la dirección efectiva de un store previo, ya que podría
      coincidir con la dirección del load.
   Este último punto introduce el problema de la ambigüedad de memoria, dado que diferentes
combinaciones de registros y offsets pueden apuntar finalmente a la misma dirección. Resolver esta
ambigüedad no es trivial y complica el control de dependencias a través de memoria.

Saltos e Interrupciones
   El ROB permite tanto recuperarse de saltos mal predichos como implementar un modelo de ex-
cepciones precisas.

      Si un salto bien predicho llega a la cabecera del ROB, simplemente se elimina de la cola y se
      continúa.

      Si un salto mal predicho llega a la cabecera:

<!-- p. 158 -->

        • Se borra todo el contenido del ROB.
        • Se eliminan los tags en los registros que apuntaban a entradas del ROB.
        • Se limpian las estaciones de reserva y los load/store buffers.
        • Se busca y recupera la instrucción correcta (ya se había guardado su dirección).

      Si una instrucción genera una interrupción, esta se marca en el ROB. Cuando llega a la cabecera:

        • Se reconoce la excepción únicamente si la instrucción no era especulativa.
        • Todas las instrucciones anteriores ya habrán finalizado.
        • Ninguna instrucción posterior habrá sido completada.

    De este modo, se garantiza la propiedad de excepciones precisas: todas las instrucciones previas
a la que generó la excepción están terminadas, y ninguna posterior se ha ejecutado.
    Cabe destacar que las entradas del ROB deberían tener un flag para marcar si la instrucción
generó una excepción, de modo que el chequeo se haga justo cuando la instrucción llega a la cabecera
del ROB.

¿Qué pasa cuando hay más de un hilo?
    En un procesador multihilo, cada hilo podría tener su propio flujo de instrucciones, un ROB
dedicado y un banco de registros independiente. El problema es que, si un hilo no está ejecutando, su
ROB quedaría vacío y se desperdiciarían recursos.
    La solución es utilizar un ROB compartido más grande, con una única entrada y múltiples
salidas hacia distintos bancos de registros. De esta forma, la salida se selecciona dinámicamente según
el hilo al que pertenece cada instrucción.

<!-- p. 159 -->

                                                                Figura 126: Resumen conceptual de la Unidad N°4: Lanzamiento Múltiple - Límites de ILP - Multithreading
