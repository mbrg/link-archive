---
date: '2025-07-24'
description: A recent investigation reveals the emergence of the website "thaar.ir,"
  which allegedly supports a crowdfunding initiative for the assassination of former
  President Trump, linked to a fatwa issued by an Iranian cleric. Utilizing OSINT
  techniques, the identification of an individual, Hossein Abbasifar, involved in
  its creation was achieved through WordPress metadata exposure and social media cross-referencing.
  The site left WordPress API endpoints open, revealing identifiable data. This case
  underscores the importance of cyber threat intelligence and OSINT in tracking and
  mitigating digital threats, particularly from malicious actors leveraging online
  platforms for violence.
link: https://www.memeticwarfare.io/p/guest-post-that-thaar-over-there
tags:
- WordPress Security
- Digital Investigations
- OSINT
- Cyber Threat Intelligence
- Memetic Warfare
title: 'Guest Post: Hash Slinging Slasher - Memetic Warfare'
---

[![Memetic Warfare](https://substackcdn.com/image/fetch/$s_!rZ8h!,w_80,h_80,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4e1851a2-3e96-416d-85f1-a17f2513d19a_1280x1280.png)](https://www.memeticwarfare.io/)

# [![Memetic Warfare](https://substackcdn.com/image/fetch/$s_!Ezsu!,e_trim:10:white/e_trim:10:transparent/h_72,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3c8bb9dd-44a9-4277-9a5c-c3163148c634_5334x3205.png)](https://www.memeticwarfare.io/)

SubscribeSign in

![User's avatar](https://substackcdn.com/image/fetch/$s_!d2pp!,w_64,h_64,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcfa70fd6-1bdd-43e0-b651-31ebd235b535_1668x1668.png)

Discover more from Memetic Warfare

Influence & Cyber Operations, OSINT, CTI, Memes and Bad Jokes.

Over 1,000 subscribers

Subscribe

By subscribing, I agree to Substack's [Terms of Use](https://substack.com/tos), and acknowledge its [Information Collection Notice](https://substack.com/ccpa#personal-data-collected) and [Privacy Policy](https://substack.com/privacy).

Already have an account? Sign in

# Guest Post: Hash Slinging Slasher

[![Memetic Warfare's avatar](https://substackcdn.com/image/fetch/$s_!d2pp!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcfa70fd6-1bdd-43e0-b651-31ebd235b535_1668x1668.png)](https://substack.com/@memeticwarfareweekly)

[Memetic Warfare](https://substack.com/@memeticwarfareweekly)

Jul 12, 2025

3

[View comments (0)](https://www.memeticwarfare.io/p/guest-post-that-thaar-over-there/comments)

1

Share

Welcome to a special guest post of Memetic Warfare! My friend and colleague Max Lesser recently did some great investigative work at the FDD and had more details to add, so see below. Give him a follow as well on the FDD site as he always puts out great stuff.

Guest post begins below:

This Substack is reader-supported. To receive new posts and support my work, consider becoming a free or paid subscriber.

Subscribe

My name is [Max Lesser](https://www.fdd.org/team/max-lesser/). I work with Ari at the Foundation for Defense of Democracies (FDD). Today, I am sharing an investigation I worked on with one of our fantastic interns. Reach out to me or Ari if you are looking for new talent. We highly recommend her.

We first became aware of the website [thaar\[.\]ir](https://web.archive.org/web/20250708171625/https://thaar.ir/) on July 8 after our intern came across it while “doomscrolling” on Twitter monitoring for malicious Iranian activity. The site, which has seen increasing [news coverage](https://www.newsweek.com/iran-trump-fatwa-iran-40-million-2097043) over the past few days, allegedly has been crowdfunding a bounty for Trump’s assassination. It first appeared in DNS records on July 2, shortly after one of Iran’s top Shiite clerics [issued a fatwa](https://www.fdd.org/analysis/2025/06/30/iranian-grand-ayatollah-issues-fatwa-calling-for-president-trumps-murder/) for Trump’s assassination on June 29.

[![](https://substackcdn.com/image/fetch/$s_!1R1f!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa0827f60-5cbb-49fd-b8dc-33581ec019d9_1600x856.png)](https://substackcdn.com/image/fetch/$s_!1R1f!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa0827f60-5cbb-49fd-b8dc-33581ec019d9_1600x856.png)

_**Figure 1.** Thaar\[.\]ir homepage as of July 8, 2025._

We then conducted a technical investigation into the website – as well as open-source intelligence (OSINT) investigation to identify related emails and social media profiles – that uncovered a man involved in the website’s creation, Hossein Abbasifar (حسین عباسی‌فر).

[![](https://substackcdn.com/image/fetch/$s_!j2-M!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6ed77963-8d4e-4fe0-9391-0f0e14b583cd_750x750.png)](https://substackcdn.com/image/fetch/$s_!j2-M!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6ed77963-8d4e-4fe0-9391-0f0e14b583cd_750x750.png)

_**Figure 2.** Profile image for Hossein Abbasifar’s [Skype](https://web.archive.org/web/20250712134038/https://avatar.skype.com/v1/avatars/live:.cid.bcf22f6e239cb66e/public?size=l), showing him in front of photos of Islamic Republic founder and first Supreme Leader, Ruhollah Khomeini (left), and his successor, Ali Khamenei (right)._

Here’s a step-by-step overview of how we unmasked Abbasifar.

First, we observed that thaar\[.\]ir uses WordPress, an open-source content management system (CMS) used by millions of websites worldwide. Wordpress automatically creates author pages for users who publish content on a website. We then discovered a Wordpress [author page](https://web.archive.org/web/20250708185435/https://thaar.ir/author/h_abbasifar/) with the username “H\_abbasifar.”

[![](https://substackcdn.com/image/fetch/$s_!Jf19!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdcbb129f-d507-404a-bfb6-17dafcc9dbaf_1042x278.png)](https://substackcdn.com/image/fetch/$s_!Jf19!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdcbb129f-d507-404a-bfb6-17dafcc9dbaf_1042x278.png)

_**Figure 3.** WordPress author page on Thaar\[.\]ir showing username H\_abbasifar_

We searched the username “H\_abbasifar” on Google, which led to an [account on Eitaa](https://archive.ph/vgpIN), a popular Iranian messaging app, with a slightly different username, “H\_abasifar.” This profile image of this Eitaa account showed the same logo seen on thaar\[.\]ir. The account also revealed the full name of the person linked to the account, Hossein Abbasifar (حسین عباسی‌فر). The Eitaa account also links a related “cultural, artistic, and literary channel” with the username “H\_abbasifar,” which has the same spelling as the WordPress user account associated with thaar\[.\]ir.

[![](https://substackcdn.com/image/fetch/$s_!Kbta!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdda88fd5-36b5-49fb-be06-6bb52fdf5f0d_1600x973.png)](https://substackcdn.com/image/fetch/$s_!Kbta!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdda88fd5-36b5-49fb-be06-6bb52fdf5f0d_1600x973.png)

_**Figure 4.** Eitaa channel with the same logo used on thaar\[.\]ir and linking to another account with the same username (@h\_abasifar) as the exposed WordPress author page, suggesting a clear link between the platforms._

An [archived version](https://web.archive.org/web/20221020193423/https://eitaa.com/h_abasifar) of the same Eitaa channel, “H\_abasifar,” from October 20, 2022, displayed a different profile photo than the channel’s current photo.

[![](https://substackcdn.com/image/fetch/$s_!2bzN!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F111289d6-f0b8-43e6-b336-254961333b84_932x794.png)](https://substackcdn.com/image/fetch/$s_!2bzN!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F111289d6-f0b8-43e6-b336-254961333b84_932x794.png)

_**Figure 5.** Archived version of the Eitaa channel from February 18, 2022, showing a different profile photo than the channel’s current photo._

A reverse image search of this profile photo on Google surfaced the same photo on a [Clubhouse account](https://web.archive.org/web/20250709001143/https:/clubhousedb.com/user/h_abbasifar). This account lists an email, econcul@gmail\[.\]com.

[![](https://substackcdn.com/image/fetch/$s_!gCQ0!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F918f6a89-7ecf-4f2a-aa48-a2f102b32866_1472x690.png)](https://substackcdn.com/image/fetch/$s_!gCQ0!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F918f6a89-7ecf-4f2a-aa48-a2f102b32866_1472x690.png)

_**Figure 6-7 .** Clubhouse account associated with @H\_ABBASIFAR, which reveals a personal email address_

We then connected this email to thaar\[.\]ir, confirming Abbasifar’s involvement in the website.

As mentioned above, thaar\[.\]ir uses WordPress. WordPress includes a REST API that allows various applications—like SEO tools, site analytics platforms, mobile apps, and custom front ends—to interact with the website. Although this API can be [fully or partially disabled](https://www.getastra.com/blog/cms/disable-wp-api-json-in-wp/), or limited to [specific endpoints](https://wordpress.stackexchange.com/questions/228585/hiding-wordpress-rest-api-v2-endpoints-from-public-viewing), many developers leave it publicly accessible unless configured otherwise. Thaar\[.\]ir left an [endpoint exposed](https://archive.ph/g9sjO), thaar\[.\]ir/wp-json/wp/v2/users/2, which reveals metadata associated with the WordPress author “H\_abbasifar.”

[![](https://substackcdn.com/image/fetch/$s_!Aw3u!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F71575681-786d-4d76-b697-a3025fdffa25_1226x650.jpeg)](https://substackcdn.com/image/fetch/$s_!Aw3u!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F71575681-786d-4d76-b697-a3025fdffa25_1226x650.jpeg)

_**Figure 8.** Exposed WordPress API endpoint for the H\_abbasifar user page on thaar\[.\]ir, revealing a Gravatar URL containing the SHA-256 hash of the associated email address._

This exposed endpoint reveals a link to the author’s Gravatar profile, an image service that associates a globally recognized avatar with a user’s email address. Gravatar images can automatically appear across platforms such as WordPress, Slack, and GitHub.

Gravatar generates a [hash](https://docs.gravatar.com/rest/hash/) from a user’s email address, which is embedded in the URL associated with their profile. This allows platforms to retrieve the user’s avatar without directly exposing the email itself. Gravatar now [recommends](https://github.com/FusionAuth/fusionauth-issues/issues/2856) using SHA-256 hashing for added security, replacing the less secure MD5 hashes previously used.

The exposed endpoint, thaar\[.\]ir/wp-json/wp/v2/users/2, reveals the Gravatar URL associated with the WordPress user “H\_abbasifar.” The URL contains the SHA-256 hash

9f1fcc3cd7af925c34e316e948bae92d9839c687f465616dd9b11fa6b40c31e8.

While SHA-256 hashes are not easily reversible, they can be “cracked” by generating hashes of likely email addresses and comparing them against the exposed hash. In this case, we hypothesized that the WordPress user “H\_abbasifar” may have used the email econcul@gmail\[.\]com, which is linked to Hossein Abbasifar. Applying the SHA-256 algorithm to this email produced a hash identical to the one in the Gravatar URL, reinforcing the attribution of Abbasifar’s involvement with the website.

[![](https://substackcdn.com/image/fetch/$s_!EG-_!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8b01c717-d895-455d-83ca-32860eeb46b2_1600x1018.png)](https://substackcdn.com/image/fetch/$s_!EG-_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8b01c717-d895-455d-83ca-32860eeb46b2_1600x1018.png)

_**Figure 9.** Hash value generated from the econcul@gmail\[.\]com email input, which matches the SHA-256 hash listed in the metadata under the Gravatar URL_

We then attempted to find as much information as we could about Hossein Abbasifar, to determine whether he had any official ties to the Iranian regime. Running searches on Google and the online investigation tool [OSINT Industries](https://www.osint.industries/) for his email, econcul@gmail\[.\]com, as well as his usernames, “h\_abbasifar” and “h\_abasifar,” surfaced many significant results. These include accounts across [Telegram](https://archive.ph/RZtxd), [Skype](https://archive.ph/4Dwbu), western social media sites like [X](https://archive.ph/6h0Cz) and [Instagram](https://archive.ph/Ln13O), and Iranian sites such as [Aparat](https://archive.ph/9ta2Z), a video sharing platform, and [Virasty](https://archive.ph/BKWi3), an Iranian X knockoff. Notably, Abbasifar’s LinkedIn account lists his location in New Jersey, potentially providing him a vehicle to pose as a U.S.-based person and approach Americans.

[![](https://substackcdn.com/image/fetch/$s_!91Gd!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2e14e01e-84ee-4337-b284-4e7653bacd7e_1567x387.png)](https://substackcdn.com/image/fetch/$s_!91Gd!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2e14e01e-84ee-4337-b284-4e7653bacd7e_1567x387.png)

_**Figure 10.** OSINT Industries results for h\_abasifar as of July 11, 2025._

[![](https://substackcdn.com/image/fetch/$s_!4YkA!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc52b6434-3719-48a3-bc2f-15fd54ce6cd1_1044x220.png)](https://substackcdn.com/image/fetch/$s_!4YkA!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc52b6434-3719-48a3-bc2f-15fd54ce6cd1_1044x220.png)

_**Figure 11.** OSINT Industries results for “h\_abbasifar” as of June 11, 2025._

[![](https://substackcdn.com/image/fetch/$s_!pKpg!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3872c00b-09e9-4945-86c5-47c787886ff9_489x239.png)](https://substackcdn.com/image/fetch/$s_!pKpg!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3872c00b-09e9-4945-86c5-47c787886ff9_489x239.png)

_**Figure 12.** Data associated with Abbasifar’s LinkedIn account, as per OSINT Industries search on July 11 2025._

We also queried Abbasifar’s email using Dehashed, a tool that allows investigators to search data breaches. This search surfaced account details from the 2024 breach of Cutout\[.\]pro, an AI-powered photo editing and content generation platform. The leaked account included the IP address 5\[.\]112.76.118, which is [registered](https://whatismyipaddress.com/ip/5.112.76.118) to an Iranian cellular provider. This supports the assessment that Abbasifar was operating from inside Iran as recently as 2024.

[![](https://substackcdn.com/image/fetch/$s_!xAoN!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1f623d8e-a14e-425d-8844-5fe236a8a90e_958x295.png)](https://substackcdn.com/image/fetch/$s_!xAoN!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1f623d8e-a14e-425d-8844-5fe236a8a90e_958x295.png)

_**Figure 12.** Dehashed result showing breach data associated with econcul@gmail\[.\]com, including an Iranian IP address associated with his Cutout\[.\]pro account._

We eventually discovered that Abbasifar at one point claimed to have worked for Islamic Republic of Iran Broadcasting (IRIB), the regime’s main propaganda network. Abassifar’s [Clubhouse account](https://web.archive.org/web/20250709001143/https:/clubhousedb.com/user/h_abbasifar), mentioned earlier, states that he directs an institution called the Seda Media School, and provides a link, heyat\[.\]school/seda, which is now broken. An [archived version](https://web.archive.org/web/20210724134600/https://heyat.school/seda) of the link from 2021 shows what appears to be a school dedicated to teaching students how to produce and publish audio content including podcasts and radio shows. The site displays lessons taught by “Professor Abbasifar,” which then led us to a 2021 [teacher profile](https://web.archive.org/web/20210928172738/https://heyat.school/component/joomdle/teacher/abbasifar?Itemid=164) for Abbasifar. On this profile, Abbasifar claims that he serves as a specialist at the [IRIB’s radio station](https://web.archive.org/web/20250710040632/https:/radio.iranseda.ir/radiolist/?VALID=TRUE) (صدای جمهوری اسلامی ایران), and that he produces the [IRIB program](https://www.radiofarda.com/a/hacking-iranian-state-television/31674296.html) Radio Javan.

[![](https://substackcdn.com/image/fetch/$s_!DhLW!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff7893858-d72b-4c87-8a5c-8ac74f95ce19_425x733.png)](https://substackcdn.com/image/fetch/$s_!DhLW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff7893858-d72b-4c87-8a5c-8ac74f95ce19_425x733.png)

_**Figure 12.** Archived copy from September 28, 2021 of Abbasfiar’s teacher profile associated with the Seda School, claiming that Abbasifar works for the IRIB._

As of July 12, 2025, Abbasifar’s campaign continues unabated. Recently he has posted on his Eitaa account encouraging more people to donate to his campaign, which he refers to as Blood Pledge (عهد خون). He also shared a photo of deceased Hezbollah chief [Imad Mughniyeh](https://www.theguardian.com/world/2008/feb/14/israelandthepalestinians.lebanon) accompanied by Arabic text calling for the complete destruction of Israel.

[![](https://substackcdn.com/image/fetch/$s_!Lc-1!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F842348cd-3e54-4ae5-99fb-ed0c96acc197_1294x1248.png)](https://substackcdn.com/image/fetch/$s_!Lc-1!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F842348cd-3e54-4ae5-99fb-ed0c96acc197_1294x1248.png)

_**Figure 13-14.** Translated [posts](https://archive.ph/M3rS2) from associated Eitaa channel (@h\_abasifar) [promoting](https://archive.ph/LQxBC) the campaign._

A quick search using Sprout Social’s social listening tools shows that the related hashtag (#عهد\_خون) peaked at approximately 800 posts on X just days after the creation of thaar\[.\]ir. This suggests that Abbasifar’s mobilization campaign briefly gained traction and achieved limited success in circulating on at least one Western social media platform.

[![](https://substackcdn.com/image/fetch/$s_!11dX!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0a248bab-cc30-4e69-b364-551eccf50609_1582x894.jpeg)](https://substackcdn.com/image/fetch/$s_!11dX!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0a248bab-cc30-4e69-b364-551eccf50609_1582x894.jpeg)

_**Figure 15.** A Sprout Social snapshot showing trends in the volume of posts containing the hashtag #عهد\_خون on X between June 10 and July 10 2025._

This investigative overview demonstrates how a combination of cyber threat intelligence (CTI) and OSINT can be used to identify malicious actors, including those seeking to mobilize violence through digital platforms. If you have any questions, feel free to contact Ari, who can connect you with me directly.

This Substack is reader-supported. To receive new posts and support my work, consider becoming a free or paid subscriber.

Subscribe

[![David's avatar](https://substackcdn.com/image/fetch/$s_!3j_W!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Faf3f17b6-8ad2-4856-b789-148f431917bd_144x144.png)](https://substack.com/profile/60114297-david)

3 Likes∙

[1 Restack](https://substack.com/note/p-168148988/restacks?utm_source=substack&utm_content=facepile-restacks)

3

[View comments (0)](https://www.memeticwarfare.io/p/guest-post-that-thaar-over-there/comments)

1

Share

PreviousNext

#### Discussion about this post

CommentsRestacks

![User's avatar](https://substackcdn.com/image/fetch/$s_!TnFC!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Favatars%2Fdefault-light.png)

TopLatestDiscussions

[This Report Goes to 11](https://www.memeticwarfare.io/p/this-report-goes-to-11)

[Welcome to Memetic Warfare.](https://www.memeticwarfare.io/p/this-report-goes-to-11)

Feb 4•
[Memetic Warfare](https://substack.com/@memeticwarfareweekly)

9

[2](https://www.memeticwarfare.io/p/this-report-goes-to-11/comments)

![](https://substackcdn.com/image/fetch/$s_!-JCK!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_center/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff75fbb4d-4ea0-4698-bcf8-ad15f5285ed8_1029x1291.png)

[Insane in the Meme-Brane](https://www.memeticwarfare.io/p/insane-in-the-meme-brane)

[Welcome to Memetic Warfare.](https://www.memeticwarfare.io/p/insane-in-the-meme-brane)

Jun 17, 2024•
[Memetic Warfare](https://substack.com/@memeticwarfareweekly)

12

[View comments (0)](https://www.memeticwarfare.io/p/insane-in-the-meme-brane/comments)

![](https://substackcdn.com/image/fetch/$s_!D4hN!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_center/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb4795589-2248-463f-80e9-43abdf804654_500x750.jpeg)

[Habemus Viginum](https://www.memeticwarfare.io/p/habemus-viginum)

[Welcome to Memetic Warfare.](https://www.memeticwarfare.io/p/habemus-viginum)

May 12•
[Memetic Warfare](https://substack.com/@memeticwarfareweekly)

6

[View comments (0)](https://www.memeticwarfare.io/p/habemus-viginum/comments)

![](https://substackcdn.com/image/fetch/$s_!UwBX!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_center/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F81861353-805e-4fd0-8252-7f38b8942b34_1124x675.png)

See all

Ready for more?

Subscribe
