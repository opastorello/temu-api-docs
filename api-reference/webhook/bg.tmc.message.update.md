# bg.tmc.message.update

**Update Shop Webhook**

This API updates the shop's webhook for specific event codes.

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
| cancelEventCodeList | 8 | No |  |  |
| permitEventCodeList | 8 | No |  |  |

## Response Parameters

| Parameter | Type | Required | Description | Example |
|---|---|---|---|---|
| result | 5 | No |  |  |
| success | 5 | No |  |  |
| errorCode | 1 | No |  |  |
| errorMsg | 4 | No |  |  |

## Error Codes

| Error Code | Message |
|---|---|
| 110020005 | Cancel and permit parameters must not exceed 20. |
| 110020006 | Cancel and permit parameters are not allowed to be the same. |
| 110020007 | Too many requests in 1 sec, please try again later. |
| 110020008 | Access_token don't have this event access, please ask for seller to authorize this event in seller center first,and share the new access_token with you. |
| 110020009 | App don't have this event subscription. |

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "access_token" : "test",
  "cancelEventCodeList" : [ "test", "test" ],
  "app_key" : "test",
  "sign" : "test",
  "data_type" : "test",
  "permitEventCodeList" : [ "test", "test" ],
  "type" : "test",
  "version" : "test",
  "timestamp" : "test"
}'
```

## Response Example

```json
{
  "result" : true,
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```