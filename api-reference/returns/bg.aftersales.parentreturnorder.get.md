# bg.aftersales.parentreturnorder.get

**Query after-sales reverse logistics information.**

This interface is designed to provide merchants or administrators within an e-commerce platform with detailed return logistics information for a set of after-sales service requests.

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
| parentAfterSalesSn | 4 | No |  |  |
| afterSalesSn | 4 | No |  |  |

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
| 130010001 | The parameter is illegal. Please check if the input parameter meets the regulations. |

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "access_token" : "test",
  "parentAfterSalesSn" : "test",
  "app_key" : "test",
  "afterSalesSn" : "test",
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
    "logisticsInfoList" : [ {
      "carrierName" : "test",
      "returnWarehouseRegion1Name" : "test",
      "returnWarehouseType" : 1,
      "trackingNumber" : "test"
    } ]
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```