# Computer Architecture Lab

Sitio de material interactivo de arquitectura de computadoras (repo
`agustin130a/computer-architecture-lab`, antes `tomasulo-web`): un home que
indexa todo, el puerto web (TypeScript + Canvas) del algoritmo de Tomasulo y
dos guías interactivas. Ver
`README.md` para la descripción general del proyecto; esto es orientación
para trabajar en el repo.

## Invariante que no hay que romper

El motor en `web/src/engine/` (`mainLogic.ts`, `parseFile.ts`) es un port
estructural de `reference-java/`. `npm test` (en `web/`) corre
`test/fidelity.test.ts`, que compara la temporización (ciclos de Issue/Exe/
Write Back) contra la salida del motor Java de referencia para los 7
programas de ejemplo — no los valores numéricos de registros/memoria
(esos no son reproducibles porque el Java inicializa memoria con valores
aleatorios). Cualquier cambio en el motor debe seguir pasando 7/7. Antes
de tocar `engine/`, correr el `HeadlessTest` de `reference-java/` si hace
falta regenerar el golden de referencia.

## Páginas del sitio y cómo agregar una nueva

El sitio tiene cinco páginas HTML servidas como multi-page app de Vite:

- `web/index.html`: el home/índice del sitio (autocontenido, igual que las
  guías). Una tarjeta por página con enlaces directos a sus secciones.
- `web/tomasulo.html`: el simulador de Tomasulo (usa `src/main.ts`, `diagram.ts`,
  `examples.ts` — requiere el bundle de Vite).
- `web/predictores.html`, `web/cache.html` y `web/coherencia.html`: guías interactivas
  **autocontenidas** — CSS y JS inline en el propio archivo, sin imports de
  `src/`, sin dependencias externas (ni siquiera fuentes de Google Fonts).

Cada HTML de nivel superior tiene que estar listado en
`rollupOptions.input` de `web/vite.config.ts` — si no está ahí, Vite no lo
copia a `dist/` y la página no se despliega (falla silenciosa: el archivo
existe en el repo pero nunca llega a GitHub Pages).

Para agregar una guía o una sección nueva, o para llevar una página al formato
común, usar la skill del repo **`guia-arquitectura`**
(`.claude/skills/guia-arquitectura/`). Ahí están el template
(`assets/guide-template.html`, fuente de verdad del estándar: header, nav lateral,
secciones `s-*` numeradas, componentes, quiz, tokens), el porqué de cada regla
(`references/standard.md`) y el validador:

```bash
python3 .claude/skills/guia-arquitectura/scripts/check_guide.py check        # todas las páginas
python3 .claude/skills/guia-arquitectura/scripts/check_guide.py sync web/x.html  # re-copia los bloques STD:*
```

Resumen de lo que exige: registrar la página en `vite.config.ts`, darle tarjeta en
el home con un link por sección, `<a class="backlink" href="index.html">&larr; Inicio</a>`,
bloques `STD:*` idénticos al template (no se editan a mano en las páginas) y el CSS/JS
propio de cada widget en `PAGE`, scopeado bajo la clase de su sección.
`tomasulo.html` solo sigue el estándar en el chrome (header/footer); su CSS está en
`src/style.css`. `predictores.html#t0`…`#t5` (links de la versión con pestañas)
redirigen a las secciones `s-*` equivalentes.

## Contrato de tema claro/oscuro

Las cinco páginas comparten el mismo mecanismo:

- Atributo `data-theme` (`"light"` / `"dark"`) en `<html>`, persistido en
  `localStorage['tw-theme']`.
- Script inline en `<head>` que aplica el tema guardado (o el de
  `prefers-color-scheme`) *antes* del primer render, para evitar el
  parpadeo de tema equivocado.
- Botón `#theme-toggle` con el mismo marcado en las cinco páginas.
- En las guías los tokens base viven en el bloque `STD:TOKENS` (nombres canónicos
  `--bg-panel`, `--line`, `--text`, `--highlight`, `--ok`/`--err`/`--warn`…) y los
  semánticos de cada página en `PAGE:TOKENS`, siempre con par claro/oscuro.
  `src/style.css` (Tomasulo) y `index.html` (home) tienen su propia copia con los
  mismos valores hex pero otros nombres (`--ink`/`--border`, `--panel`).
- `--accent` queda reservado para el "chrome" (links, foco, activo del nav, botón
  primario).
- Nada de colores literales fuera de los tokens: el toggle no los cambia.

## Comandos (todo corre desde `web/`)

```bash
npm install
npm run dev       # servidor de desarrollo
npm test          # fidelidad del motor vs. golden de Java (rápido, correrlo seguido)
npm run build     # tsc + vite build → web/dist/ (usa VITE_BASE=/computer-architecture-lab/ en CI)
```

## Despliegue

Push a `main` dispara `.github/workflows/deploy.yml`: corre `npm test`,
build con `VITE_BASE=/computer-architecture-lab/`, y publica `web/dist/` en GitHub
Pages (origen debe estar en **GitHub Actions**). URL:
`https://agustin130a.github.io/computer-architecture-lab/`. Si el repo se
renombra de nuevo, cambiar `VITE_BASE` en `deploy.yml` (la URL vieja de
Pages deja de servirse, GitHub no la redirige).

## Estilo del código y del contenido

- El proyecto (código y prosa de las guías) está en voseo — mantenerlo al
  editar contenido existente o agregar secciones nuevas a las guías, para
  no mezclar registros dentro de la misma página.
- Sin build step ni TypeScript en `index.html` y las guías (`predictores.html`, `cache.html`, `coherencia.html`) — es
  intencional (son documentos autocontenidos, fáciles de abrir sin
  compilar). No migrarlas a `src/` sin que se pida explícitamente.
