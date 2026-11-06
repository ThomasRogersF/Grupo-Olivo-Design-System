# Skeleton

Bloques de carga con la forma exacta de BookCard, con un brillo lento.

## Uso
- Mismas proporciones que el contenido real para que nada salte al cargar.
- Contenedor con `aria-busy="true"`. Con `prefers-reduced-motion` el brillo se detiene.
- Solo para cargas de más de 300 ms; las páginas de libro se generan estáticas y casi no lo necesitan.
