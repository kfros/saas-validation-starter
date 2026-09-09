# Stage 1 Willingness-to-Pay (WTP) & Costly Labor Map: Multi-Brand Content Production

**Idea:** `multi-brand-content`  
**Scope:** `MULTIBRAND-OPERATOR-01` (Owner-led SMM freelancers and boutique agencies producing recurring static content for multiple unrelated client brands)  
**Date:** 2026-09-09  
**Agent:** `wtp-research`  
**Status:** `PARTIAL` (4/10 inspected & repaired; 6/10 blocked by non-JS tool limitation on client-rendered Reddit comments)  
**Dataset Reference:** `ideas/multi-brand-content/raw/wtp/evidence.jsonl` (10 atomic records: `mb-wtp-001` through `mb-wtp-010`)  
**Repair Log:** `ideas/multi-brand-content/raw/wtp/repair-log.md`

---

## 1. Scope and ICP Coverage Overview

This research examines revealed economic commitments—cash software spend, human subcontracting expenditures, internal operator labor, and explicit subscription churn/refusals—related to recurring multi-brand social post and carousel production within scope `MULTIBRAND-OPERATOR-01`.

### Key Scope & Attribution Principles Enforced in Repair:
1. **Client Count vs. Organizational Headcount:** Managing 5 client accounts describes client workload, not team size. Organizational headcount is left `null` unless explicitly stated by the practitioner (`mb-wtp-002`, `mb-wtp-008`).
2. **Planned Purchase vs. Revealed Spend:** Stated intent to purchase software or pass costs through to clients is classified as `stated_wtp`, not confirmed expenditure (`mb-wtp-002`).
3. **Price Friction vs. Confirmed SaaS Expenditure:** Expressed dissatisfaction with tool pricing (e.g., Planable's Grid view) establishes pricing resistance, but cannot be counted as confirmed dollar spend when the active tier, dollar amount, or billing period is unstated (`mb-wtp-004`).
4. **Individual Churn vs. Market-Wide Price Ceilings:** An individual small business canceling Canva in favor of an existing Adobe Suite bundle demonstrates personal switching behavior and bundled substitution, not a universal market price ceiling (`mb-wtp-005`).
5. **In-House Operator Labor vs. Software Buyer Authority:** Heavy internal labor across multiple client accounts demonstrates operational capacity constraints, but entry-level agency employees handling multi-discipline execution (video, photography, copy, scheduling, and static design) are not equivalent to software budget holders (`mb-wtp-008`).
6. **Separation of Verified Facts from Blocked Legacy Claims:** Due to browser tool limitations (disabled `chrome_devtools` MCP server; non-JS HTTP fetcher unable to render client-side Lit comment trees on Reddit), only 4 thread OP records were verified against live text (`mb-wtp-002`, `mb-wtp-004`, `mb-wtp-005`, `mb-wtp-008`). The remaining 6 commenter records (`mb-wtp-001`, `mb-wtp-003`, `mb-wtp-006`, `mb-wtp-007`, `mb-wtp-009`, `mb-wtp-010`) remain unverified and are preserved as `PENDING` with unresolved overclaims documented in `repair-log.md`.

---

## 2. Verified Findings from Directly Inspected Sources

### A. Stated Willingness to Pay & Client Pass-Through Intent (`mb-wtp-002`)
- **Verified Finding:** A solo agency designer managing ~5 client brands with expansion plans is evaluating upgrading from Canva Pro to Canva Business at \$30/month for multiple brand kits and controls. The designer explicitly plans to pass this \$30/month software cost directly to clients by dividing it among retainers (\$6/client).
- **Economic Implication:** Confirms willingness to consider \$30/month for multi-brand asset controls, but reveals that agency designers prefer passing software expenses directly to clients rather than absorbing them into agency operating overhead. Because the purchase was not executed at the time of posting, this represents stated WTP rather than revealed spend.

### B. Feature-Specific Price Friction & Dissatisfaction (`mb-wtp-004`)
- **Verified Finding:** A social media practitioner uses Planable for client approvals on social posts and finds it "quite good," but seeks alternatives because Planable charges heavily ("charges a bomb") for its Grid view planner, which is the only view the team requires.
- **Economic Implication:** Establishes concrete price sensitivity around visual grid planning and multi-brand preview features. However, the source does not disclose whether the team is on a paid tier, the dollar amount spent, or the billing period; it cannot be treated as proven cash expenditure.

### C. Churn and Bundled Suite Substitution (`mb-wtp-005`)
- **Verified Finding:** A small business operator canceled their Canva account following a price increase combined with browser performance/lag issues in Chrome. The operator switched entirely to Adobe Express because they were already paying for the Adobe Creative Suite and found Express's generative AI features adequate to replace Canva for their business.
- **Economic Implication:** Illustrates churn risk when design software increases prices without perceived performance parity. Highlights substitution into already-paid software bundles (Adobe Suite). This reflects an individual switching event rather than an absolute market-wide price ceiling.

### D. In-House Labor Allocation & Multi-Discipline Load (`mb-wtp-008`)
- **Verified Finding:** An entry-level agency social media manager manages 5 client accounts across diverse industries as a single operator, handling content calendars, video recording with a professional camera, graphic design, post scheduling, captions, and account management. The operator reports feeling drained and notes compensation is low relative to the multi-account workload.
- **Economic Implication:** Confirms significant in-house labor allocation for multi-brand management (5 client accounts per operator under heavy load). However, compensation is not quantified, the workload spans photography, video, reels, and stories alongside static design, and the operator is an agency employee rather than an independent software buyer.

---

## 3. Unresolved Legacy Records (Blocked by Tool Limitations)

The following 6 records were attributed to Reddit commenters and could not be verified in live source text due to client-side rendering limitations. They are preserved in `evidence.jsonl` with `audit_status: PENDING`:

- **`mb-wtp-001` (Canva Teams Legacy Plan):** Raw record claims practitioner pays \$120/yr for a legacy Canva Teams plan with 1,000 brand kits. *Unresolved overclaim:* Legacy grandfathered pricing does not prove that all brand kits are utilized, that the payer matches target ICP, or that the subscription was bought specifically for the target job.
- **`mb-wtp-003` (Bulk Account Management Spend):** Raw record claims \$200 for 100 accounts on Postmypost (\$2/account/month). *Unresolved overclaim:* Inferred monthly price is invalid because the billing period is unstated; scheduling spend is adjacent to static content production; universal WTP ceiling is unsupported.
- **`mb-wtp-006` (Outsourced Contractor Spend):** Raw record claims \$1,500/month contractor spend dropped due to overhead. *Unresolved overclaim:* The contractor package covered filming, video editing, and posting with unknown static allocation; generalizing one failed contract into "human subcontracting fails" is an unsupported conclusion.
- **`mb-wtp-007` (Contractor Rate Benchmarks):** Raw record claims \$600/month contractor spend. *Unresolved overclaim:* The source text discussed standard rate ranges (\$400–\$800/mo, \$20–\$40/hr) and illustrative 50% margin arithmetic; retaining \$600 as actual spend was an overclaim.
- **`mb-wtp-009` (Task Timing Footprint):** Raw record claims 25–45+ monthly hours per client. *Unresolved overclaim:* The source provided task-level estimates (e.g., 30m–1h per static post), but the 25–45+ hour monthly total was a constructed summary; solo-owner status and client count were unverified.
- **`mb-wtp-010` (Canva Free Tier Advice):** Raw record claims free-tier retention and avoidance of paid tools. *Unresolved overclaim:* General forum advice stating Canva has a free version and can be used for client ads does not establish the speaker's personal tool status or deliberate paid-tool avoidance.

---

## 4. Category Coverage & G3 Mapping Status

Across the 10 atomic records in `evidence.jsonl`:

| G3 Spend Family | Raw Record IDs | Verified Current Status | Unresolved / Blocked Status |
| :--- | :--- | :--- | :--- |
| **`paid_tool_or_pilot`** | `mb-wtp-001`, `003`, `004`, `005` | `mb-wtp-004` (price friction, unconfirmed spend), `mb-wtp-005` (churn to existing Adobe bundle) | `mb-wtp-001` (unverified legacy plan), `mb-wtp-003` (unverified bulk tier) |
| **`internal_labor`** | `mb-wtp-008`, `009` | `mb-wtp-008` (agency operator labor, unquantified pay) | `mb-wtp-009` (unverified monthly total) |
| **`outsourced_labor`** | `mb-wtp-006`, `007` | None directly verified | `mb-wtp-006` (unverified contractor spend), `mb-wtp-007` (unverified rate benchmark) |
| **Stated WTP / Advisory** | `mb-wtp-002`, `010` | `mb-wtp-002` (\$30/mo stated WTP with pass-through intent) | `mb-wtp-010` (unverified free tier advice) |

**Current Run Coverage:** Because 6 of 10 records remain blocked by browser tool limitations, the WTP research run is formally designated as `PARTIAL`.

---

## 5. Tool Failures & Investigation Constraints

- **`chrome_devtools` Disallowed:** The MCP server was not permitted in this execution context, preventing headless browser automation.
- **Non-JavaScript HTTP Client:** The available tool `read_url_content` fetches static HTML only. Reddit's modern desktop architecture renders post bodies in SSR HTML, but renders comment threads via client-side JavaScript / GraphQL.
- **Ad-hoc Workarounds Prohibited:** In strict adherence to Validation Rules 25, 27, and 28, custom scraping scripts, unauthorized browser workarounds, or guessing comment text from memory were not attempted.

---

## 6. Material Unknowns for Subsequent Evaluation

1. **Pass-Through Feasibility:** How widely do boutique agencies and freelance SMMs successfully bill specialized software seats directly to clients versus absorbing software costs into fixed overhead?
2. **Static vs. Multi-Media Labor Allocation:** When practitioners report managing 5 accounts under heavy load, what exact portion of their hours is dedicated specifically to static graphics/carousels versus short-form video shooting and editing?
3. **WTP for Automated Grid Preview & Approvals:** Given that price friction was observed for Planable's Grid view (`mb-wtp-004`), what is the actual commercial willingness to pay for a dedicated multi-brand visual approval tool?
