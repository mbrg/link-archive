---
date: '2025-07-26'
description: A recent security analysis disclosed a vulnerability in Microsoft's Copilot
  Enterprise, featuring a Jupyter Notebook sandbox. The exploit involves executing
  arbitrary commands by leveraging the user `ubuntu`, which possesses sudo privileges
  absent of the sudo binary. The security risk stems from a loop in the entrypoint
  script that executes `pgrep` without a full path, allowing manipulation via writable
  directories in the `$PATH`. Although access to the system was gained, it was ultimately
  non-productive, classifying this as a moderate severity vulnerability, which has
  since been patched by Microsoft.
link: https://research.eye.security/how-we-rooted-copilot/
tags:
- Python Sandbox
- Cybersecurity
- Microsoft Copilot
- Vulnerability Assessment
- Jupyter Notebook
title: How we Rooted Copilot - Eye Research
---

Manage Consent

To provide the best experiences, we use technologies like cookies to store and/or access device information. Consenting to these technologies will allow us to process data such as browsing behavior or unique IDs on this site. Not consenting or withdrawing consent, may adversely affect certain features and functions.

FunctionalFunctional
Always active

The technical storage or access is strictly necessary for the legitimate purpose of enabling the use of a specific service explicitly requested by the subscriber or user, or for the sole purpose of carrying out the transmission of a communication over an electronic communications network.

PreferencesPreferences

The technical storage or access is necessary for the legitimate purpose of storing preferences that are not requested by the subscriber or user.

StatisticsStatistics

The technical storage or access that is used exclusively for statistical purposes.The technical storage or access that is used exclusively for anonymous statistical purposes. Without a subpoena, voluntary compliance on the part of your Internet Service Provider, or additional records from a third party, information stored or retrieved for this purpose alone cannot usually be used to identify you.

MarketingMarketing

The technical storage or access is required to create user profiles to send advertising, or to track the user on a website or across several websites for similar marketing purposes.

[Manage options](https://research.eye.security/sharepoint-under-siege/#cmplz-manage-consent-container) [Manage services](https://research.eye.security/sharepoint-under-siege/#cmplz-cookies-overview) [Manage {vendor\_count} vendors](https://research.eye.security/sharepoint-under-siege/#cmplz-tcf-wrapper) [Read more about these purposes](https://cookiedatabase.org/tcf/purposes/)

AcceptDenyView preferencesSave preferences [View preferences](https://research.eye.security/sharepoint-under-siege/#cmplz-manage-consent-container)

[Privacy Statement](https://www.eye.security/privacy) [{title}](https://research.eye.security/how-we-rooted-copilot/#)

[![Eye Research](https://research.eye.security/wp-content/uploads/eye-Research-w-v4@4x.png)](https://research.eye.security/)[![Eye Research](https://research.eye.security/wp-content/uploads/eye-Research-w-v4_1@4x.png)](https://research.eye.security/)

[eye.security](https://www.eye.security/) [About the Product](https://www.eye.security/solutions/managed-xdr) [Partner Portal](https://info.eye.security/en/partner/gateway) [Customer Portal](https://portal.eye.security/)

[← Return to overview](https://research.eye.security/how-we-rooted-copilot/#)

# How we Rooted Copilot

Jul 25, 2025

![Vaisha Bernard](https://secure.gravatar.com/avatar/8f581a3cfc77da6775c6e6668d76c3e36358a49e5d87fdd7c87f68f3588be064?s=150&d=identicon&r=g)

By: Vaisha Bernard

Microsoft has silently pushed an update back in April 2025 for Copilot Enterprise, enabling a live Python sandbox running Jupyter Notebook that can execute code in the backend. Well, that sounds like a terrific idea, let’s explore it for a bit!

It turns out to be easy to have it execute exactly the code we want to on the underlying system using Jupyter Notebook syntax `%command`.

![Screenshot showing environment variables output in Jupyter Notebook after executing the command '%env'.](https://i0.wp.com/research.eye.security/wp-content/uploads/image-47.png?resize=934%2C883&ssl=1)

Well, it worked most of the time. It feels like telling an 8-year-old child to do something. If it’s in a good mood (probably because it just had an ice cream), Copilot enthusiastically complies, but if it is hungry, it starts to become reluctant or passive-aggressively explains you how the world works according to its vision.

![Screenshot showing an explanation of the %env command in a Jupyter Notebook interface, with examples of listing, setting, and retrieving environment variables.](https://i0.wp.com/research.eye.security/wp-content/uploads/image-57.png?resize=816%2C566&ssl=1)

Increasing our frustration tolerance by having some ice cream ourselves, we explore further. It seems to be executing Linux commands as the ‘ubuntu’ user in a miniconda environment. Funny thing is that the user `ubuntu` is in the `sudo` group, but there is no sudo binary on the filesystem. Copilot also seems to understand that and assists us with some context.

![Screenshot of output from the Copilot environment showing the results of executing the 'id' command, displaying user and group IDs for the 'ubuntu' user.](https://i0.wp.com/research.eye.security/wp-content/uploads/image-48.png?resize=736%2C194&ssl=1)

It uses quite a similar model as the ChatGPT sandbox, but with a newer kernel version. And Python version 3.12, where ChatGPT is still running Python 3.11 (at least in April 2025).

![Output display of the command 'uname -a' executed successfully in Copilot, showing system information.](https://i0.wp.com/research.eye.security/wp-content/uploads/image-49.png?resize=746%2C152&ssl=1)

The main functionality of the sandbox is running Jupyter Notebooks, together with a Tika server.

![Command line output showing various processes running in a Linux environment related to Jupyter, Go applications, and system scripts.](https://i0.wp.com/research.eye.security/wp-content/uploads/image-52.png?resize=586%2C666&ssl=1)

The container does seem to have a link-local network interface next to its loopback interface, limited to a /32 netmask and route.

![Output of the command /sbin/ifconfig executed in a Python interpreter, showing network interface details like IP address, netmask, and packet statistics.](https://i0.wp.com/research.eye.security/wp-content/uploads/image-53.png?resize=667%2C412&ssl=1)

We can see that it is using an OverlayFS filesystem that originates in some /legion file system path on the container host system.

![Output of the command mount executed in the Python interpreter showing overlay filesystem details and mount options.](https://i0.wp.com/research.eye.security/wp-content/uploads/image-55.png?resize=740%2C595&ssl=1)

Most custom scripts are located in the `/app` directory.

![Output of the command 'ls -al /app' executed in the Python interpreter, showing file details such as permissions, owner, group, size, and modification date.](https://i0.wp.com/research.eye.security/wp-content/uploads/image-50.png?resize=744%2C475&ssl=1)

After executing a lot of commands, it starts to really be in the mood to help out. It is then even possible to simply ask to download files or tar entire folders and provide them for download. Definitely don’t try this as the first command in a fresh session. It will throw a tantrum!

It does still somehow feel the need to corrupt any binary data. Another passive-aggressive trait? Text files or command output work fine though, so base64 encoding binary files before downloading them works. Most of the time.

It copies files to a working directory at `/mnt/data`, from where they can be picked up outside of the sandbox with a link that looks like `blob:https://outlook.office.com/<guid>`.

![Screenshot showing a chat interface with a message from Copilot stating that the user can download the file 'generateLicense.py' and including a link for the download.](https://i0.wp.com/research.eye.security/wp-content/uploads/image-54.png?resize=567%2C197&ssl=1)

The `goclientapp` binary in `/app` is a Go binary that is the interface into this container. It opens a web server on port 6000 that listens for POST requests to the `/execute` endpoint. These POST requests come in as a very simple JSON, for example after asking it to execute the `%env` command, this JSON came in.

```
{"code":"%env"}
```

The `goclientapp` binary then executes the code in the Jupyter notebook environment and we get the output. There is also a `httpproxy` go binary, that seems to function as an HTTP proxy for outgoing web traffic originating from the Jupyter environment. The container did not enable any outgoing traffic (and `ENABLE_EGRESS` was false), so this binary was probably there for a future update which would potentially allow outgoing HTTP traffic.

An interesting script is `entrypoint.sh` in the `/app` directory. This seems to be the script that is executed as the entrypoint into the container, so this is running as root.

![A shell script for setting up the Jupyter environment, handling environment variables, and configuring HTTP proxy settings to allow the execution of services in a container.](https://i0.wp.com/research.eye.security/wp-content/uploads/image-58.png?resize=747%2C1024&ssl=1)

As can been seen in line 42 and 55, the `httpproxyapp` and the `goclientapp` drop privileges and run as the `ubuntu` user. But in line 45 we see the `keepAliveJupyterSvc.sh` being started as root.

Exciting! Let’s dive in.

![A bash script that initializes and starts a Jupyter notebook server in a Linux environment, checking available kernels and managing service status.](https://i0.wp.com/research.eye.security/wp-content/uploads/image-56.png?resize=941%2C1001&ssl=1)

Most further commands on line 10, 32 and 35 are run with dropped privileges. But can you spot the potential vulnerability?

Have a look at line 28 of the script, where the script is executing the following `pgrep` command.

```
JUPYTER_PID=$(pgrep -f "jupyter notebook --ip=0.0.0.0 --port=8888")
```

As this part of the script is in a ‘while true’ loop, this part will be executed every two seconds. The command `pgrep` is executing without a full path, which means the script will search all directories in the `$PATH` variable for the existence of `pgrep`. Going back to the output of the `%env` command, we see that the `$PATH` variable is populated with some custom paths.

```
PATH=/home/ubuntu/snenv/bin:/app/miniconda/condabin:/home/ubuntu/.cache/ms-playwright:
/home/ubuntu/snenv/bin:/app/miniconda/bin:/usr/bin/gcc:/usr/local/sbin:/usr/local/bin:
/usr/sbin:/usr/bin:/sbin:/bin
```

Iterestingly, the `/app/miniconda/bin` is writable for the `ubuntu` user and is listed before `/usr/bin`, where pgrep resides. And the root user has the same directory in the `$PATH`, before `/usr/bin`.

We can now create a file in `/app/minicoda/bin` that looks like this.

```
#!/home/ubuntu/snenv/bin/python
import os
with open('/mnt/data/in','r') as fin:
  with open('/mnt/data/out','a') as fout:
    fout.write(os.popen(fin.read()).read())
print('1')
```

This small Python script checks for the existence of a file `/mnt/data/in`, reads the input, executes it with `popen`, and writes the output to `/mnt/data/out`. We upload it to Copilot by attaching it to a message, which puts the script in `/mnt/data/pgrep.py` and have Copilot do the rest.

![Screenshot showing a Copilot interface executing a series of commands using Jupyter Notebook syntax in a Python environment.](https://i0.wp.com/research.eye.security/wp-content/uploads/3.png?resize=824%2C459&ssl=1)

Now what have we gained with root access to the container?

Absolutely nothing!

We can now use this access to explore parts of the container that were previously inaccessible to us. We explored the filesystem, but there were no files in /root, no interesting logging to find, and a container breakout looked out of the question as every possible known breakout had been patched.

But at least we had fun!

We reported the vulnerability to Microsoft in April and they have since fixed it as a moderate severity vulnerability. As only important and critical vulnerabilities qualify for a bounty award, we did not receive anything, except for an acknowledgement on the [Security Researcher Acknowledgments for Microsoft Online Services](https://portal.msrc.microsoft.com/en-us/security-guidance/researcher-acknowledgments-online-services) webpage.

Want to know how we also got access to the Responsible AI Operations control panel, where we could administer Copilot and 21 other internal Microsoft services?

Come see our talk [Consent & Compromise: Abusing Entra OAuth for Fun and Access to Internal Microsoft Applications](https://www.blackhat.com/us-25/briefings/schedule/#consent--compromise-abusing-entra-oauth-for-fun-and-access-to-internal-microsoft-applications-45128) at BlackHat USA 2025, Thursday August 7th at 1:30 PM in Las Vegas.

### **Timeline**

April 18th 2025 – Vulnerability reported to MSRC

July 25th 2025 – MSRC notifies that the issue has been fixed

July 25th 2025 – MSRC closes the case as a moderate severity vulnerability

July 25th 2025 – Blog published

### About Eye Security

We are a European cybersecurity company focused on 24/7 threat monitoring, incident response, and cyber insurance. Our research team performs proactive scans and threat intelligence operations across the region to defend our customers and their supply chains.

Learn more at [https://eye.security/](https://eye.security/) and [follow us on LinkedIn](https://www.linkedin.com/company/eyesecurity/) to help us spread the word.

[“Master” Malware – a new C2 framework](https://research.eye.security/master-malware-a-new-c2-framework/ "“Master” Malware &#8211; a new C2 framework")

[SharePoint 0-day uncovered (CVE-2025-53770)](https://research.eye.security/sharepoint-under-siege/ "SharePoint 0-day uncovered (CVE-2025-53770)")

[8Base Ransomware Recovery: Key and File Retrieval](https://research.eye.security/8base-ransomware-recovery-key-and-file-retrieval/ "8Base Ransomware Recovery: Key and File Retrieval")

Share this article.

## Related articles **.**

![](https://i0.wp.com/research.eye.security/wp-content/uploads/critical_zero_day_vulnerability_red_16x9_3.jpg?fit=768%2C432&ssl=1)

→

[SharePoint 0-day uncovered (CVE-2025-53770)](https://research.eye.security/sharepoint-under-siege/ "SharePoint 0-day uncovered (CVE-2025-53770)")

## [SharePoint 0-day uncovered (CVE-2025-53770)](https://research.eye.security/sharepoint-under-siege/)

From SOC Alert Triage to 0-day Mass Exploitation On the evening of July 18, 2025, Eye Security was…

- [Tech blog](https://research.eye.security/category/blog/)

![](https://i0.wp.com/research.eye.security/wp-content/uploads/sneaky2fa-emerging-cyber-threat-make-an-image-of-a-user.png?fit=768%2C576&ssl=1)

→

[Sneaky2FA: Use This KQL Query to Stay Ahead of the Emerging Threat](https://research.eye.security/sneaky2fa-use-this-kql-query-to-stay-ahead-of-the-emerging-threat/ "Sneaky2FA: Use This KQL Query to Stay Ahead of the Emerging Threat")

## [Sneaky2FA: Use This KQL Query to Stay Ahead of the Emerging Threat](https://research.eye.security/sneaky2fa-use-this-kql-query-to-stay-ahead-of-the-emerging-threat/)

Challenges in business are a given, but it’s our response to them that defines our trajectory. Looking beyond the immediate obstacle, there lies a realm of opportunity and learning.

- [Tech blog](https://research.eye.security/category/blog/)

![](https://i0.wp.com/research.eye.security/wp-content/uploads/picture3.jpg?fit=768%2C501&ssl=1)

→

[8Base Ransomware Recovery: Key and File Retrieval](https://research.eye.security/8base-ransomware-recovery-key-and-file-retrieval/ "8Base Ransomware Recovery: Key and File Retrieval")

## [8Base Ransomware Recovery: Key and File Retrieval](https://research.eye.security/8base-ransomware-recovery-key-and-file-retrieval/)

Every business has a unique potential waiting to be tapped. Recognizing the keys to unlock this growth can set an enterprise on the path to unprecedented success.

- [Tech blog](https://research.eye.security/category/blog/)

![](https://i0.wp.com/research.eye.security/wp-content/uploads/picture1.jpg?fit=768%2C577&ssl=1)

→

[This Is How Threat Actors Use OneDrive Compromise to Infect Local Windows Hosts](https://research.eye.security/this-is-how-threat-actors-use-onedrive-compromise-to-infect-local-windows-hosts/ "This Is How Threat Actors Use OneDrive Compromise to Infect Local Windows Hosts")

## [This Is How Threat Actors Use OneDrive Compromise to Infect Local Windows Hosts](https://research.eye.security/this-is-how-threat-actors-use-onedrive-compromise-to-infect-local-windows-hosts/)

In the ever-evolving world, the art of forging genuine connections remains timeless. Whether it’s with colleagues, clients, or partners, establishing a genuine rapport paves the way for collaborative success.

- [Tech blog](https://research.eye.security/category/blog/)

Manage consent

[Toggle photo metadata visibility](https://research.eye.security/how-we-rooted-copilot/#)
