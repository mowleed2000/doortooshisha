import os

target_dir = r"C:\Users\fifia\.gemini\antigravity\scratch\shisha-delivery-london"

# 1. REBUILD STYLE.CSS (RESTRAINED 5-STAR HOTEL CONCIERGE LUXURY)
css_content = """
:root {
    --bg-dark: #07080A;
    --bg-card: #0F1117;
    --gold: #C5A059;
    --gold-hover: #DFCA9B;
    --text-ivory: #F4F1EA;
    --text-muted: #8E96A4;
    --border-subtle: rgba(255, 255, 255, 0.08);
    --border-gold: rgba(197, 160, 89, 0.35);
    --shadow-luxury: 0 25px 50px rgba(0, 0, 0, 0.7);
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

/* NAVIGATION (SECTION 1) */
header {
    background: rgba(7, 8, 10, 0.96);
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
    font-size: 1.2rem;
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
    transition: color 0.3s ease;
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
    color: #07080A;
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
    background: var(--gold-hover);
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

/* SECTION SPACING & RESPONSIVE CONTAINERS */
section {
    padding: 120px 6%;
}

.section-title-wrap {
    text-align: center;
    max-width: 800px;
    margin: 0 auto 75px;
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

/* SECTION 2 — HERO (H01.png) */
.hero {
    position: relative;
    min-height: 90vh;
    display: flex;
    align-items: center;
    background: linear-gradient(180deg, rgba(7, 8, 10, 0.4) 0%, rgba(7, 8, 10, 0.96) 100%), url('assets/images/shisha/hero/H01.png') center/cover no-repeat;
    padding: 120px 6%;
}

.hero-content {
    max-width: 800px;
    margin: 0 auto;
    text-align: center;
}

.hero h1 {
    font-size: 4.2rem;
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

/* SECTION 3 — PRIVATE SHISHA (H02.png) */
.private-grid {
    max-width: 1300px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 60px;
    align-items: center;
}

.private-img-wrap img {
    width: 100%;
    height: 480px;
    object-fit: cover;
    border-radius: 4px;
    border: 1px solid var(--border-subtle);
    box-shadow: var(--shadow-luxury);
}

/* SECTION 4 — HOW IT WORKS */
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
    padding: 50px 35px;
    border-radius: 4px;
    transition: border-color 0.3s ease;
}

.step-card:hover {
    border-color: var(--border-gold);
}

.step-num {
    font-family: 'Cinzel', serif;
    font-size: 2.8rem;
    color: var(--gold);
    font-weight: 700;
    margin-bottom: 20px;
    display: block;
}

.step-card h3 {
    font-size: 1.25rem;
    margin-bottom: 12px;
}

.step-card p {
    font-size: 0.95rem;
    color: var(--text-muted);
}

/* SECTION 5 — PACKAGES (P01, P02, P03) */
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
    transition: border-color 0.3s ease;
}

.pkg-card:hover {
    border-color: var(--border-gold);
}

.pkg-card.highlight {
    border: 1px solid var(--gold);
    position: relative;
}

.pkg-pop-tag {
    position: absolute;
    top: 15px;
    right: 15px;
    background: var(--gold);
    color: #000;
    font-size: 0.65rem;
    font-weight: 800;
    padding: 4px 12px;
    border-radius: 2px;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.pkg-card-img {
    height: 260px;
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
    font-size: 1.35rem;
    margin-bottom: 10px;
}

.pkg-price {
    font-size: 2.8rem;
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
    gap: 12px;
}

.pkg-features i {
    color: var(--gold);
    font-size: 0.75rem;
}

/* SECTION 6 — FLAVOURS (F01 - F08) */
.flavour-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 25px;
    max-width: 1300px;
    margin: 0 auto;
}

.flavour-card {
    background: var(--bg-card);
    border: 1px solid var(--border-subtle);
    border-radius: 4px;
    overflow: hidden;
    cursor: pointer;
    transition: all 0.3s ease;
}

.flavour-card:hover {
    border-color: var(--border-gold);
    transform: translateY(-4px);
}

.flavour-img {
    height: 200px;
    width: 100%;
    object-fit: cover;
}

.flavour-info {
    padding: 22px;
    text-align: center;
}

.flavour-info h4 {
    font-size: 1.1rem;
    margin-bottom: 4px;
}

.flavour-info span {
    font-size: 0.75rem;
    color: var(--gold);
    letter-spacing: 1px;
}

/* SECTION 7 — DELIVERY EXPERIENCE (D01, D02, D03) */
.story-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 35px;
    max-width: 1300px;
    margin: 0 auto;
}

.story-card {
    background: var(--bg-card);
    border: 1px solid var(--border-subtle);
    border-radius: 4px;
    overflow: hidden;
}

.story-img {
    height: 250px;
    width: 100%;
    object-fit: cover;
}

.story-body {
    padding: 30px;
}

.story-body h4 {
    font-size: 1.2rem;
    margin-bottom: 10px;
}

.story-body p {
    font-size: 0.9rem;
    color: var(--text-muted);
}

/* SECTION 8 — OPTIONAL UPGRADES (U01 - U04) */
.upgrades-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 25px;
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
    font-size: 1.15rem;
}

.upgrade-price {
    font-size: 1.15rem;
    color: var(--gold);
    font-weight: 700;
    font-family: 'Cinzel', serif;
}

.upgrade-body p {
    font-size: 0.88rem;
    color: var(--text-muted);
}

/* SECTION 9 — PRIVATE EXPERIENCE (E01, E02, E03) */
.exp-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 35px;
    max-width: 1300px;
    margin: 0 auto;
}

.exp-card {
    background: var(--bg-card);
    border: 1px solid var(--border-subtle);
    border-radius: 4px;
    overflow: hidden;
}

.exp-img {
    height: 260px;
    width: 100%;
    object-fit: cover;
}

.exp-body {
    padding: 25px;
}

.exp-body h4 {
    font-size: 1.15rem;
    margin-bottom: 8px;
}

.exp-body p {
    font-size: 0.88rem;
    color: var(--text-muted);
}

/* SECTION 10 — COVERAGE */
.coverage-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
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

/* SECTION 12 — FINAL CTA (D03 / H01) */
.cta-section {
    position: relative;
    padding: 140px 6%;
    text-align: center;
    background: linear-gradient(180deg, rgba(7, 8, 10, 0.6) 0%, rgba(7, 8, 10, 0.98) 100%), url('assets/images/shisha/delivery/D03.png') center/cover no-repeat;
}

/* ORDER CONCIERGE MODAL */
.config-modal {
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0,0,0,0.88);
    backdrop-filter: blur(15px);
    z-index: 3000;
    justify-content: center;
    align-items: center;
}

.config-modal-content {
    background: #0B0D13;
    border: 1px solid var(--border-gold);
    border-radius: 4px;
    width: 90%;
    max-width: 680px;
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

/* FOOTER (SECTION 13) */
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

/* RESPONSIVE DESIGN (SECTION 19) */
@media (max-width: 1100px) {
    .flavour-grid, .upgrades-grid, .coverage-grid { grid-template-columns: repeat(2, 1fr); }
    .packages-grid, .steps-grid, .story-grid, .exp-grid { grid-template-columns: 1fr; }
    .private-grid { grid-template-columns: 1fr; }
    .hero h1 { font-size: 3.2rem; }
}

@media (max-width: 768px) {
    nav ul { display: none; }
    .hero h1 { font-size: 2.5rem; }
    .flavour-grid, .upgrades-grid, .coverage-grid { grid-template-columns: 1fr; }
    section { padding: 80px 5%; }
}
"""

with open(os.path.join(target_dir, "style.css"), "w", encoding="utf-8") as f:
    f.write(css_content)

def get_header(active_page="home"):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Door To Door Shisha Delivery | Private Shisha Concierge Central London</title>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800;900&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <div class="nav-container">
            <a href="index.html" class="logo">
                <div class="logo-text">
                    <h1>DOOR TO DOOR SHISHA DELIVERY</h1>
                    <span>CENTRAL LONDON CONCIERGE</span>
                </div>
            </a>
            <nav>
                <ul>
                    <li><a href="menu.html" class="{'active' if active_page == 'flavours' else ''}">Flavours</a></li>
                    <li><a href="packages.html" class="{'active' if active_page == 'packages' else ''}">Packages</a></li>
                    <li><a href="about.html" class="{'active' if active_page == 'experience' else ''}">The Experience</a></li>
                    <li><a href="areas.html" class="{'active' if active_page == 'coverage' else ''}">Coverage</a></li>
                    <li><a href="contact.html" class="{'active' if active_page == 'contact' else ''}">Contact</a></li>
                </ul>
            </nav>
            <div class="nav-actions">
                <a href="https://wa.me/447903375779" target="_blank" class="btn-outline"><i class="fa-brands fa-whatsapp"></i> WhatsApp Concierge</a>
                <a href="tel:07903375779" class="btn-concierge"><i class="fa-solid fa-phone"></i> 07903375779</a>
            </div>
        </div>
    </header>
"""

def get_footer():
    return """
    <footer>
        <div class="footer-grid">
            <div class="footer-col">
                <div class="logo-text" style="margin-bottom: 20px;">
                    <h1 style="color: #FFF; font-size: 1.2rem; letter-spacing: 2px;">DOOR TO DOOR SHISHA DELIVERY</h1>
                    <span style="color: var(--gold); font-size: 0.65rem; letter-spacing: 3px;">CENTRAL LONDON CONCIERGE</span>
                </div>
                <p style="font-size: 0.9rem; margin-bottom: 20px; line-height: 1.7;">Private shisha delivery across Central London. Delivering ready-to-smoke luxury setups directly to your home, hotel suite or private residence.</p>
                <p><strong style="color: #FFF;">Direct Concierge Line:</strong> <a href="tel:07903375779" style="color: var(--gold); text-decoration: none;">07903375779</a></p>
                <p><strong style="color: #FFF;">Email:</strong> Mrshawest26@gmail.com</p>
            </div>

            <div class="footer-col">
                <h4>Navigation</h4>
                <ul>
                    <li><a href="index.html">Home</a></li>
                    <li><a href="menu.html">Choose Flavour</a></li>
                    <li><a href="packages.html">Shisha Packages</a></li>
                    <li><a href="about.html">The Experience</a></li>
                    <li><a href="areas.html">Central London Coverage</a></li>
                    <li><a href="contact.html">Contact Concierge</a></li>
                </ul>
            </div>

            <div class="footer-col">
                <h4>Coverage Zones</h4>
                <ul>
                    <li>Westminster</li>
                    <li>Knightsbridge</li>
                    <li>Chelsea</li>
                    <li>Vauxhall</li>
                    <li>South Kensington</li>
                    <li>High Street Kensington</li>
                    <li>Baker Street & Marble Arch</li>
                </ul>
            </div>

            <div class="footer-col">
                <h4>Private Booking</h4>
                <p style="font-size: 0.9rem; margin-bottom: 15px;">24/7 Service operating around the clock in Central London.</p>
                <button onclick="openOrderModal('PRIVATE SESSION', 50)" class="btn-concierge" style="width: 100%; justify-content: center;">BOOK YOUR SHISHA</button>
            </div>
        </div>

        <div style="text-align: center; border-top: 1px solid var(--border-subtle); padding-top: 25px; font-size: 0.8rem; color: var(--text-muted);">
            <p>&copy; 2026 Door To Door Shisha Delivery. All Rights Reserved. | Strictly 18+ Adults Only. | 24/7 Hotline: 07903375779</p>
        </div>
    </footer>

    <!-- ORDER CONCIERGE MODAL -->
    <div id="orderModal" class="config-modal">
        <div class="config-modal-content">
            <span class="close-modal" onclick="closeOrderModal()">&times;</span>
            <span class="section-label">Private Concierge Order</span>
            <h2 style="font-size: 1.8rem; margin-bottom: 25px;">Complete Your Booking</h2>
            
            <div style="background: var(--bg-card); padding: 25px; border: 1px solid var(--border-subtle); border-radius: 4px; margin-bottom: 25px;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 10px;">
                    <span style="color: var(--text-muted);">Selected Package:</span>
                    <strong id="modal-pkg" style="color: var(--gold);">PRIVATE SESSION (£50)</strong>
                </div>
                <div style="display: flex; justify-content: space-between; margin-bottom: 10px;">
                    <span style="color: var(--text-muted);">Selected Flavour:</span>
                    <strong id="modal-flavour" style="color: #FFF;">Al Fakher Double Apple</strong>
                </div>
                <div style="display: flex; justify-content: space-between; margin-bottom: 15px;">
                    <span style="color: var(--text-muted);">Upgrades:</span>
                    <strong id="modal-addons" style="color: #FFF;">None</strong>
                </div>
                <div style="display: flex; justify-content: space-between; border-top: 1px solid var(--border-subtle); padding-top: 15px;">
                    <span style="font-size: 1.1rem; color: #FFF; font-weight: 700;">Total Payable:</span>
                    <span style="font-size: 1.8rem; font-family: 'Cinzel', serif; color: var(--gold); font-weight: 700;" id="modal-total">£50</span>
                </div>
            </div>

            <div style="margin-bottom: 25px;">
                <label style="display: block; font-size: 0.85rem; color: var(--gold); letter-spacing: 1px; margin-bottom: 8px; font-weight: 600;">SELECT YOUR FLAVOUR</label>
                <select onchange="selectFlavour(this.value)" style="width: 100%; padding: 12px; background: var(--bg-card); border: 1px solid var(--border-subtle); color: #FFF; border-radius: 2px; margin-bottom: 15px;">
                    <option value="Al Fakher Double Apple">Al Fakher Double Apple (Red & Green Apples)</option>
                    <option value="Al Fakher Fresh Mint">Al Fakher Fresh Mint</option>
                    <option value="Adalya Love 66">Adalya Love 66 (Watermelon, Melon & Mint)</option>
                    <option value="Adalya Lady Killer">Adalya Lady Killer (Mango, Melon, Berries & Mint)</option>
                    <option value="Mazaya Watermelon Mint">Mazaya Watermelon Mint</option>
                    <option value="Paan Ras / Paan Mint">Paan Ras / Paan Mint (Betel Leaf)</option>
                    <option value="Starburst Candy Mix">Starburst Candy Mix</option>
                    <option value="Savaco Luxury Line (£30/50g)">Savaco Luxury Line (+£30)</option>
                </select>

                <label style="display: block; font-size: 0.85rem; color: var(--gold); letter-spacing: 1px; margin-bottom: 8px; font-weight: 600;">OPTIONAL UPGRADES</label>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-bottom: 20px;">
                    <label style="font-size: 0.85rem; color: var(--text-muted); cursor: pointer;"><input type="checkbox" onchange="toggleUpgrade('Fresh Fruit Head', 30, this)"> Fresh Fruit Head (+£30)</label>
                    <label style="font-size: 0.85rem; color: var(--text-muted); cursor: pointer;"><input type="checkbox" onchange="toggleUpgrade('Electric Coal Burner', 35, this)"> Electric Coal Burner (+£35)</label>
                    <label style="font-size: 0.85rem; color: var(--text-muted); cursor: pointer;"><input type="checkbox" onchange="toggleUpgrade('Chilled Juice Base', 15, this)"> Chilled Juice Base (+£15)</label>
                    <label style="font-size: 0.85rem; color: var(--text-muted); cursor: pointer;"><input type="checkbox" onchange="toggleUpgrade('Under-Shisha LED Base', 15, this)"> Under-Shisha LED (+£15)</label>
                </div>

                <label style="display: block; font-size: 0.85rem; color: var(--gold); letter-spacing: 1px; margin-bottom: 8px; font-weight: 600;">DELIVERY DETAILS</label>
                <input type="text" id="cust-name" placeholder="Full Name" style="width: 100%; padding: 12px; background: var(--bg-card); border: 1px solid var(--border-subtle); color: #FFF; border-radius: 2px; margin-bottom: 10px;">
                <select id="cust-area" style="width: 100%; padding: 12px; background: var(--bg-card); border: 1px solid var(--border-subtle); color: #FFF; border-radius: 2px; margin-bottom: 10px;">
                    <option>Westminster</option>
                    <option>Knightsbridge</option>
                    <option>Chelsea</option>
                    <option>Vauxhall</option>
                    <option>South Kensington</option>
                    <option>High Street Kensington</option>
                    <option>Baker Street</option>
                    <option>Marble Arch</option>
                </select>
                <input type="tel" id="cust-phone" placeholder="Contact Phone Number" style="width: 100%; padding: 12px; background: var(--bg-card); border: 1px solid var(--border-subtle); color: #FFF; border-radius: 2px;">
            </div>

            <button onclick="dispatchWhatsAppOrder()" class="btn-concierge" style="width: 100%; justify-content: center; padding: 16px;"><i class="fa-brands fa-whatsapp"></i> CONFIRM BOOKING VIA WHATSAPP</button>
            <p style="font-size: 0.8rem; text-align: center; color: var(--text-muted); margin-top: 12px;">Or call concierge directly: <a href="tel:07903375779" style="color: var(--gold);">07903375779</a></p>
        </div>
    </div>

    <script src="script.js"></script>
</body>
</html>
"""

# INDEX.HTML
index_html = get_header("home") + """
    <!-- SECTION 2 — HERO (H01.png) -->
    <section class="hero">
        <div class="hero-content">
            <h1>PREMIUM SHISHA.<br><span>DELIVERED TO YOUR DOOR.</span></h1>
            <p class="hero-p">Private shisha delivery across Central London. Premium pipes, authentic tobacco and a complete ready-to-smoke setup, delivered directly to your home, hotel or private event.</p>
            
            <div class="hero-actions">
                <button onclick="openOrderModal('PRIVATE SESSION', 50)" class="btn-concierge">BOOK YOUR SHISHA</button>
                <a href="https://wa.me/447903375779" target="_blank" class="btn-outline"><i class="fa-brands fa-whatsapp"></i> WHATSAPP CONCIERGE</a>
            </div>

            <div class="hero-trust">24/7 CENTRAL LONDON • 30–45 MIN DELIVERY</div>
        </div>
    </section>

    <!-- SECTION 3 — PRIVATE SHISHA (H02.png) -->
    <section style="background: #0B0D13;">
        <div class="private-grid">
            <div>
                <span class="section-label">DISCREET & EXCLUSIVE</span>
                <h2 style="font-size: 2.5rem; margin-bottom: 20px;">PRIVATE SHISHA, WITHOUT LEAVING HOME.</h2>
                <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 25px;">We deliver a complete premium shisha experience directly to customers across Central London. Enjoy ready-to-smoke setups delivered to your home, private apartment, penthouse, hotel suite or intimate gathering.</p>
                <button onclick="openOrderModal('PRIVATE SESSION', 50)" class="btn-outline">BOOK YOUR SHISHA</button>
            </div>
            <div class="private-img-wrap">
                <img src="assets/images/shisha/hero/H02.png" alt="H02 Private Shisha">
            </div>
        </div>
    </section>

    <!-- SECTION 4 — HOW IT WORKS -->
    <section>
        <div class="section-title-wrap">
            <span class="section-label">HOW IT WORKS</span>
            <h2>SIMPLE THREE-STEP CONCIERGE</h2>
        </div>

        <div class="steps-grid">
            <div class="step-card">
                <span class="step-num">01</span>
                <h3>CHOOSE YOUR FLAVOUR</h3>
                <p>Select your package and preferred authentic flavour blend from our catalogue.</p>
            </div>

            <div class="step-card">
                <span class="step-num">02</span>
                <h3>WE DELIVER</h3>
                <p>Your ready-to-smoke setup is delivered directly to your location in Central London.</p>
            </div>

            <div class="step-card">
                <span class="step-num">03</span>
                <h3>ENJOY YOUR SESSION</h3>
                <p>Enjoy premium shisha in your own space with natural coals and sterile mouthpieces.</p>
            </div>
        </div>
    </section>

    <!-- SECTION 5 — PACKAGES (P01.png, P02.png, P03.png) -->
    <section style="background: #0B0D13;">
        <div class="section-title-wrap">
            <span class="section-label">TRANSPARENT PRICING</span>
            <h2>SHISHA PACKAGES</h2>
        </div>

        <div class="packages-grid">
            <!-- P01 -->
            <div class="pkg-card">
                <img src="assets/images/shisha/packages/P01.png" class="pkg-card-img" alt="P01 Private Session">
                <div class="pkg-card-body">
                    <div>
                        <h3 class="pkg-name">PRIVATE SESSION</h3>
                        <div class="pkg-price">£50</div>
                        <ul class="pkg-features">
                            <li><i class="fa-solid fa-square"></i> 1 Premium Hookah Pipe</li>
                            <li><i class="fa-solid fa-square"></i> 1 Fresh Flavour Head</li>
                            <li><i class="fa-solid fa-square"></i> 10 Natural Coconut Coals</li>
                            <li><i class="fa-solid fa-square"></i> Sealed Hygienic Mouthpiece</li>
                        </ul>
                    </div>
                    <button onclick="openOrderModal('PRIVATE SESSION', 50)" class="btn-outline" style="width: 100%; justify-content: center;">BOOK £50 SESSION</button>
                </div>
            </div>

            <!-- P02 (Highlight) -->
            <div class="pkg-card highlight">
                <span class="pkg-pop-tag">POPULAR</span>
                <img src="assets/images/shisha/packages/P02.png" class="pkg-card-img" alt="P02 Double Session">
                <div class="pkg-card-body">
                    <div>
                        <h3 class="pkg-name">DOUBLE SESSION</h3>
                        <div class="pkg-price">£80</div>
                        <ul class="pkg-features">
                            <li><i class="fa-solid fa-square"></i> 2 Premium Hookah Pipes</li>
                            <li><i class="fa-solid fa-square"></i> 2 Fresh Flavour Heads</li>
                            <li><i class="fa-solid fa-square"></i> 20 Natural Coconut Coals</li>
                            <li><i class="fa-solid fa-square"></i> Electric Coal Burner Included</li>
                        </ul>
                    </div>
                    <button onclick="openOrderModal('DOUBLE SESSION', 80)" class="btn-concierge" style="width: 100%; justify-content: center;">BOOK £80 SESSION</button>
                </div>
            </div>

            <!-- P03 -->
            <div class="pkg-card">
                <img src="assets/images/shisha/packages/P03.png" class="pkg-card-img" alt="P03 Group Session">
                <div class="pkg-card-body">
                    <div>
                        <h3 class="pkg-name">GROUP SESSION</h3>
                        <div class="pkg-price">£110</div>
                        <ul class="pkg-features">
                            <li><i class="fa-solid fa-square"></i> 3 Premium Hookah Pipes</li>
                            <li><i class="fa-solid fa-square"></i> 3 Fresh Flavour Heads</li>
                            <li><i class="fa-solid fa-square"></i> 30 Natural Coconut Coals</li>
                            <li><i class="fa-solid fa-square"></i> Electric Coal Burner Included</li>
                        </ul>
                    </div>
                    <button onclick="openOrderModal('GROUP SESSION', 110)" class="btn-outline" style="width: 100%; justify-content: center;">BOOK £110 SESSION</button>
                </div>
            </div>
        </div>
    </section>

    <!-- SECTION 6 — FLAVOURS (F01.png - F08.png) -->
    <section>
        <div class="section-title-wrap">
            <span class="section-label">AUTHENTIC SELECTION</span>
            <h2>CHOOSE YOUR FLAVOUR</h2>
        </div>

        <div class="flavour-grid">
            <div class="flavour-card" onclick="openOrderModal('PRIVATE SESSION', 50)">
                <img src="assets/images/shisha/flavours/F01.png" class="flavour-img" alt="F01 Al Fakher Double Apple">
                <div class="flavour-info">
                    <h4>Al Fakher Double Apple</h4>
                    <span>CLASSIC APPLE & ANISEED</span>
                </div>
            </div>

            <div class="flavour-card" onclick="openOrderModal('PRIVATE SESSION', 50)">
                <img src="assets/images/shisha/flavours/F02.png" class="flavour-img" alt="F02 Al Fakher Fresh Mint">
                <div class="flavour-info">
                    <h4>Al Fakher Fresh Mint</h4>
                    <span>FRESH MINT LEAVES</span>
                </div>
            </div>

            <div class="flavour-card" onclick="openOrderModal('PRIVATE SESSION', 50)">
                <img src="assets/images/shisha/flavours/F03.png" class="flavour-img" alt="F03 Adalya Love 66">
                <div class="flavour-info">
                    <h4>Adalya Love 66</h4>
                    <span>WATERMELON & MELON</span>
                </div>
            </div>

            <div class="flavour-card" onclick="openOrderModal('PRIVATE SESSION', 50)">
                <img src="assets/images/shisha/flavours/F04.png" class="flavour-img" alt="F04 Adalya Lady Killer">
                <div class="flavour-info">
                    <h4>Adalya Lady Killer</h4>
                    <span>MANGO, BERRIES & MINT</span>
                </div>
            </div>

            <div class="flavour-card" onclick="openOrderModal('PRIVATE SESSION', 50)">
                <img src="assets/images/shisha/flavours/F05.png" class="flavour-img" alt="F05 Mazaya Watermelon Mint">
                <div class="flavour-info">
                    <h4>Mazaya Watermelon Mint</h4>
                    <span>WATERMELON & FRESH MINT</span>
                </div>
            </div>

            <div class="flavour-card" onclick="openOrderModal('PRIVATE SESSION', 50)">
                <img src="assets/images/shisha/flavours/F06.png" class="flavour-img" alt="F06 Paan Ras / Paan Mint">
                <div class="flavour-info">
                    <h4>Paan Ras / Paan Mint</h4>
                    <span>FRESH BETEL LEAF</span>
                </div>
            </div>

            <div class="flavour-card" onclick="openOrderModal('PRIVATE SESSION', 50)">
                <img src="assets/images/shisha/flavours/F07.png" class="flavour-img" alt="F07 Starburst Candy Mix">
                <div class="flavour-info">
                    <h4>Starburst Candy Mix</h4>
                    <span>GOURMET SWEET CANDY</span>
                </div>
            </div>

            <div class="flavour-card" onclick="openOrderModal('PRIVATE SESSION', 50)">
                <img src="assets/images/shisha/flavours/F08.png" class="flavour-img" alt="F08 Savaco Luxury Line">
                <div class="flavour-info">
                    <h4>Savaco Luxury Line</h4>
                    <span>GOLDEN TOBACCO (+£30)</span>
                </div>
            </div>
        </div>
    </section>

    <!-- SECTION 7 — DELIVERY EXPERIENCE (D01.png, D02.png, D03.png) -->
    <section style="background: #0B0D13;">
        <div class="section-title-wrap">
            <span class="section-label">WHITE GLOVE CONCIERGE</span>
            <h2>FROM OUR DOOR TO YOURS.</h2>
        </div>

        <div class="story-grid">
            <div class="story-card">
                <img src="assets/images/shisha/delivery/D01.png" class="story-img" alt="D01 Delivery Arrival">
                <div class="story-body">
                    <h4>01. DELIVERY</h4>
                    <p>Discreet concierge driver arrival at your Central London home or hotel suite with leather equipment case.</p>
                </div>
            </div>

            <div class="story-card">
                <img src="assets/images/shisha/delivery/D02.png" class="story-img" alt="D02 Preparation">
                <div class="story-body">
                    <h4>02. PREPARATION</h4>
                    <p>Close-up professional preparation of freshly packed tobacco head and hot coconut coals.</p>
                </div>
            </div>

            <div class="story-card">
                <img src="assets/images/shisha/delivery/D03.png" class="story-img" alt="D03 Ready To Enjoy">
                <div class="story-body">
                    <h4>03. READY TO ENJOY</h4>
                    <p>Completed pristine shisha setup sitting ready in your penthouse lounge.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- SECTION 8 — OPTIONAL UPGRADES (U01.png - U04.png) -->
    <section>
        <div class="section-title-wrap">
            <span class="section-label">CUSTOMISE YOUR SESSION</span>
            <h2>OPTIONAL UPGRADES</h2>
        </div>

        <div class="upgrades-grid">
            <div class="upgrade-card">
                <img src="assets/images/shisha/upgrades/U01.png" class="upgrade-img" alt="U01 Fresh Fruit Head">
                <div class="upgrade-body">
                    <div class="upgrade-header">
                        <h4>FRESH FRUIT HEAD</h4>
                        <span class="upgrade-price">+£30</span>
                    </div>
                    <p>Carved fresh fruit bowl for longer sessions and an elevated presentation.</p>
                </div>
            </div>

            <div class="upgrade-card">
                <img src="assets/images/shisha/upgrades/U02.png" class="upgrade-img" alt="U02 Electric Coal Burner">
                <div class="upgrade-body">
                    <div class="upgrade-header">
                        <h4>ELECTRIC COAL BURNER</h4>
                        <span class="upgrade-price">+£35</span>
                    </div>
                    <p>High-speed electric burner for convenient coal preparation.</p>
                </div>
            </div>

            <div class="upgrade-card">
                <img src="assets/images/shisha/upgrades/U03.png" class="upgrade-img" alt="U03 Chilled Juice Base">
                <div class="upgrade-body">
                    <div class="upgrade-header">
                        <h4>CHILLED JUICE BASE</h4>
                        <span class="upgrade-price">+£15</span>
                    </div>
                    <p>Replace the standard water base with chilled apple, orange or pineapple juice.</p>
                </div>
            </div>

            <div class="upgrade-card">
                <img src="assets/images/shisha/upgrades/U04.png" class="upgrade-img" alt="U04 Under-Shisha LED Base">
                <div class="upgrade-body">
                    <div class="upgrade-header">
                        <h4>UNDER-SHISHA LED BASE</h4>
                        <span class="upgrade-price">+£15</span>
                    </div>
                    <p>Subtle illuminated base for a more atmospheric setup.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- SECTION 9 — PRIVATE EXPERIENCE (E01.png, E02.png, E03.png) -->
    <section style="background: #0B0D13;">
        <div class="section-title-wrap">
            <span class="section-label">PRIVATE RESIDENCE POSITIONING</span>
            <h2>YOUR SPACE. YOUR SHISHA.</h2>
        </div>

        <div class="exp-grid">
            <div class="exp-card">
                <img src="assets/images/shisha/experience/E01.png" class="exp-img" alt="E01 Single Private Experience">
                <div class="exp-body">
                    <h4>PRIVATE APARTMENT</h4>
                    <p>Solo evening relaxation in your penthouse residence.</p>
                </div>
            </div>

            <div class="exp-card">
                <img src="assets/images/shisha/experience/E02.png" class="exp-img" alt="E02 Two Person Experience">
                <div class="exp-body">
                    <h4>HOTEL SUITE</h4>
                    <p>Intimate two-person session in luxury London accommodations.</p>
                </div>
            </div>

            <div class="exp-card">
                <img src="assets/images/shisha/experience/E03.png" class="exp-img" alt="E03 Group Private Experience">
                <div class="exp-body">
                    <h4>PRIVATE GATHERING</h4>
                    <p>Small group evening in a private residence lounge.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- SECTION — VIDEO SHOWCASE -->
    <section style="background: #060709; padding: 100px 6%; text-align: center;">
        <div class="section-title-wrap" style="margin-bottom: 45px;">
            <span class="section-label">EXCLUSIVE VISUAL EXPERIENCE</span>
            <h2 style="font-size: 2.8rem;">DOOR TO DOOR SHISHA IN MOTION</h2>
            <p style="color: var(--text-muted); max-width: 650px; margin: 15px auto 0; font-size: 1rem;">Experience the luxury, precision, and ambiance of Central London's premier private shisha concierge.</p>
        </div>
        <div style="max-width: 1050px; margin: 0 auto; border-radius: 6px; overflow: hidden; border: 1px solid var(--border-gold); box-shadow: var(--shadow-luxury); position: relative; background: #000;">
            <video autoplay loop muted playsinline controls poster="assets/images/shisha/hero/H01.png" style="width: 100%; display: block; max-height: 580px; object-fit: cover;">
                <source src="assets/videos/gemini_generated_video_5cb81314.mp4" type="video/mp4">
                <source src="assets/videos/hero_video.mp4" type="video/mp4">
                Your browser does not support the video tag.
            </video>
        </div>
    </section>

    <!-- SECTION 10 — CENTRAL LONDON COVERAGE -->
    <section>
        <div class="section-title-wrap">
            <span class="section-label">DISPATCH FLEET</span>
            <h2>CENTRAL LONDON, DELIVERED.</h2>
        </div>

        <div class="coverage-grid">
            <div class="coverage-item"><strong>Westminster</strong><span>20 – 30 MINS</span></div>
            <div class="coverage-item"><strong>Knightsbridge</strong><span>20 – 30 MINS</span></div>
            <div class="coverage-item"><strong>Chelsea</strong><span>20 – 35 MINS</span></div>
            <div class="coverage-item"><strong>Vauxhall</strong><span>25 – 35 MINS</span></div>
            <div class="coverage-item"><strong>South Kensington</strong><span>25 – 35 MINS</span></div>
            <div class="coverage-item"><strong>High Street Kensington</strong><span>25 – 40 MINS</span></div>
            <div class="coverage-item"><strong>Baker Street</strong><span>30 – 40 MINS</span></div>
            <div class="coverage-item"><strong>Marble Arch</strong><span>30 – 40 MINS</span></div>
        </div>
    </section>

    <!-- SECTION 11 — 24/7 SERVICE -->
    <section style="background: #0B0D13;">
        <div style="max-width: 800px; margin: 0 auto; text-align: center; background: var(--bg-card); border: 1px solid var(--border-gold); padding: 55px 40px; border-radius: 4px;">
            <span class="section-label">ROUND THE CLOCK</span>
            <h2 style="font-size: 2.2rem; margin-bottom: 20px;">AVAILABLE 24/7.</h2>
            <p style="color: var(--text-muted); font-size: 1.1rem; margin-bottom: 30px;">Whether you're hosting at home, staying in a hotel or arranging a private gathering, our Central London delivery service operates around the clock.</p>
            <a href="tel:07903375779" class="btn-concierge"><i class="fa-solid fa-phone"></i> CALL 07903375779</a>
        </div>
    </section>

    <!-- SECTION 12 — FINAL CTA (D03.png) -->
    <section class="cta-section">
        <div style="max-width: 800px; margin: 0 auto;">
            <h2 style="font-size: 3.8rem; line-height: 1.1; margin-bottom: 30px;">YOUR SHISHA.<br><span>YOUR SPACE. YOUR NIGHT.</span></h2>
            
            <div style="display: flex; justify-content: center; gap: 20px; flex-wrap: wrap; margin-bottom: 35px;">
                <button onclick="openOrderModal('PRIVATE SESSION', 50)" class="btn-concierge" style="padding: 18px 40px;">BOOK YOUR SHISHA</button>
                <a href="https://wa.me/447903375779" target="_blank" class="btn-outline" style="padding: 18px 40px;"><i class="fa-brands fa-whatsapp"></i> WHATSAPP CONCIERGE</a>
            </div>

            <p style="font-size: 1.3rem; color: var(--gold); font-family: 'Cinzel', serif; font-weight: 700;">DIRECT HOTLINE: 07903375779</p>
        </div>
    </section>
""" + get_footer()

with open(os.path.join(target_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(index_html)

# OTHER PAGES (menu.html, packages.html, etc.)
menu_html = get_header("flavours") + """
    <section class="hero" style="min-height: 40vh; align-items: center;">
        <div class="hero-content">
            <span class="hero-trust">CURATED SELECTION</span>
            <h1>CHOOSE YOUR FLAVOUR</h1>
            <p class="hero-p">100% authentic tobacco brands delivered with ready-to-smoke setups in Central London.</p>
        </div>
    </section>

    <section>
        <div class="flavour-grid">
            <div class="flavour-card" onclick="openOrderModal('PRIVATE SESSION', 50)">
                <img src="assets/images/shisha/flavours/F01.png" class="flavour-img" alt="F01 Al Fakher Double Apple">
                <div class="flavour-info">
                    <h4>Al Fakher Double Apple</h4>
                    <span>CLASSIC APPLE & ANISEED</span>
                </div>
            </div>

            <div class="flavour-card" onclick="openOrderModal('PRIVATE SESSION', 50)">
                <img src="assets/images/shisha/flavours/F02.png" class="flavour-img" alt="F02 Al Fakher Fresh Mint">
                <div class="flavour-info">
                    <h4>Al Fakher Fresh Mint</h4>
                    <span>FRESH MINT LEAVES</span>
                </div>
            </div>

            <div class="flavour-card" onclick="openOrderModal('PRIVATE SESSION', 50)">
                <img src="assets/images/shisha/flavours/F03.png" class="flavour-img" alt="F03 Adalya Love 66">
                <div class="flavour-info">
                    <h4>Adalya Love 66</h4>
                    <span>WATERMELON & MELON</span>
                </div>
            </div>

            <div class="flavour-card" onclick="openOrderModal('PRIVATE SESSION', 50)">
                <img src="assets/images/shisha/flavours/F04.png" class="flavour-img" alt="F04 Adalya Lady Killer">
                <div class="flavour-info">
                    <h4>Adalya Lady Killer</h4>
                    <span>MANGO, BERRIES & MINT</span>
                </div>
            </div>

            <div class="flavour-card" onclick="openOrderModal('PRIVATE SESSION', 50)">
                <img src="assets/images/shisha/flavours/F05.png" class="flavour-img" alt="F05 Mazaya Watermelon Mint">
                <div class="flavour-info">
                    <h4>Mazaya Watermelon Mint</h4>
                    <span>WATERMELON & FRESH MINT</span>
                </div>
            </div>

            <div class="flavour-card" onclick="openOrderModal('PRIVATE SESSION', 50)">
                <img src="assets/images/shisha/flavours/F06.png" class="flavour-img" alt="F06 Paan Ras / Paan Mint">
                <div class="flavour-info">
                    <h4>Paan Ras / Paan Mint</h4>
                    <span>FRESH BETEL LEAF</span>
                </div>
            </div>

            <div class="flavour-card" onclick="openOrderModal('PRIVATE SESSION', 50)">
                <img src="assets/images/shisha/flavours/F07.png" class="flavour-img" alt="F07 Starburst Candy Mix">
                <div class="flavour-info">
                    <h4>Starburst Candy Mix</h4>
                    <span>GOURMET SWEET CANDY</span>
                </div>
            </div>

            <div class="flavour-card" onclick="openOrderModal('PRIVATE SESSION', 50)">
                <img src="assets/images/shisha/flavours/F08.png" class="flavour-img" alt="F08 Savaco Luxury Line">
                <div class="flavour-info">
                    <h4>Savaco Luxury Line</h4>
                    <span>GOLDEN TOBACCO (+£30)</span>
                </div>
            </div>
        </div>
    </section>
""" + get_footer()

with open(os.path.join(target_dir, "menu.html"), "w", encoding="utf-8") as f:
    f.write(menu_html)

packages_html = get_header("packages") + """
    <section class="hero" style="min-height: 40vh; align-items: center;">
        <div class="hero-content">
            <span class="hero-trust">TRANSPARENT PRICING</span>
            <h1>SHISHA PACKAGES</h1>
            <p class="hero-p">Ready-to-smoke setups, glowing coals, tongs, and sealed hygienic mouthpieces included.</p>
        </div>
    </section>

    <section>
        <div class="packages-grid">
            <div class="pkg-card">
                <img src="assets/images/shisha/packages/P01.png" class="pkg-card-img" alt="P01 Private Session">
                <div class="pkg-card-body">
                    <div>
                        <h3 class="pkg-name">PRIVATE SESSION</h3>
                        <div class="pkg-price">£50</div>
                        <ul class="pkg-features">
                            <li><i class="fa-solid fa-square"></i> 1 Premium Hookah Pipe</li>
                            <li><i class="fa-solid fa-square"></i> 1 Fresh Flavour Head</li>
                            <li><i class="fa-solid fa-square"></i> 10 Natural Coconut Coals</li>
                            <li><i class="fa-solid fa-square"></i> Sealed Hygienic Mouthpiece</li>
                        </ul>
                    </div>
                    <button onclick="openOrderModal('PRIVATE SESSION', 50)" class="btn-outline" style="width: 100%; justify-content: center;">BOOK £50 SESSION</button>
                </div>
            </div>

            <div class="pkg-card highlight">
                <span class="pkg-pop-tag">POPULAR</span>
                <img src="assets/images/shisha/packages/P02.png" class="pkg-card-img" alt="P02 Double Session">
                <div class="pkg-card-body">
                    <div>
                        <h3 class="pkg-name">DOUBLE SESSION</h3>
                        <div class="pkg-price">£80</div>
                        <ul class="pkg-features">
                            <li><i class="fa-solid fa-square"></i> 2 Premium Hookah Pipes</li>
                            <li><i class="fa-solid fa-square"></i> 2 Fresh Flavour Heads</li>
                            <li><i class="fa-solid fa-square"></i> 20 Natural Coconut Coals</li>
                            <li><i class="fa-solid fa-square"></i> Electric Coal Burner Included</li>
                        </ul>
                    </div>
                    <button onclick="openOrderModal('DOUBLE SESSION', 80)" class="btn-concierge" style="width: 100%; justify-content: center;">BOOK £80 SESSION</button>
                </div>
            </div>

            <div class="pkg-card">
                <img src="assets/images/shisha/packages/P03.png" class="pkg-card-img" alt="P03 Group Session">
                <div class="pkg-card-body">
                    <div>
                        <h3 class="pkg-name">GROUP SESSION</h3>
                        <div class="pkg-price">£110</div>
                        <ul class="pkg-features">
                            <li><i class="fa-solid fa-square"></i> 3 Premium Hookah Pipes</li>
                            <li><i class="fa-solid fa-square"></i> 3 Fresh Flavour Heads</li>
                            <li><i class="fa-solid fa-square"></i> 30 Natural Coconut Coals</li>
                            <li><i class="fa-solid fa-square"></i> Electric Coal Burner Included</li>
                        </ul>
                    </div>
                    <button onclick="openOrderModal('GROUP SESSION', 110)" class="btn-outline" style="width: 100%; justify-content: center;">BOOK £110 SESSION</button>
                </div>
            </div>
        </div>
    </section>
""" + get_footer()

with open(os.path.join(target_dir, "packages.html"), "w", encoding="utf-8") as f:
    f.write(packages_html)

print("[+] Master rebuild with user image library and business name Door To Door Shisha Delivery completed!")
