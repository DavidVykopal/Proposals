# Email reply to Patrick: phased budget and timeline

**Draft:** 30 July 2026 (v3, prototype at 2–3 weeks, mobile framing)
**Re:** Rise of a Nation, request for budget and timeline per phase

---

**Subject:** Rise of a Nation: time and budget by phase

Hi Patrick,

Thanks for coming back so quickly. Your three-phase split is the right frame, and it maps closely onto how we would actually run the project. Numbers against each one below, on the basis of the bespoke nation builder route you have selected.

**Phase 1: Playable prototype**

Time: 2 to 3 weeks from signature. The technical setup and the discovery we need run in the first few days, alongside the start of the build.

Budget: USD 40,000, fixed.

What you get: a build installed on a phone, not a deck. The visual direction, one full build-and-balance loop, the district-to-nation fantasy, one national mission, and a first working version of the persistent city dashboard.

The most valuable thing this phase settles is performance. The multi-city dashboard you have asked for is demanding on a phone, and we want to prove it holds up on mid-range Android hardware before either of us commits to a full build. We would rather find that in week two than in month four, and it is the main reason to get something in your hands this quickly.

Payment: prepayment against the preliminary agreement, credited in full against the total project price.

**Phase 2: First complete game, India launch**

Time: production starts in October 2026 and runs to a release at the end of Q1 2027. That is roughly four and a half to five and a half months of full production with a reserved team.

Budget: USD 550,000 to 600,000 for the product, inclusive of the Phase 1 prototype. Net of Phase 1, that is USD 510,000 to 560,000.

I want to be straight with you about why that sits at the top of the range we quoted rather than in the middle. The bespoke route builds the core systems, the interface and the platform engineering from the ground up instead of adapting an existing engine, and that was always the more expensive of the two options. Compressing the schedule on top of that is achieved by running more work in parallel, not by cutting scope, so it holds the cost at the upper end rather than reducing it. What you get for it is the product that matches your original vision: persistent city and state management with the dashboard depth the other route would have had to simplify or push into a metagame.

Payment: USD 100,000 on signature of the development contract, which reserves the team, and the balance across delivery milestones.

We remain willing to commit to a concrete release date in that contract and to accept a price reduction if we miss it, in the region of 10 to 20 percent. Given the compressed schedule, the contract needs to be precise about the measurement milestone, the grace period, written change control for added scope, and exclusions where client inputs or approvals arrive late. Those are the normal terms, and on this timeline they matter more than usual.

**Phase 3: Global launch readiness**

Time: approximately two and a half months, with the first part running in parallel with the tail of Phase 2, followed by a soft-launch window. Global launch in early Q3 2027 on that basis.

Budget: indicative USD 120,000 to 180,000 on top of Phase 2. This is the least defined of the three, because it scales almost entirely with how many languages and territories you want.

Scope: additional languages and localisation QA, per-territory store submission and compliance work covering child safety, privacy and data handling, backend hardening and load testing, device validation across the range of hardware your audience actually uses, live-operations tooling and a content pipeline, economy and retention tuning against real soft-launch data, and an agreed post-launch support period.

The accelerated schedule pays off here specifically. An India release at the end of Q1 2027 gives us close to five months of live data and tuning before 15 August 2027, and it puts global launch in the anniversary window itself rather than after it. On the original timing we would have been arriving late to your own campaign moment. This version does not.

**Where the numbers still move**

With the route settled, three things drive the remaining spread, and settling them early is exactly the friction saver you are describing:

1. Languages and territories for Phase 3. This is the single biggest lever on that phase.
2. Whether state-versus-state competition and social features are required in version one. On the route you have chosen this matters more than it would have on the other one, because persistent multi-city play plus competition means real backend infrastructure rather than a mostly self-contained app.
3. How much dashboard depth has to be in version one against the first content update. The named risk on this route is scope creep, and the compressed schedule leaves less room to absorb it. Being deliberate here is what protects the date.

**What would help from your side**

The target age range, the launch territories and languages, and any mandatory national initiatives or messages that have to be in version one. On this schedule the discovery window is days rather than weeks, so having those at or before signature is what makes the fast start realistic. With them in hand, we can turn the Phase 2 range into a fixed price at the end of the prototype rather than at the end of discovery.

Happy to walk through any of this on a call if that is quicker.

Best regards,

David Vykopal
Production Director, NOXGAMES

---

## Internal notes (not for sending)

**Changes from v2**
- Prototype cut again, from 3–4 weeks to 2–3 weeks. Discovery is no longer a separate block, it runs inside the first few days of the build.
- All web-first positioning removed from the client copy. The product is presented as a phone app throughout. No mention of the underlying stack, Three.js, browsers, or Capacitor, since Patrick does not need to care which wrapper ships it.
- The performance argument for the prototype is kept, reframed as "the multi-city dashboard is demanding on a phone" rather than "web rendering in a wrapper". Same risk, client-appropriate framing.
- Phase 2 value trade rewritten: no longer "runs on web as well as phones", now the dashboard depth that Route 1 would have had to simplify. That is accurate to the brief, which lists exactly that as the Route 1 trade-off.

**Calendar chain (holds, with more slack than v2)**
Signature Aug 2026 → prototype delivered late Aug or very early Sept → development contract September → production Oct 2026 to Mar 2027 → India launch end Q1 2027 → Phase 3 parallel from ~Feb, soft launch through Q2 → global launch early Q3 2027.

The extra week does not compress production. It lands in the gap between prototype delivery and production start, which is where contracting and team reservation happen. That window was tight in v2 and is now more comfortable.

**Delivery approach: settled**
Web technology for the build, shipped to phone as a Capacitor app. Decided, not an open question. The practical consequence is that the Phase 1 prototype has to prove rendering and interface performance inside the wrapper on mid-range Android, because that is where this approach either works or does not. If it does not hold up, week two of the prototype is when we find out and the technical approach can still be changed before the development contract is signed. That is the real value of the 40k.

**Commercial exposure to be aware of**
- Phase 2 quoted at USD 550–600k against the 400–600k already on record. Defensible, and the email states the reason plainly rather than hiding it, but it is a narrowing upward and Patrick will notice.
- The deadline penalty remains the main risk. Bespoke route, compressed schedule, 10–20% reduction if the date slips. Already on record from the proposal so withdrawing it would look bad, but the change-control and late-client-input exclusions are now load-bearing rather than boilerplate. Worth having those tightened specifically before signature.
- A 2–3 week prototype at 40k is a firm public commitment on the hardest-to-estimate phase. It is achievable, but only if client inputs land at or before signature, which is why the email says so directly in the closing section.
- Optional live-ops retainer (indicative USD 15–25k/month) still left out to keep the three-phase answer clean. Raise it when the post-launch support period comes up.

**Divergence: published proposal is now out of date**
The live proposal page and `PROJECT_BRIEF.md` still present both routes as open, quote 400–600k without narrowing, carry the old dates, and state 3–4 weeks for the prototype. If Patrick re-reads either while considering this email, they contradict it on four separate points. Worth updating both before he circulates this internally.
