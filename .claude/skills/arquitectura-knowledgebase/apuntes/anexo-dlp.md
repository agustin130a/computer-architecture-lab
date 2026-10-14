<!-- p. 243 -->

## ANEXO: Paralelismo a Nivel de Datos (Data-Level Parallelism, DLP)
   El paralelismo a nivel de datos (DLP) surge porque existen múltiples elementos de datos
que pueden ser operados en forma simultánea. Este tipo de paralelismo se explota cuando una misma
operación se aplica en paralelo sobre diferentes datos.

### Modelo SIMD
    El modelo SIMD (Single Instruction, Multiple Data) consiste en que una única instrucción es
ejecutada en paralelo sobre múltiples flujos de datos. De esta manera, todos los procesadores realizan
la misma operación, pero con datos distintos. Este concepto fue introducido en la taxonomía de Flynn
(1966).

       SISD (Single Instruction, Single Data): arquitectura escalar tradicional.

       SIMD (Single Instruction, Multiple Data): una instrucción aplicada a múltiples datos
       (ejemplo: GPUs).

       MISD (Multiple Instruction, Single Data): caso teórico, con aplicaciones muy limitadas
       (ejemplo: ciertos algoritmos de criptografía).

       MIMD (Multiple Instruction, Multiple Data): múltiples instrucciones sobre múltiples
       datos; corresponde a multiprocesadores modernos.

### Aplicaciones de SIMD
     SIMD explota directamente el paralelismo a nivel de datos y resulta fundamental en:

       Procesamiento digital de señales (DSP).

       Procesamiento de imágenes y video.

       Procesamiento de audio y radar.

       Computación científica y simulaciones vectoriales.

### Ejemplos de arquitecturas SIMD
     1. Procesadores vectoriales: utilizan registros vectoriales especiales que permiten aplicar ope-
        raciones en paralelo sobre un conjunto de datos. El flujo consiste en:

             Cargar un vector completo desde memoria.
             Aplicar la misma operación sobre todos los elementos del vector.
             Guardar nuevamente los resultados en memoria.

     2. Extensiones multimedia SIMD: agregadas a procesadores escalares convencionales (por
        ejemplo, MMX, SSE, AVX en Intel o NEON en ARM).

     3. Unidades de procesamiento gráfico (GPUs): arquitecturas masivamente paralelas basadas
        en el modelo SIMD, donde miles de hilos ejecutan en paralelo la misma instrucción sobre distintos
        datos.

<!-- p. 244 -->

Resumen. El paralelismo a nivel de datos es un complemento fundamental al ILP (Instruction-Level
Parallelism) y al TLP (Thread-Level Parallelism). Mientras que ILP se limita por dependencias entre
instrucciones y TLP depende del número de hilos disponibles, el DLP permite escalar el rendi-
miento cuando el problema a resolver involucra grandes volúmenes de datos homogéneos.

### Arquitecturas Vectoriales
   Las arquitecturas vectoriales son una forma clásica de explotar el paralelismo a nivel de datos
(DLP). La idea principal es trabajar con vectores completos de datos en lugar de operar elemento
por elemento.
   El flujo es el siguiente:
   1. Carga: se toma un conjunto de elementos dispersos en memoria principal y se cargan en registros
      vectoriales especiales.
   2. Ejecución: una sola instrucción vectorial indica la operación a realizar (por ejemplo, suma,
      multiplicación, división, lógica entera). Esto desencadena múltiples operaciones en paralelo, una
      por cada elemento del vector.
   3. Almacenamiento: los resultados procesados en los registros vectoriales son enviados nueva-
      mente a memoria.

                                                          Características principales
                                                               Los registros vectoriales son mucho más
                                                               grandes que los escalares, permitiendo ope-
                                                               rar con múltiples elementos simultánea-
                                                               mente.

                                                               Cada instrucción vectorial produce decenas
                                                               de operaciones registro–registro en paralelo
                                                               sobre datos independientes.

                                                               Incluyen unidades funcionales dedicadas:
                                                               suma/resta de coma flotante, multiplica-
                                                               ción, división, enteros y operaciones lógicas.

                                                               Proveen instrucciones load/store vecto-
                                                               riales que mueven bloques enteros de datos
Figura 132: Arquitectura vectorial: conjuntos de
                                                               entre memoria y registros vectoriales.
datos se cargan desde memoria a registros vecto-
riales, se procesan en paralelo con una sola ins-
trucción, y luego se almacenan nuevamente en
memoria.

Ejemplo típico Un bucle como:
                           for (i=0; i<N; i++) C[i] = A[i] + B[i];
puede ejecutarse con una sola instrucción vectorial de suma, en lugar de N instrucciones escalares.
Esto permite reducir la sobrecarga de control y aumentar el throughput significativamente.

<!-- p. 245 -->

#### Ejemplo en RISC-V
    Las letras mayúsculas representan vectores. En este caso, el vector Y es igual al vector X multi-
plicado por un literal a más el mismo vector Y .

Y = a * X + Y

   El código en RISC-V es el siguiente:

          fld     f0,a                    # Load scalar a
          addi    x28,x5,#256             # Last address to load
Loop:     fld f1,0(x5)                    # Load X[i]
          fmul.d f1,f1,f0                 # a × X[i]
          fld f2,0(x6)                    # Load Y[i]
          fadd.d f2,f2,f1                 # a × X[i] + Y[i]
          fsd f2,0(x6)                    # Store into Y[i]
          addi x5,x5,#8                   # Increment index to X
          addi x6,x6,#8                   # Increment index to Y
          bne x28,x5,Loop                 # Check if done

   El acento de este ejemplo es que se hace un load del literal a en el registro f0, se prepara el loop
con la última dirección y luego en cada iteración:

      Se hace el load de X[i].

      Se multiplica por a.

      Se hace el load de Y [i].

      Se suma el resultado de la multiplicación con Y [i].

      Se almacena nuevamente en Y [i].

      Se incrementan los punteros de X e Y .

      Se verifica si terminó el loop.

#### Ejemplo en RV64V (Vectorial)
    En el caso vectorial, se habilitan los registros de punto flotante vectoriales y se opera sobre conjuntos
completos de datos en una sola iteración. A diferencia del caso escalar, no se necesita un loop, ya que
las instrucciones vectoriales actúan sobre múltiples elementos simultáneamente.

vsetdcfg 4*FP64            # Enable 4 DP FP vregs
fld      f0,a              # Load scalar a
vld      v0,x5             # Load vector X
vmul     v1,v0,f0          # Vector-scalar multiply
vld      v2,x6             # Load vector Y
vadd     v3,v1,v2          # Vector-vector add
vst      v3,x6             # Store the sum
vdisable                   # Disable vector regs

<!-- p. 246 -->

Descripción

       vsetdcfg habilita los registros vectoriales de punto flotante.

       Se carga el escalar a en un registro (fld).

       Se carga el vector X completo en un registro vectorial (vld).

       Se realiza la multiplicación vector-escalar (vmul), aplicando a × X en paralelo sobre todos los
       elementos.

       Se carga el vector Y (vld) y se realiza la suma vectorial (vadd).

       El resultado se almacena de una sola vez en memoria (vst).

       Finalmente, se deshabilitan los registros vectoriales (vdisable).

Observación No hay loop explícito: en una sola iteración se procesan todos los elementos del vector.
Esto ilustra claramente la diferencia entre el enfoque escalar (SISD) y el enfoque vectorial (SIMD),
donde una sola instrucción opera en paralelo sobre múltiples datos.

### Extensiones SIMD para Multimedia
    Muchas aplicaciones multimedia (procesamiento de audio, video, imágenes, gráficos) operan so-
bre tipos de datos más angostos que los procesadores de 32 bits tradicionales. Para aprovechar
el paralelismo a nivel de datos en estos casos, se introdujeron las extensiones de conjuntos de
instrucciones SIMD, que permiten aplicar la misma operación sobre múltiples datos en paralelo.

       Al igual que las instrucciones vectoriales, una instrucción SIMD especifica la misma operación
       sobre un conjunto de datos.

       A diferencia de las instrucciones vectoriales clásicas, las extensiones SIMD suelen especificar
       menos operandos y, en consecuencia, utilizan archivos de registros mucho más pequeños.

       Estas extensiones presentan tres limitaciones importantes:

         1. No cuentan con un registro de longitud de vector que permita variar el tamaño diná-
            micamente.
         2. No soportan transferencias de datos con stride ni operaciones gather/scatter (acceso
            disperso en memoria).
         3. No disponen de registros de máscara, lo que limita la ejecución condicional a nivel de
            elementos vectoriales.

Ejemplos comunes Extensiones como MMX, SSE y AVX en procesadores Intel, o NEON en pro-
cesadores ARM, representan este tipo de SIMD orientado a multimedia.

### x86: Extensiones SIMD para Multimedia
   Otro tipo de SIMD, muy popular en la arquitectura x86, son las llamadas instrucciones mul-
timedia. Su fundamento está en que muchos algoritmos de procesamiento digital de señales (DSP),
audio, video e imagen, trabajan con tipos de datos pequeños (8 o 16 bits), en lugar de enteros de
32 o 64 bits.

<!-- p. 247 -->

Idea principal En lugar de sumar dos registros de 64 bits como un todo, las extensiones SIMD
permiten dividir esos registros en múltiples subcampos más pequeños y realizar operaciones en paralelo.
Por ejemplo, en lugar de sumar 64 + 64, se pueden realizar 8 sumas de 8 bits o 4 sumas de 16 bits
dentro del mismo registro.
    Esto aumenta el paralelismo sin requerir la complejidad de un procesador vectorial completo. A
diferencia de las arquitecturas vectoriales:

      No se utilizan registros vectoriales grandes, sino registros más pequeños subdivididos.

      No existen operaciones de memoria vectorial (vector load/store).

      La complejidad de hardware es menor, aunque requiere consideraciones de caché.

Principales extensiones en x86

      MMX (Multi-Media eXtension) (1996): Utilizaba registros de 64 bits. Permitía:

        • Ocho operaciones de 8 bits en paralelo.
        • Cuatro operaciones de 16 bits en paralelo.

      SSE (Streaming SIMD Extension): Introdujo los registros XMM de 128 bits. Permitía:

        • Dieciséis operaciones de 8 bits en paralelo.
        • Ocho operaciones de 16 bits en paralelo.
        • Cuatro operaciones de 32 bits en paralelo.

      AVX (Advanced Vector Extension): Extendió los registros a YMM de 256 bits. Permitía:

        • Treinta y dos operaciones de 8 bits en paralelo.
        • Dieciséis operaciones de 16 bits en paralelo.
        • Ocho operaciones de 32 bits en paralelo.

Comparación con procesadores vectoriales

      Ambas aproximaciones explotan el paralelismo a nivel de datos (SIMD).

      Los procesadores vectoriales acceden a memoria con instrucciones vectoriales (load/store de
      vectores completos).

      Las extensiones SIMD multimedia, en cambio, trabajan únicamente sobre registros subdivididos,
      sin longitud vectorial variable ni operaciones de memoria dispersa.

<!-- p. 248 -->

#### Ejemplo SIMD estilo ``GMMX'': Y = a X + Y (4 anchos en paralelo)
                                                          Descripción
                                                                Copia del escalar: splat.4D duplica
                                                                el escalar a en las 4 posiciones del regis-
                                                                tro vectorizado (4 copias).
                                                                Cargas empaquetadas: fld.4D trae
                                                                {X[i], X[i + 1], X[i + 2], X[i + 3]} (y lo
   fld         f0, a             # Load scalar a                mismo para Y ) en un solo registro.
   splat.4D    f0, f0            # Make 4 copies of a
   addi        x28, x5, #256     # Last address to load         Operaciones SIMD: fmul.4D y
                                                                fadd.4D operan en paralelo sobre las 4
   Loop:                                                        posiciones (una instrucción, 4 productos
     fld.4D      f1, 0(x5)       # Load X[i] ... X[i+3]         o sumas).
     fmul.4D     f1, f1, f0      # a*X[i] ... a*X[i+3]
     fld.4D      f2, 0(x6)       # Load Y[i] ... Y[i+3]         Store empaquetado: fsd.4D escribe
     fadd.4D     f2, f2, f1      # a*X + Y (4 lanes)            los 4 resultados de una vez.
     fsd.4D      f2, 0(x6)       # Store Y[i] ... Y[i+3]
     addi        x5, x5, #32     # Increment index to X         Avance del loop: los addi avanzan los
     addi        x6, x6, #32     # Increment index to Y         punteros para procesar el siguiente gru-
     bne         x28, x5, Loop   # Check if done                po de 4 elementos.

                                                          Intuición de ancho El registro que se ope-
                                                          ra se interpreta como 4 elementos en paralelo
                                                          (p. ej., dividir un registro en 4 subcampos); en
                                                          lugar de sumar dos registros “enteros”, se su-
                                                          man/multiplican cuatro datos empaquetados
                                                          con una sola instrucción.

### GPU: Graphics Processing Unit
   Las GPUs surgieron a fines de los 90 principalmente para procesamiento gráfico (imágenes 2D/3D,
video). Con el tiempo se convirtieron en una plataforma de cómputo masivamente paralelo utilizada
en blockchain, HPC y, más recientemente, en inteligencia artificial.

Diferencias fundamentales con la CPU

       CPU: está diseñada para ejecutar un hilo secuencial lo más rápido posible, con mucho hard-
       ware de control y jerarquías de caché sofisticadas. Puede manejar unas pocas decenas de hilos
       en paralelo.

       GPU: está diseñada para maximizar el throughput, ejecutando miles de hilos en paralelo.
       Reduce el hardware de control y privilegia la cantidad de núcleos (cores). La latencia de memoria
       no se elimina, pero se amortiza ocultándola con paralelismo masivo.

Arquitectura

<!-- p. 249 -->

Figura 133: Comparación CPU vs GPU: la CPU dedica gran parte del chip a control y jerarquías de
memoria, mientras que la GPU maximiza la proporción de cores para explotar el paralelismo masivo
de datos.

Notas

       NVIDIA domina actualmente el mercado de GPUs, seguida por AMD y otras competidoras
       menores.

       Su desarrollo explosivo se asocia a la IA moderna, donde se requieren arquitecturas con miles
       de cores paralelos.

       Ejemplo: una GPU moderna puede superar los 10.000 cores de procesamiento.

### CPU vs GPU

Figura 134: Comparación arquitectónica CPU vs GPU. La CPU dedica gran parte del chip a lógica
de control y jerarquías de caché, mientras que la GPU maximiza la cantidad de ALUs para cómputo
paralelo.

Características destacadas

       CPU:

<!-- p. 250 -->

        • Optimizada para baja latencia en accesos a memoria cacheada.
        • Compleja lógica de control para ejecución fuera de orden y especulativa.
        • Pocos núcleos pero muy potentes, con alto rendimiento por hilo.

       GPU:

        • Optimizada para paralelismo de datos y alto throughput.
        • Arquitectura tolerante a la latencia de memoria mediante miles de hilos en paralelo.
        • Más transistores dedicados a unidades de cómputo (ALUs) en lugar de control.

Tabla comparativa

 Aspecto                   CPU                                    GPU
 Objetivo                  Baja latencia, alto rendimiento por    Alto throughput, miles de hilos
                           hilo
 Unidades de cómputo       Pocos núcleos complejos                Cientos/miles de ALUs simples
 Control                   Lógica compleja (OoO, especula-        Control mínimo, simplicidad
                           ción)
 Memoria                   Jerarquía profunda (L1, L2, L3)        L2 compartida, alta dependencia de
                                                                  DRAM
 Uso de transistores       Mayormente en control y cachés         Mayormente en ALUs para cómputo
                                                                  paralelo
 Aplicaciones típicas      Procesamiento secuencial, sistemas,    Gráficos, IA, blockchain, HPC, DLP
                           ILP

### CUDA: Compute Unified Device Architecture

Figura 135: Ecosistema CUDA: librerías optimizadas, lenguajes de programación soportados y familias
de GPUs habilitadas para CUDA.

<!-- p. 251 -->

   CUDA es la plataforma de cómputo paralelo de propósito general y el modelo de programación
desarrollado por NVIDIA. Permite aprovechar el motor de cómputo masivo de las GPUs para resolver
problemas complejos de forma más eficiente que en CPUs tradicionales.

      Objetivo: proporcionar un framework que exponga el paralelismo masivo de las GPUs.

      Modelo: programa heterogéneo compuesto por código de host (CPU) y de device (GPU).

      Lenguajes soportados: C, C++, Fortran, Python, Java (wrappers) y directivas como Ope-
      nACC.

      Middleware y librerías: cuDNN, cuBLAS, cuFFT, cuRAND, cuSPARSE, MAGMA, Thrust,
      NPP, entre otras.

Compilación y ejecución

      Los programas CUDA se compilan con nvcc, el compilador de NVIDIA.

      El resultado es un binario heterogéneo que contiene código para CPU (host) y para GPU
      (device).

      El programador puede definir kernels (funciones que se ejecutan en la GPU) y configurar explí-
      citamente la cantidad de threads, bloques y grids.

Alternativas

      OpenCL: estándar abierto para cómputo heterogéneo, soportado por múltiples fabricantes.

      Vulkan y OpenGL: APIs gráficas que permiten acceso de bajo nivel al hardware, con algunas
      capacidades de cómputo general.

Flujo de Compilación CUDA
   1. Programa integrado en C con extensiones CUDA: El programador escribe un único
      código en C/C++ que incluye palabras clave de CUDA (__global__, __device__, __host__).
      Este código contiene tanto las partes que se ejecutarán en la CPU (host) como en la GPU
      (device).

   2. Compilador NVCC: El compilador de NVIDIA (nvcc) divide automáticamente el código en
      dos secciones:

           Host code: Se compila con un compilador C/C++ convencional (ej. GCC, Clang, MSVC).
           Incluye la lógica de control, gestión de memoria y lanzamiento de kernels en la GPU.
           Device code: Se traduce a un código intermedio llamado PTX (Parallel Thread Execu-
           tion), que representa un ensamblador virtual de CUDA.

   3. Host Code: Tras pasar por el compilador de C estándar, genera el ejecutable del lado de la
      CPU. Este código contiene las llamadas a kernels y coordina la ejecución en la GPU.

   4. Device Code (PTX): El código PTX se compila en tiempo de ejecución mediante un compi-
      lador just-in-time, produciendo instrucciones máquina específicas para la GPU instalada en el
      sistema.

<!-- p. 252 -->

   5. Ejecución en plataforma heterogénea: Finalmente, el programa se ejecuta en un sistema
      compuesto por CPU y GPU. La CPU controla la ejecución general, mientras que la GPU acelera
      los cálculos masivos en paralelo.

                           Figura 136: Flujo de compilación en CUDA con nvcc.

### Traza de Programas con GPU
   El flujo de ejecución de un programa que utiliza GPU puede resumirse en los siguientes pasos:

   1. Código en CPU: El programa principal comienza ejecutándose en el procesador (CPU). Allí
      se prepara la lógica y los datos.

   2. Invocación de un kernel: Un kernel es el código que se ejecuta en la GPU. La CPU es la
      encargada de:

           Alocar memoria en la GPU.
           Copiar los datos desde la CPU hacia la GPU.
           Invocar la ejecución del kernel en la GPU.
           Recuperar los resultados desde la GPU a la CPU.

   3. Ejecución en la GPU: El kernel se ejecuta de forma masivamente paralela en una grilla de
      threads:

           Una grilla (grid) está compuesta por múltiples bloques (blocks).
           Cada bloque está compuesto por múltiples threads.
           Tanto las grillas como los bloques pueden organizarse en 1D, 2D o 3D, dependiendo de la
           naturaleza de los datos (vectores, imágenes, volúmenes).

   4. Mapeo de datos: El diseño 1D, 2D o 3D facilita el mapeo de threads a datos reales:

           Una imagen 2D puede asignar cada píxel (x,y) a un thread (x,y).

<!-- p. 253 -->

           Un volumen 3D puede mapear cada voxel (x,y,z) a un thread (x,y,z).

Figura 137: Organización de la ejecución en GPU: la CPU invoca kernels que se ejecutan en grillas de
bloques, y cada bloque contiene múltiples threads.

Ejemplo: Vector Add en GPU (CUDA)
   La ejecución en GPU sigue una traza en tres pasos principales:

   1. Asignación de memoria y copia hacia la GPU: La CPU reserva memoria en la GPU (device
      memory) para los vectores y copia los datos desde la memoria del host (CPU) a la memoria del
      dispositivo (GPU).

   2. Ejecución del kernel: La CPU invoca el kernel en la GPU. Cada thread de la GPU se encarga
      de procesar una parte del vector (suma elemento a elemento).

   3. Copia de resultados y liberación de memoria: Los resultados calculados en la GPU se
      copian nuevamente hacia la memoria del host. Finalmente, se libera la memoria reservada en el
      dispositivo.

<!-- p. 254 -->

Figura 138: Flujo CPU–GPU en CUDA: memoria host → memoria device, ejecución del kernel y copia
de resultados.

### CUDA Functions y Ejecución de Kernels
   Cuando se programa en CUDA, las funciones se clasifican según dónde se ejecutan y desde dónde
pueden ser llamadas:

      __device__ → Se ejecutan en el device (GPU) y sólo pueden ser llamadas desde el device.

      __global__ → Se ejecutan en el device pero se llaman desde el host (CPU). Estas funciones son
      los kernels.

      __host__ → Se ejecutan en el host (CPU) y sólo se llaman desde el host.

   Para poder ejecutar un kernel en GPU es necesario:

   1. Definir la grilla y los bloques de threads. La grilla puede ser de 1D, 2D o 3D, y cada
      bloque también puede organizarse en hasta 3 dimensiones. Al invocar un kernel se le pasan estos
      parámetros como argumentos de ejecución:

                                  kernel´ < dimGrid, dimBlockˇ > (. . .)

   2. Asignar memoria en GPU y transferir datos. Esto se hace mediante:

           cudaMalloc((void**)&x, size) para reservar memoria en la GPU.
           cudaMemcpy(d_x, x, size, cudaMemcpyHostToDevice) para copiar datos desde la CPU
           hacia la GPU.
           cudaMemcpy(x, d_x, size, cudaMemcpyDeviceToHost) para traer los resultados de vuel-
           ta a la CPU.

<!-- p. 255 -->

   3. Ejecutar el kernel. Una vez definido el número de bloques y threads, el kernel se ejecuta en
      paralelo en la GPU. Por ejemplo, si se define:
                                          vecAdd´ < 1, nˇ > (A, B, C);
      significa que se lanza un único bloque con n threads, cada thread procesa un elemento del vector.
    De esta forma, la CPU organiza la grilla de ejecución (dimensiones de bloques y threads), invoca
el kernel en la GPU y luego recoge los resultados.

### Ejecución de Kernels en CUDA
    Un kernel se define en CUDA con la declaración __global__. La cantidad de threads que ejecutan
ese kernel para una invocación se especifica mediante la sintaxis de configuración de ejecución «<...»>.
Cada thread tiene un identificador único que se accede a través de variables internas como threadIdx,
blockIdx y blockDim.
                            Listing 1: Ejemplo de kernel para suma de vectores.
__global__ void VecAdd ( f l o a t ∗ A, f l o a t ∗ B, f l o a t ∗ C) {
    int i = t h r e a d I d x . x ; // ID d e l t h r e a d d e n t r o d e l b l o q u e
    C[ i ] = A[ i ] + B [ i ] ;
}

int main ( ) {
    ...
    // Kernel i n v o c a t i o n con N t h r e a d s
    VecAdd<<<1, N>>>(A, B, C ) ;
    ...
}
Este caso simple utiliza un único bloque con N threads. Cada thread ejecuta la misma instrucción,
pero sobre diferentes datos (paradigma SIMD: Single Instruction, Multiple Data).

Threads, Bloques y Grids
   Los threads en CUDA se organizan jerárquicamente:
      Thread: unidad mínima de ejecución.
      Block: conjunto de threads. Puede ser 1D, 2D o 3D.
      Grid: conjunto de bloques, también puede organizarse en 1D, 2D o 3D.
   Cada thread calcula su índice global combinando:
                           globalIdx = blockIdx.x × blockDim.x + threadIdx.x

Limitaciones de Hardware
   La ejecución real se da en Streaming Multiprocessors (SMs), que tienen un máximo de 1024
threads por bloque. Esto implica:
      Si N ≤ 1024, alcanza con un solo bloque.
      Si N > 1024, deben usarse múltiples bloques. Ejemplo: para N = 2048, se requieren 2 bloques
      con 1024 threads cada uno.

<!-- p. 256 -->

Comparación con Código Secuencial
   En código secuencial, la suma de vectores se realizaría con un bucle:
f or ( int i = 0 ; i < N; i ++)
     C[ i ] = A[ i ] + B [ i ] ;
   En CUDA, cada thread procesa un elemento, eliminando el bucle explícito. Lo único que varía entre
threads es el índice i, obtenido mediante las variables internas (threadIdx, blockIdx, blockDim).

### Ejecución con Múltiples Bloques
    Cuando el vector a procesar es más grande que el máximo número de threads por bloque (1024),
es necesario dividir la ejecución en múltiples bloques. Un caso típico es fijar el tamaño de bloque en
256 threads, y calcular la cantidad de bloques necesarios como:
                                                           &    '
                                                       N
                                          numBlocks =

   El índice global se obtiene combinando el identificador del bloque y el identificador del thread
dentro de ese bloque:
                          i = blockIdx.x × blockDim.x + threadIdx.x

[caption={Kernel de suma de vectores con múltiples bloques.}]
__global__ void VecAdd(float* A_d, float* B_d, float* C_d, int N) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < N) // condición de seguridad
        C_d[i] = A_d[i] + B_d[i];
}

En este caso, cada bloque procesa 256 elementos. Por ejemplo:

      El Bloque 0 procesa los índices 0 . . . 255.

      El Bloque 1 procesa los índices 256 . . . 511.

      El Bloque N − 1 procesa los últimos elementos, incluso si no completa los 256.

<!-- p. 257 -->

Ejecución en el Hardware
    En la GPU, los bloques son asignados a los Streaming Multiprocessors (SMs). Cada SM puede ma-
nejar hasta 1024 threads en paralelo, agrupados internamente en warps de 32 threads. La organización
jerárquica queda entonces:

      Warp: 32 threads.

      Block: conjunto de warps (por ejemplo, 8 warps si el bloque tiene 256 threads).

      Grid: conjunto de bloques distribuidos sobre los distintos SMs.

Memoria en CUDA
      Memoria global: accesible por todos los threads, pero lenta.

      Memoria compartida (shared): dentro de cada bloque, mucho más rápida, requiere que el
      programador gestione la copia desde la memoria global.

      Registros: memoria privada de cada thread.

      Memoria constante: una sección de la memoria global marcada como read-only, optimizada
      para accesos uniformes.

   El uso eficiente de la memoria compartida y de la organización en warps es lo que permite apro-
vechar al máximo la arquitectura paralela de la GPU.

¿Por qué existen dos niveles de threads?
    La organización de CUDA utiliza una grilla (grid) de bloques (blocks) de threads, en lugar
de un único bloque gigante. De esta manera, el Gigathread Engine reparte bloques entre los SMs
(Streaming Multiprocessors), cada uno con registros, memoria compartida y planificador propio.
    Dentro de un bloque, los threads se ejecutan en warps de 32. Conocer el tamaño del bloque
al invocar el kernel permite preasignar recursos (sin asignación dinámica), haciendo muy rápido el
cambio de contexto.

      Miles de cores agrupados en decenas de SMs; cada SM maneja bloques, no toda la grilla.

      Un bloque consume recursos del SM (registros, memoria compartida). Al finalizar, libera recursos
      y el SM toma otro bloque.

      Los threads de un bloque no corren todos a la vez: se planifican en warps de 32.

Ejemplo 1D: Suma de vectores
[ caption={Kernel y función host para suma de vectores en CUDA}]
__global__ void vecAddKernel(const float* A, const float* B, float* C, int N) {
    // índice global del thread dentro de la grilla
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < N) C[i] = A[i] + B[i];
}

void vecAdd(const float* A_h, const float* B_h, float* C_h, int N) {

<!-- p. 258 -->

     size_t bytes = N * sizeof(float);
     float *A_d = nullptr, *B_d = nullptr, *C_d = nullptr;

     // 1) Reservar y copiar a device
     cudaMalloc((void**)&A_d, bytes);
     cudaMalloc((void**)&B_d, bytes);
     cudaMalloc((void**)&C_d, bytes);
     cudaMemcpy(A_d, A_h, bytes, cudaMemcpyHostToDevice);
     cudaMemcpy(B_d, B_h, bytes, cudaMemcpyHostToDevice);

     // 2) Lanzar kernel: bloques de 256 hilos (<= 1024 hilos por bloque)
     const int blockSize = 256;
     const int gridSize = (N + blockSize - 1) / blockSize; // ceil(N/256)
     vecAddKernel<<<gridSize, blockSize>>>(A_d, B_d, C_d, N);
     cudaDeviceSynchronize();

     // 3) Copiar resultado y liberar
     cudaMemcpy(C_h, C_d, bytes, cudaMemcpyDeviceToHost);
     cudaFree(A_d); cudaFree(B_d); cudaFree(C_d);
}

Ejemplo 2D: Procesamiento de imágenes

                      Listing 2: Kernel CUDA para operación sobre imagen en 2D
__global__ void imgOpKernel ( const unsigned char∗ in , unsigned char∗ out ,
                                      int width , int h e i g h t , int p i t c h ) {
    int x = b l o c k I d x . x ∗ blockDim . x + t h r e a d I d x . x ; // columna
    int y = b l o c k I d x . y ∗ blockDim . y + t h r e a d I d x . y ; // f i l a
    i f ( x >= width | | y >= h e i g h t ) return ;

      int i d x = y ∗ p i t c h + x ;                 // a c c e s o l i n e a l
      out [ i d x ] = 255 − i n [ i d x ] ;           // e j e m p l o : n e g a t i v o de imagen en g r i s
}

// Lanzamiento ( b l o q u e s 16 x16 ; g r i l l a c u b r e t o d a l a imagen )
dim3 b l o c k ( 1 6 , 1 6 ) ;
dim3 g r i d ( ( width + b l o c k . x − 1 ) / b l o c k . x ,
               ( height + block . y − 1) / block . y ) ;
imgOpKernel<<<g r i d , bl ock >>>(in_d , out_d , width , h e i g h t , width ) ;
    Puntos clave:
      blockDim: tamaño del bloque (p.ej., 256 en 1D, 16x16 en 2D).
      blockIdx y threadIdx: identificadores del bloque y del hilo.
      Máx. hilos por bloque típico: 1024 (según arquitectura).
      Fórmula usual para cobertura completa:
                                                          &          '
                                                            N
                                              gridSize =
                                                         blockSize
