# temu.local.goods.v3.add

**Add New Items On Temu**

Post products to temu and automatically populate the database based on the original product data provided.

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
| goodsBasic | 6 | No |  |  |
| attributes | 8 | No |  |  |
| skuList | 8 | No |  |  |

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
| 150010260 | No results for category recommendations, please complete the product information and try again. |
| 150011018 | Price currency {*} can have at most {*} decimal points. |
| 150011019 | The input {*}:{*} is incorrect, please modify it. |
| 150011020 | There is an abnormal number of product operations. Related actions have been temporarily restricted for today. If you have any questions, please contact your sales representative for help. |
| 150011041 | Exceeded the maximum number of {*} allowed. |
| 150011038 | Duplicate attribute values were entered for a single SKU. |
| 150011022 | Specification information repeated: {*}. |
| 150010254 | Second-hand stores do not support publishing products in this category. |
| 150010253 | The selected businessScope is not applicable to the current product. |
| 150011100 | The number of products that can be listed each day is limited to {*}. Reason: {*} |
| 150011101 | The price change in this request exceeds the allowed range. Please check the request parameters. If the change is confirmed, please retry within {*} minutes. |
| 150011028 | Specification information repeated: [{*}]. |
| 150010216 | The property value repeated. |
| 150010215 | The number of property value over size. |
| 150010090 | SKU duplicated |
| 150010003 | Invalid Request Parameters |
| 150010030 | Price input error |
| 150010163 | Please enter list price |
| 150010002 | System error, please try again later |
| 150013001 | Duplicate SKUs detected. Please remove them and try again |
| 150011055 | {*} is required fields. |
| 150011003 | Invalid Request Parameters [{*}] |
| 150010084 | Invalid currency |
| 150011034 | The value of {*} is empty. Please check and enter correctly. |

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "access_token" : "test",
  "app_key" : "test",
  "skuList" : [ {
    "images" : [ "test", "test" ],
    "quantity" : 1,
    "references" : {
      "note" : [ "test", "test" ],
      "code" : {
        "name" : "test",
        "id" : "test"
      }
    },
    "externalSkuId" : "test",
    "price" : {
      "listPrice" : {
        "amount" : "test",
        "currency" : "test"
      },
      "basePrice" : {
        "amount" : "test",
        "currency" : "test"
      }
    },
    "variations" : [ {
      "name" : "test",
      "value" : "test"
    } ],
    "packageInfo" : {
      "length" : "test",
      "width" : "test",
      "weight" : "test",
      "height" : "test"
    },
    "barCode" : {
      "barCodeId" : [ "test", "test" ],
      "barCodeType" : "test"
    }
  } ],
  "sign" : "test",
  "data_type" : "test",
  "language" : "test",
  "attributes" : [ {
    "name" : "test",
    "value" : [ "test", "test" ]
  } ],
  "type" : "test",
  "version" : "test",
  "timestamp" : "test",
  "goodsBasic" : {
    "shipmentLimitDay" : 1,
    "extCatName" : "test",
    "externalGoodsId" : "test",
    "goodsCarouselImage" : [ "test", "test" ],
    "goodsName" : "test",
    "productType" : 1,
    "goodsDesc" : "test",
    "detailImage" : [ "test", "test" ]
  }
}'
```

## Response Example

```json
{
  "result" : {
    "externalGoodsId" : "test",
    "goodsId" : 1
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```