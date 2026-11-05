# Sistema de diseño de Grupo Olivo · Colofón

> Fuente de verdad: `design-system/project/` (tokens.json, tokens.css, components/). Publicado también como Design System en Claude.

La página blanca de un libro bien compuesto. Grupo Olivo es una editorial independiente que crea libros pensados en su lector; el sitio se comporta como un libro: márgenes generosos, tipografía de imprenta, y las portadas como única fuente de color fuerte. La dirección se llama **Colofón**.

## Principios

1. **Las portadas mandan.** Son el mejor activo de la marca. Todo lo demás (fondo, texto, filetes) se mantiene en blanco, negro y un verde, para que cada portada brille.
2. **Oficio de imprenta.** Detalles de libro impreso: colofón con ISBN, eyebrows en mono, comillas latinas «», filetes finos. Nada de tarjetas con sombra por todas partes.
3. **Movimiento con intención.** Una coreografía al cargar, portadas que se sienten objetos y un catálogo que se reordena con suavidad. Nunca un fade-up genérico en todo.
4. **Rápido en un teléfono venezolano.** Mobile-first, imágenes livianas, animaciones solo con `transform` y `opacity`.

## Voz y contenido

- Español de Venezuela, **tuteo** cercano y profesional: «Explora el catálogo», «Sube la captura del comprobante».
- Botones con verbo y objeto: «Agregar al carrito», «Ir a pagar», «Publica con nosotros». Nunca «Enviar» o «OK» solos.
- Mayúscula solo al inicio de la frase y en nombres propios: «Del catálogo», no «Del Catálogo». Los eyebrows se escriben en minúscula y el CSS los pasa a mayúsculas.
- Citas con comillas latinas: «Porque los cuentos no son sólo cuentos.»
- Usa el texto real de la editorial. Lemas existentes: «Libros pensados en su lector», «Vive y crea tu historia», «llevar más libros de Venezuela al mundo».
- Precios: `US$ 15,00` y `Bs 1.234,56` (coma decimal). Si falta un dato, muestra `[PRECIO]`; nunca inventes cifras, títulos ni reseñas.
- Sin emojis en la interfaz.

## Logo

- Usa siempre los archivos originales del grupo **Logos**; nunca redibujes, deformes, recolorees ni cambies la tipografía del logo (manual de uso).
- `grupo-olivo-color.png` sobre `surface` en tema claro. `grupo-olivo-negativo.png` sobre `brand-black`, `brand-green`, fotos y en tema oscuro (clases `go-logo-pos` / `go-logo-neg`).
- Alto: 26px en la navegación, 22px en el pie. El PNG mide 547 × 116 px: no lo uses a más de 270px de ancho hasta tener el SVG.
- Deja alrededor un margen libre igual a la altura de la «O».
- Los dos círculos de las «O» (anillo `brand-green` con centro `brand-leaf`) se pueden usar como **motivo** suelto (EmptyState, loader), nunca junto a letras que imiten el logo.
- Sellos: `sello-tucoach-go`, `sello-alita` y `sello-reto-escritor` (negro) para fondos claros; `sello-reto-escritor-negativo` para oscuros.

## Color

- Fondo de página `surface` (blanco, como pidió la clienta). Superficies hundidas en `surface-sunk`: el pozo de cada portada, la sección destacada, los skeletons.
- Texto en `ink`; secundario en `ink-muted`. Los dos pasan 6.5:1 o más en ambos temas.
- `accent` es el único color de interfaz: eyebrows, sello en BookCard, enlaces, método de pago elegido, foco. Úsalo con moderación; si todo es verde, nada lo es.
- Los tres colores oficiales (`brand-black`, `brand-green`, `brand-leaf`) son fijos en los dos temas y se usan para identidad: PromoBar, motivo de las «O», bloques de marca.
- **`brand-leaf` nunca como texto normal sobre blanco** (2.6:1). Sí sobre `brand-black` (6.5:1), en puntos y en texto de 24px o más.
- Estados: `warning` para «Pendiente de verificación», `success` para «Pago aprobado», `danger` para errores y rechazos. Siempre con palabra o icono además del color.
- Botón primario: `ink` con texto `on-ink`; en hover, `accent` con `on-accent`.

## Tipografía

| Rol | Familia | Estilos |
|---|---|---|
| Titulares | Libre Caslon Display | `display-xl` (hero), `display-l` (sección), `display-m` (página de libro) |
| Lectura | Libre Caslon Text | `quote` (itálica), `book-title`, `lede` |
| Interfaz | Hanken Grotesk | `body`, `body-s`, `nav`, `button`, `price` |
| Metadatos | IBM Plex Mono | `label` (eyebrow, sello, ISBN), `code` (referencias de pago) |

- Un `display-xl` por página. En código, los tamaños grandes son fluidos: `display-xl` = `clamp(48px, 7.4vw, 104px)`, `display-l` = `clamp(36px, 4.6vw, 60px)`, `quote` = `clamp(26px, 3vw, 38px)`.
- La palabra clave de un titular puede ir en Libre Caslon Text itálica `accent` al 86% del tamaño: «Libros pensados en su *lector.*» Una por titular.
- Texto serif corrido a `measure` (52ch) como máximo; `text-wrap: balance` en titulares.
- Precios y cantidades con `font-variant-numeric: tabular-nums`.
- Todas las fuentes son libres (OFL) y están en `fonts/`. En Next.js, cárgalas con `next/font/local`.

## Espacio y retícula

- Contenedor de `container` (1280px) con gutter de `space-4` en móvil y `space-5` en escritorio.
- Secciones separadas por `space-9` (96px) en escritorio y `space-8` en móvil.
- Catálogo: `repeat(auto-fill, minmax(book-card-min, 1fr))`, filas a `space-7` y columnas a `space-6`; bajo 600px, dos columnas fijas a `space-4`.
- Navegación sticky de `header-height` (68px).
- Radios: `radius-book` en portadas (lomo 2px, canto 4px), `radius-s` en inputs, `radius-m` en paneles, `radius-pill` en botones y tabs. Las tarjetas de libro no llevan borde ni radio: la portada es el objeto.

## Imágenes

- Portadas planas en proporción 2:3, en WebP/AVIF a unos 600px de alto, con `loading="lazy"` y placeholder con blur. Nunca mockups 3D, fotos de un libro físico ni portadas desplegadas con lomo.
- La portada lleva `shadow-book` (de pie) o `shadow-book-card` (en el catálogo). Son las únicas sombras con peso del sistema.
- Fotos de autores recortadas en círculo (AuthorCard). No uses el banco de imágenes de stock.

## Movimiento

Stack: Motion para la interfaz, GSAP + ScrollTrigger + Flip para las secuencias y Lenis para el scroll suave. GSAP y Lenis se cargan de forma dinámica solo en las páginas que los usan (límite de 3 MiB del Worker de Cloudflare).

| Momento | Duración | Curva |
|---|---|---|
| Hover de color, foco | `duration-fast` | `ease-out` |
| Subrayado de navegación, flecha del botón | `duration-base` | `ease-out` |
| Reordenar catálogo (Flip), abrir Drawer | `duration-slow` | `ease-in-out` / `ease-out` |
| Portada que vuela al carrito | 900ms | `ease-in` |
| Titular por líneas, abanico de portadas | `duration-hero` | `ease-out` (expo.out) |

- Firma de la marca: el **abanico de portadas** del hero (cinco portadas suben escalonadas, se abren en abanico y se abren más con el scroll), la **portada que vuela al carrito** y el **reordenado con Flip** al filtrar por sello.
- La portada de un libro se convierte en el hero de su página (transición de elemento compartido).
- Inclinación 3D con brillo solo con cursor fino.
- Anima solo `transform` y `opacity`. El contenido es visible sin esperar al scroll: las entradas parten de un estado legible.
- Con `prefers-reduced-motion`, todo queda estático: sin Lenis, sin GSAP, y el carrito solo actualiza el contador y muestra un Toast.

## Estados e interacción

- Foco: anillo sólido `focus` de 2px con 3px de separación en todo lo interactivo.
- Bordes de controles en `control-border` (3:1 o más); filetes decorativos en `rule`.
- Objetivos táctiles de 44px o más (botones de 48px, `sm` de 36px solo con espacio alrededor).
- Errores: el borde pasa a `danger` y un texto dice qué pasó y cómo arreglarlo.

## Iconografía

No hay un set de iconos de marca (los del sitio de 2021 eran de la plantilla). Usa pocos iconos de línea, dibujados en SVG con trazo de 1.6px y `currentColor`: flecha, carrito, menú, subir archivo, check. Ningún emoji.

## Flujo de pago

Cinco métodos: Pago Móvil, transferencia, Zelle y Binance Pay (manuales) y PayPal (automático). Los manuales siguen PaymentMethodSelector → UploadComprobante → OrderStatusTimeline, con el pedido «Pendiente de verificación» hasta que la editorial lo aprueba desde el panel de administración.
