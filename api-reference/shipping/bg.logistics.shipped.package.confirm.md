# bg.logistics.shipped.package.confirm

**bg logistics shipped package confirm**

The bg.logistics.shipped.package.confirm interface is for sellers to support batch conversion of packages that have been fulfilled successfully by Temu-integrated channel but not shipped to shipped, and will be automatically converted to shipped if not converted within 48 hours.

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
| packageSendInfoList | 8 | No |  |  |

## Response Parameters

| Parameter | Type | Required | Description | Example |
|---|---|---|---|---|
| result | 6 | No |  |  |
| success | 5 | No |  |  |
| errorCode | 1 | No |  |  |
| errorMsg | 4 | No |  |  |

## Error Codes

| Error Code | Message |
|---|---|
| 120018010 | The packages {*} have been canceled. Please fulfill again by Temu non-integrated logistics or Temu integrated logistics. |
| 120014002 | The field trackingNumber {*} does not match packageSn {*}. Please check the matching relationship between the two fields. |
| 120011030 | Cooperative warehouse order fulfillment restricted. |
| 120018015 | The package has been canceled, please fulfill again by Temu non-integrated logistics or Temu integrated logistics. |
| 120012012 | There are no shippable orders matching the item. |
| 120012004 | The order has been shipped. This submission is not effective for the shipped order. |
| 120013002 | Item quantity does not match. |
| 120011046 | Sub package not allowed. |
| 120015026 | A large items template has been used for the items in this package. Only specified logistics providers can be used for shipping. |
| 120015027 | A large items template has been used for the items in this package. Only special channels can be used for shipping. |
| 120018025 | Orders exist after-sales applications, please complete the processing before operation |
| 120011072 | The request area is incorrect. Please check the request area and replace it with the correct request area. The request area for the United States is US, and the request area for other non-European countries is global. |
| 120012007 | The parentOrder or Order is invalid. Please check if the parentOrder matches the Order, the parentOrder or Order is nonexistent etc. |
| 120012016 | The parentOrder or Order is invalid. Please check if the parentOrder matches the Order, the parentOrder or Order is nonexistent etc. |
| 120018027 | The packageSn is invalid. Please check the request area or if the packageSn is nonexistent etc. |

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "access_token" : "test",
  "app_key" : "test",
  "packageSendInfoList" : [ {
    "packageSn" : "test",
    "trackingNumber" : "test",
    "packageDetail" : [ {
      "orderSn" : "test",
      "parentOrderSn" : "test",
      "quantity" : 1
    } ]
  } ],
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
    "warningMessage" : [ {
      "packageSn" : "test",
      "warningMessage" : "test"
    } ]
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```