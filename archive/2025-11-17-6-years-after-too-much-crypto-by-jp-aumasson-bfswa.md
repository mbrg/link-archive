---
date: '2025-11-17'
description: In his analysis, JP Aumasson revisits the efficacy of symmetric cryptographic
  algorithms, emphasizing that many designs incorporate excessive security margins
  without post-standardization adjustments. He evaluates AES, BLAKE2, ChaCha20, and
  Keccak/SHA-3, suggesting reduced rounds without significant attacks against lower
  configurations. Notably, he proposes ChaCha8 and 10-round Keccak for performance
  improvements, benefiting applications like Ethereum. Despite the lack of practical
  advancements against these proposed reductions, standardization bodies remain resistant
  to change, highlighting inertia in cryptographic practice amidst evolving threat
  landscapes. Further review is suggested for 25 years hence.
link: https://bfswa.substack.com/p/6-years-after-too-much-crypto
tags:
- algorithm optimization
- AES
- BLAKE2
- cryptography
- Keccak
title: 6 years after too much crypto - by JP Aumasson - bfSwA
---

# [bfSwA](https://bfswa.substack.com/)

SubscribeSign in

# 6 years after too much crypto

### Test of time passed

[![JP Aumasson's avatar](https://substackcdn.com/image/fetch/$s_!jlto!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3bfff7ae-0be3-4504-a445-97335b8103c0_232x232.png)](https://substack.com/@veorq)

[JP Aumasson](https://substack.com/@veorq)

Nov 16, 2025

4

Share

In 2019 I published [Too much crypto](https://eprint.iacr.org/2019/1492.pdf) and presented it at Real World Crypto 2020 in New York. I argued that symmetric algorithms burn unnecessary cycles because:

1. Designers rightfully set many rounds in their initial design as a security margin, but

2. Once an algorithm is standardized, the round count isn’t adjusted after we know it’s oversized.


The saddest case is Keccak/SHA3: submitted with 18 rounds, designers raised it to 24 rounds during the SHA3 competition after a [pretty dumb](https://www.aumasson.jp/data/talks/zerosum_rump.pdf) 2¹⁰²⁴-complexity attack on 18 rounds. The observable universe contains only about 2²⁶⁶ atoms. As of November 2025, there are no practical attacks for more than five rounds.

I argued we could safely lower the rounds of AES, ChaCha20, Keccak/SHA-3, and BLAKE2. How did these suggestions age?

# AES

I proposed **9 rounds instead of 10**.

**No meaningful cryptanalysis progress**. The best practical attack remains stuck at 6 rounds. A [2025 paper](https://eprint.iacr.org/2025/1326.pdf) proved that 8-round AES behaves at least close to ideally with respect to input–output differentials’ distribution.

✅ Test passed

# BLAKE2

I proposed **8 rounds instead of 12** for BLAKE2b and **7 rounds instead of 10** for BLAKE2s.

And the same year we designed **[BLAKE3](https://blake3.io/)** with 7 rounds.

**No meaningful cryptanalysis progress**. No non-trivial practical attacks even on reduced versions. The astronomical-complexity [“boomerang distinguishers”](https://eprint.iacr.org/2014/1012.pdf) up to 7.5 rounds are unimproved since 2014.

✅ Test passed

# ChaCha20

I proposed **8 rounds instead of 20**, that is, ChaCha8.

Daniel J. Bernstein, the designer of ChaCha20, [finds it too risky](https://cr.yp.to/talks/2025.03.24/slides-djb-20250324-mceliece-4x3.pdf).

**ChaCha6 cryptanalysis progressed**: complexity [dropped](https://eprint.iacr.org/2019/1492.pdf) from 2¹²⁷ to 2⁵⁷. Doing 2⁵⁷ operations is practical; at most minutes on a small GPU cluster. But here the attacker needs 2⁵⁵ outputs, or about 2⁶¹ bytes, two exbibytes. That’s more data than every hyperscaler on Earth stores combined. The attacker also needs to control the nonces.

**ChaCha7 cryptanalysis progressed**: complexity [dropped](https://eprint.iacr.org/2019/1492.pdf) from 2²³⁸ to 2¹⁴⁸. The attacker needs about 2¹²⁶ known-ciphertext data blocks. GPT says “2¹²⁶ is the number of grains of sand if you crushed amillion Earths into sand.” True or not, 2¹²⁶ is a shockingly high number. Anything with time or data complexity above 2¹⁰⁰ is and will likely remain impossible.

**ChaCha8: still no attack published**.

✅ Test passed

# Keccak/SHA3

I proposed **10 rounds instead of 24**. The Keccak designers had proposed [KangarooTwelve](https://keccak.team/kangarootwelve.html) with 12 rounds.

**No meaningful [cryptanalysis progress](https://keccak.team/third_party.html)**, just practical attacks on 4-round SHA3-384. The [best practical attack](https://keccak.team/crunchy_contest.html) breaks 5 rounds.

✅ Test passed

# To conclude

IETF and NIST won’t revise the standardized round counts of AES, ChaCha20, or SHA-3. AES is already so fast on hardware that shaving one round brings no meaningful gain.

But there are places where reduced rounds make sense:

- **ChaCha8** delivers a 2.5× speed-up when the 20-round standard isn’t required. For example, Rust programs can integrate ChaCha8 via [RustCrypto](https://docs.rs/chacha20/latest/chacha20/type.ChaCha8.html).

- **10-round Keccak/SHA3** yields a 2.4× speed-up and would benefit Ethereum and every blockchain relying on Keccak, especially when computed as a circuit inside ZK proof systems.


Let’s revisit all this again in **25 years**.

* * *

#### Subscribe to bfSwA

By JP Aumasson · Launched 4 days ago

It’s not true, but it is shocking.

Subscribe

By subscribing, I agree to Substack's [Terms of Use](https://substack.com/tos), and acknowledge its [Information Collection Notice](https://substack.com/ccpa#personal-data-collected) and [Privacy Policy](https://substack.com/privacy).

[![Quang Dao's avatar](https://substackcdn.com/image/fetch/$s_!341i!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F646cd6c3-6b3a-466b-ae55-2f05b0e2df63_400x400.jpeg)](https://substack.com/profile/25693310-quang-dao)

[![Steve Piper's avatar](https://substackcdn.com/image/fetch/$s_!1qiv!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F1c1fe9b4-c2d5-465a-97a2-2b7720ba0be0_144x144.png)](https://substack.com/profile/20198624-steve-piper)

4 Likes

4

Share

#### Discussion about this post

CommentsRestacks

![User's avatar](https://substackcdn.com/image/fetch/$s_!TnFC!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Favatars%2Fdefault-light.png)

TopLatestDiscussions

[Quantum computers will not steal your bitcoins, even if they can](https://bfswa.substack.com/p/quantum-computers-will-not-steal)

[The quantum gravity principle](https://bfswa.substack.com/p/quantum-computers-will-not-steal)

Nov 13•
[JP Aumasson](https://substack.com/@veorq)

9

2

1

![](https://substackcdn.com/image/fetch/$s_!2YeU!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4ddbf6c7-b965-4fc6-bd7b-a828f8eb1113_1118x1148.png)

Ready for more?

Subscribe
