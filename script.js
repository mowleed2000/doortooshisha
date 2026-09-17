/* SHISHA DELIVERY — site behaviour & checkout */

const STRIPE_PAYMENT_LINKS = {
  // Replace these with live Stripe Payment Links when ready
  "1 Shisha": "",
  "2 Shisha": "",
  "3 Shisha": "",
};

const MENU = {
  packages: [
    {
      id: "1",
      name: "1 Shisha",
      price: 50,
      blurb: "Solo session — pipe, head, coals & mouthpiece.",
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
      blurb: "Best for couples or a shared lounge night.",
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
      blurb: "Group setup for flats, suites & private gatherings.",
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
  package: MENU.packages[0],
  flavour: MENU.flavours[0].name,
  addons: [],
  payment: "card",
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

function total() {
  const add = state.addons.reduce((s, a) => s + a.price, 0);
  return state.package.price + add;
}

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
  };

  toggle.addEventListener("click", () => {
    const open = header.classList.toggle("is-open");
    toggle.setAttribute("aria-expanded", open ? "true" : "false");
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

function syncSummary() {
  const pkg = $("#summary-package");
  const flav = $("#summary-flavour");
  const adds = $("#summary-addons");
  const tot = $("#summary-total");
  if (pkg) pkg.textContent = `${state.package.name} (${money(state.package.price)})`;
  if (flav) flav.textContent = state.flavour;
  if (adds) {
    adds.textContent = state.addons.length
      ? state.addons.map((a) => `${a.name} (+${money(a.price)})`).join(", ")
      : "None";
  }
  if (tot) tot.textContent = money(total());
}

function selectPackage(pkg, row) {
  state.package = pkg;
  $all(".pkg-row").forEach((el) => el.classList.remove("is-selected"));
  if (row) row.classList.add("is-selected");
  syncSummary();
}

function selectFlavour(name) {
  state.flavour = name;
  $all(".chip").forEach((c) => {
    c.classList.toggle("is-active", c.dataset.flavour === name);
  });
  syncSummary();
}

function toggleAddon(addon, checked) {
  if (checked) {
    if (!state.addons.find((a) => a.name === addon.name)) {
      state.addons.push(addon);
    }
  } else {
    state.addons = state.addons.filter((a) => a.name !== addon.name);
  }
  syncSummary();
}

function buildOrderPage() {
  const list = $("#package-list");
  if (!list) return;

  list.innerHTML = MENU.packages
    .map((pkg, i) => {
      const img = `assets/images/shisha/packages/P0${pkg.id}.png`;
      return `
      <article class="pkg-row${i === 0 ? " is-selected" : ""}" data-pkg="${pkg.id}" role="button" tabindex="0">
        <img src="${img}" alt="${pkg.name} package">
        <div>
          ${pkg.popular ? '<span class="pkg-badge">Most ordered</span>' : ""}
          <h3>${pkg.name}</h3>
          <p style="color:var(--cream-mute);font-size:0.92rem;margin-bottom:0.35rem;">${pkg.blurb}</p>
          <ul>${pkg.includes.map((x) => `<li>${x}</li>`).join("")}</ul>
        </div>
        <div class="pkg-cta">
          <div class="price">${money(pkg.price)}</div>
          <button type="button" class="btn btn-soft" style="margin-top:0.75rem;" data-select-pkg="${pkg.id}">Select</button>
        </div>
      </article>`;
    })
    .join("");

  list.addEventListener("click", (e) => {
    const btn = e.target.closest("[data-select-pkg]");
    const row = e.target.closest(".pkg-row");
    const id = btn?.dataset.selectPkg || row?.dataset.pkg;
    if (!id) return;
    e.preventDefault();
    const pkg = MENU.packages.find((p) => p.id === id);
    const targetRow = $(`.pkg-row[data-pkg="${id}"]`, list);
    if (pkg) selectPackage(pkg, targetRow);
  });

  list.addEventListener("keydown", (e) => {
    if (e.key !== "Enter" && e.key !== " ") return;
    const row = e.target.closest(".pkg-row");
    if (!row) return;
    e.preventDefault();
    const pkg = MENU.packages.find((p) => p.id === row.dataset.pkg);
    if (pkg) selectPackage(pkg, row);
  });

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
      if (btn) selectFlavour(btn.dataset.flavour);
    });
  }

  const addons = $("#addon-checks");
  if (addons) {
    addons.innerHTML = MENU.addons
      .map(
        (a) => `
      <label>
        <input type="checkbox" data-addon="${a.name}" data-price="${a.price}">
        <span>${a.name} <em style="color:var(--gold);font-style:normal;">(+${money(a.price)})</em></span>
      </label>`
      )
      .join("");
    addons.addEventListener("change", (e) => {
      const input = e.target;
      if (!input.matches("[data-addon]")) return;
      toggleAddon(
        { name: input.dataset.addon, price: Number(input.dataset.price) },
        input.checked
      );
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
      state.payment = input.value;
      $all(".pay-option").forEach((el) => el.classList.remove("is-active"));
      input.closest(".pay-option")?.classList.add("is-active");
      const btn = $("#place-order-btn");
      if (btn) {
        btn.textContent =
          state.payment === "card" ? "Pay by card" : "Place cash order";
      }
    });
  });

  const form = $("#order-form");
  if (form) {
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      placeOrder(new FormData(form));
    });
  }

  syncSummary();
}

function placeOrder(fd) {
  const name = (fd.get("name") || "").toString().trim();
  const phone = (fd.get("phone") || "").toString().trim();
  const area = (fd.get("area") || "").toString();
  const address = (fd.get("address") || "").toString().trim();
  const notes = (fd.get("notes") || "").toString().trim();

  if (!name || !phone || !address) {
    showToast("Missing details", "Please add your name, phone and delivery address.");
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
    total: total(),
    createdAt: new Date().toISOString(),
  };

  try {
    const prev = JSON.parse(localStorage.getItem("shishaOrders") || "[]");
    prev.unshift(order);
    localStorage.setItem("shishaOrders", JSON.stringify(prev.slice(0, 40)));
  } catch (_) {
    /* ignore storage errors */
  }

  if (state.payment === "card") {
    const link = STRIPE_PAYMENT_LINKS[state.package.name];
    if (link) {
      showToast(
        "Redirecting to card payment",
        `Order saved for ${name}. Opening secure Stripe checkout…`
      );
      setTimeout(() => {
        window.location.href = link;
      }, 700);
      return;
    }
    showToast(
      "Card payment ready to connect",
      `Order for ${money(order.total)} saved. Add your Stripe Payment Link in script.js — for now call 07903375779 to take card payment.`
    );
    return;
  }

  showToast(
    "Cash order placed",
    `Thanks ${name}. Pay ${money(order.total)} in cash on delivery to ${area}. We'll confirm on ${phone}.`
  );
  const form = $("#order-form");
  if (form) form.reset();
  state.addons = [];
  $all("#addon-checks input").forEach((i) => (i.checked = false));
  selectPackage(MENU.packages[0], $(".pkg-row"));
  selectFlavour(MENU.flavours[0].name);
  state.payment = "cash";
  const cash = $('#payment-cash');
  if (cash) cash.checked = true;
  $all(".pay-option").forEach((el) => el.classList.remove("is-active"));
  cash?.closest(".pay-option")?.classList.add("is-active");
  const btn = $("#place-order-btn");
  if (btn) btn.textContent = "Place cash order";
  syncSummary();
}

/** Quick-add from other pages */
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
    if (!pkg) return;
    const row = $(`.pkg-row[data-pkg="${pkg.id}"]`);
    selectPackage(pkg, row);
  } catch (_) {}
}

document.addEventListener("DOMContentLoaded", () => {
  initNav();
  initReveal();
  buildOrderPage();
  applyPreselect();
});

window.startOrder = startOrder;
window.MENU = MENU;
