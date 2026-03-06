import re

with open('store-lp/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ── LINKS ──────────────────────────────────────────────────────────────────────
html = html.replace('LINK_JOELHEIRA_1x', 'https://app.coinzz.com.br/checkout/joelheira-premium-vne4y-1291')
html = html.replace('LINK_JOELHEIRA_2x', 'https://app.coinzz.com.br/checkout/joelheira-premium---2-unidades-1291')
html = html.replace('LINK_JOELHEIRA_3x', 'https://app.coinzz.com.br/checkout/joelheira-premium---2-unidades-1291')
html = html.replace('LINK_CLAREADOR_1x', 'https://app.coinzz.com.br/checkout/sabonete-em-pasta-clareador-moajy-1249')
html = html.replace('LINK_CLAREADOR_2x', 'https://app.coinzz.com.br/checkout/sabonete-clareador---2-unidades-1249')
html = html.replace('LINK_CLAREADOR_3x', 'https://app.coinzz.com.br/checkout/sabonete-clareador---3-unidades---tratamento-completo-1249')
html = html.replace('LINK_PISTOLA_1x',   'https://app.coinzz.com.br/checkout/pistola-massageadora-customizada-1292')
html = html.replace('LINK_PISTOLA_2x',   'https://app.coinzz.com.br/checkout/pistola-massageadora-customizada-2-unidades-1292')
html = html.replace('LINK_PISTOLA_3x',   'https://app.coinzz.com.br/checkout/pistola-massageadora-customizada-2-unidades-1292')

# ── JS PRODUCT DATA ────────────────────────────────────────────────────────────
old_js = """    joelheira: { tiers: {
      1: { label: '1 Joelheira',  total: 97,   inst: '4x de R$ 24,25', link: 'LINK_JOELHEIRA_1x' },
      2: { label: '2 Joelheiras', total: 170,  inst: '4x de R$ 42,50', link: 'LINK_JOELHEIRA_2x' },
      3: { label: '3 Joelheiras', total: 225,  inst: '4x de R$ 56,25', link: 'LINK_JOELHEIRAS_3x' }
    }},
    clareador: { tiers: {
      1: { label: '1 Clareador',  total: 97,   inst: '4x de R$ 24,25', link: 'LINK_CLAREADOR_1x' },
      2: { label: '2 Claradores', total: 170,  inst: '4x de R$ 42,50', link: 'LINK_CLAREADOR_2x' },
      3: { label: '3 Claradores', total: 225,  inst: '4x de R$ 56,25', link: 'LINK_CLAREADOR_3x' }
    }},
    pistola: { tiers: {
      1: { label: '1 Pistola',  total: 127,  inst: '4x de R$ 31,75', link: 'LINK_PISTOLA_1x' },
      2: { label: '2 Pistolas', total: 220,  inst: '4x de R$ 55,00', link: 'LINK_PISTOLA_2x' },
      3: { label: '3 Pistolas', total: 285,  inst: '4x de R$ 71,25', link: 'LINK_PISTOLA_3x' }
    }}"""

# The links are already replaced above, so we need to search for the already-replaced version
# Let's do a targeted replacement of the JS totals and labels
html = re.sub(
    r"joelheira: \{ tiers: \{.*?\}\}",
    """joelheira: { tiers: {
      1: { label: '1 Joelheira',  total: 97,     inst: '4x de R$ 24,25', link: 'https://app.coinzz.com.br/checkout/joelheira-premium-vne4y-1291' },
      2: { label: '2 Joelheiras', total: 119.97, inst: '4x de R$ 29,99', link: 'https://app.coinzz.com.br/checkout/joelheira-premium---2-unidades-1291' },
      3: { label: '2 Joelheiras', total: 119.97, inst: '4x de R$ 29,99', link: 'https://app.coinzz.com.br/checkout/joelheira-premium---2-unidades-1291' }
    }}""",
    html, flags=re.DOTALL
)
html = re.sub(
    r"clareador: \{ tiers: \{.*?\}\}",
    """clareador: { tiers: {
      1: { label: '1 Clareador',  total: 97,     inst: '4x de R$ 24,25', link: 'https://app.coinzz.com.br/checkout/sabonete-em-pasta-clareador-moajy-1249' },
      2: { label: '2 Claradores', total: 124.97, inst: '4x de R$ 31,24', link: 'https://app.coinzz.com.br/checkout/sabonete-clareador---2-unidades-1249' },
      3: { label: '3 Claradores', total: 197,    inst: '4x de R$ 49,25', link: 'https://app.coinzz.com.br/checkout/sabonete-clareador---3-unidades---tratamento-completo-1249' }
    }}""",
    html, flags=re.DOTALL
)
html = re.sub(
    r"pistola: \{ tiers: \{.*?\}\}",
    """pistola: { tiers: {
      1: { label: '1 Pistola',  total: 119.97, inst: '4x de R$ 29,99', link: 'https://app.coinzz.com.br/checkout/pistola-massageadora-customizada-1292' },
      2: { label: '2 Pistolas', total: 197,    inst: '4x de R$ 49,25', link: 'https://app.coinzz.com.br/checkout/pistola-massageadora-customizada-2-unidades-1292' },
      3: { label: '2 Pistolas', total: 197,    inst: '4x de R$ 49,25', link: 'https://app.coinzz.com.br/checkout/pistola-massageadora-customizada-2-unidades-1292' }
    }}""",
    html, flags=re.DOTALL
)

# ── HERO CHIP PISTOLA PRICE ────────────────────────────────────────────────────
html = html.replace('Pistola &mdash; R$127', 'Pistola &mdash; R$119,97')
html = html.replace('Pistola R$127', 'Pistola R$119,97')

# ── JOELHEIRA QTY CARDS ────────────────────────────────────────────────────────
html = html.replace(
    '<div class="qty-card" data-qty="2" onclick="selectQty(\'joelheira\',2)" role="button" aria-pressed="false" tabindex="0">\n            <div class="qty-tag popular">+ Popular</div>\n            <div class="qty-num">2 unidades</div>\n            <div class="qty-price-unit">R$ 85/un</div>\n            <div class="qty-price-total">R$ 170,00 total</div>\n            <div class="qty-save">Economize R$ 24</div>',
    '<div class="qty-card" data-qty="2" onclick="selectQty(\'joelheira\',2)" role="button" aria-pressed="false" tabindex="0">\n            <div class="qty-tag popular">+ Popular</div>\n            <div class="qty-num">2 unidades</div>\n            <div class="qty-price-unit">R$ 59,99/un</div>\n            <div class="qty-price-total">R$ 119,97 total</div>\n            <div class="qty-save">Economize R$ 74,03</div>'
)
html = html.replace(
    '<div class="qty-card" data-qty="3" onclick="selectQty(\'joelheira\',3)" role="button" aria-pressed="false" tabindex="0">',
    '<div class="qty-card" data-qty="3" onclick="selectQty(\'joelheira\',3)" role="button" aria-pressed="false" tabindex="0" style="display:none">'
)

# ── CLAREADOR QTY CARDS ────────────────────────────────────────────────────────
html = html.replace(
    '<div class="qty-card" data-qty="2" onclick="selectQty(\'clareador\',2)" role="button" aria-pressed="false" tabindex="0">\n            <div class="qty-tag popular">+ Popular</div>\n            <div class="qty-num">2 unidades</div>\n            <div class="qty-price-unit">R$ 85/un</div>\n            <div class="qty-price-total">R$ 170,00 total</div>\n            <div class="qty-save">Economize R$ 24</div>',
    '<div class="qty-card" data-qty="2" onclick="selectQty(\'clareador\',2)" role="button" aria-pressed="false" tabindex="0">\n            <div class="qty-tag popular">+ Popular</div>\n            <div class="qty-num">2 unidades</div>\n            <div class="qty-price-unit">R$ 62,49/un</div>\n            <div class="qty-price-total">R$ 124,97 total</div>\n            <div class="qty-save">Economize R$ 69,03</div>'
)
html = html.replace(
    '<div class="qty-price-unit">R$ 75/un</div>\n            <div class="qty-price-total">R$ 225,00 total</div>\n            <div class="qty-save">Economize R$ 66</div>',
    '<div class="qty-price-unit">R$ 65,67/un</div>\n            <div class="qty-price-total">R$ 197,00 total</div>\n            <div class="qty-save">Economize R$ 94,00</div>'
)

# ── PISTOLA QTY CARDS ─────────────────────────────────────────────────────────
html = html.replace(
    '<div class="qty-card active" data-qty="1" onclick="selectQty(\'pistola\',1)" role="button" aria-pressed="true" tabindex="0">\n            <div class="qty-num">1 unidade</div>\n            <div class="qty-price-unit">R$ 127</div>\n            <div class="qty-price-total">R$ 127,00 total</div>',
    '<div class="qty-card active" data-qty="1" onclick="selectQty(\'pistola\',1)" role="button" aria-pressed="true" tabindex="0">\n            <div class="qty-num">1 unidade</div>\n            <div class="qty-price-unit">R$ 119,97</div>\n            <div class="qty-price-total">R$ 119,97 total</div>'
)
html = html.replace(
    '<div class="qty-card" data-qty="2" onclick="selectQty(\'pistola\',2)" role="button" aria-pressed="false" tabindex="0">\n            <div class="qty-tag popular">+ Popular</div>\n            <div class="qty-num">2 unidades</div>\n            <div class="qty-price-unit">R$ 110/un</div>\n            <div class="qty-price-total">R$ 220,00 total</div>\n            <div class="qty-save">Economize R$ 34</div>',
    '<div class="qty-card" data-qty="2" onclick="selectQty(\'pistola\',2)" role="button" aria-pressed="false" tabindex="0">\n            <div class="qty-tag popular">+ Popular</div>\n            <div class="qty-num">2 unidades</div>\n            <div class="qty-price-unit">R$ 98,50/un</div>\n            <div class="qty-price-total">R$ 197,00 total</div>\n            <div class="qty-save">Economize R$ 42,94</div>'
)
html = html.replace(
    '<div class="qty-card" data-qty="3" onclick="selectQty(\'pistola\',3)" role="button" aria-pressed="false" tabindex="0">',
    '<div class="qty-card" data-qty="3" onclick="selectQty(\'pistola\',3)" role="button" aria-pressed="false" tabindex="0" style="display:none">'
)

# ── PISTOLA PRICE BOX + BUTTON ────────────────────────────────────────────────
html = html.replace(
    '<div class="prod-price-main" id="price-pistola">R$ 127,00</div>\n          <div class="prod-price-inst" id="inst-pistola">ou 4x de R$ 31,75 sem juros</div>',
    '<div class="prod-price-main" id="price-pistola">R$ 119,97</div>\n          <div class="prod-price-inst" id="inst-pistola">ou 4x de R$ 29,99 sem juros</div>'
)
html = html.replace(
    'Quero 1 Pistola &mdash; R$ 127,00',
    'Quero 1 Pistola &mdash; R$ 119,97'
)

# ── HERO BACKGROUND IMAGE ─────────────────────────────────────────────────────
old_hero_css = """    .hero {
      padding: 72px 24px 56px; text-align: center;
      position: relative; overflow: hidden;
    }
    .hero::before {
      content: ''; position: absolute; inset: 0;
      background: radial-gradient(ellipse 90% 55% at 50% 0%, rgba(0,230,118,.1) 0%, transparent 70%);
      pointer-events: none;
    }"""
new_hero_css = """    .hero {
      padding: 72px 24px 56px; text-align: center;
      position: relative; overflow: hidden;
      background-image: url('https://images.unsplash.com/photo-1571019614242-c5c5dee9f50b?w=1600&q=80');
      background-size: cover;
      background-position: center 25%;
      background-repeat: no-repeat;
    }
    .hero::before {
      content: ''; position: absolute; inset: 0;
      background:
        linear-gradient(to bottom, rgba(11,11,16,0.82) 0%, rgba(11,11,16,0.70) 40%, rgba(11,11,16,0.88) 100%),
        radial-gradient(ellipse 90% 55% at 50% 0%, rgba(0,230,118,.10) 0%, transparent 70%);
      pointer-events: none;
    }"""
html = html.replace(old_hero_css, new_hero_css)

with open('store-lp/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Done! Checking remaining LINK_ placeholders:')
import re
links = re.findall(r'LINK_\w+', html)
print('Remaining:', links if links else 'None - all replaced!')
print('Pistola price check:', 'R$ 119,97' in html)
print('Joelheira 2x check:', 'R$ 59,99/un' in html)
print('Clareador 2x check:', 'R$ 62,49/un' in html)
print('Hero bg check:', 'unsplash' in html)
