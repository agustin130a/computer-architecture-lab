# Computer Architecture Lab

Simuladores y guías interactivas de arquitectura de computadoras, pensados para
estudiar tocando: todo corre en el navegador y se despliega en **GitHub Pages**.

**Sitio:** <https://agustin130a.github.io/computer-architecture-lab/>

| Página | Qué es |
| --- | --- |
| [Inicio](web/index.html) | Índice del sitio: una tarjeta por página con enlaces directos a cada sección. |
| [Coloquio](web/coloquio.html) | Modalidad del coloquio y todos los temas que entran (marcando los que más salen), cada uno con resumen y enlace a la sección donde se desarrolla. |
| [Procesador y paralelismo](web/pipeline.html) | Unidades 2 a 4: monociclo y multiciclo, pipeline y speedup, riesgos (simulador de pipeline), loop unrolling y software pipelining, planificación estática y dinámica, excepciones precisas con vector de estado y ROB, Tomasulo ciclo a ciclo, superescalar/VLIW y multithreading, con quiz. |
| [Simulador de Tomasulo](web/tomasulo.html) | Planificación dinámica fuera de orden, ciclo a ciclo (Issue → Execute → Write Back). |
| [Predicción de saltos](web/predictores.html) | Contador saturado de 2 bits, 1 bit vs. 2 bits con BTAC/BTB, predictor local, global, comparación lado a lado, híbrido (juez) y quiz. |
| [Coherencia de caché](web/coherencia.html) | Unidad 6: snoopy (dos estados, MSI, MESI, con diagrama de estados y saturación del bus) y coherencia con directorio (red de cuatro nodos, mensajes y sobrecarga), más consistencia de memoria, con simuladores y quiz. |
| [Jerarquía de memoria y caché](web/cache.html) | Unidad 5 completa: emplazamiento directo / N-way / totalmente asociativo, simulador de caché con caché de víctima, simulador de tipos de fallo (las 3 C), políticas, rendimiento, caché y memoria virtual (física, parcial y total) y memoria principal, con quiz. |

## Simulador de Tomasulo

Port a web (TypeScript + Canvas) de **Tomasulo-Visual**. La aplicación original
de escritorio (Java Swing) se conserva como referencia en
[`reference-java/`](reference-java/); su motor no puede ejecutarse en un
navegador, por eso el motor de simulación fue **reescrito en TypeScript**
replicando ciclo a ciclo el comportamiento del original.

- **Selector de ejemplos**: los programas `.s` incluidos se eligen desde un
  desplegable. También se puede cargar un archivo `.s` propio o editar el código.
- **Latencias configurables** por unidad funcional.
- **Controles**: paso a paso (1 ciclo), multi-paso configurable, ejecutar todo,
  reiniciar.
- **Diagrama en Canvas** con el estado de cada instrucción en el pipeline.
- **Tabla de tiempos** accesible (Issue / Exe / Write Back) y lista de registros
  ocupados — alternativa textual al canvas para lectores de pantalla.

### Fidelidad del motor

El motor TypeScript (`web/src/engine/`) es un port estructural de
`MainLogic.java`. Se valida contra la salida del motor Java de referencia
(`HeadlessTest`) para los 7 programas de ejemplo: la tabla de tiempos por
instrucción y el número total de ciclos coinciden **exactamente**.

```
npm test    # en web/  → 7/7 samples match the Java golden output
```

Nota: los *valores* numéricos de registros/memoria no son reproducibles porque
el motor Java inicializa la memoria con valores aleatorios; sólo se verifica la
temporización (que es lo relevante para Tomasulo).

## Guías interactivas

`coloquio.html`, `pipeline.html`, `predictores.html`, `cache.html` y `coherencia.html` son páginas HTML **autocontenidas** (CSS y JS
inline, sin dependencias externas): se pueden abrir directamente sin compilar.
Comparten con el resto del sitio el tema claro/oscuro (`localStorage['tw-theme']`).

La sección de **caché y memoria virtual** (`cache.html#s-virtual`) incluye tres
widgets:

- **Las tres variantes en el tiempo**: línea de tiempo TLB / caché / memoria para
  direccionamiento físico, parcial (solapamiento) y total, en acierto y en fallo.
- **Virtual total**: dos procesos, con y sin PID en el tag, para provocar
  homónimos (falsos aciertos) y sinónimos (copias incoherentes).
- **Virtual parcial**: configurás página, caché, bloque y asociatividad y ves si
  el índice cabe en el desplazamiento (caché ≤ página × asociatividad), con un
  recorrido paso a paso de accesos.

## Estructura

```
.claude/skills/guia-arquitectura/  # skill: template, estándar y validador de guías
web/                 # sitio (TypeScript + Vite, multi-page)
  index.html         # inicio: índice de todas las páginas (standalone)
  tomasulo.html      # simulador de Tomasulo (usa src/main.ts)
  predictores.html   # guía interactiva de predictores de salto (standalone)
  cache.html         # guía interactiva de jerarquía de memoria y caché (standalone)
  coherencia.html    # guía interactiva de coherencia de caché: snoopy y directorios (standalone)
  pipeline.html      # guía interactiva del procesador: pipeline, planificación, excepciones, Tomasulo, VLIW (standalone)
  coloquio.html      # modalidad del coloquio y temas frecuentes, con enlaces a cada guía (standalone)
  src/engine/        # port del motor (mainLogic.ts, parseFile.ts)
  src/               # UI del simulador: main.ts, diagram.ts, examples.ts, style.css
  public/asm/        # corpus de ejemplos .s (assets estáticos)
  test/              # test de fidelidad vs golden de Java
reference-java/      # app original Java Swing (referencia, no se ejecuta en web)
.github/workflows/   # despliegue a GitHub Pages
```

Cada página HTML de nivel superior debe registrarse en `web/vite.config.ts`
(`rollupOptions.input`) para que el build la incluya, y enlazarse desde el
inicio (`index.html`).

## Agregar temas

Las guías siguen un estándar común (header, índice lateral, secciones numeradas,
componentes, quiz y tema claro/oscuro) definido en la skill de Claude Code del repo,
[`.claude/skills/guia-arquitectura/`](.claude/skills/guia-arquitectura/):

- `assets/guide-template.html`: template de una guía nueva (fuente de verdad del estándar).
- `references/standard.md`: reglas, catálogo de componentes, cómo migrar una página.
- `scripts/check_guide.py`: valida todas las páginas (`check`) y re-sincroniza los
  bloques comunes desde el template (`sync`).

```bash
python3 .claude/skills/guia-arquitectura/scripts/check_guide.py check
```

## Desarrollo

```bash
cd web
npm install
npm run dev       # servidor de desarrollo
npm test          # test de fidelidad
npm run build     # build de producción (VITE_BASE=/computer-architecture-lab/ en CI)
```

## Despliegue

Cada push a `main` dispara el workflow de GitHub Actions
(`.github/workflows/deploy.yml`), que corre los tests, construye con la base
`/computer-architecture-lab/` y publica en GitHub Pages. Habilitá Pages con
origen **GitHub Actions** en la configuración del repositorio.

El repo se llamaba `tomasulo-web`; la URL vieja de Pages
(`agustin130a.github.io/tomasulo-web/`) ya no se sirve.

## Créditos

El simulador de Tomasulo está basado en Tomasulo-Visual (proyecto de curso
UMass ENG668). Este repositorio es material de estudio con fines educativos.
