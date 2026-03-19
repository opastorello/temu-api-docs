# Special Category Requirements

**Last update:** 2026-02-13 10:17:44

---

In `bg.local.goods.cats.get`, the `expandCatType` field indicates special category types:
- `0` = Apparel
- `1` = Others
- `2` = Books
- `3` = DVD
- `4` = CD
- `5` = Seed

Certain categories have additional requirements when listing products.

---

## Books Category

### Required Attribute: Publisher

Publisher information must be created in advance in:
**Seller Center → Products → Brands & Intellectual Property → Copyright**

> Note: This attribute's `controlType=0` (Input only) in `temu.local.product.attributes.get` — the value provided in `goodsProperty.value` must already exist in the seller's TEMU shop. If not found, the Publisher attribute will be considered empty.

### Require ISBN

**`temu.local.goods.v2.add`:**

| Property | Description |
|---|---|
| `barCodeType` | External product code type: 1=EAN, 2=UPC, **3=ISBN**, 4=GTIN-14 |
| `barCodeId` | External goods code. Must conform to encoding type standards. `barCodeType` must be `3`. `barCodeId` must match actual book information. Verify at: https://eancheck.com/ |

**`bg.local.goods.add`:**

| Property | Description |
|---|---|
| `externalProductType` | External product code type: 1=EAN, 2=UPC, **3=ISBN**, 4=GTIN-14 |
| `externalProductId` | External goods code. `externalProductType` must be `3`. Must match actual book information. Verify at: https://eancheck.com/ |

---

## DVD and CD Category

### Required Attribute: Studio/Manufacturer

Studio/Manufacturer must be created in advance in:
**Seller Center → Products → Brands & Intellectual Property → Copyright**

### Require ISBN (Conditional)

Required if the copyright information selected in "Studio/Manufacturer" is configured with **China** as "Manufacturer's country of origin".

Same ISBN fields as Books category above apply for both `temu.local.goods.v2.add` and `bg.local.goods.add`.

---

## Additional Notes

> EAN, UPC, GTIN-14 are optional fields and are not subject to mandatory validation constraints during product creation. No additional special requirements apply to other categories at this time.
