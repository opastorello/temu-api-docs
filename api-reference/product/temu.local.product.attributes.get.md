# temu.local.product.attributes.get

**Query Attribute Template**

Query Attribute Template

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
| costTemplateId | 4 | No |  |  |

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
| 150010042 | Category unavailable |
| 150010124 | The catId not a leaf category |

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
  "costTemplateId" : "test",
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
    "attributeList" : [ {
      "attributeValueDetail" : [ {
        "attributeValueList" : [ {
          "vid" : 1,
          "value" : "test",
          "childAttribute" : [ {
            "childAttributeValueGroupId" : "test",
            "childAttributeId" : 1
          } ]
        } ],
        "groupId" : "test"
      } ],
      "attributeName" : "test",
      "attributeRules" : {
        "chooseMaxNum" : 1,
        "controlType" : 1,
        "transnationalAttribute" : true,
        "attributeValueRules" : {
          "valuePrecision" : 1,
          "minValue" : "test",
          "numberInputTitle" : "test",
          "maxValue" : "test",
          "valueRule" : 1,
          "propertyChooseTitle" : "test"
        }
      },
      "required" : true,
      "refPid" : 1,
      "attributeValueUnitList" : [ {
        "valueUnitName" : "test",
        "valueUnitId" : 1
      } ]
    } ]
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```