# temu.local.goods.sku.stock.query

**local goods query product stock**

local-local goods B

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
| language | 4 | No |  |  |
| outSkuSnList | 8 | No |  |  |
| skuIdList | 8 | No |  |  |
| goodsId | 2 | No |  |  |

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
| 150010002 | System error, please try again later |
| 150010003 | Invalid Request Parameters |
| 150010005 | Try again later |

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "access_token" : "test",
  "app_key" : "test",
  "outSkuSnList" : [ "test", "test" ],
  "goodsId" : 1,
  "sign" : "test",
  "data_type" : "test",
  "language" : "test",
  "type" : "test",
  "version" : "test",
  "skuIdList" : [ 1, 1 ],
  "timestamp" : "test"
}'
```

## Response Example

```json
{
  "result" : {
    "stockList" : [ {
      "goodsId" : 1,
      "skuStockInfoList" : [ {
        "outSkuSn" : "test",
        "selfOrdinaryStock" : {
          "stock" : 1,
          "stockType" : 1
        },
        "certOrdinaryStock" : {
          "stock" : 1,
          "stockType" : 1
        },
        "skuId" : 1,
        "selfPreSaleStock" : {
          "stock" : 1,
          "preSaleEndTime" : 1,
          "stockType" : 1,
          "skuPreSaleStockLimit" : 1,
          "mallPreSaleSkuNumLimit" : 1
        }
      } ]
    } ]
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```