# temu.local.goods.cats.rules.get

**Query the rules for posting products**

Query the rules for posting products

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
| language | 4 | No |  |  |
| catId | 2 | No |  |  |

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
| 150010262 | Category prohibited from being published and sold on Temu Platform. For more information or help, please contact your BD |
| 150010002 | System error, please try again later |
| 150010003 | Invalid Request Parameters |
| 150010005 | Try again later |
| 150010124 | The catId not a leaf category |
| 150010042 | Category unavailable |
| 150010106 | Shop status abnormal |
| 150010220 | Book products cannot be published by non-book store |

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "access_token" : "test",
  "catId" : 1,
  "app_key" : "test",
  "sign" : "test",
  "data_type" : "test",
  "language" : "test",
  "type" : "test",
  "version" : "test",
  "timestamp" : "test"
}'
```

## Response Example

```json
{
  "result" : {
    "secondHand" : [ {
      "businessScope" : 1,
      "condition" : [ {
        "type" : 1,
        "agency" : [ {
          "insName" : "test",
          "grade" : [ "test", "test" ]
        } ],
        "level" : [ {
          "name" : "test",
          "number" : 1
        } ]
      } ]
    } ],
    "fieldRules" : [ {
      "requirementType" : 1,
      "filedName" : "test"
    } ],
    "expandCatType" : 1,
    "warnings" : [ {
      "message" : "test"
    } ]
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```