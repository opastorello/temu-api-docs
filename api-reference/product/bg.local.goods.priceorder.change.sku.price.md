# bg.local.goods.priceorder.change.sku.price

**Batch change SKU base price**

Support merchants within the white list to modify sku base prices in batches.

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
| goodsId | 2 | No |  |  |
| changeSkuPriceDTOList | 8 | No |  |  |
| rejectSkuPricing | 5 | No |  |  |

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
| 150011103 | The price imported from your ERP system for this product has not been confirmed. Please confirm the imported price in the Seller Center before making any new price adjustments. |
| 150011101 | The price change in this request exceeds the allowed range. Please check the request parameters. If the change is confirmed, please retry within {*} minutes. |
| 150019004 | Invalid newSupplierPrice. The recommended price for skuId: {*} is {*}. |
| 150011018 | Price currency {*} can have at most {*} decimal points. |
| 150010233 | The product is participating in an activity or the activity's cool-down period still applies to the product. Price adjustment to a lower level is not available. |
| 150010105 | Mall information not found |
| 150010188 | The mall and goods not match. |
| 150010189 | The sku and goods not match |
| 150010190 | The sku repeat in batch change sku price |
| 150010191 | The reason repeat in batch change sku price |
| 150010192 | Clothes sku supplier price or reason not equal |
| 150010197 | The count of reason is over size. |
| 150010198 | The count of SKU is over size. |
| 150010003 | Invalid Request Parameters |

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "access_token" : "test",
  "app_key" : "test",
  "goodsId" : 1,
  "changeSkuPriceDTOList" : [ {
    "reason" : "test",
    "skuChangePriceBaseDTOList" : [ {
      "skuId" : 1,
      "newSupplierPrice" : {
        "amount" : "test",
        "currency" : "test"
      }
    } ]
  } ],
  "sign" : "test",
  "data_type" : "test",
  "type" : "test",
  "version" : "test",
  "rejectSkuPricing" : true,
  "timestamp" : "test"
}'
```

## Response Example

```json
{
  "result" : {
    "successPriceOrderList" : [ {
      "skuIdList" : [ 1, 1 ],
      "priceOrderSn" : "test"
    } ],
    "failedSkuReasonMap" : {
      "$key" : "test",
      "$value" : "test"
    },
    "failedSkuList" : [ 1, 1 ],
    "successSkuList" : [ 1, 1 ]
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```