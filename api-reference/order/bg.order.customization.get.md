# bg.order.customization.get

**Query order customization information**

Self developed sellers and third-party ISVs obtain customized product content information in bulk through Open API

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
| orderSnList | 8 | No |  |  |

## Response Parameters

| Parameter | Type | Required | Description | Example |
|---|---|---|---|---|
| success | 5 | No |  |  |
| errorCode | 1 | No |  |  |
| errorMsg | 4 | No |  |  |
| result | 8 | No |  |  |

## Error Codes

| Error Code | Message |
|---|---|
| 120020001 | API service exception, please try again later. |
| 120020002 | Invalid request. |
| 120020003 | There are no orderSns in body. |
| 120020004 | The passed OrderSns value do not contain a custom type order. |
| 120020005 | OrderSns are invalid. |

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "access_token" : "test",
  "app_key" : "test",
  "sign" : "test",
  "data_type" : "test",
  "type" : "test",
  "version" : "test",
  "orderSnList" : [ "test", "test" ],
  "timestamp" : "test"
}'
```

## Response Example

```json
{
  "result" : [ {
    "templateType" : 1,
    "customizedSvgList" : [ {
      "compressedFileUrl" : "test"
    } ],
    "previewList" : [ {
      "customizedText" : "test",
      "previewType" : 1,
      "customizedAreaId" : "test",
      "imageUrl" : "test"
    } ],
    "customizedData" : "test",
    "orderSn" : "test",
    "customizedText" : "test",
    "templateId" : 1,
    "customizedType" : 1
  } ],
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```