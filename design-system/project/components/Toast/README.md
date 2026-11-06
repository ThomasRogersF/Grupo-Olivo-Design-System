# Toast

Aviso flotante abajo a la derecha (abajo al centro en móvil) que confirma una acción o informa un error.

## Uso
- Éxito: miniatura de la portada o icono en `accent-soft`, `role="status"`, se cierra solo a los 4 s.
- Error: icono en `danger-soft`, `role="alert"`, no se cierra solo.
- Entra subiendo 16px con `ease-out` en `duration-base`.
- El texto dice qué pasó y, en errores, cómo arreglarlo.
