# The event of webhook

**1. bg_order_status_change_event**

| Properties | Type | Description |
|---|---|---|
| mallId | LONG | mall id |
| parentOrderSn | STRING | parent Order number |
| orderSn | STRING | Order number |
| orderStatus | INTEGER | Order Status |
| updateTime | INTEGER | Order update time, timestamp in seconds |

**2. bg_trade_logistics_address_changed**

| Properties | Type | Description |
|---|---|---|
| mallId | LONG | mall id |
| parentOrderSn | STRING | parent order number |

**3. bg_aftersales_status_change**

| Properties | Type | Description |
|---|---|---|
| mallId | LONG | mall id |
| afterSalesType | INTEGER | After-sales type: 1-Refund only; 2-Return and refund |
| parentAfterSalesSn | STRING | parent After sales order number |
| parentOrderSn | STRING | parent Order number |
| updateAt | LONG | Status update time, millisecond timestamp |
| applyOperatorRole | INTEGER | After-sales source: 1-user; 2-merchant; 3-platform customer service; 4-system |
| parentAfterSalesStatus | INTEGER | After-sales order status after the change: 1-The buyer applied for a refund, pending processing; 5-Refunded; 6-The buyer has cancelled the after-sales service; 7-Rejected; 8-The buyer returns the goods using the waybill provided by the merchant, waiting for the merchant to review and upload the waybill; 10-The buyer has applied for a return |

**4. bg_cancel_order_status_change**

| Properties | Type | Description |
|---|---|---|
| mallId | LONG | mall id |
| parentAfterSalesSn | STRING | parent After sales order number |
| parentOrderSn | STRING | parent Order number |
| parentAfterSalesStatus | INTEGER | Changed after-sales order status: 5-Refunded |
| updateAt | LONG | Status update time, millisecond timestamp |
| applyOperatorRole | INTEGER | After-sales initiation source: 1-user; 2-merchant; 3-platform customer service; 4-system |
