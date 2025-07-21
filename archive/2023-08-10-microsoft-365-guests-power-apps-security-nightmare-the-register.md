---
date: 2023-08-10
description: In a recent Black Hat presentation, Michael Bargury unveiled vulnerabilities
  in Microsoft 365's guest accounts, exposing potential exploits in Power Apps. Guest
  accounts can circumvent restrictions using trial licenses, enabling attackers to
  access and manipulate internal applications and databases, including sensitive data.
  Bargury demonstrated his tool, Powerpwn, which accesses Azure SQL databases, highlighting
  user negligence in access management and credential embedding as critical risk factors.
  While Microsoft is addressing these gaps, organizations must enforce stricter access
  controls to mitigate risks associated with low-code platforms. Effective governance
  is essential to safeguard internal data against guest account misuse.
link: https://www.theregister.com/2023/08/10/microsoft_365_guest_accounts_power/
tags:
- Power Apps
- Microsoft 365
- Cybersecurity
- Guest Accounts
- Data Loss Prevention
title: Microsoft 365 guests + Power Apps = security nightmare • The Register
---

[![](https://www.theregister.com/design_picker/ae01b183a707a7db8cd5f2c947715ed56d335138/graphics/std/user_icon_white_extents_16x16.png)![](https://www.theregister.com/design_picker/ae01b183a707a7db8cd5f2c947715ed56d335138/graphics/std/user_icon_white_filled_extents_16x16.png)Sign in / up](https://account.theregister.com/login?r=https%3A//www.theregister.com/2023/08/10/microsoft_365_guest_accounts_power/ "Sign in / up")

[The Register](https://www.theregister.com/)

[![](https://www.theregister.com/design_picker/ae01b183a707a7db8cd5f2c947715ed56d335138/graphics/std/magnifying_glass_white_extents_16x16.png)](https://search.theregister.com/)

![](https://www.theregister.com/design_picker/ae01b183a707a7db8cd5f2c947715ed56d335138/graphics/icon/burger_menu_white_16x16.png)![](https://www.theregister.com/design_picker/ae01b183a707a7db8cd5f2c947715ed56d335138/graphics/icon/burger_menu_white_close_16x16.png)

## Topics

[Special Features](https://www.theregister.com/2023/08/10/microsoft_365_guest_accounts_power/#subnav-box-nav-special_features)

## Special Features

## Vendor Voice

[Resources](https://www.theregister.com/2023/08/10/microsoft_365_guest_accounts_power/#subnav-box-nav-resources)

## Resources

#### [Black Hat and DEF CON](https://www.theregister.com/special_features/blackhat_and_defcon/)

[**5**![comment bubble on white](https://www.theregister.com/design_picker/f5daacc84b9722c1e31ba85f836c37e4ad993fc4/graphics/icons/bubble_comment_white.png)](https://forums.theregister.com/forum/all/2023/08/10/microsoft_365_guest_accounts_power/ "View comments on this article")

This article is more than **1 year old**

# Microsoft 365 guest accounts + Power Apps = security nightmare

[**5**![comment bubble on white](https://www.theregister.com/design_picker/f5daacc84b9722c1e31ba85f836c37e4ad993fc4/graphics/icons/bubble_comment_white.png)](https://forums.theregister.com/forum/all/2023/08/10/microsoft_365_guest_accounts_power/ "View comments on this article")

## A login, a PA trial license, and some good old hacking are all that's needed to nab SQL databases

![icon](https://www.theregister.com/design_picker/d518b499f8a6e2c65d4d8c49aca8299d54b03012/graphics/icon/vulture_red.svg)[Brandon Vigliarolo](https://www.theregister.com/Author/Brandon-Vigliarolo "Read more by this author")

Thu 10 Aug 2023  //
18:30 UTC

![](https://www.theregister.com/design_picker/d2e337b97204af4aa34dda04c4e5d56d954b216f/graphics/icons/social_share_icon.svg)

Black Hat Microsoft 365 guest accounts aren't nearly as secure as Redmond would lead customers to believe, as low-code security expert Michael Bargury demonstrated at Black Hat.

Guest accounts are commonly used by Microsoft shops to give non-employees access to their 365 tenancy with limited permissions, usually just access to a Teams channel and Sharepoint. There are a few [other things](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/about-guest-users?view=o365-worldwide) that guest accounts can get into to, however, and it's Power Apps, Microsoft's low-code platform, where problems can bubble.

Guest accounts, by default, don't have Power Apps licenses assigned to them, but there's an easy way around this, Bargury said during the [Black Hat](https://www.theregister.com/special_features/blackhat_and_defcon) talk, " [All You Need is Guest](https://www.blackhat.com/us-23/briefings/schedule/index.html#all-you-need-is-guest-32647)": Power Apps trial licenses.

Armed with a compromised or obtained guest account and a Power Apps trial license (available free to anyone who wants one from the Power Apps [website](https://powerapps.microsoft.com/en-us/)), all an attacker needs to do is log in to Power Apps and switch directories to the target tenant they're a guest user on, and _voila_: they can see a list of all the Power Apps connections their account has access to, and can even create applications inside the tenant. With enough work, the attacker can potentially make off with gobs of internal data.

"But wait," you may be thinking at this point, "that shouldn't matter if a company is practicing good access management." That would be true, but it's here that Bargury's experience as co-founder and CTO of Zenity, a [low-code/no-code](https://www.zenity.io/) security and governance startup, comes into play: he says many companies aren't.

While Microsoft shares some responsibility for allowing Power Apps trial users to gain access to – and create – apps in guest tenancies without appropriate controls, "business users are building things in Power Apps and not properly restricting access," Bargury said.

Bargury added that many organizations embed credentials into Power Apps to make them easier for various employees to use, and argued many business users who create apps don't understand the implications of simply sharing them across a whole organization - which includes guest accounts - instead of being granular in granting access.

"It's important to note that all of this is made possible by user mistakes," Bargury told us.

If you have Power Apps in your infrastructure, double check what guests can access.

### From trial license to data breach

All of what Bargury demonstrated in the first bit of his talk was relatively straightforward: the attacker gets access to a guest account on the target Microsoft 365 tenant, snags a Power Apps trial license, and hopes that the Power Apps users in their target tenant have provided access to some juicy internal apps.

It's here that Microsoft's default [data loss prevention policies](https://www.microsoft.com/en-us/security/business/security-101/what-is-data-loss-prevention-dlp) (DLP) come into play: they block connectors in existing apps from being accessed by 365 trial accounts. As mentioned above, however, guest accounts on a trial license can create their own Power Apps, and with some clever API manipulation can essentially side-step DLP policies, we're told, to go right to the source: the connectors themselves, which are all too willing to dump any and all data contained in the databases they're linked to.

- [Those low-code tools devs love so much? They'll grow 20% in 2023, says Gartner](https://www.theregister.com/2022/12/13/lowcode_tools_2023_rise/)
- [Meet TeamT5, the Taiwanese infosec outfit taking on Beijing and defeating its smears](https://www.theregister.com/2023/06/05/teamt5_taiwan_threat_intelligence/)
- [Scribble to app: Microsoft's Power Apps VP talks us through 'Express design'](https://www.theregister.com/2022/06/01/power_apps_express_design/)
- [TETRA radio comms used by emergency heroes easily cracked, say experts](https://www.theregister.com/2023/07/24/tetra_radio_security_flaws/)

During his talk, Bargury demonstrated the use of a tool he built called [Powerpwn](https://github.com/mbrg/power-pwn) that was able to gain access to, and dump data from, all sorts of Azure and SQL databases used by Power Apps, including a test database that contained customer information like social security numbers.

### Permission: Impossible – or at least less likely, please

Bargury told us Microsoft has been a strong and willing collaborator in addressing the weaknesses he discovered, and that the Azure titan is working on a patch for the Power Apps DLP bypasses that he discovered, in addition to working to prevent guest accounts from creating Power Apps apps as well.

As for Power Apps users, it's time to start cutting down on those doling out organization-wide access to internal apps, regardless of what Microsoft fixes or doesn't. It also might not be a bad idea to start requiring users to sign in to individual Power Apps, or at least not embedding shared credentials into apps the entire company can use.

Along with his talk, Bargury [provided](https://github.com/mbrg/bhusa23) sample code, additional details, and code to help companies determine if such vulnerabilities exist in their own environments. ®

[Sponsored: Is your password ecosystem ready for the regulators?](https://go.theregister.com/tl/3211/shttps://www.theregister.com/2025/07/08/password_ecosystem_regulators/)

![](https://www.theregister.com/design_picker/d2e337b97204af4aa34dda04c4e5d56d954b216f/graphics/icons/social_share_icon.svg)Share

#### More about

- [Black Hat](https://www.theregister.com/Tag/Black%20Hat/)
- [Cybersecurity](https://www.theregister.com/Tag/Cybersecurity/)
- [Low code](https://www.theregister.com/Tag/Low%20code/)

More like these

×

### More about

- [Black Hat](https://www.theregister.com/Tag/Black%20Hat/)
- [Cybersecurity](https://www.theregister.com/Tag/Cybersecurity/)
- [Low code](https://www.theregister.com/Tag/Low%20code/)
- [Microsoft 365](https://www.theregister.com/Tag/Microsoft%20365/)

### Narrower topics

- [Black Hat Asia](https://www.theregister.com/Tag/Black%20Hat%20Asia/)
- [Microsoft Teams](https://www.theregister.com/Tag/Microsoft%20Teams/)
- [RSA Conference](https://www.theregister.com/Tag/RSA%20Conference/)

### Broader topics

- [Microsoft](https://www.theregister.com/Tag/Microsoft/)
- [Office 365](https://www.theregister.com/Tag/Office%20365/)
- [Programming](https://www.theregister.com/Tag/Programming/)
- [Security](https://www.theregister.com/Tag/Security/)
- [Software](https://www.theregister.com/Tag/Software/)

#### More about

![](https://www.theregister.com/design_picker/d2e337b97204af4aa34dda04c4e5d56d954b216f/graphics/icons/social_share_icon.svg)Share

[**5**![comment bubble on white](https://www.theregister.com/design_picker/f5daacc84b9722c1e31ba85f836c37e4ad993fc4/graphics/icons/bubble_comment_white.png)\\
COMMENTS](https://forums.theregister.com/forum/all/2023/08/10/microsoft_365_guest_accounts_power/ "View comments on this article")

#### More about

- [Black Hat](https://www.theregister.com/Tag/Black%20Hat/)
- [Cybersecurity](https://www.theregister.com/Tag/Cybersecurity/)
- [Low code](https://www.theregister.com/Tag/Low%20code/)

More like these

×

### More about

- [Black Hat](https://www.theregister.com/Tag/Black%20Hat/)
- [Cybersecurity](https://www.theregister.com/Tag/Cybersecurity/)
- [Low code](https://www.theregister.com/Tag/Low%20code/)
- [Microsoft 365](https://www.theregister.com/Tag/Microsoft%20365/)

### Narrower topics

- [Black Hat Asia](https://www.theregister.com/Tag/Black%20Hat%20Asia/)
- [Microsoft Teams](https://www.theregister.com/Tag/Microsoft%20Teams/)
- [RSA Conference](https://www.theregister.com/Tag/RSA%20Conference/)

### Broader topics

- [Microsoft](https://www.theregister.com/Tag/Microsoft/)
- [Office 365](https://www.theregister.com/Tag/Office%20365/)
- [Programming](https://www.theregister.com/Tag/Programming/)
- [Security](https://www.theregister.com/Tag/Security/)
- [Software](https://www.theregister.com/Tag/Software/)

#### TIP US OFF

[Send us news](https://www.theregister.com/Profile/contact/)

* * *

### Other stories you might like

[![](https://regmedia.co.uk/2022/03/18/shutterstock_digitalrussia.jpg?x=150&y=100&crop=1)\\
\\
**Russia, hotbed of cybercrime, says nyet to ethical hacking bill** \\
\\
Politicians uneasy over potential impact on national security, local reports say\\
\\
Security11 days \| 4](https://www.theregister.com/2025/07/10/russia_ethical_hacking_bill/?td=keepreading)[![](https://regmedia.co.uk/2023/05/24/cloud_shutterstock.jpg?x=150&y=100&crop=1)\\
\\
**EU cloud gang wins Microsoft concessions, but fair software licensing group brands them 'stalling tactic'**\\
\\
Updated Pay-as-you-go model, privacy protections agreed – but critics say it just buys 'Microsoft more time to lock in customers'\\
\\
PaaS + IaaS3 days \|](https://www.theregister.com/2025/07/18/cispe_microsoft_concessions/?td=keepreading)[![](https://regmedia.co.uk/2019/04/16/shutterstock_train.jpg?x=150&y=100&crop=1)\\
\\
**A software-defined radio can derail a US train by slamming the brakes on remotely**\\
\\
Updated Neil Smith has been trying to get the railroad industry to listen since 2012, but it took a CISA warning to get there\\
\\
Security7 days \| 74](https://www.theregister.com/2025/07/14/train_brakes_flaw/?td=keepreading)[![](https://regmedia.co.uk/2017/05/26/lenovo_web_page_shutterstock.jpg?x=150&y=100&crop=1)\\
\\
**AI and virtualization are two major headaches for CIOs. Can storage help solve them both?** \\
\\
It's about evolution not revolution, says Lenovo\\
\\
Sponsored feature](https://www.theregister.com/2025/05/22/lenovo_ai_virtualization_headaches/?td=keepreading)

[![](https://regmedia.co.uk/2023/10/24/police_shutterstock.jpg?x=150&y=100&crop=1)\\
\\
**Suspected Chinese cybersnoop grounded in Italy after US tipoff** \\
\\
Zewei Xu's family reportedly bemused at arrest as extradition tabled\\
\\
Security13 days \| 10](https://www.theregister.com/2025/07/08/silk_typhoon_italy_arrest/?td=keepreading)[![](https://regmedia.co.uk/2025/07/15/shutterstock_1712116168.jpg?x=150&y=100&crop=1)\\
\\
**Security shop Adarma ceases trading, confirms it will enter administration** \\
\\
Former staffers of struggling UK biz say they don’t expect to be paid for July\\
\\
Security5 days \| 1](https://www.theregister.com/2025/07/16/adarma_will_enter_administration/?td=keepreading)[![](https://regmedia.co.uk/2021/04/09/shutterstock_knight_castle.jpg?x=150&y=100&crop=1)\\
\\
**IT consultancy settles US battle over alleged $14.75M government contract fraud** \\
\\
Outfit was accused of charging for specialist IT labor performed by uncertified folks\\
\\
Public Sector6 days \| 2](https://www.theregister.com/2025/07/15/us_puts_it_consultancy_to/?td=keepreading)[![](https://regmedia.co.uk/2023/03/14/embed_amd.jpg?x=150&y=100&crop=1)\\
\\
**AMD warns of new Meltdown, Spectre-like bugs affecting CPUs** \\
\\
Low-severity bugs but infosec pros claim they are a 'critical' overall threat – patch accordingly\\
\\
Security12 days \| 27](https://www.theregister.com/2025/07/09/amd_tsa_side_channel/?td=keepreading)

[![](https://regmedia.co.uk/2021/09/30/shutterstock_green_plane.jpg?x=150&y=100&crop=1)\\
\\
**Scattered Spider crime spree takes flight as focus turns to aviation sector** \\
\\
Time ticking for defenders as social engineering pros weave wider web\\
\\
Cyber-crime21 days \| 2](https://www.theregister.com/2025/06/30/scattered_spider_aviation/?td=keepreading)[![](https://regmedia.co.uk/2019/01/29/thumbs_up_shutterstock.jpg?x=150&y=100&crop=1)\\
\\
**23andMe's new owner says your DNA is safe this time** \\
\\
Nonprofit TTAM assures everything is BAU. Whether that makes customers feel better is another matter\\
\\
Cyber-crime19 days \| 18](https://www.theregister.com/2025/07/02/23andme_buyer_writes_to_customers/?td=keepreading)[![](https://regmedia.co.uk/2020/01/22/money_shutterstock.jpg?x=150&y=100&crop=1)\\
\\
**It's 2025 and almost half of you are still paying ransomware operators**\\
\\
Infosec in Brief PLUS: Crooks target hardware crypto wallets; Bad flaws in Brother printers; ,O365 allows takeover-free phishing; and more\\
\\
Security22 days \| 2](https://www.theregister.com/2025/06/30/information_security_in_brief/?td=keepreading)[![](https://regmedia.co.uk/2016/07/21/chain-paper.jpg?x=150&y=100&crop=1)\\
\\
**Supply chain attacks surge with orgs 'flying blind' about dependencies** \\
\\
Who is the third party that does the thing in our thing? Yep. Attacks explode over past year\\
\\
CSO26 days \| 4](https://www.theregister.com/2025/06/25/supply_chain_attacks_hammer_organizations/?td=keepreading)
