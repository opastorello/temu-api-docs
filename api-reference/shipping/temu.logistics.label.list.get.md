# temu.logistics.label.list.get

**temu logistics label list get**

You can use this interface to query the package information that has been fulfilled using the temu shipping form.

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
| temuLabelStatus | 1 | No |  |  |
| printStatus | 1 | No |  |  |
| createAtStart | 1 | No |  |  |
| createAtEnd | 1 | No |  |  |
| trackingNumberList | 8 | No |  |  |
| shippingCompanyIdList | 8 | No |  |  |
| parentOrderSnList | 8 | No |  |  |
| pageNumber | 1 | No |  |  |
| pageSize | 1 | No |  |  |

## Response Parameters

| Parameter | Type | Required | Description | Example |
|---|---|---|---|---|
| success | 5 | No |  |  |
| errorCode | 1 | No |  |  |
| errorMsg | 4 | No |  |  |
| result | 6 | No |  |  |

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "createAtEnd" : 1,
  "pageNumber" : 1,
  "printStatus" : 1,
  "sign" : "test",
  "trackingNumberList" : [ "test", "test" ],
  "packageSnList" : [ "test", "test" ],
  "pageSize" : 1,
  "type" : "test",
  "version" : "test",
  "createAtStart" : 1,
  "access_token" : "test",
  "temuLabelStatus" : 1,
  "parentOrderSnList" : [ "test", "test" ],
  "app_key" : "test",
  "shippingCompanyIdList" : [ "test", "test" ],
  "data_type" : "test",
  "timestamp" : "test"
}'
```

## Response Example

```json
{
  "result" : {
    "totalItemNum" : 1,
    "shippingLabelInfoList" : [ {
      "warehouseInfo" : {
        "warehouseId" : "test",
        "warehouseName" : "test"
      },
      "shippingLabelStatus" : 1,
      "createTime" : 1,
      "labelPrintStatus" : 1,
      "packageSn" : "test",
      "trackingInfoList" : [ {
        "trackingNumber" : "test",
        "shippingCompanyId" : 1,
        "shippingCompanyName" : "test"
      } ],
      "orderInfoList" : [ {
        "orderSn" : "test",
        "parentOrderSn" : "test",
        "quantity" : 1
      } ],
      "packageDimensionInfo" : {
        "extendWeightUnit" : "test",
        "extendWeight" : "test",
        "length" : "test",
        "width" : "test",
        "dimensionUnit" : "test",
        "weight" : "test",
        "weightUnit" : "test",
        "height" : "test"
      }
    } ]
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```