---
title: "Build a Knowledge Graph with MCP Memory and Amazon Neptune ◆ by David Bechberger ◆ Apr, 2025 ◆ Medium"
tags:
   - Amazon Neptune
   - Knowledge Graph
   - MCP Server
   - Graph Database
   - Generative AI
link: https://medium.com/@bechbd/build-a-knowledge-graph-with-mcp-memory-and-amazon-neptune-6dbf191c1f6c
date: 2025-05-10
description: "The article outlines a method for building a knowledge graph using MCP Memory and Amazon Neptune without coding. It introduces the `neptune-memory` MCP server, which utilizes LLMs (like Anthropic's Claude) to facilitate conversation-based graph construction. Key elements include entities, relations, and observations making up the graph's structure. The system allows seamless integration and retrieval across sessions, enhancing information management across AI interactions. This presents significant implications for AI application development, making knowledge graph integration more user-friendly and accessible."
---

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F6dbf191c1f6c&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderUser&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40bechbd%2Fbuild-a-knowledge-graph-with-mcp-memory-and-amazon-neptune-6dbf191c1f6c&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Homepage](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40bechbd%2Fbuild-a-knowledge-graph-with-mcp-memory-and-amazon-neptune-6dbf191c1f6c&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

# Build a Knowledge Graph with MCP Memory and Amazon Neptune

[![David Bechberger](https://miro.medium.com/v2/resize:fill:64:64/0*Kxvp7rPY4J-HjUUd.jpg)](https://medium.com/@bechbd?source=post_page---byline--6dbf191c1f6c---------------------------------------)

[David Bechberger](https://medium.com/@bechbd?source=post_page---byline--6dbf191c1f6c---------------------------------------)

Follow

6 min read

·

Apr 30, 2025

6

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D6dbf191c1f6c&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40bechbd%2Fbuild-a-knowledge-graph-with-mcp-memory-and-amazon-neptune-6dbf191c1f6c&source=---header_actions--6dbf191c1f6c---------------------post_audio_button------------------)

Share

_Note: For foundational knowledge about MCP and its benefits, please refer to the_ [_Introduction_](https://modelcontextprotocol.io/introduction) _on the MCP website and this post on a_ [_Model Context Protocol (MCP) and Amazon Bedrock_](https://community.aws/content/2uFvyCPQt7KcMxD9ldsJyjZM1Wp/model-context-protocol-mcp-and-amazon-bedrock) _. For information on example_ [_Amazon Neptune MCP servers_](https://github.com/aws-samples/amazon-neptune-generative-ai-samples/tree/main/neptune-mcp-servers) _, please refer to the blog post_ [_Simplifying Amazon Neptune Integration with MCP Servers_](https://community.aws/content/2ka3KTHYB2zwAaIhqTK1cLWpocH/simplifying-amazon-neptune-integration-with-mcp-servers) _._

Knowledge graphs are becoming increasingly useful when working with Generative AI, as they help model how different pieces of information connect to each other. Up until now, building these graphs has been pretty challenging — you needed to know how to code, understand graph data modeling, work with specialized query languages, and handle complex tasks like entity extraction and resolution. That’s a lot to learn just to get started!

We’re going to show you an easier way to build a knowledge graph — by simply having a conversation with an AI assistant. In this post, we’ll walk through using `neptune-memory` along with an LLM of your choice, in our case we will use Anthropic's Claude, and Amazon Neptune to create a knowledge graph through conversation, no complex coding required!

# Prerequisites and Setup

Before we get started, there are a few prerequisites you need to have installed on your system or in your AWS account.

- To run these servers, you must install `uv` following the directions [here](https://docs.astral.sh/uv/getting-started/installation/). You will also need to install Python 3.12 using `uv python install 3.12`
- An MCP client — There are a variety of MCP client applications available such as [Cursor](http://cursor.com/), [Cline](https://cline.bot/), [Claude Code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview), etc., but for this post I will be using Anthropic’s [Claude Desktop](https://claude.ai/download) to demonstrate how you can leverage these servers.
- An Amazon Neptune Database or an Amazon Neptune Analytics graph — Verify that your MCP client has network access to the Neptune endpoint for your graph/cluster
- The AWS CLI with appropriate credentials configured as the MCP server uses the credentials chain of the CLI to provide authentication. Please refer to these [directions](https://docs.aws.amazon.com/cli/v1/userguide/cli-chap-configure.html) for options and configuration.

Once the prerequisites are configured, the next step is to install and configure the `neptune-memory` MCP server. While the configuration may vary based on the client used, the configuration for Claude Desktop for the `neptune-memory` server looks like:

```
{
  "mcpServers": {
    "Neptune Memory": {
      "command": "uvx",
      "args": [\
        "https://github.com/aws-samples/amazon-neptune-generative-ai-samples/releases/download/mcp-servers-v0.0.9-beta/neptune_memory_mcp_server-0.0.9-py3-none-any.whl"\
       ],
      "env": {
        "FASTMCP_LOG_LEVEL": "INFO",
        "NEPTUNE_MEMORY_ENDPOINT": "<INSERT NEPTUNE ENDPOINT IN FORMAT SPECIFIED BELOW>"
      }
    }
  }
}
```

When specifying the Neptune Endpoint, the following formats are expected:

For Neptune Database: `neptune-db://<Cluster Endpoint>`

For Neptune Analytics: `neptune-graph://<graph identifier>`

# Building our Knowledge Graph

Let’s talk about the `neptune-memory` MCP server we'll be using to build our knowledge graph. This server helps systems (like AI agents) remember information across different conversations by creating what we call a "Fact" knowledge graph. Think of it as a way to connect and store important pieces of information. Here's how it works:

The graph uses three main building blocks:

- **Entity** — These are the “facts” we want to remember. Each one has its own ID, a type, and a list of observations. They show up as nodes in the graph.
- **Relation** — These show how different facts connect to each other. They appear as lines (or edges) connecting two entities.
- **Observation** — These are extra details about each fact, stored as text attached to the entity nodes.

This straightforward setup lets us create a web of connected information — kind of like a digital memory bank, that helps us understand how different pieces of information relate to each other. It’s particularly useful when we want to get a clear picture of a specific topic.

To demonstrate how we can create a fact knowledge graph, let’s choose a specific topic, in this case let’s build a graph about me. To start, let’s first connect to our memory and see what information already exists.

![](https://miro.medium.com/v2/resize:fit:700/0*uj3WfPAdM3vt9hdc)

It looks like our graph is empty, so let’s start by adding some information to a prompt.

![](https://miro.medium.com/v2/resize:fit:700/0*BZZmu3x_RCbZdg8d)

Let’s see what happens when we run the prompt. The LLM goes through the text and picks out important pieces like People and Technologies, along with how they’re connected to each other. It then uses the `neptune-memory` MCP server to add this information to our graph using openCypher statements (don't worry if that sounds technical - the system handles it for us). Want to see what we've created? We can ask for a visualization of our knowledge graph to get a clear picture of how everything fits together.

![](https://miro.medium.com/v2/resize:fit:700/0*L7haT-su18dtoJQh)

Looking at the visualization, we can see that our LLM has done a nice job pulling out important information and showing how different pieces connect to each other. While this is useful, we’ve only used information we directly provided — and knowledge graphs really shine when they can connect dots from different sources. Let’s take this a step further and see what happens when we let the LLM tap into its broader knowledge. For example, we can ask it to tell us more about Dave Bechberger and Amazon Neptune, adding these extra details to our graph.

![](https://miro.medium.com/v2/resize:fit:700/0*Yan962tSbAl8pZMU)

Nice! It looks like Claude dug up some interesting tidbits. For Dave Bechberger, it found out he’s an author, which is pretty cool. And for Amazon Neptune, we now know when the service was launched. These are great examples of how an LLM can fill in gaps with publicly available info. Let’s take a look at our updated knowledge graph and see how these new facts fit into the bigger picture.

![](https://miro.medium.com/v2/resize:fit:700/0*P-CLg4D1PzBozbSe)

As you can see, our knowledge graph now includes all these new connections and facts alongside our original information. One of the handy things about setting this up is that we can now ask our LLM to pull information from the graph and give us useful summaries of what it knows. Think of it as having a smart assistant that can connect the dots between different pieces of information we’ve collected.

![](https://miro.medium.com/v2/resize:fit:700/0*zVkzS7U3eMGoGTG-)

Storing and retrieving data in one session is useful, but the real magic happens when we use this information across different chats, tools, and even with different AI assistants. Let’s test this out. Go ahead and open up a fresh chat in Claude Desktop. Now, ask this new chat about some of the information we’ve stored in our graph. Pretty neat, right? You’ll see that we can still pull up all that knowledge we’ve gathered, even in our new conversation. This is what makes a persistent memory so powerful — it’s like having a shared brain that different AIs can tap into whenever they need it.

![](https://miro.medium.com/v2/resize:fit:700/0*tDNA1hM7dZ4IRkGe)

Let’s wrap up what we’ve accomplished with the `neptune-memory` MCP server. The cool thing is, we didn't have to write any code at all, but we still managed to:

- Set up a “fact” knowledge graph that serves as a memory bank
- Add information from our conversations to the graph
- Expand the graph with extra public information that Claude knew about
- Use this stored knowledge across different chat sessions

Bottom line? Adding these MCP servers to your workflow makes it much easier to work with Amazon Neptune when building knowledge graphs. No complex coding required — just straightforward conversations that get the job done.

[Amazon Neptune](https://medium.com/tag/amazon-neptune?source=post_page-----6dbf191c1f6c---------------------------------------)

[Mcp Server](https://medium.com/tag/mcp-server?source=post_page-----6dbf191c1f6c---------------------------------------)

[Knowledge Graph](https://medium.com/tag/knowledge-graph?source=post_page-----6dbf191c1f6c---------------------------------------)

[Ai Agent Development](https://medium.com/tag/ai-agent-development?source=post_page-----6dbf191c1f6c---------------------------------------)

[Graph Database](https://medium.com/tag/graph-database?source=post_page-----6dbf191c1f6c---------------------------------------)

[![David Bechberger](https://miro.medium.com/v2/resize:fill:96:96/0*Kxvp7rPY4J-HjUUd.jpg)](https://medium.com/@bechbd?source=post_page---post_author_info--6dbf191c1f6c---------------------------------------)

[![David Bechberger](https://miro.medium.com/v2/resize:fill:128:128/0*Kxvp7rPY4J-HjUUd.jpg)](https://medium.com/@bechbd?source=post_page---post_author_info--6dbf191c1f6c---------------------------------------)

Follow

[**Written by David Bechberger**](https://medium.com/@bechbd?source=post_page---post_author_info--6dbf191c1f6c---------------------------------------)

[39 followers](https://medium.com/@bechbd/followers?source=post_page---post_author_info--6dbf191c1f6c---------------------------------------)

· [3 following](https://medium.com/@bechbd/following?source=post_page---post_author_info--6dbf191c1f6c---------------------------------------)

Follow

## No responses yet

![](https://miro.medium.com/v2/resize:fill:32:32/1*dmbNkD5D-u45r44go_cf0g.png)

Write a response

[What are your thoughts?](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40bechbd%2Fbuild-a-knowledge-graph-with-mcp-memory-and-amazon-neptune-6dbf191c1f6c&source=---post_responses--6dbf191c1f6c---------------------respond_sidebar------------------)

Cancel

Respond

## More from David Bechberger

![Simplifying Amazon Neptune Integration with MCP Servers](https://miro.medium.com/v2/resize:fit:679/0*XwO6uDdU0e-sHgAq)

[![David Bechberger](https://miro.medium.com/v2/resize:fill:20:20/0*Kxvp7rPY4J-HjUUd.jpg)](https://medium.com/@bechbd?source=post_page---author_recirc--6dbf191c1f6c----0---------------------d8ac8f37_74c2_4bf6_bb45_154b9a4af3ae--------------)

[David Bechberger](https://medium.com/@bechbd?source=post_page---author_recirc--6dbf191c1f6c----0---------------------d8ac8f37_74c2_4bf6_bb45_154b9a4af3ae--------------)

[**Simplifying Amazon Neptune Integration with MCP Servers**\\
\\
**Recently, Amazon Neptune has released several example Amazon Neptune MCP servers, demonstrating how you can use Model Context Protocol…**](https://medium.com/@bechbd/simplifying-amazon-neptune-integration-with-mcp-servers-8693d78063ae?source=post_page---author_recirc--6dbf191c1f6c----0---------------------d8ac8f37_74c2_4bf6_bb45_154b9a4af3ae--------------)

Apr 30

![Knowledge Graphs and Generative AI (GraphRAG) with Amazon Neptune and LlamaIndex (Part 1) —…](https://miro.medium.com/v2/resize:fit:679/0*Q_lK8HInV4XlRD1J)

[![David Bechberger](https://miro.medium.com/v2/resize:fill:20:20/0*Kxvp7rPY4J-HjUUd.jpg)](https://medium.com/@bechbd?source=post_page---author_recirc--6dbf191c1f6c----1---------------------d8ac8f37_74c2_4bf6_bb45_154b9a4af3ae--------------)

[David Bechberger](https://medium.com/@bechbd?source=post_page---author_recirc--6dbf191c1f6c----1---------------------d8ac8f37_74c2_4bf6_bb45_154b9a4af3ae--------------)

[**Knowledge Graphs and Generative AI (GraphRAG) with Amazon Neptune and LlamaIndex (Part 1) —…**\\
\\
**In this blog series, we will explore various methods that can be used with LlamaIndex to create applications built on top of LlamaIndex to…**](https://medium.com/@bechbd/knowledge-graphs-and-generative-ai-graphrag-with-amazon-neptune-and-llamaindex-part-1-39cd7255bac4?source=post_page---author_recirc--6dbf191c1f6c----1---------------------d8ac8f37_74c2_4bf6_bb45_154b9a4af3ae--------------)

Aug 12, 2024

![Knowledge Graph And Generative AI applications (GraphRAG) with Amazon Neptune and LlamaIndex (Part…](https://miro.medium.com/v2/resize:fit:679/1*BAnb1NMuYN4LPlCGyrWPOQ.png)

[![David Bechberger](https://miro.medium.com/v2/resize:fill:20:20/0*Kxvp7rPY4J-HjUUd.jpg)](https://medium.com/@bechbd?source=post_page---author_recirc--6dbf191c1f6c----2---------------------d8ac8f37_74c2_4bf6_bb45_154b9a4af3ae--------------)

[David Bechberger](https://medium.com/@bechbd?source=post_page---author_recirc--6dbf191c1f6c----2---------------------d8ac8f37_74c2_4bf6_bb45_154b9a4af3ae--------------)

[**Knowledge Graph And Generative AI applications (GraphRAG) with Amazon Neptune and LlamaIndex (Part…**\\
\\
**This is the second post in this blog series where we are explore various methods that can be used with LlamaIndex to create applications…**](https://medium.com/@bechbd/knowledge-graph-and-generative-ai-applications-graphrag-with-amazon-neptune-and-llamaindex-part-0942b2beec4b?source=post_page---author_recirc--6dbf191c1f6c----2---------------------d8ac8f37_74c2_4bf6_bb45_154b9a4af3ae--------------)

Aug 12, 2024

[See all from David Bechberger](https://medium.com/@bechbd?source=post_page---author_recirc--6dbf191c1f6c---------------------------------------)

## Recommended from Medium

![Text2Cypher: The Impact of Difficult Example Selection](https://miro.medium.com/v2/resize:fit:679/0*bLTX_MxjKIFv_Mwn)

[![Neo4j Developer Blog](https://miro.medium.com/v2/resize:fill:20:20/1*dbXVrszMTRob9qYMUY2lqg.png)](https://medium.com/neo4j?source=post_page---read_next_recirc--6dbf191c1f6c----0---------------------c7175fae_57bf_494f_b485_a3351cb5cd8d--------------)

In

[Neo4j Developer Blog](https://medium.com/neo4j?source=post_page---read_next_recirc--6dbf191c1f6c----0---------------------c7175fae_57bf_494f_b485_a3351cb5cd8d--------------)

by

[Makbule Gulcin Ozsoy](https://medium.com/@makbule.ozsoy_73232?source=post_page---read_next_recirc--6dbf191c1f6c----0---------------------c7175fae_57bf_494f_b485_a3351cb5cd8d--------------)

[**Text2Cypher: The Impact of Difficult Example Selection**\\
\\
**Examine How Subset Selection Strategies Impact Performance and Computational Efficiency**](https://medium.com/neo4j/text2cypher-the-impact-of-hard-example-selection-4a579454c292?source=post_page---read_next_recirc--6dbf191c1f6c----0---------------------c7175fae_57bf_494f_b485_a3351cb5cd8d--------------)

Apr 29

![MCP Made Simple: Connect Models to Real-World Data](https://miro.medium.com/v2/resize:fit:679/1*pENSXZFoGPGjrl-qKcD3CQ.png)

[![Dev Genius](https://miro.medium.com/v2/resize:fill:20:20/1*CvejhRq3NYsivxILYXEdfA.jpeg)](https://medium.com/dev-genius?source=post_page---read_next_recirc--6dbf191c1f6c----1---------------------c7175fae_57bf_494f_b485_a3351cb5cd8d--------------)

In

[Dev Genius](https://medium.com/dev-genius?source=post_page---read_next_recirc--6dbf191c1f6c----1---------------------c7175fae_57bf_494f_b485_a3351cb5cd8d--------------)

by

[Madhav Arora](https://medium.com/@madhavarora1988?source=post_page---read_next_recirc--6dbf191c1f6c----1---------------------c7175fae_57bf_494f_b485_a3351cb5cd8d--------------)

[**MCP Made Simple: Connect Models to Real-World Data**\\
\\
**TL;DR  Spin up a local SQLite MCP server, point your favourite LLM at it, and start talking SQL — in under five minutes.**](https://medium.com/dev-genius/mcp-made-simple-connect-models-to-real-world-data-62505b0e2baf?source=post_page---read_next_recirc--6dbf191c1f6c----1---------------------c7175fae_57bf_494f_b485_a3351cb5cd8d--------------)

5d ago

![Diffusion Models, Explained Simply](https://miro.medium.com/v2/resize:fit:679/1*_iFQi2IFPuGfa0lZmlKlmQ.png)

[![Data Science Collective](https://miro.medium.com/v2/resize:fill:20:20/1*0nV0Q-FBHj94Kggq00pG2Q.jpeg)](https://medium.com/data-science-collective?source=post_page---read_next_recirc--6dbf191c1f6c----0---------------------c7175fae_57bf_494f_b485_a3351cb5cd8d--------------)

In

[Data Science Collective](https://medium.com/data-science-collective?source=post_page---read_next_recirc--6dbf191c1f6c----0---------------------c7175fae_57bf_494f_b485_a3351cb5cd8d--------------)

by

[Vyacheslav Efimov](https://medium.com/@slavahead?source=post_page---read_next_recirc--6dbf191c1f6c----0---------------------c7175fae_57bf_494f_b485_a3351cb5cd8d--------------)

[**Diffusion Models, Explained Simply**\\
\\
**From noise to art: how to generate high-quality images using diffusion models**](https://medium.com/data-science-collective/diffusion-models-explained-simply-3a41fea596e0?source=post_page---read_next_recirc--6dbf191c1f6c----0---------------------c7175fae_57bf_494f_b485_a3351cb5cd8d--------------)

6d ago

[3](https://medium.com/data-science-collective/diffusion-models-explained-simply-3a41fea596e0?source=post_page---read_next_recirc--6dbf191c1f6c----0---------------------c7175fae_57bf_494f_b485_a3351cb5cd8d--------------)

![New winner: Qwen3–30B-A3B takes the crown for document Q&A](https://miro.medium.com/v2/resize:fit:679/1*yuVzMhCJyDENbyhwAsrkwA.png)

[![Billy Newport](https://miro.medium.com/v2/resize:fill:20:20/1*4NK88JyUNUAekydzgaoUHw.jpeg)](https://medium.com/@billynewport?source=post_page---read_next_recirc--6dbf191c1f6c----1---------------------c7175fae_57bf_494f_b485_a3351cb5cd8d--------------)

[Billy Newport](https://medium.com/@billynewport?source=post_page---read_next_recirc--6dbf191c1f6c----1---------------------c7175fae_57bf_494f_b485_a3351cb5cd8d--------------)

[**New winner: Qwen3–30B-A3B takes the crown for document Q&A**\\
\\
**Up to now, the Deepseek-Qwen-32B-R1 is the best local LLM for asking questions against a large document that I’ve tested. I use a large…**](https://medium.com/@billynewport/new-winner-qwen3-30b-a3b-takes-the-crown-for-document-q-a-197bac0c8a39?source=post_page---read_next_recirc--6dbf191c1f6c----1---------------------c7175fae_57bf_494f_b485_a3351cb5cd8d--------------)

May 1

[1](https://medium.com/@billynewport/new-winner-qwen3-30b-a3b-takes-the-crown-for-document-q-a-197bac0c8a39?source=post_page---read_next_recirc--6dbf191c1f6c----1---------------------c7175fae_57bf_494f_b485_a3351cb5cd8d--------------)

![Why You Should Build an MCP Server This Weekend](https://miro.medium.com/v2/resize:fit:679/0*62naVzWllpwZbqsk)

[![Coding Nexus](https://miro.medium.com/v2/resize:fill:20:20/1*KCZtO6-wFqmTaMmbTMicbw.png)](https://medium.com/coding-nexus?source=post_page---read_next_recirc--6dbf191c1f6c----2---------------------c7175fae_57bf_494f_b485_a3351cb5cd8d--------------)

In

[Coding Nexus](https://medium.com/coding-nexus?source=post_page---read_next_recirc--6dbf191c1f6c----2---------------------c7175fae_57bf_494f_b485_a3351cb5cd8d--------------)

by

[Code Pulse](https://medium.com/@CodePulse?source=post_page---read_next_recirc--6dbf191c1f6c----2---------------------c7175fae_57bf_494f_b485_a3351cb5cd8d--------------)

[**Why You Should Build an MCP Server This Weekend**\\
\\
**I haven’t seen an opportunity this wide open since the early days of mobile apps.**](https://medium.com/coding-nexus/why-you-should-build-an-mcp-server-this-weekend-dd965208c042?source=post_page---read_next_recirc--6dbf191c1f6c----2---------------------c7175fae_57bf_494f_b485_a3351cb5cd8d--------------)

6d ago

[14](https://medium.com/coding-nexus/why-you-should-build-an-mcp-server-this-weekend-dd965208c042?source=post_page---read_next_recirc--6dbf191c1f6c----2---------------------c7175fae_57bf_494f_b485_a3351cb5cd8d--------------)

![This new IDE from Google is an absolute game changer](https://miro.medium.com/v2/resize:fit:679/1*f-1HQQng85tbA7kwgECqoQ.png)

[![Coding Beauty](https://miro.medium.com/v2/resize:fill:20:20/1*ViyWUoh4zqx294no1eENxw.png)](https://medium.com/coding-beauty?source=post_page---read_next_recirc--6dbf191c1f6c----3---------------------c7175fae_57bf_494f_b485_a3351cb5cd8d--------------)

In

[Coding Beauty](https://medium.com/coding-beauty?source=post_page---read_next_recirc--6dbf191c1f6c----3---------------------c7175fae_57bf_494f_b485_a3351cb5cd8d--------------)

by

[Tari Ibaba](https://medium.com/@tariibaba?source=post_page---read_next_recirc--6dbf191c1f6c----3---------------------c7175fae_57bf_494f_b485_a3351cb5cd8d--------------)

[**This new IDE from Google is an absolute game changer**\\
\\
**This new IDE from Google is seriously revolutionary.**](https://medium.com/coding-beauty/new-google-project-idx-fae1fdd079c7?source=post_page---read_next_recirc--6dbf191c1f6c----3---------------------c7175fae_57bf_494f_b485_a3351cb5cd8d--------------)

Mar 11

[309](https://medium.com/coding-beauty/new-google-project-idx-fae1fdd079c7?source=post_page---read_next_recirc--6dbf191c1f6c----3---------------------c7175fae_57bf_494f_b485_a3351cb5cd8d--------------)

[See more recommendations](https://medium.com/?source=post_page---read_next_recirc--6dbf191c1f6c---------------------------------------)

[Help](https://help.medium.com/hc/en-us?source=post_page-----6dbf191c1f6c---------------------------------------)

[Status](https://medium.statuspage.io/?source=post_page-----6dbf191c1f6c---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----6dbf191c1f6c---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----6dbf191c1f6c---------------------------------------)

[Press](mailto:pressinquiries@medium.com)

[Blog](https://blog.medium.com/?source=post_page-----6dbf191c1f6c---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----6dbf191c1f6c---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----6dbf191c1f6c---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----6dbf191c1f6c---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----6dbf191c1f6c---------------------------------------)
