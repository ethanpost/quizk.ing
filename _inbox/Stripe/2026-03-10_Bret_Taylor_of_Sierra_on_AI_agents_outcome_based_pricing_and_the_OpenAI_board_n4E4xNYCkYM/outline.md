
Title: Bret Taylor of Sierra on AI Agents, Outcome-Based Pricing, and the OpenAI Board
Source: https://www.youtube.com/watch?v=n4E4xNYCkYM
Date: 2026-03-10
Folder: Stripe
---

# Detailed Outline

## I. Introduction: Bret Taylor’s background and context

- **Silicon Valley veteran:** Google Maps, Like button, co-CEO of Salesforce, Twitter board (Elon acquisition), chairman of OpenAI board
- **Current role:** Founder and CEO of Sierra--AI for customer service
- **Frame:** How AI is changing established companies

## II. Coding agents and the state of consumer AI

- **OpenClaw and hobbyist AI:** semi-rogue open-source project, WhatsApp/Telegram, "mildly unhinged and insecure"
- **Memory and interfaces**
  - **Mainstream apps (Gemini, ChatGPT):** blank slate, no memory
  - **OpenClaw:** proactive capability plus memory via "janky" markdown file (Memento-like), buggy compaction
  - **Contrast:** polished apps with no memory vs. insecure project that "almost remembers"
- **Why coding is a favorable domain for agents (Oct 2025 vs. early 2026 shift)**
  - **Context in one place:** textual files, not scattered systems
  - **Feedback loop:** compile errors, unit tests, integration tests, version history, code review--environment "designed for a robot"
  - **Harness engineering:** directory of product/architecture docs; agent's markdown as pointers; documentation as durable artifact (intention, PRD, customer problem) vs. transient code
  - **Markdown/file-system:** efficient mix of context and "random access" memory; vector DBs are more random-access, real memory is mixed
- **Terminal/Unix compatibility:** grep, Unix tools, no need for custom vector DBs; "software engineers made tools for ourselves first"
- **Multi-agent vs. single-agent with rich context**
  - **Critique of "multi-agent" whiteboard:** subagents with context, orchestrator with none -> robotic experience
  - **OpenClaw-style:** markdown files, "memory feels right"; repo-like expansiveness
  - **MCP skepticism:** agents need more context than MCP affords; context sharing may look more like OpenClaw over time
- **From codebase to "agent harness" for products**
  - **Social shopping / agentic commerce:** "action at a distance," APIs built years ago
  - **Patrick (Stripe):** "SSH into your Stripe account"--CLI, tail, pipe; now building for agentic world
  - **Unix elegance:** small tools, chainable; curl on Stripe homepage
  - **Future SaaS:** web app for rare human login + "agent harness" (skills, docs, rules)--Stripe expert knowledge as endpoint, not just API
  - **Dashboard vs. harness:** many dashboard switches have no API; "add the switch to the dashboard," harness describes when to use it; agents can handle complexity
  - **Tension:** more APIs for agents vs. agent with Chrome + login (Dario's race)

## III. Sierra: AI agents for customer experience

- **What Sierra does:** companies build AI agents for customer experience--phone (replace IVR), digital chat; answer questions and take action
- **Scale and metrics:** ~$165M ARR (from $100M in seven quarters, $150M in eight); leader in space
- **Adoption pattern**
  - **Median:** one channel, few use cases first (e.g., phone for healthcare, first notice of loss for car insurance, chat for digital-native)
  - **Most clients:** do both phone and digital; one team once telephone is digitized (e.g., SiriusXM: Harmony on phone and web)
  - **"Glimpse of the future":** Rocket Mortgage--Redfin (search home), Rocket (originate mortgage), Mr. Cooper (service); end-to-end product usage, not just support
- **"Digital front door":** company's primary AI agent as majority of digital interactions; "digital" now includes telephone
- **Economics of customer service**
  - **Traditionally cost center:** $10-$20 per call (or more), limits who can get phone support (e.g., Google)
  - **AI:** ~10-20 cents (or 1-2 cents) per "call" -> affordable great experience for more customers, including less profitable ones
  - **Subscription businesses:** same service budget -> many more conversations -> reduce churn, improve LTV
  - **Competitive dynamics:** when all have same tech, adoption is imperative not advantage; second/third-order effects (e.g., ATM didn't reduce branches--reallocated labor)
- **Healthcare example:** payers, providers, revenue cycle (R1); AI agents on both sides, English over PSTN--"TCP/IP and English over PSTN"; no custom agent protocol needed
- **Design point:** agent harness optimized for multi-step context and procedures, not for human UI elegance; "harness for coding agent is very different than UI design"

## IV. Agentic UX and interfaces

- **Agent as primary interface:** not just "no web form"--conversational across WhatsApp, phone, smart speakers; "market share of digital interactions"
- **Device evolution:** PC -> browser -> smartphone/tablet -> voice/chat (and possibly 3D); additive, not full replacement
- **Possibility:** less screen-centric, less addictive interfaces if voice/agents absorb more interaction
- **Cost and resolution metrics (Sierra)**
  - **Mix of priorities:** some heavy cost savings (e.g., Ramp ~90% automated, 70-90% range)
  - **Escalated cases:** can be harder -> average handle time up; agent satisfaction can rise (harder problems only)
  - **Jevons paradox:** one retailer's volume went up almost as much as savings--delightful agent -> more conversations; CEO valued "listening to clients"
  - **Top-line:** NPS and positioning often preferred over pure cost savings
- **"If you don't launch a website" (1994):** parity is table stakes; AI savings -> consumer surplus in competitive markets unless monopoly
- **Standout adoption:** Rocket (Varun, Shawn Malhotra)--reimagining home ownership journey with AI; "iPhone moment" for shifting competitive equilibrium (e.g., telcos, SoftBank)

## V. Building support agents: knowledge and guardrails

- **Customer service != codebase:** context not in one textual repo; "domain-specific language for specifying customer experience"
- **Journeys:** end-to-end customer journey, tools and information needed for success
- **Reasoning as breakthrough vs. old chatbots:** step-by-step reasoning, handling conflicting/duplicate data across systems ("what does a person do? They think about it")
- **LLM's innate knowledge:** e.g., Sonos + Wi-Fi--models have seen "every possible Wi-Fi problem"; training on human knowledge as starting point
- **Niche domains:** e.g., deep medical device--train heavily; well-known brands harder to ground (LLM "I got this") than obscure ones
- **Constellation of models / supervisor pattern:** goals and guardrails (not fixed steps); supervisor inspects reasoning, forces lookups, sends back "redo"; layering 90% x 90% -> ~99%
- **Agent Studio:** configure goals and guardrails; evals and tests; abstract complexity from clients
- **Sierra launch:** Feb 13, 2024 (~two years at time of interview)

## VI. Co-developing with the models

- **Building with planned obsolescence:** "so much of what we write we plan to throw out"; models will commoditize capabilities
- **Chain of thought:** Google paper before o1; RL on chain of thought (OpenAI); Sierra used CoT early
- **Example:** Cantonese voice--Sierra best today, likely commoditized in a few years; sell on technology now, on product later (like multi-tenant DB in early SaaS)
- **Avoiding "precious code" culture:** teams that treat obsoleted code as precious will fall behind; same for legacy vendor lock-in (cloud laggards)
- **Public markets:** software valuations down 20-30%; "SaaSpocalypse" framing

## VII. Software valuations and "SaaSpocalypse"

- **Two views:** (1) valuations were long-dated, more uncertainty -> re-rate rational; (2) agentic production doesn't yet build a Workday (Anthropic installed Workday)
- **Taylor:** rational but overblown; sector-level uncertainty, not necessarily every company; "vibe code in a weekend" was never the real moat
- **Moats:** compliance, relationships, fraud, distribution (AEs, channel), "no one gets fired for buying IBM," network effects
- **Risks to value:** (1) build vs. buy shifts (marginal cost of software down); (2) systems of record
- **Systems of record (ERP, CRM, etc.):** gravitational center by department; "collect taxes" from ecosystem; revenue expansion
- **Agents as labor:** is the database still the center, or the process the agent runs? Marketing: DB of customers vs. agent driving more leads; CRM: agent carving territories with no one logging in
- **Taylor's framing:** agents as "system of record of a process"; durability: ledger/ERP more durable, "system of engagement" less; agents plucking from many sources may weaken "data in one place" advantage
- **Bull case:** incumbents have right to win (scale, sales); race is whether smaller players build differentiated scale before incumbents adapt (disruption of own model is hard)
- **Annuity and DCF:** if ARR isn't assumed stable, PE-style "slow growth SaaS" math changes; "weighing machine" vs. "voting machine"
- **Microsoft analogy:** turnaround with Azure, OpenAI; individual companies can execute

## VIII. Outcome-based pricing

- **Sierra model:** resolved case (no human) = pre-negotiated rate; escalation to human = free; sales = commission; align interests where possible
- **Analogy:** impression-based -> CPC (and pay-per-install); charge for outcome, not input
- **Outcomes vs. usage:** token use not well correlated with value (e.g., "negative lines of code"); outcomes-based = align with business result; efficiency (fewer tokens for same outcome) is vendor's problem
- **Growth:** making product better, not just selling more capacity
- **Beyond support:** product usage (e.g., home shopping) harder to tie to single outcome; aspiration: agents that "drive home ownership over time," territory-like
- **Accountability:** old world--software vs. implementation vs. usage, "success has a thousand fathers"; outcomes-based pulls vendor into last mile, skin in the game
- **ERP analogy:** multi-year, "invading Russia"; outcomes-based encourages helping client succeed
- **Stripe:** outcome-based where possible; same incentive as customer (e.g., pushing local payment methods, features)

## IX. Is Sierra "short AGI?"

- **Question:** building things to throw away as models improve--is Sierra short the underlying tech?
- **Taylor:** applied AI belief; companies buy solutions, not models or raw software
- **Cloud analogy:** Amazon/Microsoft don't do everything; nuance by department, GTM, ecosystem; "coding the software wasn't necessarily the hard part"
- **Buyers:** GPT/Claude sold to different buyer than CFO/Chief Customer Officer; software orients around departments and buyers
- **If model development paused:** "trillions of dollars of economic value" still to realize; mature applied AI (e.g., CFO buys agent to onboard vendors) could accelerate that
- **Lack of applied AI companies as impediment:** many startups "rote tools around AI" vs. "agents for boring but important" processes
- **Sierra's edge:** best tech today; long-term value in product (workflows, customer experience, sales optimization), purpose-built for those teams
- **"We've never lived in a world where software engineering was the most plentiful" asset**

## X. AI productivity and where it shows up

- **Atomic unit:** process, not person; AI good at digital tasks (prep for podcast, meeting), not "get coffee" (no robotics)
- **Wrong frame:** "AI replacing people"; AI is in digital world; many jobs involve physical or multi-system work
- **Example:** onboarding a supplier--legal, procurement, IT, sponsor; median 17 days -> could optimize to 17 hours with PM + AI, but "we ship our org charts"--no one owns the process
- **Reimagining companies:** organize around processes with owners and KPIs who apply AI, not just by department
- **Coding:** clear productivity gains; engineers tool-obsessed, diving in
- **Flower shop / local business:** superintelligence helps some, but someone still clips stems, arranges, greets; much of economy not maximally absorbent of pure intelligence
- **Finance:** highly digital (ledgers, data)--meaningful; wet labs, ships, physical logistics--slower
- **White-collar knowledge work:** finance, legal--potential uplift; "by department" vs. "by process" is key
- **Narrow domains:** "improve legal redlining" = hard science; "automate onboarding for our 90% of suppliers with rigid terms" = narrower, "turn science into engineering"
- **Barrier:** applied AI market immaturity; hope for step change as it matures
- **Copilot:** incremental; "we're AI now" without process ownership is insufficient

## XI. How to structure a tech business post-AI

- **Canonical playbook:** engineering/product/design ratios, go-to-market, pipeline coverage; shared recipe across Silicon Valley
- **Tech leads over engineering managers:** Google, Facebook--product review with tech lead + PM; worse software often "up the chain"
- **"Product engineer" (or similar):** taste + infrastructure grasp + deep customer understanding + Codex -> "worth a thousand X"; produce valuable products with relative autonomy
- **Generalists:** often sidelined as companies specialize; with AI, high-agency, customer-caring, "care period" people "massively ascendant" (exoskeleton); same at Stripe
- **Work ethic:** "everyone who really used it works harder"--can do so much, novelty may wear off
- **New role:** "minister without portfolio," product/design/engineer blend; flatter orgs as impact per person grows
- **Org structure:** functional vs. business unit pendulum; "one reorg away"; if these people are central, how to organize is blurry

## XII. Board and leadership experience

- **Twitter board (Elon takeover):** public spotlight, mainstream attention; Taylor realized he prefers building (enterprise software); conflict "didn't fill my bucket"
- **X (Twitter) headcount:** 80-85% fewer people; eng/product/design ~50; service works, new features ship; "size of team does not produce linearly greater outcomes"; two-pizza teams; "clever but not smart" if competitor wins with more people
- **OpenAI board:** joined after Sam firing as agreed mediator; chairman; built board "from scratch" (bulk add)
- **Learnings:** (1) AI research inspiring--everyone aiming for safe AGI; (2) first not-for-profit board--fiduciary to mission (AGI benefits humanity), not shareholders; (3) board composition: nonprofit, safety, economic impact, infrastructure/finance expertise
- **"Have you considered you are the problem?"** Taylor joined after the drama; "hands clean"

## XIII. AI predictions for 2026

- **Scientific breakthrough:** AI breakthrough that breaks into mainstream awareness (beyond "interventional manifold"); e.g., math proofs -> something like AlphaGo/Kasparov; positive narrative alongside economic and risk discourse
- **Mainstream adoption:** by consumers and companies; "year of adoption of agents"; ChatGPT growth; OpenClaw-style agents from niche to more mainstream
- **Most Silicon Valley companies won't write code by hand:** "obvious" now, bold four months ago; state change; diffusion beyond Silicon Valley will take time

## XIV. Stripe Sessions

- **Conference (April):** see "wave of AI agents" up close; internet economy, production use, agents in commerce; code "Cheeky Pint" for 50% off at sessions.stripe.com

# Core Ideas

* AI agents need rich, shared context (e.g., markdown-style memory, repo-like docs); multi-agent designs that starve the orchestrator of context produce robotic experiences, while simple file-based memory can feel “right.”
* Coding is uniquely suited to agents (context in one place, tests, version control); “harness engineering” and documentation as durable artifacts may generalize—future SaaS may expose “agent harnesses” (skills, docs, rules) alongside APIs.
* Sierra powers companies’ primary AI agents for customer experience (phone, chat, etc.); economics shift from “cost center” to affordable, scalable service and new competitive dynamics (adoption as imperative, second-order effects).
* Outcome-based pricing aligns vendor and client (pay per resolved case or sale); it differs from usage-based (tokens ≠ value) and creates accountability through the last mile of implementation.
* Applied AI (solutions for specific buyers and processes) has enduring value; “short AGI” underrates product, GTM, and departmental nuance—and if model progress paused, trillions in value remain to be realized.
* AI productivity is about processes and ownership, not just “replace people” or “Copilot everywhere”; organizing by process with clear accountability and narrowing domains (e.g., supplier onboarding) turns science into engineering.
* High-agency, customer-caring generalists gain an “exoskeleton” with AI; tech leads and product-minded engineers who deeply understand customers become disproportionately valuable; org structures may flatten.
* Systems of record may be challenged where agents perform labor and value lives in the process or outcome rather than the database; ledger/ERP more durable, “system of engagement” less so.
* Software valuations reflect sector uncertainty (rational, possibly overblown); moats are distribution, relationships, compliance—not “could have been coded in a weekend.”

# Key Terms

* **Agent harness** — The context, skills, documentation, and rules given to an AI agent (e.g., for a codebase or a product like Stripe) so it can act effectively; distinct from raw API or UI.
* **Outcome-based pricing** — Charging for business results (e.g., resolved support case, sale) rather than usage (tokens) or seats; aligns vendor and client.
* **Harness engineering** — Designing the environment and documentation around an agent (e.g., directory of product/architecture, agent’s memory as pointers) so it can work reliably.
* **System of record** — The canonical database or platform for a domain (e.g., ERP for finance, CRM for sales); “gravitational center” that other apps integrate with.
* **Jevons paradox** — When efficiency (e.g., better chatbot) increases usage so much that total cost or activity rises (e.g., more conversations, same or higher spend).
* **MCP (Model Context Protocol)** — Protocol for exposing tools/context to agents; Taylor is skeptical that it provides enough context compared to richer, OpenClaw-style setups.
* **Chain of thought** — Having the model reason step-by-step; improves robustness; later extended with RL (e.g., o1).
* **Constellation of models / supervisor** — Using a second model to inspect and correct the first (e.g., “go look up the policy”) to improve reliability (e.g., 90% × 90% → ~99%).
* **ARR** — Annual recurring revenue; standard SaaS metric.
* **Net promoter score (NPS)** — Customer satisfaction/loyalty metric.

# People

* **Bret Taylor** — Guest; co-creator of Google Maps, invented Like button, ex–co-CEO Salesforce, ex–Twitter board (Elon deal), chairman of OpenAI board, CEO/founder of Sierra.
* **Patrick (Collison)** — Co-founder of Stripe; referenced as wanting “SSH into your Stripe account” (CLI, tail, pipe).
* **Dario Amodei** — Referenced re: race between “more APIs for agents” vs. “agent with Chrome + login.”
* **Varun** — CEO of Rocket Mortgage (Sierra customer).
* **Shawn Malhotra** — CTO of Rocket Mortgage.
* **Eric** — From Ramp (recent visitor at Stripe).
* **Sam (Altman)** — OpenAI CEO; referenced in context of board firing and Taylor joining as mediator.
* **Sundar (Pichai)** — Referenced re: ease of calling him vs. getting Google customer service.
* **Nikita Bier** — Tweet about X/Twitter eng/product/design being ~50 people.
* **Jeff Bezos** — “Two pizza” team concept.
* **Arvind (Krishna)** — IBM CEO; “no one gets fired for buying IBM” (IBM doing well under him).
* **John** — Hypothetical AI agent in Sierra example (supervisor tells “John” to look up policy).

# Dates / Periods

* **Feb 13, 2024** — Sierra company launch (~two years before interview).
* **Oct 2025 vs. early 2026** — Conversation about coding agents would be “materially different”; coding agents transformed in “past four months.”
* **2026** — Interview and predictions: year of agent adoption, scientific breakthrough in mainstream, most Silicon Valley companies not writing code by hand.
* **~2018** — Pre-LLM chatbot hype wave ( “multiple choice machines” ).
* **1994** — Analogy: “If you don’t launch a website” for banks; internet as table stakes.
* **~100 years** — PSTN; “English over PSTN” for agent-to-agent phone.
* **“Three months back” / “a day ago”** — Public markets deeming software 20–30% less valuable (SaaSpocalypse).

# Geography

* **Silicon Valley** — Where Taylor and Stripe operate; “canonical” company-building playbook; where “most companies won’t write code by hand” by end of 2026.
* **San Francisco** — Startups “doing relatively rote tools around AI” rather than agents for “boring but important” processes.
* **Detroit** — Rocket Mortgage (Rocket, Redfin, Mr. Cooper) as “great Detroit company.”
* **Japan** — SoftBank and “iPhone moment” for telcos (competitive equilibrium shift).
* **Hong Kong** — Bank (Sierra client) with Cantonese voice support.

# Expected Outcome

After taking notes from this outline and watching or listening to the source material, an **A+ student** would be capable of:

### Knowing

* Why coding is a favorable domain for AI agents (single context, tests, version control) and how “harness engineering” and documentation-as-artifact extend the idea to other products.
* The difference between multi-agent designs that hoard context in subagents vs. single (or few) agents with rich, shared context (e.g., OpenClaw-style memory).
* What Sierra does (AI agents for customer experience across phone/chat), how adoption typically starts (one channel, few use cases) and scales, and the economics (cost per contact, NPS, churn, “imperative vs. advantage”).
* How outcome-based pricing works (e.g., per resolved case, per sale), why it differs from usage-based (tokens ≠ value), and how it creates alignment and accountability.
* Taylor’s argument for applied AI (solutions for buyers/departments, not just models) and why “short AGI” may underrate product, GTM, and process ownership.
* Why AI productivity is best thought of at the process level with clear ownership, and why “by department” or “Copilot for everyone” without that can underdeliver.
* The supervisor/constellation-of-models idea and how it improves reliability (e.g., 90% × 90%).
* How systems of record (ERP, CRM) could be challenged when agents perform labor and value shifts toward process/outcome vs. “data in one place.”
* The “SaaSpocalypse” debate: rationality of software re-rating, moats (distribution, compliance, relationships), and durability of ledger vs. engagement systems.

### Reciting

* In 30–60 seconds: explain what an “agent harness” is and why it might matter more than raw API or UI for future SaaS (e.g., Stripe).
* In 30–60 seconds: define outcome-based pricing and give one example (e.g., resolved support case vs. escalation); why it aligns vendor and client.
* In 30–60 seconds: summarize why Taylor is bullish on applied AI and why “if we paused model development, trillions of dollars of value” could still be realized.
* In 30–60 seconds: state the “atomic unit of productivity” (process, not person) and why organizing by process and narrowing the domain (e.g., supplier onboarding) matters for AI adoption.

### Sharing

* Teach a colleague how to think about “multi-agent vs. single agent with context” using the OpenClaw vs. MCP and “orchestrator with no context” examples.
* Explain to a product or eng lead how Sierra’s “journeys,” goals/guardrails, and supervisor pattern work to improve reliability and grounding (including for well-known brands).
* Describe to a finance or ops person how outcome-based pricing changes vendor incentives and implementation (skin in the game, last mile) and how it differs from usage-based.
* Outline for a leadership team why “AI productivity” might show up faster when the company is organized around processes with owners and narrow domains, rather than only “Copilot per department.”

### Conversing

* Debate whether “most companies in Silicon Valley won’t write code by hand” by end of 2026 is plausible and what “writing code” might mean (e.g., editing vs. generating).
* Compare Taylor’s “systems of record vs. process/outcome” view with a defender of incumbents (Salesforce, Workday, etc.) and their moats.
* Discuss whether the software valuation reset is mostly “rational uncertainty” or overblown, using his points about moats, annuity, and individual company execution (e.g., Microsoft).
* Connect the “high-agency generalist with exoskeleton” idea to your own org: who benefits, how roles might change, and how flatter or process-oriented structure could look.
* Relate outcome-based pricing to other domains (e.g., legal, consulting) and where it might or might not be feasible.
