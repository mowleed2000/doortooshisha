import os

target_dir = r"C:\Users\fifia\.gemini\antigravity\scratch\shisha-delivery-london"
os.makedirs(target_dir, exist_ok=True)

# 1. REWRITE STYLE.CSS FOR ULTRA VISUAL HIGH-END LOUNGE EXPERIENCE
css_content = """
:root {
    --bg-dark: #050608;
    --bg-card: #0D0F15;
    --bg-card-hover: #141722;
    --gold: #D4AF37;
    --gold-glow: #FFD700;
    --gold-gradient: linear-gradient(135deg, #FFD700 0%, #D4AF37 50%, #997507 100%);
    --neon-accent: #00E5FF;
    --text-white: #FFFFFF;
    --text-muted: #A0AEC0;
    --border-gold: rgba(212, 175, 55, 0.35);
    --shadow-card: 0 15px 35px rgba(0,0,0,0.6);
    --shadow-gold: 0 10px 30px rgba(212, 175, 55, 0.25);
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
    line-height: 1.5;
    overflow-x: hidden;
}

h1, h2, h3, h4 {
    font-family: 'Cinzel', Georgia, serif;
    letter-spacing: 1px;
}

/* Header & Announcement */
.top-announcement {
    background: linear-gradient(90deg, #090B10, #1C160B, #090B10);
    border-bottom: 1px solid var(--border-gold);
    color: var(--gold);
    padding: 10px 5%;
    font-size: 0.85rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-weight: 600;
}

header {
    background: rgba(5, 6, 8, 0.95);
    backdrop-filter: blur(15px);
    position: sticky;
    top: 0;
    z-index: 1000;
    border-bottom: 1px solid rgba(255,255,255,0.08);
}

.nav-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 16px 5%;
}

.logo {
    display: flex;
    align-items: center;
    gap: 12px;
    text-decoration: none;
}

.logo-icon {
    font-size: 2.2rem;
    background: var(--gold-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    filter: drop-shadow(0 0 10px rgba(212,175,55,0.5));
}

.logo-text h1 {
    font-size: 1.4rem;
    font-weight: 800;
    color: #FFF;
    letter-spacing: 2px;
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
    gap: 30px;
}

nav a {
    text-decoration: none;
    color: var(--text-muted);
    font-size: 0.95rem;
    font-weight: 600;
    transition: all 0.3s ease;
}

nav a:hover, nav a.active {
    color: var(--gold);
    text-shadow: 0 0 10px rgba(212,175,55,0.4);
}

.btn-gold {
    background: var(--gold-gradient);
    color: #050608;
    padding: 12px 28px;
    border-radius: 6px;
    font-weight: 800;
    font-size: 0.95rem;
    border: none;
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: 8px;
    text-decoration: none;
    box-shadow: var(--shadow-gold);
    transition: all 0.3s ease;
}

.btn-gold:hover {
    transform: translateY(-3px) scale(1.02);
    box-shadow: 0 12px 30px rgba(212, 175, 55, 0.5);
}

.btn-whatsapp {
    background: #25D366;
    color: #FFF;
    padding: 12px 24px;
    border-radius: 6px;
    font-weight: 800;
    font-size: 0.95rem;
    text-decoration: none;
    display: inline-flex;
    align-items: center;
    gap: 8px;
    box-shadow: 0 6px 20px rgba(37, 211, 102, 0.35);
    transition: all 0.3s ease;
}

.btn-whatsapp:hover {
    background: #1EBE55;
    transform: translateY(-3px);
}

/* Fullscreen Visual Hero */
.hero {
    position: relative;
    min-height: 88vh;
    display: flex;
    align-items: center;
    background: linear-gradient(180deg, rgba(5, 6, 8, 0.4) 0%, rgba(5, 6, 8, 0.95) 100%), url('https://images.unsplash.com/photo-1517457373958-b7bdd4587205?auto=format&fit=crop&w=1920&q=80') center/cover no-repeat;
    padding: 80px 5%;
}

.hero-content {
    max-width: 750px;
    position: relative;
    z-index: 10;
}

.hero-badge {
    background: rgba(212, 175, 55, 0.15);
    border: 1px solid var(--border-gold);
    color: var(--gold-glow);
    padding: 8px 22px;
    border-radius: 30px;
    font-size: 0.85rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 3px;
    display: inline-flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 25px;
    backdrop-filter: blur(10px);
}

.hero h1 {
    font-size: 4.2rem;
    line-height: 1.08;
    margin-bottom: 25px;
    color: #FFFFFF;
    text-shadow: 0 10px 30px rgba(0,0,0,0.8);
}

.hero h1 span {
    background: var(--gold-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero p {
    font-size: 1.25rem;
    color: #E2E8F0;
    margin-bottom: 40px;
    max-width: 620px;
    text-shadow: 0 2px 10px rgba(0,0,0,0.9);
}

.hero-btns {
    display: flex;
    gap: 20px;
    flex-wrap: wrap;
}

/* Section Header */
.section-header {
    text-align: center;
    max-width: 750px;
    margin: 0 auto 50px;
    padding: 0 5%;
}

.section-subtitle {
    color: var(--gold);
    font-size: 0.85rem;
    text-transform: uppercase;
    letter-spacing: 4px;
    font-weight: 800;
    display: block;
    margin-bottom: 10px;
}

.section-header h2 {
    font-size: 3rem;
    color: #FFF;
}

/* VISUAL CARDS GRID */
.visual-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
    gap: 30px;
    padding: 0 5% 80px;
    max-width: 1400px;
    margin: 0 auto;
}

.visual-card {
    background: var(--bg-card);
    border: 1px solid var(--border-gold);
    border-radius: 16px;
    overflow: hidden;
    box-shadow: var(--shadow-card);
    transition: all 0.4s ease;
    position: relative;
    display: flex;
    flex-direction: column;
}

.visual-card:hover {
    transform: translateY(-8px);
    border-color: var(--gold-glow);
    box-shadow: 0 20px 40px rgba(212, 175, 55, 0.25);
}

.visual-card-img {
    height: 240px;
    position: relative;
    overflow: hidden;
}

.visual-card-img img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.6s ease;
}

.visual-card:hover .visual-card-img img {
    transform: scale(1.08);
}

.visual-badge {
    position: absolute;
    top: 15px;
    right: 15px;
    background: rgba(5, 6, 8, 0.85);
    border: 1px solid var(--gold);
    color: var(--gold);
    font-weight: 800;
    font-size: 0.75rem;
    padding: 6px 14px;
    border-radius: 20px;
    text-transform: uppercase;
    backdrop-filter: blur(8px);
}

.visual-card-body {
    padding: 25px;
    flex-grow: 1;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.visual-card-title {
    font-size: 1.4rem;
    color: #FFF;
    margin-bottom: 8px;
}

.visual-card-price {
    font-size: 2.2rem;
    font-weight: 800;
    color: var(--gold);
    margin-bottom: 15px;
}

/* VISUAL FLAVOUR GALLERY */
.flavour-gallery-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 25px;
    padding: 0 5% 80px;
    max-width: 1400px;
    margin: 0 auto;
}

.flavour-card {
    background: var(--bg-card);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 14px;
    overflow: hidden;
    transition: all 0.3s ease;
    cursor: pointer;
    position: relative;
}

.flavour-card:hover, .flavour-card.active {
    border-color: var(--gold);
    transform: translateY(-5px);
    box-shadow: 0 15px 30px rgba(212,175,55,0.2);
}

.flavour-card-img {
    height: 180px;
    width: 100%;
    object-fit: cover;
}

.flavour-card-content {
    padding: 18px;
    text-align: center;
}

.flavour-card-content h4 {
    font-size: 1.15rem;
    color: #FFF;
    margin-bottom: 4px;
}

.flavour-card-content span {
    font-size: 0.8rem;
    color: var(--gold);
    font-weight: 600;
}

/* PHOTO VISUAL AREA GRID */
.area-visual-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 25px;
    padding: 0 5% 80px;
    max-width: 1400px;
    margin: 0 auto;
}

.area-photo-card {
    height: 220px;
    border-radius: 14px;
    overflow: hidden;
    position: relative;
    box-shadow: var(--shadow-card);
    border: 1px solid rgba(255,255,255,0.1);
    transition: all 0.3s ease;
}

.area-photo-card img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.5s ease;
}

.area-photo-card:hover img {
    transform: scale(1.1);
}

.area-photo-overlay {
    position: absolute;
    inset: 0;
    background: linear-gradient(180deg, transparent 30%, rgba(5,6,8,0.95) 100%);
    padding: 20px;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
}

.area-photo-overlay h3 {
    font-size: 1.3rem;
    color: #FFF;
}

.area-photo-overlay span {
    font-size: 0.85rem;
    color: var(--gold);
    font-weight: 700;
}

/* VISUAL CONFIGURATOR STUDIO */
.config-section {
    padding: 80px 5%;
    background: #080A0E;
}

.config-studio {
    max-width: 1300px;
    margin: 0 auto;
    background: var(--bg-card);
    border: 1px solid var(--border-gold);
    border-radius: 20px;
    overflow: hidden;
    display: grid;
    grid-template-columns: 1.2fr 0.8fr;
    box-shadow: 0 30px 70px rgba(0,0,0,0.8);
}

.studio-left {
    padding: 45px;
    border-right: 1px solid rgba(255,255,255,0.08);
}

.studio-right {
    padding: 45px;
    background: #07080B;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

/* Sticky Bottom Order Bar */
.sticky-bar {
    position: fixed;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%);
    background: rgba(13, 15, 21, 0.95);
    backdrop-filter: blur(20px);
    border: 1px solid var(--border-gold);
    border-radius: 50px;
    padding: 12px 35px;
    display: flex;
    align-items: center;
    gap: 30px;
    box-shadow: 0 20px 40px rgba(0,0,0,0.8);
    z-index: 2000;
}

/* Footer */
footer {
    background: #030405;
    border-top: 1px solid rgba(255,255,255,0.08);
    padding: 70px 5% 30px;
    color: var(--text-muted);
}
"""

with open(os.path.join(target_dir, "style.css"), "w", encoding="utf-8") as f:
    f.write(css_content)

print("[+] Wrote ultra visual style.css")
