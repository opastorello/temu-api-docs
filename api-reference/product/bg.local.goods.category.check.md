# bg.local.goods.category.check

**goods category precheck**

precheck category misplacement

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
| catId | 2 | No |  |  |
| hdThumbUrl | 4 | No |  |  |
| carouselImageList | 8 | No |  |  |
| language | 4 | No |  |  |
| goodsName | 4 | No |  |  |

## Response Parameters

| Parameter | Type | Required | Description | Example |
|---|---|---|---|---|
| result | 6 | No |  |  |
| success | 5 | No |  |  |
| errorCode | 1 | No |  |  |
| errorMsg | 4 | No |  |  |

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "access_token" : "test",
  "catId" : 1,
  "app_key" : "test",
  "hdThumbUrl" : "test",
  "sign" : "test",
  "data_type" : "test",
  "carouselImageList" : [ "test", "test" ],
  "language" : "test",
  "type" : "test",
  "version" : "test",
  "goodsName" : "test",
  "timestamp" : "test"
}'
```

## Response Example

```json
{
  "result" : {
    "checkResult" : true,
    "recommendedCatIds" : [ 1, 1 ]
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```