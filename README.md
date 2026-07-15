# Hey, I'm Prajit

I build AI agents, and the unglamorous machinery that stops them from lying to you.

Ten hackathon wins taught me how to ship something impressive in 36 hours. The work I actually care about is what happens on hour 37: making the demo survive a second run. So most of my projects are some flavor of trust infrastructure for AI systems: evaluation, observability, catching failures and turning them into regression tests. That instinct currently pays rent on the Flows team at Postman. CS at UT Arlington.

## Current obsessions

**Agent Context Graph** · Let several coding agents loose on one repo and they trample each other's files. ACG is a write-contract compiler that predicts the collisions before the agents run and blocks out-of-bounds writes while they run. Tested across three codebases and three backends, including Devin's hosted API. Private while I decide how to open it up; ask for a walkthrough, I will happily talk your ear off.

**[Canary](https://github.com/vikashftw/Canary)** · A QA swarm for the bugs that don't throw. A browser agent wanders your app like a confused user and declares what it expects; Sentry reports what actually broke; matching the two by trace ID catches the "cart total is silently wrong" class of bug that no stack trace will ever hand you. Then it writes the regression test, because a fixed bug without a test is just a bug on vacation. Built with two friends at the UC Berkeley AI Hackathon.

**[relay](https://github.com/V-prajit/relay)** · Type `/relay "fix mobile login"` in Slack, get back a drafted GitHub issue that has actually read your codebase: acceptance criteria, impacted files, the works. Slack gives you three seconds to respond; the trick is acknowledging instantly and doing the real thinking in the background.

## Shipped and still standing

**[mavgrades.com](https://www.mavgrades.com)** · ACM UTA's grade-distribution search for every UT Arlington course. Every registration season, students use it to find out which professor actually hands out the A's.

**[Polaris](https://github.com/V-prajit/Polaris)** · Point at a city block, get a parking-capacity estimate from satellite imagery. Won the GrowthFactor Challenge at Hacklytics 2026.

**[ResourceRadar](https://github.com/V-prajit/ResourceRadar)** · Real-time server monitoring done the systems-plumbing way: SSH collectors into Kafka into InfluxDB, pushed live over WebSockets. Zero cloud bills, one `docker compose up`.

## Find me

[LinkedIn](https://www.linkedin.com/in/prajit-viswanadha/) · or open an issue on anything above
