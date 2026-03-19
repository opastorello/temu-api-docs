# Integration Guide: Placing Outbound Orders from ERP to Partner Warehouses

**Last update:** 2026-02-13 06:06:22

---

# 
**Overview**

This document primarily introduces the relevant interfaces for integrating ERP systems with partner warehouses. It covers pre-integration preparations and interfaces related to placing outbound orders, including partner warehouse authorization inquiry, authorization, and outbound order placement. Orders successfully placed through these interfaces will be marked as "Shipped by Partner Warehouse" in the seller center. When integrating with these interfaces, it is recommended to consult with the product manager of the partner warehouse in advance.

- 
## 
Interface Call Flowchart

## 
Warehouse Outbound Order State Machine

- 
## 
**Status Description**

### 
Fulfillment Order Status（fulfillStatus）

| 

**Status Code**
 | 

**Description**
 | 

**Usage Context**
 
| 

5
 | 

Order Successfully Received by Platform
 | 

IOrder Placement Interface
 
| 

7
 | 

Fulfillment Order Processing
 | 

 Order Placement Interface
 
| 

10
 | 

Order Successfully Received by Partner Warehouse
 | 

Fulfillment Order Query
 
| 

20
 | 

Wave Picking Completed
 | 

 Fulfillment Order Query
 
| 

30
 | 

Sorting Completed
 | 

Fulfillment Order Query
 
| 

40
 | 

Packing Completed
 | 

 Fulfillment Order Query
 
| 

50
 | 

Shipping Completed
 | 

Fulfillment Order Query, III. Order Placement Interface
 
| 

60
 | 

Fulfillment Order Successfully Canceled
 | 

Fulfillment Order Query
 
| 

99
 | 

Fulfillment Order Exception
 | 

Fulfillment Order Query
 

### 
Fulfillment Order Cancellation Status（fulfillCancelStatus）

| 

**Status Code**
 | 

**Description**
 | 

**Usage Context**
 
| 

0
 | 

Not Initiated
 | 

 Fulfillment Order Query
 
| 

10
 | 

Cancelling
 | 

 Fulfillment Order Query
 
| 

20
 | 

Successfully Cancelled
 | 

VFulfillment Order Query
 
| 

99
 | 

Cancellation Failed
 | 

VFulfillment Order Query
 

# 
总览

当前文档主要介绍ERP转合作对接仓的相关接口，包括接入前的准备工作和出库单下单的相关接口，如合作仓授权查询、授权、下出库单等；通过该接口下单成功在订单，卖家中心将会将对应的订单标记为合作仓发货；对接该接口时，建议先找合作对接仓的产品经理进行咨询。

- 
## 
接口调用流程图

### 

- 
## 
出库单状态

### 

- 
## 
状态说明

### 
履约单状态（fulfillStatus）

| 

状态码
 | 

描述
 | 

出现场景
 
| 

5
 | 

平台接单成功
 | 

三、下单接口
 
| 

7
 | 

履约单处理中
 | 

三、下单接口
 
| 

10
 | 

合作仓接单成功
 | 

五、履约单查询
 
| 

20
 | 

组波完成
 | 

五、履约单查询
 
| 

30
 | 

分拣完成
 | 

五、履约单查询
 
| 

40
 | 

打包完成
 | 

五、履约单查询
 
| 

50
 | 

发货完成
 | 

五、履约单查询，三、下单接口
 
| 

60
 | 

履约单取消成功
 | 

五、履约单查询
 
| 

99
 | 

履约单异常
 | 

五、履约单查询
 

### 
取消状态（fulfillCancelStatus）

| 

状态码
 | 

描述
 | 

出现场景
 
| 

0
 | 

未发起
 | 

五、履约单查询
 
| 

10
 | 

取消中
 | 

五、履约单查询
 
| 

20
 | 

取消成功
 | 

五、履约单查询
 
| 

99
 | 

取消失败
 | 

五、履约单查询
