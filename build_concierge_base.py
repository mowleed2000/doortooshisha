import os

target_dir = r"C:\Users\fifia\.gemini\antigravity\scratch\shisha-delivery-london"
os.makedirs(target_dir, exist_ok=True)

# 1. STYLE.CSS - 5-STAR HOTEL CONCIERGE DARK LUXURY THEME
css_content = """
:root {
    --bg-dark: #08090C;
    --bg-card: #11131A;
    --bg-card-hover: #181B24;
    --gold: #C5A059;
    --gold-muted: rgba(197, 160, 89, 0.4);
    --gold-light: #DFCA9B;
    --text-ivory: #F4F1EA;
    --text-muted: #8E96A4;
    --border-subtle: rgba(255, 255, 255, 0.07);
    --border-gold: rgba(197, 160, 89, 0.3);
    --shadow-luxury: 0 30px 60px rgba(0, 0, 0, 0.7);
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
}

body {
    background-color: var(--bg-dark);
    color: var(--text-ivory);
    line-height: 1.7;
    overflow-x: hidden;
}

h1, h2, h3, h4 {
    font-family: 'Cinzel', Georgia, serif;
    font-weight: 700;
    letter-spacing: 1px;
    color: var(--text-ivory);
}

/* Navigation */
header {
    background: rgba(8, 9, 12, 0.96);
    backdrop-filter: blur(20px);
    position: sticky;
    top: 0;
    z-index: 1000;
    border-bottom: 1px solid var(--border-subtle);
}

.nav-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 22px 6%;
    max-width: 1400px;
    margin: 0 auto;
}

.logo {
    display: flex;
    align-items: center;
    gap: 14px;
    text-decoration: none;
}

.logo-text h1 {
    font-size: 1.25rem;
    letter-spacing: 3px;
    color: #FFF;
    font-weight: 800;
}

.logo-text span {
    font-size: 0.65rem;
    text-transform: uppercase;
    letter-spacing: 3px;
    color: var(--gold);
    display: block;
}

nav ul {
    display: flex;
    list-style: none;
    gap: 35px;
}

nav a {
    text-decoration: none;
    color: var(--text-muted);
    font-size: 0.9rem;
    font-weight: 500;
    letter-spacing: 1px;
    transition: all 0.3s ease;
}

nav a:hover, nav a.active {
    color: var(--gold);
}

.nav-actions {
    display: flex;
    align-items: center;
    gap: 20px;
}

.btn-concierge {
    background: var(--gold);
    color: #08090C;
    padding: 12px 28px;
    border-radius: 2px;
    font-weight: 700;
    font-size: 0.85rem;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    text-decoration: none;
    border: none;
    cursor: pointer;
    transition: all 0.3s ease;
    display: inline-flex;
    align-items: center;
    gap: 8px;
}

.btn-concierge:hover {
    background: var(--gold-light);
    transform: translateY(-2px);
}

.btn-outline {
    background: transparent;
    color: var(--text-ivory);
    border: 1px solid var(--border-gold);
    padding: 12px 28px;
    border-radius: 2px;
    font-weight: 600;
    font-size: 0.85rem;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    text-decoration: none;
    cursor: pointer;
    transition: all 0.3s ease;
    display: inline-flex;
    align-items: center;
    gap: 8px;
}

.btn-outline:hover {
    border-color: var(--gold);
    color: var(--gold);
}

/* HERO SECTION */
.hero {
    position: relative;
    min-height: 90vh;
    display: flex;
    align-items: center;
    background: linear-gradient(180deg, rgba(8, 9, 12, 0.4) 0%, rgba(8, 9, 12, 0.95) 100%), url('https://images.unsplash.com/photo-1541532713592-79a0317b6b77?auto=format&fit=crop&w=1920&q=80') center/cover no-repeat;
    padding: 100px 6%;
}

.hero-content {
    max-width: 800px;
    margin: 0 auto;
    text-align: center;
}

.hero h1 {
    font-size: 4rem;
    line-height: 1.1;
    margin-bottom: 25px;
    color: var(--text-ivory);
}

.hero h1 span {
    color: var(--gold);
}

.hero-p {
    font-size: 1.2rem;
    color: var(--text-muted);
    margin: 0 auto 40px;
    max-width: 680px;
    font-weight: 400;
}

.hero-actions {
    display: flex;
    justify-content: center;
    gap: 20px;
    margin-bottom: 35px;
}

.hero-trust {
    font-size: 0.8rem;
    letter-spacing: 3px;
    color: var(--gold);
    text-transform: uppercase;
    font-weight: 700;
}

/* SECTION STRUCTURE & WHITESPACE */
section {
    padding: 110px 6%;
}

.section-title-wrap {
    text-align: center;
    max-width: 750px;
    margin: 0 auto 70px;
}

.section-label {
    font-size: 0.8rem;
    letter-spacing: 4px;
    color: var(--gold);
    text-transform: uppercase;
    font-weight: 700;
    display: block;
    margin-bottom: 12px;
}

.section-title-wrap h2 {
    font-size: 3rem;
    line-height: 1.2;
}

/* VALUE PROPOSITION (3 EDITORIAL STEPS) */
.steps-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 40px;
    max-width: 1200px;
    margin: 0 auto;
}

.step-card {
    background: var(--bg-card);
    border: 1px solid var(--border-subtle);
    padding: 45px 35px;
    border-radius: 4px;
    position: relative;
    transition: all 0.3s ease;
}

.step-card:hover {
    border-color: var(--border-gold);
    transform: translateY(-5px);
}

.step-num {
    font-family: 'Cinzel', serif;
    font-size: 2.5rem;
    color: var(--gold);
    font-weight: 700;
    margin-bottom: 20px;
    display: block;
}

.step-card h3 {
    font-size: 1.3rem;
    margin-bottom: 12px;
    letter-spacing: 1px;
}

.step-card p {
    font-size: 0.95rem;
    color: var(--text-muted);
}

/* PACKAGES SECTION */
.packages-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 35px;
    max-width: 1300px;
    margin: 0 auto;
}

.pkg-card {
    background: var(--bg-card);
    border: 1px solid var(--border-subtle);
    border-radius: 4px;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    box-shadow: var(--shadow-luxury);
    transition: all 0.3s ease;
}

.pkg-card:hover {
    border-color: var(--border-gold);
}

.pkg-card.highlight {
    border: 1px solid var(--gold);
    position: relative;
}

.pkg-card-img {
    height: 250px;
    width: 100%;
    object-fit: cover;
}

.pkg-card-body {
    padding: 40px 30px;
    display: flex;
    flex-direction: column;
    flex-grow: 1;
    justify-content: space-between;
}

.pkg-name {
    font-size: 1.4rem;
    letter-spacing: 1px;
    margin-bottom: 10px;
}

.pkg-price {
    font-size: 2.6rem;
    font-family: 'Cinzel', serif;
    color: var(--gold);
    font-weight: 700;
    margin-bottom: 25px;
}

.pkg-features {
    list-style: none;
    margin-bottom: 35px;
}

.pkg-features li {
    font-size: 0.95rem;
    color: var(--text-muted);
    margin-bottom: 12px;
    display: flex;
    align-items: center;
    gap: 10px;
}

.pkg-features i {
    color: var(--gold);
    font-size: 0.8rem;
}

/* FLAVOUR SECTION */
.flavour-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 25px;
    max-width: 1300px;
    margin: 0 auto;
}

.flavour-card {
    background: var(--bg-card);
    border: 1px solid var(--border-subtle);
    border-radius: 4px;
    overflow: hidden;
    transition: all 0.3s ease;
}

.flavour-card:hover {
    border-color: var(--border-gold);
    transform: translateY(-4px);
}

.flavour-img {
    height: 180px;
    width: 100%;
    object-fit: cover;
}

.flavour-info {
    padding: 22px;
}

.flavour-info h4 {
    font-size: 1.1rem;
    margin-bottom: 4px;
}

.flavour-info span {
    font-size: 0.8rem;
    color: var(--gold);
    letter-spacing: 1px;
}

/* UPGRADES SECTION */
.upgrades-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 30px;
    max-width: 1300px;
    margin: 0 auto;
}

.upgrade-card {
    background: var(--bg-card);
    border: 1px solid var(--border-subtle);
    border-radius: 4px;
    overflow: hidden;
}

.upgrade-img {
    height: 220px;
    width: 100%;
    object-fit: cover;
}

.upgrade-body {
    padding: 25px;
}

.upgrade-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 10px;
}

.upgrade-header h4 {
    font-size: 1.2rem;
}

.upgrade-price {
    font-size: 1.2rem;
    color: var(--gold);
    font-weight: 700;
    font-family: 'Cinzel', serif;
}

.upgrade-body p {
    font-size: 0.9rem;
    color: var(--text-muted);
}

/* COVERAGE SECTION */
.coverage-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 20px;
    max-width: 1200px;
    margin: 0 auto;
}

.coverage-item {
    background: var(--bg-card);
    border: 1px solid var(--border-subtle);
    padding: 25px;
    border-radius: 4px;
    text-align: center;
}

.coverage-item strong {
    font-size: 1.1rem;
    display: block;
    color: var(--text-ivory);
    margin-bottom: 4px;
}

.coverage-item span {
    font-size: 0.8rem;
    color: var(--gold);
    letter-spacing: 1px;
}

/* CONCIERGE ORDERING STUDIO (MODAL & FORM) */
.config-modal {
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0,0,0,0.85);
    backdrop-filter: blur(12px);
    z-index: 3000;
    justify-content: center;
    align-items: center;
}

.config-modal-content {
    background: #0B0D13;
    border: 1px solid var(--border-gold);
    border-radius: 6px;
    width: 90%;
    max-width: 700px;
    max-height: 90vh;
    overflow-y: auto;
    padding: 40px;
    position: relative;
    box-shadow: var(--shadow-luxury);
}

.close-modal {
    position: absolute;
    top: 20px;
    right: 25px;
    font-size: 1.8rem;
    color: var(--text-muted);
    cursor: pointer;
}

.close-modal:hover {
    color: var(--gold);
}

/* FOOTER */
footer {
    background: #040507;
    border-top: 1px solid var(--border-subtle);
    padding: 80px 6% 30px;
    color: var(--text-muted);
}

.footer-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 40px;
    max-width: 1300px;
    margin: 0 auto 50px;
}

.footer-col h4 {
    color: #FFF;
    font-size: 1.1rem;
    margin-bottom: 20px;
    letter-spacing: 1px;
}

.footer-col ul {
    list-style: none;
}

.footer-col li {
    margin-bottom: 12px;
}

.footer-col a {
    color: var(--text-muted);
    text-decoration: none;
    transition: color 0.3s ease;
}

.footer-col a:hover {
    color: var(--gold);
}

/* RESPONSIVE DESIGN */
@media (max-width: 1024px) {
    .hero h1 { font-size: 3rem; }
    .steps-grid, .packages-grid { grid-template-columns: 1fr; }
    nav ul { display: none; }
}
"""

with open(os.path.join(target_dir, "style.css"), "w", encoding="utf-8") as f:
    f.write(css_content)

# 2. SCRIPT.JS - CLEAN ORDERING ENGINE & MODAL CONTROLLER
js_content = """
let selectedPackage = { name: "PRIVATE SESSION", price: 50 };
let selectedFlavour = "Al Fakher Double Apple";
let selectedAddons = [];

function openOrderModal(pkgName, pkgPrice) {
    if (pkgName && pkgPrice) {
        selectedPackage = { name: pkgName, price: pkgPrice };
    }
    updateOrderSummary();
    document.getElementById('orderModal').style.display = 'flex';
}

function closeOrderModal() {
    document.getElementById('orderModal').style.display = 'none';
}

function selectFlavour(name) {
    selectedFlavour = name;
    updateOrderSummary();
}

function toggleUpgrade(name, price, checkbox) {
    if (checkbox.checked) {
        selectedAddons.push({ name: name, price: price });
    } else {
        selectedAddons = selectedAddons.filter(a => a.name !== name);
    }
    updateOrderSummary();
}

function updateOrderSummary() {
    let addonSum = selectedAddons.reduce((sum, a) => sum + a.price, 0);
    let total = selectedPackage.price + addonSum;
    
    let pkgElem = document.getElementById('modal-pkg');
    let flavElem = document.getElementById('modal-flavour');
    let addonsElem = document.getElementById('modal-addons');
    let totalElem = document.getElementById('modal-total');
    
    if (pkgElem) pkgElem.innerText = selectedPackage.name + ' (£' + selectedPackage.price + ')';
    if (flavElem) flavElem.innerText = selectedFlavour;
    if (addonsElem) {
        addonsElem.innerText = selectedAddons.length > 0 ? selectedAddons.map(a => a.name + ' (+£' + a.price + ')').join(', ') : 'None';
    }
    if (totalElem) totalElem.innerText = '£' + total;
}

function dispatchWhatsAppOrder() {
    let name = document.getElementById('cust-name').value || 'Customer';
    let area = document.getElementById('cust-area').value || 'Central London';
    let phone = document.getElementById('cust-phone').value || '';
    
    let addonStr = selectedAddons.length > 0 ? selectedAddons.map(a => a.name + ' (£' + a.price + ')').join(', ') : 'None';
    let totalStr = document.getElementById('modal-total').innerText;
    
    let msg = `*NEW CONCIERGE SHISHA BOOKING*%0A` +
              `*Client:* ${name}%0A` +
              `*Delivery Location:* ${area}%0A` +
              `*Contact Phone:* ${phone}%0A` +
              `------------------------%0A` +
              `*Package:* ${selectedPackage.name}%0A` +
              `*Flavour:* ${selectedFlavour}%0A` +
              `*Upgrades:* ${addonStr}%0A` +
              `*Total Amount:* ${totalStr}%0A` +
              `------------------------%0A` +
              `Please confirm 24/7 delivery dispatch.`;
              
    window.open(`https://wa.me/447903375779?text=${msg}`, '_blank');
}

window.onclick = function(event) {
    let modal = document.getElementById('orderModal');
    if (event.target == modal) {
        modal.style.display = 'none';
    }
}
"""

with open(os.path.join(target_dir, "script.js"), "w", encoding="utf-8") as f:
    f.write(js_content)

print("[+] Wrote rebrand style.css and script.js")
