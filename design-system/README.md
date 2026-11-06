# Sistema de diseño · Colofón

Copia completa del Design System «Grupo Olivo» publicado en Claude, la dirección visual A (Colofón).

| Ruta | Qué es |
|---|---|
| `project/README.md` | Guía de marca: voz, logo, color, tipografía, espacio, imágenes, movimiento |
| `project/tokens.json` | Fuente de verdad de los tokens (color claro/oscuro, tipografía, espacio, radios, sombras, duraciones, curvas) |
| `project/tokens.css` | Los tokens compilados como variables CSS, listos para importar |
| `project/components/bundle.css` | Estilos de los 23 componentes (prefijo `go-`) |
| `project/components/<Componente>/` | `README.md` (guía de uso) y `preview.html` (vista previa) de cada componente; `Cover/` es la portada del sistema |
| `project/fonts/` | Archivos de fuente (OFL): Libre Caslon Display y Text, Hanken Grotesk, IBM Plex Mono |
| `project/assets/` | Logos, portadas y fotos de autores, por grupo, cada uno con su `README.md` |
| `project/design-system.json` | Índice del artifact (nombre, grupos de assets e ids) |
| `asset-map.json` | Qué archivo de `project/assets/` corresponde a cada enlace `/_blob/<id>` de las vistas previas |
| `tailwind.preset.ts` | Preset de Tailwind que nombra los tokens de `tokens.css` |

## Uso en Next.js

1. Copia `project/tokens.css`, `project/components/bundle.css` y `project/fonts/` al proyecto e impórtalos en `app/globals.css`.
2. Añade `tailwind.preset.ts` en `tailwind.config.ts` (`presets: [goPreset]`).
3. Las vistas previas usan enlaces `/_blob/<id>` del artifact; fuera de él, sustitúyelos con `asset-map.json`.

Si cambias el sistema en Claude, vuelve a traerlo a esta carpeta; si lo cambias aquí, publícalo de nuevo en el artifact.
