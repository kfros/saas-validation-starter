# Adversarial Skeptic Case: Vertical B2B Deck / Sales-Collateral Automation

**Idea**: `deck-automation`  
**Phase**: Stage 1 Research (Adversarial Falsification Track)  
**Agent**: `skeptic-research`  
**Audit Status**: All raw evidence records remain `PENDING` awaiting independent audit.  
**Notice**: This document does not issue the official Stage 1 verdict.

---

## 1. Hypothesis and Scope Tested

### 1.1 The Stated Hypothesis
> "B2B teams that regularly create customer-specific sales decks spend meaningful recurring time adapting PowerPoint presentations to individual opportunities. Existing presentation AI tools do not fully solve the workflow because teams require company-specific templates, trusted source material, accurate client customization, and reliably editable native PPTX output. A sufficiently painful segment can justify a B2B SaaS price materially above low-cost consumer presentation subscriptions." (`hypothesis.yaml`)

### 1.2 Written Job Under Investigation
A business user takes an approved master corporate presentation plus opportunity-specific context (discovery notes, CRM opportunity data, case studies) and creates an on-brand, customer-specific, accurate, editable `.pptx` presentation for an external buyer.

### 1.3 Target Business & MVP Constraints
- **Target ARPU**: Minimum \$100/user/month.
- **Founder Model**: Solo technical founder with coding/research agents.
- **MVP Scope**: Buildable by a solo founder; strictly no full in-app presentation editor; native editable PPTX deliverable required.
- **Sales Model**: Self-service, remote sales, or founder-led outbound (avoiding heavy enterprise procurement).

### 1.4 Declared Candidate ICPs Evaluated
Each declared ICP from `hypothesis.yaml` was tested independently against market substitutes, workflow reality, and economic feasibility:
1. **B2B SaaS Account Executives (AEs)**
2. **Sales Enablement Teams**
3. **Boutique Consultancies**
4. **Agencies Producing Client Decks**
5. **Professional-Services Firms**
6. **Commercial Real-Estate (CRE) Teams**

---

## 2. Substitute Assessment Matrix

For each identified substitute, four discrete dimensions are evaluated per the Evidence Standard: capability, ICP/output fit, friction/economics, and observed adoption/sufficiency.

| Substitute | Target Workflow Capability | ICP / Input / Output Fit | Supported Price & Friction | Observed Adoption / Sufficiency Evidence | Unresolved Threats | Evidence IDs |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Microsoft 365 Copilot for PowerPoint** | High. Generates multi-slide presentations directly from structured Word files and notes within native PowerPoint. Learns corporate `.potx` layout rules and Brand Kits. | **High fit.** Targets knowledge workers & sales professionals using Microsoft 365. Native PPTX output without export degradation. | **\$23.50–\$30/user/mo.** Zero procurement friction (bundled into M365 tenant). No third-party security approval needed. | Broad enterprise deployment across Fortune 500 & mid-market. Native PowerPoint UI. | Output quality on highly complex custom layouts remains imperfect; requires structured Word inputs. | `ev-skp-m365-copilot-ppt-features`<br>`ev-skp-m365-copilot-brand-templates`<br>`ev-skp-m365-copilot-pricing` |
| **Seismic LiveDocs & Content Automation** | Complete. Dynamic slide assembly driven by Salesforce/HubSpot data; guided rep questionnaires; automated dynamic variable substitution. | **Exact fit for Sales Enablement.** Native PowerPoint plugin + cloud web app. Strict template permission controls. | **\$55/user/mo** on AppExchange; annual contracts. High implementation friction (weeks of setup, enterprise procurement). | Widely adopted standard in mid-market and enterprise B2B sales organizations. | Prohibitive setup and contract size for sub-50 employee SMBs without dedicated sales ops. | `ev-skp-seismic-livedocs-automation`<br>`ev-skp-seismic-appexchange-pricing`<br>`ev-skp-enablement-brand-lockdown` |
| **Highspot (Dynamic Pitch & Remix)** | High. Slide remixing from approved company libraries, CRM deal integration, digital sales rooms (Pitch), buyer engagement tracking. | **Exact fit for Enablement & AEs.** Reps customize approved slides; outputs tracked web links or PPTX. | **\$45–\$65/user/mo** (Median contract \$60,428/yr). Requires Sales Ops buy-in and platform onboarding. | Dominant enablement platform alongside Seismic; high switching costs. | High minimum contract values leave micro-SMBs underserved. | `ev-skp-highspot-pricing-procurement` |
| **Buildout (Showcase & Suite)** | Complete for CRE. Generates proposals, pitch decks, Offering Memorandums (OMs), flyers, and property sites directly from property database. | **Exact fit for Commercial Real Estate.** Integrates property comps, financial tables, and broker branding. | **\$125/user/mo.** High vertical stickiness (combines CRM, marketing materials, and syndication). | **50,000+ CRE brokers** across major national brokerages (Coldwell Banker Commercial, SVN, NAI Global). | Strictly limited to commercial real estate; not applicable to SaaS or general consulting. | `ev-skp-buildout-cre-suite`<br>`ev-skp-buildout-pricing` |
| **Plus AI for PowerPoint** | Moderate-High. Document-to-presentation conversion, slide-by-slide AI remixing, custom corporate template upload inside PowerPoint. | **High fit for SMBs, AEs, Consultants.** Operates directly inside PowerPoint and Google Slides. | **\$25–\$30/user/mo** for Team tier with custom templates and shared presets. Self-serve onboarding. | Growing adoption among individual consultants and small teams seeking native PowerPoint AI. | Limited complex data integration; lacks automated CRM field mapping. | `ev-skp-plusai-pricing-tier` |
| **think-cell** | Complete for quantitative slides. Direct bidirectional linking between Excel models and complex PowerPoint charts. | **Dominant in Strategy & Boutique Consulting.** Native PowerPoint plugin. | **\$22.00–\$28.60/user/mo** billed annually. High stickiness in professional services. | De facto standard in McKinsey, BCG, Bain, and boutique advisory firms. | Strictly quantitative charting; does not automate narrative qualitative slides. | `ev-skp-consulting-thinkcell-standard` |
| **Manual Status Quo (Slide Truncation / Demos)** | High sufficiency. Reps maintain a 5–10 slide "core deck" and hide unused slides; conduct live software walkthroughs; or pay freelancers \$100/deal. | **Directly matches current B2B AE and CRE workflow.** Zero software spend; zero security review. | **\$0 incremental software spend** or ~\$100/deal contractor fee. 2–5 minutes per opportunity. | Extensive reported practice on r/sales and r/CommercialRealEstate. High user satisfaction. | Still requires occasional manual deck compilation for RFPs or formal board reviews. | `ev-skp-ae-ditching-decks`<br>`ev-skp-ae-deck-truncation`<br>`ev-skp-cre-practitioner-om-spending` |

---

## 3. Strongest Recurrence Objection

### Finding: The hypothesized recurring deck creation loop does not exist for modern B2B SaaS AEs
The hypothesis assumes quota-carrying account executives spend frequent, recurring weekly hours assembling custom PowerPoint presentations for individual sales opportunities. 

**Adversarial Evidence**:
1. **Modern Sales Methodology Rejects Pitch Decks**: Field practitioners on `r/sales` consistently report abandoning slides during discovery and demo calls (`ev-skp-ae-ditching-decks`). Enterprise buyers perceive PowerPoint presentations as canned, impersonal pitches. Top-performing reps conduct live platform walkthroughs and interactive problem-solving directly in the software, eliminating the need to assemble opportunity-specific decks.
2. **Aggressive Deck Truncation**: When company management enforces pitch decks, reps actively minimize usage—cutting mandated 30-slide decks down to 5–7 core slides (`ev-skp-ae-deck-truncation`). Routine opportunities use static, uncustomized one-pagers or standard overview slides.
3. **Bespoke Decks Are Ad-Hoc, Not Daily/Weekly**: Full bespoke presentation assembly is reserved almost exclusively for massive multi-stakeholder enterprise RFPs or board-level proposals. These occur ad-hoc (a few times per quarter), rather than forming a high-frequency recurring SaaS workflow.

---

## 4. Strongest Willingness-to-Pay (WTP) Objection

### Finding: Incumbent bundling and vertical platforms crush WTP far below the \$100/mo ARPU target
The hypothesis requires an eventual ARPU of at least \$100/user/month to support a viable B2B SaaS business under solo-founder acquisition constraints.

**Adversarial Evidence**:
1. **The \$23.50–\$30/mo Microsoft Price Anchor**: Microsoft 365 Copilot provides presentation generation from source files directly inside native PowerPoint for \$23.50–\$30/user/month (`ev-skp-m365-copilot-pricing`). Enterprise and mid-market IT buyers already paying for Microsoft 365 will not authorize a \$100+/mo add-on for a point solution that performs a subset of Copilot's features.
2. **Specialized Add-Ins Standardized at \$25–\$30/mo**: Third-party in-tool add-ins (Plus AI at \$30/mo, think-cell at \$22–\$28.60/mo) have commoditized presentation automation at the \$25–\$30/seat level (`ev-skp-plusai-pricing-tier`, `ev-skp-consulting-thinkcell-standard`).
3. **Enterprise Suites Bundle Decks with LMS & Analytics for \$45–\$65/mo**: Enterprise enablement platforms (Highspot at \$45–\$65/mo, Seismic at \$55/mo) bundle CRM presentation generation with learning management, conversation intelligence, and buyer tracking (`ev-skp-seismic-appexchange-pricing`, `ev-skp-highspot-pricing-procurement`). A standalone slide tool cannot command a 2x premium over a full-suite enablement platform.
4. **Cheap Manual Alternatives in Real Estate**: In commercial real estate, where decks (Offering Memorandums) are mandatory, brokers pay freelancers \$100 per deal for manual plug-and-play assembly, while buyers discard qualitative narrative filler slides (`ev-skp-cre-practitioner-om-spending`).

---

## 5. Strongest Adoption & Procurement Blocker

### Finding: Enablement brand lockdown and enterprise InfoSec audits block solo-founder self-service adoption

**Adversarial Evidence**:
1. **Brand Lockdown and Compliance Gatekeeping**: Sales Enablement and Marketing leadership intentionally restrict reps from altering presentations (`ev-skp-enablement-brand-lockdown`). In regulated and mid-market B2B organizations, unvetted deck generation introduces severe compliance risks (unapproved pricing, non-standard SLAs, unauthorized roadmap commitments). Enablement teams want centralized lockdown (as provided by Seismic/Highspot), not distributed rep-level AI generation.
2. **The 4.2-Week InfoSec Barrier for CRM / Transcript Access**: To generate meaningful "customer-specific" decks, the tool must ingest CRM deal fields, customer websites, and discovery transcripts. SyncGTM security benchmarks document that sales software accessing CRM data faces average security review cycles of 4.2 weeks, requiring SOC 2 Type II certification, GDPR DPAs, and zero-data-retention AI commitments (`ev-skp-infosec-procurement-hurdles`). A solo technical founder pursuing self-serve or lightweight outbound cannot absorb this enterprise compliance overhead.
3. **Budget Ownership Mismatch**: Individual AEs lack corporate credit card authority for \$100/mo ongoing subscriptions. Purchases must be approved by Sales Ops / Finance, immediately routing the tool into enterprise procurement.

---

## 6. Strongest Technical / MVP Blocker

### Finding: Maintaining 100% editable corporate PPTX fidelity without a dedicated presentation editor is technically fragile
The hypothesis explicitly assumes an MVP constraint: *buildable by a solo technical founder without building a full presentation editor*, relying on native editable PPTX output.

**Adversarial Evidence**:
1. **OpenXML Template Complexity**: Corporate PowerPoint templates (`.potx`) rely on deeply nested XML slide masters, custom layout geometries, placeholder inheritance hierarchies, embedded custom corporate typography, and strict aspect ratio rules. Existing venture-backed tools (Gamma, Beautiful.ai) consistently experience layout breakage and formatting degradation when exporting to native PPTX because standard web layout engines (HTML/CSS/Canvas) do not map cleanly to OpenXML rendering trees.
2. **Microsoft's Native Architectural Moat**: Microsoft Copilot runs directly within the native PowerPoint codebase, possessing direct telemetry over master layouts, placeholder types, content density, and visual hierarchy (`ev-skp-m365-copilot-brand-templates`). A third-party headless generator must reverse-engineer proprietary PowerPoint layout behavior without an interactive visual editor to let the user fix alignment glitches before export.

---

## 7. ICP-by-ICP Falsification Evaluation

| Candidate ICP | Hypothesized Need | Skeptic Findings & Ground Truth | Verdict for this ICP |
| :--- | :--- | :--- | :--- |
| **B2B SaaS Account Executives** | Adapt decks weekly for individual sales opportunities; will pay \$100/mo to save 3+ hours/week. | AEs avoid pitch decks on calls in favor of live software demos (`ev-skp-ae-ditching-decks`). Lack purchasing authority; cannot pass CRM security audits (`ev-skp-infosec-procurement-hurdles`). | **Falsified.** Workflow does not recur at sufficient frequency; no budget authority. |
| **Sales Enablement Teams** | Need tools to help reps generate on-brand customized collateral efficiently. | Enablement's primary goal is *brand and compliance lockdown* (`ev-skp-enablement-brand-lockdown`). Already deployed on Seismic (\$55/mo) or Highspot (\$45–\$65/mo) for unified governance (`ev-skp-seismic-livedocs-automation`). | **Falsified.** Problem already solved by enterprise incumbents; buyer resists rep-level autonomy. |
| **Commercial Real-Estate Teams** | Generate property pitch decks and Offering Memorandums (OMs) for listings. | Completely dominated by **Buildout** (50,000+ brokers, \$125/mo), which connects deal data, proposal creation, and listing syndication (`ev-skp-buildout-cre-suite`). Lenders ignore narrative slides (`ev-skp-cre-practitioner-om-spending`). | **Falsified.** Incumbent vertical killer substitute exists with massive market share. |
| **Boutique Consultancies** | Generate client proposals and deliverables from proprietary methodologies. | Standardized on **think-cell** (\$22–\$28/mo) for quantitative models (`ev-skp-consulting-thinkcell-standard`). Slide formatting is inseparable from partner synthesis loops and protected by strict client NDAs (`ev-skp-consulting-slide-formatting-synthesis`). | **Falsified.** High NDA sensitivity; bespoke partner craft; unbundled spend capped at \$25/mo. |
| **Agencies Producing Client Decks** | Produce client presentations and pitch decks quickly. | Agencies sell bespoke high-touch creative design and storytelling (charging \$10k–\$50k+ per project); adopting automated template generation contradicts their core value proposition and agency margins. | **Falsified.** Low willingness to use generic automation; rely on Figma/InDesign and dedicated designers. |
| **Professional-Services Firms** | Adapt service proposals and statements of work (SOWs) for clients. | SOWs and proposals are typically legal/contractual documents handled via Word, Google Docs, or CPQ/PandaDoc/Qwilr rather than graphic PowerPoint presentations. | **Falsified.** Wrong deliverable format; market uses document/proposal tools. |

---

## 8. Evidence Sufficient to Rebut Each Major Objection

To overturn these skeptic findings and justify proceeding to Stage 2, future validation research must discover verified primary evidence satisfying the following criteria:

1. **Rebutting the Recurrence Objection**:
   - Primary evidence (interviews or timestamped logs) showing a specific, reachable B2B segment where reps build **at least 3–5 customer-specific presentations per week** as a mandatory deal prerequisite.
   - Proof that live demos or static 5-slide decks cannot replace this deliverable.
2. **Rebutting the WTP / Price Anchor Objection**:
   - At least 3 verified money signals showing non-enterprise SMB buyers paying **\$100+/user/month specifically for slide deck automation** (not bundled enablement, not CRM syndication, and not full digital sales rooms).
   - Evidence of buyers actively churning from Microsoft Copilot (\$30/mo) or Plus AI (\$30/mo) to adopt a higher-priced point solution due to template/accuracy failures.
3. **Rebutting the Brand Lockdown / Enablement Blocker**:
   - Evidence of Sales Enablement or Marketing leaders purchasing third-party AI deck tools for their reps, including documented administrative controls that satisfy brand compliance without requiring full enterprise platform migration.
4. **Rebutting the CRE Buildout Dominance**:
   - Identification of an underserved CRE niche (e.g., independent boutique leasing brokers) that refuses Buildout's \$125/mo suite but possesses recurring deck automation volume and standalone willingness to pay.

---

## 9. Candidate New Scopes Discovered (`UNVALIDATED`)

During the adversarial research, several adjacent pain points were noted. Under workspace methodology, these cannot inherit evidence or rescue the current idea, and are recorded strictly as unvalidated exploratory leads:

- `SCOPE-UNVALIDATED-01`: **Automated RFP & Security Questionnaire Completion**: AEs and Sales Ops report recurring frustration with 100+ question spreadsheet and portal questionnaires during enterprise procurement. (Substitutes exist: Loopio, Responsive).
- `SCOPE-UNVALIDATED-02`: **Post-Demo Interactive Executive Summaries (Digital Sales Rooms)**: AEs moving away from slides report using interactive one-pagers or web-based mutual action plans (e.g., Dock, Flowla) to follow up after discovery calls.

---

## 10. Research Shortfall and Tooling Blockers

- **Records Collected**: 16 primary (Tier A) and secondary (Tier B) records successfully written to `evidence.jsonl`.
- **Validation Check**: Verified via `python scripts/validate_evidence.py ideas/deck-automation/raw/skeptic/evidence.jsonl` (exited with code 0; 0 errors).
- **Tool / Resource Status**: Chrome DevTools MCP browser subagent operated without failure; zero research tool exhaustion; no fallback scraping required.
- **Unresolved Threats Left Unresolved**:
  - The exact market share and churn rate of Microsoft Copilot for PowerPoint among mid-market sales teams remains unmeasured by public sources.
  - Whether boutique M&A advisory or investment banking pitch books represent a viable high-WTP niche was not fully falsified, as investment banks operate under strict on-premise/enterprise security constraints outside the solo-founder scope.
