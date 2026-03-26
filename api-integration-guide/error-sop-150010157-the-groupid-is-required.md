# [Error SOP][150010157]The groupId  is required.

| Error Code | Error Message |
|---|---|
| 150010157 | The groupId  is required. |

- 

**Root cause:**

For temu.local.goods.v2.add, if size specification is included, groupId must also be provided.

```
{  
  "app_key": "f860e759073f9d1e5c8bbeb7baac1dbf",  
  "data_type": "JSON",  
  "access_token": "eplwmc9efqzy0rwenlz8jsmkumobexpyzhzy6qzfz6bpn8ygeq5hikzfeq7",  
  "timestamp": 1773146074,  
  "type": "temu.local.goods.v2.add",  
  "version": "V1",  
  "goodsBasic": {  
    "goodsName": "opengoodsV2 0310001 T-Shirts",  
    "catId": 29069  
  },  
  "goodsServicePromise": {  
    "shipmentLimitDay": 1,  
    "costTemplateId": "LFT-13630901943132180183"  
  },  
  "goodsSize": {  
    "groupId": "16",              -> # "groupId" must be provided as in specDetails, Size specification is included.  
    "goodsSizeImage": [  
      "https://img-eu.kwcdn.com/local-goods-img/1f79704990/d3d2d27a-0ebc-4ed2-955f-1be2ec6598f3_1361x1815.jpeg"  
    ]  
  },  
  "skuList": [  
    {  
      "price": {  
        "basePrice": {  
          "amount": "100",  
          "currency": "EUR"  
        }  
      },  
      "quantity": 100,  
      "specDetails": [  
        {  
          "specId": "2001",  
          "parentSpecId": "1001",  
          "specName": "White"  
        },  
        {  
          "specId": "15136",  
          "parentSpecId": "3001",  
          "specName": "Size"  
        }  
      ],  
      "packageInfo": {  
        "weight": "2",  
        "length": "2",  
        "width": "32",  
        "height": "2"  
      },  
      "images": [  
        "https://img-eu.kwcdn.com/local-goods-img/1f79704990/d3d2d27a-0ebc-4ed2-955f-1be2ec6598f3_1361x1815.jpeg"  
      ]  
    }  
  ],  
  "sign": "E091C065FBBDABE3DCA2A4F9A1AE3A91"  
}
```

- 

**From seller center perspective:**

Size Standard contains different size groups. All size variants under the same `goodsId` must come from the same Size Standard (`groupId`).

![image](https://bstatic.kwcdn.com/open-outer/211a2a40000/f3e7b495ffd54be16215984da90d5f31.png)

- 

**Next step:**

Query temu.local.product.variation.get to get the "groupId" of the size specification.

```
{  
    "subGroupName": "Numeric",  
    "specId": 15136,  
    "groupName": "Brazil size",  
    "specName": "34",  
    "groupId": 16,  
    "subGroupId": 7  
},
```
