# bg.open.accesstoken.create

**Get Access Token**

Temu's authorization callback interface allows developers to receive notifications when a user has successfully authorized their application. When after the user grants permission, Temu will redirect back to the developer's specified callback URL with an authorization code. Use this api to request an access token.

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
| code | 4 | No |  |  |

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
| 110020001 | System error, please try again. |
| 110020002 | Invalid code, please check and try again. |
| 110020003 | The error occurred when creating access token, please authorize again. |

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "access_token" : "test",
  "app_key" : "test",
  "code" : "test",
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
    "regionId" : 1,
    "mallId" : 1,
    "appSubscribeEventCodeList" : [ "test", "test" ],
    "appSubscribeStatus" : 1,
    "authEventCodeList" : [ {
      "eventCode" : "test",
      "permitsStatus" : 1
    } ],
    "accessToken" : "test",
    "associatedMallTokenList" : [ {
      "accessToken" : "test",
      "mallId" : 1
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