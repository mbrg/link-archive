---
date: '2025-11-14'
description: The critique of X Chat reveals significant vulnerabilities in its messaging
  protocol, primarily focusing on static key management, lack of public protocol transparency,
  and susceptibility to man-in-the-middle attacks. Key findings include the absence
  of forward and post-compromise security due to the use of a static conversation
  key, which threatens the confidentiality of messages once a key is compromised.
  Additionally, the app's reliance on server-generated public keys for key distribution
  raises major security concerns. Despite claims of encryption, these technical deficiencies
  suggest users should reconsider X Chat for sensitive communications.
link: https://david.nepozitek.cz/blog/can-elon-musk-read-your-x-chat-messages
tags:
- data-security
- X-Chat
- end-to-end-encryption
- cryptography
- secure-messaging
title: Can Elon Musk Read Your X Chat Messages?
---

## Wanna see more post like this one?

Get notified when I write the next blog post.

Subscribe

You can unsubscribe at any time.

[Built with Kit](https://kit.com/features/forms?utm_campaign=poweredby&utm_content=form&utm_medium=referral&utm_source=dynamic)

![Can Elon Musk Read Your X Chat Messages?](https://david.nepozitek.cz/_astro/messages_hero.DX_aUL3e_1fKBPr.webp)

# Can Elon Musk Read Your X Chat Messages?

Published on
Nov 9, 2025.

Celebrated

22

times.

Earlier this year, X announced a new generation of their messaging system called X Chat.
It’s been recently praised by people on X including Elon Musk himself.
He claimed that **even with a gun to his head, he wouldn’t be able to read X Chat messages** due to their “full encryption”.[Go to source](https://x.com/elonmusk/status/1980210961152926044)
He’s made a similar claim before, back when the X (Twitter) messages were rather subpar[Go to source](https://mjg59.dreamwidth.org/66791.html), so I was curious to see if things have improved.

I’ve reversed-engineered the X Android app as I was interested in the cryptographic design.
Feel free to skip to the [Appendix section](https://david.nepozitek.cz/blog/can-elon-musk-read-your-x-chat-messages#appendix-how-the-current-x-chat-protocol-works) if you want to see the description of the protocol.
But even without going into the details of the protocol, several issues stand out that make the X Chat far from satisfactory, in my eyes.
I’ll go over four specific reasons why you might reconsider using X Chat for sensitive conversations.

TLDR

Does X Chat provide end-to-end encrypted messaging?

**No.**

How much effort would it take for a malicious server operator to read your messages?

**Rather little.**

## The Promise of End-to-End Encryption

As more and more of our communication moves online, the need for secure messaging becomes increasingly important.
Modern messaging apps like Signal try to satisfy this need by providing end-to-end encrypted (E2EE) messaging.
Simply put, E2EE messaging is a method of secure communication where **only the participating users can read the plaintext messages.**
We also typically want to ensure that the messages cannot be modified by other parties.

This strong property should protect the users even from the server operator itself, a malicious actor compromising the server, or governments trying to spy on private conversations.

## Issue \#1: Using Long-Term Keys for Encryption

When talking about secure messaging, there are two properties that are particularly relevant due to the long-term nature of messaging:

1. **Forward Secrecy:** If secrets are compromised at some point, past messages should remain secure.
2. **Post-Compromise Security:** If secrets are compromised at some point, future messages should remain secure once the compromise is resolved.

![Forward Secrecy and Post-Compromise Security](https://david.nepozitek.cz/secrecy.svg)

To be fair, I’m simplifying things a bit here.
There are more details to consider, like exactly which keys might get exposed or how long it takes for things to become secure again.
With that in mind, how does X Chat perform in these areas?

### No Forward Secrecy and No Post-Compromise Security

X Chat encrypts messages using a shared secret called a conversation key.
This key is generated at the start of the conversation and then used to encrypt all messages in that conversation.
The problem is that this conversation key basically never changes.
That makes all the potential attacks way worse.
**If the conversation key is ever compromised, all past and future messages can be decrypted.**

Not only that the conversation keys are static, but they can be also always restored using the long-term identity keys of the participants.
If an attacker manages to compromise the long-term identity keys of one of the participants, they can decrypt every message that user has ever sent or received and will ever send or receive in the future.

### Falling Behind The State of The Art

Modern secure messaging apps usually implement some form of [key ratcheting](https://signal.org/docs/specifications/doubleratchet/) and [more sophisticated key agreement protocols](https://signal.org/docs/specifications/x3dh/).
Thanks to that, the conversation keys change frequently and cannot be derived from past or future keys.

The documentation mentions that X is “working on mechanisms to allow private key rotation to offer some forward security in the future.”
Still, it feels quite underwhelming given that other messaging apps have had this for years.

## Issue \#2: The Protocol Is Not Public

You can’t meaningfully evaluate the security of a protocol unless you know the protocol.
The only documentation about X Chat’s encryption is a brief help center article.[Go to source](https://help.x.com/en/using-x/encrypted-direct-messages)
It lists some particular properties, but it does not go into any technical details about the protocol itself.

The documentation says a white paper will be published someday.
Until then, people must either trust X or reverse-engineer the clients.

Deep Dive

### Is the App Running The Protocol?

Our goal isn’t just to read a protocol on paper.
We want to be confident the app actually implements that protocol, and that everyone adheres to it.
That’s a difficult problem, and it’s especially hard for web applications like the web implementation of X Chat.

Some messaging apps ship only native clients that makes some things easier.
If a project is open source and have reproducible builds, you can verify that a binary downloaded from an app store matches the source that was reviewed.
Even without reproducibility, you can check that the app is not capable of changing its code after being installed, and you control when the app is updated.
Also, the binary signed by developer certificates should make certain scenarios of shipping modified code more difficult.

Web apps are messier: browsers fetch code from the server on every visit (aside from caching).
That makes it nearly impossible for a user to tell what JavaScript is running in their browser at any given moment.
Also, without code signing, the security basically shrinks into the last TLS hop between the browser and the server.
Although there are some [proposals](https://github.com/WICG/isolated-web-apps/tree/main) on how to provide verifiable code delivery for web apps, I’m not aware of any major app adopting them.

If you don’t have your Network Tab constantly open and watch every single request, something like this could easily go unnoticed:

```
function sendMessage(plaintextMessage: string) {
    // The original function that encrypts and sends the message
    encryptAndSend(plaintextMessage);

    if (username === "@david_nepozitek") {
        sendToElon(plaintextMessage); // Send the plaintext message
    }
}
```

Remember that X Chat does not provide forward secrecy nor post-compromise security.
That means **a single successful modification of the app is enough for an attacker to access all past and future messages of the targeted user.**

## Issue \#3: Man in the Middle Attacks

Let’s assume that the code actually does what it says on the tin.
Well, the [tin](https://help.x.com/en/using-x/encrypted-direct-messages) literally says: **“we do not offer protections against man-in-the-middle attacks”**.

This is the primary reason why I state that X Chat currently does not provide end-to-end encryption.
The main problem is that it is not possible to verify the public keys of the participants outside the app.
Let me walk you through a simple attack that allows the server to compromise an X Chat conversation without anyone noticing.

### The Attack on Key Distribution

First, let’s look at how the key distribution works in X Chat.
At the start of the conversation, one participant generates a random conversation key.
Then, it is encrypted using the public keys of the participants and sent to the server.
When a participant wants to read or send messages in the conversation, it retrieves the encrypted conversation key from the server and decrypts it using their private key.

However, the server is the one providing both the public keys of the participants and the encrypted conversation keys.
Thanks to that, **the server can hijack the key distribution process and consequently read all messages in the conversation.**
In a concrete example, when Alice wants to start a conversation with Bob, the server could simply do the following:

1. Alice generates a new conversation key **CA**.
2. Alice asks the server for Bob’s public key.
3. The server provides Alice with a public key **PS** controlled by the server instead of Bob’s real public key.
4. Alice encrypts the conversation key **CA** with the public key **PS** and sends it to the server.
5. The server decrypts the conversation key **CA** using its private key.
6. The server now generates another conversation key **CS**.
7. The server encrypts the conversation key **CS** with Bob’s real public key and sends it to Bob.
8. Now, when Alice sends a message, the server can decrypt it using the conversation key **CA**, read it, re-encrypt it using the conversation key **CS**, and send it to Bob.

### The Standard Fix

The problem with this implementation is that users always rely on the server.
The standard way to prevent this kind of attack is to perform some kind of mutual verification of the participants outside the app.
For example, the users could compare fingerprints of their public keys in person.
Thanks to that, even if the server tries to perform a man-in-the-middle attack, the users would notice that the public keys do not match.

## Issue \#4: Users Are Forced to Use Weak PINs

Now we’re getting into a bit more subtle territory.
One of the traditional problems with secure messaging is the need for strong key material that is only known to the user.
Unfortunately, humans are notoriously bad at remembering long, random passwords, yet they also want to access their messages from multiple devices.
Some messaging apps let users authenticate with short PINs, which are then in a relatively secure way “hardened” into strong keys.

### Juicebox

X Chat uses [Juicebox](https://juicebox.xyz/), an open-source project for distributed storage and recovery of secrets using PIN authentication.
Here’s how it works: a user defines a PIN and a secret (in this case, their long-term keys).
The secret is split into multiple shares and stored across several servers with Hardware Security Modules (HSMs).
The original secret can be reconstructed by combining a predefined number of shares and the correct PIN.

The security of this system relies on the proper setup of the HSMs and strict rate-limiting of retrieval attempts from the HSMs.
If any of these is not done correctly, an attacker could brute-force the PIN and recover the secrets.

### UX Traded Off for Security

This approach improves usability, but it shifts some trust towards the server operator and the HSMs.
Juicebox describes a detailed [ceremony](https://github.com/juicebox-systems/ceremony/tree/main) that should be followed and published to initialize the HSMs securely.
The X engineering team has shared a recording of a slightly altered ceremony from one of their datacenters.[Go to source](https://x.com/XEng/status/1971739456857145574)
For some reason, there is no recording from the other one.

While the Juicebox protocol itself supports long PINs, **X Chat limits users to 4-character PINs.**
That is not inherently bad, but I would expect at least an option to provide strong PINs for users who want to rely on math rather than trust.

## Appendix: How The Current X Chat Protocol Works

Below is a high-level description of how the current X Chat protocol works.
I’ve reconstructed it by reverse-engineering the X Android app from October 2025.
Note that it might miss some details or contain inaccuracies, but it should give you a general idea of the overall design.

### Registration Process

When a user wants to start using X Chat, they go through a registration process to set up their long-term keys:

```
function registerUserForXChat(userPin: string) {

    // Step 1: Generate two secp256r1 key pairs
    const identityKeyPair = generateSecp256r1KeyPair(); // 32 bytes private key
    const signingKeyPair = generateSecp256r1KeyPair();   // 32 bytes private key

    // Step 2: Concatenate the private keys
    const combinedPrivateKeys = concat(
        identityKeyPair.privateKey,  // 32 bytes
        signingKeyPair.privateKey    // 32 bytes
    );

    // Step 3: Sign the identity public key with the signing key
    const identityKeySignature = ecdsaSign(identityKeyPair.publicKey, signingKeyPair.privateKey);

    // Send public keys and signature to the server
    sendToServer({
        identityPublicKey: identityKeyPair.publicKey,
        signingPublicKey: signingKeyPair.publicKey,
        identityKeySignature: identityKeySignature
    });

    // Step 5: Store the private keys as secret shares in Juicebox HSMs
    juiceboxClient.storeSecretShares(
        userPin,
        combinedPrivateKeys
    );
}
```

### One-On-One Conversation

When a user wants to send a message to another user, the following steps are performed:

```
function sendOneOnOneMessage(
    userRecipientId: string,
    plaintextMessage: string
) {
    const participants = [currentUserId, userRecipientId];

    // Step 1: Get or create a conversation key for this recipient
    const conversationId = XChatConverationId(participants);

    let conversationKey = await getExistingConversationKey(conversationId);

    if (!conversationKey) {
        // Generate a new 32-byte random conversation key
        conversationKey = generateRandomBytes(32);

        for (const participant of participants) {
            // Get the participant's public identity key from the server
            const participantIdentityPublicKey = await getPublicIdentityKey(participant);

            // Generate a new ephemeral secp256r1 key pair
            const ephemeralKeyPair = generateSecp256r1KeyPair();

            // Perform ECDH key agreement to get a shared secret
            const baseSharedSecret = ecdh(
                participantIdentityPublicKey,
                ephemeralKeyPair.privateKey
            );

            // Derive an AES key using HKDF
            const derivedSharedSecret = hkdf(baseSharedSecret, ephemeralKeyPair.publicKey);

            // Encrypt the conversation key with the derived key using AES-GCM
            const encryptedConversationKey = AES_GCM(
                conversationKey,
                derivedSharedSecret
            );

            // Send to server
            await sendToServer({
                participant: participant,
                ephemeralPublicKey: ephemeralKeyPair.publicKey,
                encryptedConversationKey: encryptedConversationKey
            });
        }
    }

    // Step 2: Encrypt the message using libsodium's SecretBox
    // (XSalsa20-Poly1305 with a fresh nonce)
    const nonce = libsodium.getSecretBoxNonce();
    const encryptedMessage = libsodium.cryptoSecretBoxEasy(
        plaintextMessage,
        nonce,
        conversationKey
    );

    // Step 3: Sign the message metadata with the signing key
    const signingKeyPair = getMySigningKeyPair();

    const messageEnvelope = {
        encryptedMessage,
        messageType,
        senderId,
        conversationId,
        conversationKeyVersion,
        messageId: randomUUID(),
    };

    const signature = ecdsaSign(
        messageEnvelope,
        signingKeyPair.privateKey
    );

    // Send the encrypted message with signature to the server
    sendToServer({
        envelope: messageEnvelope,
        signature: signature,
        ... // extra metadata
    });
}
```

### Group Conversation

I decided to not reverse-engineer the group conversation protocol as it is a bit more complex.
From what I could gather, it uses a Ratchet Tree structure to derive shared secrets among the group members.
The tree is updated when the group membership changes.
However, it does not seem to be periodically ratcheted symmetrically nor asymmetrically like in some other protocols.

22

celebrations

Celebrate, if you liked the post!

![David Nepožitek](https://david.nepozitek.cz/_astro/portrait.CRpQwDuf_1JFlrK.webp)

Written by David Nepožitek


I'm a software engineer who enjoys cryptography, cloud development,
design engineering and some other fun tech stuff. I currently work
in [Spotflow](https://spotflow.io/) building
an observability platform for embedded devices.


## Keep in touch.

david@nepozitek.cz

[RSS Feed](https://david.nepozitek.cz/rss.xml)

•

[X](https://x.com/david_nepozitek)

[LinkedIn](https://www.linkedin.com/in/david-nepozitek/)

[Github](https://github.com/DavidNepozitek)
