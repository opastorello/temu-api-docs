# Return and Refund Guide

#### 

**Return and Refund Interfaces:**

Our interfaces provide the ability to view return details, upload shipping labels and issue refunds in Temu Seller Center.

#### 

**Interface Limitations vs. Temu Seller Center**

- 

Reject return requests is not supported. 

- 

Issue a partial refund or refuse to issue a refund(includes upload proof of your refusal to issue a refund) is not supported.

- 

Initiate an appeal to file a claim is not supported.

#### 

**API workflow**

![image](https://bstatic.kwcdn.com/open-outer/21a488cbd6/e377a3f9bf4b00c6167add7e4419438f)

#### 

**Important Status of parentAfterSalesStatus.[****bg.aftersales.parentaftersales.list.get****]**

PA orders(parent after-sales orders) should primarily be handled based on the PA status.

Each PA order has **one unique PA status** (`parentAfterSalesStatus`), but it **may belong to multiple PA status groups** (`afterSalesStatusGroup`).

PA status groups are **aggregations of PA statuses**.

A single PA order can belong to multiple status groups at the same time.

For example, when the PA status is **1**, it belongs to both the **Pending** and **Requested** status groups.

- 

**parentAfterSalesStatus**

****

****

| parentAfterSalesStatus | Description |
|---|---|
| 1 2 3 4 5 6 7 8 9 1011 | Buyer applied for refund, pending processingBuyer's return package has been shippedReturn package received, pending merchant processingRefund initiated, system processingRefund completedBuyer canceled after-sales serviceRefund request deniedBuyer used merchant-provided shipping label for return, pending merchant review and upload of shipping labelRefund initiated, system processingBuyer has applied for returnPlatform review in progress |

- 

**afterSalesStatusGroup** (aggregations of **parentAfterSalesStatus**)

****

****

| afterSalesStatusGroup | Aggregations of parentAfterSalesStatus |
|---|---|
| 1234567 | Pending: PA statuses 1, 3, 8Requested:  PA statuses 1, 10Package Shipped:  PA statuses 2Platform Reviewing:  PA statuses 11Refunded:  PA statuses 5Rejected:  PA statuses 7Cancelled:  PA statuses 6 |

#### 

**Other Status Enumeration value**

- 

**afterSalesReasonCode.****[temu.aftersales.parentaftersales.detail.get]**

****

| afterSalesReasonCode | Description |
|---|---|
| 2    4    8    11   14   15   17   18   19   22   23   24   25   26   27   28   34   36   40   41   42   44   46   47   48   49   51   52   53   54   55   56   57   58   59   60   61   4000140002400044000540006400074000840009400104001240013400144001540016400174001840019400204002140022 | Order created by mistake Forgot to apply coupons Fabric/material not as expected Color/Pattern not as expected Item defective or doesn't work Wrong item was sent Better price available Inaccurate website description Item arrived too late Missing item Product damaged, but shipping box OK Product and shipping box both damaged Item(s) would not arrive on time Need to change payment method Didn't approve purchase Found cheaper somewhere else No longer needed Missing or broken parts Price adjustment refund Shipping cost too high Item price too high Poor Condition/Presentation Need to change shipping address Need to change shipping speed Need to change billing address Bought by mistake Defective item Style not as expected Bought wrong style/color Too large/long Too small/short Missing or loose stone Broken or malfunctioning clasp Tarnished/unacceptable condition Price match refund Received the wrong package No reason given Refund from risk control department "Incorrect recipient information  Out of stock Payment rejected Refund shipping Delivery failure "No available delivery options  Refund Tax Haven't received the package Payment rejected notice Cancel free gift Received extra return item Capture failed Interest fee refund refund after recharge on advanced refu Missed fulfillment promise Provider accepted the chargeback Refund sign on delivery fee Service fee refund general reason code Unable to sell due to product issue |
