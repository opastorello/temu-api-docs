# bg.local.goods.sale.status.set

**Modify The Listing Status Of Products**

Support goods/SKU dimension for listing and delisting operations

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
| goodsId | 2 | No |  |  |
| skuIdList | 8 | No |  |  |
| onsale | 1 | No |  |  |
| operationType | 1 | No |  |  |

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
  "goodsId" : 1,
  "sign" : "test",
  "data_type" : "test",
  "operationType" : 1,
  "onsale" : 1,
  "type" : "test",
  "version" : "test",
  "skuIdList" : [ 1, 1 ],
  "timestamp" : "test"
}'
```

## Response Example

```json
{
  "result" : {
    "success" : true
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```