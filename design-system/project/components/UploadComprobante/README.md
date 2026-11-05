# UploadComprobante

Paso final de un pago manual: número de referencia más la captura del comprobante.

## Uso
- Zona de carga con borde punteado `control-border`; en hover o al arrastrar encima toma `accent` y `accent-soft`.
- Acepta imagen o PDF hasta 5 MB. El archivo va a Cloudflare R2; la referencia a la tabla `payments`.
- Tras enviar, el pedido queda «Pendiente de verificación» (Badge `--warning`) y se muestra OrderStatusTimeline.
- Errores claros: «El archivo pesa 8 MB. Sube uno de hasta 5 MB.»
