# Fase 0: inventario de Grupo Olivo

Revisión de los 464 archivos del repositorio, de los 17 documentos .docx (convertidos a texto en `docs/textos/`) y del brief (`docs/brief.md`).

---

## 1. Lo más importante: cinco cosas que cambian el diseño

1. **No hay ningún precio de libro en todo el material.** Los únicos precios son de servicios (coaching $97, programa de 7 días $129). La tienda, el PriceTag en USD/Bs y el checkout van a usar `[PRECIO]` hasta que la clienta los dé.
2. **Hoy la clienta vende por Amazon, no en su sitio.** Cada libro del catálogo enlaza a Amazon (uno a wonderbook.store). El brief propone una tienda propia con cinco métodos de pago. Hay que decidir si conviven: comprar aquí *y* "también en Amazon".
3. **Grupo Olivo vende servicios, no solo libros.** Esto responde una pregunta pendiente del brief. Tiene seis servicios editoriales con precios y CTAs a WhatsApp/Calendly, más dos concursos (Reto Escritor y Reto Expresivo) con webs propias. El brief no incluye ninguna página de servicios; propongo agregarla a la Fase 3.
4. **El logo solo existe como PNG pequeño (547 × 116 px).** Se ve borroso en pantallas retina y en un hero grande. Existe un `.eps` vectorial, pero hay que convertirlo a SVG (no hay Illustrator/Ghostscript aquí). Los logos de los sellos también son PNG chicos.
5. **Hay contradicciones en el contenido** que la clienta tiene que resolver (sección 6).

---

## 2. Marca

| Elemento | Fuente | Estado |
| --- | --- | --- |
| Negro `#1C1C1B` | Manual de uso del logo | ✅ Oficial |
| Verde oscuro `#487434` | Manual | ✅ Oficial. Contraste sobre blanco ≈ 5.5:1, sirve para texto |
| Verde claro `#70B12C` | Manual | ✅ Oficial. Contraste sobre blanco ≈ 2.6:1, **no** sirve para texto normal |
| Tipografía del logo "Nova regular" | Manual | ⚠️ Sin archivos de fuente |
| Reglas del logo | Manual | Positivo y negativo permitidos. Prohibido distorsionar, recolorear o cambiar tipografía |
| Paleta del sitio 2021 (`#467006`, `#71BC42`, `#EBF7DA`, `#364D59`) | `css/style.css` | Histórica, no se usa |
| Fuente del sitio 2021 (DM Sans) | Bootstrap | Declarada pero nunca cargada |
| Contacto | Manual | +58 414 8680195 · editorialgrupoolivo@gmail.com · @grupolivo |
| Afiliación | Diagrama 2026 | Cámara Venezolana del Libro desde 2018 |

---

## 3. Logos

`Web Assets/WEB GO 2026/LOGOS GO/` (la versión más actual; la carpeta de 2021 tiene copias idénticas).

| Archivo | Uso propuesto | Nota |
| --- | --- | --- |
| `Grupo Olivo Logo (1)-01.png` | Logo principal a color, sobre fondos claros | 547 px, PNG con transparencia |
| `Grupo Olivo Logo (1)-02.png` | Versión monocroma oscura (círculos grises) | Para fondos claros sin color |
| `Grupo Olivo Logo (1)-03.png` | Versión en negativo (blanco) | Para fondos oscuros y fotos |
| `Logo And Design System/Grupo Olivo Logo.eps` | **Fuente para generar el SVG** | Vectorial, falta convertir |
| `logo sellos tucoachgo.png` | Sello tucoach.go | Wordmark negro |
| `logo sellos alita.png` | Sello Alita | Caligráfico negro |
| `Reto escritor logo/icono … sin fondo.png` (×4) | Sello Reto Escritor, en negro y en blanco | Usar los PNG sin fondo; los JPG son CMYK con fondo |
| `Logo hechos criollos.png` / `negativo.png` | Sello Hechos Criollos | ⚠️ La clienta pidió quitarlo (ver §6) |

**Falta:** el logo en SVG, logos de Reto Expresivo y FanSeller, y versión en blanco de tucoach.go y Alita.

---

## 4. Catálogo de libros

35 archivos en `WEB GO 2026/PORTADAS DE LIBROS/`, que corresponden a unos 30 títulos. Los textos vienen de `SINOPSIS DE LIBROS Y ENLACES AMAZON` y `AUTORES_`.

### Con portada, autor y sinopsis (listos para las páginas de referencia)

| Sello | Título | Autor/a | Portada | Amazon |
| --- | --- | --- | --- | --- |
| tucoach.go | Coaching y ecología de las emociones | Ricardo Aquino | `portada para impresion.jpg` (CMYK, 397 px) ⚠️ | — |
| tucoach.go | Con sentido | José Espósito | `portada con sentido.png` | ✅ |
| tucoach.go | 7 pasos para construir tu sueño | Ana Andrea Labrador | `portada ana labrador-1-02.png` (29 KB, baja calidad) ⚠️ | ✅ |
| tucoach.go | Líder Coach | Norberto Peña | `PORTADAePub.jpg` | ✅ |
| Alita | El príncipe de la máscara | Jemmy Lee Carvajal | `portada el principe.png` (260 px) ⚠️ | ✅ |
| Alita | Fleur | Florencia Frezza | `portada fleur new-02.jpg` (CMYK, alta resolución) | ✅ |
| Alita | 21 preguntas para conquistarte | Jemmy Lee | `21 preguntas.png` | — (sinopsis incompleta) |
| Independiente | Un caso indefendible (2.ª ed.) | José Custodio Sánchez | `Un caso indefendible 2da edición.png` | ✅ |
| Reto Escritor | Anécdotas de una viajera del tercer mundo | Lissette Van Der Biest | ✅ alta resolución | ✅ |
| Reto Escritor | Descubre lo extraordinario en ti | Mariene Piñero | ✅ | ✅ |
| Reto Escritor | Historias a Coletepelo | Irene Carrasquero | ✅ | wonderbook.store |
| Reto Escritor | Soledad, ¿una cura o locura? | Zuleima Virguez | ✅ alta resolución | ✅ |
| Reto Escritor | Escribir para sanar | 18 autoras, prólogo de Ismael Cala | ✅ alta resolución | ✅ |
| Reto Escritor | Al cruzar el alambre de púas | Esmeralda Villanueva | ✅ | — |
| Hechos Criollos | Héroes muertos y otros cuentos | Juan Carlos Díaz Quilen | 260 px ⚠️ | ✅ |
| Hechos Criollos | Reliquias olvidadas | Juan Carlos Díaz Quilen | 260 px ⚠️ | ✅ |

### Con portada pero sin sinopsis
Un caso imposible (José Custodio, colección CASOS / noir), A quién le escribes (Adriana Mara Olivares), Por si me muero sin que lo sepas (María Elena Fernández-Morán Spear), Las sombras de Vincent van Gogh (Luis Manuel Marcano), Engranaje vital (Francisco Rangel Gómez), 7 errores clínicos (Mónica Chirinos), El horror de emprender (Rafa Solbas), El poder del fee (Jennifer Fernández), el libro de Yulis Rondón (solo hay un mockup en tablet), la serie Diosa Yekuana de Adriana Mara (4 portadas cuadradas en español e inglés) y las antologías de Reto Expresivo (Haz real tu sueño 2023, Fogata de ideales 2024).

### Con sinopsis pero sin portada
Feliz donde sea (Yesmin Sánchez).

### Archivos que no son portadas planas
`libro Ricardo aquino.jpg` (foto de un libro físico), `IMG-20191008-WA0096.jpg` (mockup en tablet), `pack promo.png` (mockup 3D), `Completa Por si me muero….png` (portada desplegada con lomo y contraportada). Sirven para ambientar, no para la ficha del libro.

---

## 5. Fotos, videos y material de apoyo

| Material | Ubicación | Cantidad | Uso propuesto |
| --- | --- | --- | --- |
| Fotos de autores | `WEB GO 2023/FOTO DE AUTORES/` (por sello) | 14 | AuthorCard, página de autor |
| Fotos del equipo | `WEB GO 2023/EQUIPO OPERATIVO GO/` + `2021/Fotos equipo…` | ~16 | Página "Sobre nosotros" |
| Fotos de las fundadoras | `2021/Fotos fundadoras de grupo olivo/` | 3 + firma digital | Sección "Quiénes somos" |
| Videos de testimonios | `WEB GO 2023/VIDEOS TESTIMINIOS AUTORES/` | 8 (6 únicos: 2 son duplicados de Ana Labrador), 47 s a 3 min, ~130 MB | Testimonios en video. Hay que comprimirlos y servirlos desde R2 |
| Video de intro | `2021/Intro Grupolivo.mp4` | 1 (21 s, 720p) | Posible fondo del hero o del loader |
| Catálogo 2023 | `WEB GO 2023/Catalogo 2023/` | ~35 piezas (~96 MB) | Artes promocionales, referencia |
| Banco de imágenes | `2021/Banco de imágenes 1920x1280/` | ~30 fotos de stock | ❌ No recomiendo usarlas: son genéricas y bajan el nivel premium |
| Iconos de servicios | `2021/ICONOS WEB GRUPO OLIVO/` | 10 PNG + EPS | Referencia. Conviene rehacerlos en el estilo nuevo |
| Fuentes de iconos | `2021/GO/fonts/` (icomoon, flaticon) | — | ❌ Son de la plantilla, no de la marca |

---

## 6. Contenido extraído (en `docs/textos/`)

| Documento | Qué contiene |
| --- | --- |
| `DIAGRAMA PÁGINA WEB GRUPOLIVO` | La estructura que pidió la clienta: quiénes somos, 4 bloques de sellos, concursos, servicios, contacto y redes |
| `ESTRUCTURA Y ORDEN DEL SITIO WEB` | Menú para el lanzamiento (Libros, Autores, Servicios, Blog, Sobre nosotros, Contacto) y planes a futuro (sellos AlitaSeller y FanSeller, noticias) |
| `ACTUALIZACIÓN SITIO WEB` (mayo 2023) | Los 6 servicios con precio y CTA, "fondo blanco para el sitio", "la página es pesada para cargar" y "quitar Hechos Criollos" |
| `SINOPSIS … Y ENLACES AMAZON` | Sinopsis y enlaces de ~17 libros |
| `AUTORES_`, `RESEÑA DE AUTORES` | Biografías e Instagram de 24 autores |
| `EQUIPO EDITORIAL`, `RESEÑA EQUIPO OPERATIVO` | Equipo por áreas (editores, Team Reto Escritor, marketing, administración) |
| `TEXTO PARA LA PAGINA WEB`, `Textos de pagina web actual` | Copy de "Quiénes somos", misión, visión y citas literarias |
| `PLANTILLAS DE EMAILS COMMERCE` | Plantillas de correos de pedido (útiles para Resend) |
| `OBSERVACIONES TÉCNICAS` | Notas técnicas del sitio anterior |

### Contradicciones que hay que resolver
- **Hechos Criollos:** en 2023 la clienta pidió quitarlo de la web, pero el diagrama de 2026 lo incluye en "Novelas independientes".
- **Sede:** el brief dice Caracas, pero el diagrama dice "creada en 2016 en Ciudad Bolívar".
- **Sellos:** según el documento, son tres (tucoach.go, Reto Escritor, Alita), cuatro (más Hechos Criollos) o cinco (más AlitaSeller y FanSeller). Además aparecen las colecciones Diosa Yekuana, CASOS (noir) y Reto Expresivo.
- **Reto Escritor:** el brief lo trata como producto de $15, pero los documentos lo describen como un concurso con web propia (retoescritor.com).
- **Fondo:** en 2023 la clienta pidió "fondo blanco". Esto choca con la idea de un fondo color papel.

---

## 7. Datos que faltan

- [ ] Precio en USD de cada libro
- [ ] Formatos disponibles (físico, ebook) y stock
- [ ] Logo en SVG (o permiso para convertir el EPS)
- [ ] Portadas en alta resolución de: El príncipe de la máscara, Héroes muertos, Reliquias olvidadas, 7 pasos para construir tu sueño y Coaching y ecología de las emociones
- [ ] Portada plana del libro de Yulis Rondón y de Feliz donde sea
- [ ] Sinopsis de los ~12 títulos que solo tienen portada
- [ ] Datos de pago (Pago Móvil, banco, Zelle, Binance) para el checkout. Para las referencias bastan marcadores
- [ ] Enlaces de Calendly para los servicios
- [ ] Logos de Reto Expresivo y FanSeller

---

## 8. Preguntas para ti antes de la Fase 1

1. **Tienda propia o Amazon:** ¿las fichas de libro muestran "Comprar aquí" con los cinco métodos de pago, con Amazon como alternativa, o solo la tienda propia?
2. **Servicios:** ¿agrego una página de Servicios editoriales y una de Concursos a las páginas de referencia?
3. **Hechos Criollos:** ¿se incluye o no?
4. **Fondo blanco:** la clienta lo pidió en 2023. ¿Las direcciones visuales respetan el blanco, o puedo proponer un fondo color papel en alguna?
5. **Logo en SVG:** ¿se lo pides a la clienta o al diseñador, o lo convierto yo desde el EPS (necesito instalar Ghostscript)?
