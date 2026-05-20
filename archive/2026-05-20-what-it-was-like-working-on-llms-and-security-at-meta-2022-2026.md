---
date: '2026-05-20'
description: Joshua Saxe reflects on his experience at Meta, emphasizing the challenges
  and dynamics of working on large language models (LLMs) within a unique corporate
  culture. He critiques a meritocratic environment that pressures employees towards
  individual ambition over collective purpose, leading to a lack of coherent product
  vision. Saxe notes the powerful role of data science in performance metrics, resulting
  in a culture of metric manipulation. He highlights the innovation potential in AI
  security collaborations, while also exposing the emotional toll of job insecurity
  and performance anxiety. This candid assessment offers insights into modern tech
  workplace dynamics, particularly in AI-focused environments.
link: https://joshuasaxe181906.substack.com/p/what-it-was-like-working-on-llms
tags:
- Workplace Culture
- Meta
- AI Security
- Machine Learning
- Cybersecurity
title: What it was like working on LLMs and security at Meta (2022-2026)
---

# [Joshua Saxe](https://joshuasaxe181906.substack.com/)

SubscribeSign in

![User's avatar](https://substackcdn.com/image/fetch/$s_!HJ5b!,w_64,h_64,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F8bbf753c-129e-42b9-a54a-8e593c37a02f_144x144.png)

Discover more from Joshua Saxe

Machine learning, cyber security, social science, philosophy, classical/jazz piano. Currently at Meta working at the intersection of Llama and cybersecurity

Subscribe

By subscribing, you agree Substack's [Terms of Use](https://substack.com/tos), and acknowledge its [Information Collection Notice](https://substack.com/ccpa#personal-data-collected) and [Privacy Policy](https://substack.com/privacy).

Already have an account? Sign in

# What it was like working on LLMs and security at Meta (2022-2026)

[![Joshua Saxe's avatar](https://substackcdn.com/image/fetch/$s_!HJ5b!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F8bbf753c-129e-42b9-a54a-8e593c37a02f_144x144.png)](https://substack.com/@joshuasaxe181906)

[Joshua Saxe](https://substack.com/@joshuasaxe181906)

May 20, 2026

20

3

Share

[![](https://substackcdn.com/image/fetch/$s_!eJCW!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F749672cf-fd91-4e56-bda6-6cab9f17ca24_1334x880.png)](https://substackcdn.com/image/fetch/$s_!eJCW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F749672cf-fd91-4e56-bda6-6cab9f17ca24_1334x880.png)

I loved my time at Meta, and I also counted the days between equity vests and daydreamed about quitting on the morning after almost every one. It was the most exciting engineering culture I’ve ever been part of, and at its worst it could feel like a perverse psychology experiment. I was proud to work on Llama, CodeLlama, the foundations of LLM security and LLMs for security, on AI content moderation tech for 3.5 billion people, on the open source AI security products my teams shipped; I was also embarrassed by the internal incentives that motivated us to get people wasting more and more minutes of their wild and precious lives scrolling Instagram Reels.

Today Meta laid off ten percent of its employees. I left on my own volition in February. Many of the people I looked up to have already gone to Anthropic, OpenAI, and Microsoft. With a couple of months of distance from working there, after layoffs, departures, and the strange feeling of watching a place I loved take one more step down the staircase of its cultural ruin, it feels like the right moment to write something in the hopes it’ll be helpful to myself and others.

## A beehive of individual ambition

Imagine someone who freaked out the one time they got an A-minus, who has passed a series of meritocratic gates and received the appropriate accolades and awards, and for whom getting into Meta was like getting into their second choice elite college, and is now at Meta, and expects a series of good accolades and rewards to continue to be meted out by the new institution they’ve joined.

This felt like the median engineer and product manager at Meta; the company recruited for and filtered for such people, placing them inside a Skinnerian conditioning experiment in which bad performance gets you managed out and good performance is rewarded with money that can change the shape of your life, or at least buy you a house and a financial cushion in San Jose or Fremont; everyone at Meta is running from desperately from the former and manically chasing the latter.

The upside of this is that you could assume far more competence from basically everyone you interacted with at Meta than at other places I’ve worked, and a kind of background urgency and low-key fight or flight trauma energy animating whatever they were doing, including when they were collaborating with you.

I joined in summer 2022 at the tail end of the pandemic hiring boom, when I suspect they’d lowered the hiring bar, and of the ten or so friends I referred during my time there - once the company had begun the process of layoffs and attrition and raised the bar again - none made it through.

I always felt like an odd duck; I’m self taught, have a graduate degree in the humanities, live and work remotely from Kansas, and somehow clawed my way up. But I learned that that’s comparing my insides to others’ outsides; I think all of us felt lucky to be there but that our status there was contingent and unstable.

## Flatness

Meta’s employee net worth ranges from billions to nothing and is wildly unequal, but also no one said “I manage a team” at Meta, everyone said “I support a team,” and in most companies engineering managers manage engineers, but at Meta, in the language at least, they served them.

This felt actually meaningful and good, as did the fact that every engineer’s title was simply “software engineer”, not “senior principal architect of X.” There’s probably an IC9 somewhere at Meta who runs all of Meta’s billion dollar datacenters and undersea network cabling and thus manages billions of dollars in global capital but whose title is the same as the new grad’s and I really liked this.

There was also an unpretentiousness and kind of Israeli directness and flatness about the place I really enjoyed; any engineer could propose anything, could give blunt, polite feedback about anything to anyone, although how far the proposal or critique traveled depended somewhat on prestige, social network, and level.

Also, the place was full of nerds who played Magic the Gathering and were part of Linux club in college, and aside from the competition there was genuine bonding over craft.

## Workplace

The internal communication system, Workplace, is a literal fork of the Facebook app. Whereas on Facebook people flex about their vacations, on Workplace people flex about both their vacations and also how productive and impactful they are.

Whereas people on Facebook fret about how many likes they got on their wedding photos, people on Workplace fret about that but also whether their director ‘heart’ emojied their confessional piece about the stress they’d been under in shipping that director-priority thing that half.

A typical thing on a team is for the tech lead to start a Google doc with a draft Workplace post that people pile into, which they then post on Workplace the next morning, for maximum engagement, while the tagged team members count the love and like emojis that roll in and think about their performance ratings.

The good part of this is that Meta is Workplace is full of nerd sniping about new optimization methods for post-training LLMs, new ideas in low dimensional embeddings, and also, in the more fun groups, pictures of animals people spotted on campus, the canned food they’re eating while working from home, or dumb, borderline NSFW jokes.

The way I got involved with the Llama effort was by lurking in the Llama team’s Workplace group, reading their posts, and messaging people about how to start a security workstream within it. My team and I did the same to get AI protections into smart glasses, AI agents in Facebook Groups, WhatsApp, whatever else looked interesting.

The place was alive. People cared about ideas; you could find people who’d debate AI xrisk with you, the fine grained details of how we should evaluate fuzzers, and who cared about politics and social theory and the world. People argued from first principles. You could message someone working on one of the most important AI systems in the world and, if your idea was good enough, find yourself in the workstream a week later.

## Missionlessness

I never sensed a broad cross-company feeling of purpose at Meta. Well-tenured folks I talked to were often lukewarm or privately acerbic about the societal value of our products, even though one could sense they’d been more passionate about mission in the 2010s, and you could see their old Workplace posts from back then.

The company had incinerated tens of billions on AR/VR hardware in catastrophic attempt to pivot, and then tried to keep up in the AI race partly by firehosing cash onto the problem, failing to make it into the lead there too; there was a muddle of narratives where a cross-company sense of purpose should have been, none of which really landed.

In the vacuum where company mission should have induced some selflessness and company-level alignment was really everybody’s individual ambition. Sometimes, when good people clustered together on a team, there was a team mission shared by a dozen people who banded together as in a zombie apocalypse movie to try to succeed together and make sure no one was part of the 20% or so that’d be pushed out that year.

I was fortunate to work with some of these teams. But in aggregate what this dynamic wound up meaning was that for big pushes like virtual reality or scaled AI, the company often struggled to ship coherent products that would have required hundreds of people marching passionately behind one banner.

## Conway’s law in a company of individualists

I don’t know if you, dear reader, have ever tried using Horizon Worlds, Meta’s VR app, but it feels like a dumping ground of individual engineers’, individual PMs’, and maybe individual small teams’ ambitions with no coherence; it feels unfinished, basically, as do Meta’s smartglasses and VR headsets.

How this happens at the pattern level is few really deeply believe in the thing Zuck starts; people flood into it because it’s a project Zuck cares about, and they try to use the new project as an opportunity to get promoted so they can spend a few years at the next level and make retirement-level money, and everyone does the showiest thing so they can post on Workplace about what they’ve done in a greedy algorithm that serves their own goals but not a larger goal. The result is a massive muddle of a product or product family.

The same thing happened with AI. You had product leaders from mature, 2010s-era social products flooding in; some had background in older AI models, many had little experience with current AI, and the pivot to AI was obviously a career opportunity and an opportunity for individual advancement or at least survival.

This stood in contrast to more focused cultures like OpenAI, Anthropic, and DeepMind who have not necessarily smarter people, but a stronger shared center of gravity.

## Performance measurement panopticon

At Meta, data scientists were the performance monitors for the entire company; the way reward and punishment are meted out at Meta runs through what the data science org says about you, and downstream of those judgments are layoff decisions, manage-out decisions, promotions, bonuses, equity refreshers.

This meant data scientists wielded enormous power, even though they were compensated far less than engineers and product managers, and it meant people metric-hacked constantly, expending energy on bad metrics that didn’t model the problem they were actually solving, just to look good at promo and performance review time.

## Performance purgatory

I got lucky with the teams I worked on and the projects I picked, but I did have one stretch, about two months long, that gave me a taste of what performance purgatory feels like. I’d advocated for and bootstrapped and done 60 hour weeks to start the workstream applying large language models to content moderation, and it had gone well; the workstream grew into a whole org.

Once we had several other IC7s on it, some of who had been at the company for years and had big social networks (I was an IC7 in my first year), I gave my scope away to them, figuring delegation was a virtue; what I’d actually done was render myself scopeless inside the org I’d been the first cause of forming, and I floundered for a month and a half, not knowing what to work on, while my manager became increasingly alarmed and started sending the kinds of signals you learn quickly to read there: that if I didn’t figure out a role for myself, I’d be managed out.

It got to the point where I cried in a meeting with him after working three weekends in a row trying to get myself back on track, feeling sure I’d need to quit in the next few weeks if I couldn’t solve my problem.

Fortunately an opening came up in Meta’s security org around then, and I’m a security person through and through; I rescued my performance rating, and did great after that.

But the feeling of being on track to fail at Meta is awful in a particular, hollowing way; you can sense when it starts, people begin to shun you, don’t want to be in your meetings, your invites thin out, and you descend into a slow spiral that usually ends with people quitting of their own volition before the company quite gets around to firing them.

If they stick it out they become the walking dead of the company, going through the motions of a job that’s already over, knowing the writing is on the wall, commiserating with others anonymously on Blind, almost never getting back on track.

## What I loved

I lasted three years and seven months there, which transformed my career. I joined at the perfect moment; I’d been obsessed with neural scaling laws and LLMs when I got there and rode that wave; it felt like Type II fun, like running a marathon. The singular focus of it and the trees and air and road blurring by exhilarates you, but you’re always looking at your watch wanting it to be over and you’re always painfully fatigued and increasingly unsure of whether you have the stamina to continue.

The reward and punishment machine at Meta led to some great AI security work done by the sweat and tears of the folks I worked with. I left a few months ago, right after my promotion to IC8, and right as I felt I had a tenured position helping to lead the company’s AI security work. I counterfactually incinerated the financial and career windfall that would have come with that by leaving to start a company. I miss Meta, and I’m also so glad I’m gone.

* * *

#### Subscribe to Joshua Saxe

Launched a year ago

Machine learning, cyber security, social science, philosophy, classical/jazz piano. Currently at Meta working at the intersection of Llama and cybersecurity

Subscribe

By subscribing, you agree Substack's [Terms of Use](https://substack.com/tos), and acknowledge its [Information Collection Notice](https://substack.com/ccpa#personal-data-collected) and [Privacy Policy](https://substack.com/privacy).

[![Maryl Gearhart's avatar](https://substackcdn.com/image/fetch/$s_!rMbw!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F31a14175-f85b-4081-8e94-a77e67dc5ccf_144x144.png)](https://substack.com/profile/17465346-maryl-gearhart)[![Dr. Pravi Devineni's avatar](https://substackcdn.com/image/fetch/$s_!KiQl!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F696074d4-c36f-4c30-bcfb-d5f496cd1d28_842x842.jpeg)](https://substack.com/profile/21657432-dr-pravi-devineni)[![Sharon Goldman's avatar](https://substackcdn.com/image/fetch/$s_!TCMf!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb63b5aac-bf1c-4f77-b127-2861e2e7123d_7360x4912.jpeg)](https://substack.com/profile/16683303-sharon-goldman)[![Tyler Winchester's avatar](https://substackcdn.com/image/fetch/$s_!_yt9!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb63a47db-89ad-4d61-9489-25fe854f72b9_1166x1166.jpeg)](https://substack.com/profile/123449616-tyler-winchester)[![Saurabh Singh's avatar](https://substackcdn.com/image/fetch/$s_!5CV6!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff1f005c9-e4b6-4b70-9d0d-6230a75e0e12_144x144.png)](https://substack.com/profile/1375117-saurabh-singh)

20 Likes

20

3

Share

#### Discussion about this post

CommentsRestacks

![User's avatar](https://substackcdn.com/image/fetch/$s_!TnFC!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Favatars%2Fdefault-light.png)

[![Gus Sandoval's avatar](https://substackcdn.com/image/fetch/$s_!TmUg!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F868fa330-dca2-4214-a9f9-5d59bd3cfd52_144x144.png)](https://substack.com/profile/14962269-gus-sandoval?utm_source=comment)

[Gus Sandoval](https://substack.com/profile/14962269-gus-sandoval?utm_source=substack-feed-item)

[2h](https://substack.com/note/c-262319733 "May 20, 2026, 2:04 PM")

Liked by Joshua Saxe

Such an insightful piece. Thanks for sharing

Like (1)

Reply

Share

[![Letlotlo Mokuoa's avatar](https://substackcdn.com/image/fetch/$s_!gCkG!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F508b9398-ace9-405d-be7c-865b566ed459_1167x1058.jpeg)](https://substack.com/profile/201891640-letlotlo-mokuoa?utm_source=comment)

[Letlotlo Mokuoa](https://substack.com/profile/201891640-letlotlo-mokuoa?utm_source=substack-feed-item)

[2h](https://substack.com/note/c-262313797 "May 20, 2026, 1:53 PM")

Liked by Joshua Saxe

Really enjoyed this piece, thank you for sharing!

Like (1)

Reply

Share

[1 more comment...](https://joshuasaxe181906.substack.com/p/what-it-was-like-working-on-llms/comments)

TopLatestDiscussions

[How to defend an exploding AI attack surface when the attackers haven't shown up (yet)](https://joshuasaxe181906.substack.com/p/how-to-defend-an-exploding-ai-attack)

[The dilemma in AI agent security in 2026 is that organizational attack surface is expanding at comic pace but, at least as of January, the attackers…](https://joshuasaxe181906.substack.com/p/how-to-defend-an-exploding-ai-attack)

Jan 6•[Joshua Saxe](https://substack.com/@joshuasaxe181906)

34

6

![](https://substackcdn.com/image/fetch/$s_!gt8X!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbf53439a-f190-464e-bddd-1007f2a2e088_1024x559.png)

[Swallowing the reality pill in AI agent security](https://joshuasaxe181906.substack.com/p/swallowing-the-reality-pill-in-ai)

[And why we need to focus on low friction security technology in the era of AI acceleration](https://joshuasaxe181906.substack.com/p/swallowing-the-reality-pill-in-ai)

Dec 23, 2025•[Joshua Saxe](https://substack.com/@joshuasaxe181906)

21

1

4

![](https://substackcdn.com/image/fetch/$s_!XoHO!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff6437866-d834-4fbb-8a67-b4712f274345_1024x1024.png)

[Exploits don't cause cyberattacks](https://joshuasaxe181906.substack.com/p/exploits-dont-cause-cyberattacks)

[On thinking clearly about frontier AI advances and cyber conflict](https://joshuasaxe181906.substack.com/p/exploits-dont-cause-cyberattacks)

Apr 8•[Joshua Saxe](https://substack.com/@joshuasaxe181906)

17

7

5

![](https://substackcdn.com/image/fetch/$s_!a-by!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc78e6b3d-e671-415f-9c02-cab32af9bca7_1276x644.png)

See all

### Ready for more?

Subscribe

#### Cookie Policy

We use cookies to improve your experience, for analytics, and for marketing. You can accept, reject, or manage your preferences. See our [privacy policy](https://substack.com/tos).

ManageRejectAccept
