# [Error SOP][150011003]Invalid Request Parameters [{*}]

| Error Code | Error Message |
|---|---|
| 150011003 | Invalid Request Parameters [{*}] |

- 

**Potential Cause:**

Required parameters are missing, or the parameter names/data types are incorrect. Please note that any parameters not defined in our API request specification will be ignored.

- 

**Example1："Invalid Request Parameters [goodsServicePromise]"**

goodsServicePromise parameter is **required**.

```
{  
    "success": false,  
    "requestId": "gl-018bd6bd-8d8a-4388-b779-05431bb84fa6",  
    "errorCode": 150011003,  
    "errorMsg": "Invalid Request Parameters [goodsServicePromise]"  
}
```

```
{  
  "app_key": "xxxxx",  
  "data_type": "JSON",  
  "access_token": "xxxxx",  
  "timestamp": 1773736136,  
  "type": "bg.local.goods.add",  
  "version": "V1",  
  "goodsBasic": {  
    "goodsName": "Utilisons ce tableau",  
    "catId": 33965  
  },  
  "goodsProperty": {  
    "goodsProperties": [  
      {  
        "pid": 1,  
        "vid": 3,  
        "value": "Elastane",  
        "templatePid": 863134,  
        "refPid": 12  
      },  
      {  
        "pid": 5,  
        "vid": 172,  
        "value": "Hooded",  
        "templatePid": 863139,  
        "refPid": 21  
      },  
      {  
        "pid": 14,  
        "vid": 317,  
        "value": "M",  
        "templatePid": 863132,  
        "refPid": 65,  
        "parentSpecId": "3001",  
        "specId": "9005"  
      },  
      {  
        "pid": 13,  
        "vid": 376,  
        "value": "White",  
        "templatePid": 863133,  
        "refPid": 63,  
        "parentSpecId": "1001",  
        "specId": "2001"  
      }  
    ]  
  },  
  "skuList": [  
    {  
      "price": {  
        "listPriceType": "1",  
        "basePrice": {  
          "amount": "34800",  
          "currency": "JPY"  
        }  
      },  
      "quantity": 77,  
      "specIdList": [  
        2001,  
        9005  
      ],  
      "weight": "12",  
      "weightUnit": "g",  
      "length": "1",  
      "width": "1",  
      "height": "1",  
      "volumeUnit": "cm",  
      "images": [  
        "https://img.kwcdn.com/local-image/s119/2066d90972/834824af-c19e-47e3-94de-bebad267f10c_1340x1787.jpeg.format.jpg"  
      ],  
      "multiplePackage": {  
        "mixedSetType": 1,  
        "numberOfPieces": 98  
      }  
    }  
  ],  
  "sign": "FAB6F17101D7AFBA54068E883D9D625C"  
}
```

Correct Example:

```
{  
  "app_key": "xxxx",  
  "data_type": "JSON",  
  "access_token": "xxxx",  
  "timestamp": 1773736195,  
  "type": "bg.local.goods.add",  
  "version": "V1",  
  "goodsBasic": {  
    "goodsName": "Utilisons ce tableau",  
    "catId": 33965  
  },  
  "goodsServicePromise": {  
    "shipmentLimitDay": 1,  
    "fulfillmentType": 1,  
    "costTemplateId": "LFT-16090107374182530848"  
  },  
  "goodsProperty": {  
    "goodsProperties": [  
      {  
        "pid": 1,  
        "vid": 3,  
        "value": "Elastane",  
        "templatePid": 863134,  
        "refPid": 12  
      },  
      {  
        "pid": 5,  
        "vid": 172,  
        "value": "Hooded",  
        "templatePid": 863139,  
        "refPid": 21  
      },  
      {  
        "pid": 14,  
        "vid": 317,  
        "value": "M",  
        "templatePid": 863132,  
        "refPid": 65,  
        "parentSpecId": "3001",  
        "specId": "9005"  
      },  
      {  
        "pid": 13,  
        "vid": 376,  
        "value": "White",  
        "templatePid": 863133,  
        "refPid": 63,  
        "parentSpecId": "1001",  
        "specId": "2001"  
      }  
    ]  
  },  
  "skuList": [  
    {  
      "price": {  
        "listPriceType": "1",  
        "basePrice": {  
          "amount": "34800",  
          "currency": "JPY"  
        }  
      },  
      "quantity": 77,  
      "specIdList": [  
        2001,  
        9005  
      ],  
      "weight": "12",  
      "weightUnit": "g",  
      "length": "1",  
      "width": "1",  
      "height": "1",  
      "volumeUnit": "cm",  
      "images": [  
        "https://img.kwcdn.com/local-image/s119/2066d90972/834824af-c19e-47e3-94de-bebad267f10c_1340x1787.jpeg.format.jpg"  
      ],  
      "multiplePackage": {  
        "mixedSetType": 1,  
        "numberOfPieces": 98  
      }  
    }  
  ],  
  "sign": "4AD2842A830CE83F4330E24D6EF87C9F"  
}
```

- 

**Example2："Invalid Request Parameters [specIdList]"**

Please make sure each added sku in skuList has **specIdList**.

Ref: [https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=ea85c857a38d42a7a22fb6779776b166](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=ea85c857a38d42a7a22fb6779776b166)
