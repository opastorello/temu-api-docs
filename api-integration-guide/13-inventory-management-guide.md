# Inventory Management Guide

**Last update:** 2025-01-26 11:13:34

---

## Overview

Inventory management is a critical integrated process. Automated inventory management helps reduce overselling and minimizes loss of sales opportunities. The inventory management API enhances real-time accuracy of inventory updates.

---

## Inventory Management Modes

### Full Inventory Update

Overwrites the inventory value provided in the input parameters, adjusting inventory to the desired value. **Suitable for most scenarios.**

### Incremental Inventory Update

Modifies inventory incrementally — adds the specified value to current inventory (negative values trigger deduction). **Ideal for sellers with established inventory management systems using outbound/inbound documentation.**

---

## How to Implement Inventory Integration

### Step 1: Query Current Inventory Level

Use `bg.local.goods.sku.list.query` to retrieve the current sales inventory value of the SKU.

### Step 2: Determine Update Mode and Value

Choose the appropriate update mode for your business scenario. Use API: `bg.local.goods.stock.edit`.

### Step 3: Submit the Inventory Update Request

**Full inventory update** — use `skuStockTargetList`:

```json
{
  "type": "bg.local.goods.stock.edit",
  "access_token": "uplkbmf5vg0myfpxf4zwrqsc4ckchfcpliybejcpjfbv8pnruu67bibgfkk",
  "app_key": "4ebbc9190ae410443d65b4c2faca981f",
  "data_type": "JSON",
  "goodsId": 603050097881935,
  "sign": "29B41A0038BB8AE9AED1F896CA457CBA",
  "timestamp": 1733997133,
  "skuStockTargetList": [
    {
      "skuId": 51481625557677,
      "stockTarget": 10
    }
  ]
}
```

**Incremental inventory update** — use `skuStockChangeList`:

```json
{
  "type": "bg.local.goods.stock.edit",
  "access_token": "uplkbmf5vg0myfpxf4zwrqsc4ckchfcpliybejcpjfbv8pnruu67bibgfkk",
  "app_key": "4ebbc9190ae410443d65b4c2faca981f",
  "data_type": "JSON",
  "goodsId": 603050097881935,
  "requestUniqueKey": "12321",
  "sign": "5BC9111D9C61C9F65AC0F8D670B4F2DD",
  "timestamp": 1733996761,
  "skuStockChangeList": [
    {
      "skuId": 51481625557677,
      "stockDiff": 10
    }
  ]
}
```

---

## Notes

- **Cannot combine** full and incremental updates for the same SKU in a single request — system error will result.
- **Prevent duplicate requests**: Frequent duplicate inventory requests may trigger multiple operations on the inventory value. Ensure proper **idempotency controls** are in place (use `requestUniqueKey`).
