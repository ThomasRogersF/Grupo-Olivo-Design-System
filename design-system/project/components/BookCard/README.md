# BookCard

La unidad del catálogo: la portada en un pozo `surface-sunk`, el sello en mono, el título en serif, autor, precio y «Agregar +».

## Anatomía
1. `go-book__well`: pozo 2:3 con la portada apoyada abajo; en hover la portada sube 12px (`ease-out`, 500ms). Es el enlace a la página del libro.
2. `go-book__sello`: el sello editorial en `accent`.
3. `go-book__title`: estilo `book-title` (21px; 17px en móvil).
4. `go-book__author`: `body-s` en `ink-muted`.
5. `go-book__row`: PriceTag y el botón «Agregar +», separados por un filete `rule`.

## Retícula
`repeat(auto-fill, minmax(200px, 1fr))` con 48px de fila y 32px de columna. Bajo 600px, dos columnas fijas con 16px de separación.

## Comportamiento
- «Agregar +» lanza una copia de la portada que vuela al carrito (`ease-in`, 900ms, escala 0.08) y hace rebotar el contador. Con `prefers-reduced-motion`, solo se actualiza el contador y aparece un Toast.
- Al filtrar por sello, las tarjetas se reordenan con GSAP Flip (`duration-slow`, `ease-in-out`).

## Lo que provee quien lo usa
Portada, título, autor, sello, precio en USD (o `[PRECIO]` mientras no exista) y el slug para el enlace.
