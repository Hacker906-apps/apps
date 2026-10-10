#!/usr/bin/env python3
"""Generate indexable static app detail pages and sitemap from data/apps.json.
Run: python3 build.py
"""
import json, html, os, re
from datetime import date
ROOT=os.path.dirname(os.path.abspath(__file__))
BASE='https://hacker906-apps.github.io/apps/'
def esc(x): return html.escape(str(x or ''), quote=True)
def safe_slug(x): return re.sub(r'[^a-z0-9-]','',str(x).lower())
with open(os.path.join(ROOT,'data/apps.json'),encoding='utf-8') as f: apps=json.load(f)
with open(os.path.join(ROOT,'data/categories.json'),encoding='utf-8') as f: cats=json.load(f)
catmap={c['id']:c['name'] for c in cats}
urls=[BASE,BASE+'about.html',BASE+'contact.html',BASE+'privacy-policy.html',BASE+'terms.html',BASE+'disclaimer.html']
for app in apps:
    if app.get('published') is False: continue
    appid=safe_slug(app.get('id') or app.get('slug') or '')
    if not appid: raise ValueError('Every published app must have a valid id')
    name=esc(app.get('name','Application'))
    title=esc((app.get('seo') or {}).get('title') or f"{app.get('name','Application')} — Download & App Details | Hacker Apps")
    description=esc((app.get('seo') or {}).get('description') or app.get('shortDescription') or f"Explore {app.get('name','this app')}, review compatibility and visit its official download source.")
    url=BASE+f'apps/{appid}/'
    img=esc(app.get('image') or '')
    category=esc(catmap.get(app.get('category'),app.get('category','Application')))
    platforms=', '.join(app.get('platforms') or ['Not specified'])
    features=''.join('<li>'+esc(x)+'</li>' for x in (app.get('features') or []))
    if not features: features='<li>Check the official project page for current features and requirements.</li>'
    official=esc(app.get('officialUrl') or '')
    download=esc(app.get('downloadUrl') or app.get('officialUrl') or '')
    official_button=f'<a class="official-button" href="{official}" target="_blank" rel="noopener noreferrer">Visit official website ↗</a>' if official else ''
    download_button=f'<a class="download-button" href="{download}" target="_blank" rel="noopener noreferrer">Go to download source <span>↗</span></a>' if download else '<p class="notice">A verified download link is not available yet. Visit the official project website for current options.</p>'
    safety=esc(app.get('safetyNote') or 'Verify the publisher and review permissions before installing. Use security features only with proper authorization.')
    image_tag=f'<img class="app-icon" src="../../{img}" alt="{name} app icon" width="78" height="78">' if img else f'<div class="app-icon app-icon-fallback">{esc(name[:1])}</div>'
    content=f'''<!doctype html><html lang="en" data-theme="light"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title><meta name="description" content="{description}"><meta name="robots" content="index,follow,max-image-preview:large"><link rel="canonical" href="{url}"><meta property="og:type" content="website"><meta property="og:site_name" content="Hacker Apps"><meta property="og:title" content="{title}"><meta property="og:description" content="{description}"><meta property="og:url" content="{url}"><meta name="twitter:card" content="summary"><link rel="icon" href="../../assets/images/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="../../assets/css/style.css"><script src="../../assets/js/theme.js"></script><script defer src="../../assets/js/ads.js"></script><script type="application/ld+json">{json.dumps({'@context':'https://schema.org','@type':'SoftwareApplication','name':app.get('name'),'applicationCategory':catmap.get(app.get('category'),'Application'),'operatingSystem':', '.join(app.get('platforms') or []),'description':app.get('shortDescription') or '', 'url':url, 'downloadUrl':app.get('downloadUrl') or None},ensure_ascii=False,separators=(',',':')).replace('<','\\u003c')}</script></head><body><header class="site-header"><div class="container header-inner"><a class="brand" href="../../"><span class="brand-mark">H</span><span>Hacker<span class="brand-accent">Apps</span></span></a><nav class="main-nav"><a href="../../">Discover</a><a href="../../#apps">All Apps</a><a href="../../about.html">About</a></nav><div class="header-actions"><button class="icon-button" id="themeToggle" type="button" aria-label="Toggle theme">◐</button><a class="header-download-link" href="../../#apps">Browse apps</a></div></div></header><main class="container detail-page"><div class="breadcrumbs"><a href="../../">Home</a> / <a href="../../#apps">Apps</a> / {name}</div><div class="detail-layout"><article class="detail-main"><div class="detail-title-row">{image_tag}<div><div class="card-category">{category}</div><h1>{name}</h1><div class="platform-tags">{''.join('<span>'+esc(p)+'</span>' for p in app.get('platforms') or [])}</div></div></div><p class="detail-summary">{esc(app.get('shortDescription') or '')}</p><h2>About this app</h2><p>{esc(app.get('description') or app.get('shortDescription') or 'Check the official project page for details.')}</p><h2>Key features</h2><ul>{features}</ul><div class="ad-slot" data-ad-slot="native" aria-label="Advertisement"><span class="ad-label">ADVERTISEMENT</span></div><h2>Download</h2><p>Use the official website or the linked download source to check the latest release and installation requirements.</p><div class="download-actions">{download_button}{official_button}</div><h2>Safety and responsible use</h2><p>{safety}</p><div class="ad-slot" data-ad-slot="other" aria-label="Advertisement"><span class="ad-label">ADVERTISEMENT</span></div><p class="notice">Hacker Apps is an independent directory. App availability, versions and compatibility may change; confirm details at the source before installing.</p></article><aside class="detail-side"><h2>App information</h2><div class="meta-list"><div class="meta-row"><span>Category</span><span>{category}</span></div><div class="meta-row"><span>Platforms</span><span>{esc(platforms)}</span></div><div class="meta-row"><span>License</span><span>{esc(app.get('license') or 'Not verified')}</span></div><div class="meta-row"><span>Version</span><span>{esc(app.get('version') or 'Not specified')}</span></div><div class="meta-row"><span>Last updated</span><span>{esc(app.get('updatedAt') or 'Not specified')}</span></div></div><div class="notice">Only install software from sources you trust. Review permissions and use security tools only where you have authorization.</div><div class="ad-slot" data-ad-slot="banner" aria-label="Advertisement"><span class="ad-label">ADVERTISEMENT</span></div></aside></div></main><footer class="site-footer"><div class="container footer-top"><a class="brand" href="../../"><span class="brand-mark">H</span><span>Hacker<span class="brand-accent">Apps</span></span></a><p>A focused directory for discovering cybersecurity and Android applications.</p><nav class="footer-links"><a href="../../about.html">About</a><a href="../../contact.html">Contact</a><a href="../../privacy-policy.html">Privacy</a><a href="../../terms.html">Terms</a><a href="../../disclaimer.html">Disclaimer</a></nav></div><div class="container footer-bottom"><span>© {date.today().year} Hacker Apps</span><span>Use responsibly. Verify downloads before installing.</span></div></footer></body></html>'''
    out=os.path.join(ROOT,'apps',appid,'index.html');os.makedirs(os.path.dirname(out),exist_ok=True)
    with open(out,'w',encoding='utf-8') as f:f.write(content)
    urls.append(url)
# Sitemap and robots for GitHub Pages project site.
with open(os.path.join(ROOT,'sitemap.xml'),'w',encoding='utf-8') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    for u in urls:f.write(f'  <url><loc>{esc(u)}</loc></url>\n')
    f.write('</urlset>\n')
print(f'Generated {len(urls)-6} app pages and sitemap.xml')
