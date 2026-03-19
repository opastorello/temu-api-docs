# Product Listing and Delisting Guide

**Last update:** 2025-09-09 06:37:09

---

## Overview

Listing and delisting products are common operations that sellers perform for various reasons.

---

## How to Integrate Listing and Delisting

### Step 1: Query the Current Product Status

Use `bg.local.goods.list.query` or `temu.local.goods.list.retrieve` to retrieve the current product status.

> Note: In `temu.local.goods.list.retrieve`, statuses `2005` and `2006` have been merged into status `2002`.

#### Product Status Enum Values (`goodsStatusFilterType` / `goodsSubStatusFilterType`)

| `goodsStatusFilterType` | `goodsSubStatusFilterType` | Description |
|---|---|---|
| 1 - Active | 2001: On sale | Available for sale and visible to customers. |
| 1 - Active | 2002: On sale - need to supplement materials | On sale, but additional materials required within specified period. |
| 1 - Active | 2005: On sale - waiting category rectification | On sale, but incorrect category must be corrected. |
| 1 - Active | 2006: On sale - waiting sku multiset rectification | On sale, but some product information needs modification. |
| 1 - Active | 2101: On sale - single sku goods with low traffic | On sale, but price needs adjustment to improve traffic. |
| 1 - Inactive | 3001: Off sale due to punishment | Taken offline — information didn't meet platform requirements. |
| 1 - Inactive | 3002: Off sale due to operation | Taken offline manually or after system audit completion. |
| 1 - Inactive | 3003: Sold out | Taken offline because sold out — displayed as sold out to customers. |
| 1 - Inactive | 3004: Inactive high price | Delisted due to pricing issues. |
| 4 - Incomplete | 4001: Price evaluation in progress | Not yet published — platform still evaluating price. |
| 4 - Incomplete | 4002: Auditing and processing | Still in process of being published — data processing ongoing. |
| 4 - Incomplete | 4003: Price evaluation failed | Not published — platform has not accepted the price. |
| 4 - Incomplete | 4004: Product to be completed | Not published — system audit failure or other data processing reasons. |
| 5 - Draft | 5001: New draft not submitted | Not yet submitted for publication. |
| 6 - Deleted | 6001: Non-first release product deleted | Product has been deleted. |
| 6 - Deleted | 6002: Price verification terminated product deleted | Product deleted due to price rejection. |

---

### Step 2: Use `bg.local.goods.sale.status.set` to Set the Status

#### Listing Operation (`onsale: 1`)

Change the status of delisted products (Inactive → Active).

**Restrictions:**
- Products in "Draft" or "Incomplete" status **cannot** be set to Active.
- Products delisted due to compliance reasons **cannot** be relisted. Check the Seller Center or `sub-status` field for details.

```json
{
  "type": "bg.local.goods.sale.status.set",
  "access_token": "uplkbmf5vg0myfpxf4zwrqsc4ckchfcpliybejcpjfbv8pnruu67bibgfkk",
  "app_key": "4ebbc9190ae410443d65b4c2faca981f",
  "data_type": "JSON",
  "goodsId": 602445044379954,
  "onsale": 1,
  "sign": "53DBAC46FA841B0678709DE76585366A",
  "timestamp": 1734009735
}
```

#### Delisting Operation (`onsale: 0`)

Change status from Active to Inactive (sub-status `3002: Off sale due to operation`).

```json
{
  "type": "bg.local.goods.sale.status.set",
  "access_token": "uplkbmf5vg0myfpxf4zwrqsc4ckchfcpliybejcpjfbv8pnruu67bibgfkk",
  "app_key": "4ebbc9190ae410443d65b4c2faca981f",
  "data_type": "JSON",
  "goodsId": 602445044379954,
  "onsale": 0,
  "sign": "53DBAC46FA841B0678709DE76585366A",
  "timestamp": 1734009735
}
```

---

## SKU Status Enum Values

For `bg.local.goods.sku.list.query` / `temu.local.sku.list.retrieve`:

> Note: In `temu.local.sku.list.retrieve`, statuses `2005` and `2006` have been merged into `2002`.

| `skuStatusFilterType` | `skuSubStatusFilterType` | Description |
|---|---|---|
| 2 - Active | 2001: On sale | Available for sale and visible to customers. |
| 2 - Active | 2002: On sale - need to supplement materials | On sale, but additional materials required. |
| 2 - Active | 2005: On sale - waiting category rectification | On sale, but category must be corrected. |
| 2 - Active | 2006: On sale - waiting sku multiset rectification | On sale, but some info needs modification. |
| 2 - Active | 2101: On sale - low traffic | On sale, but price needs adjustment to improve traffic. |
| 3 - Inactive | 3001: Off sale due to punishment | Taken offline — didn't meet platform requirements. |
| 3 - Inactive | 3002: Off sale due to operation | Taken offline manually or after system audit. |
| 3 - Inactive | 3003: Sold out | Taken offline because sold out. |
| 3 - Inactive | 3004: Inactive high price | Delisted due to pricing issues. |
