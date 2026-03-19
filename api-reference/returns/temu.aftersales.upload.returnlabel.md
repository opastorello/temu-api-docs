# temu.aftersales.upload.returnlabel

**Upload return label**

This interface is designed to upload return label.

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
| returnLabelDTOList | 8 | No |  |  |
| pickUpTimeScheduleMode | 1 | No |  |  |
| startTimestamp | 2 | No |  |  |
| endTimestamp | 2 | No |  |  |
| latestTimestamp | 2 | No |  |  |

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
| 130010000 | system error |
| 130010001 | The parameter is illegal. Please check if the input parameter meets the regulations. |
| 130010004 | no afterSales found |
| 130010005 | operate forbid |
| 130010006 | return label invalid |
| 130010007 | tracking number invalid |

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "parentAfterSalesSn" : "test",
  "latestTimestamp" : 1,
  "sign" : "test",
  "type" : "test",
  "version" : "test",
  "access_token" : "test",
  "returnLabelDTOList" : [ {
    "mallWarehouseId" : "test",
    "pickUpCertificateImageUrl" : "test",
    "returnLabelUrl" : "test",
    "carrierId" : 1,
    "trackingNumber" : "test"
  } ],
  "app_key" : "test",
  "parentOrderSn" : "test",
  "pickUpTimeScheduleMode" : 1,
  "data_type" : "test",
  "endTimestamp" : 1,
  "startTimestamp" : 1,
  "timestamp" : "test"
}'
```

## Response Example

```json
{
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```