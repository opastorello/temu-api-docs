# temu.local.goods.missing.attributes.get

**temu.local.goods.missing.attributes.get**

temu.local.goods.missing.attributes.get

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
| goodsId | 2 | No |  |  |

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
| 150011130 | The product is under review. Missing required attributes cannot be queried or edited. Please try again later. |
| 150010003 | Invalid Request Parameters |
| 150010188 | The mall and goods not match. |

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "access_token" : "test",
  "app_key" : "test",
  "goodsId" : 1,
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
    "missingAttributeList" : [ {
      "attributeValueDetail" : [ {
        "attributeValueList" : [ {
          "vid" : 1,
          "value" : "test",
          "childAttribute" : [ {
            "childAttributeValueGroupId" : "test",
            "childAttributeName" : "test",
            "childAttributeId" : 1
          } ]
        } ],
        "groupId" : "test"
      } ],
      "attributeName" : "test",
      "refPid" : 1,
      "attributeValueUnitList" : [ {
        "valueUnitName" : "test",
        "valueUnitId" : 1
      } ]
    } ],
    "goodsId" : 1,
    "language" : "test"
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```