# bg.logistics.shipment.v2.confirm

**Confirm Order Shipment**

The bg.logistic.shipment.v2.confirm interface is designed to synchronize and return order fulfillment information through this interface. Switch the order status from pending shipment to shipped.

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
| sendType | 1 | No |  |  |
| sendRequestList | 8 | No |  |  |

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
| 120015539 | Combination failed: certain orders cannot be shipped together due to Seller Center restrictions. Please refer to Seller Central for specific rules or check with Seller Center support. |
| 120012004 | The order has been shipped. This submission is not effective for the shipped order. |
| 120012015 | Combined delivery failed since the delivery addresses for PO orders are different. |
| 120014001 | Tracking number is blank. |
| 120014023 | Tracking number is invalid: {*}. |
| 120014005 | Tracking number may be invalid. Please verify before proceeding. |
| 120014008 | Delivery failed because the tracking number cannot be recognized. Please check and try again. |
| 120014022 | Incorrect trackingNumber/carrierId. Please check and retry. |
| 120012064 | The parentOrderSn is not valid for the selected selfShippingWarehouseId. |
| 120012063 | The parentOrderSn is not valid for the selected selfShippingWarehouseId. |
| 120011011 | Items from the current warehouse cannot be delivered to the user's address. |
| 120011086 | Please fill in the warehouse management type and warehouse brand in the Temu seller center first. Then you can confirm shipment as usual. |
| 120011085 | selfShippingWarehouseId is invalid, please have a check |
| 120012041 | A duplicate sub-order number has been entered for tracking number {*}. |
| 120015537 | Brazil orders require Temu shipping labels exclusively |
| 120011045 | For splitSubPackage quantity needs to be 1. |
| 120011098 | A package is allowed to add a maximum of only 10 sub tracking numbers. |
| 120015543 | The Order with label "signature_required_on_delivery" and other orders cannot be fulfilled at the same time. Please fulfill the order with label "signature_required_on_delivery" separately. |
| 120015037 | This logistics provider does not support this business scenario. |
| 120011030 | Cooperative warehouse order fulfillment restricted. |
| 120012020 | Buy shipping failed. Package number {*} is existent. Courier and tracking number cannot be entered directly. Please edit or try again on the order details page. |
| 120011059 | Your store has been restricted from confirming shipment by USPS tracking number. Please use the online buy shipping function to buy USPS shipping label instead. |
| 120014020 | Delivery failed because the tracking number cannot be recognized. Please delete specific symbol such as -, %, # etc. |
| 120011031 | The provider has at least one unsigned agreement. Please go to the home page to sign. |
| 120015518 | The order with "US-to-CA" Label and the order without "US-to-CA" Label can't be shipped together. |
| 120012023 | Address change pending. Please process before shipping. |
| 120012030 | Order cancel pending. Please process before shipping. |
| 120011065 | Please fill in the shipping address. |
| 120014019 | Cannot ship with Platform-Generated tracking number. |
| 120011006 | The parameter warehouseId is invalid. |
| 120015026 | A large items template has been used for the items in this package. Only specified logistics providers can be used for shipping. |
| 120015527 | Missing required parameter selfShippingWarehouseId |
| 120012031 | The current parent order has a pending risk control alert. |
| 120018021 | The BC order is not allowed. |
| 120012007 | The parentOrder or Order is invalid. Please check if the parentOrder matches the Order, the parentOrder or Order is nonexistent etc. |
| 120017007 | The cancellation application is under review and cannot be shipped. |
| 120011072 | The request area is incorrect. Please check the request area and replace it with the correct request area. The request area for the United States is US, and the request area for other non-European countries is global. |
| 120012016 | The parentOrder or Order is invalid. Please check if the parentOrder matches the Order, the parentOrder or Order is nonexistent etc. |
| 120015528 | O-orders of COD type exist in body, and COD type O-orders can only be shipped with Temu Label. |
| 120012034 | Your store has been restricted from confirming shipment by tracking number. Please use the online buy shipping function instead. For more details, please refer to the message in the Seller Center regarding the notice on the restriction of the "confirm shipment by tracking number". |
| 120015030 | A large items template has been used for the items in this package. Only specified logistics providers can be used for shipping. |
| 120014003 | Duplicate tracking number |
| 120014004 | Tracking number has been used |
| 120014006 | System abnormality, please try again later |

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "access_token" : "test",
  "sendRequestList" : [ {
    "orderSendInfoList" : [ {
      "quantity" : 1,
      "orderSn" : "test",
      "parentOrderSn" : "test",
      "goodsId" : 1,
      "skuId" : 1
    } ],
    "selfShippingWarehouseId" : "test",
    "subSendRequests" : [ {
      "carrierId" : 1,
      "trackingNumber" : "test",
      "selfShippingWarehouseId" : "test"
    } ],
    "confirmAcceptance" : [ "test", "test" ],
    "carrierId" : 1,
    "trackingNumber" : "test"
  } ],
  "app_key" : "test",
  "sign" : "test",
  "data_type" : "test",
  "sendType" : 1,
  "type" : "test",
  "version" : "test",
  "timestamp" : "test"
}'
```

## Response Example

```json
{
  "result" : {
    "assistantAgreementText" : "test",
    "warningMessage" : [ "test", "test" ]
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```