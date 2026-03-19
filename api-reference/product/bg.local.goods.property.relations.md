# bg.local.goods.property.relations

**Query relation-property data of the product**

Query the relational database data associated with goods, such as vehicle library.

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
| relationType | 1 | No |  |  |
| goodsId | 2 | No |  |  |
| relationId | 2 | No |  |  |
| queryLastVersion | 5 | No |  |  |

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
| 150010003 | Invalid Request Parameters |
| 150010213 | The goods property relation not exist |
| 150010210 | The property value id is not exist |

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "access_token" : "test",
  "relationType" : 1,
  "app_key" : "test",
  "goodsId" : 1,
  "sign" : "test",
  "data_type" : "test",
  "relationId" : 1,
  "type" : "test",
  "version" : "test",
  "queryLastVersion" : true,
  "timestamp" : "test"
}'
```

## Response Example

```json
{
  "result" : {
    "relationType" : 1,
    "goodsLinkPropValList" : [ {
      "goodsPropValList" : [ {
        "propertyValue" : "test",
        "propValDepId" : 1
      } ]
    } ],
    "relationId" : 1
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```