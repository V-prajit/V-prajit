# Prajit Viswanadha

I build reliable AI agents and the developer infrastructure that keeps them honest: evaluation, observability, and failure analysis over demos that only work once.

My recent work is about making multi-agent and AI-driven pipelines trustworthy instead of impressive-once: predicting where parallel coding agents will collide before they run, catching the bugs that don't throw exceptions, and turning caught failures into regression tests instead of tickets, plus the developer infrastructure (MCP servers, CLI surfaces, CI wiring) that makes that usable outside a demo. Two things anchor it: [mavgrades](https://www.mavgrades.com), a grade-lookup tool live in production and used by UT Arlington students, and a judged, verified hackathon win with Polaris. Summer 2026 I'm interning on the Postman Flows team.

## Currently exploring

- **Pre-flight coordination for parallel coding agents**: predicting each agent's write-set before execution and blocking out-of-bounds writes at validation time, not after the merge conflict
- **Agent evaluation and failure reproduction**: running the same task set against multiple backends (local models, hosted agents) and measuring conflict counts, blocked writes, and wall-clock deltas, not just pass/fail
- **Dual-oracle QA**: pairing error monitoring (what throws) with an agent that declares an expectation and checks it (what's silently wrong), then correlating the two by trace ID
- **Tool-schema reliability and provenance**: write-contracts (`allowed_paths`, `predicted_writes`) that are committable and human-reviewable, not just prompts
- **Regression generation**: closing the loop from a caught failure to a fix diff to a test that stops it recurring
- **Developer infrastructure**: MCP servers, CLI surfaces, and CI wiring around the above so they're usable outside a demo environment

The flagship project here is **Agent Context Graph (ACG)**, a write-contract compiler for multi-agent code generation. Given a task list and a repo, it scans the codebase, predicts which tasks will contend on shared files, sequences the contending ones deterministically, and validates every proposed write against a per-task contract in real time. It's been evaluated across three codebases (a Java Spring service, a TypeScript T3 stack, a NestJS backend) and three execution backends, including a live integration with Devin's hosted agent API; every proposed write, on any backend, is checked against its per-task contract before it lands. It's currently private while I decide on the right way to open it up, ask if you want a walkthrough.

## Selected work

### [Canary / Bloodhound](https://github.com/vikashftw/Canary)
A dual-oracle autonomous QA swarm that catches the bugs that don't throw: a headless-browser agent explores a real app like a chaos-user and declares what it expects before each action, while Sentry watches for what actually crashes. The two oracles are correlated by Sentry trace ID (browser = symptom, error monitor = cause), then a triage agent root-causes each finding, writes the fix, and generates a regression test so the bug can't recur. Anything touching Anthropic or Sentry is dependency-injected behind fakes, so the full suite runs offline in CI.
Built at the UC Berkeley AI Hackathon 2026 as a three-person team; I own the dashboard wiring and the memory/persistence layer.

### [Polaris](https://github.com/V-prajit/Polaris)
An ML platform that turns satellite imagery into a parking-capacity estimate: drop a pin in a city and get stall counts, confidence intervals, and a 0-100 accessibility score. It fuses three independent methods into one weighted, confidence-scored estimate: a SegFormer-b5 model fine-tuned on the 12,617-tile ParkSeg12k dataset, YOLO detectors run under SAHI sliced inference to catch small objects, and geometry-only heuristics from OSM boundaries. Mapped the entirety of Atlanta on H3 hex grids as the demo dataset.
**Winner, GrowthFactor Challenge at Hacklytics 2026 (Georgia Tech).** [Devpost](https://devpost.com/software/parasite-2dri43)

### [relay](https://github.com/V-prajit/relay)
Turns a Slack slash command into a codebase-aware GitHub issue: `/relay "fix mobile login"` searches the repo and drafts a GitHub-ready issue with acceptance criteria and an impacted-files list. Built on Postman Flows: an immediate "Processing..." acknowledgment lands inside Slack's 3-second webhook window while search-and-generate runs in the background, backed by a small ripgrep API service for fast codebase search.

### [mavgrades](https://github.com/acmuta/mavgrades) (live at [mavgrades.com](https://www.mavgrades.com))
A grade-distribution search tool for UT Arlington courses and professors, shipped by ACM UTA and used by real students to pick classes and professors before they register. Serves 15+ semesters of grade data (Fall 2020 onward) from a ~21MB SQLite file bundled into the deploy artifact and queried directly by Next.js route handlers behind an in-memory LRU cache, with no external database service and no user write path.

### [ResourceRadar](https://github.com/V-prajit/ResourceRadar)
A real-time monitoring dashboard for CPU and memory across multiple remote servers over SSH, shipped as one `docker compose up`. Metrics flow from SSH collectors through Kafka topics into an InfluxDB time-series store, with Postgres holding server config; the React frontend gets live values over a Socket.IO WebSocket the backend pushes every second, not REST polling. Systems plumbing (message brokering, time-series storage, multi-service orchestration) rather than a CRUD app.

## Recent highlights

Winner, GrowthFactor Challenge at Hacklytics 2026 (Georgia Tech), for Polaris, turning satellite imagery into city-scale parking intelligence. I build at hackathons regularly, and the recent ones (like the dual-oracle QA swarm above, built at the UC Berkeley AI Hackathon 2026) have moved from one-weekend demos toward making agent behavior predictable and verifiable.

## Contact

- LinkedIn: [linkedin.com/in/prajit-viswanadha](https://linkedin.com/in/prajit-viswanadha)
- GitHub: [github.com/V-prajit](https://github.com/V-prajit)
