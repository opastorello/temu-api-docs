# bg.local.goods.property.relations.template

**Query property data in relation- property database**

Query the full quantum attribute by the dependency id of the parent attribute value and the hierarchical id.

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
| relationId | 2 | No |  |  |
| relationType | 1 | No |  |  |
| propertyRelationQueryDTOList | 8 | No |  |  |

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
| 150010211 | The relation type is not allowed |
| 150010212 | The relation id is wrong |

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "access_token" : "test",
  "relationType" : 1,
  "catId" : 1,
  "app_key" : "test",
  "propertyRelationQueryDTOList" : [ {
    "propertyDependencyId" : 1,
    "parentPropertyValueDependencyId" : 1
  } ],
  "sign" : "test",
  "data_type" : "test",
  "relationId" : 1,
  "type" : "test",
  "version" : "test",
  "timestamp" : "test"
}'
```

## Response Example

```json
{
  "result" : {
    "parentPropValDepMapDTOList" : [ {
      "parentPropertyValueDependencyId" : 1,
      "propValDepDTOList" : [ {
        "propertyDependencyId" : 1,
        "propertyValueDependencyId" : 1,
        "propertyValue" : "test",
        "parentPropertyValueDependencyId" : 1,
        "isLeafProperty" : true,
        "propertyValueId" : 1
      } ]
    } ]
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```