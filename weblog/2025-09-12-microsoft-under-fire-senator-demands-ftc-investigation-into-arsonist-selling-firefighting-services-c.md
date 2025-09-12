---
date: '2025-09-12'
description: "Senator Ron Wyden has called for an FTC investigation into Microsoft,\
  \ labeling it \"gross cybersecurity negligence\" related to ransomware attacks exploiting\
  \ long-known Windows vulnerabilities. Wyden's critique centers on Microsoft's continued\
  \ use of outdated RC4 encryption in Active Directory, which facilitates attacks\
  \ like Kerberoasting. This has enabled widespread breaches, notably the Ascension\
  \ Health incident, which compromised 5.6 million records. With Microsoft's security\
  \ division generating over $20 billion, concerns arise over its dual approach\u2014\
  selling add-on cybersecurity services while neglecting core product security. The\
  \ implications could reshape industry standards for secure software development."
link: /archive/2025-09-12-microsoft-under-fire-senator-demands-ftc-investigation-into-arsonist-selling-firefighting-services-c
tags:
- Microsoft
- FTC investigation
- ransomware
- vulnerabilities
- cybersecurity
- weblog
title: "Microsoft under fire: Senator demands FTC investigation into \u2018arsonist\
  \ selling firefighting services\u2019 \u25C6 CSO Online"
type: weblog
---

I think it's good for congress to put pressure on ecosystem maintainers. But people own their choices, including the choice ti blindly use Microsoft's defaults.

---

> “Microsoft has become like an arsonist selling firefighting services to their victims,” Wyden wrote in the [letter](https://www.wyden.senate.gov/imo/media/doc/wyden_letter_to_ftc_on_microsoft_kerberoasting_ransomwarepdf.pdf), arguing that the company had built a profitable cybersecurity business while simultaneously leaving its core products vulnerable to attack.

Shots fired 

---

> The letter presented a detailed case study of the February 2024 ransomware attack against [Ascension Health](https://www.csoonline.com/article/3480397/how-cyber-insurance-shapes-risk-ascension-and-the-limits-of-lessons-learned.html) that compromised 5.6 million patient records, demonstrating how Microsoft’s default security configurations enabled hackers to move from a single infected laptop to an organization-wide breach.

Microsoft has a great tradition of insecure configs.

---

> “That’s exactly what played out in the Ascension case, where one weak default snowballed into a ransomware disaster,” said Sanchit Vir Gogia, chief analyst and CEO at Greyhound Research.

If one wrong config means domain admin you've got bigger problems than Microsoft's defaults..

---

> Microsoft’s response fell short, publishing guidance as “a highly technical blog post on an obscure area of the company’s website on a Friday afternoon.” The company also promised to release a software update disabling RC4 encryption, but eleven months later, “Microsoft has yet to release that promised security update,” Wyden noted.

This is a good point. It's difficult telling your customers that your product comes with a real productivity-security tradeoff, so corps don't. They hide it away behind technical details and unclear language.

