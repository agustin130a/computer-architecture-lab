---
name: guia-arquitectura
description: Agrega temas nuevos al sitio Computer Architecture Lab (guías interactivas de arquitectura de computadoras en web/*.html) y aplica el estándar de páginas (header común, nav lateral, secciones numeradas, componentes, quiz, tema claro/oscuro, registro en vite y en el home). Usar siempre que en este repo se pida sumar una guía o un tema nuevo (pipeline, TLB, coherencia, memoria virtual, etc.), agregar una sección o simulador a una guía existente, portar un HTML externo o unos apuntes como página del sitio, o "aplicar el estándar"/unificar/migrar el formato de predictores.html, cache.html, tomasulo.html o cualquier página, aunque el pedido no diga "estándar" ni "template".
---

# Guías del Computer Architecture Lab

El sitio (`web/`) tiene un home (`index.html`), una app (`tomasulo.html`) y guías
autocontenidas (`predictores.html`, `cache.html`, …). Esta skill mantiene todas las
guías con la misma forma, para que el sitio se lea como un solo material y no como
páginas sueltas con índices y estilos distintos.

Recursos:
- `assets/guide-template.html`: **la fuente de verdad** del estándar. Esqueleto
  completo con bloques `STD:*` (no se editan a mano) y huecos `{{…}}` para el contenido.
- `references/standard.md`: el porqué de cada regla, catálogo de componentes, cómo
  registrar una página, cómo migrar una existente y cómo cambiar el estándar.
  Leerlo antes de la primera modificación de la sesión.
- `scripts/check_guide.py`: validador (`check`) y sincronizador de bloques (`sync`).

Todos los comandos se corren desde la raíz del repo y con la ruta completa del script
(no guardar la ruta en una variable de shell: no persiste entre llamadas):

```bash
python3 .claude/skills/guia-arquitectura/scripts/check_guide.py check [web/x.html ...]
python3 .claude/skills/guia-arquitectura/scripts/check_guide.py sync web/x.html [...]
```

## Primero: qué tipo de pedido es

| Pedido | Flujo |
| --- | --- |
| "Agregá una guía de X" / "un tema nuevo" que no encaja en ninguna guía | A. Guía nueva |
| "Sumá X a la guía de caché" / una sección o simulador más | B. Sección nueva |
| "Aplicá el estándar a …" / "unificá las páginas" / "migrá predictores" | C. Aplicar estándar |
| Se cambió el template y hay que propagarlo | `sync` sobre cada guía y después `check` |

Si no está claro si un tema es una guía nueva o una sección de una existente,
preguntar: cambia el archivo, el nav, la tarjeta del home y el vite config. Regla
práctica: si comparte el hilo conductor de una guía (p. ej. TLB dentro de memoria),
es sección; si tiene su propio recorrido de 4 o más secciones, es guía.

Si el material fuente viene del usuario (HTML, apuntes, PDF), leerlo entero antes de
escribir. No inventar contenido técnico que no esté en la fuente; si falta algo para
que la sección se entienda, marcarlo y preguntar, o sumarlo aclarando en el resumen
que es un agregado propio.

## A. Guía nueva

1. Nombre de archivo corto en español, sin tildes (`pipeline.html`, `coherencia.html`).
2. Copiar `assets/guide-template.html` a `web/<nombre>.html` y completar los `{{…}}`:
   title, description, kicker, h1, lede, brand del nav, grupos, secciones, footer.
   Borrar los ejemplos que no se usen; no dejar ningún `{{` (el checker lo marca).
3. Escribir las secciones según `references/standard.md` §4–5: `s-<slug>`, `h2 > .num`,
   `p.sub`, teoría en `details.card`/`.panel`, reglas en `.formula`, notas.
4. Widgets: CSS en `PAGE` bajo la clase de la sección, ids con prefijo, JS en un IIFE
   por widget en `PAGE:SCRIPT` (§6). Colores solo vía tokens; los propios del tema van
   en `PAGE:TOKENS` con par claro/oscuro.
5. Quiz final con `stdQuiz([...])`, 5–10 preguntas con explicación.
6. Registrarla (§7): `web/vite.config.ts`, tarjeta en `web/index.html` con un link por
   sección, README (tabla de páginas + árbol) y `CLAUDE.md` del repo (lista de páginas).
7. Verificar (ver abajo).

## B. Sección nueva en una guía existente

1. Ubicarla en el orden lógico de la guía y elegir su número (§4).
2. Escribirla con los componentes estándar; si trae widget, aplicar scope + prefijo + IIFE.
   Si viene de un HTML externo: sacar fuentes externas, tokenizar los colores, pasar los
   estilos globales (`body`, `h2`, `button`, `table`…) a selectores bajo su clase y
   renombrar ids genéricos. Son la causa típica de romper la página anfitriona.
3. Sumarla al nav lateral (en el grupo que corresponda) y a la tarjeta de esa guía en
   el home.
4. Verificar.

## C. Aplicar el estándar a una página existente

1. `check` sobre la página para ver qué falta.
2. Si le faltan los bloques STD o el layout, es una **migración**: seguir
   `references/standard.md` §9 al pie de la letra. Lo importante es no perder nada:
   inventariar widgets, ids y clases que usa el JS antes de tocar el marcado, y al
   final comprobar que cada widget sigue respondiendo.
3. Si ya tiene los bloques pero difieren del template: `sync` sobre la página.
4. `tomasulo.html` es una app: solo se estandariza el chrome (§8); su CSS está en
   `web/src/style.css`. No tocar `web/src/engine/`.
5. Los avisos (tuteo, `onclick` inline, colores literales) se corrigen si son baratos
   y seguros; los `onclick` de páginas viejas se dejan salvo que se pida reescribir el JS.

## Verificación (siempre, antes de dar por terminado)

```bash
python3 .claude/skills/guia-arquitectura/scripts/check_guide.py check   # 0 errores
cd web && npm test                  # motor de Tomasulo: 7/7
npm run build && ls dist            # la página tiene que estar en dist/
```

Además, probar en un navegador real: los choques de CSS/JS y los colores que no
siguen el tema no los detecta ningún check estático. Si hay Playwright disponible
(`find ~/.npm/_npx -maxdepth 3 -name playwright -type d` y un `chrome-headless-shell`
en `~/.cache/ms-playwright`), levantar `npx vite preview` y, con un script headless:
abrir cada página tocada, hacer click en cada control de los widgets nuevos, capturar
errores de consola (`pageerror`), sacar capturas en claro y oscuro y comprobar que a
390 px de ancho `document.documentElement.scrollWidth <= innerWidth`. Para probar un
link con hash, abrir una pestaña nueva: navegar de `x.html` a `x.html#y` en la misma
pestaña no recarga la página y no vuelve a correr sus scripts. Si no hay navegador
disponible, decirlo en el resumen en lugar de afirmar que se ve bien.

## Estilo del contenido

- La prosa de las guías va en voseo ("probá", "fijate", "podés"), igual que el resto
  del sitio. El checker avisa formas de tuteo frecuentes.
- Explicar el mecanismo antes que la definición: qué problema resuelve, cómo funciona,
  qué cuesta. El widget es para *ver* eso, no un adorno.
- Nada de dependencias externas (ni CDNs ni Google Fonts): las guías se abren sin
  servidor ni conexión.

## Commits

Seguir la convención del repo (`feat(web): …`, `docs: …`, descripción en español,
imperativo, minúscula, sin punto). Una guía o migración por commit, separando los
cambios de docs. No commitear ni pushear a `main` sin que el usuario lo pida: un push
a `main` despliega el sitio.
