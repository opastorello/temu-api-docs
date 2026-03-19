# bg.promotion.activity.candidate.goods.query

**paged query for activity candidate products.**

the local to local activity candidate goods

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
| activityId | 2 | No |  |  |
| pageNumber | 1 | No |  |  |
| pageSize | 1 | No |  |  |

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
| 220010001 | parameter is illegal |
| 220010002 | system error, please try again later |
| 220010003 | The activity has been cancelled, please select another activity to participate |
| 220010004 | The activity has ended, please select another activity to participate |

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "access_token" : "test",
  "activityId" : 1,
  "app_key" : "test",
  "pageNumber" : 1,
  "sign" : "test",
  "data_type" : "test",
  "pageSize" : 1,
  "type" : "test",
  "version" : "test",
  "timestamp" : "test"
}'
```

## Response Example

```json
{
  "result" : {
    "goodsList" : [ {
      "recommendActivityQuantity" : 1,
      "skuList" : [ {
        "recommendActivitySupplierPrice" : 1,
        "skuId" : 1
      } ],
      "isAllowedEnroll" : true,
      "goodsId" : 1
    } ],
    "activityInfo" : {
      "activityId" : 1,
      "activityEndTime" : 1,
      "activityName" : "test",
      "activityStatus" : 1,
      "activityStartTime" : 1,
      "activityType" : 1,
      "isJoinedActivity" : true
    },
    "total" : 1
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```