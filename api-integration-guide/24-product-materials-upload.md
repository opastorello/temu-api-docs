# Product Materials Upload

**Last update:** 2025-01-26 12:01:47

---

# 
Image Upload

**API**

`/api/galerie/v3/store_image`

**Format**

form-data

**Input Parameters**

| 

**Parameter Name**
 | 

**Type**
 | 

**Required**
 | 

**Description**
 
| 

image
 | 

file
 | 

Yes
 | 

The image to be uploaded (currently supports jpg, jpeg, gif, png, webp, bmp)
 
| 

upload_sign
 | 

string
 | 

Yes
 | 

The signature obtained from the signature retrieval interface. Refer to `bg.local.goods.gallery.signature.get` for the retrieval method.
 

**Return Values**

| 

**Parameter Name**
 | 

**Type**
 | 

**Description**
 
| 

url
 | 

string
 | 

The URL to download the image (if signing is required, it will be the signed URL)
 
| 

etag
 | 

string
 | 

The unique identifier of the image (not guaranteed to be md5!!!!)
 
| 

error_code
 | 

int
 | 

(Not specified in the original document)
 

**Code Example**

JavaScript

```
var form = new FormData();
form.append("upload_sign", "${signature}");
form.append("image", document.getElementById("image").files[0]);

var settings = {
  "url": "http://${endpoint}/api/galerie/v3/store_image",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "multipart/form-data"
  },
  "processData": false,
  "mimeType": "multipart/form-data",
  "contentType": false,
  "data": form
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

cURL

```
curl --location --request POST 'http://${endpoint}/api/galerie/v3/store_image' \
--header 'Content-Type: multipart/form-data' \
--form 'upload_sign=${signature}' \
--form 'image=@/xxx/xxx.png' \
```

# 
Video Upload

## 
**General Video Upload API**

For videos of 20MB or less, use this API.

**API**

`api/galerie/v1/store_video`

**Format**

POST form-data

**Request Parameters**

| 

**Parameter Name**
 | 

**Type**
 | 

**Description**
 | 

**Required**
 
| 

file
 | 

file
 | 

The file to be uploaded
 | 

Yes
 
| 

sign
 | 

string
 | 

The signature obtained from the signature API. For obtaining the signature, refer to `bg.local.goods.gallery.signature.get`
 | 

Yes
 
| 

create_media
 | 

boolean
 | 

Whether to create a media resource for the uploaded file (enable video transcoding by setting to true). The file type must be video. Otherwise, an error will be returned.
 | 

No
 

**Response Parameters**

| 

**Parameter Name**
 | 

**Type**
 | 

**Description**
 
| 

url
 | 

string
 | 

The URL to download the video (if signature is required, it will be the signed URL)
 
| 

etag
 | 

string
 | 

The etag of the video file (not guaranteed to be md5!!!!)
 
| 

vid
 | 

string
 | 

The vid corresponding to the created video resource
 
| 

error_code
 | 

int
 | 

Not returned if successful
 
| 

error_msg
 | 

string
 | 

Error message (not an int as stated in the original document)
 

## 
**Chunked Video Upload API**

For videos larger than 20MB, use this API.

**API**

`/api/galerie/large_file/v1/video/upload_init`

**Format**

POST JSON

**Input Parameters**

| 

**Parameter Name**
 | 

**Type**
 | 

**Description**
 | 

**Required**
 
| 

sign
 | 

string
 | 

Signature
 | 

Yes
 
| 

content_type
 | 

string
 | 

The contentType corresponding to the file, which must be a video type
 | 

Yes
 
| 

create_media
 | 

boolean
 | 

Whether to create media resources for the uploaded file. (Set to true)
 | 

No
 

**Return Values**

| 

**Parameter Name**
 | 

**Type**
 | 

**Description**
 
| 

sign
 | 

string
 | 

Marks the ID of this large file upload
 

## 
**Chunked Upload**

**API**

`/api/galerie/large_file/v1/video/upload_part`

**Format**

POST form-data

**Input Parameters**

| 

**Parameter Name**
 | 

**Type**
 | 

**Description**
 | 

**Required**
 
| 

sign
 | 

string
 | 

Marks the ID of this large file upload (returned during the init phase)
 | 

Yes
 
| 

part_num
 | 

string
 | 

The current chunk number, starting from 1
 | 

Yes
 
| 

part_file
 | 

file
 | 

The content of the current chunk file
 | 

Yes
 

**Return Values**

| 

**Parameter Name**
 | 

**Type**
 | 

**Description**
 
| 

uploaded_part_num
 | 

int
 | 

Represents the part number successfully uploaded this time
 
| 

error_code
 | 

int
 | 

Returned when failed
 
| 

error_msg
 | 

string
 | 

Returned when failed
 

## 
**Complete Chunked Upload**

**API**

`/api/galerie/large_file/v1/video/upload_complete`

**Format**

POST JSON

**Input Parameters**

| 

Parameter Name
 | 

Type
 | 

Description
 | 

Required
 
| 

sign
 | 

string
 | 

Marks the ID of this large file upload (returned during the init phase)
 | 

Yes
 

**Return Values**

| 

Parameter Name
 | 

Type
 | 

Description
 
| 

url
 | 

string
 | 

Download URL
 
| 

vid
 | 

string
 | 

The vid corresponding to the created video resource (only returned when integrated with multimedia file processing)
 
# 
General File Upload

**API**

/api/galerie/general_file

**ContentType**

form-data

**Input Parameters**

| 

Parameter Name
 | 

Type
 | 

Description
 | 

Required
 
| 

file
 | 

file
 | 

The file to be uploaded
 | 

Yes
 
| 

sign
 | 

string
 | 

The signature obtained from the signature API. Please refer to `bg.local.goods.gallery.signature.get` for details on how to obtain it
 | 

Yes
 

**Return Values**

| 

Parameter Name
 | 

Type
 | 

Description
 
| 

url
 | 

string
 | 

The URL to download the image (if CDN signing is required, it will be the signed URL)
 
| 

md5
 | 

string
 | 

The MD5 hash of the image
 
| 

error_code
 | 

int
 | 

Error code (if any)
 

**Code Example**

JavaScript

```
var form = new FormData();
form.append("sign", "${signature}");
form.append("file", document.getElementById("file").files[0]);

var settings = {
  "url": "http://${endpoint}/api/galerie/general_file",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "multipart/form-data"
  },
  "processData": false,
  "mimeType": "multipart/form-data",
  "contentType": false,
  "data": form
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

cURL

```
curl --location --request POST 'http://${endpoint}/api/galerie/general_file' \
--header 'Content-Type: multipart/form-data' \
--form 'sign=${signature}' \
--form 'file=xxx.txt' \
```

# 
Large File Upload

## 
Initialization of Chunked Upload 

**API**

/api/galerie/cos_large_file/upload_init

**Input Parameters**

| 

Parameter Name
 | 

Type
 | 

Description
 | 

Required
 
| 

upload_sign
 | 

string
 | 

The signature obtained from the signature API. Please refer to `bg.local.goods.gallery.signature.get` for details on how to obtain it. The signature obtained will expire within 5 minutes before calling the init method, and 12 hours after calling the init method.
 | 

Yes
 

**Code Example**

JavaScript

```
var settings = {
  "url": "https://${endpoint}/api/galerie/cos_large_file/upload_init",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json"
  },
  "data": JSON.stringify({"upload_sign":"${signature}","file_name":"xxx.mp4","content_type":"video/mp4"}),
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

cURL

```
curl --location --request POST 'https://${endpoint}/api/galerie/cos_large_file/upload_init' \
--header 'Content-Type: application/json' \
--data-raw '{"upload_sign":"${signature}","file_name":"xxx.mp4","content_type":"video/mp4"}'
```

## 
Upload Part 

**API**

/api/galerie/cos_large_file/upload_part

**Input Parameters**

| 

Parameter Name
 | 

Type
 | 

Description
 | 

Required
 
| 

upload_sign
 | 

string
 | 

The signature obtained from the signature API. Please refer to `bg.local.goods.gallery.signature.get` for details on how to obtain it.
 | 

Yes
 
| 

total_part_num
 | 

string
 | 

Each part request can carry multiple part contents, and this parameter indicates the total number of parts in this part request. Each part in the request corresponds to a part_numx, part_filex, content_md5x, where x starts from 1.
 | 

Yes
 
| 

part_num1
 | 

string
 | 

The number "1" in the key of the parameter "part_num1" indicates the number of the current part in this part request. The parameter represents the part number (relative to the entire large file, also starting from 1).
 | 

Yes
 
| 

part_file1
 | 

string
 | 

The file content of the part. It supports a maximum of 10,000 parts, each with a size of 5MB to 5GB. The last part can be less than 5MB. Similarly, the number "1" in the parameter "part_file1" indicates the number of the current part in this part request. We allow a part request to carry multiple parts.
 | 

Yes
 

**Example**

There is a 30MB large file, and we set the part size to 10MB, so the total number of parts is 3.

Method 1: Each part request carries only one part, so there are a total of three part requests.

```
First part request
total_part_num: 1
part_num1: 1
part_file1: {Content of Part 1}
content_md51: {MD5 of Part 1}
Second part request
total_part_num: 1
part_num1: 2
part_file1: {Content of Part 2}
content_md51: {MD5 of Part 2}
Third part request
total_part_num: 1
part_num1: 3
part_file1: {Content of Part 3}
content_md51: {MD5 of Part 3}
```

Method 2: One of the part requests carries two parts, so there are a total of two part requests.

```
First part request
total_part_num: 2
part_num1: 1
part_file1: {Content of Part 1}
content_md51: {MD5 of Part 1}
part_num2: 2
part_file2: {Content of Part 2}
content_md52: {MD5 of Part 2}
Second part request
total_part_num: 1
part_num1: 3
part_file1: {Content of Part 3}
content_md51: {MD5 of Part 3}
```

**Code Example**

JavaScript

```
var form = new FormData();
form.append("upload_sign", "${signature}");
form.append("total_part_num", "1");
form.append("part_num1", "1");
form.append("part_file1", sliced_file);

var settings = {
  "url": "https://${endpoint}/api/galerie/cos_large_file/upload_part",
  "method": "POST",
  "timeout": 0,
  "processData": false,
  "mimeType": "multipart/form-data",
  "contentType": false,
  "data": form
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

cURL

```
curl --location --request POST 'https://${endpoint}/api/galerie/cos_large_file/upload_part' \
--header 'Content-Type: multipart/form-data' \
--form 'upload_sign=${signature}' \
--form 'total_part_num=1' \
--form 'part_num1=1' \
--form 'part_file1=/xxx/xxx.mp4'
```

## 
Complete Part 

**API**

/api/galerie/cos_large_file/upload_complete

**Input Parameters**

| 

Parameter Name
 | 

Type
 | 

Description
 | 

Required
 
| 

upload_sign
 | 

string
 | 

The signature obtained from the signature API. Please refer to `bg.local.goods.gallery.signature.get` for details on how to obtain it.
 | 

Yes
 

**Code Example**

JavaScript

```
var settings = {
  "url": "https://${endpoint}/api/galerie/cos_large_file/upload_complete",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json"
  },
  "data": JSON.stringify({"upload_sign":"${signature}"}),
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

cURL

```
curl --location --request POST 'https://${endpoint}/api/galerie/cos_large_file/upload_complete' \
--header 'Content-Type: application/json' \
--data-raw '{"upload_sign": "${signature}"}'
```
