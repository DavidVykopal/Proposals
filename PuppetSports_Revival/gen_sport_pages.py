#!/usr/bin/env python3
"""Build soccer.html and hockey.html from index.html.

Everything from the LED board divider down (proof, bundles, add-ons, process,
term sheet, CTA, footer, script) is copied byte-identical from index.html so the
commercial terms can never drift between the three pages. Only a handful of
sport-specific strings are substituted in that tail.
"""
import pathlib

PUB = pathlib.Path('/Users/davidvykopal/.superset/worktrees/78e07d52-6fb3-4c2e-a8e7-bd8bf30ca9dc/puppets/PuppetSports_Revival/public')
core = (PUB / 'index.html').read_text()

TAIL_MARK = '  <!-- ===== Board divider ===== -->'
assert TAIL_MARK in core
tail = core[core.index(TAIL_MARK):]


def head(title, note):
    return f'''<!doctype html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="robots" content="noindex, nofollow" />
  <title>{title}</title>
  <link rel="icon" href="assets/noxgames-logo.png" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&family=Montserrat:wght@700;800;900&display=swap" rel="stylesheet" />

  <!--
    ============================================================
    {note}
    Generated from index.html by gen_sport_pages.py. Everything from the LED board
    divider down is copied from index.html so bundle prices and the term sheet stay
    identical across all three pages. Edit index.html, then regenerate.
    ============================================================
  -->

  <link rel="stylesheet" href="assets/style.css" />
</head>
<body>
'''


NAV = '''
  <!-- ===== Navigation ===== -->
  <nav id="navbar">
    <div class="shell nav-inner">
      <a href="#top" class="brand">
        <img src="assets/noxgames-logo.png" alt="NOXGAMES logo" />
        <span>NOXGAMES</span>
      </a>
      <div class="nav-links">
        <a href="#legacy">Legacy</a>
        <a href="#game">The Game</a>
        <a href="#brand">Your Brand</a>
        <a href="#proof">Proof</a>
        <a href="#bundles">Bundles</a>
        <a href="#process">Process</a>
        <a href="#terms" class="nav-cta">Term Sheet</a>
      </div>
      <button class="nav-burger" aria-label="Open menu" aria-expanded="false" onclick="toggleMenu()">
        <svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M3 6h18M3 12h18M3 18h18"/></svg>
      </button>
    </div>
    <div id="mobileMenu">
      <a href="#legacy" onclick="toggleMenu()">Legacy</a>
      <a href="#game" onclick="toggleMenu()">The Game</a>
      <a href="#brand" onclick="toggleMenu()">Your Brand</a>
      <a href="#proof" onclick="toggleMenu()">Proof</a>
      <a href="#bundles" onclick="toggleMenu()">Bundles</a>
      <a href="#process" onclick="toggleMenu()">Process</a>
      <a href="#terms" onclick="toggleMenu()">Term Sheet</a>
    </div>
  </nav>
'''

CARDS_WHY = '''
      <div class="grid-4" style="margin-top: 22px;">
        <div class="glass-card reveal">
          <h3>The code still runs</h3>
          <p class="card-text">This is not a rewrite from a design document. We own the source and the title ships updates today. A branded edition is a re-skin and a re-balance, which is why the timeline reads in weeks.</p>
        </div>
        <div class="glass-card reveal d1">
          <h3>The shelf is empty</h3>
          <p class="card-text">Casual arcade sports has been largely vacated on mobile. The genre that once filled the top charts has almost no active competition and no licensed presence at all.</p>
        </div>
        <div class="glass-card reveal d2">
          <h3>A board lasts a second</h3>
          <p class="card-text">A perimeter impression is over before it registers. A match runs for minutes, with your identity in the frame the entire time, on a device the fan is already holding.</p>
        </div>
        <div class="glass-card reveal d3">
          <h3>Brand safe by construction</h3>
          <p class="card-text">Cartoon puppets, no violence, no chat rooms, no gambling mechanics. The rating that let the franchise reach forty-two million downloads is the rating that lets you put your crest on it.</p>
        </div>
      </div>
'''


# ----------------------------------------------------------------- SOCCER ---
SOCCER = head(
    'Puppet Soccer | Club, League &amp; Brand Partnership | NOXGAMES',
    'PUPPET SOCCER partnership page. Store figures verified on Google Play 23 Aug 2026:\n    10M+ installs, 4.3 stars, 467K ratings, last updated 7 Aug 2026.',
) + NAV + '''
  <!-- ===== Hero ===== -->
  <header class="hero" id="top">
    <span class="orb o1"></span>
    <span class="orb o2"></span>
    <span class="orb o3"></span>

    <div class="shell hero-grid">
      <div>
        <span class="eyebrow"><span class="dot"></span> NOXGAMES &middot; Puppet Soccer &middot; Partnership Offer</span>
        <h1>
          Your crest, on<br />
          <span class="grad-pitch">ten million phones.</span>
        </h1>
        <p class="hero-sub">
          Puppet Soccer has <strong>10 million plus downloads</strong> and <b>4.3 stars from 467,000 ratings</b>.
          It is still on Google Play and it was updated this month. We own the code, we are rebuilding it for
          the players who grew up on it, and <strong>one football partner</strong> gets the kit, the boards,
          the cup and the league inside it.
        </p>
        <div class="hero-actions">
          <a href="#bundles" class="btn btn-neon">
            <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 1v22M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
            See the bundles
          </a>
          <a href="#brand" class="btn btn-ghost">
            <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12h20M12 2v20"/><circle cx="12" cy="12" r="9"/></svg>
            Where your brand lives
          </a>
        </div>
      </div>

      <div class="mock-wrap reveal">
        <div class="mock-chip c1">10M+<small>Downloads on Google Play</small></div>
        <div class="mock-chip c2">4.3 stars<small>From 467,000 ratings</small></div>
        <div class="mock-chip c3">1 partner<small>Football, category exclusive</small></div>
        <div class="mock-chip c4"><b>42M downloads</b><small>Across the Puppet Sports lineup</small></div>
        <div class="device">
          <img src="assets/soccer-1.jpg" alt="Puppet Soccer match in progress with sponsor boards around the pitch" />
        </div>
      </div>
    </div>

    <span class="scroll-hint">
      <svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M6 9l6 6 6-6"/></svg>
    </span>
  </header>

  <!-- ===== Stat strip ===== -->
  <div class="stat-strip">
    <div class="shell">
      <div class="stat-grid">
        <div class="stat">
          <div class="n grad-pitch">10M+</div>
          <p>Downloads on <b>Google Play alone</b>, before the other stores.</p>
        </div>
        <div class="stat">
          <div class="n grad-text">467K</div>
          <p>Player ratings, <b>still arriving</b> a decade after release.</p>
        </div>
        <div class="stat">
          <div class="n grad-gold">4.3</div>
          <p>Current store rating. The title was <b>last updated this month</b>.</p>
        </div>
        <div class="stat">
          <div class="n grad-ice">1</div>
          <p>Football partner. <b>Category exclusive</b>, for the length of the deal.</p>
        </div>
      </div>
    </div>
  </div>

  <!-- ===== Legacy ===== -->
  <section id="legacy">
    <div class="shell">
      <div class="sec-head">
        <div class="reveal">
          <span class="sec-label">The Legacy</span>
          <h2>Football already <span class="grad-pitch">played this game.</span></h2>
        </div>
        <p class="reveal d1">
          Puppet Soccer was one of the biggest arcade football games on mobile. It is not a concept we are
          pitching, it is a product with ten million downloads, a decade of players and a live store listing
          you can check right now.
        </p>
      </div>

      <div class="grid-3">
        <div class="glass-card reveal">
          <div class="icon-badge pitch">
            <svg viewBox="0 0 24 24" fill="none" stroke="#2fd98b" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 3v18h18"/><path d="M7 14l4-4 3 3 6-6"/></svg>
          </div>
          <h3>The numbers held</h3>
          <p class="card-text">
            <strong>10 million plus installs</strong> and <strong>4.3 stars from 467,000 ratings</strong> on
            Google Play. Across the whole Puppet Sports franchise, more than
            <strong>42 million downloads</strong>. Most new football titles never reach either number.
          </p>
        </div>
        <div class="glass-card reveal d1">
          <div class="icon-badge gold">
            <svg viewBox="0 0 24 24" fill="none" stroke="#ffb938" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
          </div>
          <h3>No tutorial, no translation</h3>
          <p class="card-text">
            A big head, a big boot, a ball and two goals. <strong>Nothing to read and nothing to learn.</strong>
            The game travelled to every market it was published in, which is why a club's international
            following can play it as easily as the people in the stadium.
          </p>
        </div>
        <div class="glass-card reveal d2">
          <div class="icon-badge">
            <svg viewBox="0 0 24 24" fill="none" stroke="#00d2ff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12a9 9 0 1 1-9-9"/><path d="M21 3v6h-6"/></svg>
          </div>
          <h3>Still live, still updated</h3>
          <p class="card-text">
            The listing is open, the build is current and the last update shipped
            <strong>this month</strong>. Your edition is not a resurrection project, it is
            <strong>a new coat of paint on a running game</strong>.
          </p>
        </div>
      </div>
''' + CARDS_WHY + '''
    </div>
  </section>

  <!-- ===== The game ===== -->
  <section id="game" class="darker">
    <div class="shell">
      <div class="sec-head">
        <div class="reveal">
          <span class="sec-label">The Game</span>
          <h2>Ninety seconds. <span class="grad-gold">One thumb.</span></h2>
        </div>
        <p class="reveal d1">
          Two puppets, one ball, two goals and a clock. Power-ups, national teams, a cup to win and a league
          to climb. It reads instantly on any phone, in any market, at any age.
        </p>
      </div>

      <div class="grid-3">
        <div class="shot reveal" data-label="Puppet Soccer match">
          <img src="assets/soccer-4.jpg" alt="Puppet Soccer match with two puppet players and a power-up" />
        </div>
        <div class="shot reveal d1" data-label="The cast">
          <img src="assets/soccer-3.jpg" alt="The Puppet Soccer character line-up" />
        </div>
        <div class="shot reveal d2" data-label="Power-ups">
          <img src="assets/soccer-2.jpg" alt="Puppet Soccer match showing power-up icons above the pitch" />
        </div>
      </div>

      <div class="grid-4" style="margin-top: 26px;">
        <div class="glass-card reveal">
          <h3>One-thumb controls</h3>
          <p class="card-text">Move, jump, kick. Four buttons and no menu between opening the app and playing a match.</p>
        </div>
        <div class="glass-card reveal d1">
          <h3>Physics does the comedy</h3>
          <p class="card-text">The puppets are on strings and the ball is unpredictable. Every match produces a moment worth sending to a friend.</p>
        </div>
        <div class="glass-card reveal d2">
          <h3>Cup and league already built</h3>
          <p class="card-text">Group stages, knockouts, tables and a trophy are in the game today. Your competition drops straight into that structure.</p>
        </div>
        <div class="glass-card reveal d3">
          <h3>Real faces already supported</h3>
          <p class="card-text">The character head is a slot and the shipped game already runs recognisable footballer heads. Your squad goes in the same way, with your clearances.</p>
        </div>
      </div>

      <div class="grid-2" style="margin-top: 22px;">
        <div class="glass-card reveal">
          <div class="icon-badge pitch">
            <svg viewBox="0 0 24 24" fill="none" stroke="#2fd98b" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87M16 3.13A4 4 0 0 1 16 11"/></svg>
          </div>
          <h3>Four players, one device</h3>
          <p class="card-text">Local multiplayer for <strong>up to four people on a single phone or tablet</strong>, in the game today. No network, no accounts, no signal. It is why a fan zone, a concourse or a school hall works as an activation venue, and why an in-venue tournament needs nothing but the device already in someone's hand.</p>
        </div>
        <div class="glass-card reveal d1">
          <div class="icon-badge">
            <svg viewBox="0 0 24 24" fill="none" stroke="#00d2ff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.55a11 11 0 0 1 14.08 0M1.42 9a16 16 0 0 1 21.16 0M8.53 16.11a6 6 0 0 1 6.95 0"/><circle cx="12" cy="20" r="1"/></svg>
          </div>
          <h3>Online multiplayer is coming</h3>
          <p class="card-text">Online play is <strong>in build for the revival</strong>: ranked matches, leaderboards and season-long ladders against other fans wherever they are. A partner signing now <strong>launches with it</strong> rather than waiting for a later update.</p>
        </div>
      </div>

      <p class="note reveal">
        <strong>Puppet Soccer is one title in a franchise.</strong> The same core runs Puppet Ice Hockey and has
        shipped as field hockey, and it extends to basketball, handball, volleyball, futsal and floorball.
        If you hold rights in more than one sport, see the <a href="index.html" style="color: var(--gold); font-weight: 700;">full Puppet Sports offer</a>.
      </p>
    </div>
  </section>

  <!-- ===== Your brand ===== -->
  <section id="brand">
    <div class="shell">
      <div class="sec-head">
        <div class="reveal">
          <span class="sec-label">Where Your Brand Lives</span>
          <h2>Everything on this screen is <span class="grad-gold">a slot.</span></h2>
        </div>
        <p class="reveal d1">
          This is a live screenshot from Puppet Soccer as it ships today. Right now the boards say NOXGAMES.
          Every marked element is a surface that can carry your identity instead, without touching a line of
          gameplay code.
        </p>
      </div>

      <figure class="annotated reveal">
        <img src="assets/soccer-2.jpg" alt="Puppet Soccer match with the pitch, boards, crowd, trophy and team flags marked as branding surfaces" />
        <span class="hot" style="--x: 78%; --y: 65%; --d: 0s;">1</span>
        <span class="hot" style="--x: 50%; --y: 49%; --d: 0.4s;">2</span>
        <span class="hot" style="--x: 64%; --y: 70%; --d: 0.8s;">3</span>
        <span class="hot" style="--x: 47%; --y: 88%; --d: 1.2s;">4</span>
        <span class="hot" style="--x: 88%; --y: 33%; --d: 1.6s;">5</span>
        <span class="hot" style="--x: 12%; --y: 5%; --d: 2s;">6</span>
      </figure>

      <ol class="hot-legend reveal">
        <li>
          <h4>Pitch-side boards</h4>
          <p>They currently read NOXGAMES. In your edition they read whatever you want, in every second of every match.</p>
        </li>
        <li>
          <h4>The cup</h4>
          <p>The competition carries your name. Your trophy, your final, your winner screen, your celebration.</p>
        </li>
        <li>
          <h4>Kits and characters</h4>
          <p>Your colours, your crest, your squad. The puppet head is a slot and the game already ships real faces.</p>
        </li>
        <li>
          <h4>Teams and flags</h4>
          <p>Your league replaces the national teams. Your table, your fixtures, your derby week.</p>
        </li>
        <li>
          <h4>Crowd and stadium</h4>
          <p>Your ground as a playable venue, your colours in the stands, your chants on the audio track.</p>
        </li>
        <li>
          <h4>HUD and shop</h4>
          <p>Your mark in the frame of every screen, and your merch, codes or ticket drops inside the shop.</p>
        </li>
      </ol>

      <h3 style="margin: 60px 0 22px; font-size: 0.76rem; letter-spacing: 0.28em; text-transform: uppercase; color: var(--cyan);">What a club or league actually gets</h3>

      <div class="grid-4">
        <div class="glass-card reveal">
          <div class="icon-badge pitch">
            <svg viewBox="0 0 24 24" fill="none" stroke="#2fd98b" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M8 2v4M16 2v4M3 10h18M5 4h14a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2z"/></svg>
          </div>
          <h3>Matchday activation</h3>
          <p class="card-text">A derby-week event, a bracket on the big screen at half time, a prize weekend around a fixture. The game is the mechanic your matchday marketing has been missing.</p>
        </div>
        <div class="glass-card reveal d1">
          <div class="icon-badge gold">
            <svg viewBox="0 0 24 24" fill="none" stroke="#ffb938" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 1v22M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
          </div>
          <h3>New inventory to sell</h3>
          <p class="card-text">From Bundle 02 the in-game boards, events and rewards are <strong>yours to resell to your own sponsors</strong>, and you keep every cent of it. For some partners the edition pays for itself.</p>
        </div>
        <div class="glass-card reveal d2">
          <div class="icon-badge">
            <svg viewBox="0 0 24 24" fill="none" stroke="#00d2ff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87M16 3.13A4 4 0 0 1 16 11"/></svg>
          </div>
          <h3>The academy audience</h3>
          <p class="card-text">A brand-safe, no-chat, no-gambling game you can put in front of an academy, a school programme or a junior membership without a compliance conversation.</p>
        </div>
        <div class="glass-card reveal d3">
          <div class="icon-badge magenta">
            <svg viewBox="0 0 24 24" fill="none" stroke="#ff00ff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
          </div>
          <h3>Reach past the ground</h3>
          <p class="card-text">The fans who will never buy a ticket are the ones the game reaches. No language dependency means an overseas following engages exactly like the local one.</p>
        </div>
      </div>
    </div>
  </section>

''' + tail

SOCCER = SOCCER.replace(
    '<tr><th>Product</th><td>A branded edition of a <strong>Puppet Sports</strong> title. Built on the shipped, live codebase behind <strong>Puppet Soccer</strong> (10M+ installs, 4.3 stars) and <strong>Puppet Ice Hockey</strong> (5M+ installs, 4.8 stars), a franchise with <strong>42 million lifetime downloads</strong>.</td></tr>',
    '<tr><th>Product</th><td>A branded edition of <strong>Puppet Soccer</strong>, built on the shipped, live codebase behind the title as it stands on Google Play today: <strong>10M+ installs, 4.3 stars, 467K ratings</strong>, part of a franchise with <strong>42 million lifetime downloads</strong>.</td></tr>',
)
SOCCER = SOCCER.replace(
    '<tr><th>Sports available</th><td><strong>Soccer</strong> and <strong>ice hockey</strong> first. Field hockey already shipped as a reskin. Basketball, handball, volleyball, futsal and floorball are buildable on the same core; scope and timing agreed per sport.</td></tr>',
    '<tr><th>Other sports</th><td>The same core runs <strong>Puppet Ice Hockey</strong> and has shipped as field hockey. Basketball, handball, volleyball, futsal and floorball are buildable on it. A second sport can be added to any bundle for <strong>$15,000</strong>.</td></tr>',
)
SOCCER = SOCCER.replace(
    '''      <h2 class="reveal d1">Pick <span class="grad-gold">your sport.</span></h2>
      <p class="reveal d2">
        Your sport is <strong class="mins">30 minutes</strong> from reality. That is one call, long enough to pick the
        sport, the bundle and the launch window. You bring the crest. Forty-two million downloads' worth of goodwill
        is already sitting on our side of the table.
      </p>''',
    '''      <h2 class="reveal d1">Get <span class="grad-pitch">your kit on.</span></h2>
      <p class="reveal d2">
        Your club is <strong class="mins">30 minutes</strong> from being in a game. That is one call, long enough to
        pick the bundle and the launch window. You bring the crest. Ten million downloads' worth of goodwill is
        already sitting on our side of the table.
      </p>''',
)
SOCCER = SOCCER.replace(
    'mailto:studio@noxgames.com?subject=Puppet%20Sports%20Revival%20partnership',
    'mailto:studio@noxgames.com?subject=Puppet%20Soccer%20partnership',
)
SOCCER = SOCCER.replace(
    '<span>Puppet Sports Revival &middot; August 2026 &middot; Confidential &middot; Store figures from Google Play, 23 August 2026</span>',
    '<span>Puppet Soccer partnership &middot; August 2026 &middot; Confidential &middot; Store figures from Google Play, 23 August 2026</span>',
)

# ----------------------------------------------------------------- HOCKEY ---
HOCKEY = head(
    'Puppet Ice Hockey | Club, League &amp; Federation Partnership | NOXGAMES',
    'PUPPET ICE HOCKEY partnership page. Store figures verified on Google Play 23 Aug 2026:\n    5M+ installs, 4.8 stars, 99.9K ratings, last updated 7 Aug 2026.',
) + NAV + '''
  <!-- ===== Hero ===== -->
  <header class="hero" id="top">
    <span class="orb o1"></span>
    <span class="orb o2"></span>
    <span class="orb o3"></span>

    <div class="shell hero-grid">
      <div>
        <span class="eyebrow"><span class="dot"></span> NOXGAMES &middot; Puppet Ice Hockey &middot; Partnership Offer</span>
        <h1>
          Your jersey, on<br />
          <span class="grad-ice">five million phones.</span>
        </h1>
        <p class="hero-sub">
          Puppet Ice Hockey holds <b>4.8 stars from 99,900 ratings</b>, the highest score anything we have ever
          shipped, on <strong>5 million plus downloads</strong>. The national squads are already in it.
          We own the code, we are rebuilding it, and <strong>one hockey partner</strong> gets the jersey,
          the boards, the cup and the league.
        </p>
        <div class="hero-actions">
          <a href="#bundles" class="btn btn-neon">
            <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 1v22M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
            See the bundles
          </a>
          <a href="#brand" class="btn btn-ghost">
            <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12h20M12 2v20"/><circle cx="12" cy="12" r="9"/></svg>
            Where your brand lives
          </a>
        </div>
      </div>

      <div class="mock-wrap reveal">
        <div class="mock-chip c1">4.8 stars<small>From 99,900 ratings</small></div>
        <div class="mock-chip c2">5M+<small>Downloads on Google Play</small></div>
        <div class="mock-chip c3">1 partner<small>Hockey, category exclusive</small></div>
        <div class="mock-chip c4"><b>42M downloads</b><small>Across the Puppet Sports lineup</small></div>
        <div class="device">
          <img src="assets/hockey-8.jpg" style="object-position: center 62%;" alt="Puppet Ice Hockey match in progress with sponsor boards around the rink" />
        </div>
      </div>
    </div>

    <span class="scroll-hint">
      <svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M6 9l6 6 6-6"/></svg>
    </span>
  </header>

  <!-- ===== Stat strip ===== -->
  <div class="stat-strip">
    <div class="shell">
      <div class="stat-grid">
        <div class="stat">
          <div class="n grad-ice">4.8</div>
          <p>Store rating. The <b>highest score in the franchise</b>, and it is current.</p>
        </div>
        <div class="stat">
          <div class="n grad-text">5M+</div>
          <p>Downloads on <b>Google Play alone</b>, before the other stores.</p>
        </div>
        <div class="stat">
          <div class="n grad-gold">99.9K</div>
          <p>Player ratings. The title was <b>last updated this month</b>.</p>
        </div>
        <div class="stat">
          <div class="n grad-pitch">1</div>
          <p>Hockey partner. <b>Category exclusive</b>, for the length of the deal.</p>
        </div>
      </div>
    </div>
  </div>

  <!-- ===== Legacy ===== -->
  <section id="legacy">
    <div class="shell">
      <div class="sec-head">
        <div class="reveal">
          <span class="sec-label">The Legacy</span>
          <h2>Hockey fans rated it <span class="grad-ice">4.8.</span></h2>
        </div>
        <p class="reveal d1">
          Nearly a hundred thousand people rated Puppet Ice Hockey and the average never dropped below 4.8.
          That is not a nostalgic memory of a game, it is a live listing with a score most publishers would
          spend a marketing budget to buy.
        </p>
      </div>

      <div class="grid-3">
        <div class="glass-card reveal">
          <div class="icon-badge">
            <svg viewBox="0 0 24 24" fill="none" stroke="#00d2ff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2l3 6.9 7.5.8-5.6 5 1.6 7.3L12 18l-6.5 4 1.6-7.3-5.6-5 7.5-.8z"/></svg>
          </div>
          <h3>The rating is the story</h3>
          <p class="card-text">
            <strong>4.8 stars from 99,900 ratings</strong> on <strong>5 million plus installs</strong>.
            Across the whole Puppet Sports franchise, <strong>42 million downloads</strong>.
            Hockey audiences are small and loud, and this one liked the game.
          </p>
        </div>
        <div class="glass-card reveal d1">
          <div class="icon-badge ice" style="background: rgba(127,227,255,0.1); border-color: rgba(127,227,255,0.35);">
            <svg viewBox="0 0 24 24" fill="none" stroke="#7fe3ff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 21V5a2 2 0 0 1 2-2h8l-1 3 1 3H6"/><path d="M4 21h6"/></svg>
          </div>
          <h3>The nations are already in</h3>
          <p class="card-text">
            Czechia, Sweden, Finland, Canada, the United States, Norway, Slovakia, Denmark, France and Italy
            already play in the shipped game, with squads, flags and a tournament ladder.
            <strong>A federation is looking at a slot that already exists.</strong>
          </p>
        </div>
        <div class="glass-card reveal d2">
          <div class="icon-badge pitch">
            <svg viewBox="0 0 24 24" fill="none" stroke="#2fd98b" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12a9 9 0 1 1-9-9"/><path d="M21 3v6h-6"/></svg>
          </div>
          <h3>Still live, still updated</h3>
          <p class="card-text">
            The listing is open, the build is current and the last update shipped
            <strong>this month</strong>. Your edition is not a resurrection project, it is
            <strong>a new coat of paint on a running game</strong>.
          </p>
        </div>
      </div>
''' + CARDS_WHY + '''
    </div>
  </section>

  <!-- ===== The game ===== -->
  <section id="game" class="darker">
    <div class="shell">
      <div class="sec-head">
        <div class="reveal">
          <span class="sec-label">The Game</span>
          <h2>Faceoff. Body check. <span class="grad-ice">Goal.</span></h2>
        </div>
        <p class="reveal d1">
          Two puppets on skates, a puck, two nets and a clock. Goalie duels, power-ups, national squads and a
          tournament ladder. It reads instantly on any phone, in any market, at any age.
        </p>
      </div>

      <div class="grid-3">
        <div class="shot reveal" data-label="Rink match">
          <img src="assets/hockey-1.jpg" alt="Puppet Ice Hockey match with two puppet players and sponsor boards" />
        </div>
        <div class="shot reveal d1" data-label="National squads">
          <img src="assets/hockey-3.jpg" alt="Puppet Ice Hockey squad selection showing national teams and player stats" />
        </div>
        <div class="shot reveal d2" data-label="Top-down mode">
          <img src="assets/hockey-6.jpg" alt="Puppet Ice Hockey top-down four-player rink mode" />
        </div>
      </div>

      <div class="grid-4" style="margin-top: 26px;">
        <div class="glass-card reveal">
          <h3>One-thumb controls</h3>
          <p class="card-text">Skate, jump, shoot. Four buttons and no menu between opening the app and dropping the puck.</p>
        </div>
        <div class="glass-card reveal d1">
          <h3>Checks and keeper duels</h3>
          <p class="card-text">Body checks, deflections and a goalie who can be beaten. The physics produce the highlight, not a scripted animation.</p>
        </div>
        <div class="glass-card reveal d2">
          <h3>Squads and stats built in</h3>
          <p class="card-text">Named players with upgradeable shot, speed and jump ratings, grouped into national teams. Your roster drops into that structure.</p>
        </div>
        <div class="glass-card reveal d3">
          <h3>Two ways to play a rink</h3>
          <p class="card-text">The side-on duel and a top-down full-rink mode ship in the same build, so a branded edition gets two match formats for free.</p>
        </div>
      </div>

      <div class="grid-2" style="margin-top: 22px;">
        <div class="glass-card reveal">
          <div class="icon-badge pitch">
            <svg viewBox="0 0 24 24" fill="none" stroke="#2fd98b" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87M16 3.13A4 4 0 0 1 16 11"/></svg>
          </div>
          <h3>Four players, one device</h3>
          <p class="card-text">Local multiplayer for <strong>up to four people on a single phone or tablet</strong>, in the game today. No network, no accounts, no signal. It is why a fan zone, a concourse or a school hall works as an activation venue, and why an in-venue tournament needs nothing but the device already in someone's hand.</p>
        </div>
        <div class="glass-card reveal d1">
          <div class="icon-badge">
            <svg viewBox="0 0 24 24" fill="none" stroke="#00d2ff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.55a11 11 0 0 1 14.08 0M1.42 9a16 16 0 0 1 21.16 0M8.53 16.11a6 6 0 0 1 6.95 0"/><circle cx="12" cy="20" r="1"/></svg>
          </div>
          <h3>Online multiplayer is coming</h3>
          <p class="card-text">Online play is <strong>in build for the revival</strong>: ranked matches, leaderboards and season-long ladders against other fans wherever they are. A partner signing now <strong>launches with it</strong> rather than waiting for a later update.</p>
        </div>
      </div>

      <p class="note reveal">
        <strong>Puppet Ice Hockey is one title in a franchise.</strong> The same core runs Puppet Soccer and has
        shipped as field hockey, and it extends to floorball, basketball, handball and volleyball.
        If you hold rights in more than one sport, see the <a href="index.html" style="color: var(--gold); font-weight: 700;">full Puppet Sports offer</a>.
      </p>
    </div>
  </section>

  <!-- ===== Your brand ===== -->
  <section id="brand">
    <div class="shell">
      <div class="sec-head">
        <div class="reveal">
          <span class="sec-label">Where Your Brand Lives</span>
          <h2>Everything on this screen is <span class="grad-gold">a slot.</span></h2>
        </div>
        <p class="reveal d1">
          This is a live screenshot from Puppet Ice Hockey as it ships today. Right now the boards say
          NOXGAMES. Every marked element is a surface that can carry your identity instead, without touching
          a line of gameplay code.
        </p>
      </div>

      <figure class="annotated reveal">
        <img src="assets/hockey-8.jpg" alt="Puppet Ice Hockey match with the rink boards, jerseys, puck, crowd and ice marked as branding surfaces" />
        <span class="hot" style="--x: 17%; --y: 77%; --d: 0s;">1</span>
        <span class="hot" style="--x: 59%; --y: 72%; --d: 0.4s;">2</span>
        <span class="hot" style="--x: 40%; --y: 71%; --d: 0.8s;">3</span>
        <span class="hot" style="--x: 50%; --y: 38%; --d: 1.2s;">4</span>
        <span class="hot" style="--x: 30%; --y: 90%; --d: 1.6s;">5</span>
        <span class="hot" style="--x: 88%; --y: 8%; --d: 2s;">6</span>
      </figure>

      <ol class="hot-legend reveal">
        <li>
          <h4>Rink boards</h4>
          <p>They currently read NOXGAMES, all the way around the rink. In your edition they read whatever you want, in every second of every match.</p>
        </li>
        <li>
          <h4>Jerseys and helmets</h4>
          <p>Your colours, your crest, your squad. The puppet head is a slot and the game already ships recognisable faces.</p>
        </li>
        <li>
          <h4>Puck and equipment</h4>
          <p>Puck, stick, gloves and pads in your identity. Small surfaces the player stares at for the whole match.</p>
        </li>
        <li>
          <h4>Crowd and arena</h4>
          <p>Your arena as a playable venue, your colours in the stands, your goal horn on the audio track.</p>
        </li>
        <li>
          <h4>The ice itself</h4>
          <p>Centre ice, the zones and the crease. The most valuable painted surface in real hockey, and here it costs nothing to print.</p>
        </li>
        <li>
          <h4>HUD and shop</h4>
          <p>Your mark in the frame of every screen, and your merch, codes or ticket drops inside the shop.</p>
        </li>
      </ol>

      <h3 style="margin: 60px 0 22px; font-size: 0.76rem; letter-spacing: 0.28em; text-transform: uppercase; color: var(--cyan);">What a club, league or federation gets</h3>

      <div class="grid-4">
        <div class="glass-card reveal">
          <div class="icon-badge" style="background: rgba(127,227,255,0.1); border-color: rgba(127,227,255,0.35);">
            <svg viewBox="0 0 24 24" fill="none" stroke="#7fe3ff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M8 2v4M16 2v4M3 10h18M5 4h14a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2z"/></svg>
          </div>
          <h3>The season has intermissions</h3>
          <p class="card-text">Two twenty-minute breaks, every home game, with a crowd holding phones. An in-arena bracket or a period-break tournament is the most obvious activation in the sport.</p>
        </div>
        <div class="glass-card reveal d1">
          <div class="icon-badge gold">
            <svg viewBox="0 0 24 24" fill="none" stroke="#ffb938" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 1v22M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
          </div>
          <h3>New inventory to sell</h3>
          <p class="card-text">From Bundle 02 the in-game boards, events and rewards are <strong>yours to resell to your own sponsors</strong>, and you keep every cent of it. For some partners the edition pays for itself.</p>
        </div>
        <div class="glass-card reveal d2">
          <div class="icon-badge pitch">
            <svg viewBox="0 0 24 24" fill="none" stroke="#2fd98b" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87M16 3.13A4 4 0 0 1 16 11"/></svg>
          </div>
          <h3>A recruitment tool</h3>
          <p class="card-text">Federations spend real money getting children onto skates. A brand-safe, no-chat, no-gambling hockey game is the cheapest first touch you will ever buy.</p>
        </div>
        <div class="glass-card reveal d3">
          <div class="icon-badge magenta">
            <svg viewBox="0 0 24 24" fill="none" stroke="#ff00ff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
          </div>
          <h3>Tournament season</h3>
          <p class="card-text">World championships, junior tournaments and playoff runs already drive the calendar. The game gives you something to run alongside them that lasts after the final whistle.</p>
        </div>
      </div>
    </div>
  </section>

''' + tail

HOCKEY = HOCKEY.replace(
    '<tr><th>Product</th><td>A branded edition of a <strong>Puppet Sports</strong> title. Built on the shipped, live codebase behind <strong>Puppet Soccer</strong> (10M+ installs, 4.3 stars) and <strong>Puppet Ice Hockey</strong> (5M+ installs, 4.8 stars), a franchise with <strong>42 million lifetime downloads</strong>.</td></tr>',
    '<tr><th>Product</th><td>A branded edition of <strong>Puppet Ice Hockey: Pond Head</strong>, built on the shipped, live codebase behind the title as it stands on Google Play today: <strong>5M+ installs, 4.8 stars, 99.9K ratings</strong>, part of a franchise with <strong>42 million lifetime downloads</strong>.</td></tr>',
)
HOCKEY = HOCKEY.replace(
    '<tr><th>Sports available</th><td><strong>Soccer</strong> and <strong>ice hockey</strong> first. Field hockey already shipped as a reskin. Basketball, handball, volleyball, futsal and floorball are buildable on the same core; scope and timing agreed per sport.</td></tr>',
    '<tr><th>Other sports</th><td>The same core runs <strong>Puppet Soccer</strong> and has shipped as field hockey. Floorball, basketball, handball and volleyball are buildable on it. A second sport can be added to any bundle for <strong>$15,000</strong>.</td></tr>',
)
HOCKEY = HOCKEY.replace(
    '''      <h2 class="reveal d1">Pick <span class="grad-gold">your sport.</span></h2>
      <p class="reveal d2">
        Your sport is <strong class="mins">30 minutes</strong> from reality. That is one call, long enough to pick the
        sport, the bundle and the launch window. You bring the crest. Forty-two million downloads' worth of goodwill
        is already sitting on our side of the table.
      </p>''',
    '''      <h2 class="reveal d1">Drop <span class="grad-ice">the puck.</span></h2>
      <p class="reveal d2">
        Your club is <strong class="mins">30 minutes</strong> from being in a game. That is one call, long enough to
        pick the bundle and the launch window. You bring the crest. A 4.8 star rating and five million downloads are
        already sitting on our side of the table.
      </p>''',
)
HOCKEY = HOCKEY.replace(
    'mailto:studio@noxgames.com?subject=Puppet%20Sports%20Revival%20partnership',
    'mailto:studio@noxgames.com?subject=Puppet%20Ice%20Hockey%20partnership',
)
HOCKEY = HOCKEY.replace(
    'href="https://play.google.com/store/apps/details?id=air.com.noxgames.PuppetSoccer2014" target="_blank" rel="noopener">Play it yourself</a>',
    'href="https://play.google.com/store/apps/details?id=air.com.noxgames.PuppetHockey" target="_blank" rel="noopener">Play it yourself</a>',
)
HOCKEY = HOCKEY.replace(
    '<span>Puppet Sports Revival &middot; August 2026 &middot; Confidential &middot; Store figures from Google Play, 23 August 2026</span>',
    '<span>Puppet Ice Hockey partnership &middot; August 2026 &middot; Confidential &middot; Store figures from Google Play, 23 August 2026</span>',
)

(PUB / 'soccer.html').write_text(SOCCER)
(PUB / 'hockey.html').write_text(HOCKEY)
print('soccer.html', len(SOCCER), 'bytes')
print('hockey.html', len(HOCKEY), 'bytes')

# sanity: no leftover core-only strings
for name, doc in (('soccer', SOCCER), ('hockey', HOCKEY)):
    for bad in ('Pick <span class="grad-gold">your sport.</span>',
                '<tr><th>Sports available</th>'):
        if bad in doc:
            print('WARNING leftover in', name, ':', bad[:50])
    for need in ('$20,000', '$60,000', '$120,000', '$250,000', '$150,000', '$300,000', 'Your own sponsors', 'Monetised edition', 'Clean edition'):
        if need not in doc:
            print('WARNING missing in', name, ':', need)
print('checks done')
