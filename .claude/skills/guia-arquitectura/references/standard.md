# Estándar de guías — v1

Fuente de verdad: `assets/guide-template.html`. Este documento explica *por qué* es
así y qué hacer en los casos que el template no muestra. Si algo acá contradice al
template, gana el template (y hay que corregir este archivo).

## Índice

1. Anatomía de la página
2. Bloques STD (lo que no se edita a mano)
3. Tokens
4. Secciones: ids, numeración, contenido
5. Componentes
6. Widgets interactivos (CSS/JS propio)
7. Registro en el sitio (vite + home)
8. Chrome del simulador de Tomasulo
9. Migrar una página existente
10. Cambiar el estándar

---

## 1. Anatomía de la página

```
<head>  title "<Tema corto> | Computer Architecture Lab", meta description,
        script de tema (tw-theme) ANTES del <style>, <style> con:
          STD:TOKENS → STD:SHELL → STD:COMPONENTS → PAGE:TOKENS → PAGE
<body>  a.skip-link
        header.site   .site-top(a.backlink "← Inicio" + #theme-toggle)
                      p.kicker "Arquitectura de Computadoras — <unidad/tema>"
                      h1, p.lede, [div.hero opcional]
        div.shell     nav.side#sidenav  (div.brand + ol > li.grp > p.grp-title + a…)
                      main#main         section.block#s-* …, section#s-quiz,
                                        footer.pagefoot (dentro de main)
        <script> STD:SCRIPT </script>
        <script> PAGE:SCRIPT </script>
```

Por qué un nav lateral y una sola página larga: los temas crecen (la guía de caché
ya tiene 14 secciones) y con pestañas no se puede buscar con Ctrl+F, ni enlazar una
sección desde el home, ni leer de corrido. En celular el nav queda arriba del contenido.

## 2. Bloques STD

Los bloques entre `/* ==== STD:X v1 ==== */` y `/* ==== /STD:X ==== */` son copias
exactas del template. `check_guide.py check` los compara y `check_guide.py sync`
los reescribe. Así, mejorar el estándar = editar el template + `sync` en cada página.

- **No editar un bloque STD dentro de una página.** Si una página necesita algo
  distinto, va en `PAGE` (con un selector más específico, bajo la clase de su sección).
- Si hace falta algo que *todas* las páginas deberían tener, va al template (ver §10).

## 3. Tokens

Base (en STD:TOKENS, claro en `:root`, oscuro en `html[data-theme='dark']`):

| Token | Uso |
| --- | --- |
| `--bg`, `--bg-grad` | fondo de la página |
| `--bg-panel`, `--bg-panel-2` | superficies (tarjetas, nav) y superficie secundaria (th, chips, hover) |
| `--line`, `--line-soft` | bordes |
| `--text`, `--muted` | texto principal y secundario |
| `--accent`, `--accent-ink`, `--focus` | *chrome*: links, foco, activo en nav, botón primario |
| `--highlight` | numeración de secciones, `<strong>` dentro de tarjetas |
| `--ok`/`--ok-soft`, `--err`/`--err-soft`, `--warn`/`--warn-soft` | estados: acierto/fallo/advertencia |

Semánticos de la página (en `PAGE:TOKENS`, siempre con par claro + oscuro): nombres por
significado (`--taken`, `--tag`, `--page`…), no por color. `cache.html` usa
`--amber/--teal/--violet/--rust` por herencia; está permitido pero no es el modelo.

Regla dura: **ningún color literal fuera de los bloques de tokens**, ni en CSS ni
en `style=""` ni generado desde JS. Un hex suelto se ve bien en un tema y mal en el
otro, y el toggle no lo cambia. El checker lo avisa en CSS y `style=""` (no analiza JS).

Excepción aceptada: paletas categóricas generadas desde JS cuyo texto usa un token de
tinta fijo, que se leen igual en los dos temas. Ejemplo: `PALETTE` en `cache.html`
(bloques de memoria de colores con `--blk-ink`). Una paleta nueva de este tipo hay que
revisarla en claro y oscuro.

## 4. Secciones

- `id="s-<slug>"`, slug corto en minúsculas y sin tildes (`s-nway`, `s-virtual`).
  Sub-anclas dentro de una sección: `h3 id="s-<slug>-<sub>"`.
- `<h2><span class="num">N</span> Título</h2>`. `N` es:
  - el número del programa de la materia si existe (`5.3`, `5.12–5.14`);
  - si no, un ordinal simple (`1`, `2`, …);
  - `↳` para un simulador que cuelga de la sección anterior;
  - `✓` para el quiz.
- `p.sub` inmediatamente debajo: una oración con la pregunta que responde la sección.
- Orden interno sugerido: teoría (tarjetas / panel) → regla o fórmula → widget →
  nota "fijate que…". Una sección sin widget está bien; un widget sin explicación no.
- Cada sección de nivel superior va en el nav, y el nav se agrupa en `li.grp`
  con `p.grp-title` (3–6 grupos). Las sub-anclas pueden ir en el nav con `↳ `.
- El quiz (`#s-quiz`) cierra la guía: 5–10 preguntas que crucen toda la página,
  cada una con `exp` que explique *por qué*, no solo la respuesta.

## 5. Componentes (STD:COMPONENTS)

| Clase | Para qué |
| --- | --- |
| `details.card > summary + div.body` | teoría desplegable; `open` en la primera de cada sección |
| `div.panel` | caja fija para texto + diagrama que no conviene esconder |
| `div.table-scroll > table.cmp` | tablas comparativas (`td.hi` resalta una celda) |
| `div.formula` | regla/fórmula clave, monoespaciada |
| `div.note` / `div.note.info` | advertencia / aclaración al margen |
| `div.pill-row > span.pill` | etiquetas cortas (`<b>` para el valor) |
| `div.sim` | contenedor de todo widget: `.cfg` (grilla de `label`+`select`), `.actions` (botones), `.msg[.ok/.err]` (estado, con `aria-live`) |
| `button.btn`, `button.btn.ghost`, `.ghost.sel` | primario, secundario, seleccionado |
| `div.stat-row > div.stat[.ok/.err] > .n + .l` | contadores (aciertos, fallos…) |
| `stdQuiz(items)` + `#quizWrap`/`#quizScore` | quiz; `items = [{q, opts, correct, exp}]` |

Antes de inventar una clase nueva, revisar si una de estas alcanza. Si un patrón
nuevo aparece en dos páginas, es candidato a componente (§10).

## 6. Widgets interactivos

- CSS en `PAGE`, todo bajo la clase de la sección: `<section class="block vm" …>` →
  `.vm .vm-bar{…}`. Así no choca con nada (en `cache.html` ya pasó con `.blk`, `.card`, `.row`).
- Ids con prefijo de la sección (`vm-step`, `vm-msg`).
- JS en `PAGE:SCRIPT`, un IIFE por widget, `addEventListener` (no `onclick` inline,
  no globales). Página vieja con `onclick`: se tolera (aviso) y no se reescribe salvo
  que se pida.
- Respetar `prefers-reduced-motion` en animaciones.
- El widget tiene que funcionar a 390 px de ancho sin scroll horizontal de la página
  (si una tabla o diagrama es ancho, envolverlo en `.table-scroll` o `overflow-x:auto`).

## 7. Registro en el sitio

Una página nueva no existe hasta que:

1. está en `rollupOptions.input` de `web/vite.config.ts` (si no, Vite no la copia a
   `dist/` y no se despliega — falla silenciosa);
2. tiene tarjeta en `web/index.html`: `article.card.<clave>#p-<clave>` con `span.tag`,
   `h2 > a`, `p.desc`, `h3 Contenido`, `ul.toc` con **un link por cada sección de
   nivel superior** (`<a href="pagina.html#s-x"><span class="n">N</span>Título</a>`) y
   `a.open`. Color propio: par `--c-<clave>`/`--c-<clave>-soft` en ambos temas y la
   regla `.card.<clave>{ --c:…; --c-soft:… }` + `.dot.<clave>` si entra en el recorrido;
3. si es parte del recorrido del procesador, suma un `.stop` en `nav.path`;
4. el README (tabla de páginas + árbol de `web/`) y el `CLAUDE.md` del repo la mencionan.

Una sección nueva dentro de una guía existente: nav lateral + link en la tarjeta del
home (`span.new` "nuevo" opcional, sacarlo en la siguiente modificación).

## 8. Chrome del simulador de Tomasulo

`tomasulo.html` es una app de Vite (`src/main.ts`, `src/style.css`): el estándar le
aplica **solo al chrome** — mismo header (`.site-top` con backlink y toggle,
`kicker`, `h1`, `lede`), `<title>` con el sufijo y footer con link al home. El cuerpo
(controles, canvas, tablas) queda como está. Sus estilos viven en `src/style.css` con
nombres propios (`--ink`, `--border`, `--panel`); no se sincroniza con bloques STD.
**No tocar `src/engine/`** — el test de fidelidad tiene que seguir 7/7.

## 9. Migrar una página existente

Objetivo: que el checker quede sin errores sin perder contenido ni romper widgets.

1. Leer la página entera y hacer un inventario: secciones, widgets, ids que usa el JS,
   clases que genera el JS (`className`, `innerHTML` con `class="…"`), tokens propios.
2. Tokens: pasar los base a los nombres estándar (p. ej. `--panel` → `--bg-panel`,
   `--panel-2` → `--bg-panel-2`); los semánticos van a `PAGE:TOKENS`. Borrar los que
   el layout nuevo ya no usa.
3. Reemplazar head/header/nav/footer y los bloques de CSS/JS base por los del template.
4. Contenido: cada vista/pestaña/bloque pasa a `section.block#s-*` con `h2 > .num` y
   `p.sub`. Si el texto habla de la navegación vieja ("andá a la pestaña 1"), reescribirlo.
5. Componentes: mapear cajas, botones, notas y stats a las clases de §5
   (ej. `div.card` → `div.panel`, `button.action` → `button.btn.ghost`,
   `.note.blue` → `.note.info`). Lo que sea propio del widget queda en `PAGE`.
6. Anclas viejas: si otras páginas o el home enlazaban ids que desaparecen
   (p. ej. `#t2`), actualizar esos links; si puede haber links externos, agregar un
   pequeño redirect de hash en `PAGE:SCRIPT` (como en `predictores.html`).
7. `check_guide.py check`, `npm test`, `npm run build` y prueba en navegador (ver SKILL.md).

## 10. Cambiar el estándar

1. Editar `assets/guide-template.html` (y subir la versión del marcador, `v1` → `v2`,
   si el cambio no es retrocompatible).
2. Actualizar este documento.
3. `check_guide.py sync web/<cada guía>.html` y después `check_guide.py check`.
4. Probar todas las páginas en ambos temas: un cambio en STD las toca a todas.
