# temu.searchrec.ad.detail.query

**Advertising campaign details query interface**

Advertising campaign details query

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
| goodsList | 8 | No |  |  |

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
  "goodsList" : [ 1, 1 ],
  "type" : "test",
  "version" : "test",
  "timestamp" : "test"
}'
```

## Response Example

```json
{
  "result" : {
    "adsDetail" : [ {
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
      "adPhase" : 1,
      "siteStatusInfoList" : [ {
        "forbidReason" : "test",
        "siteNameList" : [ "test", "test" ],
        "adShowStatus" : 1
      } ],
      "goodsId" : 1,
      "reportsSummaryDTO" : {
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
      },
      "roas" : 1,
      "adShowStatus" : 1,
      "budget" : 1
    } ]
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```