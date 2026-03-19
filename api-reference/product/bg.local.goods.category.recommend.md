# bg.local.goods.category.recommend

**Query Recommended Category by Product Name**

query recommended category by product name

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
| description | 4 | No |  |  |
| imageUrl | 4 | No |  |  |
| expandCatType | 1 | No |  |  |
| expandCatName | 4 | No |  |  |

## Response Parameters

| Parameter | Type | Required | Description | Example |
|---|---|---|---|---|
| success | 5 | No |  |  |
| errorCode | 1 | No |  |  |
| errorMsg | 4 | No |  |  |
| result | 6 | No |  |  |

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "access_token" : "test",
  "expandCatName" : "test",
  "app_key" : "test",
  "imageUrl" : "test",
  "sign" : "test",
  "data_type" : "test",
  "description" : "test",
  "type" : "test",
  "version" : "test",
  "goodsName" : "test",
  "expandCatType" : 1,
  "timestamp" : "test"
}'
```

## Response Example

```json
{
  "result" : {
    "catId" : 1,
    "catIdList" : [ 1, 1 ]
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```