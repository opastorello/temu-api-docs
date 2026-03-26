# [Error SOP][150011074] Upload {*} to {*} images

| Error Code | Error Message |
|---|---|
| 150011074 | Upload {*} to {*} images |

- 

**Root cause:**

SKU image quantity is 1 - 10.

Example:

In the `images` parameter, the number of images exceeds the maximum limit.

```
{  
  "app_key": "f7f83a8058228c1bc8f4993f28d95557",  
  "data_type": "JSON",  
  "access_token": "upl0gho4ovopvyvfiky4x7prgwh3dt1gfjea8ogdfqq1czzblsxs5aeyqew",  
  "timestamp": 1773648255,  
  "type": "bg.local.goods.add",  
  "version": "V1",  
  "goodsBasic": {  
    "goodsName": "수도세와 전기세, 공룡 시대의 체중 감량",  
    "catId": 1466  
  },  
  "goodsServicePromise": {  
    "shipmentLimitDay": 1,  
    "fulfillmentType": 1,  
    "costTemplateId": "LFT-15630053225717890848"  
  },  
  "goodsProperty": {  
    "goodsProperties": [  
      {  
        "pid": 1,  
        "vid": 381,  
        "value": "Stainless Steel",  
        "templatePid": 937018,  
        "refPid": 12  
      }  
    ]  
  },  
  "skuList": [  
    {  
      "price": {  
        "listPriceType": 1,  
        "basePrice": {  
          "amount": "3",  
          "currency": "KRW"  
        }  
      },  
      "quantity": 1,  
      "specIdList": [  
        76394262,  
        92523259  
      ],  
      "weight": "1",  
      "weightUnit": "g",  
      "length": "1",  
      "width": "1",  
      "height": "1",  
      "volumeUnit": "cm",  
      "images": [                           
        "https://img.kwcdn.com/local-image/s119/21a4885b68/198fc479-f78e-4549-a900-3c73f88cf556_1024x1024.png",  
        "https://img.kwcdn.com/local-image/s119/21a4885b68/198fc479-f78e-4549-a900-3c73f88cf556_1024x1024.png",  
        "https://img.kwcdn.com/local-image/s119/21a4885b68/198fc479-f78e-4549-a900-3c73f88cf556_1024x1024.png",  
        "https://img.kwcdn.com/local-image/s119/21a4885b68/198fc479-f78e-4549-a900-3c73f88cf556_1024x1024.png",  
        "https://img.kwcdn.com/local-image/s119/21a4885b68/198fc479-f78e-4549-a900-3c73f88cf556_1024x1024.png",  
        "https://img.kwcdn.com/local-image/s119/21a4885b68/198fc479-f78e-4549-a900-3c73f88cf556_1024x1024.png",  
        "https://img.kwcdn.com/local-image/s119/21a4885b68/198fc479-f78e-4549-a900-3c73f88cf556_1024x1024.png",  
        "https://img.kwcdn.com/local-image/s119/21a4885b68/198fc479-f78e-4549-a900-3c73f88cf556_1024x1024.png",  
        "https://img.kwcdn.com/local-image/s119/21a4885b68/198fc479-f78e-4549-a900-3c73f88cf556_1024x1024.png",  
        "https://img.kwcdn.com/local-image/s119/21a4885b68/198fc479-f78e-4549-a900-3c73f88cf556_1024x1024.png",  
        "https://img.kwcdn.com/local-image/s119/21a4885b68/198fc479-f78e-4549-a900-3c73f88cf556_1024x1024.png"  
      ]  
    }  
  ],  
  "sign": "66B3AE9662AE59F8F3C439D42458A1DE"  
}
```

- 

**From seller center perspective:**

![image](https://bstatic.kwcdn.com/open-outer/211a2a40000/494b9e5eb5abad6951a0dc1667a546d6.png)
