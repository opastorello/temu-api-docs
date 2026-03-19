# bg.local.goods.image.upload

**Image material processing**

Image material processing

**Method:** POST  
**URL:** https://openapi-b-global.temu.com/openapi/router

---

## Common Parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| type | 4 | No |  |
| app_key | 4 | No |  |
| access_token | 4 | No |  |
| sign | 4 | No |  |
| timestamp | 4 | No |  |
| data_type | 4 | No |  |
| version | 4 | No |  |

## Request Parameters

| Parameter | Type | Required | Description | Example |
|---|---|---|---|---|
| fileUrl | 4 | No |  |  |
| scalingType | 1 | No |  |  |
| compressionType | 1 | No |  |  |
| formatConversionType | 1 | No |  |  |
| autoCrop | 5 | No |  |  |

## Response Parameters

| Parameter | Type | Required | Description | Example |
|---|---|---|---|---|
| success | 5 | No |  |  |
| errorCode | 1 | No |  |  |
| errorMsg | 4 | No |  |  |
| result | 6 | No |  |  |

## Error Codes

| Error Code | Message |
|---|---|
| 150011075 | When autoCrop is enabled, the image size must be no larger than {*}px. |
| 150011021 | Image upload timed out, please try again later |
| 150010003 | Invalid Request Parameters |
| 150010002 | System error, please try again later |

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "access_token" : "test",
  "app_key" : "test",
  "autoCrop" : true,
  "scalingType" : 1,
  "sign" : "test",
  "data_type" : "test",
  "fileUrl" : "test",
  "compressionType" : 1,
  "type" : "test",
  "version" : "test",
  "formatConversionType" : 1,
  "timestamp" : "test"
}'
```

## Response Example

```json
{
  "result" : {
    "autoCropUrls" : [ "test", "test" ],
    "url" : "test"
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```