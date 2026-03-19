# bg.local.goods.sku.list.query

**Get sku list**

Get sku list, as well as get  Variants

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
| skuSearchType | 1 | No |  |  |
| searchText | 4 | No |  |  |
| statusFilterType | 1 | No |  |  |
| crtFrom | 2 | No |  |  |
| crtTo | 2 | No |  |  |
| skuIdList | 8 | No |  |  |
| catIdList | 8 | No |  |  |
| skuStatusFilterType | 1 | No |  |  |
| skuSubStatusFilterType | 1 | No |  |  |
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

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "orderType" : 1,
  "skuSearchType" : 1,
  "sign" : "test",
  "crtTo" : 1,
  "pageSize" : 1,
  "type" : "test",
  "statusFilterType" : 1,
  "skuStatusChangeTimeTo" : 1,
  "goodsSearchTags" : [ 1, 1 ],
  "version" : "test",
  "access_token" : "test",
  "searchText" : "test",
  "skuSubStatusFilterType" : 1,
  "app_key" : "test",
  "skuStatusFilterType" : 1,
  "skuStatusChangeTimeFrom" : 1,
  "pageNo" : 1,
  "data_type" : "test",
  "crtFrom" : 1,
  "orderField" : "test",
  "skuIdList" : [ 1, 1 ],
  "catIdList" : [ 1, 1 ],
  "timestamp" : "test"
}'
```

## Response Example

```json
{
  "result" : {
    "pageNo" : 1,
    "total" : 1,
    "skuList" : [ {
      "status4VO" : 1,
      "goodsId" : 1,
      "subStatus4VO" : 1,
      "specList" : [ {
        "specId" : 1,
        "parentSpecId" : 1
      } ],
      "crtTime" : 1,
      "restrictedTrafficTag" : 1,
      "lowTrafficTag" : 1,
      "specName" : "test",
      "price" : "test",
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
      "goodsIsOnSale" : 1,
      "currency" : "test",
      "skuShowSubStatus4VO" : 1,
      "thumbUrl" : "test",
      "stock" : 1,
      "goodsName" : "test",
      "retailPrice" : {
        "amount" : "test",
        "currency" : "test"
      },
      "skuStatusChangeTime" : "test",
      "skuId" : 1,
      "skuSn" : "test"
    } ]
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```