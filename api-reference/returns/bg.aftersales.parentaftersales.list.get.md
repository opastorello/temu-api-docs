# bg.aftersales.parentaftersales.list.get

**Query the information of parent after-sales orders**

This interface is designed to provide real-time updates on the current after-sales status of an order within an e-commerce platform. It allows merchants and buyers to retrieve detailed information about the progress of a refund or return request, facilitating efficient communication and processing.

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
| pageSize | 1 | No |  |  |
| pageNo | 1 | No |  |  |
| parentOrderSnList | 8 | No |  |  |
| parentAfterSalesSnList | 8 | No |  |  |
| createAtStart | 1 | No |  |  |
| createAtEnd | 1 | No |  |  |
| updateAtStart | 1 | No |  |  |
| updateAtEnd | 1 | No |  |  |
| afterSalesStatusGroup | 1 | No |  |  |

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

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "createAtEnd" : 1,
  "sign" : "test",
  "parentAfterSalesSnList" : [ "test", "test" ],
  "pageSize" : 1,
  "updateAtStart" : 1,
  "type" : "test",
  "version" : "test",
  "createAtStart" : 1,
  "access_token" : "test",
  "afterSalesStatusGroup" : 1,
  "parentOrderSnList" : [ "test", "test" ],
  "app_key" : "test",
  "updateAtEnd" : 1,
  "pageNo" : 1,
  "data_type" : "test",
  "timestamp" : "test"
}'
```

## Response Example

```json
{
  "result" : {
    "data" : [ {
      "parentAfterSalesSn" : "test",
      "afterSalesStatusGroup" : 1,
      "operateExpireTimeMs" : 1,
      "availableOperateList" : [ 1, 1 ],
      "returnDeliveryType" : 1,
      "parentAfterSalesStatus" : 1,
      "parentOrderSn" : "test",
      "updateAt" : 1,
      "afterSalesType" : 1,
      "createAt" : 1
    } ],
    "total" : 1,
    "pageNumber" : 1
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```