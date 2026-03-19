# How to Release a Product?

**Last update:** 2025-10-11 00:52:54

---

## Overview

The Product API helps sellers manage their product catalog at scale. Using the Product API, a seller can create products.

### APIs Involved in Product Release

| API Name | Overview |
|---|---|
| `bg.local.goods.cats.get` | Get the complete category of TEMU |
| `bg.local.goods.template.get` | Obtain attribute/variant data corresponding to TEMU category |
| `bg.local.goods.spec.id.get` | Generate custom variant specification IDs |
| `bg.local.goods.size.element.get` | Whether to fill in the size chart and requirements for categories |
| `bg.local.goods.image.upload` | Upload product images |
| `bg.local.goods.gallery.signature.get` | Upload product videos, files, and images |
| `bg.local.goods.compliance.property.check` | Verify whether product attributes comply with the site's sales rules |
| `bg.local.goods.tax.code.get` | Obtain the product tax code |
| `bg.local.goods.out.sn.check` / `bg.local.goods.sku.out.sn.check` | Verify if external product code / SKU code are duplicated |
| `bg.freight.template.list.query` | Get the seller's shipping template |
| `temu.local.goods.brand.trademark.V2.get` | Obtain the brand information registered by the seller |
| `temu.local.goods.sku.net.content.unit.query` | Obtain SKU net content unit information |
| `temu.local.goods.illegal.vocabulary.check` | Verify whether there are violations in product name, description, etc. |
| `bg.local.goods.compliance.rules.get` / `bg.local.goods.compliance.extra.template.get` | Query product compliance and governance attribute requirements |
| `bg.local.goods.compliance.info.fill.list.query` | Obtain product compliance information and fill in |
| `bg.local.goods.add` | Create a new product |

---

## Notes on Product Release Fields

### goodsBasic (Required)

| Field | Required | How to Fill | Notes |
|---|---|---|---|
| `goodsName` | True | User inputs | Only English letters, numbers, symbols. No decorative chars. Max 500 chars. Use `temu.local.goods.illegal.vocabulary.check` to pre-validate. |
| `catId` | True | From `bg.local.goods.cats.get` | Use leaf category ID. `catType=0`=Apparel, `catType=1`=Non-Apparel. Only `availableStatus=0` categories are sellable. |
| `goodsGallery.detailVideo` | False | User inputs | Max 1 video. Duration ≤180s. Ratio: 1:1, 4:3, 16:9. Resolution ≥720P. Size ≤300MB. Formats: wmv, avi, 3gp, mov, mp4, flv, rmvb, mkv, m4v. |
| `goodsGallery.detailImage` | False | User inputs | Max 49 images. Ratio ≥1:3. Width/Height ≥480px. Size ≤3MB. Formats: JPEG, JPG, PNG. Convert with `bg.local.goods.image.upload`. |
| `goodsGallery.carouselVideo` | False | User inputs | Max 1. Duration ≤60s. Resolution ≥720P. Size ≤100MB. |
| `outGoodsSn` | False | User inputs | External product code. Must be unique in store. Max 100 chars. Verify with `bg.local.goods.out.sn.check`. |

### goodsServicePromise (Required)

| Field | Required | How to Fill | Notes |
|---|---|---|---|
| `shipmentLimitDay` | True | User inputs | Days from order receipt to shipment. Default: 1 or 2. |
| `fulfillmentType` | True | User inputs | Delivery Method: `1` = Self-fulfillment (fixed). |
| `costTemplateId` | True | From `bg.freight.template.list.query` | User must create shipping template in Seller Center first. |

### goodsProperty (Required)

Obtained from `bg.local.goods.template.get`. Very complex — includes normal attributes (`isSale=false`) and variant attributes (`isSale=true`).

- **Required attributes**: Pass attributes where `required=True` per `bg.local.goods.template.get`.
- **Parent-child attributes**: `showType=0` = parent; `showType=1` = child.
- **controlType**: Determines how child attributes are triggered.
- **Units**: When units available, include both `valueUnitId` and `valueUnit`.
- Use `bg.local.goods.compliance.property.check` to pre-validate.

### goodsOriginInfo (Optional but needed for sale)

| Field | Required | Notes |
|---|---|---|
| `originRegion1` | False | Origin enum; see docs |
| `originRegion2` | False | Required when originRegion1 = China |
| `agreeDefaultOriginRegion` | False | `true` = auto-fill from manufacturer/business address |
| `proofImageUrls` | False | Size ≤3MB. JPG/PNG/JPEG. Convert with `bg.local.goods.image.upload`. |

### bulletPoints (Optional)

Max 6 lines, max 700 chars. English letters/numbers/symbols only. Pre-validate with `temu.local.goods.illegal.vocabulary.check`.

### goodsDesc (Optional)

Detailed product description. Max 10,000 chars. No rich text. Pre-validate with `temu.local.goods.illegal.vocabulary.check`.

### certificationInfo (Optional but required before sale)

Compliance qualifications. Source: `bg.local.goods.compliance.rules.get` for required types.

**contentType codes for extraTemplate:**
- `1` = qualification certificate (use `certFiles`)
- `2` = inspection report (use `inspectReportFiles`)
- `3` = qualification code (use `authCodes`)
- `4` = actualPhoto
- `5` = selectedCheckItems
- `6` = EU energyLabel

### guideFileInfo (Optional)

Product manual (PDF). English version required. Upload via file upload interface. `lang2GuideFileUrl` format:
```json
{
  "lang2GuideFileUrl": {
    "en": "",
    "es": "",
    "de": ""
  }
}
```

### skuList (Required)

| Field | Required | Notes |
|---|---|---|
| `basePrice` | True | Seller price. See currency docs per site. |
| `listPrice` | False/True | Recommended retail price (≥basePrice). If `listPriceType=1`, no listPrice needed. If empty/`0`, listPrice is required. |
| `quantity` | True | Inventory. Range: [0, 999999]. |
| `specIdList` | True | Variant identifiers (color, size, etc.). If `inputMaxSpecNum>0` = custom allowed. Use `bg.local.goods.spec.id.get` for custom spec IDs. |
| `outSkuSn` | False | External SKU ID. Max 100 chars. Must be unique. Verify with `bg.local.goods.sku.out.sn.check`. |
| `weight` | True | See site-specific requirements. |
| `weightUnit` | True | See site-specific requirements. |
| `length`/`width`/`height` | True | See site-specific requirements. |
| `volumeUnit` | True | See site-specific requirements. |
| `images` | True | **Apparel**: 3:4, ≥1340×1785px. **Non-Apparel**: 1:1, ≥800×800px. Size ≤3MB. JPEG/JPG/PNG. Upload via `bg.local.goods.image.upload`. |
| `externalProductType` | False | 1=EAN, 2=UPC, 3=ISBN, 4=GTIN-14 |
| `externalProductId` | False | Required when `externalProductType` set. |
| `referenceLink` | False | Links to same product on other platforms. |

#### multiplePackage sub-fields

| Field | Notes |
|---|---|
| `skuClassification` | 1=Single Product, 2=Combination, 3=Mixed |
| `numberOfPieces` | [1,100] |
| `pieceUnitCode` | 1=Piece, 2=Pair, 3=Bag |
| `originNetContentNumber` | Physical unit quantity for unit price calc. Max 3 decimal places. |
| `netContentUnitCode` | Unit for net content. Get from `temu.local.goods.sku.net.content.unit.query`. |
| `individuallyPacked` | Required for `skuClassification=2` or `3`. |

### goodsTrademark (Optional)

Use `temu.local.goods.brand.trademark.V2.get` to get `brandId` and `trademarkId`. Must be pre-approved in Seller Center.

### taxCodeInfo (Optional)

Use `bg.local.goods.tax.code.get`. Different categories have different tax rate codes.

### secondHand (Optional)

Requires prior approval from TEMU. Check via `bg.local.goods.cats.get` — `secondHandCategory=true` if eligible.
- `level`: 1=usedLikeNew, 2=usedVeryGood, 3=usedGood, 4=UsedAcceptable.

---

## Test Product Categories

Recommended for testing product publishing:

| catId | Category |
|---|---|
| `29069` | Clothing, Shoes & Jewelry / Women / Clothing / Tops, Tees & Blouses / T-Shirts |
| `44936` | Books / Arts & Photography / History & Criticism / Criticism |
| `24388` | Cell Phones & Accessories / Cell Phones |
