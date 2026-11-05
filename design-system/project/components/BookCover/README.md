# BookCover

Una portada como objeto físico: proporción 2:3, esquinas `radius-book` (2px el lomo, 4px el canto), sombra `shadow-book` y un brillo de lomo a la izquierda.

## Uso
- Es la base de BookCard, del hero en abanico, de la página de libro y del Toast.
- `go-cover--tilt` añade inclinación 3D (±8°) y brillo siguiendo el cursor. Solo en dispositivos con cursor fino y sin `prefers-reduced-motion`.
- En el hero, cinco portadas suben y se abren en abanico (`duration-hero`, `ease-out`), y se abren un poco más con el scroll.

## Lo que provee quien lo usa
La portada real (WebP/AVIF, unos 600px de alto) y un `alt` con «Portada de <título>».

## No
- No recortes ni deformes la portada: siempre `object-fit: cover` sobre 2:3 exacto. Si la imagen no es 2:3, pide la portada plana.
- No uses mockups 3D ni fotos de libros como portada.
