---
date: '2025-10-19'
description: Matt Brown emphasizes the critical role of a startup's data model in
  determining its success. The data model shapes product design, customer workflows,
  and competitive strategy. In crowded markets, a differentiated data model becomes
  essential, aiding in feature integration and enhancing user experience. Brown illustrates
  this with examples like Slack, Toast, and Notion, where foundational choices led
  to compounding advantages. As AI commoditizes technical barriers, the focus shifts
  to strategic data modeling. Founders must consciously design their data models to
  align with market realities, fostering long-term sustainability and competitive
  moats.
link: https://notes.mtb.xyz/p/your-data-model-is-your-destiny
tags:
- fintech
- startup_advice
- data_model
- vertical_software
- product_strategy
title: Your data model is your destiny - Matt Brown's Notes
---

[![Matt Brown's Notes](https://substackcdn.com/image/fetch/$s_!ky1q!,w_80,h_80,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd3e2a521-9211-46b1-ad0e-847b79a0aabe_746x746.png)](https://notes.mtb.xyz/)

# [Matt Brown's Notes](https://notes.mtb.xyz/)

SubscribeSign in

![User's avatar](https://substackcdn.com/image/fetch/$s_!oOGS!,w_64,h_64,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F4a2e671b-46fc-43ec-bb61-e86a56121204_259x228.png)

Discover more from Matt Brown's Notes

Notes on fintech, vertical software, and VC.

Subscribe

By subscribing, I agree to Substack's [Terms of Use](https://substack.com/tos), and acknowledge its [Information Collection Notice](https://substack.com/ccpa#personal-data-collected) and [Privacy Policy](https://substack.com/privacy).

Already have an account? Sign in

# Your data model is your destiny

### Your product's core abstractions determine whether new features compound into a moat or just add to a feature list. Here's how to get it right.

[Matt Brown](https://substack.com/@matttbrown)

Oct 14, 2025

3

Share

Product market fit is the startup holy grail. “Product” and “market” are essential, but a startup’s data model is the dark matter that holds them together.

**“Data model” refers to what a startup emphasizes in its product, i.e., which parts of reality matter most in how the product represents the world.** It’s the core concepts or objects a startup prioritizes and builds around, the load-bearing assumptions at the heart of their strategy and worldview. It’s partially captured in the database architecture (hence the name), but it shapes everything from the UI/UX to the product marketing, pricing model, and GTM strategy.

[![Abstract Geometric Texture](https://substackcdn.com/image/fetch/$s_!rKtk!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9be4eb95-95ab-4f22-afbc-ac13d41f868f_3000x2165.jpeg)](https://substackcdn.com/image/fetch/$s_!rKtk!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9be4eb95-95ab-4f22-afbc-ac13d41f868f_3000x2165.jpeg)

This shows up differently depending on the layer. In the database, it’s which tables are central and how they relate. In the product, it’s which UI elements dominate and what actions are easiest. In pricing, it’s what you charge by. In GTM, it’s the workflow or pain point you lead with. But they all stem from the same choice about what deserves to be the center of gravity.

Every founder has a data model, whether they realize it or not. Either you choose it explicitly or it gets inherited from whatever you’re copying. Most founders never articulate it. By the time the architecture solidifies around these implicit choices, it’s nearly impossible to change.

And that’s generally fine, because most companies shouldn’t innovate on their data model. Customers have existing mental models and workflows built around incumbent tools. Fighting that is expensive and slow. But at the extreme ends of markets—where you’re toppling multi-billion-dollar incumbents or creating entirely new categories—a distinctive data model becomes a critical and non-obvious edge.

The biggest breakout companies of the last decade often trace their success to an early, non-obvious data model choice that seemed minor at the time but proved decisive. Consider:

**Slack’s persistent channels vs 1:1/group messages**: While Yammer and HipChat replicated email’s ephemeral group messages, Slack made persistent, searchable channels the atomic unit. This created organizational memory—every decision, discussion, and document lives forever in context. Incumbents couldn’t match this without rebuilding from scratch.

[![](https://substackcdn.com/image/fetch/$s_!kV2x!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F505afe63-e760-4016-8ae3-25fa69d165b1_1702x683.png)](https://substackcdn.com/image/fetch/$s_!kV2x!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F505afe63-e760-4016-8ae3-25fa69d165b1_1702x683.png)

**Toast’s menu-item-centric architecture vs generic POS SKUs**: Toast makes menu items first-class objects with embedded restaurant logic—prep times, kitchen routing, and modifier hierarchies built in. Generic point-of-sale systems treat menu items as retail SKUs, requiring third-party integrations for kitchen workflows. Toast’s model enables native order routing and real-time kitchen management, plus natural extensions like ingredient-level inventory and prep-based labor scheduling—creating a locked-in ecosystem that becomes the restaurant’s operational backbone.

[![](https://substackcdn.com/image/fetch/$s_!CmTJ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbaabe7cf-5336-4b6d-b8b2-2dd0816886bf_1701x698.png)](https://substackcdn.com/image/fetch/$s_!CmTJ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbaabe7cf-5336-4b6d-b8b2-2dd0816886bf_1701x698.png)

**Notion’s blocks vs Google’s documents**: Google Docs gives you documents; Notion gives you Lego blocks. Every piece of content can be rearranged, nested, or transformed into databases, kanban boards, or wikis. This modularity collapses entire tool categories into one system. Traditional tools can’t compete without abandoning their document-centric architecture.

[![](https://substackcdn.com/image/fetch/$s_!Bbzh!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb4004988-63c2-4d02-b5f6-6618f8269c80_1702x709.png)](https://substackcdn.com/image/fetch/$s_!Bbzh!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb4004988-63c2-4d02-b5f6-6618f8269c80_1702x709.png)

**Figma’s canvas vs files**: Photoshop and Sketch are built on local files. Figma is built on a shared web canvas where everyone sees changes instantly. This eliminates version conflicts and “final\_final\_v2” chaos. Adobe couldn’t respond without deprecating their entire desktop-first ecosystem.

[![](https://substackcdn.com/image/fetch/$s_!eSfA!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff48f9836-9184-4193-91ad-e9d4435c7de1_1702x731.png)](https://substackcdn.com/image/fetch/$s_!eSfA!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff48f9836-9184-4193-91ad-e9d4435c7de1_1702x731.png)

**Rippling’s employee data model vs siloed tools**: Rippling treats the employee record as the lynchpin connecting HR, IT, payroll, and finance. Not separate products sharing data, but one product with multiple views. Each new product module is automatically more powerful than standalone alternatives because it inherits full employee context. Competitors remain trapped in single categories or attempt inferior integrations.

[![](https://substackcdn.com/image/fetch/$s_!TZ2k!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fba04b227-faea-4ba8-98e9-c859b1e0744d_1701x713.png)](https://substackcdn.com/image/fetch/$s_!TZ2k!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fba04b227-faea-4ba8-98e9-c859b1e0744d_1701x713.png)

**Klaviyo’s order-centric data model vs email-centric tools**: MailChimp optimizes for email campaigns. Klaviyo optimizes for customer lifetime value by making order data a first-class citizen alongside emails. This lets e-commerce brands segment by purchase behavior, not just email engagement. Generic email tools can’t match this without rebuilding for vertical-specific data.

[![](https://substackcdn.com/image/fetch/$s_!hmk2!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd5349cad-205b-4c29-bbe1-42157eb65ebc_1701x769.png)](https://substackcdn.com/image/fetch/$s_!hmk2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd5349cad-205b-4c29-bbe1-42157eb65ebc_1701x769.png)

**ServiceNow’s connected services vs standalone tickets**: Traditional help desks treat tickets like isolated emails. ServiceNow links every ticket to a service map—showing which system is down, who owns it, and what it affects downstream. This transforms IT from ticket-closing to problem-preventing, making ServiceNow irreplaceable once companies reorganize operations around this model.

[![](https://substackcdn.com/image/fetch/$s_!cjlu!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2a0c198b-7898-42ef-8602-c7c42f52da44_1736x714.png)](https://substackcdn.com/image/fetch/$s_!cjlu!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2a0c198b-7898-42ef-8602-c7c42f52da44_1736x714.png)

### Data models matter more than ever now

The importance of a differentiated data model is rising dramatically. AI is commoditizing code. Technical execution is table stakes rather than a competitive advantage. AI can generate code, but it can’t refactor the organizational reality customers have built around your architecture—the workflows, integrations, and institutional muscle memory that compound over time.

Meanwhile, many markets have become so crowded that single-product companies can’t survive. This is particularly true in vertical markets, where companies are [expanding into adjacent software products](https://notes.mtb.xyz/p/invisible-asymptotes-vertical-software), [embedding payments](https://notes.mtb.xyz/p/payfac-1000-words) and [other financial products](https://notes.mtb.xyz/p/embedded-fintech-1000-words), and even [competing with their customers’ labor and supply chains with AI and managed marketplaces](https://notes.mtb.xyz/p/vc-pe-envy).

**This all points to the same conclusion: when code is cheap, competition is fierce, and vertical depth matters, your data model is the foundation of your moat. The companies that win won’t be those with the most or even the best features. AI will democratize those. The winners will be built on a data model that captures something true about their market, which in turn creates compounding advantages competitors can’t replicate.**

Consider how this plays out. Rippling’s employee-centric model made it trivial to add payments, benefits, and spend management. Each new product inherits rich context, making it instantly more powerful than standalone alternatives. Toast’s menu-item architecture naturally extended to inventory, labor, and supplier management. The data model wasn’t just their first product decision. It was their platform destiny.

### Designing the right data model

The path to a differentiated data model depends on your market. The more horizontal you go, the more your moat comes from technical and interface innovation. The more vertical you go, the more your moat comes from elevating the right domain objects with the right attributes.

**Horizontal tools serve broad use cases where underlying concepts are already familiar. Leverage comes from changing how the product is built or experienced.** Notion reimagined documents as composable blocks. Figma rebuilt the foundation entirely as a multiplayer web canvas.

**[Vertical tools](https://notes.mtb.xyz/p/vertical-ai-beware-what-you-wrap) serve specific industries with deep domain complexity. Leverage comes from what you choose to emphasize.** Toast elevated menu items—not transactions—with prep times and kitchen routing as first-class data. Klaviyo promoted order data to equal status alongside email metrics.

A good place to start is by looking for model mismatches in existing successful products. Where are incumbent products forcing an incorrect or outdated model on their customers? Where are customers using workarounds—spreadsheets, low/no code tools, extensive in-product configuration—to make the product match how they think and work?

Despite all the emphasis on data models, start with the workflow, not the technical implementation. Don’t ask “what data do we need to store?” Ask “what’s the atomic unit of work in this domain?” For restaurants it’s the menu item. For design it’s the canvas. For employee operations it’s the human.

If you’ve already built a product, you can audit how powerful and correct your data model is. Open your database schema and see which table has the most foreign keys pointing to it. Is that the atomic unit your customers actually think in? List your product’s core actions. Do they all strengthen one central object, or are you building a feature buffet? What would break if you deleted your second-most important table? If the answer is “not much,” you probably have the wrong data model.

Test whether your data model creates compound advantages. When you add a new feature or product, does it automatically become more powerful because of data you’re already capturing? If your answer is “we’d need to build that feature from scratch with no inherited context,” you don’t have a compounding data model—you have a product suite. The right model creates natural expansion paths that feel obvious in retrospect but were invisible to competitors.

### Conclusion

Your data model is your destiny. The paradox is that this choice happens when you know the least about your market, but that’s also why it’s so powerful when you get it right. Competitors who’ve already built on different foundations can’t simply copy your insight. They’d have to start over, and by then, you’ve compounded your advantage.

* * *

_My name is **[Matt Brown](http://mtb.xyz/)**. I’m a partner at **[Matrix](http://matrix.vc/)**, where I invest in and help early-stage fintech and vertical software startups. Matrix is an early-stage VC that leads pre-seed to Series As from an $800M fund across AI, developer tools and infra, fintech, B2B software, healthcare, and more. If you’re building something interesting in fintech or vertical software, I’d love to chat: [mb@matrix.vc](mailto:mb@matrix.vc)_

* * *

#### Subscribe to Matt Brown's Notes

Notes on fintech, vertical software, and VC.

Subscribe

By subscribing, I agree to Substack's [Terms of Use](https://substack.com/tos), and acknowledge its [Information Collection Notice](https://substack.com/ccpa#personal-data-collected) and [Privacy Policy](https://substack.com/privacy).

3

Share

Previous

TopLatest

[Payfac in 1,000 words](https://notes.mtb.xyz/p/payfac-1000-words)

[Payfac is the model behind fintech’s biggest successes, from Stripe and Square, to Shopify, Uber, and more. It's a critical but misunderstood topic, so…](https://notes.mtb.xyz/p/payfac-1000-words)

Feb 7, 2024•
[Matt Brown](https://substack.com/@matttbrown)

[1](https://notes.mtb.xyz/p/payfac-1000-words/comments)

![](https://substackcdn.com/image/fetch/$s_!gLx3!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_center/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffcb87e80-6dcd-4e1c-b719-804f75a79a8e_3154x2104.png)

[B2B payments aren’t payments, they’re workflows](https://notes.mtb.xyz/p/b2b-payments-workflows)

[B2B payments is a ghost market because everyone focuses on the “payments” part. The real problem is in the workflows and data that precede the actual…](https://notes.mtb.xyz/p/b2b-payments-workflows)

Nov 6, 2023•
[Matt Brown](https://substack.com/@matttbrown)

![](https://substackcdn.com/image/fetch/$s_!35nZ!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_center/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6b99d729-ecfa-4a42-9843-25889ca17f39_1540x784.png)

[Stablecoins in 1,000 words](https://notes.mtb.xyz/p/stablecoins-1000-words)

[Stablecoins are an exciting and powerful upgrade to financial technology, both in their own right and complementing traditional fiat money movement…](https://notes.mtb.xyz/p/stablecoins-1000-words)

Jan 7

![](https://substackcdn.com/image/fetch/$s_!KR0w!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_center/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff70111c6-70e0-44c3-a6ce-bc2a4280af55_1932x1216.png)

See all

Ready for more?

Subscribe

#### Cookie Policy

We use cookies to improve your experience, for analytics, and for marketing. You can accept, reject, or manage your preferences. See our [privacy policy](https://substack.com/tos).

ManageRejectAccept
