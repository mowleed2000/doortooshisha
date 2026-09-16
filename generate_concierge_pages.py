import os

target_dir = r"C:\Users\fifia\.gemini\antigravity\scratch\shisha-delivery-london"

def get_header(active_page="home"):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SHISHA DELIVERY | Private Shisha Concierge Central London</title>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800;900&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <div class="nav-container">
            <a href="index.html" class="logo">
                <div class="logo-text">
                    <h1>SHISHA DELIVERY</h1>
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
                    <h1 style="color: #FFF; font-size: 1.3rem; letter-spacing: 3px;">SHISHA DELIVERY</h1>
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
            <p>&copy; 2026 Shisha Delivery London. All Rights Reserved. | Strictly 18+ Adults Only. | 24/7 Hotline: 07903375779</p>
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
                    <option value="Al Fakher Double Apple">Al Fakher Double Apple (Classic)</option>
                    <option value="Al Fakher Fresh Mint">Al Fakher Fresh Mint</option>
                    <option value="Adalya Love 66">Adalya Love 66 (Watermelon, Melon & Mint)</option>
                    <option value="Adalya Lady Killer">Adalya Lady Killer (Mango, Melon, Berries & Mint)</option>
                    <option value="Mazaya Watermelon Mint">Mazaya Watermelon Mint</option>
                    <option value="Paan Ras / Paan Mint">Paan Ras / Paan Mint</option>
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

# INDEX.HTML - FULL EDITORIAL LUXURY REBUILD
index_html = get_header("home") + """
    <!-- HERO SECTION -->
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

    <!-- VALUE PROPOSITION -->
    <section>
        <div class="section-title-wrap">
            <span class="section-label">HOW IT WORKS</span>
            <h2>PRIVATE SHISHA, WITHOUT LEAVING HOME.</h2>
        </div>

        <div class="steps-grid">
            <div class="step-card">
                <span class="step-num">01</span>
                <h3>CHOOSE YOUR FLAVOUR</h3>
                <p>Select your package and authentic tobacco blend from our curated menu.</p>
            </div>

            <div class="step-card">
                <span class="step-num">02</span>
                <h3>WE DELIVER</h3>
                <p>Our concierge driver delivers your ready-to-smoke setup in 30–45 minutes.</p>
            </div>

            <div class="step-card">
                <span class="step-num">03</span>
                <h3>ENJOY YOUR SESSION</h3>
                <p>Relax in your home, penthouse or hotel suite with fresh coconut coals and sterile mouthpieces.</p>
            </div>
        </div>
    </section>

    <!-- SHISHA PACKAGES -->
    <section style="background: #0B0D13;">
        <div class="section-title-wrap">
            <span class="section-label">TRANSPARENT PRICING</span>
            <h2>SHISHA PACKAGES</h2>
        </div>

        <div class="packages-grid">
            <!-- Package 1 -->
            <div class="pkg-card">
                <img src="https://images.unsplash.com/photo-1527661591475-527312dd65f5?auto=format&fit=crop&w=800&q=80" class="pkg-card-img" alt="Private Session">
                <div class="pkg-card-body">
                    <div>
                        <h3 class="pkg-name">PACKAGE 1: PRIVATE SESSION</h3>
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

            <!-- Package 2 (Highlight) -->
            <div class="pkg-card highlight">
                <img src="https://images.unsplash.com/photo-1541532713592-79a0317b6b77?auto=format&fit=crop&w=800&q=80" class="pkg-card-img" alt="Double Session">
                <div class="pkg-card-body">
                    <div>
                        <h3 class="pkg-name">PACKAGE 2: DOUBLE SESSION</h3>
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

            <!-- Package 3 -->
            <div class="pkg-card">
                <img src="https://images.unsplash.com/photo-1517457373958-b7bdd4587205?auto=format&fit=crop&w=800&q=80" class="pkg-card-img" alt="Group Session">
                <div class="pkg-card-body">
                    <div>
                        <h3 class="pkg-name">PACKAGE 3: GROUP SESSION</h3>
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

    <!-- FLAVOUR SELECTION -->
    <section>
        <div class="section-title-wrap">
            <span class="section-label">AUTHENTIC TOBACCO</span>
            <h2>CHOOSE YOUR FLAVOUR</h2>
        </div>

        <div class="flavour-grid">
            <div class="flavour-card" onclick="openOrderModal()">
                <img src="https://images.unsplash.com/photo-1560806887-1e4cd0b6cbd6?auto=format&fit=crop&w=600&q=80" class="flavour-img" alt="Double Apple">
                <div class="flavour-info">
                    <h4>Al Fakher Double Apple</h4>
                    <span>AUTHENTIC CLASSIC</span>
                </div>
            </div>

            <div class="flavour-card" onclick="openOrderModal()">
                <img src="https://images.unsplash.com/photo-1628557044797-f21a177c37ec?auto=format&fit=crop&w=600&q=80" class="flavour-img" alt="Fresh Mint">
                <div class="flavour-info">
                    <h4>Al Fakher Fresh Mint</h4>
                    <span>PURE COOLING</span>
                </div>
            </div>

            <div class="flavour-card" onclick="openOrderModal()">
                <img src="https://images.unsplash.com/photo-1589984662646-e7b2e4962f18?auto=format&fit=crop&w=600&q=80" class="flavour-img" alt="Love 66">
                <div class="flavour-info">
                    <h4>Adalya Love 66</h4>
                    <span>WATERMELON & MELON</span>
                </div>
            </div>

            <div class="flavour-card" onclick="openOrderModal()">
                <img src="https://images.unsplash.com/photo-1553279768-865429fa0078?auto=format&fit=crop&w=600&q=80" class="flavour-img" alt="Lady Killer">
                <div class="flavour-info">
                    <h4>Adalya Lady Killer</h4>
                    <span>MANGO & BERRIES</span>
                </div>
            </div>

            <div class="flavour-card" onclick="openOrderModal()">
                <img src="https://images.unsplash.com/photo-1587049352847-4a222e784d38?auto=format&fit=crop&w=600&q=80" class="flavour-img" alt="Watermelon Mint">
                <div class="flavour-info">
                    <h4>Mazaya Watermelon Mint</h4>
                    <span>SWEET REFRESHING</span>
                </div>
            </div>

            <div class="flavour-card" onclick="openOrderModal()">
                <img src="https://images.unsplash.com/photo-1615485290382-441e4d049cb5?auto=format&fit=crop&w=600&q=80" class="flavour-img" alt="Paan Ras">
                <div class="flavour-info">
                    <h4>Paan Ras / Paan Mint</h4>
                    <span>TRADITIONAL SPICED</span>
                </div>
            </div>

            <div class="flavour-card" onclick="openOrderModal()">
                <img src="https://images.unsplash.com/photo-1582058091505-f87a2e55a40f?auto=format&fit=crop&w=600&q=80" class="flavour-img" alt="Starburst Mix">
                <div class="flavour-info">
                    <h4>Starburst Candy Mix</h4>
                    <span>SWEET GOURMET</span>
                </div>
            </div>

            <div class="flavour-card" onclick="openOrderModal()">
                <img src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=600&q=80" class="flavour-img" alt="Savaco Luxury">
                <div class="flavour-info">
                    <h4>Savaco Luxury Line</h4>
                    <span>GOLDEN TOBACCO (+£30)</span>
                </div>
            </div>
        </div>
    </section>

    <!-- OPTIONAL UPGRADES -->
    <section style="background: #0B0D13;">
        <div class="section-title-wrap">
            <span class="section-label">CUSTOM PRESENTATION</span>
            <h2>OPTIONAL UPGRADES</h2>
        </div>

        <div class="upgrades-grid">
            <div class="upgrade-card">
                <img src="https://images.unsplash.com/photo-1550258987-190a2d41a8ba?auto=format&fit=crop&w=600&q=80" class="upgrade-img" alt="Fresh Fruit Head">
                <div class="upgrade-body">
                    <div class="upgrade-header">
                        <h4>FRESH FRUIT HEAD</h4>
                        <span class="upgrade-price">+£30</span>
                    </div>
                    <p>Carved fresh fruit bowl for longer sessions and an elevated presentation.</p>
                </div>
            </div>

            <div class="upgrade-card">
                <img src="https://images.unsplash.com/photo-1508873696983-2df515122519?auto=format&fit=crop&w=600&q=80" class="upgrade-img" alt="Electric Coal Burner">
                <div class="upgrade-body">
                    <div class="upgrade-header">
                        <h4>ELECTRIC COAL BURNER</h4>
                        <span class="upgrade-price">+£35</span>
                    </div>
                    <p>High-speed electric burner for convenient coal preparation.</p>
                </div>
            </div>

            <div class="upgrade-card">
                <img src="https://images.unsplash.com/photo-1613478223719-2ab802602423?auto=format&fit=crop&w=600&q=80" class="upgrade-img" alt="Chilled Juice Base">
                <div class="upgrade-body">
                    <div class="upgrade-header">
                        <h4>CHILLED JUICE BASE</h4>
                        <span class="upgrade-price">+£15</span>
                    </div>
                    <p>Replace the standard water base with chilled apple, orange or pineapple juice.</p>
                </div>
            </div>

            <div class="upgrade-card">
                <img src="https://images.unsplash.com/photo-1563245372-f21724e3856d?auto=format&fit=crop&w=600&q=80" class="upgrade-img" alt="Under-Shisha LED Base">
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

    <!-- THE EXPERIENCE -->
    <section>
        <div class="section-title-wrap">
            <span class="section-label">WHITE GLOVE CONCIERGE</span>
            <h2>MORE THAN A DELIVERY.</h2>
        </div>

        <div style="max-width: 900px; margin: 0 auto; text-align: center;">
            <p style="font-size: 1.25rem; color: var(--text-ivory); margin-bottom: 40px; font-weight: 300;">We provide a complete luxury service: bespoke shisha pipes, fresh authentic tobacco, natural coconut coals, sterile mouthpieces, and professional setup delivered directly to your door.</p>

            <div style="display: flex; justify-content: center; gap: 40px; flex-wrap: wrap;">
                <div style="text-align: center;">
                    <i class="fa-solid fa-gem" style="font-size: 2rem; color: var(--gold); margin-bottom: 10px;"></i>
                    <h4 style="font-size: 1rem;">PREMIUM PIPES</h4>
                </div>
                <div style="text-align: center;">
                    <i class="fa-solid fa-leaf" style="font-size: 2rem; color: var(--gold); margin-bottom: 10px;"></i>
                    <h4 style="font-size: 1rem;">AUTHENTIC TOBACCO</h4>
                </div>
                <div style="text-align: center;">
                    <i class="fa-solid fa-fire" style="font-size: 2rem; color: var(--gold); margin-bottom: 10px;"></i>
                    <h4 style="font-size: 1rem;">COCONUT COALS</h4>
                </div>
                <div style="text-align: center;">
                    <i class="fa-solid fa-shield-halved" style="font-size: 2rem; color: var(--gold); margin-bottom: 10px;"></i>
                    <h4 style="font-size: 1rem;">STERILE TIPS</h4>
                </div>
            </div>
        </div>
    </section>

    <!-- COVERAGE -->
    <section style="background: #0B0D13;">
        <div class="section-title-wrap">
            <span class="section-label">DISPATCH FLEET</span>
            <h2>CENTRAL LONDON, DELIVERED.</h2>
        </div>

        <div class="coverage-grid">
            <div class="coverage-item">
                <strong>Westminster</strong>
                <span>20 – 30 MINS</span>
            </div>
            <div class="coverage-item">
                <strong>Knightsbridge</strong>
                <span>20 – 30 MINS</span>
            </div>
            <div class="coverage-item">
                <strong>Chelsea</strong>
                <span>20 – 35 MINS</span>
            </div>
            <div class="coverage-item">
                <strong>Vauxhall</strong>
                <span>25 – 35 MINS</span>
            </div>
            <div class="coverage-item">
                <strong>South Kensington</strong>
                <span>25 – 35 MINS</span>
            </div>
            <div class="coverage-item">
                <strong>High Street Kensington</strong>
                <span>25 – 40 MINS</span>
            </div>
            <div class="coverage-item">
                <strong>Baker Street</strong>
                <span>30 – 40 MINS</span>
            </div>
            <div class="coverage-item">
                <strong>Marble Arch</strong>
                <span>30 – 40 MINS</span>
            </div>
        </div>
    </section>

    <!-- 24/7 SERVICE -->
    <section>
        <div style="max-width: 800px; margin: 0 auto; text-align: center; background: var(--bg-card); border: 1px solid var(--border-gold); padding: 50px; border-radius: 4px;">
            <span class="section-label">ROUND THE CLOCK</span>
            <h2 style="font-size: 2.2rem; margin-bottom: 20px;">AVAILABLE 24/7.</h2>
            <p style="color: var(--text-muted); font-size: 1.1rem; margin-bottom: 30px;">Whether you're hosting at home, staying in a hotel or arranging a private gathering, our Central London delivery service operates around the clock.</p>
            <a href="tel:07903375779" class="btn-concierge"><i class="fa-solid fa-phone"></i> CALL 07903375779</a>
        </div>
    </section>

    <!-- FINAL CTA -->
    <section style="background: linear-gradient(180deg, rgba(8, 9, 12, 0.6) 0%, rgba(8, 9, 12, 0.98) 100%), url('https://images.unsplash.com/photo-1517457373958-b7bdd4587205?auto=format&fit=crop&w=1920&q=80') center/cover no-repeat; text-align: center; padding: 120px 6%;">
        <div style="max-width: 800px; margin: 0 auto;">
            <h2 style="font-size: 3.5rem; line-height: 1.1; margin-bottom: 30px;">YOUR SHISHA.<br><span>YOUR SPACE. YOUR NIGHT.</span></h2>
            
            <div style="display: flex; justify-content: center; gap: 20px; flex-wrap: wrap; margin-bottom: 30px;">
                <button onclick="openOrderModal('PRIVATE SESSION', 50)" class="btn-concierge" style="padding: 16px 36px;">BOOK YOUR SHISHA</button>
                <a href="https://wa.me/447903375779" target="_blank" class="btn-outline" style="padding: 16px 36px;"><i class="fa-brands fa-whatsapp"></i> WHATSAPP CONCIERGE</a>
            </div>

            <p style="font-size: 1.2rem; color: var(--gold); font-family: 'Cinzel', serif; font-weight: 700;">DIRECT HOTLINE: 07903375779</p>
        </div>
    </section>
""" + get_footer()

with open(os.path.join(target_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(index_html)

# MENU.HTML
menu_html = get_header("flavours") + """
    <section class="hero" style="min-height: 40vh; align-items: center;">
        <div class="hero-content">
            <span class="hero-trust">CURATED AUTHENTIC SELECTION</span>
            <h1>CHOOSE YOUR FLAVOUR</h1>
            <p class="hero-p">100% authentic tobacco brands delivered with ready-to-smoke setups in Central London.</p>
        </div>
    </section>

    <section>
        <div class="flavour-grid">
            <div class="flavour-card" onclick="openOrderModal()">
                <img src="https://images.unsplash.com/photo-1560806887-1e4cd0b6cbd6?auto=format&fit=crop&w=600&q=80" class="flavour-img" alt="Double Apple">
                <div class="flavour-info">
                    <h4>Al Fakher Double Apple</h4>
                    <span>AUTHENTIC CLASSIC</span>
                </div>
            </div>

            <div class="flavour-card" onclick="openOrderModal()">
                <img src="https://images.unsplash.com/photo-1628557044797-f21a177c37ec?auto=format&fit=crop&w=600&q=80" class="flavour-img" alt="Fresh Mint">
                <div class="flavour-info">
                    <h4>Al Fakher Fresh Mint</h4>
                    <span>PURE COOLING</span>
                </div>
            </div>

            <div class="flavour-card" onclick="openOrderModal()">
                <img src="https://images.unsplash.com/photo-1589984662646-e7b2e4962f18?auto=format&fit=crop&w=600&q=80" class="flavour-img" alt="Love 66">
                <div class="flavour-info">
                    <h4>Adalya Love 66</h4>
                    <span>WATERMELON & MELON</span>
                </div>
            </div>

            <div class="flavour-card" onclick="openOrderModal()">
                <img src="https://images.unsplash.com/photo-1553279768-865429fa0078?auto=format&fit=crop&w=600&q=80" class="flavour-img" alt="Lady Killer">
                <div class="flavour-info">
                    <h4>Adalya Lady Killer</h4>
                    <span>MANGO & BERRIES</span>
                </div>
            </div>

            <div class="flavour-card" onclick="openOrderModal()">
                <img src="https://images.unsplash.com/photo-1587049352847-4a222e784d38?auto=format&fit=crop&w=600&q=80" class="flavour-img" alt="Watermelon Mint">
                <div class="flavour-info">
                    <h4>Mazaya Watermelon Mint</h4>
                    <span>SWEET REFRESHING</span>
                </div>
            </div>

            <div class="flavour-card" onclick="openOrderModal()">
                <img src="https://images.unsplash.com/photo-1615485290382-441e4d049cb5?auto=format&fit=crop&w=600&q=80" class="flavour-img" alt="Paan Ras">
                <div class="flavour-info">
                    <h4>Paan Ras / Paan Mint</h4>
                    <span>TRADITIONAL SPICED</span>
                </div>
            </div>

            <div class="flavour-card" onclick="openOrderModal()">
                <img src="https://images.unsplash.com/photo-1582058091505-f87a2e55a40f?auto=format&fit=crop&w=600&q=80" class="flavour-img" alt="Starburst Mix">
                <div class="flavour-info">
                    <h4>Starburst Candy Mix</h4>
                    <span>SWEET GOURMET</span>
                </div>
            </div>

            <div class="flavour-card" onclick="openOrderModal()">
                <img src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=600&q=80" class="flavour-img" alt="Savaco Luxury">
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

# PACKAGES.HTML
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
                <img src="https://images.unsplash.com/photo-1527661591475-527312dd65f5?auto=format&fit=crop&w=800&q=80" class="pkg-card-img" alt="Private Session">
                <div class="pkg-card-body">
                    <div>
                        <h3 class="pkg-name">PACKAGE 1: PRIVATE SESSION</h3>
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
                <img src="https://images.unsplash.com/photo-1541532713592-79a0317b6b77?auto=format&fit=crop&w=800&q=80" class="pkg-card-img" alt="Double Session">
                <div class="pkg-card-body">
                    <div>
                        <h3 class="pkg-name">PACKAGE 2: DOUBLE SESSION</h3>
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
                <img src="https://images.unsplash.com/photo-1517457373958-b7bdd4587205?auto=format&fit=crop&w=800&q=80" class="pkg-card-img" alt="Group Session">
                <div class="pkg-card-body">
                    <div>
                        <h3 class="pkg-name">PACKAGE 3: GROUP SESSION</h3>
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

# AREAS.HTML
areas_html = get_header("coverage") + """
    <section class="hero" style="min-height: 40vh; align-items: center;">
        <div class="hero-content">
            <span class="hero-trust">DISPATCH FLEET</span>
            <h1>CENTRAL LONDON, DELIVERED.</h1>
            <p class="hero-p">Delivery drivers on standby 24/7 across all major Central London locations.</p>
        </div>
    </section>

    <section>
        <div class="coverage-grid">
            <div class="coverage-item">
                <strong>Westminster</strong>
                <span>20 – 30 MINS</span>
            </div>
            <div class="coverage-item">
                <strong>Knightsbridge</strong>
                <span>20 – 30 MINS</span>
            </div>
            <div class="coverage-item">
                <strong>Chelsea</strong>
                <span>20 – 35 MINS</span>
            </div>
            <div class="coverage-item">
                <strong>Vauxhall</strong>
                <span>25 – 35 MINS</span>
            </div>
            <div class="coverage-item">
                <strong>South Kensington</strong>
                <span>25 – 35 MINS</span>
            </div>
            <div class="coverage-item">
                <strong>High Street Kensington</strong>
                <span>25 – 40 MINS</span>
            </div>
            <div class="coverage-item">
                <strong>Baker Street</strong>
                <span>30 – 40 MINS</span>
            </div>
            <div class="coverage-item">
                <strong>Marble Arch</strong>
                <span>30 – 40 MINS</span>
            </div>
        </div>
    </section>
""" + get_footer()

with open(os.path.join(target_dir, "areas.html"), "w", encoding="utf-8") as f:
    f.write(areas_html)

# ABOUT.HTML & CONTACT.HTML
about_html = get_header("experience") + """
    <section class="hero" style="min-height: 40vh; align-items: center;">
        <div class="hero-content">
            <span class="hero-trust">WHITE GLOVE CONCIERGE</span>
            <h1>MORE THAN A DELIVERY.</h1>
            <p class="hero-p">Providing Central London with pristine, lounge-grade shisha sessions delivered straight to private residences, hotels, and luxury apartments.</p>
        </div>
    </section>

    <section>
        <div style="max-width: 800px; margin: 0 auto; text-align: center; background: var(--bg-card); border: 1px solid var(--border-gold); padding: 50px; border-radius: 4px;">
            <h2 style="font-size: 2.2rem; margin-bottom: 20px;">AVAILABLE 24/7.</h2>
            <p style="color: var(--text-muted); font-size: 1.1rem; margin-bottom: 30px;">Whether you're hosting at home, staying in a hotel or arranging a private gathering, our Central London delivery service operates around the clock.</p>
            <a href="tel:07903375779" class="btn-concierge"><i class="fa-solid fa-phone"></i> CALL 07903375779</a>
        </div>
    </section>
""" + get_footer()

with open(os.path.join(target_dir, "about.html"), "w", encoding="utf-8") as f:
    f.write(about_html)

contact_html = get_header("contact") + """
    <section class="hero" style="min-height: 40vh; align-items: center;">
        <div class="hero-content">
            <span class="hero-trust">DIRECT HOTLINE</span>
            <h1>CONTACT CONCIERGE</h1>
            <p class="hero-p">Call or message us directly on WhatsApp for immediate Central London shisha delivery.</p>
        </div>
    </section>

    <section>
        <div style="max-width: 800px; margin: 0 auto; text-align: center; background: var(--bg-card); border: 1px solid var(--border-gold); padding: 50px; border-radius: 4px;">
            <h2 style="color: #FFF; margin-bottom: 10px;">WHATSAPP CONCIERGE</h2>
            <p style="font-size: 1.3rem; color: var(--gold); font-weight: bold; margin-bottom: 25px;">07903375779</p>
            <a href="https://wa.me/447903375779" target="_blank" class="btn-concierge" style="padding: 16px 36px; font-size: 1rem;"><i class="fa-brands fa-whatsapp"></i> CHAT VIA WHATSAPP</a>
        </div>
    </section>
""" + get_footer()

with open(os.path.join(target_dir, "contact.html"), "w", encoding="utf-8") as f:
    f.write(contact_html)

print("[+] All concierge rebrand HTML pages generated successfully!")
