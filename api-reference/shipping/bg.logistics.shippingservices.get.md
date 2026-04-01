# bg.logistics.shippingservices.get

**Get available shipping services api**

The bg.logistics.shippingservices.get interface is for sellers to retrieve supported shipping carriers based on package dimensions and weight, which allows sellers to quickly determine which carriers can handle shipment based on the provided package weight and volume information. This interface simplifies the process of selecting the right shipping option, ensuring packages arrive safely and on time.

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
| warehouseId | 4 | No |  |  |
| orderSnList | 8 | No |  |  |
| shipOrderInfoList | 8 | No |  |  |
| weight | 4 | No |  |  |
| weightUnit | 4 | No |  |  |
| extendWeight | 4 | No |  |  |
| extendWeightUnit | 4 | No |  |  |
| length | 4 | No |  |  |
| width | 4 | No |  |  |
| height | 4 | No |  |  |
| dimensionUnit | 4 | No |  |  |
| signatureOnDelivery | 5 | No |  |  |
| invoiceAccessKey | 4 | No |  |  |

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
| 120015507 | Wrong package {*} information. Try again. |
| 120011101 | The invoice has expired. |
| 120011102 | The CNPJ on the invoice does not match the current entity's CNPJ. |
| 120011103 | The invoice amount cannot be zero. |
| 120011104 | The invoice issue date exceeds the allowed 180-day period. |
| 120011105 | The specified state code in the accessKey does not exist. |
| 120011106 | Invoice type validation in the accessKey failed. |
| 120011107 | Verification timed out, please try again. |
| 120011108 | The specified invoice does not exist. |
| 120012061 | The current parent order has a pending risk control alert, It is not recommended to proceed with the performance. You can submit a cancellation request. |
| 120018071 | The orderSn is not found under the parentOrderSn. |
| 120018072 | At least one of orderSnList or <parentOrderSn, orderSn> list must be provided. |
| 120018070 | Only one of orderSnList or <parentOrderSn, orderSn> list can be provided. |
| 120015569 | Orders to this country under the long-haul shipping mode do not support online ordering. Please remove the long-haul shipping items from your input parameters and place the order again. |
| 120018020 | The BBC order is not allowed. |
| 120011015 | Incomplete warehouse details. Update in Seller Central to process shipment. |
| 120015538 | Brazil orders are restricted to using exclusively TEMU platform shipping labels for self-fulfillment |
| 120011094 | The necessary parameter invoiceAccessKey is missing |
| 120011088 | Invoice access key verification failed. Please check if the invoiceAccessKey is valid |
| 120015544 | Orders {*} need to sign on delivery. Please request the field "signatureOnDelivery" with "True". |
| 120011030 | Cooperative warehouse order fulfillment restricted. |
| 120013007 | Product sku sensitive query fail |
| 120013008 | Order lacks necessary sensitive attributes. |
| 120013009 | Order lacks necessary sensitive attributes. |
| 120011047 | Not support local mall |
| 120011006 | The parameter warehouseId is invalid. |
| 120012007 | The parentOrder or Order is invalid. Please check if the parentOrder matches the Order, the parentOrder or Order is nonexistent etc. |
| 120015521 | The parameter Weight should be integer. |
| 120012016 | The parentOrder or Order is invalid. Please check if the parentOrder matches the Order, the parentOrder or Order is nonexistent etc. |
| 120011072 | The request area is incorrect. Please check the request area and replace it with the correct request area. The request area for the United States is US, and the request area for other non-European countries is global. |

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "invoiceAccessKey" : "test",
  "extendWeightUnit" : "test",
  "shipOrderInfoList" : [ {
    "orderSn" : "test",
    "parentOrderSn" : "test",
    "quantity" : 1
  } ],
  "extendWeight" : "test",
  "sign" : "test",
  "length" : "test",
  "dimensionUnit" : "test",
  "weight" : "test",
  "signatureOnDelivery" : true,
  "type" : "test",
  "version" : "test",
  "orderSnList" : [ "test", "test" ],
  "access_token" : "test",
  "app_key" : "test",
  "warehouseId" : "test",
  "data_type" : "test",
  "width" : "test",
  "timestamp" : "test",
  "weightUnit" : "test",
  "height" : "test"
}'
```

## Response Example

```json
{
  "result" : {
    "unavailableChannelDtoList" : [ {
      "estimatedText" : "test",
      "unavailableReason" : "test",
      "supportInterlineShipping" : true,
      "shipLogisticsType" : "test",
      "shippingCompanyName" : "test",
      "channelId" : 1,
      "shipCompanyId" : 1,
      "unavailableInterlineChannelList" : [ {
        "shipStageType" : "test",
        "shipLogisticsType" : "test",
        "shippingCompanyName" : "test",
        "channelId" : 1,
        "shipCompanyId" : 1
      } ]
    } ],
    "onlineChannelDtoList" : [ {
      "estimatedText" : "test",
      "estimatedCurrencyCode" : "test",
      "channelRules" : "test",
      "signServiceName" : "test",
      "infoNeeded" : [ "test", "test" ],
      "shipCompanyId" : 1,
      "pickupRules" : "test",
      "availablePickupTimeSlotList" : [ {
        "pickupEndTime" : 1,
        "pickupStartTime" : 1
      } ],
      "isNoContactDeliveryChannel" : true,
      "supportInterlineShipping" : true,
      "interlineChannelInfoList" : [ {
        "shipStageType" : "test",
        "shipLogisticsType" : "test",
        "shippingCompanyName" : "test",
        "channelId" : 1,
        "shipCompanyId" : 1
      } ],
      "shipLogisticsType" : "test",
      "signServiceId" : 1,
      "shippingCompanyName" : "test",
      "estimatedAmount" : "test",
      "channelId" : 1,
      "payWayCode" : 1
    } ]
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```