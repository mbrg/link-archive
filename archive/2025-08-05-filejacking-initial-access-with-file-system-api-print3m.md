---
date: '2025-08-05'
description: The research outlines the exploitation of the File System API in Chromium-based
  browsers for initial access and file backdooring. The key functions, `showOpenFilePicker`,
  `showSaveFilePicker`, and `showDirectoryPicker`, enable unauthenticated file manipulation
  without user awareness, focusing on sensitive file types and paths. No Mark of the
  Web (MotW) bypass was found, raising concerns about the API's security implications.
  Notably, users can be tricked into interacting with malicious files or directories,
  effectively allowing remote file system manipulation, enhancing social engineering
  attack vectors. Recommendations include monitoring for abuse and refining web security
  protocols to mitigate risks.
link: https://print3m.github.io/blog/filejacking-initial-access-with-file-system-api
tags:
- Web Security
- Initial Access
- Browser Exploitation
- Malware Development
- File System API
title: FileJacking – Initial Access with File System API ◆ Print3M
---

[All posts](https://print3m.github.io/)

# FileJacking – Initial Access with File System API

Created at: 2025-08-04

TL;DR:

- Smuggling technique via File System API
- Backdooring files directly from a browser
- Reading, creating, removing folders and files directly from a browser
- No MotW bypass

## Introduction

The **File System API** is a browser API that allows web apps to do some local file system operations such as direct file editing, saving, and directory access. It was introduced by Google in 2020. Currently, it is **supported by Chromium-based browsers**: Chrome, Edge, Opera, and Brave. It is not supported by **Firefox and Safari** due to ongoing security and privacy concerns. On MDN this API is marked as "experimental" and its behavior may change in the future.

> DISCLAIMER: This research was done in July 2025 on Windows 11 with Chrome and Edge browser. I didn't do any tests on any other Chromium-based browsers.

The File System API implements 4 interesting features that can be abused for initial access:

- `window.showOpenFilePicker()`
- `window.showSaveFilePicker()`
- `window.showDirectoryPicker()`
- `DataTransferItem.getAsFileSystemHandle()`

A few notes before you read on:

- I observed no MotW bypass during the research. All functions that allowed writing to a file during the first modification immediately added MotW.
- File System API is available on:
  - pages with TLS ( `https://***`)
  - local HTML files (e.g. `file:///Z:/index.html`). Sending `.html` implementing FileJacking via email attachement is possible.
- None of the File System API functions allow you to discover which path the user has chosen. You can only guess.
- I am not discussing here the social engineering tricks and aspects of using FileJacking.
- Once a website has access to the directory / file, it can interact with them "in the background", even if the user is not currently active on the page.
- I don't show here all possible file operations. They are very simple and well documented: [file write](https://developer.mozilla.org/en-US/docs/Web/API/FileSystemWritableFileStream), [file read](https://developer.mozilla.org/en-US/docs/Web/API/FileSystemFileHandle), [directory operations](https://developer.mozilla.org/en-US/docs/Web/API/FileSystemDirectoryHandle).

## showOpenFilePicker()

This function opens File Explorer and allows you to select one or more files. Then you can request access to edit the files (popup) and continue editing them without the user's knowledge.

Example usage:

```MDRenderer_code___eFJE
// 1. Open file explorer and select a file(s)
const [fileHandle] = await showOpenFilePicker({
    startIn: "desktop"
});

// 2. Grant write permission [popup]
const writable = await fileHandle.createWritable();
await writable.write("lorem ipsum")
await writable.close();
```

It is possible to read and edit any file(s) - e.g. DLL, EXE, MSI - with restrictions:

- The file cannot come from `RESTRICTED-PATHS-2` (see below).
- The LNK cannot point to the binary in `RESTRICTED-PATHS-2`. If the LNK does not point to a restricted path, then you can edit the LNK structures as any other file. But if it points to a file in a restricted path, then the LNK is magically resolved and the browser returns an restriction error. Very strange.

> **NOTE**: It's not possible to rename or remove the file after creation.

Restricted path demo:

An interesting feature of this function is `types` property. It allows you to write something in File Explorer popup (bottom-right corner), and force user to select only files we are interested in. Using `excludeAcceptAllOption: true` you hide "All types" option in the dropdown menu. This label can serve as a credibility factor in a social engineering context.

```MDRenderer_code___eFJE
showOpenFilePicker({
    types: [\
        {\
            description: "THIS IS CONTROLLED", // <--- HERE\
            accept: { "*/*": [".dll", ".chm"] },\
        },\
    ]
    excludeAcceptAllOption: true,
});
```

![Controlled label in File Explorer](https://print3m.github.io/imgs/filejacking-initial-access-with-file-system-api/label-shown.png)

Another interesting feature is `startIn` property. This property allows you to define which folder File Explorer should open by default. The possible values are limited to the following: `desktop`, `documents`, `downloads`, `music`, `pictures`, `videos`. These are the default directories in the current user context. This allows you to better guide the user to where they should look.

**Abuse idea**: Trick a user to "upload" or "select" some file and edit it without user's knowledge. Use some container file ( `.7z`, `.zip`) and override them with your files. Use EXE, DLL or any application config file and backdoor it. This operation looks like uploading but it allows us to modify the file.

## showSaveFilePicker()

This function opens File Explorer and allows you to save a file, change it's name, extension and location. It creates the file on a disk, then you can edit the file without the user's knowledge.

Example usage:

```MDRenderer_code___eFJE
// 1. Open file explorer and select where to save the file
//    (the name is already suggested in the explorer)
//    [warning popup]
const fileHandle = await window.showSaveFilePicker({
    suggestedName: "test.dll",
    startIn: "desktop"
});

// 2. Write to file [no popup]
const writable = await fileHandle.createWritable();
await writable.write("lorem ipsum");
await writable.close();
```

It is possible to create any file (e.g. DLL, EXE, LNK, MSI) with two restrictions:

- The file with the extension from `WARNING-EXTENSIONS` (see below) list triggers warning popup but it's still possible to create it.
- The file cannot be created in `RESTRICTED-PATHS-2` (see below).

> **NOTE**: It's not possible to rename or remove the file after creation via JS.

This functions implements the same `types` and `startIn` property as described in `showOpenFilePicker()`. It also implements `suggestedName: string` property which allows us to control the default name (including the extension) of the file that will be created. This value can be changed by the user in File Explorer window.

**It is worth noting that the file created this way does not appear in the download history!** Additional icon appears on the left side of the URL bar, which indicates just what item the current page is accessing and allows you to revoke the access. It works the same way for opening directories which I describe below.

What a standard download looks like...

![Download history](https://print3m.github.io/imgs/filejacking-initial-access-with-file-system-api/download-history.png)

... and the File System API "download" (this popup doesn't show up automatically, you have to click on the icon):

![File System API icon](https://print3m.github.io/imgs/filejacking-initial-access-with-file-system-api/fs-api-icon.png)

**Abuse idea**: It's like a classic "download" mechanism on steroids. It doesn't show any artifact in "download history" menu. It allows you to modify the file after it has been created. Use it as a clever smuggling technique, maybe bypassing some detection?

## showDirectoryPicker()

This function opens File Explorer and allows you to select a directory in `readwrite` mode. After selecting a folder, a confirmation pop-up appears in the browser. Then you can create, edit and delete files and child directories in the selected directory without user's knowledge.

Example usage:

```MDRenderer_code___eFJE
// 1. Open file explorer and select a directory
// 2. Grant "readwrite" permission [popup]
const dirHandle = await window.showDirectoryPicker({
    mode: "readwrite",
    startIn: "desktop"
});

// 3. Create a new file [no popup]
const fileHandle = await dirHandle.getFileHandle("test.chm", { create: true });

// 4. Write to file [no popup]
const writable = await fileHandle.createWritable();
await writable.write("lorem ipsum");
await writable.close();
```

There are restrictions on the use of this function:

- The paths that we can open with this feature are quite limited. All allowed and not allowed paths are described in `RESTRICTED-PATHS-1` (see below).
- There is a short list of files that we cannot create, read, or modify: `RESTRICTED-EXTENSIONS` (see below).

This functions implements the same `startIn` property as described in `showOpenFilePicker()`. Creating files and subfolders also doesn't generate any visible artifacts in the user interface or “download history”.

**Abuse idea**:

1. With just 2 clicks it gives you access to the entire directory and all of its subdirectories. Perhaps there is a custom folder (not on the blacklist) that you know exists in the organization and would like to access it. Trick the user to give it to you, read and modify files and look for a way to persist.
2. Trick user it's a new fancy "download" mechanism and use it as a clever smuggling technique. Remember, you have the entire directory for yourself. It's a bit like a container (e.g. `zip`, `.7z`) without using the container.

## DataTransferItem.getAsFileSystemHandle()

Some other browser APIs create a [DataTransferItem](https://developer.mozilla.org/en-US/docs/Web/API/DataTransferItem) object. If `DataTransferItem` is a file or directory (it doesn't have to be, you always need to check `DataTransferItem.kind`), you can call the `.getAsFileSystemHandle()` method on it. This method returns us a handle to this item in the file system. Then, we request `readwrite` access to the object, which opens a confirmation pop-up in the browser.

As of today, there are 3 known browser APIs that use `DataTransferItem`:

- [HTML Drag and Drop API](https://developer.mozilla.org/en-US/docs/Web/API/HTML_Drag_and_Drop_API)
- [Clipboard API](https://developer.mozilla.org/en-US/docs/Web/API/Clipboard_API)
- [UI Events: InputEvent](https://developer.mozilla.org/en-US/docs/Web/API/InputEvent/dataTransfer)

This list of APIs may be extended in the future. I will focus on Drag and Drop and Clipboard API because I didn't find a way to use the filesystem item in InputEvent API.

Example usage of Drag and Drop API (works by dropping file or directory onto the page):

```MDRenderer_code___eFJE
addEventListener("drop", async (e) => {
    // 1. Fire "drop" event by dropping file(s) or dir(s) [no popup]
    const [item] = e.dataTransfer.items;
    const fileHandle = await item.getAsFileSystemHandle();

    if (handle.kind === "directory") {
        // Same thing as in showDirectoryPicker() example
    } else {
        // 2. Grant "readwrite" permission [popup]
        await fileHandle.requestPermission({ mode: "readwrite" });

        // 3. Write to file [no popup]
        const writable = await fileHandle.createWritable();
        await writable.write(content);
        await writable.close();
    }
});
```

Example usage of Clipboard API (works by "ctrl + v" pasting file or directory when the page is focused):

```MDRenderer_code___eFJE
addEventListener("paste", async (e) => {
    // 1. Fire "paste" event by "ctrl + v" [no popup]
    const [item] = e.clipboardData.items;
    const fileHandle = await item.getAsFileSystemHandle();

    // Everything else is the same as for "drop" event...
});
```

Dropping / pasting directory works exactly the same as `showDirectoryPicker()`. It has exactly the same restrictions and behaviors, I haven't noticed any differences. Please refer to the above.

Dropping / pasting file works uniquely. **There are no restrictions.** Nothing. Zero. Null. Nein. You can drop / paste an LNK, DLL, EXE from any location you want (as long as your Windows account has permission to this location of course), read and modify them.

**Abuse idea**:

1. Same as for `showDirectoryPicker()`, but you have a different way of interacting with the user. Dragging or pasting a directory may justify other social engineering scenarios.
2. It's obvious. Backdoor some LNK with it. "This is your helpdesk, here's a new smart update mechanism, you have to just drop a program icon here and confirm the popup", whoops...

Here's a small Proof-of-Concept how to execute browser-based backdooring: [_FileJacking-PoC (GitHub)_](https://github.com/Print3M/FileJacking-PoC)

## Restrictions

![FileJacking cheat sheet](https://print3m.github.io/imgs/filejacking-initial-access-with-file-system-api/filejacking-cheat-sheet.png)

**NOTE**: The lists I present here are the result of my research. I have not found any documentation explaining why these extensions or paths are blocked while others are not.

The [W3C specification](https://wicg.github.io/file-system-access/) only mentions [certain possible threats and provides a list of suggested sensitive directories](https://wicg.github.io/file-system-access/#wellknowndirectory-too-sensitive-or-dangerous).

Sometimes writing to a file blocks Google Safe Browsing, but I don't really know how it works. I didn't focus on it too much. The user doesn't get any information. The programmer gets an exception that they can handle. I don't think this mechanism is a reliable security measure.

### RESTRICTED-EXTENSIONS

- Chrome: `.dll`, `.lnk`, `.scf`, `.url`
- Edge: `.dll`, `.drv`, `.gadget`, `.grp`, `.hta`, `.lnk`, `.ocx`, `.scf`, `.sys`, `.url`, `.xbap`
- Other: not tested.

> I tested it against 141 extensions form this [amazing list](https://docs.google.com/spreadsheets/d/1alEKmI7oUlyed7rLH4ymSnX2CD9GxYshGq5qKMXFCGI/edit?gid=0#gid=0) . The list is always the same. During testing, I did not observe any discrepancies within the same browser. Why do these extensions differ between browsers? I have no idea. You can test it on your browser using the following snippet:

```MDRenderer_code___eFJE
for (const ext of extensions) {
    try {
        await dirHandle.getFileHandle(name, {
            create: true,
        });
    } catch (err) {
        if (err instanceof TypeError) {
            console.error("Extension not allowed:", ext);
        } else {
            console.error(`Error: [${ext}]`, err);
        }
    }
}
```

### WARNING-EXTENSIONS

These extensions cause a warning pop-up to appear, which you can accept or reject. I don't really know what the full list of these extensions looks like, because I haven't found any other method than manually saving a file via File Explorer with each extension to check it.

I was too lazy to check all of them but the list must be much broader than `RESTRICTED-EXTENSIONS` because `EXE` and `CHM` are behind the popup too.

It's safe to say that if you're saving something shady, you'll probably get that popup, but you need to check to be sure.

### RESTRICTED-PATHS-1

> I assume that the following list is not complete. It is the result of my manual checking directory by directory. I tested mainly on Chrome. I didn't notice discrepancies between browsers, but that doesn't mean they aren't there.

**Not allowed**:

- current `\desktop` folder (regardless if default or OneDrive)
- current `\documents` folder (regardless if default or OneDrive)
- current `\downloads` folder (regardless if default or OneDrive)
- `C:\`
- `C:\Program Files\*`
- `C:\Program Files (x86)\*`
- `C:\ProgramData\*`
- `%APPDATA%\*`
- `%LOCALAPPDATA%\*`
- `%TEMP%\*`
- `%CommonProgramFiles%\*`
- `C:\Users\<user>\`

**Allowed**:

- Subdirectories of current `\desktop`
- Subdirectories of current `\documents`
- Subdirectories of current `\downloads`
- If not set as a current active (e.g. if the default `\desktop` folder is switched to OneDrive the old one is allowed):
  - `C:\Users\<user>\Desktop`
  - `C:\Users\<user>\Documents`
  - `C:\Users\<user>\Downloads`
- `C:\inetpub\*`
- `C:\PerfLogs\*`
- Custom directories in `C:\*`
- `C:\Windows\*`
- `%PUBLIC%\*`
- `C:\Users\Default\*`
- `C:\Users\<user>\Contacts`
- `C:\Users\<user>\Favorites`
- `C:\Users\<user>\Links`
- `C:\Users\<user>\Pictures`
- `C:\Users\<user>\Music`
- `C:\Users\<user>\Searches`
- `C:\Users\<user>\Videos`
- Root directories other than `C:\` (e.g. `D:\`, `Z:\`)

### RESTRICTED-PATHS-2

**Not allowed**:

- `C:\`
- `C:\Program Files\*`
- `C:\Program Files (x86)\*`
- `C:\ProgramData\*`
- `C:\Users\`
- `C:\Windows\`
- `%CommonProgramFiles%\*`
- `%TEMP%\*`
- `%LOCALAPPDATA%\*`
- `%APPDATA%\*`

**Allowed**:

- All allowed from `RESTRICTED-PATHS-1`
- `desktop\*`
- `documents\*`
- `downloads\*`
- `C:\Users\<user>\`

## Resources

- [https://developer.chrome.com/docs/capabilities/web-apis/file-system-access](https://developer.chrome.com/docs/capabilities/web-apis/file-system-access)
- [https://developer.mozilla.org/en-US/docs/Web/API/File\_System\_API](https://developer.mozilla.org/en-US/docs/Web/API/File_System_API)
- [https://developer.mozilla.org/en-US/docs/Web/API/HTML\_Drag\_and\_Drop\_API](https://developer.mozilla.org/en-US/docs/Web/API/HTML_Drag_and_Drop_API)
