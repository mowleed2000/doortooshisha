import os

target_dir = r"C:\Users\fifia\.gemini\antigravity\scratch\shisha-delivery-london"
os.makedirs(target_dir, exist_ok=True)

# 1. STYLE.CSS
css_content = """
:root {
    --bg-dark: #07080B;
    --bg-card: #0F1117;
    --bg-card-hover: #171A24;
    --gold: #D4AF37;
    --gold-light: #F3E5AB;
    --gold-gradient: linear-gradient(135deg, #FFD700 0%, #D4AF37 50%, #AA820A 100%);
    --neon-red: #FF3366;
    --neon-blue: #00D2FF;
    --text-white: #FFFFFF;
    --text-gray: #94A3B8;
    --border-gold: rgba(212, 175, 55, 0.3);
    --shadow-glow: 0 10px 30px rgba(212, 175, 55, 0.15);
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
}

body {
    background-color: var(--bg-dark);
    color: var(--text-white);
    line-height: 1.6;
    overflow-x: hidden;
}

h1, h2, h3, h4 {
    font-family: 'Cinzel', serif;
    letter-spacing: 1px;
}

/* Top Announcement Bar */
.top-announcement {
    background: linear-gradient(90deg, #11131A, #1F190B, #11131A);
    border-bottom: 1px solid var(--border-gold);
    color: var(--gold-light);
    padding: 10px 5%;
    font-size: 0.85rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.top-announcement div {
    display: flex;
    gap: 20px;
    align-items: center;
}

.top-announcement i {
    color: var(--gold);
    margin-right: 6px;
}

/* Header & Nav */
header {
    background: rgba(7, 8, 11, 0.95);
    backdrop-filter: blur(12px);
    position: sticky;
    top: 0;
    z-index: 1000;
    border-bottom: 1px solid rgba(255,255,255,0.05);
}

.nav-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 18px 5%;
}

.logo {
    display: flex;
    align-items: center;
    gap: 12px;
    text-decoration: none;
}

.logo-icon {
    font-size: 2rem;
    background: var(--gold-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.logo-text h1 {
    font-size: 1.3rem;
    font-weight: 700;
    color: #FFF;
    line-height: 1.1;
}

.logo-text span {
    font-size: 0.7rem;
    text-transform: uppercase;
    letter-spacing: 2px;
    color: var(--gold);
}

nav ul {
    display: flex;
    list-style: none;
    gap: 30px;
}

nav a {
    text-decoration: none;
    color: var(--text-gray);
    font-size: 0.95rem;
    font-weight: 500;
    transition: all 0.3s ease;
}

nav a:hover, nav a.active {
    color: var(--gold);
}

.btn-gold {
    background: var(--gold-gradient);
    color: #07080B;
    padding: 12px 26px;
    border-radius: 4px;
    font-weight: 700;
    font-size: 0.95rem;
    border: none;
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: 8px;
    text-decoration: none;
    box-shadow: 0 4px 20px rgba(212, 175, 55, 0.3);
    transition: all 0.3s ease;
}

.btn-gold:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(212, 175, 55, 0.5);
}

.btn-whatsapp {
    background: #25D366;
    color: #FFF;
    padding: 12px 24px;
    border-radius: 4px;
    font-weight: 700;
    font-size: 0.95rem;
    text-decoration: none;
    display: inline-flex;
    align-items: center;
    gap: 8px;
    box-shadow: 0 4px 15px rgba(37, 211, 102, 0.3);
}

.btn-whatsapp:hover {
    background: #20BA5A;
    transform: translateY(-2px);
}

/* Hero Section */
.hero {
    position: relative;
    padding: 100px 5% 120px;
    background: radial-gradient(circle at 70% 30%, rgba(212, 175, 55, 0.08) 0%, transparent 60%), linear-gradient(180deg, #07080B 0%, #0F1117 100%);
    overflow: hidden;
}

.hero-grid {
    display: grid;
    grid-template-columns: 1.1fr 0.9fr;
    gap: 60px;
    align-items: center;
    max-width: 1300px;
    margin: 0 auto;
}

.hero-badge {
    background: rgba(212, 175, 55, 0.1);
    border: 1px solid var(--border-gold);
    color: var(--gold);
    padding: 8px 20px;
    border-radius: 30px;
    font-size: 0.85rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 2px;
    display: inline-flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 25px;
}

.hero h1 {
    font-size: 3.8rem;
    line-height: 1.1;
    margin-bottom: 25px;
    background: linear-gradient(180deg, #FFFFFF 0%, #CBD5E1 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero h1 span {
    background: var(--gold-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero p {
    font-size: 1.2rem;
    color: var(--text-gray);
    margin-bottom: 35px;
    line-height: 1.7;
}

.hero-actions {
    display: flex;
    gap: 15px;
    flex-wrap: wrap;
}

.hero-card-preview {
    background: var(--bg-card);
    border: 1px solid var(--border-gold);
    border-radius: 16px;
    padding: 30px;
    box-shadow: 0 20px 50px rgba(0,0,0,0.5);
    position: relative;
}

.preview-badge {
    position: absolute;
    top: -15px;
    right: 25px;
    background: var(--gold-gradient);
    color: #000;
    font-weight: 800;
    font-size: 0.75rem;
    padding: 6px 14px;
    border-radius: 20px;
    text-transform: uppercase;
}

/* Feature Grid */
.features-strip {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 20px;
    max-width: 1300px;
    margin: -50px auto 80px;
    padding: 0 5%;
    position: relative;
    z-index: 10;
}

.feature-box {
    background: var(--bg-card);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 12px;
    padding: 25px;
    text-align: center;
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
}

.feature-box i {
    font-size: 2rem;
    color: var(--gold);
    margin-bottom: 12px;
}

.feature-box h4 {
    font-size: 1.1rem;
    margin-bottom: 6px;
}

.feature-box p {
    font-size: 0.85rem;
    color: var(--text-gray);
}

/* Configurator Section */
.builder-section {
    padding: 80px 5%;
    background: #0B0D13;
}

.section-header {
    text-align: center;
    max-width: 700px;
    margin: 0 auto 60px;
}

.section-subtitle {
    color: var(--gold);
    font-size: 0.85rem;
    text-transform: uppercase;
    letter-spacing: 3px;
    font-weight: 700;
    display: block;
    margin-bottom: 8px;
}

.section-header h2 {
    font-size: 2.8rem;
}

.config-container {
    max-width: 1200px;
    margin: 0 auto;
    background: var(--bg-card);
    border: 1px solid var(--border-gold);
    border-radius: 16px;
    overflow: hidden;
    display: grid;
    grid-template-columns: 1.2fr 0.8fr;
    box-shadow: 0 30px 60px rgba(0,0,0,0.6);
}

.config-options {
    padding: 40px;
    border-right: 1px solid rgba(255,255,255,0.06);
}

.step-title {
    font-size: 1.2rem;
    color: var(--gold);
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    gap: 10px;
}

.package-cards {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 15px;
    margin-bottom: 35px;
}

.pkg-card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 10px;
    padding: 20px 15px;
    text-align: center;
    cursor: pointer;
    transition: all 0.3s ease;
}

.pkg-card.active, .pkg-card:hover {
    border-color: var(--gold);
    background: rgba(212, 175, 55, 0.1);
    transform: translateY(-4px);
}

.pkg-price {
    font-size: 1.8rem;
    font-weight: 800;
    color: var(--gold);
    margin: 8px 0;
}

.flavour-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(140px, 1fr));
    gap: 10px;
    margin-bottom: 35px;
}

.flavour-chip {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.08);
    padding: 10px 12px;
    border-radius: 6px;
    font-size: 0.85rem;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 8px;
    transition: all 0.2s ease;
}

.flavour-chip.active {
    border-color: var(--gold);
    color: var(--gold);
    background: rgba(212, 175, 55, 0.15);
}

.addons-list {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
}

.addon-item {
    background: rgba(255,255,255,0.02);
    border: 1px solid rgba(255,255,255,0.06);
    padding: 12px 15px;
    border-radius: 8px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 0.85rem;
    cursor: pointer;
}

.addon-item input {
    accent-color: var(--gold);
}

.config-summary {
    padding: 40px;
    background: #090B0F;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.summary-title {
    font-size: 1.3rem;
    color: #FFF;
    border-bottom: 1px solid rgba(255,255,255,0.1);
    padding-bottom: 15px;
    margin-bottom: 20px;
}

.summary-rows {
    display: flex;
    flex-direction: column;
    gap: 12px;
    margin-bottom: 30px;
}

.summary-row {
    display: flex;
    justify-content: space-between;
    font-size: 0.9rem;
    color: var(--text-gray);
}

.summary-row strong {
    color: #FFF;
}

.total-box {
    background: rgba(212, 175, 55, 0.08);
    border: 1px solid var(--border-gold);
    padding: 20px;
    border-radius: 10px;
    margin-bottom: 25px;
}

.total-amount {
    font-size: 2.8rem;
    font-weight: 800;
    color: var(--gold);
}

/* Coverage Areas */
.areas-section {
    padding: 80px 5%;
}

.areas-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
    max-width: 1200px;
    margin: 0 auto;
}

.area-card {
    background: var(--bg-card);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 10px;
    padding: 25px;
    display: flex;
    align-items: center;
    gap: 15px;
    transition: all 0.3s ease;
}

.area-card:hover {
    border-color: var(--gold);
    transform: translateY(-4px);
}

.area-card i {
    font-size: 1.5rem;
    color: var(--gold);
}

/* Floating Order Bar */
.sticky-order-bar {
    position: fixed;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%);
    background: rgba(15, 17, 23, 0.95);
    backdrop-filter: blur(15px);
    border: 1px solid var(--border-gold);
    border-radius: 50px;
    padding: 10px 30px;
    display: flex;
    align-items: center;
    gap: 25px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.7);
    z-index: 1500;
}

/* Footer */
footer {
    background: #050608;
    border-top: 1px solid rgba(255,255,255,0.05);
    padding: 60px 5% 30px;
    color: var(--text-gray);
    font-size: 0.9rem;
}

.footer-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 40px;
    max-width: 1200px;
    margin: 0 auto 40px;
}

.footer-col h4 {
    color: #FFF;
    margin-bottom: 20px;
}

.footer-col ul {
    list-style: none;
}

.footer-col li {
    margin-bottom: 10px;
}

.footer-col a {
    color: var(--text-gray);
    text-decoration: none;
}

.footer-col a:hover {
    color: var(--gold);
}
"""

with open(os.path.join(target_dir, "style.css"), "w", encoding="utf-8") as f:
    f.write(css_content)

# 2. SCRIPT.JS
js_content = """
let selectedPkg = { name: "1 Shisha Set", price: 50 };
let selectedFlavour = "Al Fakher Double Apple";
let addons = [];

function selectPkg(name, price, elem) {
    selectedPkg = { name: name, price: price };
    document.querySelectorAll('.pkg-card').forEach(c => c.classList.remove('active'));
    elem.classList.add('active');
    updateSummary();
}

function selectFlavour(name, elem) {
    selectedFlavour = name;
    document.querySelectorAll('.flavour-chip').forEach(c => c.classList.remove('active'));
    elem.classList.add('active');
    updateSummary();
}

function toggleAddon(name, price, checkbox) {
    if (checkbox.checked) {
        addons.push({ name: name, price: price });
    } else {
        addons = addons.filter(a => a.name !== name);
    }
    updateSummary();
}

function updateSummary() {
    let addonTotal = addons.reduce((sum, a) => sum + a.price, 0);
    let grandTotal = selectedPkg.price + addonTotal;
    
    document.getElementById('sum-pkg').innerText = selectedPkg.name + ' (£' + selectedPkg.price + ')';
    document.getElementById('sum-flavour').innerText = selectedFlavour;
    
    let addonText = addons.length > 0 ? addons.map(a => a.name + ' (£' + a.price + ')').join(', ') : 'None selected';
    document.getElementById('sum-addons').innerText = addonText;
    
    document.getElementById('grand-total').innerText = '£' + grandTotal;
}

function sendWhatsAppOrder() {
    let name = document.getElementById('cust-name').value || 'Customer';
    let area = document.getElementById('cust-area').value || 'Central London';
    let phone = document.getElementById('cust-phone').value || '';
    
    let addonText = addons.length > 0 ? addons.map(a => a.name + ' (£' + a.price + ')').join(', ') : 'None';
    let total = document.getElementById('grand-total').innerText;
    
    let msg = `*NEW 24/7 SHISHA ORDER*%0A` +
              `*Name:* ${name}%0A` +
              `*Area:* ${area}%0A` +
              `*Phone:* ${phone}%0A` +
              `------------------------%0A` +
              `*Package:* ${selectedPkg.name}%0A` +
              `*Flavour:* ${selectedFlavour}%0A` +
              `*Extras:* ${addonText}%0A` +
              `*Total Amount:* ${total}%0A` +
              `------------------------%0A` +
              `Please confirm 24/7 delivery arrival time!`;
              
    window.open(`https://wa.me/447903375779?text=${msg}`, '_blank');
}
"""

with open(os.path.join(target_dir, "script.js"), "w", encoding="utf-8") as f:
    f.write(js_content)

print("[+] Created style.css and script.js")
