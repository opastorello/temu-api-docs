# temu.order.cancel.outofstock.apply

**Merchant order out of stock cancel apply**

The user takes the initiative to initiate a stock-out situation, which will be submitted to the risk control department for review.

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
| parentOrderSn | 4 | No |  |  |
| orderSnList | 8 | No |  |  |

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
| 140040001 | request param error |
| 140040002 | no fulfillment under this condition |
| 140040003 | please try again later |

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "access_token" : "test",
  "app_key" : "test",
  "parentOrderSn" : "test",
  "sign" : "test",
  "data_type" : "test",
  "type" : "test",
  "version" : "test",
  "orderSnList" : [ "test", "test" ],
  "timestamp" : "test"
}'
```

## Response Example

```json
{
  "result" : {
    "failReasonList" : [ {
      "reasonList" : [ "test", "test" ],
      "orderSn" : "test",
      "parentOrderSn" : "test"
    } ],
    "applyResult" : true
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```