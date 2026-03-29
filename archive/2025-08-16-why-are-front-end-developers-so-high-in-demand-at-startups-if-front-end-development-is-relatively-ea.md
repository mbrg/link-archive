---
date: '2025-08-16'
description: Simon Willison argues that front-end development is significantly more
  complex than perceived, challenging the notion that it is an "easier" discipline.
  Developers must navigate a myriad of environments, including multiple browser versions
  and device variations, which require extensive debugging and feature detection strategies.
  Front-end engineers also confront unique security challenges such as CSRF and XSS,
  alongside performance optimization considerations that span from DNS to caching.
  The evolving landscape of web technologies—including responsive design, WebGL, and
  HTML5—further complicates their role. This insight underscores the critical need
  for skilled front-end developers in startups.
link: https://simonwillison.net/2012/Feb/13/why-are-front-end/
tags:
- frontend
- web-development
- web-performance
- programming
- recruiting
title: Why are front end developers so high in demand at startups if front end development
  is relatively easier than other fields of engineering?
---

# [Simon Willison’s Weblog](https://simonwillison.net/)

[Subscribe](https://simonwillison.net/about/#subscribe)

## Why are front end developers so high in demand at startups if front end development is relatively easier than other fields of engineering?

13th February 2012

_My answer to [Why are front end developers so high in demand at startups if front end development is relatively easier than other fields of engineering?](https://www.quora.com/Why-are-front-end-developers-so-high-in-demand-at-startups-if-front-end-development-is-relatively-easier-than-other-fields-of-engineering/answer/Simon-Willison) on Quora_

You’re starting with an invalid assumption. Front end development is absolutely not “easier” than other forms of engineering.

When you’re writing server-side code, you’re writing for one language on one operating system with (usually) one database implementation. Write the code, test that it works, go home.

Front end developers have to write code that works in dozens of different environments. It’s not just different browsers (IE/Firefox/Safari/Chrome/Opera)—it’s also the different versions of those browsers. IE 6, 7, 8, 9 and 10 all have their own bugs and limitations. Mobile is even worse—hundreds of different browser/OS/device variations, and even Android has bugs and even feature regressions on different browser versions.

To make things worse, they have to do most of their work in HTML and CSS, which provide extremely limited tools for working around bugs (hence the past decade’s obsession with CSS hacks). JavaScript helps a lot here because at least you can use feature detection (though that in itself is controversial due to the performance overhead)—but now you’re handling even more code branches and potential areas for bugs to creep in.

Not to mention that a good frontend engineer will need an understanding of web performance—which incorporates everything from DNS lookup times to HTTP caching behaviour to minification build scripts to CSS layout engine implementation details.

Oh, and they’re on the frontline of web application security, so they need to understand CSRF, XSS, Click Jacking, DNS pinning (that was a fun one), UTF-7 character encoding attacks...

And these days there’s responsive design, media queries, HTML5 AppCache, WebGL, CSS transforms, SVG, Canvas, localStorage, WebSockets and so on to worry about as well—each one introducing exciting new capabilities, and each one introducing brand new browser support challenges to figure out.

Seriously. Server-side developers have it easy.

Posted [13th February 2012](https://simonwillison.net/2012/Feb/13/) at 4:32 pm · Follow me on [Mastodon](https://fedi.simonwillison.net/@simon), [Bluesky](https://bsky.app/profile/simonwillison.net), [Twitter](https://twitter.com/simonw) or [subscribe to my newsletter](https://simonwillison.net/about/#subscribe)

## More recent articles

- [The Summer of Johann: prompt injections as far as the eye can see](https://simonwillison.net/2025/Aug/15/the-summer-of-johann/) \- 15th August 2025
- [Open weight LLMs exhibit inconsistent performance across providers](https://simonwillison.net/2025/Aug/15/inconsistent-performance/) \- 15th August 2025
- [LLM 0.27, the annotated release notes: GPT-5 and improved tool calling](https://simonwillison.net/2025/Aug/11/llm-027/) \- 11th August 2025

This is **Why are front end developers so high in demand at startups if front end development is relatively easier than other fields of engineering?** by Simon Willison, posted on [13th February 2012](https://simonwillison.net/2012/Feb/13/).

[programming\\
156](https://simonwillison.net/tags/programming/) [recruiting\\
8](https://simonwillison.net/tags/recruiting/) [web-development\\
169](https://simonwillison.net/tags/web-development/) [quora\\
1005](https://simonwillison.net/tags/quora/) [frontend\\
19](https://simonwillison.net/tags/frontend/)

**Next:** [How can a new developer get involved in open-source projects?](https://simonwillison.net/2012/Feb/14/how-can-a-new/)

**Previous:** [Which core programming principles apply to all languages?](https://simonwillison.net/2012/Feb/13/which-core-programming-principles/)

### Monthly briefing

Sponsor me for **$10/month** and get a curated email digest of the month's most important LLM developments.


Pay me to send you less!


[Sponsor & subscribe](https://github.com/sponsors/simonw/)

- [Colophon](https://simonwillison.net/about/#about-site)
- ©
- [2002](https://simonwillison.net/2002/)
- [2003](https://simonwillison.net/2003/)
- [2004](https://simonwillison.net/2004/)
- [2005](https://simonwillison.net/2005/)
- [2006](https://simonwillison.net/2006/)
- [2007](https://simonwillison.net/2007/)
- [2008](https://simonwillison.net/2008/)
- [2009](https://simonwillison.net/2009/)
- [2010](https://simonwillison.net/2010/)
- [2011](https://simonwillison.net/2011/)
- [2012](https://simonwillison.net/2012/)
- [2013](https://simonwillison.net/2013/)
- [2014](https://simonwillison.net/2014/)
- [2015](https://simonwillison.net/2015/)
- [2016](https://simonwillison.net/2016/)
- [2017](https://simonwillison.net/2017/)
- [2018](https://simonwillison.net/2018/)
- [2019](https://simonwillison.net/2019/)
- [2020](https://simonwillison.net/2020/)
- [2021](https://simonwillison.net/2021/)
- [2022](https://simonwillison.net/2022/)
- [2023](https://simonwillison.net/2023/)
- [2024](https://simonwillison.net/2024/)
- [2025](https://simonwillison.net/2025/)
