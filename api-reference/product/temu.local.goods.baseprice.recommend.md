# temu.local.goods.baseprice.recommend

**recommend base price**

recommend baseprice

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
| supplierPriceEstimateQry | 6 | No |  |  |

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
| 150012003 | List price for the same color must match. |
| 150012002 | The site size/currency information needs to be consistent with the site's product support information. |
| 150012001 | The "Product Dimensions" information is a mandatory field for the Brazilian site. |
| 150010124 | The catId not a leaf category |
| 150010003 | Invalid Request Parameters |
| 150010002 | System error, please try again later |

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "access_token" : "test",
  "app_key" : "test",
  "sign" : "test",
  "data_type" : "test",
  "language" : "test",
  "supplierPriceEstimateQry" : {
    "trademarkInfo" : {
      "trademarkId" : 1,
      "brandId" : 1
    },
    "goodsBasicInfo" : {
      "taxCode" : "test",
      "costTemplateId" : "test",
      "catId" : 1
    },
    "supplierPriceEstimateSkuQryList" : [ {
      "productDimensionsInfo" : {
        "length" : "test",
        "width" : "test",
        "dimensionUnit" : "test",
        "weight" : "test",
        "weightUnit" : "test",
        "height" : "test"
      },
      "specIdList" : [ 1, 1 ],
      "externPlatformPriceInfo" : {
        "amount" : "test",
        "currency" : "test"
      }
    } ]
  },
  "type" : "test",
  "version" : "test",
  "timestamp" : "test"
}'
```

## Response Example

```json
{
  "result" : {
    "supplierPriceEstimateInfo" : {
      "skuEstimateInfoList" : [ {
        "recommendBasePriceInfo" : {
          "amount" : "test",
          "currency" : "test"
        },
        "specIdList" : [ 1, 1 ],
        "externPlatformPriceInfo" : {
          "amount" : "test",
          "currency" : "test"
        }
      } ]
    }
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```