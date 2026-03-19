# bg.local.goods.sku.list.price.query

**Batch query latest supplier price of SKUs.**

This is an API for batch querying the latest supply prices of SKUs for local-to-local goods.

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
| querySupplierPriceBaseList | 8 | No |  |  |
| language | 4 | No |  |  |

## Response Parameters

| Parameter | Type | Required | Description | Example |
|---|---|---|---|---|
| result | 6 | No |  |  |
| success | 5 | No |  |  |
| errorCode | 1 | No |  |  |
| errorMsg | 4 | No |  |  |

## Error Codes

| Error Code | Message |
|---|---|
| 150010105 | Mall information not found |
| 150010003 | Invalid Request Parameters |
| 150010002 | System error, please try again later |

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "access_token" : "test",
  "querySupplierPriceBaseList" : [ {
    "skuIdList" : [ 1, 1 ],
    "goodsId" : 1
  } ],
  "app_key" : "test",
  "sign" : "test",
  "data_type" : "test",
  "language" : "test",
  "type" : "test",
  "version" : "test",
  "timestamp" : "test"
}'
```

## Response Example

```json
{
  "result" : {
    "openapiGoodsSupplierPriceDTOList" : [ {
      "openapiSkuSupplierPriceDTOList" : [ {
        "supplierPrice" : {
          "amount" : "test",
          "currency" : "test"
        },
        "skuId" : 1
      } ],
      "goodsId" : 1
    } ]
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```