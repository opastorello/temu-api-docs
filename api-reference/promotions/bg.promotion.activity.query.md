# bg.promotion.activity.query

**paging query activity information**

query the local to local activity

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
| pageNumber | 1 | No |  |  |
| activityEndTime | 2 | No |  |  |
| activityIdList | 8 | No |  |  |
| activityStatus | 1 | No |  |  |
| pageSize | 1 | No |  |  |
| activityStartTime | 2 | No |  |  |
| activityType | 1 | No |  |  |
| onlyQueryJoinedActivity | 5 | No |  |  |

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

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "pageNumber" : 1,
  "sign" : "test",
  "pageSize" : 1,
  "activityStartTime" : 1,
  "type" : "test",
  "version" : "test",
  "access_token" : "test",
  "app_key" : "test",
  "activityEndTime" : 1,
  "activityIdList" : [ 1, 1 ],
  "data_type" : "test",
  "activityStatus" : 1,
  "activityType" : 1,
  "onlyQueryJoinedActivity" : true,
  "timestamp" : "test"
}'
```

## Response Example

```json
{
  "result" : {
    "activityList" : [ {
      "activityId" : 1,
      "activityEndTime" : 1,
      "activityName" : "test",
      "activityStatus" : 1,
      "activityStartTime" : 1,
      "activityType" : 1,
      "isJoinedActivity" : true
    } ],
    "total" : 1
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```