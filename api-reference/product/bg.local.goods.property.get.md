# bg.local.goods.property.get

**Get temu attributes**

Get Temu goods attributes

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
| goodsName | 4 | No |  |  |
| catId | 2 | No |  |  |
| goodsDesc | 4 | No |  |  |
| thirdPartyErpType | 1 | No |  |  |
| thirdPartyMall | 4 | No |  |  |
| thirdPartyCatName | 4 | No |  |  |
| goodsPropList | 8 | No |  |  |

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
| 150010002 | System error, please try again later |

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "goodsPropList" : [ {
    "propName" : "test",
    "values" : [ "test", "test" ]
  } ],
  "sign" : "test",
  "thirdPartyCatName" : "test",
  "language" : "test",
  "thirdPartyMall" : "test",
  "type" : "test",
  "version" : "test",
  "access_token" : "test",
  "catId" : 1,
  "app_key" : "test",
  "data_type" : "test",
  "thirdPartyErpType" : 1,
  "goodsName" : "test",
  "timestamp" : "test",
  "goodsDesc" : "test"
}'
```

## Response Example

```json
{
  "result" : {
    "goodsPropertyList" : [ {
      "vid" : 1,
      "valueUnitId" : 1,
      "valueUnit" : "test",
      "pid" : 1,
      "templatePid" : 1,
      "numberInputValue" : "test",
      "value" : "test",
      "refPid" : 1
    } ]
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```