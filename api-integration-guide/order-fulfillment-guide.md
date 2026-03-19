# Order Fulfillment Guide

# 

**Overview**

This document provides an overview of the order fulfillment process, detailing the two primary methods: Buy-Shipping(platform-generated shipping labels) and Self-Fulfilled Shipments(seller self-fulfillment). The following schematic illustrates the workflow for each method. Subsequently, a detailed tutorial involved in both processes is provided.

![image](https://bstatic.kwcdn.com/open-outer/21a488b06a/c0cfb7006168193b7fa7ab611c261330)

## 

**Fulfillment Method with Step-to-Step Tutorial**

- 
## 

**Buy-Shipping**

### 

**What Means Buy-shipping**

1. 

Temu has always been committed to building a more convenient shipping system.

1. 

Purchase labels with Temu buy-shipping can receive following benefits.

  1. 

Competitive prices

  1. 

Guidance on avoiding performance violations

### 

**Buy shipping-Fulfillment Steps and Process**

1. 

**Determine the composition of the package and query recommended logistics channels:**

  - 

Use [`**bg.logistics.warehouse.list.get**`](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=eb414749aff646d184c2129737a48229)to query the warehouse available for shipping in the store.

  - 

Use [`**bg.logistics.shippingservices.get**`](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=faf297e439f841009d417aabe52b7999) to query the **recommended logistics channels.**

1. 

**Use **[`**bg.logistics.shipment.create**`](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=0af17643465346f9b72bd7478b2a8254)** to to place orders with recommended channels:**

  - 

Note that the current structure supports merging shipments for the `parentOrder`, and also supports partial fulfillment for individual orders within a single `parentOrder`.

  - 

Pay attention to the following restrictions:

    1. 

**SHIP LATER: **At the moment when the default package successfully places an order with the logistics provider, the order inside the package will automatically flow to the shipped status. But it supports merchants to choose to adjust the logic and set to ship later. At this point, even if the order is successfully placed, the order inside the package will not be immediately converted to shipped.

    1. 

**shipLaterLimitTime**: Used in conjunction with SHIP LATR, it is used to set the time when the order will be converted to shipped after a successful call. Default is 24 hours

1. 

**Use** [`**bg.logistics.shipment.result.get**`](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=122ba56121114e4ba72292fafe0ff509)** to view the Buy-shipping results:**

  - 

Buy shipping is an asynchronous return process, and it does not succeed simply by calling after receiving the package number. We need to use this interface to check the actual call results and whether the corresponding logistics service provider has successfully purchased the waybill

    1. 

**shippingLabelStatus: ShippingLabelStatus represents the actual result of purchasing the waybill. The corresponding enumeration is as follows:**

      1. 

**0 ：in application**

      1. 

**1： successful**

      1. 

**2 ：failed**

1. 

**Use **[`**bg.logistics.shipment.update**`](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=e698d355abd641119dd3f5f44d60804a)** to buy-shipping again**

  - 

In the event of a first-time ship shipping failure, this interface is required to retry buy-shipping

  - 

How to obtain the packageSn

  - 

Call successful and ship immediately：by bg.logistics.shipment.get to get the packagesn

    - 

Call successful and ship later：by bg.order.unshipped.package.get to get the packagesn

1. 

**Use**[`**bg.logistics.shipment.document.get**`](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=f7190502aaf2433d94877589beefa31f)** to get the labal**

  - 

**How to obtain label after obtaining URL**

    - 

the return URL is a signed resource, which can be accessed using the following method

      - 

ccess address: The URL returned here will expire after 10 minutes. If timeout occurs, please call bg.logistics.shipment.document.get again to obtain a new URL

      - 

Request method: GET

> 

The request header contains the following 5 parameters:

> 

{

> 

"toa-app-key": ${app_key},

> 

"toa-access-token": ${access_token},

> 

"toa-random": "${32 random numbers}",

> 

"toa-timestamp":"${timestamp}",

> 

"toa-sign":"${sign}"

> 

}

    - 

Among them, toa random customizes 32 random numbers

    - 

The toa timestamp requires a length of 10 bits, accurate to the second level, current_time-300<=toa-timestamp<=current_time+300

    - 

The calculation logic of toa sign is consistent with the calculation logic of the common parameter sign in normal requests:

      - 

-Sort the four parameters, toa access token, toa app key, toa rand, and toa timestamp, in ascending ASCII format with the first letter. For identical letters, use the next letter for secondary sorting, with alphabetical order from left to right, and so on

      - 

-The sorted result is concatenated into strings in the order of parameter name $key and parameter value $value, without any characters at the concatenation point

      - 

-The concatenated string is further concatenated into one string (including all kv strings), and app_crit is concatenated at the beginning and end of the long string to complete the assembly of the signature string

      - 

-Finally, the signature string is encrypted using the MD5 algorithm, and the resulting MD5 encrypted ciphertext is converted to uppercase, which is the toa sign value the interface returns a file stream.

1. 

**Use **[`**bg.logistics.shipped.package.confirm**`](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=3766a8cd5b2f4db79558429805d8b7a7)** to convert the package that was successfully called but not shipped to shipped**

## 

**Prerequisite for fulfillment**

- 

Confirm whether the seller is using Self-Fulfilled Shipments or Buy-Shipping

- 

Confirm whether the logistics company selected by the seller for fulfillment is approved to ship in the local area

- 
## 

Self-Fulfilled Shipments

1. 

**Get the logistics companies that can deliver to the order's region:**

  - 

Use [`bg.logistics.companies.get`](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=2b0c4fc8bf2b4a74969df538f4dadb88) to query the logistics companies supported by the corresponding `regionId`.

1. 

**Use **[`**bg.logistics.shipment.v2.confirm**`](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=27ff4f3d7b0b4c07862769d11f638ef0) **to confirm the order's shipping information:**

  - 

Note that the current structure supports merging shipments for the `parentOrder`, and also supports partial fulfillment for individual orders within a single `parentOrder`.

  - 

Pay attention to the following restrictions:

    1. 

**Tracking numbers** are allowed to be used only once for successful fulfillment; they cannot be used for multiple orders (unless declared as completed in one fulfillment statement).

    1. 

The system will validate whether the tracking number matches the courier's regular expression format. Please ensure that the correct tracking number is provided.

  - 

If you are merging multiple orders for fulfillment, please note the following:

    1. 

**Partial order fulfillment** across multiple `parentOrders` is not allowed. If you are merging shipments, all orders under the `parentOrder` must be fulfilled together.

    1. 

The fulfillment quantity for each order must be fully completed at once. Partial fulfillment is not allowed (if the fulfillment occurs in multiple stages, all tracking numbers should be collected and shipped together).

1. 

**Use **[`**bg.logistics.shipment.v2.get**`](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=4af2bc744d5a4e09bc476b017696cea9)** ****to query the current shipment status:**

  - 

Ensure that the shipping information is as expected and confirm that the fulfillment is progressing as planned.
