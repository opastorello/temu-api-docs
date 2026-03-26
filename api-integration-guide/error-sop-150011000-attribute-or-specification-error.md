# [Error SOP][150011000] Attribute or Specification Error: {*}

| Error Code | Error Message |
|---|---|
| 150011000 | Attribute or Specification Error: {*} |

- 

**Potential cause:**

The attribute passed in goodsProperties is incorrect.

Example: "Attribute or Specification Error: Keyword attribute [Upper Material] verification error: the value Fabric is not valid."

```
{  
    "success": false,  
    "requestId": "eu-51d24db3-dabc-4aa6-98d9-ca995230e345",  
    "errorCode": 150011000,  
    "errorMsg": "Attribute or Specification Error: Keyword attribute [Upper Material] verification error: the value Fabric is not valid."  
}
```

```
{  
  "app_key": "f860e759073f9d1e5c8bbeb7baac1dbf",  
  "data_type": "JSON",  
  "access_token": "eplz5amozhb9umkpjbmjau1kzwmxofpmk9xfgfclnategkthtsa2bhye2w3",  
  "timestamp": 1773642435,  
  "type": "bg.local.goods.add",  
  "version": "V1",  
  "goodsBasic": {  
    "goodsName": "DemoProduct0122",  
    "catId": 30567  
  },  
  "goodsServicePromise": {  
    "shipmentLimitDay": 1,  
    "fulfillmentType": 1,  
    "costTemplateId": "LFT-16010906347151571388"  
  },  
  "goodsProperty": {  
    "goodsProperties": [  
      {  
        "pid": 1294,  
        "value": "Fabric",  
        "templatePid": 1589588,  
        "refPid": 1259            -> Upper Material refPid is 1259, the control type of Upper Material is 1, which is a select type(must select a value(vid) from the values[])  
      },  
      {  
        "pid": 1289,  
        "vid": 31037,  
        "value": "Rubber",  
        "templatePid": 1589589,  
        "refPid": 1261  
      },  
      {  
        "pid": 1293,  
        "vid": 31074,  
        "value": "PVC",  
        "templatePid": 1589590,  
        "refPid": 1260  
      },  
      {  
        "pid": 1290,  
        "vid": 31049,  
        "value": "PU",  
        "templatePid": 1589601,  
        "refPid": 1262  
      },  
      {  
        "pid": 13,  
        "vid": 433,  
        "value": "Beige",  
        "templatePid": 1589586,  
        "refPid": 63,  
        "specId": "15060"  
      },  
      {  
        "pid": 14,  
        "vid": 72311,  
        "value": "51.5",  
        "templatePid": 1589587,  
        "refPid": 65,  
        "specId": "50262713"  
      }  
    ]  
  },  
  "skuList": [  
    {  
      "price": {  
        "listPriceType": 1,  
        "basePrice": {  
          "amount": "3",  
          "currency": "EUR"  
        }  
      },  
      "quantity": 999,  
      "specIdList": [  
        15060,  
        50262713  
      ],  
      "weight": "1",  
      "weightUnit": "g",  
      "length": "1",  
      "width": "1",  
      "height": "1",  
      "volumeUnit": "cm",  
      "images": [  
        "https://img-eu.kwcdn.com/local-goods-img/21a4886834/4811653b-14d4-41c4-99ac-be8dc264814d_800x800.jpeg.format.jpg"  
      ]  
    }  
  ],  
  "sign": "841820707B0ADC91C34F04851414A24E"  
}
```

```
        {  
          "chooseMaxNum": 1,  
          "controlType": 1,  
          "feature": 0,  
          "isSale": false,  
          "mainSale": null,  
          "maxValue": "",  
          "minValue": "",  
          "name": "Upper Material",  
          "numberInputTitle": null,  
          "parentSpecId": null,  
          "parentTemplatePid": 0,  
          "pid": 1294,  
          "propertyChooseTitle": null,  
          "propertyValueType": 0,  
          "refPid": 1259,  
          "referenceType": null,  
          "required": false,  
          "showCondition": null,  
          "showType": 0,  
          "templateModuleId": 285972,  
          "templatePid": 1589588,  
          "templatePropertyValueParentList": null,  
          "transnationalAttribute": null,  
          "valuePrecision": 0,  
          "valueRule": 0,  
          "valueUnitList": null,  
          "values": [  
            {  
              "additionalInfo": null,  
              "brandId": null,  
              "extendInfo": null,  
              "group": null,  
              "parentVids": null,  
              "specId": null,  
              "subGroup": null,  
              "value": "PU",  
              "vid": 31092  
            },  
            ...  
        ]
```

From API per perspective:

attribute [Upper Material] refPid is 1259, the control type of Upper Material is 1, which is a select type (must select a value(vid) from the values[]).

ref： [https://partner.temu.com/documentation?menu_code=38e79b35d2cb463d85619c1c786dd303&sub_menu_code=d7943785ff2e4185976170f07924256e](https://partner.temu.com/documentation?menu_code=38e79b35d2cb463d85619c1c786dd303&sub_menu_code=d7943785ff2e4185976170f07924256e)

From seller center perspective:

The attribute (`refPid`) is not choosed correctly. For example, this field is an input box, but no value was provided.

![image](https://bstatic.kwcdn.com/open-outer/211a2a40000/815b5a50f6ecaa509c26013820c93527.png)

- 

**Next step:**

Query bg.local.goods.template.get or temu.local.product.attributes.get to get the attributes.

Make sure the passed attributes meet the following requirements:

![image](https://bstatic.kwcdn.com/open-outer/211a2a40000/9cca6dadf1a10be7b6553bd16a64e6fa.png)

ref: [https://partner.temu.com/documentation?menu_code=38e79b35d2cb463d85619c1c786dd303&sub_menu_code=d7943785ff2e4185976170f07924256e](https://partner.temu.com/documentation?menu_code=38e79b35d2cb463d85619c1c786dd303&sub_menu_code=d7943785ff2e4185976170f07924256e)
