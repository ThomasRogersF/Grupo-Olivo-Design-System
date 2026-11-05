"""Construye las páginas de referencia de Grupo Olivo (Fase 3).
Une tokens.css + bundle.css + site.css + site.js dentro de cada HTML para que cada página funcione sola."""
import os, re, sys, html
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
DS = os.path.join(OUT, "..", "design-system", "project")

tokens = open(os.path.join(DS, "tokens.css")).read()
tokens = "\n".join(l for l in tokens.splitlines() if not l.startswith("@font-face"))  # fuentes vía Google Fonts
CSS = tokens + "\n" + open(os.path.join(DS, "components", "bundle.css")).read() + "\n" + open(os.path.join(HERE, "site.css")).read()
JS = open(os.path.join(HERE, "site.js")).read()
FONTS = "https://fonts.googleapis.com/css2?family=Libre+Caslon+Display&family=Libre+Caslon+Text:ital,wght@0,400..700;1,400..700&family=Hanken+Grotesk:wght@400..700&family=IBM+Plex+Mono:wght@400;500&display=swap"

ARROW = '<svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M1 8h13M9 3l5 5-5 5" stroke="currentColor" stroke-width="1.6"/></svg>'
I = {  # iconos de línea, trazo 1.6
 "chat": '<path d="M4 5h16v10H9l-5 4z"/>',
 "cal": '<rect x="4" y="5" width="16" height="15" rx="1"/><path d="M4 10h16M9 3v4M15 3v4"/>',
 "pen": '<path d="M5 19l3.5-.8L19 7.7 16.3 5 5.8 15.5z"/><path d="M14 7l3 3"/>',
 "layout": '<rect x="5" y="3" width="14" height="18" rx="1"/><path d="M8 7h8M8 11h8M8 15h5"/>',
 "up": '<path d="M4 18l6-6 4 4 6-8"/><path d="M15 8h5v5"/>',
 "globe": '<circle cx="12" cy="12" r="8"/><path d="M4 12h16M12 4c3 3 3 13 0 16M12 4c-3 3-3 13 0 16"/>',
 "play": '<path d="M9 7l8 5-8 5z" fill="currentColor"/>',
 "truck": '<path d="M3 7h11v9H3zM14 10h4l3 3v3h-7"/><circle cx="7" cy="17.5" r="1.5"/><circle cx="17" cy="17.5" r="1.5"/>',
}
def icon(k, s=22): return f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round" aria-hidden="true">{I[k]}</svg>'

BOOKS = [
 ("fleur","Fleur","Florencia Frezza","alita","Alita"),
 ("21-preguntas","21 preguntas para conquistarte","Jemmy Lee","alita","Alita"),
 ("con-sentido","Con sentido","José Espósito","tucoach","tucoach.go"),
 ("lider-coach","Líder Coach","Norberto Peña","tucoach","tucoach.go"),
 ("poder-del-fee","El poder del fee","Jennifer Fernández","tucoach","tucoach.go"),
 ("horror-emprender","El horror de emprender","Rafa Solbas","tucoach","tucoach.go"),
 ("errores-clinicos","7 errores clínicos","Mónica Chirinos","tucoach","tucoach.go"),
 ("anecdotas","Anécdotas de una viajera del tercer mundo","Lissette Van Der Biest","reto","Reto Escritor"),
 ("soledad","Soledad, ¿una cura o locura?","Zuleima Virguez","reto","Reto Escritor"),
 ("escribir-para-sanar","Escribir para sanar","18 autoras","reto","Reto Escritor"),
 ("extraordinario","Descubre lo extraordinario en ti","Mariene Piñero","reto","Reto Escritor"),
 ("coletepelo","Historias a Coletepelo","Irene Carrasquero","reto","Reto Escritor"),
 ("alambre","Al cruzar el alambre de púas","Esmeralda Villanueva","reto","Reto Escritor"),
 ("engranaje","Engranaje vital","Francisco Rangel Gómez","reto","Reto Escritor"),
 ("caso-indefendible","Un caso indefendible","José Custodio Sánchez Morante","indep","Independiente"),
 ("caso-imposible","Un caso imposible","José Custodio Sánchez Morante","indep","Independiente"),
 ("van-gogh","Las sombras de Vincent van Gogh","Luis Manuel Marcano","indep","Independiente"),
 ("por-si-me-muero","Por si me muero sin que lo sepas","María Elena Fernández-Morán Spear","indep","Independiente"),
 ("a-quien","A quién le escribes","Adriana Mara Olivares","indep","Independiente"),
]
B = {b[0]: b for b in BOOKS}
PRICE = '<span class="go-price"><span class="go-price__usd">US$ <span class="go-price__ph">[PRECIO]</span></span></span>'

def card(id_, badge=False):
    _, t, a, s, sl = B[id_]
    bd = '<span class="go-badge go-badge--new">Novedad</span>' if badge else ''
    return f'''<article class="go-book" data-s="{s}">
  <a class="go-book__well" href="libro.html">{bd}<img src="img/{id_}.webp" alt="Portada de {html.escape(t)}" loading="lazy"></a>
  <span class="go-book__sello">{sl}</span>
  <h3 class="go-book__title"><a href="libro.html">{html.escape(t)}</a></h3>
  <p class="go-book__author">{html.escape(a)}</p>
  <div class="go-book__row">{PRICE}<button class="go-add" data-add data-title="{html.escape(t)}">Agregar +</button></div>
</article>'''

PAGES = [("index.html","Inicio"),("catalogo.html","Catálogo"),("libro.html","Libro · Fleur"),("servicios.html","Servicios"),("autores.html","Autores y sellos"),("comunidad.html","Comunidad"),("checkout.html","Checkout"),("pedido.html","Estado del pedido"),("admin.html","Admin · pagos")]
NAV = [("catalogo.html","Libros"),("servicios.html","Servicios"),("autores.html","Autores"),("index.html#concursos","Concursos"),("comunidad.html","Comunidad"),("index.html#nosotros","Nosotros")]

def header(cur):
    links = "".join(f'<li><a href="{h}"{" aria-current=\"page\"" if h==cur else ""}>{t}</a></li>' for h,t in NAV)
    mlinks = "".join(f'<a href="{h}">{t}</a>' for h,t in NAV)
    return f'''<div class="go-promo">Envíos a toda Venezuela y Latinoamérica · Paga con <b>Pago Móvil, Zelle, Binance Pay o PayPal</b></div>
<header class="site-head"><nav class="go-nav" aria-label="Principal"><div class="go-nav__inner">
  <a class="go-nav__logo" href="index.html" aria-label="Grupo Olivo, inicio"><img class="go-logo-pos" src="img/logo-go-color.png" alt="Grupo Olivo" width="123" height="26"><img class="go-logo-neg" src="img/logo-go-blanco.png" alt="" width="123" height="26"></a>
  <ul class="go-nav__links">{links}</ul>
  <a class="go-btn go-btn--secondary nav-cta" href="servicios.html">Publica tu libro</a>
  <button class="go-nav__menu" aria-label="Abrir menú" data-menu-open><svg width="22" height="22" viewBox="0 0 22 22" aria-hidden="true"><path d="M3 7h16M3 15h16" stroke="currentColor" stroke-width="1.6"/></svg></button>
  <a class="go-cart-btn" href="checkout.html" aria-label="Carrito">Carrito <span class="go-cart-btn__n">2</span></a>
</div></nav></header>
<div class="mmenu" id="mmenu" hidden><div class="mmenu__panel"><button class="go-drawer__close mmenu__close" aria-label="Cerrar menú" data-menu-close>✕</button>{mlinks}<a href="servicios.html">Publica tu libro</a></div></div>'''

FOOTER = '''<footer class="wrap"><div class="go-footer">
  <div><img class="go-logo-pos" src="img/logo-go-color.png" alt="Grupo Olivo" width="104" height="22"><img class="go-logo-neg" src="img/logo-go-blanco.png" alt="" width="104" height="22"><p style="margin:0;max-width:34ch">Empresa editorial familiar, creada en 2016. Afiliada a la Cámara Venezolana del Libro desde 2018.</p></div>
  <div><h4>Libros</h4><ul><li><a href="catalogo.html">Catálogo</a></li><li><a href="autores.html">Sellos</a></li><li><a href="autores.html">Autores</a></li><li><a href="comunidad.html">Comunidad</a></li></ul></div>
  <div><h4>Para autores</h4><ul><li><a href="servicios.html">Servicios editoriales</a></li><li><a href="servicios.html#coaching">Coaching editorial</a></li><li><a href="servicios.html#distribucion">Distribución</a></li><li><a href="index.html#concursos">Concursos</a></li></ul></div>
  <div><h4>Contacto</h4><ul><li>editorialgrupoolivo@gmail.com</li><li>+58 414 8680195</li><li><a href="https://www.instagram.com/grupolivo/">@grupolivo</a></li></ul></div>
  <div class="go-footer__legal"><span>© Editorial Grupo Olivo</span><span>Envíos a Venezuela y Latinoamérica · Precios en USD y Bs a tasa BCV</span></div>
</div></footer>'''

def switcher(cur):
    items = "".join(f'<li><a href="{h}"{" aria-current=\"page\"" if h==cur else ""}>{t}<span>{i+1:02d}</span></a></li>' for i,(h,t) in enumerate(PAGES))
    return f'<details class="pages go-root"><summary>Páginas de referencia ▴</summary><ol>{items}</ol></details>'

def page(fname, title, body, flip=False, admin=False):
    libs = '<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>\n<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>\n'
    if flip: libs += '<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/Flip.min.js"></script>\n'
    if not admin: libs += '<script src="https://cdn.jsdelivr.net/npm/lenis@1.1.13/dist/lenis.min.js"></script>\n'
    head = f'''<title>{title}</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<style>
{CSS}
</style>'''
    doc = f'''{head}
<div class="go-root">
{header(fname)}
<main id="main">
{body}
</main>
{"" if admin else FOOTER}
</div>
{switcher(fname)}
{libs}<script>
{JS}
</script>
'''
    if fname != "index.html":
        doc = '<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n' + doc.replace("</style>", "</style>\n</head>\n<body>", 1) + "</body>\n</html>\n"
    open(os.path.join(OUT, fname), "w").write(doc)

# ======================= INICIO =======================
SERVICES = [
 ("coaching","chat","Sesión 1:1","Coaching editorial","Sesión de 45 minutos para descubrir ideas de libros, desatar nudos creativos, encontrar el propósito de tu libro o armar su estructura.","US$ 97","Agenda una sesión"),
 ("correccion","pen","Por cotización","Paquete corrección","Revisión de contenido, corrección de estilo y ortotipográfica para concursos, editoriales o autopublicación.","Cotiza","Pide tu cotización"),
 ("diseno","layout","Por cotización","Paquete diseño","Diagramación, corrección ortotipográfica y diseño de portada para tu proyecto de autopublicación.","Cotiza","Pide tu cotización"),
 ("escala","up","Programa · 12 semanas","Escala como autor","Acompañamiento para coaches, especialistas y conferencistas que quieren publicar su primer libro de no ficción.","12 semanas","Más información"),
 ("distribucion","globe","9 países","Distribución on-demand","Tu libro físico en más de 200 librerías de Latinoamérica y España, además de Amazon.","+200 librerías","Pide información"),
]
def svc_card(s):
    id_, ic, kind, t, d, p, cta = s
    return f'''<a class="svc" href="servicios.html#{id_}"><div class="svc__top"><span class="svc__icon">{icon(ic)}</span><span class="svc__kind">{kind}</span></div>
<h3>{t}</h3><p>{d}</p><div class="svc__foot"><span class="svc__price">{p}</span><span class="svc__cta">{cta} {ARROW}</span></div></a>'''

home = f'''
<section class="wrap hero">
  <div>
    <span class="go-eyebrow">Editorial independiente · desde 2016</span>
    <h1 class="h-xl"><span class="line"><span>Libros pensados</span></span><span class="line"><span>en su <em>lector.</em></span></span></h1>
    <p class="lede">Una editorial con tres sellos de publicación, creciendo para llevar más libros de Venezuela al mundo. Innovando en servicios para autores y nuevos títulos para nuestros lectores.</p>
    <div class="ctas"><a class="go-btn go-btn--primary" href="catalogo.html">Explorar el catálogo {ARROW}</a><a class="go-btn go-btn--secondary" href="servicios.html">Publica tu libro</a></div>
  </div>
  <div class="stage" aria-label="Portadas destacadas">
    {"".join(f'<div class="bk"><span class="go-cover"><img src="img/{k}.webp" alt="Portada de {html.escape(B[k][1])}"></span></div>' for k in ["soledad","anecdotas","caso-indefendible","con-sentido","fleur"])}
  </div>
</section>

<section class="wrap doors" aria-label="¿Lees o escribes?" data-reveal>
  <a class="door door--read" href="catalogo.html"><div><span class="go-eyebrow">Para lectores</span><h2>Encuentra tu próxima lectura</h2><p>Novela, testimonio, coaching y no ficción de autores venezolanos, con envío a Venezuela y Latinoamérica.</p></div><span class="arrow">{ARROW}</span>
    <div class="door__covers" aria-hidden="true"><img src="img/van-gogh.webp" alt=""><img src="img/caso-imposible.webp" alt=""></div></a>
  <a class="door door--write" href="servicios.html"><div><span class="go-eyebrow">Para autores</span><h2>Publica tu libro con nosotros</h2><p>Te acompañamos desde la idea hasta las librerías.</p>
    <ul><li>Coaching editorial</li><li>Corrección</li><li>Diseño y diagramación</li><li>Distribución</li></ul></div><span class="arrow">{ARROW}</span></a>
</section>

<section class="sellos-strip" aria-label="Sellos editoriales"><div class="wrap">
  <span class="go-eyebrow go-eyebrow--bare">Sellos editoriales</span>
  <img src="img/logo-tucoach.png" alt="tucoach.go"><img src="img/logo-alita.png" alt="Alita"><img class="reto" src="img/logo-reto-negro.png" alt="Reto Escritor">
</div></section>

<section class="wrap sec" id="catalogo">
  <div class="sec-head">
    <div><span class="go-eyebrow">Catálogo</span><h2 class="h-l">Del catálogo</h2></div>
    <div class="go-filter" role="group" aria-label="Filtrar por sello" data-toggle-group>
      <button class="go-filter__tab" aria-pressed="true" data-filter="all">Todos</button><button class="go-filter__tab" aria-pressed="false" data-filter="tucoach">tucoach.go</button><button class="go-filter__tab" aria-pressed="false" data-filter="alita">Alita</button><button class="go-filter__tab" aria-pressed="false" data-filter="reto">Reto Escritor</button><button class="go-filter__tab" aria-pressed="false" data-filter="indep">Independientes</button>
    </div>
  </div>
  <div class="cat-grid" data-flip-grid>
    {"".join(card(k, badge=(k in ("caso-imposible","van-gogh"))) for k in ["caso-imposible","van-gogh","fleur","con-sentido","soledad","anecdotas","lider-coach","21-preguntas","escribir-para-sanar","caso-indefendible"])}
  </div>
  <div style="margin-top:var(--space-7);text-align:center"><a class="link-arrow" href="catalogo.html">Ver los {len(BOOKS)} libros del catálogo {ARROW}</a></div>
</section>

<section class="svc-band sec" id="servicios"><div class="wrap">
  <div class="sec-head">
    <div><span class="go-eyebrow">Servicios editoriales</span><h2 class="h-l">De tu idea <em>a las librerías.</em></h2></div>
    <p class="lede" style="max-width:44ch">Servicios de autopublicación y proyectos editoriales a pedido para empresas. Te acompañamos en cada paso.</p>
  </div>
  <div class="svc-grid">
    <a class="svc svc--feature" href="servicios.html#siete-dias"><div class="svc__top"><span class="svc__icon">{icon("cal")}</span><span class="svc__kind">Programa</span></div>
      <h3>Escribe tu libro profesional en 7 días</h3><p>Tu manuscrito profesional, listo para entrar en proceso de edición.</p>
      <ul><li>Una sesión online de coaching editorial</li><li>Guía para estructurar tu libro</li><li>Técnica y herramientas para tu redacción</li><li>Acompañamiento por WhatsApp</li></ul>
      <div class="svc__foot"><span class="svc__price">US$ 129</span><span class="svc__cta">Agenda tu programa {ARROW}</span></div></a>
    {"".join(svc_card(s) for s in SERVICES)}
  </div>
  <div class="svc-band__foot"><p>¿No sabes por dónde empezar? Escríbenos por WhatsApp y te recomendamos el servicio que necesita tu manuscrito.</p><a class="go-btn btn-on-green go-btn" href="servicios.html">Ver todos los servicios {ARROW}</a></div>
</div></section>

<section class="sunk"><div class="wrap sec spot">
  <div class="big"><div class="go-cover go-cover--tilt"><img src="img/fleur.webp" alt="Portada de Fleur, de Florencia Frezza"><span class="go-cover__glare"></span></div></div>
  <div>
    <span class="go-eyebrow">Libro destacado · Sello Alita</span>
    <blockquote>«Porque los cuentos no son sólo cuentos.»</blockquote>
    <p class="lede">Seguramente conoces el cuento de la zapatilla de cristal, el príncipe y el final feliz. ¿Pero qué pensarías si te dijeran que la historia está mal y que la Cenicienta no es tan buena como parece?</p>
    <dl class="go-colofon"><dt>Autora</dt><dd>Florencia Frezza</dd><dt>ISBN</dt><dd>9807804221</dd><dt>Precio</dt><dd><span class="go-price__ph">[PRECIO]</span></dd></dl>
    <div class="ctas"><button class="go-btn go-btn--primary" data-add data-title="Fleur">Agregar al carrito</button><a class="go-btn go-btn--text" href="libro.html">Leer la sinopsis {ARROW}</a></div>
  </div>
</div></section>

<section class="wrap sec">
  <div class="sec-head"><div><span class="go-eyebrow">Publica con Grupo Olivo</span><h2 class="h-l">Así nace un libro</h2></div><a class="link-arrow" href="servicios.html">Conoce los servicios {ARROW}</a></div>
  <ol class="steps" data-reveal style="list-style:none;padding-left:0;margin:0">
    <li class="step"><span class="step__n">1</span><h3>La idea</h3><p>Una sesión de coaching editorial para encontrar el propósito y la estructura de tu libro.</p><a href="servicios.html#coaching">Coaching editorial</a></li>
    <li class="step"><span class="step__n">2</span><h3>El manuscrito</h3><p>Escribe tu manuscrito profesional con guía, técnica y acompañamiento.</p><a href="servicios.html#siete-dias">Programa de 7 días</a></li>
    <li class="step"><span class="step__n">3</span><h3>Corrección y diseño</h3><p>Corrección de estilo y ortotipográfica, diagramación y portada.</p><a href="servicios.html#correccion">Paquetes</a></li>
    <li class="step"><span class="step__n">4</span><h3>Las librerías</h3><p>Distribución on-demand en 9 países y más de 200 librerías, además de Amazon.</p><a href="servicios.html#distribucion">Distribución</a></li>
  </ol>
</section>

<section class="wrap sec--tight" id="concursos">
  <div class="sec-head"><div><span class="go-eyebrow">Concursos literarios</span><h2 class="h-l">Escribe, <em>participa,</em> publica</h2></div></div>
  <div class="contests" data-reveal>
    <article class="contest"><span class="contest__mark"><img src="img/logo-reto-negro.png" alt="Reto Escritor"></span><div><span class="go-eyebrow go-eyebrow--bare">Mayores de 18 años</span><h3>Reto Escritor</h3><p>Para quienes tienen un testimonio de vida, un evento que les hizo girar 180 grados, y desean dejarlo como legado a sus seres queridos.</p><div class="meta"><span class="go-badge go-badge--success">Libros publicados</span></div><a class="go-btn go-btn--secondary go-btn--sm" href="https://retoescritor.com/concurso/">Ir a retoescritor.com {ARROW}</a></div></article>
    <article class="contest"><span class="contest__mark contest__mark--text">RE</span><div><span class="go-eyebrow go-eyebrow--bare">Jóvenes de 12 a 17 años</span><h3>Reto Expresivo</h3><p>Concurso literario y de dibujo escolar con la misión de promover la creatividad y la lectoescritura en los chicos.</p><div class="meta"><span class="go-badge go-badge--neutral">Antologías 2023 y 2024</span></div><a class="go-btn go-btn--secondary go-btn--sm" href="https://retoexpresivo.com/">Ir a retoexpresivo.com {ARROW}</a></div></article>
  </div>
</section>

<section class="wrap sec">
  <div class="sec-head"><div><span class="go-eyebrow">Autores</span><h2 class="h-l">Las voces del catálogo</h2></div><a class="link-arrow" href="autores.html">Todos los autores {ARROW}</a></div>
  <div class="authors-row" data-reveal>
    {"".join(f'<a class="au" href="autores.html"><img src="img/{img}.webp" alt="" loading="lazy"><b>{n}</b><span>{s}</span></a>' for img,n,s in [("autor-florencia-frezza","Florencia Frezza","Alita"),("autor-jose-custodio","José Custodio Sánchez","Independiente"),("autor-zuleima-virguez","Zuleima Virguez","Reto Escritor"),("autor-jose-esposito","José Espósito","tucoach.go"),("autor-esmeralda-villanueva","Esmeralda Villanueva","Reto Escritor"),("autor-ana-labrador","Ana Andrea Labrador","tucoach.go")])}
  </div>
  <div class="videos">
    {"".join(f'<div class="vid"><img src="media/testimonio-{k}.jpg" alt="" loading="lazy"><button data-src="media/testimonio-{k}.mp4" aria-label="Ver el testimonio de {n}"><span><small>Testimonio en video</small><b>{n}</b></span><span class="play">{icon("play",20)}</span></button></div>' for k,n in [("zuleima","Zuleima Virguez"),("jose-custodio","José Custodio Sánchez Morante"),("esmeralda","Esmeralda Villanueva")])}
  </div>
</section>

<section class="sunk" id="nosotros"><div class="wrap sec about">
  <img src="img/fundadora-adriana.webp" alt="Adriana Mara Olivares" loading="lazy">
  <div><span class="go-eyebrow">Quiénes somos</span>
    <blockquote>«Promovemos el talento de nuevas generaciones de escritores, que viven y crean su propia historia.»</blockquote>
    <p class="lede">Empresa editorial familiar, creada en 2016 en Ciudad Bolívar. Nacimos como una empresa de servicios editoriales para autores independientes; hoy somos una editorial con tres sellos de publicación.</p>
    <div class="facts"><div><b>2016</b><span>Fundada</span></div><div><b>3</b><span>Sellos</span></div><div><b>2018</b><span>Cámara Venezolana del Libro</span></div></div>
  </div>
</div></section>

<section class="wrap sec"><div class="cta-band"><div class="os" aria-hidden="true"><i></i><i></i></div>
  <div><h2>¿Tienes un libro dentro?</h2><p>Cuéntanos en qué etapa está tu manuscrito y te decimos cómo te podemos ayudar.</p></div>
  <div class="actions"><a class="go-btn btn-on-green go-btn" href="servicios.html">Ver servicios</a><a class="go-btn go-btn--secondary" style="color:#fff;border-color:#fff" href="servicios.html#coaching">Agenda una sesión</a></div>
</div></section>
'''
page("index.html", "Grupo Olivo · Inicio", home, flip=True)

# ======================= CATÁLOGO =======================
def cnt(s): return sum(1 for b in BOOKS if b[3]==s)
cat = f'''
<section class="page-head"><div class="wrap">
  <nav class="crumbs" aria-label="Ruta"><a href="index.html">Inicio</a><span>/</span><span>Libros</span></nav>
  <h1 class="h-l">Catálogo</h1><p class="lede">Ficción, testimonio, coaching y no ficción de autores venezolanos. Precios en dólares y en bolívares a la tasa BCV del día.</p>
</div></section>
<div class="wrap cat-layout">
  <aside class="filters" aria-label="Filtros">
    <div><h3>Sello</h3><div class="go-filter" role="group" aria-label="Filtrar por sello" data-toggle-group>
      <button class="go-filter__tab" aria-pressed="true" data-filter="all">Todos<span class="go-filter__count">{len(BOOKS)}</span></button>
      <button class="go-filter__tab" aria-pressed="false" data-filter="tucoach">tucoach.go<span class="go-filter__count">{cnt("tucoach")}</span></button>
      <button class="go-filter__tab" aria-pressed="false" data-filter="alita">Alita<span class="go-filter__count">{cnt("alita")}</span></button>
      <button class="go-filter__tab" aria-pressed="false" data-filter="reto">Reto Escritor<span class="go-filter__count">{cnt("reto")}</span></button>
      <button class="go-filter__tab" aria-pressed="false" data-filter="indep">Independientes<span class="go-filter__count">{cnt("indep")}</span></button></div></div>
    <div class="rest"><h3>Género</h3><label class="check"><input type="checkbox" id="g1"> Novela</label><label class="check"><input type="checkbox" id="g2"> Testimonio</label><label class="check"><input type="checkbox" id="g3"> Coaching y desarrollo</label><label class="check"><input type="checkbox" id="g4"> Romance y fantasía</label></div>
    <div class="rest"><h3>Formato</h3><label class="check"><input type="checkbox" id="f1"> Físico</label><label class="check"><input type="checkbox" id="f2"> Ebook</label></div>
    <div class="rest"><h3>Ofertas</h3><label class="check"><input type="checkbox" id="o1"> Solo libros con descuento</label></div>
  </aside>
  <div>
    <div class="toolbar"><span class="count" data-count>{len(BOOKS)} libros</span>
      <div class="go-field"><label class="go-label" for="ord">Ordenar por</label><select class="go-select" id="ord"><option>Novedades</option><option>Más vendidos</option><option>Precio: menor a mayor</option><option>Título A–Z</option></select></div></div>
    <div class="cat-grid" data-flip-grid>{"".join(card(b[0], badge=(b[0] in ("caso-imposible","van-gogh"))) for b in BOOKS)}</div>
  </div>
</div>'''
page("catalogo.html", "Grupo Olivo · Catálogo", cat, flip=True)

# ======================= LIBRO =======================
libro = f'''
<div class="wrap" style="padding-top:var(--space-5)"><nav class="crumbs" aria-label="Ruta"><a href="index.html">Inicio</a><span>/</span><a href="catalogo.html">Libros</a><span>/</span><a href="autores.html">Alita</a><span>/</span><span>Fleur</span></nav></div>
<section class="wrap book-hero">
  <div class="big"><div class="go-cover go-cover--tilt"><img src="img/fleur.webp" alt="Portada de Fleur, de Florencia Frezza"><span class="go-cover__glare"></span></div></div>
  <div>
    <span class="go-eyebrow">Sello Alita · Romance y fantasía</span>
    <h1>Fleur</h1>
    <p class="by">de <a href="autores.html">Florencia Frezza</a></p>
    <span class="go-stars" aria-label="Sin reseñas todavía"><span class="go-stars__row" style="--value:0" aria-hidden="true"><span class="go-stars__fill"></span></span>Sin reseñas todavía · <a href="#resenas" style="color:var(--accent)">Escribe la primera</a></span>
    <div class="buy">
      <div class="formats" role="group" aria-label="Formato" data-toggle-group><button aria-pressed="true">Libro físico<small>[PRECIO]</small></button><button aria-pressed="false">Ebook<small>[PRECIO]</small></button></div>
      <div class="buy__row"><span class="go-price go-price--lg"><span class="go-price__usd">US$ <span class="go-price__ph">[PRECIO]</span></span><span class="go-price__ves">Bs [tasa BCV del día]</span></span>
        <div style="display:flex;gap:var(--space-3);flex-wrap:wrap"><button class="go-btn go-btn--primary" data-add data-title="Fleur">Agregar al carrito</button></div></div>
      <div class="buy__ships">{icon("truck",18)} Envíos a toda Venezuela y Latinoamérica · Pago Móvil, Zelle, Binance Pay, transferencia o PayPal</div>
      <a class="go-btn go-btn--text" href="https://www.amazon.com/dp/9807804221" style="justify-self:start">También disponible en Amazon {ARROW}</a>
    </div>
    <div class="synopsis">
      <p>Seguramente conoces el cuento de la zapatilla de cristal, el príncipe y el final feliz. ¿Pero qué pensarías si te dijeran que la historia está mal y que la Cenicienta no es tan buena como parece?</p>
      <p>Cuando la hija bastarda del duque de Geal llega al hogar de los Blanchett, la vida de Fleur da un giro completo y comienza a perderlo todo: su familia, su prometido y el destino para el cual fue preparada. Acusada de traición, acaba quemada en la hoguera, pero ese no fue el final. Al sonar la doceava campanada, las manecillas del reloj retrocedieron.</p>
      <p class="pull">«—Nos encontramos de nuevo en esta vida, ¿ahora sí serás mi esposa?»</p>
      <p>Entre intrigas y secretos, Fleur lucha por cambiar la historia y buscar a aquel que lleva escrito en la piel.</p>
    </div>
    <dl class="go-colofon" style="margin-top:var(--space-6)"><dt>Título</dt><dd>Fleur</dd><dt>Autora</dt><dd>Florencia Frezza</dd><dt>Sello</dt><dd>Alita</dd><dt>ISBN</dt><dd>9807804221</dd><dt>Páginas</dt><dd><span class="go-price__ph">[PÁGINAS]</span></dd></dl>
  </div>
</section>
<section class="sunk"><div class="wrap sec--tight">
  <article class="go-author" style="max-width:720px"><img class="go-author__photo" src="img/autor-florencia-frezza.webp" alt="Florencia Frezza"><div><span class="go-eyebrow go-eyebrow--bare">Sobre la autora</span><h2 class="go-author__name">Florencia Frezza</h2><p class="go-author__bio">Escribe desde 2016 con el pseudónimo de Flor. Estudiante de Letras en la Universidad Nacional del Litoral, en Argentina; sus primeras publicaciones estuvieron en Wattpad y Fanfiction, y su estilo se inspira en la épica y los clásicos literarios. Autora de Fleur y de La dama negra.</p><div class="go-author__links"><a href="autores.html">Ver sus libros</a></div></div></article>
</div></section>
<section class="wrap sec" id="resenas">
  <div class="reviews">
    <div class="rating-sum"><span class="go-eyebrow">Reseñas</span><b>—</b><span class="go-stars"><span class="go-stars__row" style="--value:0" aria-hidden="true"><span class="go-stars__fill"></span></span>0 reseñas</span>
      <div class="bars" aria-hidden="true">{"".join(f'<div>{n}★<i style="--w:0%"></i>0</div>' for n in (5,4,3,2,1))}</div>
      <p style="font-size:14.5px;color:var(--ink-muted);margin:0">Solo quienes compraron el libro pueden reseñarlo.</p></div>
    <div>
      <div class="go-empty" style="padding:var(--space-6) 0;margin:0;justify-items:start;text-align:left;max-width:none">
        <h3 class="go-empty__title">Sé la primera persona en reseñar Fleur</h3>
        <p class="go-empty__text">¿Ya lo leíste? Cuéntale a otros lectores qué te pareció.</p>
        <div class="go-stars go-stars--input" role="group" aria-label="Tu calificación" data-toggle-group><button aria-pressed="false" aria-label="1 estrella">★</button><button aria-pressed="false" aria-label="2 estrellas">★</button><button aria-pressed="false" aria-label="3 estrellas">★</button><button aria-pressed="false" aria-label="4 estrellas">★</button><button aria-pressed="false" aria-label="5 estrellas">★</button></div>
        <div class="go-field" style="width:100%;max-width:560px"><label class="go-label" for="rev">Tu reseña</label><textarea class="go-input" id="rev" rows="4" style="padding:12px 16px;min-height:120px" placeholder="Lo que más te gustó, lo que no, a quién se lo recomendarías…"></textarea></div>
        <button class="go-btn go-btn--primary">Publicar reseña</button>
      </div>
    </div>
  </div>
</section>
<section class="wrap sec" style="padding-top:0">
  <div class="sec-head"><div><span class="go-eyebrow">También te puede gustar</span><h2 class="h-m">Más de Alita y otros sellos</h2></div><a class="link-arrow" href="catalogo.html">Ver catálogo {ARROW}</a></div>
  <div class="rail">{"".join(card(k) for k in ["21-preguntas","van-gogh","por-si-me-muero","caso-imposible","anecdotas","soledad"])}</div>
</section>'''
page("libro.html", "Fleur · Grupo Olivo", libro)

# ======================= SERVICIOS =======================
def detail(id_, kind, title, price, price_note, paras, inc=None, extra="", cta="Agenda una sesión", cta2=None):
    incl = f'<ul class="inc">{"".join(f"<li>{x}</li>" for x in inc)}</ul>' if inc else ""
    c2 = f'<a class="go-btn go-btn--text" href="#">{cta2}</a>' if cta2 else ""
    return f'''<article class="svc-detail" id="{id_}" data-reveal>
  <div><span class="go-eyebrow">{kind}</span><h2>{title}</h2><div class="price-big">{price}<small>{price_note}</small></div></div>
  <div class="body">{"".join(f"<p>{p}</p>" for p in paras)}{incl}{extra}
    <div style="display:flex;gap:var(--space-3);flex-wrap:wrap;align-items:center"><a class="go-btn go-btn--primary" href="#">{cta} {ARROW}</a>{c2}</div></div>
</article>'''
serv = f'''
<section class="wrap svc-hero">
  <div><nav class="crumbs" aria-label="Ruta"><a href="index.html">Inicio</a><span>/</span><span>Servicios editoriales</span></nav>
    <h1 class="h-xl" style="margin:var(--space-4) 0 var(--space-5)">Tu libro, <em>de la idea a las librerías.</em></h1>
    <p class="lede">Servicios editoriales de autopublicación y creación de proyectos editoriales a pedido para empresas. Nacimos como una empresa de servicios para autores independientes: es lo que mejor sabemos hacer.</p></div>
  <div class="stats"><div><b>6</b><span>servicios para cada etapa del libro</span></div><div><b>9</b><span>países con distribución</span></div><div><b>200+</b><span>librerías en la red</span></div></div>
</section>
<nav class="svc-nav" aria-label="Servicios"><div class="wrap" style="display:flex;gap:6px;flex-wrap:inherit"><a class="go-filter__tab" style="display:inline-flex;align-items:center;text-decoration:none" href="#coaching">Coaching</a><a class="go-filter__tab" style="display:inline-flex;align-items:center;text-decoration:none" href="#siete-dias">7 días</a><a class="go-filter__tab" style="display:inline-flex;align-items:center;text-decoration:none" href="#correccion">Corrección</a><a class="go-filter__tab" style="display:inline-flex;align-items:center;text-decoration:none" href="#diseno">Diseño</a><a class="go-filter__tab" style="display:inline-flex;align-items:center;text-decoration:none" href="#escala">Escala como autor</a><a class="go-filter__tab" style="display:inline-flex;align-items:center;text-decoration:none" href="#distribucion">Distribución</a></div></nav>
<div class="wrap">
{detail("coaching","Sesión 1:1 · 45 minutos","Coaching editorial","US$ 97","por sesión",["Sesión de coaching para descubrir ideas potenciales de libros, desatar nudos creativos, encontrar el propósito de tu libro y generar la estructura para escribirlo."],cta="Agenda una sesión")}
{detail("siete-dias","Programa","Escribe tu libro profesional en 7 días","US$ 129","el programa",["Programa para escribir tu manuscrito profesional, listo para entrar en proceso de edición de tu libro."],inc=["Una sesión online de coaching editorial","Guía para estructurar tu libro","Técnica y herramientas para accionar tu redacción","Comunicación por WhatsApp para dudas durante el programa"],cta="Agenda tu programa")}
{detail("correccion","Paquete","Corrección","Cotiza","según tu manuscrito",["Revisión de contenido, corrección de estilo y ortotipográfica, para mejorar tus posibilidades de éxito en concursos literarios, postulaciones a editoriales especializadas e inicio de procesos de autopublicación."],cta="Pide tu cotización por WhatsApp")}
{detail("diseno","Paquete","Diseño","Cotiza","según tu proyecto",["Diagramación, corrección ortotipográfica y diseño de portada para proyectos de autopublicación de ficción y no ficción."],cta="Pide tu cotización por WhatsApp")}
{detail("escala","Programa · 12 semanas","Escala como autor","12","semanas de acompañamiento",["Acompañamiento para coaches, profesionales especialistas y conferencistas que desean publicar su primer libro de no ficción, escalar su autoridad y conectar a otro nivel con sus lectores."],cta="Más información")}
{detail("distribucion","Para autores independientes","Distribución on-demand","200+","librerías",["Si tienes el 100 % de los derechos de tu obra, sus artes finales para impresión, y necesitas más puntos de venta además de Amazon, este servicio es para ti. Distribuimos los metadatos de tu libro físico para que esté disponible en estos países:"],inc=["Envío más barato para los lectores de cada país","Una red de más de 200 librerías","Seguimiento e informe semestral de tus ventas"],extra='<div class="countries">'+"".join(f"<span>{c}</span>" for c in ["Argentina","Brasil","Colombia","Chile","Ecuador","España","México","Perú","Uruguay"])+'</div>',cta="Pide información por WhatsApp",cta2="Ver librerías por país")}
</div>
<section class="sunk"><div class="wrap sec">
  <div class="sec-head"><div><span class="go-eyebrow">Libros que nacieron aquí</span><h2 class="h-l">Autores que ya publicaron</h2></div><a class="link-arrow" href="catalogo.html">Ver catálogo {ARROW}</a></div>
  <div class="rail">{"".join(card(k) for k in ["con-sentido","lider-coach","horror-emprender","poder-del-fee","errores-clinicos","a-quien"])}</div>
</div></section>
<section class="wrap sec"><div class="cta-band"><div class="os" aria-hidden="true"><i></i><i></i></div>
  <div><h2>Proyectos editoriales para empresas</h2><p>Creamos libros a pedido para organizaciones: desde la idea hasta el libro impreso.</p></div>
  <div class="actions"><a class="go-btn btn-on-green go-btn" href="#">Escríbenos</a></div></div></section>'''
page("servicios.html", "Servicios editoriales · Grupo Olivo", serv)

# ======================= AUTORES Y SELLOS =======================
def acard(img, sello, name, bio):
    return f'<article class="go-author"><img class="go-author__photo" src="img/{img}.webp" alt="{name}" loading="lazy"><div><span class="go-eyebrow go-eyebrow--bare">{sello}</span><h3 class="go-author__name">{name}</h3><p class="go-author__bio">{bio}</p><div class="go-author__links"><a href="catalogo.html">Ver sus libros</a></div></div></article>'
aut = f'''
<section class="page-head"><div class="wrap">
  <nav class="crumbs" aria-label="Ruta"><a href="index.html">Inicio</a><span>/</span><span>Autores y sellos</span></nav>
  <h1 class="h-l">Autores y sellos</h1><p class="lede">Hoy somos una editorial con tres sellos de publicación y autores independientes, creciendo para llevar más libros de Venezuela al mundo.</p>
</div></section>
<div class="wrap">
<section class="sello-block"><div><img class="logo" src="img/logo-tucoach.png" alt="tucoach.go"><h2>tucoach.go</h2><p>Coaching, liderazgo y desarrollo profesional.</p></div>
  <div class="authors-grid" data-reveal>{acard("autor-jose-esposito","tucoach.go","José Espósito","Coach organizacional, conferencista y empresario, CEO de Grupo Con Sentido Internacional. Escribe sobre el coaching como herramienta organizacional, propósito de vida y autoconocimiento.")}{acard("autor-ana-labrador","tucoach.go","Ana Andrea Labrador","Venezolana radicada en Canadá, con experticia en coaching corporal y ontológico; conferencista y facilitadora organizacional.")}</div></section>
<section class="sello-block"><div><img class="logo" src="img/logo-alita.png" alt="Alita"><h2>Alita</h2><p>Romance, fantasía y acción.</p></div>
  <div class="authors-grid" data-reveal>{acard("autor-florencia-frezza","Alita","Florencia Frezza","Escribe desde 2016 con el pseudónimo de Flor. Autora de Fleur, que reinterpreta la Cenicienta desde la perspectiva de su hermanastra, y de La dama negra.")}{acard("autor-jemmy-lee","Alita","Jemmy Lee Carvajal","Conocida como CherryLeeUp, pasó del mundo de la química a la novela en 2017. Su estilo se destaca en la fantasía, el romance y la acción. Autora de El príncipe de la máscara.")}</div></section>
<section class="sello-block"><div><img class="logo reto" src="img/logo-reto-negro.png" alt="Reto Escritor"><h2>Reto Escritor</h2><p>Testimonios de vida que se convierten en legado.</p></div>
  <div class="authors-grid" data-reveal>{acard("autor-zuleima-virguez","Reto Escritor","Zuleima Virguez","Docente y magíster en Orientación de la conducta. Se ha formado como coach y en mindfulness. Autora de Soledad, ¿una cura o locura?")}{acard("autor-esmeralda-villanueva","Reto Escritor","Esmeralda Villanueva","Finalista de Reto Escritor Vol. II. Coautora de un libro que une las cartas de su padre, mecánico militar de la aviación en la Guerra Civil española, con su propio relato.")}{acard("autor-lissette","Reto Escritor","Lissette Van Der Biest","Más de dieciséis años en el área financiera, alternando su pasión por la poesía, el cuento, la novela y la dramaturgia. Autora de Anécdotas de una viajera del tercer mundo.")}{acard("autor-mariene","Reto Escritor","Mariene Piñero","Autora de Descubre lo extraordinario en ti.")}</div></section>
<section class="sello-block"><div><h2>Independientes</h2><p>Novela negra, historia del arte y no ficción.</p></div>
  <div class="authors-grid" data-reveal>{acard("autor-jose-custodio","Independiente","José Custodio Sánchez Morante","Abogado penal, profesor universitario y conferencista. Autor de la novela negra Un caso indefendible, inspirada en hechos reales de su ejercicio en tribunales.")}{acard("fundadora-adriana","Independiente","Adriana Mara Olivares","Empresaria, coach ejecutiva, comunicadora social y editora. Autora de A quién le escribes, coeditado con AB Ediciones de la UCAB.")}</div></section>
</div>'''
page("autores.html", "Autores y sellos · Grupo Olivo", aut)

# ======================= COMUNIDAD =======================
THREADS = [("¿Qué están leyendo este mes?","Comparte el libro que tienes en la mesa de noche y qué te está pareciendo.",["General"],24,"M"),
 ("Club de lectura: Fleur","Hablemos de la reinterpretación de la Cenicienta. Spoilers marcados.",["Club de lectura","Alita"],41,"A"),
 ("Novela negra venezolana: recomendaciones","Después de Un caso indefendible, ¿qué otras novelas de tribunales recomiendan?",["Recomendaciones"],13,"J"),
 ("Me estoy preparando para Reto Escritor","¿Alguien que haya participado puede contar cómo fue el proceso?",["Concursos"],9,"L"),
 ("Escribir para sanar: ¿qué historia les tocó más?","Un hilo para hablar de los testimonios de la antología.",["Reto Escritor"],17,"C")]
com = f'''
<section class="page-head"><div class="wrap">
  <nav class="crumbs" aria-label="Ruta"><a href="index.html">Inicio</a><span>/</span><span>Comunidad</span></nav>
  <div class="sec-head" style="margin:0"><div><h1 class="h-l">Comunidad de lectores</h1><p class="lede">Comenta, recomienda y comparte tus libros favoritos con otros lectores.</p></div><a class="go-btn go-btn--primary" href="#">Abrir un hilo</a></div>
</div></section>
<div class="wrap" style="padding-top:var(--space-5)"><div class="example-note">Hilos y nombres de ejemplo: el foro se llena con lo que publiquen los lectores.</div></div>
<div class="wrap forum">
  <div>
    <div class="go-filter" role="group" aria-label="Ordenar hilos" data-toggle-group style="margin-bottom:var(--space-3)"><button class="go-filter__tab" aria-pressed="true">Recientes</button><button class="go-filter__tab" aria-pressed="false">Más comentados</button><button class="go-filter__tab" aria-pressed="false">Clubes de lectura</button></div>
    {"".join(f'<a class="thread" href="#hilo"><span class="go-review__avatar" aria-hidden="true">{av}</span><div><h3>{t}</h3><p>{d}</p><div class="tags">{"".join(f"<span class=\"go-badge go-badge--neutral\">{g}</span>" for g in tags)}</div></div><span class="cnt"><b>{c}</b>respuestas</span></a>' for t,d,tags,c,av in THREADS)}
    <section id="hilo" style="margin-top:var(--space-8)">
      <span class="go-eyebrow">Hilo abierto · Club de lectura</span><h2 class="h-m" style="margin:var(--space-3) 0 var(--space-5)">Club de lectura: Fleur</h2>
      <div class="post"><span class="go-review__avatar">A</span><div><div class="who">Lectora de ejemplo<small>hace 2 días</small></div><p>Me encantó que la historia se cuente desde la hermanastra. ¿En qué momento cambiaron de opinión sobre la Cenicienta?</p></div></div>
      <div class="post"><span class="go-review__avatar">M</span><div><div class="who">Lector de ejemplo<small>hace 1 día</small></div><p>Para mí fue con la campanada. Desde ahí todo lo que creía saber del cuento se dio vuelta.</p></div></div>
      <div class="go-field" style="margin-top:var(--space-5)"><label class="go-label" for="reply">Tu respuesta</label><textarea class="go-input" id="reply" rows="3" style="padding:12px 16px;min-height:100px" placeholder="Escribe con respeto: aquí todos somos lectores."></textarea></div>
      <button class="go-btn go-btn--primary" style="margin-top:var(--space-3)">Responder</button>
    </section>
  </div>
  <aside>
    <div class="side-box"><h3>Club de lectura del mes</h3><div class="mini-books"><a href="libro.html"><img src="img/fleur.webp" alt=""><span>Fleur<small>Florencia Frezza</small></span></a></div></div>
    <div class="side-box"><h3>Lo más comentado</h3><div class="mini-books">{"".join(f'<a href="libro.html"><img src="img/{k}.webp" alt=""><span>{B[k][1]}<small>{B[k][2]}</small></span></a>' for k in ["caso-indefendible","escribir-para-sanar","soledad"])}</div></div>
    <div class="side-box"><h3>Normas</h3><p style="margin:0;font-size:14.5px;color:var(--ink-muted)">Respeto ante todo. Marca los spoilers. Los moderadores de Grupo Olivo pueden ocultar mensajes que no cumplan las normas.</p></div>
  </aside>
</div>'''
page("comunidad.html", "Comunidad · Grupo Olivo", com)

# ======================= CHECKOUT =======================
line = lambda k: f'<li class="go-line"><img src="img/{k}.webp" alt=""><div><p class="go-line__title">{B[k][1]}</p><span class="go-line__meta">{B[k][2]} · 1 ud.</span></div><span class="go-price"><span class="go-price__usd"><span class="go-price__ph">[PRECIO]</span></span></span></li>'
co = f'''
<section class="page-head" style="padding-block:var(--space-6) var(--space-5)"><div class="wrap">
  <h1 class="h-m">Finaliza tu compra</h1>
  <div class="steps-bar" style="margin-top:var(--space-4)"><span class="done" data-n="1">Carrito</span><span class="on" data-n="2"><b>Datos y pago</b></span><span data-n="3">Comprobante</span></div>
</div></section>
<div class="wrap co">
  <div>
    <section><h2>Tus datos</h2><div class="fgrid">
      <div class="go-field"><label class="go-label" for="n">Nombre y apellido</label><input class="go-input" id="n" autocomplete="name"></div>
      <div class="go-field"><label class="go-label" for="ci">Cédula o documento</label><input class="go-input" id="ci" placeholder="V-00.000.000"></div>
      <div class="go-field"><label class="go-label" for="em">Correo electrónico</label><input class="go-input" id="em" type="email" autocomplete="email"><span class="go-help">Te enviamos la confirmación del pedido aquí.</span></div>
      <div class="go-field"><label class="go-label" for="tel">Teléfono (WhatsApp)</label><input class="go-input" id="tel" type="tel" autocomplete="tel" placeholder="+58 414 000 0000"></div>
    </div></section>
    <section><h2>Envío</h2><div class="fgrid">
      <div class="go-field"><label class="go-label" for="pais">País</label><select class="go-select" id="pais"><option>Venezuela</option><option>Argentina</option><option>Chile</option><option>Colombia</option><option>Ecuador</option><option>México</option><option>Perú</option><option>Uruguay</option></select></div>
      <div class="go-field"><label class="go-label" for="edo">Estado</label><select class="go-select" id="edo"><option>Distrito Capital</option><option>Bolívar</option><option>Miranda</option><option>Zulia</option><option>Carabobo</option></select></div>
      <div class="go-field full"><label class="go-label" for="dir">Dirección o agencia de envío</label><input class="go-input" id="dir" autocomplete="street-address"></div>
    </div></section>
    <section><fieldset class="go-pay"><legend><h2 style="margin:0">Método de pago</h2></legend>
      <label class="go-pay__opt"><input type="radio" name="pm" checked><span><span class="go-pay__name">Pago Móvil</span><span class="go-pay__desc">Envía el pago y sube tu comprobante.</span></span><span class="go-pay__tag">Venezuela</span>
        <div class="go-pay__details"><dl><dt>Banco</dt><dd>[BANCO]</dd><dt>Teléfono</dt><dd>[TELÉFONO]</dd><dt>RIF / C.I.</dt><dd>[RIF]</dd><dt>Monto</dt><dd>Bs [monto a tasa BCV]</dd></dl></div></label>
      <label class="go-pay__opt"><input type="radio" name="pm"><span><span class="go-pay__name">Transferencia bancaria</span><span class="go-pay__desc">Transfiere y sube tu comprobante.</span></span><span class="go-pay__tag">Venezuela</span>
        <div class="go-pay__details"><dl><dt>Banco</dt><dd>[BANCO]</dd><dt>Cuenta</dt><dd>[NÚMERO DE CUENTA]</dd><dt>Titular</dt><dd>[TITULAR]</dd></dl></div></label>
      <label class="go-pay__opt"><input type="radio" name="pm"><span><span class="go-pay__name">Zelle</span><span class="go-pay__desc">Paga en dólares y sube tu comprobante.</span></span><span class="go-pay__tag">USD</span>
        <div class="go-pay__details"><dl><dt>Correo</dt><dd>[CORREO ZELLE]</dd><dt>Titular</dt><dd>[TITULAR]</dd></dl></div></label>
      <label class="go-pay__opt"><input type="radio" name="pm"><span><span class="go-pay__name">Binance Pay</span><span class="go-pay__desc">Paga con USDT y sube tu comprobante.</span></span><span class="go-pay__tag">USDT</span>
        <div class="go-pay__details"><dl><dt>Pay ID</dt><dd>[BINANCE PAY ID]</dd></dl></div></label>
      <label class="go-pay__opt"><input type="radio" name="pm"><span><span class="go-pay__name">PayPal</span><span class="go-pay__desc">Pago automático, se confirma al instante.</span></span><span class="go-pay__tag">Latinoamérica</span></label>
    </fieldset></section>
    <a class="go-btn go-btn--primary go-btn--block" href="pedido.html" style="margin-top:var(--space-6)">Confirmar pedido y subir comprobante {ARROW}</a>
  </div>
  <aside class="summary"><h2 class="h-m" style="font-size:26px;margin-bottom:var(--space-3)">Tu pedido</h2>
    <ul style="list-style:none;margin:0;padding:0">{line("fleur")}{line("con-sentido")}</ul>
    <div style="margin-top:var(--space-4)"><div class="sum-row"><span>Subtotal</span><span class="ph">[PRECIO]</span></div><div class="sum-row"><span>Envío</span><span style="color:var(--ink-muted)">Se calcula con tu dirección</span></div>
    <div class="sum-row total"><span>Total</span><span class="go-price" style="align-items:end"><span class="go-price__usd"><span class="go-price__ph">[PRECIO]</span></span><span class="go-price__ves">Bs [tasa BCV del día]</span></span></div></div>
    <div class="go-field" style="margin-top:var(--space-5)"><label class="go-label" for="cup">Código de descuento</label><div style="display:flex;gap:8px"><input class="go-input" id="cup"><button class="go-btn go-btn--secondary">Aplicar</button></div></div>
  </aside>
</div>'''
page("checkout.html", "Checkout · Grupo Olivo", co)

# ======================= PEDIDO =======================
ped = f'''
<section class="page-head" style="padding-block:var(--space-6) var(--space-5)"><div class="wrap">
  <span class="go-eyebrow">Pedido de ejemplo · GO-0000</span><h1 class="h-m" style="margin-top:var(--space-3)">Gracias por tu compra</h1>
  <p class="lede" style="margin-top:var(--space-3)">Sube el comprobante de tu Pago Móvil para que podamos verificarlo. Te avisamos por correo en cada paso.</p>
</div></section>
<div class="wrap order">
  <div>
    <div class="order-card"><div style="display:flex;justify-content:space-between;align-items:center;gap:var(--space-3);flex-wrap:wrap;margin-bottom:var(--space-5)"><h2 class="h-m" style="font-size:26px">Estado</h2><span class="go-badge go-badge--warning">Pendiente de verificación</span></div>
      <ol class="go-timeline">
        <li class="go-step go-step--done"><span class="go-step__dot" aria-hidden="true">✓</span><div><p class="go-step__title">Pedido recibido</p><p class="go-step__meta">Recibimos tu pedido y los datos de envío.</p></div></li>
        <li class="go-step go-step--current" aria-current="step"><span class="go-step__dot" aria-hidden="true"></span><div><p class="go-step__title">Pendiente de verificación</p><p class="go-step__meta">Cuando subas el comprobante, confirmamos tu pago con el banco.</p></div></li>
        <li class="go-step go-step--todo"><span class="go-step__dot" aria-hidden="true"></span><div><p class="go-step__title">Pago aprobado</p></div></li>
        <li class="go-step go-step--todo"><span class="go-step__dot" aria-hidden="true"></span><div><p class="go-step__title">Enviado</p></div></li>
      </ol></div>
    <div class="order-card"><h2 class="h-m" style="font-size:26px;margin-bottom:var(--space-5)">Sube tu comprobante</h2>
      <div class="go-upload">
        <div class="go-field"><label class="go-label" for="ref">Número de referencia</label><input class="go-input" id="ref" inputmode="numeric" placeholder="Ej. 004512903381"><span class="go-help">Lo encuentras en el comprobante de tu banco.</span></div>
        <label class="go-drop" for="file"><input id="file" type="file" accept="image/*,application/pdf" style="position:absolute;opacity:0;width:1px;height:1px">
          <svg width="28" height="28" viewBox="0 0 28 28" fill="none" aria-hidden="true"><path d="M14 19V6m0 0-5 5m5-5 5 5M5 20v3h18v-3" stroke="currentColor" stroke-width="1.6" style="color:var(--accent)"/></svg>
          <span class="go-drop__title">Sube la captura del comprobante</span><span class="go-drop__hint">JPG, PNG o PDF, hasta 5 MB. Arrástrala aquí o toca para elegirla.</span></label>
        <button class="go-btn go-btn--primary go-btn--block">Enviar comprobante</button>
      </div></div>
  </div>
  <aside>
    <div class="order-card"><h3 class="h-m" style="font-size:22px;margin-bottom:var(--space-4)">Datos para pagar</h3>
      <dl class="kv"><dt>Método</dt><dd>Pago Móvil</dd><dt>Banco</dt><dd>[BANCO]</dd><dt>Teléfono</dt><dd>[TELÉFONO]</dd><dt>RIF / C.I.</dt><dd>[RIF]</dd><dt>Monto</dt><dd>Bs [monto a tasa BCV]</dd></dl></div>
    <div class="order-card"><h3 class="h-m" style="font-size:22px;margin-bottom:var(--space-2)">Tu pedido</h3><ul style="list-style:none;margin:0;padding:0">{line("fleur")}{line("con-sentido")}</ul></div>
    <p style="font-size:14px;color:var(--ink-muted);margin-top:var(--space-4)">¿Dudas con tu pedido? Escríbenos a editorialgrupoolivo@gmail.com o al +58 414 8680195.</p>
  </aside>
</div>'''
page("pedido.html", "Estado del pedido · Grupo Olivo", ped)

# ======================= ADMIN =======================
ROWS = [("GO-0041","Cliente de ejemplo 1","Pago Móvil","004512903381","Bs [monto]","warning","Pendiente"),
 ("GO-0040","Cliente de ejemplo 2","Zelle","ZL-88213","US$ [monto]","warning","Pendiente"),
 ("GO-0039","Cliente de ejemplo 3","Binance Pay","BP-551902","USDT [monto]","warning","Pendiente"),
 ("GO-0038","Cliente de ejemplo 4","Transferencia","0102-77341","Bs [monto]","success","Aprobado"),
 ("GO-0037","Cliente de ejemplo 5","PayPal","Automático","US$ [monto]","success","Aprobado"),
 ("GO-0036","Cliente de ejemplo 6","Pago Móvil","004511007220","Bs [monto]","danger","Rechazado")]
adm = f'''
<div class="admin">
  <nav aria-label="Administración"><a href="#">Resumen</a><a href="#">Libros</a><a href="#">Pedidos</a><a href="#" aria-current="page">Pagos por confirmar <span class="n">3</span></a><a href="#">Descuentos</a><a href="#">Barra promocional</a><a href="#">Moderación</a><a href="#">Tasa BCV</a></nav>
  <main>
    <div class="example-note">Panel de ejemplo: pedidos, clientes y montos son de muestra.</div>
    <div class="sec-head" style="margin:var(--space-5) 0 0"><div><span class="go-eyebrow">Administración</span><h1 class="h-m" style="margin-top:var(--space-3)">Pagos por confirmar</h1></div>
      <div class="go-field" style="flex-direction:row;align-items:center;gap:var(--space-3)"><label class="go-label" for="fm">Método</label><select class="go-select" id="fm" style="min-height:40px;width:auto"><option>Todos</option><option>Pago Móvil</option><option>Transferencia</option><option>Zelle</option><option>Binance Pay</option></select></div></div>
    <div class="kpis"><div class="kpi"><span>Por confirmar</span><b>3</b></div><div class="kpi"><span>Aprobados hoy</span><b>—</b></div><div class="kpi"><span>Tasa BCV</span><b style="font-size:24px">[TASA]</b></div><div class="kpi"><span>Actualizada</span><b style="font-size:24px">06:00</b></div></div>
    <div class="table-wrap"><table class="t"><thead><tr><th>Pedido</th><th>Cliente</th><th>Método</th><th>Referencia</th><th>Monto</th><th>Estado</th></tr></thead>
      <tbody data-rows>{"".join(f'<tr data-order="{o}" aria-selected="{"true" if i==0 else "false"}" style="cursor:pointer"><td class="mono">{o}</td><td class="who"><b>{c}</b><small>2 libros</small></td><td>{m}</td><td class="mono">{r}</td><td class="mono">{a}</td><td><span class="go-badge go-badge--{s}">{st}</span></td></tr>' for i,(o,c,m,r,a,s,st) in enumerate(ROWS))}</tbody></table></div>
    <section class="review-pane">
      <div class="proof">Captura del comprobante<br>que subió el cliente</div>
      <div><span class="go-eyebrow">Revisando</span><h2 class="h-m" style="font-size:30px;margin:var(--space-3) 0 var(--space-4)">Pedido <span data-sel-order>GO-0041</span></h2>
        <dl class="kv"><dt>Método</dt><dd>Pago Móvil</dd><dt>Referencia</dt><dd>004512903381</dd><dt>Monto esperado</dt><dd>Bs [monto a tasa BCV]</dd><dt>Libros</dt><dd>Fleur · Con sentido</dd><dt>Envío</dt><dd>Distrito Capital, Venezuela</dd></dl>
        <div class="go-field" style="margin-top:var(--space-5)"><label class="go-label" for="note">Nota para el cliente (opcional)</label><input class="go-input" id="note" placeholder="Ej. el monto no coincide con el pedido"></div>
        <div class="decide"><button class="go-btn go-btn--primary">Aprobar pago</button><button class="go-btn btn-danger">Rechazar</button></div>
        <p class="go-help" style="margin-top:var(--space-3)">Al aprobar, el cliente recibe un correo y el pedido pasa a «Pago aprobado».</p></div>
    </section>
  </main>
</div>'''
page("admin.html", "Admin · Pagos por confirmar", adm, admin=True)
print("ok", len(PAGES), "páginas")
