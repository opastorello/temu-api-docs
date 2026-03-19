# bg.order.list.v2.get

**Batch Get Order Information**

The bg.order.list.v2.get interface is designed for support batch return of corresponding order lists based on filtering criteria.

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
| pageNumber | 1 | No |  |  |
| pageSize | 1 | No |  |  |
| parentOrderStatus | 1 | No |  |  |
| parentOrderSnList | 8 | No |  |  |
| createAfter | 1 | No |  |  |
| createBefore | 1 | No |  |  |
| expectShipLatestTimeStart | 1 | No |  |  |
| expectShipLatestTimeEnd | 1 | No |  |  |
| updateAtStart | 1 | No |  |  |
| updateAtEnd | 1 | No |  |  |
| parentConfirmTimeStart | 1 | No |  |  |
| parentConfirmTimeEnd | 1 | No |  |  |
| regionId | 2 | No |  |  |
| fulfillmentTypeList | 8 | No |  |  |
| parentOrderLabel | 8 | No |  |  |
| packageAbnormalTypeList | 8 | No |  |  |
| sortby | 4 | No |  |  |
| hasPreSaleOrder | 5 | No |  |  |
| hasQualificationRequiredOrder | 5 | No |  |  |
| skuId | 2 | No |  |  |

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
| 140020012 | parentConfirmTimeEnd needs to be greater than the parentConfirmTimeStart |
| 140020013 | {*} not passed in |
| 140020014 | The format of {*} is inaccurate and requires a second level timestamp |
| 140020001 | This interface does not support cross-border sellers. Please check whether the store bound to the token is a SEMI or LOCAL store! |

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "pageNumber" : 1,
  "sign" : "test",
  "hasQualificationRequiredOrder" : true,
  "pageSize" : 1,
  "type" : "test",
  "expectShipLatestTimeStart" : 1,
  "expectShipLatestTimeEnd" : 1,
  "packageAbnormalTypeList" : [ "test", "test" ],
  "parentConfirmTimeStart" : 1,
  "fulfillmentTypeList" : [ "test", "test" ],
  "parentConfirmTimeEnd" : 1,
  "skuId" : 1,
  "timestamp" : "test",
  "parentOrderLabel" : [ "test", "test" ],
  "createAfter" : 1,
  "updateAtStart" : 1,
  "version" : "test",
  "access_token" : "test",
  "parentOrderSnList" : [ "test", "test" ],
  "app_key" : "test",
  "createBefore" : 1,
  "updateAtEnd" : 1,
  "regionId" : 1,
  "hasPreSaleOrder" : true,
  "data_type" : "test",
  "sortby" : "test",
  "parentOrderStatus" : 1
}'
```

## Response Example

```json
{
  "result" : {
    "totalItemNum" : 1,
    "pageItems" : [ {
      "parentOrderMap" : {
        "parentOrderLabel" : [ {
          "name" : "test",
          "value" : 1
        } ],
        "shippingMethod" : 1,
        "parentShippingTime" : 1,
        "updateTime" : 1,
        "latestDeliveryTime" : 1,
        "parentConfirmTime" : 1,
        "fulfillmentWarning" : [ "test", "test" ],
        "parentOrderTime" : 1,
        "orderPaymentType" : "test",
        "batchOrderNumberList" : [ "test", "test" ],
        "regionId" : 1,
        "parentOrderSn" : "test",
        "parentOrderPendingFinishTime" : 1,
        "siteId" : 1,
        "expectShipLatestTime" : 1,
        "parentOrderStatus" : 1,
        "hasShippingFee" : true
      },
      "orderList" : [ {
        "canceledQuantityBeforeShipment" : 1,
        "quantity" : 1,
        "orderSn" : "test",
        "goodsId" : 1,
        "orderCreateTime" : 1,
        "orderLabel" : [ {
          "name" : "test",
          "value" : 1
        } ],
        "orderStatus" : 1,
        "inventoryDeductionWarehouseId" : "test",
        "originalGoodsName" : "test",
        "qualificationUploadEndTime" : 1,
        "fulfillmentType" : "test",
        "isCancelledDuringPending" : true,
        "spec" : "test",
        "fulfillmentWarning" : [ "test", "test" ],
        "packageAbnormalTypeList" : [ "test", "test" ],
        "orderPaymentType" : "test",
        "originalSpecName" : "test",
        "originalOrderQuantity" : 1,
        "thumbUrl" : "test",
        "goodsName" : "test",
        "inventoryDeductionWarehouseName" : "test",
        "skuId" : 1,
        "productList" : [ {
          "productSkuId" : 1,
          "soldFactor" : 1,
          "extCode" : "test",
          "productId" : 1
        } ],
        "orderShippingTime" : 1
      } ]
    } ]
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```