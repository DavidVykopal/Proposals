# Puppet Sports Revival — partnership offer pages

Static pages served from a Cloudflare Worker. Audience: brands, clubs, leagues and
sport associations we want as licensing / sponsorship partners for the Puppet Sports revival.

## Pages

| File | Purpose | Send to |
| --- | --- | --- |
| `public/index.html` | **Core offer.** Franchise, whole lineup, all four bundles. | Anyone, first contact |
| `public/soccer.html` | Soccer-only cut of the offer | Football clubs, leagues, federations, football brands |
| `public/hockey.html` | Ice hockey-only cut of the offer | Hockey clubs, leagues, federations, winter-sport brands |

The two sport pages are forks of the core page: same CSS system, same bundles, sport-specific
copy, screenshots and examples. When the commercials change, change all three.

## Commands

```bash
npm run cf:deploy     # deploy to production
npm run cf:preview    # local wrangler dev (start it yourself, do not leave it running)
```

Worker name: `puppet-sports-revival`. Account: NOXGAMES (`0b01374e269cd80008534b2efebe3c58`).

## Numbers on the pages — where they came from

Verified from Google Play on **23 Aug 2026**:

| Title | Package | Installs | Rating | Ratings | Last update |
| --- | --- | --- | --- | --- | --- |
| Puppet Soccer - Football | `air.com.noxgames.PuppetSoccer2014` | 10M+ | 4.3 | 467K | 7 Aug 2026 |
| Puppet Ice Hockey: Pond Head | `air.com.noxgames.PuppetHockey` | 5M+ | 4.8 | 99.9K | 7 Aug 2026 |

Combined ratings figure used on the pages: **567K**.

**Franchise total: 42M downloads across the lineup**, all titles, all stores, lifetime. This is
Jiri's figure, given 24 Aug 2026, and it replaced the earlier unverified "100M+" everywhere on the
three pages. It is the headline claim, so if a partner's analyst asks for the source we should have
it ready (old Play Console exports, App Annie / Sensor Tower history).

## Prices on the pages

Two commercial approaches, chosen by the partner at Bundle 03 and above:

- **Approach A, monetised edition** — the game keeps its ads and in-app purchases, NOXGAMES
  operates it, and **50% of net revenue goes to the partner, settled quarterly**, from month one
  and for the whole term. No recoup ladder, no phases, no cap. It is deliberately **not** sold as a
  payback plan; the pages say out loud that most partners will not recover the full fee from it.
- **Approach B, clean edition** — no ads, no in-app purchases, higher fee, no revenue for either
  side. For federations, associations and anything aimed at children.

Bundles 01 and 02 sit inside our existing live titles, which are monetised, so they are
monetised-only: no revenue share and no clean option at those tiers.

| Bundle | Monetised (A) | Clean (B) | Production | Included window |
| --- | --- | --- | --- | --- |
| 01 Sponsor Drop | $20,000 | n/a | 4 weeks | 3 months |
| 02 Branded Team | $60,000 | n/a | 8 weeks | 12 months |
| 03 Licensed Edition | $120,000 | $150,000 | 12 weeks | 12 months operated |
| 04 Franchise Partner | $250,000 | $300,000 | 16 to 20 weeks | 24 months operated |

**Multiplayer** is on all three pages: local multiplayer for up to four players on one device
ships today, online multiplayer is in build for the revival and partners signing now launch with it.

**Scarcity caps, set by Jiri:** a game carries a maximum of **8 sponsor slots** (the boards rotate
through roughly 5 creatives during play, text or image) and a maximum of **4 branded teams**. The
cap is a selling point, not a limitation: it is what stops a Sponsor Drop being one logo among forty.

**Publishing under the partner's own developer accounts is an add-on at $6,000**, not included.
It is materially more work on our side. By default everything ships under NOXGAMES accounts.

Add-ons $2K to $18K, listed on the page. Payment 50% signing / 50% launch.
Season extension after the included window: **$18,000** per 12 months per title on a monetised
edition, **$24,000** on a clean one (nothing offsets the running cost there).

All USD, excluding VAT. **Change these in `public/index.html` and rerun `gen_sport_pages.py`** so
all three pages stay identical.

## Assets

`public/assets/`

| File | Source |
| --- | --- |
| `soccer-1..4.jpg` | Google Play store screenshots, Puppet Soccer, pulled at 1600x900 |
| `hockey-1..8.jpg` | Google Play store screenshots, Puppet Ice Hockey, 1280x720 |
| `icon-soccer.png`, `icon-hockey.png` | Play store app icons, 512x512 |
| `noxgames-logo.png` | copied from `../CPI_Tests/assets` |
| `sport-{floorball,football,quidditch,polo}.gif` | Jiri's SnapCast gameplay captures (20 Jul 2026), re-encoded to 10 s / 640x360 / 10 fps / 128 colors with ffmpeg (2.2 to 3.6 MB each, originals ~19-32 MB). `sport-football.gif` shows American football, `sport-quidditch.gif` shows Quadball — page labels match the build's watermarks, filenames kept for the svg fallback pairing |
| `meowcup-1..4.jpg` | **MISSING — drop the four MeowCup Field Hockey creatives here** |

Until those files exist, the tiles render as labelled placeholder panels (dark diagonal-stripe
tiles naming the missing file). The pages do not break. Filenames must match exactly.

### The "any sport" strip in the CTA

Each tile loads `assets/sport-<name>.gif` and, if that 404s, falls back to
`assets/sport-<name>.svg`. **The real gameplay GIFs are in place since 28 Aug 2026** (see the
assets table); the SVGs stay as fallbacks only. The strip is a 2x2 grid of 16:9 tiles, lazy-loaded,
so the ~12 MB of GIFs only download when a visitor scrolls to the CTA.

The `.svg` files are flat-vector placeholders generated by `tools/make_sport_placeholders.py`.
They are deliberately illustrations, not fake gameplay: two puppets, the right surface and
equipment, and a sponsor board reading YOUR BRAND, so even the placeholder sells the boards story.
Regenerate or add a sport with:

```bash
python3 tools/make_sport_placeholders.py
```

To add another sport, copy one of the four blocks in that script and add a tile to the
`.sports-strip` in `public/index.html`, then rerun `gen_sport_pages.py`.

## Things to check before sending to a partner

1. **Player likenesses.** The Puppet Soccer screenshots we use show puppet heads modelled on
   recognisable real footballers. They are the live store screenshots so they are already public,
   but do not caption them with player names, and do not promise real-player likenesses to a
   partner without their own clearances. The term sheet says this explicitly.
2. **Contact address.** Pages use `studio@noxgames.com`. This is gaming business, so that is correct.
3. **The 42M figure.** See above, and have the source ready.
4. Swap the CTA and the footer line if the page is going to a named partner rather than being
   used as a cold-outreach link.

## Making a new per-sport page

Copy `soccer.html`, then change: `<title>`, hero copy, the sport-specific sections, the screenshots,
the store link and the footer. Everything below "Bundles" is identical across the three pages
on purpose, so a partner comparing two of our pages sees the same commercial terms.
