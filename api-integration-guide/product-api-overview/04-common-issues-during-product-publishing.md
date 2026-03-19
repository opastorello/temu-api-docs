# Common Issues During Product Publishing

**Last update:** 2025-07-14 23:53:23

During the product publishing process, the following common issues may arise. This guide describes frequently encountered errors to help developers quickly identify and resolve problems.

---

## 1. Incorrect `importDesignation` Value

**Error Message:** `"Invalid Request Parameters"`

**Requirement:** The following four values are supported exactly (case-sensitive, exact spacing):
- `"Imported"`
- `"Made in the USA"`
- `"Made in the USA and Imported"`
- `"Made in the USA or Imported"`

**Error Example:**
```json
"goodsBasic": {
  "catId": 28949,
  "goodsName": "...",
  "importDesignation": "imported"
}
```
*Cause: First letter was lowercase.*

---

## 2. `outSkuSn` and `outGoodsSn` Length Issue

**Requirement:** `outSkuSn` and `outGoodsSn` must be ≤ 100 characters.

**Error Example:**
```json
"skuList": [
  {
    "outSkuSn": "101 chars is too long for the out sku sn..."
  }
]
```

---

## 3. Issues with Images, Videos, and Links

**Requirement:**
- The backend validates size, dimensions, and ratio of images and videos.
- Links must be publicly accessible.
- The `image` field requires at least **3 distinct images**.

**Error Example:**
```json
"images": [
  "https://img.kwcdn.com/...",
  "https://img.kwcdn.com/...",
  "https://img.kwcdn.com/..."
]
```
*Cause: The link must be accessible (3 identical links provided).*

---

## 4. Issues with Qualification Links

**Error:** `"Invalid Request Parameters"`

**Requirement:** Qualification-related files and images are signed with `mallId`. Switching stores renders the links unusable.

**Error Example:** The qualification file for Store A was used for Store B.

---

## 5. `specIdList` in SKU List vs `specId` in `goodsProperties`

**Error:** `"System error, please try again later"`

**Requirement:**
- Each SKU's `specIdList` should contain at least 1 and no more than 2 `specId`s.
- Each `specId` in the SKU must also be listed in `goodsProperties`.

**Error Causes:**
1. Not all `specId` in SKU are listed in `goodsProperties`.
2. Each SKU has more than two `specId`.

---

## 6. `costTemplateId` is Linked to `mallId`

**Requirement:** Each store has its own shipping template. When adding products, the store's shipping template is validated against `costTemplateId`. Do not mix shipping templates across stores.

---

## 7. Field Type Issues

**Requirement:**
- The `weight`, `length`, `width`, and `height` fields in `skuList` must be of type **String**, not Integer.
- Volume: integer part ≤ 3 digits, decimal part ≤ 1 digit.
- Weight: integer part ≤ 4 digits, decimal part ≤ 1 digit.

**Error Cause:** `weight`, `length`, `width`, `height` were incorrectly entered as Integer types.

---

## 8. Missing Trademark Information

**Error:** `"Invalid Request Parameters"`

**Cause:** If the product attribute includes a brand (`name=brand`, `templatePid=597281`, `refPid=1960`), trademark information must be included when adding the product.

---

## 9. Incorrect Attribute Field Mapping

**Error:** `"Invalid Request Parameters"`

**Cause:** The product attribute template returned `templatePid=597281`, but when adding the product, `templatePid` was incorrectly set to `504023`.

**Rule:** When adding a product, all relevant attribute fields must exactly match the fields returned by the template interface.
