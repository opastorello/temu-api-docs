# temu.order.amount.v2.query

**Get order amount api**

Provide the supply price information corresponding to the orders for the self-developed ERP. This API is currently available only for the Japan and Korea sites.

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
| 140020015 | This API is currently available only for the Japan and South Korea sites. |
| 140020002 | Order not found |
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
      "parentOrderSn" : "test",
      "salesProceeds" : {
        "shippingTemuTotalTaxExcl" : {
          "currency" : "test",
          "amount" : 1
        },
        "productTax" : {
          "currency" : "test",
          "amount" : 1
        },
        "productTaxCustomerDiscounted" : {
          "currency" : "test",
          "amount" : 1
        },
        "shippingTaxCustomerDiscounted" : {
          "currency" : "test",
          "amount" : 1
        },
        "basePriceSellerDiscount" : {
          "currency" : "test",
          "amount" : 1
        },
        "shippingTotalTaxExcl" : {
          "currency" : "test",
          "amount" : 1
        },
        "basePriceOff" : {
          "currency" : "test",
          "amount" : 1
        },
        "basePriceDiscountedTotal" : {
          "currency" : "test",
          "amount" : 1
        },
        "estimatedSettlementTotal" : {
          "currency" : "test",
          "amount" : 1
        },
        "taxTemuDiscount" : {
          "currency" : "test",
          "amount" : 1
        },
        "shippingTax" : {
          "currency" : "test",
          "amount" : 1
        },
        "productTaxTemu" : {
          "currency" : "test",
          "amount" : 1
        },
        "shippingTaxTemu" : {
          "currency" : "test",
          "amount" : 1
        },
        "shippingCustomerTotalTaxExcl" : {
          "currency" : "test",
          "amount" : 1
        },
        "estimatedDeduction" : {
          "currency" : "test",
          "amount" : 1
        },
        "basePriceTotal" : {
          "currency" : "test",
          "amount" : 1
        }
      },
      "customerPaid" : {
        "shippingTemuTotalTaxExcl" : {
          "currency" : "test",
          "amount" : 1
        },
        "shippingTaxCustomerTotal" : {
          "currency" : "test",
          "amount" : 1
        },
        "retailPriceCustomerTotalTaxExcl" : {
          "currency" : "test",
          "amount" : 1
        },
        "productRefundsTotal" : {
          "currency" : "test",
          "amount" : 1
        },
        "retailPriceTemuDiscountTaxExcl" : {
          "currency" : "test",
          "amount" : 1
        },
        "retailPriceSellerDiscountTaxExcl" : {
          "currency" : "test",
          "amount" : 1
        },
        "retailPriceTotalTaxIncl" : {
          "currency" : "test",
          "amount" : 1
        },
        "shippingTotalTaxExcl" : {
          "currency" : "test",
          "amount" : 1
        },
        "shippingTax" : {
          "currency" : "test",
          "amount" : 1
        },
        "customerPaidTotal" : {
          "currency" : "test",
          "amount" : 1
        },
        "retailPriceTotalTaxExcl" : {
          "currency" : "test",
          "amount" : 1
        },
        "productTaxCustomerTotal" : {
          "currency" : "test",
          "amount" : 1
        },
        "shippingCustomerTotalTaxExcl" : {
          "currency" : "test",
          "amount" : 1
        },
        "shippingTaxTemuTotal" : {
          "currency" : "test",
          "amount" : 1
        },
        "shippingTotalTaxIncl" : {
          "currency" : "test",
          "amount" : 1
        }
      }
    },
    "orderList" : [ {
      "shippingTemuTotalTaxExcl" : {
        "currency" : "test",
        "amount" : 1
      },
      "productTax" : {
        "currency" : "test",
        "amount" : 1
      },
      "productTaxCustomerDiscounted" : {
        "currency" : "test",
        "amount" : 1
      },
      "orderSn" : "test",
      "shippingTaxCustomerDiscounted" : {
        "currency" : "test",
        "amount" : 1
      },
      "retailPriceTotalTaxIncl" : {
        "currency" : "test",
        "amount" : 1
      },
      "basePriceSellerDiscount" : {
        "currency" : "test",
        "amount" : 1
      },
      "shippingTotalTaxExcl" : {
        "currency" : "test",
        "amount" : 1
      },
      "basePriceOff" : {
        "currency" : "test",
        "amount" : 1
      },
      "estimatedSettlementTotal" : {
        "currency" : "test",
        "amount" : 1
      },
      "shippingTax" : {
        "currency" : "test",
        "amount" : 1
      },
      "taxTemuDiscount" : {
        "currency" : "test",
        "amount" : 1
      },
      "productTaxTemu" : {
        "currency" : "test",
        "amount" : 1
      },
      "shippingCustomerTotalTaxExcl" : {
        "currency" : "test",
        "amount" : 1
      },
      "unitRetailPriceTaxExcl" : {
        "currency" : "test",
        "amount" : 1
      },
      "productTaxRate" : 1,
      "shippingTotalTaxIncl" : {
        "currency" : "test",
        "amount" : 1
      },
      "retailPriceDiscountedTotalTaxExcl" : {
        "currency" : "test",
        "amount" : 1
      },
      "quantity" : 1,
      "retailPriceTemuDiscountTaxExcl" : {
        "currency" : "test",
        "amount" : 1
      },
      "unitRetailPriceTaxIncl" : {
        "currency" : "test",
        "amount" : 1
      },
      "basePriceDiscountedTotal" : {
        "currency" : "test",
        "amount" : 1
      },
      "unitBasePrice" : {
        "currency" : "test",
        "amount" : 1
      },
      "shipTaxRate" : 1,
      "shippingTaxTemu" : {
        "currency" : "test",
        "amount" : 1
      },
      "retailPriceTotalTaxExcl" : {
        "currency" : "test",
        "amount" : 1
      },
      "estimatedDeduction" : {
        "currency" : "test",
        "amount" : 1
      },
      "basePriceTotal" : {
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