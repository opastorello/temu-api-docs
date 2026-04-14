# temu.local.goods.image.v2.upload

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
| catId | 2 | No |  |  |
| usage | 1 | No |  |  |

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
| 150010002 | System error, please try again later |
| 150010003 | Invalid Request Parameters |
| 150010008 | Category not found |
| 150010005 | Try again later |
| 150011019 | The input {*}:{*} is incorrect, please modify it. |
| 150011021 | Image upload timed out, please try again later |
| 150011064 | The input {*} is incorrect, image exceeds {*}. |

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "access_token" : "test",
  "catId" : 1,
  "app_key" : "test",
  "usage" : 1,
  "sign" : "test",
  "data_type" : "test",
  "fileUrl" : "test",
  "type" : "test",
  "version" : "test",
  "timestamp" : "test"
}'
```

## Response Example

```json
{
  "result" : {
    "images" : [ {
      "url" : "test"
    } ]
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```