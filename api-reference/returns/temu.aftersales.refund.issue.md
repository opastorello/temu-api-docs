# temu.aftersales.refund.issue

**issue refund**

This interface is designed to enable merchants to efficiently process refund requests within the e-commerce platform.

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
| parentAfterSalesSn | 4 | No |  |  |
| parentOrderSn | 4 | No |  |  |
| openApiRefundType | 1 | No |  |  |

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
| 130010004 | no afterSales found |
| 130010005 | operate forbid |
| 130010003 | There were some payable in your account, please process them in the merchant workbench before proceeding. |
| 130010000 | system error |
| 130010001 | The parameter is illegal. Please check if the input parameter meets the regulations. |

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "access_token" : "test",
  "parentAfterSalesSn" : "test",
  "app_key" : "test",
  "parentOrderSn" : "test",
  "openApiRefundType" : 1,
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
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```