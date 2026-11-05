# Button

Botón en píldora: la acción principal en `ink`, la secundaria con contorno, la terciaria como texto.

## Variantes
- `go-btn--primary`: fondo `ink`, texto `on-ink`. En hover pasa a `accent`. Una sola por vista: «Explorar el catálogo», «Agregar al carrito», «Confirmar pedido».
- `go-btn--secondary`: contorno `ink`; en hover se rellena. Para la alternativa: «Publica con nosotros».
- `go-btn--text`: sin borde, para acciones menores como «También en Amazon».
- `go-btn--sm` (36px de alto) en tarjetas y en el Drawer; `go-btn--block` a todo el ancho en checkout móvil.
- Estados: `disabled` (Agotado), `go-btn--loading` con `aria-busy="true"` mientras se procesa un pago.

## Lo que provee quien lo usa
Un verbo con objeto, en español y en tuteo: «Agregar al carrito», no «Agregar». La flecha SVG solo en enlaces que llevan a otra página; se desplaza 4px en hover.

## No
- No uses `brand-leaf` como fondo de botón: el texto blanco no llega a 3:1.
- No pongas dos primarios lado a lado.
