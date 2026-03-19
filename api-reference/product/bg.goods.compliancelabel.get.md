# bg.goods.compliancelabel.get

**bg.goods.compliancelabel.get**

page query goods compliance labels

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
| productIds | 8 | No |  |  |
| pageSize | 1 | No |  |  |
| page | 1 | No |  |  |

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
  "app_key" : "test",
  "productIds" : [ 1, 1 ],
  "sign" : "test",
  "data_type" : "test",
  "pageSize" : 1,
  "page" : 1,
  "type" : "test",
  "version" : "test",
  "timestamp" : "test"
}'
```

## Response Example

```json
{
  "result" : {
    "pageResult" : {
      "data" : [ {
        "productId" : 1,
        "skuComplianceLabels" : [ {
          "complianceLabelPics" : [ "test", "test" ],
          "complianceLabelStatus" : 1,
          "productSkuId" : 1
        } ]
      } ],
      "totalCount" : 1
    }
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```