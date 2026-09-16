import os

target_dir = r"C:\Users\fifia\.gemini\antigravity\scratch\shisha-delivery-london"

def get_header(active_page="home"):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>24 HOUR SHISHA DELIVERY | Ultra-Premium Hookah Delivery Central London</title>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800;900&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="top-announcement">
        <div>
            <span><i class="fa-solid fa-moon"></i> 24/7 EXPRESS SHISHA DELIVERY</span>
            <span><i class="fa-solid fa-truck-fast"></i> Central London Within 30-45 Mins</span>
        </div>
        <div>
            <span><i class="fa-solid fa-phone" style="color: var(--gold);"></i> Call Now: <strong style="color: #FFF;">07903375779</strong></span>
            <span><i class="fa-solid fa-envelope" style="color: var(--gold);"></i> Mrshawest26@gmail.com</span>
        </div>
    </div>

    <header>
        <div class="nav-container">
            <a href="index.html" class="logo">
                <i class="fa-solid fa-fire-burner logo-icon"></i>
                <div class="logo-text">
                    <h1>SHISHA DELIVERY</h1>
                    <span>24/7 CENTRAL LONDON</span>
                </div>
            </a>
            <nav>
                <ul>
                    <li><a href="index.html" class="{'active' if active_page == 'home' else ''}">Home</a></li>
                    <li><a href="menu.html" class="{'active' if active_page == 'menu' else ''}">Flavour Menu</a></li>
                    <li><a href="packages.html" class="{'active' if active_page == 'packages' else ''}">Packages & Pricing</a></li>
                    <li><a href="areas.html" class="{'active' if active_page == 'areas' else ''}">Coverage Areas</a></li>
                    <li><a href="about.html" class="{'active' if active_page == 'about' else ''}">Our 24/7 Promise</a></li>
                    <li><a href="contact.html" class="{'active' if active_page == 'contact' else ''}">Contact</a></li>
                </ul>
            </nav>
            <div style="display: flex; gap: 10px;">
                <a href="https://wa.me/447903375779" target="_blank" class="btn-whatsapp"><i class="fa-brands fa-whatsapp"></i> WhatsApp Order</a>
                <a href="tel:07903375779" class="btn-gold"><i class="fa-solid fa-phone"></i> 07903375779</a>
            </div>
        </div>
    </header>
"""

def get_footer():
    return """
    <footer>
        <div class="footer-grid">
            <div class="footer-col">
                <div class="logo" style="margin-bottom: 20px;">
                    <i class="fa-solid fa-fire-burner logo-icon"></i>
                    <div class="logo-text">
                        <h1 style="color: #FFF;">SHISHA DELIVERY</h1>
                        <span>24/7 CENTRAL LONDON</span>
                    </div>
                </div>
                <p style="margin-bottom: 15px;">London's premier 24-hour shisha delivery service. Delivering ready-to-smoke luxury pipes, premium authentic flavours, and glowing coals straight to your doorstep.</p>
                <p><i class="fa-solid fa-phone" style="color: var(--gold);"></i> <strong>07903375779</strong> (24/7 Delivery Line)</p>
                <p><i class="fa-solid fa-envelope" style="color: var(--gold);"></i> Mrshawest26@gmail.com</p>
            </div>
            
            <div class="footer-col">
                <h4>Coverage Areas</h4>
                <ul>
                    <li><a href="areas.html">Westminster Delivery</a></li>
                    <li><a href="areas.html">Knightsbridge Delivery</a></li>
                    <li><a href="areas.html">Chelsea Delivery</a></li>
                    <li><a href="areas.html">Vauxhall Delivery</a></li>
                    <li><a href="areas.html">South Kensington Delivery</a></li>
                    <li><a href="areas.html">High Street Kensington</a></li>
                    <li><a href="areas.html">Baker Street & Marble Arch</a></li>
                </ul>
            </div>

            <div class="footer-col">
                <h4>Flavour Brands</h4>
                <ul>
                    <li><a href="menu.html">Al Fakher Signature Collection</a></li>
                    <li><a href="menu.html">Adalya (Love 66 & Lady Killer)</a></li>
                    <li><a href="menu.html">Mazaya Premium Blends</a></li>
                    <li><a href="menu.html">Layali Exotic Flavours</a></li>
                    <li><a href="menu.html">Paan Ras & Paan Mint</a></li>
                    <li><a href="menu.html">Starburst Candy Flavours</a></li>
                    <li><a href="menu.html">Savaco £30 Luxury Line</a></li>
                </ul>
            </div>

            <div class="footer-col">
                <h4>Packages & Extras</h4>
                <p style="color: var(--gold); font-weight: bold; margin-bottom: 8px;">1 Shisha Set: £50</p>
                <p style="color: var(--gold); font-weight: bold; margin-bottom: 8px;">2 Shisha Set: £80</p>
                <p style="color: var(--gold); font-weight: bold; margin-bottom: 15px;">3 Shisha Set: £110</p>
                <a href="#builder" class="btn-gold" style="width: 100%; justify-content: center;">Build Your Session</a>
            </div>
        </div>

        <div style="text-align: center; border-top: 1px solid rgba(255,255,255,0.05); padding-top: 25px;">
            <p>&copy; 2026 Shisha Delivery 24/7. All Rights Reserved. | Strictly 18+ Adults Only. Enjoy Responsibly. | 07903375779</p>
        </div>
    </footer>

    <!-- Sticky Mobile Order Bar -->
    <div class="sticky-order-bar">
        <div>
            <span style="font-size: 0.75rem; text-transform: uppercase; color: var(--gold); font-weight: bold; display: block;">24/7 Delivery Line</span>
            <strong style="font-size: 1.1rem; color: #FFF;">07903375779</strong>
        </div>
        <div style="display: flex; gap: 10px;">
            <a href="https://wa.me/447903375779" class="btn-whatsapp"><i class="fa-brands fa-whatsapp"></i> Order WhatsApp</a>
            <a href="tel:07903375779" class="btn-gold"><i class="fa-solid fa-phone"></i> Call 24/7</a>
        </div>
    </div>

    <script src="script.js"></script>
</body>
</html>
"""

# INDEX.HTML
index_html = get_header("home") + """
    <section class="hero">
        <div class="hero-grid">
            <div>
                <span class="hero-badge"><i class="fa-solid fa-bolt"></i> 24/7 Immediate Delivery in 30 Mins</span>
                <h1>SAME FLAVOURS. SAME VIBE. <span>AT YOUR DOOR.</span></h1>
                <p>Ultra-premium hookah pipes, authentic tobacco brands, and glowing charcoal delivered ready-to-smoke anywhere in Central London.</p>
                <div class="hero-actions">
                    <a href="#builder" class="btn-gold"><i class="fa-solid fa-sliders"></i> Build & Order Session</a>
                    <a href="https://wa.me/447903375779" target="_blank" class="btn-whatsapp"><i class="fa-brands fa-whatsapp"></i> Instant WhatsApp Order</a>
                </div>
            </div>

            <div class="hero-card-preview">
                <span class="preview-badge">Most Popular Package</span>
                <h3 style="font-size: 1.6rem; color: var(--gold); margin-bottom: 10px;">2 SHISHA COMPLETE SET</h3>
                <p style="color: var(--text-gray); font-size: 0.95rem; margin-bottom: 20px;">Includes 2 luxury shisha pipes, 2 fruit/clay heads of your choice, electric coal burner, 20 coals, and sterile tips.</p>
                <div style="display: flex; justify-content: space-between; align-items: center; background: rgba(0,0,0,0.4); padding: 15px; border-radius: 8px;">
                    <div>
                        <span style="font-size: 0.8rem; color: var(--text-gray); display: block;">SPECIAL BUNDLE</span>
                        <strong style="font-size: 2rem; color: #FFF;">£80</strong>
                    </div>
                    <a href="#builder" class="btn-gold">Order Now</a>
                </div>
            </div>
        </div>
    </section>

    <div class="features-strip">
        <div class="feature-box">
            <i class="fa-solid fa-gem"></i>
            <h4>100% Authentic Brands</h4>
            <p>Al Fakher, Adalya, Mazaya, Layali, Paan, and Savaco Luxury.</p>
        </div>
        <div class="feature-box">
            <i class="fa-solid fa-clock"></i>
            <h4>24/7 Non-Stop Service</h4>
            <p>Day or night, our drivers arrive at your door in 30-45 mins.</p>
        </div>
        <div class="feature-box">
            <i class="fa-solid fa-user-shield"></i>
            <h4>100% Discreet & Clean</h4>
            <p>Sanitised equipment and individual sealed mouthpieces.</p>
        </div>
        <div class="feature-box">
            <i class="fa-solid fa-truck-ramp-box"></i>
            <h4>Central London Fleet</h4>
            <p>Westminster, Knightsbridge, Chelsea, Vauxhall & Kensington.</p>
        </div>
    </div>

    <!-- Interactive Configurator -->
    <section id="builder" class="builder-section">
        <div class="section-header">
            <span class="section-subtitle">High-Conversion Order Engine</span>
            <h2>Build Your 24/7 Shisha Order</h2>
        </div>

        <div class="config-container">
            <div class="config-options">
                <!-- Step 1 -->
                <div class="step-title">
                    <i class="fa-solid fa-circle-1" style="color: var(--gold);"></i> Step 1: Select Shisha Package
                </div>
                <div class="package-cards">
                    <div class="pkg-card" onclick="selectPkg('1 Shisha Set', 50, this)">
                        <h4 style="font-size: 1rem;">1 Shisha</h4>
                        <div class="pkg-price">£50</div>
                        <span style="font-size: 0.75rem; color: var(--text-gray);">1 Pipe + Coals</span>
                    </div>

                    <div class="pkg-card active" onclick="selectPkg('2 Shisha Set', 80, this)">
                        <h4 style="font-size: 1rem;">2 Shisha</h4>
                        <div class="pkg-price">£80</div>
                        <span style="font-size: 0.75rem; color: var(--gold);">Best Value Bundle</span>
                    </div>

                    <div class="pkg-card" onclick="selectPkg('3 Shisha Set', 110, this)">
                        <h4 style="font-size: 1rem;">3 Shisha</h4>
                        <div class="pkg-price">£110</div>
                        <span style="font-size: 0.75rem; color: var(--text-gray);">VIP Group Party</span>
                    </div>
                </div>

                <!-- Step 2 -->
                <div class="step-title">
                    <i class="fa-solid fa-circle-2" style="color: var(--gold);"></i> Step 2: Select Premium Flavour
                </div>
                <div class="flavour-grid">
                    <div class="flavour-chip active" onclick="selectFlavour('Al Fakher Double Apple', this)"><i class="fa-solid fa-apple-whole"></i> Double Apple</div>
                    <div class="flavour-chip" onclick="selectFlavour('Al Fakher Mint', this)"><i class="fa-solid fa-leaf"></i> Fresh Mint</div>
                    <div class="flavour-chip" onclick="selectFlavour('Adalya Love 66', this)"><i class="fa-solid fa-heart"></i> Love 66</div>
                    <div class="flavour-chip" onclick="selectFlavour('Adalya Lady Killer', this)"><i class="fa-solid fa-crown"></i> Lady Killer</div>
                    <div class="flavour-chip" onclick="selectFlavour('Mazaya Watermelon Mint', this)"><i class="fa-solid fa-water-ladder"></i> Watermelon</div>
                    <div class="flavour-chip" onclick="selectFlavour('Paan Ras / Paan Mint', this)"><i class="fa-solid fa-cannabis"></i> Paan Ras</div>
                    <div class="flavour-chip" onclick="selectFlavour('Starburst Sweet Mix', this)"><i class="fa-solid fa-candy-cane"></i> Starburst</div>
                    <div class="flavour-chip" onclick="selectFlavour('Savaco Luxury (£30/50g)', this)"><i class="fa-solid fa-gem"></i> Savaco (£30)</div>
                </div>

                <!-- Step 3 -->
                <div class="step-title">
                    <i class="fa-solid fa-circle-3" style="color: var(--gold);"></i> Step 3: Add Extras & Upgrades
                </div>
                <div class="addons-list">
                    <label class="addon-item">
                        <span><input type="checkbox" onchange="toggleAddon('Extra Fruit/Clay Head', 30, this)"> Extra Fruit/Clay Head</span>
                        <strong style="color: var(--gold);">+£30</strong>
                    </label>

                    <label class="addon-item">
                        <span><input type="checkbox" onchange="toggleAddon('Extra 10 Coals', 5, this)"> Extra 10 Coals</span>
                        <strong style="color: var(--gold);">+£5</strong>
                    </label>

                    <label class="addon-item">
                        <span><input type="checkbox" onchange="toggleAddon('Electric Coal Burner', 35, this)"> Coal Burner</span>
                        <strong style="color: var(--gold);">+£35</strong>
                    </label>

                    <label class="addon-item">
                        <span><input type="checkbox" onchange="toggleAddon('Fresh Juice Base (Apple/Orange)', 15, this)"> Liquid Base</span>
                        <strong style="color: var(--gold);">+£15</strong>
                    </label>

                    <label class="addon-item">
                        <span><input type="checkbox" onchange="toggleAddon('LED Under-Glow Light Base', 15, this)"> Under-Glow LED</span>
                        <strong style="color: var(--gold);">+£15</strong>
                    </label>

                    <label class="addon-item">
                        <span><input type="checkbox" onchange="toggleAddon('Extra 50g Flavour Pack', 10, this)"> Extra 50g Flavour</span>
                        <strong style="color: var(--gold);">+£10</strong>
                    </label>
                </div>
            </div>

            <div class="config-summary">
                <div>
                    <h3 class="summary-title"><i class="fa-solid fa-receipt" style="color: var(--gold);"></i> Order Checkout Summary</h3>
                    
                    <div class="summary-rows">
                        <div class="summary-row">
                            <span>Selected Package:</span>
                            <strong id="sum-pkg">1 Shisha Set (£50)</strong>
                        </div>
                        <div class="summary-row">
                            <span>Primary Flavour:</span>
                            <strong id="sum-flavour">Al Fakher Double Apple</strong>
                        </div>
                        <div class="summary-row">
                            <span>Selected Add-ons:</span>
                            <strong id="sum-addons">None selected</strong>
                        </div>
                    </div>

                    <div style="margin-bottom: 20px;">
                        <input type="text" id="cust-name" placeholder="Your Name" style="width: 100%; padding: 12px; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: 6px; color: #FFF; margin-bottom: 10px;">
                        <select id="cust-area" style="width: 100%; padding: 12px; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: 6px; color: #FFF; margin-bottom: 10px;">
                            <option>Westminster (20-30 Mins)</option>
                            <option>Knightsbridge (20-30 Mins)</option>
                            <option>Chelsea (20-35 Mins)</option>
                            <option>Vauxhall (25-35 Mins)</option>
                            <option>South Kensington (25-35 Mins)</option>
                            <option>High Street Kensington (25-40 Mins)</option>
                            <option>Baker Street (30-40 Mins)</option>
                            <option>Marble Arch (30-40 Mins)</option>
                        </select>
                        <input type="tel" id="cust-phone" placeholder="Your Contact Phone (e.g. 07123456789)" style="width: 100%; padding: 12px; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: 6px; color: #FFF;">
                    </div>
                </div>

                <div>
                    <div class="total-box">
                        <span style="font-size: 0.85rem; color: var(--text-gray); display: block;">TOTAL ESTIMATED PAYABLE:</span>
                        <div class="total-amount" id="grand-total">£50</div>
                    </div>
                    
                    <button class="btn-gold" onclick="sendWhatsAppOrder()" style="width: 100%; justify-content: center; padding: 16px;"><i class="fa-brands fa-whatsapp"></i> Confirm & Dispatch Order via WhatsApp</button>
                    <p style="font-size: 0.75rem; text-align: center; color: var(--text-gray); margin-top: 10px;">Or call 24/7 hotline directly: <a href="tel:07903375779" style="color: var(--gold);">07903375779</a></p>
                </div>
            </div>
        </div>
    </section>

    <!-- Central London Coverage -->
    <section class="areas-section">
        <div class="section-header">
            <span class="section-subtitle">Rapid Dispatch Fleet</span>
            <h2>24/7 Central London Delivery Zones</h2>
        </div>
        <div class="areas-grid">
            <div class="area-card">
                <i class="fa-solid fa-location-dot"></i>
                <div>
                    <strong>Westminster</strong>
                    <p style="font-size: 0.8rem; color: var(--text-gray);">20 - 30 Min Delivery</p>
                </div>
            </div>

            <div class="area-card">
                <i class="fa-solid fa-location-dot"></i>
                <div>
                    <strong>Knightsbridge</strong>
                    <p style="font-size: 0.8rem; color: var(--text-gray);">20 - 30 Min Delivery</p>
                </div>
            </div>

            <div class="area-card">
                <i class="fa-solid fa-location-dot"></i>
                <div>
                    <strong>Chelsea</strong>
                    <p style="font-size: 0.8rem; color: var(--text-gray);">20 - 35 Min Delivery</p>
                </div>
            </div>

            <div class="area-card">
                <i class="fa-solid fa-location-dot"></i>
                <div>
                    <strong>Vauxhall</strong>
                    <p style="font-size: 0.8rem; color: var(--text-gray);">25 - 35 Min Delivery</p>
                </div>
            </div>

            <div class="area-card">
                <i class="fa-solid fa-location-dot"></i>
                <div>
                    <strong>South Kensington</strong>
                    <p style="font-size: 0.8rem; color: var(--text-gray);">25 - 35 Min Delivery</p>
                </div>
            </div>

            <div class="area-card">
                <i class="fa-solid fa-location-dot"></i>
                <div>
                    <strong>High Street Kensington</strong>
                    <p style="font-size: 0.8rem; color: var(--text-gray);">25 - 40 Min Delivery</p>
                </div>
            </div>

            <div class="area-card">
                <i class="fa-solid fa-location-dot"></i>
                <div>
                    <strong>Baker Street</strong>
                    <p style="font-size: 0.8rem; color: var(--text-gray);">30 - 40 Min Delivery</p>
                </div>
            </div>

            <div class="area-card">
                <i class="fa-solid fa-location-dot"></i>
                <div>
                    <strong>Marble Arch</strong>
                    <p style="font-size: 0.8rem; color: var(--text-gray);">30 - 40 Min Delivery</p>
                </div>
            </div>
        </div>
    </section>
""" + get_footer()

with open(os.path.join(target_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(index_html)

# MENU.HTML
menu_html = get_header("menu") + """
    <section class="hero" style="padding: 60px 5%;">
        <div style="max-width: 800px; margin: 0 auto; text-align: center;">
            <span class="hero-badge">Curated Tobacco Selection</span>
            <h1>Full 24/7 Flavour Menu & Add-ons</h1>
            <p>100% authentic tobacco brands, fresh fruit heads, and liquid bases delivered ready to smoke in Central London.</p>
        </div>
    </section>

    <section style="padding: 60px 5%; max-width: 1200px; margin: 0 auto;">
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px;">
            <div style="background: var(--bg-card); border: 1px solid var(--border-gold); padding: 30px; border-radius: 12px;">
                <h3 style="color: var(--gold); margin-bottom: 15px;">Al Fakher Collection</h3>
                <p style="font-size: 0.9rem; color: var(--text-gray); margin-bottom: 20px;">The world's most iconic smooth tobacco.</p>
                <ul style="line-height: 2;">
                    <li><i class="fa-solid fa-check" style="color: var(--gold);"></i> Double Apple (Classic)</li>
                    <li><i class="fa-solid fa-check" style="color: var(--gold);"></i> Fresh Mint</li>
                    <li><i class="fa-solid fa-check" style="color: var(--gold);"></i> Grape & Mint</li>
                    <li><i class="fa-solid fa-check" style="color: var(--gold);"></i> Blueberry Mist</li>
                    <li><i class="fa-solid fa-check" style="color: var(--gold);"></i> Watermelon Chill</li>
                </ul>
            </div>

            <div style="background: var(--bg-card); border: 1px solid var(--border-gold); padding: 30px; border-radius: 12px;">
                <h3 style="color: var(--gold); margin-bottom: 15px;">Adalya Premium Blends</h3>
                <p style="font-size: 0.9rem; color: var(--text-gray); margin-bottom: 20px;">Exotic modern Turkish tobacco recipes.</p>
                <ul style="line-height: 2;">
                    <li><i class="fa-solid fa-check" style="color: var(--gold);"></i> Love 66 (Watermelon, Passionfruit, Melon, Mint)</li>
                    <li><i class="fa-solid fa-check" style="color: var(--gold);"></i> Lady Killer (Mango, Melon, Berries, Mint)</li>
                    <li><i class="fa-solid fa-check" style="color: var(--gold);"></i> Mango Tango</li>
                    <li><i class="fa-solid fa-check" style="color: var(--gold);"></i> Hawai (Pineapple, Mango, Mint)</li>
                </ul>
            </div>

            <div style="background: var(--bg-card); border: 1px solid var(--border-gold); padding: 30px; border-radius: 12px;">
                <h3 style="color: var(--gold); margin-bottom: 15px;">Paan & Specialty Blends</h3>
                <p style="font-size: 0.9rem; color: var(--text-gray); margin-bottom: 20px;">Traditional rich spiced betel leaf blends.</p>
                <ul style="line-height: 2;">
                    <li><i class="fa-solid fa-check" style="color: var(--gold);"></i> Paan Ras</li>
                    <li><i class="fa-solid fa-check" style="color: var(--gold);"></i> Paan Mint</li>
                    <li><i class="fa-solid fa-check" style="color: var(--gold);"></i> Starburst Sweet Candy Mix</li>
                    <li><i class="fa-solid fa-check" style="color: var(--gold);"></i> Savaco Luxury (£30/50g)</li>
                </ul>
            </div>
        </div>
    </section>
""" + get_footer()

with open(os.path.join(target_dir, "menu.html"), "w", encoding="utf-8") as f:
    f.write(menu_html)

# PACKAGES.HTML
packages_html = get_header("packages") + """
    <section class="hero" style="padding: 60px 5%;">
        <div style="max-width: 800px; margin: 0 auto; text-align: center;">
            <span class="hero-badge">Transparent Pricing</span>
            <h1>24/7 Delivery Packages</h1>
            <p>Everything included: ready-to-smoke pipes, fresh coal burner, tongs, and individual hygienic tips.</p>
        </div>
    </section>

    <section style="padding: 60px 5%; max-width: 1200px; margin: 0 auto;">
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 30px;">
            <div style="background: var(--bg-card); border: 1px solid rgba(255,255,255,0.1); padding: 40px; border-radius: 16px; text-align: center;">
                <h3 style="font-size: 1.5rem; margin-bottom: 10px;">1 SHISHA SET</h3>
                <div style="font-size: 3rem; font-weight: 800; color: var(--gold); margin: 20px 0;">£50</div>
                <ul style="list-style: none; line-height: 2.2; color: var(--text-gray); margin-bottom: 30px;">
                    <li>1 Premium Hookah Pipe</li>
                    <li>1 Flavour Head of Choice</li>
                    <li>10 Natural Coconut Coals</li>
                    <li>Hygienic Sealed Mouthpieces</li>
                    <li>24/7 Delivery Included</li>
                </ul>
                <a href="index.html#builder" class="btn-gold" style="width: 100%; justify-content: center;">Select This Package</a>
            </div>

            <div style="background: var(--bg-card); border: 2px solid var(--gold); padding: 40px; border-radius: 16px; text-align: center; position: relative;">
                <span style="position: absolute; top: -15px; left: 50%; transform: translateX(-50%); background: var(--gold-gradient); color: #000; font-weight: bold; padding: 4px 16px; border-radius: 20px; font-size: 0.8rem;">MOST POPULAR</span>
                <h3 style="font-size: 1.5rem; margin-bottom: 10px; color: var(--gold);">2 SHISHA SET</h3>
                <div style="font-size: 3rem; font-weight: 800; color: var(--gold); margin: 20px 0;">£80</div>
                <ul style="list-style: none; line-height: 2.2; color: var(--text-gray); margin-bottom: 30px;">
                    <li>2 Premium Hookah Pipes</li>
                    <li>2 Flavour Heads of Choice</li>
                    <li>20 Natural Coconut Coals</li>
                    <li>Electric Coal Burner Included</li>
                    <li>Hygienic Sealed Mouthpieces</li>
                    <li>24/7 Delivery Included</li>
                </ul>
                <a href="index.html#builder" class="btn-gold" style="width: 100%; justify-content: center;">Select This Package</a>
            </div>

            <div style="background: var(--bg-card); border: 1px solid rgba(255,255,255,0.1); padding: 40px; border-radius: 16px; text-align: center;">
                <h3 style="font-size: 1.5rem; margin-bottom: 10px;">3 SHISHA SET</h3>
                <div style="font-size: 3rem; font-weight: 800; color: var(--gold); margin: 20px 0;">£110</div>
                <ul style="list-style: none; line-height: 2.2; color: var(--text-gray); margin-bottom: 30px;">
                    <li>3 Premium Hookah Pipes</li>
                    <li>3 Flavour Heads of Choice</li>
                    <li>30 Natural Coconut Coals</li>
                    <li>Electric Coal Burner Included</li>
                    <li>Hygienic Sealed Mouthpieces</li>
                    <li>24/7 Delivery Included</li>
                </ul>
                <a href="index.html#builder" class="btn-gold" style="width: 100%; justify-content: center;">Select This Package</a>
            </div>
        </div>
    </section>
""" + get_footer()

with open(os.path.join(target_dir, "packages.html"), "w", encoding="utf-8") as f:
    f.write(packages_html)

# AREAS.HTML
areas_html = get_header("areas") + """
    <section class="hero" style="padding: 60px 5%;">
        <div style="max-width: 800px; margin: 0 auto; text-align: center;">
            <span class="hero-badge">Central London Coverage</span>
            <h1>24/7 Shisha Delivery Zones</h1>
            <p>Our dedicated driver fleet delivers ready-to-smoke shisha pipes within 20 to 45 minutes across Central London.</p>
        </div>
    </section>

    <section style="padding: 60px 5%; max-width: 1100px; margin: 0 auto;">
        <div class="areas-grid">
            <div class="area-card">
                <i class="fa-solid fa-building-columns"></i>
                <div>
                    <strong>Westminster</strong>
                    <p style="font-size: 0.85rem; color: var(--text-gray);">SW1A, SW1P, SW1H • 20-30 Mins</p>
                </div>
            </div>

            <div class="area-card">
                <i class="fa-solid fa-crown"></i>
                <div>
                    <strong>Knightsbridge</strong>
                    <p style="font-size: 0.85rem; color: var(--text-gray);">SW1X, SW7 • 20-30 Mins</p>
                </div>
            </div>

            <div class="area-card">
                <i class="fa-solid fa-city"></i>
                <div>
                    <strong>Chelsea</strong>
                    <p style="font-size: 0.85rem; color: var(--text-gray);">SW3, SW10 • 20-35 Mins</p>
                </div>
            </div>

            <div class="area-card">
                <i class="fa-solid fa-bridge"></i>
                <div>
                    <strong>Vauxhall</strong>
                    <p style="font-size: 0.85rem; color: var(--text-gray);">SE11, SW8 • 25-35 Mins</p>
                </div>
            </div>

            <div class="area-card">
                <i class="fa-solid fa-graduation-cap"></i>
                <div>
                    <strong>South Kensington</strong>
                    <p style="font-size: 0.85rem; color: var(--text-gray);">SW7, SW5 • 25-35 Mins</p>
                </div>
            </div>

            <div class="area-card">
                <i class="fa-solid fa-shop"></i>
                <div>
                    <strong>High Street Kensington</strong>
                    <p style="font-size: 0.85rem; color: var(--text-gray);">W8, W14 • 25-40 Mins</p>
                </div>
            </div>

            <div class="area-card">
                <i class="fa-solid fa-hat-cowboy"></i>
                <div>
                    <strong>Baker Street</strong>
                    <p style="font-size: 0.85rem; color: var(--text-gray);">NW1, W1U • 30-40 Mins</p>
                </div>
            </div>

            <div class="area-card">
                <i class="fa-solid fa-monument"></i>
                <div>
                    <strong>Marble Arch</strong>
                    <p style="font-size: 0.85rem; color: var(--text-gray);">W1H, W1C • 30-40 Mins</p>
                </div>
            </div>
        </div>
    </section>
""" + get_footer()

with open(os.path.join(target_dir, "areas.html"), "w", encoding="utf-8") as f:
    f.write(areas_html)

# ABOUT.HTML
about_html = get_header("about") + """
    <section class="hero" style="padding: 60px 5%;">
        <div style="max-width: 800px; margin: 0 auto; text-align: center;">
            <span class="hero-badge">Uncompromising Quality</span>
            <h1>The 24/7 Shisha Delivery Guarantee</h1>
            <p>Providing Central London with pristine, lounge-grade shisha sessions delivered straight to private residences, hotels, and luxury apartments.</p>
        </div>
    </section>

    <section style="padding: 60px 5%; max-width: 900px; margin: 0 auto; line-height: 1.8;">
        <h2 style="color: var(--gold); margin-bottom: 20px;">Why We Are Central London's #1 Choice</h2>
        <p style="color: var(--text-gray); margin-bottom: 20px;">At 24 HOUR SHISHA DELIVERY, we believe you shouldn't have to leave the comfort of your home or hotel room to enjoy a lounge-quality hookah session. Our mobile delivery fleet is equipped to deliver ready-to-smoke setups 24 hours a day, 7 days a week.</p>
        <p style="color: var(--text-gray); margin-bottom: 30px;">Every shisha pipe undergoes rigorous medical-grade steam cleaning after every rental. Tobacco heads are freshly packed to order using 100% authentic Al Fakher, Adalya, and Savaco tobacco brands.</p>

        <div style="background: var(--bg-card); border: 1px solid var(--border-gold); padding: 30px; border-radius: 12px; margin-top: 40px;">
            <h3 style="color: #FFF; margin-bottom: 15px;"><i class="fa-solid fa-headset" style="color: var(--gold);"></i> 24/7 Direct Contact Information</h3>
            <p style="color: var(--text-gray);">Telephone / WhatsApp: <strong style="color: var(--gold);">07903375779</strong></p>
            <p style="color: var(--text-gray);">Email Enquiries: <strong style="color: var(--gold);">Mrshawest26@gmail.com</strong></p>
        </div>
    </section>
""" + get_footer()

with open(os.path.join(target_dir, "about.html"), "w", encoding="utf-8") as f:
    f.write(about_html)

# CONTACT.HTML
contact_html = get_header("contact") + """
    <section class="hero" style="padding: 60px 5%;">
        <div style="max-width: 800px; margin: 0 auto; text-align: center;">
            <span class="hero-badge">24/7 Hotline</span>
            <h1>Contact & Instant Dispatch</h1>
            <p>Call or message us on WhatsApp anytime. Our dispatch team is on standby 24/7.</p>
        </div>
    </section>

    <section style="padding: 60px 5%; max-width: 1000px; margin: 0 auto;">
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 40px;">
            <div style="background: var(--bg-card); border: 1px solid var(--border-gold); padding: 40px; border-radius: 12px;">
                <h3 style="color: var(--gold); margin-bottom: 20px;">24/7 Dispatch Details</h3>
                <div style="margin-bottom: 20px;">
                    <strong style="color: #FFF; display: block;"><i class="fa-solid fa-phone" style="color: var(--gold);"></i> 24/7 Delivery Line</strong>
                    <span style="font-size: 1.2rem; color: var(--gold); font-weight: bold;">07903375779</span>
                </div>
                <div style="margin-bottom: 20px;">
                    <strong style="color: #FFF; display: block;"><i class="fa-brands fa-whatsapp" style="color: #25D366;"></i> WhatsApp Instant Order</strong>
                    <a href="https://wa.me/447903375779" target="_blank" style="color: #25D366; font-weight: bold;">Click Here to Chat on WhatsApp</a>
                </div>
                <div>
                    <strong style="color: #FFF; display: block;"><i class="fa-solid fa-envelope" style="color: var(--gold);"></i> Email Address</strong>
                    <span style="color: var(--text-gray);">Mrshawest26@gmail.com</span>
                </div>
            </div>

            <div style="background: var(--bg-card); border: 1px solid rgba(255,255,255,0.1); padding: 40px; border-radius: 12px;">
                <h3 style="color: #FFF; margin-bottom: 20px;">Send Quick Message</h3>
                <form onsubmit="event.preventDefault(); sendWhatsAppOrder();">
                    <input type="text" placeholder="Your Full Name" required style="width: 100%; padding: 12px; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: 6px; color: #FFF; margin-bottom: 15px;">
                    <input type="tel" placeholder="Your Phone Number" required style="width: 100%; padding: 12px; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: 6px; color: #FFF; margin-bottom: 15px;">
                    <textarea rows="4" placeholder="Your Delivery Address & Special Requests" required style="width: 100%; padding: 12px; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: 6px; color: #FFF; margin-bottom: 15px;"></textarea>
                    <button type="submit" class="btn-gold" style="width: 100%; justify-content: center;">Send Order via WhatsApp</button>
                </form>
            </div>
        </div>
    </section>
""" + get_footer()

with open(os.path.join(target_dir, "contact.html"), "w", encoding="utf-8") as f:
    f.write(contact_html)

print("[+] All Shisha Delivery HTML pages generated successfully!")
