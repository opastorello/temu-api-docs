# temu.searchrec.ad.reports.goods.query

**Advertisement goods data report (goods dimension) interface**

Advertisement goods data report (goods dimension)

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
| startTs | 2 | No |  |  |
| endTs | 2 | No |  |  |
| goodsId | 2 | No |  |  |

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
| 230012000 | bad query params |
| 230012003 | unmatch mall and goods |
| 230013000 | business exception |
| 230014000 | system exception |
| 230016701 | has no permission |
| 230016103 | not signed because of not main account |

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
  "endTs" : 1,
  "startTs" : 1,
  "type" : "test",
  "version" : "test",
  "timestamp" : "test"
}'
```

## Response Example

```json
{
  "result" : {
    "goodsInfo" : {
      "goodsId" : 1
    },
    "reportInfo" : {
      "reportsItemList" : [ {
        "ctr" : {
          "val" : 1
        },
        "cartCnt" : {
          "val" : 1
        },
        "clkCnt" : {
          "val" : 1
        },
        "orderPayAmt" : {
          "val" : 1
        },
        "goodsId" : 1,
        "orderPayCnt" : {
          "val" : 1
        },
        "roas" : {
          "val" : 1
        },
        "acos" : {
          "val" : 1
        },
        "adSpend" : {
          "val" : 1
        },
        "imprCnt" : {
          "val" : 1
        },
        "ts" : 1
      } ],
      "reportsSummary" : {
        "clkCntAll" : {
          "val" : 1
        },
        "orderPayCntAll" : {
          "val" : 1
        },
        "adSpendAll" : {
          "val" : 1
        },
        "acosAll" : {
          "val" : 1
        },
        "ctrAll" : {
          "val" : 1
        },
        "imprCntAll" : {
          "val" : 1
        },
        "orderPayAmtAll" : {
          "val" : 1
        },
        "cartCntAll" : {
          "val" : 1
        },
        "roasAll" : {
          "val" : 1
        }
      }
    }
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```