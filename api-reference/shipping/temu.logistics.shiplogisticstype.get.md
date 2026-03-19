# temu.logistics.shiplogisticstype.get

**Get all online ship logistics type**

You can get all online ship logistics type information from this api. After that, they can call "bg.logistics.shipment.create" to buy-shipping on Temu. Once you choose to buy-shipping with ship logistics type, Temu will automatically chose the most recommended channel id and buy-shipping for you.

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
| regionId | 2 | No |  |  |

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
| 120011001 | System abnormality, please check the data and try again |
| 120011002 | Invalid request parameters. |
| 120011072 | The request area is incorrect. Please check the request area and replace it with the correct request area. The request area for the United States is US, and the request area for other non-European countries is global. |

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "access_token" : "test",
  "app_key" : "test",
  "regionId" : 1,
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
    "shipLogisticsTypeInfoDTOList" : [ {
      "logisticsProviderLabelList" : [ "test", "test" ],
      "shipLogisticsType" : "test",
      "shippingCompanyName" : "test",
      "shipCompanyId" : 1
    } ],
    "regionId" : 1
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```