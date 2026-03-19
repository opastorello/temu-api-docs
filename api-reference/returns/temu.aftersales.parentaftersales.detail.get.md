# temu.aftersales.parentaftersales.detail.get

**query aftersales detail**

This interface is designed to provide detailed information on after-sales orders in real time

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
| parentAfterSalesSn | 4 | No |  |  |

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
| 130010000 | system error |
| 130010005 | operate forbid |
| 130010001 | The parameter is illegal. Please check if the input parameter meets the regulations. |
| 130010002 | The order has been fully shipped. |

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
    "parentAfterSalesSn" : "test",
    "availableOperateList" : [ 1, 1 ],
    "createAtMillis" : 1,
    "parentAfterSalesStatus" : 1,
    "refundSummary" : {
      "discountFromSellerRefund" : {
        "currency" : "test",
        "amount" : 1
      },
      "discountFromTEMURefund" : {
        "currency" : "test",
        "amount" : 1
      },
      "buyerTotalRefund" : {
        "currency" : "test",
        "amount" : 1
      },
      "shippingAmountRefundTaxExcl" : {
        "currency" : "test",
        "amount" : 1
      },
      "taxTotalRefund" : {
        "currency" : "test",
        "amount" : 1
      },
      "retailPriceRefundTaxExcl" : {
        "currency" : "test",
        "amount" : 1
      }
    },
    "parentOrderSn" : "test",
    "lastUpdateAtMillis" : 1,
    "afterSalesType" : 1,
    "afterSalesList" : [ {
      "applyAfterSalesGoodsNumber" : 1,
      "afterSalesSn" : "test",
      "orderSn" : "test",
      "applyRefundAmount" : {
        "currency" : "test",
        "amount" : 1
      },
      "afterSalesReasonDesc" : "test",
      "afterSalesGoodsInfo" : {
        "productSkuId" : 1,
        "goodsId" : 1,
        "skuId" : 1,
        "productList" : [ {
          "productSkuId" : 1,
          "extCode" : "test"
        } ]
      },
      "afterSalesReasonCode" : 1,
      "buyerComment" : "test",
      "afterSalesStatus" : 1
    } ]
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```