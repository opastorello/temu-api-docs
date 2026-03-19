# bg.local.goods.stock.edit

**Edit product stock**

Edit product stock with full-update and diff-update

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
| stockType | 1 | No |  |  |
| skuStockChangeList | 8 | No |  |  |
| skuStockTargetList | 8 | No |  |  |
| requestUniqueKey | 4 | No |  |  |

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
| 150013003 | Only one stock adjustment method can be active at a time. |
| 150013001 | Duplicate SKUs detected. Please remove them and try again |
| 150013002 | Quantity must be between 0 and 1000000 |
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
  "stockType" : 1,
  "goodsId" : 1,
  "skuStockTargetList" : [ {
    "stockTarget" : 1,
    "skuId" : 1
  } ],
  "sign" : "test",
  "data_type" : "test",
  "type" : "test",
  "requestUniqueKey" : "test",
  "version" : "test",
  "skuStockChangeList" : [ {
    "skuId" : 1,
    "stockDiff" : 1
  } ],
  "timestamp" : "test"
}'
```

## Response Example

```json
{
  "result" : {
    "msg" : "test",
    "skuStockEditStatusInfoList" : [ {
      "errorCode" : 1,
      "stockEditStatus" : true,
      "skuId" : 1,
      "errorMsg" : "test"
    } ],
    "operateResult" : true,
    "goodsId" : 1
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```