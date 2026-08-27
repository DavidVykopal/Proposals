#!/usr/bin/env python3
"""Generate flat-vector placeholder tiles for the 'any sport' strip.

These stand in until Jiri's real GIFs land. The pages reference the .gif first and
fall back to these .svg files, so dropping the GIFs in needs no code change.
"""
import pathlib

OUT = pathlib.Path(__file__).resolve().parent.parent / 'public' / 'assets'
W, H = 480, 360
BOARD_Y = 200          # sponsor board strip
GROUND_Y = 226         # grass / floor starts
STAND = 334            # where a puppet's boots meet the ground


def puppet(x, base, kit, flip=False, skin='#f6cfa8', hair='#3b2a1c', head_r=27, shadow=True):
    """One big-headed puppet on a string, boots at `base`."""
    d = -1 if flip else 1
    boot_y = base - 6
    torso_y = boot_y - 34
    head_y = torso_y - head_r - 4
    sh = (f'<ellipse cx="{x}" cy="{boot_y + 8}" rx="{head_r + 5}" ry="5" fill="#000000" opacity="0.3"/>'
          if shadow else '')
    return f'''
  <g>
    <line x1="{x}" y1="0" x2="{x}" y2="{head_y - head_r + 4}" stroke="#ffffff" stroke-opacity="0.16" stroke-width="2"/>
    {sh}
    <rect x="{x - 15}" y="{torso_y}" width="30" height="36" rx="12" fill="{kit}"/>
    <rect x="{x - 13}" y="{boot_y - 8}" width="10" height="13" rx="4" fill="#20303f"/>
    <rect x="{x + 3}" y="{boot_y - 8}" width="10" height="13" rx="4" fill="#20303f"/>
    <circle cx="{x}" cy="{head_y}" r="{head_r}" fill="{skin}"/>
    <path d="M {x - head_r} {head_y - 3} a {head_r} {head_r} 0 0 1 {head_r * 2} 0 z" fill="{hair}"/>
    <circle cx="{x - 9 * d}" cy="{head_y + 4}" r="3.3" fill="#26303a"/>
    <circle cx="{x + 7 * d}" cy="{head_y + 4}" r="3.3" fill="#26303a"/>
    <path d="M {x - 8 * d} {head_y + 15} q {8 * d} 7 {16 * d} 0" stroke="#26303a" stroke-width="2.6"
          fill="none" stroke-linecap="round"/>
  </g>'''


def frame(sport, sky_top, sky_bottom, ground, accent, back='', front=''):
    """back = drawn behind the ground band, front = drawn on top of everything."""
    pill_w = len(sport) * 9 + 26
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 62 {W} 298" width="{W}" height="298" role="img" aria-label="{sport} on the Puppet Sports core">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{sky_top}"/>
      <stop offset="1" stop-color="{sky_bottom}"/>
    </linearGradient>
    <linearGradient id="grd" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{ground}"/>
      <stop offset="1" stop-color="{ground}" stop-opacity="0.7"/>
    </linearGradient>
  </defs>
  <rect width="{W}" height="{H}" fill="url(#sky)"/>
  <circle cx="80" cy="60" r="130" fill="{accent}" opacity="0.10"/>
  <circle cx="410" cy="180" r="120" fill="{accent}" opacity="0.07"/>
{back}
  <g>
    <rect x="0" y="{BOARD_Y}" width="{W}" height="26" fill="#0a1f33"/>
    <rect x="0" y="{BOARD_Y}" width="{W}" height="2" fill="#ffffff" opacity="0.16"/>
    <rect x="24" y="{BOARD_Y + 6}" width="112" height="15" rx="3" fill="#ffffff" opacity="0.14"/>
    <rect x="148" y="{BOARD_Y + 6}" width="184" height="15" rx="3" fill="#ffb938"/>
    <text x="240" y="{BOARD_Y + 17}" text-anchor="middle" font-family="Verdana, Geneva, sans-serif"
          font-size="9" font-weight="bold" letter-spacing="1.8" fill="#241500">YOUR BRAND</text>
    <rect x="344" y="{BOARD_Y + 6}" width="112" height="15" rx="3" fill="#ffffff" opacity="0.14"/>
  </g>
  <rect x="0" y="{GROUND_Y}" width="{W}" height="{H - GROUND_Y}" fill="url(#grd)"/>
{front}
  <rect x="18" y="76" width="{pill_w}" height="28" rx="14" fill="#000000" opacity="0.5"/>
  <text x="{18 + pill_w / 2}" y="95" text-anchor="middle" font-family="Verdana, Geneva, sans-serif"
        font-size="12" font-weight="bold" letter-spacing="2" fill="{accent}">{sport}</text>
</svg>
'''


# ---------------------------------------------------------------- floorball --
floorball = frame(
    'FLOORBALL', '#16314f', '#081a2d', '#b9793a', '#7fe3ff',
    back=f'''
  <g stroke="#e9eef4" stroke-width="4" fill="none" opacity="0.85">
    <path d="M 20 {GROUND_Y + 6} h 46 v 58 h -46"/>
    <path d="M 460 {GROUND_Y + 6} h -46 v 58 h 46"/>
  </g>''',
    front=puppet(146, STAND, '#7fe3ff') + puppet(334, STAND, '#ff6b6b', flip=True) + f'''
  <path d="M 174 {STAND - 44} l 40 32 l -15 8 l -36 -30 z" fill="#e9eef4"/>
  <path d="M 306 {STAND - 44} l -40 32 l 15 8 l 36 -30 z" fill="#e9eef4"/>
  <circle cx="240" cy="{STAND - 12}" r="11" fill="#f7f9fb"/>
  <circle cx="236" cy="{STAND - 16}" r="1.9" fill="#a2652f"/>
  <circle cx="244" cy="{STAND - 9}" r="1.9" fill="#a2652f"/>
  <circle cx="242" cy="{STAND - 18}" r="1.7" fill="#a2652f"/>''')

# ----------------------------------------------------------------- football --
football = frame(
    'FOOTBALL', '#0d3a63', '#06203a', '#2fa85f', '#2fd98b',
    back='',
    front=f'''
  <g stroke="#eef4fa" stroke-width="4" fill="none" opacity="0.9">
    <path d="M 18 {STAND - 4} v -66 h 50 v 66"/>
    <path d="M 462 {STAND - 4} v -66 h -50 v 66"/>
  </g>''' + puppet(150, STAND, '#2fd98b') + puppet(330, STAND, '#ffb938', flip=True) + f'''
  <path d="M 192 {STAND - 46} q 30 -30 50 -22" stroke="#ffffff" stroke-opacity="0.4"
        stroke-width="4" fill="none" stroke-linecap="round"/>
  <circle cx="248" cy="{STAND - 72}" r="16" fill="#f7f9fb"/>
  <path d="M 248 {STAND - 83} l 9 6.5 l -3.5 10.5 h -11 l -3.5 -10.5 z" fill="#1d2b38"/>''')

# ---------------------------------------------------------------- quidditch --
quidditch = frame(
    'QUIDDITCH', '#3d2265', '#150b26', '#35704a', '#c9a3ff',
    back=f'''
  <g stroke="#ffb938" stroke-width="6" fill="none" opacity="0.7">
    <circle cx="58" cy="96" r="28"/><path d="M 58 124 v {GROUND_Y - 116}"/>
    <circle cx="424" cy="72" r="23"/><path d="M 424 95 v {GROUND_Y - 87}"/>
  </g>''',
    front=f'''
  <ellipse cx="150" cy="{STAND - 6}" rx="34" ry="6" fill="#000000" opacity="0.22"/>
  <ellipse cx="330" cy="{STAND - 6}" rx="30" ry="5" fill="#000000" opacity="0.18"/>
  <path d="M 104 200 l 96 -18" stroke="#8a5a2b" stroke-width="8" stroke-linecap="round"/>
  <path d="M 100 201 l -20 10 l 24 0 l -16 10 l 22 -4" stroke="#d8a24a" stroke-width="4"
        fill="none" stroke-linecap="round"/>
  <path d="M 284 166 l 96 -18" stroke="#8a5a2b" stroke-width="8" stroke-linecap="round"/>
  <path d="M 384 145 l 20 10 l -24 0 l 16 10 l -22 -4" stroke="#d8a24a" stroke-width="4"
        fill="none" stroke-linecap="round"/>
''' + puppet(150, 196, '#ffb938', shadow=False)
        + puppet(330, 162, '#c9a3ff', flip=True, shadow=False) + '''
  <g>
    <circle cx="243" cy="118" r="11" fill="#ffd066"/>
    <path d="M 232 118 q -24 -18 -33 -2 q 15 11 33 2 z" fill="#ffe9b0" opacity="0.95"/>
    <path d="M 254 118 q 24 -18 33 -2 q -15 11 -33 2 z" fill="#ffe9b0" opacity="0.95"/>
  </g>''')

# --------------------------------------------------------------- horse polo --
polo = frame(
    'HORSE POLO', '#154064', '#07203a', '#3f8f4f', '#ffb938',
    back='',
    front=f'''
  <g fill="#7a4a24">
    <ellipse cx="152" cy="{STAND + 4}" rx="62" ry="7" fill="#000000" opacity="0.28"/>
    <rect x="106" y="{STAND - 54}" width="92" height="34" rx="16"/>
    <rect x="184" y="{STAND - 78}" width="22" height="32" rx="10"/>
    <rect x="116" y="{STAND - 24}" width="10" height="24" rx="5"/>
    <rect x="178" y="{STAND - 24}" width="10" height="24" rx="5"/>
    <path d="M 106 {STAND - 52} q -20 8 -22 28 q 14 -10 22 -14 z"/>
  </g>
  <g fill="#5e3418">
    <ellipse cx="328" cy="{STAND + 4}" rx="62" ry="7" fill="#000000" opacity="0.28"/>
    <rect x="282" y="{STAND - 54}" width="92" height="34" rx="16"/>
    <rect x="274" y="{STAND - 78}" width="22" height="32" rx="10"/>
    <rect x="292" y="{STAND - 24}" width="10" height="24" rx="5"/>
    <rect x="354" y="{STAND - 24}" width="10" height="24" rx="5"/>
    <path d="M 374 {STAND - 52} q 20 8 22 28 q -14 -10 -22 -14 z"/>
  </g>''' + puppet(148, STAND - 56, '#ffb938', shadow=False)
        + puppet(332, STAND - 56, '#ff6b6b', flip=True, shadow=False) + f'''
  <path d="M 174 {STAND - 96} l 46 76" stroke="#d9b489" stroke-width="5" stroke-linecap="round"/>
  <rect x="215" y="{STAND - 26}" width="17" height="8" rx="3" fill="#8a5a2b"/>
  <path d="M 306 {STAND - 96} l -46 76" stroke="#d9b489" stroke-width="5" stroke-linecap="round"/>
  <rect x="248" y="{STAND - 26}" width="17" height="8" rx="3" fill="#8a5a2b"/>
  <circle cx="240" cy="{STAND - 4}" r="9" fill="#f7f9fb"/>''')

for name, doc in (('floorball', floorball), ('football', football),
                  ('quidditch', quidditch), ('polo', polo)):
    (OUT / f'sport-{name}.svg').write_text(doc)
    print(f'sport-{name}.svg  {len(doc)} bytes')
