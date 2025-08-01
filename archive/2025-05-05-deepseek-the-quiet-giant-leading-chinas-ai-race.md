---
title: "Deepseek: The Quiet Giant Leading China’s AI Race"
tags:
   - Open Source
   - Chinese Tech
   - Artificial Intelligence
   - Deep Learning
   - AGI
link: https://www.chinatalk.media/p/deepseek-ceo-interview-with-chinas
date: 2025-05-05
description: "Deepseek, a Chinese AI startup funded by the High-Flyer hedge fund, has emerged as a key player in the AI landscape, recently surpassing OpenAI’s models in reasoning benchmarks. Their innovative architectures, including multi-head latent attention (MLA) and sparse mixture-of-experts, have significantly reduced computational costs, triggering a price war among competitors. Focused purely on foundational tech and AGI, Deepseek aims to foster original innovation rather than mere application-focused efforts. The company's commitment to open-source principles contrasts with the trend among larger firms, positioning it as a potential disruptor amidst ongoing AI advancements."
---

[![ChinaTalk](https://substackcdn.com/image/fetch/w_80,h_80,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F9b5dde60-871d-48d4-9c21-e4f434b3f3c1_256x256.png)](https://www.chinatalk.media/)

# [ChinaTalk](https://www.chinatalk.media/)

SubscribeSign in

# Deepseek: The Quiet Giant Leading China’s AI Race

### Annotated translation of its CEO's deepest interview

[Jordan Schneider](https://substack.com/@chinatalk)

,

[Angela Shen](https://substack.com/@angelash)

,

[Irene Zhang](https://substack.com/@irenezhang)

, and 3 others

Nov 27, 2024

316

[2](https://www.chinatalk.media/p/deepseek-ceo-interview-with-chinas/comments)
65

Share

Deepseek is a Chinese AI startup whose latest R1 model **[beat OpenAI’s o1](https://api-docs.deepseek.com/news/news1120) on multiple reasoning benchmarks**. Despite its low profile, Deepseek is the Chinese AI lab to watch.

Before Deepseek, CEO Liang Wenfeng’s main venture was High-Flyer (幻方), a top 4 Chinese quantitative hedge fund last valued at $8 billion. Deepseek is fully funded by High-Flyer and has no plans to fundraise. It focuses on building foundational technology rather than commercial applications and has committed to open sourcing all of its models. It has also singlehandedly kicked off price wars in China by charging very affordable API rates. Despite this, Deepseek can afford to stay in the scaling game: with access to High-Flyer’s compute clusters, Dylan Patel’s [best guess](https://x.com/dylan522p/status/1859302712803807696) is they have upwards of “50k Hopper GPUs,” orders of magnitude more compute power than the 10k A100s they cop to publicly.

Deepseek’s strategy is grounded in their ambition to build AGI. Unlike previous spins on the theme, Deepseek’s mission statement does not mention safety, competition, or stakes for humanity, but only “unraveling the mystery of AGI with curiosity”. Accordingly, the lab has been laser-focused on research into potentially game-changing architectural and algorithmic innovations.

Deepseek has delivered a series of impressive technical breakthroughs. Before R1-Lite-Preview, there had been a longer track record of wins: [architectural improvements](https://arxiv.org/abs/2401.06066) like multi-head latent attention (MLA) and sparse mixture-of-experts (DeepseekMoE) had reduced inference costs so much as to trigger a price war among Chinese developers. Meanwhile, Deepseek’s [coding model](https://arxiv.org/abs/2406.11931) trained on these architectures outperformed open weights rivals like July’s GPT4-Turbo.

As a first step to understanding what’s in the water at Deepseek, we’ve translated a rare, in-depth interview with CEO Liang Wenfeng, originally published this past July on a 36Kr sub-brand. It contains some deep insights into:

- How DeepSeek’s ambitions for AGI flow through their research strategy

- Why it views open source as the dominant strategy and why it ignited a price war

- How he hires and organizes researchers to leverage young domestic talent far better than other labs that have splurged on returnees

- Why Chinese firms settle for copying and commercialization instead of “hardcore innovation” and how Liang hopes Deepseek will ignite more “hardcore innovation” across the Chinese economy.


# Uncovering DeepSeek: The Ultimate Tale of Chinese Tech Idealism

[Wechat](https://mp.weixin.qq.com/s/r9zZaEgqAa_lml_fOEZmjg), [Archive link](https://archive.is/JnE4j). Text \| Lily Yu 于丽丽. Editor \| Liu Jing 刘旌.

Of China’s seven large-model startups, DeepSeek has been the most discreet — yet it consistently manages to be memorable in unexpected ways.

A year ago, this unexpectedness came from its backing by High-Flyer 幻方, a quantitative hedge fund powerhouse, making it the only non-big tech giant with a reserve of 10,000 A100 chips. A year later, it became known as the catalyst for China’s AI model price war.

In May, amid continuous AI developments, DeepSeek suddenly rose to prominence. The reason was that they released an open-source model called DeepSeek V2, which offered an unprecedented price/performance ratio: inference costs were reduced to only 1 RMB per million tokens, which is about one-seventh of the cost of Llama3 70B and one-seventieth of the cost of GPT-4 Turbo.

DeepSeek was quickly dubbed the “Pinduoduo of AI,” and other major tech giants such as ByteDance, Tencent, Baidu, and Alibaba couldn’t hold back, cutting their prices one after another. A price war for large models in China was imminent.

**This diffuse smoke of war actually concealed one fact: unlike many big companies burning money on subsidies, DeepSeek is profitable.**

​​This success stems from DeepSeek’s comprehensive innovation in model architecture. They proposed a novel MLA ( **multi-head latent attention**) architecture that reduces memory usage to 5-13% of the commonly used MHA architecture. Additionally, their original DeepSeekMoESparse structure minimized computational costs, ultimately leading to reduced overall costs.

In Silicon Valley, DeepSeek is known as “the mysterious force from the East” 来自东方的神秘力量. SemiAnalysis’s chief analyst believes the DeepSeek V2 paper “may be the best one of the year.” Former OpenAI employee Andrew Carr found the paper “full of amazing wisdom” 充满惊人智慧, and applied its training setup to his own models. And Jack Clark, former policy head at OpenAI and co-founder of Anthropic, believes DeepSeek “hired a group of unfathomable geniuses” 雇佣了一批高深莫测的奇才, adding that large models made in China “will be as much of a force to be reckoned with as drones and electric cars” 将和无人机、电动汽车一样，成为不容忽视的力量.

**In the AI ​​wave — where the story is largely driven by Silicon Valley — this is a rare occurrence.** Several industry insiders told us that **this strong response stems from innovation at the architectural level, a rare attempt by domestic large model companies and even global open-source large-scale models**. One AI researcher said that the Attention architecture has hardly been successfully modified, let alone validated on a large scale, in the years since it was proposed. “It’s an idea that would be shut down at the decision-making stage because most people lack confidence” 这甚至是一个做决策时就会被掐断的念头，因为大部分人都缺乏信心.

On the other hand, large domestic models have rarely dabbled in innovation at the architectural level before, partly due to a prevailing belief that **Americans excel at 0-to-1 technical innovation, while Chinese excel at 1-to-10 application innovation**. Moreover, this kind of behavior is very unprofitable — after all, a new generation of models will inevitably emerge after a few months, so Chinese companies need only follow along and focus on downstream applications. Innovating the model architecture means that there is no path to follow, meaning multiple failures and substantial time and economic costs.

DeepSeek is clearly going against the grain. Amid the clamor that large-model technology is bound to converge and following is a smarter shortcut, DeepSeek values the learning accumulated through “detours” 弯路, and believes that Chinese large-model entrepreneurs can join the global technological innovation stream beyond just application innovation.

Many of DeepSeek’s choices differ from the norm. Until now, among the seven major Chinese large-model startups, it’s the only one that has given up the “want it all” 既要又要 approach, so far focusing on only research and technology, without the toC applications. It’s also the only one that hasn’t fully considered commercialization, firmly choosing the open-source route without even raising capital. While these choices often leave it in obscurity, DeepSeek frequently gains organic user promotion within the community.

How did DeepSeek achieve this all? We interviewed DeepSeek’s seldom-seen founder, Liang Wenfeng 梁文锋, to find out.

The post-80s founder, who has been working behind the scenes on technology since the High-Flyer era, continues his low-key style in the DeepSeek era — “reading papers, writing code, and participating in group discussions” 看论文，写代码，参与小组讨论 every day, just like every other researcher does.

And unlike many quant fund founders — who have overseas hedge-fund experience and physics or mathematics degrees — Liang Wenfeng has always maintained a local background: in his early years, he studied artificial intelligence at Zhejiang University’s Department of Electrical Engineering.

Multiple industry insiders and DeepSeek researchers told us that Liang Wenfeng is a very rare person in China’s AI industry — someone who has “both strong infra engineering and modeling capabilities, as well as the ability to mobilize resources” he “can make accurate, high-level judgments, while also remaining stronger than first-line researchers in the details”. He has a “terrifying ability to learn”, and at the same time, he is “not at all like a boss and much more like a geek.”

This is a particularly rare interview. Here, this technological idealist provides a voice that is especially scarce in China’s tech world: **he is one of the few who puts “right and wrong” before “profits and losses”** 把“是非观”置于“利害观”之前, **who reminds us to see the inertia of the times, and who puts “original innovation”** 原创式创新 **at the top of the agenda**.

A year ago, when DeepSeek first came off the market, we interviewed Liang Wenfeng: “ [Crazy High-Flyer: A Stealth AI Giant’s Road to Large Models](https://mp.weixin.qq.com/s/fpnmf5W1rr6qTIQjbf9aCg)” [疯狂的幻方：一家隐形AI巨头的大模型之路](https://archive.is/OoId6). If the phrase “be insanely ambitious and insanely sincere” 务必要疯狂地怀抱雄心，且还要疯狂地真诚 was merely a beautiful slogan back then, a year later, it has become action.

[![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4ec5a64f-4afd-4349-888f-49c1e26bb292_1866x1078.jpeg)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4ec5a64f-4afd-4349-888f-49c1e26bb292_1866x1078.jpeg)

# Part 1: How was the first shot of the price war fired?

Waves: After DeepSeek V2’s release, it quickly triggered a fierce price war in the large-model market. Some say you’ve become the industry’s catfish.

Liang Wenfeng: We didn’t mean to become a catfish — we just accidentally became a catfish. \[ _Translator’s note: This is likely a reference to Wong Kar-wai’s new tv show_ 王家卫“Blossoms Shanghai” 繁花 _, where catfish are symbolic of market disruptors due to their cannibalistic nature._\]

Waves: Was this outcome a surprise to you?

Liang Wenfeng: Very surprising. We didn’t expect pricing to be so sensitive to everyone. We were just doing things at our own pace and then accounted for and set the price. Our principle is that we don’t subsidize nor make exorbitant profits. This price point gives us just a small profit margin above costs.

Waves: Zhipu AI 智谱AI followed suit five days later, followed by ByteDance, Alibaba, Baidu, Tencent, and other big players.

Liang Wenfeng: Zhipu AI reduced the price of an entry-level product, while their models comparable to ours remained expensive. ByteDance was truly the first to follow, reducing its flagship model to match our price, which then triggered other tech giants to cut prices. Since big companies’ model costs are much higher than ours, we never expected anyone would do this at a loss, but it eventually turned into the familiar subsidy-burning logic of the internet era.

Waves: From the outside, price cuts look a lot like bids for users, which is usually the case in internet-era price wars.

Liang Wenfeng: Poaching users is not our main purpose. We cut prices because, on the one hand, our costs decreased while exploring next-generation model architectures, and on the other hand, we also feel that both APIs and AI should be accessible and affordable to everyone.

Waves: Before this, most Chinese companies would directly copy the current generation’s Llama architecture for applications. Why did you start from the model structure?

Liang Wenfeng: If the goal is to make applications, using the Llama structure for quick product deployment is reasonable. But our destination is AGI, which means we need to study new model structures to realize stronger model capability with limited resources. This is one of the fundamental research areas needed for scaling up to larger models. And beyond model structure, we’ve done extensive research in other areas, including data construction and making models more human-like — which are all reflected in the models we released. In addition, Llama’s structure, in terms of training efficiency and inference cost, is estimated to have a two-generation gap behind international frontier levels in training efficiency and inference costs.

Waves: Where does this generation gap mainly come from?

Liang Wenfeng: First of all, there’s a training efficiency gap. We estimate that compared to the best international levels, China’s best capabilities might have a twofold gap in model structure and training dynamics — meaning we have to consume twice the computing power to achieve the same results. In addition, there may also be a twofold gap in data efficiency, that is, we have to consume twice the training data and computing power to achieve the same results. Combined, that’s four times more computing power needed. What we’re trying to do is to keep closing these gaps.

Waves: Most Chinese companies choose to have both models and applications. Why has DeepSeek chosen to focus on only research and exploration?

Liang Wenfeng: Because we believe the most important thing now is to participate in the global innovation wave. For many years, Chinese companies are used to others doing technological innovation, while we focused on application monetization — but this isn’t inevitable. In this wave, our starting point is not to take advantage of the opportunity to make a quick profit, but rather to reach the technical frontier and drive the development of the entire ecosystem.

Waves: The Internet and mobile Internet eras left most people with the belief that the United States excels at technological innovation, while China excels at making applications.

Liang Wenfeng: We believe that as the economy develops, **China should gradually become a contributor instead of freeriding**. In the past 30+ years of the IT wave, we basically didn’t participate in real technological innovation. **We’re used to Moore’s Law falling out of the sky, lying at home waiting 18 months for better hardware and software to emerge. That’s how the Scaling Law is being treated**.

**But in fact, this is something that has** **been created through the tireless efforts of generations of Western-led tech communities. It’s just because we weren’t previously involved in this process that we’ve ignored its existence.**

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb41161e2-7139-4c15-84ba-0fff53b18561_452x370.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb41161e2-7139-4c15-84ba-0fff53b18561_452x370.png)

# Part 2: The Real Gap Isn’t One or Two Years. It’s Between Original Innovation and Imitation.

Waves: Why did DeepSeek V2 surprise so many people in Silicon Valley?

Liang Wenfeng: Among the numerous innovations happening daily in the United States, this is quite ordinary. They were surprised because it was a Chinese company joining their game as an innovation contributor. After all, most Chinese companies are used to following, not innovating.

Waves: But choosing to innovate in the Chinese context is a very extravagant decision. Large models are a heavy investment game, and not all companies have the capital to solely research and innovate instead of thinking about commercialization first.

Liang Wenfeng: The cost of innovation is definitely not low, and past tendencies toward indiscriminate borrowing were also related to China’s previous conditions. But now you see, whether it’s China’s economic scale, or the profits of giants like ByteDance and Tencent — none of it is low by global standards. **What we lack in innovation is definitely not capital, but a lack of confidence and knowledge of how to organize high-density talent for effective innovation.**

Waves: Why do Chinese companies — including the huge tech giants — default to rapid commercialization as their #1 priority?

Liang Wenfeng: In the past 30 years, we’ve emphasized only making money while neglecting innovation. Innovation isn’t entirely business-driven; it also requires curiosity and a desire to create. We’re just constrained by old habits, but this is tied to a particular economic phase.

Waves: But you’re ultimately a business organization, not a public-interest research institution — so where do you build your moat when you choose to innovate and then open source your innovations? Won’t the MLA architecture you released in May be quickly copied by others?

Liang Wenfeng: I **n the face of disruptive technologies, moats created by closed source are temporary. Even OpenAI’s closed source approach can’t prevent others from catching up**. S **o we anchor our value in our team — our colleagues grow through this process, accumulate know-how, and form an organization and culture capable of innovation. That’s our moat.**

Open source, publishing papers, in fact, do not cost us anything. For technical talent, having others follow your innovation gives a great sense of accomplishment. In fact, open source is more of a cultural behavior than a commercial one, and contributing to it earns us respect. There is also a cultural attraction for a company to do this.

Waves: What do you think of those who believe in the market, like \[GSR Ventures’\[ Zhu Xiaohu 朱啸虎?\
\
Liang Wenfeng: Zhu Xiaohu is logically consistent, but his style of play is more suitable for fast money-making companies. And if you look at America’s most profitable companies, they’re all high-tech companies that accumulated deep technical foundations before making major breakthroughs.\
\
Waves: But when it comes to large models, pure technical leadership rarely forms an absolute advantage. What bigger thing are you betting on?\
\
Liang Wenfeng: **What we see is that Chinese AI can’t be in the position of following forever. We often say that there is a gap of one or two years between Chinese AI and the United States, but the real gap is the difference between originality and imitation. If this doesn’t change, China will always be only a follower — so some exploration is inescapable.**\
\
Nvidia’s leadership isn’t just the effort of one company, but the result of the entire Western technical community and industry working together. They see the next generation of technology trends and have a roadmap in hand. Chinese AI development needs such an ecosystem. Many domestic chip developments struggle because they lack supporting technical communities and have only second-hand information. China inevitably needs people to stand at the technical frontier.\
\
# Part 3: More Investments Do Not Equal More Innovation\
\
Waves: DeepSeek, right now, has a kind of idealistic aura reminiscent of the early days of OpenAI, and it’s open source. Will you change to closed source later on? Both OpenAI and Mistral moved from open-source to closed-source.\
\
Liang Wenfeng: We will not change to closed source. We believe having a strong technical ecosystem first is more important.\
\
Waves: Do you have a financing plan? I’ve seen media reports saying that High-Flyer plans to spin off DeepSeek for an IPO. AI startups in Silicon Valley inevitably end up binding themselves to major firms.\
\
Liang Wenfeng: We do not have financing plans in the short term. **Money has never been the problem for us; bans on shipments of advanced chips are the problem.**\
\
Waves: Many people believe that developing AGI and quantitative finance are completely different endeavors. Quantitative finance can be pursued quietly, but AGI may require a high-profile and bold approach, forming alliances to amplify your investments.\
\
Liang Wenfeng: More investments do not equal more innovation. Otherwise, big firms would’ve monopolized all innovation already.\
\
Waves: Are you not focusing on applications right now because you lack the operational expertise?\
\
Liang Wenfeng: We believe the current stage is a period of explosive growth in technological innovation, not in applications. In the long run, we hope to create an ecosystem where the industry directly utilizes our technology and outputs. Our focus will remain on foundational models and cutting-edge innovation, while other companies can build B2B and B2C businesses based on DeepSeek’s foundation. If a complete industry value chain can be established, there’s no need for us to develop applications ourselves. Of course, if needed, nothing stops us from working on applications, but research and technological innovation will always be our top priority.\
\
Waves: But when customers are choosing APIs, why should they choose DeepSeek over offerings from bigger firms?\
\
Liang Wenfeng: The future world is likely to be one of specialized division of labor. Foundational large models require continuous innovation, and large companies have limits on their capabilities, which may not necessarily make them the best fit.\
\
Waves: But can technology itself really create a significant gap? You’ve also mentioned that there are no absolute technological secrets.\
\
Liang Wenfeng: There are no secrets in technology, but replication requires time and cost. Nvidia’s graphics cards, theoretically, have no technological secrets and are easy to replicate. However, building a team from scratch and catching up with the next generation of technology takes time, so the actual moat remains quite wide.\
\
Waves: Once DeepSeek lowered its prices, ByteDance followed suit, which shows that they feel a certain level of threat. How do you view new approaches to competition between startups and big firms?\
\
**Liang Wenfeng: Honestly, we don’t really care, because it was just something we did along the way. Providing cloud services isn’t our main goal. Our ultimate goal is still to achieve AGI.**\
\
Right now I don’t see any new approaches, but big firms do not have a clear upper hand. **Big firms have existing customers, but their cash-flow businesses are also their burden, and this makes them vulnerable to disruption at any time.**\
\
Waves: What do you see as the end game of the six other large-model startups?\
\
Liang Wenfeng: Two or three may survive. All of them are in the “burning-money” phase right now, so those with a clear self-positioning and better refinement of operations have a higher chance of making it. Other companies might undergo significant transformations. Things of value won’t simply disappear but will instead take on a different form.\
\
Waves: High-Flyer’s approach to competition has been described as “impervious,” as it pays little attention to horizontal competition. What’s your starting point when it comes to thinking about competition?\
\
Liang Wenfeng: What I often think about is whether something can improve the efficiency of society’s operations, and whether you can find a point of strength within its industrial chain. As long as the ultimate goal is to make society more efficient, it’s valid. Many things in between are just temporary phases, and overly focusing on them can lead to confusion.\
\
# Part 4: A group of young people doing “inscrutable” work\
\
Waves: Jack Clark, former policy director at OpenAI and co-founder of Anthropic, said that DeepSeek hired [“inscrutable wizards.”](https://importai.substack.com/p/import-ai-372-gibberish-jailbreak) What kind of people are behind DeepSeek V2?\
\
**Liang Wenfeng: There are no wizards. We are mostly fresh graduates from top universities, PhD candidates in their fourth or fifth year, and some young people who graduated just a few years ago.**\
\
Waves: Many LLM companies are obsessed with recruiting talents from overseas, and it’s often said that the top 50 talents in this field might not even be working for Chinese companies. Where are your team members from?\
\
**Liang Wenfeng: The team behind the V2 model doesn’t include anyone returning to China from overseas — they are all local. The top 50 experts might not be in China, but perhaps we can train such talents ourselves.**\
\
**Waves: How did this MLA innovation come about? I heard the idea originated from the personal interest of a young researcher?**\
\
**Liang Wenfeng: After summarizing some mainstream evolutionary trends of the attention mechanism, he just thought to design an alternative. However, turning the idea into reality was a lengthy process. We formed a team specifically for this and spent months getting it to work. \[** _Jordan: really reminiscent of how [Alec Radford’s early contribution to the GPT series](https://aibusiness.com/nlp/sxsw-23-openai-co-founder-shares-the-story-behind-chatgpt) and speaks to the broader thesis we’ve argued in the past on ChinaTalk that algorithmic innovation is fundamentally different from pushing the technological frontier in something like semiconductor fabrication. Instead of needing a PhD and years of industry experience to really be useful, you can push the frontier by being a really sharp and hungry 20something (of which China has many!). Dwarkesh’s interview with OpenAI [Sholto Douglass and Anthropic’s Trenton Bricken](https://www.dwarkeshpatel.com/p/sholto-douglas-trenton-bricken) illustrates this dynamic well. Dwarkesh opens with the ine “Noam Brown, who wrote the Diplomacy paper, said this about Sholto: “he's only been in the field for 1.5 years, but people in AI know that he was one of the most important people behind Gemini's success.”_ **\]**\
\
Waves: The emergence of such divergent thinking seems closely related to your innovation-driven organizational structure. Back in the High-Flyer era, your team rarely assigned goals or tasks from the top down. But AGI involves frontier exploration with much uncertainty — has that led to more management intervention?\
\
**Liang Wenfeng: DeepSeek is still entirely bottom-up. We generally don’t predefine roles; instead, the division of labor occurs naturally. Everyone has their own unique journey, and they bring ideas with them, so there’s no need to push anyone. While we explore, if someone sees a problem, they will naturally discuss it with someone else. However, if an idea shows potential, we do allocate resources top-down.**\
\
Waves: I heard that DeepSeek is very flexible in mobilizing resources like GPUs and people.\
\
**Liang Wenfeng: Anyone on the team can access GPUs or people at any time. If someone has an idea, they can access the training cluster cards anytime without approval. Similarly, since we don’t have hierarchies or separate departments, people can collaborate across teams, as long as there’s mutual interest.**\
\
Waves: Such a loose management style relies on having highly self-driven people. I heard you excel at identifying exceptional talent through non-traditional evaluation criteria.\
\
Liang Wenfeng: **Our hiring standard has always been passion and curiosity. Many of our team members have unusual experiences, and that is very interesting. Their desire to do research often comes before making money.**\
\
Waves: Transformers was born at Google’s AI Lab, and ChatGPT at OpenAI. How do you compare the value of innovations at big companies’ AI labs versus startups?\
\
Liang Wenfeng: Google’s AI Lab, OpenAI, and even Chinese tech companies’ AI labs are all immensely valuable. The fact that OpenAI succeeded was partly due to a few historical coincidences.\
\
Waves: So, is innovation largely a matter of luck? I noticed that the middle row of meeting rooms in your office has doors on both sides that anyone can open. Your colleagues said that this design leaves room for serendipity. The creation of transformers involved someone overhearing a discussion and joining, ultimately turning it into a general framework.\
\
Liang Wenfeng: I believe innovation starts with believing. **Why is Silicon Valley so innovative? Because they dare to do things. When ChatGPT came out, the tech community in China lacked confidence in frontier innovation. From investors to big tech, they all thought that the gap was too big and opted to focus on applications instead. But innovation starts with confidence, which we often see more from young people.**\
\
Waves: But you don’t fundraise or even speak to the public, so your visibility is lower than those companies actively fundraising. How do you ensure DeepSeek remains the top choice for those working on LLMs?\
\
Liang Wenfeng: Because we’re tackling the hardest problems. Top talents are most drawn to solving the world’s toughest challenges. In fact, **top talents in China are underestimated because there’s so little hardcore innovation happening at the societal level, leaving them unrecognized. We’re addressing the hardest problems, which makes us inherently attractive to them.**\
\
Waves: When OpenAI’s latest release didn’t bring us GPT5, many people feel that this indicates technological progress is slowing and are starting to question the Scaling Law. What do you think?\
\
Liang Wenfeng: We’re relatively optimistic. Our industry as a whole seems to be meeting expectations. **OpenAI is not a god (OpenAI不是神), they won’t necessarily always be at the forefront.**\
\
Waves: How long until AGI is realized? Before releasing DeepSeek V2, you had models for math and code generation and also switched from dense models to Mixture of Experts. What are the key points on your AGI roadmap?\
\
Liang Wenfeng: It could be two, five, or ten years–in any case, it will happen in our lifetimes. There’s no unified opinion on a roadmap even within our company. That said, we’ve taken real bets on three directions. First is mathematics and code, second multimodality, and third natural language itself.\
\
Mathematics and code are natural AGI testing grounds, somewhat like Go. They’re closed, verifiable systems where high levels of intelligence can be self-taught. Multimodality and engagement with the real human world, on the other hand, might also be a requirement for AGI. We remain open to different possibilities.\
\
Waves: What do you think is the end game for large models?\
\
Liang Wenfeng: There will be specialized companies providing foundation models and services, achieving extensive specialization in every node of the supply chain. More people will build on top of all of this to meet society’s diverse needs.\
\
# Part 5: All the methods are products of a previous generation\
\
Waves: Over the past year, there have been many changes in China's large model startups. For example, Wang Huiwen \[co-founder of RenRen, a facebook clone, and Meituan, a food delivery company\], who was very active at the beginning of last year, withdrew midway, and companies that joined later began to show differentiation.\
\
Liang Wenfeng: Wang Huiwen bore all the losses himself, allowing others to withdraw unscathed. He made a choice that was worst for himself but good for everyone else, so he's very decent in his conduct - this is something I really admire. \[ _Wang Huiyuan founded foundation model company 光年之外 Lightyear only to quickly fold it back into Meituan. For more on Meituan and AI, [see this recent 36Kr feature](https://36kr.com/p/3053948838351233)_\].\
\
Waves: Where are you focusing most of your energy now?\
\
Liang Wenfeng: My main energy is focused on researching the next generation of large models. There are still many unsolved problems.\
\
Waves: Other large model startups are insisting on pursuing both \[technology and commercialization\], after all, technology won't bring permanent leadership as it's also important to capitalize on a window of opportunity to translate technological advantages into products. Is DeepSeek daring to focus on model research because its model capabilities aren't sufficient yet?\
\
Liang Wenfeng: All these business patterns are products of the previous generation and may not hold true in the future. Using Internet business logic to discuss future AI profit models is like discussing General Electric and Coca-Cola when Pony Ma was starting his business. It’s a pointless exercise (刻舟求剑).\
\
Waves: In the past, your quant fund High-Flyer had a strong foundation in technology and innovation, and its growth was relatively smooth. Is this the reason for your optimism?\
\
Liang Wenfeng: In some ways, High-Flyer strengthened our confidence in technology-driven innovation, but it wasn't all smooth sailing. We went through a long accumulation process. What outsiders see is the part of High-Flyer after 2015, but in fact, we've been at it for 16 years.\
\
Waves: Returning to the topic of innovation. Now that the economy is starting to decline and capital is no longer as loose as it was, will this suppress basic research?\
\
Liang Wenfeng: I don't necessarily think so. The adjustment of China's industrial structure will necessarily rely more on hardcore technological innovation. When people realize that making quick money in the past was likely due to lucky windows, they'll be more willing to humble themselves and engage in genuine innovation.\
\
An Yong: So you're optimistic about this as well?\
\
Liang Wenfeng: I grew up in the 1980s in a fifth-tier city in Guangdong. My father was a primary school teacher. In the 1990s, there were many opportunities to make money in Guangdong. At that time, many parents came to my home; basically, they thought studying was useless. But looking back now, they’ve all changed their views. Because making money isn't easy anymore—even the opportunity to drive a taxi might be gone soon. It’s only taken one generation.\
\
In the future, hardcore innovation will become increasingly common. It’s not easy to understand right now, because society as a whole needs to be educated on this point. Once society allows people dedicated to hardcore innovation to achieve fame and fortune, then our collective mindset will adapt. We just need some examples and a process\
\
ChinaTalk is a reader-supported publication. To receive new posts and support our work, consider becoming a free or paid subscriber.\
\
Subscribe\
\
[![Phil S's avatar](https://substackcdn.com/image/fetch/w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1b52c657-a876-43ac-9a81-c5d4dffbc5c3_144x144.png)](https://substack.com/profile/96189014-phil-s)\
\
[![Ashish Rao's avatar](https://substackcdn.com/image/fetch/w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1ccfc6b1-133c-4d58-ad0e-00a9ca28486b_144x144.png)](https://substack.com/profile/12965842-ashish-rao)\
\
[![Tim Koors's avatar](https://substackcdn.com/image/fetch/w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F79513d5d-94ff-4b76-b2d1-3078bb3618c9_144x144.png)](https://substack.com/profile/22504501-tim-koors)\
\
[![William Martin Keating's avatar](https://substackcdn.com/image/fetch/w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F134138a0-6120-436e-a97d-ff18316aaad8_399x257.png)](https://substack.com/profile/79433880-william-martin-keating)\
\
[![Jordan Schneider's avatar](https://substackcdn.com/image/fetch/w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F03d46bad-4858-4a40-a833-24843e15bf6f_400x400.jpeg)](https://substack.com/profile/1145-jordan-schneider)\
\
316 Likes∙\
\
[65 Restacks](https://substack.com/note/p-152222744/restacks?utm_source=substack&utm_content=facepile-restacks)\
\
316\
\
[2](https://www.chinatalk.media/p/deepseek-ceo-interview-with-chinas/comments)\
65\
\
Share\
\
#### Discussion about this post\
\
CommentsRestacks\
\
![User's avatar](https://substackcdn.com/image/fetch/w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Favatars%2Fdefault-light.png)\
\
[![James Wang's avatar](https://substackcdn.com/image/fetch/w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd7ea988e-c6f5-4b1e-9041-8a3081bccb3f_2200x2220.jpeg)](https://substack.com/profile/7343257-james-wang?utm_source=comment)\
\
[James Wang](https://substack.com/profile/7343257-james-wang?utm_source=substack-feed-item)\
\
[Nov 27](https://www.chinatalk.media/p/deepseek-ceo-interview-with-chinas/comment/79140275 "Nov 27, 2024, 10:45 AM")\
\
Liked by Jordan Schneider\
\
This is an amazing interview! A rare glimpse behind the curtain for Chinese AI. Deepseek isn't alone though, Alibaba's Qwen is actually also quite good.\
\
I think too many people refuse to admit when they're wrong. I wasn't precisely wrong (there was nuance in the view), but I have stated, including in my interview on ChinaTalk, that I thought China would be lagging for a while. That was in October 2023, which is over a year ago (a lot of time for AI!), but I think it's worth reflecting on why I thought that and what's changed as well.\
\
\> Now, why has the Chinese AI ecosystem as a whole, not just in terms of LLMs, not been progressing as fast? This is speculation, but I’ve heard that China has much more stringent regulations on what you’re supposed to check and what the model is supposed to do. Putting that much time and energy into compliance is a big burden. A lot of Chinese tech companies and entrepreneurs don’t seem the most motivated to create huge, impressive, globally dominant models.\
\
I never thought that Chinese entrepreneurs/engineers didn't have the capability of catching up. LLMs weren't "hitting a wall" at the time or (less hysterically) leveling off, but catching up to what was known possible wasn't an endeavor that's as hard as doing it the first time.\
\
There's a lot more regulatory clarity, but it's actually fascinating that the culture has also shifted since then. I don't think you would have Liang Wenfeng's type of quotes that the goal is AGI, and they are hiring people who are interested in doing hard things above the money—that was much more part of the culture of Silicon Valley, where the money is kind of expected to come from doing hard things, so it doesn't have to be stated either.\
\
That all being said, LLMs are still struggling to monetize (relative to their cost of both training and running). We'll see if OpenAI justifies its $157B valuation and how many takers they have for their $2k/month subscriptions. This is not really the sector that I would personally bet on creating a huge amount of global leadership in AI in-and-of-itself...\
\
Except for helping train individuals and create an ecosystem where there's a lot of AI talent that can go elsewhere to create the AI applications that will actually generate value. Or be highly valuable in, say, military applications.\
\
Anyway, again, this is an amazing interview and really suggests a big shift in the AI talent ecosystem.\
\
Expand full comment\
\
Like (11)\
\
Reply\
\
Share\
\
[![jeff fultz's avatar](https://substackcdn.com/image/fetch/w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Favatars%2Fyellow.png)](https://substack.com/profile/3308576-jeff-fultz?utm_source=comment)\
\
[jeff fultz](https://substack.com/profile/3308576-jeff-fultz?utm_source=substack-feed-item)\
\
[Nov 28](https://www.chinatalk.media/p/deepseek-ceo-interview-with-chinas/comment/79243059 "Nov 28, 2024, 6:21 AM")\
\
I just wonder on the ways High Flyer makes it money to fund this?\
\
This type set up needs to be done here in the USA too. Maybe have a Sovereign Wealth Fund set up to fund this type innovation? And many other future technologies too.\
\
Expand full comment\
\
Like (5)\
\
Reply\
\
Share\
\
TopLatestDiscussions\
\
[DeepSeek: The View from China](https://www.chinatalk.media/p/deepseek-the-view-from-china)\
\
[China's takes are better than yours](https://www.chinatalk.media/p/deepseek-the-view-from-china)\
\
Jan 28•\
[Jordan Schneider](https://substack.com/@chinatalk)\
,\
[Irene Zhang](https://substack.com/@irenezhang)\
,\
[Angela Shen](https://substack.com/@angelash)\
, and\
[Yiwen](https://substack.com/@uncoolkids)\
\
144\
\
[5](https://www.chinatalk.media/p/deepseek-the-view-from-china/comments)\
\
![](https://substackcdn.com/image/fetch/w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_center/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1dbe6258-c75b-4792-8c7f-ed719685a249_1219x702.png)\
\
[DeepSeek: What the Headlines Miss](https://www.chinatalk.media/p/deepseek-what-the-headlines-miss)\
\
[Posting will continue until the takes improve](https://www.chinatalk.media/p/deepseek-what-the-headlines-miss)\
\
Jan 25•\
[Jordan Schneider](https://substack.com/@chinatalk)\
\
278\
\
[16](https://www.chinatalk.media/p/deepseek-what-the-headlines-miss/comments)\
\
![](https://substackcdn.com/image/fetch/w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_center/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7c26fd59-f6b7-49fc-93d0-4dfd45ed5a7d_975x437.png)\
\
[Rickover’s Lessons](https://www.chinatalk.media/p/rickovers-lessons-how-to-build-a)\
\
["The status quo has no absolute sanctity"](https://www.chinatalk.media/p/rickovers-lessons-how-to-build-a)\
\
Mar 20•\
[Lily Ottinger](https://substack.com/@voidpoliticstaiwan)\
and\
[Charles Yang](https://substack.com/@charlesyang)\
\
75\
\
[16](https://www.chinatalk.media/p/rickovers-lessons-how-to-build-a/comments)\
\
![](https://substackcdn.com/image/fetch/w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_center/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3f3bbc65-a335-4044-9d7b-0306dd601f4f_1062x786.jpeg)\
\
See all\
\
Ready for more?\
\
Subscribe
