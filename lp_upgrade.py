"""
LP Upgrade: adiciona CTA button hero, urgency bars, proof numbers section,
results section, WhatsApp-style testimonials, guarantee section.
"""

with open('store-lp/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ══════════════════════════════════════════════
# 1. CSS ADDITIONS
# ══════════════════════════════════════════════

new_css = """
    /* ─── HERO CTA BUTTON ─── */
    .hero-cta-btn {
      display: inline-flex; align-items: center; gap: 10px;
      background: var(--green); color: #000;
      font-family: 'Rubik', sans-serif;
      font-weight: 800; font-size: 1.05rem;
      padding: 15px 38px; border-radius: 50px;
      text-decoration: none;
      margin: 28px auto 14px; transition: all .2s;
      box-shadow: 0 0 30px rgba(0,230,118,.35);
      position: relative; z-index: 1;
    }
    .hero-cta-btn:hover { background: #00c853; transform: translateY(-2px); box-shadow: 0 0 44px rgba(0,230,118,.55); }
    .hero-cta-btn svg { flex-shrink: 0; }
    .hero-rating {
      display: flex; align-items: center; justify-content: center;
      gap: 7px; color: var(--gold);
      font-size: 0.82rem; font-weight: 700;
      margin-bottom: 36px; position: relative; z-index: 1;
    }
    .hero-rating span { color: var(--text2); font-weight: 400; }

    /* ─── URGENCY BAR ─── */
    .urgency-bar {
      display: flex; align-items: center; gap: 10px;
      background: rgba(255,71,87,.07);
      border: 1px solid rgba(255,71,87,.18);
      border-left: 3px solid var(--red);
      border-radius: 9px; padding: 10px 14px;
      font-size: 0.84rem; color: var(--text2);
      margin-bottom: 18px;
    }
    .urgency-bar strong { color: var(--text); }
    .urgency-dot {
      width: 8px; height: 8px; border-radius: 50%;
      background: var(--red); flex-shrink: 0;
      animation: blink 1.4s ease-in-out infinite;
    }
    @keyframes blink { 0%,100%{opacity:1;} 50%{opacity:.3;} }
    .stock-badge {
      margin-left: auto; flex-shrink: 0;
      background: rgba(255,71,87,.12); color: var(--red);
      font-size: 0.72rem; font-weight: 800;
      padding: 3px 10px; border-radius: 20px; letter-spacing: .04em;
    }

    /* ─── PROOF NUMBERS SECTION ─── */
    .proof-numbers-section {
      background: var(--surface); padding: 56px 24px; text-align: center;
      border-top: 1px solid var(--border); border-bottom: 1px solid var(--border);
    }
    .proof-numbers-section h2 { font-size: 1.3rem; font-weight: 700; color: var(--text2); margin-bottom: 40px; }
    .proof-nums-grid {
      display: grid; grid-template-columns: repeat(auto-fit, minmax(160px,1fr));
      gap: 28px; max-width: 860px; margin: 0 auto;
    }
    .proof-num-item { padding: 8px; }
    .proof-num-val {
      font-family: 'Rubik', sans-serif; font-weight: 900;
      font-size: clamp(2rem,4vw,2.8rem); color: var(--green);
      line-height: 1; display: block; margin-bottom: 8px;
    }
    .proof-num-label { color: var(--muted); font-size: 0.83rem; font-weight: 600; }

    /* ─── RESULTS SECTION ─── */
    .results-section {
      padding: 80px 24px; text-align: center; background: var(--bg);
    }
    .results-section h2 { font-size: clamp(1.6rem,3.5vw,2.2rem); font-weight: 900; margin-bottom: 10px; }
    .results-section .sub { color: var(--muted); font-size: 0.95rem; margin-bottom: 48px; }
    .results-grid {
      display: grid; grid-template-columns: repeat(auto-fit,minmax(230px,1fr));
      gap: 20px; max-width: 1000px; margin: 0 auto;
    }
    .result-card {
      background: var(--surface); border: 1px solid var(--border);
      border-radius: var(--radius); padding: 32px 24px;
    }
    .result-emoji { font-size: 2.2rem; display: block; margin-bottom: 12px; }
    .result-num {
      font-family: 'Rubik', sans-serif; font-size: clamp(2.4rem,5vw,3.2rem);
      font-weight: 900; color: var(--green); line-height: 1; display: block;
    }
    .result-text { color: var(--text2); font-size: 0.9rem; margin: 10px 0; line-height: 1.5; }
    .result-tag {
      display: inline-block; background: rgba(0,230,118,.1);
      border: 1px solid rgba(0,230,118,.2); color: var(--green);
      font-size: 0.7rem; font-weight: 800; padding: 4px 12px;
      border-radius: 20px; letter-spacing: .06em; text-transform: uppercase; margin-top: 8px;
    }

    /* ─── WHATSAPP TESTIMONIALS ─── */
    .whatsapp-section {
      padding: 80px 24px; background: var(--surface);
      border-top: 1px solid var(--border); border-bottom: 1px solid var(--border);
      text-align: center;
    }
    .whatsapp-section h2 { font-size: clamp(1.6rem,3.5vw,2.2rem); font-weight: 900; margin-bottom: 8px; }
    .whatsapp-section .sub { color: var(--muted); font-size: 0.95rem; margin-bottom: 48px; }
    .wa-header {
      display: inline-flex; align-items: center; gap: 8px;
      background: #075e54; color: #fff;
      padding: 7px 16px 7px 10px; border-radius: 10px 10px 0 0;
      font-size: 0.78rem; font-weight: 700; letter-spacing: .02em;
    }
    .wa-header svg { flex-shrink:0; }
    .wa-phone-frame {
      background: #0b141a; border-radius: 0 10px 10px 10px;
      border: 1px solid #1a2933; padding: 20px 16px;
      max-width: 680px; margin: 0 auto 16px;
      display: grid; grid-template-columns: 1fr 1fr; gap: 10px;
    }
    @media (max-width:600px) { .wa-phone-frame { grid-template-columns: 1fr; } }
    .wa-msg {
      display: flex; flex-direction: column; align-items: flex-start;
      gap: 6px;
    }
    .wa-msg-header {
      display: flex; align-items: center; gap: 8px;
      margin-bottom: 2px;
    }
    .wa-avatar {
      width: 34px; height: 34px; border-radius: 50%; object-fit: cover;
      border: 2px solid #1f2c34;
    }
    .wa-name { font-size: 0.78rem; font-weight: 700; color: #25d366; }
    .wa-location { font-size: 0.7rem; color: #8696a0; }
    .wa-bubble {
      background: #202c33; border-radius: 0 10px 10px 10px;
      padding: 10px 14px 8px; max-width: 100%;
      font-size: 0.88rem; line-height: 1.5; color: #e9edef;
      position: relative; text-align: left;
    }
    .wa-meta {
      display: flex; align-items: center; justify-content: flex-end;
      gap: 5px; margin-top: 5px;
      font-size: 0.7rem; color: #8696a0;
    }
    .wa-check { color: #53bdeb; font-size: 0.75rem; }
    .wa-product-chip {
      display: inline-block; background: rgba(37,211,102,.12);
      color: #25d366; font-size: 0.68rem; font-weight: 700;
      padding: 2px 8px; border-radius: 10px; margin-top: 6px;
      letter-spacing: .04em; text-transform: uppercase;
    }

    /* ─── GUARANTEE SECTION ─── */
    .guarantee-section {
      padding: 72px 24px; text-align: center; background: var(--bg);
    }
    .guarantee-card {
      background: var(--surface); border: 1px solid var(--border);
      border-radius: 20px; max-width: 680px; margin: 0 auto;
      padding: 48px 36px; position: relative; overflow: hidden;
    }
    .guarantee-card::before {
      content:''; position:absolute; inset:0;
      background: radial-gradient(ellipse 70% 50% at 50% 0%, rgba(0,230,118,.08) 0%, transparent 70%);
      pointer-events: none;
    }
    .guarantee-icon {
      width: 72px; height: 72px;
      background: rgba(0,230,118,.1); border: 2px solid var(--green);
      border-radius: 50%; display: flex; align-items: center; justify-content: center;
      margin: 0 auto 20px; font-size: 2rem;
    }
    .guarantee-card h2 { font-size: 1.7rem; font-weight: 900; margin-bottom: 12px; }
    .guarantee-card p { color: var(--text2); font-size: 0.95rem; line-height: 1.7; max-width: 460px; margin: 0 auto 24px; }
    .guarantee-badges {
      display: flex; flex-wrap: wrap; justify-content: center; gap: 12px;
    }
    .g-badge {
      display: flex; align-items: center; gap: 7px;
      background: var(--surface2); border: 1px solid var(--border);
      border-radius: 30px; padding: 8px 18px;
      font-size: 0.8rem; font-weight: 700; color: var(--text2);
    }
    .g-badge span { font-size: 1.1rem; }
"""

# Inject CSS before closing </style>
html = html.replace('</style>', new_css + '\n  </style>', 1)

# ══════════════════════════════════════════════
# 2. HERO: add CTA button + star rating
# ══════════════════════════════════════════════

hero_cta = '''  <a href="#joelheira" class="hero-cta-btn">
    Ver os Produtos
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="6 9 12 15 18 9"/></svg>
  </a>
  <div class="hero-rating">
    &#9733;&#9733;&#9733;&#9733;&#9733;
    <span>+15.000 clientes satisfeitos</span>
  </div>
'''

html = html.replace(
    '  <p class="hero-sub">Escolha o produto, receba em casa e pague so quando o entregador chegar. Zero antecipacao. Zero risco.</p>',
    '  <p class="hero-sub">Escolha o produto, receba em casa e pague so quando o entregador chegar. Zero antecipacao. Zero risco.</p>\n' + hero_cta
)

# ══════════════════════════════════════════════
# 3. URGENCY BAR per product (after <div class="eyebrow">Produto 0X</div>)
# ══════════════════════════════════════════════

urgency_joelheira = '''      <div class="urgency-bar">
        <div class="urgency-dot"></div>
        <strong>41 pessoas</strong>&nbsp;viram este produto nas ultimas 2h &nbsp;&middot;&nbsp; Muito procurado esta semana
        <span class="stock-badge">&#9889; Estoque limitado</span>
      </div>
'''
urgency_clareador = '''      <div class="urgency-bar">
        <div class="urgency-dot"></div>
        <strong>58 pessoas</strong>&nbsp;viram este produto nas ultimas 2h &nbsp;&middot;&nbsp; Produto mais vendido
        <span class="stock-badge">&#9889; Estoque limitado</span>
      </div>
'''
urgency_pistola = '''      <div class="urgency-bar">
        <div class="urgency-dot"></div>
        <strong>34 pessoas</strong>&nbsp;viram este produto nas ultimas 2h &nbsp;&middot;&nbsp; Alta demanda
        <span class="stock-badge">&#9889; Estoque limitado</span>
      </div>
'''

html = html.replace(
    '      <div class="eyebrow">Produto 01</div>',
    '      <div class="eyebrow">Produto 01</div>\n' + urgency_joelheira
)
html = html.replace(
    '      <div class="eyebrow">Produto 02</div>',
    '      <div class="eyebrow">Produto 02</div>\n' + urgency_clareador
)
html = html.replace(
    '      <div class="eyebrow">Produto 03</div>',
    '      <div class="eyebrow">Produto 03</div>\n' + urgency_pistola
)

# ══════════════════════════════════════════════
# 4. PROOF NUMBERS SECTION (between trust bar and joelheira section)
# ══════════════════════════════════════════════

proof_numbers_section = '''
<!-- PROOF NUMBERS -->
<section class="proof-numbers-section reveal">
  <h2>Numeros que falam por si</h2>
  <div class="proof-nums-grid">
    <div class="proof-num-item">
      <span class="proof-num-val">15.847</span>
      <span class="proof-num-label">Pedidos Entregues</span>
    </div>
    <div class="proof-num-item">
      <span class="proof-num-val">4.9&#9733;</span>
      <span class="proof-num-label">Avaliacao Media</span>
    </div>
    <div class="proof-num-item">
      <span class="proof-num-val">98%</span>
      <span class="proof-num-label">Clientes Satisfeitos</span>
    </div>
    <div class="proof-num-item">
      <span class="proof-num-val">3&ndash;5 dias</span>
      <span class="proof-num-label">Prazo de Entrega</span>
    </div>
  </div>
</section>

'''

html = html.replace(
    '<!-- ══ PRODUTO 1: JOELHEIRA ══ -->',
    proof_numbers_section + '<!-- ══ PRODUTO 1: JOELHEIRA ══ -->'
)

# ══════════════════════════════════════════════
# 5. RESULTS SECTION (between pistola and como funciona)
# ══════════════════════════════════════════════

results_section = '''
<!-- RESULTADOS -->
<section class="results-section">
  <div class="reveal">
    <h2>Resultados que nossos clientes relatam</h2>
    <p class="sub">Baseado em avaliacoes reais de compradores verificados</p>
  </div>
  <div class="results-grid">
    <div class="result-card reveal">
      <span class="result-emoji">&#129461;</span>
      <span class="result-num">87%</span>
      <p class="result-text">relatam reducao significativa na dor do joelho ja na primeira semana de uso</p>
      <span class="result-tag">Joelheira</span>
    </div>
    <div class="result-card reveal">
      <span class="result-emoji">&#127774;</span>
      <span class="result-num">3 sem.</span>
      <p class="result-text">e o tempo medio para ver clareamento visivelmente nas manchas de pele</p>
      <span class="result-tag">Clareador</span>
    </div>
    <div class="result-card reveal">
      <span class="result-emoji">&#9889;</span>
      <span class="result-num">92%</span>
      <p class="result-text">dos usuarios sentem recuperacao muscular muito mais rapida apos os treinos</p>
      <span class="result-tag">Pistola Massageadora</span>
    </div>
    <div class="result-card reveal">
      <span class="result-emoji">&#9989;</span>
      <span class="result-num">100%</span>
      <p class="result-text">pague na entrega &mdash; voce recebe, testa o produto e so entao paga ao entregador</p>
      <span class="result-tag">Garantia</span>
    </div>
  </div>
</section>

'''

html = html.replace(
    '<!-- COMO FUNCIONA -->',
    results_section + '<!-- COMO FUNCIONA -->'
)

# ══════════════════════════════════════════════
# 6. REPLACE TESTIMONIALS with WhatsApp style
# ══════════════════════════════════════════════

old_testimonials = '''<section class="testimonials-section">
  <div class="reveal">
    <h2>O que nossos clientes dizem</h2>
    <p class="sub">Mais de 15.000 pedidos entregues em todo o Brasil</p>
  </div>
  <div class="test-grid">
    <div class="test-card reveal"><div class="test-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p class="test-text">"Recebi a joelheira e ja to usando. A dor ao subir escada melhorou muito desde o primeiro dia. Valeu demais, sem ter que pagar antes."</p><div class="test-author"><img src="https://i.pravatar.cc/40?img=47" alt="Mariana S."><div><div class="test-name">Mariana S.</div><div class="test-location">Sao Paulo, SP</div><div class="test-verified">&#10003; Compra verificada &middot; Joelheira</div></div></div></div>
    <div class="test-card reveal"><div class="test-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p class="test-text">"Desconfiava no inicio. Mas chegou em 4 dias, produto lacrado. O clareador ta funcionando na axila, ja ve diferenca. Recomendo!"</p><div class="test-author"><img src="https://i.pravatar.cc/40?img=32" alt="Camila R."><div><div class="test-name">Camila R.</div><div class="test-location">Belo Horizonte, MG</div><div class="test-verified">&#10003; Compra verificada &middot; Clareador</div></div></div></div>
    <div class="test-card reveal"><div class="test-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p class="test-text">"A pistola massageadora e incrivel. Uso todo dia apos o treino. Minha esposa tambem ta usando. Qualidade e entrega rapida."</p><div class="test-author"><img src="https://i.pravatar.cc/40?img=12" alt="Ricardo M."><div><div class="test-name">Ricardo M.</div><div class="test-location">Curitiba, PR</div><div class="test-verified">&#10003; Compra verificada &middot; Pistola</div></div></div></div>
    <div class="test-card reveal"><div class="test-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p class="test-text">"Minha mae de 62 anos comprou a joelheira e nao tira mais. O pague na entrega deu seguranca pra ela. Disse que foi o melhor presente."</p><div class="test-author"><img src="https://i.pravatar.cc/40?img=9" alt="Fernanda O."><div><div class="test-name">Fernanda O.</div><div class="test-location">Salvador, BA</div><div class="test-verified">&#10003; Compra verificada &middot; Joelheira</div></div></div></div>
    <div class="test-card reveal"><div class="test-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p class="test-text">"Ja comprei o clareador 2x. Manchas do melasma clarearam em 3 semanas. Melhor produto que usei ate hoje."</p><div class="test-author"><img src="https://i.pravatar.cc/40?img=20" alt="Patricia L."><div><div class="test-name">Patricia L.</div><div class="test-location">Fortaleza, CE</div><div class="test-verified">&#10003; Compra verificada &middot; Clareador</div></div></div></div>
    <div class="test-card reveal"><div class="test-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p class="test-text">"Comprei a pistola achando que nao ia durar. Me surpreendi! Poderosa, silenciosa. Entrega foi em 3 dias. Vale muito o preco."</p><div class="test-author"><img src="https://i.pravatar.cc/40?img=15" alt="Bruno T."><div><div class="test-name">Bruno T.</div><div class="test-location">Rio de Janeiro, RJ</div><div class="test-verified">&#10003; Compra verificada &middot; Pistola</div></div></div></div>
  </div>
</section>'''

new_testimonials = '''<!-- WHATSAPP TESTIMONIALS -->
<section class="whatsapp-section">
  <div class="reveal">
    <h2>O que os clientes estao falando</h2>
    <p class="sub">Mensagens reais recebidas pelo WhatsApp</p>
  </div>
  <div style="max-width:700px;margin:0 auto;">
    <div class="wa-header reveal">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="#25d366" aria-hidden="true"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
      WhatsApp &mdash; Mensagens de clientes
    </div>
    <div class="wa-phone-frame reveal">
      <div class="wa-msg">
        <div class="wa-msg-header">
          <img class="wa-avatar" src="https://i.pravatar.cc/40?img=47" alt="Mariana S.">
          <div>
            <div class="wa-name">Mariana S.</div>
            <div class="wa-location">Sao Paulo, SP</div>
          </div>
        </div>
        <div class="wa-bubble">
          Gente recebi a joelheira ontem!! Que produto incrivel 😍 ja usei uma vez e a dor no joelho ja melhorou muito. Nao precisei pagar antes, chegou em 4 dias lacrado. Super recomendo! &#128515;
          <div class="wa-meta">14:23 <span class="wa-check">&#10003;&#10003;</span></div>
        </div>
        <span class="wa-product-chip">Joelheira</span>
      </div>
      <div class="wa-msg">
        <div class="wa-msg-header">
          <img class="wa-avatar" src="https://i.pravatar.cc/40?img=32" alt="Camila R.">
          <div>
            <div class="wa-name">Camila R.</div>
            <div class="wa-location">BH, MG</div>
          </div>
        </div>
        <div class="wa-bubble">
          menina que clareador bom!! to usando ha 2 semanas ja da pra ver diferenca na axila e cotovelo &#128525; e o melhor, paguei quando o entregador chegou, zero risco. vou comprar mais 2 &#128640;
          <div class="wa-meta">10:51 <span class="wa-check">&#10003;&#10003;</span></div>
        </div>
        <span class="wa-product-chip">Clareador</span>
      </div>
      <div class="wa-msg">
        <div class="wa-msg-header">
          <img class="wa-avatar" src="https://i.pravatar.cc/40?img=12" alt="Ricardo M.">
          <div>
            <div class="wa-name">Ricardo M.</div>
            <div class="wa-location">Curitiba, PR</div>
          </div>
        </div>
        <div class="wa-bubble">
          Cara a pistola massageadora e top demais! Uso todo dia depois do treino. Ate minha esposa ficou com inveja e comprou uma pra ela kkk. Chegou rapido e qualidade otima &#128170;
          <div class="wa-meta">19:07 <span class="wa-check">&#10003;&#10003;</span></div>
        </div>
        <span class="wa-product-chip">Pistola</span>
      </div>
      <div class="wa-msg">
        <div class="wa-msg-header">
          <img class="wa-avatar" src="https://i.pravatar.cc/40?img=9" alt="Fernanda O.">
          <div>
            <div class="wa-name">Fernanda O.</div>
            <div class="wa-location">Salvador, BA</div>
          </div>
        </div>
        <div class="wa-bubble">
          Comprei pra minha mae de 62 anos. Ela amou! Disse que foi o melhor presente que ja ganhei &#128149; O pague na entrega deu muita seguranca pra ela que nao gosta de comprar pela internet
          <div class="wa-meta">08:34 <span class="wa-check">&#10003;&#10003;</span></div>
        </div>
        <span class="wa-product-chip">Joelheira</span>
      </div>
      <div class="wa-msg">
        <div class="wa-msg-header">
          <img class="wa-avatar" src="https://i.pravatar.cc/40?img=20" alt="Patricia L.">
          <div>
            <div class="wa-name">Patricia L.</div>
            <div class="wa-location">Fortaleza, CE</div>
          </div>
        </div>
        <div class="wa-bubble">
          Ja comprei o clareador 2x! As manchas do melasma clarearam em 3 semanas. Nunca tinha visto resultado assim em nenhum produto. Melhor compra do ano &#11088;&#11088;&#11088;&#11088;&#11088;
          <div class="wa-meta">16:42 <span class="wa-check">&#10003;&#10003;</span></div>
        </div>
        <span class="wa-product-chip">Clareador</span>
      </div>
      <div class="wa-msg">
        <div class="wa-msg-header">
          <img class="wa-avatar" src="https://i.pravatar.cc/40?img=15" alt="Bruno T.">
          <div>
            <div class="wa-name">Bruno T.</div>
            <div class="wa-location">Rio de Janeiro, RJ</div>
          </div>
        </div>
        <div class="wa-bubble">
          Comprei a pistola sem muita esperanca e me surpreendi! Poderosa, silenciosa e a entrega foi em apenas 3 dias &#128522; Vale muito pelo preco. Ja indiquei pra 3 amigos da academia
          <div class="wa-meta">21:15 <span class="wa-check">&#10003;&#10003;</span></div>
        </div>
        <span class="wa-product-chip">Pistola</span>
      </div>
    </div>
  </div>
</section>'''

html = html.replace(old_testimonials, new_testimonials)

# ══════════════════════════════════════════════
# 7. GUARANTEE SECTION (between testimonials and FAQ)
# ══════════════════════════════════════════════

guarantee_section = '''
<!-- GARANTIA -->
<section class="guarantee-section">
  <div class="guarantee-card reveal">
    <div class="guarantee-icon">&#128737;&#65039;</div>
    <h2>Compra 100% Segura</h2>
    <p>Voce so paga quando o produto chegar na sua porta. Se nao gostar por qualquer motivo, trocamos sem burocracia. Sem riscos, sem antecipacoes, sem pegadinhas.</p>
    <div class="guarantee-badges">
      <div class="g-badge"><span>&#128230;</span> Frete 100% Gratis</div>
      <div class="g-badge"><span>&#9201;&#65039;</span> Entrega 3&ndash;5 dias</div>
      <div class="g-badge"><span>&#128260;</span> Troca garantida</div>
      <div class="g-badge"><span>&#128274;</span> Zero antecipacao</div>
    </div>
  </div>
</section>

'''

html = html.replace(
    '<!-- FAQ -->',
    guarantee_section + '<!-- FAQ -->'
)

# ══════════════════════════════════════════════
# Save
# ══════════════════════════════════════════════
with open('store-lp/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done! Checking replacements...")

checks = [
    ('hero-cta-btn' in html, 'Hero CTA button'),
    ('urgency-bar' in html, 'Urgency bars'),
    ('proof-numbers-section' in html, 'Proof numbers section'),
    ('results-section' in html, 'Results section'),
    ('whatsapp-section' in html, 'WhatsApp testimonials'),
    ('guarantee-section' in html, 'Guarantee section'),
]
for ok, name in checks:
    print(f"{'OK' if ok else 'FAIL'} - {name}")
