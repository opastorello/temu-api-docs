# temu.track.trackinginfo.get

**temu.track.trackinginfo.get**

Logistics trajectory detail query interface

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
| packageSn | 4 | No |  |  |
| language | 4 | No |  |  |

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
| 170070012 | Unsupported languages, {*} |
| 170070011 | Tracking Number Not Found |
| 170070010 | Invalid Parameters: {*} |

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
  "packageSn" : "test",
  "language" : "test",
  "type" : "test",
  "version" : "test",
  "timestamp" : "test"
}'
```

## Response Example

```json
{
  "result" : {
    "packageSn" : "test",
    "trackingInfo" : [ {
      "logisticsStatus" : "test",
      "logisticsUpdatedAt" : "test",
      "statusText" : "test"
    } ],
    "trackingNum" : "test"
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```