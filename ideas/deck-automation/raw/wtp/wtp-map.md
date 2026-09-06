# Willingness-to-Pay (WTP) Research Map — Vertical B2B Deck Automation

**Idea ID:** `deck-automation`  
**Stage:** 1 (Discovery & Hypothesis Validation)  
**Agent:** `wtp-research`  
**Status:** Complete (10 Candidate Records, 5 Money-Signal Categories)  
**Audit Status:** `PENDING` (Subject to Evidence Auditor review)  
**Verdict Note:** Per Workspace Rule 17, research agents do not issue PASS/FAIL decisions.

---

## 1. Executive Summary

This research investigates revealed willingness to pay (WTP) and actual economic spend for custom sales deck generation, presentation formatting, and sales collateral adaptation. 

Rather than relying purely on competitor list prices, this investigation prioritizes **actual spend and costly labor**:
1. **Full-time dedicated labor** allocated to slide design and presentation production ($60,000 to $89,000+ base salary).
2. **Outsourced agencies and retainer subscriptions** ($699/month to $15,000/month minimum commitments; $11 to $66/slide variable fees).
3. **Freelance contractors** ($35 to $60/hour median; $1,125 to $3,750 per deck cleanup).
4. **Enterprise sales enablement and deck assembly suites** ($31,000 to $60,000+ median annual contract values; $45 to $75/user/month).
5. **Budget ceilings and low-end resistance** (Founders substituting with $30–$50 static templates; RevOps rejecting "6-figure solutions").

### Core Takeaways for the Hypothesis:
- **Commercial Viability of a B2B SaaS Price Point:** The market already tolerates and reveals substantial spend to solve presentation customization. Companies pay thousands of dollars per month to agencies or tens of thousands annually to enterprise suites (Highspot/Seismic) to automate or offload presentation creation.
- **The Mid-Market "Air Gap":** Enterprise platforms solve dynamic deck assembly from CRM data, but their **$30,000 to $100,000+ annual price floor** leaves mid-market and SMB teams stranded between expensive enterprise software and manual, slow agency/freelance labor.
- **Negative / Falsification Boundary:** Early-stage founders and small teams (1–10 employees) display very low willingness to pay for slide automation, routinely relying on cheap $30–$50 static templates (Canva, Etsy) and DIY editing. Targeting early-stage founders at \$100+/mo would face steep resistance; the viable buyer persona lives in teams with dedicated sales motions, high opportunity values, and active CRM pipelines.

---

## 2. Willingness-to-Pay Hierarchy & Spend Tiers

| Tier / Category | Spend Level / Pricing Structure | Typical Providers / Benchmarks | Budget Owner / Buyer | WTP Signal Type |
| :--- | :--- | :--- | :--- | :--- |
| **Tier 1: In-House Headcount** | **$60,000 – $89,147/year** base salary ($30 – $45/hr) | Corporate Presentation Designers (e.g. Unbridled, Vercel, THE·TEAM, BNY) | Head of Sales Enablement / VP Marketing / Creative Director | `dedicated_role` |
| **Tier 2: Agency Retainers & Per-Slide** | **$15,000/mo min** (Superside); **$899 – $2,950/mo** (24Slides); **$699/mo** (PitchWorx); **$11 – $66/slide** | Superside, 24Slides, Buffalo 7 (£1,900+), PitchWorx, SlideGenius | VP Marketing, VP Sales, RevOps | `agency_spend` |
| **Tier 3: Freelance Contractors** | **$45/hr median** ($35–$60/hr range); **$75–$150/hr** senior; **$1,125–$3,750/deck** | Upwork marketplace, independent presentation contractors | Sales Directors, Consultants, Boutique Agency Owners | `contractor_spend` |
| **Tier 4: Enterprise Enablement SaaS** | **$31,950 – $60,405/year median** ($45–$75/user/mo + $5k onboarding) | Highspot, Seismic, Templafy ($40/user/mo) | VP Sales Operations, Chief Commercial Officer, Enterprise IT | `saas_spend` |
| **Tier 5: Horizontal Tools & Templates (Low Anchor)** | **$10 – $20/user/month** or **$30 – $50 one-time** | Gamma ($10–$20/mo), Beautiful.ai ($14.50/mo), Canva/Etsy templates ($30–$50) | Individual AEs, Bootstrapped Founders | `stated_wtp` / `competitor_price` |

---

## 3. Detailed Spend Category Breakdowns

### 3.1 Dedicated Internal Labor (`dedicated_role`)
- **ZipRecruiter US Benchmark (Sep 2026):** Average annual pay for a dedicated PowerPoint Presentation Designer in the US is **$89,147/year** (~$42.86/hour), while general presentation specialists average **$63,706/year** ($30.63/hour). Senior roles in major metros reach **$105–$165/hour** on contract.
- **Verified Job Postings:**
  - *Unbridled (Aug 2026):* Posted base salary of **$65,000 – $72,000/year** for a full-time Presentation Designer to manage corporate templates and client presentation delivery.
  - *THE·TEAM (2026):* Posted base salary of **$60,000 – $70,304/year** for a Presentation Designer embedded with business development leads to produce RFP and sales pitch decks.
  - *Clear Visions / RRD (2026):* Hourly wage of **$30.30 – $46.06/hour** ($63k–$95k annualized) for dedicated slide formatting.
- **Implication:** Mid-market and enterprise organizations readily allocate $60,000 to $90,000+ in annual salary per person solely to take rough notes/data and format them into client-ready presentation slides.

### 3.2 Agency Spend & Recurring Retainers (`agency_spend`)
- **Superside:** Explicitly mandates an annual contract with a **$15,000 monthly minimum** ($180,000/year commitment) for enterprise design-as-a-service, which includes pitch decks, ABM collateral, and sales presentations.
- **24Slides:**
  - *Pay-as-you-go per slide:* $11 to $16 for "Fix Up" (alignment/formatting), $28 to $43 for "Redesign", and $44 to $66 for "Redraw" (from scratch/notes).
  - *Dedicated Teams:* Retainer packages starting at **$899 to $2,950/month** ($10,800 to $35,400/year) for guaranteed daily slide throughput and a dedicated project manager.
- **PitchWorx & Specialist Agencies:**
  - PitchWorx sells an unlimited deck design subscription for **$699/month**.
  - Traditional agencies (e.g. Buffalo 7) charge project fees starting at **£1,900 (~$2,450 USD)** up to **£8,550+** per deck.
  - Industry per-slide vendor average is ~$50/slide ($1,000 for a 20-slide deck).

### 3.3 Freelance Contractor Spend (`contractor_spend`)
- **Upwork Hiring Benchmarks:** Median hourly rate for freelance presentation designers is **$45/hour**, with typical rates between **$35 and $60/hour**.
- **First-Hand Designer Disclosures (Reddit r/powerpoint):**
  - Freelance presentation designers report quoting **$75 to $150/hour** for slide cleanup projects.
  - A standard corporate deck of 20 to 30 slides typically requires **15 to 25 hours** of manual alignment, typography matching, and table cleanup, yielding an invoice of **$1,125 to $3,750 per deck**.

### 3.4 Enterprise SaaS Spend & Budget Boundaries (`saas_spend` & `stated_wtp`)
- **Highspot & Seismic (Vendr Benchmarks & Reddit Disclosures):**
  - Vendr procurement data reveals a median annual buyer spend of **$60,405/year** for Highspot ($45–$65/seat/month + $5,000+ onboarding) and **$31,950/year** for Seismic ($50–$75/seat/month).
  - Reddit r/sales discussions confirm seat pricing of $45–$75/user/month plus mandatory $5k implementation fees.
- **The "6-Figure Solution" Blocker (Reddit r/revops):**
  - In an r/revops inquiry seeking to push Salesforce fields into presentation slides, the practitioner explicitly notes: *"Was hoping for something that's not a 6 figure solution since we only need it for 1 use case."*
  - This establishes both a ceiling (buyers revolt at $100k+ enterprise suites for narrow deck workflows) and a revealed willingness to pay for a dedicated mid-market tool.

---

## 4. Negative Evidence & Falsification Signals

Workspace Rules 9 and 22 require preserving contradictory evidence. WTP research identified clear boundaries where willingness to pay collapses:

1. **Early-Stage Founder Resistance (Reddit r/startups — `ev-wtp-reddit-startups-low-wtp-diy`):**
   - Founders overwhelmingly advise against spending $500–$2,000 on deck designers or paying for recurring presentation software before achieving product-market fit.
   - The established workaround is purchasing a **$30–$50 one-off static template** on Canva, Creative Market, or Etsy, and manually updating text in Google Slides.
   - *Falsification Risk:* If the product is marketed generically to early-stage founders or seed startups, WTP will fail to support a \$100+/mo ARPU.

2. **Horizontal AI Tool Pricing Anchors:**
   - Tools like Gamma ($10–$20/mo), Beautiful.ai ($14.50/mo), and Microsoft 365 Copilot ($30/mo) anchor end-user perception of "AI presentation generators" at $10 to $30/month.
   - *Requirement:* To achieve \$100+/mo ARPU, the product cannot position as an "AI slide maker." It must position as a **sales workflow automation engine** directly tied to CRM deal stages, revenue operations, and corporate brand governance.

---

## 5. Candidate Evidence Records Summary

The accompanying file [`ideas/deck-automation/raw/wtp/evidence.jsonl`](file:///c:/Work/Projects/saas-validation-starter/ideas/deck-automation/raw/wtp/evidence.jsonl) contains 10 structured evidence records adhering to `methodology/evidence-schema.json`:

| Record ID | Type / Subtype | Money Signal | Amount / Period | Polarity | Source / Organization | Independence Key |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `ev-wtp-superside-minimum-annual` | `wtp` / `agency_spend` | `agency_spend` | \$15,000 / month | `supports` | Superside Official Pricing | `superside-official-pricing-2026` |
| `ev-wtp-24slides-pricing-models` | `wtp` / `agency_spend` | `agency_spend` | \$899 / month | `supports` | 24Slides Official Pricing | `24slides-official-pricing-2026` |
| `ev-wtp-pitchworx-deck-cost-guide` | `wtp` / `agency_spend` | `agency_spend` | \$699 / month | `supports` | PitchWorx Benchmark Guide | `pitchworx-deck-cost-guide-2026` |
| `ev-wtp-upwork-presentation-designer-hourly` | `wtp` / `contractor_spend` | `contractor_spend` | \$45 / hour | `supports` | Upwork Hiring Benchmark | `upwork-presentation-designer-rates-2026` |
| `ev-wtp-ziprecruiter-powerpoint-designer-salary` | `wtp` / `dedicated_role` | `dedicated_role` | \$89,147 / year | `supports` | ZipRecruiter National Data | `ziprecruiter-powerpoint-designer-salary-2026` |
| `ev-wtp-builtin-unbridled-presentation-designer` | `wtp` / `dedicated_role` | `dedicated_role` | \$65,000 / year | `supports` | Built In Job Posting (Unbridled) | `builtin-job-unbridled-presentation-designer` |
| `ev-wtp-vendr-sales-enablement-median-spend` | `wtp` / `saas_spend` | `saas_spend` | \$60,405 / year | `supports` | Vendr Marketplace & r/sales | `vendr-highspot-seismic-procurement-benchmark` |
| `ev-wtp-reddit-revops-six-figure-ceiling` | `wtp` / `stated_wtp` | `stated_wtp` | \$100,000 / year | `supports` | Reddit r/revops | `reddit-revops-sfdc-slides-six-figure-complaint` |
| `ev-wtp-reddit-powerpoint-cleanup-hourly-rates` | `wtp` / `contractor_spend` | `contractor_spend` | \$1,125 / one_time | `supports` | Reddit r/powerpoint Practitioner | `reddit-powerpoint-freelancer-hourly-cleanup-cost` |
| `ev-wtp-reddit-startups-low-wtp-diy` | `wtp` / `stated_wtp` | `stated_wtp` | \$30 / one_time | `contradicts` | Reddit r/startups Discussions | `reddit-startups-low-wtp-cheap-templates` |

---

## 6. Verification Status

- Canonical schema validation: **PASSED** via `scripts/validate_evidence.py` and Python schema assertion.
- Duplicate checks: **PASSED** (all 10 records have unique IDs and distinct `independence_key` values).
- Initial Audit Status: All 10 records initialized to `PENDING` for Stage 1 Evidence Auditor review.
