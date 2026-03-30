---
date: '2026-02-21'
description: Cloudflare's new Model Context Protocol (MCP) server leverages Code Mode
  to streamline AI agent interactions with extensive APIs, specifically the Cloudflare
  API, while drastically minimizing token consumption. By consolidating calls into
  two functions—`search()` and `execute()`—the server achieves a 99.9% reduction in
  token usage compared to traditional methods, maintaining a fixed footprint of ~1,000
  tokens. This approach enables efficient discovery and execution of API endpoints
  without overwhelming context windows. Furthermore, it employs an OAuth 2.1 compliant
  system for secure, user-defined permissions. This marks a significant advancement
  in optimizing API access for AI agents.
link: https://blog.cloudflare.com/code-mode-mcp/
tags:
- MCP
- AI Agents
- API Optimization
- Code Mode
- Cloudflare
title: 'Code Mode: give agents an entire API in 1,000 tokens'
---

# Code Mode: give agents an entire API in 1,000 tokens

2026-02-20

- [![Matt Carey](https://blog.cloudflare.com/cdn-cgi/image/format=auto,dpr=3,width=64,height=64,gravity=face,fit=crop,zoom=0.5/https://cf-assets.www.cloudflare.com/zkvhlag99gkb/3tQWp2cSHTttrxFseVLgH9/e468b31725cc9f8c61dae5e87b8da6a0/91c78ad4-3d50-4256-872b-ec4398e8f7f1_224x224.png)](https://blog.cloudflare.com/author/matt-carey/)
  [Matt Carey](https://blog.cloudflare.com/author/matt-carey/)


6 min read

![](https://cf-assets.www.cloudflare.com/zkvhlag99gkb/6YAHY3FwNCFMGMYtIDuri7/139b77ff4e1b71ca706af22064222f67/images_BLOG-3184_1.png)

[Model Context Protocol (MCP)](https://www.cloudflare.com/learning/ai/what-is-model-context-protocol-mcp/) has become the standard way for AI agents to use external tools. But there is a tension at its core: agents need many tools to do useful work, yet every tool added fills the model's context window, leaving less room for the actual task.

[Code Mode](https://blog.cloudflare.com/code-mode/) is a technique we first introduced for reducing context window usage during agent tool use. Instead of describing every operation as a separate tool, let the model write code against a typed SDK and execute the code safely in a [Dynamic Worker Loader](https://developers.cloudflare.com/workers/runtime-apis/bindings/worker-loader/). The code acts as a compact plan. The model can explore tool operations, compose multiple calls, and return just the data it needs. Anthropic independently explored the same pattern in their [Code Execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp) post.

Today we are introducing [a new MCP server](https://github.com/cloudflare/mcp) for the [entire Cloudflare API](https://developers.cloudflare.com/api/) — from [DNS](https://developers.cloudflare.com/dns/) and [Zero Trust](https://developers.cloudflare.com/cloudflare-one/) to [Workers](https://workers.cloudflare.com/product/workers/) and [R2](https://workers.cloudflare.com/product/r2/) — that uses Code Mode. With just two tools, search() and execute(), the server is able to provide access to the entire Cloudflare API over MCP, while consuming only around 1,000 tokens. The footprint stays fixed, no matter how many API endpoints exist.

For a large API like the Cloudflare API, Code Mode reduces the number of input tokens used by 99.9%. An equivalent MCP server without Code Mode would consume 1.17 million tokens — more than the entire context window of the most advanced foundation models.

![images/BLOG-3184 3](https://cf-assets.www.cloudflare.com/zkvhlag99gkb/7KqjQiI09KubtUSe9Dgf0N/6f37896084c7f34abca7dc36ab18d8e0/image2.png)

_Code mode savings vs native MCP, measured with_[_tiktoken_](https://github.com/openai/tiktoken)

You can start using this new Cloudflare MCP server today. And we are also open-sourcing a new [Code Mode SDK](https://github.com/cloudflare/agents/tree/main/packages/codemode) in the [Cloudflare Agents SDK](https://github.com/cloudflare/agents), so you can use the same approach in your own MCP servers and AI Agents.

### Server‑side Code Mode

![images/BLOG-3184 2](https://cf-assets.www.cloudflare.com/zkvhlag99gkb/ir1KOZHIjVNyqdC9FSuZs/334456a711fb2b5fa612b3fc0b4adc48/images_BLOG-3184_2.png)

This new MCP server applies Code Mode server-side. Instead of thousands of tools, the server exports just two: `search()` and `execute()`. Both are powered by Code Mode. Here is the full tool surface area that gets loaded into the model context:

```javascript
[\
  {\
    "name": "search",\
    "description": "Search the Cloudflare OpenAPI spec. All $refs are pre-resolved inline.",\
    "inputSchema": {\
      "type": "object",\
      "properties": {\
        "code": {\
          "type": "string",\
          "description": "JavaScript async arrow function to search the OpenAPI spec"\
        }\
      },\
      "required": ["code"]\
    }\
  },\
  {\
    "name": "execute",\
    "description": "Execute JavaScript code against the Cloudflare API.",\
    "inputSchema": {\
      "type": "object",\
      "properties": {\
        "code": {\
          "type": "string",\
          "description": "JavaScript async arrow function to execute"\
        }\
      },\
      "required": ["code"]\
    }\
  }\
]
```

To discover what it can do, the agent calls `search()`. It writes JavaScript against a typed representation of the OpenAPI spec. The agent can filter endpoints by product, path, tags, or any other metadata and narrow thousands of endpoints to the handful it needs. The full OpenAPI spec never enters the model context. The agent only interacts with it through code.

When the agent is ready to act, it calls `execute()`. The agent writes code that can make Cloudflare API requests, handle pagination, check responses, and chain operations together in a single execution.

Both tools run the generated code inside a [Dynamic Worker](https://developers.cloudflare.com/workers/runtime-apis/bindings/worker-loader/) isolate — a lightweight V8 sandbox with no file system, no environment variables to leak through prompt injection and external fetches disabled by default. Outbound requests can be explicitly controlled with outbound fetch handlers when needed.

#### Example: Protecting an origin from DDoS attacks

Suppose a user tells their agent: "protect my origin from DDoS attacks." The agent's first step is to consult documentation. It might call the [Cloudflare Docs MCP Server](https://developers.cloudflare.com/agents/model-context-protocol/mcp-servers-for-cloudflare/), use a [Cloudflare Skill](https://github.com/cloudflare/skills), or search the web directly. From the docs it learns: put [Cloudflare WAF](https://www.cloudflare.com/application-services/products/waf/) and [DDoS protection](https://www.cloudflare.com/ddos/) rules in front of the origin.

**Step 1: Search for the right endpoints** The `search` tool gives the model a `spec` object: the full Cloudflare OpenAPI spec with all `$refs` pre-resolved. The model writes JavaScript against it. Here the agent looks for WAF and ruleset endpoints on a zone:

```javascript
async () => {
  const results = [];
  for (const [path, methods] of Object.entries(spec.paths)) {
    if (path.includes('/zones/') &&
        (path.includes('firewall/waf') || path.includes('rulesets'))) {
      for (const [method, op] of Object.entries(methods)) {
        results.push({ method: method.toUpperCase(), path, summary: op.summary });
      }
    }
  }
  return results;
}
```

The server runs this code in a Workers isolate and returns:

```javascript
[\
  { "method": "GET",    "path": "/zones/{zone_id}/firewall/waf/packages",              "summary": "List WAF packages" },\
  { "method": "PATCH",  "path": "/zones/{zone_id}/firewall/waf/packages/{package_id}", "summary": "Update a WAF package" },\
  { "method": "GET",    "path": "/zones/{zone_id}/firewall/waf/packages/{package_id}/rules", "summary": "List WAF rules" },\
  { "method": "PATCH",  "path": "/zones/{zone_id}/firewall/waf/packages/{package_id}/rules/{rule_id}", "summary": "Update a WAF rule" },\
  { "method": "GET",    "path": "/zones/{zone_id}/rulesets",                           "summary": "List zone rulesets" },\
  { "method": "POST",   "path": "/zones/{zone_id}/rulesets",                           "summary": "Create a zone ruleset" },\
  { "method": "GET",    "path": "/zones/{zone_id}/rulesets/phases/{ruleset_phase}/entrypoint", "summary": "Get a zone entry point ruleset" },\
  { "method": "PUT",    "path": "/zones/{zone_id}/rulesets/phases/{ruleset_phase}/entrypoint", "summary": "Update a zone entry point ruleset" },\
  { "method": "POST",   "path": "/zones/{zone_id}/rulesets/{ruleset_id}/rules",        "summary": "Create a zone ruleset rule" },\
  { "method": "PATCH",  "path": "/zones/{zone_id}/rulesets/{ruleset_id}/rules/{rule_id}", "summary": "Update a zone ruleset rule" }\
]
```

The full Cloudflare API spec has over 2,500 endpoints. The model narrowed that to the WAF and ruleset endpoints it needs, without any of the spec entering the context window.

The model can also drill into a specific endpoint's schema before calling it. Here it inspects what phases are available on zone rulesets:

```javascript
async () => {
  const op = spec.paths['/zones/{zone_id}/rulesets']?.get;
  const items = op?.responses?.['200']?.content?.['application/json']?.schema;
  // Walk the schema to find the phase enum
  const props = items?.allOf?.[1]?.properties?.result?.items?.allOf?.[1]?.properties;
  return { phases: props?.phase?.enum };
}

{
  "phases": [\
    "ddos_l4", "ddos_l7",\
    "http_request_firewall_custom", "http_request_firewall_managed",\
    "http_response_firewall_managed", "http_ratelimit",\
    "http_request_redirect", "http_request_transform",\
    "magic_transit", "magic_transit_managed"\
  ]
}
```

The agent now knows the exact phases it needs: `ddos_l7`for DDoS protection and `http_request_firewall_managed` for WAF.

**Step 2: Act on the API** The agent switches to using `execute`. The sandbox gets a `cloudflare.request()` client that can make authenticated calls to the Cloudflare API. First the agent checks what rulesets already exist on the zone:

```javascript
async () => {
  const response = await cloudflare.request({
    method: "GET",
    path: `/zones/${zoneId}/rulesets`
  });
  return response.result.map(rs => ({
    name: rs.name, phase: rs.phase, kind: rs.kind
  }));
}

[\
  { "name": "DDoS L7",          "phase": "ddos_l7",                        "kind": "managed" },\
  { "name": "Cloudflare Managed","phase": "http_request_firewall_managed", "kind": "managed" },\
  { "name": "Custom rules",     "phase": "http_request_firewall_custom",   "kind": "zone" }\
]
```

The agent sees that managed DDoS and WAF rulesets already exist. It can now chain calls to inspect their rules and update sensitivity levels in a single execution:

```javascript
async () => {
  // Get the current DDoS L7 entrypoint ruleset
  const ddos = await cloudflare.request({
    method: "GET",
    path: `/zones/${zoneId}/rulesets/phases/ddos_l7/entrypoint`
  });

  // Get the WAF managed ruleset
  const waf = await cloudflare.request({
    method: "GET",
    path: `/zones/${zoneId}/rulesets/phases/http_request_firewall_managed/entrypoint`
  });
}
```

This entire operation, from searching the spec and inspecting a schema to listing rulesets and fetching DDoS and WAF configurations, took four tool calls.

### The Cloudflare MCP server

We started with MCP servers for individual products. Want an agent that manages DNS? Add the [DNS MCP server](https://github.com/cloudflare/mcp-server-cloudflare/tree/main/apps/dns-analytics). Want Workers logs? Add the [Workers Observability MCP server](https://developers.cloudflare.com/agents/model-context-protocol/mcp-servers-for-cloudflare/). Each server exported a fixed set of tools that mapped to API operations. This worked when the tool set was small, but the Cloudflare API has over 2,500 endpoints. No collection of hand-maintained servers could keep up.

The Cloudflare MCP server simplifies this. Two tools, roughly 1,000 tokens, and coverage of every endpoint in the API. When we add new products, the same `search()` and `execute()` code paths discover and call them — no new tool definitions, no new MCP servers. It even has support for the [GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/).

Our MCP server is built on the latest MCP specifications. It is OAuth 2.1 compliant, using [Workers OAuth Provider](https://github.com/cloudflare/workers-oauth-provider) to downscope the token to selected permissions approved by the user when connecting. The agent  only gets the capabilities the user explicitly granted.

For developers, this means you can use a simple agent loop and still give your agent access to the full Cloudflare API with built-in progressive capability discovery.

![images/BLOG-3184 4](https://cf-assets.www.cloudflare.com/zkvhlag99gkb/60ZoSFdK6t6hR6DpAn6Bub/93b86239cedb06d7fb265859be7590e8/images_BLOG-3184_4.png)

### Comparing approaches to context reduction

Several approaches have emerged to reduce how many tokens MCP tools consume:

**Client-side Code Mode** was our first experiment. The model writes TypeScript against typed SDKs and runs it in a Dynamic Worker Loader on the client. The tradeoff is that it requires the agent to ship with secure sandbox access. Code Mode is implemented in [Goose](https://block.github.io/goose/blog/2025/12/15/code-mode-mcp/) and Anthropics Claude SDK as [Programmatic Tool Calling](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling).

**Command-line interfaces** are another path. CLIs are self-documenting and reveal capabilities as the agent explores. Tools like [OpenClaw](https://openclaw.ai/) and [Moltworker](https://blog.cloudflare.com/moltworker-self-hosted-ai-agent/) convert MCP servers into CLIs using [MCPorter](https://github.com/steipete/mcporter) to give agents progressive disclosure. The limitation is obvious: the agent needs a shell, which not every environment provides and which introduces a much broader attack surface than a sandboxed isolate.

**Dynamic tool search**, as used by [Anthropic in Claude Code](https://x.com/trq212/status/2011523109871108570), surfaces a smaller set of tools hopefully relevant to the current task. It shrinks context use but now requires a search function that must be maintained and evaluated, and each matched tool still uses tokens.

![images/BLOG-3184 5](https://cf-assets.www.cloudflare.com/zkvhlag99gkb/5FPxVAuJggv7A08DbPsksb/aacb9087a79d08a1430ea87bb6960ad3/images_BLOG-3184_5.png)

Each approach solves a real problem. But for MCP servers specifically, server-side Code Mode combines their strengths: fixed token cost regardless of API size, no modifications needed on the agent side, progressive discovery built in, and safe execution inside a sandboxed isolate. The agent just calls two tools with code. Everything else happens on the server.

### Get started today

The Cloudflare MCP server is available now. Point your MCP client at the server URL and you'll be redirected to Cloudflare to authorize and select the permissions to grant to your agent. Add this config to your MCP client:

```javascript
{
  "mcpServers": {
    "cloudflare-api": {
      "url": "https://mcp.cloudflare.com/mcp"
    }
  }
}
```

For CI/CD, automation, or if you prefer managing tokens yourself, create a Cloudflare API token with the permissions you need. Both user tokens and account tokens are supported and can be passed as bearer tokens in the `Authorization` header.

More information on different MCP setup configurations can be found at the [Cloudflare MCP repository](https://github.com/cloudflare/mcp).

### Looking forward

Code Mode solves context costs for a single API. But agents rarely talk to one service. A developer's agent might need the Cloudflare API alongside GitHub, a database, and an internal docs server. Each additional MCP server brings the same context window pressure we started with.

[Cloudflare MCP Server Portals](https://blog.cloudflare.com/zero-trust-mcp-server-portals/) let you compose multiple MCP servers behind a single gateway with unified auth and access control. We are building a first-class Code Mode integration for all your MCP servers, and exposing them to agents with built-in progressive discovery and the same fixed-token footprint, regardless of how many services sit behind the gateway.

Cloudflare's connectivity cloud protects [entire corporate networks](https://www.cloudflare.com/network-services/), helps customers build [Internet-scale applications efficiently](https://workers.cloudflare.com/), accelerates any [website or Internet application](https://www.cloudflare.com/performance/accelerate-internet-applications/), [wards off DDoS attacks](https://www.cloudflare.com/ddos/), keeps [hackers at bay](https://www.cloudflare.com/application-security/), and can help you on [your journey to Zero Trust](https://www.cloudflare.com/products/zero-trust/).

Visit [1.1.1.1](https://one.one.one.one/) from any device to get started with our free app that makes your Internet faster and safer.

To learn more about our mission to help build a better Internet, [start here](https://www.cloudflare.com/learning/what-is-cloudflare/). If you're looking for a new career direction, check out [our open positions](http://www.cloudflare.com/careers).

[Discuss on Hacker News](https://news.ycombinator.com/item?id=47089505 "Discuss on Hacker News")

[Developers](https://blog.cloudflare.com/tag/developers/) [Developer Platform](https://blog.cloudflare.com/tag/developer-platform/) [AI](https://blog.cloudflare.com/tag/ai/) [Workers AI](https://blog.cloudflare.com/tag/workers-ai/) [Cloudflare Workers](https://blog.cloudflare.com/tag/workers/) [Optimization](https://blog.cloudflare.com/tag/optimization/) [Open Source](https://blog.cloudflare.com/tag/open-source/)

Follow on X

Matt Carey\| [mattzcarey](https://x.com/mattzcarey)

Cloudflare\| [@cloudflare](https://x.com/@cloudflare)

Related posts

February 13, 2026 9:00 AM

[**Shedding old code with ecdysis: graceful restarts for Rust services at Cloudflare**](https://blog.cloudflare.com/ecdysis-rust-graceful-restarts/)

ecdysis is a Rust library enabling zero-downtime upgrades for network services. After five years protecting millions of connections at Cloudflare, it’s now open source....

By - [Manuel Olguín Muñoz](https://blog.cloudflare.com/author/manuel-olguin-munoz/)


[Rust,](https://blog.cloudflare.com/tag/rust/)[Open Source,](https://blog.cloudflare.com/tag/open-source/)[Infrastructure,](https://blog.cloudflare.com/tag/infrastructure/)[Engineering,](https://blog.cloudflare.com/tag/engineering/)[Edge,](https://blog.cloudflare.com/tag/edge/)[Developers,](https://blog.cloudflare.com/tag/developers/)[Developer Platform,](https://blog.cloudflare.com/tag/developer-platform/)[Application Services,](https://blog.cloudflare.com/tag/application-services/)[Rust](https://blog.cloudflare.com/tag/rust/)

February 12, 2026 9:03 AM

[**Introducing Markdown for Agents**](https://blog.cloudflare.com/markdown-for-agents/)

The way content is discovered online is shifting, from traditional search engines to AI agents that need structured data from a Web built for humans. It’s time to consider not just human visitors, but start to treat agents as first-class citizens. Markdown for Agents automatically converts any HTML page requested from our network to markdown....

By - [Celso Martinho](https://blog.cloudflare.com/author/celso/),

- [Will Allen](https://blog.cloudflare.com/author/will-allen/)


[AI,](https://blog.cloudflare.com/tag/ai/)[Agents,](https://blog.cloudflare.com/tag/agents/)[Developers,](https://blog.cloudflare.com/tag/developers/)[Developer Platform](https://blog.cloudflare.com/tag/developer-platform/)

February 05, 2026 9:00 AM

[**2025 Q4 DDoS threat report: A record-setting 31.4 Tbps attack caps a year of massive DDoS assaults**](https://blog.cloudflare.com/ddos-threat-report-2025-q4/)

The number of DDoS attacks more than doubled in 2025. The network layer is under particular threat as hyper-volumetric attacks grew 700%....

By - [Omer Yoachimik](https://blog.cloudflare.com/author/omer/),

- [Jorge Pacheco](https://blog.cloudflare.com/author/jorge/),

- [Cloudforce One](https://blog.cloudflare.com/author/cloudforce/)


[DDoS Reports,](https://blog.cloudflare.com/tag/ddos-reports/)[DDoS,](https://blog.cloudflare.com/tag/ddos/)[Cloudforce One,](https://blog.cloudflare.com/tag/cloudforce-one/)[Security,](https://blog.cloudflare.com/tag/security/)[Advanced DDoS,](https://blog.cloudflare.com/tag/advanced-ddos/)[AI](https://blog.cloudflare.com/tag/ai/)

January 30, 2026 12:01 PM

[**Google’s AI advantage: why crawler separation is the only path to a fair Internet**](https://blog.cloudflare.com/uk-google-ai-crawler-policy/)

Google's dual-purpose crawler creates an unfair AI advantage. To protect publishers and foster competition, the UK’s Competition and Markets Authority must mandate crawler separation for search and AI....

By - [Maria Palmieri](https://blog.cloudflare.com/author/maria-palmieri/),

- [Sebastian Hufnagel](https://blog.cloudflare.com/author/sebastian-hufnagel/)


[AI,](https://blog.cloudflare.com/tag/ai/)[AI Bots,](https://blog.cloudflare.com/tag/ai-bots/)[Google,](https://blog.cloudflare.com/tag/google/)[Legal,](https://blog.cloudflare.com/tag/legal/)[Policy & Legal](https://blog.cloudflare.com/tag/policy/)
