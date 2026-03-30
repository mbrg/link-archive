---
date: '2026-02-06'
description: The latest DOJ release of the Epstein archives has raised substantial
  criticism regarding data management practices, including mishandled redactions and
  corrupted files. Key insights reveal improper handling of base64 encoded attachments
  leading to significant data losses and difficulties reconstructing documents. Notably,
  the OCR utilized on the PDFs exacerbated issues by misidentifying characters, particularly
  distinguishing between `1` and `l`, due to poor font readability and encoding artifacts.
  A collaborative approach utilizing ML and OCR refinement techniques is suggested
  to facilitate the recovery of original attachments from corrupted data, highlighting
  unresolved security operational challenges.
link: https://neosmart.net/blog/recreating-epstein-pdfs-from-raw-encoded-attachments/
tags:
- DoJ
- OCR
- base64
- data-recovery
- Epstein
title: Recreating uncensored Epstein PDFs from raw encoded attachments ◆ The NeoSmart
  FilesThe NeoSmart Files
---

There have been a lot of complaints about both the competency and the logic behind the latest Epstein archive release by the DoJ: from censoring the names of co-conspirators to [censoring pictures of random women](https://x.com/Surajit_/status/2018007528110776656?s=20) in a way that makes individuals look guiltier [than they really are](https://x.com/FATCAed/status/2018258403336815092?s=20), [forgetting to redact credentials](https://x.com/vxunderground/status/2018914471834456465?s=20) that made it possible for all of Reddit to log into Epstein’s account and trample over all the evidence, and the complete ineptitude that resulted in most of the latest batch being corrupted thanks to [incorrectly converted Quoted-Printable encoding artifacts](https://x.com/mqudsi/status/2017790922830893422?s=20), it’s safe to say that Pam Bondi’s DoJ did not put its best and brightest on this (admittedly gargantuan) undertaking. But the most damning evidence has all been thoroughly redacted… hasn’t it? Well, maybe not.

I was thinking of writing an article on the mangled quoted-printable encoding the day this latest dump came out in response to all the misinformed musings and conjectures that were littering social media (and my dilly-dallying cost me, as someone [beat me to the punch](https://lars.ingebrigtsen.no/2026/02/02/whats-up-with-all-those-equals-signs-anyway/)), and spent some time searching through the latest archives looking  for some SMTP headers that I could use in the article when I came across a curious artifact: not only were the emails badly transcoded into plain text, but also some binary attachments were actually included in the dumps in their over-the-wire `Content-Transfer-Encoding: base64` format, and the unlucky intern that was assigned to the documents in question didn’t realize the significance of what they were looking at and didn’t see the point in censoring seemingly meaningless page after page of hex content!

Just take a look at [EFTA00400459](https://archive.org/details/efta-00400459), an email from correspondence between (presumably) one of Epstein’s assistants and Epstein lackey/co-conspirator Boris Nikolic and his friend, Sam Jaradeh, inviting them to a ████████ benefit:

[![](https://neosmart.net/blog/wp-content/uploads/2026/02/EFTA00400459-Sample.webp)](https://neosmart.net/blog/wp-content/uploads/2026/02/EFTA00400459-Sample.webp)

Those hex characters go on for 76 pages, and represent the file `DBC12 One Page Invite with Reply.pdf` encoded as base64 so that it can be included in the email without breaking the SMTP protocol. And converting it back to the original PDF is, theoretically, as easy as copy-and-pasting those 76 pages into a text editor, stripping the leading `>` bytes, and piping all that into `base64 -d > output.pdf`… or it would be, if we had the original (badly converted) email and not a partially redacted scan of a printout of said email with some shoddy OCR applied.

If you tried to actually copy that text as digitized by the DoJ from the PDF into a text editor, here’s what you’d see:

[![](https://neosmart.net/blog/wp-content/uploads/2026/02/DoJ-OCR-Sample.webp)](https://neosmart.net/blog/wp-content/uploads/2026/02/DoJ-OCR-Sample.webp)

You can ignore the `EFTA00400459` on the second line; that (or some variant thereof) will be interspersed into the base64 text since it’s stamped at the bottom of every page to identify the piece of evidence it came from. But what else do you notice? Here’s a hint: this is what proper base64 looks like:

[![](https://neosmart.net/blog/wp-content/uploads/2026/02/Proper-base64.webp)](https://neosmart.net/blog/wp-content/uploads/2026/02/Proper-base64.webp)

Notice how in this sample everything lines up perfectly (when using a monospaced font) at the right margin? And how that’s not the case when we copied-and-pasted from the OCR’d PDF? That’s because it wasn’t a great OCR job: extra characters have been hallucinated into the output, some of them not even legal base64 characters such as the `,` and `[`, while other characters have been omitted altogether, giving us content we can’t use:[1](https://neosmart.net/blog/recreating-epstein-pdfs-from-raw-encoded-attachments/#fn1-5373 "In case you’re wondering, the shell session excerpts in this article are all in fish, which I think is a good fit for string wrangling because of its string builtin with extensive operations with a very human-readable syntax (at least compared to perl or awk, the usual go-tos for string manipulation), and it lets you compose multiple operations as separate commands while not devolving to performing pathologically because no external commands are fork/exec‘d because of its builtin nature. And I’m not just saying that because of the blood, sweat, and tears I’ve contributed to the project.")\
\
```\
> pbpaste \\
     | string match -rv 'EFTA' \\
     | string trim -c " >" \\
     | string join "" \\
     | base64 -d >/dev/null\
base64: invalid input\
```\
\
I tried the easiest alternative I had at hand: I loaded up the PDF in Adobe Acrobat Pro and re-ran an OCR process on the document, but came up with even worse results, with spaces injected in the middle of the base64 content (easily fixable) in addition to other characters being completely misread and butchered – it really didn’t like the cramped monospace text at all. So I thought to do it manually with `tesseract`, which, while very far from state-of-the-art, can still be useful because it lets you do things like limit its output to a certain subset of characters, constraining the field of valid results and hopefully coercing it into producing better results.\
\
Only one problem: `tesseract` can’t read PDF input (or not by default, anyway). No problem, I’ll just use `imagemagick`/`ghostscript` to convert the PDF into individual PNG images (to avoid further generational loss) and provide those to `tesseract`, right? But that didn’t quite work out, they seem (?) to try to load and perform the conversion of all 76 separate pages/png files all at once, and then naturally crash on too-large inputs (but only after taking forever and generating the 76 (invalid) output files that you’re forced to subsequently clean up, of course):\
\
```\
> convert -density 300 EFTA00400459.pdf \\
        -background white -alpha remove \\
        -alpha off out.png\
convert-im6.q16: cache resources exhausted `/tmp/magick-QqXVSOZutVsiRcs7pLwwG2FYQnTsoAmX47' @ error/cache.c/OpenPixelCache/4119.\
convert-im6.q16: cache resources exhausted `out.png' @ error/cache.c/OpenPixelCache/4119.\
convert-im6.q16: No IDATs written into file `out-0.png' @ error/png.c/MagickPNGErrorHandler/1643.\
```\
\
So we turn to `pdftoppm` from the `poppler-utils` package instead, which does indeed handle each page of the source PDF separately and turned out to be up to the task, though incredibly slow:\
\
```bash\
> pdftoppm -png -r 300 EFTA00400459.pdf out.png\
```\
\
After waiting the requisite amount of time (and then some), I had files `out-01.png` through `out-76.png`, and was ready to try them with `tesseract`:\
\
```bash\
for n in (printf "%02d\n" (seq 1 76))\
    tesseract out-$n.png output-$n \\
        --psm 6 \\
        -c tessedit_char_whitelist='>'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/= \\
        -c load_system_dawg=0 \\
        -c load_freq_dawg=0\
end\
```\
\
The above `fish-shell` command [instructs](https://manpages.ubuntu.com/manpages/xenial/man1/tesseract.1.html)`tesseract(1)` to assume the input is a single block of text (the `--psm 6` argument) and limit itself to decoding only legal base64 characters (and the leading `>` so we can properly strip it out thereafter). My original attempt included a literal space in the valid char whitelist, but that gave me worse results: the very badly kerned base64 has significant apparent spacing between some adjacent characters (more on this later) and that caused tesseract to both incorrectly inject spaces (bad but fixable) and also possibly affect how it handled the character after the space (worse).\
\
Unfortunately, while tesseract gave me _slightly_ better output than either the original OCR’d DoJ text or the (terrible) Adobe Acrobat Pro OCR results, it too suffered from poor recognition and gave me very inconsistent line lengths… but it also suffered from something that I didn’t really think a heuristic-based, algorithm-driven tool like tesseract would succumb to, as it was more reminiscent of how first-generation LLMs would behave: in a few places, it would only read the first dozen or so characters on a line then leave the rest of the line blank, then pick up (correctly enough) at the start of the next line. Before I saw how generally useless the OCR results were and gave up on tesseract, I figured I’d just manually type out the rest of the line (the aborted lines were easy enough to find, thanks to the monospaced output), and _that_ was when I ran into the _real_ issue that took this from an interesting challenge to being almost mission impossible.\
\
I mentioned earlier the bad kerning, which tricked the OCR tools into injecting spaces where there were supposed to be none, but that was far from being the worst issue plaguing the PDF content. The real problem is that the text is rendered in possibly the worst typeface for the job at hand: Courier New.\
\
If you’re a font enthusiast, I certainly don’t need to say any more – you’re probably already shaking with a mix of PTSD and rage. But for the benefit of everyone else, let’s just say that Courier New is… not a great font. It was a digitization of the venerable (though certainly primitive) [Courier](https://en.wikipedia.org/wiki/Courier_(typeface)) fontface, commissioned by IBM in the 1950s. Courier was used (with some tweaks) for IBM typewriters, including [the IBM Selectric](https://en.wikipedia.org/wiki/IBM_Selectric), and in the 1990s it was “digitized directly from the golf ball of the IBM Selectric” by Monotype, and shipped with Windows 3.1, where it remained the default monospace font on Windows [until Consolas shipped with Windows Vista](https://neosmart.net/blog/a-comprehensive-look-at-the-new-microsoft-fonts/). Among the many issues with Courier New is that it was digitized from the Selectric golf ball “without accounting for the visual weight normally added by the typewriter’s ink ribbon”, which gives its characteristic “thin” look. Microsoft ClearType, which was only enabled by default with Windows Vista, addressed this major shortcoming to some extent, but Courier New has always struggled with general readability… and more importantly, with its poor distinction between characters.\
\
[![](https://neosmart.net/blog/wp-content/uploads/2026/02/Courier-Weight-Comparison.svg)](https://neosmart.net/blog/wp-content/uploads/2026/02/Courier-Weight-Comparison.svg)\
\
You can clearly see how downright anemic Courier New is when compared to the original Courier.\
\
While not as bad as some typewriter-era typefaces that actually reused the same symbol for `1` (one) and `l` (ell), Courier New came pretty close. Here is a comparison between the two fonts when rendering these two characters, only considerably enlarged:\
\
[![](https://neosmart.net/blog/wp-content/uploads/2026/02/Courier-New-1-and-l-Horizontal-Comparison.svg)](https://neosmart.net/blog/wp-content/uploads/2026/02/Courier-New-1-and-l-Horizontal-Comparison.svg)\
\
Comparing Courier and Courier New when it comes to differentiating between 1 (one) and l (ell).\
\
The combination of the two faults (the anemic weights and the even less distinction between 1 and l as compared to Courier) makes Courier New a terrible choice as a programming font. But as a font used for base64 output you want to OCR? You really couldn’t pick a worse option! To add fuel to the fire, you’re looking at SVG outlines of the fonts, meticulously converted and preserving all the fine details. But in the Epstein PDFs released by the DoJ, we only have low-quality JPEG scans at a fairly small point size. Here’s an actual (losslessly encoded) screenshot of the DoJ text at 100% – I challenge you to tell me which is a `1` and which is an `l` in the excerpt below:\
\
[![](https://neosmart.net/blog/wp-content/uploads/2026/02/Scanned-1-vs-l-png.webp)](https://neosmart.net/blog/wp-content/uploads/2026/02/Scanned-1-vs-l.png)\
\
It’s not that there isn’t _any_ difference between the two, because there is. And sometimes you get a clear gut feeling which is which – I was midway through manually typing out one line of base64 text when I got stuck on identifying a one vs ell… only to realize that, at the same time, I had confidently transcribed one of them earlier that same line without even pausing to think about which it was. Here’s a zoomed-in view of the scanned PDF: you can clearly see all the JPEG DCT artifacts, the color fringing, and the smearing of character shapes, all of which make it hard to properly identify the characters. But at the same time, at least in this particular sample, you can see which of the highlighted characters have a straight serif leading out the top-left (the middle, presumably an ell) and which of those have the slightest of strokes/feet extending from them (the first and last, presumably ones). But whether that’s because that’s how the original glyph appeared or it’s because of how the image was compressed, it’s tough to say:\
\
[![](https://neosmart.net/blog/wp-content/uploads/2026/02/Scanned-1-vs-l-zoomed-in-png.webp)](https://neosmart.net/blog/wp-content/uploads/2026/02/Scanned-1-vs-l-zoomed-in.png)\
\
But that’s getting ahead of myself: at this point, none of the OCR tools had actually given me usable results, even ignoring the very important question of `l` vs `1`. After having been let down by one open source offering (tesseract) and two commercial ones (Adobe Acrobat Pro and, presumably, whatever the DoJ used), I made the very questionable choice of writing a script to use yet another commercial offering, this time [Amazon/AWS Textract](https://aws.amazon.com/textract/pricing/), to process the PDF. Unfortunately, using it directly via the first-party tooling was (somewhat) of a no-go as it only supports smaller/shorter inputs for direct use; longer PDFs like this one need to be uploaded to S3 and then use the async workflow to start the recognition and poll for completion.\
\
Amazon Textract did possibly the best out of all the tools I tried, but its output still had obvious line length discrepancies – albeit only one to two characters or so off on average. I decided to try again, this time blowing up the input 2x (using nearest neighbor sampling to preserve sharp edges) as a workaround for Textract not having a tunable I could set to configure the DPI the document is processed at, though I worried all inputs could possibly be prescaled to a fixed size prior to processing once more:[2](https://neosmart.net/blog/recreating-epstein-pdfs-from-raw-encoded-attachments/#fn2-5373 "I didn’t want to convert the PNGs back to a single PDF as I didn’t want any further loss in quality.")\
\
```bash\
> for n in (printf "%02d\n" (seq 01 76))\
      convert EFTA00400459-$n.png -scale 200% \\
              EFTA00400459-$n"_2x".png; or break\
  end\
> parallel -j 16 ./textract.sh {} ::: EFTA00400459-*_2x.png\
```\
\
These results were notably better, and I’ve included them in an archive, but some of the pages scanned better than others. Textract doesn’t seem to be 100% deterministic from my brief experience with it, and their features page does make vague or unclear mentions to “ML”, though it’s not obvious when and where it kicks in or what it exactly refers to, but that could explain why a couple of the pages (like `EFTA00400459-62_2x.txt`) are considerably worse than others, even while the source images don’t show a good reason for that divergence.\
\
With the Textract 2x output cleaned up and piped into `base64 -i` (which ignores garbage data, generating invalid results that can still be usable for forensic analysis), I can get far enough to see that the PDF within the PDF (i.e. the actual PDF attachment originally sent) was at least partially (de)flate-encoded. Unfortunately, PDFs are binary files with different forms of compression applied; you can’t just use something like `strings` to extract any usable content. [`qpdf(1)` can be (ab)used](https://man.archlinux.org/man/extra/qpdf/qpdf.1.en) to decompress a PDF (while leaving it a PDF) via `qpdf --qdf --object-streams=disable input.pdf decompressed.pdf`, but, predictably, this doesn’t work when your input is garbled and corrupted:\
\
```\
> qpdf --qdf --object-streams=disable recovered.pdf decompressed.pdf\
WARNING: recovered.pdf: file is damaged\
WARNING: recovered.pdf: can't find startxref\
WARNING: recovered.pdf: Attempting to reconstruct cross-reference table\
WARNING: recovered.pdf (object 34 0, offset 52): unknown token while reading object; treating as string\
WARNING: recovered.pdf (object 34 0, offset 70): unknown token while reading object; treating as string\
WARNING: recovered.pdf (object 34 0, offset 85): unknown token while reading object; treating as string\
WARNING: recovered.pdf (object 34 0, offset 90): unexpected >\
WARNING: recovered.pdf (object 34 0, offset 92): unknown token while reading object; treating as string\
WARNING: recovered.pdf (object 34 0, offset 116): unknown token while reading object; treating as string\
WARNING: recovered.pdf (object 34 0, offset 121): unknown token while reading object; treating as string\
WARNING: recovered.pdf (object 34 0, offset 121): too many errors; giving up on reading object\
WARNING: recovered.pdf (object 34 0, offset 125): expected endobj\
WARNING: recovered.pdf (object 41 0, offset 9562): expected endstream\
WARNING: recovered.pdf (object 41 0, offset 8010): attempting to recover stream length\
WARNING: recovered.pdf (object 41 0, offset 8010): unable to recover stream data; treating stream as empty\
WARNING: recovered.pdf (object 41 0, offset 9616): expected endobj\
WARNING: recovered.pdf (object 41 0, offset 9616): EOF after endobj\
qpdf: recovered.pdf: unable to find trailer dictionary while recovering damaged file\
```\
\
Between the inconsistent OCR results and the problem with the `l` vs `1`, it’s not a very encouraging situation. To me, this is a problem begging for a (traditional, non-LLM) ML solution, specifically leveraging the fact that we know the font in question and, roughly, the compression applied. Alas, I don’t have more time to lend to this challenge at the moment, as there are a number of things I set aside just in order to publish this article.\
\
So here’s the challenge for anyone I can successfully nerdsnipe:\
\
- Can you manage to recreate the original PDF from the `Content-Transfer-Encoding: base64` output included in the dump? It can’t be that hard, can it?\
- Can you find other attachments included in the latest Epstein dumps that might also be possible to reconstruct? Unfortunately, the contractor that developed [the full-text search](https://www.justice.gov/epstein) for the Department of Justice did a pretty crappy job and full-text search is practically broken even accounting for the bad OCR and wrangled quoted-printable decoding (malicious compliance??); nevertheless, searching for `Content-Transfer-Encoding` and `base64` returns a number of results – it’s just that, unfortunately, most are uselessly truncated or only the SMTP headers from Apple Mail curiously extracted.\
\
I have uploaded [the original EFTA00400459.pdf](https://www.justice.gov/epstein/files/DataSet%209/EFTA00400459.pdf) from Epstein Dataset 9 as downloaded from the DoJ website [to the Internet Archive](https://archive.org/details/efta-00400459), as well as [the individual pages losslessly encoded to WebP images](https://archive.org/download/efta-00400459-lossless-webp) to save you the time and trouble of converting them yourself. If it’s of any use to anyone, I’ve also uploaded the very-much-invalid Amazon Textract OCR text (from the losslessly 2x’d images), [which you can download here](https://neosmart.net/blog/wp-content/uploads/2026/02/EFTA00400459_2x-textract.zip).\
\
Oh, and one final hint: when trying to figure out `1` vs `l`, I was able to do this with 100% accuracy only via trial-and-error, decoding one line of base64 text at-a-time, but this only works for the plain-text portions of the PDF (headers, etc). For example, I started with my best guess for one line that I had to type out myself when trying with tesseract, and then was able to (in this case) deduce which particular `1`s or `l`s were flipped:\
\
[![](https://neosmart.net/blog/wp-content/uploads/2026/02/Distinguishing-flipped-base64.webp)](https://neosmart.net/blog/wp-content/uploads/2026/02/Distinguishing-flipped-base64.webp)\
\
```\
> pbpaste\
SW5mbzw8L01sbHVzdHJhdG9yIDgxIDAgUj4+L1Jlc29lcmNlczw8L0NvbG9yU3BhY2U8PC9DUzAG\
> pbpaste | base64 -d\
Info<</Mllustrator 81 0 R>>/Resoerces<</ColorSpace<</CS0\
>\
> # which I was able to correct:\
>\
> pbpaste\
SW5mbzw8L0lsbHVzdHJhdG9yIDgxIDAgUj4+L1Jlc291cmNlczw8L0NvbG9yU3BhY2U8PC9DUzAG\
> pbpaste | base64 -d\
Info<</Illustrator 81 0 R>>/Resources<</ColorSpace<</CS0\
```\
\
…but good luck getting that to work once you get to the flate-compressed sections of the PDF.\
\
I’ll be posting updates on Twitter [@mqudsi](https://x.com/mqudsi), and you can reach out to me on Signal at `mqudsi.42` if you have anything sensitive you would like to share. You can join in the discussion [on Hacker News](https://news.ycombinator.com/item?id=46890335) or on [r/netsec](https://old.reddit.com/r/netsec/comments/1qw4sfa/recreating_uncensored_epstein_pdfs_from_raw/?). Leave a comment below if you have any ideas/questions, or if you think I missed something!\
\
* * *\
\
1. In case you’re wondering, the shell session excerpts in this article [are all in `fish`](https://github.com/fish-shell/fish-shell/), which I think is a good fit for string wrangling because of its [`string` builtin](https://fishshell.com/docs/current/cmds/string.html) with extensive operations with a very human-readable syntax (at least compared to `perl` or `awk`, the usual go-tos for string manipulation), and it lets you compose multiple operations as separate commands while not devolving to performing pathologically because no external commands are `fork`/`exec`‘d because of its builtin nature. And I’m not just saying that because of the blood, sweat, and tears I’ve contributed to the project. [↩](https://neosmart.net/blog/recreating-epstein-pdfs-from-raw-encoded-attachments/#rf1-5373 "Jump back to footnote 1 in the text.")\
\
2. I didn’t want to convert the PNGs back to a single PDF as I didn’t want any further loss in quality. [↩](https://neosmart.net/blog/recreating-epstein-pdfs-from-raw-encoded-attachments/#rf2-5373 "Jump back to footnote 2 in the text.")\
\
\
## 12 thoughts on “Recreating uncensored Epstein PDFs from raw encoded attachments”\
\
01. By playing with the curves using photopea I’m able to improve the readability a bit.\
\
\
    I’m applying the curve layer only at the top of the character\
\
    [https://full.ouplo.com/1a/6/ECnz.png](https://full.ouplo.com/1a/6/ECnz.png)\
\
\
\
    And I use a “sketch” curve to precisely darken the selection\
\
    [https://full.ouplo.com/1a/6/7msk.png](https://full.ouplo.com/1a/6/7msk.png)\
\
\
\
    Might also be interesting to extract small jpegs from all the ambiguous “1/l” and then make a website to crowd source the most likely character, like captchas.\
\
02. An alternative approach — captcha style:\
\
\
\
    – Divide the image into chunks like 50 characters long\
\
\
    – Put it on a website where anyone can type up the small amount of characters\
\
\
    – Reconstruct the text from the chunks\
\
\
\
    I have no doubt the masses of the internet will deliver on this one.\
\
03. Oh! That’s embarrassing – the previous commenter had the exact same idea.\
\
\
\
    AND i wrote my name as “anon” — but my picture is there 💀\
\
04. It’s interesting how the poorly executed encoding and redactions have turned this into more of a mystery than an actual release of information. I wonder how much more is still hidden in these corrupted files.\
\
05. Perhaps this can be turned into a very tedious, monotone but mostly straight-forward task suitable for an AI assistant. The method for deciding 1 vs l would be roughly:\
\
\
    – Try the four possible combinations for two consecutive uncertain 1/l sites.\
\
\
    – Attempt a decode where every layer outputs verbose error messages and exits early on error.\
\
\
    – Ideally, 2 of the cases will produce identical error output. These should correspond to the two combos where the first l/1 site was chosen wrong. Congrats, you have now determined the correct value for the first of the uncertain sites.\
\
06. chatgpt was excellent here … I fed it the EFTA00754474.pdf, and it quickly decoded the text portion of it.\
\
07. I was able to generate images for each page of base64, apply some color curves to all of them, working now on training a tesseract model on this font, I’m pretty close, but it still has trouble with 1/l when the l is blurry, and sometimes duplicates characters, but I’m getting multiple lines with zero errors, and very good accuracy.\
\
08. There is also EFTA02153691 which appears to be another email in the thread. Maybe a second source will help disambiguate some of the characters.\
\
09. Make your own OCR!\
\
\
\
    This a bit more of a boring solution … but if you know the font, make a dataset analogous to MNIST and train a CNN. Then cut out every character, convert to an image and feed it to the trained CNN. I’m pretty sure it would be very quick to run and very accurate.\
\
\
\
    With the help of a good LLM, I think this could be hacked together in a few hours.\
\
10. I’ve been trying to get this up and running in Azure Document intelligence, will post an update once I have more.\
\
11. This little helper tool can help decode a base64 string and highlight selected sections in base64 / plain text to try different variations of ones and “l”s:\
\
    [https://claude.ai/public/artifacts/4fb1c92c-a816-4b44-82b4-c2a1af1ca7bc](https://claude.ai/public/artifacts/4fb1c92c-a816-4b44-82b4-c2a1af1ca7bc)\
\
\
\
    You can test with the code from the example above:\
\
\
    SW5mbzw8L01sbHVzdHJhdG9yIDgxIDAgUj4+L1Jlc291cmN1czw8L0NvbG9yU3BhY2U8PC9DUzAG\
\
12. My best effort so far, basic ML with manual labelling.\
\
\
\
    Error rate seems fairly low, but there’s still random corruption.\
\
\
\
    [https://pastebin.com/UXRAJdKJ](https://pastebin.com/UXRAJdKJ)\
\
\
### Leave a Reply\
\
Your email address will not be published.Required fields are marked \*\
\
Comment \*\
\
Name \*\
\
Email \*\
\
Website\
\
Notify me of follow-up comments by email.\
\
Notify me of new posts by email.\
\
Δ
