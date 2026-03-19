# temu.aftersales.returnlabel.prepare.get

**Query return label preparation information**

This interface is designed to query return label preparation information.

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
| parentOrderSn | 4 | No |  |  |

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
| 130010001 | The parameter is illegal. Please check if the input parameter meets the regulations. |
| 130010005 | operate forbid |

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "access_token" : "test",
  "parentAfterSalesSn" : "test",
  "app_key" : "test",
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
    "userPickUpTimezone" : "test",
    "userSelectedPickUpTimeList" : [ {
      "endTimestamp" : 1,
      "startTimestamp" : 1
    } ],
    "availableReturnWarehouseList" : [ {
      "warehouseId" : "test",
      "warehouseName" : "test"
    } ],
    "merchantLatestPickUpTime" : 1
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```