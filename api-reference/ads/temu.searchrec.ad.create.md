# temu.searchrec.ad.create

**Advertisement creation interface**

Advertisement creation

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
| createAdReqs | 8 | No |  |  |

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
| 230012000 | bad query params |
| 230012003 | unmatch mall and goods |
| 230013000 | business exception |
| 230014000 | system exception |
| 230016701 | has no permission |
| 230016103 | not signed because of not main account |

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "access_token" : "test",
  "app_key" : "test",
  "createAdReqs" : [ {
    "roas" : 1,
    "roasType" : 1,
    "goodsId" : 1,
    "budget" : 1
  } ],
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
    "alreadyCreatedGoodsNum" : 1,
    "createGoodsFailMap" : {
      "$key" : "test",
      "$value" : "test"
    },
    "successGoodsIdLists" : [ 1, 1 ],
    "successCreateProductNum" : 1,
    "createGoodsFailObjList" : [ {
      "reason" : "test",
      "goodsId" : 1,
      "success" : true
    } ]
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```