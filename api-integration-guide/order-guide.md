# Order Guide

# 

**Overview**

This document outlines the core concepts and hierarchy of orders as managed in the Seller Center. Key topics includes the relationship between a **Parent Order (PO)** and its constituent **Order Items (Order Item IDs)**, the lifecycle of an order as defined by its **status**, and other essential order attributes.

![image](https://bstatic.kwcdn.com/open-outer/21a4886cc6/0b428e199acb03783ecbae3ae6dd79c3.jpeg)

## 

**Parent Order (PO)**

In Temu's order model, every consumer purchases results in a two-tier hierarchy: a single **Parent Order** (`parentOrderSn`) encompassing one or more **Order Item ID(s)**.

- 

`**parentOrderSn**` is the unique, global identifier for the entire transaction. Example: PO-211-XXXXXXXXXXXXXXXXX, which 211 is the [regionID](https://partner.temu.com/documentation?menu_code=38e79b35d2cb463d85619c1c786dd303&sub_menu_code=07938e60f95344a0a9444f524ea61e31) for this PO order. This regionID will always be the same the the one in the Order Item IDs.

- 

A **Parent Order** can consolidate multiple **Order Items**.

#### 

**Where to find Parent Order (PO)**

In the seller center, you can find your PO order numbers under Order → Manage orders, like in the following screenshot.

![image](https://bstatic.kwcdn.com/open-outer/21a4886cc6/c63304d8488ebb7391988d53722787bd.png)

## 

**Order Items (Order Item IDs)**

In Temu's order model, under each Parent Order, it will at least have one order item. Each** Order** is linked to precisely one Temu SKU. 

![image](https://bstatic.kwcdn.com/open-outer/21a4886cc6/cc66ee1c95d38345ae1a7ba5659b9f39.png)

## 

**Order Status**

Generally, Temu order lifecycle includes five statuses: **Pending**, **Unshipped**, **Shipped**, **Delivered** and **Canceled**

**Pending:** A Parent Order enters this status when a consumer places an order. It remains Pending for a set period before automatically transitioning to **Unshipped**.

- 

**Pending:** A Parent Order enters this status when a consumer places an order. It remains Pending for a set period before automatically transitioning to **Unshipped**.

- 

**Unshipped:** In this status, the seller must arrange shipment. They can choose between **Temu-Integrated Logistics** or **Self-Fulfillment Shipping**

- 

**Shipped:** Once the seller confirms shipment (through either method), the Parent Order status updates to **Shipped**

- 

**Delivered:** This final status is set when the package is successfully delivered and signed for by the end consumer.

- 

**Canceled:** An order may be canceled under specific conditions, ending the lifecycle

## 

**Things to Note**

1. 

**Cancellation Requests:** Sellers have a **24-hour window** to respond to a consumer's cancellation request. Unanswered requests will be auto-approved by the system after this period.

1. 

**Orders in Pending Status:** Consumers may alter their order (e.g., change address, update quantity) while it is **Pending**. To avoid fulfillment errors, we recommend that sellers only begin processing once the order advances to **Unshipped**, at which point the final address is confirmed and displayed.

1. 

**Processing Time:** The system automatically processes orders from **Pending** to **Unshipped**. This usually completes within minutes but can take up to several hours in rare cases. If an order is stuck in **Pending** for an extended duration, please reach out to **Store Operations** for investigation.
