# bg.promotion.activity.goods.operation.query

**querying the operation result of active goods.**

query the result of operation in the local to local activity

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
| draftIdList | 8 | No |  |  |

## Response Parameters

| Parameter | Type | Required | Description | Example |
|---|---|---|---|---|
| result | 8 | No |  |  |
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
  "access_token" : "test",
  "draftIdList" : [ 1, 1 ],
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
  "result" : [ {
    "draftId" : 1,
    "operationStatus" : 1,
    "failReason" : "test",
    "goodsId" : 1
  } ],
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```