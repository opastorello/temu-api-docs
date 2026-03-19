# temu.order.cancel.appeal.apply

**Merchant initiates order cancellation application interface**

Support merchants to initiate cancellation requests through the interface

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
| cancelType | 1 | No |  |  |
| applyOrder | 6 | No |  |  |
| reason | 6 | No |  |  |

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
| 120050003 | Cancel appeal failed |
| 120050002 | Invalid parent order sn |
| 120050001 | Invalid cancel type |

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "access_token" : "test",
  "reason" : {
    "description" : "test",
    "proofUrlList" : [ "test", "test" ]
  },
  "applyOrder" : {
    "parentOrderSn" : "test"
  },
  "app_key" : "test",
  "cancelType" : 1,
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
    "applySn" : "test"
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```