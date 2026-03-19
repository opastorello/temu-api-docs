# bg.logistics.shipment.shippingtype.update

**Edit shipping information api**

The bg.logistics.shipment.shippingtype.update interface is used by sellers to update logistics tracking numbers, supporting the following scenarios: non-integrated logistics updating logistics tracking numbers; Temu-integrated logistics has been changed to non-integrated logistics.

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
| editPackageRequestList | 8 | No |  |  |

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
| 120012015 | Combined delivery failed since the delivery addresses for PO orders are different. |
| 120012064 | The parentOrderSn is not valid for the selected selfShippingWarehouseId. |
| 120012063 | The parentOrderSn is not valid for the selected selfShippingWarehouseId. |
| 120011011 | Items from the current warehouse cannot be delivered to the user's address. |
| 120011086 | Please fill in the warehouse management type and warehouse brand in the Temu seller center first. Then you can confirm shipment as usual. |
| 120011085 | selfShippingWarehouseId is invalid, please have a check |
| 120015527 | Missing required parameter selfShippingWarehouseId |
| 120015537 | Brazil orders require Temu shipping labels exclusively |
| 120015037 | This logistics provider does not support this business scenario. |
| 120018010 | The packages {*} have been canceled. Please fulfill again by Temu non-integrated logistics or Temu integrated logistics. |
| 120015528 | O-orders of COD type exist in body, and COD type O-orders can only be shipped with Temu Label. |
| 120018015 | The package has been canceled, please fulfill again by Temu non-integrated logistics or Temu integrated logistics. |
| 120011030 | Cooperative warehouse order fulfillment restricted. |
| 120018049 | Failed to update shipping information. Please cancel the appointment for pickup first. |
| 120011059 | Your store has been restricted from confirming shipment by USPS tracking number. Please use the online buy shipping function to buy USPS shipping label instead. |
| 120014020 | Delivery failed because the tracking number cannot be recognized. Please delete specific symbol such as -, %, # etc. |
| 120011020 | Invalid request parameters |
| 120011043 | Missing required parameters for 'sendSubRequestList'. |
| 120011044 | Exceeded maximum allowed attached packages. Limit is 10. |
| 120011045 | For splitSubPackage quantity needs to be 1. |
| 120015520 | Call failed: Cannot convert subPackage to self-shipment. |
| 120014019 | Cannot ship with Platform-Generated tracking number. |
| 120015026 | A large items template has been used for the items in this package. Only specified logistics providers can be used for shipping. |
| 120018021 | The BC order is not allowed. |
| 120018027 | The packageSn is invalid. Please check the request area or if the packageSn is nonexistent etc. |
| 120015529 | The current package does not meet the modification conditions and cannot be edited. |
| 120012034 | Your store has been restricted from confirming shipment by tracking number. Please use the online buy shipping function instead. For more details, please refer to the message in the Seller Center regarding the notice on the restriction of the "confirm shipment by tracking number". |
| 120015030 | A large items template has been used for the items in this package. Only specified logistics providers can be used for shipping. |

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "access_token" : "test",
  "editPackageRequestList" : [ {
    "packageSn" : "test",
    "selfShippingWarehouseId" : "test",
    "trackingNumber" : "test",
    "shipCompanyId" : 1
  } ],
  "app_key" : "test",
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
  "result" : true,
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```