# bg.logistics.shipment.update

**Try buy shipping again api**

The bg.logistics.shipment.update interface is for sellers to create shipment logistics orders later, and to re-order online if the order fails.

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
| retrySendPackageRequestList | 8 | No |  |  |
| shipLaterLimitTime | 4 | No |  |  |

## Response Parameters

| Parameter | Type | Required | Description | Example |
|---|---|---|---|---|
| success | 5 | No |  |  |
| errorCode | 1 | No |  |  |
| errorMsg | 4 | No |  |  |
| result | 5 | No |  |  |

## Error Codes

| Error Code | Message |
|---|---|
| 120018078 | Cannot set shipLaterLimitTime: order was created for immediate shipment. |
| 120011018 | Orders with "signature_required_on_delivery" can only buy shipping label from the channel which provide signature service,please call "bg.logistics.shippingservices.get" to get the recommended channels. |
| 120015507 | Wrong package {*} information. Try again. |
| 120012044 | This channel requires passing the exam  to gain access. |
| 120011101 | The invoice has expired. |
| 120011102 | The CNPJ on the invoice does not match the current entity's CNPJ. |
| 120011103 | The invoice amount cannot be zero. |
| 120011104 | The invoice issue date exceeds the allowed 180-day period. |
| 120011105 | The specified state code in the accessKey does not exist. |
| 120011106 | Invoice type validation in the accessKey failed. |
| 120011107 | Verification timed out, please try again. |
| 120011108 | The specified invoice does not exist. |
| 120012061 | The current parent order has a pending risk control alert, It is not recommended to proceed with the performance. You can submit a cancellation request. |
| 120011096 | Invalid parameters detected in interlineShipCompanyList |
| 120019009 | Invalid pickup reservation time. See pickupRules for valid options. |
| 120011015 | Incomplete warehouse details. Update in Seller Central to process shipment. |
| 120015538 | Brazil orders are restricted to using exclusively TEMU platform shipping labels for self-fulfillment |
| 120011094 | The necessary parameter invoiceAccessKey is missing |
| 120011088 | Invoice access key verification failed. Please check if the invoiceAccessKey is valid |
| 120015040 | The parent order {*} can not be fulfilled by the selected logistics provider due to the customer's delivery preferences. Please change another logistics provider to fulfill again. |
| 120015545 | Orders with "signature_required_on_delivery" can only buy shipping label from the channel which provide signature service. Please call "bg.logistics.shippingservices.get" to get the recommended channel and request with the field "signServiceId". |
| 120015543 | The Order with label "signature_required_on_delivery" and other orders cannot be fulfilled at the same time. Please fulfill the order with label "signature_required_on_delivery" separately. |
| 120015037 | This logistics provider does not support this business scenario. |
| 120018010 | The packages {*} have been canceled. Please fulfill again by Temu non-integrated logistics or Temu integrated logistics. |
| 120019024 | Invalid pickup time range. Please ensure times are within the next 5 calendar days (9:00-16:00), on the same day,  and pickupStartTime is before pickupEndTime |
| 120018062 | COD orders do not allow updating shipping information. |
| 120011051 | COD orders do not allow adding sub-packages |
| 120015032 | You should choose one fulfillment way and fulfill channelId or shipLogisticsType. |
| 120011030 | Cooperative warehouse order fulfillment restricted. |
| 120018049 | Failed to update shipping information. Please cancel the appointment for pickup first. |
| 120011082 | Failed to buy the shipping label. Please fill in the warehouse management type and warehouse brand in the Temu seller center first. |
| 120015518 | The order with "US-to-CA" Label and the order without "US-to-CA" Label can't be shipped together. |
| 120011043 | Missing required parameters for 'sendSubRequestList'. |
| 120011044 | Exceeded maximum allowed attached packages. Limit is 10. |
| 120011045 | For splitSubPackage quantity needs to be 1. |
| 120012029 | Warehouse and recipient in different countries splitSubPackage cannot enter "TRUE". |
| 120015520 | Call failed: Cannot convert subPackage to self-shipment. |
| 120012023 | Address change pending. Please process before shipping. |
| 120012030 | Order cancel pending. Please process before shipping. |
| 120019016 | Unexpected  parameter pickupTime. |
| 120019017 | Miss required parameter pickupTime. |
| 120018017 | Does not support retrying twice |
| 120018013 | Does not support this package retry |
| 120015026 | A large items template has been used for the items in this package. Only specified logistics providers can be used for shipping. |
| 120013007 | Product sku sensitive query fail |
| 120013008 | Order lacks necessary sensitive attributes. |
| 120013009 | Order lacks necessary sensitive attributes. |
| 120018004 | Only allow adjustments to warehouseId, weight, dimensions, shipping company, etc. |
| 120011047 | Not support local mall |
| 120011048 | Usage channel does not match the confirmation scenario |
| 120012031 | The current parent order has a pending risk control alert. |
| 120018020 | The BBC order is not allowed. |
| 120015027 | A large items template has been used for the items in this package. Only special channels can be used for shipping. |
| 120018025 | Orders exist after-sales applications, please complete the processing before operation |
| 120012007 | The parentOrder or Order is invalid. Please check if the parentOrder matches the Order, the parentOrder or Order is nonexistent etc. |
| 120015521 | The parameter Weight should be integer. |
| 120011006 | The parameter warehouseId is invalid. |
| 120011072 | The request area is incorrect. Please check the request area and replace it with the correct request area. The request area for the United States is US, and the request area for other non-European countries is global. |
| 120012016 | The parentOrder or Order is invalid. Please check if the parentOrder matches the Order, the parentOrder or Order is nonexistent etc. |
| 120018027 | The packageSn is invalid. Please check the request area or if the packageSn is nonexistent etc. |
| 120015528 | O-orders of COD type exist in body, and COD type O-orders can only be shipped with Temu Label. |
| 120018002 | The package is not in failed state, please check the package status. |
| 120011020 | Invalid request parameters |

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "access_token" : "test",
  "retrySendPackageRequestList" : [ {
    "invoiceAccessKey" : "test",
    "extendWeightUnit" : "test",
    "pickupStartTime" : 1,
    "splitSubPackage" : true,
    "extendWeight" : "test",
    "pickupEndTime" : 1,
    "packageSn" : "test",
    "length" : "test",
    "dimensionUnit" : "test",
    "weight" : "test",
    "retrySendSubRequestList" : [ {
      "invoiceAccessKey" : "test",
      "extendWeightUnit" : "test",
      "pickupStartTime" : 1,
      "extendWeight" : "test",
      "pickupEndTime" : 1,
      "packageSn" : "test",
      "length" : "test",
      "dimensionUnit" : "test",
      "weight" : "test",
      "interlineShipCompanyList" : [ {
        "shipLogisticsType" : "test",
        "shipStageType" : "test",
        "shipCompanyId" : 1,
        "channelId" : 1
      } ],
      "shipCompanyId" : 1,
      "confirmAcceptance" : [ "test", "test" ],
      "warehouseId" : "test",
      "width" : "test",
      "shipLogisticsType" : "test",
      "signServiceId" : 1,
      "channelId" : 1,
      "weightUnit" : "test",
      "height" : "test"
    } ],
    "interlineShipCompanyList" : [ {
      "shipLogisticsType" : "test",
      "shipStageType" : "test",
      "shipCompanyId" : 1,
      "channelId" : 1
    } ],
    "shipCompanyId" : 1,
    "confirmAcceptance" : [ "test", "test" ],
    "warehouseId" : "test",
    "orderSendInfoList" : [ {
      "quantity" : 1,
      "orderSn" : "test",
      "parentOrderSn" : "test",
      "goodsId" : 1,
      "skuId" : 1
    } ],
    "width" : "test",
    "shipLogisticsType" : "test",
    "signServiceId" : 1,
    "autoConfirmAfterPickup" : true,
    "channelId" : 1,
    "weightUnit" : "test",
    "height" : "test"
  } ],
  "app_key" : "test",
  "sign" : "test",
  "data_type" : "test",
  "shipLaterLimitTime" : "test",
  "type" : "test",
  "version" : "test",
  "timestamp" : "test"
}'
```

## Response Example

```json
{
  "result" : true,
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```