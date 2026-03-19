# Price Management Guide

**Last update:** 2025-10-11 00:52:47

---

## Overview

Price management is crucial in the sales process, involving competitive analysis, dynamic pricing, promotional strategies, and other aspects. Adjust pricing according to consumer demand and market changes, utilizing promotional activities and discount management.

---

## Price Management Modes

### 1. Incomplete Offers

After product release, the platform evaluates the **base price** to ensure consistency and transparency.

### 2. Pricing Opportunities

After the product goes on sale, the platform evaluates the base price of products being sold, helping merchants optimize pricing strategies and avoid profit losses or sales declines.

### 3. Pricing Modification

The seller modifies the base price of the product.

---

## Price Order Status Codes

| Code | Status |
|---|---|
| `100` | Under review |
| `101` | Awaiting confirmation from the merchant |
| `201` | Through (approved) |
| `202` | Reject pending modification |
| `203` | Merchant confirmation |
| `204` | Merchant initiates modification |
| `205` | Merchant refuses |
| `206` | Reject |

**Action required when status = `101`** (awaiting merchant confirmation).

---

## How to Implement Incomplete Offers Integration

**Step 1:** Call `bg.local.goods.priceorder.query` with `priceOrderType=1` to get pending price tasks.

**Step 2:** Perform task operations:
- **Agree** with platform's suggested price → call `bg.local.goods.priceorder.accept`
- **Reject** the price → call `temu.local.goods.priceorder.reject`
- **Negotiate** (adjust price) → call `bg.local.goods.priceorder.negotiate`, then wait for platform's evaluation

### Restricted Traffic Handling

**Step 1:** Call `temu.local.goods.recommendedprice.query` with `recommendedPriceType=20` to get recommended prices for products with restricted traffic.

**Step 2:** Call `bg.local.goods.priceorder.change.sku.price` to modify the price. Pass the recommended price as `newSupplierPrice`.

---

## How to Implement Pricing Opportunities Integration

**Step 1:** Call `bg.local.goods.priceorder.query` with `priceOrderType=2` to get pending price tasks. Use `priceOrderSubType` to confirm the specific price subtask type.

**Step 2:** Perform task operations:
- **Agree** → call `bg.local.goods.priceorder.accept`
- **Reject** → call `temu.local.goods.priceorder.reject`

**Step 3:** Call `temu.local.goods.appealorder.query` to view price proposal data.

#### Appeal Order Status Codes

| Code | Status |
|---|---|
| `10` | APPEALING |
| `20` | PLATFORM_PASS |
| `30` | PLATFORM_REJECT |
| `40` | PLATFORM_TERMINATE |

**When status = `10` (APPEALING):**
- Accept price: call `bg.local.goods.priceorder.accept`
- Initiate price proposal again: call `temu.local.goods.appealorder.create`

---

## How to Implement Pricing Modification Integration

**Step 1:** Call `bg.local.goods.priceorder.query` with `priceOrderType=2` to check for ongoing tasks.

Only these statuses allow initiating a price modification:
- `201` (Through/Approved)
- `202` (Reject pending modification)
- `203` (Merchant confirmation)
- `205` (Merchant refuses)
- `206` (Reject)

**Step 2:** Call `bg.local.goods.priceorder.change.sku.price` to modify the price.

---

## Notes

- Current `basePrice` can be obtained via `bg.local.goods.sku.list.price.query`.
- `bg.local.goods.sku.list.price.query` is only available to **self-developed sellers** or a small number of third-party service providers.
