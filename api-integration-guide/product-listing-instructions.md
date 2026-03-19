# Product Listing Instructions

# 

Category Query

Query the categories that can be posted in the current store `catId`

Relevant Interface:

`bg.local.goods.cats.get` Product Standard Category Interface

Interface Description

1. 

Entering `parentCatId`=0 retrieves all available first-level categories for posting.

1. 

To obtain leaf categories: Recursively call this interface, entering `parentCatId` with the `catId` selected from the previous call's results to get the next level of category ID until the leaf categories are reached.

  1. 

When entering a leaf category, the interface returns empty.

Important: 

1. 

Ensure to use the most specific (leaf) category ID for posting products; you must keep calling the aforementioned interface until the most specific category is obtained.

1. 

`catType` is an important varibale for judgement whether category is an Apparel (`catType=0`) or Non-Apparel(`catType=1`) one, it will effect at the image required shape.

```
{  
 "goodsCatsList": [  
  {  
   "catId": 32266,  
   "catName": "Pants",  
   "catType": 0,  
   "leaf": true,  
   "level": 6,  
   "parentId": 32263  
  },  
  {  
   "catId": 32267,  
   "catName": "Shirts",  
   "catType": 1,  
   "leaf": false,  
   "level": 6,  
   "parentId": 32263  
  }  
 ]  
}
```

# 

Prepare Product Information

## 

2.1 Prepare Basic Product Information

a. Product Name (`goodsName`): Supports only English, numerals, and common symbols, with a maximum of 500 characters.

b. Product Description (`goodsDesc`): Supports only English, numerals, and common symbols, with a maximum of 10000 characters.

c. Product Highlights (`bulletPoints`): Supports only English, numerals, and common symbols, with a maximum of 700 characters, and up to six points.

## 

2.2 Upload Product Carousel Images/Detail Images/Videos/Certificates and Other Materials

Upload images, videos, and files required for product sales and certificates, sign the materials, and upload the files along with the product creation interface. When adding a new product, include the URLs of images and videos, along with vid.

Relevant Interface:

`bg.local.goods.gallery.signature.get` Get Signature for Uploading Materials

**Step 1: **Call `bg.local.goods.gallery.signature.get` to get a signature for uploading materials, taking note to pass in different `uploadFileType` for different file types.

**Step 2: **Call the multimedia file upload interface, include the signature in the input parameters, and upload the file.

`api/galerie/general_file` for instruction manuals

`api/galerie/general_file` for certification files (less than 20MB)

`api/galerie/cos_large_file/upload_ini`t for initializing large certification file uploads (more than 20MB)

`api/galerie/cos_large_file/upload_part` for chunk upload of large certification files (more than 20MB)

`api/galerie/v1/store_video?sdk_version=js-0.0.32` for videos

`api/galerie/large_file/v1/video/upload_init` for initializing large video uploads

`api/galerie/large_file/v1/video/upload_part` for large video uploads

`api/galerie/large_file/v1/video/upload_complete` for completing large video uploads

`api/galerie/v3/store_image?sdk_version=js-0.0.32` for product images or live photos

Requirements for business materials are as follows:

******

******

******

******

******

******

| Functional module | Material | Dimensions | Size | Type | Note |
|---|---|---|---|---|---|
| Product Description | Detail Video | Duration: ≤180sAspect Ratio: 1:1, 4:3, 16:9Resolution: ≥720P | ≤300 MB | wmv, avi, 3gp, mov, mp4, flv, rmvb, mkv, m4v, x-flv, WMV, AVI, 3GP, MOV, MP4, FLV, RMVB, MKV, M4V, X-FLV | Product Description, Detail Video, Product Images make up the detailed presentation. By default, the video is displayed as the first element of this presentation. |
| Product Images | Quantity: ≤50Aspect Ratio: ≥1:3Width: ≥480pxHeight: ≥480px | ≤3MB | JPEG, JPG, PNG |
| SKU Carousel Images | Apparel Carousel Images | Quantity: 3-10Aspect Ratio: 3:4Width:≥1340pxHeight: ≥1785px | ≤3 MB | JPEG, JPG, PNG | Take the first image of each SKC as the SKC preview image |
| Non-Apparel Carousel Images | Quantity: 3-10Aspect Ratio: 1:1Width:≥800pxHeight: ≥800px | ≤3 MB | JPEG, JPG, PNG | SPU carousel- Take the first image of the first SKU as the first image- Splice the images of each SKU from the second image onwards after the first imageSKU preview image- Take the first image of each SKU as the SKU preview image |
| Product Video | Product Video | Quantity: ≤1Aspect Ratio: Not restrictedDuration: ≤60sResolution: ≥720P | ≤100 MB | wmv, avi, 3gp, mov mp4, flv, rmvb, mkv, m4v, x-flv, WMV, AVI, 3GP, MOV, MP4, FLV, RMVB, MKV, M4V, X-FLV |  |
| Safety and Compliance | Product Actual Images | Quantity: 1-6 | ≤3 MB | JPG, PNG, JPEG |  |
| Product Guides or Documents | Quantity: same as the language requirement | ≤3 MB | JPG, PNG, JPEG |  |

## 

## 

2.3 Query Product Attribute Template and Attribute Compliance Check [Replicated]

Query the required and optional attributes of products to help buyers better understand the merchandise.

Relevant Interfaces:

`bg.local.goods.template.get` Category Product Attribute Template Query Interface

`bg.local.goods.property.compliance.check` Product Attribute Compliance Prohibition Verification Interface

Specific Operations:

Query the category's required attributes and other publishing rules for product release using `bg.local.goods.template.get`.

**Note:** Logic related to the attribute template is completely consistent with the semi-managed. Refer to the semi-managed related functional implementation plan to proceed with development.

1. 

Get the publishing rules for the category through `catId`, currently returning attribute names and values, brands, attribute parent-child relationships, and other rules.

1. 

Retrieve `refPid`, `vid` (no such parameter for input type attribute values), and `value` from return parameters to enter into the `goodsProperties` field of the product upload interface.

1. 

Note: Attributes returned by the interface with `isSale`=`true` are sales attributes (standard attributes), and when entering these types of attributes, combine with the specifications and get the `specId` (specification id) directly from this interface, entering it into both the attribute field `goodsProperties` and the specification field `specIdList` of `skuList` .

  1. 

If there's no data in the templateInfo. `goodsSpecProperties` of the attribute template, you need to select a system predefined specification from `userInputParentSpecList`, and the number of specifications is decided by `inputMaxSpecNum`.

******

******

******

**

```
  
  
  
  
  
  

```

```
  
  
  
  
  
  
  
  

```

**

```
  
  
  
  
  
  

```

``

```
  
  
  
  
  
  

```

**

```
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

```

| ControlType | Description | Property Object Paramters |
|---|---|---|
| 0 | Input type property | {    "templatePid": property['templatePid'],    "refPid": property['refPid'],    "pid": property['pid'],    "vid": 0,    "value": str(random.randint(int(property['minValue']), int(property['maxValue'])))}Note: if value property['valueUnitList'] defined an unit for value{    "templatePid": property['templatePid'],    "refPid": property['refPid'],    "pid": property['pid'],    "vid": 0,    "value": str(random.randint(int(property['minValue']), int(property['maxValue']))),    "valueUnitId": property['valueUnitList'][0]['valueUnitId'],    "valueUnit": property['valueUnitList'][0]['valueUnit']} |
| 1 | Select type property | {    "templatePid": property['templatePid'],    "refPid": property['refPid'],    "pid": property['pid'],    "vid": property['values'][0]['vid'],    "value": property['values'][0]['value']}Note: If property is defined at goodsSpecProperties , you should follow the Sale Property rule, model like that:{    "templatePid": saleProperty['templatePid'],    "refPid": saleProperty['refPid'],    "pid": saleProperty['pid'],    "vid": saleProperty['values'][0]['vid'],    "specId": saleProperty['values'][0]['specId']} |
| 16 | Numeric Input type property | {    "templatePid": property['templatePid'],    "refPid": property['refPid'],    "pid": property['pid'],    "vid": property['values'][0]['vid'],    "value": property['values'][0]['value'], // "Nylon"    "numberInputValue": "50",    "valueUnitId": property['valueUnitList'][0]['valueUnitId'],    "valueUnit": property['valueUnitList'][0]['valueUnit']},{    "templatePid": property['templatePid'],    "refPid": property['refPid'],    "pid": property['pid'],    "vid": property['values'][0]['vid'],    "value": property['values'][0]['value'], // "Cotton"    "numberInputValue": "50",    "valueUnitId": property['valueUnitList'][0]['valueUnitId'],    "valueUnit": property['valueUnitList'][0]['valueUnit']} |

1. 

Parent-child attribute calling method (`showType` attribute display type, 0-normal display, 1-display when choosing specific parent attribute values):

  1. 

If there is data corresponding to `showType`=1 and `parentTemplatePid`=`templatePid` when linking through parent attribute `templatePid`, it is considered a child attribute.

  1. 

Data that exists in `templatePropertyValueParentList` through parent attribute `templatePid` serves as the values of the child attributes.

  1. 

Find the corresponding vid's value from vidList under `parentVidList`, to be entered for product release.

After filling in all attribute values, call `bg.goods.property.compliance.check` to verify whether the current product attribute value settings comply with regulatory requirements.

- 

Write `refPid`, `vid`, `pid` into `normalPropertyList` from the attribute template; if any prohibited sale rules are hit, the `errorMsg` will return the non-compliant attribute names that were hit.

## 

2.4 Query and Assemble Product Specification SKU List

Set the sales specifications for the product; scenarios of the relationship between product category and attribute template on specifications are as follows:

1. 

Specifications for some category attribute templates have been configured; fill in according to the rules. For example: For clothing products, set color as the parent specification and size as the child specification.

1. 

Some category attribute templates have a selectable range configured for specifications, with at most two and at least one specification.

1. 

If none of the above two scenarios matches, it will report an error: Category unavailable.

Relevant Interfaces:

`bg.local.goods.template.get` Product Attribute Category Interface

`bg.local.goods.spec.id.get` Generate Merchant Custom Specifications

Specific Operations:

a. Obtain the specId required for the category of the product to be released through the `bg.local.goods.template.get` interface.

b. Query or generate merchant custom specifications using the `bg.local.goods.spec.id`.get interface according to the obtained specification attribute id.

"Specification name does not exceed 2": No more than two `specId` in `specIdList`;

"Number of specification values does not exceed 44" implies a total of no more than 44 specification values: e.g., colors and sizes "black, white..." combined with "X, XL..." should not exceed 44 in total.

All specifications in `specIdList` need to be entered as a Cartesian product, i.e., combine two specifications in pairs. For example: if there are colors A, B and sizes a, b, then there are four SKUs: [A, a][A, b][B, a][B, b].

### 

SKU Basic Validation

******

******

******

| Content | Judgment conditions | Error |
|---|---|---|
| Specification value basic check | Specification name does not exceed 2 | Number of parent specifications exceeds limit |
| Within the limited quantity range | SKU must not exceed 500 |
| the parent specification quantity consistent with the specification value quantity of the SKU | SKU specification information is inconsistent |
| SKU specification structure check | SKU with the same specification | SKU specification value ID is incorrect |
| SKU with the same sub-specification name | The sub-specification names for a single SKU are duplicated |
| The parent specification of each sku needs to be the same | SKU's parent specifications are inconsistent |

### 

SKU content verification

******

******

******

| Content | Judgment conditions | Error |
|---|---|---|
| SKU quantity check | SKU quantity must be greater than 0 | Product must have at least one SKC |
| SKU preview image check | Product carousel image cannot be empty | Upload product carousel images |
| SKU thumbnail image cannot be empty | Upload SKU thumbnail image |
| SKC carousel image cannot be empty | Upload SKC carousel images |
| Sku external code | outSkuSn contains special characters | Only use letters, numbers and common punctuation for contribution SKU |
| outSkuSn is repeated | SKU duplicated |
| Product price | Base price must be greater than 0 | Base price must be greater than 0 with valid currency |
| List price must be greater than base price | List price must be greater than base price |
| The currency unit of all sku supply prices under the same goods must be consistent | Invalid currency |
| Under the same SKC, the SKU List price needs to be consistent | List price for the same color must match |
| Under the same skc, the sku Base price needs to be consistent | Base price for the same color must match |
| Under the same skc, the sku Base price currency unit needs to be consistent | Invalid currency |

## 

## 

2.5 Prepare Size Chart

Query the size elements content that needs to be completed for the product to make it easier for buyers to purchase the right size.

Relevant Interface:

`bg.local.goods.size.element.get` Size Element Information Query Interface

`bg.local.goods.image.upload` Image material processing Interface

Specific Operations:

1. 

Use bg.local.goods.size.element.get interface, obtain the size element rules of the category through `catId`, which currently returns mapping area codes (US site only supports US code), product elements, and body elements information;

  1. 

When the interface returns empty, this indicates the current category does not require a size element;

  1. 

When the interface returns not empty, this indicates the current category require a size element. Merchants can upload size elements in one of two ways: size chart or size image. And when publishing /modifying products, merchants can only choose one of them.

1. 

If merchants use size image to publish products, merchants need to call bg.local.goods.image.upload to convert them into temu images.

  1. 

The size chart image you uploaded will be displayed in the product pages. The image must meet the following conditions:

    1. 

Quantity: 1 pieces;

    1. 

Format: jpeg, jpg, png;

    1. 

Aspect Ratio(with:height): ≥1:3;

    1. 

Width: ≥800px; 

    1. 

High: ≥800px;

    1. 

Size: ≤3MB;

  1. 

It is recommended that the image include the following information: all selected size, product parameters, use size units in.

![image](https://bstatic.kwcdn.com/open-outer/2079f61f2c/cafee884ff3ff9e498855616450e85c3)

1. 

If add a size chart manually, please refer to the following specific Operations

1. 

Size column

  1. 

The size elements returned by the interface with `sizeSpecType`=0 indicate the first column of the size chart is mapped from the specification value, which should be entered into the groups field of the product upload interface from the selected `specId` and `name` by the merchant;

  1. 

The size elements returned by the interface with `sizeSpecType`=1 indicate that the first column of the size chart is fixed as 'size';

  1. 

The first row of the `groups` field defaults to `{"id":1,"name":"size"}`;

1. 

Mapping area code (US size)

  1. 

The size elements returned by the interface with `needUSSpec` determine whether the current category needs additional US size information;

  1. 

Body element size charts do not need to fill in the US size;

1. 

Size element columns

  1. 

The size elements returned by the interface with `type`=1 are product elements, which should be entered into the `meta` field of the product upload interface from the returned `elementId` and `elementName`; merchant-provided product element information should be entered into the records field of the product upload interface;

  1. 

The size elements returned by the interface with `type`=2 are body elements, which should be entered into the `bodyMeta` field of the product upload interface from the returned `elementId` and `elementName`; merchant-provided body element information should be entered into the `bodyRecords` field of the product upload interface;

  1. 

Note: The returned size elements will definitely have product elements, but not necessarily body elements, depending on the product category;

1. 

`sizeSpecElementList` represents non-suite information, `setElementList` represents suite information, and suite size groups will contain multiple size group information referenced above;

1. 

Adding size chart for custom specifications

  1. 

Call the `bg.local.goods.template.get` method, if no product specifications are returned, custom specifications need to be selected from `userInputParentSpecList`, and the specifications in `userInputParentSpecLis`t will include size specifications (`feature`=2);

  1. 

If a size specification (`feature`=2) is selected, enter custom specification values, such as "small", "Big", then the size chart's record is "small", "Big", and the `record` records two lines;

  1. 

If not selected, then only one line of `record` needs to be entered.

### 

Code Example

Only product sizes

The size element query interface returns the following information:

```
{  
    "sizeSpecElementRule": {  
        "catId": 108965,  
        "classId": 5,  
        "className": null,  
        "allowRange": false,  
        "needUSSpec": true,  
        "sizeSpecType": 0,  
        "sizeSpecElementList": [  
            {  
                "elementId": 10001,  
                "elementName": null,  
                "type": "1",  
                "value": "Shoulder",  
                "description": "Measure your waist at the thinnest place1.",  
                "necessary": true  
            },  
            {  
                "elementId": 10002,  
                "elementName": null,  
                "type": "1",  
                "value": "Chest Circumference",  
                "description": "full chest circumference",  
                "necessary": true  
            },  
            {  
                "elementId": 10003,  
                "elementName": null,  
                "type": "1",  
                "value": "Clothes length",  
                "description": "The length of the clothes1",  
                "necessary": false  
            },  
            {  
                "elementId": 10004,  
                "elementName": null,  
                "type": "1",  
                "value": "Sleeve length",  
                "description": "The length of the sleeves",  
                "necessary": false  
            },  
            {  
                "elementId": 10008,  
                "elementName": null,  
                "type": "1",  
                "value": "Bottom Length",  
                "description": "trouser length",  
                "necessary": true  
            }  
        ],  
        "setElementList": null  
    }  
}
```

The corresponding parameters for creating a size chart are as follows

```
{  
    "sizeSpecInfoList": [  
        {  
            "classId": 5,  
            "meta": {  
                "groups": [  
                    {  
                        "id": 1,  
                        "name": "size"  
                    },  
                    {  
                        "id": 6,  
                        "name": "us"      
                    }  
                ],  
                "elements": [  
                    {  
                        "id": 10001,  
                        "name": "Shoulder"  
                    },  
                    {  
                        "id": 10002,  
                        "name": "Chest Circumference"  
                    },  
                    {  
                        "id": 10003,  
                        "name": "Clothes length"  
                    },  
                    {  
                        "id": 10008,  
                        "name": "Bottom Length"  
                    }  
                ]  
            },  
            "records": [  
                {  
                    "values": [  
                        {  
                            "id": 1,  
                            "value": "11"  
                        },  
                        {  
                            "id": 6,  
                            "value": "1"  
                        },  
                        {  
                            "id": 10001,  
                            "value": "3"  
                        },  
                        {  
                            "id": 10002,  
                            "value": "2"  
                        },  
                        {  
                            "id": 10003,  
                            "value": "23"  
                        },  
                        {  
                            "id": 10008,  
                            "value": "3"  
                        }  
                    ]  
                },  
                {  
                    "values": [  
                        {  
                            "id": 1,  
                            "value": "11.5"  
                        },  
                        {  
                            "id": 6,  
                            "value": "2"  
                        },  
                        {  
                            "id": 10001,  
                            "value": "3"  
                        },  
                        {  
                            "id": 10002,  
                            "value": "2"  
                        },  
                        {  
                            "id": 10003,  
                            "value": "3"  
                        },  
                        {  
                            "id": 10008,  
                            "value": "2"  
                        }  
                    ]  
                }  
            ]  
        }  
    ]  
}
```

#### 

Both product and body size are included

The query size element interface returns the following information

```
{  
    "sizeSpecElementRule": {  
        "catId": 39153,  
        "classId": 28,  
        "className": null,  
        "allowRange": true,  
        "needUsspec": true,  
        "sizeSpecType": 0,  
        "sizeSpecElementList": [  
            {  
                "elementId": 10005,  
                "elementName": null,  
                "type": "1",  
                "value": "Waist size",  
                "description": "Measure straight across the top of the waistband from one side to the other.",  
                "necessary": true  
            },  
            {  
                "elementId": 10006,  
                "elementName": null,  
                "type": "1",  
                "value": "Full hip circumference",  
                "description": "Measure straight from edge to edge on the widest hip line",  
                "necessary": false  
            },  
            {  
                "elementId": 10008,  
                "elementName": null,  
                "type": "1",  
                "value": "Bottom length",  
                "description": "Measure from the waistband to the leg opening or hem.",  
                "necessary": false  
            },  
            {  
                "elementId": 10009,  
                "elementName": null,  
                "type": "1",  
                "value": "Inseam length",  
                "description": "Measure the length from the crotch seam to the bottom of the leg.",  
                "necessary": false  
            },  
            {  
                "elementId": 10010,  
                "elementName": null,  
                "type": "1",  
                "value": "Length",  
                "description": "Measure from the waistband to the leg opening or hem.",  
                "necessary": true  
            },  
            {  
                "elementId": 30002,  
                "elementName": null,  
                "type": "2",  
                "value": "Bust",  
                "description": "Bust"  
            },  
            {  
                "elementId": 30000,  
                "elementName": null,  
                "type": "2",  
                "value": "Waist",  
                "description": "Waist"  
            },  
            {  
                "elementId": 30001,  
                "elementName": null,  
                "type": "2",  
                "value": "Hips",  
                "description": "Hips"  
            },  
            {  
                "elementId": 30003,  
                "elementName": null,  
                "type": "2",  
                "value": "Height",  
                "description": "Height"  
            }  
        ]  
    }  
}
```

The corresponding parameters for creating a size chart are as follows

```
{  
    "sizeSpecInfoList": [  
        {  
            "classId": 28,  
            "meta": {  
                "groups": [  
                    {  
                        "id": 1,  
                        "name": "size"  
                    },  
                    {  
                        "id": 6,  
                        "name": "us"  
                    }  
                ],  
                "elements": [  
                    {  
                        "id": 10005,  
                        "name": "Waist size"  
                    },  
                    {  
                        "id": 10010,  
                        "name": "Length"  
                    }  
                ]  
            },  
            "records": [  
                {  
                    "values": [  
                        {  
                            "id": 1,  
                            "value": "XXS"  
                        },  
                        {  
                            "id": 6,  
                            "value": "1"  
                        },  
                        {  
                            "id": 10005,  
                            "value": "1"  
                        },  
                        {  
                            "id": 10010,  
                            "value": "1"  
                        }  
                    ]  
                }  
            ],  
            "bodyMeta": {  
                "groups": [  
                    {  
                        "id": 1,  
                        "name": "size"  
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
                    },  
                    {  
                        "id": 30001,  
                        "name": "Hips"  
                    },  
                    {  
                        "id": 30003,  
                        "name": "Height"  
                    }  
                ]  
            },  
            "bodyRecords": [  
                {  
                    "values": [  
                        {  
                            "id": 1,  
                            "value": "XXS"  
                        },  
                        {  
                            "id": 30000,  
                            "value": "1-2"  
                        },  
                        {  
                            "id": 30001,  
                            "value": "1-2"  
                        },  
                        {  
                            "id": 30002,  
                            "value": "1-2"  
                        },  
                        {  
                            "id": 30003,  
                            "value": "1-2"  
                        }  
                    ]  
                }  
            ]  
        }  
    ]  
}
```

## 

## 

2.6 Prepare Product Fulfillment Logistics Information

Set product skuId, preparation time, shipping template, import settings, and fulfillment channel information.

Preparation time: 0 days, 1 day, 2 days

Import settings: Imported, Made in the USA, Made in the USA and Imported, Made in the USA or Imported

Fulfillment channel: The first phase only supports self-delivery (Merchant Fulfilled)

Shipping template: `bg.local.freight.template.query.list` Product Shipping Template Query Interface

## 

2.7 Safety and Compliance [Replicated]

**Note:** The current object no longer needs to be assembled when listing products. For those already integrated, no action is required as the logic remains unchanged. The only adjustment is that the fields have been changed from mandatory to optional parameters.

Query the current product's required compliance and qualification information.

Relevant Interfaces:

`bg.local.goods.compliance.extra.template.get` Governance Attribute Template Query Interface

`bg.local.goods.compliance.rules.get` Qualification and Actual Image Query Interface

Specific Operations:

a. Use `bg.local.goods.compliance.extra.template.get` to query the basic governance attribute information that the product in the category should fill in according to the current attributes value settings.

Points to note:

- 

Attributes without a parent attribute are mandatory (parentPid is empty or 0).

- 

Attributes that have a parent and have selected a value from the parent attribute value list are mandatory (parentPid is not empty or 0, and a value has been chosen under parentPid and parentVidList).

- 

Cannot select mutually exclusive attribute values under an attribute (use excludeVidMap to determine, if a value has been chosen from excludeVidMap as a key, no values can be chosen from the corresponding values).

- 

The number of attribute values chosen under an attribute should not exceed the maximum allowable limit (use selectNum to judge).

b. Use `bg.local.goods.compliance.rules.get` to query the qualification and real shot image information that should be filled in according to the current ordinary attribute values and basic governance attribute settings of the product in the category.

Points to note:

Qualifications:

- 

Whether a qualification type `certType` is mandatory is determined by `isRequired`.

- 

All content types returned under the qualification must be completed, `contentType`=1 for qualification certificates (corresponding to the `certFiles` field in the submission interface), `contentType`=2 for inspection reports (corresponding to the `inspectReportFiles` field), `contentType`=3 for qualification numbers (corresponding to the `authCode` field).

- 

For non-mandatory qualifications, if entered, all content types `contentType` must be completed.

Real Shot Images:

- 

Each `position` returned by real shot images is mandatory.

- 

In the submission interface, the `sameSku` field for real shot images indicates whether the product real shot is the same as the sku real shot. If `sameSku` is false, it indicates that the product and sku real shots are different, and therefore a combination of all unremoved skus' specification information (`specIdList`) and the corresponding sku real shots need to be entered; if `sameSku` is true, it means that the product real shot is consistent with the sku real shot, and only one set of real shots must be entered, in which case the `specIdList` field is unnecessary.

- 

The number of real shot images that can be uploaded is controlled by the `maxPhotoSize` field.

# 

Publish Product

## 

3.1 Direct Publishing and Listing

Enter the prepared product parameter information into the `bg.local.goods.add` product addition interface and submit for publication. If successfully published, the product enters the inspection process. If publication fails, the system will not save a draft, so please ensure to save relevant product information.

Interface Parameter Explanation

******

******

******

``

``

``

``

``

``

````

``

``

``

``

``

| Element | Description | Remarks |
|---|---|---|
| goodsBasic | Basic Product Information |  |
| goodsServicePromise | Merchant Service Information | Includes information about stocking, delivery, shipping costs, etc. |
| goodsProperty | Product Attributes | Includes attributes and specifications that define the product variants. |
| bulletPoints | Product Bullet Points | A maximum of five selling points, each not exceeding 200 characters. |
| goodsDesc | Product Description | The description should not exceed 2000 characters. |
| certificationInfo[Replicated] | Governance Attributes, Qualification Documents, and Real Shot Images | Governance attributes require calling the bg.local.goods.compliance.extra.template.get to get the rules; after filling in the governance attributes, use the bg.local.goods.compliance.rules.get interface to get the rules for filling out qualifications and real shot images. |
| guideFileInfo | Guide file | Check whether the user manual is mandatory and what language it should be in by querying bg.local.goods.compliance.extra.template.get. Only PDF format user manuals can be uploaded. |
| goodsSizeChartList | Size Chart | The required parameters for the size chart are determined by the bg.goods.size.element.get method and the specified specifications. |
| skuList | SKU List |  |

## 

3.2 View Product Publishing Status and Edit

`bg.local.goods.publish.status.get` Batch query the latest review status based on goodsId.

# 

Orig**i**nlnfo  of Product

**originRegion1**

First level address of origin, indicating a country or region

**originRegion2**

Secondary address of origin, indicating provincial or state level

Note: Only when the primary address is in Chinese Mainland, the secondary address is required; When the primary address is in another country or region, a secondary address is not required

**agreeDefaultOriginRegion**

Platform default value

true： This submission/modification will be read and written by Temu based on the product and merchant's authenticated information by default

false： This submission/modification will read interface parameters and write values

Default to false

Default rule:

1. Prioritize obtaining the address information of the product manufacturer

2. If the manufacturer's address is unavailable, obtain the business address

Listing of Origin Information：[https://dl.kwcdn.com/upload-common/seller-protocol/45824d2f-aa16-481a-aef5-607039cd79a0](https://dl.kwcdn.com/upload-common/seller-protocol/45824d2f-aa16-481a-aef5-607039cd79a0)

# 

Requirements for publishing special category products

According to the category type returned by this interface：bg.local.goods.cats.get -expandCatType

-bg.local.goods.template.get: Added parameters [additionalInfo] and [needIsbn] to determine if a mandatory ISBN code is required

Business Description

1. DVD/CD category, add mandatory attribute manufacturer information, if the country of origin is Chinese Mainland, ISBN code is required

-Manufacturer reference: 7150

-Manufacturer PID: 2167

2. Book category, required publisher information

3. The manufacturer & publisher  information needs to be created by the seller in advance on the [Seller Center~Performance~Account health~Copyright] page
