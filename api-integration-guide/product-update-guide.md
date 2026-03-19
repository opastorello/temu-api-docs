# Product Update Guide

Both **bg.local.goods.update** and **bg.local.goods.partial.update** can be used to update product data, but we recommend using the **bg.local.goods.partial.update** API.

- 
### 

**Guidelines for Modifying SKUs**

1. 

For a modified SKU: the **skuId** must be included in **skuList**.

1. 

For a modified SKU: the **base price**, **inventory**, and **variant specifications** cannot be modified through the current interface. Therefore, **skuList** mast not include **basePrice**, **quantity**, and **specIdList** fields.

- 
### 

**Guidelines for Adding SKUs**

1. 

For a newly added SKU: do not include **skuId** in **skuList**.

1. 

For a newly added SKU: **basePrice (amount/currency)**, **quantity**, and **specIdList** are required.

1. 

For a newly added SKU: the **specIdList** cannot duplicate that of any existing SKU of the product.

1. 

If a new SKU is added, the corresponding specifications need to be provided in **goodsProperties**.

1. 

If adding a new SKU modifies **goodsSizeChartList**, the updated **goodsSizeChartList** must also be uploaded.

*Example*: If the product originally has short-sleeved shirts in sizes S and M, and size L is added, the size data for L must also be included in **goodsSizeChartList**.

1. 

After adding a SKU, all variant combinations must have corresponding SKUs.

*Example*: If the product has short-sleeved shirts in [Black, S] and [Black, M], and the "White" specification is added, then [White, S] and [White, M] SKUs must also be added.

- 
### 

**Interface Description**

#### 

**bg.local.goods.update**

1. 

You must provide all product data. Any fields not provided will be cleared. Before updating, use **bg.local.goods.detail.query** to retrieve the current product data.

1. 

When modifying an existing SKU, **inventory and price cannot be updated**. To modify inventory or price, use:

  1. 

**bg.local.goods.stock.edit**

  1. 

**bg.local.goods.priceorder.change.sku.price**

1. 

Any items in **skuList** without a **skuId** will be treated as newly added SKUs.

1. 

New parameter description：

  1. 

**basePrice**：

    1. 

Both *amount* and *currency* must be set. For details, please refer to the document: [Product Differences in site currency, volume](https://partner-eu.temu.com/documentation?menu_code=85762c6ccc5a4dbc8c023ea5e10c6dc0&sub_menu_code=17b01376cfff4877a144df2c09ce3ace).

    1. 

Required when adding a SKU.

    1. 

Must not be included when modifying an existing SKU.

  1. 

**quantity**：

    1. 

Represents the inventory of the product. Valid range: **[0, 999999]**.

    1. 

When adding (appending) a SKU, quantity must be passed in;

    1. 

When modifying an existing SKU, **quantity** must not be passed.

  1. 

**specIdList**：

    1. 

 Represents the product’s sales attributes. For details, please refer to the document: [Product Attributes](https://partner-eu.temu.com/documentation?menu_code=85762c6ccc5a4dbc8c023ea5e10c6dc0&sub_menu_code=4fe287d454d14fd89056bd80438bb08a);

    1. 

When adding (appending) a SKU, **specIdList** is required;

    1. 

When modifying an existing SKU, **specIdList** must not be passed.

  1. 

**outSkuSn**：

    1. 

Allowed characters: English letters, numbers, and symbols;

    1. 

Maximum length: 100 characters;

    1. 

Must not duplicate any other SKU/SPU ID within the same store;

    1. 

When adding (appending) a SKU, if **outSkuSn** is provided, it must comply with the above rules; otherwise, it can be omitted;

    1. 

When modifying an existing SKU, if **outSkuSn** is provided, it will overwrite the original value. If left empty or omitted, the original value will be cleared.

#### 

**bg.local.goods.partial.update**

1. 

Submitted product data will overwrite existing values, while data not submitted will remain unchanged.

1. 

When modifying an existing SKU, **inventory and price cannot be updated**. To modify inventory or price, use:

  1. 

**bg.local.goods.stock.edit**

  1. 

**bg.local.goods.priceorder.change.sku.price**

1. 

Any items in **skuList** without a **skuId** will be treated as newly added SKUs.

1. 

New parameter description：

  1. 

**basePrice**：

    1. 

Both *amount* and *currency* must be set. For details, please refer to the document: [Product Differences in site currency, volume](https://partner-eu.temu.com/documentation?menu_code=85762c6ccc5a4dbc8c023ea5e10c6dc0&sub_menu_code=17b01376cfff4877a144df2c09ce3ace);

    1. 

When adding (appending) a SKU, **basePrice** is required;

    1. 

When modifying an existing SKU, **basePrice** must not be passed.

  1. 

**quantity**：

    1. 

Represents the inventory of the product. Valid range: **[0, 999999]**.

    1. 

When adding (appending) a SKU, quantity must be passed in;

    1. 

When modifying an existing SKU, **quantity** must not be passed.

  1. 

**specIdList**：

    1. 

 Represents the product’s sales attributes. For details, please refer to the document: [Product Attributes](https://partner-eu.temu.com/documentation?menu_code=85762c6ccc5a4dbc8c023ea5e10c6dc0&sub_menu_code=4fe287d454d14fd89056bd80438bb08a);

    1. 

When adding (appending) a SKU, **specIdList** is required;

    1. 

When modifying an existing SKU, **specIdList** must not be passed.

  1. 

**outSkuSn**：

    1. 

Allowed characters: English letters, numbers, and symbols;

    1. 

Maximum length: 100 characters;

    1. 

Must not duplicate any other SKU/SPU ID within the same store;

    1. 

When adding (appending) a SKU, if **outSkuSn** is provided, it must comply with the above rules; otherwise, it can be omitted;

    1. 

When modifying an existing SKU: if **outSkuSn** is provided, it will overwrite the original value; if provided as empty, it will clear the original value; if omitted, the original value will be retained.

### 

**The following product statuses do not support updating product data:**

****

****

****

| goodsStatusFilterType | goodsSubStatusFilterType | Description |
|---|---|---|
| 4-Incomplete | 4001: Price evaluation in progress | The product has not been successfully published because the platform is still evaluating its price. |
| 4-Incomplete | 4002: Auditing and processing | The product is still in the process of being published because data processing is ongoing. |
| 6-Deleted | 6001: Non-first release product deleted | The product has been deleted. |
| 6-Deleted | 6002: Price verification terminated product deleted | The product was deleted due to price rejection. |

Additionally, when a product is in the **“New version processing”** status, product data cannot be updated. You need to wait until the new version processing is completed before updating the product data.

![image](https://bstatic.kwcdn.com/open-outer/2066d9197e/6b6b2bcbe7bdd85840a5425167872e1d.png)

### 

**Demo for adding SKUs：**

#### 

**bg.local.goods.update**

```
{  
    "goodsId": 604284632545419,  
    "goodsBasic": {  
        "goodsName": "kaiping quanliang gengxin "  
    },  
    "goodsServicePromise": {  
        "shipmentLimitDay": 1,  
        "fulfillmentType": 1,  
        "costTemplateId": "LFT-11620561533419540183"  
    },  
    "goodsProperty": {  
        "goodsProperties": [  
            {  
                "value": "yellow",  
                "parentSpecId": "1001",  
                "specId": 72537089,  
            },  
            {  
                "value": "black",  
                "parentSpecId": "1001",  
                "specId": 72260020, //The specId used for the additional SKU  
            },  
        ]  
    },  
    "skuList": [  
        {//Since skuId is included in this struct, basePrice, quantity, and specIdList are not passed in.  
            "skuId":58795954861238,  
            "listPrice": {  
                "amount": "20",  
                "currency": "EUR"  
            },  
            "weight": "1",  
            "length": "1",  
            "width": "1",  
            "height": "1",  
            "weightUnit": "g",  
            "volumeUnit": "cm",  
            "images": [  
                "https://img-eu.kwcdn.com/local-goods-img/*********.jpg"  
            ]  
        },  
        {//This struct is for an additional SKU, so skuId is not provided; instead, basePrice, quantity, and specIdList are passed in.  
            "basePrice": {  
                "amount": "10",  
                "currency": "EUR"  
            },  
            "listPrice": {  
                "amount": "30",  
                "currency": "EUR"  
            },  
            "listPriceType": 0,  
            "specIdList": [72260020],  
            "quantity": 100,  
            "weight": "12",  
            "weightUnit": "g",  
            "length": "213",  
            "width": "32",  
            "height": "23",  
            "volumeUnit": "cm",  
            "images": [  
                "https://img-eu.kwcdn.com/local-goods-img/*********.jpg"  
            ],  
        },  
    ],  
    "goodsOriginInfo": {//Other parameters already associated with the product.  
        "originRegion1": "Albania",  
        "agreeDefaultOriginRegion": False  
    }  
}
```

#### 

**bg.local.goods.partial.update**

```
{  
    "goodsId": 604284632545419,  
    "goodsBasic": {  
        "goodsName": "kaiping quanliang gengxin "  
    },  
    "goodsProperty": {  
        "goodsProperties": [  
            {  
                "value": "black",  
                "parentSpecId": "1001",  
                "specId": 72260020, //The specId used for the additional SKU  
            },  
        ],  
    },  
    "skuList": [//This is a partial update API, so only the data for the SKUs to be added is passed; existing SKUs do not need to be sent again.  
        {//This struct is for an additional SKU, so skuId is not provided; instead, basePrice, quantity, and specIdList are passed in.  
            "basePrice": {  
                "amount": "3",  
                "currency": "EUR"  
            },  
            "listPrice": {  
                "amount": "100",  
                "currency": "EUR"  
            },  
            "listPriceType": 0,  
            "quantity": 90,  
            "specIdList": [72260020],  
            "weight": "2",  
            "weightUnit": "g",  
            "length": "2",  
            "width": "2",  
            "height": "2",  
            "volumeUnit": "cm",  
            "images": [  
                "https://img-eu.kwcdn.com/local-goods-img/*********.jpg"  
            ],  
        },  
    ],  
},
```
