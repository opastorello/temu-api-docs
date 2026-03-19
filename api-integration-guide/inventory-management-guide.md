# Inventory Management Guide

# 

Overview

Inventory management is a critical integrated process. Automated inventory management helps reduce overselling and minimizes the loss of sales opportunities. To achieve this, we provide an inventory management API designed to enhance the real-time accuracy of inventory updates, ensuring the objectives mentioned above are met.

# 

Inventory Management Modes

We offer two methods for inventory updates:

- 

**Full Inventory Update**

This operation overwrites the inventory value provided in the input parameters, adjusting the inventory level to the desired value. This method is suitable for most scenarios.

- 

**Incremental Inventory Update**

This operation modifies the inventory incrementally. Once the request is made, the system adds the specified inventory value in the input parameters to the current inventory level (negative values will trigger a deduction). This update method is ideal for sellers who have a well-established inventory management system using outbound and inbound documentation. You only need to input the inventory change value from the respective documentation in the request.

# 

How to Implement Inventory Integration

The integration involves the following three steps:

**Step 1: Query the Current Inventory Level of the Product SKU**

Use `bg.local.goods.sku.list.query` to retrieve the current sales inventory value of the SKU to be updated.

**Step 2: Determine the Update Mode and Inventory Value to Be Updated**

Choose the appropriate update mode based on your business scenario. Use the API `bg.local.goods.stock.edit`.

**Step 3: Submit the Inventory Update Request**

- 

For a full inventory update, include the inventory value in the `skuStockTargetList` object. Below is a sample request.

```
{  
 "access_token": "uplkbmf5vg0myfpxf4zwrqsc4ckchfcpliybejcpjfbv8pnruu67bibgfkk",  
 "app_key": "4ebbc9190ae410443d65b4c2faca981f",  
 "data_type": "JSON",  
 "goodsId": 603050097881935,  
 "sign": "29B41A0038BB8AE9AED1F896CA457CBA",  
 "skuStockTargetList": [  
  {  
   "skuId": 51481625557677,  
   "stockTarget": 10  
  }  
 ],  
 "timestamp": 1733997133,  
 "type": "bg.local.goods.stock.edit"  
}
```

1. 

Similarly, for an incremental inventory update, include the inventory value in the `skuStockTargetList` object. A sample request for incremental updates is also provided below.

```
{  
 "access_token": "uplkbmf5vg0myfpxf4zwrqsc4ckchfcpliybejcpjfbv8pnruu67bibgfkk",  
 "app_key": "4ebbc9190ae410443d65b4c2faca981f",  
 "data_type": "JSON",  
 "goodsId": 603050097881935,  
 "requestUniqueKey": "12321",  
 "sign": "5BC9111D9C61C9F65AC0F8D670B4F2DD",  
 "skuStockChangeList": [  
  {  
   "skuId": 51481625557677,  
   "stockDiff": 10  
  }  
 ],  
 "timestamp": 1733996761,  
 "type": "bg.local.goods.stock.edit"  
}
```

**Notes:**

- 

It is not possible to perform both a full inventory update and an incremental inventory update for the same SKU in a single request, as this will result in a system error.

- 

Frequent duplicate inventory requests may lead to multiple operations on the inventory value. To prevent such issues, ensure proper idempotency controls are in place.
