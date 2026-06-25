# Token Waster Verbose Mode (#verbose)

## A Comprehensive Multi-Section Analysis of the History of Programming Language Paradigms

---

## Section 1: Scope, Definitions, and Conceptual Foundations

Programming language paradigms are often discussed as if they were stable, mutually exclusive camps — functional versus object-oriented versus imperative, as though choosing one obligates a developer to a lifelong affiliation. That framing is pedagogically convenient but historically inaccurate. A paradigm, in the sense used throughout this analysis, is a constellation of ideas about how programs should be structured, how change over time should be represented, and how human reasoning should map onto machine behavior. Paradigms are not identical to languages. They are intellectual frameworks that languages partially implement, partially reject, and frequently combine.

This document examines the history of programming paradigms as an evolving negotiation between hardware realities, mathematical aesthetics, organizational pressures, and the stubborn limits of human attention. It is intentionally verbose: length here serves the goal of tracing nuance that compressed summaries flatten. The analysis focuses on general-purpose programming languages and the mainstream intellectual currents that shaped them, while acknowledging that domain-specific languages, spreadsheet programming, hardware description languages, and proof assistants constitute parallel histories that intersect only briefly with the narrative below.

Five paradigm families receive sustained attention:

- **Imperative and structured/procedural** models, which treat programs as sequences of commands that mutate state.
- **Object-oriented** models, which bundle state and behavior and emphasize message passing, encapsulation, and polymorphism.
- **Functional** models, which elevate expression evaluation, immutability, and function composition.
- **Logic and declarative** models, which specify relations or constraints and delegate search to an engine.
- **Concurrent and distributed** models, which treat interaction, isolation, and partial failure as first-class design problems.

Three conceptual axes organize the historical material:

1. **Control versus specification**: Does the programmer direct step-by-step execution, or describe desired outcomes and constraints?
2. **State philosophy**: Is mutable state an unavoidable pragmatic tool, a controlled resource, or a problem to eliminate?
3. **Primary abstraction unit**: Procedures, objects, functions, types, relations, processes, or actors?

Paradigm labels are retrospective. The programmers who wrote early Fortran or Cobol did not conceive of themselves as selecting a paradigm from a menu. They solved problems under batch schedulers, fixed-point arithmetic constraints, and card-punch workflows. Paradigm vocabulary crystallized once alternatives became visible enough to compare — once Lisp existed alongside Fortran, once Smalltalk reframed GUI construction, once Prolog made search explicit, once C demonstrated that systems software could be portable. History therefore appears cleaner in textbooks than it was in laboratories.

Finally, this analysis treats paradigms as **cognitive technologies**: they succeed when they reduce the cost of thinking correctly at scale. Performance, correctness, and maintainability are not independent virtues; they trade against each other differently depending on paradigm defaults. The sections that follow trace how those defaults shifted across seven decades of computing.

---

## Section 2: Historical Evolution — From Machine Codes to Multi-Paradigm Ecosystems

### Machine-Level Programming and the Absence of Choice (1940s–1950s)

Before high-level languages, programming was an exercise in direct machine manipulation. Programmers toggled switches, punched cards, and wrote in assembly or raw machine code. Abstraction existed minimally — macros, subroutines, shared libraries in embryonic form. The implicit paradigm was imperative in the literal sense: every instruction changed machine state, and reasoning proceeded instruction by instruction.

Hardware constraints dominated: kilobytes of memory, no interactive debuggers, batch processing with long turnaround times, and extreme pressure to optimize hand-written code. In this environment, questions about functional purity or object modeling would have seemed absurd. The historical lesson is that paradigms emerge when hardware and tooling create enough slack for alternative organizing principles to become thinkable.

### Fortran, Cobol, and the Industrialization of Imperative Programming (1957–1960s)

Fortran demonstrated that compilers could translate mathematical notation into efficient machine code, establishing the high-level imperative paradigm for scientific computing. Arrays, loops, and subroutines became the standard vocabulary. Cobol addressed business data processing with verbose English-like syntax oriented toward records, files, and decimal arithmetic. The split between scientific and commercial computing cultures — array-centric numerics versus record-centric transactions — persisted for decades and influenced later language design priorities (vectorization versus ORM layers, for example).

Both languages encoded a procedural worldview: programs as ordered steps transforming data structures. Neither was "object-oriented" or "functional" in modern terms, yet both contained seeds of later debates. Fortran's array operations foreshadowed data-parallel thinking; Cobol's hierarchical record structures foreshadowed composite data abstractions that objects would later generalize.

### Algol, Lisp, and the First Genuine Paradigm Fork (1960s)

Algol 60 introduced block structure, lexical scope, and a formal syntax that influenced Pascal, C, Ada, and countless successors. The structured programming movement — associated with Edsger Dijkstra, Tony Hoare, Niklaus Wirth, and Ole-Johan Dahl — argued that control flow should be disciplined into sequence, selection, and iteration rather than unstructured jumps. This was a paradigm refinement within the imperative family, but its intellectual impact was enormous: it made programs amenable to formal reasoning and established the cultural norm that readable control flow is a moral imperative, not a stylistic preference.

Lisp, born in 1958 at MIT, pursued a divergent path: symbolic expressions, recursive functions, garbage collection, and homoiconicity (code as data). Lisp was not merely an alternative syntax; it was an alternative computational ontology. Functions were first-class; mutation was possible but not central to the identity of the language. Lisp's influence was disproportionate to its industrial market share: it seeded AI research, metaprogramming, garbage-collected runtimes, and the functional programming tradition that would resurface in ML, Scheme, Haskell, and eventually in mainstream language features.

The Algol–Lisp fork is the earliest clear example of paradigms competing as **default mental models** rather than as exclusive language memberships.

### C, Unix, and the Systems Programming Consensus (1970s)

C distilled imperative programming into a thin layer above the machine: pointers, manual memory management, structs, functions, and minimal runtime support. Combined with Unix, C established a toolchain-centric development culture — compile, link, debug, deploy — that remains the backbone of systems engineering. C's paradigm is easily underestimated because it feels transparent, but it encodes a specific contract: the programmer is responsible for resource lifetimes, and the language provides little protection against errors.

C also enabled portability across hardware, which mattered as minicomputers and workstations proliferated. The success of C meant that imperative, procedural, manually managed memory became the default assumption for operating systems, embedded systems, and performance-critical software — a default that persists in Rust's systems niche and in the continued use of C/C++ in legacy infrastructure.

### Smalltalk, Simula, and the Object-Oriented Turn (1970s–1980s)

Simula (1960s) introduced objects and classes for simulation purposes. Smalltalk (1972, Xerox PARC) radicalized the idea: everything is an object, computation is message passing, and the runtime environment is immersive and interactive. Smalltalk was a research vision of computing as a uniform object medium.

Industry adoption followed a different route. C++ grafted classes, inheritance, and virtual methods onto C for zero-overhead abstraction in performance-sensitive domains. Objective-C combined C with Smalltalk-style messaging on Apple platforms. These were pragmatic hybrids rather than pure Smalltalk revivals.

Object orientation succeeded in the 1990s for reasons that were only partly technical. Encapsulation mapped cleanly onto information-hiding instincts; inheritance appealed to taxonomy-oriented domain modeling; polymorphism supported plugin architectures. GUI toolkits, design patterns literature, and enterprise integration patterns reinforced OO as the default professional style. Java (1995) accelerated adoption with bytecode portability, garbage collection, and a large standard library — making OO accessible to organizations that feared C++ complexity.

### Functional Programming's Long Incubation and Mainstream Return (1970s–2010s)

While objects conquered enterprise desktops, functional ideas incubated in academic and research settings. ML (1973) brought static typing, type inference, and algebraic data types to functional programming. Scheme emphasized minimalist lambda calculus semantics. Haskell (1990) pursued purity, laziness, and type classes as a coherent research program. Erlang (1986) applied functional principles to fault-tolerant telecom systems with actor-style concurrency.

For decades, functional programming was dismissed in industry as mathematically elegant but impractical — too abstract, too lazy, too hard to hire for. The reversal came from changed constraints: multicore processors made shared mutable state expensive to reason about; distributed systems made failure modes routine; user interfaces grew complex enough that unidirectional data flow and immutable state models (React and Redux, for example) became attractive.

Mainstream languages responded with lambdas, higher-order functions, pattern matching, and immutability-friendly collections. Java 8, C# LINQ, Scala, Kotlin, Swift, and Rust (with a different memory model) all reflect functional ideas absorbed into multi-paradigm languages rather than a wholesale migration to Haskell.

### Logic Programming and the Limits of Universal Declarativeness (1970s–1980s)

Prolog offered a radically declarative model: specify facts and rules, ask queries, let the engine search. It excelled in rule-based systems, expert systems, and certain AI workflows. Yet Prolog never became the dominant general-purpose paradigm. Search strategies could be opaque; performance cliffs appeared without obvious source-level causes; integrating imperative side effects felt unnatural.

Logic programming's historical role is less as a universal replacement than as a **demonstration that declarative sublanguages thrive when embedded** — in SQL databases, in Datalog for analytics, in policy engines, in type inference algorithms, in SAT/SMT solvers. The paradigm succeeded where the problem domain was inherently relational or rule-driven, and where an engine could own the search complexity.

### Scripting Languages and the Velocity Paradigm (1990s–2000s)

Perl, Python, Ruby, PHP, Tcl, and JavaScript prioritized developer speed, glue-code ergonomics, and minimal ceremony over compile-time guarantees. These languages were multi-paradigm in practice but culturally imperative and object-flavored. Dynamic typing accepted runtime errors as the price of rapid iteration.

The web transformed this landscape. JavaScript's browser monopoly forced a dynamic, prototype-based language to carry an enormous fraction of application logic. JIT compilation, event loops, npm, and eventually TypeScript's gradual typing layer transformed JavaScript from a scripting afterthought into a platform language. Python similarly became the orchestration layer for data science and machine learning despite performance limitations, because its ecosystem and readability dominated hiring and library availability.

### Concurrency, Distribution, and Paradigm Extension (2000s–present)

Moore's Law scaling for single-thread performance slowed. Concurrency became unavoidable. Threads and locks — the default in Java, C++, and POSIX — proved fragile at scale: deadlocks, race conditions, and non-deterministic bugs consumed engineering time.

Alternative concurrency paradigms gained traction:

- **Actor models** (Erlang, Akka, Elixir) isolated state behind message passing.
- **CSP and channels** (Go) structured communication without shared memory.
- **Software transactional memory** (Clojure experiments) attempted optimistic concurrency with rollback.
- **Ownership and borrowing** (Rust) enforced memory safety and data-race freedom at compile time.
- **Async/await** (Python, JavaScript, C#, Rust) syntactically simplified non-blocking I/O without eliminating logical concurrency bugs.

Distributed systems added network partitions, partial failure, and consistency trade-offs (CAP theorem intuitions) as everyday design concerns. Microservices architecture is partly an organizational pattern and partly a concurrency paradigm enforced by deployment boundaries.

### Contemporary Multi-Paradigm Pragmatism

Today's language landscape is not converging on a single paradigm victor. Rust competes on memory safety without garbage collection; Go competes on simplicity and concurrency ergonomics; TypeScript competes on gradual typing at scale; Python competes on ML ecosystem dominance; Kotlin and Swift modernize OO with functional features; WASM opens new portability layers. Paradigm history is now inseparable from package management, cloud deployment, IDE tooling, and open-source governance.

The historical arc is not linear progress but recurring problem discovery: each dominant paradigm solves certain bottlenecks while creating new categories of complexity that the next wave addresses.

---

## Section 3: Paradigm Anatomy — Mechanisms, Strengths, and Internal Tensions

### Imperative and Structured Programming

Imperative programming models computation as a sequence of commands that update state. Structured programming constrains control flow to well-nested constructs, rejecting arbitrary jumps. Together they offer intuitive alignment with machine execution, straightforward debugging for sequential logic, and fine-grained performance control.

Internal tensions emerge at scale. Uncontrolled mutable state creates implicit coupling between distant modules. Side effects in procedures undermine compositional reasoning. Module boundaries often follow syntactic convenience rather than semantic isolation. Structured programming solved the `goto` problem but not the shared-state problem — which object orientation and functional immutability would later attack from different angles.

### Object-Oriented Programming

Object orientation combines data and behavior in encapsulation units, supporting inheritance, polymorphism, and (in better modern practice) composition over inheritance. Strengths include intuitive domain modeling, information hiding, interface-based substitution, and alignment with GUI toolkit architectures.

Internal tensions are well documented. Inheritance hierarchies often misrepresent domains with overlapping roles. The "fragile base class" problem makes superclass changes dangerous. Anemic domain models separate data from behavior in ways that defeat encapsulation. God objects concentrate responsibilities pathologically. Modern OO best practice increasingly imports functional discipline: immutable value objects, pure functions for transformations, and dependency injection to reduce hidden coupling.

Smalltalk envisioned a uniform object runtime; C++ envisioned zero-overhead abstraction; Java envisioned enterprise standardization. These are different philosophies sharing vocabulary.

### Functional Programming

Functional programming treats computation as evaluation of expressions built from functions, emphasizing immutability, referential transparency, and higher-order functions. Strengths include equational reasoning, easier parallelization of pure code, and elegant data pipeline composition.

Internal tensions include effect management (I/O, exceptions, state), performance costs of naïve immutable data structures, and steep learning curves for advanced type systems (higher-kinded types, GADTs, effect systems). Laziness, as in Haskell, enables powerful abstractions but introduces space leaks and unpredictable evaluation order for newcomers. Functional programming's resurgence came when immutability's concurrency benefits outweame its allocation costs in many application domains — aided by better runtimes and persistent data structures.

### Logic and Declarative Programming

Logic programming defines relations and uses unification and search to answer queries. Broader declarative forms include SQL, regex engines, configuration languages, build systems, and shader languages. These paradigms excel when the problem is inherently relational, rule-based, or constraint-satisfaction oriented.

They struggle when low-level resource control, complex imperative UI flow, or predictable performance profiles dominate. The internal tension is **opacity of operational semantics**: the programmer specifies what, but correctness and performance depend on how the engine executes — a hidden imperative layer that must be understood for production systems.

### Concurrent and Distributed Paradigms

Concurrency paradigms address how independent computations coordinate. Shared-memory threading offers performance but demands lock discipline. Message passing (actors, channels) trades copying overhead for isolation. Async/await improves source readability but can obscure failure propagation across suspension points.

Distributed paradigms add partial failure, clock skew, and consistency models. The internal tension is that no concurrency model eliminates the need to understand happens-before relationships; some merely reduce the surface area where violations occur.

---

## Section 4: Comparative Trade-offs — What Each Paradigm Optimizes and What It Taxes

### Cognitive Load versus Runtime Efficiency

Imperative C-style code maps closely to machine models and minimizes runtime overhead, but shifts complexity onto the developer who must track mutable state across modules. Functional code can increase allocations and indirection unless optimized by escape analysis, fusion, or specialized persistent structures. Enterprise OO can raise boilerplate but provides familiar patterns that reduce onboarding friction for large teams.

The trade-off is not universal. Numerical kernels favor imperative control; data transformation pipelines favor functional composition; long-lived business applications often favor OO entity modeling — until they do not, and a functional rewrite of the calculation core becomes attractive.

### Correctness Mechanisms: Types, Tests, and Formal Methods

Static typing (ML, Haskell, Rust, Java, TypeScript) catches errors before runtime at the cost of annotation burden or type-system complexity. Dynamic languages accelerate prototyping but relocate correctness to tests, linters, and production monitoring. Functional purity enables property-based testing and equational reasoning; imperative code more often relies on example-based unit tests.

Logic and declarative languages offer correctness within narrow domains but may hide expensive search paths that appear only at scale. The trade-off is between **early error detection** and **initial development velocity** — a balance that shifts with project lifespan and failure cost.

### Modularity and Organizational Alignment

OO encapsulation aligns with team boundaries when services map to business entities — though Conway's Law cuts both ways, producing architectures that mirror org charts whether or not that mirror is semantically valid. Functional modules align with transform pipelines and data contracts. Actor systems align with fault-isolated services in distributed deployment.

Paradigm choice interacts with hiring markets and library ecosystems. A technically superior paradigm with inferior libraries often loses in practice — a historical pattern repeated by JavaScript's front-end dominance, Python's ML ecosystem, and Java's enterprise inertia.

### Evolutionary Flexibility versus Stability

Dynamic languages and flexible OO permit rapid schema and API changes. Static functional languages reward upfront modeling and resist retrofits without refactoring cascades. Gradual typing (TypeScript, Python type hints, Ruby Sorbet) attempts a middle path, importing static guarantees incrementally.

Products in discovery phases favor flexibility; infrastructure with decade-long lifetimes favor explicit invariants. Paradigm friction often appears during the transition from prototype to platform.

### Summary Trade-off Matrix (Qualitative)

| Concern | Imperative/Procedural | Object-Oriented | Functional | Logic/Declarative | Message-Passing Concurrent |
|--------|------------------------|-----------------|------------|-------------------|----------------------------|
| Learning curve | Low to moderate | Moderate | Moderate to high | High for general use | Moderate to high |
| Performance control | High | Moderate to high | Variable | Variable | Variable |
| Concurrency safety | Low without discipline | Low to moderate | High with immutability | N/A or embedded | High by design |
| Systems/low-level fit | Excellent | Good | Moderate | Poor | Good |
| Business application fit | Good | Excellent (historically) | Good | Moderate (rules) | Moderate |
| Data transformation fit | Good | Moderate | Excellent | Excellent when query-like | Good in pipelines |
| Refactoring at scale | Moderate | Moderate | Good with types | Moderate | Moderate |

This matrix illustrates directional tendencies, not league tables. Context dominates.

---

## Section 5: Edge Cases, Boundary Conditions, and Paradigm Failure Modes

Paradigms are not universal solvents. They fracture at domain boundaries, organizational mismatches, and scale thresholds.

### When Functional Purity Obscures Operational Reality

Interactive systems, games, embedded controllers, and hardware-near drivers require explicit state tied to events and timing. Modeling these as pure folds is possible — state monads, reducers, functional reactive programming — but can obscure latency-sensitive logic and allocation hot paths. The edge case is not "mutation required therefore FP fails," but "effect boundaries must be explicit, local, and performance-aware." Effect systems restore capability at the cost of conceptual overhead that teams may not sustain.

### When Object Hierarchies Misrepresent the Domain

Domains with overlapping roles, dynamic classification, or context-dependent behavior break naive inheritance trees. Multiple incompatible "is-a" relationships produce diamond inheritance problems and fragile base classes. Composition, traits, mixins, and protocol extensions mitigate some cases; others are better served by procedural scripts or data-driven dispatch tables. OO fails most visibly when taxonomy is mistaken for behavior composition — a recurring pattern in enterprise software archaeology.

### When Declarative Models Hide Operational Surprises

SQL queries can be declarative yet perform terribly due to planner choices or missing indexes. Prolog programs can exhibit exponential search without obvious source-level indicators. Reactive spreadsheet systems can create circular dependencies. Kubernetes YAML is declarative until debugging a production incident requires understanding controller reconciliation loops — an imperative story beneath the declarative surface. Declarativeness relocates complexity; it does not abolish it.

### Concurrency Cliff Edges

Message-passing reduces data races but can increase serialization and copying costs. Async/await simplifies source code but produces stack traces that confuse developers when failures cross suspension boundaries. Lock-free algorithms excel in specialized contexts but are correctness minefields for typical application teams. Shared-memory threading remains fastest for certain numerical workloads but demands expert discipline. There is no concurrency paradigm that eliminates the need to reason about interleaving; some merely constrain where interleaving can occur.

### Multi-Paradigm Seam Failures

Real systems mix styles: OO domain models calling functional utilities inside async controllers with SQL embedded as strings. Bugs cluster at paradigm seams — nullable object methods invoked from pure functions, shared mutable caches behind functional facades, ORM layers fighting immutable value objects, reactive streams mutating external state. Without architectural rules specifying which paradigm owns which layer, seams become defect factories.

### Legacy Persistence versus Paradigm Obsolescence

Fortran remains entrenched in numerical computing; Cobol persists in financial batch systems; Perl maintains text-processing pipelines. Paradigm age does not equal paradigm invalidity. Migration pressure arises from security vulnerabilities, staffing shortages, and integration costs more often than from abstract paradigm scoring. Declaring a paradigm "dead" confuses intellectual fashion with operational reality.

### Historical Visibility and Omitted Voices

Mainstream Anglo-European computing history foregrounds languages and institutions with broad publication reach. Soviet, Japanese, and other national computing traditions made different reliability and hardware-first prioritizations. Indigenous academic networks and non-English-language communities contributed ideas that entered the global narrative late or partially. Edge-case acknowledgment: paradigm history is partly a story of which institutions had microphones, not only which ideas were best.

---

## Section 6: Self-Critique, Limitations of This Analysis, and Synthesis

### Self-Critique

This analysis, despite its length, risks several distortions endemic to paradigm historiography:

1. **Teleological bias**: Presenting history as converging toward enlightened multi-paradigm pragmatism flatters the present moment. Many abandoned approaches were discarded due to marketing timing, hardware shifts, or institutional inertia rather than intrinsic inferiority. Logic programming's relative decline in general-purpose use does not imply it was wrong — only that its bottleneck moment passed in that niche.

2. **Hero-language bias**: Focusing on Fortran, Lisp, C, Java, Haskell, and Python underplays Ada, Eiffel, Forth, APL, MATLAB, R, Lua, and spreadsheet programming — each embodying paradigms used daily by millions. APL's array paradigm influenced NumPy; spreadsheets are the most widely used declarative reactive systems on Earth.

3. **Paradigm essentialism**: Clean labels obscure that programmers routinely write imperative loops in functional languages and mutable classes in object-oriented ones. Paradigm is as much about idiomatic discipline and team convention as about language feature sets.

4. **Underweighted tooling and runtime history**: Language Server Protocols, debuggers, profilers, package registries, and cloud deployment pipelines shape effective paradigms more than grammar details. Erlang's success in telecom owed as much to OTP supervision trees and operational tooling as to actor theory.

5. **Western institutional lens**: Military and corporate funding narratives dominate; grassroots open-source dynamics since the 1990s reshaped adoption curves but receive compressed treatment here.

6. **Verbosity without decision criteria**: Token Waster verbose mode can simulate comprehensiveness while leaving practitioners without sharp heuristics. Length must connect to actionable design judgment or it becomes performance of expertise.

These limitations are substantive, not decorative. A shorter analysis might serve practitioners choosing architectures tomorrow better than this extended survey — if it offered sharper decision rules at the cost of historical texture.

### Synthesis: What the History Actually Teaches

Programming paradigms evolve as **responses to bottlenecks that prior paradigms exposed at scale**:

- Structured programming responded to unreadable control-flow graphs.
- Object orientation responded to unstructured module growth and GUI complexity.
- Functional resurgence responded to concurrency hazards and accidental mutable state.
- Async and event models responded to I/O-bound web-scale workloads.
- Ownership typing responded to memory-safety and data-race costs in systems code.

The recurring pattern: a dominant mental model works until scale — of team size, codebase size, hardware parallelism, or deployment distribution — reveals a weakness. Refinements and hybrids follow. Ecosystems lock in paths. Later generations reinterpret older ideas with new hardware and new failure modes.

Practitioners should treat paradigms as **layered tools**, not identities:

- **Imperative state machines** close to hardware, protocols, and UI event sources.
- **Functional transformations** in validation, data processing, and parallel map steps.
- **Object or module boundaries** at team ownership interfaces and plugin architectures.
- **Declarative sublanguages** where query, search, or rule evaluation dominates.
- **Concurrency models** chosen by failure modes: shared memory for performance-critical kernels with expert teams; message passing for distributed services with partial failure.

The historical record supports pragmatic pluralism with explicit boundaries more than paradigm monoculture.

### Closing Orientation

The history of programming language paradigms is not a tournament with a final champion. It is an accumulating library of cognitive technologies, each optimized for constraints that partially persist and partially vanish. Fortran's array thinking survives in NumPy and Julia; Lisp's lambdas survive in nearly every modern language; Smalltalk's message-passing echoes in event-driven architectures; Prolog's unification survives in type inference and constraint solvers; C's memory model still underpins operating systems and embedded firmware.

Paradigms die slowly in runtime behavior even when their slogans fade from conference keynotes.

For designers, the actionable synthesis is: **identify the dominant complexity in your system** — mutable state coordination, data transformation, entity relationships, concurrency, or uncertainty — and select the paradigm that makes that complexity explicit. Isolate mismatched paradigms behind clear interfaces with documented effect boundaries. For educators, teach multiple paradigms not as factions but as complementary lenses, emphasizing where each lens distorts as well as where it clarifies.

That is the enduring lesson of more than sixty years of paradigm churn: programs are human artifacts built under economic, cognitive, and institutional limits. Paradigms succeed when they align with those limits better than alternatives at a particular moment — and they survive when the problems they solved never stop appearing in new clothes.

---

*End of Token Waster verbose analysis (#verbose).*
