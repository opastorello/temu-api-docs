# bg.order.detail.v2.get

**Get Order Detail information**

The bg.order.detail.v2.get interface is designed for merchants to retrieve detailed information about a specific order within their respective stores. This functionality provides merchants with access to comprehensive order details, enabling them to process, fulfill, and manage individual orders with precision.

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
| fulfillmentTypeList | 8 | No |  |  |

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
| 140020009 | Some order fields are still being calculated by the system. Please try again later. |
| 140020001 | This interface does not support cross-border sellers. Please check whether the store bound to the token is a SEMI or LOCAL store! |
| 140020002 | Order not found |
| 140020003 | The provider has at least one unsigned agreement. Please go to the home page to sign. |

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "access_token" : "test",
  "app_key" : "test",
  "fulfillmentTypeList" : [ "test", "test" ],
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
      "regionName3" : "test",
      "parentOrderLabel" : [ {
        "name" : "test",
        "value" : 1
      } ],
      "regionName1" : "test",
      "regionName2" : "test",
      "shippingMethod" : 1,
      "parentShippingTime" : 1,
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
      "hasShippingFee" : true,
      "paymentInfo" : [ {
        "paymentMethod" : "test",
        "paymentProcessorRegister" : "test",
        "paymentCardBrand" : "test",
        "paymentAuthCode" : "test"
      } ]
    },
    "orderList" : [ {
      "orderSn" : "test",
      "goodsId" : 1,
      "orderLabel" : [ {
        "name" : "test",
        "value" : 1
      } ],
      "orderStatus" : 1,
      "fulfillmentType" : "test",
      "isCancelledDuringPending" : true,
      "spec" : "test",
      "packageAbnormalTypeList" : [ "test", "test" ],
      "orderPaymentType" : "test",
      "thumbUrl" : "test",
      "goodsName" : "test",
      "skuId" : 1,
      "canceledQuantityBeforeShipment" : 1,
      "quantity" : 1,
      "orderCreateTime" : 1,
      "inventoryDeductionWarehouseId" : "test",
      "originalGoodsName" : "test",
      "qualificationUploadEndTime" : 1,
      "fulfillmentWarning" : [ "test", "test" ],
      "originalSpecName" : "test",
      "hasUploadedEvidence" : true,
      "originalOrderQuantity" : 1,
      "packageSnInfo" : [ {
        "packageSn" : "test",
        "packageDeliveryType" : 1,
        "callSuccess" : true
      } ],
      "inventoryDeductionWarehouseName" : "test",
      "productList" : [ {
        "productSkuId" : 1,
        "soldFactor" : 1,
        "extCode" : "test",
        "productId" : 1
      } ],
      "orderShippingTime" : 1
    } ]
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```