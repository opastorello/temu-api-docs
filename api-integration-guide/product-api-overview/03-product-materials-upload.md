# Product Materials Upload

**Last update:** 2025-01-26 12:01:47

All file uploads require a signature first. Obtain the signature via: `bg.local.goods.gallery.signature.get`

---

## Image Upload

**API:** `/api/galerie/v3/store_image`
**Format:** POST `form-data`

### Input Parameters

| Parameter Name | Type | Required | Description |
|---|---|---|---|
| `image` | file | Yes | Image to upload (jpg, jpeg, gif, png, webp, bmp) |
| `upload_sign` | string | Yes | Signature from `bg.local.goods.gallery.signature.get` |

### Return Values

| Parameter Name | Type | Description |
|---|---|---|
| `url` | string | URL to download the image (signed URL if signing required) |
| `etag` | string | Unique identifier of the image (NOT guaranteed to be md5) |
| `error_code` | int | Error code (if any) |

### Code Example

```javascript
// JavaScript
var form = new FormData();
form.append("upload_sign", "${signature}");
form.append("image", document.getElementById("image").files[0]);

var settings = {
  "url": "http://${endpoint}/api/galerie/v3/store_image",
  "method": "POST",
  "headers": { "Content-Type": "multipart/form-data" },
  "processData": false,
  "mimeType": "multipart/form-data",
  "contentType": false,
  "data": form
};
$.ajax(settings).done(function (response) { console.log(response); });
```

```bash
# cURL
curl --location --request POST 'http://${endpoint}/api/galerie/v3/store_image' \
--header 'Content-Type: multipart/form-data' \
--form 'upload_sign=${signature}' \
--form 'image=@/xxx/xxx.png'
```

---

## Video Upload

### General Video Upload API

For videos **20MB or less**.

**API:** `api/galerie/v1/store_video`
**Format:** POST `form-data`

#### Request Parameters

| Parameter Name | Type | Required | Description |
|---|---|---|---|
| `file` | file | Yes | File to upload |
| `sign` | string | Yes | Signature from `bg.local.goods.gallery.signature.get` |
| `create_media` | boolean | No | Set to `true` to enable video transcoding |

#### Response Parameters

| Parameter Name | Type | Description |
|---|---|---|
| `url` | string | URL to download the video (signed URL if required) |
| `etag` | string | Etag of the video file (NOT guaranteed to be md5) |
| `vid` | string | The vid of the created video resource |
| `error_code` | int | Not returned if successful |
| `error_msg` | string | Error message |

---

### Chunked Video Upload API

For videos **larger than 20MB**. Three-step process: init → upload parts → complete.

#### Step 1: Initialize Upload

**API:** `/api/galerie/large_file/v1/video/upload_init`
**Format:** POST JSON

| Parameter | Type | Required | Description |
|---|---|---|---|
| `sign` | string | Yes | Signature |
| `content_type` | string | Yes | ContentType of the file (must be a video type) |
| `create_media` | boolean | No | Set to `true` to create media resources |

**Return:** `sign` — ID marking this large file upload.

#### Step 2: Upload Chunks

**API:** `/api/galerie/large_file/v1/video/upload_part`
**Format:** POST `form-data`

| Parameter | Type | Required | Description |
|---|---|---|---|
| `sign` | string | Yes | ID from init phase |
| `part_num` | string | Yes | Chunk number, starting from 1 |
| `part_file` | file | Yes | Content of the current chunk |

**Return:** `uploaded_part_num`, `error_code`, `error_msg`

#### Step 3: Complete Upload

**API:** `/api/galerie/large_file/v1/video/upload_complete`
**Format:** POST JSON

| Parameter | Type | Required | Description |
|---|---|---|---|
| `sign` | string | Yes | ID from init phase |

**Return:** `url` (download URL), `vid` (video resource ID)

---

## General File Upload

For instruction manuals and certification files **under 20MB**.

**API:** `/api/galerie/general_file`
**ContentType:** `form-data`

### Input Parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| `file` | file | Yes | File to upload |
| `sign` | string | Yes | Signature from `bg.local.goods.gallery.signature.get` |

### Return Values

| Parameter | Type | Description |
|---|---|---|
| `url` | string | Download URL (signed URL if CDN signing required) |
| `md5` | string | MD5 hash of the file |
| `error_code` | int | Error code (if any) |

### Code Example

```javascript
// JavaScript
var form = new FormData();
form.append("sign", "${signature}");
form.append("file", document.getElementById("file").files[0]);

var settings = {
  "url": "http://${endpoint}/api/galerie/general_file",
  "method": "POST",
  "headers": { "Content-Type": "multipart/form-data" },
  "processData": false,
  "mimeType": "multipart/form-data",
  "contentType": false,
  "data": form
};
$.ajax(settings).done(function (response) { console.log(response); });
```

```bash
# cURL
curl --location --request POST 'http://${endpoint}/api/galerie/general_file' \
--header 'Content-Type: multipart/form-data' \
--form 'sign=${signature}' \
--form 'file=xxx.txt'
```

---

## Large File Upload (Certification Files > 20MB)

### Step 1: Initialize Chunked Upload

**API:** `/api/galerie/cos_large_file/upload_init`

| Parameter | Type | Required | Description |
|---|---|---|---|
| `upload_sign` | string | Yes | Signature (expires within 5 minutes before calling init, valid 12 hours after init) |

```bash
curl --location --request POST 'https://${endpoint}/api/galerie/cos_large_file/upload_init' \
--header 'Content-Type: application/json' \
--data-raw '{"upload_sign":"${signature}","file_name":"xxx.mp4","content_type":"video/mp4"}'
```

### Step 2: Upload Parts

**API:** `/api/galerie/cos_large_file/upload_part`

| Parameter | Type | Required | Description |
|---|---|---|---|
| `upload_sign` | string | Yes | Signature |
| `total_part_num` | string | Yes | Total number of parts in this request |
| `part_num1` | string | Yes | Part number (relative to entire file, starts from 1) |
| `part_file1` | file | Yes | Content of the part. Max 10,000 parts, each 5MB–5GB; last part can be < 5MB |

**Multi-part per request example (30MB file, 10MB parts):**

```
# Method 1: One part per request (3 requests total)
First request: total_part_num=1, part_num1=1, part_file1=...
Second request: total_part_num=1, part_num1=2, part_file1=...
Third request: total_part_num=1, part_num1=3, part_file1=...

# Method 2: Multiple parts in one request (2 requests total)
First request: total_part_num=2, part_num1=1, part_file1=..., part_num2=2, part_file2=...
Second request: total_part_num=1, part_num1=3, part_file1=...
```

### Step 3: Complete Upload

**API:** `/api/galerie/cos_large_file/upload_complete`

| Parameter | Type | Required | Description |
|---|---|---|---|
| `upload_sign` | string | Yes | Signature |

```bash
curl --location --request POST 'https://${endpoint}/api/galerie/cos_large_file/upload_complete' \
--header 'Content-Type: application/json' \
--data-raw '{"upload_sign": "${signature}"}'
```
