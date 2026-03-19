# bg.arbok.open.cert.queryNeedUploadItems

**bg.arbok.open.cert.queryNeedUploadItems**

￼External key customers have their own development capabilities and can call APIs to query the content to be uploaded

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
| productId | 2 | No |  |  |
| certType | 1 | No |  |  |

## Response Parameters

| Parameter | Type | Required | Description | Example |
|---|---|---|---|---|
| success | 5 | No |  |  |
| errorCode | 1 | No |  |  |
| errorMsg | 4 | No |  |  |
| result | 6 | No |  |  |

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "access_token" : "test",
  "certType" : 1,
  "app_key" : "test",
  "productId" : 1,
  "sign" : "test",
  "data_type" : "test",
  "type" : "test",
  "version" : "test",
  "timestamp" : "test"
}'
```

## Response Example

```json
{
  "result" : {
    "certNeedUploadItems" : [ {
      "aliasName" : "test",
      "hasExpireTime" : true,
      "expireDays" : 1,
      "needShowCustomer" : true,
      "expireTime" : 1,
      "expireType" : 1,
      "expireNoticeDays" : 1,
      "contentType" : 1
    } ]
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```