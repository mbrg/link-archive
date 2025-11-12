---
date: '2025-11-12'
description: In his humorous recount of battling raccoons in coastal California, Alex
  Smolen highlights critical security lessons relevant to both home defense and cybersecurity.
  He emphasizes the ineffectiveness of basic deterrents against advanced threats,
  akin to outdated security measures failing to protect against sophisticated attacks.
  Excessive alerting results in "alert fatigue," detracting from actual response capability.
  Innovative solutions, like integrating motion sensors with a creative deterrent
  (air dancers), showcase the necessity of tailored defensive strategies. Ultimately,
  he underscores that removing the incentive for threats—using nematodes to eliminate
  grubs—is a foundational approach that parallels cybersecurity best practices.
link: https://engseclabs.com/blog/raccoon-diaries/
tags:
- Home Automation
- Urban Wildlife Management
- Smart Home Technology
- Security Best Practices
- Pest Control
title: 'Backyard APT: A Raccoon Story - EngSec Labs'
---

Living in urban coastal California means you’re never far from an APT: an Advanced Persistent Trashpanda. Cute, yes. Harmless? Not even close. In my battle against backyard raccoons, I learned some things about security. I learned some things about myself. I learned some things about MCP servers and microscopic nematodes. Allow me to tell you my story.

![Raccon](https://engseclabs.com/assets/images/raccoon/raccoon.png)

_I Can Haz Grub?_

Every fall, we’d observe their nocturnal wanderings through our little grass patch of a backyard. Sometimes they’d bring the whole family on their explorations - furry assorted-size blobs clambering over the fence. The raccoons began to wear out their welcome, though, when they started “rolling the grass” - tearing up big chunks of lawn to (as I learned from our gardener) look for grubs growing beneath the sod until their emergence as mature bugs. This foraging made our lawn an eyesore and muddy mess.

![Grass](https://engseclabs.com/assets/images/raccoon/grass.jpg)

_Looking for grubs in all the wrong places_

Muddy lawns made me grumpy, but hardly battle-ready. That changed the night our beloved chihuahua Jolene darted out between my legs through a cracked-open back door to “sweep the perimeter” - part of her canine rituals. Perhaps she had sensed the family of raccoons perusing the yard at that moment. Once she spotted them, she immediately gave chase. The largest raccoon broke towards her and began a fierce attack as Jolene yelped in fear and pain.

Panicking, I leapt off the deck onto the lawn and gave chase. The raccoon had Jo and was heading under the patio. I bent down, snatched Jo from its clutches, and issued a stern Birkenstock-ed kick to the intruder.

Your browser doesn't support embedded videos.

_The fateful encounter_

As I carried Jo back inside, the raccoon followed me, glaring at us from the back door as if to continue the altercation. My inner Jersey Shore came out as I raged - “you wanna go bro?” - but my wife wisely encouraged me to keep the door shut and alerted me to Jo’s wound: a bite mark opened on her belly. We spent that night at an emergency vet (waiting in our car, as was the style in those COVID-era times) before Jojo returned to us, stitched up, rabies-inoculated, and more than a little terrified by her assault.

I’m generally a peacenik, but I was stirred with a revenge-fueled craving for justice. First you come for my lawn, then you come for my dog? I made it a goal - a mission, a blood pact, even - to keep these pests out of my backyard. As a security thought leader, I first wanted to evaluate the effectiveness of my defenses. So I put out a camera to see the action.

![Jo](https://engseclabs.com/assets/images/raccoon/jo.jpg)

_Jo investigating the surveillance system_

## Security Lesson \#1: You Can’t Stop Advanced Threats with Basic Defense

I searched Amazon for “raccoon deterrent” and purchased a few different ultrasonic/flashing light yard stakes. Well, if you’re in my shoes in the future, let me save you a few dollars and suggest you skip these devices. he raccoons looked at my fancy deterrents and kept right on digging. Much like deploying a flashy new security product without tuning, my defenses looked good on paper and did nothing in the field. Maybe these things work for rural raccoons unaccustomed to strange noises and signs of humans, but my backyard baby bug burglars were entirely nonplussed.

![Motion detector](https://engseclabs.com/assets/images/raccoon/motion.png)

_Ornamental e-waste_

## Security Lesson \#2: Too Many False Positives Spoil the Detection

My next defensive strategy: spray them with water. I bought a motion-activated sprinkler to soak their spirits. I did get a few good direct shots. But more than once, I took out the trash and forgot to disarm, activating the system and soaking myself - a serious case of “alert fatigue”.

![Motion-activated sprinkler](https://engseclabs.com/assets/images/raccoon/sprinkler.png)

_My petard on which I was hoist_

I also found water just wasn’t a big deal to these raccoons. I’d see them outside and accost them with a hose and spray nozzle: full blast, point blank. They would give no ground, just stare at me with their glowing eyes from the tree branches.

I commiserated with neighbors, consulted message boards, and talked with friends. A buddy whose family grew up on a farm suggested cages to trap the raccoons. “Well what do you do then?”, I asked. “Well,” he said, “my dad was a bit of a softie and would take them somewhere far away and release them. My mom, though, she would go get the gun and…” I blanched at the notion of dispatching anything more sentient than a housefly, so blowing a raccoon’s brains out was a hard no. Also, the idea of Ubering raccoon after raccoon from Oakland to Vacaville didn’t seem like a sustainable strategy.

## Security Lesson \#3: Custom Code to Wire Defensive Controls Together is a Superpower

I’d set up Home Assistant and been tinkering with a few different motion sensors and smart switches. That’s when I got an idea - what if I connected something that moved to my own motion sensor? This would also let me build increasingly sophisticated detection and response flows.

My first challenge: what could I plug in outdoors that would move around and be threatening to a raccoon? Of course - those wild wacky inflatable arm guys! It’s basically just a fan and a sock with both ends open. I had to solve two problems. One was figuring out the right search term to buy one (“air dancer”), and the second was finding a supplier that had the right size - “scare a backyard raccoon”-size rather than “pay attention to my used car lot from the freeway”-size.

![Air dancer](https://engseclabs.com/assets/images/raccoon/airdancer.png)

_Like a scarecrow, but make it wacky_

After building a few automations to wire the motion sensor to the plug (plus some patio lights) and turn the whole formula on only at night, I watched in glee as raccoons startled at the initial whir of the fan and then retreated from the wacky air dancing.

While I thought my problem was solved, a new wrinkle emerged. While the raccoons had made the “flight” decision, another backyard visitor was provoked to aggression - the normally placid possum. Reviewing my video audit log footage one night, I was shocked to see a possum react to my air dancer not with deference, but instead grab the flapping sock in its mouth and carry it off to somewhere I never found it.

Your browser doesn't support embedded videos.

_Fearless possum claiming its prize_

Supposing this may have been a one-time act of bravery, I replaced the lost investment and purchased a spooky ghost version that I believe will intimidate even the most resolute possum.

Your browser doesn't support embedded videos.

_The ghost air dancer - surely possum-proof_

Through all of this, I’ve been using Home Assistant to power my surveillance and wildlife PsyOps architecture. In this AI era, I’ve started using Claude Code and the Home Assistant MCP server to make some sick dashboards.

![Dashabord](https://engseclabs.com/assets/images/raccoon/dashboard.png)

_Vibe coding and the vibe is - raccoons begone!_

## Security Lesson \#4: Remove the Attacker Incentives

Despite my creativity in keeping these garden grub guzzlers at bay, I’d still wander out some mornings to find a corner of lawn beyond sensor distance torn up. This is where I discovered the most effective element of my defensive system. In a line of thinking that has deep profundity for all security endeavors, I realized the best defense isn’t higher fences. It’s changing what makes the target appealing in the first place. That’s true for raccoons and ransomware alike.

Toxic pesticides may have worked, but I didn’t want to poison my poor beset small dog. Instead, I identified glorious nematodes - microscopic organisms that feed on grubs and can be bought by the millions, mixed with water, and sprayed on the lawn.

![Nematode](https://engseclabs.com/assets/images/raccoon/nematodes.png)

_Microscopic, macro-effective_

With these latest technological advantages, I believe I’ve won the cat and mouse game - or rather, the raccoon and person game - at least for now. And though there have been costs to my lawn’s integrity, my dog’s safety, and my sanity, I gained valuable security insights which I share with you. Good luck out there, whether your APTs wear hoodies or fur coats.

* * *

Backyard APT: A Raccoon Story \| Alex Smolen

[![View profile for Alex Smolen](https://media.licdn.com/dms/image/v2/D5603AQH_gt7nMYQG0w/profile-displayphoto-shrink_400_400/B56ZRcaqNXHQAg-/0/1736717280437?e=2147483647&v=beta&t=QFknyJH5O43D-BUnmauHaLRBZxVb2EKj4aGGF9YCUmM)](https://www.linkedin.com/in/alex-smolen-8a59a31?trk=public_post_embed_feed-actor-image)

[Alex Smolen](https://www.linkedin.com/in/alex-smolen-8a59a31?trk=public_post_embed_feed-actor-name)

Security, Engineering, Leadership




































1d


[LinkedIn](https://www.linkedin.com/feed/?trk=public_post_embed_linkedin-logo-image)

I attended an AI Security Leaders dinner a couple of weeks ago where we were asked "what's the coolest thing you've done with AI recently?"

After sharing my story, I was encouraged to write it up as a blog post - so, here it is.

[https://lnkd.in/gH-vRZeB](https://lnkd.in/gH-vRZeB)

…more


[![Backyard APT: A Raccoon Story](https://media.licdn.com/dms/image/sync/v2/D5627AQEmV2iG7qCNXg/articleshare-shrink_1280_800/B56ZpvOEDpHkAQ-/0/1762802549685?e=2147483647&v=beta&t=J28-MuD2wux1ATxuT-YAwzdrRk9gaxEmldeSu2uX3n4)](https://engseclabs.com/blog/raccoon-diaries/)

````

[![](https://static.licdn.com/aero-v1/sc/h/bn39hirwzjqj18ej1fkz55671)![](https://static.licdn.com/aero-v1/sc/h/22ifp2etz8kb9tgjqn65s9ics)![](https://static.licdn.com/aero-v1/sc/h/2tzoeodxy0zug4455msr0oq0v)\\
36](https://www.linkedin.com/feed/update/urn:li:activity:7393730689185222656?trk=public_post_embed_social-actions-reactions)`````````````` [7 Comments](https://www.linkedin.com/feed/update/urn:li:activity:7393730689185222656?trk=public_post_embed_social-actions-comments)

[Like](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Ffeed%2Fupdate%2Furn%3Ali%3Aactivity%3A7393730689185222656&trk=public_post_embed_like-cta) [Comment](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Ffeed%2Fupdate%2Furn%3Ali%3Aactivity%3A7393730689185222656&trk=public_post_embed_comment-cta)

Share


_Sharing the raccoon saga on LinkedIn_

[Back to Blog](https://engseclabs.com/blog/)
