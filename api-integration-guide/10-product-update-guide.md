# Product Update Guide

**Last update:** 2025-10-26 00:06:45

Both `bg.local.goods.update` and `bg.local.goods.partial.update` can update product data. **Recommended:** use `bg.local.goods.partial.update`.

---

## Guidelines for Modifying Existing SKUs

- The `skuId` **must** be included in `skuList`.
- The following fields **cannot** be modified via these interfaces: `basePrice`, `quantity`, `specIdList`.
- To modify inventory: use `bg.local.goods.stock.edit`.
- To modify price: use `bg.local.goods.priceorder.change.sku.price`.

## Guidelines for Adding New SKUs

- Do **not** include `skuId` for new SKUs.
- Required for new SKUs: `basePrice` (amount/currency), `quantity`, `specIdList`.
- The `specIdList` of the new SKU cannot duplicate any existing SKU's `specIdList`.
- New SKU's corresponding specifications must be provided in `goodsProperties`.
- If `goodsSizeChartList` is affected, upload the updated `goodsSizeChartList`.
- After adding a SKU, **all variant combinations** must have corresponding SKUs.

**Example:** Product has [Black, S] and [Black, M]. Adding "White" requires adding both [White, S] and [White, M].

---

## Interface Description

### `bg.local.goods.update`

- **Must provide ALL product data.** Fields not provided will be **cleared**.
- Before updating, retrieve current product data via `bg.local.goods.detail.query`.
- Items in `skuList` without a `skuId` are treated as new SKUs.

### `bg.local.goods.partial.update`

- Submitted data **overwrites** existing values; data not submitted **remains unchanged**.
- Items in `skuList` without a `skuId` are treated as new SKUs.
- Key difference from full update: only pass the data you want to change; existing SKUs don't need to be re-sent.

### Parameter Rules (both interfaces)

| Parameter | Adding New SKU | Modifying Existing SKU |
|---|---|---|
| `basePrice` | Required (amount + currency) | Must NOT be passed |
| `quantity` | Required (range: [0, 999999]) | Must NOT be passed |
| `specIdList` | Required | Must NOT be passed |
| `outSkuSn` | Optional; if provided must be ≤100 chars, no duplicates | Full update: empty/omit clears it. Partial update: empty clears, omit retains. |

---

## Product Statuses That Do NOT Support Updates

| `goodsStatusFilterType` | `goodsSubStatusFilterType` | Description |
|---|---|---|
| 4 - Incomplete | 4001: Price evaluation in progress | Platform is still evaluating product price |
| 4 - Incomplete | 4002: Auditing and processing | Data processing is ongoing |
| 6 - Deleted | 6001: Non-first release product deleted | Product has been deleted |
| 6 - Deleted | 6002: Price verification terminated product deleted | Product was deleted due to price rejection |

Also: when a product is in "New version processing" status, it cannot be updated. Wait until processing completes.

---

## Demo: Adding SKUs

### Using `bg.local.goods.update`

```json
{
  "goodsId": 604284632545419,
  "goodsBasic": {
    "goodsName": "Product Name"
  },
  "goodsServicePromise": {
    "shipmentLimitDay": 1,
    "fulfillmentType": 1,
    "costTemplateId": "LFT-11620561533419540183"
  },
  "goodsProperty": {
    "goodsProperties": [
      {
        "value": "yellow",
        "parentSpecId": "1001",
        "specId": 72537089
      },
      {
        "value": "black",
        "parentSpecId": "1001",
        "specId": 72260020
      }
    ]
  },
  "skuList": [
    {
      // Existing SKU — has skuId, no basePrice/quantity/specIdList
      "skuId": 58795954861238,
      "listPrice": { "amount": "20", "currency": "EUR" },
      "weight": "1", "length": "1", "width": "1", "height": "1",
      "weightUnit": "g", "volumeUnit": "cm",
      "images": ["https://img-eu.kwcdn.com/local-goods-img/..."]
    },
    {
      // New SKU — no skuId, must have basePrice/quantity/specIdList
      "basePrice": { "amount": "10", "currency": "EUR" },
      "listPrice": { "amount": "30", "currency": "EUR" },
      "listPriceType": 0,
      "specIdList": [72260020],
      "quantity": 100,
      "weight": "12", "weightUnit": "g",
      "length": "213", "width": "32", "height": "23", "volumeUnit": "cm",
      "images": ["https://img-eu.kwcdn.com/local-goods-img/..."]
    }
  ],
  "goodsOriginInfo": {
    "originRegion1": "Albania",
    "agreeDefaultOriginRegion": false
  }
}
```

### Using `bg.local.goods.partial.update`

```json
{
  "goodsId": 604284632545419,
  "goodsBasic": {
    "goodsName": "Product Name"
  },
  "goodsProperty": {
    "goodsProperties": [
      {
        "value": "black",
        "parentSpecId": "1001",
        "specId": 72260020
      }
    ]
  },
  "skuList": [
    {
      // Only pass new SKUs — existing SKUs are not re-sent
      "basePrice": { "amount": "3", "currency": "EUR" },
      "listPrice": { "amount": "100", "currency": "EUR" },
      "listPriceType": 0,
      "quantity": 90,
      "specIdList": [72260020],
      "weight": "2", "weightUnit": "g",
      "length": "2", "width": "2", "height": "2", "volumeUnit": "cm",
      "images": ["https://img-eu.kwcdn.com/local-goods-img/..."]
    }
  ]
}
```
