#!/usr/bin/env python3
"""Static site generator for the Rajasthan Tourism website (basic HTML/CSS/JS only)."""
import json, os, html

ROOT = os.path.dirname(os.path.abspath(__file__))

SITES = [
 dict(
  slug="amber-fort", name="Amber Fort", city="Jaipur",
  tagline="The majestic hill fort of the Kachhwaha Rajputs",
  facts=[("Built", "1592 onwards"), ("Built by", "Raja Man Singh I; expanded by Sawai Jai Singh"),
         ("Architecture", "Rajput – Mughal"), ("Recognition", "UNESCO World Heritage Site (Hill Forts of Rajasthan, 2013)")],
  description=[
   "Amber Fort, also spelled Amer Fort, rises from the Cheel ka Teela hill overlooking Maota Lake, about 11 kilometres from Jaipur. Its massive ramparts of pale yellow and pink sandstone enclose a complete royal complex of palaces, halls, gardens and temples.",
   "Inside, the fort unfolds as a sequence of courtyards: the Diwan-e-Aam (Hall of Public Audience) with its double row of columns, the stunning Sheesh Mahal (Mirror Palace) whose walls glitter with thousands of mirror inlays, the Sukh Niwas cooled by water channels, and the Jas Mandir with delicate floral glasswork. The fort is reached by a steep cobbled climb, traditionally on elephant back, through the Suraj Pol gate."],
  history=[
   "The Kachhwaha Rajputs ruled the Amber region long before Jaipur existed. Construction of the present fort began in 1592 under Raja Man Singh I, the trusted general of the Mughal emperor Akbar, and continued under his successors including Mirza Raja Jai Singh.",
   "When Sawai Jai Singh II founded the new planned city of Jaipur in 1727, the royal court moved down to the City Palace, but Amber Fort remained the ceremonial heart of the kingdom — coronations and major rituals were still performed here.",
   "In 2013, Amber Fort was inscribed as a UNESCO World Heritage Site as part of the serial nomination 'Hill Forts of Rajasthan', recognising it as an outstanding example of Rajput military and courtly architecture."]),
 dict(
  slug="mehrangarh-fort", name="Mehrangarh Fort", city="Jodhpur",
  tagline="The 'Citadel of the Sun' towering over the Blue City",
  facts=[("Built", "1459 onwards"), ("Built by", "Rao Jodha, Rathore chief of Marwar"),
         ("Architecture", "Rajput military"), ("Recognition", "One of the largest forts in India")],
  description=[
   "Mehrangarh Fort stands on a 410-foot-high rocky cliff, its walls rising almost vertically from the rock so that fort and hill look like one continuous mass of stone. From its ramparts, the blue-painted houses of Jodhpur's old city spread out below — the famous 'Blue City' view.",
   "Within the fort are some of Rajasthan's finest palace interiors: the Moti Mahal (Pearl Palace), Phool Mahal (Flower Palace) with its gilded ceiling, Sheesh Mahal, and the Takhat Vilas. The fort museum holds royal palanquins, howdahs, armoury, miniature paintings and the cradle room, while Chamunda Mataji temple at the southern end is still an active shrine."],
  history=[
   "Rao Jodha, chief of the Rathore clan, founded Jodhpur in 1459 and began the fort the same year, shifting his capital here from Mandore. Legend says a hermit, Cheeria Nathji, was displaced from the hill and cursed the land with drought — Rao Jodha built a temple to him and a house in atonement.",
   "Successive Rathore rulers added palaces and gates over nearly five centuries, including the Jai Pol (Victory Gate, 1806) and Fateh Pol. The fort was never taken by force in its early centuries, and its massive walls — up to 36 metres high and 21 metres thick in places — testify to Marwar's military might.",
   "Today the fort is managed by the Mehrangarh Museum Trust, set up by the Jodhpur royal family, and its museum is counted among the finest in Rajasthan."]),
 dict(
  slug="hawa-mahal", name="Hawa Mahal", city="Jaipur",
  tagline="The Palace of Winds with 953 windows",
  facts=[("Built", "1799"), ("Built by", "Maharaja Sawai Pratap Singh; architect Lal Chand Ustad"),
         ("Architecture", "Rajput, pink sandstone"), ("Recognition", "Icon of Jaipur, the Pink City")],
  description=[
   "Hawa Mahal is a five-storey pyramid-shaped facade of pink sandstone, famous for its 953 small latticed windows (jharokhas) decorated with intricate carvings. From the street it looks like a giant honeycomb crowned with domed canopies.",
   "The tiny windows were designed so royal ladies could observe everyday street life and festivals unseen, in keeping with purdah custom. The latticework also creates a natural cooling effect — the Venturi effect pulls breezes through the narrow passages, which is how the 'Palace of Winds' earned its name."],
  history=[
   "Maharaja Sawai Pratap Singh, a devotee of Lord Krishna, commissioned the Hawa Mahal in 1799. Its crown-like shape is said to represent the crown of Krishna, whom the king worshipped.",
   "The architect Lal Chand Ustad designed it as an extension of the City Palace complex, blending Rajput and Mughal elements. Unlike a conventional palace it has no grand front courtyard — it is essentially a screened gallery behind a spectacular facade.",
   "The Hawa Mahal remains Jaipur's most recognisable landmark and the visual symbol of the Pink City worldwide."]),
 dict(
  slug="jantar-mantar", name="Jantar Mantar", city="Jaipur",
  tagline="The world's largest stone astronomical observatory",
  facts=[("Built", "1734"), ("Built by", "Maharaja Sawai Jai Singh II"),
         ("Architecture", "Masonry astronomical instruments"), ("Recognition", "UNESCO World Heritage Site (2010)")],
  description=[
   "Jantar Mantar is a collection of nineteen enormous masonry instruments built to measure time, track celestial bodies and predict eclipses with the naked eye. The instruments are startling in scale — staircases climb the sides of giant sundials and curved quadrants.",
   "The centrepiece is the Samrat Yantra, the world's largest stone sundial at 27 metres tall, which tells local time accurate to about two seconds. Other instruments include the Jai Prakash Yantra, Ram Yantra and the Rashivalaya Yantras for the twelve zodiac constellations."],
  history=[
   "Sawai Jai Singh II, the astronomer-king who founded Jaipur, was troubled by errors in the calendars and astronomical tables of his day. Between 1724 and 1735 he built five observatories — at Delhi, Jaipur, Ujjain, Varanasi and Mathura — with Jaipur's the largest and best preserved.",
   "Jai Singh studied Ptolemy, Islamic zij tables and European astronomy, then had his scholars build instruments of unprecedented size because he believed larger instruments would give finer readings.",
   "In 2010 Jantar Mantar, Jaipur was inscribed as a UNESCO World Heritage Site as an outstanding expression of the astronomical and cosmological knowledge of an Indian princely court."]),
 dict(
  slug="city-palace-jaipur", name="City Palace", city="Jaipur",
  tagline="The royal residence at the heart of the Pink City",
  facts=[("Built", "1729–1732"), ("Built by", "Maharaja Sawai Jai Singh II; later additions by successors"),
         ("Architecture", "Rajput, Mughal and European blend"), ("Recognition", "Still the residence of Jaipur's royal family")],
  description=[
   "The City Palace occupies one-seventh of old Jaipur's walled area — a sprawling complex of courtyards, gardens, palaces and temples in the middle of the city Sawai Jai Singh II founded.",
   "Its highlights include the Chandra Mahal (seven storeys, still the royal residence), the Mubarak Mahal museum of textiles and costumes, the Diwan-e-Khas with two giant silver vessels (the largest silver objects in the world, used to carry Ganga water to London in 1902), and the famous Peacock Gate (Mor Chowk) with its vivid peacock mosaics."],
  history=[
   "When Sawai Jai Singh II moved his capital from Amber to the new planned city of Jaipur in 1727, the City Palace was built as the seat of his court between 1729 and 1732, designed with the help of the Bengali architect Vidyadhar Bhattacharya.",
   "Successive rulers added their own wings — Sawai Madho Singh II built the Mubarak Mahal in the late 19th century — so the complex records two centuries of evolving royal taste, from Rajput-Mughal fusion to colonial-era European touches.",
   "Part of the palace is a museum open to visitors, while the Chandra Mahal remains the home of Jaipur's erstwhile royal family."]),
 dict(
  slug="chittorgarh-fort", name="Chittorgarh Fort", city="Chittorgarh",
  tagline="The largest fort complex in India, symbol of Rajput valour",
  facts=[("Built", "7th century onwards"), ("Built by", "Maurya/Guhila rulers; expanded by Mewar's Sisodias"),
         ("Architecture", "Rajput military and temple architecture"), ("Recognition", "UNESCO World Heritage Site (Hill Forts of Rajasthan, 2013)")],
  description=[
   "Chittorgarh Fort sprawls over 700 acres on a 180-metre-high hill, stretching nearly 3 kilometres — the largest fort complex in India. Within its walls lies almost a complete medieval city: palaces, temples, reservoirs and towers.",
   "Its two great towers dominate the skyline — the 37-metre Vijay Stambha (Tower of Victory), carved inside and out with Hindu deities, and the older Kirti Stambha dedicated to Jain Tirthankaras. The Rana Kumbha Palace, Padmini's Palace by its lotus pool, and the Meera Temple are among its many monuments."],
  history=[
   "Tradition credits the fort's founding to the 7th century; it became the capital of the Sisodia Rajputs of Mewar and the stage for Rajasthan's most storied acts of resistance.",
   "Chittorgarh withstood three great sieges — by Alauddin Khalji in 1303, Bahadur Shah of Gujarat in 1535, and Akbar in 1567–68. Each ended in jauhar, the Rajput rite of collective self-immolation by the women, and saka, the final suicidal charge of the men — events that made Chittor the eternal symbol of Rajput honour.",
   "After Akbar's conquest the capital shifted to Udaipur, but the fort remained a place of pilgrimage. It was inscribed by UNESCO in 2013 as part of the Hill Forts of Rajasthan."]),
 dict(
  slug="ranthambore-fort", name="Ranthambore Fort", city="Sawai Madhopur",
  tagline="A thousand-year-old fort inside a tiger reserve",
  facts=[("Built", "10th century onwards"), ("Built by", "Chauhan Rajputs; famed under Hammir Dev Chauhan"),
         ("Architecture", "Rajput military"), ("Recognition", "UNESCO World Heritage Site (Hill Forts of Rajasthan, 2013)")],
  description=[
   "Ranthambore Fort crowns a 700-foot-high hill deep inside Ranthambore National Park, so visitors climb through forest where tigers, leopards and sloth bears roam. Its walls enclose temples, stepwells, palaces and the great Hammir's Court.",
   "The fort's Ganesh Temple is one of Rajasthan's most visited shrines — thousands of wedding invitations are sent to Lord Ganesha here each year. From the ramparts there are sweeping views over the lakes and forests of the reserve."],
  history=[
   "Built by Chauhan Rajputs in the 10th century, Ranthambore rose to fame under Hammir Dev Chauhan, who defied Alauddin Khalji and held the fort until its fall in 1301 after a legendary siege.",
   "The fort later passed to the Kachhwahas of Jaipur and served as a royal hunting ground — the surrounding forest that is now the national park.",
   "Inscribed by UNESCO in 2013 as part of the Hill Forts of Rajasthan, it is the rare World Heritage fort where history and wilderness meet: the climb up passes through one of India's finest tiger habitats."]),
 dict(
  slug="junagarh-fort", name="Junagarh Fort", city="Bikaner",
  tagline="The unconquered desert fort of Bikaner",
  facts=[("Built", "1589–1594"), ("Built by", "Raja Rai Singh, ruler of Bikaner"),
         ("Architecture", "Rajput with Mughal influence"), ("Recognition", "Never captured in battle")],
  description=[
   "Unlike most Rajasthan forts, Junagarh stands on the desert plain rather than a hill — yet its 986-metre-long wall with 37 bastions was never breached. Inside is a dazzling sequence of palaces rather than a single fortress block.",
   "The Anup Mahal, Chandra Mahal and Phool Mahal glow with gold leaf, mirror work and lacquered panels; the Karan Mahal was built to celebrate a Mughal victory, and the Badal Mahal is painted like a monsoon sky. The fort museum displays royal costumes, manuscripts and even a WWI biplane presented by the British."],
  history=[
   "Rao Bika founded Bikaner in 1488, but the present fort was built by his descendant Raja Rai Singh between 1589 and 1594. Rai Singh was a distinguished general in the Mughal armies of Akbar and Jahangir, and his campaigns funded the fort's lavish palaces.",
   "Though attacked several times, Junagarh was never captured — a record its rulers proudly maintained for over four centuries.",
   "The fort remained the seat of Bikaner's rulers until the 20th century and is now among Rajasthan's best-preserved palace-forts, famed for the contrast between its stern red-sandstone exterior and its jewel-box interiors."]),
 dict(
  slug="kumbhalgarh-fort", name="Kumbhalgarh Fort", city="Rajsamand",
  tagline="The fort with the 36-km wall, second longest in the world",
  facts=[("Built", "15th century (rebuilt 1443–1458)"), ("Built by", "Rana Kumbha of Mewar"),
         ("Architecture", "Rajput military"), ("Recognition", "UNESCO World Heritage Site (Hill Forts of Rajasthan, 2013)")],
  description=[
   "Kumbhalgarh's claim to fame is its wall — 36 kilometres of ramparts snaking over the Aravalli ridges, wide enough in places for eight horses to ride abreast. Only the Great Wall of China is longer among continuous walls.",
   "Inside are more than 360 temples, stepwells and palaces, including the Badal Mahal (Palace of Clouds) at the summit with its painted halls offering views across the Aravallis. The fort's seven massive gates guard the single winding approach road."],
  history=[
   "An earlier fort on the site was rebuilt and hugely expanded by Rana Kumbha, the great builder-king of Mewar, between 1443 and 1458, as part of his chain of 32 frontier forts.",
   "Kumbhalgarh was the refuge of Mewar's rulers in times of danger — most famously, Maharana Pratap was born here in 1540, and the infant prince was smuggled to safety within these walls during the crises of his reign.",
   "The fort withstood sieges by the combined armies of Malwa and Gujarat, and was inscribed by UNESCO in 2013 as part of the Hill Forts of Rajasthan."]),
 dict(
  slug="jaisalmer-fort", name="Jaisalmer Fort", city="Jaisalmer",
  tagline="The living Golden Fort of the Thar Desert",
  facts=[("Built", "1156"), ("Built by", "Rawal Jaisal, Bhati Rajput chief"),
         ("Architecture", "Rajput, yellow sandstone"), ("Recognition", "UNESCO World Heritage Site (Hill Forts of Rajasthan, 2013); one of the world's last living forts")],
  description=[
   "Jaisalmer Fort rises from Trikuta Hill like a giant sandcastle, its golden-yellow sandstone glowing amber at sunset — hence 'Sonar Quila', the Golden Fort. It is one of the very few living forts in the world: nearly 4,000 people still live and work inside its walls.",
   "Within are the Raj Mahal palace, exquisite Jain temples of the 12th–16th centuries with Dilwara-style carving, the Laxminath temple, and bazaars selling embroidery, leather and silver. Cannon points on the ramparts face the desert trade routes the fort once guarded."],
  history=[
   "Rawal Jaisal, chief of the Bhati Rajputs, founded the fort in 1156 on the old Silk Road caravan route, and Jaisalmer grew rich taxing the trade between India and Central Asia.",
   "The fort endured sieges, including a famous half-century-long standoff, and its Bhatis held it through the medieval era. Under the British it lost military importance but survived as a town.",
   "In 2013 it joined the UNESCO Hill Forts of Rajasthan listing. Conservationists now work to protect its sandstone from water seepage — the challenge of keeping a 900-year-old living fort alive in the modern age."]),
 dict(
  slug="umaid-bhawan-palace", name="Umaid Bhawan Palace", city="Jodhpur",
  tagline="One of the world's largest private residences, in golden Art Deco",
  facts=[("Built", "1929–1943"), ("Built by", "Maharaja Umaid Singh; architect Henry Vaughan Lanchester"),
         ("Architecture", "Art Deco / Beaux-Arts with Rajput motifs"), ("Recognition", "Among the largest private residences on earth (347 rooms)")],
  description=[
   "Umaid Bhawan Palace is a colossus of golden-yellow sandstone — 347 rooms arranged around a 105-foot-high central dome, blending Art Deco geometry with Rajput domes, jharokhas and courtyards.",
   "Today the palace is divided three ways: the royal family's private residence, the Taj-run luxury hotel, and a museum displaying clocks, vintage cars, stuffed leopards and the palace's original Art Deco interiors, including a striking indoor swimming pool."],
  history=[
   "Maharaja Umaid Singh commissioned the palace in 1929, partly as famine relief — its construction employed thousands of Jodhpur's citizens for over a decade during the Great Depression.",
   "The British architect Henry Vaughan Lanchester designed it in the fashionable Art Deco style, while Indian craftsmen gave it Rajput soul: the famous Makrana marble and sandstone inlay work echoes the Taj Mahal's pietra dura.",
   "Completed in 1943, it was among the last great palaces built in India before Independence, and remains a working palace, a heritage hotel and a museum all at once."]),
 dict(
  slug="city-palace-udaipur", name="City Palace, Udaipur", city="Udaipur",
  tagline="The lake palace complex of the Mewar Maharanas",
  facts=[("Built", "1559 onwards (over 400 years)"), ("Built by", "Maharana Udai Singh II and successors"),
         ("Architecture", "Rajput with Mughal, Chinese and European touches"), ("Recognition", "Largest palace complex in Rajasthan")],
  description=[
   "Udaipur's City Palace is Rajasthan's largest palace complex, a glittering facade of balconies, towers and cupolas rising directly from the eastern shore of Lake Pichola. Its terraces frame postcard views of the lake, Jag Mandir island and the Aravallis.",
   "Inside are the Mor Chowk (Peacock Courtyard) with its famous blue peacock mosaics, the Sheesh Mahal of mirrors, the Crystal Gallery housing the world's largest private crystal collection, and the Amar Vilas hanging garden. Much of the complex is now the City Palace Museum."],
  history=[
   "Maharana Udai Singh II founded Udaipur in 1559 after abandoning Chittorgarh, and began the palace on the lake's edge. For the next four centuries, 22 successive Maharanas each added their own palaces and courtyards — making it a living timeline of Mewar architecture.",
   "The palace witnessed the signing of the 1818 treaty with the British and survived the upheavals of 1947, when the Mewar royal family converted much of it into heritage hotels and museums.",
   "Today it anchors Udaipur's identity as India's most romantic heritage city, its lakefront silhouette familiar from films and postcards worldwide."]),
]

CITIES = ["Jaipur", "Jodhpur", "Udaipur", "Jaisalmer", "Bikaner", "Chittorgarh", "Mount Abu", "Sawai Madhopur", "Rajsamand"]

# ---------------- templates ----------------

BASE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | Rajasthan Tourism</title>
<meta name="description" content="{meta}">
<link rel="stylesheet" href="{root}css/style.css">
</head>
<body data-page="{page}">
<header class="site-header">
  <div class="header-inner">
    <a class="brand" href="{root}index.html">
      <img src="{root}images/logo.svg" alt="Rajasthan Tourism logo" class="logo">
      <span class="brand-text"><span class="brand-city">Rajasthan</span><span class="brand-sub">Land of Kings</span></span>
    </a>
    <button class="nav-toggle" id="navToggle" aria-label="Toggle navigation">&#9776;</button>
    <nav class="tabs" id="mainNav">
      <a href="{root}index.html" data-tab="home">Home</a>
      <a href="{root}heritage.html" data-tab="heritage">Heritage</a>
      <a href="{root}booking.html" data-tab="booking">Hotel Booking</a>
      <a href="{root}gallery.html" data-tab="gallery">Gallery</a>
    </nav>
  </div>
</header>
<main class="container">
{content}
</main>
<footer class="site-footer">
  <p><strong>Rajasthan Tourism</strong> &mdash; a student project showcasing the heritage of Rajasthan, India.</p>
  <p>Images: Wikimedia Commons contributors (see gallery captions). Built with basic HTML, CSS &amp; JavaScript.</p>
</footer>
<script src="{root}js/main.js"></script>
</body>
</html>
"""

def page(title, meta, pagename, root, content):
    return BASE.format(title=html.escape(title), meta=html.escape(meta),
                       page=pagename, root=root, content=content)

def site_card(s, root):
    return f"""<article class="card">
  <a class="card-link" href="{root}sites/{s['slug']}.html">
    <img src="{s['hero']}" alt="{html.escape(s['name'])}" loading="lazy">
    <span class="card-body">
      <span class="card-title">{html.escape(s['name'])}</span>
      <span class="card-city">{html.escape(s['city'])}</span>
      <span class="card-tag">{html.escape(s['tagline'])}</span>
      <span class="btn">Explore &rarr;</span>
    </span>
  </a>
</article>"""

# ---------------- page builders ----------------

def build_home(sites, bg):
    featured = sites[:4]
    cards = "\n".join(site_card(s, "") for s in featured)
    content = f"""
<section class="hero">
  <h2>Welcome to Rajasthan</h2>
  <p class="lead">Forts that touch the sky, palaces of mirror and marble, desert cities glowing gold at sunset &mdash; explore the royal heritage of India's Land of Kings.</p>
  <div class="hero-cta">
    <a class="btn btn-big" href="heritage.html">Explore Heritage Sites</a>
    <a class="btn btn-big btn-ghost" href="booking.html">Book a Hotel</a>
  </div>
</section>
<section>
  <h2>About Rajasthan</h2>
  <div class="panel">
    <p>Rajasthan, India's largest state, was once a land of proud Rajput kingdoms &mdash; Mewar, Marwar, Amber, Bikaner and Jaisalmer. Their legacy survives in some of the finest forts and palaces on earth, six of which are UNESCO World Heritage Sites under the "Hill Forts of Rajasthan" listing.</p>
    <p>This website is your guide to <strong>twelve</strong> of the greatest heritage sites of Rajasthan. Visit the <a href="heritage.html">Heritage</a> page to browse them all, open any site for its story and history, wander through the <a href="gallery.html">Gallery</a>, and plan your stay on the <a href="booking.html">Hotel Booking</a> page.</p>
  </div>
</section>
<section>
  <h2>Featured Sites</h2>
  <div class="grid">{cards}</div>
  <p class="center"><a class="btn" href="heritage.html">View all 12 heritage sites &rarr;</a></p>
</section>
<section>
  <h2>Plan Your Visit</h2>
  <div class="panel two-col">
    <div>
      <h3>Best time to visit</h3>
      <p>October to March, when the desert heat eases and festivals like the Pushkar Fair and Desert Festival light up the state.</p>
    </div>
    <div>
      <h3>Getting around</h3>
      <p>Jaipur, Jodhpur and Udaipur are well connected by rail and air. The classic route &mdash; Delhi &rarr; Jaipur &rarr; Jodhpur &rarr; Jaisalmer &rarr; Udaipur &mdash; covers most sites on this website.</p>
    </div>
  </div>
</section>"""
    return page("Home", "Rajasthan Tourism - explore forts, palaces and heritage sites of Rajasthan", "home", "", content)

def build_heritage(sites):
    cards = "\n".join(site_card(s, "") for s in sites)
    content = f"""
<section>
  <h2>Heritage Sites of Rajasthan</h2>
  <p class="lead">Twelve magnificent forts, palaces and observatories. Click any picture to open its dedicated page with a full description and history.</p>
  <div class="panel">
    <label class="filter-label" for="siteFilter">Search sites:</label>
    <input type="text" id="siteFilter" placeholder="Type a name or city, e.g. Jaipur&hellip;" autocomplete="off">
  </div>
  <div class="grid" id="siteGrid">{cards}</div>
  <p class="center muted" id="noResults" hidden>No sites match your search.</p>
</section>"""
    return page("Heritage Sites", "List of heritage sites of Rajasthan with photos", "heritage", "", content)

def build_site_page(s):
    facts = "\n".join(f"<tr><th>{html.escape(k)}</th><td>{html.escape(v)}</td></tr>" for k, v in s["facts"])
    desc = "\n".join(f"<p>{html.escape(p)}</p>" for p in s["description"])
    hist = "\n".join(f"<p>{html.escape(p)}</p>" for p in s["history"])
    extra = "\n".join(
        f'<figure class="thumb"><img src="{u}" alt="{html.escape(s["name"])} photo" loading="lazy"></figure>'
        for u in s["images"] if u != s["hero"])
    content = f"""
<section>
  <p class="crumb"><a href="../heritage.html">&larr; All heritage sites</a></p>
  <h2>{html.escape(s['name'])}</h2>
  <p class="lead">{html.escape(s['tagline'])} &mdash; {html.escape(s['city'])}, Rajasthan</p>
  <figure class="hero-img"><img src="{s['hero']}" alt="{html.escape(s['name'])}"></figure>
  <div class="two-col">
    <div>
      <h3>About this site</h3>
      <div class="panel">{desc}</div>
      <h3>History</h3>
      <div class="panel">{hist}</div>
    </div>
    <aside>
      <h3>Quick facts</h3>
      <table class="facts">{facts}</table>
      <h3>More photos</h3>
      <div class="thumb-row">{extra}</div>
    </aside>
  </div>
</section>"""
    return page(s["name"], f"{s['name']}, {s['city']} - description and history", "heritage", "../", content)

def build_booking():
    city_opts = "\n".join(f'<option value="{c}">{c}</option>' for c in CITIES)
    content = f"""
<section>
  <h2>Hotel Booking</h2>
  <p class="lead">Fill in the form below to reserve your stay in Rajasthan. All fields marked * are required.</p>
  <form id="bookingForm" class="panel form" novalidate>
    <fieldset>
      <legend>Guest details</legend>
      <div class="form-row">
        <div class="form-group"><label for="fullName">Full name *</label><input type="text" id="fullName" name="fullName" required placeholder="e.g. Aman Sharma"></div>
        <div class="form-group"><label for="email">Email *</label><input type="email" id="email" name="email" required placeholder="you@example.com"></div>
      </div>
      <div class="form-row">
        <div class="form-group"><label for="phone">Phone number *</label><input type="tel" id="phone" name="phone" required placeholder="10-digit mobile number"></div>
        <div class="form-group"><label for="idProof">ID proof *</label>
          <select id="idProof" name="idProof" required>
            <option value="">-- Select --</option><option>Aadhaar Card</option><option>Passport</option><option>Driving Licence</option><option>Voter ID</option>
          </select></div>
      </div>
    </fieldset>
    <fieldset>
      <legend>Stay details</legend>
      <div class="form-row">
        <div class="form-group"><label for="city">City *</label><select id="city" name="city" required><option value="">-- Select city --</option>{city_opts}</select></div>
        <div class="form-group"><label for="hotelCat">Hotel category *</label>
          <select id="hotelCat" name="hotelCat" required><option value="">-- Select --</option><option>Budget</option><option>3-Star</option><option>4-Star</option><option>5-Star</option><option>Heritage Palace Hotel</option></select></div>
      </div>
      <div class="form-row">
        <div class="form-group"><label for="checkin">Check-in date *</label><input type="date" id="checkin" name="checkin" required></div>
        <div class="form-group"><label for="checkout">Check-out date *</label><input type="date" id="checkout" name="checkout" required></div>
      </div>
      <div class="form-row three">
        <div class="form-group"><label for="adults">Adults *</label><input type="number" id="adults" name="adults" min="1" max="10" value="2" required></div>
        <div class="form-group"><label for="children">Children</label><input type="number" id="children" name="children" min="0" max="10" value="0"></div>
        <div class="form-group"><label for="rooms">Rooms *</label><input type="number" id="rooms" name="rooms" min="1" max="10" value="1" required></div>
      </div>
      <div class="form-group"><span class="label">Room type *</span>
        <div class="radio-row">
          <label><input type="radio" name="roomType" value="Standard" checked> Standard</label>
          <label><input type="radio" name="roomType" value="Deluxe"> Deluxe</label>
          <label><input type="radio" name="roomType" value="Suite"> Suite</label>
          <label><input type="radio" name="roomType" value="Family"> Family</label>
        </div>
      </div>
      <div class="form-group"><span class="label">Meal plan</span>
        <div class="radio-row">
          <label><input type="checkbox" name="meals" value="Breakfast" checked> Breakfast</label>
          <label><input type="checkbox" name="meals" value="Lunch"> Lunch</label>
          <label><input type="checkbox" name="meals" value="Dinner"> Dinner</label>
        </div>
      </div>
      <div class="form-group"><label for="requests">Special requests</label><textarea id="requests" name="requests" rows="4" placeholder="Early check-in, extra bed, honeymoon setup&hellip;"></textarea></div>
    </fieldset>
    <div class="form-group check"><label><input type="checkbox" id="agree" required> I agree to the booking terms and cancellation policy *</label></div>
    <p class="form-error" id="formError" hidden></p>
    <div class="form-actions"><button type="submit" class="btn btn-big">Confirm Booking</button><button type="reset" class="btn btn-ghost">Reset</button></div>
  </form>
  <div class="panel" id="bookingDone" hidden>
    <h3>Booking confirmed!</h3>
    <p id="bookingRef"></p>
    <div id="bookingSummary"></div>
    <p class="muted">This is a demo confirmation &mdash; no real reservation was made.</p>
  </div>
</section>"""
    return page("Hotel Booking", "Book a hotel in Rajasthan - booking form", "booking", "", content)

def build_gallery(sites):
    figs = []
    for s in sites:
        for u in s["images"]:
            figs.append(f'<figure class="g-item"><img src="{u}" alt="{html.escape(s["name"])}" loading="lazy" data-caption="{html.escape(s["name"])} &mdash; {html.escape(s["city"])}"><figcaption>{html.escape(s["name"])}, {html.escape(s["city"])}</figcaption></figure>')
    content = f"""
<section>
  <h2>Photo Gallery</h2>
  <p class="lead">Photographs of Rajasthan's heritage sites. Click any photo to view it larger.</p>
  <div class="gallery" id="galleryGrid">
{"".join(figs)}
  </div>
</section>
<div class="lightbox" id="lightbox" hidden>
  <button class="lb-close" id="lbClose" aria-label="Close">&times;</button>
  <img id="lbImg" alt="">
  <p id="lbCap"></p>
</div>"""
    return page("Gallery", "Photo gallery of Rajasthan heritage sites", "gallery", "", content)

# ---------------- css ----------------

CSS = """/* Rajasthan Tourism - shared look for every page (basic CSS, no frameworks) */
:root {
  --maroon: #7b1e1e;
  --saffron: #e07b1f;
  --gold: #c9a227;
  --sand: #f7f0e1;
  --ink: #2e2018;
}
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; }
body {
  font-family: Georgia, 'Times New Roman', serif;
  color: var(--ink);
  min-height: 100vh;
  background-color: #3a2415;
  background-image: url("__BG__");
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
}
body::before { /* warm readable overlay over the shared background */
  content: ""; position: fixed; inset: 0; z-index: -1;
  background: linear-gradient(rgba(58,36,21,.72), rgba(58,36,21,.78));
}
.container { max-width: 1100px; margin: 0 auto; padding: 20px 16px 40px; }
.center { text-align: center; }
.muted { color: #6b5844; font-size: .95em; }
.lead { font-size: 1.12em; line-height: 1.6; }

/* header: logo + city name + tabs, identical on all pages */
.site-header {
  background: linear-gradient(180deg, var(--maroon), #5e1414);
  border-bottom: 4px solid var(--gold);
  box-shadow: 0 2px 10px rgba(0,0,0,.35);
  position: sticky; top: 0; z-index: 50;
}
.header-inner { max-width: 1100px; margin: 0 auto; padding: 10px 16px; display: flex; align-items: center; gap: 16px; flex-wrap: wrap; }
.brand { display: flex; align-items: center; gap: 12px; text-decoration: none; margin-right: auto; }
.logo { width: 56px; height: 56px; }
.brand-text { display: flex; flex-direction: column; line-height: 1.1; }
.brand-city { font-size: 1.9em; font-weight: bold; color: #fff; letter-spacing: 1px; }
.brand-sub { color: var(--gold); font-style: italic; font-size: .95em; }
.nav-toggle { display: none; background: var(--gold); border: none; border-radius: 6px; font-size: 1.4em; padding: 6px 12px; cursor: pointer; color: #4a2c12; }
.tabs { display: flex; gap: 6px; flex-wrap: wrap; }
.tabs a {
  color: #fff; text-decoration: none; font-family: Verdana, sans-serif; font-size: .95em;
  padding: 10px 16px; border-radius: 8px 8px 0 0; border: 1px solid transparent; border-bottom: none;
}
.tabs a:hover { background: rgba(255,255,255,.14); }
.tabs a.active { background: var(--sand); color: var(--maroon); font-weight: bold; border-color: var(--gold); }

/* content */
h2 { color: #fff; font-size: 1.8em; border-bottom: 3px solid var(--gold); padding-bottom: 8px; text-shadow: 1px 1px 3px rgba(0,0,0,.5); }
h3 { color: var(--maroon); }
section { margin-bottom: 34px; }
.panel { background: var(--sand); border: 1px solid var(--gold); border-radius: 12px; padding: 18px 22px; box-shadow: 0 2px 8px rgba(0,0,0,.25); line-height: 1.65; }
.panel a { color: var(--maroon); }
.two-col { display: grid; grid-template-columns: 1fr 340px; gap: 24px; align-items: start; }
@media (max-width: 860px) { .two-col { grid-template-columns: 1fr; } }
.hero { text-align: center; background: rgba(123,30,30,.85); border: 2px solid var(--gold); border-radius: 14px; padding: 34px 22px; color: #fff; }
.hero h2 { border: none; font-size: 2.2em; margin: 0 0 10px; text-shadow: 2px 2px 4px rgba(0,0,0,.5); }
.hero .lead { max-width: 640px; margin: 0 auto 20px; }
.hero-cta { display: flex; gap: 12px; justify-content: center; flex-wrap: wrap; }

/* buttons */
.btn { display: inline-block; background: var(--saffron); color: #fff; text-decoration: none; font-family: Verdana, sans-serif;
  padding: 10px 18px; border-radius: 8px; border: 1px solid #b35f14; cursor: pointer; font-size: .95em; }
.btn:hover { background: #c96a12; }
.btn-big { font-size: 1.05em; padding: 12px 26px; }
.btn-ghost { background: transparent; border: 2px solid #fff; }
.btn-ghost:hover { background: rgba(255,255,255,.15); }
form .btn-ghost { border-color: var(--maroon); color: var(--maroon); }
form .btn-ghost:hover { background: rgba(123,30,30,.08); }

/* heritage cards */
.grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 18px; margin: 18px 0; }
.card { background: var(--sand); border-radius: 12px; overflow: hidden; border: 1px solid var(--gold); box-shadow: 0 2px 8px rgba(0,0,0,.3); transition: transform .2s; }
.card:hover { transform: translateY(-4px); }
.card-link { text-decoration: none; color: inherit; display: block; }
.card img { width: 100%; height: 180px; object-fit: cover; display: block; }
.card-body { padding: 14px 16px; display: flex; flex-direction: column; gap: 6px; }
.card-title { font-size: 1.2em; font-weight: bold; color: var(--maroon); }
.card-city { font-family: Verdana, sans-serif; font-size: .8em; color: #fff; background: var(--maroon); align-self: flex-start; padding: 2px 10px; border-radius: 10px; }
.card-tag { font-style: italic; color: #6b5844; font-size: .95em; }
.card .btn { align-self: flex-start; margin-top: 6px; }
.filter-label { font-weight: bold; margin-right: 8px; }
#siteFilter { font-size: 1em; padding: 8px 12px; border-radius: 8px; border: 1px solid var(--gold); width: min(360px, 100%); font-family: inherit; }

/* site pages */
.crumb a { color: var(--gold); }
.hero-img img { width: 100%; max-height: 420px; object-fit: cover; border-radius: 12px; border: 3px solid var(--gold); box-shadow: 0 4px 14px rgba(0,0,0,.4); }
table.facts { width: 100%; border-collapse: collapse; background: var(--sand); border-radius: 12px; overflow: hidden; font-size: .95em; }
table.facts th, table.facts td { text-align: left; padding: 10px 12px; border-bottom: 1px solid #e0d3b8; vertical-align: top; }
table.facts th { background: var(--maroon); color: #fff; width: 38%; font-family: Verdana, sans-serif; font-size: .85em; }
.thumb-row { display: flex; gap: 10px; flex-wrap: wrap; }
.thumb img { width: 150px; height: 100px; object-fit: cover; border-radius: 8px; border: 2px solid var(--gold); }

/* gallery + lightbox */
.gallery { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 14px; }
.g-item { margin: 0; background: var(--sand); border-radius: 10px; overflow: hidden; border: 1px solid var(--gold); cursor: pointer; }
.g-item img { width: 100%; height: 170px; object-fit: cover; display: block; transition: transform .2s; }
.g-item:hover img { transform: scale(1.04); }
.g-item figcaption { padding: 8px 10px; font-size: .85em; color: #5a4632; font-family: Verdana, sans-serif; }
.lightbox { position: fixed; inset: 0; background: rgba(0,0,0,.88); display: flex; flex-direction: column; align-items: center; justify-content: center; z-index: 100; padding: 20px; }
.lightbox[hidden] { display: none; }
.lightbox img { max-width: 92vw; max-height: 78vh; border: 3px solid var(--gold); border-radius: 8px; }
.lightbox p { color: #fff; margin-top: 12px; }
.lb-close { position: absolute; top: 14px; right: 22px; font-size: 2.4em; background: none; border: none; color: #fff; cursor: pointer; }

/* booking form */
.form fieldset { border: 2px solid var(--gold); border-radius: 10px; margin: 0 0 18px; padding: 16px; }
.form legend { font-weight: bold; color: var(--maroon); padding: 0 8px; font-size: 1.1em; }
.form-row { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; }
.form-row.three { grid-template-columns: 1fr 1fr 1fr; }
@media (max-width: 640px) { .form-row, .form-row.three { grid-template-columns: 1fr; } }
.form-group { margin-bottom: 12px; }
.form-group label, .form-group .label { display: block; font-weight: bold; margin-bottom: 5px; font-family: Verdana, sans-serif; font-size: .88em; }
.form-group input[type=text], .form-group input[type=email], .form-group input[type=tel],
.form-group input[type=date], .form-group input[type=number], .form-group select, .form-group textarea {
  width: 100%; padding: 9px 10px; border: 1px solid #b89b5e; border-radius: 8px; font-size: 1em; font-family: inherit; background: #fffdf7;
}
.radio-row { display: flex; gap: 16px; flex-wrap: wrap; }
.radio-row label { font-weight: normal; display: flex; align-items: center; gap: 6px; }
.check label { font-weight: normal; }
.form-error { color: #a31212; font-weight: bold; background: #fbe3e3; border: 1px solid #a31212; border-radius: 8px; padding: 10px 14px; }
.form-actions { display: flex; gap: 12px; flex-wrap: wrap; }
#bookingSummary table { width: 100%; border-collapse: collapse; }
#bookingSummary td { padding: 6px 8px; border-bottom: 1px solid #e0d3b8; }
#bookingSummary td:first-child { font-weight: bold; width: 40%; }

/* footer */
.site-footer { background: #2b1408; color: #d9c9a8; text-align: center; padding: 22px 16px; border-top: 4px solid var(--gold); font-size: .9em; }
.site-footer p { margin: 6px 0; }

@media (max-width: 720px) {
  .nav-toggle { display: block; margin-left: auto; }
  .tabs { display: none; width: 100%; flex-direction: column; }
  .tabs.open { display: flex; }
  .tabs a { border-radius: 8px; }
  .brand-city { font-size: 1.5em; }
}
"""

# ---------------- js ----------------

JS = """/* Rajasthan Tourism - basic JavaScript */
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
      if (!/^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/.test(email)) return showError('Please enter a valid email address.');
      if (!/^[0-9+\\-\\s]{10,15}$/.test(phone)) return showError('Please enter a valid phone number (10-15 digits).');
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
"""

# ---------------- logo ----------------

LOGO = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="47" fill="#7b1e1e" stroke="#c9a227" stroke-width="4"/>
  <path d="M28 72 V46 l6 -4 v-8 l6 4 v-8 l6 6 v-8 l6 6 v-8 l6 4 v-8 l6 4 V72 Z" fill="#c9a227"/>
  <path d="M40 72 V56 a10 10 0 0 1 20 0 V72 Z" fill="#7b1e1e"/>
  <rect x="22" y="72" width="56" height="6" fill="#c9a227"/>
  <circle cx="50" cy="30" r="4" fill="#e07b1f"/>
</svg>
"""

# ---------------- readme ----------------

README = """# Rajasthan Tourism

A tourism website for the heritage sites of **Rajasthan, India** — built with **only basic HTML, CSS and JavaScript** (no frameworks, no build tools).

🌍 **Live website:** https://aman05cody.github.io/rajasthan-tourism/

## Pages (16)

| Page | File |
|---|---|
| Home (city name + logo, navigation tabs) | `index.html` |
| Heritage — list of 12 sites, each picture links to its own page | `heritage.html` |
| Hotel Booking — booking form | `booking.html` |
| Gallery — photos of heritage sites | `gallery.html` |
| 12 dedicated heritage-site pages (description + history) | `sites/*.html` |

### Heritage sites covered
Amber Fort, Mehrangarh Fort, Hawa Mahal, Jantar Mantar (Jaipur) · City Palace Jaipur · Chittorgarh Fort · Ranthambore Fort · Junagarh Fort (Bikaner) · Kumbhalgarh Fort · Jaisalmer Fort · Umaid Bhawan Palace (Jodhpur) · City Palace Udaipur.

## Features
- Same background image and identical header/footer styling on every page
- Navigation tabs on all pages: Home · Heritage · Hotel Booking · Gallery
- Live search filter on the Heritage page, lightbox on the Gallery page
- Hotel booking form with full client-side validation and a booking confirmation summary
- Mobile-friendly responsive layout

## Run locally
Just open `index.html` in a browser, or serve the folder:
```
python3 -m http.server
```

## Credits
Photographs: Wikimedia Commons contributors. Site generated by `gen.py` (Python build script; the website itself is pure HTML/CSS/JS).
"""

# ---------------- main ----------------

def load_images():
    path = os.path.join(ROOT, "data", "images.json")
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    # placeholder until the image search finishes
    return {"background": "", "sites": {s["slug"]: {"hero": "", "images": ["", "", ""]} for s in SITES}}

def main():
    data = load_images()
    bg = data.get("background", "")
    for s in SITES:
        info = data.get("sites", {}).get(s["slug"], {})
        s["hero"] = info.get("hero", "")
        s["images"] = info.get("images", []) or [""]

    def w(rel, text):
        p = os.path.join(ROOT, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w") as f:
            f.write(text)

    w("css/style.css", CSS.replace("__BG__", bg))
    w("js/main.js", JS)
    w("images/logo.svg", LOGO)
    w("README.md", README)
    w("index.html", build_home(SITES, bg))
    w("heritage.html", build_heritage(SITES))
    w("booking.html", build_booking())
    w("gallery.html", build_gallery(SITES))
    for s in SITES:
        w(f"sites/{s['slug']}.html", build_site_page(s))
    print("wrote 16 pages + css/js/logo/readme")

if __name__ == "__main__":
    main()
