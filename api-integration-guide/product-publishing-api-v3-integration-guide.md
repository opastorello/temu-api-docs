# Product Publishing API V3 Integration Guide

## 

**Interface Details**

**Interface Name:** [temu.local.goods.v3.add](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=419748d505a3483f8d210d978cb813f8)

**Request:**

- 

1. 

1. 

- 

  - 

1. 

1. 

1. 

1. 

  - 

1. 

1. 

1. 

  - 

1. 

1. 

1. 

1. 

``

  - 

1. 

1. 

  - 

1. 

````

  - 

1. 

````

  - 

  - 

- 

1. 

1. 

````

  - 

1. 

1. 

  - 

1. 

1. 

1. 

- 

1. 

  - 

1. 

1. 

1. 

1. 

  - 

1. 

1. 

````

  - 

1. 

1. 

[](https://partner.temu.com/documentation?menu_code=38e79b35d2cb463d85619c1c786dd303&sub_menu_code=2cc05ca389ca4eeb8e704e903ebcc6bd)

1. 

    - 

      - 

      - 

    - 

      - 

      - 

  - 

1. 

1. 

``

  - 

1. 

1. 

``

1. 

``

    - 

1. 

1. 

``****

    - 

1. 

1. 

``****

    - 

1. 

1. 

``****

    - 

1. 

1. 

``****

  - 

1. 

1. 

````

    - 

1. 

    - 

1. 

  - 

    - 

1. 

    - 

1. 

1. 

1. 

  1. 

  1. 

1. 

  - 

1. 

    - 

      - 

1. 

1. 

      - 

1. 

    - 

1. 

| PropertiesCollapse | Type | Required | Field Constraints | Interface Field Optimization |
|---|---|---|---|---|
| request | OBJECT | False |  |  |
| language | OBJECT | False | For strings such as title, description, attribute values, and variation values, the system will prioritize the language provided by the ERP.If no language is provided, the system will automatically detect and determine the language. |  |
| goodsBasic | OBJECT | False |  |  |
| externalGoodsId | STRING | True | Maximum length: 128 characters.External product identifier used to associate product data between Temu and the ERP.Required. Requests without this field will be rejected.Within the same store, multiple products cannot share the same identifier. |  |
| goodsName | STRING | True | Maximum length: 500 characters. Excess content will be truncated.Rich text tags will be automatically removed while preserving the text content.Emoji and other special characters will be automatically filtered out. |  |
| extCatName | STRING | False | Maximum length: 500 characters. Excess content will be truncated.Providing this field helps the system assign a more suitable category.Rich text tags will be automatically removed while preserving the text content.Emoji and other special characters will be automatically filtered out. | No need to call the bg.local.goods.cats.get API to retrieve the Temu category tree.Simply provide the category name used in your ERP or external platform, and the system will automatically recommend the most suitable Temu category. |
| goodsDesc | STRING | False | Maximum length: 10,000 characters. Excess content will be truncated.Rich text formatting is supported. |  |
| goodsCarouselImage | STRING[] | False | Up to 10 images are supported. Additional images will be automatically discarded. | No need to call the bg.local.goods.image.upload or temu.local.goods.image.v2.upload APIs to upload images.The system will automatically download and store images from the provided URLs. |
| detailImage | STRING[] | False | Up to 50 images are supported. Additional images will be automatically discarded. | No need to call the bg.local.goods.image.upload or temu.local.goods.image.v2.upload APIs to upload images.The system will automatically download and store images from the provided URLs. |
| productType | INTEGER | False | Product type, supporting optional enumeration values:1: Normal2: Custom3: MTO4: Second-handWhen no product type is declared, the default product type for non-second-hand stores is "Normal," while the default product type for second-hand stores is "Second-hand." |  |
| shipmentLimitDay | INTEGER | False | If no "shipmentLimitDay" is set when shipping, the maximum number of days will be automatically filled in based on the product type. |  |
| attributes | OBJECT[] | False | Used for various product information such as material, battery type, manufacturer, etc.Up to 200 attributes are supported. | No need to call the bg.local.goods.template.get or temu.local.product.attributes.get APIs to retrieve Temu attribute definitions.Simply provide the variation attribute types and values used on the external platform. |
| name | STRING | False | Maximum length: 128 characters.Rich text and special characters are not supported. |  |
| value | STRING[] | False | Maximum length: 128 characters.Rich text and special characters are not supported.Each attribute can contain up to 1,000 values. |  |
| skuList | OBJECT[] | True | Up to 500 SKUs are supported per product. |  |
| externalSkuId | STRING | True | Maximum length: 128 characters.External SKU identifier used to associate SKU data between Temu and the ERP.Required. Requests without this field will be rejected.Within the same store, multiple SKUs cannot share the same identifier. |  |
| images | STRING[] | True | Up to 10 images are supported. Additional images will be automatically discarded.Required. Requests without this field will be rejected. | No need to call the bg.local.goods.image.upload or temu.local.goods.image.v2.upload APIs to upload images.The system will automatically download and store images from the provided URLs. |
| price | OBJECT | True | Required. Requests without this field will be rejected.Decimal precision and currency requirements vary by site. Please refer to: Product Differences in site currency, volume.Requests will be rejected if the amount precision, minimum/maximum value, or currency does not meet site requirements. |  |
| basePrice | OBJECT | True |  |  |
| amount | STRING | True |  |  |
| currency | STRING | True |  |  |
| listPrice | OBJECT | False |  |  |
| amount | STRING | False |  |  |
| currency | STRING | False |  |  |
| quantity | LONG | True | Required.If inventory is not provided, the system will automatically set it to 0. |  |
| packageInfo | OBJECT | True | If dimensions or weight are not provided, default values will be applied automatically.If the provided values exceed Temu's supported range, they will be discarded and replaced with default values (for example, if the submitted value is 0).Values will be rounded according to the required precision. If the rounded value exceeds Temu's limits, it will be discarded and replaced with default values (for example, if the rounded value becomes 0.0). |  |
| weight | STRING | True | Provide numeric values only; do not include units.If the value is 0, the default value of 100 g will be used. |  |
| length | STRING | True | Provide numeric values only; do not include units.If the value is 0, the default value of 10 cm will be used. |  |
| width | STRING | True | Provide numeric values only; do not include units.If the value is 0, the default value of 20 cm will be used. |  |
| height | STRING | True | Provide numeric values only; do not include units.If the value is 0, the default value of 30 cm will be used. |  |
| variations | OBJECT[] | True | Used to define the differences between SKUs.Up to 5 variation attributes are supported per SKU. | No need to call the bg.local.goods.template.get or temu.local.product.variation.get APIs to retrieve Temu variation definitions.Simply provide the variation attribute types and values used on the external platform. |
| Name | STRING | True | Maximum length: 128 characters. |  |
| value | STRING | True | Maximum length: 128 characters. |  |
| barCode | OBJECT |  |  |  |
| barCodeType | STRING | False | Barcode Information. Supported barcode types: EAN, UPC, ISBN, and GTIN-14. |  |
| barCodeId | STRING[] | False | Multiple ISBNs can be provided.For all other barcode types, if multiple codes are provided, only the first one will be saved.If the barcode does not meet platform requirements:For non-book categories, the barcode will be discarded.For book categories, the product draft will be saved, but the ISBN field will remain empty.If the barcode type does not match the provided type, the system will automatically correct the type based on the barcode value. |  |
| References | OBJECT | False | Used to store external product reference information. |  |
| code | OBJECT | False |  |  |
| name | STRING | False | Maximum length: 128 characters.ASIN values are supported. |  |
| id | STRING | False | Maximum length: 128 characters. |  |
| note | STRING[] | False | Can be used to provide any additional product remarks or notes. |  |

Response

- 

- 

- 

- 

  - 

  - 

| Properties | Type | Description |
|---|---|---|
| response | OBJECT |  |
| success | BOOLEAN | success |
| errorCode | INTEGER | error code |
| errorMsg | STRING | error message |
| result | OBJECT |  |
| goodsId | LONG | goodsId |
| externalGoodsId | LONG | external Goods Id |

## 

API Calling Guide

1. 
#### 

Required Fields

When creating a product, the following fields are required. The API request will fail if any required field is missing:

- 

`externalGoodsId`

- 

`goodsName`

- 

`externalSkuId`

- 

`images`

- 

`basePrice`

1. 
#### 

Product Types

Temu supports product types:

- 

Normal Products

- 

Customized Products

- 

Made-To-Order (MTO) Products

- 

Second-hand Products

You can declare the product type used for the product in the productType field.

Please note: 

- 

If the store is not a secondhand store and the product type is not declared when listing the product, the system will default to "Normal Products". 

- 

If the store is a secondhand store and the product type is not declared when listing the product, the system will default to "Secondhand Products".

1. 
#### 

Condition of second-hand goods

- 

All secondhand condition information is passed through the `attributes` field, which is an array where each element has a structure of `{ "name": "xxx", "value": "yyy" }`.

```
{  
  "attributes": [  
    { "name": "Second-hand type", "value": "regular | collectible | luxury" },  
    { "name": "Condition", "value": "Like New | Very Good | Good | Acceptable | Open Box" },  
    { "name": "Grading Company", "value": "PSA | BGS | SGC | CGC" },  
    { "name": "Grade", "value": "1 ~ 10（Contains 0.5）| Authentic | Authentic altered" }  
  ]  
}
```

- 

All types of second-hand  goods support the use of condition descriptions to declare the condition of the second-hand goods. The supported conditions for each type of second-hand goods are as follows:

- 

- 

- 

- 

- 

```
  
  
  
  
  
  
  
  
  
  
  

```

- 

- 

- 

- 

```
  
  
  
  
  
  
  
  
  
  
  

```

- 

- 

- 

- 

```
  
  
  
  
  
  
  
  
  
  
  

```

| Second-hand type | Using condition description | case |
|---|---|---|
| name: Second-hand typevalue: regular | name: Conditionvalue:Like NewVery GoodGoodAcceptableOpen BoxChoose one of five secondhand conditions. | {    "attributes": [        {            "name": "Second-hand type",            "value": "regular"        },        {            "name": "Condition",            "value": "Like New"        }    ]} |
| name: Second-hand typevalue: collectible | name: Conditionvalue:Like NewVery GoodGoodAcceptableChoose one of four secondhand conditions. | {    "attributes": [        {            "name": "Second-hand type",            "value": "collectible"        },        {            "name": "Condition",            "value": "Very Good"        }    ]} |
| name: Second-hand typevalue: luxury | name: Conditionvalue:Like NewVery GoodGoodAcceptableChoose one of four secondhand conditions. | {    "attributes": [        {            "name": "Second-hand type",            "value": "luxury"        },        {            "name": "Condition",            "value": "Good"        }    ]} |

- 

If you do not wish to use Condition's standards and instead intend to use the standards of an Grading Companies' grade, please send your request according to the following structure. Please note: Grading Companies' grade standards are only supported when the secondhand item is a collectible.

  - 

When submitting ratings from both TEMU and external agencies for second-hand collectibles, the external agencies' rating will be used first.

  - 

If multiple Grading Companies and their corresponding grades are provided, the system will default to using the first company and its corresponding rating.

- 

- 

- 

- 

- 

```
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

```

| Second-hand type | Supported Grading Companies | Grading Companies' available ratings |  |
|---|---|---|---|
| name: Second-hand typevalue: collectible | name: Grading Companyvalue:PSABGSSGCCGCChoose one of the four external agencies. | name: Gradevalue:1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, Authentic, Authentic alteredChoose one from the above grades.All Grading Companies use the same grading criteria. | {    "attributes": [        {            "name": "Second-hand type",            "value": "collectible"        },        {            "name": "Grading Company",            "value": "PSA"        },        {            "name": "Grade",            "value": "9.5"        }    ]} |

1. 
#### 

Post-Product Creation Process

When the API request is successfully executed:

3.1 Retrieve Product IDs

The response will return the following fields:

- 

`goodsId` generated by the Temu platform

- 

`externalGoodsId` provided by the merchant

It is recommended that merchants maintain a mapping between these two IDs in their own system to facilitate subsequent product management and status queries.

> 

**Note:** The returned `goodsId` only indicates successful product creation, and does not imply that the product meets publication requirements.

3.2 Automatic Product Information Enrichment

After product creation, the system will automatically process the submitted data, including but not limited to:

- 

Category recognition and assignment

- 

Product attribute enrichment

- 

SKU generation

- 

Other necessary processing for publication

3.3 Query Product Processing Status

After receiving the `goodsId`, it is recommended to wait approximately 10 minutes before querying the product status via the following APIs:

- 

[`bg.local.goods.list.query`](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=6bf4cb321e7c478c8dcb7d40f724c4e5)

- 

[`temu.local.goods.list.retrieve`](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=ce4883149f784c208e1b9a52566ea2c8)

The possible product statuses are as follows:

| Product Status | Description |
|---|---|
| Draft | The product information is incomplete and cannot be submitted for publication. |
| Incomplete | The product information is complete and has been automatically submitted for review. The system is waiting for the platform’s review result. |

#### 

1. 
#### 

Common Reasons Why Products Remain in “Draft” Status

If a product cannot be automatically submitted for publication, it will remain in **Draft** status. Common reasons include:

4.1 Missing Required Attributes

Required attributes defined by the product’s category are not provided.

For example:

The system identifies that the category requires the **“Voltage”** attribute, but this attribute is not included in the product information.

4.2 Image Processing Failure

The system is unable to download or process product images. Common causes include:

- 

Restricted access to the image hosting server

- 

Rate limiting on the image storage service

- 

Incorrect image URL configuration

- 

Expired or invalid image links

- 

Image file size too large, causing download timeout

4.3 Duplicate Product Identifiers

The product ID conflicts with an existing product in the store, including:

- 

Duplicate `externalGoodsId`

- 

Duplicate `externalSkuId`

This is relatively rare, but may still prevent the product from being automatically submitted for publication.

## 

How to Effectively Use the Product Add API V3

1. 

1. 

1. 

1. 

1. 

1. 

1. 

```
  
  
  
  
  
  
  
  
  
  
  
  
  

```

![image](https://bstatic.kwcdn.com/open-outer/217a7c4554/68bf3bcf1a3d046b5ee3e9967f4f4dca.png)

```
  
  
  
  
  
  
  
  

```

![image](https://bstatic.kwcdn.com/open-outer/217a7c4554/da781938f23bf4d31361e25222dc3221.png)

```
  
  
  
  
  
  
  

```

![image](https://bstatic.kwcdn.com/open-outer/217a7c4554/c86e4e2d6cfd769844b9237b32fb9279.png)

```
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

```

![image](https://bstatic.kwcdn.com/open-outer/217a7c4554/50d0d3d84126d8769a0d9a28a92177be.png)

```
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

```

![image](https://bstatic.kwcdn.com/open-outer/217a7c4554/5e872d5428456a24408c9aaa124576a8.png)

```
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

```

![image](https://bstatic.kwcdn.com/open-outer/217a7c4554/cc66174ec0343b53fb9283a15575b53d.png)

1. 

1. 

```
  
  
  
  
  
  
  
  
  
  
  

```

- 

****

- 

****

- 

****

![image](https://bstatic.kwcdn.com/open-outer/217a7c4554/9c2cf4be3dcdea7cd825ff45b1bf0eab.png)

``

![image](https://bstatic.kwcdn.com/open-outer/217a7c4554/f718d7b84c846ace488247b1aa64bc69.png)

```
  
  
  
  

```

| Product Content | Expected Objective |  |
|---|---|---|
| Basic Product Information | Providing complete basic product information helps better identify and enrich the following fields:CategoryAttributesBrandSpecificationsNet content and other related informationProduct TypeShipment limit day | "goodsBasic": {        "goodsName": "test XXX",        "externalGoodsId": "goodssn0610003",        "goodsDesc": "XXXXX",        "extCatName": "lm Office Products / Office & School Supplies / Tape, Adhesives & Fasteners / Tape / Packaging Tape",        "goodsCarouselImage": [            "https://s11.aconvert.com/convert/p3r68-cdx67/dopcc-dtvgs.jpg"        ],        "detailImage": [            "https://s11.aconvert.com/convert/p3r68-cdx67/yr4eb-v8em1.jpg"        ]        "productType": 1,        "shipmentLimitDay": 2    }, |
| Custom product | Customized product can be shipped with a longer "shipment limit day". | {    "type": "temu.local.goods.v3.add",    "goodsBasic": {        "goodsName": "3 Office Products / Office & School Supplies / Tape, Adhesives & Fasteners / Tape / Packaging Tape",        "externalGoodsId": "07081621",        "productType": 2,        "shipmentLimitDay": 3    },} |
| Made-To-Order (MTO) Products | The "shipmentLimitDay" for MTO products is related to the time the seller applied and the maximum time allowed by the category. | {    "type": "temu.local.goods.v3.add",    "goodsBasic": {        "goodsName": "3 Office Products / Office & School Supplies / Tape, Adhesives & Fasteners / Tape / Packaging Tape",        "externalGoodsId": "07081624",        "productType": 3    },} |
| Second-hand products | Listing second-hand goods while choosing the best appropriate condition | {    "type": "temu.local.goods.v3.add",    "goodsBasic": {        "goodsName": "3 Office Products / Office & School Supplies / Tape, Adhesives & Fasteners / Tape / Packaging Tape",        "externalGoodsId": "07081624",        "productType": 4    },    "attributes": [        {            "name": "Second-hand type",            "value": ["regular"]        },        {            "name": "condition",            "value": ["good"]        }    ],} |
| Second-hand collectibles products | Listing second-hand collectibles while also using external agency ratings | {    "type": "temu.local.goods.v3.add",    "goodsBasic": {        "goodsName": "Toys & Games / Games & Accessories / Card Games / Collectible Card Games / Decks & Sets",        "externalGoodsId": "07082204",        "productType": 4    },    "attributes": [        {            "name": "Second-hand type",            "value": ["collectible"]        },        {            "name": "Grading Company",            "value": ["PSA"]        },        {            "name": "Grade",            "value": ["Authentic"]        }    ],} |
| Product Attribute Information | Only need to submit product attribute information used on external platforms.Complete attribute data helps the system better enrich and map required Temu platform attributes. | {    "attributes": [        {            "name": "Power Mode",            "value": [                "Power Supply"            ]        },        {            "name": "Operating Voltage",            "value": [                "100V"            ]        },        {            "name": "Plug Type",            "value": [                "Type A Plug Socket (US Two-pin)"            ]        },        {            "name": "Battery Properties",            "value": [                "Rechargeable Battery"            ]        },        {            "name": "Operating System",            "value": [                "Android"            ]        },        {            "name": "Cellular Technology",            "value": [                "2g"            ]        },        {            "name": "Wireless Property",            "value": [                "With Wi-Fi function"            ]        },        {            "name": "SIM Card Slot Count",            "value": [                "0"            ]        }    ],} |
| Product Specification Information | You only need to provide the specification information used on external platforms. Even if the submitted specifications do not fully match Temu’s requirements, the system will automatically process and normalize them.Examples:If only size is provided but Temu requires color as well, the system will automatically fill in “color: as shown”If multiple specifications are provided (e.g. “size: XL, “color: re, quantity: 2“) and Temu only allows up to two specification dimensions per SKU, the system will automatically perform a cross-combination to normalize them into valid SKU structures. | {    "skuList": [        {            "variations": [                {                    "name": "Color",                    "value": "red"                }            ]        }    ]} |
| Product Service Information | This section does not require merchant input. The system will automatically populate default values. | Fulfillment Time: 2 daysFulfillment Method: Merchant shippingShipping Template: Default shipping template under the store |
| Product Identifier | The system will use externalSkuId as the default product identifier. No additional input is required. |  |
| Compliance Attributes / Manufacturer Information | Compliance attributes and manufacturer information will be automatically extracted based on the product title, description, and attributes provided by the merchant. | "goodsBasic": {        "goodsName": "test XXX",        "externalGoodsId": "goodssn0610003",        "goodsDesc": "age:5 years+. Overview Details Content: High-quality medical skin care for sensitive skin. Cream for application on the skin. Dermocosmetic from the pharmacy. Manufacturer: Shenzhen Zhilian Shengya Electronic Technology Co., Ltd. Germany (Original product from Germany). PZN: 08712740, PZN: 8712740. Product properties: for dry and very dry skin, intensely replenishing lipids - provides moisture for 24 hours, makes the skin noticeably smooth and supple. For the natural regeneration of the skin. Balneum Intensiv Creme was specifically developed to maintain the natural protective function of dry and very dry skin. The cream contains substances naturally present in the skin: urea, ceramides, and physiological lipids (3 in) - which may be reduced in dry skin. Free from dyes, fragrances, and preservatives (3 out), therefore particularly skin-friendly. In this way, the fat and moisture content of the skin is regulated and the natural skin barrier function is maintained. The rich cream provides moisture for 24 hours and thus protects it from further moisture loss. Feelings of tightness disappear, the skin becomes noticeably smooth and supple. Recommended by dermatologists. Clinically tested efficacy. Composition according to INCI: Aqua, Glycine Soja, Propylene Glycol, Cetearyl Alcohol, Paraffinum Liquidum, Urea, Isohexadecane, Sodium Lactate, PEG-20 Stearate, Lactic Acid, Polysorbate 60, Squalane, Stearic Acid, Ceramide 3, Lecithin, Tocopherol, Ascorbyl Palmitate, Hydrogenated Palm Glycerides Citrate, Disodium EDTA. Source: Information from the packaging. Status: 04/2017",    } |

## 

Product Add V3 API – Full Request Example

```
{  
    "goodsBasic": {  
        "goodsName": "3 Office Products / Office & School Supplies / Tape, Adhesives & Fasteners / Tape / Packaging Tape",  
        "externalGoodsId": "goodssn0610003",  
        "goodsDesc": "ms Office Products / Office & School Supplies / Tape, Adhesives & Fasteners / Tape / Packaging Tape",  
        "extCatName": "lm Office Products / Office & School Supplies / Tape, Adhesives & Fasteners / Tape / Packaging Tape",  
        "goodsCarouselImage": [  
            "https://s11.aconvert.com/convert/p3r68-cdx67/dopcc-dtvgs.jpg"  
        ],  
        "detailImage": [  
            "https://s11.aconvert.com/convert/p3r68-cdx67/yr4eb-v8em1.jpg"  
        ]  
    },  
    "skuList": [  
        {  
            "price": {  
                "basePrice": {  
                    "amount": "1000",  
                    "currency": "JPY"  
                },  
                "listPrice": {  
                    "amount": "2000",  
                    "currency": "JPY"  
                }  
            },  
            "images": [  
                "https://s11.aconvert.com/convert/p3r68-cdx67/3a9gb-wqj8e.jpg"  
            ],  
            "externalSkuId": "skusn0610003",  
            "variations": [  
                {  
                    "name": "Color",  
                    "value": "red"  
                }  
            ],  
            "quantity": 100,  
            "packageInfo": {  
                "weight": "22",  
                "length": "33",  
                "width": "44",  
                "height": "55"  
            },  
            "barCode": {  
                "barCodeType": "EAN",  
                "barCodeId": [  
                    "0123456789012"  
                ]  
            },  
            "references": {  
                "code": {  
                    "name": "asin123",  
                    "id": "123"  
                },  
                "note": [  
                    "www.baidu.com"  
                ]  
            }  
        }  
    ]  
}  
---------------------------------------------------------------------------------------------------------------------------------  
{  
    "result": {  
        "goodsId": 608573962731830,  
        "externalGoodsId": "goodssn0610003"  
    },  
    "success": true,  
    "requestId": "gl-42bbc01d-b4bb-4366-bf93-5ac3e5f9ef8a",  
    "errorCode": 1000000,  
    "errorMsg": ""  
}
```
