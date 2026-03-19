# bg.logistics.shipment.sub.confirm

**Add additional tracking information in batch api**

The bg.logistics.shipment.sub.confirm interface should only be used in scenarios where the smallest sku needs to be shipped as split packages, and can append the sub-parcel information to the main parcel.

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
| mainPackageSn | 4 | No |  |  |
| sendSubRequestList | 8 | No |  |  |

## Response Parameters

| Parameter | Type | Required | Description | Example |
|---|---|---|---|---|
| result | 5 | No |  |  |
| success | 5 | No |  |  |
| errorCode | 1 | No |  |  |
| errorMsg | 4 | No |  |  |

## Error Codes

| Error Code | Message |
|---|---|
| 120014022 | Incorrect trackingNumber/carrierId. Please check and retry. |
| 120014001 | Tracking number is blank. |
| 120014023 | Tracking number is invalid: {*}. |
| 120014005 | Tracking number may be invalid. Please verify before proceeding. |
| 120014008 | Delivery failed because the tracking number cannot be recognized. Please check and try again. |
| 120012064 | The parentOrderSn is not valid for the selected selfShippingWarehouseId. |
| 120012063 | The parentOrderSn is not valid for the selected selfShippingWarehouseId. |
| 120011011 | Items from the current warehouse cannot be delivered to the user's address. |
| 120011086 | Please fill in the warehouse management type and warehouse brand in the Temu seller center first. Then you can confirm shipment as usual. |
| 120011085 | selfShippingWarehouseId is invalid, please have a check |
| 120015537 | Brazil orders require Temu shipping labels exclusively |
| 120012043 | Sub-package can only be added once. |
| 120015037 | This logistics provider does not support this business scenario. |
| 120011059 | Your store has been restricted from confirming shipment by USPS tracking number. Please use the online buy shipping function to buy USPS shipping label instead. |
| 120014020 | Delivery failed because the tracking number cannot be recognized. Please delete specific symbol such as -, %, # etc. |
| 120011001 | System abnormality, please check the data and try again |
| 120011002 | Invalid request parameters. |
| 120011006 | The parameter warehouseId is invalid. |
| 120011020 | Invalid request parameters |
| 120011022 | Invalid request parameters |
| 120011030 | Cooperative warehouse order fulfillment restricted. |
| 120011031 | The provider has at least one unsigned agreement. Please go to the home page to sign. |
| 120014003 | Duplicate tracking number |
| 120014004 | Tracking number has been used |
| 120014006 | System abnormality, please try again later |
| 120015002 | Invalid logistics company ID |
| 120015559 | Delivery failed because the tracking number cannot be recognized. Please check and try again. |
| 120015560 | The requirements for creating a package are incorrect or conditions are not met. Please check again. |
| 120011065 | Please fill in the shipping address. |
| 120015026 | A large items template has been used for the items in this package. Only specified logistics providers can be used for shipping. |
| 120015527 | Missing required parameter selfShippingWarehouseId |
| 120018021 | The BC order is not allowed. |
| 120018027 | The packageSn is invalid. Please check the request area or if the packageSn is nonexistent etc. |
| 120015528 | O-orders of COD type exist in body, and COD type O-orders can only be shipped with Temu Label. |
| 120012034 | Your store has been restricted from confirming shipment by tracking number. Please use the online buy shipping function instead. For more details, please refer to the message in the Seller Center regarding the notice on the restriction of the "confirm shipment by tracking number". |
| 120015030 | A large items template has been used for the items in this package. Only specified logistics providers can be used for shipping. |
| 120014019 | Cannot ship with Platform-Generated tracking number. |

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
  "mainPackageSn" : "test",
  "sendSubRequestList" : [ {
    "carrierId" : 1,
    "selfShippingWarehouseId" : "test",
    "trackingNumber" : "test"
  } ],
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