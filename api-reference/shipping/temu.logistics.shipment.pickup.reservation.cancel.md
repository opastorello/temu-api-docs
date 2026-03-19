# temu.logistics.shipment.pickup.reservation.cancel

**Cancel reservationSn  api**

The temu.logistics.shipment.pickup.reservation.cancel API enables sellers to cancel reservationSn.

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
| reservationSn | 4 | No |  |  |

## Response Parameters

| Parameter | Type | Required | Description | Example |
|---|---|---|---|---|
| success | 5 | No |  |  |
| errorCode | 1 | No |  |  |
| errorMsg | 4 | No |  |  |

## Error Codes

| Error Code | Message |
|---|---|
| 120011002 | Invalid request parameters. |
| 120019007 | The reservationSn is invalid. |
| 120019010 | The channel don't allow seller cancel the pickup reservation. |
| 120019022 | Current reservation status don't allow you to cancel the reservation, only successful reservation can be cancelled. |

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "access_token" : "test",
  "app_key" : "test",
  "reservationSn" : "test",
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
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```