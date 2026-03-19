# bg.logistics.shipment.v2.get

**Get Order Shipment Information**

The bg.logistics.shipment.v2.get interface is for sellers to verify shipped info after self-fulfillment.

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
| parentOrderSn | 4 | No |  |  |
| orderSn | 4 | No |  |  |

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
| 120011072 | The request area is incorrect. Please check the request area and replace it with the correct request area. The request area for the United States is US, and the request area for other non-European countries is global. |
| 120012007 | The parentOrder or Order is invalid. Please check if the parentOrder matches the Order, the parentOrder or Order is nonexistent etc. |
| 120012016 | The parentOrder or Order is invalid. Please check if the parentOrder matches the Order, the parentOrder or Order is nonexistent etc. |

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "access_token" : "test",
  "app_key" : "test",
  "orderSn" : "test",
  "parentOrderSn" : "test",
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
    "shipmentInfoDTO" : [ {
      "quantity" : 1,
      "carrierName" : "test",
      "packageSn" : "test",
      "packageDeliveryType" : 1,
      "cooperativeWarehouseDTO" : {
        "warehouseProviderBrandName" : "test",
        "warehouseName" : "test",
        "warehouseProviderCode" : "test",
        "warehouseCode" : "test"
      },
      "carrierId" : 1,
      "trackingNumber" : "test",
      "trackingWarningLabel" : 1,
      "skuId" : 1,
      "subPackageShipmentInfoList" : [ {
        "packageSn" : "test",
        "packageDeliveryType" : 1,
        "carrierId" : 1,
        "carrierName" : "test",
        "trackingNumber" : "test"
      } ]
    } ]
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```