# Unslop website-design skills (verified Oct 27, 2026 ET)

Research window: roughly the past 30 days on X (from ~2026-09-27) plus GitHub/web sources.
Query volume on X for `(frontend-design|unslop|anti-slop|impeccable) (skill|claude) (website|design|UI)`: **321 posts in the last ~7 days alone**, peaking Oct 25–27.

## Skills selected (4)

### 1. Anthropic `frontend-design`
- **Source:** https://github.com/anthropics/skills/tree/main/skills/frontend-design
- **SKILL.md:** https://raw.githubusercontent.com/anthropics/skills/main/skills/frontend-design/SKILL.md
- **Blog:** https://claude.com/blog/improving-frontend-design-through-skills
- **Stars (repo):** ~183K (cited widely on X Oct 2026; e.g. @aiupdatelog Oct 24, @0xRafy Oct 24–26)
- **Why it ranked:** Official Anthropic skill; default recommendation whenever people complain about purple-gradient AI landing pages.

**Key rules applied here**
- Plan a token system (color, type, layout, principles) before code; revise anything that matches a generic default.
- Avoid the five AI-default clusters: cream+terracotta, black+acid-green, broadsheet hairlines, SaaS identical-card kit, template chrome (ALL-CAPS eyebrows, middle-dot meta, spaced em-dash labels, Inter, soft grey shadows).
- Distinctive typography (not Inter/Arial); type as an active design element.
- One orchestrated motion moment, not fade-and-slide on every section.
- Hero opens with the most characteristic thing in the subject's world (here: chrome robot bottle / ampules).
- Copy is design content: active voice, sentence case, no filler; CTAs name the action.
- Spend boldness in one place; Chanel rule (remove one accessory).

### 2. Taste Skill (`design-taste-frontend`) — Leonxlnx
- **Source:** https://github.com/Leonxlnx/taste-skill
- **Site:** https://www.tasteskill.dev/
- **SKILL.md:** https://raw.githubusercontent.com/Leonxlnx/taste-skill/main/skills/taste-skill/SKILL.md
- **Stars:** ~99K; repeatedly listed in Oct 2026 "anti-slop" roundups (@lorden_eth Oct 6, @bibryam Oct 25, @craftworkdesign Oct 26, @madebyluca Oct 18).

**Key rules applied here (house style)**
- Idea sentence from the subject itself, not the category: "On this page, [subject thing] becomes [design device]."
- No eyebrows / pill badges above headings.
- No gradients, no resting shadows/glows, no glass/backdrop-blur nav.
- No icon-topped feature cards or rows of identical cards.
- No index numbering (01/02/03), no thin hairline rules, no monospace outside code.
- No assistant palette (cream+terracotta, violet/indigo).
- No styled accent word inside a headline.
- Two typefaces at most; headlines ≤2 lines at every width.
- Equal outer margins; no blank half-screens; section compositions must differ from neighbors.
- Real product photography (project's own), large; at least one dominant image ≥~40% of first screen.
- Motion: one signature move + staggered section entrances + control feedback; respect `prefers-reduced-motion`.

### 3. Impeccable — Paul Bakaus
- **Source:** https://github.com/pbakaus/impeccable
- **Site:** https://impeccable.style
- **Why it ranked:** Explicitly built as the successor/extension of Anthropic frontend-design; cited with frontend-design in Oct setups (@rwspatin Oct 3, @craftworkdesign Oct 26, @HAnetoh Oct 6). 62 deterministic anti-slop detectors.

**Key rules applied here**
- Ban overused fonts (Inter, Arial, system-ui as the only face).
- Don't wrap everything in cards or nest cards.
- Don't use gray text on colored backgrounds; tint neutrals.
- No bounce/elastic easing.
- Critique/polish pass after build: hierarchy, clarity, responsive, a11y focus rings.
- PRODUCT truth first (audience, purpose, real prices, real links) before visual direction.

### 4. UI/UX Pro Max — nextlevelbuilder
- **Source:** https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
- **Stars:** ~137–139K (cited Oct 22–25 as a top design skill on X).
- **Why included:** Searchable industry palettes + 74 font pairings + anti-patterns (e.g. "no AI purple/pink gradients" for athletic/ecom).

**Key rules applied here**
- Match sports/e-commerce mood: high-contrast athletic photography, sparse nav, product-first.
- Curated font pairings instead of Inter.
- Industry anti-patterns: no purple gradients, no fake vanity stats, no emoji icon tiles.

## Also noted (not primary for this build)
- Emil Kowalski frontend skill (mentioned on X; smaller footprint than the four above).
- Hallmark, no-slop-ui, avoid-ai-design, huashu-motion (appear in roundup lists; less traction than the four selected).

## How this Syborg pass uses them
| Design | Idea (Taste) | Type pairing (Pro Max + frontend-design) | Palette | Composition |
|--------|--------------|------------------------------------------|---------|-------------|
| d1 Ampule | Sealed glass ampule becomes the page's unit | Syne + Instrument Sans | Slate `#0c1218`, ice `#8ad4f0`, paper `#e8eef2` | Vertical ampule columns; clinical crop |
| d2 Platform | Chalked lifting platform becomes every ground | Barlow Condensed + Newsreader | Chalk `#f2efe6`, iron `#121212`, meet red `#b91c1c` | Horizontal platform bands; light-first editorial |
| d3 Chrome | Extreme chrome-robot crop fills the viewport; bottle packshot rides negative space | Archivo Black + Sora | Void `#05070d`, mercury `#c5ccd4`, signal cyan `#3eb7ff` | Extreme packshot crop; asymmetric type overlay |

Shared bans across all three: no purple gradients, no Inter, no icon-card grids, no ALL-CAPS eyebrows, no numbered steps as decoration, no glass nav, no invented reviews/stats. Real SKUs and store links only.
