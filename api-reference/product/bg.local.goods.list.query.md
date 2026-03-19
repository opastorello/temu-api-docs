# bg.local.goods.list.query

**Get product list**

Get product list

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
| pageNo | 1 | No |  |  |
| pageSize | 1 | No |  |  |
| orderField | 4 | No |  |  |
| orderType | 1 | No |  |  |
| goodsSearchType | 1 | No |  |  |
| searchText | 4 | No |  |  |
| statusFilterType | 1 | No |  |  |
| crtFrom | 2 | No |  |  |
| crtTo | 2 | No |  |  |
| goodsIdList | 8 | No |  |  |
| catIdList | 8 | No |  |  |
| goodsStatusFilterType | 1 | No |  |  |
| goodsSubStatusFilterType | 1 | No |  |  |
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
| 150010003 | Invalid Request Parameters |
| 150010005 | Try again later |

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "goodsSubStatusFilterType" : 1,
  "orderType" : 1,
  "goodsSearchType" : 1,
  "sign" : "test",
  "crtTo" : 1,
  "pageSize" : 1,
  "type" : "test",
  "statusFilterType" : 1,
  "goodsSearchTags" : [ 1, 1 ],
  "version" : "test",
  "goodsIdList" : [ 1, 1 ],
  "goodsStatusChangeTimeFrom" : 1,
  "access_token" : "test",
  "searchText" : "test",
  "app_key" : "test",
  "goodsStatusFilterType" : 1,
  "pageNo" : 1,
  "goodsStatusChangeTimeTo" : 1,
  "data_type" : "test",
  "crtFrom" : 1,
  "orderField" : "test",
  "catIdList" : [ 1, 1 ],
  "timestamp" : "test"
}'
```

## Response Example

```json
{
  "result" : {
    "goodsList" : [ {
      "marketPrice" : 1,
      "goodsId" : 1,
      "outSkuSnList" : [ "test", "test" ],
      "goodsStatusChangeTime" : "test",
      "crtTime" : 1,
      "skuInfoList" : [ {
        "specList" : [ {
          "specId" : 1,
          "parentSpecId" : 1
        } ],
        "skuId" : 1,
        "skuSn" : "test"
      } ],
      "goodsShowSubStatus" : 1,
      "lowTrafficTag" : 1,
      "outGoodsSn" : "test",
      "price" : "test",
      "currency" : "test",
      "thumbUrl" : "test",
      "goodsName" : "test",
      "skuIdList" : [ 1, 1 ],
      "status4VO" : 1,
      "quantity" : 1,
      "subStatus4VO" : 1,
      "restrictedTrafficTag" : 1,
      "costTemplateId" : "test",
      "shipmentLimitSecond" : 1,
      "catId" : 1,
      "specName" : "test",
      "trademarkId" : 1,
      "brandId" : 1,
      "retailPrice" : {
        "amount" : "test",
        "currency" : "test"
      },
      "listPrice" : {
        "amount" : "test",
        "currency" : "test"
      }
    } ],
    "pageNo" : 1,
    "total" : 1
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```