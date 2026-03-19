# bg.local.goods.template.get

**Query Product Attributes Template**

query product attributes template

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
| goodsId | 2 | No |  |  |
| goodsBrandProperties | 8 | No |  |  |
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
| 150010203 | This product doesn't belong to this shop. |

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "access_token" : "test",
  "catId" : 1,
  "goodsBrandProperties" : [ {
    "value" : "test",
    "refPid" : 1
  } ],
  "app_key" : "test",
  "goodsId" : 1,
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
    "singleSpecValueNum" : 1,
    "inputMaxSpecNum" : 1,
    "templateInfo" : {
      "templateId" : 1,
      "goodsProperties" : [ {
        "numberInputTitle" : "test",
        "templatePropertyValueParentList" : [ {
          "vids" : [ 1, 1 ],
          "parentVids" : [ 1, 1 ]
        } ],
        "values" : [ {
          "vid" : 1,
          "specId" : 1,
          "subGroup" : {
            "name" : "test",
            "id" : 1
          },
          "parentVids" : [ 1, 1 ],
          "brandId" : 1,
          "additionalInfo" : {
            "needIsbn" : true
          },
          "extendInfo" : "test",
          "value" : "test",
          "group" : {
            "name" : "test",
            "id" : 1
          }
        } ],
        "referenceType" : 1,
        "pid" : 1,
        "templatePid" : 1,
        "transnationalAttribute" : true,
        "required" : true,
        "propertyValueType" : 1,
        "minValue" : "test",
        "feature" : 1,
        "valueRule" : 1,
        "propertyChooseTitle" : "test",
        "showType" : 1,
        "parentTemplatePid" : 1,
        "mainSale" : true,
        "templateModuleId" : 1,
        "parentSpecId" : 1,
        "maxValue" : "test",
        "chooseMaxNum" : 1,
        "valuePrecision" : 1,
        "showCondition" : [ {
          "parentRefPid" : 1,
          "parentVids" : [ 1, 1 ]
        } ],
        "controlType" : 1,
        "valueUnitList" : [ {
          "valueUnit" : "test",
          "valueUnitId" : 1
        } ],
        "name" : "test",
        "isSale" : true,
        "refPid" : 1
      } ],
      "goodsSpecProperties" : [ {
        "numberInputTitle" : "test",
        "templatePropertyValueParentList" : [ {
          "vids" : [ 1, 1 ],
          "parentVids" : [ 1, 1 ]
        } ],
        "values" : [ {
          "vid" : 1,
          "specId" : 1,
          "subGroup" : {
            "name" : "test",
            "id" : 1
          },
          "parentVids" : [ 1, 1 ],
          "brandId" : 1,
          "additionalInfo" : {
            "needIsbn" : true
          },
          "extendInfo" : "test",
          "value" : "test",
          "group" : {
            "name" : "test",
            "id" : 1
          }
        } ],
        "referenceType" : 1,
        "pid" : 1,
        "templatePid" : 1,
        "required" : true,
        "propertyValueType" : 1,
        "minValue" : "test",
        "feature" : 1,
        "valueRule" : 1,
        "propertyChooseTitle" : "test",
        "showType" : 1,
        "parentTemplatePid" : 1,
        "mainSale" : true,
        "templateModuleId" : 1,
        "parentSpecId" : 1,
        "maxValue" : "test",
        "chooseMaxNum" : 1,
        "valuePrecision" : 1,
        "showCondition" : [ {
          "parentRefPid" : 1,
          "parentVids" : [ 1, 1 ]
        } ],
        "controlType" : 1,
        "valueUnitList" : [ {
          "valueUnit" : "test",
          "valueUnitId" : 1
        } ],
        "name" : "test",
        "isSale" : true,
        "refPid" : 1
      } ]
    },
    "userInputParentSpecList" : [ {
      "parentSpecId" : 1,
      "feature" : 1,
      "parentSpecName" : "test"
    } ]
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```