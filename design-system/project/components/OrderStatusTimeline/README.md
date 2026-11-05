# OrderStatusTimeline

Línea de tiempo vertical del pedido: recibido, pendiente de verificación, aprobado y enviado.

## Uso
- Hecho: punto `accent` con ✓ y línea `accent`. Actual: punto `warning` con `aria-current="step"`. Por hacer: contorno `control-border` y título en `ink-muted`.
- Cada paso puede llevar fecha y un texto corto que diga qué pasa y qué sigue.
- Si el pago se rechaza, el paso actual pasa a Badge `--danger` con el motivo y un botón para subir otro comprobante.
