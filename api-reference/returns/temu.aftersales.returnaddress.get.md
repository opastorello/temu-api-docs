# temu.aftersales.returnaddress.get

**Get Return Order Buyer Address Information**

temu.aftersales.returnaddress.get interface is designed to retrieve sensitive shipping address information for a specific return order.

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
| 180020001 | This country has not yet opened address query capabilities |
| 180020008 | Please sign on DPA agreement first |
| 180021001 | full managed, unSupport query address |
| 180021002 | only refund type, unSupport query address |
| 180021003 | uploaded label, unSupport query address |
| 180021004 | no need upload label, unSupport query address |

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "access_token" : "test",
  "parentAfterSalesSn" : "test",
  "app_key" : "test",
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
    "receiptAdditionalName" : "test",
    "regionName3" : "test",
    "regionName4" : "test",
    "mail" : "test",
    "regionName1" : "test",
    "regionName2" : "test",
    "mobile" : "test",
    "addressLineAll" : "test",
    "receiptName" : "test",
    "backupMobile" : "test",
    "addressLine1" : "test",
    "addressLine2" : "test",
    "postCode" : "test",
    "addressLine3" : "test"
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```