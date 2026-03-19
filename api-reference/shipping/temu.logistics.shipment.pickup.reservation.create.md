# temu.logistics.shipment.pickup.reservation.create

**Create package reservation api**

The temu.logistics.shipment.pickup.reservation.create API enables sellers to schedule package pickups. When multiple packages meet the criteria for consolidated pickup appointments, they will be merged into a single reservation (reservationSn). Note: Reservation results must be retrieved via temu.logistics.shipment.pickup.reservation.result.get.

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
| pickupStartTime | 2 | No |  |  |
| pickupEndTime | 2 | No |  |  |
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
| 120019030 | The number of packages must be less than {*} |
| 120019009 | Invalid pickup reservation time. See pickupRules for valid options. |
| 120011002 | Invalid request parameters. |
| 120019001 | We haven't support the pickup reservation of this channel through open api yet. |
| 120019002 | The PackageSn in one api call doesn't match, please make sure they come from the same channel and same warehouse. |
| 120019005 | PackageSn in "packageSnList" is invalid,please have a check. |
| 120019006 | The pickup reservation of this pacakge is under going, you can't make the pickup reservation again. |
| 120019025 | The pickupStartTime or pickupEndTime is invalid, please get the valid time slot from "bg.logistics.shippingservices.get". |
| 120019023 | There are duplicated packageSn in one api call, please delete one. |

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "access_token" : "test",
  "app_key" : "test",
  "pickupStartTime" : 1,
  "pickupEndTime" : 1,
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
    "pickupReservationList" : [ {
      "pickupWarehouseId" : "test",
      "packageSnList" : [ "test", "test" ],
      "pickupStartTime" : 1,
      "pickupEndTime" : 1
    } ]
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```