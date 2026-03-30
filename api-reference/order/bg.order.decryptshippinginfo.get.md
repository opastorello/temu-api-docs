# bg.order.decryptshippinginfo.get

**Get Order Buyer Sensitive Address Information**

bg.order.decryptshippinginfo.get interface is designed to retrieve sensitive shipping address information for a specific order.

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
| 180020003 | Invalid param |
| 180020004 | Invalid business type |
| 180020008 | Please sign on DPA agreement first |
| 180020030 | Your store has been restricted from confirming shipment by tracking number. Please use the online buy shipping function instead. For more details, please refer to the message in the Seller Center regarding the notice on the restriction of the "confirm shipment by tracking number". |

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "access_token" : "test",
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
    "receiptAdditionalName" : "test",
    "regionName3" : "test",
    "regionName4" : "test",
    "mail" : "test",
    "regionName1" : "test",
    "regionName2" : "test",
    "mobile" : "test",
    "addressExtra" : {
      "additionalLastName" : "test",
      "firstName" : "test",
      "lastName" : "test",
      "contactlessDropPoint" : "test",
      "additionalFirstName" : "test"
    },
    "taxCode" : "test",
    "addressLineAll" : "test",
    "receiptName" : "test",
    "taxCodeType" : 1,
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