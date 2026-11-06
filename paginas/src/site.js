(function(){
const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
const fine = matchMedia('(hover:hover) and (pointer:fine)').matches;
const hasG = !!window.gsap && !reduce;
const $ = (s, r=document) => r.querySelector(s), $$ = (s, r=document) => [...r.querySelectorAll(s)];

/* cart count, remembered per viewer */
let n = 2; try { const s = localStorage.getItem('go-cart'); if (s !== null) n = +s || 0; } catch(e) {}
const counts = () => $$('.go-cart-btn__n');
const paint = () => counts().forEach(c => c.textContent = n);
paint();
function bump(){ n++; try{localStorage.setItem('go-cart', n)}catch(e){} paint();
  if (hasG) counts().forEach(c => gsap.fromTo(c, {scale:1.7}, {scale:1, duration:.6, ease:'elastic.out(1,.4)'})); }

/* toast */
function toast(img, title, text){
  let host = $('.toast-host'); if (!host){ host = document.createElement('div'); host.className = 'toast-host go-root'; document.body.appendChild(host); }
  host.innerHTML = `<div class="go-toast go-toast--success" role="status">${img?`<img src="${img}" alt="">`:'<span class="go-toast__icon">✓</span>'}<div><p class="go-toast__title">${title}</p><p class="go-toast__text">${text}</p></div><a class="go-toast__action" href="checkout.html">Ver carrito</a></div>`;
  const t = host.firstElementChild;
  if (hasG) gsap.from(t, {y:16, opacity:0, duration:.35, ease:'power3.out'});
  clearTimeout(host._t); host._t = setTimeout(() => { if (hasG) gsap.to(t, {opacity:0, y:8, duration:.3, onComplete:()=>t.remove()}); else t.remove(); }, 4000);
}

/* add to cart: the cover flies to the cart */
document.addEventListener('click', e => {
  const b = e.target.closest('[data-add]'); if (!b) return;
  e.preventDefault();
  const scope = b.closest('.go-book, .spot, .book-hero, .svc') || document;
  const img = $('img', scope); const title = b.dataset.title || ($('.go-book__title', scope)||{}).textContent || 'Libro';
  const cart = $('.site-head .go-cart-btn');
  if (!hasG || !img || !cart){ bump(); toast(img && img.src, 'Agregado al carrito', title); return; }
  const r = img.getBoundingClientRect(), c = cart.getBoundingClientRect();
  const fl = img.cloneNode(); fl.className = 'flyer';
  Object.assign(fl.style, {left:r.left+'px', top:r.top+'px', width:r.width+'px', height:r.height+'px', objectFit:'cover'});
  document.body.appendChild(fl);
  gsap.to(fl, {x:c.left+c.width/2-r.left-r.width/2, y:c.top+c.height/2-r.top-r.height/2, scale:.08, rotation:-14, duration:.9, ease:'power3.in',
    onComplete:()=>{ fl.remove(); bump(); toast(img.src, 'Agregado al carrito', title.trim()); }});
});

/* mobile menu */
const mm = $('#mmenu');
$$('[data-menu-open]').forEach(b => b.addEventListener('click', () => { mm.hidden = false; $('a', mm).focus(); }));
$$('[data-menu-close]').forEach(b => b.addEventListener('click', () => { mm.hidden = true; }));
if (mm) mm.addEventListener('click', e => { if (e.target === mm) mm.hidden = true; });
document.addEventListener('keydown', e => { if (e.key === 'Escape' && mm && !mm.hidden) mm.hidden = true; });

/* tilt */
if (fine && !reduce) $$('.go-cover--tilt').forEach(t => {
  t.addEventListener('pointermove', e => { const r = t.getBoundingClientRect(), px = (e.clientX-r.left)/r.width, py = (e.clientY-r.top)/r.height;
    t.style.transform = `rotateY(${(px-.5)*16}deg) rotateX(${(.5-py)*12}deg)`; t.style.setProperty('--gx', px*100+'%'); t.style.setProperty('--gy', py*100+'%'); });
  t.addEventListener('pointerleave', () => t.style.transform = '');
});

/* toggles: aria-pressed groups */
$$('[data-toggle-group]').forEach(g => g.addEventListener('click', e => {
  const b = e.target.closest('button'); if (!b || !g.contains(b)) return;
  $$('button', g).forEach(x => x.setAttribute('aria-pressed', x === b));
}));

/* catalog filter with Flip */
const grid = $('[data-flip-grid]');
$$('[data-filter]').forEach(tab => tab.addEventListener('click', () => {
  const f = tab.dataset.filter, cards = $$('.go-book', grid);
  const state = hasG && window.Flip ? Flip.getState(cards) : null;
  cards.forEach(c => c.hidden = !(f === 'all' || c.dataset.s === f));
  const cnt = $('[data-count]'); if (cnt) cnt.textContent = cards.filter(c => !c.hidden).length + ' libros';
  if (state) Flip.from(state, {duration:.7, ease:'power3.inOut', absolute:true,
    onEnter: els => gsap.fromTo(els, {opacity:0, scale:.92}, {opacity:1, scale:1, duration:.5}),
    onLeave: els => gsap.to(els, {opacity:0, scale:.92, duration:.35})});
  if (window.ScrollTrigger) ScrollTrigger.refresh();
}));

/* video testimonials */
$$('.vid button').forEach(b => b.addEventListener('click', () => {
  const v = document.createElement('video'); v.src = b.dataset.src; v.controls = true; v.autoplay = true; v.playsInline = true;
  const box = b.closest('.vid'); box.innerHTML = ''; box.appendChild(v); v.focus();
}));

/* payment details reveal is CSS (:has); upload drop zone */
$$('.go-drop').forEach(d => {
  ['dragenter','dragover'].forEach(ev => d.addEventListener(ev, e => { e.preventDefault(); d.classList.add('go-drop--over'); }));
  ['dragleave','drop'].forEach(ev => d.addEventListener(ev, e => { e.preventDefault(); d.classList.remove('go-drop--over'); }));
});

/* admin: select a row */
$$('[data-rows] tr').forEach(tr => tr.addEventListener('click', () => {
  $$('[data-rows] tr').forEach(x => x.setAttribute('aria-selected', x === tr));
  const o = $('[data-sel-order]'); if (o) o.textContent = tr.dataset.order;
}));

if (!hasG) { $$('.stage .bk').forEach((el, i, a) => { const k = i-(a.length-1)/2; el.style.transform = `translate(${k*44}px,${Math.abs(k)*12}px) rotate(${k*9}deg)`; }); return; }

gsap.registerPlugin(ScrollTrigger); if (window.Flip) gsap.registerPlugin(Flip);
if (window.Lenis){ const lenis = new Lenis({lerp:.1}); lenis.on('scroll', ScrollTrigger.update); gsap.ticker.add(t => lenis.raf(t*1000)); gsap.ticker.lagSmoothing(0); }

/* hero: lines + cover fan */
const bks = $$('.stage .bk');
if ($('.hero')){
  const unit = () => Math.min(56, $('.stage').clientWidth/13);
  const fan = s => bks.map((el,i) => { const k = i-(bks.length-1)/2; return {el, x:k*s*unit(), r:k*s*9, y:Math.abs(k)*s*14}; });
  const tl = gsap.timeline({defaults:{ease:'expo.out'}});
  tl.from('.hero h1 .line>span', {yPercent:110, duration:1.2, stagger:.12})
    .from('.hero .go-eyebrow, .hero .lede, .hero .ctas', {y:16, opacity:0, duration:.9, stagger:.08}, '-=.9')
    .from(bks, {y:240, duration:1.3, stagger:.07, ease:'power4.out'}, '-=1.1');
  fan(1).forEach(({el,x,r,y},i) => tl.to(el, {x, y, rotation:r, duration:1.1}, 1.0+i*.04));
  ScrollTrigger.create({trigger:'.stage', start:'top 20%', end:'bottom top', scrub:.6, onUpdate:s => fan(1+s.progress*.35).forEach(({el,x,r,y}) => gsap.set(el, {x,y,rotation:r}))});
  bks.forEach(el => { const c = $('.go-cover', el);
    el.addEventListener('mouseenter', () => gsap.to(c, {y:-26, duration:.5, ease:'power3.out'}));
    el.addEventListener('mouseleave', () => gsap.to(c, {y:0, duration:.6, ease:'power3.out'})); });
}
/* reveals from a readable resting state */
$$('[data-reveal]').forEach(el => gsap.from(el.children, {y:36, duration:1, stagger:.06, ease:'expo.out', scrollTrigger:{trigger:el, start:'top 88%'}}));
$$('.page-head h1').forEach(h => gsap.from(h, {y:24, duration:1, ease:'expo.out'}));
const sb = $('.svc-band'); if (sb) gsap.from('.svc', {y:50, rotation:(i)=>i%2?1:-1, duration:1.1, stagger:.07, ease:'expo.out', scrollTrigger:{trigger:sb, start:'top 75%'}});
})();
