# PriceTag

Precio en dólares con su equivalente en bolívares a la tasa BCV del día debajo.

## Uso
- Los precios se guardan en USD; los bolívares se calculan con la tasa de `settings` que actualiza el cron diario.
- Formato venezolano: `US$ 15,00` y `Bs 1.234,56` (coma decimal, punto de miles), siempre con `tabular-nums`.
- `go-price--sale`: precio anterior tachado en `ink-muted` y precio nuevo en `accent`.
- `go-price--lg` (24px) en la página del libro y en el total del carrito.
- `go-price__ph` muestra `[PRECIO]` mientras la clienta no haya cargado el precio.
