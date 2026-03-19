# bg.local.goods.spec.id.get

**Search And Generate Merchant-Customized Specifications**

Search And Generate Merchant-Customized Specifications

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
| catId | 2 | No |  |  |
| parentSpecId | 2 | No |  |  |
| childSpecName | 4 | No |  |  |

## Response Parameters

| Parameter | Type | Required | Description | Example |
|---|---|---|---|---|
| result | 6 | No |  |  |
| success | 5 | No |  |  |
| errorCode | 1 | No |  |  |
| errorMsg | 4 | No |  |  |

## Error Codes

| Error Code | Message |
|---|---|
| 150010002 | System error, please try again later |
| 150010003 | Invalid Request Parameters |
| 150010005 | Try again later |
| 150010011 | Only use letters, numbers and common punctuation for product name |
| 150010027 | Variant too long |
| 150010124 | The catId not a leaf category |
| 150010125 | Non-existent parentSpecId |
| 150010044 | Special characters not allowed in text |
| 150010043 | Chinese characters not allowed in text |

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "access_token" : "test",
  "catId" : 1,
  "app_key" : "test",
  "parentSpecId" : 1,
  "sign" : "test",
  "data_type" : "test",
  "childSpecName" : "test",
  "type" : "test",
  "version" : "test",
  "timestamp" : "test"
}'
```

## Response Example

```json
{
  "result" : {
    "specId" : 1
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```