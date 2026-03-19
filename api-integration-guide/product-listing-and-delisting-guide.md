# Product Listing and Delisting Guide

# 

Overview

Listing and delisting products are common operations. Sellers may perform these actions for various reasons.

# 

How to Integrate Listing and Delisting

**Step 1: Query the Current Product Status**

Use `bg.local.goods.list.query` or `temu.local.goods.list.retrieve` to retrieve the current product status. The status enumeration values are provided in the response fields. Below is a list of enumeration values. In `temu.local.goods.list.retrieve`, the `2005` and `2006` statuses have been merged into status `2002`.

****

****

****

| goodsStatusFilterType | goodsSubStatusFilterType | Description |
|---|---|---|
| 1-Active | 2001: On sale | The product is available for sale and visible to customers on the platform. |
| 1-Active | 2002: On sale - need to supplement materials within the specified time | The product is available for sale and visible to customers on the platform, but additional materials must be provided within the specified period. |
| 1-Active | 2005: On sale - waiting category rectification | The product is available for sale and visible to customers on the platform, but its incorrect category must be corrected. |
| 1-Active | 2006: On sale - waiting sku multiset rectification | The product is available for sale and visible to customers on the platform, but some product information needs to be modified. |
| 1-Active | 2101: On sale - single sku goods and has low traffic status | The product is available for sale and visible to customers on the platform, but the price needs to be adjusted to improve traffic. |
| 1-Inactive | 3001: Off sale due to punishment | The product was taken offline after publication because its information did not meet platform requirements or due to other data processing reasons. |
| 1-Inactive | 3002: Off sale due to operation | The product has been taken offline after publication, either manually or following the completion of system audits. |
| 1-Inactive | 3003: Sold out | The product has been taken offline after being published because it is sold out, and it will be displayed as sold out to customers. |
| 1-Inactive | 3004: inactive high price | The product has been delisted after publication because of pricing issues. |
| 4-Incomplete | 4001: Price evaluation in progress | The product has not been successfully published because the platform is still evaluating its price. |
| 4-Incomplete | 4002: Auditing and processing | The product is still in the process of being published because data processing is ongoing. |
| 4-Incomplete | 4003: Price evaluation failed | The product has not been successfully published because the platform has not accepted the price. |
| 4-Incomplete | 4004: Product to be completed | The product has not been successfully published due to system audit failure or other data processing reasons. |
| 5-Draft | 5001: New draft not submitted | The product has not yet been submitted for publication. |
| 6-Deleted | 6001: Non-first release product deleted | The product has been deleted. |
| 6-Deleted | 6002: Price verification terminated product deleted | The product was deleted due to price rejection. |

**Step 2: Use **`**bg.local.goods.sale.status.set**`** to Set the Status**

- 

**Listing Operation**

Change the status of delisted products to "*Inactive*." Products in "*Draft*" or "*Incomplete*" status cannot be set to "*Active*." Similarly, products delisted due to compliance reasons cannot be listed. For detailed reasons, you can check the Seller Center or obtain the information from the sub-status field.

```
{  
 "access_token": "uplkbmf5vg0myfpxf4zwrqsc4ckchfcpliybejcpjfbv8pnruu67bibgfkk",  
 "app_key": "4ebbc9190ae410443d65b4c2faca981f",  
 "data_type": "JSON",  
 "goodsId": 602445044379954,  
 "onsale": 1,  
 "sign": "53DBAC46FA841B0678709DE76585366A",  
 "timestamp": 1734009735,  
 "type": "bg.local.goods.sale.status.set"  
}
```

- 

**Delisting Operation**

Change the status from "*Active*" to "*Inactive*," with a sub-status of `3002: Off sale due to operation`.

```
{  
 "access_token": "uplkbmf5vg0myfpxf4zwrqsc4ckchfcpliybejcpjfbv8pnruu67bibgfkk",  
 "app_key": "4ebbc9190ae410443d65b4c2faca981f",  
 "data_type": "JSON",  
 "goodsId": 602445044379954,  
 "onsale": 0,  
 "sign": "53DBAC46FA841B0678709DE76585366A",  
 "timestamp": 1734009735,  
 "type": "bg.local.goods.sale.status.set"  
}
```

**-bg.local.goods.sku.list.query/temu.local.sku.list.retrieve**

In `temu.local.sku.list.retrieve`, the `2005` and `2006` statuses have been merged into status `2002`.

****

****

****

| skuStatusFilterType | skuSubStatusFilterType | Description |
|---|---|---|
| 2-Active | 2001: On sale | The product is available for sale and visible to customers on the platform. |
| 2-Active | 2002: On sale - need to supplement materials within the specified time | The product is available for sale and visible to customers on the platform, but additional materials must be provided within the specified period. |
| 2-Active | 2005: On sale - waiting category rectification | The product is available for sale and visible to customers on the platform, but its incorrect category must be corrected. |
| 2-Active | 2006: On sale - waiting sku multiset rectification | The product is available for sale and visible to customers on the platform, but some product information needs to be modified. |
| 2-Active | 2101: On sale - single sku goods and has low traffic status | The product is available for sale and visible to customers on the platform, but the price needs to be adjusted to improve traffic. |
| 3-Inactive | 3001: Off sale due to punishment | The product was taken offline after publication because its information did not meet platform requirements or due to other data processing reasons. |
| 3-Inactive | 3002: Off sale due to operation | The product has been taken offline after publication, either manually or following the completion of system audits. |
| 3-Inactive | 3003: Sold out | The product has been taken offline after being published because it is sold out, and it will be displayed as sold out to customers. |
| 3-Inactive | 3004: inactive high price | The product has been delisted after publication because of pricing issues. |
