---
title: "TrustedSec | Hunting Deserialization Vulnerabilities With Claude"
tags:
   - MCP
   - exploit
   - vulnerabilities
   - dotnet
   - deserialization
link: https://trustedsec.com/blog/hunting-deserialization-vulnerabilities-with-claude
date: 2025-07-20
summary: "The blog post details the use of an MCP (Model Context Protocol) server to leverage AI, specifically Claude, for identifying deserialization vulnerabilities in .NET assemblies. It guides the setup of an MCP server via Docker and demonstrates how to detect known vulnerabilities, such as unsafe deserialization in `AddinUtil.exe`. The AI successfully maps attack paths and can generate proof-of-concept exploit code. Future exploration will aim at automating this analysis at scale, presenting potential implications for mitigating .NET security risks more efficiently. The approach highlights the evolving role of AI in cybersecurity vulnerability assessment and exploitation."
---

- [Blog](https://trustedsec.com/blog)
- [Hunting Deserialization Vulnerabilities With Claude](https://trustedsec.com/blog/hunting-deserialization-vulnerabilities-with-claude)

June 12, 2025

# Hunting Deserialization Vulnerabilities With Claude

Written by
James Williams


Artificial Intelligence (AI)

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/HuntingDeserializationVulnsClaude_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1749496812&s=3a91953a1f0c944dd6788fe2226c512b)

Table of contents

- [Setup](https://trustedsec.com/blog/hunting-deserialization-vulnerabilities-with-claude#Setup)
- [Finding Existing Vulnerabilities](https://trustedsec.com/blog/hunting-deserialization-vulnerabilities-with-claude#vulnerabilities)
- [Finding New Vulnerabilities](https://trustedsec.com/blog/hunting-deserialization-vulnerabilities-with-claude#newvulnerabilities)
- [Final Thoughts](https://trustedsec.com/blog/hunting-deserialization-vulnerabilities-with-claude#Final)

Share

- [Share URL](https://trustedsec.com/blog/hunting-deserialization-vulnerabilities-with-claude "Share URL")
- [Share via Email](mailto:?subject=Check%20out%20this%20article%20from%20TrustedSec%21&body=Hunting%20Deserialization%20Vulnerabilities%20With%20Claude%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fhunting-deserialization-vulnerabilities-with-claude "Share via Email")
- [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fhunting-deserialization-vulnerabilities-with-claude "Share on Facebook")
- [Share on X](http://twitter.com/share?text=Hunting%20Deserialization%20Vulnerabilities%20With%20Claude%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fhunting-deserialization-vulnerabilities-with-claude "Share on X")
- [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fhunting-deserialization-vulnerabilities-with-claude&mini=true "Share on LinkedIn")

In this post, we are going to look at how we can find zero-days in .NET assemblies using Model Context Protocol (MCP).

## Setup

Before we can start vibe hacking, we need an MCP that will allow Claude to disassemble .NET assemblies. Reversing a .NET binary is normally something I would do with [**dotPEAK**](https://www.jetbrains.com/decompiler/); however, this is a Windows-only tool. Luckily for us, [ilspycmd](https://github.com/icsharpcode/ILSpy) exists and can be run on Mac/Linux. The [ilspycmd-docker](https://github.com/berdav/ilspycmd-docker/tree/main) repository provides a Dockerfile for ilspycmd, but the current version on GitHub is a few years out of date and won’t build.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/HuntingDeserialVulnsClaude_Williams/Fig01_Williams_VulnsWithClaude.png?w=320&q=90&auto=format&fit=max&dm=1749527487&s=8ab9469644ed9fa0573c6767f6c004f1)Figure 1 - Build Error for ilspycmd-docker

Luckily, the error message is quite explicit about the problem, and a small change to the Dockerfile will fix the problem.

```hljs bash
FROM mcr.microsoft.com/dotnet/sdk:8.0

RUN useradd -m -s /bin/bash ilspy
USER ilspy

WORKDIR /home/ilspy

RUN dotnet tool install -g ilspycmd

RUN echo 'export PATH="$PATH:/home/ilspy/.dotnet/tools/"' >> /home/ilspy/.bashrc

ENTRYPOINT [ "/bin/bash", "-l", "-c" ]
```

We can build this new image with the following command:

```hljs undefined
docker build -t ilspycmd .
```

With our Dockerfile updated and our container built, we can build a simple MCP server using Python. We’ll use the same framework as shown in our [previous blog that discusses building an MCP server](https://trustedsec.com/blog/teaching-a-new-dog-old-tricks-phishing-with-mcp).

```hljs python
from mcp.server.fastmcp import FastMCP
import subprocess
import os

server = FastMCP("ilspy docker")

@server.prompt()
def setup_prompt() -> str:
    return """
    You can use the following commands to decompile .NET assemblies, using ilspy:
    - decompile(file: str, output_folder: str) -> int: Decompile the file at the provided path.
    The returned value is the success code, with 0 indicating a successful run
    """

@server.tool()
def run_ilspycmd_docker(exe_path, output_folder) -> int:
    """
    Run ilspycmd in a Docker container to decompile a DLL

    Args:
        dll_path (str): Path to the DLL file to decompile
        output_folder (str): Folder where decompiled code will be placed

    Returns:
        tuple: (return_code, stdout, stderr)
    """
    # Get absolute paths
    input_dir = os.path.abspath(os.path.dirname(exe_path))
    output_dir = os.path.abspath(output_folder)
    exe_filename = os.path.basename(exe_path)

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Create input directory inside container
    container_input_dir = "/decompile_in"
    container_output_dir = "/decompile_out"

    ilspy_cmd_path = "/home/ilspy/.dotnet/tools/ilspycmd"
    ilspy_command = f"{ilspy_cmd_path} -p -o {container_output_dir} {container_input_dir}/{exe_filename}"

    # Build the Docker command
    docker_cmd = [\
        "docker", "run", "--rm",\
        "-v", f"{input_dir}:{container_input_dir}",\
        "-v", f"{output_dir}:{container_output_dir}",\
        "ilspycmd",\
        ilspy_command\
    ]

    # Run the command
    process = subprocess.run(
        docker_cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    return process.returncode

if __name__ == "__main__":
    # Initialize and run the server
    server.run(transport='stdio')
```

This is a little more complicated than the example in our [previous blog](https://trustedsec.com/blog/teaching-a-new-dog-old-tricks-phishing-with-mcp), but at a higher level, we’ll use some file paths to run a Docker command. Next, we’ll edit the **_claude\_desktop\_config.json_** file and add our new MCP server. It will look something like this:

```hljs json
{
    "mcpServers": {
        "FS": {
            "command": "/Users/james/Library/Python/3.9/bin/uv",
            "args": [\
                "--directory",\
                "/Users/james/Research/MCP/FS",\
                "run",\
                "FS.py"\
            ]
        },
        "brave-search": {
      "command": "docker",
      "args": [\
        "run",\
        "-i",\
        "--rm",\
        "-e",\
        "BRAVE_API_KEY",\
        "mcp/brave-search"\
      ],
      "env": {
        "BRAVE_API_KEY": "try_harder"
      }
    },
    "ilspy": {
            "command": "/Users/james/Library/Python/3.9/bin/uv",
            "args": [\
                "--directory",\
                "/Users/james/Research/MCP/ilspy_docker",\
                "run",\
                "ilspy.py"\
            ]
        }
    }
}
```

After restarting Claude for Desktop, we should see that our MCP server is now available.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/HuntingDeserialVulnsClaude_Williams/Fig02_Williams_VulnsWithClaude.png?w=320&q=90&auto=format&fit=max&dm=1749527489&s=d28b823f33f6c14b62e569c3ddfbd415)Figure 2 - MCP Server Available

## Finding Existing Vulnerabilities

Now, let's see if Claude can find a known vulnerability. In September 2023, [Blue-Prints Blog](https://www.blue-prints.blog/content/blog/posts/lolbin/addinutil-lolbas.html) posted about an insecure deserialization in **_AddinUtil.exe_**, a .NET binary that ships with Windows by default. This binary has also been added to the [LOLBAS project](https://lolbas-project.github.io/lolbas/Binaries/Addinutil/). Note that if you want to follow along at home, you’ll need the [MCP servers we created in this blog](https://trustedsec.com/blog/teaching-a-new-dog-old-tricks-phishing-with-mcp).

This vulnerability is interesting because the unsafe deserialization happens in a DLL, but the entry point is in an .EXE. First, we’ll see if Claude can find the vulnerable code in the DLL. Let’s start by checking if Claude recognizes the new MCP server.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/HuntingDeserialVulnsClaude_Williams/Fig03_Williams_VulnsWithClaude.png?w=320&q=90&auto=format&fit=max&dm=1749527490&s=c2b4162c38350a53db058768f5294d59)Figure 3 - Confirming Claude can Decompile .NET Binaries

Next, we tell Claude to decompile and review **System.AddIn.dll**.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/HuntingDeserialVulnsClaude_Williams/Fig04_Williams_VulnsWithClaude.png?w=320&q=90&auto=format&fit=max&dm=1749527491&s=fb1093448b9f36b6836c269f8d2f45fe)Figure 4 - Telling Claude to Review the DLL

Eventually, Claude comes back with a list of potential vulnerabilities, including an unsafe deserialization call in .NET remoting due to the use of **TypeFilterLevel.Full**.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/HuntingDeserialVulnsClaude_Williams/Fig05_Williams_VulnsWithClaude.png?w=320&q=90&auto=format&fit=max&dm=1749527492&s=c349fd547ead1614fb40f48bef5d406d)Figure 5 - Deserialization Identified in .NET Remoting

This is likely related to the functionality used by **_AddinProcess.exe_**, which contains a .NET remoting vulnerability identified by [Nettitude](https://github.com/nettitude/Aladdin).

We want to focus on deserialization flaws, so we adjust our prompt and try again.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/HuntingDeserialVulnsClaude_Williams/Fig06_Williams_VulnsWithClaude.png?w=320&q=90&auto=format&fit=max&dm=1749527493&s=c6f2dd0cba362ce8f8adcb6fdbd193c1)Figure 6 - Adjusted Prompt

This also failed to find the known vulnerability. Now, let’s Claude ask which files have been reviewed.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/HuntingDeserialVulnsClaude_Williams/Fig07_Williams_VulnsWithClaude.png?w=320&q=90&auto=format&fit=max&dm=1749527494&s=52dd8e12f66dbcb95bdea1bddbf65965)Figure 7 - Claude Listing 14 Reviewed Files

Luckily, Claude will usually tell us the truth when asked, so let’s ask why it has only reviewed 14 files.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/HuntingDeserialVulnsClaude_Williams/Fig08_Williams_VulnsWithClaude.png?w=320&q=90&auto=format&fit=max&dm=1749527496&s=ce8d16f551296dce7881c8418eee749a)Figure 8 - Claude's Confession

After confirming that we want it to review all of the files, Claude finally identifies the known vulnerability.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/HuntingDeserialVulnsClaude_Williams/Fig09_Williams_VulnsWithClaude.png?w=320&q=90&auto=format&fit=max&dm=1749527497&s=0f37345ef665f69ab3dcb799a767029f)Figure 9 - Claude Identifies the Unsafe Deserialize Call

It also recognizes that the cache file is potentially untrusted.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/HuntingDeserialVulnsClaude_Williams/Fig10_Williams_VulnsWithClaude.png?w=320&q=90&auto=format&fit=max&dm=1749527498&s=cacf6026b3b3020d7026b26441ee055d)Figure 10 - Claude Recognizing the Cache File is Untrusted

So far, so good. Now we want to see if Claude is effective enough to find the actual exploit path from **_AddinUtil.exe_** to the unsafe deserialize call.

We’re going to give Claude a little guidance here and tell it that the DLL is referenced by **_AddinUtil.exe_**. We could get Claude to figure this out by itself, but that will be the subject of a future post.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/HuntingDeserialVulnsClaude_Williams/Fig11_Williams_VulnsWithClaude.png?w=320&q=90&auto=format&fit=max&dm=1749527499&s=29c9dc7a604fa2ceaeff88e633a64ccf)Figure 11 - Telling Claude to Identify Paths to the Unsafe Code

After a little thinking, Claude successfully identifies the possible entry points, including the **_pipelineroot_** flag, which is mentioned in the Blue-Prints Blog post as another path to a deserialize call.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/HuntingDeserialVulnsClaude_Williams/Fig12_Williams_VulnsWithClaude.png?w=320&q=90&auto=format&fit=max&dm=1749527500&s=c8ada39a23c2bb24007ab0728d25252d)Figure 12 - Claude Identifies Entry Points

Claude also correctly identifies the attack path.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/HuntingDeserialVulnsClaude_Williams/Fig13_Williams_VulnsWithClaude.png?w=320&q=90&auto=format&fit=max&dm=1749527501&s=89d00cff6a34d56d297ad14fbef9c23e)Figure 13 - Claude Identifies Attack Path

Time to push our luck and see if Claude can figure out how to build an exploit for this vulnerability. For those who didn’t read the [Blue-Prints Blog](https://www.blue-prints.blog/content/blog/posts/lolbin/addinutil-lolbas.html), **_AddinUtil.exe_** expects the cache file to contain a specific series of bytes which precede the data that is deserialized. Let’s see if Claude can figure this out.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/HuntingDeserialVulnsClaude_Williams/Fig14_Williams_VulnsWithClaude.png?w=320&q=90&auto=format&fit=max&dm=1749527502&s=5179f7d5f89cc391e09af344824719d5)Figure 14 - Prompting Claude to Build a Proof-of-Concept Tool

The generated code, which I won’t reproduce in full here, references the fact that we need to create the store file in a format expected by **_ReadCache_**.

```hljs lua
# Create the AddIns.store file with the format expected by ReadCache<T> print("[+] Creating malicious AddIns.store file")
cache_file_path = os.path.join(output_dir, "AddIns.store")

with open(cache_file_path, 'wb') as f:
    # Write the format version (int32 = 1)
    f.write(struct.pack("<i", 1))
    # Write the payload size (int64)
    f.write(struct.pack("<q", len(payload_data)))
    Write the payload data
    f.write(payload_data)
```

We can get Claude to explain its choice here, just to see if it understands the exploit code.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/HuntingDeserialVulnsClaude_Williams/Fig15_Williams_VulnsWithClaude.png?w=320&q=90&auto=format&fit=max&dm=1749527503&s=d7616bdec1544cf5550ff3787e2898bd)Figure 15 - Claude Correctly Identifying the Padding Needed

So, it correctly recognizes that we need to pad by 12 bytes but guesses at the purpose of those bytes. They are not used in the decompiled code, so it is impossible to determine their actual purpose.

## Finding New Vulnerabilities

Let’s see if Claude can identify the attack path for the **_pipelineroot_** flag, which wasn’t expanded on in the Blue-Prints Blog.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/HuntingDeserialVulnsClaude_Williams/Fig16_Williams_VulnsWithClaude.png?w=320&q=90&auto=format&fit=max&dm=1749527504&s=282644f1d57cecbb31b8b6087ff04725)Figure 16 - Prompting Claude to Generate a Proof of Concept for the pipelineroot Flag

After generating some Python code (included at end of this post), Claude gives a detailed explanation of the vulnerability.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/HuntingDeserialVulnsClaude_Williams/Fig17_Williams_VulnsWithClaude.png?w=320&q=90&auto=format&fit=max&dm=1749527505&s=e930e80573990c8f0602926a69414377)Figure 17 - Claude Explaining the pipelineroot Path

All that’s left to do is check Claude's work. We’ll use a simple **_ysoserial.net_** payload to pop **_calc.exe_** as our Proof-of-Concept payload, which we’ll use with the code generated by Claude.

```hljs python
ysoserial.exe -f BinaryFormatter -g TypeConfuseDelegate -c calc -o raw > e:\tools\payload.bin
```

We can then run the Proof-of-Concept code generated by Claude.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/HuntingDeserialVulnsClaude_Williams/Fig18_Williams_VulnsWithClaude.png?w=320&q=90&auto=format&fit=max&dm=1749527505&s=a98a0693e1ce0f7340a8751f87ebcefa)Figure 18 - Running the Proof-of-Concept Code

Running **_AddinUtil.exe_** with the generated **_-pipelineroot_** flag, perhaps unsurprisingly, didn’t work. Luckily, we can debug this quite easily with **_Visual Studio_** and **_dotPeek_**. First, we make sure **_dotPeek_** has the .EXE and DLL loaded, then we start its symbol server. Next, we decompile **_AddinUtil.exe_** using **_dotPeek_** and create a project file. We load this file into **_Visual Studio_**, then add **_dotPeek_** as a symbol server. Finally, we change the project debug options to start the compiled .EXE, so we can pass our **_pipelineroot_** flag as an argument.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/HuntingDeserialVulnsClaude_Williams/Fig19_Williams_VulnsWithClaude.png?w=320&q=90&auto=format&fit=max&dm=1749527506&s=8feaced70a1f050d299e34dda44d1d85)Figure 19 - Visual Studio Debug Options

Now, we can add a break point to the decompiled code, run the binary, and enjoy step-through debugging.

After a quick step-through, it becomes apparent that Claude had missed a step.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/HuntingDeserialVulnsClaude_Williams/Fig20_Williams_VulnsWithClaude.png?w=320&q=90&auto=format&fit=max&dm=1749527507&s=2d4e3c39297fc6a57a6139ae167e86a5)Figure 20 - AddIns.store File Check

Claude has neglected to create the **_AddIns_** directory and named the .store file something else, meaning this check failed and **_BuildAddInCache_** was never called. A quick update to the generated Python code resulted in a folder structure that passed all the checks and, when executed, popped **_calc.exe_**.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/HuntingDeserialVulnsClaude_Williams/Fig21_Williams_VulnsWithClaude.png?w=320&q=90&auto=format&fit=max&dm=1749527508&s=25fe16f6107c447a92ed9007971e10bb)Figure 21 - calc.exe Launched

This exploit isn’t as useful as the **_-AddinRoot_** flag because we need to drop a complete folder structure to disk. I haven’t seen a public implementation for this attack path yet, which makes it a good candidate for testing with Claude.

## Final Thoughts

In this post, we’ve seen how we can use an MCP server to give Claude the ability to analyze .NET assemblies. We’ve used that ability to find a known vulnerability in a Microsoft-signed binary and seen how we need to be explicit when giving Claude instructions (such as telling it to review every file). Finally, we’ve built a working Proof-of-Concept for an attack path mentioned in the original disclosure of this vulnerability, which was left as an exercise for the reader in the Blue-Prints blog.

While we had to give Claude a few hints along the way, this process of analyzing a file and getting close to a working exploit was much faster than what we could do manually. The next step will be to see if it’s possible to do this at scale, but that will be the subject of a future post.

The full Proof-of-Concept code can be found [here](https://gist.github.com/two06/cab20270db6b2f04c99a56956b5dffb2).

CloseShow Transcript
