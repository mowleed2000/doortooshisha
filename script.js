
let selectedPackage = { name: "PRIVATE SESSION", price: 50 };
let selectedFlavour = "Al Fakher Double Apple";
let selectedAddons = [];

function openOrderModal(pkgName, pkgPrice) {
    if (pkgName && pkgPrice) {
        selectedPackage = { name: pkgName, price: pkgPrice };
    }
    updateOrderSummary();
    document.getElementById('orderModal').style.display = 'flex';
}

function closeOrderModal() {
    document.getElementById('orderModal').style.display = 'none';
}

function selectFlavour(name) {
    selectedFlavour = name;
    updateOrderSummary();
}

function toggleUpgrade(name, price, checkbox) {
    if (checkbox.checked) {
        selectedAddons.push({ name: name, price: price });
    } else {
        selectedAddons = selectedAddons.filter(a => a.name !== name);
    }
    updateOrderSummary();
}

function updateOrderSummary() {
    let addonSum = selectedAddons.reduce((sum, a) => sum + a.price, 0);
    let total = selectedPackage.price + addonSum;
    
    let pkgElem = document.getElementById('modal-pkg');
    let flavElem = document.getElementById('modal-flavour');
    let addonsElem = document.getElementById('modal-addons');
    let totalElem = document.getElementById('modal-total');
    
    if (pkgElem) pkgElem.innerText = selectedPackage.name + ' (£' + selectedPackage.price + ')';
    if (flavElem) flavElem.innerText = selectedFlavour;
    if (addonsElem) {
        addonsElem.innerText = selectedAddons.length > 0 ? selectedAddons.map(a => a.name + ' (+£' + a.price + ')').join(', ') : 'None';
    }
    if (totalElem) totalElem.innerText = '£' + total;
}

function dispatchWhatsAppOrder() {
    let name = document.getElementById('cust-name').value || 'Customer';
    let area = document.getElementById('cust-area').value || 'Central London';
    let phone = document.getElementById('cust-phone').value || '';
    
    let addonStr = selectedAddons.length > 0 ? selectedAddons.map(a => a.name + ' (£' + a.price + ')').join(', ') : 'None';
    let totalStr = document.getElementById('modal-total').innerText;
    
    let msg = `*NEW CONCIERGE SHISHA BOOKING*%0A` +
              `*Client:* ${name}%0A` +
              `*Delivery Location:* ${area}%0A` +
              `*Contact Phone:* ${phone}%0A` +
              `------------------------%0A` +
              `*Package:* ${selectedPackage.name}%0A` +
              `*Flavour:* ${selectedFlavour}%0A` +
              `*Upgrades:* ${addonStr}%0A` +
              `*Total Amount:* ${totalStr}%0A` +
              `------------------------%0A` +
              `Please confirm 24/7 delivery dispatch.`;
              
    window.open(`https://wa.me/447903375779?text=${msg}`, '_blank');
}

window.onclick = function(event) {
    let modal = document.getElementById('orderModal');
    if (event.target == modal) {
        modal.style.display = 'none';
    }
}
