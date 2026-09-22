/* Shared polished footer — injected on every page */
(function () {
  const path = location.pathname;
  const inBlog = /\/blog\//.test(path);
  const p = inBlog ? "../" : "";
  const wa = "https://wa.me/447903375779";
  const tiktok = "#"; // connect TikTok later

  const html = `
  <div class="container footer-top">
    <div class="footer-brand-block">
      <a class="brand" href="${p}index.html">
        <div class="brand-mark" aria-hidden="true"><i class="fa-solid fa-wind"></i></div>
        <div class="brand-copy">
          <strong>Shisha Delivery</strong>
          <span>Trusted · Central London · 24/7</span>
        </div>
      </a>
      <p class="footer-lead">Premium shisha delivered to your door across Central London. Ready-to-smoke setups, discreet service, card or cash on delivery.</p>
      <div class="footer-contact-row">
        <a href="tel:07903375779"><i class="fa-solid fa-phone"></i> 07903375779</a>
        <a href="mailto:Mrshawest26@gmail.com"><i class="fa-solid fa-envelope"></i> Mrshawest26@gmail.com</a>
      </div>
      <div class="footer-social">
        <a href="${wa}" target="_blank" rel="noopener noreferrer" aria-label="WhatsApp"><i class="fa-brands fa-whatsapp"></i></a>
        <a href="${tiktok}" aria-label="TikTok"><i class="fa-brands fa-tiktok"></i></a>
      </div>
      <div class="pay-accept footer-pay">
        <span>We accept</span>
        <i class="fa-brands fa-cc-visa" title="Visa"></i>
        <i class="fa-brands fa-cc-mastercard" title="Mastercard"></i>
        <span class="cash-pill">Cash</span>
      </div>
      <a class="btn btn-gold footer-order-btn" href="${p}order.html">Order your shisha</a>
    </div>
    <div class="footer-cols">
      <div>
        <h4>Shop</h4>
        <ul>
          <li><a href="${p}order.html">Order online</a></li>
          <li><a href="${p}packages.html">Packages</a></li>
          <li><a href="${p}menu.html">Flavours</a></li>
          <li><a href="${p}areas.html">Delivery areas</a></li>
        </ul>
      </div>
      <div>
        <h4>Company</h4>
        <ul>
          <li><a href="${p}about.html">About</a></li>
          <li><a href="${p}blog.html">Blog</a></li>
          <li><a href="${p}contact.html">Contact</a></li>
        </ul>
      </div>
      <div>
        <h4>Trust &amp; safety</h4>
        <ul>
          <li>Photo ID checked on delivery</li>
          <li>Discreet professional service</li>
          <li>Card &amp; cash accepted</li>
          <li><span class="age-badge age-badge--sm">18+</span> Adults only</li>
        </ul>
      </div>
    </div>
  </div>
  <div class="container footer-bottom">
    <span class="age-badge">18+</span>
    <span>© ${new Date().getFullYear()} Shisha Delivery. Central London. Smoke responsibly.</span>
    <span class="age-note">Valid photo ID required on delivery</span>
  </div>`;

  function mount() {
    document.querySelectorAll("footer.site-footer").forEach((el) => {
      el.innerHTML = html;
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", mount);
  } else {
    mount();
  }
})();
