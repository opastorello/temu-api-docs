# Product Publishing API V3 Integration Guide

## 

**Interface Details**

**Interface Name:** temu.local.goods.v3.add

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

Unsupported Product Types

The following product types are not supported by this API:

- 

Customized Products

- 

Made-To-Order (MTO) Products

- 

Used Products

If any of the above product types are submitted, they will be treated as standard products by the system.

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

`bg.local.goods.list.query`

- 

`temu.local.goods.list.retrieve`

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

```
  
  
  
  
  
  
  
  
  
  
  

```

- 

****

- 

****

- 

****

![image](https://bstatic.kwcdn.com/open-outer/2123a60000/dc8502cf60d7debcec19bccdded6d5bf)

![image](https://bstatic.kwcdn.com/open-outer/2123a60000/521dd68763a58209631c9392d6e725e3)

```
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

```

![image](https://bstatic.kwcdn.com/open-outer/2123a60000/4ce00e20b9a43bbf29b9046f4c309bf5)

1. 

1. 

```
  
  
  
  
  
  
  
  
  
  
  

```

``

![image](https://bstatic.kwcdn.com/open-outer/2123a60000/39622056f66ce7387c4b6e94d50bd368)

```
  
  
  
  

```

| Product Content | Expected Objective |  |
|---|---|---|
| Basic Product Information | Providing complete basic product information helps better identify and enrich the following fields:CategoryAttributesBrandSpecificationsNet content and other related information | "goodsBasic": {        "goodsName": "test XXX",        "externalGoodsId": "goodssn0610003",        "goodsDesc": "XXXXX",        "extCatName": "lm Office Products / Office & School Supplies / Tape, Adhesives & Fasteners / Tape / Packaging Tape",        "goodsCarouselImage": [            "https://s11.aconvert.com/convert/p3r68-cdx67/dopcc-dtvgs.jpg"        ],        "detailImage": [            "https://s11.aconvert.com/convert/p3r68-cdx67/yr4eb-v8em1.jpg"        ]    }, |
| Product Service Information | This section does not require merchant input. The system will automatically populate default values. | Fulfillment Time: 2 daysFulfillment Method: Merchant shippingShipping Template: Default shipping template under the store |
| Product Attribute Information | Only need to submit product attribute information used on external platforms.Complete attribute data helps the system better enrich and map required Temu platform attributes. | {    "attributes": [        {            "name": "Power Mode",            "value": [                "Power Supply"            ]        },        {            "name": "Operating Voltage",            "value": [                "100V"            ]        },        {            "name": "Plug Type",            "value": [                "Type A Plug Socket (US Two-pin)"            ]        },        {            "name": "Battery Properties",            "value": [                "Rechargeable Battery"            ]        },        {            "name": "Operating System",            "value": [                "Android"            ]        },        {            "name": "Cellular Technology",            "value": [                "2g"            ]        },        {            "name": "Wireless Property",            "value": [                "With Wi-Fi function"            ]        },        {            "name": "SIM Card Slot Count",            "value": [                "0"            ]        }    ],} |
| Product Specification Information | You only need to provide the specification information used on external platforms. Even if the submitted specifications do not fully match Temu’s requirements, the system will automatically process and normalize them.Examples:If only size is provided but Temu requires color as well, the system will automatically fill in “color: as shown”If multiple specifications are provided (e.g. “size: XL, “color: re, quantity: 2“) and Temu only allows up to two specification dimensions per SKU, the system will automatically perform a cross-combination to normalize them into valid SKU structures. | {    "skuList": [        {            "variations": [                {                    "name": "Color",                    "value": "red"                }            ]        }    ]} |
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
