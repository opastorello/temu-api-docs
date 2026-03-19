# temu.local.order.verification.upload

**Merchants upload verification information before shipping.**

The interface supports uploading serial numbers (SN) / International Mobile Equipment Identity (IMEI) of high-value goods, or authentication information for second-hand goods.

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
| orderList | 8 | No |  |  |

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
| 140040001 | request param error |
| 140040003 | please try again later |
| 140040005 | This order is not in the "wait-shipping" status. |
| 140040006 | This order is not a designated order and does not require verification (high-value order, pre-owned luxury goods order, pre-owned collectibles order). |
| 140040007 | The parameters uploaded for this order are incorrect. |
| 140040008 | Only the serial number (SN) can be transmitted; transmitting the IMEI results in an error. |
| 140040009 | Only IMEI can be transmitted; transmitting SN results in an error. |
| 140040010 | The number of items uploaded for this order does not match the number of SKU. |

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "access_token" : "test",
  "app_key" : "test",
  "sign" : "test",
  "data_type" : "test",
  "orderList" : [ {
    "secondHandVerificationInfo" : [ {
      "secondHandProofCertificateCode" : "test"
    } ],
    "orderSn" : "test",
    "verificationInfo" : [ {
      "imeiNumberList" : [ "test", "test" ],
      "serialNumber" : "test"
    } ]
  } ],
  "type" : "test",
  "version" : "test",
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