/* Rajasthan Tourism - basic JavaScript */
(function () {
  // 1. highlight the active tab on every page
  var page = document.body.getAttribute('data-page');
  var links = document.querySelectorAll('.tabs a');
  for (var i = 0; i < links.length; i++) {
    if (links[i].getAttribute('data-tab') === page) links[i].classList.add('active');
  }

  // 2. mobile navigation toggle
  var toggle = document.getElementById('navToggle');
  var nav = document.getElementById('mainNav');
  if (toggle && nav) toggle.addEventListener('click', function () { nav.classList.toggle('open'); });

  // 3. heritage page live search filter
  var filter = document.getElementById('siteFilter');
  var grid = document.getElementById('siteGrid');
  var noResults = document.getElementById('noResults');
  if (filter && grid) {
    filter.addEventListener('input', function () {
      var q = filter.value.trim().toLowerCase(), visible = 0;
      var cards = grid.querySelectorAll('.card');
      for (var i = 0; i < cards.length; i++) {
        var hit = cards[i].textContent.toLowerCase().indexOf(q) !== -1;
        cards[i].style.display = hit ? '' : 'none';
        if (hit) visible++;
      }
      if (noResults) noResults.hidden = visible !== 0;
    });
  }

  // 4. gallery lightbox
  var lightbox = document.getElementById('lightbox');
  var lbImg = document.getElementById('lbImg');
  var lbCap = document.getElementById('lbCap');
  var lbClose = document.getElementById('lbClose');
  function closeLb() { if (lightbox) lightbox.hidden = true; }
  if (lightbox) {
    document.querySelectorAll('.g-item img').forEach(function (img) {
      img.addEventListener('click', function () {
        lbImg.src = img.src; lbImg.alt = img.alt; lbCap.innerHTML = img.getAttribute('data-caption');
        lightbox.hidden = false;
      });
    });
    lbClose.addEventListener('click', closeLb);
    lightbox.addEventListener('click', function (e) { if (e.target === lightbox) closeLb(); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeLb(); });
  }

  // 5. booking form validation + confirmation summary
  var form = document.getElementById('bookingForm');
  var errBox = document.getElementById('formError');
  function showError(msg) { errBox.textContent = msg; errBox.hidden = false; errBox.scrollIntoView(); }
  if (form) {
    // sensible date limits: check-in from today
    var today = new Date().toISOString().split('T')[0];
    var ci = document.getElementById('checkin'), co = document.getElementById('checkout');
    ci.min = today; co.min = today;
    form.addEventListener('submit', function (e) {
      e.preventDefault(); errBox.hidden = true;
      var name = document.getElementById('fullName').value.trim();
      var email = document.getElementById('email').value.trim();
      var phone = document.getElementById('phone').value.trim();
      if (name.length < 3) return showError('Please enter your full name.');
      if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) return showError('Please enter a valid email address.');
      if (!/^[0-9+\-\s]{10,15}$/.test(phone)) return showError('Please enter a valid phone number (10-15 digits).');
      if (!document.getElementById('city').value) return showError('Please choose a city.');
      if (!document.getElementById('hotelCat').value) return showError('Please choose a hotel category.');
      if (!ci.value || !co.value) return showError('Please choose check-in and check-out dates.');
      if (co.value <= ci.value) return showError('Check-out date must be after check-in date.');
      if (!document.getElementById('agree').checked) return showError('Please accept the booking terms to continue.');
      var nights = Math.round((new Date(co.value) - new Date(ci.value)) / 86400000);
      var roomType = form.querySelector('input[name=roomType]:checked').value;
      var meals = Array.prototype.map.call(form.querySelectorAll('input[name=meals]:checked'), function (m) { return m.value; }).join(', ') || 'None';
      var ref = 'RT-' + Date.now().toString().slice(-6);
      document.getElementById('bookingRef').innerHTML = 'Your booking reference is <strong>' + ref + '</strong>.';
      document.getElementById('bookingSummary').innerHTML =
        '<table>' +
        '<tr><td>Guest</td><td>' + escapeHtml(name) + ' (' + escapeHtml(email) + ', ' + escapeHtml(phone) + ')</td></tr>' +
        '<tr><td>Stay</td><td>' + escapeHtml(document.getElementById('city').value) + ' &mdash; ' + escapeHtml(document.getElementById('hotelCat').value) + ', ' + roomType + ' room</td></tr>' +
        '<tr><td>Dates</td><td>' + ci.value + ' to ' + co.value + ' (' + nights + ' night' + (nights > 1 ? 's' : '') + ')</td></tr>' +
        '<tr><td>Guests</td><td>' + document.getElementById('adults').value + ' adult(s), ' + document.getElementById('children').value + ' child(ren), ' + document.getElementById('rooms').value + ' room(s)</td></tr>' +
        '<tr><td>Meals</td><td>' + escapeHtml(meals) + '</td></tr>' +
        '</table>';
      document.getElementById('bookingDone').hidden = false;
      document.getElementById('bookingDone').scrollIntoView();
    });
  }
  function escapeHtml(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }
})();
