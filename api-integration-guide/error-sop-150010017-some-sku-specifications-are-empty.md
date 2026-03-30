# [Error SOP][150010017] Some SKU specifications are empty

| Error Code | Error Message |
|---|---|
| 150010017 | Some SKU specifications are empty |

- 

**Potential cause:**

If you are adding a new SKU under an existing `goodsId`, ensure that the `parentSpecId` of the new `specId` matches the existing `parentSpecId`.

For example;

```
  "skuList": [  
    {  
      "price": {  
        "basePrice": {  
          "amount": "26.60",  
          "currency": "EUR"  
        },  
        "listPriceType": "1"  
      },  
      "quantity": 50,  
      "specIdList": [  
        2001,              ---> From "specName": "White", "parentSpecName": "Color",  "parentSpecId": 1001          
        75366446           ---> From "specName": "1pc", "parentSpecName": "Size", "parentSpecId": 3001  
      ],                   ---> If the orginal goodsId's parentSpecName is "Color", "Style", you can now add a new SKU with  "Color", "Size"  
      "outSkuSn": "*6DZ0361WH-1",  
      "weight": "150",  
      "weightUnit": "g",  
      "length": "11.5",  
      "width": "8.4",  
      "height": "2.6",  
      "volumeUnit": "cm",  
      "images": [  
  
  
      ]  
    }  
  ],
```

- 

**From Seller Center Perspective:**

If a goods is defined by 2 variation type, then all the skus must contain variants from these 2 variation type. Add a variant from other variation type is not allowed.

![image](https://bstatic.kwcdn.com/open-outer/211a2a40000/48a9c51bc0d49448ca20375a2a610129.png)

- 

**Next Step**

Please review your request payload and ensure that every SKU includes variants from the two defined variation types. Remove any variants that belong to other variation types before sending the request again.
