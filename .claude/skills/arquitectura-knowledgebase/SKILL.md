---
name: arquitectura-knowledgebase
description: Base de conocimiento con el texto completo de los apuntes de Arquitectura de Computadoras (UNC, FCEFyN), indexado por unidad, sección y página. Usar siempre que se consulte sobre un tema de la materia (rendimiento, CPI, Amdahl, consumo, pipeline/segmentación MIPS-DLX, riesgos, predicción de saltos, ILP, Tomasulo, especulación, buffer de reordenamiento, VLIW, superescalares, multithreading, jerarquía de memoria, caché, memoria virtual, TLB, coherencia snoopy/MSI/MESI, directorios, consistencia, sincronización, SIMD, vectoriales, GPU/CUDA), para preparar el coloquio o para verificar contra los apuntes el contenido de una guía del sitio, aunque la pregunta no mencione los apuntes.
---

# Knowledge base: apuntes de Arquitectura de Computadoras

Texto completo de los *Apuntes Teóricos de Arquitectura de Computadoras* (UNC, FCEFyN, IComp),
de Augusto Gabriel Cabrera, versión del 6 de marzo de 2024. **Son apuntes no oficiales de la
cátedra**: sirven de referencia, pero no reemplazan las diapositivas ni la bibliografía oficial.

## Archivos

- `index.md`: índice completo (unidad, sección y subsección) con `archivo:línea` y página del PDF.
  **Leerlo primero** para ubicar el tema.
- `apuntes/unidad-1.md` … `apuntes/unidad-6.md`, `apuntes/anexo-dlp.md`: el texto, con marcas
  `<!-- p. N -->` al inicio de cada página del PDF y encabezados `##`/`###`/`####` por sección.

| Archivo | Tema |
| --- | --- |
| `unidad-1.md` | Tendencias tecnológicas, costo, rendimiento y consumo |
| `unidad-2.md` | Segmentación (MIPS-DLX, riesgos, predicción, excepciones, multiciclo, R4000) |
| `unidad-3.md` | ILP (dependencias, Tomasulo, especulación) |
| `unidad-4.md` | Lanzamiento múltiple, límites del ILP, multithreading |
| `unidad-5.md` | Jerarquía de memoria (caché, memoria virtual) |
| `unidad-6.md` | Multiprocesadores: coherencia, consistencia y sincronización |
| `anexo-dlp.md` | Paralelismo a nivel de datos (SIMD, vectoriales, GPU, CUDA) |

## Cómo responder una consulta

1. Buscar en `index.md` la sección del tema. Si el término no aparece como título, buscarlo en
   el texto: `grep -n -i "<término>" .claude/skills/arquitectura-knowledgebase/apuntes/*.md`.
2. Leer la sección con Read (`offset` = línea del índice, `limit` alrededor de 80–150 líneas)
   en lugar de cargar la unidad entera.
3. Responder basándose en el texto y citar la fuente como «apuntes, sección X.Y (p. N)». El
   número de sección está en la línea original debajo del encabezado y la página en la marca
   `<!-- p. N -->` anterior.
4. Si algo no está en los apuntes, decirlo y separar con claridad lo que viene de otro lado.

## Limitaciones de la conversión

- **Figuras y diagramas no están**: solo queda su epígrafe («Figura N: …»). Si la respuesta
  depende de una figura, avisar y remitir a la página del PDF.
- **Fórmulas y tablas** se extrajeron con `pdftotext -layout`: conservan la disposición en
  columnas pero no son LaTeX. Fracciones y subíndices pueden aparecer en dos o tres líneas
  (numerador arriba y denominador abajo); leer el bloque completo antes de interpretarlo.
- **Los apuntes tienen erratas.** Ejemplo conocido: en la sección 6.24 (sobrecarga del
  directorio) los números no cierran con «4 nodos», «25 nodos» y «línea de 4 bytes»; sí cierran
  con línea de 64 B y 64, 256 y 1024 nodos. Si un número no cierra, señalarlo en lugar de
  repetirlo.

## Regenerar

Si cambia el PDF (ruta por defecto: `~/obsidian/poveda-cel/Apuntes de Arquitectura de Computadoras.pdf`):

```bash
SP=<directorio temporal>
pdftotext -layout "<pdf>" $SP/all.txt
python3 -c "import pymupdf,json; json.dump(pymupdf.open('<pdf>').get_toc(), open('$SP/toc.json','w'))"
python3 .claude/skills/arquitectura-knowledgebase/scripts/build_kb.py $SP .claude/skills/arquitectura-knowledgebase
```

`pymupdf` solo se usa para leer el índice (bookmarks) del PDF; se puede instalar en un venv
temporal. El script tiene que terminar con `faltantes: 0` (todos los títulos del índice
ubicados en su página).

## Uso del contenido

El texto de los apuntes es de su autor y se versiona en este repo solo como referencia de estudio.
No copiar fragmentos largos a las páginas del sitio: resumir con palabras propias y citar la sección.
