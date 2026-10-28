#!/usr/bin/env python3
"""Syborg v4: people-free, correct aspect ratios, unslop skills."""
from pathlib import Path

ROOT = Path('/workspace/syborg/build')
SAFE = '../assets/safe'
BOTTLE_URL = 'https://syborgsalts.com/products/syborg-smelling-salts'
AMP_URL = 'https://syborgsalts.com/products/syborg-smelling-salts-50-count-ampules'
STORE = 'https://syborgsalts.com/'
EMAIL = 'fifabros150@gmail.com'
REFUND = 'https://syborgsalts.com/policies/refund-policy'

FAQ = [
  ('What are Syborg smelling salts?',
   'Ammonia inhalants sold as Syborg Strength. Athletes use them for a sharp hit of alertness before a heavy set or a play.'),
  ('How do I use the bottle?',
   'Open the cap, hold the bottle about 6 inches from your nose, and take a short inhale. Follow the label. Do not put it against your nose.'),
  ('How do I use an ampule?',
   'Crush one sealed ampule, inhale once, and discard it. Each ampule is single-use.'),
  ('What does each product cost?',
   'The multi-use bottle is $24.99. The 50-count ampule jar is $44.99. Prices match the live store.'),
  ('Can I get a refund?',
   'Syborg Strength lists refunds for up to 30 days on their refund policy page.'),
  ('Who do I contact?',
   f'Email {EMAIL}. That is the address listed on the store contact information policy.'),
]

def faq_html():
  parts = []
  for q,a in FAQ:
    parts.append(f'<details><summary>{q}</summary><p>{a}</p></details>')
  return ''.join(parts)

def nav(active, prefix='./'):
  items = [('index.html','Home'),('bottle.html','Bottle'),('ampules.html','Ampules'),
           ('faq.html','FAQ'),('contact.html','Contact')]
  links = []
  for href, label in items:
    cur = ' aria-current=page' if active==href else ''
    links.append(f'<a href="{prefix}{href}"{cur}>{label}</a>')
  return ''.join(links)

def footer(extra=''):
  return f'''
<footer class="site-footer">
  <div class="wrap foot">
    <div>
      <div class="logo">Syborg Salts</div>
      <p>Syborg Strength. Smelling salts for hard training.</p>
      <p style="margin-top:.5rem"><a href="mailto:{EMAIL}">{EMAIL}</a></p>
    </div>
    <div class="foot-links">
      <a href="./bottle.html">Bottle ($24.99)</a>
      <a href="./ampules.html">Ampules ($44.99)</a>
      <a href="./faq.html">FAQ</a>
      <a href="./contact.html">Contact</a>
      <a href="{STORE}" rel="noopener">syborgsalts.com</a>
      <a href="{REFUND}" rel="noopener">Refunds</a>
    </div>
  </div>
  {extra}
</footer>
<script>
(function(){{
  var btn=document.querySelector('[data-nav]');
  var links=document.querySelector('[data-nav-links]');
  if(btn&&links){{btn.addEventListener('click',function(){{links.classList.toggle('open');btn.setAttribute('aria-expanded',links.classList.contains('open'));}});}}
}})();
</script>
'''

def head(title, fonts_href, css_extra='', fav='d1'):
  return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="Syborg Strength smelling salts. Multi-use bottle $24.99 and 50 ampules $44.99.">
<link rel="icon" href="../assets/favicons/{fav}-32.png" sizes="32x32">
<link rel="apple-touch-icon" href="../assets/favicons/{fav}-180.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{fonts_href}" rel="stylesheet">
<link rel="stylesheet" href="./styles.css">
{css_extra}
</head>
<body>
'''

HEADER = '''
<header class="site-header">
  <div class="wrap nav">
    <a class="logo" href="./index.html">Syborg Salts</a>
    <button class="mobile-toggle" type="button" data-nav aria-expanded="false" aria-label="Menu">Menu</button>
    <nav class="nav-links" data-nav-links>{nav}</nav>
    <a class="nav-cta" href="{store}" rel="noopener">Live store</a>
  </div>
</header>
'''

# Shared image CSS contract: every .media is a locked ratio box; img never stretches.
IMG_CSS = '''
/* IMAGE CONTRACT: never stretch. Box ratio matches source. */
.media{position:relative;overflow:hidden;background:var(--media-bg, var(--bg2));isolation:isolate}
.media > img{position:absolute;inset:0;width:100%;height:100%;object-fit:contain;object-position:center;display:block}
.media.cover > img{object-fit:cover} /* only when source and box share the same ratio */
.ratio-1x1{aspect-ratio:1 / 1}
.ratio-2x3{aspect-ratio:2 / 3} /* bottle-cutout ~0.665 */
.ratio-hero{aspect-ratio:1 / 1; max-width:min(520px, 100%)}
.media-cap{display:flex;justify-content:space-between;gap:1rem;padding:.65rem 0 0;font-size:.85rem;color:var(--muted)}
.duo-grid{display:grid;grid-template-columns:1fr 1fr;gap:clamp(1rem,3vw,1.75rem)}
@media (max-width:720px){.duo-grid{grid-template-columns:1fr}}
.product-card{display:grid;gap:.75rem;color:inherit;text-decoration:none}
.product-card h3{font-family:var(--display);font-size:1.35rem;letter-spacing:-.02em}
.product-card .price{font-weight:700;color:var(--accent)}
'''

# ---------- D1 Ampule: slate/ice, Syne + Instrument Sans ----------
D1_CSS = '''
:root{
  --display:'Syne',sans-serif; --body:'Instrument Sans',system-ui,sans-serif;
  --bg:#0c1218; --bg2:#141c24; --ink:#e8eef2; --muted:#9aafbd;
  --accent:#8ad4f0; --accent-ink:#061018; --line:rgba(138,212,240,.18);
  --gutter:clamp(1.1rem,4vw,2.5rem); --media-bg:#0a1016;
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{font-family:var(--body);background:var(--bg);color:var(--ink);line-height:1.55;font-size:17px;-webkit-font-smoothing:antialiased}
a{color:inherit;text-decoration:none}
img{max-width:100%;height:auto}
:focus-visible{outline:2px solid var(--accent);outline-offset:3px}
.wrap{width:min(1120px,100%);margin-inline:auto;padding-inline:var(--gutter)}
.site-header{position:sticky;top:0;z-index:40;background:rgba(12,18,24,.94);border-bottom:1px solid var(--line);backdrop-filter:none}
.nav{display:flex;align-items:center;gap:1rem;min-height:64px;position:relative}
.logo{font-family:var(--display);font-weight:800;letter-spacing:-.03em;font-size:1.15rem}
.nav-links{display:flex;gap:1.25rem;font-size:.92rem;color:var(--muted);margin-left:auto}
.nav-links a:hover,.nav-links a[aria-current=page]{color:var(--ink)}
.nav-cta{background:var(--accent);color:var(--accent-ink);padding:.55rem 1rem;font-weight:700;font-size:.88rem}
.mobile-toggle{display:none;background:none;border:1px solid var(--line);color:var(--ink);padding:.35rem .65rem;font:inherit}
.hero{display:grid;grid-template-columns:1.05fr .95fr;gap:clamp(1.5rem,4vw,3rem);align-items:center;padding:clamp(2.5rem,6vw,4.5rem) 0}
.hero-copy h1{font-family:var(--display);font-weight:800;font-size:clamp(2.6rem,6.5vw,4.8rem);line-height:.95;letter-spacing:-.04em;max-width:12ch}
.hero-copy p{margin-top:1.1rem;color:var(--muted);max-width:38ch;font-size:1.05rem}
.hero-actions{display:flex;flex-wrap:wrap;gap:.75rem;margin-top:1.5rem}
.btn{display:inline-flex;align-items:center;justify-content:center;padding:.85rem 1.25rem;font-weight:700;font-size:.95rem;border:0;cursor:pointer;font-family:inherit}
.btn-primary{background:var(--accent);color:var(--accent-ink)}
.btn-ghost{border:1px solid var(--line);color:var(--ink);background:transparent}
.btn-ghost:hover{border-color:var(--accent)}
.price-note{margin-top:.9rem;font-size:.9rem;color:var(--muted)}
.hero-visual{display:grid;gap:1rem}
.stack{display:grid;grid-template-columns:1fr 1fr;gap:.85rem;align-items:end}
.stack .media:first-child{grid-column:1 / -1}
.section{padding:clamp(2.5rem,6vw,4rem) 0}
.section h2{font-family:var(--display);font-size:clamp(1.8rem,4vw,2.6rem);letter-spacing:-.03em;line-height:1.05;max-width:16ch}
.lede{margin-top:.85rem;color:var(--muted);max-width:48ch}
.band{background:var(--bg2);border-block:1px solid var(--line)}
.how{display:grid;grid-template-columns:1fr 1fr;gap:clamp(1rem,3vw,2rem);margin-top:1.5rem;align-items:start}
.how ol{list-style:none;display:grid;gap:1rem}
.how li{border-left:3px solid var(--accent);padding-left:1rem}
.how strong{display:block;font-family:var(--display);font-size:1.05rem;margin-bottom:.2rem}
.faq-list{margin-top:1.5rem;border-top:1px solid var(--line)}
.faq-list details{border-bottom:1px solid var(--line);padding:1rem 0}
.faq-list summary{cursor:pointer;font-weight:600;list-style:none;display:flex;justify-content:space-between;gap:1rem}
.faq-list summary::after{content:"+";color:var(--accent);font-weight:700}
.faq-list details[open] summary::after{content:"–"}
.faq-list p{margin-top:.65rem;color:var(--muted);max-width:60ch}
.pdp{display:grid;grid-template-columns:1fr 1fr;gap:clamp(1.5rem,4vw,3rem);align-items:start;padding:clamp(2rem,5vw,3.5rem) 0}
.pdp h1{font-family:var(--display);font-size:clamp(2rem,4.5vw,3rem);line-height:1.05}
.pdp .price{font-size:1.6rem;font-weight:800;margin:.75rem 0 1rem}
.pdp .bullets{margin-top:1.25rem;display:grid;gap:.55rem}
.pdp .bullets li{list-style:none;padding-left:1rem;position:relative}
.pdp .bullets li::before{content:"";position:absolute;left:0;top:.55em;width:.45rem;height:.45rem;background:var(--accent)}
.contact-grid{display:grid;grid-template-columns:1fr 1fr;gap:2rem;padding:clamp(2rem,5vw,3.5rem) 0}
.contact-block a.mail{color:var(--accent);font-weight:700;font-size:1.15rem;word-break:break-all}
form{display:grid;gap:.75rem}
label{font-size:.88rem;color:var(--muted)}
input,textarea{background:var(--bg2);border:1px solid var(--line);color:var(--ink);padding:.75rem .85rem;font:inherit;border-radius:0;width:100%}
textarea{min-height:140px;resize:vertical}
.site-footer{border-top:1px solid var(--line);padding:2rem 0;margin-top:2rem;font-size:.92rem;color:var(--muted)}
.foot{display:flex;flex-wrap:wrap;gap:1.5rem;justify-content:space-between}
.foot-links{display:flex;flex-wrap:wrap;gap:.85rem 1.25rem}
.rise{opacity:0;transform:translateY(14px);animation:rise .65s ease forwards}
.rise.d1{animation-delay:.08s}.rise.d2{animation-delay:.16s}.rise.d3{animation-delay:.24s}
@keyframes rise{to{opacity:1;transform:none}}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}.rise{opacity:1;transform:none}}
@media (max-width:900px){
  .hero,.pdp,.how,.contact-grid{grid-template-columns:1fr}
  .nav-links{display:none}
  .nav-links.open{display:flex;flex-direction:column;position:absolute;top:100%;left:0;right:0;background:var(--bg);padding:1rem var(--gutter);border-bottom:1px solid var(--line)}
  .mobile-toggle{display:block;margin-left:auto}
  .nav-cta{margin-left:0}
}
''' + IMG_CSS

# ---------- D2 Platform: chalk/iron/red, Barlow Condensed + Newsreader ----------
D2_CSS = '''
:root{
  --display:'Barlow Condensed',sans-serif; --body:'Newsreader',Georgia,serif;
  --bg:#f2efe6; --bg2:#e6e1d4; --ink:#121212; --muted:#4a4740;
  --accent:#b91c1c; --accent-ink:#fff; --line:rgba(18,18,18,.14);
  --dark:#121212; --dark-ink:#f2efe6;
  --gutter:clamp(1.1rem,4vw,2.5rem); --media-bg:#ddd7c8;
}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:var(--body);background:var(--bg);color:var(--ink);line-height:1.55;font-size:18px;-webkit-font-smoothing:antialiased}
a{color:inherit;text-decoration:none}
img{max-width:100%;height:auto}
:focus-visible{outline:2px solid var(--accent);outline-offset:3px}
.wrap{width:min(1120px,100%);margin-inline:auto;padding-inline:var(--gutter)}
.site-header{position:sticky;top:0;z-index:40;background:var(--bg);border-bottom:3px solid var(--ink)}
.nav{display:flex;align-items:center;gap:1rem;min-height:68px;position:relative}
.logo{font-family:var(--display);font-weight:800;text-transform:uppercase;letter-spacing:.02em;font-size:1.35rem}
.nav-links{display:flex;gap:1.4rem;font-family:var(--display);font-weight:600;text-transform:uppercase;letter-spacing:.04em;font-size:.95rem;margin-left:auto}
.nav-links a[aria-current=page]{text-decoration:underline;text-underline-offset:4px}
.nav-cta{background:var(--accent);color:var(--accent-ink);padding:.55rem 1.1rem;font-family:var(--display);font-weight:700;text-transform:uppercase;letter-spacing:.04em;font-size:.9rem}
.mobile-toggle{display:none;background:none;border:2px solid var(--ink);color:var(--ink);padding:.3rem .6rem;font-family:var(--display);text-transform:uppercase;font-weight:700}
.hero{display:grid;grid-template-columns:1.1fr .9fr;gap:clamp(1.5rem,4vw,2.5rem);align-items:end;padding:clamp(2.2rem,5vw,3.5rem) 0}
.hero-copy h1{font-family:var(--display);font-weight:800;text-transform:uppercase;font-size:clamp(2.8rem,8vw,5.8rem);line-height:.88;letter-spacing:-.01em;max-width:12ch}
.hero-copy p{margin-top:1rem;max-width:36ch}
.hero-actions{display:flex;flex-wrap:wrap;gap:.75rem;margin-top:1.4rem}
.btn{display:inline-flex;align-items:center;justify-content:center;padding:.85rem 1.3rem;font-family:var(--display);font-weight:700;text-transform:uppercase;letter-spacing:.04em;font-size:1rem;border:0;cursor:pointer}
.btn-primary{background:var(--accent);color:var(--accent-ink)}
.btn-ghost{background:transparent;border:2px solid var(--ink)}
.price-note{margin-top:.9rem;font-size:.95rem;color:var(--muted);font-family:var(--display);text-transform:uppercase;letter-spacing:.06em}
.platform{background:var(--dark);color:var(--dark-ink);border-top:3px solid var(--ink);border-bottom:3px solid var(--ink)}
.platform-inner{display:grid;grid-template-columns:1fr 1fr;gap:0}
.platform-inner > a{padding:clamp(1.5rem,4vw,2.5rem);border-right:3px solid rgba(242,239,230,.2);color:inherit;text-decoration:none;display:grid;gap:.5rem}
.platform-inner > a:last-child{border-right:0}
.platform-inner h3{font-family:var(--display);font-size:clamp(1.6rem,3vw,2.2rem);text-transform:uppercase}
.platform-inner .price{font-family:var(--display);font-weight:700;color:#f5c2c2;font-size:1.2rem}
.section{padding:clamp(2.5rem,6vw,4rem) 0}
.section h2,.band h2{font-family:var(--display);font-size:clamp(2rem,5vw,3.2rem);text-transform:uppercase;line-height:.95}
.lede{margin-top:.75rem;max-width:46ch;color:var(--muted)}
.band{padding:clamp(2.5rem,6vw,4rem) 0;border-bottom:3px solid var(--ink)}
.how{display:grid;grid-template-columns:1fr 1fr;gap:1.5rem;margin-top:1.5rem}
.how ol{list-style:none;display:grid;gap:1rem}
.how li{border-left:4px solid var(--accent);padding-left:1rem}
.how strong{display:block;font-family:var(--display);text-transform:uppercase;font-size:1.15rem}
.faq-list{margin-top:1.5rem;border-top:3px solid var(--ink)}
.faq-list details{border-bottom:3px solid var(--ink);padding:1rem 0}
.faq-list summary{cursor:pointer;font-family:var(--display);font-weight:700;text-transform:uppercase;font-size:1.15rem;list-style:none;display:flex;justify-content:space-between}
.faq-list summary::after{content:"+";color:var(--accent)}
.faq-list details[open] summary::after{content:"–"}
.faq-list p{margin-top:.65rem;max-width:60ch}
.pdp{display:grid;grid-template-columns:1fr 1fr;gap:clamp(1.5rem,4vw,3rem);padding:clamp(2rem,5vw,3.5rem) 0;align-items:start}
.pdp h1{font-family:var(--display);font-size:clamp(2.2rem,5vw,3.4rem);text-transform:uppercase;line-height:.95}
.pdp .price{font-family:var(--display);font-size:1.8rem;font-weight:800;color:var(--accent);margin:.75rem 0 1rem}
.pdp .bullets{margin-top:1.25rem;display:grid;gap:.55rem;list-style:none}
.pdp .bullets li{padding-left:1rem;border-left:3px solid var(--accent)}
.contact-grid{display:grid;grid-template-columns:1fr 1fr;gap:2rem;padding:clamp(2rem,5vw,3.5rem) 0}
.contact-block a.mail{color:var(--accent);font-weight:700;font-size:1.15rem;word-break:break-all}
form{display:grid;gap:.75rem}
label{font-size:.88rem;color:var(--muted);font-family:var(--display);text-transform:uppercase}
input,textarea{background:#fff;border:2px solid var(--ink);color:var(--ink);padding:.75rem .85rem;font:inherit;width:100%}
textarea{min-height:140px;resize:vertical}
.site-footer{border-top:3px solid var(--ink);padding:2rem 0;margin-top:0;font-size:.95rem}
.foot{display:flex;flex-wrap:wrap;gap:1.5rem;justify-content:space-between}
.foot-links{display:flex;flex-wrap:wrap;gap:.85rem 1.25rem;font-family:var(--display);text-transform:uppercase;letter-spacing:.04em;font-size:.9rem}
.rise{opacity:0;transform:translateY(14px);animation:rise .65s ease forwards}
.rise.d1{animation-delay:.08s}.rise.d2{animation-delay:.16s}.rise.d3{animation-delay:.24s}
@keyframes rise{to{opacity:1;transform:none}}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}.rise{opacity:1;transform:none}}
@media (max-width:900px){
  .hero,.pdp,.how,.contact-grid,.platform-inner{grid-template-columns:1fr}
  .platform-inner > a{border-right:0;border-bottom:3px solid rgba(242,239,230,.2)}
  .nav-links{display:none}
  .nav-links.open{display:flex;flex-direction:column;position:absolute;top:100%;left:0;right:0;background:var(--bg);padding:1rem var(--gutter);border-bottom:3px solid var(--ink)}
  .mobile-toggle{display:block;margin-left:auto}
}
''' + IMG_CSS

# ---------- D3 Chrome: void/mercury/cyan, Archivo Black + Sora ----------
D3_CSS = '''
:root{
  --display:'Archivo Black',sans-serif; --body:'Sora',system-ui,sans-serif;
  --bg:#05070d; --bg2:#0c1018; --ink:#e7ebf0; --muted:#8b95a3; --metal:#c5ccd4;
  --accent:#3eb7ff; --accent-ink:#031018; --line:rgba(62,183,255,.16);
  --gutter:clamp(1.1rem,4vw,2.5rem); --media-bg:#080b12;
}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:var(--body);background:var(--bg);color:var(--ink);line-height:1.55;font-size:16.5px;-webkit-font-smoothing:antialiased}
a{color:inherit;text-decoration:none}
img{max-width:100%;height:auto}
:focus-visible{outline:2px solid var(--accent);outline-offset:3px}
.wrap{width:min(1120px,100%);margin-inline:auto;padding-inline:var(--gutter)}
.site-header{position:sticky;top:0;z-index:40;background:rgba(5,7,13,.94);border-bottom:1px solid var(--line)}
.nav{display:flex;align-items:center;gap:1rem;min-height:64px;position:relative}
.logo{font-family:var(--display);font-size:1.05rem;letter-spacing:.02em}
.nav-links{display:flex;gap:1.2rem;font-size:.88rem;color:var(--muted);font-weight:500;margin-left:auto}
.nav-links a:hover,.nav-links a[aria-current=page]{color:var(--accent)}
.nav-cta{background:var(--accent);color:var(--accent-ink);padding:.55rem 1rem;font-weight:700;font-size:.85rem}
.mobile-toggle{display:none;background:none;border:1px solid var(--line);color:var(--ink);padding:.35rem .65rem;font:inherit}
.hero{display:grid;grid-template-columns:1fr 1fr;gap:clamp(1.25rem,4vw,2.5rem);align-items:center;padding:clamp(2.2rem,6vw,4rem) 0;min-height:auto}
.hero-copy h1{font-family:var(--display);font-size:clamp(2.6rem,7vw,5.2rem);line-height:.92;letter-spacing:-.02em;color:var(--metal);max-width:11ch}
.hero-copy p{margin-top:1.1rem;color:var(--muted);max-width:36ch}
.hero-actions{display:flex;flex-wrap:wrap;gap:.75rem;margin-top:1.5rem}
.btn{display:inline-flex;align-items:center;justify-content:center;padding:.85rem 1.2rem;font-weight:700;font-size:.92rem;border:0;cursor:pointer;font-family:inherit}
.btn-primary{background:var(--accent);color:var(--accent-ink)}
.btn-ghost{border:1px solid var(--line);background:transparent;color:var(--ink)}
.price-note{margin-top:.85rem;font-size:.88rem;color:var(--muted)}
.section{padding:clamp(2.5rem,6vw,4rem) 0}
.section h2{font-family:var(--display);font-size:clamp(1.9rem,4.5vw,3rem);line-height:1.05;letter-spacing:-.02em;color:var(--metal);max-width:14ch}
.lede{margin-top:.85rem;color:var(--muted);max-width:46ch}
.band{background:var(--bg2);border-block:1px solid var(--line)}
.how{display:grid;grid-template-columns:1.1fr .9fr;gap:clamp(1rem,3vw,2rem);margin-top:1.5rem;align-items:start}
.how ol{list-style:none;display:grid;gap:1rem}
.how li{border-left:2px solid var(--accent);padding-left:.85rem}
.how strong{display:block;font-family:var(--display);font-size:1rem;color:var(--metal);margin-bottom:.2rem}
.faq-list{margin-top:1.5rem;border-top:1px solid var(--line)}
.faq-list details{border-bottom:1px solid var(--line);padding:1rem 0}
.faq-list summary{cursor:pointer;font-weight:600;list-style:none;display:flex;justify-content:space-between}
.faq-list summary::after{content:"+";color:var(--accent)}
.faq-list details[open] summary::after{content:"–"}
.faq-list p{margin-top:.65rem;color:var(--muted);max-width:60ch}
.pdp{display:grid;grid-template-columns:1fr 1fr;gap:clamp(1.5rem,4vw,3rem);padding:clamp(2rem,5vw,3.5rem) 0;align-items:start}
.pdp h1{font-family:var(--display);font-size:clamp(2rem,4.5vw,3rem);line-height:1.05;color:var(--metal)}
.pdp .price{font-size:1.55rem;font-weight:700;color:var(--accent);margin:.75rem 0 1rem}
.pdp .bullets{margin-top:1.25rem;display:grid;gap:.55rem;list-style:none}
.pdp .bullets li{border-left:2px solid var(--accent);padding-left:.85rem}
.contact-grid{display:grid;grid-template-columns:1fr 1fr;gap:2rem;padding:clamp(2rem,5vw,3.5rem) 0}
.contact-block a.mail{color:var(--accent);font-weight:700;font-size:1.1rem;word-break:break-all}
form{display:grid;gap:.75rem}
label{font-size:.85rem;color:var(--muted)}
input,textarea{background:var(--bg2);border:1px solid var(--line);color:var(--ink);padding:.75rem .85rem;font:inherit;width:100%}
textarea{min-height:140px;resize:vertical}
.site-footer{border-top:1px solid var(--line);padding:2rem 0;margin-top:2rem;font-size:.9rem;color:var(--muted)}
.foot{display:flex;flex-wrap:wrap;gap:1.5rem;justify-content:space-between}
.foot-links{display:flex;flex-wrap:wrap;gap:.85rem 1.25rem}
.mark-row{display:grid;grid-template-columns:120px 1fr;gap:1.25rem;align-items:center;margin-top:2rem;padding:1.25rem;border:1px solid var(--line);background:var(--bg2)}
.mark-row p{color:var(--muted);font-size:.95rem}
.rise{opacity:0;transform:translateY(14px);animation:rise .65s ease forwards}
.rise.d1{animation-delay:.08s}.rise.d2{animation-delay:.16s}.rise.d3{animation-delay:.24s}
@keyframes rise{to{opacity:1;transform:none}}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}.rise{opacity:1;transform:none}}
@media (max-width:900px){
  .hero,.pdp,.how,.contact-grid{grid-template-columns:1fr}
  .nav-links{display:none}
  .nav-links.open{display:flex;flex-direction:column;position:absolute;top:100%;left:0;right:0;background:rgba(5,7,13,.98);padding:1rem var(--gutter);border-bottom:1px solid var(--line)}
  .mobile-toggle{display:block;margin-left:auto}
  .mark-row{grid-template-columns:80px 1fr}
}
''' + IMG_CSS


def media(src, alt, ratio='ratio-1x1', cover=False, caption=None):
  cls = f'media {ratio}' + (' cover' if cover else '')
  cap = f'<div class="media-cap"><span>{caption[0]}</span><span>{caption[1]}</span></div>' if caption else ''
  return f'<figure class="{cls}"><img src="{SAFE}/{src}" alt="{alt}" width="1200" height="1200" decoding="async">{cap}</figure>'


def write_design(key, title_suffix, fonts, css, fav, home_body, bottle_extra_img, amp_extra_img):
  d = ROOT / key
  d.mkdir(parents=True, exist_ok=True)
  (d/'styles.css').write_text(css)

  def page(fname, title, body):
    h = head(title, fonts, fav=fav)
    hdr = HEADER.format(nav=nav(fname), store=STORE)
    html = h + hdr + f'<main>{body}</main>' + footer() + '</body></html>'
    (d/fname).write_text(html)

  page('index.html', f'Syborg Salts / {title_suffix}', home_body)

  bottle_body = f'''
<section class="wrap pdp">
  <div>
    {media(bottle_extra_img, 'Syborg smelling salts multi-use bottle', 'ratio-1x1')}
    <div style="margin-top:.85rem" class="duo-grid">
      {media('bottle-detail.png' if key!='d2' else 'bottle-chalk.png', 'Syborg bottle label art with chrome robot', 'ratio-1x1', cover=True)}
      {media('robot-void.png' if key=='d3' else 'bottle-sports.png', 'Syborg chrome robot mark', 'ratio-1x1', cover=True)}
    </div>
  </div>
  <div>
    <h1>Syborg Smelling Salts</h1>
    <div class="price">$24.99</div>
    <p>Multi-use bottle. Pre-activated. Keep it about 6 inches from your nose. Up to hundreds of uses per bottle.</p>
    <div class="hero-actions" style="margin-top:1.25rem">
      <a class="btn btn-primary" href="{BOTTLE_URL}" rel="noopener">Buy on syborgsalts.com</a>
      <a class="btn btn-ghost" href="./index.html">Back to home</a>
    </div>
    <ul class="bullets">
      <li>Pre-activated multi-use bottle</li>
      <li>Hold about 6 inches from your nose</li>
      <li>Made for powerlifting, football, hockey, strongman, and fighters</li>
      <li>Lab-grade ingredients per the brand label</li>
    </ul>
  </div>
</section>'''
  page('bottle.html', 'Syborg Smelling Salts ($24.99)', bottle_body)

  amp_body = f'''
<section class="wrap pdp">
  <div>
    {media(amp_extra_img, 'Syborg 50-count ammonia ampules jar', 'ratio-1x1')}
    <div style="margin-top:.85rem" class="duo-grid">
      {media('ampules-compact.png', 'Compact jar of Syborg ampules', 'ratio-1x1', cover=True)}
      {media('ampules-hero.png', 'Syborg ampules product graphic', 'ratio-1x1', cover=True)}
    </div>
  </div>
  <div>
    <h1>Syborg Smelling Salts 50 Count Ampules</h1>
    <div class="price">$44.99</div>
    <p>50 individually wrapped ampules. Crush, inhale, throw away. Built for travel and meet bags.</p>
    <div class="hero-actions" style="margin-top:1.25rem">
      <a class="btn btn-primary" href="{AMP_URL}" rel="noopener">Buy on syborgsalts.com</a>
      <a class="btn btn-ghost" href="./index.html">Back to home</a>
    </div>
    <ul class="bullets">
      <li>50 individually wrapped ampules</li>
      <li>Crush, inhale, discard</li>
      <li>Portable jar for meets and travel</li>
      <li>Highest-strength formula per the brand label</li>
    </ul>
  </div>
</section>'''
  page('ampules.html', 'Syborg Ampules ($44.99)', amp_body)

  faq_body = f'''
<section class="wrap section">
  <h2>FAQ</h2>
  <p class="lede">Answers pulled from the live store policies and product pages. No invented stats.</p>
  <div class="faq-list">{faq_html()}</div>
</section>'''
  page('faq.html', 'FAQ | Syborg Salts', faq_body)

  contact_body = f'''
<section class="wrap contact-grid">
  <div class="contact-block">
    <h1 style="font-family:var(--display);font-size:clamp(2rem,4vw,2.8rem);margin-bottom:1rem">Contact</h1>
    <p>Reach Syborg Strength at the email listed on their store contact policy.</p>
    <p style="margin-top:1rem">Trade name: Syborg Strength</p>
    <p style="margin-top:1rem"><a class="mail" href="mailto:{EMAIL}">{EMAIL}</a></p>
    <p style="margin-top:1rem;color:var(--muted)">Or shop directly at <a href="{STORE}" rel="noopener">syborgsalts.com</a>.</p>
  </div>
  <form action="mailto:{EMAIL}" method="post" enctype="text/plain">
    <label>Name<input name="name" required></label>
    <label>Email<input type="email" name="email" required></label>
    <label>Message<textarea name="message" required></textarea></label>
    <button class="btn btn-primary" type="submit">Open email draft</button>
  </form>
</section>'''
  page('contact.html', 'Contact | Syborg Salts', contact_body)
  print('wrote', key)


# HOME BODIES
d1_home = f'''
<section class="hero wrap">
  <div class="hero-copy">
    <h1 class="rise">One sniff. Clear head.</h1>
    <p class="rise d1">Syborg Strength ammonia inhalants for powerlifters, football, hockey, and fighters. Bottle or 50 ampules.</p>
    <div class="hero-actions rise d2">
      <a class="btn btn-primary" href="{BOTTLE_URL}" rel="noopener">Buy bottle ($24.99)</a>
      <a class="btn btn-ghost" href="{AMP_URL}" rel="noopener">Buy ampules ($44.99)</a>
    </div>
    <p class="price-note rise d3">Prices from the live store. Refunds up to 30 days.</p>
  </div>
  <div class="hero-visual rise d1">
    <div class="stack">
      {media('ampules-void.png', 'Syborg 50-count ammonia ampules jar', 'ratio-1x1', caption=('50 ampules','$44.99'))}
      {media('bottle-void.png', 'Syborg smelling salts bottle with chrome robot label', 'ratio-1x1', caption=('Multi-use bottle','$24.99'))}
      {media('robot-void.png', 'Syborg chrome robot mark', 'ratio-1x1')}
    </div>
  </div>
</section>
<section class="section wrap">
  <h2>Pick the format that fits your bag.</h2>
  <p class="lede">Two SKUs. Same brand. Buy on the live store.</p>
  <div class="duo-grid" style="margin-top:1.5rem">
    <a class="product-card" href="./bottle.html">
      {media('bottle-void.png', 'Syborg bottle', 'ratio-1x1')}
      <h3>Multi-use bottle</h3>
      <div class="price">$24.99</div>
      <p style="color:var(--muted)">Pre-activated. Hold about 6 inches from your nose.</p>
    </a>
    <a class="product-card" href="./ampules.html">
      {media('ampules-void.png', 'Syborg ampules', 'ratio-1x1')}
      <h3>50-count ampules</h3>
      <div class="price">$44.99</div>
      <p style="color:var(--muted)">Crush, inhale, discard. Meet-bag portable.</p>
    </a>
  </div>
</section>
<section class="section band">
  <div class="wrap">
    <h2>How to use them</h2>
    <div class="how">
      <ol>
        <li><strong>Bottle</strong> Open the cap. Hold about 6 inches from your nose. One short inhale. Cap it.</li>
        <li><strong>Ampule</strong> Crush one sealed ampule. Inhale once. Throw it away.</li>
        <li><strong>Safety</strong> Not a medical product. Keep away from eyes and broken skin. Adult athletes only.</li>
      </ol>
      {media('artboard3.png', 'How to use Syborg smelling salts', 'ratio-1x1', cover=True)}
    </div>
  </div>
</section>
<section class="section wrap">
  <h2>Quick answers</h2>
  <div class="faq-list">{faq_html()}</div>
</section>
'''

d2_home = f'''
<section class="hero wrap">
  <div class="hero-copy">
    <h1 class="rise">Smelling salts for the platform.</h1>
    <p class="rise d1">Two formats. Same lab-grade formula. Buy the multi-use bottle or the 50-count ampule jar.</p>
    <div class="hero-actions rise d2">
      <a class="btn btn-primary" href="{BOTTLE_URL}" rel="noopener">Buy bottle ($24.99)</a>
      <a class="btn btn-ghost" href="{AMP_URL}" rel="noopener">Buy ampules ($44.99)</a>
    </div>
    <p class="price-note rise d3">From the live store. Refunds up to 30 days.</p>
  </div>
  <div class="rise d1">
    {media('bottle-chalk.png', 'Syborg bottle on chalk ground', 'ratio-1x1')}
  </div>
</section>
<section class="platform">
  <div class="wrap platform-inner">
    <a href="./bottle.html">
      <h3>Multi-use bottle</h3>
      <div class="price">$24.99</div>
      <p>Pre-activated. Hold about 6 inches from your nose.</p>
    </a>
    <a href="./ampules.html">
      <h3>50 ampules</h3>
      <div class="price">$44.99</div>
      <p>Crush, inhale, discard. Meet-day portable.</p>
    </a>
  </div>
</section>
<section class="section wrap">
  <h2>Same formula. Two ways to carry it.</h2>
  <div class="duo-grid" style="margin-top:1.5rem">
    <a class="product-card" href="./bottle.html">
      {media('bottle-chalk.png', 'Syborg bottle', 'ratio-1x1')}
      <h3>Bottle ($24.99)</h3>
    </a>
    <a class="product-card" href="./ampules.html">
      {media('ampules-chalk.png', 'Syborg ampules', 'ratio-1x1')}
      <h3>Ampules ($44.99)</h3>
    </a>
  </div>
</section>
<section class="band">
  <div class="wrap">
    <h2>How to use</h2>
    <div class="how">
      <ol>
        <li><strong>Bottle</strong> Cap open. Short inhale at about 6 inches. Cap closed.</li>
        <li><strong>Ampule</strong> Crush one. Inhale once. Discard.</li>
        <li><strong>Rules</strong> Follow the label. Not for medical revival.</li>
      </ol>
      {media('ampules-compact.png', 'Compact Syborg ampule jar', 'ratio-1x1', cover=True)}
    </div>
  </div>
</section>
<section class="section wrap">
  <h2>FAQ</h2>
  <div class="faq-list">{faq_html()}</div>
</section>
'''

d3_home = f'''
<section class="hero wrap">
  <div class="hero-copy">
    <h1 class="rise">Chrome robot. Ammonia hit.</h1>
    <p class="rise d1">The bottle that wears a chrome robot. Pre-activated salts for hard training days.</p>
    <div class="hero-actions rise d2">
      <a class="btn btn-primary" href="{BOTTLE_URL}" rel="noopener">Buy bottle ($24.99)</a>
      <a class="btn btn-ghost" href="{AMP_URL}" rel="noopener">Buy ampules ($44.99)</a>
    </div>
    <p class="price-note rise d3">Live prices on syborgsalts.com</p>
  </div>
  <div class="rise d1">
    {media('bottle-void-deep.png', 'Syborg bottle with chrome robot label on void', 'ratio-1x1')}
  </div>
</section>
<section class="section wrap">
  <h2>Two SKUs. No filler catalog.</h2>
  <p class="lede">Buy the bottle you see on the label, or the jar of 50 ampules.</p>
  <div class="duo-grid" style="margin-top:1.5rem">
    <a class="product-card" href="./bottle.html">
      {media('bottle-void-deep.png', 'Syborg bottle', 'ratio-1x1')}
      <h3>Multi-use bottle</h3>
      <div class="price">$24.99</div>
    </a>
    <a class="product-card" href="./ampules.html">
      {media('ampules-void-deep.png', 'Syborg ampules', 'ratio-1x1')}
      <h3>50-count ampules</h3>
      <div class="price">$44.99</div>
    </a>
  </div>
  <div class="mark-row">
    {media('robot-void.png', 'Syborg chrome robot mark', 'ratio-1x1')}
    <p>The chrome robot on the label is the brand mark. No athlete photos on this preview. Product and mark only.</p>
  </div>
</section>
<section class="section band">
  <div class="wrap">
    <h2>Hold distance. Short inhale.</h2>
    <div class="how">
      <ol>
        <li><strong>Bottle</strong> About 6 inches from the nose. One short inhale. Cap it.</li>
        <li><strong>Ampule</strong> Crush, inhale once, discard.</li>
        <li><strong>Store</strong> Checkout and shipping run on the live Shopify store.</li>
      </ol>
      {media('artboard3.png', 'How to use Syborg', 'ratio-1x1', cover=True)}
    </div>
  </div>
</section>
<section class="section wrap">
  <h2>FAQ</h2>
  <div class="faq-list">{faq_html()}</div>
</section>
'''

write_design(
  'd1', 'Ampule',
  'https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500;600;700&family=Syne:wght@600;700;800&display=swap',
  D1_CSS, 'd1', d1_home, 'bottle-void.png', 'ampules-void.png'
)
write_design(
  'd2', 'Platform',
  'https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700;800&family=Newsreader:opsz,wght@6..72,400;6..72,500;6..72,600&display=swap',
  D2_CSS, 'd2', d2_home, 'bottle-chalk.png', 'ampules-chalk.png'
)
write_design(
  'd3', 'Chrome',
  'https://fonts.googleapis.com/css2?family=Archivo+Black&family=Sora:wght@400;500;600;700&display=swap',
  D3_CSS, 'd3', d3_home, 'bottle-void-deep.png', 'ampules-void-deep.png'
)

# Picker
picker = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Syborg redesigns picker</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;600;700&display=swap" rel="stylesheet">
<style>
:root{--bg:#0a0a0b;--ink:#f2f2f0;--muted:#9a9a92;--line:#222}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'IBM Plex Sans',system-ui,sans-serif;background:var(--bg);color:var(--ink);line-height:1.5;padding:clamp(1.5rem,5vw,3rem)}
h1{font-size:clamp(1.8rem,4vw,2.6rem);letter-spacing:-.03em}
.lede{margin:.75rem 0 2rem;color:var(--muted);max-width:56ch}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:1rem}
.card{display:grid;gap:.55rem;padding:1.35rem;border:1px solid var(--line);color:inherit;text-decoration:none;min-height:200px;align-content:start}
.card:hover{border-color:#8ad4f0}
.kicker{font-size:.75rem;color:#8ad4f0;font-weight:700;letter-spacing:.08em}
h2{font-size:1.45rem}
p{color:var(--muted);font-size:.95rem}
.note{margin-top:2rem;color:var(--muted);font-size:.88rem}
</style>
</head>
<body>
<h1>Syborg redesigns</h1>
<p class="lede">Three from-scratch concepts. Product and brand-mark photography only. No athlete photos. Real prices from syborgsalts.com. Built with Anthropic frontend-design, Taste Skill, Impeccable, and UI/UX Pro Max rules.</p>
<div class="grid">
  <a class="card" href="./d1/index.html"><div class="kicker">D1</div><h2>Ampule</h2><p>Clinical slate and ice. Sealed ampule as the page unit. Syne + Instrument Sans.</p></a>
  <a class="card" href="./d2/index.html"><div class="kicker">D2</div><h2>Platform</h2><p>Chalk and iron meet-day editorial. Barlow Condensed + Newsreader.</p></a>
  <a class="card" href="./d3/index.html"><div class="kicker">D3</div><h2>Chrome</h2><p>Void field. Chrome robot bottle as the hero. Archivo Black + Sora.</p></a>
</div>
<p class="note">Concept previews only. Checkout stays on the live Shopify store. No theme zip in this round.</p>
</body>
</html>
'''
(ROOT/'index.html').write_text(picker)
print('picker ok')
print('DONE')
