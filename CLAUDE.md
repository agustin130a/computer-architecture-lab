# Tomasulo Web

Puerto web (TypeScript + Canvas) del algoritmo de Tomasulo, con dos guías
interactivas complementarias sobre arquitectura de computadoras. Ver
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

El sitio tiene tres páginas HTML servidas como multi-page app de Vite:

- `web/index.html`: el simulador de Tomasulo (usa `src/main.ts`, `diagram.ts`,
  `examples.ts` — requiere el bundle de Vite).
- `web/predictores.html` y `web/cache.html`: guías interactivas
  **autocontenidas** — CSS y JS inline en el propio archivo, sin imports de
  `src/`, sin dependencias externas (ni siquiera fuentes de Google Fonts).

Cada HTML de nivel superior tiene que estar listado en
`rollupOptions.input` de `web/vite.config.ts` — si no está ahí, Vite no lo
copia a `dist/` y la página no se despliega (falla silenciosa: el archivo
existe en el repo pero nunca llega a GitHub Pages).

Para agregar una guía nueva del mismo estilo (`.html` autocontenido):
1. Registrarla en `vite.config.ts` (`rollupOptions.input`).
2. Enlazarla desde `index.html` con un segundo bloque `.page-nav`
   (mismo patrón que el de "Predicción de saltos").
3. Darle su propio `<a class="backlink" href="index.html">` de vuelta al
   simulador — no hace falta que las guías se enlacen entre sí.
4. Seguir el contrato de tema de la siguiente sección.

## Contrato de tema claro/oscuro

Las tres páginas comparten el mismo mecanismo, cada una con su propia copia
del CSS (no hay un stylesheet compartido entre `index.html` y las guías
autocontenidas):

- Atributo `data-theme` (`"light"` / `"dark"`) en `<html>`, persistido en
  `localStorage['tw-theme']`.
- Script inline en `<head>` que aplica el tema guardado (o el de
  `prefers-color-scheme`) *antes* del primer render, para evitar el
  parpadeo de tema equivocado.
- Botón `#theme-toggle` con el mismo marcado e igual script al final del
  `<body>` en las tres páginas.
- Tokens base compartidos: mismos valores hex en las tres páginas (claro en
  `:root`, oscuro en `html[data-theme='dark']`), aunque cada archivo los
  nombra a su manera — `src/style.css` usa `--ink`/`--panel`/`--border`,
  `predictores.html` y `cache.html` usan `--text`/`--panel` o
  `--bg-panel`/`--line`. Al portar una página nueva, copiar los *valores*
  de `predictores.html` (es el ejemplo más reciente), no asumir que los
  nombres de variable coinciden entre archivos.
- Cada guía puede sumar tokens semánticos propios por encima de esa base
  (p. ej. `predictores.html` usa `--taken`/`--nottaken` para tomado/no
  tomado; `cache.html` usa `--amber`/`--teal`/`--violet` para
  tag/índice/desplazamiento). `--accent` queda reservado para elementos de
  "chrome" compartido (links, foco, indicador activo de nav/tabs, botón
  primario); los tokens semánticos de cada página son para su contenido
  propio, no para reemplazar `--accent`.

Al portar una página HTML externa a este proyecto: los colores "quemados"
(hex u `rgba()` literales, sobre todo los ajustados para un solo tema
oscuro) hay que tokenizarlos con esta convención antes de integrarla —
si no, el toggle de tema no tiene efecto sobre esos elementos.

## Comandos (todo corre desde `web/`)

```bash
npm install
npm run dev       # servidor de desarrollo
npm test          # fidelidad del motor vs. golden de Java (rápido, correrlo seguido)
npm run build     # tsc + vite build → web/dist/ (usa VITE_BASE=/tomasulo-web/ en CI)
```

## Despliegue

Push a `main` dispara `.github/workflows/deploy.yml`: corre `npm test`,
build con `VITE_BASE=/tomasulo-web/`, y publica `web/dist/` en GitHub
Pages (origen debe estar en **GitHub Actions**). URL:
`https://agustin130a.github.io/tomasulo-web/`.

## Estilo del código y del contenido

- El proyecto (código y prosa de las guías) está en voseo — mantenerlo al
  editar contenido existente o agregar secciones nuevas a las guías, para
  no mezclar registros dentro de la misma página.
- Sin build step ni TypeScript en `predictores.html`/`cache.html` — es
  intencional (son documentos autocontenidos, fáciles de abrir sin
  compilar). No migrarlas a `src/` sin que se pida explícitamente.
