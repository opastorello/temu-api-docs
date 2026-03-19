# bg.local.goods.priceorder.query

**Query price offer Info**

Support merchants within the white list to query the price offer list.

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
| page | 1 | No |  |  |
| size | 1 | No |  |  |
| priceOrderType | 1 | No |  |  |
| priceOrderSubType | 1 | No |  |  |
| goodsName | 4 | No |  |  |
| goodsId | 4 | No |  |  |
| priceOrderSnList | 8 | No |  |  |
| orderBy | 4 | No |  |  |
| orderByType | 1 | No |  |  |
| goodsCreateTimeFrom | 2 | No |  |  |
| goodsCreateTimeTo | 2 | No |  |  |
| priceOrderCreateTimeFrom | 2 | No |  |  |
| priceOrderCreateTimeTo | 2 | No |  |  |
| goodsIdList | 8 | No |  |  |
| status | 1 | No |  |  |

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
| 150010105 | Mall information not found |

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "goodsCreateTimeFrom" : 1,
  "priceOrderSubType" : 1,
  "goodsId" : "test",
  "priceOrderCreateTimeTo" : 1,
  "sign" : "test",
  "orderBy" : "test",
  "priceOrderSnList" : [ "test", "test" ],
  "priceOrderCreateTimeFrom" : 1,
  "type" : "test",
  "version" : "test",
  "goodsIdList" : [ "test", "test" ],
  "access_token" : "test",
  "app_key" : "test",
  "size" : 1,
  "data_type" : "test",
  "orderByType" : 1,
  "page" : 1,
  "priceOrderType" : 1,
  "goodsCreateTimeTo" : 1,
  "goodsName" : "test",
  "timestamp" : "test",
  "status" : 1
}'
```

## Response Example

```json
{
  "result" : {
    "pageNum" : 1,
    "priceAuditList" : [ {
      "rejectTypeDesc" : "test",
      "reason" : "test",
      "priceOrderId" : 1,
      "goodsId" : 1,
      "supplierPrice" : {
        "amount" : "test",
        "currency" : "test"
      },
      "priceCommitId" : 1,
      "sourceSupplierPrice" : {
        "amount" : "test",
        "currency" : "test"
      },
      "suggestSupplierPrice" : {
        "amount" : "test",
        "currency" : "test"
      },
      "specName" : [ "test", "test" ],
      "targetSupplierPrice" : {
        "amount" : "test",
        "currency" : "test"
      },
      "priceCommitVersion" : 1,
      "skuIdList" : [ 1, 1 ],
      "pricingType" : 1,
      "status" : 1
    } ],
    "total" : 1
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```