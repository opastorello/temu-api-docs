# temu.local.product.variation.get

**Query Mandatory And Optional Variations Of Products**

Query Mandatory And Optional variations Of Products

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
| 150010003 | Invalid Request Parameters |
| 150010005 | Try again later |
| 150010042 | Category unavailable |
| 150010124 | The catId not a leaf category |
| 150010002 | System error, please try again later |

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
    "catId" : 1,
    "language" : "test",
    "variations" : [ {
      "specList" : [ {
        "specId" : 1,
        "subGroupName" : "test",
        "groupName" : "test",
        "specName" : "test",
        "groupId" : 1,
        "subGroupId" : 1
      } ],
      "parentSpecName" : "test",
      "parentSpecId" : 1,
      "variationType" : 1,
      "required" : true
    } ]
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```