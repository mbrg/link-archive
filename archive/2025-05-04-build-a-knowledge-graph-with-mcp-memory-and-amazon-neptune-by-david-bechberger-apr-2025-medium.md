---
title: "Build a Knowledge Graph with MCP Memory and Amazon Neptune | by David Bechberger | Apr, 2025 | Medium"
tags:
   - Generative AI
   - Knowledge Graph
   - Graph Database
   - Amazon Neptune
   - MCP Server
link: https://medium.com/@bechbd/build-a-knowledge-graph-with-mcp-memory-and-amazon-neptune-6dbf191c1f6c
date: 2025-05-04
summary: "This article details the streamlined process of building a knowledge graph using Amazon Neptune, the Model Context Protocol (MCP), and an AI assistant, specifically Anthropic's Claude. By leveraging the `neptune-memory` MCP server, users can construct a "Fact" graph without complex coding. This involves defining entities, relations, and observations during conversational interactions with the AI. The integration allows for persistent memory, enabling multi-session knowledge retrieval across AI tools. This approach significantly lowers barriers for developers looking to utilize knowledge graphs in generative AI workflows, enhancing information connectivity efficiently."
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

[![David Bechberger](https://miro.medium.com/v2/resize:fill:88:88/0*Kxvp7rPY4J-HjUUd.jpg)](https://medium.com/@bechbd?source=post_page---byline--6dbf191c1f6c---------------------------------------)

[David Bechberger](https://medium.com/@bechbd?source=post_page---byline--6dbf191c1f6c---------------------------------------)

·

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Ffed255a2d1c2%2F6dbf191c1f6c&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40bechbd%2Fbuild-a-knowledge-graph-with-mcp-memory-and-amazon-neptune-6dbf191c1f6c&user=David+Bechberger&userId=fed255a2d1c2&source=post_page-fed255a2d1c2--byline--6dbf191c1f6c---------------------post_header------------------)

6 min read

·

3 days ago

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

![](https://miro.medium.com/v2/da:true/resize:fit:0/5c50caa54067fd622d2f0fac18392213bf92f6e2fae89b691e62bceb40885e74)

## Sign up to discover human stories that deepen your understanding of the world.

## Free

Distraction-free reading. No ads.

Organize your knowledge with lists and highlights.

Tell your story. Find your audience.

Sign up for free

## Membership

Read member-only stories

Support writers you read most

Earn money for your writing

Listen to audio narrations

Read offline with the Medium app

Try for $5/month

[Amazon Neptune](https://medium.com/tag/amazon-neptune?source=post_page-----6dbf191c1f6c---------------------------------------)

[Mcp Server](https://medium.com/tag/mcp-server?source=post_page-----6dbf191c1f6c---------------------------------------)

[Knowledge Graph](https://medium.com/tag/knowledge-graph?source=post_page-----6dbf191c1f6c---------------------------------------)

[Ai Agent Development](https://medium.com/tag/ai-agent-development?source=post_page-----6dbf191c1f6c---------------------------------------)

[Graph Database](https://medium.com/tag/graph-database?source=post_page-----6dbf191c1f6c---------------------------------------)

[![David Bechberger](https://miro.medium.com/v2/resize:fill:96:96/0*Kxvp7rPY4J-HjUUd.jpg)](https://medium.com/@bechbd?source=post_page---post_author_info--6dbf191c1f6c---------------------------------------)

[![David Bechberger](https://miro.medium.com/v2/resize:fill:128:128/0*Kxvp7rPY4J-HjUUd.jpg)](https://medium.com/@bechbd?source=post_page---post_author_info--6dbf191c1f6c---------------------------------------)

Follow

[**Written by David Bechberger**](https://medium.com/@bechbd?source=post_page---post_author_info--6dbf191c1f6c---------------------------------------)

[33 Followers](https://medium.com/@bechbd/followers?source=post_page---post_author_info--6dbf191c1f6c---------------------------------------)

· [3 Following](https://medium.com/@bechbd/following?source=post_page---post_author_info--6dbf191c1f6c---------------------------------------)

Follow

## No responses yet

![](https://miro.medium.com/v2/resize:fill:32:32/1*dmbNkD5D-u45r44go_cf0g.png)

Write a response

[What are your thoughts?](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40bechbd%2Fbuild-a-knowledge-graph-with-mcp-memory-and-amazon-neptune-6dbf191c1f6c&source=---post_responses--6dbf191c1f6c---------------------respond_sidebar------------------)

Cancel

Respond

## More from David Bechberger

![Simplifying Amazon Neptune Integration with MCP Servers](https://miro.medium.com/v2/resize:fit:679/0*XwO6uDdU0e-sHgAq)

[![David Bechberger](https://miro.medium.com/v2/resize:fill:20:20/0*Kxvp7rPY4J-HjUUd.jpg)](https://medium.com/@bechbd?source=post_page---author_recirc--6dbf191c1f6c----0---------------------10e0e376_3b4a_4c22_a561_785a6a76d835--------------)

[David Bechberger](https://medium.com/@bechbd?source=post_page---author_recirc--6dbf191c1f6c----0---------------------10e0e376_3b4a_4c22_a561_785a6a76d835--------------)

[**Simplifying Amazon Neptune Integration with MCP Servers**\\
\\
**Recently, Amazon Neptune has released several example Amazon Neptune MCP servers, demonstrating how you can use Model Context Protocol…**](https://medium.com/@bechbd/simplifying-amazon-neptune-integration-with-mcp-servers-8693d78063ae?source=post_page---author_recirc--6dbf191c1f6c----0---------------------10e0e376_3b4a_4c22_a561_785a6a76d835--------------)

3d ago

[2](https://medium.com/@bechbd/simplifying-amazon-neptune-integration-with-mcp-servers-8693d78063ae?source=post_page---author_recirc--6dbf191c1f6c----0---------------------10e0e376_3b4a_4c22_a561_785a6a76d835--------------)

![Knowledge Graphs and Generative AI (GraphRAG) with Amazon Neptune and LlamaIndex (Part 1) —…](https://miro.medium.com/v2/resize:fit:679/0*Q_lK8HInV4XlRD1J)

[![David Bechberger](https://miro.medium.com/v2/resize:fill:20:20/0*Kxvp7rPY4J-HjUUd.jpg)](https://medium.com/@bechbd?source=post_page---author_recirc--6dbf191c1f6c----1---------------------10e0e376_3b4a_4c22_a561_785a6a76d835--------------)

[David Bechberger](https://medium.com/@bechbd?source=post_page---author_recirc--6dbf191c1f6c----1---------------------10e0e376_3b4a_4c22_a561_785a6a76d835--------------)

[**Knowledge Graphs and Generative AI (GraphRAG) with Amazon Neptune and LlamaIndex (Part 1) —…**\\
\\
**In this blog series, we will explore various methods that can be used with LlamaIndex to create applications built on top of LlamaIndex to…**](https://medium.com/@bechbd/knowledge-graphs-and-generative-ai-graphrag-with-amazon-neptune-and-llamaindex-part-1-39cd7255bac4?source=post_page---author_recirc--6dbf191c1f6c----1---------------------10e0e376_3b4a_4c22_a561_785a6a76d835--------------)

Aug 12, 2024

[92](https://medium.com/@bechbd/knowledge-graphs-and-generative-ai-graphrag-with-amazon-neptune-and-llamaindex-part-1-39cd7255bac4?source=post_page---author_recirc--6dbf191c1f6c----1---------------------10e0e376_3b4a_4c22_a561_785a6a76d835--------------)

![Knowledge Graph And Generative AI applications (GraphRAG) with Amazon Neptune and LlamaIndex (Part…](https://miro.medium.com/v2/resize:fit:679/1*BAnb1NMuYN4LPlCGyrWPOQ.png)

[![David Bechberger](https://miro.medium.com/v2/resize:fill:20:20/0*Kxvp7rPY4J-HjUUd.jpg)](https://medium.com/@bechbd?source=post_page---author_recirc--6dbf191c1f6c----2---------------------10e0e376_3b4a_4c22_a561_785a6a76d835--------------)

[David Bechberger](https://medium.com/@bechbd?source=post_page---author_recirc--6dbf191c1f6c----2---------------------10e0e376_3b4a_4c22_a561_785a6a76d835--------------)

[**Knowledge Graph And Generative AI applications (GraphRAG) with Amazon Neptune and LlamaIndex (Part…**\\
\\
**This is the second post in this blog series where we are explore various methods that can be used with LlamaIndex to create applications…**](https://medium.com/@bechbd/knowledge-graph-and-generative-ai-applications-graphrag-with-amazon-neptune-and-llamaindex-part-0942b2beec4b?source=post_page---author_recirc--6dbf191c1f6c----2---------------------10e0e376_3b4a_4c22_a561_785a6a76d835--------------)

Aug 12, 2024

[51](https://medium.com/@bechbd/knowledge-graph-and-generative-ai-applications-graphrag-with-amazon-neptune-and-llamaindex-part-0942b2beec4b?source=post_page---author_recirc--6dbf191c1f6c----2---------------------10e0e376_3b4a_4c22_a561_785a6a76d835--------------)

[See all from David Bechberger](https://medium.com/@bechbd?source=post_page---author_recirc--6dbf191c1f6c---------------------------------------)

## Recommended from Medium

![Deploy an in-house Vision Language Model to parse millions of documents: say goodbye to Gemini and…](https://miro.medium.com/v2/resize:fit:679/0*HIHlA_MVJSS7nD51)

[![Towards AI](https://miro.medium.com/v2/resize:fill:20:20/1*JyIThO-cLjlChQLb6kSlVQ.png)](https://medium.com/towards-artificial-intelligence?source=post_page---read_next_recirc--6dbf191c1f6c----0---------------------4cbd54ea_0072_42c1_853f_1a2cd5941a4f--------------)

In

[Towards AI](https://medium.com/towards-artificial-intelligence?source=post_page---read_next_recirc--6dbf191c1f6c----0---------------------4cbd54ea_0072_42c1_853f_1a2cd5941a4f--------------)

by

[Jeremy Arancio](https://medium.com/@jeremyarancio?source=post_page---read_next_recirc--6dbf191c1f6c----0---------------------4cbd54ea_0072_42c1_853f_1a2cd5941a4f--------------)

[**Deploy an in-house Vision Language Model to parse millions of documents: say goodbye to Gemini and…**\\
\\
**How to build a Document Parsing Pipeline to process millions of documents using Qwen-2.5-VL, vLLM, and AWS Batch.**](https://medium.com/towards-artificial-intelligence/deploy-an-in-house-vision-language-model-to-parse-millions-of-documents-say-goodbye-to-gemini-and-cdac6f77aff5?source=post_page---read_next_recirc--6dbf191c1f6c----0---------------------4cbd54ea_0072_42c1_853f_1a2cd5941a4f--------------)

Apr 22

[1K\\
\\
16](https://medium.com/towards-artificial-intelligence/deploy-an-in-house-vision-language-model-to-parse-millions-of-documents-say-goodbye-to-gemini-and-cdac6f77aff5?source=post_page---read_next_recirc--6dbf191c1f6c----0---------------------4cbd54ea_0072_42c1_853f_1a2cd5941a4f--------------)

![What Every AI Engineer Should Know About A2A, MCP & ACP](https://miro.medium.com/v2/resize:fit:679/1*bWg9FT2_smxDuWwntjFWVg.png)

[![Edwin Lisowski](https://miro.medium.com/v2/resize:fill:20:20/1*kfhhNvpxp7Xpq_W6Pds0Iw.png)](https://medium.com/@elisowski?source=post_page---read_next_recirc--6dbf191c1f6c----1---------------------4cbd54ea_0072_42c1_853f_1a2cd5941a4f--------------)

[Edwin Lisowski](https://medium.com/@elisowski?source=post_page---read_next_recirc--6dbf191c1f6c----1---------------------4cbd54ea_0072_42c1_853f_1a2cd5941a4f--------------)

[**What Every AI Engineer Should Know About A2A, MCP & ACP**\\
\\
**How today’s top AI protocols help agents talk, think, and work together**](https://medium.com/@elisowski/what-every-ai-engineer-should-know-about-a2a-mcp-acp-8335a210a742?source=post_page---read_next_recirc--6dbf191c1f6c----1---------------------4cbd54ea_0072_42c1_853f_1a2cd5941a4f--------------)

Apr 24

[242\\
\\
8](https://medium.com/@elisowski/what-every-ai-engineer-should-know-about-a2a-mcp-acp-8335a210a742?source=post_page---read_next_recirc--6dbf191c1f6c----1---------------------4cbd54ea_0072_42c1_853f_1a2cd5941a4f--------------)

![GraphRAG: Enhancing Retrieval Augmented Generation with Knowledge Graphs](https://miro.medium.com/v2/resize:fit:679/1*OvH3R4erohekb7yd262v8A.png)

[![Divyansh Bhatia](https://miro.medium.com/v2/resize:fill:20:20/1*t-2DlNlqOV3YDWm-XKEj1Q.jpeg)](https://medium.com/@divyanshbhatiajm19?source=post_page---read_next_recirc--6dbf191c1f6c----0---------------------4cbd54ea_0072_42c1_853f_1a2cd5941a4f--------------)

[Divyansh Bhatia](https://medium.com/@divyanshbhatiajm19?source=post_page---read_next_recirc--6dbf191c1f6c----0---------------------4cbd54ea_0072_42c1_853f_1a2cd5941a4f--------------)

[**GraphRAG: Enhancing Retrieval Augmented Generation with Knowledge Graphs**\\
\\
**In the rapidly evolving landscape of AI, Retrieval Augmented Generation (RAG) has emerged as a powerful technique for enhancing Large…**](https://medium.com/@divyanshbhatiajm19/graphrag-enhancing-retrieval-augmented-generation-with-knowledge-graphs-fc15c3901414?source=post_page---read_next_recirc--6dbf191c1f6c----0---------------------4cbd54ea_0072_42c1_853f_1a2cd5941a4f--------------)

Apr 17

![Knowledge Graph & Attention Mechanism.](https://miro.medium.com/v2/resize:fit:679/0*NGic0QU9QJ455N52)

[![Jeff Zhang](https://miro.medium.com/v2/resize:fill:20:20/1*QoTJnqdfnQCzDHpHv0Cb2A.png)](https://medium.com/@zjffdu?source=post_page---read_next_recirc--6dbf191c1f6c----1---------------------4cbd54ea_0072_42c1_853f_1a2cd5941a4f--------------)

[Jeff Zhang](https://medium.com/@zjffdu?source=post_page---read_next_recirc--6dbf191c1f6c----1---------------------4cbd54ea_0072_42c1_853f_1a2cd5941a4f--------------)

[**Knowledge Graph & Attention Mechanism.**\\
\\
**What if two powerful ideas in AI — attention and knowledge graphs — weren’t so different after all? One helps models like ChatGPT…**](https://medium.com/@zjffdu/knowledge-graph-attention-mechanism-134a0f7c4cec?source=post_page---read_next_recirc--6dbf191c1f6c----1---------------------4cbd54ea_0072_42c1_853f_1a2cd5941a4f--------------)

Apr 21

[6](https://medium.com/@zjffdu/knowledge-graph-attention-mechanism-134a0f7c4cec?source=post_page---read_next_recirc--6dbf191c1f6c----1---------------------4cbd54ea_0072_42c1_853f_1a2cd5941a4f--------------)

![AI-Driven Knowledge Graph Schema Discovery: Concept and Implementation](https://miro.medium.com/v2/resize:fit:679/1*DQl49VGEc9sHWpiZxyDDrQ.png)

[![Pallavi Sinha](https://miro.medium.com/v2/resize:fill:20:20/0*UP-HZmqvkX3gCUVs)](https://medium.com/@pallavisinha12?source=post_page---read_next_recirc--6dbf191c1f6c----2---------------------4cbd54ea_0072_42c1_853f_1a2cd5941a4f--------------)

[Pallavi Sinha](https://medium.com/@pallavisinha12?source=post_page---read_next_recirc--6dbf191c1f6c----2---------------------4cbd54ea_0072_42c1_853f_1a2cd5941a4f--------------)

[**AI-Driven Knowledge Graph Schema Discovery: Concept and Implementation**\\
\\
**A knowledge graph structures data into entities (things like people, product, or event) and relationships (how these entities are…**](https://medium.com/@pallavisinha12/ai-driven-knowledge-graph-schema-discovery-concept-and-implementation-50843bb90fbb?source=post_page---read_next_recirc--6dbf191c1f6c----2---------------------4cbd54ea_0072_42c1_853f_1a2cd5941a4f--------------)

Mar 7

[179\\
\\
4](https://medium.com/@pallavisinha12/ai-driven-knowledge-graph-schema-discovery-concept-and-implementation-50843bb90fbb?source=post_page---read_next_recirc--6dbf191c1f6c----2---------------------4cbd54ea_0072_42c1_853f_1a2cd5941a4f--------------)

![Graph RAG vs. Vector RAG](https://miro.medium.com/v2/resize:fit:679/1*i3dPsnlokUcv1KBLG8mEtg.gif)

[![AI Advances](https://miro.medium.com/v2/resize:fill:20:20/1*R8zEd59FDf0l8Re94ImV0Q.png)](https://medium.com/ai-advances?source=post_page---read_next_recirc--6dbf191c1f6c----3---------------------4cbd54ea_0072_42c1_853f_1a2cd5941a4f--------------)

In

[AI Advances](https://medium.com/ai-advances?source=post_page---read_next_recirc--6dbf191c1f6c----3---------------------4cbd54ea_0072_42c1_853f_1a2cd5941a4f--------------)

by

[Rudresh Narwal 👨‍💻](https://medium.com/@rudresh.narwal?source=post_page---read_next_recirc--6dbf191c1f6c----3---------------------4cbd54ea_0072_42c1_853f_1a2cd5941a4f--------------)

[**Graph RAG vs. Vector RAG**\\
\\
**A Simple Guide to Smarter AI (Why Relationships Beat Random Searches)**](https://medium.com/ai-advances/graph-rag-vs-vector-rag-cec6d5961140?source=post_page---read_next_recirc--6dbf191c1f6c----3---------------------4cbd54ea_0072_42c1_853f_1a2cd5941a4f--------------)

Feb 2

[102](https://medium.com/ai-advances/graph-rag-vs-vector-rag-cec6d5961140?source=post_page---read_next_recirc--6dbf191c1f6c----3---------------------4cbd54ea_0072_42c1_853f_1a2cd5941a4f--------------)

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

[iframe](https://www.google.com/recaptcha/enterprise/anchor?ar=1&k=6Le-uGgpAAAAAPprRaokM8AKthQ9KNGdoxaGUvVp&co=aHR0cHM6Ly9tZWRpdW0uY29tOjQ0Mw..&hl=en&v=Hi8UmRMnhdOBM3IuViTkapUP&size=invisible&cb=87346tymmh1x)
