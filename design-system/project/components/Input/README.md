# Input

Campo de texto de 48px de alto con etiqueta visible siempre encima.

## Uso
- Envuelve en `go-field` con `go-label`, el `go-input` y opcionalmente `go-help`.
- Borde `control-border` (3.5:1); en foco, anillo `focus` de 2px.
- Error: añade `go-field--error`, `aria-invalid="true"` y un `go-help` enlazado con `aria-describedby` que diga qué está mal y cómo arreglarlo.
- Tamaño de letra 16px para que iOS no haga zoom.

## Lo que provee quien lo usa
`id`, etiqueta, `type` correcto (`email`, `tel`, `text`) y `autocomplete`.

## No
- No uses el placeholder como etiqueta.
