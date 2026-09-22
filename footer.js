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
        <div class="brand-mark" aria-hidden="true"><span class="icon icon-wind"></span></div>
        <div class="brand-copy">
          <strong>Door To Door</strong>
          <span>Shisha Delivery · Central London</span>
        </div>
      </a>
      <p class="footer-lead">Premium shisha delivered to your door across Central London. Ready-to-smoke setups, discreet service, card or cash on delivery.</p>
      <div class="footer-contact-row">
        <a href="tel:07903375779"><span class="icon icon-phone" aria-hidden="true"></span> 07903375779</a>
        <a href="mailto:Mrshawest26@gmail.com"><span class="icon icon-mail" aria-hidden="true"></span> Mrshawest26@gmail.com</a>
      </div>
      <div class="footer-social">
        <a href="${wa}" target="_blank" rel="noopener noreferrer" aria-label="WhatsApp"><span class="icon icon-whatsapp"></span></a>
        <a href="${tiktok}" aria-label="TikTok"><span class="icon icon-tiktok"></span></a>
      </div>
      <div class="pay-accept footer-pay">
        <span>We accept</span>
        <span class="icon icon-visa" title="Visa" aria-label="Visa"></span>
        <span class="icon icon-mc" title="Mastercard" aria-label="Mastercard"></span>
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
    <span>© ${new Date().getFullYear()} Door To Door Shisha Delivery. Smoke responsibly.</span>
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
