---
date: '2025-08-13'
description: 'At Black Hat and DEF CON, AI''s dual role in cybersecurity was emphasized:
  as both a vulnerable target and a defender against attacks. Key insights include:
  1. **Zero-click Attacks**: Researchers demonstrated how hacked ChatGPT connectors
  can extract sensitive data without user interaction, highlighting risks in API integrations.
  2. **AI Cyber Challenge**: DARPA''s initiative showcased autonomous systems that
  can identify vulnerabilities in critical infrastructure, marking progress in AI-driven
  security. 3. **AI Competitiveness**: Anthropic''s Claude AI participated in cybersecurity
  competitions, revealing AI''s potential yet persistent limitations in complex problem-solving.
  These developments underscore both the promise and peril of AI in security contexts.'
link: https://fortune.com/2025/08/12/hacker-bodyguard-target-ais-triple-act-at-the-years-biggest-security-showdowns/
tags:
- Tech Conferences
- AI
- Cybersecurity
- Innovation
- Hacking
title: At Black Hat and DEF CON, AI was hacker, bodyguard, and target all at once
  ◆ Fortune
---

- [Home](https://fortune.com/)

- [News](https://fortune.com/the-latest/)

- [Rankings](https://fortune.com/ranking/)


  - [Analytics](https://fortune.com/analytics)
  - [Fortune 500](https://fortune.com/ranking/fortune500/)
  - [Fortune Global 500](https://fortune.com/ranking/global500/)
  - [Fortune 500 Europe](https://fortune.com/europe/ranking/fortune500-europe/)
  - [Fortune China 500](https://www.fortunechina.com/fortune500/c/2023-07/25/content_436290.htm)
  - [FORTUNE SEA 500](https://fortune.com/asia/ranking/southeast-asia-500/)
- [Tech](https://fortune.com/section/tech/)


  - [AI](https://fortune.com/section/artificial-intelligence/)
  - [Innovation](https://fortune.com/section/innovation/)
  - [Cybersecurity](https://fortune.com/section/cybersecurity/)
- [Finance](https://fortune.com/section/finance/)


  - [Personal Finance](https://fortune.com/section/personal-finance/)
  - [Real Estate](https://fortune.com/section/real-estate/)
  - [Economy](https://fortune.com/section/economy/)
  - [Investing](https://fortune.com/section/investing/)
  - [Banking](https://fortune.com/section/banking-finance/)
  - [Crypto](https://fortune.com/crypto/)
- [Leadership](https://fortune.com/section/leadership/)


  - [Success](https://fortune.com/section/success/)
  - [Future of Work](https://fortune.com/section/future-of-work/)
  - [Workplace Culture](https://fortune.com/section/workplace-culture/)
  - [C-Suite](https://fortune.com/section/c-suite/)
  - [CEO Initiative](https://fortune.com/ceoi)
- [Lifestyle](https://fortune.com/section/lifestyle/)


  - [Arts & Entertainment](https://fortune.com/section/arts-and-entertainment/)
  - [Travel & Leisure](https://fortune.com/section/travel-and-leisure/)
  - [Well](https://fortune.com/well/)
  - [Education](https://fortune.com/education/)
- [Multimedia](https://fortune.com/2025/08/12/hacker-bodyguard-target-ais-triple-act-at-the-years-biggest-security-showdowns/#)


  - [Live Media](https://fortune.com/conferences)
  - [Magazine](https://fortune.com/magazine/)
  - [Newsletters](https://fortune.com/newsletters/)
  - [Video](https://fortune.com/videos/)
  - [Podcasts](https://fortune.com/podcasts/)

[Homepage](https://fortune.com/)

[Newsletters](https://fortune.com/section/newsletters/)· [Eye on AI](https://fortune.com/tag/eye-on-a-i/)

# Hacker, bodyguard, target: AI’s triple act at the year’s biggest security showdowns

By [Sharon Goldman](https://fortune.com/author/sharon-goldman/)

![Sharon Goldman](https://fortune.com/img-assets/wp-content/uploads/2024/03/Untitled-design-2024-04-02T114832.907-1.png?w=1440&q=75)By [Sharon Goldman](https://fortune.com/author/sharon-goldman/)AI Reporter

[![](https://fortune.com/img-assets/wp-content/uploads/2024/03/Untitled-design-2024-04-02T114832.907-1.png?w=1440&q=75)](https://fortune.com/author/sharon-goldman/)

[Sharon Goldman](https://fortune.com/author/sharon-goldman/) AI Reporter

- [Go to our linkedin profile](https://www.linkedin.com/in/sharongoldman/)

Sharon Goldman is an AI reporter at _Fortune_ and co-authors [Eye on AI](https://www.fortune.com/newsletters/eye-on-ai?&itm_source=fortune&itm_medium=author_bio_footer&itm_campaign=eye_on_ai&itm_content=sharon_goldman), _Fortune_’s flagship AI newsletter. She has written about digital and enterprise tech for over a decade.

[SEE FULL BIO](https://fortune.com/author/sharon-goldman/)

August 12, 2025 at 1:19 PM EDT

![Five people stand on a stage. The middle three people hold a large check worth four million dollars.](https://fortune.com/img-assets/wp-content/uploads/2025/08/image001.jpg?w=1440&q=90)

U.S. Department of Health and Human Services Deputy Secretary Jim O’Neill and DARPA Director Stephen Winchell congratulate AIxCC team Atlanta.

DARPA \| Matt Dombro

Trinity Player

Listen now

Listen to the article now

English
Deutsch
Français

Español
中文
Italiano

10

10

1.0x

0.50.60.70.80.91.01.11.21.31.41.51.61.71.81.92.0

1.0x

**Powered by:** [Trinity Audio](https://trinityaudio.ai/?utm_source=https%3A%2F%2Ffortune.com&utm_medium=player%2520lin)

00:00

09:33

_Welcome to Eye on AI! AI reporter Sharon Goldman here, filling in for Jeremy Kahn, who is on holiday. In this edition… China tells firms to avoid Nvidia H20 Chips after Trump ends ban but takes cut of revenue… Students are flocking to college courses in AI… Anthropic will offer Claude AI to the U.S. government for $1._

Las Vegas in August feels like another planet—blazing heat, flashing lights, and the constant clatter of slot machines. That otherworldly vibe carried over to the two conferences I attended last week: Black Hat and DEF CON, two of the year’s biggest security and “ethical” hacking conferences, where cutting-edge security research is presented; hackers race to expose flaws in everything from AI chatbots to power grids; and governments, corporations, and hobbyists swap notes and learn the latest threat-fighting techniques.

I was there because AI now occupies a strange place in the security world—it is both a vulnerable target, often under threat from malicious AI; an armed defender using that same technology to protect systems and networks from bad actors; and an offensive player, deployed to probe weaknesses or carry out attacks (illegally in criminal hands). Sound confusing? It is—and that contradiction was on full display at the very corporate Black Hat, as well as DEF CON, often referred to as “hacker summer camp.”

Here are three of my favorite takeaways from the conferences:

- **ChatGPT agents can be hacked**. At Black Hat, researchers from security firm Zenity showed how hackers could exploit OpenAI’s new Connectors feature, which lets ChatGPT pull in data from apps like Google Drive, SharePoint, and GitHub. Their proof-of-concept attack, called _AgentFlayer_, used an innocent-looking “poisoned” document with hidden instructions to quietly make ChatGPT search the victim’s files for sensitive information and send it back to the attacker. The kicker: It required no clicks or downloads from the user—this [video](https://www.youtube.com/watch?v=JNHpZUpeOCg&feature=youtu.be) shows how it was done. OpenAI fixed the flaw after being alerted, but the episode underscores a growing risk as AI systems link to more outside apps: sneaky “prompt injection” attacks, known as zero-click attacks (like the [one I reported on](https://fortune.com/2025/06/11/microsoft-copilot-vulnerability-ai-agents-echoleak-hacking/) in June) that trick chatbots into doing the hacker’s bidding without the user realizing it.

- **AI can protect our most critical infrastructure.** That idea was the driving force behind the two-year AI Cyber Challenge (AIxCC), which tasked teams of developers with building generative AI tools to find and fix software vulnerabilities in the code that powers everything from banks and hospitals to public utilities. The competition—run by DARPA in partnership with ARPA-H—wrapped up at this year’s DEF CON, where winners showed off autonomous AI systems capable of securing the open-source software that underpins much of the world’s critical infrastructure. The top three teams will receive $4 million, $3 million, and $1.5 million, respectively, for their performance in the finals.

- **Anthropic’s Claude AI proved it can sometimes match elite hackers but still struggles on hard problems.** Keane Lucas, a member of Anthropic’s Frontier Red Team, presented the fascinating case study of how the company quietly entered its Claude AI into seven major cybersecurity competitions—events typically dominated by human hackers and security pros—to see how it stacked up. Claude often landed in the top quarter of competitors and showed standout speed on simple challenges, sometimes matching elite human teams, but it lagged badly on the hardest problems. There were also quirks unique to AI—such as getting derailed by ASCII art or lapsing into philosophical rambling during long tasks. Anthropic says these experiments highlight both the offensive potential of AI (by lowering the skill and cost barriers to launching attacks) and its defensive promise, while underscoring persistent limits like long-term memory and complex reasoning.

**Also: In just a few weeks, I will be headed to Park City, Utah, to participate in our annual Brainstorm Tech conference at the Montage Deer Valley!** Space is limited, so if you’re interested in joining me, [register here](https://conferences.fortune.com/event/brainstorm-tech-2025/home). I highly recommend: There’s a fantastic lineup of speakers, including Ashley Kramer, chief revenue officer of OpenAI; John Furner, president and CEO of Walmart U.S.; Tony Xu, founder and CEO of DoorDash; and many, many more!

With that, here’s more AI news.

**Sharon Goldman**

[sharon.goldman@fortune.com](mailto:sharon.goldman@fortune.com)

[@sharongoldman](https://x.com/sharongoldman)

### AI IN THE NEWS

**China tells firms to avoid Nvidia H20 Chips after Trump ends ban but takes cut of revenue.** According to [Bloomberg](https://www.bloomberg.com/news/articles/2025-08-12/china-urges-firms-not-to-use-nvidia-h20-chips-in-new-guidance), Beijing has quietly advised Chinese companies, especially those involved in government or national security projects, to steer clear of Nvidia’s H20 processors, undermining the U.S. chipmaker’s efforts to regain billions in lost China sales after the Trump administration lifted an effective ban on such exports. The guidance, delivered in recent weeks to a range of firms, stops short of an outright prohibition but signals strong official disapproval for H20 use in sensitive contexts. The news comes after President Trump announced the U.S. government will take 15% of the revenue that chipmaker Nvidia pulls in from sales in China of its H20 chips.

**Students are flocking to college courses in AI.** As AI transforms workplaces, growing numbers of professionals and students are pursuing advanced degrees, certificates, and training in artificial intelligence to boost skills and job prospects. The _Washington Post_[reported](https://www.washingtonpost.com/business/2025/08/11/ai-degree-education/) that universities like the University of Texas at Austin, University of Michigan at Dearborn, University of San Diego, and MIT are seeing surging enrollment in AI programs, fueled by ChatGPT’s rise and employer demand for AI literacy. Courses range from technical training in algorithms and model-building to broader instruction in creativity, ethics, and problem-solving. Corporate partnerships, such as Meta inviting university instructors to train engineers, reflect industry urgency, while new initiatives at schools like Ohio State aim to make AI literacy universal by 2029. Workers see AI skills as a competitive edge—PwC reports wages for AI-skilled employees are 56% higher—and experts stress curiosity and adaptability over credentials alone.

**Anthropic will offer Claude AI to U.S. government for $1.** Reuters [reported](https://www.reuters.com/business/retail-consumer/anthropic-offers-ai-chatbot-claude-us-government-1-2025-08-12/) that Anthropic will offer its Claude AI model to the U.S. government for $1. The announcement comes days after OpenAI [also offered ChatGPT](https://www.cnbc.com/2025/08/06/openai-is-giving-chatgpt-to-the-government-for-1-.html) to the U.S. government for $1, while Google's Gemini was also added to the government's list of approved AI vendors. “America's AI leadership requires that our government institutions have access to the most capable, secure AI tools available," CEO Dario Amodei said.

### EYE ON AI RESEARCH

**AI training to have whopping power needs, report says**

According to Axios, a [new report](https://www.axios.com/2025/08/12/ai-training-power-needs) from the Electric Power Research Institute and Epoch AI reveals the staggering energy requirements for training large “frontier” AI models: By 2028, individual training projects could demand 1–2 gigawatts (GW) of power, and by 2030 that range may extend to 4–16 GW—with the high end representing nearly 1% of total U.S. electricity capacity. Overall, U.S. AI‑related power needs (covering both training and inference) are projected to surge from 5 GW today to 50 GW by 2030 according to the report, giving policymakers and hyperscale tech firms essential insights to help plan infrastructure and energy strategies despite considerable uncertainty.

### FORTUNE ON AI

[Exclusive: Profound raises $35M as Sequoia backs its ambitious bid to become the Salesforce of AI search](https://fortune.com/2025/08/12/ai-search-startup-profound-raises-35-million-series-b-sequoia/) —by Sharon Goldman

[How deals with Apple and Trump’s Pentagon turned rare earth miner MP Materials into a red-hot stock](https://fortune.com/2025/08/12/rare-earths-magnets-mp-materials-stock-surge-landmark-deals-trump-apple/) —by Jordan Blum

[OpenAI’s open-source pivot shows how U.S. tech is trying to catch up to China’s AI boom](https://fortune.com/asia/2025/08/10/openai-open-source-china-deepseek/) —by Nicholas Gordon

[AI’s endless thirst for power is driving a natural gas boom in Appalachia—and industry stocks are booming along with it](https://fortune.com/2025/08/09/overlooked-gas-investor-darling-thanks-ai-appalachian-producers/) —by Jordan Blum

### AI CALENDAR

**Sept. 8-10**: Fortune Brainstorm Tech, Park City, Utah. Apply to attend [here](https://conferences.fortune.com/event/brainstorm-tech-2025/home).

**Oct. 6-10:** World AI Week, Amsterdam

**Oct. 21-22:** TedAI San Francisco. Apply to attend [here](https://tedai-sanfrancisco.ted.com/#how-to-attend).

**Dec. 2-7:** NeurIPS, San Diego

**Dec. 8-9:** Fortune Brainstorm AI San Francisco. Apply to attend [here](https://conferences.fortune.com/event/brainstorm-ai-2025/HOME).

### BRAIN FOOD

**An apple for the teacher? These days, it’s AI.** A new article in _[The Atlantic](https://www.theatlantic.com/technology/archive/2025/08/ai-takeover-education-chatgpt/683840/)_ focuses on the other side of AI use in schools: Chatbots like ChatGPT may be popular with high school students, but teachers, too, are embracing AI to save time on grading, lesson planning, and paperwork, with platforms like MagicSchool AI now used by millions of U.S. educators. School districts are split—some banning AI, others integrating tools like Google’s Gemini into classrooms—but examples from Houston show the risks of poor-quality, AI-generated materials. Federal policy is pushing for widespread AI adoption, with major funding and partnerships from Microsoft, OpenAI, and Anthropic. Yet consensus is lacking on how to balance AI’s efficiencies with maintaining students’ critical thinking skills, leaving schools at a crossroads where increased reliance on AI now could entrench it deeply in future education.

This is the online version of Eye on AI, Fortune's weekly newsletter on how AI is shaping the future of business. [Sign up for free](https://www.fortune.com/newsletters/eye-on-ai?&itm_source=fortune&itm_medium=nl_article_tout&itm_campaign=eye_on_ai).

#### About the Author

[![](https://fortune.com/img-assets/wp-content/uploads/2024/03/Untitled-design-2024-04-02T114832.907-1.png?w=1440&q=75)](https://fortune.com/author/sharon-goldman/)

[Sharon Goldman](https://fortune.com/author/sharon-goldman/) AI Reporter

- [Go to our linkedin profile](https://www.linkedin.com/in/sharongoldman/)

Sharon Goldman is an AI reporter at _Fortune_ and co-authors [Eye on AI](https://www.fortune.com/newsletters/eye-on-ai?&itm_source=fortune&itm_medium=author_bio_footer&itm_campaign=eye_on_ai&itm_content=sharon_goldman), _Fortune_’s flagship AI newsletter. She has written about digital and enterprise tech for over a decade.

[SEE FULL BIO](https://fortune.com/author/sharon-goldman/)

## Latest in Newsletters

- 2 hours ago


![Justin Skelton is chief information officer for restaurant operator Dine Brands.](<Base64-Image-Removed>)

[Newsletters](https://fortune.com/section/newsletters/) \- [CIO Intelligence](https://fortune.com/tag/cio-intelligence/)



## [Applebee’s and IHOP’s CIO places AI bets that can boost traffic and improve the dining experience](https://fortune.com/2025/08/13/applebees-and-ihops-cio-places-ai-bets-that-can-boost-traffic-and-improve-the-dining-experience/)





By [John Kell](https://fortune.com/author/john-kell/)

August 13, 2025

- 4 hours ago


![CVS CEO Karen Lynch talks with Fortune editor in chief Alyson Shontell at Fortune's 2023 MPW Summit in California on Oct. 9, 2023.](<Base64-Image-Removed>)

[Newsletters](https://fortune.com/section/newsletters/) \- [MPW Daily](https://fortune.com/tag/mpw-daily/)



## [The 2025 Fortune MPW Summit will feature a record number of the most powerful women in business](https://fortune.com/2025/08/13/fortune-most-powerful-women-summit-2025-speaker-lineup-selena-gomez-ceos/)





By [Emma Hinchliffe](https://fortune.com/author/emma-hinchliffe/)

August 13, 2025

- 7 hours ago


![Cava is investing up to $10 million in a food technology startup.](<Base64-Image-Removed>)

[Newsletters](https://fortune.com/section/newsletters/) \- [CFO Daily](https://fortune.com/tag/cfo-daily/)



## [Cava CFO: Automation to ‘enhance the human experience, not replace it’](https://fortune.com/2025/08/13/cava-cfo-automation-enhance-human-experience-not-replace-it/)





By [Sheryl Estrada](https://fortune.com/author/sheryl-estrada/)

August 13, 2025

- 8 hours ago


![Rebecca Lynn, managing director at Canvas Prime.](<Base64-Image-Removed>)

[Newsletters](https://fortune.com/section/newsletters/) \- [Term Sheet](https://fortune.com/tag/term-sheet/)



## [Rebecca Lynn spins out of Canvas Ventures to found Canvas Prime as solo GP](https://fortune.com/2025/08/13/rebecca-lynn-spins-out-of-canvas-ventures-to-found-canvas-prime-as-solo-gp/)





By [Allie Garfinkle](https://fortune.com/author/alexandra-garfinkle/)

August 13, 2025

- 8 hours ago


![Elon Musk at the White House on May 21, 2025 in Washington, D.C. (Photo: Chip Somodevilla/Getty Images)](<Base64-Image-Removed>)

[Newsletters](https://fortune.com/section/newsletters/) \- [Fortune Tech](https://fortune.com/tag/fortune-tech/)



## [Apple has a new AI problem: Elon Musk](https://fortune.com/2025/08/13/apple-has-a-new-ai-problem-elon-musk/)





By [Andrew Nusca](https://fortune.com/author/andrew-nusca/)

August 13, 2025

- 9 hours ago


![Trump pointing his finger](<Base64-Image-Removed>)

[Newsletters](https://fortune.com/section/newsletters/) \- [CEO Daily](https://fortune.com/tag/ceo-daily/)



## [How CEOs deal with Trump: Praise, face time, remorse, and gifts made of gold all go a long way, experience shows](https://fortune.com/2025/08/13/how-ceos-deal-with-trump-praise-face-time-remorse-and-gifts-made-of-gold-all-go-a-long-way-experience-shows/)





By [Diane Brady](https://fortune.com/author/diane-brady/)

August 13, 2025


## Most Popular

- 2 days ago


![](<Base64-Image-Removed>)

[Success](https://fortune.com/section/success)



## [OpenAI's CEO Sam Altman says in 10 years' time college graduates will be working 'some completely new, exciting, super well-paid' job in space](https://fortune.com/2025/08/11/openai-ceo-sam-altman-10-years-gen-alpha-college-graduates-working-in-solar-system-well-paid-jobs-as-gen-z-struggles-todays-job-market/?itm_source=parsely-api)





By [Preston Fore](https://fortune.com/author/preston-fore)

August 11, 2025

- 1 day ago


![](<Base64-Image-Removed>)

[Economy](https://fortune.com/section/economy)



## [Trump is bringing in enough revenue from tariffs to have a serious impact on the $37 trillion national debt, budget watchdog says](https://fortune.com/2025/08/12/trump-tariffs-revenue-crfb/?itm_source=parsely-api)





By [Nick Lichtenberg](https://fortune.com/author/nick-lichtenberg)

August 12, 2025

- 1 day ago


![](<Base64-Image-Removed>)

[Economy](https://fortune.com/section/economy)



## [Jerome Powell’s job just got a whole lot easier as inflation data sidesteps disaster](https://fortune.com/2025/08/12/jerome-powell-fed-rate-cut-july-cpi-inflation-unemployment/?itm_source=parsely-api)





By [Eleanor Pringle](https://fortune.com/author/eleanor-pringle)

August 12, 2025

- 1 day ago


![](<Base64-Image-Removed>)

[Success](https://fortune.com/section/success)



## [China’s youth unemployment is so bad that Gen Z job-seekers are paying $7 a day to pretend to work in an office](https://fortune.com/2025/08/12/china-gen-z-unemployment-fake-work-offices-careers-jobs-lying-flat-rat-people/?itm_source=parsely-api)





By [Emma Burleigh](https://fortune.com/author/emma-burleigh)

August 12, 2025

- 1 day ago


![](<Base64-Image-Removed>)

[Success](https://fortune.com/section/success)



## [Self-made multimillionaire behind $4 billion Skims empire says she was ‘using AI like a 42-year-old woman’—until Mark Cuban gave her a wake-up call](https://fortune.com/2025/08/12/self-made-multimillionaire-behind-4-billion-skims-empire-says-she-was-using-ai-like-a-42-year-old-woman-until-mark-cuban-gave-her-a-wake-up-call/?itm_source=parsely-api)





By [Orianna Rosa Royle](https://fortune.com/author/orianna-royle)

August 12, 2025

- 1 day ago


![](<Base64-Image-Removed>)

[Tech](https://fortune.com/section/tech)



## [Elon Musk's Tesla diner has already slashed its menu and restricted hours less than three weeks after its grand opening](https://fortune.com/2025/08/12/elon-musk-tesla-diner-menu-hours-changes/?itm_source=parsely-api)





By [Chris Morris](https://fortune.com/author/chris-morris)

August 12, 2025


## Related Articles

- ![](https://fortune.com/img-assets/wp-content/uploads/2025/08/GettyImages-2219351721-e1754414326217.jpg?w=1024)

[Newsletters](https://fortune.com/section/Newsletters/?queryly=related_article)



## [From OpenAI to Nvidia, researchers agree: AI agents have a long way to go](https://fortune.com/2025/08/05/from-openai-to-nvidia-researchers-agree-ai-agents-have-a-long-way-to-go/?queryly=related_article)





BY[Sharon Goldman](https://fortune.com/author/Sharon-Goldman/?queryly=related_article)



August 5, 2025

- ![](https://fortune.com/img-assets/wp-content/uploads/2025/07/GettyImages-2197573325.jpg?w=1024)

[Newsletters](https://fortune.com/section/Newsletters/?queryly=related_article)



## [What Eric Xing’s Abu Dhabi project says about the next phase of AI power](https://fortune.com/2025/07/22/eric-xings-uae-abu-dhabi-project-ai-power/?queryly=related_article)





BY[Sharon Goldman](https://fortune.com/author/Sharon-Goldman/?queryly=related_article)



July 22, 2025

- ![](https://fortune.com/img-assets/wp-content/uploads/2025/02/GettyImages-462522564-e1739908873303.jpg?w=1024)

[Newsletters](https://fortune.com/section/Newsletters/?queryly=related_article)



## [AI security risks are in the spotlight—but hackers say models are still alarmingly easy to attack](https://fortune.com/2025/02/18/ai-security-risks-are-in-the-spotlight-but-hackers-say-models-are-still-alarmingly-easy-to-attack/?queryly=related_article)





BY[Sharon Goldman](https://fortune.com/author/Sharon-Goldman/?queryly=related_article)



February 18, 2025

- ![](https://fortune.com/img-assets/wp-content/uploads/2025/05/GettyImages-2194795244-e1748367559666.jpg?w=1024)

[Newsletters](https://fortune.com/section/Newsletters/?queryly=related_article)



## [When an AI model misbehaves, the public deserves to know—and to understand what it means](https://fortune.com/2025/05/27/anthropic-ai-model-blackmail-transparency/?queryly=related_article)





BY[Sharon Goldman](https://fortune.com/author/Sharon-Goldman/?queryly=related_article)



May 27, 2025

- ![](https://fortune.com/img-assets/wp-content/uploads/2025/02/GettyImages-2197366846-e1738691547337.jpg?w=1024)

[Newsletters](https://fortune.com/section/Newsletters/?queryly=related_article)



## [DeepSeek has tilted the balance towards open source AI, but big security issues remain](https://fortune.com/2025/02/04/sam-altman-openai-wrong-side-of-history-open-source-deepseek/?queryly=related_article)





BY[Jeremy Kahn](https://fortune.com/author/Jeremy-Kahn/?queryly=related_article)



February 4, 2025

- ![](https://fortune.com/img-assets/wp-content/uploads/2025/07/GettyImages-1249937763-e1752768380583.jpg?w=1024)

[Newsletters](https://fortune.com/section/Newsletters/?queryly=related_article)



## [I’ve spent the week at one of the world’s top AI research conferences. Here’s what is sticking with me](https://fortune.com/2025/07/17/icml-big-tech-meta-ai-research-conference-vancouver/?queryly=related_article)





BY[Sharon Goldman](https://fortune.com/author/Sharon-Goldman/?queryly=related_article)



July 17, 2025


[search by queryly](https://www.queryly.com/)Advanced Search![close](https://www.queryly.com/images/whitecloseicon.png)
