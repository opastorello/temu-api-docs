# bg.cooperativewarehouse.fulfill.query

**Cooperative warehouse fulfill query**

cooperate warehouse erp order

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
| erpFulfillNoList | 8 | No |  |  |
| cwFulfillNoList | 8 | No |  |  |

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
| 170020001 | This ERP provider is not supported. |
| 170020002 | This mall is not authorized to the cooperative warehouse  service provider. |
| 170020003 | The parameter is illegal, please check  and try again. |
| 170020004 | This fulfillment order not exists, please check if the fulfillment number is correct. |
| 170020005 | This cooperative warehouse customer code is not match the authorized customer code. |

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "access_token" : "test",
  "app_key" : "test",
  "erpFulfillNoList" : [ "test", "test" ],
  "sign" : "test",
  "data_type" : "test",
  "cwFulfillNoList" : [ "test", "test" ],
  "type" : "test",
  "version" : "test",
  "timestamp" : "test"
}'
```

## Response Example

```json
{
  "result" : {
    "erpFulfillList" : [ {
      "cwFulfillNo" : "test",
      "fulfillCancelFailReason" : "test",
      "tailShippingMode" : 1,
      "fulfillStatus" : 1,
      "erpFulfillNo" : "test",
      "logisticsProductCode" : "test",
      "failCode" : "test",
      "orderList" : [ {
        "quantity" : 1,
        "orderSn" : "test",
        "shipCompanyName" : "test",
        "parentOrderSn" : "test",
        "cwSkuCode" : "test",
        "trackingNumber" : "test",
        "skuId" : 1,
        "shipCompanyId" : 1
      } ],
      "failReason" : "test",
      "warehouseProviderCode" : "test",
      "warehouseCode" : "test",
      "fulfillCancelStatus" : 1
    } ]
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```