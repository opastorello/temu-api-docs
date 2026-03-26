# [Error SOP][150011010]The keyword attribute [{*}] is required, please fill in accurately and appropriately

| Error Code | Error Message |
|---|---|
| 150011010 | The keyword attribute [{*}] is required, please fill in accurately and appropriately |

- 

**Potential cause:**

This error occurs when required attributes are not provided during product listing.

Example: The keyword attribute [Material] is required, please fill in accurately and appropriately

```
{  
    "success": false,  
    "requestId": "us-8320868f-9796-4640-b93e-cdfa59870afd",  
    "errorCode": 150011010,  
    "errorMsg": "The keyword attribute [Material] is required, please fill in accurately and appropriately"  
}
```

```
{  
  "app_key": "4ebbc9190ae410443d65b4c2faca981f",  
  "data_type": "JSON",  
  "access_token": "uplv3hfyt5kcwoymrgnajnbl1ow5qxlz4sqhev6hl3xosz5dejrtyl2jre7",  
  "timestamp": 1773752386,  
  "type": "bg.local.goods.add",  
  "version": "V1",  
  "goodsBasic": {  
    "goodsName": "DemoProduct-Brand&Sizechart",  
    "catId": 27609,  
    "importDesignation": "Imported",  
    "goodsGallery": {  
      "detailVideo": {  
        "vid": "local-goods-video#zon0bhtmbkuj20hzdwmh78w2hxe8a6m8",  
        "videoUrl": "https://goods-vod.kwcdn.com/local-goods-video/21a488e56e/dc511f468fdc4243d6aa7e6fded902ca.mp4"  
      },  
      "carouselVideo": {  
        "vid": "local-goods-video#gkfemicucebmyiszf6hs78w358bh4bgg",  
        "videoUrl": "https://goods-vod.kwcdn.com/local-goods-video/21a488e56e/4d5aa1dc86b70d5adc1166ac2c5ca4b0.mp4"  
      },  
      "detailImage": [  
        "https://img.kwcdn.com/local-goods-image/21a488e56e/b1093e02-e853-4353-bac9-3525042dae36_1024x1024.png"  
      ]  
    },  
    "productType": 1  
  },  
  "goodsServicePromise": {  
    "shipmentLimitDay": 2,  
    "fulfillmentType": 1,  
    "costTemplateId": "LFT-11910454159237172414"  
  },  
  "goodsProperty": {  
    "goodsProperties": [  
      {  
        "pid": 5,  
        "vid": 172,  
        "value": "Hooded",  
        "templatePid": 862509,  
        "refPid": 21  
      },  
      {  
        "vid": 95,  
        "value": "Nylon",  
        "valueUnit": "%",  
        "valueUnitId": 57,  
        "refPid": 15,  
        "numberInputValue": "100"  
      },  
      {  
        "pid": 1467,  
        "vid": 309620,  
        "value": "FANSIWENCESHI",  
        "templatePid": 862528,  
        "refPid": 1960  
      },  
      {  
        "pid": 13,  
        "vid": 433,  
        "value": "Beige",  
        "templatePid": 862503,  
        "refPid": 63,  
        "parentSpecId": "1001",  
        "specId": "15060"  
      },  
      {  
        "pid": 14,  
        "vid": 313,  
        "value": "XS",  
        "templatePid": 862502,  
        "refPid": 65,  
        "parentSpecId": "3001",  
        "specId": "12001"  
      },  
      {  
        "pid": 14,  
        "vid": 315,  
        "value": "S",  
        "templatePid": 862502,  
        "refPid": 65,  
        "parentSpecId": "3001",  
        "specId": "10004"  
      }  
    ]  
  },  
  "skuList": [  
    {  
      "price": {  
        "listPriceType": 0,  
        "listPrice": {  
          "amount": "0.03",  
          "currency": "USD"  
        },  
        "basePrice": {  
          "amount": "0.02",  
          "currency": "USD"  
        }  
      },  
      "quantity": 999,  
      "specIdList": [  
        12001,  
        15060  
      ],  
      "weight": "1",  
      "weightUnit": "lb",  
      "length": "1",  
      "width": "1",  
      "height": "1",  
      "volumeUnit": "in",  
      "images": [  
        "https://img.kwcdn.com/local-goods-image/21a488e56e/28964774-449b-4302-a795-89e1490ad828_1340x1787.png"  
      ],  
      "referenceLink": "https://partner-us.temu.com/documentation?menu_code=38e79b35d2cb463d85619c1c786dd303&sub_menu_code=d7943785ff2e4185976170f07924256e"  
    },  
    {  
      "price": {  
        "listPriceType": 0,  
        "listPrice": {  
          "amount": "0.03",  
          "currency": "USD"  
        },  
        "basePrice": {  
          "amount": "0.02",  
          "currency": "USD"  
        }  
      },  
      "quantity": 888,  
      "specIdList": [  
        10004,  
        15060  
      ],  
      "weight": "2",  
      "weightUnit": "lb",  
      "length": "2",  
      "width": "2",  
      "height": "2",  
      "volumeUnit": "in",  
      "images": [  
        "https://img.kwcdn.com/local-goods-image/21a488e56e/28964774-449b-4302-a795-89e1490ad828_1340x1787.png"  
      ],  
      "referenceLink": "https://partner-us.temu.com/documentation?menu_code=38e79b35d2cb463d85619c1c786dd303&sub_menu_code=d7943785ff2e4185976170f07924256e"  
    }  
  ],  
  "goodsTrademark": {  
    "trademarkId": 312000170001,  
    "noTrademark": false,  
    "brandId": 110033916002  
  },  
  "goodsSizeChartList": {  
    "goodsSizeChartList": [  
      {  
        "meta": {  
          "groups": [  
            {  
              "id": 1,  
              "name": "Size"  
            },  
            {  
              "id": 6,  
              "name": "US"  
            }  
          ],  
          "elements": [  
            {  
              "id": 10002,  
              "name": "Chest"  
            },  
            {  
              "id": 10003,  
              "name": "Length"  
            }  
          ]  
        },  
        "classId": 3,  
        "records": [  
          {  
            "values": [  
              {  
                "id": 1,  
                "value": "XS"  
              },  
              {  
                "id": 10002,  
                "value": "1"  
              },  
              {  
                "id": 10003,  
                "value": "1"  
              },  
              {  
                "id": 6,  
                "value": "XS"  
              }  
            ]  
          },  
          {  
            "values": [  
              {  
                "id": 1,  
                "value": "S"  
              },  
              {  
                "id": 10002,  
                "value": "2"  
              },  
              {  
                "id": 10003,  
                "value": "2"  
              },  
              {  
                "id": 6,  
                "value": "S"  
              }  
            ]  
          }  
        ],  
        "bodyMeta": {  
          "groups": [  
            {  
              "id": 1,  
              "name": "Size"  
            }  
          ],  
          "elements": [  
            {  
              "id": 30002,  
              "name": "Bust"  
            },  
            {  
              "id": 30000,  
              "name": "Waist"  
            }  
          ]  
        },  
        "bodyRecords": [  
          {  
            "values": [  
              {  
                "id": 30000,  
                "value": "2-3"  
              },  
              {  
                "id": 1,  
                "value": "XS"  
              },  
              {  
                "id": 30002,  
                "value": "1-2"  
              }  
            ]  
          },  
          {  
            "values": [  
              {  
                "id": 30000,  
                "value": "4-5"  
              },  
              {  
                "id": 1,  
                "value": "S"  
              },  
              {  
                "id": 30002,  
                "value": "3-4"  
              }  
            ]  
          }  
        ]  
      }  
    ]  
  },  
  "goodsOriginInfo": {  
    "agreeDefaultOriginRegion": true,  
    "originRegion1": "Mainland China",  
    "proofImageUrls": [  
      "https://dl.kwcdn.com/local-goods-specification/21a488e56e/8ac31ead47238aae7789eb13efb85681.pdf"  
    ],  
    "originRegion2": "Guangdong"  
  },  
  "sign": "723A967579C6E0CE7E49FE793D80C49C"  
}
```

Correct request:

```
{  
    "result": {  
        "goodsId": 603070943592692,  
        "warnings": null,  
        "skuInfoList": [  
            {  
                "specList": [  
                    {  
                        "specId": 12001,  
                        "parentSpecId": 3001  
                    },  
                    {  
                        "specId": 15060,  
                        "parentSpecId": 1001  
                    }  
                ],  
                "outSkuSn": "",  
                "skuId": 39604564545835  
            },  
            {  
                "specList": [  
                    {  
                        "specId": 10004,  
                        "parentSpecId": 3001  
                    },  
                    {  
                        "specId": 15060,  
                        "parentSpecId": 1001  
                    }  
                ],  
                "outSkuSn": "",  
                "skuId": 39604564578603  
            }  
        ],  
        "productType": 1  
    },  
    "success": true,  
    "requestId": "us-bbe484b9-b28e-4f7a-a240-13d31e7e6a86",  
    "errorCode": 1000000,  
    "errorMsg": ""  
}
```

```
{  
  "app_key": "4ebbc9190ae410443d65b4c2faca981f",  
  "data_type": "JSON",  
  "access_token": "uplv3hfyt5kcwoymrgnajnbl1ow5qxlz4sqhev6hl3xosz5dejrtyl2jre7",  
  "timestamp": 1773752567,  
  "type": "bg.local.goods.add",  
  "version": "V1",  
  "goodsBasic": {  
    "goodsName": "DemoProduct-Brand&Sizechart",  
    "catId": 27609,  
    "importDesignation": "Imported",  
    "goodsGallery": {  
      "detailVideo": {  
        "vid": "local-goods-video#zon0bhtmbkuj20hzdwmh78w2hxe8a6m8",  
        "videoUrl": "https://goods-vod.kwcdn.com/local-goods-video/21a488e56e/dc511f468fdc4243d6aa7e6fded902ca.mp4"  
      },  
      "carouselVideo": {  
        "vid": "local-goods-video#gkfemicucebmyiszf6hs78w358bh4bgg",  
        "videoUrl": "https://goods-vod.kwcdn.com/local-goods-video/21a488e56e/4d5aa1dc86b70d5adc1166ac2c5ca4b0.mp4"  
      },  
      "detailImage": [  
        "https://img.kwcdn.com/local-goods-image/21a488e56e/b1093e02-e853-4353-bac9-3525042dae36_1024x1024.png"  
      ]  
    },  
    "productType": 1  
  },  
  "goodsServicePromise": {  
    "shipmentLimitDay": 2,  
    "fulfillmentType": 1,  
    "costTemplateId": "LFT-11910454159237172414"  
  },  
  "goodsProperty": {  
    "goodsProperties": [  
      {  
        "pid": 1,  
        "vid": 3,  
        "value": "Spandex",  
        "templatePid": 862504,  
        "refPid": 12  
      },  
      {  
        "pid": 5,  
        "vid": 172,  
        "value": "Hooded",  
        "templatePid": 862509,  
        "refPid": 21  
      },  
      {  
        "vid": 95,  
        "value": "Nylon",  
        "valueUnit": "%",  
        "valueUnitId": 57,  
        "refPid": 15,  
        "numberInputValue": "100"  
      },  
      {  
        "pid": 1467,  
        "vid": 309620,  
        "value": "FANSIWENCESHI",  
        "templatePid": 862528,  
        "refPid": 1960  
      },  
      {  
        "pid": 13,  
        "vid": 433,  
        "value": "Beige",  
        "templatePid": 862503,  
        "refPid": 63,  
        "parentSpecId": "1001",  
        "specId": "15060"  
      },  
      {  
        "pid": 14,  
        "vid": 313,  
        "value": "XS",  
        "templatePid": 862502,  
        "refPid": 65,  
        "parentSpecId": "3001",  
        "specId": "12001"  
      },  
      {  
        "pid": 14,  
        "vid": 315,  
        "value": "S",  
        "templatePid": 862502,  
        "refPid": 65,  
        "parentSpecId": "3001",  
        "specId": "10004"  
      }  
    ]  
  },  
  "skuList": [  
    {  
      "price": {  
        "listPriceType": 0,  
        "listPrice": {  
          "amount": "0.03",  
          "currency": "USD"  
        },  
        "basePrice": {  
          "amount": "0.02",  
          "currency": "USD"  
        }  
      },  
      "quantity": 999,  
      "specIdList": [  
        12001,  
        15060  
      ],  
      "weight": "1",  
      "weightUnit": "lb",  
      "length": "1",  
      "width": "1",  
      "height": "1",  
      "volumeUnit": "in",  
      "images": [  
        "https://img.kwcdn.com/local-goods-image/21a488e56e/28964774-449b-4302-a795-89e1490ad828_1340x1787.png"  
      ],  
      "referenceLink": "https://partner-us.temu.com/documentation?menu_code=38e79b35d2cb463d85619c1c786dd303&sub_menu_code=d7943785ff2e4185976170f07924256e"  
    },  
    {  
      "price": {  
        "listPriceType": 0,  
        "listPrice": {  
          "amount": "0.03",  
          "currency": "USD"  
        },  
        "basePrice": {  
          "amount": "0.02",  
          "currency": "USD"  
        }  
      },  
      "quantity": 888,  
      "specIdList": [  
        10004,  
        15060  
      ],  
      "weight": "2",  
      "weightUnit": "lb",  
      "length": "2",  
      "width": "2",  
      "height": "2",  
      "volumeUnit": "in",  
      "images": [  
        "https://img.kwcdn.com/local-goods-image/21a488e56e/28964774-449b-4302-a795-89e1490ad828_1340x1787.png"  
      ],  
      "referenceLink": "https://partner-us.temu.com/documentation?menu_code=38e79b35d2cb463d85619c1c786dd303&sub_menu_code=d7943785ff2e4185976170f07924256e"  
    }  
  ],  
  "goodsTrademark": {  
    "trademarkId": 312000170001,  
    "noTrademark": false,  
    "brandId": 110033916002  
  },  
  "goodsSizeChartList": {  
    "goodsSizeChartList": [  
      {  
        "meta": {  
          "groups": [  
            {  
              "id": 1,  
              "name": "Size"  
            },  
            {  
              "id": 6,  
              "name": "US"  
            }  
          ],  
          "elements": [  
            {  
              "id": 10002,  
              "name": "Chest"  
            },  
            {  
              "id": 10003,  
              "name": "Length"  
            }  
          ]  
        },  
        "classId": 3,  
        "records": [  
          {  
            "values": [  
              {  
                "id": 1,  
                "value": "XS"  
              },  
              {  
                "id": 10002,  
                "value": "1"  
              },  
              {  
                "id": 10003,  
                "value": "1"  
              },  
              {  
                "id": 6,  
                "value": "XS"  
              }  
            ]  
          },  
          {  
            "values": [  
              {  
                "id": 1,  
                "value": "S"  
              },  
              {  
                "id": 10002,  
                "value": "2"  
              },  
              {  
                "id": 10003,  
                "value": "2"  
              },  
              {  
                "id": 6,  
                "value": "S"  
              }  
            ]  
          }  
        ],  
        "bodyMeta": {  
          "groups": [  
            {  
              "id": 1,  
              "name": "Size"  
            }  
          ],  
          "elements": [  
            {  
              "id": 30002,  
              "name": "Bust"  
            },  
            {  
              "id": 30000,  
              "name": "Waist"  
            }  
          ]  
        },  
        "bodyRecords": [  
          {  
            "values": [  
              {  
                "id": 30000,  
                "value": "2-3"  
              },  
              {  
                "id": 1,  
                "value": "XS"  
              },  
              {  
                "id": 30002,  
                "value": "1-2"  
              }  
            ]  
          },  
          {  
            "values": [  
              {  
                "id": 30000,  
                "value": "4-5"  
              },  
              {  
                "id": 1,  
                "value": "S"  
              },  
              {  
                "id": 30002,  
                "value": "3-4"  
              }  
            ]  
          }  
        ]  
      }  
    ]  
  },  
  "goodsOriginInfo": {  
    "agreeDefaultOriginRegion": true,  
    "originRegion1": "Mainland China",  
    "proofImageUrls": [  
      "https://dl.kwcdn.com/local-goods-specification/21a488e56e/8ac31ead47238aae7789eb13efb85681.pdf"  
    ],  
    "originRegion2": "Guangdong"  
  },  
  "sign": "28AECA2E62540A52734745E129AC8E50"  
}
```

- 

**From Seller Center Perspective**

**Product attributes: **Divided into required attributes and optional attributes;

Required attributes are important product attributes and can help buyers get a better understanding of the product. Please ensure that all required attributes are passed in goodsProperty.

      For example, “Material” is a required attribute and must be provided by the seller.

![image](https://bstatic.kwcdn.com/open-outer/211a2a4b39c/cd2189f6decb16f34433a8b5da920770.png)

- 

**Next Step**

Please pass the required attributes[{*}] in your request payload.

Ref: [https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=ea85c857a38d42a7a22fb6779776b166](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=ea85c857a38d42a7a22fb6779776b166)
