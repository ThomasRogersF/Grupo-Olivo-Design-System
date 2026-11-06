# Rediseño web de Grupo Olivo – Brief del proyecto

## 1. Resumen

Nuestro nuevo equipo de consultoría en TI y tecnología tiene un primer cliente potencial: **Grupo Olivo (Editorial Grupolivo)**, una editorial con sede en Caracas, Venezuela, dirigida por Adriana Olivares. Su sitio actual es **grupolivo.com**, una tienda en línea hecha en WordPress donde los clientes ven y compran libros.

La petición principal de la clienta es **migrar el sitio para reducir costos**. Actualmente paga alrededor de $75 por hosting y dominio en Bluehost (falta confirmar si es mensual o anual). Además, quiere que el nuevo sitio quede **extremadamente bien hecho**.

Nuestra propuesta: eliminar WordPress por completo y reconstruir el sitio con código a medida, sobre infraestructura gratuita o de muy bajo costo, con un diseño premium y varias funcionalidades extra que agreguen valor.

**Estado:** cliente potencial, todavía no ha pagado.

## 2. Objetivos de la clienta

- Reducir los costos anuales de hosting y mantenimiento
- Un sitio web con un diseño pulido y de alto nivel
- Seguir vendiendo libros en línea en Venezuela y el resto de Latinoamérica

## 3. Situación actual

- **Plataforma:** WordPress (tienda en línea)
- **Hosting:** Bluehost
- **Registrador del dominio:** desconocido, por confirmar
- **Observaciones:** el diseño se ve anticuado. Una página de plantilla sobrante (/homepage-2/) sigue pública e indexada en Google, lo que indica que el sitio nunca se terminó de limpiar.
- **Productos vistos:** libros, además de productos como el "Reto Escritor" ($15)

## 4. Solución propuesta

Un sitio web totalmente a medida, construido desde cero, sin WordPress.

**Stack propuesto:**

| Capa | Elección | Por qué |
| --- | --- | --- |
| Framework | Next.js (App Router) + TypeScript | Renderizado en servidor para SEO, y espacio para el carrito, el foro y el panel de administración |
| Hosting | Cloudflare Workers (plan gratuito) con el adaptador OpenNext | El plan gratuito permite uso comercial |
| Dominio + DNS | Cloudflare Registrar | Dominios a precio de costo, unos $10 al año por un .com |
| Base de datos, autenticación | Supabase (plan gratuito) | Postgres, inicio de sesión y seguridad a nivel de fila para reseñas y foro |
| Imágenes | Cloudflare R2 | Mantiene las portadas fuera de los límites de archivos y ancho de banda de Supabase |
| Estilos | Tailwind CSS + shadcn/ui | Rápido de construir y fácil de darle un look premium |
| Animación | Motion + GSAP + Lenis | Transiciones de página, efectos al hacer scroll, scroll suave |
| Correo | Resend (plan gratuito) | Confirmaciones de pedido y correos de pago aprobado |
| Tareas programadas | Cloudflare Cron Triggers | Actualización diaria de la tasa BCV y mantener Supabase activo |

**Por qué no Vercel:** el plan gratuito Hobby de Vercel está limitado a uso personal no comercial. Una tienda en línea necesitaría el plan Pro de $20 al mes, así que Cloudflare es la mejor opción gratuita.

**Notas de costos:**

- **Costo inicial: unos $10 al año** por el dominio. Todo lo demás funciona en planes gratuitos.
- **Cloudflare:** un Worker puede pesar hasta 3 MiB en el plan gratuito. Las librerías de animación pesadas cuentan para ese límite, así que solo se cargan en las páginas que las usan. Si el sitio lo supera, Workers Paid cuesta $5 al mes (límite de 10 MiB).
- **Supabase:** el plan gratuito incluye 500 MB de base de datos y 1 GB de archivos, y los proyectos se pausan tras 7 días sin actividad. Una tienda con visitas diarias se mantiene activa, y un ping diario programado la mantiene despierta. Si hace falta, el plan Pro cuesta $25 al mes.
- El objetivo es mantener los costos de la clienta lo más bajos posible para que nos elija.

### 4.1 Flujo de pagos

- **PayPal:** totalmente automático, con PayPal Checkout y webhooks.
- **Pago Móvil, transferencia bancaria, Zelle, Binance Pay:** el cliente ve los datos de pago y luego envía el número de referencia y una captura del comprobante. El pedido queda "pendiente" hasta que la clienta lo aprueba en el panel de administración.
- Binance Pay tiene una API para comercios, pero requiere una cuenta de comerciante. Se empieza con el flujo manual y se automatiza más adelante.
- Los precios se guardan en dólares y se muestran en bolívares a la tasa BCV del día.

### 4.2 Implementación de SEO y GEO

- Las páginas de libros se generan de forma estática, así los rastreadores reciben HTML completo.
- Datos estructurados JSON-LD por libro (Book, Product, Offer, AggregateRating) y migas de pan.
- `sitemap.xml`, `robots.txt` y `llms.txt`.
- **Redirecciones 301 desde cada URL vieja de WordPress.** Es el paso de SEO más importante de la migración; sin esto la clienta pierde el posicionamiento que ya tiene en Google.

### 4.3 Implementación de publicidad y seguimiento

- Un solo feed de productos en `/feeds/products.xml`, en formato Google Merchant, que pueden leer Meta, TikTok y Google.
- Meta Pixel, TikTok Pixel y GA4, más eventos del lado del servidor (Meta Conversions API, TikTok Events API) para que los bloqueadores de anuncios no rompan el seguimiento.
- Banner de consentimiento de cookies conectado a Google Consent Mode v2.

### 4.4 Estructura del proyecto

```
grupolivo/
├─ app/
│  ├─ (tienda)/
│  │  ├─ page.tsx                  # Inicio: portada, más vendidos, ofertas
│  │  ├─ libros/[slug]/page.tsx    # Página del libro + reseñas
│  │  ├─ categorias/[slug]/
│  │  ├─ ofertas/                  # Libros con descuento
│  │  ├─ mas-vendidos/
│  │  ├─ carrito/
│  │  ├─ checkout/
│  │  └─ pedido/[id]/              # Estado del pedido + subir comprobante
│  ├─ comunidad/                   # Foro
│  │  └─ [hilo]/
│  ├─ cuenta/                      # Pedidos y perfil del cliente
│  ├─ admin/
│  │  ├─ libros/  pedidos/  pagos/        # pagos = confirmar pagos manuales
│  │  ├─ descuentos/  barra-promo/  moderacion/
│  ├─ api/
│  │  ├─ paypal/ (crear, capturar, webhook)
│  │  └─ cron/tasa-bcv/
│  ├─ feeds/products.xml/route.ts
│  ├─ llms.txt/route.ts
│  ├─ sitemap.ts
│  └─ robots.ts
├─ components/   ui/  tienda/  motion/
├─ lib/          supabase/  pagos/  seo/  tracking/
├─ supabase/migrations/
├─ redirects.ts                    # URLs viejas de WordPress → nuevas
├─ open-next.config.ts
└─ wrangler.jsonc
```

**Tablas principales de la base de datos:** `books`, `categories`, `orders`, `order_items`, `payments` (método, referencia, comprobante, estado), `discounts`, `promo_bar`, `reviews`, `forum_threads`, `forum_posts`, `profiles`, `settings` (tasa BCV).

### 4.5 Fases de desarrollo

1. **Lanzamiento:** catálogo, carrito, checkout, los cinco métodos de pago, panel de administración, migración con redirecciones y SEO básico.
2. **Crecimiento:** reseñas y calificaciones, descuentos, más vendidos, barra promocional, píxeles, consentimiento de cookies y feed de productos.
3. **Comunidad:** foro y herramientas de moderación.

Las fases 2 y 3 se pueden cotizar por separado, así la clienta obtiene rápido un sitio más barato y más bonito.

## 5. Funcionalidades

### 5.1 Tienda y catálogo

- Catálogo de libros con páginas de producto
- Pedidos en línea y checkout
- Envíos dentro de Venezuela y a otros países de Latinoamérica

### 5.2 Panel de administración / CMS

- Agregar, editar y eliminar libros
- Gestionar precios, inventario y descuentos
- Gestionar pedidos
- **Confirmación manual de pagos** para los métodos que requieren verificación humana (Pago Móvil, transferencia bancaria, Zelle, Binance Pay)
- Gestionar la barra promocional superior y las secciones destacadas

### 5.3 Diseño y experiencia

- Diseño visual premium y muy pulido
- Animaciones e interacciones fluidas
- Totalmente responsive (mobile first)

### 5.4 Comunidad

- Foro donde los lectores pueden comentar y compartir sus libros favoritos
- Calificaciones de libros
- Reseñas

### 5.5 Ventas y promociones

- Descuentos, sobre todo para libros que se venden poco
- Sección de más vendidos
- Barra promocional superior para anuncios y campañas

### 5.6 SEO y GEO

- Construido para que Google y otros rastreadores lo lean fácilmente
- Optimizado para buscadores con IA y motores de respuesta (GEO)
- Datos estructurados para libros y productos, URLs limpias, sitemap y carga rápida
- Eliminar páginas de plantilla sobrantes y duplicadas durante la migración

### 5.7 Marketing y seguimiento

- Feed del catálogo de productos para que Meta Commerce Manager, TikTok Catalog y Google Merchant Center tomen los libros para anuncios de compra y remarketing dinámico
- Píxeles de seguimiento (Meta, TikTok, Google)
- Banner de consentimiento de cookies

## 6. Métodos de pago

Solo se aceptarán estos métodos:

| Región | Método |
| --- | --- |
| Venezuela | Pago Móvil |
| Venezuela | Transferencia bancaria |
| Venezuela | Zelle |
| Venezuela | Binance Pay |
| Resto de Latinoamérica | PayPal |

Mercado Pago **no** se incluye. No opera en Venezuela, y para recibir el dinero haría falta una empresa o cuenta bancaria en otro país. Se podría agregar más adelante si crecen las ventas fuera de Venezuela.

## 7. Referentes a estudiar

Competidores de Estados Unidos para revisar buenas prácticas:

- **Bookshop.org** – modelo de librería independiente
- **Barnes & Noble** – catálogo a gran escala y promociones
- **Powell's Books** – profundidad del catálogo y navegación
- **Goodreads** – reseñas, calificaciones y comunidad de lectores

## 8. Preguntas pendientes

- ¿Los $75 son un costo mensual o anual?
- ¿Quién es el registrador del dominio y quién tiene acceso?
- ¿Grupo Olivo vende servicios además de libros (edición, concursos de escritura, talleres)? *(Nuestro compañero lo confirmará con la clienta)*
- ¿Grupolivo International LLC (Florida) es la empresa de la clienta? Si es así, podría abrir más opciones de pago.
- ¿Qué métodos de pago acepta la clienta actualmente?
- ¿Cuántos libros hay en el catálogo, y hay que migrar contenido existente (productos, blog, clientes)?
