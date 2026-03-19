# bg.order.combinedshipment.list.get

**Combined Shipment Orders**

The bg.order.combinedshipment.list.get interface is designed for merchants to retrieve combined shipping groups including lists of parent orders that can be combined for shipping.

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
| 140020001 | This interface does not support cross-border sellers. Please check whether the store bound to the token is a SEMI or LOCAL store! |
| 140020005 | Invalid parameter, Please correct and retry. |

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
  "type" : "test",
  "version" : "test",
  "timestamp" : "test"
}'
```

## Response Example

```json
{
  "result" : {
    "combinedShippingGroups" : [ {
      "combinedShippingGroup" : [ {
        "parentOrderStatus" : 1,
        "parentOrderSn" : "test",
        "parentOrderTime" : 1
      } ]
    } ]
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```