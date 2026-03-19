# bg.aftersales.cancel.list.get

**Query cancel order after-sales information**

Query cancel order after-sales information

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
| pageSize | 1 | No |  |  |
| pageNo | 1 | No |  |  |
| parentOrderSnList | 8 | No |  |  |
| parentAfterSalesSnList | 8 | No |  |  |
| afterSalesStatusGroup | 1 | No |  |  |

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
| 130010001 | The parameter is illegal. Please check if the input parameter meets the regulations. |

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "access_token" : "test",
  "afterSalesStatusGroup" : 1,
  "parentOrderSnList" : [ "test", "test" ],
  "app_key" : "test",
  "pageNo" : 1,
  "sign" : "test",
  "data_type" : "test",
  "parentAfterSalesSnList" : [ "test", "test" ],
  "pageSize" : 1,
  "type" : "test",
  "version" : "test",
  "timestamp" : "test"
}'
```

## Response Example

```json
{
  "result" : {
    "data" : [ {
      "parentAfterSalesSn" : "test",
      "parentAfterSalesStatus" : 1,
      "afterSalesInfoList" : [ {
        "productSkuId" : 1,
        "afterSalesSn" : "test",
        "createAtMillis" : 1,
        "orderSn" : "test",
        "parentOrderSn" : "test",
        "goodsId" : 1,
        "applyGoodsNumber" : 1,
        "productList" : [ {
          "productSkuId" : 1,
          "extCode" : "test"
        } ]
      } ]
    } ],
    "total" : 1,
    "pageNumber" : 1
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```