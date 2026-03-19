# temu.local.sku.list.retrieve

**Get SKU list**

local sku list search

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
| pageSize | 1 | No |  |  |
| pageToken | 4 | No |  |  |
| orderField | 4 | No |  |  |
| orderType | 1 | No |  |  |
| skuSearchType | 4 | No |  |  |
| goodsIdList | 8 | No |  |  |
| outGoodsSnList | 8 | No |  |  |
| skuIdList | 8 | No |  |  |
| outSkuSnList | 8 | No |  |  |
| catIdList | 8 | No |  |  |
| goodsName | 4 | No |  |  |
| goodsCreateTimeFrom | 2 | No |  |  |
| goodsCreateTimeTo | 2 | No |  |  |
| skuStatusChangeTimeFrom | 2 | No |  |  |
| skuStatusChangeTimeTo | 2 | No |  |  |
| goodsSearchTags | 8 | No |  |  |

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
| 150010001 | Invalid Request Parameters |
| 150010002 | System error, please try again later |
| 150010003 | Invalid Request Parameters |
| 150010005 | Try again later |

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "orderType" : 1,
  "skuSearchType" : "test",
  "goodsCreateTimeFrom" : 1,
  "outSkuSnList" : [ "test", "test" ],
  "sign" : "test",
  "pageSize" : 1,
  "type" : "test",
  "skuStatusChangeTimeTo" : 1,
  "goodsSearchTags" : [ 1, 1 ],
  "version" : "test",
  "goodsIdList" : [ "test", "test" ],
  "access_token" : "test",
  "outGoodsSnList" : [ "test", "test" ],
  "app_key" : "test",
  "skuStatusChangeTimeFrom" : 1,
  "data_type" : "test",
  "pageToken" : "test",
  "orderField" : "test",
  "goodsCreateTimeTo" : 1,
  "skuIdList" : [ "test", "test" ],
  "catIdList" : [ "test", "test" ],
  "goodsName" : "test",
  "timestamp" : "test"
}'
```

## Response Example

```json
{
  "result" : {
    "total" : 1,
    "pagination" : {
      "nextToken" : "test",
      "previousToken" : "test"
    },
    "skuList" : [ {
      "goodsId" : "test",
      "skuStatus" : "test",
      "specList" : [ {
        "specId" : 1,
        "parentSpecId" : 1
      } ],
      "catType" : 1,
      "restrictedTrafficTag" : 1,
      "goodsCreateTime" : 1,
      "catId" : "test",
      "lowTrafficTag" : 1,
      "specName" : "test",
      "outGoodsSn" : "test",
      "skuSubStatus" : "test",
      "volumeInfo" : {
        "length" : "test",
        "width" : "test",
        "unit" : "test",
        "height" : "test"
      },
      "weightInfo" : {
        "weight" : "test",
        "unit" : "test"
      },
      "outSkuSn" : "test",
      "thumbUrl" : "test",
      "goodsName" : "test",
      "skuStatusChangeTime" : 1,
      "skuId" : "test"
    } ]
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```