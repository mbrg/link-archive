---
title: "Security for High Velocity Engineering"
tags:
   - Engineering
   - Vulnerability Management
   - Software Development
   - DevSecOps
   - Security
link: https://tldrsec.com/p/security-for-high-velocity-engineering
date: 2025-07-20
summary: "In \"Security for High Velocity Engineering,\" Jason Chan emphasizes a strategic framework for integrating security into rapid software development environments. Key insights include prioritizing developer experience, aligning security investments with organizational growth, and adopting a \"paved road\" approach for common security solutions. The framework emphasizes minimizing cognitive load on engineers and fostering an adaptive security culture. Chan categorizes the approach into context, strategy, and execution, advocating for proactive engagement with engineers through well-supported security initiatives, while continuously measuring and improving outcomes to enhance security posture without stifling innovation."
---

6

- [tl;dr sec](https://tldrsec.com/)
- Posts
- Security for High Velocity Engineering

# Security for High Velocity Engineering

## Strategy and Tactics for Protecting and Enabling Modern Software Organizations

![Author](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/guest_author/profile_picture/097b892e-c173-4245-a1fc-fb892465869e/thumb_team-jason-chan-min.jpg)

Jason Chan

May 13, 2025

_Editor’s note: I’m super excited to share this post by_ _[Jason Chan](https://www.linkedin.com/in/jasonbchan/?utm_source=tldrsec.com&utm_medium=referral&utm_campaign=security-for-high-velocity-engineering)_ _. If you’re not familiar, Jason was the VP of InfoSec at Netflix for many years, building the security culture that’s led to countless great conference talks about building scalable security programs, coining terms like Paved Road, and more. You can also watch an interview I did with Jason_ _[here](https://www.youtube.com/watch?v=xijyr54FZn4&list=PLWigkj_TLWL5pUQ8ESFzJcjgGTpt1XnYQ&index=5&utm_source=tldrsec.com&utm_medium=referral&utm_campaign=security-for-high-velocity-engineering)_ _. Enjoy! -Clint_

_This blog is based off Jason's keynote at LocoMocoSec 2024._

I retired in 2021 after spending twenty plus years in security, with most of that time focusing on what I think is one of the most interesting and challenging problems in our field - collaborating with engineering teams to build and operate secure software. The time away has given me a chance to reflect - what worked, what didn’t work, what I would have changed. I’m now combining my experience and those reflections to provide my best current guidance on how to build a security program to work effectively with high velocity engineering organizations.

#### Some Personal and Industry Background

I got started in security in the late 1990s. A few years into my career, a seminal document in the history of software security was written - Bill Gates’ (Microsoft’s founder and longtime CEO) [Trustworthy Computing memo](https://www.wired.com/2002/01/bill-gates-trustworthy-computing/?utm_source=tldrsec.com&utm_medium=referral&utm_campaign=security-for-high-velocity-engineering). The memo was published in January 2002 after Microsoft products had suffered from many years of security issues - vulnerabilities, worms, viruses, etc. Gates was asking the company to essentially halt feature work and make security Microsoft’s top priority.

This memo ushered in what you can think of as the SDL (Security Development Lifecycle - Microsoft’s term for the process of developing secure software) era of software security. I was quite entrenched in this way of thinking, and in fact I consulted for Microsoft for two and a half years during this time - doing product security work and assessments and developing and delivering security training for developers. Microsoft deserves significant credit for helping mature the field, and I and many of my contemporaries took this experience with us as we moved ahead in our careers.

Fast forward to 2009, and I joined VMware to lead their security team. At the time, VMware’s online services were developed and deployed in a very traditional and linear way. Deployments only happened once a month and required about 12-18 hours of downtime. We had 50-60 people in the room to coordinate the release, and we had a 100 plus page Word document outlining the many required steps for software deployment. For better or worse, this was how many online services were deployed around this time.

In 2011, I left VMware and joined Netflix. Netflix was maybe 600 people at the time, and fairly early in its simultaneous journeys to the public cloud and to delivering a streaming video service after many years as a DVD by mail company. Even then, Netflix was deploying code dozens of time a day. So - I went from one week at VMware doing a dozen deploys a year to the next week at Netflix doing a dozen deploys before lunch. I knew pretty quickly that what I had been doing - largely practicing “SDL style” security for engineering - wasn’t going to work and that I’d have to think differently.

Looking back, the key difference in thinking was encapsulated in a conversation I had much later on, at the last social event I went to before the COVID lockdown in 2020. It was a security happy hour in San Francisco, and there were lots of security engineers and leaders from other tech companies in attendance. I was chatting with someone from a well known large tech company about security culture, and she told me their CTO wanted every engineer at the company to think “security first”. Of course, as security folks, we love to hear this. It sets the tone from the top and provides a lot of energy and support for the security team. However, I told her that I had almost the opposite approach culturally. I want developers to focus on what they were hired to do.

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/3f634aaa-a1d8-4857-ad47-201d0c900ab8/culture_continuum.jpg?t=1743093865)

The culture continuum for security in engineering.

Engineers are expensive and hard to hire - if you find a great algorithms or personalization or data engineer - you want them focusing on their domain expertise: it’s how they bring value to the business. They are not security experts, and a core principle in my own leadership philosophy is that I don’t want to make people responsible for areas in which they are not expert.

This is really the essence of security in high velocity engineering environments - **we as security teams have to make the investments culturally and technically to allow engineers to focus and spend time in their areas of expertise**.

So - how do we approach these investments and adjust how we’ve been doing things historically? As this is a fundamental and structural shift, it’s not just about tools or technology - you’re underlying strategy and mindset must reflect the changes you want to make. I structure my recommended approach in three layers - **context**, **strategy**, and **execution**.

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/d58f0330-22de-4f57-9b76-b7a6e56f06a8/image.png?t=1744642531)

## Context

We’ll start with context - the overall environment in which a security team operates. To a large degree I think of context as non-negotiable - it’s simply the life and times you find yourself in - the collection of external and internal influences that shape much of how your team must conduct itself.

### External Context

Externally, I like to frame context in terms of secular trends - long-term, directional shifts that occurs over many years. Good examples are the global adoption of broadband Internet and mobile phones - these trends have been increasing over many years and will likely continue to do so. Contrast this with seasonal trends - for example when people tend to buy flowers (on Valentines Day and Mothers Day in the United States for example) - a trend that repeats the same up and down pattern year after year.

Your team must understand, acknowledge, and incorporate key secular trends to be successful over the long term. Some key secular trends that I advise folks to bear in mind include:

- **Increased Regulation**\- We become more regulated over time. Geographic, industry specific, partner and supply-chain requirements - these are all regulatory influences that exert influence on your organization and security team. Building a team that can effectively deal with dynamic and increasing regulatory impact over time is essential for success.

- **More Software** \- We have more software over time - whether it’s SaaS, open source, internally developed, or created by low-code/no-code tools or generative AI. The many digital transformation efforts you see only lead to more software as legacy business processes and systems are modernized.

- **More Vulnerabilities** \- And of course, if we have more software, we can guarantee that we will have more vulnerabilities. In 2024, [NIST was barely able to keep up with the backlog of vulnerabilities and the National Vulnerability Database](https://www.cybersecuritydive.com/news/nist-national-vulnerability-database/712826/?utm_source=tldrsec.com&utm_medium=referral&utm_campaign=security-for-high-velocity-engineering).


[![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/2f6fa30f-7b1f-4f50-b610-132ade4bf9e9/Number_of_CVEs_by_year__1_.png?t=1744643192)](https://www.cvedetails.com/browse-by-date.php?utm_source=tldrsec.com&utm_medium=referral&utm_campaign=security-for-high-velocity-engineering)

[https://www.cvedetails.com/browse-by-date.php](https://www.cvedetails.com/browse-by-date.php?utm_source=tldrsec.com&utm_medium=referral&utm_campaign=security-for-high-velocity-engineering)

#### Organizational Context

In addition to external context, there is a key internal driver that almost all security teams have to acknowledge. Now, more than ever, organizations see rapid tech and software innovation as keys to success. Marc Andreesen (Netscape co-founder and venture capitalist) [noted this in 2011](https://a16z.com/why-software-is-eating-the-world/?utm_source=tldrsec.com&utm_medium=referral&utm_campaign=security-for-high-velocity-engineering) when he declared that software was eating the world and Satya Nadella (Microsoft CEO), almost a decade later, stated that [“every company is now a software company”](https://www.satellitetoday.com/technology/2019/02/26/microsoft-ceo-every-company-is-now-a-software-company/?utm_source=tldrsec.com&utm_medium=referral&utm_campaign=security-for-high-velocity-engineering).

Given how critical the ability to deliver and operate software is to modern business, modern security teams must realize that **supporting this ability is one of their primary drivers**.

## Strategy

Whereas we understand context as mostly non-negotiable, strategy is all about decision making. There are libraries written about strategy, but when I talk about it I always refer back to a quote from Reed Hastings (Netflix’s co-founder and longtime CEO):

_**“Strategy is pain. Strategy has to be difficult. It’s about what you don’t do.”**_

Strategy is about focus and deciding, among all possible options, which path you are going to pursue to achieve a goal. Think about our world of securing software. There are so many potential investments - static analysis, penetration testing, threat modeling, code review, developer education, bug bounties, and fuzzing to name a few. Each of these has its place (and costs and benefits), but chances are you are not resourced to do them all, and even if you were, the business would not tolerate the overhead.

Let’s look at how to develop a strategy for securing high-velocity engineering organizations.

### Strategic Constraints

We will start with strategic constraints - essentially the box in which your strategic approach must operate. If your choices venture too far outside of this box, you will likely fail.

#### Align with Developer Experience

First and most importantly, we must align our security program to developer experience and developer productivity. Margaret-Anne Storey and colleagues provide [a good primer and framework for understanding what works in developer productivity](https://dl.acm.org/doi/pdf/10.1145/3610285?utm_source=tldrsec.com&utm_medium=referral&utm_campaign=security-for-high-velocity-engineering) \- and using this framework we understand that our security efforts must align to the three dimensions of developer productivity:

1. **Maximize flow state** \- Flow state, or uninterrupted time for deep work, must be optimized. Our security initiatives must respect flow state by minimizing unplanned work, unscheduled interruptions, and low-value meetings.

2. **Effective feedback loops** \- We must provide developers timely and validated feedback in the systems they use.

3. **Minimize cognitive load** \- Cognitive load is the amount of mental overhead required to get something done. We have to make security easy for developers to engage with.


The failure mode for not aligning with developer experience and productivity? Your developers will hate you and find ways to avoid engaging with you. Your program will fail because you’re unable to develop key relationships with engineering teams and leaders.

#### Sublinear Growth

Security teams are centralized teams - by handling security, we support the entire business. Other centralized teams include legal, human resources, facilities, and IT. The one rule that all centralized teams share - you must grow sublinear to company growth.

![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUenHWIBvFsaVrnqmV5Na_uRXvNxMiP6wP0RoxxQFPwLFzVKnqRAjlE0OFoXEMsUXDxklvREnjfvSSQeKvcN-Z2ah4AR-HuVUURuRnZDy3j5YprACY415QW4yjf4SENQiLdRpv13qJocX7ttrevIQjSGflqEIE5p=s2048?key=gIMozEiDGPXmKi-Qvo7Thg)

While this makes sense and seems uncontroversial (“of course the security team shouldn’t be growing faster than the company!”), security teams are made of humans. And humans of course have egos - we want to grow in our careers, take on additional scope, and get promoted. Success in a central team is about effectiveness, though, and not growth. Your failure mode here is you’re going to find yourself in trouble with your CFO.

#### High Leverage Investments

The last strategic constraint is that you must focus the majority of your resources and energy on high leverage investments. Edmond Lau discusses this in his book [The Effective Engineer](https://www.effectiveengineer.com/?utm_source=tldrsec.com&utm_medium=referral&utm_campaign=security-for-high-velocity-engineering) \- leverage is about maximizing impact for the time invested.

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/1cc75610-4ac9-493c-97f5-1452a2dedc87/image.png?t=1744674330)

Leverage can be thought of as a spectrum - from low to high. A very low leverage security investment would be a one-on-one meeting with an engineer to help them with a security issue (one to one). A higher leverage investment would be going to that engineering team’s meeting to educate the entire team at once (one to many). Even higher leverage would be documenting the solution (reusable artifact).

If you’re in a high growth company, this principle is even more important. You must evaluate your potential investments through the lens of leverage (remember strategy is about what you are not going to do). The failure mode here is that you are not going to be able to keep up with the engineering teams you serve and you will be wasting time on bespoke engagements and approaches rather than scalable and reusable solutions.

### Strategic Principles

In addition to constraints that help narrow your focus, we can look at some strategic principles that you can think of as the pillars upon which you build your program and approach.

#### Change is Constant (so get good at it)

Certainly security is a more addressable problem when things stay the same - no new technology, architectural changes, connectivity, or org changes to worry about. But we know that change is constant, especially in this age of digital transformation and AI. Accept that change will happen regularly and adapt so that you get good at handling these changes.

In his book [An Elegant Puzzle](https://press.stripe.com/an-elegant-puzzle?utm_source=tldrsec.com&utm_medium=referral&utm_campaign=security-for-high-velocity-engineering), Will Larson notes that engineering leaders need to be great at two things - executing technical migrations and running org changes. While this doesn’t seem flashy or revolutionary, this advice recognizes that technology is always changing and improving and that businesses are constantly adapting to market conditions. Adopting the right technology efficiently (and migrating off older technology) and adjusting the structure of your organization are the ways you effectively leverage changes in technology for the betterment of the business.

In security - we must do the same - we need to build controls and programs that work regardless of the technology and architecture in use. And we must get comfortable and competent adjusting the structure of our teams - there is no one perfect security org structure so we need to think of org changes as events to be embraced rather than avoided.

#### Change Systems, Not People

Relatedly - we want to focus on changing our systems, not the people that use those systems. Early on in my time at Netflix, we looked at some data that showed the average tenure for an engineer was around 18 to 24 months. That is the amount of time you have to get an engineer productive and delivering to benefit the business. How do you want to spend that time? It’s not in security training and awareness education. Rather, you want to invest your resources in making your security systems and interfaces simple and easy to use for even brand new engineers.

#### Guardrails, not Gates

The last strategic principle is one I first introduced at [LASCON in 2013](https://www.youtube.com/watch?v=geumLjxtc54&utm_source=tldrsec.com&utm_medium=referral&utm_campaign=security-for-high-velocity-engineering) \- guardrails, not gates. This is an analogy I pulled directly from the world of traffic control. Gates (for example a toll booth or inspection area) typically involve stopping a car and running some process (paying a toll, inspecting a vehicle) before someone decides whether that vehicle can proceed.

That is how we’ve typically placed security controls in the development process (and certainly in the aforementioned SDL-type programs). An engineering team is working and they need to pause for a design review, threat model, penetration test, vendor review, or other security activity. They then await the results of that activity before determining how and if they proceed. Think about how this approach aligns with the previously discussed dimensions of developer productivity - maximizing flow state and having effective feedback loops. **By adopting gate-based security we are explicitly choosing known anti-patterns to developer productivity.**

Guardrails, on the other hand, exist at the edge of a road and keep your vehicle moving while preventing you from going off the road. This is the approach you need for security in modern, high velocity engineering environments. Another way to think of this change is from synchronous evaluation (in-person design review or threat model, manually driven “go-live” review) to asynchronous and continuous evaluation (monitoring the use of recommended patterns and practices). It’s all about moving fast and staying safe.

## Execution

We’ve looked at the context in which we all operate in, and we understand the strategic constraints and principles we need to successfully build a security program to support modern, high velocity engineering. But, what do we actually do? What does the day to day look like? Let’s take a look at the actual execution now.

### Core Processes

The first category of execution is what I call core processes. These are fundamental security processes that just about every security team will perform. While they are ubiquitous and fundamental, it doesn’t mean they are easy. High performing teams will focus heavily in these areas and improve over time.

#### Environmental Context

With this process, we are seeking to understand the environment which we are responsible for securing. We are aiming to acknowledge and learn from the old maxim that “you can’t secure what you don’t know about”. The first process is itself composed of two sub-processes - **discovery** and **enrichment**.

With discovery, we are continuously updating the context we have of what we’re defending by identifying the various assets and components that comprise our environment. Think broadly with this process and identify systems, applications, code repositories, users, vendors, data stores, etc.

With enrichment we are taking the raw data from discovery and enhancing it with information about asset ownership, on-call rotations, criticality, regulatory impact, etc. Successful enrichment allows us to truly operationalize environmental context.

#### Vulnerability Management

The second core process is vulnerability management - likely the most heavily invested in area of cybersecurity and for good reason. Nothing new here in terms of what we’re doing, but you can also think of this as consisting of two sub-processes - **finding** (via SAST, DAST, bug bounty, etc.) and **fixing** (updates and remediation via patching, migrations, configuration changes, etc.).

#### Response

The final core process is response, inclusive of general incident response and product security incident response. This process is also typically engaged for large-scale critical vulnerabilities (e.g. log4j) and security issues that impact your key third party partners. Overall, the goal is to keep the business focused and up and running via competent and efficient response practices.

### The Paved Road

Core processes are going to be executed by just about all security teams regardless of their approach to software engineering. The differentiating component for successful security in high velocity engineering environments is the **paved road** (a concept also known by similar names such as golden path, well-lit path, etc.). The name comes from a real world analogy - if you’re trying to get from point A to point B, then a paved road is a smooth, easy, and predictable way of getting there.

In the context of engineering, **a paved road is a collection of well-supported, optional solutions for common problems, and these solutions are provided and supported by central teams**. Optionality is a key part of a paved road - if the solutions were required then we would just refer to them as requirements. One of the characteristics of most high velocity engineering environments is a rapid rate of change, and optionality in solution choices is key to innovation, learning, and improvement.

Central teams (e.g. security, observability, platform, data) are responsible for a common domain for the entire organization and offer their products and services as a paved road for other teams to use to solve domain-related problems. For example, a security team may offer a cryptography API to allow other teams to easily and securely access functions such as encryption and cryptographic signing and hashing. It’s not that this API is the only way for an engineering team to solve these problems, but using the security team’s API is going to be easy and well-supported. A successful paved road allows engineering teams to focus on their areas of expertise and responsibility by relying heavily on domain experts from central teams.

The most fundamental shift that a paved road enables is in the relationship between engineering teams and security teams. Instead of the security team chasing people only to fix issues and address vulnerabilities, the security team instead asks engineering teams to adopt paved road solutions. The payoff for this adoption is going to be increased focus, better security outcomes, and less unplanned work (e.g. time responding to incidents and patching vulnerabilities).

#### The Two Dimensions of the Paved Road

There are two dimensions to security paved roads (again matching real world paved roads) - how wide the road is and how smooth the road is.

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/a6f56aac-f5b2-42d1-90fd-80f80dac99d1/image.png?t=1745510662)

Dimensions of the Paved Road

The width of the paved road relates to how many offerings are provided by the central team. This width goes from zero (no well-supported solutions to common problems) to any number of offerings. The smoothness of the paved road is about how easy each of the paved road offerings is to adopt. Smoothness is a spectrum - you might start with a wiki page that lets engineers know how to do something and work your way up to having this functionality integrated into the environment (think secure by default). As you’d expect, **the goal of the security team is to make the road both wider and smoother**.

## Measure, Adapt, Improve

Putting it all together, this model for security in high velocity engineering environments looks something like this.

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/1ed903d1-e4a7-4de1-a24e-2ba05b4c9f85/image.png?t=1745511016)

The Building Blocks for Security in High Velocity Engineering Environments

We understand the context we’re operating in, we have built our strategy through constraints and principles, and we are executing processes and building out our paved road.

Throughout this evolution of program building and maturity, we are thinking about measuring, adapting, and improving.

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/97cdb782-4dd4-4034-9fbd-d03aabae9b34/image.png?t=1745511152)

Measure, Adapt, and Improve

There are many references and examples available for core process metrics, so I won’t cover them here. Instead, I recommend really diving deep into the interplay between your core processes and the paved road. To make this more concrete, here’s an example from early in my time at Netflix (late 2011, early 2012).

At the time, we had a pretty solid cryptographic API for developers that helped them with encryption, decryption, and signing. But it wasn’t well-suited for runtime secrets management or vaulting things like cloud credentials or database connection strings. So, many of the vulnerabilities I saw at the time involved things like secrets in code. However, I did not flag those to the developers to fix because I had no supported solution. If they had been flagged, you would see developers spending time on bespoke and one off solutions that would likely be both insecure and difficult to support.

Instead of filing tickets for vulnerabilities that had no well-supported solution, we adapted the existing cryptographic API to handle runtime secrets management. Then, we drove adoption campaigns so that developers understood this new capability and could use it in their services. Only then did we start more formal campaigns to alert engineers to issues like secrets in code.

Abstracting this, your measure, adapt, improve loop consists of hypotheses that adoption of a given paved road offering (e.g. runtime secrets management) is going to lead to better security outcomes for the teams that adopt the solution (e.g. fewer secrets in code vulnerabilities, fewer incidents involving leaked credentials or secrets).

This becomes the focus of how you engage with your engineering teams - it’s much more proactive and solution-oriented than the typical reactive relationships that security and engineering teams have. You can then do things like analyze the questions and engagement that your security team gets (i.e. in a security Slack channel). Who is asking questions? How often do they recontact us? How broad is their adoption of our paved road? Measuring these elements allows you to focus your team’s limited resources in engaging the right folks.

## Wrapping Up

We know an organization’s success is tied to its ability to deliver and operate software. We now have a framework to use to adapt our security approach in support of this success. For takeaways, I’ll leave you with three things:

**Let your developers focus, adapt to change, and be discerning with your investments!**

#### Keep reading

[![How to securely build product features using AI APIs ](https://media.beehiiv.com/cdn-cgi/image/format=auto,width=800,height=421,fit=scale-down,onerror=redirect/uploads/asset/file/e818d5ab-9e95-4023-be2a-ce67bb9baf31/tl_dr_sec_Rami_McCarthy_-_headers_diagrams.png)\\
\\
**How to securely build product features using AI APIs** \\
\\
A Practitioner’s Guide to Consuming AI](https://tldrsec.com/p/securely-build-product-ai-machine-learning) [![BSidesSF 2019: DevSecOps State of the Union](https://media.beehiiv.com/cdn-cgi/image/format=auto,width=800,height=421,fit=scale-down,onerror=redirect/uploads/asset/file/62f5eb4c-3fea-41f0-acf2-6c40a3ac7698/DevSecOps_State_of_the_Union.jpg)\\
\\
**BSidesSF 2019: DevSecOps State of the Union** \\
\\
There's been a lot of great research in SecDevOps over the past few years. This talk organizes and references around 40 useful talks in the space.](https://tldrsec.com/p/blog-bsidessf-devsecops-state-of-the-union) [![AI, Deepfakes, and Phishing](https://media.beehiiv.com/cdn-cgi/image/format=auto,width=800,height=421,fit=scale-down,onerror=redirect/uploads/asset/file/d7fe3453-1d40-448c-b57e-ecd8fcac5e9a/clint_tldrsec_cute_hacker_kid_fishing_cartoon_61cfb6e3-c298-4408-af23-71d8910dd7ee.png)\\
\\
**AI, Deepfakes, and Phishing** \\
\\
A round-up of AI and LLMs being applied to deepfakes and phishing](https://tldrsec.com/p/ai-deepfakes-phishing)

View more

Twitter Widget Iframe
