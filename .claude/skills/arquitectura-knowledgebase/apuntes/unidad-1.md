<!-- p. 9 -->

## Unidad 1: Tendencias tecnológicas, costo/rendimiento/consumo
### Arquitectura
   Describe los atributos de un sistema tal y como los ve el programador, es decir, la estructura
conceptual y el comportamiento funcional (a diferencia de la organización del flujo de datos y los
controles, el diseño lógico y la implementación física).

ISA (Arquitectura del Conjunto de Instrucciones o Instruction Set Architecture) Des-
cribe la sintaxis y la semántica de la interfaz de una computadora. Se trata del tipo y tamaño de
los operandos, estado del registro visible del programador, modelo de memoria, cómo se manejan las
interrupciones y excepciones, las instrucciones disponibles y el significado de cada instrucción.

### Microarquitectura
    Se refiere a la organización (o al nivel más alto de implementación) de un procesador en par-
ticular. Incluye canalización, paralelismo a nivel de instrucción, ejecución fuera de orden, ejecución
especulativa, predicción de salto y almacenamiento en caché.
    Generalmente, cuando se habla de Arquitectura de Computadores se está haciendo referencia
tanto a la Arquitectura del Conjunto de Instrucciones como la Microarquitectura y otras cuestiones
más amplias a nivel de sistema, como la conectividad de red en multiprocesadores.

### Niveles de Descripción y Diseño de un Computador

                        Figura 1: Niveles de Descripción y Diseño de un Computador.
     Se estudiará al computador como una estructura en capas:

       Aplicación.

       Lenguaje de alto nivel.

       Sistema Operativo / Compilador.

<!-- p. 10 -->

      Arquitectura del repertorio de instrucciones (esto es lo que ve el programador, el ISA, la
      arquitectura del procesador). Los registros que se muestran aquí existen, pero no de la manera
      que lo ve el programador. Este ve un modelo abstracto del sistema para poder programarlo.

      Organización del Hardware del sistema: Cómo se ponen cada uno de los módulos del
      sistema, cómo están interconectados, cómo interactúan el uno con el otro y cómo se definen las
      interfaces entre ellos.

      Circuito Digital: Se estudia para entender los retardos que se generan en la transferencia de
      información entre una compuerta y la siguiente.

      Sistema Físico: Se estudian con el objetivo de entender cómo se genera calor en los componentes
      y cómo esto interfiere en el procesador final.

    Cada nivel se corresponde con la visión que tiene del sistema un tipo determinado de usuario, y
en cada uno podemos considerar dos procesos de estudio diferentes, el análisis y la síntesis. El análisis
parte de la implementación del sistema a un cierto nivel en términos de elementos básicos del nivel
inferior, y llega a determinar la función del mismo, es decir, su especificación. El sentido de la síntesis
es el opuesto, parte de la especificación de un sistema y obtiene su implementación en función de
los elementos básicos del nivel inferior. En la siguiente figura hemos representado gráficamente esta
relación:

                                  Figura 2: Niveles y Características.

      Elementos de entrada: Disponibles para el nivel en cuestión, que proceden del nivel inmediato
      inferior (especificación).

<!-- p. 11 -->

       Elementos de salida: Objetivos del diseño en el nivel en cuestión destinados al nivel inmediato
       superior (implementación).

       Metodología de análisis y síntesis: Se refiere a la síntesis de los elementos de salida en
       términos de los de entrada.

Ejemplo: En la capa lógica se especifica un módulo sumador. Mediante una síntesis se obtiene la
implementación, que en este caso es la configuración de compuertas que resulta en dicho módulo.
Luego se realiza el análisis de la función que va a realizar dicha configuración de compuertas, se
obtiene como resultado el módulo sumador.

### El escalado de la Tecnología

                                              Espacio
                                              Las primeras computadoras (1930) estaban hechas a base de
                                              tubos de vacío (V Tubes) y ocupaban aproximadamente 1 mi-
                                              llón de metros cúbicos (1 × 106 m3). Actualmente, las compu-
                                              tadoras se basan en tecnología CMOS y ocupan aproximada-
                                              mente 1 × 10−12 metros cúbicos, con lo cual el tamaño de un
                                              computador ha pasado de ser el de un edificio al de un chip
                                              muy pequeño.

                                              Tiempo
                                              El tiempo de propagación (Gate Delay: tiempo desde que la
                                              entrada de una compuerta lógica es estable hasta que la salida
                                              de la misma se vuelve estable) ha pasado de ser del orden de
                                              los 100 segundos al orden de los nanosegundos (quizás menos).

                                              Energía
                                              La energía de conmutación (energía que se consume para con-
                                              mutar un transistor/válvula, etc.) ha pasado de ser del orden
                                              de los 100 Joules a 1 × 10−14 Joules.

    El desempeño (rendimiento o performance) de un computador se mide en flops (generalmente
teraflops), es decir, la cantidad de operaciones de punto flotante que se realizan por segundo. A
continuación, se muestra un listado para comparar el rendimiento de distintos procesadores (top 500 ):

       1949: El computador EDSAC realizaba alrededor de 100 operaciones por segundo.

       1957: Se inventó el transistor, llegándose a lograr diez mil operaciones por segundo.

       1965: Se inventaron los circuitos integrados (CI) logrando 1 millón de operaciones por segundo.
       Se comienza a distinguir entre arquitectura y microarquitectura de los computadores.

       1971: Primer microprocesador comercial (Intel 4004, luego 8008).

       2003: Los procesadores realizaban más de 3 × 1013 operaciones por segundo.

<!-- p. 12 -->

       2012: Más de 1015 operaciones por segundo (1 petaflop).

### El microprocesador Intel Pentium 4 y el fin de la era del aumento de frecuencia
    El Intel Pentium 4 fue introducido por Intel en el año 2000 como parte de la microarquitectura
NetBurst. Su objetivo principal fue maximizar la frecuencia de reloj, apostando por pipelines muy
profundos y una ejecución agresiva. Esta estrategia permitió alcanzar frecuencias sin precedentes para
su época, pero introdujo serias limitaciones en eficiencia energética y rendimiento por ciclo.
    En la Figura 3, se observa la evolución de diversas métricas de los microprocesadores a lo largo de
más de cuatro décadas. Durante la era del Pentium 4, el número de transistores continuó creciendo
de acuerdo con la ley de Moore, mientras que el rendimiento monohilo aumentó de forma mucho más
moderada. Al mismo tiempo, la frecuencia de reloj comenzó a estancarse y el consumo de potencia se
incrementó de manera significativa.

Figura 3: 42 años de tendencias en microprocesadores: número de transistores, rendimiento monohilo,
frecuencia, potencia y número de núcleos.

    La Figura 4 muestra específicamente la evolución de la frecuencia de reloj y la potencia en distintas
generaciones de microprocesadores Intel x86. El Pentium 4 destaca por un aumento abrupto tanto en
frecuencia como en consumo energético, sin una mejora proporcional en rendimiento real.

Características técnicas del Pentium 4
   Las principales características del Pentium 4 pueden resumirse de la siguiente manera:

       Año de introducción: 2000

       Frecuencia de reloj: desde 1.3 GHz hasta aproximadamente 3.8 GHz (modelos Prescott)

<!-- p. 13 -->

Figura 4: Frecuencia de reloj y potencia de los microprocesadores Intel x86 a lo largo de ocho genera-
ciones y 25 años.

       IPC (Instrucciones por ciclo): bajo, aproximadamente entre 0.5 y 1.0 instrucciones por ciclo,
       debido al pipeline extremadamente profundo (hasta 31 etapas en Prescott)

       Potencia típica: entre 75 W y más de 100 W en los modelos Prescott

       Número de núcleos: 1 núcleo (arquitectura mononúcleo)

    El bajo IPC del Pentium 4 implicaba que, a pesar de sus altas frecuencias, el rendimiento por
ciclo era inferior al de arquitecturas anteriores y posteriores. Además, el elevado consumo energético
y los problemas térmicos, especialmente en la versión Prescott, limitaron la escalabilidad de esta
arquitectura.

La transición hacia arquitecturas multinúcleo
    Los problemas térmicos y de consumo del Pentium 4 evidenciaron los límites físicos del aumento
continuo de la frecuencia de reloj. Como consecuencia, la industria adoptó una nueva estrategia: en
lugar de aumentar la frecuencia, se optó por incrementar el número de núcleos por chip.
    La línea Intel Core 2, introducida a partir de 2006, marcó este cambio de paradigma. Se volvió
a pipelines más cortos, frecuencias más bajas y un mayor IPC, combinados con múltiples núcleos por
procesador. Esta estrategia permitió mejorar el rendimiento total sin exceder los límites térmicos y
energéticos, sentando las bases de los procesadores modernos multinúcleo. El Pentium 4 representa
un punto de inflexión en la historia de los microprocesadores: su diseño extremo en frecuencia mostró
claramente que el futuro del rendimiento dependía de la paralelización y no únicamente de la velocidad
de reloj.

### La Ley de Moore
   El 19 de abril de 1965, la Revista Electronics publicó un documento elaborado por el Sr. Gordon
Moore en el cual él anticipaba que la complejidad de los circuitos integrados se duplicaría cada año
con una reducción de costo conmensurable.

<!-- p. 14 -->

    Conocida como la Ley de Moore, su predicción ha hecho posible la proliferación de la tecnología
en todo el mundo, y hoy se ha convertido en el motor del rápido cambio tecnológico. Moore actualizó
su predicción en 1975 para señalar que el número de transistores en un chip se duplica cada dos años,
y esto se sigue cumpliendo hoy.
    Además de proyectar cómo aumenta la complejidad de los chips (medida por el número de tran-
sistores contenidos en un chip de computador), la Ley de Moore sugiere también una disminución de
los costos. A medida que los componentes y los ingredientes de las plataformas con base de silicio
crecen en desempeño, se vuelven exponencialmente más económicos de producir, y por lo tanto, más
abundantes, poderosos y transparentemente integrados en nuestras vidas diarias.
    Los microprocesadores de hoy se encuentran en todas partes, desde juguetes hasta semáforos para
el tránsito. Una tarjeta de felicitación musical que hoy se puede adquirir por muy bajo precio tiene
más poder de cómputo que las computadoras centrales más rápidas de hace unas décadas.

                               Figura 5: La ley de Moore se cumplió.

   La ley de Moore, crece tanto por el avance de la tecnología como por la mejora de las micro-
arquitecturas.

<!-- p. 15 -->

                                Figura 6: La ley de Moore se cumplió.

    En el primer gráfico se puede ver que, a menor tamaño de la juntura de los transistores, mayor
frecuencia es posible. Para el final del gráfico, se ha incrementado la frecuencia en 13 veces. También,
gracias a la mejora de la microarquitectura, se incrementa la frecuencia en 4 veces. Si bien la mayor
contribución es debida al avance de la tecnología (disminución del tamaño de la juntura de los tran-
sistores), el incremento total es FrecInicial × 13 × 4 = FrecInicial × 52, es decir, se mejora 52 veces en
lugar de 13, con lo cual la mejora por parte de la microarquitectura es muy significativa.
    No cualquier cosa que uno haga en la microarquitectura produce una mejora, sino que solo aquellas
acciones que reduzcan el delay. Por ejemplo, si se hace una segmentación en más cantidad de etapas,
la frecuencia podrá incrementarse.
    En el segundo gráfico se hace referencia al rendimiento, es decir, a la cantidad de instrucciones que
pueden realizarse por ciclo de clock o por unidad de tiempo. Supóngase que se tome la cantidad de
instrucciones por ciclo. Al aumentar la frecuencia (por tecnología), la cantidad de instrucciones por
ciclo evidentemente aumentará. Sin embargo, esta cantidad también se incrementará ante una mejora
de la microarquitectura.
    Supóngase que se realiza una instrucción cada dos ciclos (previo a un cambio en la microarquitec-
tura). Si ahora se produce una mejora en la microarquitectura, como por ejemplo un mejor predictor
de salto (jump), ejecución fuera de orden para un orden óptimo de la ejecución de instrucciones,
evidentemente habrá una mejora en el rendimiento (por ejemplo, cada ciclo y medio se ejecuta una
instrucción). En este caso, el rendimiento se ha multiplicado por 13 gracias a la mejora en la tecnología
y por 6 gracias a la mejora en la microarquitectura (nótese que la mejora es mayor para la frecuencia).
Esto da una mejora en conjunto de 13 × 6 = 78 veces.
    El escalado tecnológico proporcionado por la Ley de Moore está próximo a su fin. Las diferentes
predicciones lo fijan para el nodo de 3nm en el entorno del 2022-2025. Esta situación abre nuevos
interrogantes sobre la futura evolución de los computadores, desde vías continuistas, como gate all-

<!-- p. 16 -->

around, chips 3D, materiales de III-V o IVta generación, a otras completamente nuevas como la
computación cuántica o la computación neuromórfica.

#### Retos de la Ley de Moore

                                        Figura 7: Retos 2015.

    1er Diagrama: Pérdida vs frecuencia normalizada, es decir, pérdida normalizada. Sabemos que
la pérdida aumenta de forma cúbica con la frecuencia (tiene una relación con la frecuencia en forma
cúbica). La gráfica es una hipérbola (se ve una forma logarítmica, pero los ejes están cambiados). No
se puede subir indiscriminadamente la frecuencia sin que la cantidad de vatios de disipación aumente
de manera cúbica.
    2do Diagrama: A medida que mejora la tecnología, es decir, a medida que disminuye el tamaño
de la juntura de los transistores, se va encontrando lo que se denomina como Soft Error.
    Soft Error: Es un tipo de error en el que una señal o dato es incorrecto sin que haya un problema
en el hardware. Este error se debe a que partículas ionizadas impactan contra la juntura de los
transistores; por ejemplo, si una partícula con cierta carga impacta una celda de memoria, esta puede
generar un cambio de estado (por ejemplo, puede que haya un 0 donde antes había un 1). Estas
partículas pueden provenir de rayos cósmicos (en integrados que se encuentran en el espacio exterior o
en aviones a gran altura), radiación (debida a materiales radioactivos en el interior de los integrados,
se da en integrados en reactores nucleares), neutrones térmicos, etc.

<!-- p. 17 -->

    El problema es que al disminuir el tamaño de la juntura, tanto el tamaño relativo de la juntura
respecto del tamaño de la partícula como la carga de la juntura respecto de la carga de la partícula
comienzan a ser factores significativos. En el diagrama se puede ver que a medida que aumenta
la densidad de transistores (disminuye el tamaño de la juntura), la cantidad relativa de Soft Error
aumenta de manera exponencial.
    Puede que estos errores ocurran en un solo ciclo y en los siguientes no, pero el error se propagará
generando una avalancha de errores. Luego, se debe hacer hardware para prevenir ese tipo de errores.
    3er Diagrama: El aumento del desempeño debido al aumento de la densidad de transistores se
vio frenado a partir del 2004-2005, por lo que comenzaron a usar multicores. Para que el software
corra a mayor velocidad, ahora debe haber multihilos, multiprocesos, etc., es decir, se debe explotar
el paralelismo, ya que en este punto fue el quiebre a partir del cual no se puede seguir aumentando la
densidad de potencia.
    4to Diagrama: Problema del wire delay, es decir, el retraso que se produce debido a las interco-
nexiones dentro de las celdas en una FPGA o en un procesador. Este delay es el tiempo que se demora
en alcanzar un porcentaje del procesador en un ciclo (véase Retardo de las Interconexiones).

   ¿Por qué una frecuencia de reloj infinita es imposible?

   El aumento indefinido de la frecuencia de reloj en un microprocesador es físicamente inviable
   debido a múltiples limitaciones fundamentales:

         Cierre de timing: Para que un circuito digital funcione correctamente, todas las se-
         ñales deben propagarse y estabilizarse dentro del período de reloj. A frecuencias muy
         altas, el tiempo disponible por ciclo se vuelve menor que los retardos de las compuertas,
         interconexiones y memorias, haciendo imposible garantizar el cierre de timing.

         Clock skew: La señal de reloj no llega simultáneamente a todos los elementos del chip
         debido a diferencias en las rutas físicas. A frecuencias elevadas, incluso variaciones de
         pocos picosegundos pueden provocar violaciones de setup y hold, generando errores de
         sincronización.

         Retardos de interconexión: En tecnologías modernas, los retardos debidos al cableado
         interno dominan sobre los retardos de las compuertas lógicas. Reducir el período de reloj
         no elimina estos retardos, lo que impone un límite práctico a la frecuencia máxima.

         Power wall: La potencia dinámica crece proporcionalmente con la frecuencia de reloj
         (P ∝ C · V 2 · f ). Aumentar la frecuencia implica un consumo energético y una disipación
         térmica insostenibles, como se evidenció claramente en el Pentium 4.

         Variabilidad y ruido: Fenómenos como variaciones de proceso, temperatura, voltaje
         (PVT) y ruido eléctrico incrementan la incertidumbre temporal, reduciendo aún más el
         margen disponible para operar a altas frecuencias.

   En conjunto, estas limitaciones establecen un límite superior práctico a la frecuencia de reloj,
   motivando el abandono de arquitecturas basadas exclusivamente en el aumento de frecuencia y
   la transición hacia diseños multinúcleo y paralelos.

#### Entorno
   Resumen de Evolución en Tecnología de Implementación

<!-- p. 18 -->

                           Tipo     Capacidad             Velocidad / Latencia
                           Lógica   ×2 en 3 años          ×2 en 3 años
                           DRAM     ×4 en 3 años          ×2 en 10 años
                           Disco    ×2 en 3 años          ×2 en 10 años

Uso de los Computadores
      La cantidad de memoria necesaria crece entre 1.5 y 2 veces por año. Esto lleva a una mayor
      necesidad de bits para direccionamiento.

      La programación en LAN se vuelve más común.

      Los compiladores son fundamentales; son la interfaz entre las aplicaciones y el computador.

¿Una Arquitectura Debe Ser Diseñada para Soportar el Paso del Tiempo?
      Cambios en tecnología, software y aplicaciones son inevitables. Ejemplos históricos incluyen la
      arquitectura IBM 360-390 (1964), X86 (1978), y Sparc (1992).

      Es importante observar las tendencias para determinar cómo progresará una tecnología especí-
      fica. No todos los componentes evolucionan de la misma manera.

      Se pueden distinguir tres apartados en cuanto a la evolución: Lógica, Memoria Dinámica RAM
      (DRAM), y Capacidad de los discos.

      Los compiladores también evolucionan, pero no de la misma manera que otros componentes.

      Una arquitectura debe ser diseñada para soportar el paso del tiempo. Los procesadores listados
      en la imagen siguen funcionando hoy en día, es decir, han soportado el paso del tiempo mediante
      el cambio de su microarquitectura, pero no de su arquitectura.

                                                                 Procesador: ’286, ’386, ’486, Pentium, Pen-
                                                                 tium Pro, Pentium 4 (21x2250x)

                                                                 Ethernet: 10Mb, 100Mb, 1000Mb, 10000
                                                                 Mb/s (16x 1000x)

                                                                 Módulo de Memoria: 16bit plain DRAM, Pa-
                                                                 ge Mode DRAM, 326, 64b, SDRAM, DDR
                                                                 SDRAM (4x,120x)

                                                                 Disco: 3600, 5400, 7200, 10000, 15000 RPM
                                                                 (8x, 143x)

                                                            Ejes del Gráfico
                                                                 Eje X: Mejora relativa de latencia.

                                                                 Eje Y: Mejora relativa en ancho de banda.

         Figura 8: Mejora Relativa de la latencia.

<!-- p. 19 -->

    Ambos ejes están en escala logarítmica y las curvas son exponenciales. Los cuadrados azules co-
rresponden a los procesadores listados.
    La recta gris punteada (que estaría a 45° si los ejes tuvieran la misma escala) divide el cuadrante
en dos. La razón para las escalas desiguales es que el ancho de banda crece mucho más rápido de lo
que mejora la latencia en procesadores, memoria, discos, etc.
    Para aumentar el ancho de banda, se deben agregar más recursos y elementos a la estructura. En
cambio, mejorar la latencia (es decir, disminuir el tiempo de propagación entre dos puntos) es costoso
y no depende únicamente de los esfuerzos realizados. En un buffer, los cambios en latencia pueden no
ser evidentes, mientras que en un multiplicador, mejorar el algoritmo puede reducir la latencia. Si la
tecnología mejora (es decir, soporta velocidades más altas), la latencia también mejorará.
    El ancho de banda se mejora principalmente mediante la inversión en infraestructura, mientras
que la latencia se mejora con el conocimiento sobre materiales o algoritmos.

Proveedores y Tecnología
    Cuando una tecnología es nueva, se obtiene de proveedores líderes (por ejemplo, para obtener un
dispositivo de red avanzado, se podría recurrir a Cisco, que es conocido como líder en el campo). Se
pueden distinguir los proveedores en líderes y seguidores:

      Líderes: Proveen tecnologías incipientes. Estos proveedores suelen ser los primeros en ofrecer
      nuevas tecnologías y tienen más conocimiento y capacidad para minimizar errores a corto plazo.

      Seguidores: Proveen tecnologías maduras. Aprenden de las tecnologías de los líderes y tienen la
      capacidad de implementar estas tecnologías a largo plazo. Eventualmente, cuando la tecnología
      madura, habrá muchos proveedores capaces de utilizarla.

   Una tecnología incipiente puede tener errores. Se espera que los desarrolladores líderes tengan
un conocimiento más profundo y reduzcan estos errores en el corto plazo. Los seguidores, aunque
no tengan esta capacidad inmediata, pueden adoptar la tecnología a largo plazo y eventualmente
contribuir a su maduración.

#### Consumo Energético en Procesadores
    La energía consumida por un procesador depende del tiempo y de la potencia. En la gráfica,
la altura representa la potencia, y el área tramada en oscuro representa la energía consumida. El
consumo energético del procesador eventualmente se convertirá en calor.
    El procesador ingresa energía para transformar información. Sin embargo, no es una máquina en
el sentido tradicional, ya que la energía ingresada no realiza un trabajo útil en términos mecánicos,
sino que se convierte en calor.
    En otras palabras, el procesador convierte la energía en información, pero el resultado final es la
disipación de esa energía en forma de calor. La eficiencia energética se convierte en un aspecto crítico
para el diseño de procesadores, ya que el calor generado debe ser gestionado adecuadamente para
evitar el sobrecalentamiento y mantener el rendimiento del sistema.

<!-- p. 20 -->

                              Figura 9: Diferentes niveles en Consumo.

Diferencia entre Energía y Potencia
    Sabemos que la potencia es la derivada de la energía respecto del tiempo, es decir, es la cantidad
de energía por unidad de tiempo. Análogamente, la energía es la potencia integrada respecto del
tiempo, lo que equivale al área gris del gráfico. En el diagrama, los rectángulos grises tienen la misma
área.
    En el segundo gráfico, la potencia es menor porque la misma energía está distribuida en un intervalo
de tiempo más largo. Es decir, si se disminuye el tiempo para una misma cantidad de energía ingresada
a un sistema, la potencia aumenta.

¿Qué Implicancia Tiene Esto para los Procesadores?
    La energía ingresada a un procesador se acumulará en forma de calor, manifestándose como un
aumento en la temperatura. El sistema tenderá a equilibrar su temperatura con la del medio ambiente,
como lo hace cualquier objeto caliente.
    A mayor potencia, mayor será el salto térmico del sistema. Un sistema tiene una capacidad térmica
y una resistencia térmica, resultando en una constante de tiempo térmica similar a la constante de
tiempo de carga en un capacitor (donde la tensión equivaldría a la temperatura). La temperatura del
sistema tiende a equilibrarse según una ecuación de primer orden ex . De manera similar a un capacitor
que tendrá más tensión cuanto más carga se le suministre, el sistema tendrá mayor temperatura cuanto
más energía se le suministre.
    Otro problema es que, si se inserta una cantidad de potencia o energía en una área extensa, no
deberían generarse problemas. Sin embargo, a medida que el área donde se aplica esta potencia (el
área del transistor) disminuye, la densidad de potencia se vuelve demasiado alta y el material puede

<!-- p. 21 -->

fundirse.
   En resumen:

      A menor tiempo de operación (mayor frecuencia, lograda mediante la inserción de más transis-
      tores más pequeños en una misma área), mayor será la potencia y, por lo tanto, mayor será la
      temperatura.

      A menor área del transistor, mayor será la densidad de potencia y mayor será la probabilidad
      de fundir el transistor.

Evolución de la Tecnología e Incremento de la Potencia
    En el gráfico (con escala logarítmica) se puede observar cómo ha aumentado la densidad de potencia
con el avance de la tecnología. Se pueden alcanzar potencias muy altas, pero existe un límite de potencia
por centímetro cuadrado que no se puede superar sin fundir el transistor (aproximadamente donde
está el Pentium III).
    Para no sobrepasar este límite, se pueden emplear métodos como la refrigeración del circuito. Por
ejemplo, si se utiliza refrigeración con aire (los refrigerantes líquidos hacen que el transistor sea más
sensible), se podría usar un tamaño de transistor muy pequeño que de otra manera superaría el límite
sin refrigeración.

                             Figura 10: problema consumo “Power Wall”.

Problemas de densidad de potencia en procesadores (2004-2005)
    En los años 2004-2005, la industria de los procesadores comenzó a enfrentar serios problemas
debido a la elevada densidad de potencia. La densidad de potencia había llegado a tal punto que
los procesadores se rompían debido al calor excesivo generado. Para mitigar este problema, se decidió
establecer un límite en la densidad de potencia, manteniéndola por debajo de los 100W por centímetro
cuadrado. Este límite buscaba evitar el sobrecalentamiento y la degradación física de los procesadores.

#### Componentes de Potencia en un Procesador
   El consumo de potencia en un procesador se divide principalmente en tres componentes:

      Potencia de Conmutación:

                                         Pconmutación = C × V 2 × f

<!-- p. 22 -->

       Es una potencia totalmente capacitiva, resultante de la conmutación de los transistores. Se
       considera dinámica porque se debe al cambio de estados lógicos en el procesador.
       Potencia de Fuga:

                                 Pfuga = Icorte × Vcorte + Isaturación × Vsaturación

       Esta potencia se debe a las corrientes de saturación y de corte (o de fuga) que no son cero. Es
       la potencia consumida ”sin hacer nada”, es decir, incluso cuando no se está conmutando. Este
       componente es estático.
       Potencia de Cortocircuito: Se produce cuando se tienen dos transistores en oposición, uno en
       estado de corte y el otro en estado de saturación. Durante este proceso, se genera un cortocircuito
       que produce esta potencia. Al igual que la potencia de fuga, esta potencia es estática.

### Potencia Estática y Dinámica
   Según estas componentes, se puede dividir la potencia en dos tipos:

       Potencia Dinámica:
                                             Pdinámica = C × V 2 × f
       Es la potencia debida a la conmutación, es decir, al trabajo que realizan los transistores.
       Potencia Estática: Es la potencia consumida por el procesador sin realizar trabajo (potencia de
       fuga y potencia de cortocircuito). Lo deseable es que el mayor porcentaje posible de la potencia
       requerida por el procesador sea para la potencia dinámica.

#### Analizando la Fórmula de Potencia de Conmutación
    Para que los transistores trabajen a cierta frecuencia, se requiere un mínimo de tensión (por
cuestiones físicas de la juntura), y a mayor frecuencia se requiere mayor tensión. Sin embargo, no es
conveniente aumentar la tensión, ya que al estar al cuadrado en la fórmula, aumenta significativamente
la potencia. Por lo tanto, se debe establecer una relación directa entre la tensión y la frecuencia en la
cual la tensión aumentará con el cubo de la frecuencia. Es decir, si aumenta la frecuencia, la potencia
que disipará el dispositivo aumentará al cubo.

#### ¿Qué hacer para seguir mejorando el rendimiento de los sistemas?
       Mejorar a nivel de core, es decir, balancear la potencia y el rendimiento (power-performance).
       Se establece una potencia máxima deseada que el dispositivo debe disipar, por ejemplo, 100W.
       A partir de esta potencia, para mejorar el rendimiento, se agregan núcleos (cores) y se evalúa si
       se produce una mejora o no, y qué tipo de núcleos deben agregarse (simples o complejos).
       Integrar múltiples cores en un chip y balancear la complejidad del core con el número de cores.
       Usar chips heterogéneos (es decir, que contienen cores simples y cores complejos) y aceleradores
       on-chip.

    Esto genera nuevos problemas. Al tener integrados cores de distinta complejidad, se necesitarán
tantos compiladores como complejidades diferentes haya en el chip para compilar las instrucciones para
cada uno de ellos, y esto (compiladores e instrucciones para distintas complejidades) estará mezclado
en el espacio de memoria, produciendo nuevos problemas. Sin embargo, esta es la forma de mejorar el
rendimiento.

<!-- p. 23 -->

#### Espacio de Diseño
Concepto de Segmentación (Pipelining) La segmentación (pipelining) es una técnica de imple-
mentación por la cual se solapa la ejecución de múltiples instrucciones. Esto es posible debido a que
las instrucciones tienen múltiples etapas que suceden de manera secuencial, de las que se encargan
distintas partes del hardware. Si se tiene una sola instrucción en el procesador y no ingresa otra hasta
que la primera pase por todas sus etapas, el hardware destinado a las etapas que no están sucediendo
en un momento dado queda ocioso. Bajo condiciones ideales, esto mejora el throughput (cantidad de
outputs producidas o instrucciones ejecutadas por ciclo de reloj) tantas veces como etapas tenga el
pipeline.

¿Cuántas etapas poner en un pipeline? Se debe buscar una forma de estudiar cómo encontrar
un balance entre potencia y rendimiento, es decir, entre el rendimiento y la potencia (cantidad de
energía) que se gasta para ejecutar una instrucción. Luego se construyen las siguientes curvas:

Figura 11: Relación entre profundidad del pipeline y métricas de eficiencia. El eje horizontal (abscisas)
representa el retardo lógico total normalizado en unidades de FO4 por etapa, equivalente al número
efectivo de etapas del pipeline (menos FO4 por etapa implica más etapas). El eje vertical muestra el
valor relativo de distintas métricas normalizadas respecto al FO4 óptimo. Se observa que un pipeline
intermedio maximiza el rendimiento por vatio y la eficiencia consumo/tiempo, mientras que pipelines
muy profundos priorizan el IPC a costa de energía y complejidad.

    El Fan-out of Four (F04) es un concepto utilizado en diseño microelectrónico que se refiere a
la condición en la que una puerta lógica, típicamente un inversor, tiene su salida conectada a cuatro
puertas lógicas idénticas a ella (o a una carga capacitiva equivalente).
    Retardo F04: Es el retardo de propagación de una compuerta lógica con una carga que es el
cuádruple de la suya propia. Se utiliza como una medida del retardo de una etapa en el pipeline y es
independiente de la tecnología.

<!-- p. 24 -->

#### Rendimiento del Pipeline
    Mientras más etapas tenga el pipeline (el procesador), mayor será el rendimiento (se incrementarán
los bips, billones de instrucciones por segundo). Sin embargo, a partir de cierta cantidad de etapas
(punto óptimo de IPC), el rendimiento comienza a decrecer. Esto se debe a dos motivos:

      Los pipelines deben transferir la información desde un latch (circuito en el que la entrada pasa a
      la salida después de un ciclo de reloj) de una etapa a la siguiente, lo que consume una cantidad
      de tiempo significativa en relación con el retardo producido por la etapa.

      A medida que el pipeline se profundiza, cada vez que se produce un problema en el que se debe
      vaciar el pipeline, como un salto o una excepción, se perderá más cantidad de instrucciones, lo
      cual afecta negativamente al rendimiento.

    Los bips/W (billones de instrucciones por segundo por vatio) disminuyen a medida que aumenta
la profundidad del pipeline, ya que se gasta más energía debido a un mayor número de circuitos latch
y más tiempo de energía dedicada a una sola instrucción. Esto aumenta la carga capacitiva y, por lo
tanto, el consumo de energía, haciendo que el denominador (potencia) sea más grande y los bips/W
decrezcan.
    El rendimiento por vatio, con independencia de la tensión, puede ser medido utilizando bips2 /W
(ya que W = C × V 2 × f y bips2 contiene V 2 , simplificando la relación). Esta curva se mantiene
relativamente constante y luego cae rápidamente. Posteriormente, los vatios comienzan a tomar más
importancia y la curva de rendimiento también cae. El mismo comportamiento se observa con bips3 /W .
    En la zona donde las curvas comienzan a caer, se encuentra el mejor rendimiento posible en
términos de profundidad del pipeline para el procesador con respecto al consumo de energía. Esta
zona corresponde a sistemas de propósito general.
    Hacia la izquierda de esta zona (cerca del eje y) se encuentra el menor consumo (sacrificando algo
de desempeño), lo cual puede ser deseable para sistemas embebidos. Hacia la derecha se obtiene un
mayor desempeño a costa de un mayor consumo, esta zona corresponde a sistemas que requieren alto
rendimiento y en los cuales se puede proporcionar más potencia.

#### Técnicas Power Aware
   Las técnicas más efectivas para manejar la potencia en los sistemas incluyen:

      Clock Gating: Se deshabilita el reloj en una parte del circuito, de manera que los flip-flops en
      esa parte no consumen energía.

      Diferentes Dominios de Reloj: En zonas del sistema donde no se necesita alta frecuencia,
      se utiliza un dominio de frecuencia más bajo. Esto es ventajoso ya que la potencia aumenta
      proporcionalmente al cubo de la frecuencia. Por ejemplo, se puede reducir la frecuencia de reloj
      de la caché.

      Cores Simples: Los núcleos más simples consumen menos energía en comparación con los
      núcleos más complejos.

      Voltage Gating: Diferentes transistores en el diseño utilizan distintos voltajes de umbral pa-
      ra optimizar el retardo y/o la potencia. Esta técnica se emplea en bloques de caché y otros
      componentes.

      Power Gating: Todas las unidades funcionales del procesador se desconectan de la fuente de
      alimentación cuando no están en uso, consumiendo así de manera efectiva cero energía.

<!-- p. 25 -->

      Voltaje Dinámico y Escalado en Frecuencia: Tanto el voltaje como la frecuencia se ajustan
      dinámicamente para lograr mejores compensaciones entre potencia y rendimiento. A medida que
      se requiere más velocidad, se incrementan el voltaje y la frecuencia.

Figura 12: Intercambios de ventajas y desventajas en la integración de múltiples núcleos en un chip.

Cores Simples vs Cores Complejos
    Cores Simples: Los núcleos simples son procesadores que ejecutan las instrucciones en el orden
en que se reciben, sin realizar especulación, predicción de saltos, ni reordenamiento de instrucciones.
Son adecuados para realizar tareas en paralelo, aprovechando el paralelismo a nivel de datos.
    Cores Complejos: Los núcleos complejos, en contraste, intentan optimizar el orden de ejecución
de las instrucciones, predecir saltos, y mejorar el paralelismo de instrucciones utilizando diversas
técnicas. Esto conlleva un mayor número de transistores y, por tanto, un mayor consumo de energía.
Son adecuados tanto para tareas paralelas como para aquellas que no presentan paralelismo, donde
los núcleos simples no pueden aprovechar el paralelismo para mejorar el rendimiento.
    Cuándo Usar Cores Simples y Cuándo Cores Complejos
    En la gráfica adjunta, se representan los cores complejos con ítems negros (cambian de forma según
la cantidad de cores) y los cores simples con ítems grises (cambian de forma según el número de cores).
El eje X muestra la productividad relativa, que en los núcleos simples se mide según la cantidad de
operaciones realizadas por segundo. El eje Y muestra la potencia relativa consumida.
    A medida que se agregan más núcleos (cores), el throughput aumenta tanto para núcleos simples
como para complejos, aunque también lo hace la potencia. Sin embargo, los núcleos simples tienen
un límite en cuanto a throughput, ya que no proporcionan un aumento adicional al incrementar la
potencia, a diferencia de los núcleos complejos. En estos últimos, el throughput sigue aumentando con
la potencia, aunque con un mayor consumo de energía.
    La conclusión es que para un número reducido de núcleos (situación aplicable cuando no hay
un buen paralelismo), los núcleos complejos son preferibles, ya que los núcleos simples no ofrecen
un aumento significativo de rendimiento al incrementar la potencia, mientras que los complejos sí lo
hacen. Esto se puede observar en la figura, donde los núcleos simples y complejos con forma circular
(1 núcleo) y romboidal (2 núcleos) se comparan.
    Por otro lado, en situaciones con buen paralelismo y utilizando muchos núcleos, para un mismo
nivel de desempeño (relative chip throughput de 2.5), los núcleos complejos consumen mucha más
energía que los núcleos simples. Por lo tanto, los núcleos simples son más eficientes en entornos donde
hay buen paralelismo. Este fenómeno se puede observar en la figura, donde se comparan núcleos simples
con forma cuadrada (8 núcleos) y núcleos complejos con forma triangular (8 núcleos).

<!-- p. 26 -->

#### Diseño para Bajo Consumo
                                                                      Donde:

                                                                            N es la cantidad de transistores.
   El cálculo de la potencia en un chip es:                                 Vdd es la tensión de alimentación.

                 ρ = N · Vdd
                             ·C ·f ·A                                       C es la capacitancia.

                                                                            f es la frecuencia del clock.

                                                                            A es el factor de actividad.

   Si se intenta reducir la potencia, se pueden considerar las siguientes estrategias:

   1. Reducir la frecuencia (f ): Esto disminuiría la cantidad de instrucciones procesadas por se-
      gundo, resultando en un menor rendimiento y velocidad más lenta.

   2. Reducir la tensión de alimentación (Vdd ): Aunque esto reduce la potencia, también dismi-
      nuye la frecuencia de operación y hace al sistema menos tolerante al ruido, ya que la diferencia
      entre un 0 y un 1 lógico será menor.

   3. Reducir la cantidad de transistores (N ): Esto disminuiría el rendimiento del sistema, ya
      que habría menos capacidad para realizar operaciones simultáneamente.

   4. Reducir la capacitancia (C): Implica que los valores almacenados en la memoria RAM du-
      rarían menos tiempo, lo que requeriría refrescar la memoria con mayor frecuencia.

   5. Reducir el factor de actividad (A): Esto significaría que el sistema realizaría menos opera-
      ciones, lo que también conllevaría una disminución en el rendimiento.

    Ejemplo ”MAS HW en Paralelo por Menos Potencia”: Un bloque procesa sonido estéreo,
con todos los pulsos de sonido.
    El bloque superior procesa el canal L (izquierdo), mientras que el bloque inferior procesa el canal
R (derecho). Esto significa que cada bloque realiza la mitad del trabajo, es decir, procesa a la mitad
de la frecuencia ( 12 f ) bajo una tensión reducida (V ).

                                       1                              1
                                                                                  
                Potencia total =         f ·V ·C ·N           +         f ·V ·C ·N           =f ·V ·C ·N
                                       2                  L           2                  R
   En este caso, al dividir el trabajo entre los dos bloques (cada uno procesando un canal), se logra
una operación a menor frecuencia y bajo un voltaje reducido, lo cual optimiza el consumo de energía
mientras se mantiene el procesamiento del sonido estéreo.

<!-- p. 27 -->

                               Figura 13: Ejemplo ”Mas HW Paralelo”.

    Supongamos que tenemos un bloque con un área A, que consume una potencia P , y que opera
a una tensión V y frecuencia f . Existe una relación entre la tensión y la frecuencia a la que puede
trabajar el bloque.
    Si dividimos el bloque en dos partes, cada una trabajando a la mitad de la tensión V2 y a la mitad de
la frecuencia f2 , manteniendo la relación original entre la tensión y la frecuencia, entonces la potencia
total consumida por cada bloque será:
                                                 !2
                                                                       1 1   1
                                                               !
                                             V            f
                                Pnuevo ∝              ·            =    · P = P
                                             2            2            4 2   8
    Sin embargo, dado que la potencia aumenta con el cubo de la frecuencia (P ∝ f 3 ), al reducir la
frecuencia a la mitad:
                                                               !3
                                                           f         1
                                           Pnuevo ∝                 = P
                                                           2         8
    Por lo tanto, la potencia consumida por cada bloque es 0, 125 veces la potencia anterior.
    Como el área total ahora es el doble (2A), la densidad de potencia se reduce aún más. Si inicialmente
la densidad de potencia era PA , después de la división y reducción de la frecuencia y tensión, la nueva
densidad de potencia será:

                                             Pnuevo   0, 125 · P   0, 125 P   1 P
                  Densidad de Potencia =            =            =       · =   ·
                                              2A          2A          2   A  16 A
   Esto implica que la densidad de potencia será 16
                                                    de la densidad de potencia original.

#### Relación entre Tensión y Frecuencia de Trabajo del Procesador
    A muy baja tensión, los procesadores no pueden operar a alta frecuencia. A medida que se aumenta
la frecuencia de trabajo, es posible que se necesite más tensión para mantener el procesador estable.

<!-- p. 28 -->

    Se puede trabajar con frecuencia y tensión elevadas (por ejemplo, 1.3V a 5GHz), pero siempre es
preferible trabajar a la menor tensión posible para una misma frecuencia, ya que de lo contrario se
gasta más energía y se disipa más potencia.
    Por lo tanto, es importante trabajar en los límites de la menor tensión posible, es decir, la tensión
mínima funcional para la frecuencia deseada. Estos límites se representan en la gráfica como rectángulos
verdes, en los que no se especifica la potencia directamente, pero sí una temperatura para estimarla.

                                       Figura 14: Celda de SPU.

#### Retardo de las Interconexiones
   El gráfico a continuación muestra cómo varían los diferentes tipos de retardos frente a la evolución
de la tecnología. En particular, los retardos de las interconexiones globales tienden a aumentar a
medida que se incrementa la cantidad de transistores en un chip.

<!-- p. 29 -->

Figura 15: El rendimiento del transistor ( retardo ) escala linealmente con la tecnología El retardo de
la interconexión no escala con la tecnología.

    A primera vista, podría parecer que el uso de repeaters (repetidores) podría solucionar este pro-
blema, ya que ayudan a mantener las señales fuertes a lo largo de largas interconexiones. Sin embargo,
los repeaters tienen un costo en términos de energía, lo que puede afectar negativamente la eficiencia
energética del chip.

                                   Figura 16: Multi - Many cores.

    El gráfico muestra cómo la fracción del chip (en términos de distancia) alcanzada en un ciclo de
reloj disminuye con la evolución de la tecnología, específicamente con la reducción del tamaño de los

<!-- p. 30 -->

transistores. A medida que la tecnología avanza y los transistores se vuelven más pequeños, se necesita
atravesar una mayor cantidad de dispositivos para cubrir una misma distancia en el chip.
    Estos dispositivos adicionales actúan como líneas de transmisión, lo que introduce retardos adicio-
nales en la propagación de señales a través del chip. Como resultado, aunque los chips más avanzados
pueden contener más transistores, la fracción del chip que puede ser alcanzada en un solo ciclo de reloj
se reduce. Esto implica que, con el avance de la tecnología, es más difícil mantener una comunicación
rápida y eficiente entre diferentes partes del chip.

#### Rendimiento
   La medida fundamental del rendimiento de un computador es el tiempo. Dependiendo de los
requisitos del usuario, se puede distinguir entre varios tipos de rendimiento:

    Rendimiento del Sistema El rendimiento del sistema se refiere al tiempo transcurrido, tiempo
de respuesta, latencia o tiempo de ejecución. Este concepto se enfoca en la velocidad a la que se realiza
una tarea determinada. Por ejemplo, en un sistema de tiempo real, es preferible tener un tiempo de
respuesta rápido.

    Tiempo de Ejecución (Tej ) es el intervalo que transcurre desde que un usuario ejecuta un
programa hasta que recibe la respuesta del sistema. Este tiempo es crucial para evaluar el rendimiento
en tareas que requieren resultados inmediatos.

   Performance (P(x)) es una medida relativa que indica cuántas veces un computador es más
rápido que otro de referencia. Se puede expresar mediante la siguiente fórmula:

                                   Donde:
                    T ej (y)
          P (x) =            =n          Tej (y) es el tiempo de ejecución del procesador de referencia.
                    T ej (x)
                                         Tej (x) es el tiempo de ejecución del procesador x.
    Por lo tanto, si P(x) es igual a n, el procesador x es n veces más rápido que el procesador de
referencia y.

    Rendimiento de la CPU se basa en el tiempo de CPU y se refiere al Throughput, es decir, la
cantidad de tareas que se completan por unidad de tiempo. En sistemas como bases de datos, donde
es necesario organizar un gran número de tuplas dentro de un tiempo determinado, es preferible que
la CPU pueda completar más tareas por unidad de tiempo para mejorar el rendimiento general.

<!-- p. 31 -->

ANALOGÍA

                           El Concorde tiene un mejor rendimiento del sistema, ya que realiza el
                           viaje en menos tiempo debido a su mayor velocidad.

                           Throughput
                           El Boeing destaca en throughput al trasladar más pasajeros por hora, ofreciendo
                           una mayor capacidad de transporte.

                           Comparación
                                Tiempo de Respuesta: Concorde realiza el viaje más rápido.

                                Throughput: Boeing transporta más pasajeros por hora.

                           La elección entre ambos depende de si se prioriza la velocidad del viaje o la
                           capacidad de transporte.

#### Tiempo de CPU y CPI
   Tiempo de CPU es el tiempo que tarda el procesador en ejecutar un programa, y se puede
expresar de las siguientes maneras:

      Tiempo de CPU = Ciclos de clock para un programa × Duración del ciclo de clock

      Tiempo de CPU = Ciclos de clock para un programa / Frecuencia de clock

    CPI (Cycles Per Instruction) El CPI es el número medio de ciclos de reloj por instrucción y
se calcula como:

                                  Ciclos de clock para un programa
                                 CPI =
                                      Cantidad de instrucciones
   La ecuación del tiempo de CPU en términos de CPI es:

               Tiempo de CPU = Cantidad de instrucciones × CPI/Frecuencia de clock

Factores que Afectan el Rendimiento
   El rendimiento de la CPU depende de tres características principales:

      Frecuencia de reloj: Determinada por la tecnología hardware y la organización.

      CPI: Depende de la organización y arquitectura a nivel lenguaje máquina.

      Cantidad de instrucciones: Influenciada por la arquitectura a nivel lenguaje máquina y la
      tecnología de compiladores.

<!-- p. 32 -->

Ejemplo de Cálculo del CPI
   Cálculo del CPI Total Supongamos que un programa utiliza los siguientes porcentajes de tiempo
para distintos tipos de instrucciones:

          50 % acceso a ALU (1 ciclo) → 0.5                     10 % store (2 ciclos) → 0.2

          20 % load (2 ciclos) → 0.4                            20 % saltos (2 ciclos) → 0.4

   El CPI total se calcula como la suma ponderada de los CPI para cada tipo de instrucción:

                     CPI Total = (0,5 × 1) + (0,4 × 2) + (0,2 × 2) + (0,4 × 2) = 1,5

Cálculo del CPI Promedio
   El CPI promedio se puede calcular utilizando la fórmula:

                            TCPU × Frecuencia de reloj           Ciclos
                    CPI =                              =
                             Número de Instrucciones     Número de Instrucciones

   Si asumimos que existen n tipos de instrucciones, la fórmula para el CPI promedio es:

                                                  j=1 (CPIj × Fj )
                                                Pn
                                  CPI =
                                          Número total de instrucciones

    donde CPIj es el CPI para el tipo de instrucción j y Fj es la frecuencia de aparición de la instrucción
tipo j.

### Ejemplo Específico

          ALU: 1 ciclo (50 %) → CPI = 0.5                       Store: 2 ciclos (10 %) → CPI = 0.2

          Load: 2 ciclos (20 %) → CPI = 0.4                     Saltos: 2 ciclos (20 %) → CPI = 0.4

   El CPI total calculado es: CPI Total = 0,5 + 0,4 + 0,2 + 0,4 = 1,5
   Para mejorar el rendimiento, es útil identificar y optimizar las áreas donde se gasta más tiempo.
Invertir recursos en la optimización de los tipos de instrucciones que tienen el mayor impacto en el
CPI puede llevar a mejoras significativas en el rendimiento del sistema.

#### Ejemplo de Cálculo de CPI y MIPS
Datos del Ejemplo
    Para un procesador con frecuencia de 160 MHz, se ejecutó un programa durante 6 segundos. La
distribución de cada tipo de instrucción es la siguiente:

       Operaciones Aritmético-lógicas: 43 %, 1 ciclo

       Carga desde Memoria: 21 %, 2 ciclos

       Almacenamiento en Memoria: 12 %, 2 ciclos

       Instrucciones de salto: 24 %, 2 ciclos

<!-- p. 33 -->

Cálculo del CPI
   El CPI se calcula como: CPI =          (Frecuenciai × Ciclosi ) .Para el ejemplo dado:
                                      P

CPI = (0,43×1)+(0,21×2)+(0,12×2)+(0,24×2) = 0,43+0,42+0,24+0,48 = 1,57 ciclos/instrucción

Cálculo de MIPS
   El rendimiento en MIPS se calcula usando la fórmula: MIPS = Frecuencia CPI
                                                                          de reloj (MHz)

   Dado que la frecuencia de reloj es 160 MHz:
                       MIPS =          = 105,76 millones de instrucciones/segundo
                                  1,57

Cálculo del Total de Instrucciones
   El tiempo de ejecución del programa (Te ) es 6 segundos, y el ciclo de reloj (t) se calcula como:
                                          1                 1
                             t=                       =           segundos
                                  Frecuencia de reloj   160 × 106
   El número total de instrucciones (N ) se puede calcular usando:

                      Tiempo de CPU = CPI × Número total de instrucciones × t
   Reorganizando para encontrar N :

           Tiempo de CPU         6          6 × 160 × 106
     N=                  =                =               ≈ 634,39 millones de instrucciones
               CPI × t     1,57 × 160×10
                                        6        1,57

Medidas de Rendimiento
    La principal medida de rendimiento es el tiempo de ejecución. Una alternativa es MIPS (Millones
de Instrucciones por Segundo):

                                           Recuento de instrucciones
                           MIPS =
                                    Frecuencia de reloj × Tiempo de ejecución

                                        634,39 × 106
                                   MIPS =            ≈ 1,76 MIPS
                                       160 × 106 × 6
   Nota: Los MIPS son dependientes del repertorio de instrucciones, lo que dificulta la comparación
entre diferentes computadores y programas.

   MFLOPS: Otra alternativa son los MFLOPS (millones de operaciones de tiempo flotante por
segundo):

                           Número de operaciones de punto flotante de un programa
                MFLOPS =
                                           Tiempo de ejecución × 106
    Una estimación en MFLOPS depende de la máquina y del programa. Como se pensaron para medir
el rendimiento en operaciones de punto flotante, no son aplicables fuera de ese rango. Los MFLOPS
no son fiables ya que el conjunto de operaciones de punto flotante no es consistente para distintas
máquinas.

<!-- p. 34 -->

#### Factores de los que Depende el Rendimiento
   En general es de interés el rendimiento que tiene para una aplicación. ¿Cómo mejorar el rendimiento
de esta aplicación?

    Lo primero será definir cómo se quiere medir el rendimiento de la aplicación (por mes, por hora, por
segundo, operaciones por segundo, tiempo por operación /TPC/, etc). Evidentemente el rendimiento
de la aplicación será una composición de los rendimientos de muchos factores distintos:

      Lenguaje de Programación: El rendimiento varía según el lenguaje elegido (Java, C, etc.),
      ya que algunos lenguajes son más eficientes para ciertas tareas.

      Compilador: El compilador transforma el código fuente en código máquina, y su eficiencia
      afecta directamente al rendimiento.

      Arquitectura de la CPU: Diferentes arquitecturas ofrecen distintos tiempos de respuesta
      medidos en MIPS (para operaciones enteras) o MFLOP/s (para operaciones de punto flotante).
      La ISA (Instruction Set Architecture) es clave aquí.

      Datapath y Control: El diseño del datapath, que gestiona el flujo de datos en el procesador,
      y el control, que orquesta estos flujos, impactan en la eficiencia de las operaciones.

      Frecuencia de Reloj: La frecuencia determina cuántas operaciones pueden realizarse por se-
      gundo, afectando directamente al rendimiento.

   Entonces, el rendimiento es una composición de todos estos factores, y se podría formar una
ecuación para analizar cuáles de ellos se pueden mejorar.

<!-- p. 35 -->

#### Benchmark
    Un benchmark es un programa que ejecuta una aplicación y encuentra las circunstancias en las que
la aplicación corre mejor. Además, debería poder prever, con algunas mediciones hechas sobre algunas
arquitecturas, si realmente la aplicación de interés tendrá el desempeño deseado en cierta arquitectura.
    Se esperan dos cosas:

      Medir y poder refinar los componentes o la configuración de la arquitectura para obtener el
      mejor rendimiento (performance o desempeño).

      Poder determinar cuál sería la arquitectura disponible que cumpla con las medidas obtenidas de
      dichas arquitecturas para obtenerla y ejecutar la aplicación con el desempeño deseado.

   Un benchmark consiste en simular la ejecución de varios programas reales y analizar el rendimien-
to del sistema. Existen varios tipos de benchmarks, por ejemplo, el SPEC89 ejecuta 10 programas
proporcionando un único valor.
   Rendimiento global del computador: Benchmarks

      La única forma fiable es ejecutando distintos programas reales.

      Programas ”de juguete”: 10 100 líneas de código con resultado conocido. Ej.: Criba de
      Eratóstenes, Puzzle, Quicksort.

      Programas de prueba (benchmarks) sintéticos: simulan la frecuencia de operaciones y
      operandos de un abanico de programas reales. Ej.: Whetstone, Dhrystone.

      Programas reales típicos con cargas de trabajo fijas: actualmente, la medida más acep-
      tada.

      SPEC89: 10 programas proporcionando un único valor.

      SPEC92: 6 programas enteros (SPECint92) y 14 en punto flotante (SPECfp92), sin límites en
      opciones de compilación.

      SPEC95: 8 programas enteros (SPECint95) y 10 en punto flotante (SPECfp95). Dos opciones
      de compilación: la mejor para cada programa y la misma en todos (base).

      SPEC2000: 12 programas enteros y 14 en punto flotante. Dos opciones de compilación (la
      mejor: spec–, la misma spec–_base).

      SPEC2006.

      Otros:

         • HPC: LINPACK, SPEChpc96, Nas Parallel Benchmark.
         • Servidores: SPECweb, SPECSFS (File servers), TPC-C.
         • Gráficos: SPECviewperf (OpenGL), SPECapc (aplicaciones 3D).
         • Winbench, EEMBC.

    Se busca un benchmark que se aproxime lo mejor posible a la aplicacion que se desea ejecutar en
el sistema. De esta forma se puede obtener el equipo optimo para el uso que se vaya a dar.
    Hay benchmarks distintos para operaciones con integers y para operaciones de pto flotante de
manera tal que puede evaluar de acuerdo al tipo de operaciones que uno planee realizar. Por ejemplo:

<!-- p. 36 -->

               Figura 17: SPEC de los ultimos procesadores (SPEC2000) o Retirarodos.

   Un procesador puede tener rendimientos distintos para diferentes tipos de operaciones. Por ejemplo,
para operaciones de punto flotante, el procesador óptimo es el Power (verde), pero para operaciones
con enteros, el de mejor rendimiento es el P Xeon5160.

#### Evolución
    En este gráfico se puede ver la evolución de las familias de procesadores Alpha, AMD e Intel. A
un valor de SPEC (de integer en este caso) constante, se obtienen hipérbolas y a medida que aumenta
la frecuencia, también lo hace la performance.

<!-- p. 37 -->

                                        Figura 18: SPECint95.

    Se observan ciertas anomalías (desviaciones de las rectas), pero la más notable es el salto de
performance de los procesadores Alpha para una misma frecuencia. Esto ocurrió cuando mejoraron
sus predictores, lo que se debe a un cambio en la microarquitectura.

#### Rendimiento con Ley de Moore

                       Figura 19: Evolución del rendimiento de los procesadores.

    La figura muestra el crecimiento del rendimiento del procesador a lo largo de 40 años. Este gráfico
representa el rendimiento de los procesadores en relación con el VAX 11/780, medido por los valores
de referencia de números SPEC integer.
    La Ley de Moore, que establece que el número de transistores en un microchip se duplica apro-
ximadamente cada dos años mientras que el costo del microchip disminuye, se ha mantenido hasta
aproximadamente 2004. El rendimiento de los nuevos procesadores se mide en relación con el proce-
sador VAX 11/780, es decir, cuántas veces más rápido es el procesador nuevo en comparación con el
VAX 11/780.
    Antes de mediados de la década de 1980, el crecimiento del rendimiento de los procesadores estaba
impulsado en gran medida por los avances tecnológicos, con un promedio de alrededor del 22 % de
crecimiento anual. A partir de 1986, el crecimiento se acerca al 52 % anual, lo que implica una duplica-
ción del rendimiento cada 2 años. Este aumento se debe a las ideas arquitectónicas y organizacionales
más avanzadas, tipificadas en las arquitecturas RISC.
    En 2003, los límites de potencia, debido al final de la Escala Dennard y al paralelismo de nivel de
instrucción disponible, ralentizaron el rendimiento de los uniprocesadores al 23 % anual hasta 2011.

<!-- p. 38 -->

De 2011 a 2015, la mejora anual fue inferior al 12 %, o se duplicó el rendimiento cada 8 años, en parte
debido a los límites del paralelismo establecidos por la Ley de Amdahl.
    Desde 2015, con el fin de la Ley de Moore, la mejora ha sido de solo el 3,5 % por año, o el doble
de rendimiento cada 20 años.
    Escala Dennard: También conocida como la escalabilidad MOSFET, es una ley que establece
aproximadamente que, a medida que los transistores se hacen más pequeños, su densidad de potencia
se mantiene constante. Esto significa que el uso de energía se mantiene en proporción con el área, y
tanto el voltaje como la corriente se escalan hacia abajo con la longitud.
    Es importante tener en cuenta que las necesidades que satisfacen los procesadores han cambiado
con el tiempo, por lo que los benchmarks también deben evolucionar.

#### Mejora de Rendimiento Mediante Paralelismo - Ley de Amdahl
    En un sistema que demora cierto tiempo total en realizar una tarea, existen diferentes partes de
la tarea que corresponden a intervalos de tiempo que, en su conjunto, suman dicho tiempo total.
Evidentemente, será deseable mejorar la parte que más contribuye al tiempo total (reduciendo su
duración), ya que es la que más influye en el tiempo total.
    En un sistema paralelo, siempre habrá una parte de la tarea que no se puede paralelizar, es decir,
una parte secuencial que requiere un tiempo fijo para completarse. Esto implica que, de acuerdo con
el porcentaje de la tarea que es secuencial y el porcentaje que es paralelizable, puede tener sentido o
no agregar más núcleos al sistema.
    Mientras mayor sea el porcentaje del tiempo atribuido a la parte secuencial de la tarea, menor será
la mejora obtenida al agregar más núcleos, y viceversa. En otras palabras, ”no se pueden añadir más
núcleos de los que se pueden paralelizar”.
    La fórmula original de la Ley de Amdahl es la siguiente:
                                                                            !
                                                                  Fm
                               Tmejorado = Tantiguo × (1 − Fm ) +
                                                                  Am
   donde:

      Fm es la fracción del tiempo que el sistema utiliza el subsistema mejorado.

      Am es el factor de mejora introducido en el subsistema mejorado.

      Tantiguo es el tiempo de ejecución antiguo.

      Tmejorado es el tiempo de ejecución mejorado.

    La fórmula original de la Ley de Amdahl se puede reescribir utilizando la definición del incremento
de la velocidad A, que se da por la expresión:

                                                     Tantiguo
                                             A=                                                               (1)
                                                    Tmejorado
   Por lo tanto, la fórmula original de la Ley de Amdahl, se puede reescribir como:
                                         A=                                                                   (2)
                                              (1 − Fm ) + A
                                                          Fm
                                                            m

   donde:

      A es la aceleración o ganancia en velocidad conseguida en el sistema completo debido a la mejora
      de uno de sus subsistemas.

<!-- p. 39 -->

      Am es el factor de mejora que se ha introducido en el subsistema mejorado.
      Fm es la fracción de tiempo que el sistema utiliza el subsistema mejorado.
   Para que A sea lo más grande posible, tanto Fm como Am deben ser lo más grandes posible.

Ejemplo
   Supongamos que se cuenta con S = 10 procesadores, y que el 80 % del programa es paralelizable,
mientras que el 20 % no lo es. La aceleración (Speedup) se calcula como:
                                        Speedup =                                                          (3)
                                                    (1 − Fm ) + FSm
   donde Fm = 0,8 y S = 10, por lo tanto:
                                              1               1        1
                           Speedup =               0,8 = 0,2 + 0,08 = 0,28 ≈ 3,57                          (4)
                                       (1 − 0,8) + 10
    Queda claro que el desempeño de un sistema con múltiples procesadores (multiprocesador) está
limitado por la fracción del programa que debe ser ejecutada de manera secuencial.

Analogía de la ley de Amdahl
    Consideremos el siguiente escenario en el que se mide el impacto de un componente rápido en un
sistema:
                                                            La tortuga cubre el recorrido inicial de 100
                                                            metros en T minutos.

                                                                Con la intención de mejorar el desempeño del
                                                                equipo, el conejo entra en la segunda parte de
                                                                la carrera.

                                                                Supongamos que el conejo es tan rápido que
                                                                el segundo trecho es recorrido en un tiempo
                                                                despreciable, equivalente a cero.
                Figura 20: Ley de Amdahl.                 La tortuga gastó T /2 minutos para recorrer
                                                          su trecho.
   Queremos calcular el nuevo tiempo total de la carrera con la entrada del conejo ultra-rápido:

      Tiempo total = T /2 + 0 = T /2 minutos.

    Aunque la velocidad del conejo es inmensa, el tiempo total del equipo solamente se redujo a la
mitad. Esto se debe a que el tiempo total está limitado por la fracción de tiempo que toma la tortuga,
que es la parte más lenta del sistema.
    Ahora, si reducimos la participación de la tortuga a solamente 1/4 del recorrido, el tiempo total
será:

      Tiempo total = 1/4 × T = T /4 minutos.

    Esto demuestra que el desempeño global del sistema está determinado principalmente por la frac-
ción de participación del componente más lento. A medida que se reduce la proporción del tiempo que
consume el componente lento (la tortuga), el desempeño global mejora significativamente.
    Este ejemplo ilustra cómo la parte más lenta de un sistema limita el desempeño general, y muestra
la importancia de optimizar las secciones que tienen mayor impacto en el tiempo total.

<!-- p. 40 -->

#### Procesadores Heterogéneos
    Dado que no se puede reducir el tiempo aportado por la parte no paralelizable de una tarea
mediante la adición de más núcleos, para mejorar esta parte serial es necesario utilizar procesadores
más eficientes o algoritmos más avanzados. Esto ha dado lugar al diseño de sistemas heterogéneos,
que combinan núcleos con diferentes capacidades: núcleos complejos con un mayor IPC (Instrucciones
Por Ciclo) para ejecutar más rápidamente la parte serial de la tarea y núcleos simples para manejar
la parte paralela.

¿Cuándo es conveniente usar procesadores heterogéneos? Primero, asumimos que un chip
multinúcleo de un tamaño y generación de tecnología determinados puede contener como máximo n
núcleos base equivalentes, donde un solo núcleo base (BCE) representa la línea base.

      (a) Multicore simétrico con 16 núcleos equivalentes a un núcleo base.

      (b) Multicore simétrico con cuatro núcleos de cuatro BCE.

      (c) Multicore asimétrico con un núcleo de cuatro BCE y 12 núcleos de un BCE.

    Para el ejemplo en el que el 80 % del programa es paralelizable y el 20 % no lo es, podemos analizar
la eficiencia de cada configuración:

      En el caso (a), con 16 núcleos equivalentes, algunos núcleos estarían inactivos si la parte paraleli-
      zable del programa no utiliza todos los núcleos disponibles. Esto puede resultar en un desperdicio
      de recursos.

      En el caso (b), con cuatro núcleos de cuatro BCE, el paralelismo se aprovecha de manera más
      eficiente. Sin embargo, el número de núcleos de alto rendimiento podría ser insuficiente para
      manejar eficazmente la parte serial.

      En el caso (c), un multicore asimétrico con un núcleo de cuatro BCE y 12 núcleos de un BCE
      permitiría utilizar el núcleo complejo para la parte serial del programa y ocho de los núcleos
      simples para la parte paralela. Esto maximiza el uso de los recursos y mejora tanto la parte
      paralela como la parte serial del programa.

   Este enfoque permite optimizar el rendimiento general del sistema al combinar diferentes tipos de
núcleos para manejar eficientemente tanto la carga paralelizable como la serial.

<!-- p. 41 -->

#### Regla de Pollack
   La Regla de Pollack analiza el rendimiento de los procesadores a lo largo de los últimos 30 años
y establece que el rendimiento de un microprocesador mejora sub-linealmente con el aumento de la
complejidad. La regla de Pollack, formulada por Intel, se expresa como:
                                                        √
                                            Perf(R) ≈       R
    donde R representa la complejidad del procesador, que puede ser medida en términos de transistores
o consumo de energía.

Interpretación de la Regla de Pollack La regla establece que el aumento del rendimiento del
microprocesador debido a avances en la microarquitectura es aproximadamente proporcional a la
raíz cuadrada del aumento en la complejidad. Esto contrasta con el consumo de energía, que es
aproximadamente lineal con el aumento de la complejidad. En este contexto, la complejidad se refiere
a la lógica del procesador, es decir, su área.

Implicaciones
      Aumento de Transistores/Consumo: Un aumento de los transistores o consumo por un factor de
      2 resulta en una mejora en el rendimiento de aproximadamente 1.4 veces. Si se duplica el número
      de transistores (es decir, n = 2), el rendimiento mejora en un 40 % (es decir, ≈ 1,4).
      Avances en Microarquitectura: Los avances en microarquitectura pueden proporcionar mejoras
      adicionales en el rendimiento. Por ejemplo, una mejora en
                                                             √ la microarquitectura podría aumentar
      el rendimiento en aproximadamente un 41 % (es decir, 2 ≈ 1,41).
      Implementación Práctica: Aunque la regla sugiere que el rendimiento podría duplicarse mante-
      niendo el mismo consumo de energía, en la práctica, implementar una nueva microarquitectura
      en cada generación es desafiante. Por lo tanto, las ganancias reales en el rendimiento suelen ser
      menores.
      Procesadores Masivamente Paralelos: Una interpretación generosa de la regla sugiere que un
      dispositivo ideal podría contener cientos de núcleos de baja complejidad, cada uno operando
      a muy baja potencia, y juntos podrían realizar grandes cantidades de trabajo rápidamente.
      Esto se asemeja a las matrices de procesadores masivamente paralelos (MPPA), que se utilizan
      actualmente en sistemas integrados y aceleradores de hardware.
    En resumen, Pollack implica que el rendimiento mejora con la raíz cuadrada del aumento en la
complejidad, mientras que el consumo de energía aumenta de manera lineal. La combinación de mejoras
en la microarquitectura y el aumento en el número de transistores puede conducir a un aumento general
en el rendimiento, aunque mantener estas mejoras en la práctica es complejo.

<!-- p. 42 -->

#### Costo y Rendimiento de los Procesadores
   Los procesadores se imprimen en wafers de silicio utilizando un procedimiento litográfico. Cada
procesador ocupa solo una pequeña fracción del wafer, y la distribución de impurezas en el wafer
puede afectar el funcionamiento de los procesadores. Cuantos más procesadores se impriman en el
wafer, mayor será la probabilidad de que algunos de ellos funcionen correctamente.
      Die: La fracción del wafer donde se imprime un procesador. Cada die tiene un costo asociado.
      Final Test Yield (Rendimiento del Test Final): El porcentaje de circuitos integrados que pasan
      la última fase de pruebas.
      Die Yield (Rendimiento del Dado): El porcentaje del die que está libre de impurezas.

Costo del Circuito Integrado
   El costo total de un circuito integrado se calcula como:

                                 Costo del Dado + Costo de Testeo del Dado + Costo de Encapsulamiento
Costo del Circuito Integrado =
                                                      Rendimiento del Test Final
      Costo del Die: Determinado por el costo del wafer, el número de dados por wafer, y el rendi-
      miento del dado. Se calcula como:

                                                Costo del Wafer
                           Costo del Die =                            × Die Yield
                                             Número de Dies por Wafer
      Costo de Testeo del Die: Relacionado con la complejidad y la cantidad de RAM del chip.
      Costo de Encapsulamiento: El costo de empaquetar el chip.

<!-- p. 43 -->

Figura 21: Esta tabla muestra cuando un procesador es ingresado y retirado del mercado y cómo
varían los precios entremedio. Es importante tener esta tabla de antemano para estimar el costo a la
hora de poner un producto que utilice procesadores en el mercado.

<!-- p. 44 -->

                                                      Figura 22: Resumen conceptual de la Unidad N°2: Segmentación (Pipeline) de procesadores.
