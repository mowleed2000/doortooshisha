/* SHISHA DELIVERY — site behaviour & checkout */

const STRIPE_PAYMENT_LINKS = {
  "1 Shisha": "",
  "2 Shisha": "",
  "3 Shisha": "",
};

/** Flip to true + fill STRIPE_PAYMENT_LINKS when card checkout goes live */
const CARD_PAYMENTS_ENABLED = false;

const WHATSAPP_NUMBER = "447903375779";

const MENU = {
  packages: [
    {
      id: "1",
      name: "1 Shisha",
      price: 50,
      blurb: "Ideal for one person — pipe, fresh head, coals and mouthpiece.",
      includes: [
        "1 premium hookah pipe",
        "1 fresh flavour head",
        "10 natural coconut coals",
        "Sealed hygienic mouthpiece",
      ],
    },
    {
      id: "2",
      name: "2 Shisha",
      price: 80,
      popular: true,
      blurb: "Our most popular choice for couples and shared nights in.",
      includes: [
        "2 premium hookah pipes",
        "2 fresh flavour heads",
        "20 natural coconut coals",
        "Electric coal burner included",
      ],
    },
    {
      id: "3",
      name: "3 Shisha",
      price: 110,
      blurb: "Built for flats, hotel suites and small gatherings.",
      includes: [
        "3 premium hookah pipes",
        "3 fresh flavour heads",
        "30 natural coconut coals",
        "Electric coal burner included",
      ],
    },
  ],
  flavours: [
    { name: "Starburst", note: "Fruit-candy mix" },
    { name: "Al Fakher", note: "Classic premium blends" },
    { name: "Mazaya", note: "Watermelon & mint" },
    { name: "Adalya", note: "Premium hookah tobacco" },
    { name: "Layali", note: "Berry-forward" },
    { name: "Paan", note: "Traditional leaf notes" },
  ],
  addons: [
    { name: "Extra Head", price: 30 },
    { name: "Extra 10 Coals", price: 5 },
    { name: "Extra Coal Burner", price: 35 },
    { name: "Extra Flavour (50g)", price: 10 },
    { name: "Savaco Tobacco 50g", price: 30 },
    { name: "Liquid Base (juice)", price: 15 },
    { name: "Light Under The Shisha", price: 15 },
  ],
  areas: [
    "Westminster",
    "Knightsbridge",
    "Chelsea",
    "Vauxhall",
    "South Kensington",
    "High Street Kensington",
    "Baker Street",
    "Marble Arch",
  ],
};

const state = {
  package: null,
  flavour: MENU.flavours[0].name,
  addons: [],
  payment: "cash", // card UI hidden until Stripe links are live; keep STRIPE_PAYMENT_LINKS ready
};

function $(sel, root = document) {
  return root.querySelector(sel);
}

function $all(sel, root = document) {
  return [...root.querySelectorAll(sel)];
}

function money(n) {
  return "£" + n;
}

function cartTotal() {
  if (!state.package) return 0;
  return state.package.price + state.addons.reduce((s, a) => s + a.price, 0);
}

function showToast(title, body) {
  let toast = $("#site-toast");
  if (!toast) {
    toast = document.createElement("div");
    toast.id = "site-toast";
    toast.className = "toast";
    document.body.appendChild(toast);
  }
  toast.innerHTML = `<strong>${title}</strong><div>${body}</div>`;
  toast.classList.add("show");
  clearTimeout(showToast._t);
  showToast._t = setTimeout(() => toast.classList.remove("show"), 5200);
}

/* ——— NAV ——— */
function initNav() {
  const header = $(".site-header");
  const toggle = $(".nav-toggle");
  const bar = $(".nav-bar");
  if (!toggle || !header || !bar) return;

  if (!$(".nav-drawer", header)) {
    const links = $(".nav-links", header);
    const cta = $(".nav-cta", header);
    if (links && cta) {
      const drawer = document.createElement("div");
      drawer.className = "nav-drawer";
      drawer.appendChild(links.cloneNode(true));
      const ctaClone = cta.cloneNode(true);
      $all(".nav-phone", ctaClone).forEach((el) => el.remove());
      drawer.appendChild(ctaClone);
      bar.appendChild(drawer);
    }
  }

  const close = () => {
    header.classList.remove("is-open");
    toggle.setAttribute("aria-expanded", "false");
    document.body.classList.remove("nav-open");
  };

  toggle.addEventListener("click", () => {
    const open = header.classList.toggle("is-open");
    toggle.setAttribute("aria-expanded", open ? "true" : "false");
    document.body.classList.toggle("nav-open", open);
  });

  $all(".nav-links a, .nav-drawer a", header).forEach((a) => {
    a.addEventListener("click", close);
  });
}

function initReveal() {
  const els = $all(".reveal");
  if (!els.length || !("IntersectionObserver" in window)) {
    els.forEach((el) => el.classList.add("in"));
    return;
  }
  const io = new IntersectionObserver(
    (entries) => {
      entries.forEach((e) => {
        if (e.isIntersecting) {
          e.target.classList.add("in");
          io.unobserve(e.target);
        }
      });
    },
    { threshold: 0.12, rootMargin: "0px 0px -40px 0px" }
  );
  els.forEach((el) => io.observe(el));
}

/* ——— FLOATING WHATSAPP + CHROME ——— */
function initSiteChrome() {
  if (!$(".wa-float")) {
    const wa = document.createElement("a");
    wa.className = "wa-float";
    wa.href = `https://wa.me/${WHATSAPP_NUMBER}`;
    wa.target = "_blank";
    wa.rel = "noopener noreferrer";
    wa.setAttribute("aria-label", "Message us on WhatsApp");
    wa.innerHTML = '<span class="icon icon-whatsapp" aria-hidden="true"></span>';
    document.body.appendChild(wa);
  }

  // Ensure age badges exist in footers after footer.js mounts
  setTimeout(() => {
    $all(".site-footer .footer-bottom").forEach((el) => {
      if (!el.querySelector(".age-badge")) {
        const badge = document.createElement("span");
        badge.className = "age-badge";
        badge.textContent = "18+";
        el.prepend(badge);
      }
    });
  }, 50);
}

/* ——— HERO VIDEO (deferred load — do not compete with LCP) ——— */
function initHeroVideo() {
  const video = document.getElementById("hero-video");
  const fallback = document.getElementById("hero-fallback");
  const playBtn = document.getElementById("hero-play-btn");
  if (!video) return;

  const resolveSrc = () => {
    if (location.hostname.includes("github.io")) {
      const parts = location.pathname.split("/").filter(Boolean);
      const root = parts.length ? `/${parts[0]}/` : "/";
      return `${root}assets/videos/hero_video_web.mp4`;
    }
    return "assets/videos/hero_video_web.mp4";
  };

  video.muted = true;
  video.defaultMuted = true;
  video.playsInline = true;
  video.loop = true;
  video.setAttribute("muted", "");
  video.setAttribute("playsinline", "");

  const showPlayBtn = () => playBtn && playBtn.classList.add("is-visible");
  const hidePlayBtn = () => playBtn && playBtn.classList.remove("is-visible");
  let loaded = false;

  const loadAndPlay = () => {
    if (!loaded) {
      loaded = true;
      video.src = resolveSrc();
      video.load();
    }
    video.muted = true;
    const p = video.play();
    if (p && typeof p.then === "function") {
      p.then(() => {
        hidePlayBtn();
        if (video.parentElement) video.parentElement.classList.add("is-playing");
        if (fallback) fallback.hidden = true;
      }).catch(showPlayBtn);
    }
  };

  video.addEventListener("playing", () => {
    hidePlayBtn();
    if (video.parentElement) video.parentElement.classList.add("is-playing");
    if (fallback) fallback.hidden = true;
  });
  video.addEventListener("error", showPlayBtn);

  if (playBtn) {
    playBtn.addEventListener("click", (e) => {
      e.preventDefault();
      loadAndPlay();
    });
  }

  const start = () => {
    if (window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
      showPlayBtn();
      return;
    }
    loadAndPlay();
  };

  // Always wait past first paint — idle alone can fire too early in some browsers
  setTimeout(() => {
    if ("requestIdleCallback" in window) {
      requestIdleCallback(start, { timeout: 800 });
    } else {
      start();
    }
  }, 900);
}

/* ——— E-COMMERCE SHOP + CHECKOUT DRAWER ——— */
function syncCheckoutUI() {
  const pkg = state.package;
  const tot = cartTotal();

  $all("[data-cart-total]").forEach((el) => {
    el.textContent = money(tot);
  });
  $all("[data-cart-package]").forEach((el) => {
    el.textContent = pkg ? `${pkg.name} (${money(pkg.price)})` : "—";
  });
  $all("[data-cart-flavour]").forEach((el) => {
    el.textContent = state.flavour;
  });
  $all("[data-cart-addons]").forEach((el) => {
    el.textContent = state.addons.length
      ? state.addons.map((a) => `${a.name} (+${money(a.price)})`).join(", ")
      : "None";
  });

  const bar = $("#cart-bar");
  if (bar) bar.classList.toggle("is-visible", !!pkg);

  const payBtn = $("#place-order-btn");
  if (payBtn) {
    payBtn.textContent =
      state.payment === "card" ? "Pay by card" : "Place cash order";
  }
}

function openCheckout(pkg) {
  if (pkg) state.package = pkg;
  if (!state.package) state.package = MENU.packages[0];

  const drawer = $("#checkout-drawer");
  const backdrop = $("#checkout-backdrop");
  if (drawer) {
    drawer.classList.add("is-open");
    drawer.setAttribute("aria-hidden", "false");
  }
  if (backdrop) backdrop.classList.add("is-open");
  document.body.classList.add("checkout-open");

  $all(".product-card").forEach((card) => {
    card.classList.toggle("is-selected", card.dataset.pkg === state.package.id);
  });

  syncCheckoutUI();
}

function closeCheckout() {
  const drawer = $("#checkout-drawer");
  if (drawer) {
    drawer.classList.remove("is-open");
    drawer.setAttribute("aria-hidden", "true");
  }
  $("#checkout-backdrop")?.classList.remove("is-open");
  document.body.classList.remove("checkout-open");
}

function buildShop() {
  const grid = $("#product-grid");
  if (!grid) return;

  grid.innerHTML = MENU.packages
    .map((pkg) => {
      const img = `assets/images/shisha/packages/P0${pkg.id}.webp`;
      return `
      <article class="product-card" data-pkg="${pkg.id}">
        ${pkg.popular ? '<span class="pkg-badge">Most popular</span>' : ""}
        <div class="product-card-media">
          <img src="${img}" alt="${pkg.name}" loading="lazy" width="640" height="480">
        </div>
        <div class="product-card-body">
          <h3>${pkg.name}</h3>
          <p class="product-blurb">${pkg.blurb}</p>
          <ul>${pkg.includes.map((x) => `<li>${x}</li>`).join("")}</ul>
          <div class="product-card-foot">
            <div class="price">${money(pkg.price)}</div>
            <button type="button" class="btn btn-gold" data-order-pkg="${pkg.id}">Order</button>
          </div>
        </div>
      </article>`;
    })
    .join("");

  grid.addEventListener("click", (e) => {
    const btn = e.target.closest("[data-order-pkg]");
    const card = e.target.closest(".product-card");
    const id = btn?.dataset.orderPkg || card?.dataset.pkg;
    if (!id) return;
    const pkg = MENU.packages.find((p) => p.id === id);
    if (pkg) openCheckout(pkg);
  });
}

function buildCheckoutDrawer() {
  const chips = $("#flavour-chips");
  if (chips) {
    chips.innerHTML = MENU.flavours
      .map(
        (f, i) =>
          `<button type="button" class="chip${i === 0 ? " is-active" : ""}" data-flavour="${f.name}">${f.name}</button>`
      )
      .join("");
    chips.addEventListener("click", (e) => {
      const btn = e.target.closest("[data-flavour]");
      if (!btn) return;
      state.flavour = btn.dataset.flavour;
      $all(".chip", chips).forEach((c) =>
        c.classList.toggle("is-active", c.dataset.flavour === state.flavour)
      );
      syncCheckoutUI();
    });
  }

  const addons = $("#addon-checks");
  if (addons) {
    addons.innerHTML = MENU.addons
      .map(
        (a) => `
      <label class="addon-row">
        <input type="checkbox" data-addon="${a.name}" data-price="${a.price}">
        <span>${a.name}</span>
        <em>+${money(a.price)}</em>
      </label>`
      )
      .join("");
    addons.addEventListener("change", (e) => {
      const input = e.target;
      if (!input.matches("[data-addon]")) return;
      const item = { name: input.dataset.addon, price: Number(input.dataset.price) };
      if (input.checked) {
        if (!state.addons.find((a) => a.name === item.name)) state.addons.push(item);
      } else {
        state.addons = state.addons.filter((a) => a.name !== item.name);
      }
      syncCheckoutUI();
    });
  }

  const area = $("#order-area");
  if (area) {
    area.innerHTML = MENU.areas
      .map((a) => `<option value="${a}">${a}</option>`)
      .join("");
  }

  $all('input[name="payment"]').forEach((input) => {
    input.addEventListener("change", () => {
      if (!CARD_PAYMENTS_ENABLED && input.value === "card") {
        input.checked = false;
        const cash = $('input[name="payment"][value="cash"]');
        if (cash) cash.checked = true;
        state.payment = "cash";
      } else {
        state.payment = input.value;
      }
      $all(".pay-option").forEach((el) => el.classList.remove("is-active"));
      $('input[name="payment"]:checked')?.closest(".pay-option")?.classList.add("is-active");
      syncCheckoutUI();
    });
  });

  // Ensure cash-only UI while card is offline
  if (!CARD_PAYMENTS_ENABLED) {
    state.payment = "cash";
    $all(".pay-option--card").forEach((el) => {
      el.hidden = true;
      el.setAttribute("aria-hidden", "true");
      const input = $("input", el);
      if (input) {
        input.disabled = true;
        input.checked = false;
      }
    });
    const cash = $('input[name="payment"][value="cash"]');
    if (cash) {
      cash.checked = true;
      cash.closest(".pay-option")?.classList.add("is-active");
    }
  } else {
    $all(".pay-option--card").forEach((el) => {
      el.hidden = false;
      el.removeAttribute("aria-hidden");
      const input = $("input", el);
      if (input) input.disabled = false;
    });
  }

  $("#checkout-close")?.addEventListener("click", closeCheckout);
  $("#checkout-backdrop")?.addEventListener("click", closeCheckout);
  $("#cart-bar-checkout")?.addEventListener("click", () => openCheckout());

  const form = $("#order-form");
  if (form) {
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      placeOrder(new FormData(form));
    });
  }

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") closeCheckout();
  });
}

function placeOrder(fd) {
  if (!state.package) {
    showToast("Choose a package", "Select a shisha package to continue.");
    return;
  }

  const name = (fd.get("name") || "").toString().trim();
  const phone = (fd.get("phone") || "").toString().trim();
  const area = (fd.get("area") || "").toString();
  const address = (fd.get("address") || "").toString().trim();
  const notes = (fd.get("notes") || "").toString().trim();
  const ageOk = fd.get("ageConfirm");

  if (!name || !phone || !address) {
    showToast("Missing details", "Please add your name, phone and delivery address.");
    return;
  }
  if (!ageOk) {
    showToast("Age confirmation needed", "You must confirm you are 18+ to order.");
    return;
  }

  const order = {
    name,
    phone,
    area,
    address,
    notes,
    package: state.package.name,
    packagePrice: state.package.price,
    flavour: state.flavour,
    addons: state.addons,
    payment: state.payment,
    total: cartTotal(),
    createdAt: new Date().toISOString(),
  };

  try {
    const prev = JSON.parse(localStorage.getItem("shishaOrders") || "[]");
    prev.unshift(order);
    localStorage.setItem("shishaOrders", JSON.stringify(prev.slice(0, 40)));
  } catch (_) {}

  if (state.payment === "card" && CARD_PAYMENTS_ENABLED) {
    // Card path kept for Stripe Payment Links — fill STRIPE_PAYMENT_LINKS when ready
    const link = STRIPE_PAYMENT_LINKS[state.package.name];
    if (link) {
      showToast("Opening secure payment", `Order saved for ${name}.`);
      setTimeout(() => {
        window.location.href = link;
      }, 600);
      return;
    }
    showToast(
      "Card payment",
      `Thanks ${name}. Your ${money(order.total)} order is saved. Call 07903375779 to complete card payment, or choose cash on delivery.`
    );
    return;
  }

  // Force cash path while card is offline
  order.payment = "cash";
  state.payment = "cash";

  showToast(
    "Opening WhatsApp",
    `Thanks ${name}. Send the order message to confirm — pay ${money(order.total)} cash on delivery.`
  );
  closeCheckout();

  // Prefill WhatsApp to the business number with full order details
  const addonLine = order.addons.length
    ? order.addons.map((a) => `${a.name} (+${money(a.price)})`).join(", ")
    : "None";
  const waText = [
    `New shisha order — Door To Door`,
    ``,
    `Name: ${name}`,
    `Phone: ${phone}`,
    `Area: ${area}`,
    `Address: ${address}`,
    `Package: ${order.package} (${money(order.packagePrice)})`,
    `Flavour: ${order.flavour}`,
    `Extras: ${addonLine}`,
    `Payment: Cash on delivery`,
    `Total: ${money(order.total)}`,
    notes ? `Notes: ${notes}` : null,
    ``,
    `18+ confirmed · please reply to confirm dispatch`,
  ]
    .filter((line) => line !== null)
    .join("\n");

  const waUrl = `https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent(waText)}`;
  setTimeout(() => {
    window.open(waUrl, "_blank", "noopener,noreferrer");
  }, 350);
}

function startOrder(pkgName) {
  const pkg = MENU.packages.find((p) => p.name === pkgName) || MENU.packages[0];
  try {
    sessionStorage.setItem("preselectPackage", pkg.name);
  } catch (_) {}
  window.location.href = "order.html";
}

function applyPreselect() {
  try {
    const name = sessionStorage.getItem("preselectPackage");
    if (!name) return;
    sessionStorage.removeItem("preselectPackage");
    const pkg = MENU.packages.find((p) => p.name === name);
    if (pkg) setTimeout(() => openCheckout(pkg), 200);
  } catch (_) {}
}

document.addEventListener("DOMContentLoaded", () => {
  initNav();
  initReveal();
  initSiteChrome();
  initHeroVideo();
  buildShop();
  buildCheckoutDrawer();
  applyPreselect();
  syncCheckoutUI();
});

window.startOrder = startOrder;
window.MENU = MENU;
window.openCheckout = openCheckout;
