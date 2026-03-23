# temu.searchrec.ad.reports.mall.query

**Advertisement overall data report (mall dimension) interface**

Advertisement overall data report (mall dimension)

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
    "summary" : {
      "ctr" : {
        "total" : {
          "val" : 1
        },
        "ad" : {
          "val" : 1
        },
        "netTotal" : {
          "val" : 1
        },
        "netAd" : {
          "val" : 1
        }
      },
      "cartCnt" : {
        "total" : {
          "val" : 1
        },
        "ad" : {
          "val" : 1
        },
        "netTotal" : {
          "val" : 1
        },
        "netAd" : {
          "val" : 1
        }
      },
      "clkCnt" : {
        "total" : {
          "val" : 1
        },
        "ad" : {
          "val" : 1
        },
        "netTotal" : {
          "val" : 1
        },
        "netAd" : {
          "val" : 1
        }
      },
      "orderPayAmt" : {
        "total" : {
          "val" : 1
        },
        "ad" : {
          "val" : 1
        },
        "netTotal" : {
          "val" : 1
        },
        "netAd" : {
          "val" : 1
        }
      },
      "spend" : {
        "total" : {
          "val" : 1
        },
        "ad" : {
          "val" : 1
        },
        "netTotal" : {
          "val" : 1
        },
        "netAd" : {
          "val" : 1
        }
      },
      "orderPayCnt" : {
        "total" : {
          "val" : 1
        },
        "ad" : {
          "val" : 1
        },
        "netTotal" : {
          "val" : 1
        },
        "netAd" : {
          "val" : 1
        }
      },
      "roas" : {
        "total" : {
          "val" : 1
        },
        "ad" : {
          "val" : 1
        },
        "netTotal" : {
          "val" : 1
        },
        "netAd" : {
          "val" : 1
        }
      },
      "acos" : {
        "total" : {
          "val" : 1
        },
        "ad" : {
          "val" : 1
        },
        "netTotal" : {
          "val" : 1
        },
        "netAd" : {
          "val" : 1
        }
      },
      "transactionCost" : {
        "total" : {
          "val" : 1
        },
        "ad" : {
          "val" : 1
        },
        "netTotal" : {
          "val" : 1
        },
        "netAd" : {
          "val" : 1
        }
      },
      "goodsNum" : {
        "total" : {
          "val" : 1
        },
        "ad" : {
          "val" : 1
        },
        "netTotal" : {
          "val" : 1
        },
        "netAd" : {
          "val" : 1
        }
      },
      "imprCnt" : {
        "total" : {
          "val" : 1
        },
        "ad" : {
          "val" : 1
        },
        "netTotal" : {
          "val" : 1
        },
        "netAd" : {
          "val" : 1
        }
      },
      "cvr" : {
        "total" : {
          "val" : 1
        },
        "ad" : {
          "val" : 1
        },
        "netTotal" : {
          "val" : 1
        },
        "netAd" : {
          "val" : 1
        }
      }
    },
    "reportsItemList" : [ {
      "totalRoas" : {
        "val" : 1
      },
      "goodsId" : 1,
      "orderPayCnt" : {
        "val" : 1
      },
      "transactionCost" : {
        "val" : 1
      },
      "netAcos" : {
        "val" : 1
      },
      "totalOrderPayAmt" : {
        "val" : 1
      },
      "totalGoodsNum" : {
        "val" : 1
      },
      "roas" : {
        "val" : 1
      },
      "adSpend" : {
        "val" : 1
      },
      "goodsNum" : {
        "val" : 1
      },
      "netOrderPayCnt" : {
        "val" : 1
      },
      "totalImprCnt" : {
        "val" : 1
      },
      "cvr" : {
        "val" : 1
      },
      "ctr" : {
        "val" : 1
      },
      "cartCnt" : {
        "val" : 1
      },
      "totalAcos" : {
        "val" : 1
      },
      "netGoodsNum" : {
        "val" : 1
      },
      "orderPayAmt" : {
        "val" : 1
      },
      "netAdSpend" : {
        "val" : 1
      },
      "totalCtr" : {
        "val" : 1
      },
      "acos" : {
        "val" : 1
      },
      "totalCvr" : {
        "val" : 1
      },
      "totalClkCnt" : {
        "val" : 1
      },
      "imprCnt" : {
        "val" : 1
      },
      "totalTransactionCost" : {
        "val" : 1
      },
      "totalOrderPayCnt" : {
        "val" : 1
      },
      "netTransactionCost" : {
        "val" : 1
      },
      "clkCnt" : {
        "val" : 1
      },
      "netRoas" : {
        "val" : 1
      },
      "netOrderPayAmt" : {
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
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```