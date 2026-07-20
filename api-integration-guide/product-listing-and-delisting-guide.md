# Product Listing and Delisting Guide

# 

bg.local.goods.sku.list.query

Request:

| Parameter | Type | Enum |
|---|---|---|
| skuSearchType | Integer | SKUSearchTypeEnum：1=ALL, 2=Active, 3=InActive, 4=INCOMPLETE, 5=DRAFT, 6=DELETED, 7=LATEST |
| statusFilterType | Integer | StatusFilterEnum：1=OUT_OF_STOCK ~ 14=DELETED_BASE_PRICE_REFUSED |
| skuStatusFilterType | Integer | SKUSearchTypeEnum：1=ALL, 2=Active, 3=InActive, 4=INCOMPLETE, 5=DRAFT, 6=DELETED, 7=LATEST |
| skuSubStatusFilterType | Integer | SkuSubStatusFilterEnum：2001=ACTIVE ~ 6002=DELETED_BASE_PRICE_REFUSED |

| skuStatusFilterType | skuSubStatusFilterType | Description |
|---|---|---|
| 2-Active | 2001: On sale | The product is available for sale and visible to customers on the platform. |
| 2-Active | 2002: On sale - need to supplement materials within the specified time | The product is available for sale and visible to customers on the platform, but additional materials must be provided within the specified period. |
| 2-Active | 2003: On sale - out of stock | The product is on-shelf with no stock. |
| 2-Active | Not available by SKU level | The product is available for sale and visible to customers on the platform, but its incorrect category must be corrected. |
| 2-Active | Not available by SKU level | The product is available for sale and visible to customers on the platform, but some product information needs to be modified. |
| 2-Active | 2101: On sale - single sku goods and has low traffic status | The product is available for sale and visible to customers on the platform, but the price needs to be adjusted to improve traffic. |
| 3-Inactive | 3001: Off sale due to punishment | The product was taken offline after publication because its information did not meet platform requirements or due to other data processing reasons. |
| 3-Inactive | 3002: Off sale due to operation | The product has been taken offline after publication, either manually or following the completion of system audits. |
| 3-Inactive | 3003: Sold out | The product has been taken offline after being published because it is sold out, and it will be displayed as sold out to customers. |
| 3-Inactive | 3004: inactive high price | The product has been delisted after publication because of pricing issues. |

Response:

| Parameter | Type | Enum |
|---|---|---|
| status4VO | Integer | SKUSearchTypeEnum：2=Active, 3=InActive, 4=INCOMPLETE |
| subStatus4VO | Integer | StatusFilterEnum：1=OUT_OF_STOCK ~ 14=DELETED_BASE_PRICE_REFUSED |
| skuShowSubStatus4VO | Integer | GoodsSubStatusShowEnum: 2001, 2002, 2005, 2006, 3001, 3002, 3003, 3004 |

## 

temu.local.sku.list.retrieve

Request:

| Parameter | Type | Enum |
|---|---|---|
| skuSearchType | String | OpenapiSkuStatusFilterTypeEnum："ALL", "ACTIVE", "INACTIVE", "INCOMPLETE", "DRAFT", "DELETED" |

Response:

| Parameter | Type | Enum |
|---|---|---|
| skuStatus | String | OpenapiSkuStatusFilterTypeEnum："ACTIVE", "INACTIVE", "INCOMPLETE", "DRAFT", "DELETED" |
| skuSubStatus | String | OpenapiSkuShowSubStatusEnum："ACTIVE", "ACTIVE_AT_RISK", "CLOSE", "BLOCK", "OUT_OF_STOCK", "PRICING_UNDER_ASSESSMENT", "PRODUCT_IN_PROCESS", "PRICING_REQUIRED", "PRODUCT_TO_BE_COMPLETED", "DRAFT", "DELETE_BY_MERCHANT", "DELETED_PRICE_TERMINATION" |

## 

bg.local.goods.list.query

Request:

| Parameter | Type | Enum |
|---|---|---|
| goodsSearchType | Integer | GoodsSearchTypeEnum：1=ALL, 4=INCOMPLETE, 5=DRAFT, 6=DELETED |
| statusFilterType | Integer | StatusFilterEnum：1=OUT_OF_STOCK ~ 14=DELETED_BASE_PRICE_REFUSED |
| goodsStatusFilterType | Integer | GoodsSearchTypeEnum：1=ALL, 4=INCOMPLETE, 5=DRAFT, 6=DELETED |
| goodsSubStatusFilterType | Integer | GoodsSubStatusFilterEnum：2001=ACTIVE ~ 6002=DELETED_BASE_PRICE_REFUSED |

****

****

****

| goodsStatusFilterType | goodsSubStatusFilterType | Description |
|---|---|---|
| 1-Active | 2001: On sale | The product is available for sale and visible to customers on the platform. |
| 1-Active | 2002: On sale - need to supplement materials within the specified time | The product is available for sale and visible to customers on the platform, but additional materials must be provided within the specified period. |
| 1-Active | Not available by SKU level | The product is available for sale and visible to customers on the platform, but its incorrect category must be corrected. |
| 1-Active | Not available by SKU level | The product is available for sale and visible to customers on the platform, but some product information needs to be modified. |
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

Response:

| Parameter | Type | Enum |
|---|---|---|
| status4VO | Integer | SKUSearchTypeEnum/GoodsSearchTypeEnum：2=Active, 3=InActive, 4=INCOMPLETE, 5=DRAFT, 6=DELETED |
| subStatus4VO | Integer | StatusFilterEnum：1=OUT_OF_STOCK ~ 14=DELETED_BASE_PRICE_REFUSED |
| goodsShowSubStatus | Integer | GoodsSubStatusShowEnum：2001=ACTIVE ~ 6002=DELETE_PRICE_TERMINATION |

## 

temu.local.goods.list.retrieve

Request:

| Parameter | Type | Enum |
|---|---|---|
| goodsSearchType | String | OpenapiGoodsStatusFilterTypeEnum："ALL", "ACTIVE", "INACTIVE", "INCOMPLETE", "DRAFT", "DELETED" |

Response:

| Parameter | Type | Enum |
|---|---|---|
| goodsStatus | String | OpenapiGoodsShowStatusEnum："ACTIVE", "INACTIVE", "INCOMPLETE", "DRAFT", "DELETED" |

---

## 

Parameters Enum in Detail

### 

statusFilterType / StatusFilterEnum / subStatus4VO

| Enum | Code | Description |
|---|---|---|
| OUT_OF_STOCK | 1 | Sold out |
| CLOSED | 2 | Manually delisted / Penalty period ended / Penalty cancelled |
| BLOCKED | 3 | Punishment removal |
| ACTIVE_AT_RISK | 4 | Qualification materials must be submitted within the specified timeframe |
| IN_PROCESS | 5 | Processing |
| QUALIFICATION_REVIEW | 6 | Qualification review |
| FAILED | 7 | Release failed |
| ACTIVE | 8 | On-shelf |
| NOT_COMPETITIVELY_PRICED | 9 | Price assessment rejected |
| PRICE_AUDIT_IN_PROCESS | 10 | Price assessment in process |
| APPROVE_IN_PROCESS | 11 | Audit processing |
| SUPPLEMENTARY_REVIEW | 12 | Supplementary review |
| DELETED | 13 | Deleted |
| DELETED_BASE_PRICE_REFUSED | 14 | Refused deletion due to price assessment |

### 

SkuSubStatusFilterEnum

``

| Enum | Code | Description |
|---|---|---|
| ACTIVE | 2001 | Active (listed on the site with inventory greater than 0 + pseudo-active) |
| ACTIVE_AT_RISK | 2002 | Active – Qualification documents must be submitted within the specified time |
| ACTIVE_AT_ON_SALE | 2003 | Listed (including out-of-stock items) |
| ACTIVE_LOW_TRAFFIC | 2101 | Active (low traffic) – Single-SKU product with low traffic status |
| INACTIVE_BLOCKED | 3001 | Delisted due to penalty |
| INACTIVE_CLOSE | 3002 | Delisted by operations (holiday/seller-initiated/operations-initiated/not relisted after penalty removal) |
| INACTIVE_OUT_OF_STOCK | 3003 | Out of stock (listed on the site but inventory is 0) |
| INACTIVE_HIGH_PRICE | 3004 | Delisted due to high price (removed by operations because of pricing) |
| INCOMPLETE_PRICING_UNDER_ASSESSMENT | 4001 | Price verification in progress (from product submission until price verification is completed, excluding rejected price verifications) |
| INCOMPLETE_IN_PROCESS | 4002 | Under review (business review in progress) |
| INCOMPLETE_PRICING_FAILURE | 4003 | Price verification failed (price verification rejected) |
| INCOMPLETE_PRODUCT_TO_BE_COMPLETE | 4004 | Product information incomplete (business review rejected and qualification documents required, or translation/transcoding failed) |
| DELETED_LOCAL_GOODS | 6001 | Non-launch product deleted (localGoods deleted) |
| DELETED_BASE_PRICE_REFUSED | 6002 | Deleted due to price verification rejection (deleted when all price verification requests are rejected) |

### 

GoodsSubStatusShowEnum

| Enum | Code | Description |
|---|---|---|
| ACTIVE | 2001 | Active |
| ACTIVE_AT_RISK | 2002 | Active – Qualification documents must be submitted within the specified time |
| ACTIVE_WAIT_FOR_PUNISHMENT | 2003 | Active – Pending penalty |
| ACTIVE_PUNISHMENT_WARNING | 2004 | Active – Penalty warning |
| ACTIVE_WAITING_CATEGORY_RECTIFICATION | 2005 | Active – Pending category rectification |
| ACTIVE_WAITING_SKU_MULTISET_RECTIFICATION | 2006 | Active – Pending SKU variant rectification |
| ACTIVE_LOW_TRAFFIC | 2101 | Active – Low traffic |
| INACTIVE_BLOCKED | 3001 | Delisted due to penalty |
| INACTIVE_CLOSE | 3002 | Delisted by operations |
| INACTIVE_OUT_OF_STOCK | 3003 | Out of stock |
| INCOMPLETE_PRICING_UNDER_ASSESSMENT | 4001 | Price assessment in progress |
| INCOMPLETE_IN_PROCESS | 4002 | Under review |
| INCOMPLETE_PRICING_FAILURE | 4003 | Price assessment failed |
| INCOMPLETE_PRODUCT_TO_BE_COMPLETE | 4004 | Product information incomplete |
| DRAFT | 5001 | Draft |
| DELETED_LOCAL_GOODS | 6001 | Non-launch product deleted |
| DELETE_PRICE_TERMINATION | 6002 | Deleted due to price assessment termination |
