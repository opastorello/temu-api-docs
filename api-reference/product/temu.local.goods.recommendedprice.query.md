# temu.local.goods.recommendedprice.query

**Batch query recommended price**

Support merchants in querying the recommended supply prices.

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
| language | 4 | No |  |  |
| recommendedPriceType | 1 | No |  |  |
| goodsIdList | 8 | No |  |  |

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

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "access_token" : "test",
  "app_key" : "test",
  "recommendedPriceType" : 1,
  "sign" : "test",
  "data_type" : "test",
  "language" : "test",
  "type" : "test",
  "version" : "test",
  "goodsIdList" : [ 1, 1 ],
  "timestamp" : "test"
}'
```

## Response Example

```json
{
  "result" : {
    "goodsList" : [ {
      "goodsId" : 1,
      "skuList" : [ {
        "skuId" : 1,
        "recommendedSupplyPrice" : {
          "amount" : "test",
          "currency" : "test"
        }
      } ]
    } ]
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```