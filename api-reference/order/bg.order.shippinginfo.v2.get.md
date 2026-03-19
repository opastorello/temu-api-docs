# bg.order.shippinginfo.v2.get

**Get Order Buyer Address Information v2**

The bg.order.shippinginfo.get.V2 interface is designed to retrieve shipping address information for a specific order. This functionality is crucial for merchants and logistics providers to ensure that orders are shipped to the correct location.

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
      "additionalFirstName" : "test"
    },
    "taxCode" : "test",
    "addressLineAll" : "test",
    "receiptName" : "test",
    "taxCodeType" : 1,
    "backupMobile" : "test",
    "addressLine1" : "test",
    "warning" : {
      "reason" : 1,
      "isRestriction" : true
    },
    "addressLine2" : "test",
    "postCode" : "test",
    "addressLine3" : "test"
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```