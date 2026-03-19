# bg.cooperativewarehouse.fulfill.submit

**Cooperative warehouse fulfill submit**

cooperativewarehouse_fulfill

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
| warehouseProviderCode | 4 | No |  |  |
| authorizeType | 1 | No |  |  |
| authorizeKey | 4 | No |  |  |
| authorizeToken | 4 | No |  |  |
| cwCustomerCode | 4 | No |  |  |
| warehouseCode | 4 | No |  |  |
| erpFulfillNo | 4 | No |  |  |
| tailShippingMode | 1 | No |  |  |
| logisticsProductCode | 4 | No |  |  |
| packageSn | 4 | No |  |  |
| shipCompanyId | 2 | No |  |  |
| channelId | 2 | No |  |  |
| channelVersionId | 2 | No |  |  |
| shipCompanyName | 4 | No |  |  |
| trackingNumber | 4 | No |  |  |
| shippingLabelFileType | 4 | No |  |  |
| shippingLabelFileBase64 | 4 | No |  |  |
| shipLogisticsType | 4 | No |  |  |
| orderList | 8 | No |  |  |

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
| 170020038 | The [authorizeType] is 1, and the required parameter [authorizeToken] has not been filled in |
| 170020037 | The [authorizeType] is 0, and the required parameter [cwCustomerCode] has not been filled in |
| 170020036 | The [tailShippingMode] is 1, and the required parameter [shipLogisticsType] has not been filled in |
| 170020035 | The [tailShippingMode] is 1, and the required parameter [channelId] has not been filled in |
| 170020034 | The [tailShippingMode] is 1, and the required parameter [shipCompanyId] has not been filled in |
| 170020033 | The [tailShippingMode] is 1, and the required parameter [shippingLabelFileBase64] has not been filled in |
| 170020032 | The [tailShippingMode] is 1, and the required parameter [shippingLabelFileType] has not been filled in |
| 170020031 | [tailShippingMode] is 1, and the required parameter [trackingNumber] has not been filled in |
| 170020030 | The [tailShippingMode] is 1, and the required parameter [shipCompanyName] has not been filled in |
| 170020029 | The [tailShippingMode] is 1, and the required parameter [packageSn] has not been filled in |
| 170020028 | The [tailShippingMode] is 0, and the required parameter [logisticsProductCode] has not been filled in |
| 170020027 | Parameter [quantity] is required but not provided in the input |
| 170020026 | Parameter [cwSkuCode] is required but not provided in the input |
| 170020025 | Parameter [parentOrderSn] is required but not provided in the input |
| 170020024 | Parameter [orderSn] is required but not provided in the input |
| 170020023 | Parameter [orderList] is required but not provided in the input |
| 170020022 | Parameter [erpFulfillNo] is required but not provided in the input |
| 170020021 | Parameter [warehouseProviderCode] is required but not provided in the input |
| 170020017 | Parameter {*} is required but not provided in the input. |
| 170020018 | The [authorizeType] is {*} , and the required parameter {*} has not been filled in. |
| 170020019 | The [tailShippingMode] is {*} and the required parameter {*} has not been filled in. |
| 170020001 | This ERP provider is not supported. |
| 170020002 | This mall is not authorized to the cooperative warehouse  service provider. |
| 170020003 | The parameter is illegal, please check  and try again. |
| 170020005 | This cooperative warehouse customer code is not match the authorized customer code. |
| 170020009 | This fulfillment order already exists, please submit another one. |
| 170020004 | This fulfillment order not exists, please check if the fulfillment number is correct. |
| 170020006 | This fulfillment order has wrong tail shipping mode, please check  and try again. |
| 170020007 | This fulfillment order has wrong shipping label file type, please check  and try again. |
| 170020008 | This fulfillment order has wrong shipping label file content, please check  and try again. |
| 170020010 | The service provider does not support shipping label for the current shippingCompanyName. Please place an order with another shippingCompanyName or place an order with another method. |
| 170020011 | This ship company id not match with the ship company name mapped. |
| 170020012 | The parentOrderSn in fulfill order is invalid. |
| 170020013 | The service provider has not signed the DPA Agreement of the country and cannot perform the contract. Please place the order in another method. |
| 170020014 | The cooperative warehouse service provider returned: API authorization exception, please update the token in time. |
| 170020015 | The current order does not support address query, please check! |
| 170020016 | Your store has been restricted from using the function of logistics shipping by partner warehouse service providers. Please use the platform shipping labels for partner warehouses or the online order shipping function instead. For more details, please refer to the message in the Seller Center regarding the notice on the restriction of the "Self-import Waybill" shipping function. |

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "sign" : "test",
  "logisticsProductCode" : "test",
  "type" : "test",
  "warehouseCode" : "test",
  "authorizeType" : 1,
  "channelVersionId" : 1,
  "authorizeKey" : "test",
  "shipLogisticsType" : "test",
  "trackingNumber" : "test",
  "warehouseProviderCode" : "test",
  "channelId" : 1,
  "timestamp" : "test",
  "tailShippingMode" : 1,
  "cwCustomerCode" : "test",
  "erpFulfillNo" : "test",
  "packageSn" : "test",
  "orderList" : [ {
    "cwSkuCode" : "test",
    "productSkuId" : 1,
    "quantity" : 1,
    "orderSn" : "test",
    "parentOrderSn" : "test",
    "skuId" : 1
  } ],
  "version" : "test",
  "shippingLabelFileType" : "test",
  "shipCompanyId" : 1,
  "access_token" : "test",
  "app_key" : "test",
  "shippingLabelFileBase64" : "test",
  "authorizeToken" : "test",
  "shipCompanyName" : "test",
  "data_type" : "test"
}'
```

## Response Example

```json
{
  "result" : {
    "fulfillStatus" : 1,
    "erpFulfillNo" : "test",
    "cwFulfillNo" : "test"
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```