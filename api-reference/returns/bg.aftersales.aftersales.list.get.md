# bg.aftersales.aftersales.list.get

**Query sub after-sales order information**

This interface is designed for use in an e-commerce platform, specifically for handling after-sales service requests related to product returns and refunds. The interface allows merchants or administrators to retrieve a list of after-sales service requests made by buyers, including detailed information about each request.

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
| parentAfterSalesSnList | 8 | No |  |  |

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
      "productSkuId" : 1,
      "applyAfterSalesGoodsNumber" : 1,
      "afterSalesSn" : "test",
      "goodsId" : 1,
      "skuId" : 1,
      "productList" : [ {
        "productSkuId" : 1,
        "extCode" : "test"
      } ],
      "afterSalesStatus" : 1,
      "afterSalesType" : 1
    } ],
    "total" : 1,
    "pageNumber" : 1
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```