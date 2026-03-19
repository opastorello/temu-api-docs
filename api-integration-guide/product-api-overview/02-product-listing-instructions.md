# Product Listing Instructions

**Last update:** 2025-10-11 00:53:03

## 1. Category Query

Query the categories that can be posted in the current store (`catId`).

**Relevant Interface:** `bg.local.goods.cats.get` — Product Standard Category Interface

### Interface Description

- `parentCatId=0` retrieves all available first-level categories.
- To obtain leaf categories: Recursively call this interface, entering `parentCatId` with the `catId` from previous call results until leaf categories are reached.
- When entering a leaf category, the interface returns empty.

**Important:**
- Use the most specific (leaf) category ID for posting products.
- `catType` is an important variable: `catType=0` = Apparel, `catType=1` = Non-Apparel. Affects required image shape.

```json
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

---

## 2. Prepare Product Information

### 2.1 Prepare Basic Product Information

- **`goodsName`** (Product Name): English, numerals, and common symbols only. Max 500 characters.
- **`goodsDesc`** (Product Description): English, numerals, and common symbols only. Max 10000 characters.
- **`bulletPoints`** (Product Highlights): English, numerals, and common symbols only. Max 700 characters, up to 6 points.

### 2.2 Upload Product Materials

Upload images, videos, and files required for product sales and certificates, get signature, then upload with the product creation interface.

**Relevant Interface:** `bg.local.goods.gallery.signature.get` — Get Signature for Uploading Materials

**Step 1:** Call `bg.local.goods.gallery.signature.get` to get a signature for uploading materials. Pass in different `uploadFileType` for different file types.

**Step 2:** Call the multimedia file upload interface with the signature:

| Upload Endpoint | Purpose |
|---|---|
| `api/galerie/general_file` | Instruction manuals |
| `api/galerie/general_file` | Certification files (< 20MB) |
| `api/galerie/cos_large_file/upload_init` | Initialize large certification file uploads (> 20MB) |
| `api/galerie/cos_large_file/upload_part` | Chunk upload large certification files (> 20MB) |
| `api/galerie/v1/store_video?sdk_version=js-0.0.32` | Videos |
| `api/galerie/large_file/v1/video/upload_init` | Initialize large video uploads |
| `api/galerie/large_file/v1/video/upload_part` | Large video uploads |
| `api/galerie/large_file/v1/video/upload_complete` | Complete large video uploads |
| `api/galerie/v3/store_image?sdk_version=js-0.0.32` | Product images or live photos |

### Material Requirements

| Functional Module | Material | Dimensions | Size | Type |
|---|---|---|---|---|
| Detail Video | Video | Duration ≤180s, Aspect Ratio 1:1/4:3/16:9, Resolution ≥720P | ≤300 MB | wmv, avi, 3gp, mov, mp4, flv, rmvb, mkv, m4v, x-flv |
| Product Images | Image | Quantity ≤50, Aspect Ratio ≥1:3, Width ≥480px, Height ≥480px | ≤3 MB | JPEG, JPG, PNG |
| Apparel Carousel Images | Image | Quantity 3-10, Aspect Ratio 3:4, Width ≥1340px, Height ≥1785px | ≤3 MB | JPEG, JPG, PNG |
| Non-Apparel Carousel Images | Image | Quantity 3-10, Aspect Ratio 1:1, Width ≥800px, Height ≥800px | ≤3 MB | JPEG, JPG, PNG |
| Product Video | Video | Quantity ≤1, Duration ≤60s, Resolution ≥720P | ≤100 MB | wmv, avi, 3gp, mov, mp4, flv, rmvb, mkv, m4v, x-flv |
| Product Actual Images (Compliance) | Image | Quantity 1-6 | ≤3 MB | JPG, PNG, JPEG |
| Product Guides/Documents (Compliance) | Document | Quantity per language requirement | ≤3 MB | JPG, PNG, JPEG |

### 2.3 Query Product Attribute Template and Compliance Check

**Relevant Interfaces:**
- `bg.local.goods.template.get` — Category Product Attribute Template Query Interface
- `bg.local.goods.property.compliance.check` — Product Attribute Compliance Prohibition Verification Interface

**Specific Operations:**
1. Use `bg.local.goods.template.get` to get publishing rules for the category via `catId`.
2. Retrieve `refPid`, `vid`, `value` from return parameters to enter into the `goodsProperties` field of the product upload interface.
3. Attributes with `isSale=true` are sales attributes (standard attributes); combine with specifications and get `specId` directly from this interface, entering it into both `goodsProperties` and `specIdList` of `skuList`.
4. If `templateInfo.goodsSpecProperties` has no data, select a system predefined specification from `userInputParentSpecList`; the number of specifications is decided by `inputMaxSpecNum`.

#### ControlType Values

| ControlType | Description | Property Object Parameters |
|---|---|---|
| `0` | Input type property | `{ "templatePid": ..., "refPid": ..., "pid": ..., "vid": 0, "value": "..." }` |
| `1` | Select type property | `{ "templatePid": ..., "refPid": ..., "pid": ..., "vid": property.values[0].vid, "value": property.values[0].value }` |
| `16` | Numeric Input type property | Includes `numberInputValue`, `valueUnitId`, `valueUnit` |

**Sale Property (for `goodsSpecProperties`):**
```json
{
  "templatePid": "...",
  "refPid": "...",
  "pid": "...",
  "vid": "...",
  "specId": "..."
}
```

**Parent-child attribute rule:** If `showType=1` and linked via `parentTemplatePid`, it is a child attribute. Values come from `templatePropertyValueParentList`.

After filling in all attribute values, call `bg.goods.property.compliance.check` to verify compliance.

### 2.4 Query and Assemble Product Specification SKU List

**Relevant Interfaces:**
- `bg.local.goods.template.get` — Product Attribute Category Interface
- `bg.local.goods.spec.id.get` — Generate Merchant Custom Specifications

**Specific Operations:**
1. Obtain `specId` required for the category via `bg.local.goods.template.get`.
2. Query or generate merchant custom specifications via `bg.local.goods.spec.id.get`.
3. No more than 2 `specId` in `specIdList`; no more than 44 combined specification values.
4. All specifications in `specIdList` must be entered as a Cartesian product (all combinations).

#### SKU Basic Validation

| Content | Judgment Conditions | Error |
|---|---|---|
| Specification name count | ≤ 2 specification names | Number of parent specifications exceeds limit |
| SKU quantity | SKU must not exceed 500 | Within the limited quantity range |
| SKU spec consistency | Parent specification quantity consistent with spec values | SKU specification information is inconsistent |
| SKU spec uniqueness | No duplicate specs within same SKU | SKU specification value ID is incorrect |
| Sub-spec names | No duplicate sub-spec names for a single SKU | Sub-specification names for a single SKU are duplicated |
| Parent spec consistency | All SKUs must have same parent specification | SKU's parent specifications are inconsistent |

#### SKU Content Verification

| Content | Judgment Conditions | Error |
|---|---|---|
| SKU quantity | Quantity > 0 | Product must have at least one SKC |
| Carousel image | Cannot be empty | Upload product carousel images |
| Thumbnail image | Cannot be empty | Upload SKU thumbnail image |
| SKC carousel image | Cannot be empty | Upload SKC carousel images |
| `outSkuSn` chars | No special characters | Only use letters, numbers and common punctuation |
| `outSkuSn` uniqueness | No duplicates | SKU duplicated |
| Base price | > 0 | Base price must be greater than 0 with valid currency |
| List price | ≥ Base price | List price must be greater than base price |
| Currency consistency | All SKU supply prices same currency | Invalid currency |
| List price per SKC | Under same SKC, all SKU list prices must match | List price for the same color must match |
| Base price per SKC | Under same SKC, all SKU base prices must match | Base price for the same color must match |

### 2.5 Prepare Size Chart

**Relevant Interfaces:**
- `bg.local.goods.size.element.get` — Size Element Information Query Interface
- `bg.local.goods.image.upload` — Image Material Processing Interface

**Specific Operations:**
1. Use `bg.local.goods.size.element.get` to obtain size element rules for the category via `catId`.
2. If interface returns empty → current category does not require a size element.
3. If interface returns data → size element required. Merchants can upload via size chart or size image (choose one).
4. Size chart image requirements: Quantity 1, Format jpeg/jpg/png, Aspect Ratio ≥1:3, Width ≥800px, Height ≥800px, Size ≤3MB.

**Size chart field mapping:**
- `sizeSpecType=0` → first column mapped from specification value (enter into `groups` field).
- `sizeSpecType=1` → first column is fixed as 'size'; first row of `groups` defaults to `{"id":1,"name":"size"}`.
- `type=1` elements → product elements → enter `elementId`/`elementName` into `meta.elements`, values into `records`.
- `type=2` elements → body elements → enter into `bodyMeta.elements`, values into `bodyRecords`.
- `needUSSpec=true` → include US size column `{"id":6,"name":"us"}` in `groups`.

### 2.6 Prepare Product Fulfillment Logistics Information

**Relevant Interface:** `bg.local.freight.template.query.list` — Product Shipping Template Query Interface

- **Preparation time:** 0 days, 1 day, 2 days
- **Import settings:** Imported / Made in the USA / Made in the USA and Imported / Made in the USA or Imported
- **Fulfillment channel:** Self-delivery (Merchant Fulfilled) only

### 2.7 Safety and Compliance

**Relevant Interfaces:**
- `bg.local.goods.compliance.extra.template.get` — Governance Attribute Template Query Interface
- `bg.local.goods.compliance.rules.get` — Qualification and Actual Image Query Interface

**Specific Operations:**
1. Use `bg.local.goods.compliance.extra.template.get` to query governance attributes for the product's category.
   - Attributes without a parent (`parentPid` empty or 0) are **mandatory**.
   - Attributes with a parent where a value has been chosen from `parentPid.parentVidList` are **mandatory**.
   - Cannot select mutually exclusive attribute values (check `excludeVidMap`).
   - Number of attribute values chosen under an attribute must not exceed `selectNum`.

2. Use `bg.local.goods.compliance.rules.get` to query qualification and real shot image requirements.
   - Qualifications: `isRequired` determines if mandatory. `contentType=1` = certificates (`certFiles`), `contentType=2` = inspection reports (`inspectReportFiles`), `contentType=3` = qualification numbers (`authCode`).
   - Real shot images: All returned positions are mandatory.
   - `sameSku=false` → product and SKU real shots differ; must provide `specIdList` + corresponding real shots for all SKUs.
   - `sameSku=true` → same real shots for all; only one set needed.
   - `maxPhotoSize` controls the maximum number of real shot images.

---

## 3. Publish Product

### 3.1 Direct Publishing and Listing

Submit product parameter information to `bg.local.goods.add`. If successfully published, product enters review. If it fails, no draft is saved.

**Interface Parameter Explanation:**

| Element | Description | Remarks |
|---|---|---|
| `goodsBasic` | Basic Product Information | |
| `goodsServicePromise` | Merchant Service Information | Stocking, delivery, shipping costs, etc. |
| `goodsProperty` | Product Attributes | Attributes and specifications defining product variants |
| `bulletPoints` | Product Bullet Points | Max 5 selling points, each ≤200 characters |
| `goodsDesc` | Product Description | ≤2000 characters |
| `certificationInfo` | Governance Attributes, Qualification Docs, Real Shot Images | Requires calling compliance template interfaces |
| `guideFileInfo` | Guide file | User manuals (PDF only); check `bg.local.goods.compliance.extra.template.get` for language requirements |
| `goodsSizeChartList` | Size Chart | Parameters determined by `bg.goods.size.element.get` |
| `skuList` | SKU List | |

### 3.2 View Product Publishing Status and Edit

`bg.local.goods.publish.status.get` — Batch query the latest review status based on `goodsId`.

### Origin Information

| Field | Description |
|---|---|
| `originRegion1` | First level address of origin (country or region) |
| `originRegion2` | Secondary address of origin (provincial or state level) — only required when primary address is Chinese Mainland |
| `agreeDefaultOriginRegion` | `true`: Temu fills based on product/merchant info. `false`: Use interface parameters. Default: `false` |

**Default rule:**
1. Prioritize obtaining the manufacturer's address.
2. If unavailable, use the business address.

**Listing of Origin Information:** https://dl.kwcdn.com/upload-common/seller-protocol/45824d2f-aa16-481a-aef5-607039cd79a0

### Requirements for Special Category Products

Based on `bg.local.goods.cats.get` → `expandCatType` and `bg.local.goods.template.get` parameters `additionalInfo` and `needIsbn`:

1. **DVD/CD category**: Mandatory manufacturer information. If country of origin is Chinese Mainland, ISBN code is required. Manufacturer reference: 7150, Manufacturer PID: 2167.
2. **Book category**: Required publisher information.
3. Manufacturer & publisher information must be created in advance on the [Seller Center → Performance → Account health → Copyright] page.
