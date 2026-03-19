# Return and Refund Guide

**Last update:** 2026-01-28 05:10:18

---

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

#### 
**Important Status of parentAfterSalesStatus.[****bg.aftersales.parentaftersales.list.get****]**

PA orders(parent after-sales orders) should primarily be handled based on the PA status.

Each PA order has **one unique PA status** (`parentAfterSalesStatus`), but it **may belong to multiple PA status groups** (`afterSalesStatusGroup`).

PA status groups are **aggregations of PA statuses**.

A single PA order can belong to multiple status groups at the same time.

For example, when the PA status is **1**, it belongs to both the **Pending** and **Requested** status groups.

- 
**parentAfterSalesStatus**

| 

**parentAfterSalesStatus**
 | 

**Description**
 
| 

1 

2 

3 

4 

5 

6 

7 

8 

9 

10

11
 | 

Buyer applied for refund, pending processing

Buyer's return package has been shipped

Return package received, pending merchant processing

Refund initiated, system processing

Refund completed

Buyer canceled after-sales service

Refund request denied

Buyer used merchant-provided shipping label for return, pending merchant review and upload of shipping label

Refund initiated, system processing

Buyer has applied for return

Platform review in progress
 

- 
**afterSalesStatusGroup** (aggregations of **parentAfterSalesStatus**)

| 

**afterSalesStatusGroup**
 | 

Aggregations of **parentAfterSalesStatus**
 
| 

1

2

3

4

5

6

7
 | 

Pending: PA statuses 1, 3, 8

Requested:  PA statuses 1, 10

Package Shipped:  PA statuses 2

Platform Reviewing:  PA statuses 11

Refunded:  PA statuses 5

Rejected:  PA statuses 7

Cancelled:  PA statuses 6
 

#### 
**Other Status Enumeration value**

- 
**afterSalesReasonCode.****[temu.aftersales.parentaftersales.detail.get]**

| 

**afterSalesReasonCode**
 | 

Description
 
| 

2    

4    

8    

11   

14   

15   

17   

18   

19   

22   

23   

24   

25   

26   

27   

28   

34   

36   

40   

41   

42   

44   

46   

47   

48   

49   

51   

52   

53   

54   

55   

56   

57   

58   

59   

60   

61   

40001

40002

40004

40005

40006

40007

40008

40009

40010

40012

40013

40014

40015

40016

40017

40018

40019

40020

40021

40022
 | 

 Order created by mistake

 Forgot to apply coupons

 Fabric/material not as expected

 Color/Pattern not as expected

 Item defective or doesn't work

 Wrong item was sent

 Better price available

 Inaccurate website description

 Item arrived too late

 Missing item

 Product damaged, but shipping box OK

 Product and shipping box both damaged

 Item(s) would not arrive on time

 Need to change payment method

 Didn't approve purchase

 Found cheaper somewhere else

 No longer needed

 Missing or broken parts

 Price adjustment refund

 Shipping cost too high

 Item price too high

 Poor Condition/Presentation

 Need to change shipping address

 Need to change shipping speed

 Need to change billing address

 Bought by mistake

 Defective item

 Style not as expected

 Bought wrong style/color

 Too large/long

 Too small/short

 Missing or loose stone

 Broken or malfunctioning clasp

 Tarnished/unacceptable condition

 Price match refund

 Received the wrong package

 No reason given

 Refund from risk control department

 "Incorrect recipient information 

 Out of stock

 Payment rejected

 Refund shipping

 Delivery failure

 "No available delivery options 

 Refund Tax

 Haven't received the package

 Payment rejected notice

 Cancel free gift

 Received extra return item

 Capture failed

 Interest fee refund

 refund after recharge on advanced refu

 Missed fulfillment promise

 Provider accepted the chargeback

 Refund sign on delivery fee

 Service fee refund general reason code

 Unable to sell due to product issue
