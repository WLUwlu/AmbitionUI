# Economics of GPU Rental Markets

**Mode:** Token Waster verbose (`#verbose`)  
**Template:** Mandatory 6-section verbose analysis  
**Subject:** Supply, demand, pricing, and institutional structure of commoditized GPU compute rental

---

## Section I — Framing, Scope, and Analytical Premises

GPU rental markets sit at an unusual intersection of industrial economics, platform strategy, and semiconductor geopolitics. The headline metric—dollars per GPU-hour—suggests a fungible commodity comparable to electricity or crude oil. In practice, GPU rental is a **layered market** in which identical silicon can trade at price ratios of 5:1 or greater depending on who is buying, for what workload, under which contract, and during which supply regime. Treating "the GPU rental market" as singular is the first analytical error most observers make.

This analysis examines GPU rental as **time-limited access to depreciating accelerator capital**, bundled with implicit services: power delivery, cooling headroom, network fabric, software compatibility, operational reliability, regulatory compliance, and—during shortage periods—**allocation priority**. The renter is not merely buying FLOPs; they are buying a probability distribution over completed work, with variance driven by eviction policies, driver drift, interconnect topology, and provider solvency.

**Scope:** General-purpose NVIDIA-class GPU rental for machine learning training, fine-tuning, and batch inference. Custom AI accelerators (Google TPU, Amazon Trainium/Inferentia, Microsoft Maia, Groq LPUs) enter the analysis only where they alter GPU supply, demand substitution, or pricing psychology. Cryptocurrency mining appears as a cross-demand channel. Consumer gaming GPUs appear where they supply decentralized rental inventory.

**Out of scope:** Detailed financial modeling of individual providers, real-time price indices, and jurisdiction-specific tax treatment—except where they materially shift equilibrium.

**Core analytical units:**

| Unit | Meaning | Why it matters |
|------|---------|----------------|
| $/GPU-hour (headline) | Sticker rental rate | Procurement shorthand; often misleading |
| Effective $/GPU-hour | All-in cost including storage, egress, orchestration, downtime | True economic comparison |
| Utilization (provider) | Sold GPU-hours ÷ available GPU-hours | Determines provider survival |
| Utilization (renter) | Active compute ÷ reserved compute | Determines rent-vs-own breakeven |
| $/kWh at site | Locational energy input | 20–50% of marginal cost at H100 density |
| Topology tier | PCIe vs NVLink vs InfiniBand | Converts chip price into cluster price |
| Contract elasticity | Spot → multi-year dedicated | Allocates obsolescence and scarcity risk |

**Premise 1 — Commodity hardware, differentiated service:** At the CUDA layer, an H100 is an H100. At the service layer, an H100 on a peer host with residential uplink is not substitutable for an H100 in a liquid-cooled rack with InfiniBand fat-tree and SOC 2 attestation. Fungibility is **conditional on workload tolerance for variance**.

**Premise 2 — Scarcity suspends price discovery:** When aggregate demand exceeds allocatable supply—as in the 2023–2025 H100 cycle—prices cease to clear markets at the margin. Queue position, prepayment, geographic eligibility, export-control compliance, and relationship capital replace marginal-cost pricing. Models assuming competitive equilibrium underpredict realized prices and overpredict spot availability.

**Premise 3 — Hyperscalers set the reference frame:** AWS, Azure, and Google Cloud establish the mental anchor for enterprise procurement even when specialists and marketplaces undercut them by 50–80% on raw compute. This **price umbrella** persists because switching costs, compliance familiarity, and existing cloud commitments outweigh hourly savings for many buyers.

**Premise 4 — Workloads bifurcate the market permanently:** Frontier pre-training (cluster-scale, communication-bound, contract-heavy) and inference/fine-tuning (latency-sensitive, bursty, fractional-GPU friendly) obey different pricing logics, buyer profiles, and hardware preferences. A single-market narrative produces incoherent strategy.

**Premise 5 — Depreciation velocity dominates provider returns:** Frontier GPU generations obsolesce in 18–36 months. Rental economics resemble aviation spare-engine leasing or container shipping more than SaaS: capital intensity, cyclical utilization, and residual-value risk determine viability—not gross margin on metered hours alone.

**Premise 6 — Cross-demand channels are non-negligible:** GPU rental competes with any workload monetizing compute-per-watt—historically proof-of-work mining, increasingly real-time rendering and generative media. Demand cross-elasticity injects supply volatility unrelated to ML fundamentals.

---

## Section II — Historical Evolution and Market Genesis

The contemporary GPU rental market did not emerge fully formed. It evolved through six overlapping phases, each depositing institutional structure, pricing mechanisms, and failure modes still visible today.

### Phase 1: Cloud attachment product (2010–2016)

Amazon Web Services and competitors introduced GPU-backed instances as **accelerator attachments** to CPU-centric cloud platforms. Early Tesla and Kepler data-center GPUs served oil-and-gas simulation, molecular dynamics, and the first post-AlexNet deep learning experiments. Pricing was **administrative**: public list rates, reserved-instance discounts, enterprise negotiation—not market clearing.

The template established: GPUs as metered add-ons within bundled cloud ecosystems, with opaque cross-subsidies between compute, storage, egress, and managed services. Rental was almost always more expensive per hour than owned hardware at high utilization, but ownership required data-center operations most research teams lacked. The market was small, concentrated, and provider-driven.

### Phase 2: Deep learning scaling and interruptible pricing (2016–2020)

ResNet, BERT, and early Transformer architectures transformed GPU demand from episodic HPC bursts into continuous experimentation loops. Hyperscalers expanded V100 and T4 instance families. AWS Spot Instances—and Azure/GCP equivalents—introduced **interruptibility as a priced dimension**: 50–75% discounts in exchange for two-minute eviction notices.

Spot pricing made **utilization risk tradable**. Providers monetized idle fleet; renters absorbed checkpoint engineering costs. The spot/on-demand/reserved spectrum became the first widely understood trade-off in GPU rental. Consumer GPU accumulation (gaming cards) seeded latent supply for later peer-to-peer markets, though bandwidth asymmetry and absent trust infrastructure kept this marginal.

### Phase 3: Cryptocurrency mining as competing bid (2017–2022)

Proof-of-work mining—especially Ethereum GPU mining before the September 2022 merge—created a **parallel demand channel** with different economics: willingness to pay tracked token prices and network difficulty, not model accuracy; operations tolerated high failure rates; hardware selection prioritized hash-per-watt on retail cards.

During the 2020–2021 crypto peak, mining bids absorbed GPU supply, inflated secondary-market prices, and lengthened OEM queues. Cloud providers faced pressure to reserve capacity for enterprise contracts. The 2022 crypto collapse produced a **reverse supply shock**: used RTX 3090s and ex-mining cards flooded secondary markets, depressing decentralized rental rates and creating temporary arbitrage for budget ML teams willing to accept reliability risk.

Enduring lesson: GPU rental demand is **not ML-exclusive**. Any workload monetizing flops-per-watt competes for the same silicon.

### Phase 4: Decentralized marketplace maturation (2019–present)

Platforms including Vast.ai, RunPod, Salad, and TensorDock implemented two-sided matching between individual hosts and renters, containerizing heterogeneous hardware behind cloud-like APIs. Innovations included auction-adjacent hourly pricing, reputation systems substituting for SLAs, and geographic arbitrage routing workloads to low power-cost regions (Nordic hydro, Quebec, US Pacific Northwest).

Hosts monetized sunk capex on underutilized hardware; renters accessed compute at 60–85% discounts versus hyperscaler list prices during competitive periods—excluding reliability and compliance premiums. Marketplace take rates of 5–15% positioned platforms as **liquidity aggregators**, not fleet owners: asset-light, trust-sensitive, scale-dependent economics resembling short-term rental platforms more than hotel chains.

### Phase 5: LLM cluster era and H100 rationing (2022–2025)

ChatGPT and successor models converted GPU demand from distributed experimentation into **concentrated cluster procurement**. Frontier training required thousands of interconnected H100s with NVLink and InfiniBand—not single-instance rentals. NVIDIA allocation politics, TSMC capacity constraints, and hyperscaler pre-commitments produced multi-year shortage characterized by:

- Lead times stretching from weeks to quarters
- Spot market thinning for premium silicon
- AI-native specialists (CoreWeave, Lambda, Crusoe) raising billions for direct hardware purchases
- Contract pricing decoupling from marginal energy cost

This crystallized **market bifurcation**: oligopolistic cluster rental (few providers, relationship-driven allocation) versus competitive single-GPU rental (marketplaces, residual spot). Hyperscaler investment in custom silicon (TPU, Trainium, Maia) accelerated as a long-run demand-side threat to general-purpose GPU rental.

### Phase 6: Normalization signals and structural maturation (2025–)

Early normalization signals include lengthening H100 marketplace availability, Blackwell transition pricing uncertainty, and inference-optimized instance families (L4, L40S) priced for sustained utilization rather than peak FLOPs. Absolute rental revenue grows as more GPUs deploy, but rental shrinks as a **fraction of total AI spend** as managed APIs and internal hyperscaler capacity absorb frontier workloads.

Historical through-line: each phase added a pricing dimension (interruptibility, reputation, fabric topology, allocation priority) that the headline $/GPU-hour compresses away—producing systematic mispricing by buyers who compare only sticker rates.

---

## Section III — Economic Mechanics and Market Structure

### Cost structure decomposition

Commercial GPU hosting at H100-class density approximates:

```
$/GPU-hour ≈ (Capex amortization + Power + Cooling + Staff + Network + Margin) ÷ Utilization-adjusted hours
```

**Capex amortization** dominates at frontier generations. An H100 SXM module at $25,000–$35,000 amortized over 24–36 months at 70–85% utilization implies roughly $1.50–$3.50/GPU-hour before margin—assuming residual value holds. Faster-than-expected generational turnover (Hopper to Blackwell) collapses residual assumptions and retroactively raises effective amortization.

**Power** varies 5–10× by jurisdiction. An 8-GPU H100 node drawing 6–8 kW costs $0.24–0.32/hour at $0.04/kWh (industrial hydro) versus $1.08–1.44/hour at $0.18/kWh (retail European rates). Energy economics explain Nordic, Gulf-state, and Quebec hosting proliferation during the LLM boom.

**Cooling** scales nonlinearly with density. Air-cooled consumer-card hosts throttle under sustained ML loads; liquid-cooled racks enable higher utilization but require capex amortized alongside GPUs.

**Staff and orchestration** are fixed per rack, diluted by utilization. Managed platforms invest in container orchestration, ML images, and fabric provisioning—costs invisible in raw $/GPU-hour comparisons but decisive for teams without infrastructure engineers.

### Market segmentation

| Segment | Examples | Pricing | Primary buyers |
|---------|----------|---------|----------------|
| Hyperscale cloud | AWS, Azure, GCP | On-demand, reserved, spot | Enterprise with cloud contracts |
| AI-native specialists | CoreWeave, Lambda, Crusoe | Monthly/annual dedicated | AI labs, funded startups |
| Decentralized marketplaces | Vast.ai, RunPod community, Salad | Hourly auction, reputation | Researchers, cost optimizers |
| Colocation bare metal | Equinix Metal, OVH, Hetzner | Monthly server/rack | Teams with ops capacity |

Each segment optimizes different **trust-cost trade-offs**. Hyperscalers sell compliance; marketplaces sell price and variety; specialists sell guaranteed topology and allocation priority.

### Utilization as existential metric

At 50% utilization, a provider pricing at marginal cost plus 15% margin may be loss-making after fixed costs. At 85%, the same pricing generates attractive returns. This drives **procyclical fleet expansion**: providers buy hardware at peak prices during booms; distressed inventory floods secondary markets during busts, compressing rates and bankrupting over-leveraged hosts. The cycle resembles shipping or semiconductor fab utilization—not SaaS margin stability.

### Interconnect and cluster economics

Single-GPU pricing misleads for frontier training. Eight H100s with NVLink and InfiniBand deliver qualitatively different throughput than eight isolated cards on Ethernet. Cluster pricing includes topology premiums (fat-tree vs torus), minimum node commitments, and dedicated-vs-shared fabric trade-offs. Renters optimizing $/TFLOP-hour on isolated cards systematically mis-procure for distributed training.

### Price discovery mechanisms

| Mechanism | Where | Strengths | Weaknesses |
|-----------|-------|-----------|------------|
| Administrative list pricing | Hyperscalers | Predictable, contractable | Sticky; may ignore scarcity |
| Spot/auction clearing | AWS Spot, Vast.ai | Reveals marginal willingness to pay | Volatile; correlated interruption |
| Negotiated enterprise contracts | CoreWeave, Lambda | Allocates scarcity via relationships | Opaque; excludes small buyers |
| Marketplace matching | RunPod, TensorDock | Aggregates fragmented supply | Quality heterogeneity; trust variance |

During shortage, negotiated allocation replaces spot clearing. Observing spot prices during rationing is informative but not representative of marginal transactions—analogous to oil spots during supply embargoes.

### Supply-side concentration and allocation politics

NVIDIA's direct allocation to hyperscalers, AI specialists, and OEM integrators creates **upstream bottlenecks** that downstream rental markets cannot price away. Providers without allocation relationships depend on secondary channels vulnerable to sudden cutoff. This upstream concentration is the structural source of scarcity rent during LLM-driven demand spikes.

---

## Section IV — Trade-offs and Strategic Tensions

### Rent versus own

**Rent when:** utilization is unpredictable (<40% sustained); hardware turnover exceeds depreciation horizon; operational expertise is absent or expensive; capital is better deployed in talent, data, or model development; compliance favors certified managed environments.

**Own when:** utilization exceeds 60–70% sustained over 18+ months; workloads are stable; direct OEM/NVIDIA relationships are accessible; power costs are structurally low; data sensitivity prohibits third-party hosting.

Breakeven analysis: renting H100 at $3–5/GPU-hour versus owning at ~$30,000/card with 24-month life implies breakeven around 55–70% utilization—before staff, power, and facility costs push the threshold higher. Inference-heavy workloads on efficiency-optimized cards (L4, A10) shift breakeven dramatically.

### Spot versus on-demand versus committed

| Contract | Price | Availability | Best for |
|----------|-------|--------------|----------|
| Spot/interruptible | Lowest (50–75% off) | None; eviction in minutes | Fault-tolerant batch, hyperparameter sweeps |
| On-demand | Reference | High for singles | Prototyping, unpredictable timelines |
| Reserved/monthly | 30–60% below on-demand | Medium | Sustained training, known schedules |
| Multi-year dedicated | Negotiated; scarcity premium | Highest | Frontier clusters, enterprise SLAs |

Critical tension: spot saves money until correlated eviction during demand spikes converts statistical bargains into project-killing tail events. Teams without checkpoint infrastructure should not optimize for spot.

### Centralized versus decentralized supply

Decentralized marketplaces offer price and variety but impose trust and variance costs: host reliability spans data-center-grade to residential broadband; security assumes container isolation without confidential computing; geographic distribution creates latency and residency complexity.

Centralized providers charge premiums for **variance reduction**—the same economic logic as insurance. The market persists in segmented equilibrium rather than converging to a single low-price pool.

### Training versus inference hardware selection

| Dimension | Training-optimized (H100, A100) | Inference-optimized (L4, L40S, T4) |
|-----------|--------------------------------|-------------------------------------|
| Peak FLOPs | High | Moderate |
| Memory bandwidth | Critical | Workload-dependent |
| Power density | High | Lower |
| $/hour | Premium | Discount |
| Availability during shortage | Constrained | More abundant |

Matching hardware generation to workload phase—frontier silicon for pre-training, efficiency silicon for inference—is a structural optimization invisible in undifferentiated $/GPU-hour comparisons.

### Multi-cloud versus single-provider concentration

Multi-cloud diversifies allocation risk but increases integration overhead: different APIs, networking, checkpoint formats, billing reconciliation. During shortage, multi-cloud can secure capacity unavailable from any single vendor—at engineering complexity small teams cannot absorb. The trade-off is **capacity optionality versus operational simplicity**.

### Build versus buy on the platform layer

Teams increasingly rent not raw GPUs but **managed training and inference platforms** (SageMaker, Vertex AI, Modal, Baseten). Abstraction collapses visible rental markets for users accepting constraints—even as absolute GPU deployment grows. The tension: lower operational burden versus reduced control, vendor lock-in, and opaque effective pricing.

---

## Section V — Edge Cases, Failure Modes, and Boundary Conditions

### Edge case 1: Egress and storage bill shock

Hyperscaler GPU instances advertise competitive compute rates but charge aggressively for egress and high-IOPS storage. Training runs generating terabytes of checkpoints can incur storage and transfer charges exceeding compute—a failure mode invisible in $/GPU-hour spreadsheets. Effective analysis must price **total workload economics**.

### Edge case 2: Correlated spot eviction

Spot instances assume independent interruption probability. Providers reclaim spot capacity en masse when reserved customers demand allocation—creating **correlated evictions** during exactly the periods when spot was cheapest. Fifty-percent spot savings can convert to one-hundred-percent project delay.

### Edge case 3: Checkpoint-dominated effective throughput

On unreliable hosts, 25–40% of wall-clock time may be checkpointing, uploading, and restarting. Quoted $/GPU-hour diverges from $/completed-training-step—a hidden multiplier on effective cost.

### Edge case 4: Host-side security and confidential computing gaps

Compromised hosts can inspect GPU memory, exfiltrate weights, or inject adversarial data unless confidential computing (TEEs, encrypted GPU memory) is deployed—still unevenly available. Markets underprice security risk until incidents reprice trust premiums.

### Edge case 5: Driver and firmware compatibility shocks

Uncoordinated driver updates break containers pinned to specific CUDA/PyTorch combinations. This compatibility externality is unpriced in hourly rates; enterprise clouds monetize curation through certified image libraries.

### Edge case 6: Unhedged power cost exposure

European energy volatility (2022 crisis) demonstrated hosts with floating power contracts exiting markets or imposing surcharges. Fixed-price rental contracts without power pass-through become **loss-making** when input costs spike—provider bankruptcy risk transfers to renters mid-contract.

### Edge case 7: Stranded infrastructure without GPU allocation

Data centers with power and cooling ready but without GPU delivery—due to allocation politics—represent stranded capital. Secondary-channel-dependent providers face sudden supply cutoff.

### Edge case 8: Algorithmic efficiency as demand destruction

Quantization, distillation, MoE sparsity, and architecture improvements reduce FLOPs per capability unit. Custom silicon further displaces GPU demand for specific workloads. Fleets amortizing on historical demand curves face **writedown risk** analogous to telecom fiber overbuild.

### Edge case 9: Export controls and gray markets

US semiconductor export restrictions segment global supply. Compliant hosting in authorized regions commands premiums; gray-market flows in restricted jurisdictions create **dual pricing structures** opaque to standard analysis.

### Edge case 10: Informal secondary markets and contract violation

Enterprises with reserved blocks resell unused capacity internally or through brokers—improving efficiency but creating legal exposure where assignment is restricted. Markets exist in semi-visible layers not captured in public indices.

### Edge case 11: Fractional GPU and MIG partitioning illusions

MIG and fractional allocation promise efficiency for small workloads, but partition boundaries and scheduling overhead can reduce effective throughput below naive division. Comparing $/GB-hour across full-GPU and fractional offerings mis-ranks options.

### Edge case 12: Inference autoscaling latency tax

Serverless GPU offerings charge cold-start provisioning and scale-to-zero idle periods. Bursty traffic may pay more per inference than sustained-rental baselines—a pricing inversion invisible in $/GPU-hour comparisons.

### Edge case 13: Noisy-neighbor fabric contention

Shared InfiniBand or NVLink fabrics introduce contention invisible in per-GPU pricing. Dedicated fabric clusters cost more but deliver predictable all-reduce latency—a quality dimension unpriced in spot marketplace listings.

### Failure mode synthesis

GPU rental markets fail visibly when: (a) rationing replaces price clearing; (b) spot correlation destroys interruptibility assumptions; (c) hidden egress/storage charges dominate compute; (d) depreciation outpaces realized utilization; (e) trust breakdown triggers renter flight from peer-to-peer layers; (f) power volatility bankrupts unhedged hosts; (g) custom silicon obsoletes fleet before amortization completes. Characteristic signatures—queue lengths instead of prices, checkpoint-heavy logs, bill-shock post-mortems, distressed hardware fire sales—distinguish cyclical stress from competitive equilibrium.

---

## Section VI — Self-Critique and Synthesis

### Self-critique

**Limitation 1 — Transactional price opacity.** Public list prices and marketplace medians are not execution prices during shortage. Enterprise discounts, prepay bundles, and informal subletting create 2–5× spreads invisible externally. This analysis emphasizes structural forces over precise spreads that may stale within weeks.

**Limitation 2 — FLOP normalization fallacy.** Peak TFLOPs ignore memory capacity, bandwidth, tensor-core precision modes (FP8, BF16), and interconnect topology. Effective economics are workload-specific; $/TFLOP-hour shorthand systematically mis-ranks memory-bound and communication-bound training.

**Limitation 3 — Hyperscaler internal economics unknowable.** Observed list prices may reflect strategic rationing, not cost-plus margins. Internal transfer prices to first-party ML teams are undisclosed—limiting confidence in competitive positioning conclusions.

**Limitation 4 — Path dependence on 2023–2025 scarcity psychology.** Buy-versus-rent recommendations assume continuation of allocation constraints. Loosened NVIDIA supply, successful custom-silicon displacement, or model-efficiency breakthroughs could invalidate shortage-calibrated conclusions.

**Limitation 5 — Geographic oversimplification.** Power costs, tax incentives, cooling advantages, and export-control regimes vary sharply by jurisdiction. US- and Western Europe-centric framing underweights hosting in Southeast Asia, Gulf states, and Latin America where policy arbitrage reshapes supply.

**Limitation 6 — Labor costs neglected relative to hardware.** For teams under roughly twenty ML engineers, MLOps salaries often exceed GPU rental spend. Optimizing $/GPU-hour while ignoring engineer time misallocates organizational attention—a procurement pathology this document risks reinforcing.

**Limitation 7 — Environmental externalities underdeveloped.** Dense GPU fleets carry carbon and water footprints varying by energy mix. Sustainability pricing may grow in salience; this analysis treats energy primarily as input cost rather than externality.

**Limitation 8 — Blackwell transition uncertainty.** Conclusions about Hopper-era economics may not transfer cleanly to Blackwell rollout dynamics—pricing, allocation, and obsolescence patterns still forming.

**What would increase confidence:** Provider utilization disclosures, secondary-market transaction logs, regional power contract structures, NVIDIA allocation by channel, and longitudinal data linking spot interruption correlation to capacity events.

### Synthesis

GPU rental markets combine **commodity hardware economics with platform differentiation, extreme depreciation velocity, and cyclical scarcity rents**. Eight structural conclusions:

1. **Depreciation sets the floor; scarcity sets the ceiling.** In competitive periods, providers price near variable cost plus minimum return on depreciating assets. During allocation constraints, scarcity rent dominates marginal cost—rates reflect queue priority and relationship capital, not watts consumed.

2. **Energy and location are silent oligarchy inputs.** Providers with structural energy advantages survive price wars that bankrupt hosts paying retail electricity on dense H100 racks.

3. **Workload bifurcation is permanent.** Frontier cluster training (oligopolistic, contract-heavy, interconnect-defined) and inference/fine-tuning (competitive, autoscaling, fractional-GPU friendly) require separate analytical lenses.

4. **Hyperscalers anchor expectations; specialists and marketplaces fill residuals.** Enterprise procurement benchmarks against AWS/Azure/GCP even when alternatives undercut dramatically—creating persistent price umbrella effects.

5. **Trust, compliance, and compatibility are priced implicitly until they are not.** Peer-to-peer layers underprice security and SLA variance; enterprise clouds monetize trust through premium tiers—a segmentation likely to persist.

6. **Cross-demand from crypto and gaming remains latent volatility.** Any resurgence in GPU-minable proof-of-work or consumer hardware scarcity ripples into ML rental availability with months of lag.

7. **Long-run maturation favors abstraction layers.** Managed inference APIs and serverless GPU offerings collapse visible rental markets for users accepting abstraction—even as absolute deployment grows.

8. **Utilization is the provider's existential metric; effective cost is the renter's.** Both sides optimize against headline prices obscuring the variables that determine outcomes.

**For renters:** Match contract type to utilization predictability and failure tolerance. Price total workload economics—compute plus storage, egress, orchestration, and engineer intervention. Treat spot as statistical, not guaranteed. During shortage, prioritize binding availability over marginal hourly savings. Match hardware generation to workload phase.

**For hosts and providers:** Utilization rate is existential; idle depreciating hardware destroys equity. Hedge power on multi-year horizons. Diversify customer segments to avoid single-channel collapse. Invest in interconnect and orchestration UX for training clusters—renters pay for completed runs, not socket occupancy.

**For observers and policymakers:** GPU rental resembles bulk shipping or aviation leasing—cyclical, capex-heavy, with visible inventory dynamics—while retaining a long-tail marketplace for price-sensitive experimenters. Export controls and energy policy intervene as non-market allocation mechanisms; pure competitive analysis is locally valid but globally incomplete.

The equilibrium irony: as AI infrastructure matures, absolute rental revenue may grow while **fraction of total AI spend** on raw GPU-hours shrinks—inference shifts to managed APIs, training consolidates among players internalizing hardware, and rental returns to its historical role as **overflow infrastructure for marginal participants**—until the next frontier workload wave resets scarcity and the cycle begins again.

---

*End of verbose analysis.*
