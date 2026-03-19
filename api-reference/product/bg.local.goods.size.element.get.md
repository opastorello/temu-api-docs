# bg.local.goods.size.element.get

**Query Size Chart Element Information**

Check size chart/image upload limits and requirements for this category.

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
| 150010002 | System error, please try again later |
| 150010003 | Invalid Request Parameters |
| 150010005 | Try again later |
| 150010124 | The catId not a leaf category |
| 150010042 | Category unavailable |

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
    "sizeSpecElementRule" : {
      "isSizeChartRequired" : true,
      "catId" : 1,
      "classId" : 1,
      "allowRange" : true,
      "needUSSpec" : true,
      "className" : "test",
      "setElementList" : [ {
        "catId" : 1,
        "classId" : 1,
        "allowRange" : true,
        "needUSSpec" : true,
        "className" : "test",
        "localCodeId" : 1,
        "localCodeName" : "test",
        "sizeSpecElementList" : [ {
          "elementId" : 1,
          "description" : "test",
          "type" : "test",
          "necessary" : true,
          "value" : "test",
          "elementName" : "test"
        } ]
      } ],
      "sizeSpecType" : 1,
      "localCodeId" : 1,
      "localCodeName" : "test",
      "sizeSpecElementList" : [ {
        "elementId" : 1,
        "description" : "test",
        "type" : "test",
        "necessary" : true,
        "value" : "test",
        "elementName" : "test"
      } ]
    }
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```