# bg.compliance.edit

**edit_compliance**

edit compliance info

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
| editReqList | 8 | No |  |  |

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
| 210010032 | The current product does not support unbinding from the current manufacturer or rebinding to another manufacturer. If modifications are needed, please contact the assigned operations representative. |

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "access_token" : "test",
  "app_key" : "test",
  "productId" : 1,
  "sign" : "test",
  "data_type" : "test",
  "editReqList" : [ {
    "inputText" : {
      "$key" : "test",
      "$value" : {
        "name" : "test",
        "lang" : {
          "$key" : "test",
          "$value" : "test"
        },
        "multiLineInputs" : [ {
          "name" : "test",
          "lang" : {
            "$key" : "test",
            "$value" : "test"
          }
        } ]
      }
    },
    "repList" : [ {
      "repId" : 1
    } ],
    "properties" : {
      "$key" : "test",
      "$value" : [ 1, 1 ]
    },
    "complianceType" : 1
  } ],
  "type" : "test",
  "version" : "test",
  "timestamp" : "test"
}'
```

## Response Example

```json
{
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```