# Co-Warehouse ERP Fulfillment Change Notification Message

## 

Co-Warehouse ERP Fulfillment Change Notification Message

****

****

| Content | Description |
|---|---|
| Message Name | bg_cooperative_warehouse_erp_fulfill_change_push |
| Message Name | Co-Warehouse ERP Fulfillment Change Notification Message |
| Call Direction | Platform → ERP |
| Authorization Required | Yes |
| Data Storage | US/EU |
| Message Description | 1. Co-warehouse order acceptance success or synchronous order placement failure2. Co-warehouse synchronous cancellation success3. Co-warehouse status callback4. Co-warehouse shipping label callback |

### 

Message Content

****

****

****

****

- 

- 

- 

- 

- 

- 

| Message Fields | Parameter Type | Required | Description |
|---|---|---|---|
| mallId | INTEGER | Yes | Mall ID to which the fulfillment order belongs |
| erpFulfillNo | STRING | Yes | ERP Fulfillment Order Number |
| fulfillStatus | INTEGER | Yes | Co-Warehouse Fulfillment Status |
| fulfillCancelStatus | INTEGER | Yes | Fulfillment Order Cancellation Status |
| trackingInfoUpdate | BOOLEAN | Yes | Whether there is an update in the logistics tracking number |
| statusChangeTime | LONG | Yes | Status change time (in milliseconds) |

Access Reference: [https://seller.kuajingmaihuo.com/sop/view/433776571266447655](https://seller.kuajingmaihuo.com/sop/view/433776571266447655)

## 

出库单状态变更消息推送

****

| 消息信息 | 内容 |
|---|---|
| 消息名 | bg_cooperative_warehouse_erp_fulfill_change_push |
| 消息中文名 | 合作仓ERP履约变更回传消息 |
| 调用方向 | 平台 -> ERP |
| 是否需要授权 | 是 |
| 数据存储 | US / EU |
| 消息说明 | 1. 合作仓接单成功或同步下单失败2. 合作仓同步取消成功3. 合作仓状态回传4. 合作仓运单回传 |

### 

消息内容

****

****

****

- 

- 

- 

- 

- 

- 

| 消息字段 | 参数类型 | 是否必填 | 说明 |
|---|---|---|---|
| mallId | INTEGER | 是 | 履约单号所属mallId |
| erpFulfillNo | STRING | 是 | ERP履约单号 |
| fulfillStatus | INTEGER | 是 | 合作仓履约状态 |
| fulfillCancelStatus | INTEGER | 是 | 履约单取消状态 |
| trackingInfoUpdate | BOOLEAN | 是 | 是否有物流跟踪单号更新 |
| statusChangeTime | LONG | 是 | 状态变更时间（毫秒） |

接入参考：[https://seller.kuajingmaihuo.com/sop/view/433776571266447655](https://seller.kuajingmaihuo.com/sop/view/433776571266447655)
