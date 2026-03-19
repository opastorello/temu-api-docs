# temu.local.goods.illegal.vocabulary.check

**check illeagl vocabulary**

check illegal vocabulary

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
| goodsName | 4 | No |  |  |
| goodsDesc | 4 | No |  |  |
| bulletPoints | 8 | No |  |  |

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
| 150010002 | System error, please try again later |
| 150010003 | Invalid Request Parameters |
| 150010005 | Try again later |

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
  "bulletPoints" : [ "test", "test" ],
  "type" : "test",
  "version" : "test",
  "goodsName" : "test",
  "timestamp" : "test",
  "goodsDesc" : "test"
}'
```

## Response Example

```json
{
  "result" : {
    "failReasonList" : [ {
      "violationWarningContentList" : [ {
        "violationType" : "test",
        "warning" : "test"
      } ],
      "violationItem" : "test"
    } ],
    "checkResult" : "test"
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```