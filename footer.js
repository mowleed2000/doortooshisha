/* Shared polished footer — injected on every page */
(function () {
  const path = location.pathname;
  const inBlog = /\/blog\//.test(path);
  const p = inBlog ? "../" : "";

  const html = `
  <div class="container footer-top">
    <div class="footer-brand-block">
      <a class="brand" href="${p}index.html">
        <div class="brand-mark" aria-hidden="true"><i class="fa-solid fa-wind"></i></div>
        <div class="brand-copy">
          <strong>Shisha Delivery</strong>
          <span>Central London · 24/7</span>
        </div>
      </a>
      <p class="footer-lead">Premium flavours delivered to your door — ready-to-smoke setups across Central London. Order online. Pay by card or cash.</p>
      <div class="footer-contact-row">
        <a href="tel:07903375779"><i class="fa-solid fa-phone"></i> 07903375779</a>
        <a href="mailto:Mrshawest26@gmail.com"><i class="fa-solid fa-envelope"></i> Mrshawest26@gmail.com</a>
      </div>
      <a class="btn btn-gold footer-order-btn" href="${p}order.html">Order your shisha</a>
    </div>
    <div class="footer-cols">
      <div>
        <h4>Menu</h4>
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
        <h4>Service</h4>
        <ul>
          <li>24 hour delivery</li>
          <li>Card &amp; cash</li>
          <li>Discreet drop-off</li>
          <li class="age-note">Strictly 18+</li>
        </ul>
      </div>
    </div>
  </div>
  <div class="container footer-bottom">
    <span>© ${new Date().getFullYear()} Shisha Delivery. Central London.</span>
    <span class="age-note">Smoke responsibly · Adults only</span>
  </div>`;

  function mount() {
    const footers = document.querySelectorAll("footer.site-footer");
    footers.forEach((el) => {
      el.innerHTML = html;
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", mount);
  } else {
    mount();
  }
})();
