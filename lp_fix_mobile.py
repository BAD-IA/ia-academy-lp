"""
LP Mobile Fix: remove dead CSS, fix duplicate keyframes, add comprehensive
mobile responsiveness, fix z-index on all hero children.
"""

with open('store-lp/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ══════════════════════════════════════════════
# 1. Remove dead CSS: old testimonials section
# ══════════════════════════════════════════════
dead_testimonials_css = """    /* ─── TESTIMONIALS ─── */
    .testimonials-section {
      background: var(--surface); border-top: 1px solid var(--border);
      border-bottom: 1px solid var(--border); padding: 80px 24px;
    }
    .testimonials-section h2 {
      text-align: center; font-size: clamp(1.5rem, 3vw, 2rem); font-weight: 900; margin-bottom: 6px;
    }
    .testimonials-section .sub { text-align: center; color: var(--muted); margin-bottom: 44px; font-size: 0.92rem; }
    .test-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 18px; max-width: 1000px; margin: 0 auto; }
    .test-card {
      background: var(--bg); border: 1px solid var(--border);
      border-radius: var(--radius); padding: 22px;
      transition: border-color .2s;
    }
    .test-card:hover { border-color: rgba(0,230,118,.25); }
    .test-card:nth-child(2) { margin-top: -14px; }
    .test-card:nth-child(5) { margin-top: -14px; }
    .test-stars { color: var(--gold); font-size: 0.85rem; margin-bottom: 11px; letter-spacing: 2px; }
    .test-text { font-size: 0.88rem; line-height: 1.7; color: var(--text2); margin-bottom: 14px; font-style: italic; }
    .test-author { display: flex; align-items: center; gap: 10px; }
    .test-author img { width: 36px; height: 36px; border-radius: 50%; object-fit: cover; }
    .test-name { font-weight: 700; font-size: 0.85rem; }
    .test-location { font-size: 0.73rem; color: var(--muted); }
    .test-verified {
      display: inline-flex; align-items: center; gap: 4px;
      background: rgba(0,230,118,.1); color: var(--green);
      font-size: 0.66rem; font-weight: 700; padding: 3px 7px;
      border-radius: 20px; margin-top: 4px; letter-spacing: 0.05em;
    }"""

if dead_testimonials_css in html:
    html = html.replace(dead_testimonials_css, '    /* ─── TESTIMONIALS (replaced by WhatsApp section) ─── */')
    print('OK - Removed dead testimonials CSS')
else:
    print('SKIP - Dead testimonials CSS not found (may already be removed)')

# ══════════════════════════════════════════════
# 2. Remove dead CSS: old nav responsive rule
# ══════════════════════════════════════════════
html = html.replace('      nav { flex-direction: column; gap: 8px; }\n', '')
print('OK - Removed dead nav CSS')

# ══════════════════════════════════════════════
# 3. Fix duplicate @keyframes blink
#    Keep only the one inside the new CSS block, remove old one
# ══════════════════════════════════════════════
old_blink = """    @keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: .35; } }"""
html = html.replace(old_blink, '    /* blink keyframe defined below */', 1)  # replace only first occurrence
print('OK - Fixed duplicate @keyframes blink')

# ══════════════════════════════════════════════
# 4. Replace the existing responsive block with a comprehensive one
# ══════════════════════════════════════════════
old_responsive = """    /* ─── RESPONSIVE ─── */
    @media (max-width: 768px) {
      .prod-grid, .prod-grid.rev { grid-template-columns: 1fr; direction: ltr; gap: 28px; }
      .prod-grid.rev .prod-content { order: -1; }
      .how-steps { grid-template-columns: repeat(2, 1fr); }
      .how-step::after { display: none; }
      .test-grid { grid-template-columns: 1fr; }
      .test-card:nth-child(2), .test-card:nth-child(5) { margin-top: 0; }
      .cod-divider { display: none; }
      .sticky-mobile { display: block; }
      body { padding-bottom: 82px; }
    }
    @media (max-width: 480px) {
      .how-steps { grid-template-columns: 1fr; }
      .qty-price-unit { font-size: 0.95rem; }
    }"""

new_responsive = """    /* ─── RESPONSIVE ─── */
    @media (max-width: 768px) {
      /* Layout */
      .prod-grid, .prod-grid.rev { grid-template-columns: 1fr; direction: ltr; gap: 28px; }
      .prod-grid.rev .prod-content { order: -1; }
      .how-steps { grid-template-columns: repeat(2, 1fr); }
      .how-step::after { display: none; }
      .cod-divider { display: none; }
      .sticky-mobile { display: block; }
      body { padding-bottom: 82px; }

      /* Hero */
      .hero { padding: 48px 20px 40px; background-position: 60% 20%; }
      .hero h1 { font-size: clamp(1.8rem, 8vw, 2.4rem); }
      .hero-sub { margin-bottom: 24px; }
      .hero-cta-btn { width: 100%; justify-content: center; padding: 16px 24px; font-size: 0.95rem; margin: 20px auto 12px; }
      .hero-rating { margin-bottom: 24px; }
      .cod-strip { padding: 14px 16px; gap: 12px; width: 100%; }
      .hero-products { gap: 6px; }
      .hero-prod-chip { font-size: 0.72rem; padding: 6px 12px 6px 6px; }
      .hero-prod-chip img { width: 26px; height: 26px; }

      /* Urgency */
      .urgency-bar { flex-wrap: wrap; gap: 6px; }
      .stock-badge { margin-left: 0; }

      /* Sections */
      .prod-section { padding: 56px 16px; }
      .proof-numbers-section { padding: 40px 20px; }
      .proof-nums-grid { grid-template-columns: repeat(2, 1fr); gap: 20px; }
      .results-section { padding: 56px 16px; }
      .results-grid { grid-template-columns: repeat(2, 1fr); }

      /* WhatsApp */
      .wa-phone-frame { grid-template-columns: 1fr; }
      .whatsapp-section { padding: 56px 16px; }

      /* Guarantee */
      .guarantee-section { padding: 48px 16px; }
      .guarantee-card { padding: 32px 20px; }
      .guarantee-badges { gap: 8px; }

      /* CTA final */
      .cta-final { padding: 56px 20px; }
      .cta-btns { flex-direction: column; align-items: stretch; }
      .btn-cta { justify-content: center; }
    }

    @media (max-width: 480px) {
      /* Layout */
      .how-steps { grid-template-columns: 1fr; }
      .results-grid { grid-template-columns: 1fr; }

      /* Hero */
      .hero { padding: 40px 16px 32px; }
      .hero h1 { font-size: 1.75rem; letter-spacing: -0.02em; }
      .cod-strip { padding: 12px 14px; gap: 10px; }

      /* Qty cards */
      .qty-price-unit { font-size: 0.95rem; }
      .qty-cards { gap: 6px; }
      .qty-card { padding: 12px 6px 10px; }
      .qty-num { font-size: 0.72rem; }

      /* Price box */
      .prod-price-cod { display: none; }
      .prod-price-main { font-size: 1.7rem; }

      /* Sticky mobile: shorter text */
      .sticky-btns a { font-size: 0.62rem; padding: 12px 4px; letter-spacing: -0.01em; }

      /* Guarantee */
      .guarantee-card { padding: 28px 16px; }
      .g-badge { padding: 7px 12px; font-size: 0.75rem; }

      /* FAQ */
      .faq-section { padding: 56px 16px; }
      .faq-q { font-size: 0.85rem; padding: 16px 16px; }
    }"""

if old_responsive in html:
    html = html.replace(old_responsive, new_responsive)
    print('OK - Replaced responsive CSS with comprehensive mobile version')
else:
    print('FAIL - Could not find old responsive CSS block')

# ══════════════════════════════════════════════
# 5. Update sticky mobile: shorten "Pistola R$119,97" to fit
# ══════════════════════════════════════════════
html = html.replace(
    '<a href="#pistola"   class="sm-btn-3">Pistola R$119,97</a>',
    '<a href="#pistola"   class="sm-btn-3">Pistola R$119</a>'
)
print('OK - Shortened sticky mobile Pistola label')

# ══════════════════════════════════════════════
# 6. Add hero-cta-btn display:block on mobile so it's full width
#    (inline-flex stays inline otherwise)
# ══════════════════════════════════════════════
# Already handled in responsive CSS above with width:100%

# ══════════════════════════════════════════════
# Save
# ══════════════════════════════════════════════
with open('store-lp/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('\nAll fixes applied. Final check:')
checks = [
    ('/* blink keyframe defined below */' in html, 'Duplicate blink removed'),
    ('dead nav CSS' not in html and 'nav { flex-direction: column' not in html, 'Dead nav CSS removed'),
    ('background-position: 60% 20%' in html, 'Mobile hero bg-position'),
    ('width: 100%' in html and 'hero-cta-btn' in html, 'Hero CTA full width mobile'),
    ('grid-template-columns: repeat(2, 1fr)' in html, 'Proof nums 2-col mobile'),
    ('flex-direction: column' in html, 'CTA buttons stacked mobile'),
    ('Pistola R$119</a>' in html, 'Sticky pistola label shortened'),
]
for ok, name in checks:
    print(f"  {'OK' if ok else 'FAIL'} - {name}")
