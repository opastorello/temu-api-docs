# Add Products Guide V2.0

**Last update:** 2026-02-08 06:21:27

---

## 
**Product Upload API Call Process**

### 
**Overview:**

### 
**Minimum Viable Integration**

#### 
**1.Product identity**

 

| 

Properties
 | 

Required
 | 

How to fill in
 | 

Precautions
 | 

 
| 

goodsBasic
 | 

True
 | 

-
 | 

 | 

 
| 

-goodsName
 | 

True
 | 

User inputs
 | 

Validation Rules:

- 
Only supports English letters, numbers, and symbols.

- 
Does not support decorative characters: ~ ! * $ ? _ ~ { } # < > | * ; ^ ¬ ¦

- 
Does not support high ASCII characters type 1, such as ®, ©, ™, etc.

- 
Character count: Within 500 characters.

temu.local.goods.illegal.vocabulary.check

Please note that it is recommended to use this interface to check for any violations in product information to avoid affecting sales
 | 

 
 
| 

-catId
 | 

True
 | 

Retrieve from other APIs

[bg.local.goods.cats.get](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=b49f03d2b1744700ab762b9fe80d1af7)

This api  [bg.local.goods.category.recommend](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=244c900c28ee4c16b3e7cc88296f74d9) will help you quickly match temu categories based on product information

 | 

[bg.local.goods.cats.get](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=b49f03d2b1744700ab762b9fe80d1af7)

- 
Entering `parentCatId`=0 retrieves all available first-level categories for posting.

- 
To obtain leaf categories: Recursively call this interface, entering `parentCatId` with the `catId` selected from the previous call's results to get the next level of category ID until the leaf categories are reached.

- 
When entering a leaf category, the interface returns empty.

Important

- 
Ensure to use the most specific (leaf) category ID for posting products; you must keep calling the aforementioned interface until the most specific category is obtained.

- 
`catType` is an important varibale for judgement whether category is an Apparel (`catType=0`) or Non-Apparel(`catType=1`) one, it will effect at the image required shape.

- 
Some categories on different sites are not sellable, only the categories with availableStatus=0 need to be obtained

 | 

 
 

#### 
**2.Attributes**

- 
**Product attributes: **Divided into required attributes and optional attributes;

- 
Required attributes are important product attributes and can help buyers get a better understanding of the product. Please ensure that all required attributes are passed in goodsProperty.

- 
Optional attributes can enhance the product description. You can choose to pass them in, but it is recommended to fill in as many optional attributes as possible.

Different category have different required attributes.

 

| 

Properties
 | 

Required
 | 

How to fill in
 | 

Precautions
 
| 

goodsProperty
 | 

False
 | 

Retrieve from other APIs:

[temu.local.product.attributes.get](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=06587aa615384310a1bac727aa82b64d)
 | 

-Please note:

Required attributes must be passed in, judging by **temu.local.product.attributes.get -  required=True**

- 
Child attribute information

When you select a parent attribute value, the available child attributes and the selectable values for those child attributes are determined by the selected parent value.

Even if the same child attribute appears under different parent attribute values, the range of selectable child attribute values may differ.

- 
Control Types

**0 – Input only: **Users can only enter a value manually.

**1 – Selection only: **Users can only choose from predefined options.

**5 – Single date (YYYY-MM-DD): **Date format with year, month, and day; When publishing a product, the value should be sent as `**YYYY-MM-DD**`.

**6 – Date range (YYYY-MM-DD,YYYY-MM-DD): **Date format with year, month, and day, including both a start date and an end date.

**7 – Single month (YYYY-MM): **Month format with year and month; When publishing a product, the value should be sent as `**YYYY-MM**`.

**8 – Month range (YYYY-MM,YYYY-MM): **Month format with year and month, including both a start month and an end month.

**16 – Input and selection required: **Users must both enter a value and select an option.

**19 – Input or selection (either one): **Users can choose **either** to enter a value **or** select an option.
 

#### 
**3.Variations **

- 
**Variation:** You must set either 1 or 2 variations for each SKU. It is used for buyers to choose from.

Different category have different variations.

| 

Properties
 | 

Required
 | 

How to fill in
 | 

Precautions
 
| 

-specDetails

 | 

True
 | 

User inputs & Retrieve from other APIs: [**temu.local.product.variation.get**](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=4d45e366dcd34dbf9b0fb8c4d27bd146)
 | 

This is a field used to distinguish variants, such as color, size, etc. Please note that there are two ways to set this information for different categories on the platform. 

Please note:

**temu.local.product.variation.get****.[variationType]**: 

0 - Only preset values ​​can be selected

1 - Custom input specifications can be selected;

2 - Both preset and custom input specifications can be selected.

variationType 0: Only specId is required in specDetails

variationType 1: Required parentspecId(variation type) and Value(User input to custom their only variatns) in specDetails

variationType 2: Either follow variationType 0 or 1
 

#### 
**4.Add Product SKUs**

**SKU**: Can be used for sellers' internal inventory management and must be unique within the store. 

 

| 

Properties
 | 

Required
 | 

How to fill in
 | 

Precautions
 
| 

skuList
 | 

True
 | 

User inputs & Retrieve from other APIs
 | 

List of SKUs. There must be at least one SKU.
 
| 

-basePrice
 | 

True
 | 

User inputs
 | 

Different sites have corresponding requirements for currency information, [please refer to this document for details](https://partner.temu.com/documentation?menu_code=38e79b35d2cb463d85619c1c786dd303&sub_menu_code=2cc05ca389ca4eeb8e704e903ebcc6bd)
 
| 

-quantity
 | 

True
 | 

User inputs
 | 

This is the inventory information corresponding to the product, with a setting range of** [0, 999999]**
 
| 

-weight
 | 

True
 | 

User inputs
 | 

Product Package Information.
 
| 

-length
 | 

True
 | 

User inputs
 | 

Product Package Information.
 
| 

-width
 | 

True
 | 

User inputs
 | 

Product Package Information.
 
| 

-height
 | 

True
 | 

User inputs
 | 

Product Package Information.
 
| 

-images
 | 

True
 | 

User inputs
 | 

Identify whether it belongs to the clothing category through the [bg.local.goods.cats.get](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=b49f03d2b1744700ab762b9fe80d1af7)-catType, as different types have differences in size ratios

- 
**Apparel Carousel Images**

Aspect Ratio: 3:4

Width:≥1340px

Height: ≥1785px

- 
**Non-Apparel Carousel Images**

Aspect Ratio: 1:1

Width:≥800px

Height: ≥800px

-Size：≤3 MB

-Format: jpeg, jpg, png

It is necessary to upload the images to TEMU in advance, and using [bg.local.goods.image.upload](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=2760e68837bc4716b0208e624558d0f4) will facilitate users to handle the corresponding image proportions and sizes in a portable manner
 

#### 
**5.Offer **

- 
Handling time: The number of days from when you receive an order to when it can be shipped. Example: 0.5 working days.

- 
Shipping template: A corresponding shipping template must be selected before the product can be listed. Click Add shipping template if there isn't one available for use.

- 
Fulfillment channel: Self-delivery is selected by default

 

| 

Properties
 | 

Required
 | 

How to fill in
 | 

Precautions
 
| 

 | 

 | 

 | 

 
| 

-costTemplateId
 | 

True
 | 

Retrieve from other APIs

[bg.freight.template.list.query](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=01a44ea6e787400fbd375947e4012ddb)
 | 

 

Users need to go to the seller center to create the shipping template page in order for this interface to return the corresponding data
 
| 

-shipmentLimitDay  
 | 

True
 | 

User inputs
 | 

Indicates the time, in days, between when you receive an order for an item and when you can ship the item. The default production time is **1 or 2.**
 
| 

-importDesignation

 | 

True
 | 

User inputs
 | 

Only for **USA**.

If made in USA from imported materials select Made in USA and Imported. If some units are from USA and some imported select Made in USA or Imported. If made in USA from Mexican materials select Made in USA. If made outside USA, select Imported.

The code provided by the platform to providers for marking and managing parent product links, filled in by the merchant.
 

### 
**Examples:**

- 
#### 
Add a product with selectable Parent-child attribtues

Add a prodcut:

```
{
    "type": "temu.local.goods.v2.add",
    "goodsBasic": {
        "catId": 24318,
        "goodsName": "packaging tape"
    },
    "goodsServicePromise": {
        "shipmentLimitDay": 1,
        "costTemplateId": "LFT-13630901943132180183"
    },
    "goodsProperty": [
        {
            "refPid": 12,
            "vid": 410
        },
        {
            "refPid": 7317,
            "vid": 213321
        },
        {
            "refPid": 7318,
            "vid": 213604
        }
    ],
    "skuList": [
        {
            "price": {
                "basePrice": {
                    "amount": "23.00",
                    "currency": "EUR"
                }
            },
            "quantity": 12,
            "images": [
                "https://img-eu.kwcdn.com/local-goods-img/212a0c692c/6269cd57-f203-4ba8-bdfb-e80138e197ea_800x800.jpeg.format.jpg"
            ],
            "specDetails": [
                {
                    "specId": "102793830",
                    "parentSpecId": "1001"
                }
            ],
            "packageInfo": {
                "weight": "2",
                "length": "2",
                "width": "32",
                "height": "2"
            }
        }
    ]
}
```

```
{
    "result": {
        "goodsId": 603940749967715,
        "skuInfoList": [
            {
                "specList": [
                    {
                        "specId": 102793830,
                        "specName": "spec name",
                        "parentSpecId": 1001
                    }
                ],
                "outSkuSn": "",
                "skuId": 53207933914717
            }
        ],
        "productType": 1
    },
    "success": true,
    "requestId": "eu-e42531ac-a77c-4f06-8013-cf847cd7b86c",
    "errorCode": 1000000,
    "errorMsg": ""
}
```

- 
#### 
Add a product with input type attributes

Add a prodcut:

```
{
    "type": "temu.local.goods.v2.add",
    "goodsBasic": {
        "catId": 29073,
        "goodsName": "packaging tape"
    },
    "goodsServicePromise": {
        "shipmentLimitDay": 1,
        "costTemplateId": "LFT-13630901943132180183"
    },
    "goodsProperty": [
        {
            "refPid": 12,
            "vid": 65
        },
        {
            "refPid": 15,
            "vid": 121,
            "numberInputValue": "100",
            "valueUnitId": 57
        },
        {
            "refPid": 6928,
            "vid": 161110
        },
        {
            "refPid": 6934,
            "value": "12",
            "valueUnitId": 240

        },
        {
            "refPid": 6547,
            "vid": 35409,
            "numberInputValue": "100",
            "valueUnitId": 57
        }
    ],
    "goodsSize": {
        "groupId": 2
    },
    "skuList": [
        {
            "price": {
                "basePrice": {
                    "amount": "23.00",
                    "currency": "EUR"
                }
            },
            "quantity": 12,
            "images": [
                "https://img-eu.kwcdn.com/local-goods-img/e71e5e45/5fa9f2e2-44f9-48d3-a22c-5b66f13c3445.jpeg"
            ],
            "specDetails": [
                {
                    "specId": "102793830",
                    "parentSpecId": "1001"
                },
                {
                    "parentSpecId": 3001,
                    "specId": 10002
                }
            ],
            "packageInfo": {
                "weight": "2",
                "length": "2",
                "width": "32",
                "height": "2"
            }
        }
    ]
}
```

```
{
    "result": {
        "goodsId": 604318707083482,
        "skuInfoList": [
            {
                "specList": [
                    {
                        "specId": 102793830,
                        "specName": "spec name",
                        "parentSpecId": 1001
                    },
                    {
                        "specId": 10002,
                        "specName": "XXS",
                        "parentSpecId": 3001
                    }
                ],
                "outSkuSn": "",
                "skuId": 56506468808188
            }
        ],
        "productType": 1
    },
    "success": true,
    "requestId": "eu-90c500e2-dcf0-4bf1-b2f8-50734b55ddf8",
    "errorCode": 1000000,
    "errorMsg": ""
}
```
