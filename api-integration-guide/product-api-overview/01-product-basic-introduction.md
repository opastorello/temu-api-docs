# Product Basic Introduction

**Last update:** 2025-10-11 00:52:57

## Summary

The Product API is designed to provide merchants with a one-stop, large-scale product management capability. This API not only supports product creation, catalog inquiry, and listing/delisting operations but also allows merchants to synchronize their products to TEMU through third-party platforms such as Shopify, achieving centralized management of product information.

### Product Creation Flow

1. Query the available product categories in the store.
2. Query the attribute templates and qualification attributes corresponding to the category.
3. Query the size chart templates corresponding to the category.
4. Query the available brand list and shipping template list in the store.
5. Upload images, videos, qualification documents, etc., and obtain the corresponding image IDs, video IDs, and file IDs.
6. Fill in the above information and submit the product. After the product submission is successful, it will enter the platform's review process.

After product creation or editing, TEMU will conduct a review and verification process of the product content. Developers can check the publication and review status of the product through the Product Status API.

---

## Terminology Concept

| Field/Element | Description |
|---|---|
| **Product** | A unit listed for sale by merchants on TEMU, created by the system with `goodsId` that serves as a globally unique identifier. |
| **SKU** | Stock Keeping Unit, an inventory unit maintained by the merchant, identified by the store with `skuId` that serves as the unique identifier. |
| **Category** | TEMU categorizes products in a pre-defined rule-based grouping, forming a tree structure organization; all products must belong to a specific leaf category. |
| **Product Basic Information** | The foundational descriptive details of a product listing, such as product descriptions, key points, brand, detail images, order fulfillment, etc. |
| **Product Pricing** | TEMU supports merchants in submitting both a supply price and a retail price. The **base price** will be used for product price verification as the supply cost, while the **list price** will be suggested as the strikethrough price on the product detail page. |
| **Attributes** | Supplementary content for product information, designed to give customers a better understanding of the product. Attributes are further divided into sale attributes and non-sale attributes. |
| **Attribute Template** | Comprised of leaf category + common attributes + sale attributes + custom specifications, the attribute names and attribute value enumerations that need to be filled in during product creation are only related to the leaf category of the product. |
| **Product Non-Sale Attributes** | Supplementary information to the product description supporting consumer judgment, such as material, components, country of origin, manufacturer, etc. |
| **Product Sale Attributes** | Information used to differentiate variants (i.e., SKUs), commonly referred to as specifications, like color, size, phone model, etc. TEMU permits at least one specification to be set for a product and a maximum of two; there must be at least one specification value. All specifications must be provided in the `specIdList`, with no more than 500 total. |
| **Product Qualification Attributes** | Used by principal merchants in the United States to supply compliance information when listing products. Unlike the attribute template, the scope of compliance properties to be filled in is determined by the attributes entered by the user and the leaf category, typically including: California Proposition 65 warnings, qualification documents, manuals, photos of the actual packaging, etc. |

---

## Product Description

| Field/Element | Description |
|---|---|
| **Product Name** | Validation Rules: Only supports English letters, numbers, and symbols. Does not support decorative characters: `~ ! * $ ? _ ~ { } # < > | * ; ^ ¬ ¦`. Does not support high ASCII characters type 1, such as ®, ©, ™, etc. Character count: Within 500 characters. |
| | Title template: `[Product brand] + [Product details] + [Application range] + [Product type] + [Main features/functions/advantages]` |
| **Category** | Choose the most appropriate category for the product, which will affect the content of product attributes. |
| **Product Description** | Detailed explanation of the product's features and uses. Only supports letters, numbers, and symbols; does not support rich text. Character count: Within 10000 characters. |
| **Bullet Point** | Highlight the main characteristics and advantages of the product. Only supports English letters, numbers, and symbols. Character count: Within 700 characters. Up to 6 lines maximum. |

---

## Attributes and Attribute Templates

| Field/Element | Description | Example |
|---|---|---|
| **Attributes and Attribute Values** | Attributes correspond to various descriptive aspects of a product and include attribute names and their respective values. | Fabric: Cotton, Nylon, Silk. Color: Red, Yellow, Blue. |
| **Relationship with Categories** | Attributes are linked to leaf categories through attribute templates. Products under different leaf categories require distinct attribute dimensions. | Dresses: Style, Fabric, Target Audience. Dishwashers: Manufacturer, Dimensions. |
| **Parent-Child Attributes** | Through the reference relationship between parent and child attributes, the selection of attributes creates a cascading effect. | Electrical Devices: When battery is rechargeable, user can choose charging power attribute. |
| **Custom Attributes (Specifications)** | For certain categories, merchants can define custom attribute values. Content should be in English and the system will translate it. | |
| **Prohibited Attributes** | To comply with local laws and regulations, certain attribute combinations may be prohibited from being published on corresponding sites. | |

### Specific Uses of Attributes

1. **Differentiate SKUs**: Attributes are the basic distinction that allows customers to purchase more specific items.
2. **Enrich Product Information**: Attributes help consumers view detailed information, assisting with purchasing decisions.
3. **Search/Filter Sorting**: Attributes enable consumers to filter and find product types within a category.
4. **Basic Fields**: Used for search/recommendation/product name assembly, etc.

---

## Images and Videos

| Functional Module | Material | Dimensions | Size | Type | Note |
|---|---|---|---|---|---|
| **Detail Video** | Video | Duration: ≤180s, Aspect Ratio: 1:1, 4:3, 16:9, Resolution: ≥720P | ≤300 MB | wmv, avi, 3gp, mov, mp4, flv, rmvb, mkv, m4v, x-flv (upper/lowercase) | By default, video is displayed as the first element of the detailed presentation. |
| **Product Images** | Image | Quantity: ≤50, Aspect Ratio: ≥1:3, Width: ≥480px, Height: ≥480px | ≤3 MB | jpeg, jpg, png | |
| **Apparel Carousel Images** | Image | Quantity: 1, Aspect Ratio: 3:4, Width: ≥1340px, Height: ≥1785px | ≤3 MB | jpeg, jpg, png | Take the first image of each SKC as the SKC preview image |
| **Non-Apparel Carousel Images** | Image | Quantity: 1, Aspect Ratio: 1:1, Width: ≥800px, Height: ≥800px | ≤3 MB | jpeg, jpg, png | SPU carousel: first image of first SKU → splice remaining SKU images after |
| **Product Video** | Video | Quantity: ≤1, Duration: ≤60s, Resolution: ≥720P | ≤100 MB | wmv, avi, 3gp, mov, mp4, flv, rmvb, mkv, m4v, x-flv | |
| **Product Actual Images** (Compliance) | Image | Quantity: 1-6 | ≤3 MB | JPG, PNG, JPEG | |
| **Product Guides/Documents** (Compliance) | Document | Quantity: same as language requirement | ≤3 MB | JPG, PNG, JPEG | |

---

## Size Chart

| Field/Element | Description |
|---|---|
| **Size Specifications** | The specification value of the 'feature' in the sales attributes is by default used as the first column of the size chart. If no size specification exists, enter 'Size' as the default first column. |
| **Size Class** | Consist of regional mapping codes (US site supports only US codes), product elements, and body element information. Determines what size chart contents to fill in per category. |
| **US Size** | Merchants customize US sizes based on size specifications relationship, supporting English letters and numerals. |
| **Product Elements** | Describes the size information of the product itself. Default unit: inches. |
| **Body Elements** | Describes the size information suitable for the target demographic. Default unit: inches. |
| **Sets** | Size categorizations for sets are linked to multiple existing size categories; at least two or more size categories should be filled in. |

---

## Valuations

| Field/Element | Description |
|---|---|
| **Variations** | Spec names and values corresponding to the current category combine to form SKUs. At least 1, at most 2 specification names; at least 1 specification value. For apparel categories, the color specification is the default parent specification (SKC). |
| **Contribution SKU** | Merchants create custom identifiers unique within their store. Data type: String. Characters: English letters/numbers/symbols. Length: ≤100 characters. Must not duplicate any other SKU/SPU ID in the same store. |
| **External Product ID** | Mandatory for book categories. UPC: 12 digits. EAN: 8 or 13 digits. ISBN: 10 or 13 digits (13-digit starts with '978' or '979'). |
| **Dimension** | Product length, width, and height. Unit: inches. Data type: Floating-point number. Format: ≤3 integer digits, ≤1 decimal place. |
| **Weight** | Unit: pounds (lb). Data type: Floating-point number. Format: ≤4 integer digits, ≤1 decimal place. |
| **Base Price** | Unit: US dollars ($). Data type: Floating-point number. Format: ≤8 integer digits, ≤2 decimal places. |
| **List Price** | Unit: US dollars ($). Data type: Floating-point number. Format: ≤8 integer digits, ≤2 decimal places. **List Price ≥ Base Price**. |
| **Quantity** | Data type: Integer. Digits: ≤6 digits. |

---

## Offer

| Field/Element | Description |
|---|---|
| **Contribution SKU** | Merchants create custom identifiers unique within the store (also serves as unique identifier for `goodsId`). String, ≤100 characters, no duplicates across the same store. |
| **Handling Time** | Enumerated values: 1/2 days. |
| **Shipping Template** | Only freight templates that have been created in MMS are supported. |
| **Import Designation** | Enumerated values: Imported / Made in the USA / Made in the USA and Imported / Made in the USA or Imported. |
| **Fulfillment Channel** | Only supports the self-delivery option. |

---

## Safety and Compliance

| Field/Element | Description |
|---|---|
| **Governance Attributes** | Determine the template for filling out governance attributes based on the category of the product + the attributes already filled out by the product. |
| **Qualification and Actual Photos** | Determine the qualification and requirement for authentic photos based on the category, existing attributes, and governance attribute values filled in. |
