import os

target_dir = r"C:\Users\fifia\.gemini\antigravity\scratch\shisha-delivery-london"

def get_header(active_page="home"):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>24 HOUR SHISHA DELIVERY | Ultra-Premium Hookah Central London</title>
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
            <span><i class="fa-solid fa-phone"></i> Hotline: <strong style="color: #FFF;">07903375779</strong></span>
            <span><i class="fa-solid fa-envelope"></i> Mrshawest26@gmail.com</span>
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
                    <li><a href="areas.html" class="{'active' if active_page == 'areas' else ''}">Coverage Zones</a></li>
                    <li><a href="about.html" class="{'active' if active_page == 'about' else ''}">Our 24/7 Promise</a></li>
                    <li><a href="contact.html" class="{'active' if active_page == 'contact' else ''}">Contact</a></li>
                </ul>
            </nav>
            <div style="display: flex; gap: 12px;">
                <a href="https://wa.me/447903375779" target="_blank" class="btn-whatsapp"><i class="fa-brands fa-whatsapp"></i> WhatsApp Order</a>
                <a href="tel:07903375779" class="btn-gold"><i class="fa-solid fa-phone"></i> 07903375779</a>
            </div>
        </div>
    </header>
"""

def get_footer():
    return """
    <footer>
        <div style="max-width: 1300px; margin: 0 auto; display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 40px; margin-bottom: 40px;">
            <div>
                <div class="logo" style="margin-bottom: 20px;">
                    <i class="fa-solid fa-fire-burner logo-icon"></i>
                    <div class="logo-text">
                        <h1 style="color: #FFF;">SHISHA DELIVERY</h1>
                        <span>24/7 CENTRAL LONDON</span>
                    </div>
                </div>
                <p style="margin-bottom: 15px; color: var(--text-muted); font-size: 0.9rem;">Central London's ultimate 24/7 shisha delivery experience. Ready-to-smoke luxury pipes, premium tobacco brands, and glowing coals straight to your door.</p>
                <p><i class="fa-solid fa-phone" style="color: var(--gold);"></i> <strong style="color: #FFF;">07903375779</strong> (24/7 Hotline)</p>
                <p><i class="fa-solid fa-envelope" style="color: var(--gold);"></i> Mrshawest26@gmail.com</p>
            </div>

            <div>
                <h4 style="color: #FFF; margin-bottom: 20px;">Delivery Zones</h4>
                <ul style="list-style: none; line-height: 2;">
                    <li><a href="areas.html" style="color: var(--text-muted); text-decoration: none;">Westminster (20-30 Mins)</a></li>
                    <li><a href="areas.html" style="color: var(--text-muted); text-decoration: none;">Knightsbridge (20-30 Mins)</a></li>
                    <li><a href="areas.html" style="color: var(--text-muted); text-decoration: none;">Chelsea (20-35 Mins)</a></li>
                    <li><a href="areas.html" style="color: var(--text-muted); text-decoration: none;">Vauxhall (25-35 Mins)</a></li>
                    <li><a href="areas.html" style="color: var(--text-muted); text-decoration: none;">Kensington (25-35 Mins)</a></li>
                    <li><a href="areas.html" style="color: var(--text-muted); text-decoration: none;">Baker Street & Marble Arch</a></li>
                </ul>
            </div>

            <div>
                <h4 style="color: #FFF; margin-bottom: 20px;">Flavour Collections</h4>
                <ul style="list-style: none; line-height: 2;">
                    <li><a href="menu.html" style="color: var(--text-muted); text-decoration: none;">Al Fakher Double Apple & Mint</a></li>
                    <li><a href="menu.html" style="color: var(--text-muted); text-decoration: none;">Adalya Love 66 & Lady Killer</a></li>
                    <li><a href="menu.html" style="color: var(--text-muted); text-decoration: none;">Mazaya Watermelon Mint</a></li>
                    <li><a href="menu.html" style="color: var(--text-muted); text-decoration: none;">Paan Ras & Paan Mint</a></li>
                    <li><a href="menu.html" style="color: var(--text-muted); text-decoration: none;">Starburst Candy Mix</a></li>
                    <li><a href="menu.html" style="color: var(--text-muted); text-decoration: none;">Savaco Luxury Line (£30)</a></li>
                </ul>
            </div>

            <div>
                <h4 style="color: #FFF; margin-bottom: 20px;">Direct Dispatch</h4>
                <p style="color: var(--gold); font-weight: bold; margin-bottom: 8px;">1 Shisha Set: £50</p>
                <p style="color: var(--gold); font-weight: bold; margin-bottom: 8px;">2 Shisha Set: £80</p>
                <p style="color: var(--gold); font-weight: bold; margin-bottom: 20px;">3 Shisha Set: £110</p>
                <a href="#builder" class="btn-gold" style="width: 100%; justify-content: center;">Build & Order Session</a>
            </div>
        </div>

        <div style="text-align: center; border-top: 1px solid rgba(255,255,255,0.08); padding-top: 25px; color: var(--text-muted); font-size: 0.85rem;">
            <p>&copy; 2026 Shisha Delivery 24/7. All Rights Reserved. | Strictly 18+ Adults Only. Enjoy Responsibly. | Phone/WhatsApp: 07903375779</p>
        </div>
    </footer>

    <div class="sticky-bar">
        <div>
            <span style="font-size: 0.75rem; text-transform: uppercase; color: var(--gold); font-weight: 800; display: block;">24/7 Central London Hotline</span>
            <strong style="font-size: 1.2rem; color: #FFF;">07903375779</strong>
        </div>
        <div style="display: flex; gap: 12px;">
            <a href="https://wa.me/447903375779" class="btn-whatsapp"><i class="fa-brands fa-whatsapp"></i> WhatsApp Dispatch</a>
            <a href="#builder" class="btn-gold"><i class="fa-solid fa-sliders"></i> Order Session</a>
        </div>
    </div>

    <script src="script.js"></script>
</body>
</html>
"""

# INDEX.HTML
index_html = get_header("home") + """
    <!-- Fullscreen Visual Hero -->
    <section class="hero">
        <div class="hero-content">
            <span class="hero-badge"><i class="fa-solid fa-bolt"></i> 24/7 Dispatch • 30 Min Arrival</span>
            <h1>SAME FLAVOURS.<br>SAME VIBE.<br><span>AT YOUR DOOR.</span></h1>
            <p>Ultra-premium hookah pipes, authentic tobacco brands, and glowing charcoal delivered ready-to-smoke across Central London.</p>
            <div class="hero-btns">
                <a href="#builder" class="btn-gold"><i class="fa-solid fa-fire"></i> Build Your Session</a>
                <a href="https://wa.me/447903375779" target="_blank" class="btn-whatsapp"><i class="fa-brands fa-whatsapp"></i> WhatsApp Order (07903375779)</a>
            </div>
        </div>
    </section>

    <!-- Visual Package Showcase (3 Large Photographic Cards) -->
    <section style="padding-top: 80px;">
        <div class="section-header">
            <span class="section-subtitle">Transparent Pricing & Packages</span>
            <h2>Select Your Shisha Experience</h2>
        </div>

        <div class="visual-grid">
            <!-- 1 Shisha -->
            <div class="visual-card">
                <div class="visual-card-img">
                    <img src="https://images.unsplash.com/photo-1527661591475-527312dd65f5?auto=format&fit=crop&w=800&q=80" alt="1 Shisha Package">
                    <span class="visual-badge">Single Set</span>
                </div>
                <div class="visual-card-body">
                    <div>
                        <div class="visual-card-title">1 Shisha Complete Set</div>
                        <div class="visual-card-price">£50</div>
                        <ul style="list-style: none; line-height: 2; color: var(--text-muted); font-size: 0.9rem; margin-bottom: 20px;">
                            <li><i class="fa-solid fa-check" style="color: var(--gold);"></i> 1 Premium Hookah Pipe</li>
                            <li><i class="fa-solid fa-check" style="color: var(--gold);"></i> 1 Fresh Flavour Head of Choice</li>
                            <li><i class="fa-solid fa-check" style="color: var(--gold);"></i> 10 Natural Coconut Coals & Tongs</li>
                            <li><i class="fa-solid fa-check" style="color: var(--gold);"></i> Sealed Hygienic Mouthpieces</li>
                        </ul>
                    </div>
                    <a href="#builder" onclick="selectPkg('1 Shisha Set', 50, document.querySelectorAll('.pkg-card')[0])" class="btn-gold" style="width: 100%; justify-content: center;">Select £50 Package</a>
                </div>
            </div>

            <!-- 2 Shisha -->
            <div class="visual-card" style="border-color: var(--gold);">
                <div class="visual-card-img">
                    <img src="https://images.unsplash.com/photo-1541532713592-79a0317b6b77?auto=format&fit=crop&w=800&q=80" alt="2 Shisha Package">
                    <span class="visual-badge" style="background: var(--gold-gradient); color: #000;">Best Value Bundle</span>
                </div>
                <div class="visual-card-body">
                    <div>
                        <div class="visual-card-title">2 Shisha Complete Set</div>
                        <div class="visual-card-price">£80</div>
                        <ul style="list-style: none; line-height: 2; color: var(--text-muted); font-size: 0.9rem; margin-bottom: 20px;">
                            <li><i class="fa-solid fa-check" style="color: var(--gold);"></i> 2 Premium Hookah Pipes</li>
                            <li><i class="fa-solid fa-check" style="color: var(--gold);"></i> 2 Fresh Flavour Heads of Choice</li>
                            <li><i class="fa-solid fa-check" style="color: var(--gold);"></i> 20 Natural Coconut Coals</li>
                            <li><i class="fa-solid fa-check" style="color: var(--gold);"></i> Electric Coal Burner Included</li>
                        </ul>
                    </div>
                    <a href="#builder" onclick="selectPkg('2 Shisha Set', 80, document.querySelectorAll('.pkg-card')[1])" class="btn-gold" style="width: 100%; justify-content: center;">Select £80 Package</a>
                </div>
            </div>

            <!-- 3 Shisha -->
            <div class="visual-card">
                <div class="visual-card-img">
                    <img src="https://images.unsplash.com/photo-1517457373958-b7bdd4587205?auto=format&fit=crop&w=800&q=80" alt="3 Shisha Package">
                    <span class="visual-badge">VIP Party Set</span>
                </div>
                <div class="visual-card-body">
                    <div>
                        <div class="visual-card-title">3 Shisha Complete Set</div>
                        <div class="visual-card-price">£110</div>
                        <ul style="list-style: none; line-height: 2; color: var(--text-muted); font-size: 0.9rem; margin-bottom: 20px;">
                            <li><i class="fa-solid fa-check" style="color: var(--gold);"></i> 3 Premium Hookah Pipes</li>
                            <li><i class="fa-solid fa-check" style="color: var(--gold);"></i> 3 Fresh Flavour Heads of Choice</li>
                            <li><i class="fa-solid fa-check" style="color: var(--gold);"></i> 30 Natural Coconut Coals</li>
                            <li><i class="fa-solid fa-check" style="color: var(--gold);"></i> Electric Coal Burner Included</li>
                        </ul>
                    </div>
                    <a href="#builder" onclick="selectPkg('3 Shisha Set', 110, document.querySelectorAll('.pkg-card')[2])" class="btn-gold" style="width: 100%; justify-content: center;">Select £110 Package</a>
                </div>
            </div>
        </div>
    </section>

    <!-- Visual Flavour Gallery Grid (8 Photo Cards) -->
    <section style="background: #07090D; padding-top: 80px;">
        <div class="section-header">
            <span class="section-subtitle">Authentic Tobacco Collections</span>
            <h2>Choose Your Signature Flavour</h2>
        </div>

        <div class="flavour-gallery-grid">
            <!-- Double Apple -->
            <div class="flavour-card active" onclick="selectFlavour('Al Fakher Double Apple', this)">
                <img src="https://images.unsplash.com/photo-1560806887-1e4cd0b6cbd6?auto=format&fit=crop&w=600&q=80" class="flavour-card-img" alt="Double Apple">
                <div class="flavour-card-content">
                    <h4>Al Fakher Double Apple</h4>
                    <span>Classic Aniseed & Red Apple</span>
                </div>
            </div>

            <!-- Fresh Mint -->
            <div class="flavour-card" onclick="selectFlavour('Al Fakher Mint', this)">
                <img src="https://images.unsplash.com/photo-1628557044797-f21a177c37ec?auto=format&fit=crop&w=600&q=80" class="flavour-card-img" alt="Fresh Mint">
                <div class="flavour-card-content">
                    <h4>Al Fakher Fresh Mint</h4>
                    <span>Cooling Refreshing Mint</span>
                </div>
            </div>

            <!-- Love 66 -->
            <div class="flavour-card" onclick="selectFlavour('Adalya Love 66', this)">
                <img src="https://images.unsplash.com/photo-1589984662646-e7b2e4962f18?auto=format&fit=crop&w=600&q=80" class="flavour-card-img" alt="Love 66">
                <div class="flavour-card-content">
                    <h4>Adalya Love 66</h4>
                    <span>Watermelon, Melon & Passionfruit</span>
                </div>
            </div>

            <!-- Lady Killer -->
            <div class="flavour-card" onclick="selectFlavour('Adalya Lady Killer', this)">
                <img src="https://images.unsplash.com/photo-1553279768-865429fa0078?auto=format&fit=crop&w=600&q=80" class="flavour-card-img" alt="Lady Killer">
                <div class="flavour-card-content">
                    <h4>Adalya Lady Killer</h4>
                    <span>Mango, Melon, Berry & Mint</span>
                </div>
            </div>

            <!-- Watermelon Mint -->
            <div class="flavour-card" onclick="selectFlavour('Mazaya Watermelon Mint', this)">
                <img src="https://images.unsplash.com/photo-1587049352847-4a222e784d38?auto=format&fit=crop&w=600&q=80" class="flavour-card-img" alt="Watermelon Mint">
                <div class="flavour-card-content">
                    <h4>Mazaya Watermelon</h4>
                    <span>Juicy Sweet Watermelon</span>
                </div>
            </div>

            <!-- Paan Ras -->
            <div class="flavour-card" onclick="selectFlavour('Paan Ras / Paan Mint', this)">
                <img src="https://images.unsplash.com/photo-1615485290382-441e4d049cb5?auto=format&fit=crop&w=600&q=80" class="flavour-card-img" alt="Paan Ras">
                <div class="flavour-card-content">
                    <h4>Paan Ras / Paan Mint</h4>
                    <span>Traditional Spiced Betel Leaf</span>
                </div>
            </div>

            <!-- Starburst -->
            <div class="flavour-card" onclick="selectFlavour('Starburst Sweet Mix', this)">
                <img src="https://images.unsplash.com/photo-1582058091505-f87a2e55a40f?auto=format&fit=crop&w=600&q=80" class="flavour-card-img" alt="Starburst Mix">
                <div class="flavour-card-content">
                    <h4>Starburst Candy Mix</h4>
                    <span>Sweet Fruit Candy Blend</span>
                </div>
            </div>

            <!-- Savaco Luxury -->
            <div class="flavour-card" onclick="selectFlavour('Savaco Luxury (£30/50g)', this)">
                <img src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=600&q=80" class="flavour-card-img" alt="Savaco Luxury">
                <div class="flavour-card-content">
                    <h4>Savaco Luxury Line</h4>
                    <span>Golden Tobacco (£30 / 50g)</span>
                </div>
            </div>
        </div>
    </section>

    <!-- Visual Add-ons Gallery Showcase -->
    <section style="padding-top: 80px;">
        <div class="section-header">
            <span class="section-subtitle">Custom Upgrades</span>
            <h2>Enhance Your Shisha Session</h2>
        </div>

        <div class="visual-grid">
            <div class="visual-card">
                <div class="visual-card-img">
                    <img src="https://images.unsplash.com/photo-1550258987-190a2d41a8ba?auto=format&fit=crop&w=600&q=80" alt="Fruit Head">
                    <span class="visual-badge">+£30 Upgrade</span>
                </div>
                <div class="visual-card-body">
                    <div class="visual-card-title">Fresh Pineapple / Grapefruit Head</div>
                    <p style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 15px;">Carved fresh real fruit bowl for longer session duration and intense tropical aroma.</p>
                </div>
            </div>

            <div class="visual-card">
                <div class="visual-card-img">
                    <img src="https://images.unsplash.com/photo-1508873696983-2df515122519?auto=format&fit=crop&w=600&q=80" alt="Coal Burner">
                    <span class="visual-badge">+£35 Upgrade</span>
                </div>
                <div class="visual-card-body">
                    <div class="visual-card-title">Electric Coal Burner</div>
                    <p style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 15px;">High-speed 1000W electric burner to light your coals indoors within minutes.</p>
                </div>
            </div>

            <div class="visual-card">
                <div class="visual-card-img">
                    <img src="https://images.unsplash.com/photo-1613478223719-2ab802602423?auto=format&fit=crop&w=600&q=80" alt="Juice Base">
                    <span class="visual-badge">+£15 Upgrade</span>
                </div>
                <div class="visual-card-body">
                    <div class="visual-card-title">Chilled Fresh Juice Base</div>
                    <p style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 15px;">Replace vase water with fresh chilled apple, orange, or pineapple juice.</p>
                </div>
            </div>

            <div class="visual-card">
                <div class="visual-card-img">
                    <img src="https://images.unsplash.com/photo-1563245372-f21724e3856d?auto=format&fit=crop&w=600&q=80" alt="LED Light Base">
                    <span class="visual-badge">+£15 Upgrade</span>
                </div>
                <div class="visual-card-body">
                    <div class="visual-card-title">Under-Shisha LED Glow Base</div>
                    <p style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 15px;">Multi-color remote controlled LED glow ring under the glass vase for lounge vibes.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Visual Central London Area Photo Grid -->
    <section style="background: #07090D; padding-top: 80px;">
        <div class="section-header">
            <span class="section-subtitle">24/7 Rapid Delivery Fleet</span>
            <h2>Central London Delivery Coverage</h2>
        </div>

        <div class="area-visual-grid">
            <!-- Westminster -->
            <div class="area-photo-card">
                <img src="https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?auto=format&fit=crop&w=600&q=80" alt="Westminster">
                <div class="area-photo-overlay">
                    <h3>Westminster</h3>
                    <span>20 - 30 Mins Arrival</span>
                </div>
            </div>

            <!-- Knightsbridge -->
            <div class="area-photo-card">
                <img src="https://images.unsplash.com/photo-1526129318478-62ed807ebdf9?auto=format&fit=crop&w=600&q=80" alt="Knightsbridge">
                <div class="area-photo-overlay">
                    <h3>Knightsbridge</h3>
                    <span>20 - 30 Mins Arrival</span>
                </div>
            </div>

            <!-- Chelsea -->
            <div class="area-photo-card">
                <img src="https://images.unsplash.com/photo-1533929736458-ca588d08c8be?auto=format&fit=crop&w=600&q=80" alt="Chelsea">
                <div class="area-photo-overlay">
                    <h3>Chelsea</h3>
                    <span>20 - 35 Mins Arrival</span>
                </div>
            </div>

            <!-- Vauxhall -->
            <div class="area-photo-card">
                <img src="https://images.unsplash.com/photo-1505761671935-60b3a7427bad?auto=format&fit=crop&w=600&q=80" alt="Vauxhall">
                <div class="area-photo-overlay">
                    <h3>Vauxhall</h3>
                    <span>25 - 35 Mins Arrival</span>
                </div>
            </div>

            <!-- Kensington -->
            <div class="area-photo-card">
                <img src="https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=600&q=80" alt="Kensington">
                <div class="area-photo-overlay">
                    <h3>South & High St Kensington</h3>
                    <span>25 - 40 Mins Arrival</span>
                </div>
            </div>

            <!-- Marble Arch -->
            <div class="area-photo-card">
                <img src="https://images.unsplash.com/photo-1543783207-ec64e4d95325?auto=format&fit=crop&w=600&q=80" alt="Baker Street & Marble Arch">
                <div class="area-photo-overlay">
                    <h3>Baker Street & Marble Arch</h3>
                    <span>30 - 40 Mins Arrival</span>
                </div>
            </div>
        </div>
    </section>

    <!-- Interactive Configurator Studio -->
    <section id="builder" class="config-section">
        <div class="section-header">
            <span class="section-subtitle">Interactive Studio</span>
            <h2>Order Your 24/7 Session</h2>
        </div>

        <div class="config-studio">
            <div class="studio-left">
                <!-- Step 1 -->
                <h3 style="color: var(--gold); margin-bottom: 15px;"><i class="fa-solid fa-circle-1"></i> Choose Package</h3>
                <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; margin-bottom: 30px;">
                    <div class="pkg-card" onclick="selectPkg('1 Shisha Set', 50, this)">
                        <strong>1 Shisha</strong>
                        <div style="color: var(--gold); font-weight: 800; font-size: 1.3rem;">£50</div>
                    </div>
                    <div class="pkg-card active" onclick="selectPkg('2 Shisha Set', 80, this)">
                        <strong>2 Shisha</strong>
                        <div style="color: var(--gold); font-weight: 800; font-size: 1.3rem;">£80</div>
                    </div>
                    <div class="pkg-card" onclick="selectPkg('3 Shisha Set', 110, this)">
                        <strong>3 Shisha</strong>
                        <div style="color: var(--gold); font-weight: 800; font-size: 1.3rem;">£110</div>
                    </div>
                </div>

                <!-- Step 2 -->
                <h3 style="color: var(--gold); margin-bottom: 15px;"><i class="fa-solid fa-circle-2"></i> Choose Flavour</h3>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-bottom: 30px;">
                    <div class="flavour-chip active" onclick="selectFlavour('Al Fakher Double Apple', this)">Double Apple</div>
                    <div class="flavour-chip" onclick="selectFlavour('Al Fakher Mint', this)">Fresh Mint</div>
                    <div class="flavour-chip" onclick="selectFlavour('Adalya Love 66', this)">Adalya Love 66</div>
                    <div class="flavour-chip" onclick="selectFlavour('Adalya Lady Killer', this)">Adalya Lady Killer</div>
                    <div class="flavour-chip" onclick="selectFlavour('Mazaya Watermelon', this)">Mazaya Watermelon</div>
                    <div class="flavour-chip" onclick="selectFlavour('Paan Ras / Paan Mint', this)">Paan Ras</div>
                </div>

                <!-- Step 3 -->
                <h3 style="color: var(--gold); margin-bottom: 15px;"><i class="fa-solid fa-circle-3"></i> Add Extras</h3>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
                    <label class="addon-item">
                        <span><input type="checkbox" onchange="toggleAddon('Fruit Head', 30, this)"> Fruit Head</span>
                        <strong style="color: var(--gold);">+£30</strong>
                    </label>
                    <label class="addon-item">
                        <span><input type="checkbox" onchange="toggleAddon('Electric Burner', 35, this)"> Burner</span>
                        <strong style="color: var(--gold);">+£35</strong>
                    </label>
                    <label class="addon-item">
                        <span><input type="checkbox" onchange="toggleAddon('Juice Base', 15, this)"> Juice Base</span>
                        <strong style="color: var(--gold);">+£15</strong>
                    </label>
                    <label class="addon-item">
                        <span><input type="checkbox" onchange="toggleAddon('LED Under-Glow', 15, this)"> LED Light</span>
                        <strong style="color: var(--gold);">+£15</strong>
                    </label>
                </div>
            </div>

            <div class="studio-right">
                <div>
                    <h3 style="color: #FFF; font-size: 1.4rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 15px; margin-bottom: 20px;">
                        <i class="fa-solid fa-receipt" style="color: var(--gold);"></i> Checkout Summary
                    </h3>
                    
                    <div style="display: flex; flex-direction: column; gap: 12px; font-size: 0.95rem; margin-bottom: 25px;">
                        <div style="display: flex; justify-content: space-between; color: var(--text-muted);">
                            <span>Package:</span> <strong id="sum-pkg" style="color: #FFF;">2 Shisha Set (£80)</strong>
                        </div>
                        <div style="display: flex; justify-content: space-between; color: var(--text-muted);">
                            <span>Flavour:</span> <strong id="sum-flavour" style="color: #FFF;">Al Fakher Double Apple</strong>
                        </div>
                        <div style="display: flex; justify-content: space-between; color: var(--text-muted);">
                            <span>Add-ons:</span> <strong id="sum-addons" style="color: #FFF;">None selected</strong>
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
                            <option>Baker Street & Marble Arch (30-40 Mins)</option>
                        </select>
                        <input type="tel" id="cust-phone" placeholder="Your Phone Number" style="width: 100%; padding: 12px; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: 6px; color: #FFF;">
                    </div>
                </div>

                <div>
                    <div style="background: rgba(212, 175, 55, 0.1); border: 1px solid var(--border-gold); padding: 20px; border-radius: 12px; margin-bottom: 20px;">
                        <span style="font-size: 0.8rem; color: var(--text-muted); display: block;">TOTAL ESTIMATED PAYABLE</span>
                        <div style="font-size: 3rem; font-weight: 800; color: var(--gold);" id="grand-total">£80</div>
                    </div>
                    
                    <button class="btn-gold" onclick="sendWhatsAppOrder()" style="width: 100%; justify-content: center; padding: 16px;"><i class="fa-brands fa-whatsapp"></i> Dispatch Order via WhatsApp</button>
                    <p style="font-size: 0.8rem; text-align: center; color: var(--text-muted); margin-top: 10px;">Or Call 24/7 Hotline: <a href="tel:07903375779" style="color: var(--gold); font-weight: bold;">07903375779</a></p>
                </div>
            </div>
        </div>
    </section>
""" + get_footer()

with open(os.path.join(target_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(index_html)

# MENU.HTML (VISUAL GALLERY)
menu_html = get_header("menu") + """
    <section class="hero" style="min-height: 40vh; align-items: center;">
        <div class="hero-content">
            <span class="hero-badge">Curated Authentic Tobacco</span>
            <h1>24/7 Flavour Menu & Add-ons</h1>
            <p>100% authentic tobacco collections delivered with ready-to-smoke setups in Central London.</p>
        </div>
    </section>

    <section style="padding-top: 60px;">
        <div class="flavour-gallery-grid">
            <div class="flavour-card active">
                <img src="https://images.unsplash.com/photo-1560806887-1e4cd0b6cbd6?auto=format&fit=crop&w=600&q=80" class="flavour-card-img" alt="Double Apple">
                <div class="flavour-card-content">
                    <h4>Al Fakher Double Apple</h4>
                    <span>Iconic Classic Blend</span>
                </div>
            </div>

            <div class="flavour-card">
                <img src="https://images.unsplash.com/photo-1628557044797-f21a177c37ec?auto=format&fit=crop&w=600&q=80" class="flavour-card-img" alt="Fresh Mint">
                <div class="flavour-card-content">
                    <h4>Al Fakher Fresh Mint</h4>
                    <span>Pure Crisp Cooling</span>
                </div>
            </div>

            <div class="flavour-card">
                <img src="https://images.unsplash.com/photo-1589984662646-e7b2e4962f18?auto=format&fit=crop&w=600&q=80" class="flavour-card-img" alt="Love 66">
                <div class="flavour-card-content">
                    <h4>Adalya Love 66</h4>
                    <span>Watermelon, Passionfruit & Mint</span>
                </div>
            </div>

            <div class="flavour-card">
                <img src="https://images.unsplash.com/photo-1553279768-865429fa0078?auto=format&fit=crop&w=600&q=80" class="flavour-card-img" alt="Lady Killer">
                <div class="flavour-card-content">
                    <h4>Adalya Lady Killer</h4>
                    <span>Mango, Melon, Berry & Mint</span>
                </div>
            </div>

            <div class="flavour-card">
                <img src="https://images.unsplash.com/photo-1587049352847-4a222e784d38?auto=format&fit=crop&w=600&q=80" class="flavour-card-img" alt="Watermelon Mint">
                <div class="flavour-card-content">
                    <h4>Mazaya Watermelon Mint</h4>
                    <span>Sweet Chilled Watermelon</span>
                </div>
            </div>

            <div class="flavour-card">
                <img src="https://images.unsplash.com/photo-1615485290382-441e4d049cb5?auto=format&fit=crop&w=600&q=80" class="flavour-card-img" alt="Paan Ras">
                <div class="flavour-card-content">
                    <h4>Paan Ras / Paan Mint</h4>
                    <span>Spiced Betel Leaf Specialty</span>
                </div>
            </div>

            <div class="flavour-card">
                <img src="https://images.unsplash.com/photo-1582058091505-f87a2e55a40f?auto=format&fit=crop&w=600&q=80" class="flavour-card-img" alt="Starburst Mix">
                <div class="flavour-card-content">
                    <h4>Starburst Candy Mix</h4>
                    <span>Sweet Gourmet Candy Blend</span>
                </div>
            </div>

            <div class="flavour-card">
                <img src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=600&q=80" class="flavour-card-img" alt="Savaco">
                <div class="flavour-card-content">
                    <h4>Savaco Luxury Line</h4>
                    <span>Golden Tobacco (£30 / 50g)</span>
                </div>
            </div>
        </div>
    </section>
""" + get_footer()

with open(os.path.join(target_dir, "menu.html"), "w", encoding="utf-8") as f:
    f.write(menu_html)

# PACKAGES.HTML (VISUAL CARDS)
packages_html = get_header("packages") + """
    <section class="hero" style="min-height: 40vh; align-items: center;">
        <div class="hero-content">
            <span class="hero-badge">Transparent Pricing</span>
            <h1>24/7 Delivery Packages</h1>
            <p>Ready-to-smoke setups, glowing coals, tongs, and sealed hygienic mouthpieces included.</p>
        </div>
    </section>

    <section style="padding-top: 60px;">
        <div class="visual-grid">
            <div class="visual-card">
                <div class="visual-card-img">
                    <img src="https://images.unsplash.com/photo-1527661591475-527312dd65f5?auto=format&fit=crop&w=800&q=80" alt="1 Shisha">
                    <span class="visual-badge">Single Package</span>
                </div>
                <div class="visual-card-body">
                    <div>
                        <div class="visual-card-title">1 Shisha Complete Set</div>
                        <div class="visual-card-price">£50</div>
                        <ul style="list-style: none; line-height: 2; color: var(--text-muted); font-size: 0.9rem; margin-bottom: 20px;">
                            <li><i class="fa-solid fa-check" style="color: var(--gold);"></i> 1 Premium Hookah Pipe</li>
                            <li><i class="fa-solid fa-check" style="color: var(--gold);"></i> 1 Flavour Head of Choice</li>
                            <li><i class="fa-solid fa-check" style="color: var(--gold);"></i> 10 Coconut Coals & Tongs</li>
                            <li><i class="fa-solid fa-check" style="color: var(--gold);"></i> Sealed Mouthpieces Included</li>
                        </ul>
                    </div>
                    <a href="index.html#builder" class="btn-gold" style="width: 100%; justify-content: center;">Order £50 Package</a>
                </div>
            </div>

            <div class="visual-card" style="border-color: var(--gold);">
                <div class="visual-card-img">
                    <img src="https://images.unsplash.com/photo-1541532713592-79a0317b6b77?auto=format&fit=crop&w=800&q=80" alt="2 Shisha">
                    <span class="visual-badge" style="background: var(--gold-gradient); color: #000;">Best Value</span>
                </div>
                <div class="visual-card-body">
                    <div>
                        <div class="visual-card-title">2 Shisha Complete Set</div>
                        <div class="visual-card-price">£80</div>
                        <ul style="list-style: none; line-height: 2; color: var(--text-muted); font-size: 0.9rem; margin-bottom: 20px;">
                            <li><i class="fa-solid fa-check" style="color: var(--gold);"></i> 2 Premium Hookah Pipes</li>
                            <li><i class="fa-solid fa-check" style="color: var(--gold);"></i> 2 Flavour Heads of Choice</li>
                            <li><i class="fa-solid fa-check" style="color: var(--gold);"></i> 20 Coconut Coals</li>
                            <li><i class="fa-solid fa-check" style="color: var(--gold);"></i> Electric Coal Burner Included</li>
                        </ul>
                    </div>
                    <a href="index.html#builder" class="btn-gold" style="width: 100%; justify-content: center;">Order £80 Package</a>
                </div>
            </div>

            <div class="visual-card">
                <div class="visual-card-img">
                    <img src="https://images.unsplash.com/photo-1517457373958-b7bdd4587205?auto=format&fit=crop&w=800&q=80" alt="3 Shisha">
                    <span class="visual-badge">VIP Group</span>
                </div>
                <div class="visual-card-body">
                    <div>
                        <div class="visual-card-title">3 Shisha Complete Set</div>
                        <div class="visual-card-price">£110</div>
                        <ul style="list-style: none; line-height: 2; color: var(--text-muted); font-size: 0.9rem; margin-bottom: 20px;">
                            <li><i class="fa-solid fa-check" style="color: var(--gold);"></i> 3 Premium Hookah Pipes</li>
                            <li><i class="fa-solid fa-check" style="color: var(--gold);"></i> 3 Flavour Heads of Choice</li>
                            <li><i class="fa-solid fa-check" style="color: var(--gold);"></i> 30 Coconut Coals</li>
                            <li><i class="fa-solid fa-check" style="color: var(--gold);"></i> Electric Coal Burner Included</li>
                        </ul>
                    </div>
                    <a href="index.html#builder" class="btn-gold" style="width: 100%; justify-content: center;">Order £110 Package</a>
                </div>
            </div>
        </div>
    </section>
""" + get_footer()

with open(os.path.join(target_dir, "packages.html"), "w", encoding="utf-8") as f:
    f.write(packages_html)

# AREAS.HTML (VISUAL PHOTO GRID)
areas_html = get_header("areas") + """
    <section class="hero" style="min-height: 40vh; align-items: center;">
        <div class="hero-content">
            <span class="hero-badge">Central London Fleet</span>
            <h1>24/7 Coverage Zones</h1>
            <p>Fast driver dispatch within 20 to 45 minutes across all major Central London locations.</p>
        </div>
    </section>

    <section style="padding-top: 60px;">
        <div class="area-visual-grid">
            <div class="area-photo-card">
                <img src="https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?auto=format&fit=crop&w=600&q=80" alt="Westminster">
                <div class="area-photo-overlay">
                    <h3>Westminster</h3>
                    <span>20 - 30 Mins Arrival</span>
                </div>
            </div>

            <div class="area-photo-card">
                <img src="https://images.unsplash.com/photo-1526129318478-62ed807ebdf9?auto=format&fit=crop&w=600&q=80" alt="Knightsbridge">
                <div class="area-photo-overlay">
                    <h3>Knightsbridge</h3>
                    <span>20 - 30 Mins Arrival</span>
                </div>
            </div>

            <div class="area-photo-card">
                <img src="https://images.unsplash.com/photo-1533929736458-ca588d08c8be?auto=format&fit=crop&w=600&q=80" alt="Chelsea">
                <div class="area-photo-overlay">
                    <h3>Chelsea</h3>
                    <span>20 - 35 Mins Arrival</span>
                </div>
            </div>

            <div class="area-photo-card">
                <img src="https://images.unsplash.com/photo-1505761671935-60b3a7427bad?auto=format&fit=crop&w=600&q=80" alt="Vauxhall">
                <div class="area-photo-overlay">
                    <h3>Vauxhall</h3>
                    <span>25 - 35 Mins Arrival</span>
                </div>
            </div>

            <div class="area-photo-card">
                <img src="https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=600&q=80" alt="Kensington">
                <div class="area-photo-overlay">
                    <h3>South & High St Kensington</h3>
                    <span>25 - 40 Mins Arrival</span>
                </div>
            </div>

            <div class="area-photo-card">
                <img src="https://images.unsplash.com/photo-1543783207-ec64e4d95325?auto=format&fit=crop&w=600&q=80" alt="Marble Arch">
                <div class="area-photo-overlay">
                    <h3>Baker Street & Marble Arch</h3>
                    <span>30 - 40 Mins Arrival</span>
                </div>
            </div>
        </div>
    </section>
""" + get_footer()

with open(os.path.join(target_dir, "areas.html"), "w", encoding="utf-8") as f:
    f.write(areas_html)

# ABOUT.HTML & CONTACT.HTML
about_html = get_header("about") + """
    <section class="hero" style="min-height: 40vh; align-items: center;">
        <div class="hero-content">
            <span class="hero-badge">Lounge Standards Delivered</span>
            <h1>Our 24/7 Quality Promise</h1>
            <p>100% authentic tobacco, sterilised equipment, and instant delivery to residences, hotels, and luxury apartments.</p>
        </div>
    </section>

    <section style="padding: 80px 5%; max-width: 1000px; margin: 0 auto;">
        <div style="background: var(--bg-card); border: 1px solid var(--border-gold); padding: 40px; border-radius: 16px; text-align: center;">
            <i class="fa-solid fa-crown" style="font-size: 3rem; color: var(--gold); margin-bottom: 20px;"></i>
            <h2 style="color: #FFF; margin-bottom: 15px;">24/7 Direct Dispatch Line</h2>
            <p style="font-size: 1.2rem; color: var(--gold); font-weight: bold; margin-bottom: 25px;">Phone / WhatsApp: 07903375779</p>
            <p style="color: var(--text-muted); margin-bottom: 30px;">Email: Mrshawest26@gmail.com</p>
            <a href="index.html#builder" class="btn-gold"><i class="fa-solid fa-fire"></i> Order Your Shisha Now</a>
        </div>
    </section>
""" + get_footer()

with open(os.path.join(target_dir, "about.html"), "w", encoding="utf-8") as f:
    f.write(about_html)

contact_html = get_header("contact") + """
    <section class="hero" style="min-height: 40vh; align-items: center;">
        <div class="hero-content">
            <span class="hero-badge">Instant Hotline</span>
            <h1>Contact 24/7 Dispatch</h1>
            <p>Call or message us directly for immediate Central London shisha delivery.</p>
        </div>
    </section>

    <section style="padding: 80px 5%; max-width: 900px; margin: 0 auto;">
        <div style="background: var(--bg-card); border: 1px solid var(--border-gold); padding: 45px; border-radius: 16px; text-align: center;">
            <i class="fa-brands fa-whatsapp" style="font-size: 3.5rem; color: #25D366; margin-bottom: 20px;"></i>
            <h2 style="color: #FFF; margin-bottom: 10px;">Fastest WhatsApp Dispatch</h2>
            <p style="font-size: 1.3rem; color: var(--gold); font-weight: bold; margin-bottom: 25px;">07903375779</p>
            <a href="https://wa.me/447903375779" target="_blank" class="btn-whatsapp" style="padding: 16px 36px; font-size: 1.1rem;"><i class="fa-brands fa-whatsapp"></i> Chat & Order on WhatsApp</a>
        </div>
    </section>
""" + get_footer()

with open(os.path.join(target_dir, "contact.html"), "w", encoding="utf-8") as f:
    f.write(contact_html)

print("[+] All ultra visual HTML pages generated successfully!")
