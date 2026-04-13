# bg.local.goods.detail.query

**Query local goods detail**

Query local goods detail

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
| goodsId | 2 | No |  |  |
| versionQueryType | 1 | No |  |  |

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
| 150010188 | The mall and goods not match. |

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
  "language" : "test",
  "versionQueryType" : 1,
  "type" : "test",
  "version" : "test",
  "timestamp" : "test"
}'
```

## Response Example

```json
{
  "result" : {
    "customized" : true,
    "skuList" : [ {
      "specIdList" : [ 1, 1 ],
      "images" : [ "test", "test" ],
      "externalProductType" : 1,
      "multiplePackage" : {
        "originNetContentNumber" : "test",
        "numberOfPieces" : 1,
        "individuallyPacked" : true,
        "netContentUnitCode" : 1,
        "skuClassification" : 1,
        "mixedSetType" : 1,
        "pieceUnitCode" : 1,
        "originTotalNetContentNumber" : "test"
      },
      "productExpressInfo" : {
        "weightInfo" : {
          "weight" : "test",
          "unit" : "test"
        },
        "volumeInfo" : {
          "length" : "test",
          "width" : "test",
          "unit" : "test",
          "height" : "test"
        }
      },
      "outSkuSn" : "test",
      "externalProductId" : "test",
      "retailPrice" : {
        "amount" : "test",
        "currency" : "test"
      },
      "referenceLink" : "test",
      "skuId" : 1,
      "listPrice" : {
        "amount" : "test",
        "currency" : "test"
      }
    } ],
    "sourceSiteInfo" : {
      "siteId" : 1,
      "goodsId" : 1
    },
    "goodsServicePromise" : {
      "costTemplateId" : "test",
      "fulfillmentType" : 1,
      "shipmentLimitDay" : 1
    },
    "itemTaxCode" : "test",
    "goodsId" : 1,
    "goodsSizeChartList" : {
      "goodsSizeChartList" : [ {
        "sizeSpecInfo" : {
          "classId" : 1,
          "records" : [ {
            "values" : [ {
              "name" : "test",
              "id" : 1
            } ]
          } ],
          "bodyRecords" : [ {
            "values" : [ {
              "name" : "test",
              "id" : 1
            } ]
          } ],
          "meta" : {
            "groups" : [ {
              "name" : "test",
              "id" : 1
            } ],
            "elements" : [ {
              "name" : "test",
              "id" : 1
            } ]
          },
          "bodyMeta" : {
            "groups" : [ {
              "name" : "test",
              "id" : 1
            } ],
            "elements" : [ {
              "name" : "test",
              "id" : 1
            } ]
          }
        }
      } ]
    },
    "goodsProperties" : [ {
      "templateModuleId" : 1,
      "specId" : 1,
      "note" : "test",
      "parentSpecId" : 1,
      "groupId" : 1,
      "valueUnit" : "test",
      "pid" : 1,
      "templatePid" : 1,
      "vid" : 1,
      "imgUrl" : "test",
      "parentSpecName" : "test",
      "valueUnitId" : 1,
      "subGroupId" : 1,
      "numberInputValue" : "test",
      "multiLineInputValue" : [ "test", "test" ],
      "value" : "test",
      "refPid" : 1
    } ],
    "goodsOriginInfo" : {
      "originRegionName1" : "test",
      "originRegionName2" : "test"
    },
    "importDesignation" : "test",
    "subStatus" : 1,
    "catId" : 1,
    "targetSiteInfo" : [ {
      "siteId" : 1,
      "goodsId" : 1
    } ],
    "outGoodsSn" : "test",
    "saveModeStatus" : 1,
    "bulletPoints" : [ "test", "test" ],
    "goodsName" : "test",
    "secondHand" : {
      "businessScope" : 1,
      "secondHandGoods" : true,
      "level" : 1,
      "insName" : "test",
      "grade" : "test"
    },
    "productType" : 1,
    "goodsGallery" : {
      "detailVideo" : [ {
        "vid" : "test",
        "url" : "test"
      } ],
      "goodsCarouselImage" : [ "test", "test" ],
      "carouselVideo" : [ {
        "vid" : "test",
        "url" : "test"
      } ],
      "detailImage" : [ "test", "test" ]
    },
    "goodsDesc" : "test",
    "goodsTrademark" : {
      "trademarkBizId" : 1,
      "trademarkId" : 1,
      "brandId" : 1
    },
    "goodsSizeImage" : [ "test", "test" ]
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```