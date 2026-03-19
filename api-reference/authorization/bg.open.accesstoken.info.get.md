# bg.open.accesstoken.info.get

**Get Accesstoken Detail Information**

This interface allows merchants to view the API permissions associated with their currently authorized token, providing a list of authorized API endpoints.

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
    "semiUniqueId" : "test",
    "regionId" : 1,
    "mallId" : 1,
    "appSubscribeEventCodeList" : [ "test", "test" ],
    "appSubscribeStatus" : 1,
    "authEventCodeList" : [ {
      "eventCode" : "test",
      "permitsStatus" : 1
    } ],
    "expiredTime" : 1,
    "mallType" : 1,
    "apiScopeList" : [ "test", "test" ]
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```