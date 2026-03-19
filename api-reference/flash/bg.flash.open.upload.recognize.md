# bg.flash.open.upload.recognize

**Kaiping real-time image acquisition test result interface**

For large merchants (10,000+ products), the cost of uploading pictures one by one is too high. We provide API and allow merchants to connect with their own ERP systems.

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
| clientId | 4 | No |  |  |
| uploadImageList | 8 | No |  |  |
| skuSame | 5 | No |  |  |
| spuId | 2 | No |  |  |
| skuId | 2 | No |  |  |

## Response Parameters

| Parameter | Type | Required | Description | Example |
|---|---|---|---|---|
| result | 6 | No |  |  |
| success | 5 | No |  |  |
| errorCode | 1 | No |  |  |
| errorMsg | 4 | No |  |  |

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "access_token" : "test",
  "app_key" : "test",
  "clientId" : "test",
  "uploadImageList" : [ {
    "image" : "test",
    "position" : 1
  } ],
  "sign" : "test",
  "data_type" : "test",
  "skuSame" : true,
  "spuId" : 1,
  "type" : "test",
  "version" : "test",
  "skuId" : 1,
  "timestamp" : "test"
}'
```

## Response Example

```json
{
  "result" : {
    "ruleCheckResult" : [ {
      "ruleStatus" : 1,
      "ruleName" : "test"
    } ],
    "checkResult" : true
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```