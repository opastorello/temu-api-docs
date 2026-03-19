# bg.compliance.metadata.get

**query_compliance_metadata**

query compliance metadata

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
| productId | 2 | No |  |  |

## Response Parameters

| Parameter | Type | Required | Description | Example |
|---|---|---|---|---|
| success | 5 | No |  |  |
| errorCode | 1 | No |  |  |
| errorMsg | 4 | No |  |  |
| result | 6 | No |  |  |

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "access_token" : "test",
  "app_key" : "test",
  "productId" : 1,
  "sign" : "test",
  "data_type" : "test",
  "type" : "test",
  "version" : "test",
  "timestamp" : "test"
}'
```

## Response Example

```json
{
  "result" : {
    "complianceInfoList" : [ {
      "name" : "test",
      "repDetailList" : [ {
        "repStatus" : 1,
        "repName" : "test",
        "personType" : 1,
        "endTimestamp" : 1,
        "repId" : 1,
        "startTimestamp" : 1,
        "repAddressInfo" : {
          "addressLineOne" : "test",
          "city" : "test",
          "stateName" : "test",
          "regionName" : "test"
        }
      } ],
      "propertyList" : [ {
        "max" : 1.0,
        "parentPid" : 1,
        "parentVidList" : [ 1, 1 ],
        "excludeVidMap" : {
          "$key" : "test",
          "$value" : [ 1, 1 ]
        },
        "langDescMap" : {
          "$key" : "test",
          "$value" : "test"
        },
        "valuePrecision" : 1,
        "selectNum" : 1,
        "inputNum" : 1,
        "needTransLang" : [ "test", "test" ],
        "unit" : "test",
        "min" : 1.0,
        "controlType" : 1,
        "propertyName" : "test",
        "inputType" : 1,
        "propertyValueList" : [ {
          "vid" : 1,
          "parentVidList" : [ 1, 1 ],
          "langValueNameMap" : {
            "$key" : "test",
            "$value" : "test"
          },
          "valueName" : "test"
        } ],
        "propertyId" : 1,
        "desc" : "test"
      } ],
      "complianceType" : 1,
      "status" : 1,
      "desc" : "test"
    } ]
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```