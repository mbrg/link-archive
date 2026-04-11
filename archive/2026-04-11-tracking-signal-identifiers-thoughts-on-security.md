---
date: '2026-04-11'
description: Recent developments reveal critical vulnerabilities in the privacy of
  Signal groups, notably their susceptibility to infiltration by law enforcement,
  including the FBI. Despite Signal's claims of limited data retention, users can
  be tracked through persistent identifiers linked to their accounts and associated
  phone numbers. Even with changing usernames and display names, member service IDs
  remain unchanged, facilitating identity tracking. The FBI may access user information
  through National Security Letters, potentially bypassing Signal's user agreements.
  This design flaw raises significant concerns regarding the effectiveness of user
  anonymity in high-risk environments, emphasizing the need for enhanced OPSEC protocols.
link: https://scriptjunkie.us/2026/01/tracking-signal-identifiers/
tags:
- Tracking Identification
- Signal App
- Government Surveillance
- Security Research
- Privacy
title: Tracking Signal Identifiers « Thoughts on Security
---

## Tracking Signal Identifiers

In the past few days Signal groups exploded in the news with [revelations that Signal groups are the primary](https://x.com/camhigby/status/2015093523733733474) "ICE tracker" channels, [may have dispatched Alex Pretti to his fatal encounter with DHS](https://www.dailymail.co.uk/news/article-15498429/Alex-Pretti-Minnesota-protest-groups-Signal-group-chats-organized.html), and are [under investigation by the FBI](https://www.nbcnews.com/tech/internet/fbi-investigating-minnesota-signal-minneapolis-group-ice-patel-kash-rcna256041). As groups frequently hit the 1000-member capacity, concern about infiltration is rampant. Key facets of the groups include:

1. [Frequently rapidly changing display names and usernames](https://x.com/camhigby/status/2015093909735571462) and
2. Members using aliases to avoid being identified by name.

**Today we'll evaluate the security of those measures. To summarize, it doesn't look good for this threat model. Users can be tracked through changing names by other users and the FBI can get members' phones.**

While Signal [claimed a few years ago](https://signal.org/bigbrother/santaclara/) all it could provide law enforcement was "Unix timestamps for when each account was created and the date that each account last connected to the Signal service. That’s it." in reality, there's far more information about accounts in identifiers it possesses, and that its server uses, and some is accessible to users as well.

Anyone in or invited to a group can get ID's for all members that Signal or AWS can obtain phone numbers for and can be linked to Apple/Google ID's and that will remain constant through username or display name changes. Some of this has been theorized before, but to prove the concept, here's a step by step guide:

01. Download Signal Desktop for Windows
02. Install it and link to your phone app
03. Quit signal (right-click on the tray icon and hit Quit. This is important!)
04. Download and unzip a current PowerShell from [https://github.com/PowerShell/PowerShell/releases/download/v7.5.4/PowerShell-7.5.4-win-x64.zip](https://github.com/PowerShell/PowerShell/releases/download/v7.5.4/PowerShell-7.5.4-win-x64.zip)
05. Right-click pwsh.exe and select run as administrator
06. Save [https://raw.githubusercontent.com/MatejKafka/PSSignalDecrypt/1c8aa1a4b5a29290f54dbd032c6228652aad8609/Unprotect-SignalConfig.ps1](https://raw.githubusercontent.com/MatejKafka/PSSignalDecrypt/1c8aa1a4b5a29290f54dbd032c6228652aad8609/Unprotect-SignalConfig.ps1) in the same folder as pwsh.exe
07. In your pwsh window, run `pwsh -ep bypass .\unprotect-signalconfig.ps1` which will show you your database key. Copy it by double-clicking the big string of letters and numbers then right-clicking.
08. Type `wsl --install Ubuntu` and hit enter then `wsl -d Ubuntu` and hit enter to install and start an Ubuntu Linux distribution
09. Type `sudo apt install sqlcipher jq -y` and hit enter to install the tools to query the database file
10. Type `read KEY` hit enter, then paste in your key from above and hit enter again
11. Paste the following and hit enter. This will spit out a list of all groups you are part of and all their member ID's and also save it in "convomembers.txt" by enumerating the mapping between ID and display names, known phone numbers, and about information, then listing all group members matching them to profile information:



    `for USER in $(ls /mnt/c/Users/);do DB=/mnt/c/Users/$USER/AppData/Roaming/Signal/sql/db.sqlite ;if [ -f $DB ] ;then declare -A mappings;while IFS= read LINE ;do SID=$(echo $LINE|tr "," "\n"|grep serviceId|awk -F'"' '{print $4}');if [ ! -z "$SID" ] ;then mappings["$SID"]="$LINE";fi;done < <(echo "PRAGMA key = \"x'$KEY'\"; select json from conversations where type = 'private';"|sqlcipher $DB|tail -n +2|jq -cr '.|{serviceId, name, e164, profileName, profileFamilyName, about}');echo "PRAGMA key = \"x'$KEY'\"; select json from conversations where type <> 'private';" | sqlcipher $DB | tail -n +2 | jq -r '.name, .membersV2[].aci' 2>/dev/null| while IFS= read -r LINE ; do if [[ -v mappings["$LINE"] ]]; then echo "${mappings["$LINE"]}";else echo -e "\n$LINE";fi;done;fi;done| tee convomembers.txt`



    You'll see output like this:

    ![](https://scriptjunkie.us/wp-content/uploads/2026/01/signal-dump.png)

    Here, the three members of a group named "The Jedi Council" are listed. While the display name and about are the same as those visible in the signal UI, we can also see the "serviceID" which is the account ID for each.



    Not shown here, but you can also identify which accounts are admins by grabbing the membersV2 array for a group conversation and looking for those serviceID's with a role of 2. (Above we simply grabbed all ID's).
12. Take the convo's and people you care about, and note their serviceID's.

Now what?

Grabbing the account data from Signal either directly or via the cloud provider they rely on ( [AWS](https://www.theverge.com/news/807147/signal-aws-outage-meredith-whittaker)) is trivial. The FBI can use National Security Letters, [as explained by the EFF](https://www.eff.org/issues/national-security-letters): "the FBI has issued hundreds of thousands of such letters seeking the private telecommunications and financial records of Americans without any prior approval from courts. In addition to this immense investigatory power, NSL statutes also permit the FBI to unilaterally gag recipients and prevent them from criticizing such actions publicly."

- Signal can do what the Signal Server does and do a simple DB query on their accounts table for the serviceId (a.k.a. aci or account id). This will return the account JSON for each. It will include a devices array which will include gcmId and/or apnId for each mobile device, and it will probably include [the phone number as well](https://github.com/signalapp/Signal-Server/blob/065e730200804c7899ac4458e3dbff82ef678c5c/service/src/main/java/org/whispersystems/textsecuregcm/storage/Account.java#L46-L47) (note how the number [provided to tests](https://github.com/signalapp/Signal-Server/blob/065e730200804c7899ac4458e3dbff82ef678c5c/service/src/test/java/org/whispersystems/textsecuregcm/storage/AccountTest.java#L81) is a plain phone number and that gets [directly set](https://github.com/signalapp/Signal-Server/blob/065e730200804c7899ac4458e3dbff82ef678c5c/service/src/test/java/org/whispersystems/textsecuregcm/tests/util/AccountsHelper.java#L40-L45) to [the number field](https://github.com/signalapp/Signal-Server/blob/065e730200804c7899ac4458e3dbff82ef678c5c/service/src/main/java/org/whispersystems/textsecuregcm/storage/Account.java#L175)).

  - This information is also likely cached in redis (see source analysis below).
  - It's a common task to grant access to an AWS hosted redis instances and probably trivial for Amazon to do so if they were served with an NSL, and not much more difficult to provide access to the underlying foundation DB as well.
  - So despite being apparently legally required, it's unlikely that Signal's cooperation would even be technically required here. Even if Signal might want to devote expensive time and resources to fight an NSL, they may never get the chance. It's worth noting that [AWS gets something like $10 billion from a single NSA contract alone](https://www.executivegov.com/articles/top-government-contracts-won-by-amazon-web-services).
- Google or Apple can then provide the phone number (and account owner name, email and likely location, birthday, payment details, etc.) for the gcmId or apnId respectively as well if the FBI wanted to pursue this avenue after obtaining them.

There are lots of other ways to get these ID's as well, including from mac or phones directly, but this is one convenient one.

Next, you can try changing your display name, about information, and username, or encouraging one of your contacts to do so. Then re-check any existing or new groups that are joined. You'll find the aci/serviceID remains the same. You can use this to track users even as they leave one chat, change username and display names, and join new chats.

If you are looking to maintain your own OPSEC, the most straightforward way to get a genuinely new identifier is to get a new phone with a new number and set up an entirely fresh Signal profile. But even this will not be secure against the FBI.

* * *

## Source analysis

Sending a group message starts from the server side with [/multi\_recipient](https://github.com/signalapp/Signal-Server/blob/065e730200804c7899ac4458e3dbff82ef678c5c/service/src/main/java/org/whispersystems/textsecuregcm/controllers/MessageController.java#L476-L503) which for normal group messages (not stories) end up here at [sendMultiRecipientMessage](https://github.com/signalapp/Signal-Server/blob/065e730200804c7899ac4458e3dbff82ef678c5c/service/src/main/java/org/whispersystems/textsecuregcm/controllers/MessageController.java#L562-L615) which does checkGroupSendToken to make sure the sender is part of the group and resolves recipients.

Resolving recipients is done by [MessageUtil.java](https://github.com/signalapp/Signal-Server/blob/065e730200804c7899ac4458e3dbff82ef678c5c/service/src/main/java/org/whispersystems/textsecuregcm/push/MessageUtil.java#L61-L77) which grabs the ServiceIdentifier (which is just a UUID via [ServiceIdentifier.java](https://github.com/signalapp/Signal-Server/blob/065e730200804c7899ac4458e3dbff82ef678c5c/service/src/main/java/org/whispersystems/textsecuregcm/identity/ServiceIdentifier.java#L81) corresponding to the serviceId's above) and calls [getByServiceIdentifierAsync](https://github.com/signalapp/Signal-Server/blob/065e730200804c7899ac4458e3dbff82ef678c5c/service/src/main/java/org/whispersystems/textsecuregcm/storage/AccountsManager.java#L1173-L1178) which can [check redis](https://github.com/signalapp/Signal-Server/blob/065e730200804c7899ac4458e3dbff82ef678c5c/service/src/main/java/org/whispersystems/textsecuregcm/storage/AccountsManager.java#L1244) then [getByAccountIdentifierAsync](https://github.com/signalapp/Signal-Server/blob/065e730200804c7899ac4458e3dbff82ef678c5c/service/src/main/java/org/whispersystems/textsecuregcm/storage/Accounts.java#L1177-L1180) which does the DB query.

Then it calls the inner [sendMultiRecipientMessage](https://github.com/signalapp/Signal-Server/blob/065e730200804c7899ac4458e3dbff82ef678c5c/service/src/main/java/org/whispersystems/textsecuregcm/controllers/MessageController.java#L661-L683) which calls messageSender's [sendMultiRecipientMessage](https://github.com/signalapp/Signal-Server/blob/065e730200804c7899ac4458e3dbff82ef678c5c/service/src/main/java/org/whispersystems/textsecuregcm/push/MessageSender.java#L186-L231) which gets service identifier and devices and which does pushNotificationManager.sendNewMessageNotification(account, deviceId, isUrgent) and [sendNewMessageNotification wraps sendNotification](https://github.com/signalapp/Signal-Server/blob/065e730200804c7899ac4458e3dbff82ef678c5c/service/src/main/java/org/whispersystems/textsecuregcm/push/PushNotificationManager.java#L49).

The notifications are scheduled by scheduleBackgroundNotification called by [sendNotification](https://github.com/signalapp/Signal-Server/blob/065e730200804c7899ac4458e3dbff82ef678c5c/service/src/main/java/org/whispersystems/textsecuregcm/push/PushNotificationManager.java#L103-L108).

Those notifications get processed by another thread, in sendBackgroundNotification which is called by [processScheduledBackgroundNotifications](https://github.com/signalapp/Signal-Server/blob/065e730200804c7899ac4458e3dbff82ef678c5c/service/src/main/java/org/whispersystems/textsecuregcm/push/PushNotificationScheduler.java#L305-L314) tokenType is APN or FCM final String pushToken = getPushToken(tokenType, device); ... sender.sendNotification(new PushNotification(pushToken, tokenType, PushNotification.NotificationType.NOTIFICATION, null, account, device, false)

[getPushToken](https://github.com/signalapp/Signal-Server/blob/065e730200804c7899ac4458e3dbff82ef678c5c/service/src/main/java/org/whispersystems/textsecuregcm/push/PushNotificationScheduler.java#L444) returns case FCM -> device.getGcmId(); case APN -> device.getApnId(); which are [private strings](https://github.com/signalapp/Signal-Server/blob/065e730200804c7899ac4458e3dbff82ef678c5c/service/src/main/java/org/whispersystems/textsecuregcm/storage/Device.java#L58-L62)

* * *

also, likewise with individual messages:

called by various methods including [sendNewMessageNotification](https://github.com/signalapp/Signal-Server/blob/065e730200804c7899ac4458e3dbff82ef678c5c/service/src/main/java/org/whispersystems/textsecuregcm/push/PushNotificationManager.java#L49)

called by MessageSender's [sendMessages](https://github.com/signalapp/Signal-Server/blob/065e730200804c7899ac4458e3dbff82ef678c5c/service/src/main/java/org/whispersystems/textsecuregcm/push/MessageSender.java#L110-L132)

called by [sendIndividualMessage](https://github.com/signalapp/Signal-Server/blob/065e730200804c7899ac4458e3dbff82ef678c5c/service/src/main/java/org/whispersystems/textsecuregcm/controllers/MessageController.java#L388-L446)

This entry was posted on January 29, 2026, 5:52 am and is filed under [Uncategorized](https://scriptjunkie.us/category/uncategorized/). You can follow any responses to this entry through [RSS 2.0](https://scriptjunkie.us/2026/01/tracking-signal-identifiers/feed/ "RSS 2.0").
You can skip to the end and leave a response. Pinging is currently not allowed.

1. No comments yet.

[Cancel Reply](https://scriptjunkie.us/2026/01/tracking-signal-identifiers/#respond)

Name (required)

E-Mail (required) _(will not be published)_

Website

Δ

Submit Comment
