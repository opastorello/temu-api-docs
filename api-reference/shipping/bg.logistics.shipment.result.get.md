# bg.logistics.shipment.result.get

**Get buy shipping detail api**

The bg.logistics.shipment.result.get interface is for sellers to query the result of placing online logistics orders, with the shipping label status including in-progress{0}, successful{1}, and failed{2}.

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
| packageSnList | 8 | No |  |  |

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
| 120018027 | The packageSn is invalid. Please check the request area or if the packageSn is nonexistent etc. |

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "access_token" : "test",
  "app_key" : "test",
  "sign" : "test",
  "data_type" : "test",
  "packageSnList" : [ "test", "test" ],
  "type" : "test",
  "version" : "test",
  "timestamp" : "test"
}'
```

## Response Example

```json
{
  "result" : {
    "packageInfoResultList" : [ {
      "estimatedText" : "test",
      "estimatedCurrencyCode" : "test",
      "extendWeight" : "test",
      "packageDeliveryType" : 1,
      "dimensionUnit" : "test",
      "solutionText" : "test",
      "warehouseName" : "test",
      "failReasonText" : "test",
      "reservationSn" : "test",
      "subPackageSnList" : [ "test", "test" ],
      "mainPackageSn" : "test",
      "signServiceId" : 1,
      "shipLogisticsType" : "test",
      "isConfirmAfterPickup" : true,
      "subPackageType" : "test",
      "trackingNumber" : "test",
      "channelId" : 1,
      "height" : "test",
      "invoiceAccessKey" : "test",
      "extendWeightUnit" : "test",
      "pickupStartTime" : 1,
      "shippingLabelStatus" : 1,
      "canChangeToManualSend" : true,
      "pickupEndTime" : 1,
      "packageSn" : "test",
      "length" : "test",
      "weight" : "test",
      "warningMessage" : [ "test", "test" ],
      "interlineShipCompanyList" : [ {
        "shipLogisticsType" : "test",
        "shipStageType" : "test",
        "shippingCompanyName" : "test",
        "channelId" : 1,
        "shipCompanyId" : 1
      } ],
      "shipCompanyId" : 1,
      "warehouseId" : "test",
      "width" : "test",
      "orderSendInfoList" : [ {
        "quantity" : 1,
        "orderSn" : "test",
        "parentOrderSn" : "test",
        "goodsId" : 1,
        "skuId" : 1
      } ],
      "shippingCompanyName" : "test",
      "estimatedAmount" : "test",
      "weightUnit" : "test"
    } ]
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```