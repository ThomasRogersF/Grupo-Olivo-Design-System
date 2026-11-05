# PaymentMethodSelector

Lista de radios grandes para elegir entre los cinco métodos de pago; el elegido despliega sus datos.

## Uso
- Orden: Pago Móvil, Transferencia, Zelle, Binance Pay y PayPal. En Venezuela el primero va preseleccionado; fuera de Venezuela, PayPal.
- La opción elegida toma borde `accent` y fondo `accent-soft`, y muestra los datos de pago en mono para copiarlos fácil (añade un botón «Copiar» por dato en la implementación).
- Los cuatro métodos manuales llevan al paso UploadComprobante; PayPal abre PayPal Checkout.
- Los datos `[BANCO]`, `[TELÉFONO]`, etc. son marcadores hasta que la clienta los envíe.
- `fieldset` + `legend`; los radios son nativos, así funcionan con teclado.
