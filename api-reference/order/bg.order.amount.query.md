# bg.order.amount.query

**Get order amount api**

Provide the supply price information corresponding to the orders for the self-developed ERP

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
| 140020008 | Some amount fields are still undergoing system calculation. Please try again later. |

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
  "timestamp" : "test"
}'
```

## Response Example

```json
{
  "result" : {
    "parentOrderMap" : {
      "shipTaxAmount" : {
        "currency" : "test",
        "amount" : 1
      },
      "shipAmountTotalTaxIncl" : {
        "currency" : "test",
        "amount" : 1
      },
      "customerPaid" : {
        "currency" : "test",
        "amount" : 1
      },
      "retailPriceTotalTaxIncl" : {
        "currency" : "test",
        "amount" : 1
      },
      "taxTotal" : {
        "currency" : "test",
        "amount" : 1
      },
      "refundsTotal" : {
        "currency" : "test",
        "amount" : 1
      },
      "estimatedRevenue" : {
        "currency" : "test",
        "amount" : 1
      },
      "discountFromTEMU" : {
        "currency" : "test",
        "amount" : 1
      },
      "discountFromSeller" : {
        "currency" : "test",
        "amount" : 1
      },
      "productTaxAmount" : {
        "currency" : "test",
        "amount" : 1
      },
      "temuTaxTotal" : {
        "currency" : "test",
        "amount" : 1
      },
      "taxTotalAfterDiscount" : {
        "currency" : "test",
        "amount" : 1
      },
      "retailPriceTotalTaxExcl" : {
        "currency" : "test",
        "amount" : 1
      },
      "parentOrderSn" : "test",
      "estimatedRevenueDeduction" : {
        "currency" : "test",
        "amount" : 1
      },
      "shippingAmountTotal" : {
        "currency" : "test",
        "amount" : 1
      },
      "totalDiscount" : {
        "currency" : "test",
        "amount" : 1
      },
      "basePriceTotal" : {
        "currency" : "test",
        "amount" : 1
      },
      "retailPriceTotal" : {
        "currency" : "test",
        "amount" : 1
      }
    },
    "orderList" : [ {
      "shipTaxAmount" : {
        "currency" : "test",
        "amount" : 1
      },
      "shipAmountTotalTaxIncl" : {
        "currency" : "test",
        "amount" : 1
      },
      "quantity" : 1,
      "orderSn" : "test",
      "retailPriceTotalTaxIncl" : {
        "currency" : "test",
        "amount" : 1
      },
      "unitRetailPriceVatIncl" : {
        "currency" : "test",
        "amount" : 1
      },
      "discountFromTEMU" : {
        "currency" : "test",
        "amount" : 1
      },
      "productTaxAmount" : {
        "currency" : "test",
        "amount" : 1
      },
      "discountFromSeller" : {
        "currency" : "test",
        "amount" : 1
      },
      "unitBasePrice" : {
        "currency" : "test",
        "amount" : 1
      },
      "unitRetailPriceVatExcl" : {
        "currency" : "test",
        "amount" : 1
      },
      "unitRetailPrice" : {
        "currency" : "test",
        "amount" : 1
      },
      "shipTaxRate" : 1,
      "productTaxRate" : 1,
      "basePrice" : {
        "currency" : "test",
        "amount" : 1
      }
    } ],
    "warning" : [ "test", "test" ]
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```