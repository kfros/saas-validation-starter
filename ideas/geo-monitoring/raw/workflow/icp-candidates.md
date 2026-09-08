# ICP Candidates: GEO / AI-Search Visibility Monitoring

## 1. Candidate Overview & Scope Classification

In accordance with `ideas/geo-monitoring/hypothesis.yaml` and `ideas/geo-monitoring/research-protocol.md`, this Stage 1 research run evaluates exactly one primary candidate ICP (`GEO-AGENCY-01`). All adjacent customer profiles are explicitly classified as `OUT_OF_SCOPE` / `UNVALIDATED` leads to prevent scope pooling.

| Segment ID | Segment Name | Scope Classification | Validation Status | Evidence Sourced |
| :--- | :--- | :--- | :--- | :--- |
| **GEO-AGENCY-01** | Small Independent SEO Agencies | **Primary Scope (IN_SCOPE)** | Active Stage 1 Evaluation (15 Records) | Direct primary case studies, verified agency profiles, pricing, workflows. |
| **GEO-BRAND-01** | Direct-to-SMB Brand Owners | **OUT_OF_SCOPE** | Unvalidated Lead | Peripheral / adjacent; excluded from G1-G5 gates. |
| **GEO-ENT-01** | Enterprise In-House SEO Teams | **OUT_OF_SCOPE** | Unvalidated Lead | Enterprise procurement; excluded from founder constraints. |
| **GEO-SOLO-01** | Solo Freelance SEO Consultants | **OUT_OF_SCOPE** | Unvalidated Lead | Single-operator, low budget threshold; not assumed agency equivalent. |
| **GEO-EXEC-01** | Autonomous Content Execution Agencies | **OUT_OF_SCOPE** | Unvalidated Lead | Content generation focus (Byword/Koala model), not monitoring. |

---

## 2. Primary Candidate ICP: GEO-AGENCY-01

### 2.1 Profile Definition

* **Organization Type**: Independent boutique digital marketing or SEO agency.
* **Firm Size**: 2 to 20 full-time staff members (verified micro/small business bracket).
* **Client Engagement Model**: Ongoing monthly recurring retainer engagements with Small and Medium-Sized Businesses (SMBs) or growth-stage tech/SaaS companies.
* **Language & Geography**: English-serving agencies (empirically observed across New Zealand, UK, Europe, and North America; country is not inferred from language).

### 2.2 Key Roles & Stakeholder Dynamic

* **Economic Buyer / Budget Owner**:
  * Agency Founder, Owner, or Managing Director.
  * In agencies with 10–20 staff: Head of SEO or Operations Director with discretionary software expenditure authority ($100–$500/month limit).
  * Purchasing Motivation: Client retention, defending retainer value against zero-click traffic drops, winning new business via prospect pitch audits.
* **Actual Operator**:
  * SEO Strategist, GEO Specialist, Senior Technical SEO, or Account Manager.
  * In 2–5 person studios: The technical co-founder / lead developer directly.
  * Operational Motivation: Eliminating manual screenshot collection and VPN switching, generating defensible white-label reports in Looker Studio, and pinpointing exact crawlability/schema actions to take.

### 2.3 Workflow Fit & Evidence Backing

* **Job Recurrence**: Recurring weekly and monthly reviews aligned with contractual client reporting cycles ([`geo-workflow-03-whatifweb-deliverable`](#), [`geo-workflow-06-sornai-reporting-cadence`](#)).
* **Observed Workaround**: High friction in manual prompt sampling using VPNs and screenshots across multiple engines ([`geo-workflow-12-manual-workaround-labor`](#)).
* **Commercial Behavior**: Agencies are actively packaging GEO monitoring and reporting into standalone client retainers at $399–$699/month ([`geo-workflow-08-butter-marketing-offer`](#)) and subscribing to agency monitoring tooling like Peec AI and Otterly.ai ([`geo-workflow-13-peec-agency-substitute`](#), [`geo-workflow-15-otterly-looker-studio-connector`](#)).
* **Confidence Level**: **HIGH** workflow fit supported by 15 atomic raw evidence records.

### 2.4 Reachability Assessment

* **Discoverability**: **HIGH**. Public B2B directories like Clutch.co provide granular filtering by headcount (2–9, 10–49 employees) and explicit service lines ("Generative Engine Optimization") with direct links to leadership ([`geo-workflow-11-reachability-clutch`](#)).
* **Outreach Surfaces**: Founders and heads of SEO maintain public contact pages, agency blogs, and direct scheduling links (HubSpot, Calendly) for discovery calls ([`geo-workflow-01-whatifweb-profile`](#), [`geo-workflow-04-sornai-profile`](#), [`geo-workflow-08-butter-marketing-offer`](#), [`geo-workflow-10-embarque-deliverable`](#)).
* **Coverage Verification**: 4 distinct matching agencies documented empirically (What IF Web, SORN.AI, Butter Marketing, Embarque).

---

## 3. Adjacent / Out-of-Scope Segments

### 3.1 Direct-to-SMB Brand Owners (`GEO-BRAND-01`)
* **Status**: `OUT_OF_SCOPE` / `UNVALIDATED`.
* **Rationale**: SMB business owners lack the technical fluency to interpret crawlability logs, JSON-LD schema gaps, or non-deterministic prompt variance. They demand traffic and sales guarantees rather than citation indexing reports. Selling to direct SMBs would introduce severe onboarding and education churn.

### 3.2 Enterprise In-House SEO / Corporate Communications (`GEO-ENT-01`)
* **Status**: `OUT_OF_SCOPE` / `UNVALIDATED`.
* **Rationale**: Enterprise teams require SOC2 compliance, SSO integration, procurement review cycles, and multi-department governance. This segment is targeted by enterprise incumbents like Profound (`tryprofound.com`) and violates the solo-founder business model constraints.

### 3.3 Solo Freelance Consultants (`GEO-SOLO-01`)
* **Status**: `OUT_OF_SCOPE` / `UNVALIDATED`.
* **Rationale**: While solo consultants perform SEO work, they manage small, irregular client rosters, frequently revert to manual spreadsheets without tool budget, and have a lower willingness to pay threshold ($20–$50/month). They are not equivalent to multi-client agencies.

### 3.4 Autonomous Content Execution Agencies (`GEO-EXEC-01`)
* **Status**: `OUT_OF_SCOPE` / `UNVALIDATED`.
* **Rationale**: Agencies focused strictly on mass AI content publishing (using tools like Byword or Koala) monetize article volume rather than visibility measurement and reporting. Their spend validates content generation, not monitoring.

---

## 4. Summary & Recommendation for Stage 1 Audit

The target segment `GEO-AGENCY-01` demonstrates clear empirical demarcation from adjacent categories. All 15 raw records in `evidence.jsonl` strictly document this profile or its direct tooling/substitute environment. No adjacent segments are used to inflate gate metrics.
