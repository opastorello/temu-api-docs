# temu.local.goods.list.retrieve

**Product list Retrieve**

local goods list search

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
| goodsSearchType | 4 | No |  |  |
| goodsIdList | 8 | No |  |  |
| outGoodsSnList | 8 | No |  |  |
| skuIdList | 8 | No |  |  |
| outSkuSnList | 8 | No |  |  |
| catIdList | 8 | No |  |  |
| goodsName | 4 | No |  |  |
| goodsCreateTimeFrom | 2 | No |  |  |
| goodsCreateTimeTo | 2 | No |  |  |
| goodsStatusChangeTimeFrom | 2 | No |  |  |
| goodsStatusChangeTimeTo | 2 | No |  |  |
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
| 150010002 | System error, please try again later |
| 150010003 | Invalid Request Parameters |

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "orderType" : 1,
  "goodsSearchType" : "test",
  "goodsCreateTimeFrom" : 1,
  "outSkuSnList" : [ "test", "test" ],
  "sign" : "test",
  "pageSize" : 1,
  "type" : "test",
  "goodsSearchTags" : [ 1, 1 ],
  "version" : "test",
  "goodsIdList" : [ "test", "test" ],
  "goodsStatusChangeTimeFrom" : 1,
  "access_token" : "test",
  "outGoodsSnList" : [ "test", "test" ],
  "app_key" : "test",
  "goodsStatusChangeTimeTo" : 1,
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
    "goodsList" : [ {
      "goodsId" : "test",
      "goodsStatusChangeTime" : 1,
      "catType" : 1,
      "restrictedTrafficTag" : 1,
      "costTemplateId" : "test",
      "shipmentLimitSecond" : 1,
      "goodsCreateTime" : 1,
      "skuInfoList" : [ {
        "specList" : [ {
          "specId" : 1,
          "parentSpecId" : 1
        } ],
        "skuId" : 1,
        "skuSn" : "test"
      } ],
      "catId" : "test",
      "lowTrafficTag" : 1,
      "goodsStatus" : "test",
      "outGoodsSn" : "test",
      "trademarkId" : "test",
      "brandId" : "test",
      "variationsCount" : 1,
      "thumbUrl" : "test",
      "goodsName" : "test"
    } ],
    "total" : 1,
    "pagination" : {
      "nextToken" : "test",
      "previousToken" : "test"
    }
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```