# bg.local.goods.compliance.extra.template.get

**Inquire Required Compliance Information**

Inquire Required Compliance Information

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
| normalPropertyList | 8 | No |  |  |
| governPropertyList | 8 | No |  |  |
| repInfoList | 8 | No |  |  |

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
  "goodsId" : 1,
  "sign" : "test",
  "language" : "test",
  "type" : "test",
  "version" : "test",
  "access_token" : "test",
  "catId" : 1,
  "governPropertyList" : [ {
    "vid" : 1,
    "pid" : 1,
    "value" : "test",
    "refPid" : 1
  } ],
  "app_key" : "test",
  "data_type" : "test",
  "repInfoList" : [ {
    "complianceRepType" : 1,
    "repIdList" : [ 1, 1 ]
  } ],
  "normalPropertyList" : [ {
    "vid" : 1,
    "pid" : 1,
    "value" : "test",
    "refPid" : 1
  } ],
  "timestamp" : "test"
}'
```

## Response Example

```json
{
  "result" : {
    "extraComplianceInfoList" : [ {
      "type" : 1,
      "isRequired" : true
    } ],
    "guideFileRequirement" : {
      "isRequired" : true,
      "requiredLanguageList" : [ "test", "test" ]
    },
    "extraTemplateList" : [ {
      "isRequired" : true,
      "templateDimensionType" : 1,
      "templateGoodsPropertyConfigDTOList" : [ {
        "showSkuVidList" : [ 1, 1 ],
        "refPid" : 1
      } ],
      "supportMultiGroup" : true,
      "templateDesc" : "test",
      "checkTypeName" : "test",
      "templateId" : 1,
      "templatePropertyDTOList" : [ {
        "max" : "test",
        "parentPid" : 1,
        "parentVidList" : [ 1, 1 ],
        "excludeVidMap" : {
          "$key" : "test",
          "$value" : [ 1, 1 ]
        },
        "inputTitle" : "test",
        "valuePrecision" : 1,
        "selectNum" : 1,
        "inputNum" : 1,
        "unit" : "test",
        "min" : "test",
        "controlType" : 1,
        "propertyName" : "test",
        "propertyDesc" : "test",
        "inputType" : 1,
        "propertyValueList" : [ {
          "vid" : 1,
          "parentVidList" : [ 1, 1 ],
          "valueName" : "test"
        } ],
        "refPid" : 1
      } ]
    } ]
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```