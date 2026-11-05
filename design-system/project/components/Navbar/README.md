# Navbar

Barra sticky de 68px con el logo original a la izquierda, seis enlaces y el carrito.

## Uso
- Logo: el PNG a color `grupo-olivo-color` a 26px de alto, nunca redibujado. En tema oscuro cambia solo al `grupo-olivo-negativo`: pon las dos imágenes con las clases `go-logo-pos` y `go-logo-neg` (la segunda con `alt=""`).
- Menú (de la estructura que pidió la clienta): Libros, Autores, Sellos, Servicios, Concursos, Nosotros.
- La página actual lleva `aria-current="page"` y el subrayado fijo.
- Fondo `surface` al 92% con desenfoque; filete `rule` abajo.
- Bajo 860px los enlaces pasan a un menú; el carrito siempre visible.
- El contador `go-cart-btn__n` rebota (escala 1.7 → 1, elastic) cuando entra un libro.
