# bg.logistics.shipment.document.get

**Print shipping label api**

The bg.logistics.shipment.document.get interface is for sellers to obtain the express delivery waybill which has been fulfilled successfully by Temu-integrated channel so as to facilitate the printing of the express delivery waybill and the package out of the warehouse.

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
| documentType | 4 | No |  |  |
| packageSnList | 8 | No |  |  |

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
| 120018010 | The packages {*} have been canceled. Please fulfill again by Temu non-integrated logistics or Temu integrated logistics. |
| 120011030 | Cooperative warehouse order fulfillment restricted. |
| 120018027 | The packageSn is invalid. Please check the request area or if the packageSn is nonexistent etc. |

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "access_token" : "test",
  "app_key" : "test",
  "documentType" : "test",
  "sign" : "test",
  "data_type" : "test",
  "packageSnList" : [ "test", "test" ],
  "type" : "test",
  "version" : "test",
  "timestamp" : "test"
}'
```

## Response Example

```json
{
  "result" : {
    "shippingLabelUrlList" : [ {
      "packageSn" : "test",
      "documentType" : "test",
      "url" : "test"
    } ],
    "warningMessage" : [ "test", "test" ]
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```