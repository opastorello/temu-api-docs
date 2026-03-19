# bg.order.unshipped.package.get

**bg order unshipped package get**

The bg.order.unshipped.package.get interface is for sellers to query information about packages that have been fulfilled successfully by Temu-integrated channel.

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
| parentOrderSnList | 8 | No |  |  |
| pageNumber | 1 | No |  |  |
| pageSize | 1 | No |  |  |
| orderSnList | 8 | No |  |  |

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
| 120011030 | Cooperative warehouse order fulfillment restricted. |
| 120011072 | The request area is incorrect. Please check the request area and replace it with the correct request area. The request area for the United States is US, and the request area for other non-European countries is global. |
| 120012016 | The parentOrder or Order is invalid. Please check if the parentOrder matches the Order, the parentOrder or Order is nonexistent etc. |

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "access_token" : "test",
  "parentOrderSnList" : [ "test", "test" ],
  "app_key" : "test",
  "pageNumber" : 1,
  "sign" : "test",
  "data_type" : "test",
  "pageSize" : 1,
  "type" : "test",
  "version" : "test",
  "orderSnList" : [ "test", "test" ],
  "timestamp" : "test"
}'
```

## Response Example

```json
{
  "result" : {
    "totalItemNum" : 1,
    "unshippedPackage" : [ {
      "carrierName" : "test",
      "subPackageSnList" : [ "test", "test" ],
      "packageDetail" : {
        "canceledOrders" : [ {
          "orderSn" : "test",
          "parentOrderSn" : "test",
          "quantity" : 1
        } ],
        "shippableOrders" : [ {
          "orderSn" : "test",
          "parentOrderSn" : "test",
          "quantity" : 1
        } ]
      },
      "packageSn" : "test",
      "mainPackageSn" : "test",
      "carrierId" : 1,
      "subPackageType" : "test",
      "trackingNumber" : "test"
    } ]
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```