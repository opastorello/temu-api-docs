# temu.local.goods.pre.sale.status.edit

**Temu Pre-sale Bulk Enable/Disable API**

This API allows batch enabling or disabling the pre-sale status for multiple SKUs belonging to a product item.

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
| targetPreSaleStatus | 1 | No |  |  |
| skuInfoList | 8 | No |  |  |

## Response Parameters

| Parameter | Type | Required | Description | Example |
|---|---|---|---|---|
| success | 5 | No |  |  |
| errorCode | 1 | No |  |  |
| errorMsg | 4 | No |  |  |
| result | 6 | No |  |  |

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "access_token" : "test",
  "app_key" : "test",
  "goodsId" : 1,
  "targetPreSaleStatus" : 1,
  "sign" : "test",
  "data_type" : "test",
  "type" : "test",
  "version" : "test",
  "skuInfoList" : [ {
    "targetPreSaleStock" : 1,
    "preSaleEndTime" : 1,
    "skuId" : 1
  } ],
  "timestamp" : "test"
}'
```

## Response Example

```json
{
  "result" : {
    "msg" : "test",
    "skuOperateResultInfoList" : [ {
      "msg" : "test",
      "skuId" : 1,
      "code" : 1
    } ],
    "code" : 1,
    "goodsId" : 1
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```