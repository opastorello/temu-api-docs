# Product Basic Introduction

# 

Summary

The Product API is designed to provide merchants with a one-stop, large-scale product management capability. This API not only supports product creation, catalog inquiry, and listing/delisting operations but also allows merchants to synchronize their products to TEMU through third-party platforms such as Shopify, achieving centralized management of product information.

Merchants can directly create and publish products through the Publish Product API, with the creation process as follows: 

1. 

Query the available product categories in the store.

1. 

[Replicated] Query the attribute templates and qualification attributes corresponding to the category.

1. 

Query the size chart templates corresponding to the category.

1. 

Query the available brand list and shipping template list in the store.

1. 

Upload images, videos, qualification documents, etc., and obtain the corresponding image IDs, video IDs, and file IDs.

1. 

Fill in the above information and submit the product. After the product submission is successful, it will enter the platform's review process.

![image](https://bstatic.kwcdn.com/open-outer/1fad18baf8/bc654fec94a2b0159a0ec75a09948680.png)

After product creation or editing, TEMU will conduct a review and verification process of the product content. Developers can check the publication and review status of the product through the Product Status API. 

# 

Terminology Concept

****

****

``

``

````

``

| Field/Element | Description |
|---|---|
| Product | A unit listed for sale by merchants on TEMU, created by the system with goodsId that serves as a globally unique identifier. |
| SKU | Stock Keeping Unit, an inventory unit maintained by the merchant, identified by the store with skuId that serves as the unique identifier. |
| Category | TEMU categorizes products in a pre-defined rule-based grouping, forming a tree structure organization; all products must belong to a specific leaf category. |
| Product Basic Information | The foundational descriptive details of a product listing, such as product descriptions, key points, brand, detail images, order fulfillment, etc. |
| Product Pricing | TEMU supports merchants in submitting both a supply price and a retail price. The base price will be used for product price verification as the supply cost, while the list price will be suggested as the strikethrough price on the product detail page. |
| Attributes | Supplementary content for product information, designed to give customers a better understanding of the product. Attributes are further divided into sale attributes and non-sale attributes. |
| Attribute Template | Comprised of leaf category + common attributes + sale attributes + custom specifications, the attribute names and attribute value enumerations that need to be filled in during product creation are only related to the leaf category of the product. |
| Product Non-Sale Attributes | Supplementary information to the product description supporting consumer judgment, such as material, components, country of origin, manufacturer, etc. |
| Product Sale Attributes | Information used to differentiate variants (i.e., SKUs), commonly referred to as specifications, like color, size, phone model, etc. TEMU permits at least one specification to be set for a product and a maximum of two; there must be at least one specification value. All specifications must be provided in the specIdList, with no more than 500 total. |
| Product Qualification Attributes [Replicated] | Used by principal merchants in the United States to supply compliance information when listing products. Unlike the attribute template, the scope of compliance properties to be filled in is determined by the attributes entered by the user and the leaf category, typically including: California Proposition 65 warnings, qualification documents, manuals, photos of the actual packaging, etc. |

# 

Product Description

****

****

****

- 

- 

- 

- 

- 

  - 

  - 

- 

- 

  - 

  - 

  - 

- 

- 

  - 

  - 

  - 

  - 

| Field/Element | Description | Example |
|---|---|---|
| Product Name | Validation Rules:Only supports English letters, numbers, and symbols.Does not support decorative characters: ~ ! * $ ? _ ~ { } # < > \| * ; ^ ¬ ¦Does not support high ASCII characters type 1, such as ®, ©, ™, etc.Character count: Within 500 characters. | To better attract customers' attention, it is recommended to fill in the title template below.Title template: [Product brand] + [Product details] + [Application range] + [Product type] + [Main features/functions/advantages]Title example: [XXX (brand)] + [Dual zone wine cooler and beverage refrigerator] + [Standalone or counter refrigerator, glass door and LED light] + [78 can and 20 bottle capacity, 24 inches] + [Stainless steel] |
| Category | Choose the most appropriate category for the product, which will affect the content of product attributes. |  |
| Product Description | Detailed explanation of the product's features and uses.Validation Rules:Only supports letters, numbers, and symbols; does not support rich text.Data type: string.Character count: Within 10000 characters. |  |
| Bullet Point | Highlight the main characteristics and advantages of the product.Validation Rules:Only supports English letters, numbers, and symbols.Data type: string.Character count: Within 700 characters.Up to 6 lines maximum. |  |

# 

Attributes and Attribute Templates

****

****

****

- 

- 

- 

- 

- 

- 

****

![image](https://bstatic.kwcdn.com/open-outer/1f19348d740/e884995eccd43cabe0dba38bc815f05a.png)

****

![image](https://bstatic.kwcdn.com/open-outer/1f19348d740/c5476980e5562c749f13b5088b50d444.png)

****

![image](https://bstatic.kwcdn.com/open-outer/1f19348d740/73897e44aa6aebce6b2267ff20eac12d.png)

****

| Field/Element | Description | Example |
|---|---|---|
| Attributes and Attribute Values | Attributes correspond to various descriptive aspects of a product and include attribute names and their respective values. | Fabric: Cotton, Nylon, Silk, etc.Color: Red, Yellow, Blue, etc. |
| Relationship with Categories | Attributes are linked to leaf categories through attribute templates. Products under different leaf categories require distinct attribute dimensions for description. | Dresses: Style, Fabric, Target Audience, Bust and Waist measurements, etc.Dishwashers: Manufacturer, Dimensions (Length x Width x Height), etc. |
| Parent-Child Attributes | Through the reference relationship between parent and child attributes, the selection of attributes creates a cascading effect. | Electrical Devices: When the battery option is rechargeable, users can choose the charging power attribute.Cable Interfaces: When the brand is chosen as one that has completed qualification certification, cable interfaces can include options like HDMI, MFI, etc. |
| Custom Attributes (Specifications) | For certain categories of products, merchants can define custom attribute values. Merchants should provide content in English, and the system will translate it into multiple languages for consumer-facing displays. |  |
| Prohibited Attributes | To comply with local laws and regulations, the simultaneous selection of certain attribute values by merchants may be prohibited from being published for sale on corresponding sites. |  |
| Specific Uses of Attributes | 1. Differentiate SKUs: Attributes are the basic distinction that allows customers to purchase more specific items. |  |
| 2. Enrich Product Information: Attributes help consumers view detailed information, assisting with purchasing decisions. |  |
| 3. Search/Filter Sorting: Attributes enable consumers to filter and find the types of products they want within a certain category, allowing for quick location. |  |
| 4. Basic Fields: Used for search/recommendation/product name assembly, etc. |  |

# 

Images and videos

****

****

****

****

****

****

| Functional module | Material | Dimensions | Size | Type | Note |
|---|---|---|---|---|---|
| Product Description | Detail Video | Duration: ≤180sAspect Ratio: 1:1, 4:3, 16:9Resolution: ≥720P | ≤300 MB | wmv, avi, 3gp, mov, mp4, flv、rmvb, mkv, m4v, x-flv, WMV, AVI, 3GP, MOV, MP4, FLV, RMVB, MKV, M4V, X-FLV | Product Description, Detail Video, Product Images make up the detailed presentation. By default, the video is displayed as the first element of this presentation. |
| Product Images | Quantity: ≤50Aspect Ratio: ≥1:3Width: ≥480pxHeight: ≥480px | ≤3MB | jpeg, jpg, png |
| SKU Carousel Images | Apparel Carousel Images | Quantity: 1Aspect Ratio: 3:4Width:≥1340pxHeight: ≥1785px | ≤3 MB | jpeg, jpg, png | Take the first image of each SKC as the SKC preview image |
| Non-Apparel Carousel Images | Quantity: 1Aspect Ratio: 1:1Width:≥800pxHeight: ≥800px | ≤3 MB | jpeg, jpg, png | SPU carousel- Take the first image of the first SKU as the first image- Splice the images of each SKU from the second image onwards after the first imageSKU preview image- Take the first image of each SKU as the SKU preview image |
| Product Video | Product Video | Quantity: ≤1Aspect Ratio: Not restrictedDuration: ≤60sResolution: ≥720P | ≤100 MB | wmv, avi, 3gp, mov, mp4, flv, rmvb, mkv, m4v, x-flv, WMV, AVI、3GP, MOV, MP4, FLV, RMVB, MKV, M4V, X-FLV |  |
| Safety and Compliance | Product Actual Images | Quantity: 1-6 | ≤3 MB | JPG, PNG, JPEG |  |
| Product Guides or Documents | Quantity: same as the language requirement | ≤3 MB | JPG, PNG, JPEG |  |

# 

Size Chart

****

****

****

![image](https://bstatic.kwcdn.com/open-outer/1f19348d740/115a5581c3f7bc4dad3a769b63afaffc.png)

![image](https://bstatic.kwcdn.com/open-outer/1f19348d740/755186a8bb512dd0a4c86655acf80ce1.png)

![image](https://bstatic.kwcdn.com/open-outer/1f19348d740/7b733d1e1bd6657651fc35a908a06313.png)

![image](https://bstatic.kwcdn.com/open-outer/1f19348d740/7d8c2f9929dd53675c80ddced514541f.png)

| Field/Element | Description | Example |
|---|---|---|
| Size Specifications | The specification value of the 'feature' in the sales attributes is by default used as the first column of the size chart. Specifically, if there is no size specification in the product category attribute template, but a size chart is required, then 'Size' should be entered in the first column as the default size. |  |
| Size Class | Size class consist of regional mapping codes (the US site supports only US codes), product elements, and body element information. The relationship between size categories and leaf categories determines that products in different categories need to fill in different size chart contents. |  |
| US Size | Merchants should customize the US sizes based on the size specifications relationship, supporting English letters and numerals. If 'Size' is entered in the first column of the size chart, it is not necessary to fill in the column for US sizes. |  |
| Product Elements | This describes the size information of the product itself, with the default unit being inches. |  |
| Body Elements | This describes the size information suitable for the target demographic, with the default unit being inches. |  |
| Sets | Size categorizations for sets are linked to multiple existing size categories; at least two or more size categories should be filled in as size chart content. |  |

# 

Valuations

****

****

****

- 

  - 

  - 

- 

![image](https://bstatic.kwcdn.com/open-outer/1f19348d740/e3f9f504802fe39f70c46f6cdf7184f7.png)

- 

- 

  - 

  - 

  - 

  - 

- 

- 

  - 

  - 

  - 

- 

- 

- 

  - 

  - 

- 

- 

  - 

  - 

- 

- 

  - 

  - 

- 

- 

  - 

  - 

  - 

- 

  - 

  - 

| Field/Element | Description | Example |
|---|---|---|
| Variations | The specification names and values corresponding to the current category combine to form SKUs through the product of parent and child specifications.At least 1 specification name and at most 2 should be selected.At least 1 specification value should be selected.For apparel categories, the color specification is the default parent specification and constitutes the SKC. |  |
| Contribution SKU | Merchants can create custom identifiers, which are unique within their store.Validation rules:Data type: StringCharacters: English letters/numbers/symbolsNumber of characters: ≤100Must not be the same as any other SKU/SPU ID in the same store. |
| External Product ID | Mandatory for book categories.Enum values and validation rules:UPC: 12 digits, the last digit is a check digit.EAN: 8 or 13 digits, the last digit is a check digit.ISBN (displayed in book category): 10 or 13 digits, for 10-digit ISBNs the last digit may be 0-9 or X; for 13-digit ISBNs, it begins with '978' or '979'. |
| Dimension | Collect product length, width, and height data.Unit: Inches (in)Validation rules:Data type: Floating-point numberDigits: ≤3 integer digits, ≤1 decimal place |
| Weight | Unit: Pounds (lb)Validation rules:Data type: Floating-point numberDigits: ≤4 integer digits, ≤1 decimal place |
| Base Price | Unit: US dollars ($)Validation rules:Data type: Floating-point numberDigits: ≤8 integer digits, ≤2 decimal places |
| List Price | Unit: US dollars ($)Validation rules:Data type: Floating-point numberDigits: ≤8 integer digits, ≤2 decimal placesList Price ≥ Base Price |
| Quantity | Validation rules:Data type: IntegerDigits: ≤6 digits |

# 

Offer

****

****

****

- 

- 

  - 

  - 

  - 

  - 

![image](https://bstatic.kwcdn.com/open-outer/1f19348d740/b60f079d491865b65fba28025dcdd92a.png)

- 

- 

- 

  - 

  - 

  - 

  - 

- 

| Field/Element | Description | Example |
|---|---|---|
| Contribution SKU | Merchants create custom identifiers, which serve as unique identifiers for goodsId within the store.validation rules:Data type: StringCharacters: English letters/numbers/symbolsNumber of characters: ≤100Cannot duplicate any other product's SKU/SPU ID under the same store. |  |
| Handling Time | Enumerated values: 1/2 days |
| Shipping Template | Only freight templates that have been created in MMS are supported. |
| Import Designation | Enumerated values:ImportedMade in the USAMade in the USA and ImportedMade in the USA or Imported |
| Fulfillment Channel | Only supports the self-delivery option. |

# 

Safety and Compliance [Replicated]

****

****

****

![image](https://bstatic.kwcdn.com/open-outer/1f19348d740/5842ea36ae967e922c05eb7d6957345b.png)

| Field/Element | Description | Example |
|---|---|---|
| Governance Attributes | Determine the template for filling out governance attributes based on the category of the product + the attributes already filled out by the product. |  |
| Qualification and Actual Photos | Determine the qualification and requirement for authentic photos based on the category of the product, the attributes already filled out by the product, and the governance attributes values filled out. |
