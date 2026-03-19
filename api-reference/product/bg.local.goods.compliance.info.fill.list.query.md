# bg.local.goods.compliance.info.fill.list.query

**Query compliance information fill in the drop-down list**

local-local goods B, query compliance information fill in the drop-down list

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
| page | 1 | No |  |  |
| size | 1 | No |  |  |
| complianceInfoType | 1 | No |  |  |
| searchText | 4 | No |  |  |

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

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "access_token" : "test",
  "searchText" : "test",
  "app_key" : "test",
  "size" : 1,
  "sign" : "test",
  "data_type" : "test",
  "complianceInfoType" : 1,
  "language" : "test",
  "page" : 1,
  "type" : "test",
  "version" : "test",
  "timestamp" : "test"
}'
```

## Response Example

```json
{
  "result" : {
    "total" : 1,
    "authRepInfoList" : [ {
      "repStatus" : 1,
      "repType" : 1,
      "repTelCode" : 1,
      "repMobile" : "test",
      "repName" : "test",
      "personType" : 1,
      "endTimestamp" : 1,
      "repId" : 1,
      "startTimestamp" : 1,
      "repAddressInfo" : {
        "addressLineTwo" : "test",
        "city" : "test",
        "stateName" : "test",
        "regionName" : "test",
        "addressLineOne" : "test",
        "fullName" : "test",
        "isEU" : true,
        "regionNameShort" : "test",
        "stateShortName" : "test"
      }
    } ]
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```