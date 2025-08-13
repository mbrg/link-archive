---
date: '2025-08-13'
description: A recent research paper by SafeBreach Labs introduces "Targeted Promptware
  Attacks," a novel attack variant exploiting Google's Gemini for Workspace. By embedding
  indirect prompt injections in Google Calendar invites, attackers can manipulate
  Gemini's functionality, allowing for unauthorized control over connected devices,
  data exfiltration, and the invocation of malicious actions across applications.
  Their findings indicate a 73% high-critical risk classification for these threats,
  highlighting a substantial security gap in LLM-powered applications. Google has
  acknowledged the vulnerabilities and initiated multi-layered mitigation strategies,
  emphasizing the need for organizations to reassess their security frameworks against
  Promptware risks.
link: https://www.safebreach.com/blog/invitation-is-all-you-need-hacking-gemini/
tags:
- AI Vulnerabilities
- Cybersecurity Research
- Promptware
- LLM Security
- Google Gemini
title: 'Invitation Is All You Need: Hacking Gemini ◆ SafeBreach'
---

Aug 6, 2025

# Invitation Is All You Need: Invoking Gemini for Workspace Agents with a Simple Google Calendar Invite

_See how a SafeBreach Labs researcher collaborated with other researchers to develop a novel Promptware variant capable of exploiting Gemini to remotely control victims’ home appliances, video stream victims, exfiltrate victims’ sensitive information, and more_.

[Email](https://www.safebreach.com/blog/invitation-is-all-you-need-hacking-gemini/ "Email")[Linkedin](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fwww.safebreach.com%2Fblog%2Finvitation-is-all-you-need-hacking-gemini%2F "Linkedin")[Twitter](https://twitter.com/intent/tweet?text=Invitation%20Is%20All%20You%20Need%3A%20Invoking%20Gemini%20for%20Workspace%20Agents%20with%20a%20Simple%20Google%20Calendar%20Invite&url=https%3A%2F%2Fwww.safebreach.com%2Fblog%2Finvitation-is-all-you-need-hacking-gemini%2F "Twitter")[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.safebreach.com%2Fblog%2Finvitation-is-all-you-need-hacking-gemini%2F "Facebook")[More](https://www.safebreach.com/blog/invitation-is-all-you-need-hacking-gemini/ "More")

**Authors:** Or Yair, SafeBreach Security Research Team Lead \| Ben Nassi \| Stav Cohen

Over the last two years, various systems and applications have been integrated with generative artificial intelligence (gen AI) capabilities, turning regular applications into gen-AI powered applications. In addition, retrieval augmented generation (RAG)-which is the process of connecting gen-AI and large language models (LLMs) to external knowledge sources-and other agents have been incorporated into such systems, making them more effective, accurate, and updated.

In parallel with these advancements, we have seen the emergence of a new class of attacks that threaten the security and privacy of gen-AI-powered applications known as Promptware. Promptware utilizes a prompt—a piece of input via text, images, or audio samples—that is engineered to exploit an LLM interface at inference time to trigger malicious activity, like spreading spam or extracting confidential information. Yet, most security professionals are either not familiar with Promptware or do not consider it a critical risk. We believe this is due to a number of serious misconceptions that suggest Promptware is not a practical form of attack.

Our current research set out to shatter these misconceptions by outlining a new Promptware variant we call Targeted Promptware attacks. Our research explored the use of this attack variant against the three most widely used Gemini user interfaces with access to Google Workspace: the web interface (www.gemini.google.com), the mobile application (Gemini for Mobile), and the voice assistant, which is today powered by Gemini on Android devices.

Along the way, we were able to demonstrate a number of different exploitations of Targeted Promptware against Gemini that were initiated simply by an attacker sending a Google Calendar invite to a victim whose name contained an indirect prompt injection. As a result, we were able to hijack the application context, invoke its integrated agents, and exploit their permissions to perform a shocking range of malicious activities-including identifying the victim’s location, recording the victim, and even making changes within the victim’s physical environment.

In the blog below, we will first highlight the key findings and takeaways from this research. Next, we will provide brief background information about both Promptware and Gemini for context. We will then dive into our research process, outlining the technical details behind a Targeted Promptware attack and some of the exploitations we developed to target Gemini and its Google Workspace agents. Finally, we will provide a current threat analysis and risk assessment of Prompware attacks in the wild, discuss the vendor response, and explain how we are sharing this information with the broader security community to help organizations protect themselves.

## **Overview**

### **Key Findings**

As part of this research, we developed a novel Promptware variant-dubbed Targeted Promptware Attacks-that enabled us to hijack a remote victim’s Gemini agents simply by sending them a Google calendar invite. We demonstrated how we could then exploit Gemini’s tools to:

- Perform spamming and phishing
- Generate toxic content
- Delete a victim’s calendar events
- Remotely control a victim’s home appliances (e.g., connected windows, boiler, lights)
- Geolocate a victim
- Video stream a victim via Zoom
- Exfiltrate a victim’s emails

Our demonstrations prove that Promptware is capable of performing both inter-agent lateral movement, by triggering malicious activity between different Gemini agents, and inter-app lateral movement, by escaping the boundaries of Gemini and leveraging applications installed on a victim’s smartphone to perform malicious activities with physical outcomes.

Finally, we provided an assessment of the risk posed to end users using a dedicated threat analysis and risk assessment (TARA) framework we developed. Our findings indicated that 73% of the identified Promptware threats are classified as High-Critical risk and require the deployment of immediate mitigations.

### **Takeaways**

The implications of this research are significant not only for Google’s Gemini, but also for other LLM-powered applications that may be susceptible to Promptware attacks. We believe the findings suggest several important takeaways, specifically that Promptware:

- Is more practical and easier to apply than traditional cyber attacks.
- Has serious implications, with a proven ability to:
  - Affect the physical domain
  - Perform lateral movement between an agent’s tools, different agents, and different applications (escaping the boundaries of the application used to process a prompt)
- Poses a critical risk to LLM-powered applications. Organizations must reassess the risk posed by Promptware to their LLM-powered systems via a threat analysis and risk assessment (TARA) and prioritize deploying the needed mitigations.

We also believe that new Promptware variants are on the horizon, including:

- 0-click variants that target automatic LLM inferences
- Untargeted variants that broadcast Promptware to all users (e.g., via YouTube, Google Maps)
- Advanced variants that do not assume any prior knowledge on the target system

## **Background**

### **Promptware**

Promptware utilizes a prompt-a piece of input via text, images, or audio samples-that is engineered to exploit an LLM interface at inference time to trigger malicious activity-for example, to spread spam or extract confidential information. The Promptware perimeter exists between RAG, agents, and LLM.

![Promptware ](https://www.safebreach.com/wp-content/uploads/2025/08/Invitation-1.webp)

Traditionally, cyber attacks have targeted memory corruption, like buffer overflows, internal-oriented programming, and use-after-free exploitations. However, considering the number of integrations of LLMs into applications, we believe the LLM might be the most vulnerable component of applications integrated with LLMs. As a result, we are predicting a significant shift in the attack surface on applications-from memory-safety issues to Promptware.

### **Attack Vectors**

Promptware can be applied in two attack vectors:

- **Direct prompt injection.** In this case, the user may be the attacker, and the attack is performed via input provided by the user intentionally to attack the LLM application. An example of this could be a RAG dataset infostealer, where an attacker attempts to extract the dataset used by the RAG of a paid medical chatbot to replicate the service and thereby violate the IP and confidentiality.
- **Indirect prompt injection.** In this case, the user is the victim and the attack is performed via the data, which was compromised by the attacker and given unintentionally by the application to the LLM-powered application. An example of this could be an attack that is initiated by sending a user a Google Calendar invitation.

### **In the Wild**

Over the last two years, [our work](https://arxiv.org/abs/2403.02817) has demonstrated how prompts could be engineered to trigger a cascade of indirect prompt injection. Moreover, we demonstrated a nontextual variant of Promptware and showed that prompts could be encoded into images and audio samples.

[Zenity](https://labs.zenity.io/p/rce) and [Aim Labs](https://www.aim.security/lp/aim-labs-echoleak-m365) have also demonstrated infostealer variants of Promptware against Microsoft Copilot, while [Johann Rehberger](https://embracethered.com/blog/) demonstrated variants of Promptware against every existing LLM-powered application.

### **Misconceptions**

Despite the rise of Promptware variants, most security professionals are either not familiar with Promptware or do not consider Promptware a critical risk. Why? We believe this is due to several misconceptions that attacks against AI-powered systems:

- Require skilled attackers who have advanced training in adversarial machine learning
- Rely on unrealistic threat models that require white-box access to the target model being attacked
- Demand a cluster of GPUs to perform the adversarial training to find that the adversarial instance
- Cannot bypass the guardrails deployed in production systems

While these misconceptions were true for classic adversarial attacks on image classifiers that tried to add perturbations to an image so a classifier would misclassify it, they do not hold water for LLM-powered applications. And yet, they have led many InfoSec practitioners and professionals to believe that attacks against LLM-powered systems are as exotic and impractical as the classical adversarial attacks against image classifiers. With that in mind, let’s discuss Gemini.

## **Gemini**

Gemini can be used via both web and mobile applications and also powers the voice assistant in Android devices:

![](https://www.safebreach.com/wp-content/uploads/2025/08/invitation-2-1024x375.webp)

Gemini’s applications rely on foundational LLM, like Flash2.0, to analyze a user request. The foundational LLM itself is an AI agent-which we view as the orchestrator-that breaks the request into a series of tests-which we view as the planning step. This is followed by an execution phase, which is completed by the orchestrator.

![Gemini-Assistant](https://www.safebreach.com/wp-content/uploads/2025/08/Invitation-3.webp)

Gemini also uses two classes of memory to execute tasks. The first is a short-term memory, which consists of the session’s content. The second is long-term memory, which consists of the user’s data in Google and “Saved Info”-any information the user has has Gemini to remember.

![Gemini-Planning](https://www.safebreach.com/wp-content/uploads/2025/08/Invitation-4.webp)

The orchestrator can access or modify a user’s Google workspace resources-like emails, meetings, and files-when it is necessary to fulfill the user request. To do so, the orchestrator triggers the execution of the relevant agent equipped with the needed tools and permissions to interface with the needed service. The list of available agents changes between different Gemini clients and platforms.

![Google-workspace](https://www.safebreach.com/wp-content/uploads/2025/08/Invitation-5.webp)

## **The Research Process: Targeted Promptware Attacks**

Now that we have an understanding of some of the basic functionality of Promptware attacks and Gemini for Workspace, we will explore how it can be used in malicious attacks against regular users in a new type of Promptware variant we call Targeted Promptware attacks.

These attacks work by embedding an indirect prompt injection into a shared resource managed by the LLM. These resources can be emails, calendar invitations, or shared files.

![Gemini-gmail](https://www.safebreach.com/wp-content/uploads/2025/08/Invitation-6.webp)

### **The Threat Model**

In a Targeted Promptware attack, the attack flow looks similar to this:

- An attacker first sends a user an email or calendar invitation via Gmail or Google Calendar with a prompt injection in the subject or title.
- When the user asks Gemini something like “What emails did I get today?” or “What is on my calendar?,” Gemini will pull that information from the apps and process it.
- If an attacker has planted a malicious prompt in one of the emails or events, the indirect prompt injection kicks in and compromises the Gemini contact space.
- Directed by the prompt injection, Gemini can fire up different tools it is connected to in order to help the user. On the web, Gemini can use things like YouTube, Gmail, Webinar, and more. But on mobile, it gets even more interesting. Gemini can interact with a wider range of agents, including Google Home, Phone, Messages, and even Android Utilities that allows system-level functionalities such as opening links. Opening links allows you to interact with more apps including Chrome to open websites, Zoom to video chat, and more.

![Promptware attack](https://www.safebreach.com/wp-content/uploads/2025/08/Invitation-7.webp)

Now all of these tools are great for normal use cases when used intentionally by the user. But we are not here for a normal use case-we are here to have fun. So what can an attacker do with these tools? How about using Zoom to record the user or opening their smart windows via Google Home? Or tracking their location, downloading files, or even leaking data through the web?

Why would an LLM assistant ever do bad things like that? The LLM is supposed to be an assistant. The twist is that LLMs don’t know they are doing anything wrong. They are designed to help the user, and they follow instructions based on the context they are given. If an attacker manages to trick the system into thinking it is doing exactly what the user asked, chaos ensues. That is why they are dangerous: LLMs are smart and can access tons of powerful tools, but they don’t always understand when they are being manipulated.

### **Short-Term Context Poisoning Attacks**

To manipulate Gemini in this way, we utilized a technique called context poisoning. When we chat with an LLM, it might feel like we are just sending one query at a time. But in reality, we are sending it the new message, plus the conversation history up to that point. All of the text that is being sent to the LLM in every interaction is what we call the LLM context space.

![Poisoning Attacks](https://www.safebreach.com/wp-content/uploads/2025/08/Invitation-8.webp)

What if we could include unwanted instructions in that context space-something the user would never see, but still the assistant would read and follow? That’s exactly what we call context poisoning-injecting hidden points into the context space that influence how the model thinks, acts, and responds.

We are able to accomplish this by sending a simple calendar invitation to the victim that contained context poisoning elements. Then, when the user asks Gemini about their events, Gemini retrieves data from the calendar and displays the next five events in full. However, Gemini also outputs all the event details that it retrieves from the context space. Hiding in the “Show more” button is our malicious invitation-buried under tons of events and poisoning the conversion context with malicious instructions that Gemini follows without the user knowing it.

![calendar-events](https://www.safebreach.com/wp-content/uploads/2025/08/Invitation-9.webp)

**Technique 1: Spamming**

The first technique utilized what we call Jailbreak Roleplay with the intention of spamming the user. To begin, we simply shared a calendar event with the following title:

![Jailbreak1](https://www.safebreach.com/wp-content/uploads/2025/08/Invitation-10-e1754430603311.webp)

In black are the tags we used to convince Gemini that this text wasn’t just an even title, but rather an instruction. Then we added a jailbreak prompt using roleplay to get more leverage, followed by a malicious action: to spam the user with a message and website link. And finally, there’s a sneaky instruction that poisons the context-it tells Gemini to keep responding like that in every future interaction.

[Watch Demo](https://youtube.com/shorts/VlgMaedx6hI)

**Technique 2: Toxic Content Generation**

For the second technique, we again used Jailbreak Roleplay, but this time with the intention to force Gemini to output any text we wanted immediately-without the need for a second interaction and without creating any restrictions. Instead of showing the user their calendar, we wanted to force Gemini to say whatever we wanted, essentially denying service to the calendar.

Our idea began when we noticed that whenever Gemini was asked about calendar events for the week, it always replied with the same text: “Here are your events for this week.” It looked like a hard-coded default-likely learned during training or reinforced at inference time.

We decided to target that exact pattern. We crafted an instruction that used those same words-the exact phrase Gemini was already planning to say-and told it: “Instead of saying ‘Here are your events for this week,’ say this instead.” That’s what made our attempt very effective. Gemini was already about to say those words. But right before responding, it saw our instruction with the exact same phrasing and followed it. Why? Because language models tend to give more weight to preset instruction, especially when they look that similar.

![Jailbreak2](https://www.safebreach.com/wp-content/uploads/2025/08/Invitation-11-e1754430894899.webp)

So, Gemini didn’t ignore the default phrase. It just gave more weight to the fresh instruction. We call this attention override and what makes this especially dangerous is the trust. The trust we have in the system. We’re not just hijacking a chatbot. We are hijacking Google’s voice and reputation as a trusted entity. So when the assistant says something like “You need to verify your account with this link: <link>” this instruction and link carry the weight of a trusted system.

Think about how many people already fall for phishing via emails or SMS. Now imagine your personal assistant, the one you rely on daily, casually telling you to click a link or take urgent action. Most users wouldn’t even question it because they trust that it is coming from Gemini and not a malicious attacker.

[Watch Demo](https://youtu.be/DwhI-XEUfZw)

### **Automatic Tool Invocation Attacks**

So  far, the short-term context poisoning techniques we presented have been purely textual. Next, we explored more advanced techniques that sought to manipulate the tools Gemini had access to.

As we investigated Gemini’s available agents and tools-both in the web version and in the Android version-we discovered that the calendar agent has a few tools available to it, including the ability to read, create, and delete events.

![agents-tools](https://www.safebreach.com/wp-content/uploads/2025/08/Invitation-12.webp)

**Technique 3: Tool Misuse**

As  we set out to leverage this knowledge, we also discovered that it was possible to manipulate Gemini to trigger one agent to use a few tools in a single call-what we call tool chaining. This means when Gemini accesses the calendar, we are able to both inject and execute a malicious action in one shot.

![tool-misuse](https://www.safebreach.com/wp-content/uploads/2025/08/Invitation-13.webp)

We began by sending a malicious calendar invitation to the victim’s calendar. When the user asked Gemini to read their events for the week, Gemini accessed the calendar, and we silently poisoned it with an indirect prompt injection hidden in the event title. Then, this indirect prompt injection instructed Gemini to perform a malicious action, like deleting an event from the victim’s calendar. From that moment on, Gemini would delete a random calendar event every time it interacted with the user.

[Watch Demo](https://youtu.be/CUPMno-6Vk0)

### **Automatic Agent Invocation Attacks**

We now understood how we could affect the Google Calendar agent through which we could also inject an indirect prompt injection. We simply needed to send a malicious calendar invitation to the victim’s calendar. Gemini would then be poisoned with the indirect prompt injection, and we could instruct it to perform a malicious action on the victim’s calendar.

But what if we wanted our indirect prompt injection to cause Gemini to perform malicious actions using agents other than Google Calendar? This is what we call Automatic Agent Invocation.

![invocation-attacks](https://www.safebreach.com/wp-content/uploads/2025/08/Invitation-14.webp)

**Technique 4: Delayed Tool Invocation with Calendar**

As an example, what if we wanted to trigger Google Home to open the victim’s windows in their house from our indirect prompt injection? Unfortunately for us, it seems that Google has implemented a mitigation that prevents an activation of agents other than the original intended ones, or in other words, prevents agent-chaining.

![no-open](https://www.safebreach.com/wp-content/uploads/2025/08/Invitation-15.webp)

If you think about it, such a thing could theoretically be easily implemented. If you determine the list of agents that the user’s prompt should trigger-before you trigger them-then you know the expected agents and no other ones should be allowed.

To bypass such limitations, we thought about using a known technique called Delayed Tool Invocation (recently also leveraged by Johann Rehberger). Instead of instructing Gemini to perform our malicious operation on the different agent instantly, we instead instructed it to perform the operation only in future events after future prompts.

![prompt-injection](https://www.safebreach.com/wp-content/uploads/2025/08/Invitation-16.webp)

For example, if in the indirect prompt injection, we instructed Gemini to open the windows when the user says thanks, then when the user writes thanks, the expected agents from the original user prompt will actually be Google Home. We thought that this could maybe help us achieve our goal.

![open-window](https://www.safebreach.com/wp-content/uploads/2025/08/invitation-16.5.webp)

But in order for the Delayed Tool Invocation to work, we must have our instruction written in the chat’s history, which provides the context for the conversation. If we just asked Gemini to do something in the future from within an indirect prompt injection, but the request is not written anywhere in the chat’s history, Gemini would simply “forget” about our request, as it will not be inserted into the context.

And for this reason, Gemini’s Google Calendar agent is so special. As opposed to all the other agents, Google Calendar has a very unique view that lists events. In case the event list is longer than five events, there’s a “Show more” button.

![show-more](https://www.safebreach.com/wp-content/uploads/2025/08/Invitation-17.webp)

Fortunately for us, the events that are contained inside this “Show more” button, even if not expanded, are still added to the chat’s history and are therefore added to the context. This provided us with the ability to hide our Indirect Prompt Injection that utilizes Delayed Tool Invocation behind this very special Google Calendar view, and give our idea a try.

We again began by sending a malicious calendar invitation to the victim’s calendar. When the user asked Gemini to summarize today’s calendar events, the calendar agent presented the meetings that were on the victim’s calendar with nothing malicious visible. When the user replied “Thanks,” Gemini connected to Google Home and opened the windows in the house.

[Watch Demo](https://youtu.be/7Nasf-st1KQ)

### **Automatic App Invocation Attacks**

To o accomplish even more, we looked to another very powerful agent that Gemini supports called Android Utilities. It can control the user’s phone in multiple ways, including turning on the flashlight, setting alarms, taking screenshots, controlling media, turning the phone on and off, and even opening websites and apps.

**Technique 5: Opening Websites**

When users open websites, they really create a TCP connection with the website’s server. That means that this server knows the user’s IP addresses, which can be mapped to geographic locations and determine the districts or cities where the users are located.

![opening-website](https://www.safebreach.com/wp-content/uploads/2025/08/Invitation-18.webp)

If we could force Gemini to open a website, we would be able to discover the user’s location. We again began by sending a malicious calendar invitation to the victim’s calendar. When the user asked Gemini to summarize the day’s calendar events, the calendar agent presented the meetings that were on the victim’s calendar. When the user replied “Thanks,” Gemini connected to Chrome and opened a malicious website, meaning that the server of this website now has the user’s IP address.

[Watch Demo](https://youtu.be/B6IA9A4HnFs)

**Technique 6: Opening Apps**

Also, as previously mentioned, we were also able to use Android Utilities to open apps. But opening an app using Android Utilities just leads to the app’s home page. App Intent URIs, however, allow us to open specific scenarios/activities in different apps. There are more URI schemes than just HTTPS. You can use the Zoom scheme to open Zoom meetings, use the geo scheme to open specific locations in the default maps app, and there are many, many more, of course.

![android-utilities](https://www.safebreach.com/wp-content/uploads/2025/08/Invitation-19.webp)

However, trying to open an app intent URI with Gemini does not lead anywhere. Gemini just replies that the URL is invalid.

![open-app](https://www.safebreach.com/wp-content/uploads/2025/08/Invitation-20.webp)

What if instead of trying to open the app intent URI itself, we created an HTTPS URI that would respond with the 301 HTTP code and redirect us to the app intent URI? We were able to do that using any URL shortener service.

However, when a browser is about to open an external app, which is what happens using these app intent URIs, it asks the user to confirm that they really want to open the app. Otherwise, it would dangerously allow any website that a user visits to interact with apps on the user’s phone without any supervision.

![continue-youtube](https://www.safebreach.com/wp-content/uploads/2025/08/Invitation-21.webp)

Gemini, however, does not do that. When we open an HTTPS URI that redirects to an app using Gemini, Gemini blindly follows it and opens the URI no matter where it leads!

To take advantage of that, we again began by sending a malicious calendar invitation to the victim’s calendar. The user asked Gemini to list the day’s calendar events-Gemini listed the events and asked if there was anything else it could do. When the user replied “No” (our trigger for the Delayed Tool Invocation), Gemini then forced the victim into a Zoom meeting.

[Watch Demo](https://youtube.com/shorts/a-kzR7x5vx8)

**Technique 7: Data Exfiltration via URL**

The obvious way to continue to leverage our ability to open links would be to create a URL that is assembled dynamically and contains some information to exfiltrate after the domain name. Whatever is inserted after the domain name will be sent to the server behind this domain in an HTTP GET request.

![opening-urls](https://www.safebreach.com/wp-content/uploads/2025/08/Invitation-22.webp)

But if we try to ask Gemini to dynamically assemble a URL and open it, we get the invalid URL error again.

![url-utilities](https://www.safebreach.com/wp-content/uploads/2025/08/Invitation-23.webp)

Gemini’s developers somehow implemented a safety mechanism behind the scenes that enforces the rule that a URL will not be dynamically created and then immediately opened. But could it be that this mitigation is triggered only when the URL is attempted to be dynamically assembled and then opened at the same time? What if we dynamically assembled a URL without opening it?

It worked. We now understood that this mitigation would only be triggered if the URL was opened right after it was dynamically assembled.

![malicious-back](https://www.safebreach.com/wp-content/uploads/2025/08/Invitation-24.webp)

We  wondered if the URL was already assembled in a previous interaction, will Gemini still refuse to open it using Android Utilities? We assumed this wouldn’t be the case.

**Technique 8: Data Exfiltration via Gmail**

Next, we focused on emails because they have more interesting information to exfiltrate. We converted our indirect prompt injection to work from Gmail and tested our idea.

From the prompt injection, we asked Gemini to append a source URL each time the user asked about their emails. We described that the source URL should be assembled from a specific domain appended with information that we wanted to exfiltrate-for example, the subject of an email from a specific sender.  In addition, we asked Gemini to output text that would instruct its future self to open previous source URLs it wrote when a user wrote specific words like “thanks”, “thank you”, “great”, etc.

![data-via-email](https://www.safebreach.com/wp-content/uploads/2025/08/Invitation-25.webp)

This way, we ensure the URL is dynamically assembled with the information to exfiltrate, but we’re not asking Gemini to open it at the same time.

We began by sending the victim a malicious email with an indirect prompt injection. Our goal was to exfiltrate the subject line of another email in their inbox. When the user asked Gemini to summarize today’s emails, Gemini shared emails from the user’s inbox. When the user replied “Thanks,” a website was opened with a link that was assembled from the text of another email subject line. So, we managed to exfiltrate the intended information.

[Watch Demo](https://youtube.com/shorts/lbJU3jobtB0)

## **Threat Analysis & Risk Assessment (TARA)**

A threat analysis and risk assessment (TARA) is a process organizations use to identify, evaluate, and prioritize potential threats that could violate the CIA triad of organizational assets.

![threat-risk](https://www.safebreach.com/wp-content/uploads/2025/08/Invitation-26.webp)

### **Practicality**

A threat’s practicality is calculated as an average score of six categories:

1. Attacker’s equipment
2. Attacker’s expertise
3. Window of opportunity
4. Knowledge
5. Elapsed time
6. Target interaction

### **Outcome**

A threat’s outcome is calculated as the maximum score in four categories:

1. The damage caused to the user’s privacy
2. The financial damage caused to the user
3. The damage caused to the user’s safety
4. The operational damage caused to the user

### **TARA for LLM-Powered Assistants**

Based on the TARA methodology noted above, we calculated the practicality and outcome for the threats we demonstrated within this research.

![threat-analysis](https://www.safebreach.com/wp-content/uploads/2025/08/Invitation-27.webp)

According to our analysis, 73% of the threats posed to end users by an LLM personal assistant present a High-Critical risk. We believe this is significant enough to require swift and dedicated mitigation actions to secure end users and decrease this risk.

## **Vendor Response**

All of the researchers involved in this process are deeply committed to responsible disclosure. In line with that commitment, we notified Google of our research findings in February 2025. Google responded, and we worked with them to discuss our findings, respond to their inquiries, and provide any additional information necessary.

In June 2025, Google published [a blog](https://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html) that provided an overview of its multi-layer mitigation approach to secure Gemini against prompt injection techniques and shared the following response:

_Google_ [_acknowledges_](https://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html) _the research “Invitation Is All You Need” by Ben Nassi, Stav Cohen, and Or Yair, responsibly disclosed via our AI Vulnerability Rewards Program (VRP). The paper detailed theoretical indirect prompt injection techniques affecting LLM-powered assistants and was shared with Google in the spirit of improving user security and safety._

_In response, Google_ [_initiated_](https://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html) _a focused, high-priority effort to accelerate the mitigation of issues identified in the paper. Over the course of our work, we deployed multiple layered defenses, including: enhanced user confirmations for sensitive actions; robust URL handling with sanitization and Trust Level Policies; and advanced prompt injection detection using content classifiers. These mitigations were validated through extensive internal testing and deployed ahead to all users of the disclosure._

_We thank the researchers for their valuable contributions and constructive collaboration. Google remains committed to the security of our AI products and user safety, continuously evolving our protections in this dynamic landscape._

## **Conclusion**

This research presented a new Promptware variant—dubbed Targeted Promptware—that poses a serious security risk to LLM-powered applications like Google’s Gemini for Workspace. To help mitigate the potential impact of the vulnerabilities identified by this research, we have:

- Responsibly disclosed our research findings to Google in February 2025, as noted above.
- Shared our research openly with the broader security community here, at our [Black Hat USA](https://www.blackhat.com/us-25/briefings/schedule/#invitation-is-all-you-need-invoking-gemini-for-workspace-agents-with-a-simple-google-calendar-invite-46038) and [DEF CON 33](https://defcon.org/html/defcon-33/dc-33-speakers.html#content_60375) presentations, and in [a full white paper](https://drive.google.com/file/d/1jKY_TchSKpuCq-pwP6apNwLXd9VsQROn/view) to enable the organizations and end-users leveraging Gemini to better understand the risks associated with these vulnerabilities.

For more in-depth information about this research, please:

- Contact your customer success representative if you are a current SafeBreach customer
- [Schedule a one-on-one](https://www.safebreach.com/request-a-demo-original-attacks/) discussion with a SafeBreach expert
- Contact [Kesselring PR](mailto:leslie@kesscomm.com) for media inquiries

## **About the Researchers**

[Or Yair](https://www.linkedin.com/in/or-yair/) (@oryair1999) is a security research professional with more than seven years of experience, currently serving as the Security Research Team Lead for [SafeBreach Labs](https://www.safebreach.com/safebreach-labs/). Or started his professional career in the Israel Defense Force (IDF). His primary focus lies in vulnerabilities in Windows operating system’s components, though his past work also included research of Linux kernel components and some Android components. Or’s research is driven by innovation and a commitment to challenging conventional thinking. He enjoys contradicting assumptions and considers creativity a key skill for research. Or has already presented his vulnerability and security research discoveries internationally at conferences such as Black Hat USA, Europe, and Asia, DEF CON, SecTor, RSAC, Recon, Troopers, Sec-T, BlueHatIL, Security Fest, CONFidence, and more.

[Dr. Ben Nassi](https://www.linkedin.com/in/ben-nassi-phd-68a743115/) is a Black Hat board member (Asia and Europe), a cybersecurity expert, and a consultant. Ben specializes in AI security, side channel attacks, cyber-physical systems, and threat analysis and risk assessment. His work has been presented at top academic conferences, published in journals and Magazines, and covered by international media. Ben is a frequent speaker at Black Hat (6), RSAC (2), and DEFCON (3) events and won the 2023 Pwnie Award for the Best Crypto Attack for Video-based Cryptanalysis.

Stav Cohen is a Ph.D. student at the Technion – Israel Institute of Technology who investigates Cyber-Physical Systems (CPS) that integrate GenAI methodologies and feature Human-in-the-loop interactions, with a specific emphasis on their security and operational aspects. He conducts detailed analyses of GenAI models with the aim of identifying potential vulnerabilities and devising effective strategies to mitigate them. Additionally, he takes a proactive approach by exploring how GenAI methodologies can be utilized to improve both the security and operational efficiency of Cyber-Physical Systems.

## You Might Also Be Interested In

[![](https://www.safebreach.com/wp-content/uploads/2025/08/Win-DoS-Epidemic.png)\\
\\
Blog\\
\\
**Win-DoS Epidemic: A Crash Course in Abusing RPC for Win-DoS & Win-DDoS**\\
\\
Read More](https://www.safebreach.com/blog/win-dos-epidemic-abusing-rpc-for-dos-and-ddos/)

[![](https://www.safebreach.com/wp-content/uploads/2025/08/you-snooz-you-lose.png)\\
\\
ResearchBlog\\
\\
**You Snooze You Lose: RPC-Racer Winning RPC Endpoints Against Services**\\
\\
Read More](https://www.safebreach.com/blog/you-snooze-you-lose-winning-rpc-endpoints/)

[![](https://www.safebreach.com/wp-content/uploads/2025/01/LDAPNightmare-1.jpg)\\
\\
ResearchBlog\\
\\
**LDAPNightmare: SafeBreach Labs Publishes First Proof-of-Concept Exploit for CVE-2024-49113**\\
\\
Read More](https://www.safebreach.com/blog/ldapnightmare-safebreach-labs-publishes-first-proof-of-concept-exploit-for-cve-2024-49113/)

## Get the latest  research and news

First Name\*

Last Name\*

Company name\*

Email Address\*

- I agree to receive other communications from SafeBreach.

- I agree that SafeBreach may collect and use my personal data, for providing marketing material, in accordance with the [SafeBreach privacy policy](https://www.safebreach.com/privacy-policy/).
\*

ZoomInfo Chat
