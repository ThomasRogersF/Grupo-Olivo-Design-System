# CartDrawer

Panel lateral derecho de 420px que se abre al tocar el carrito, sobre un velo `overlay`.

## Uso
- Entra desde la derecha en `duration-slow` con `ease-out`; el velo se desvanece. Cierra con ✕, Escape o tocando el velo, y devuelve el foco al botón del carrito.
- Cada línea: miniatura de la portada, título, autor, cantidad (`go-qty`) y precio.
- Pie: subtotal en USD y Bs, nota de envío y «Ir a pagar».
- Vacío: usa EmptyState con «Tu carrito está vacío» y «Explorar el catálogo».
- En móvil ocupa todo el ancho.
