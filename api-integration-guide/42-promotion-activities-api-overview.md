# Promotion  activities  API overview

**Last update:** 2025-02-12 10:30:18

---

The following document primarily outlines the Promotion  process.

# 
**Promotion activities  overview**

To help sellers get more traffic, attract customers, and increase sales, four activities have been launched: Clearance deals, Lightning deals, Official big sale, and Advanced big sale.

| 

Activity type
 | 

Clearance deals (CD)
 | 

Lightning deals (LD)
 | 

Official big sale(OBG)
 | 

Advanced big sale(ABG)
 
| 

Description
 | 

14-day promotion that aims to establish low prices for customers, quickly clear out slow-moving stock, and enhance turnover
 | 

7-day promotion with significantly discounted items
 | 

Low-barrier entry for time-limited discounts
 | 

series of promotional events to feature products that match the festive spirit or seasonal occasions
 
| 

Key points
 | 

Exclusive homepage banner

Clearance sale or reductions on discontinued sizes
 | 

Featured deals section on the homepage

Encourages quick purchases and increases sales
 | 

Increases traffic and recommendations

Intense promotional atmosphere
 | 

Activity banner on the homepage

Leverage peak shopping periods and customer interests
 
| 

When to use
 | 

Works best for overstocked items or significantly discounted items
 | 

Works best for in-demand items or significantly discounted items
 | 

Most suitable for long-term discounts and products with a low entry barrier
 | 

Most suitable for products that align with upcoming holiday themes or meet seasonal demand
 
| 

Duration
 | 

14 days
 | 

7 days
 | 

Variable time
 | 

 
| 

Minimum discount requirements
 | 

Refer to the product discount requirements provided on the reference system.
 
| 

Activity price
 | 

 In general, the lower the activity base price, the lower the activity price.
 

# 
**How to Register Products for an  Promotion Activity on TEMU Seller Center**

## 
**Activity homepage**

### 
**Path: TEMU Seller Center - Homepage - Promotions**

**Activity invitation:** The system regularly sends activity invitations, and multiple activities are launched on a rolling basis. Sellers can select and register for activities they are interested in.

## 
**Register and Add Products**

Activities that you have not participated in: Click **Join Now**. You will then be directed to the activity registration page.

Activities that you have started to participated in: Click **Add products**. A pop-up window will be displayed for you to add products.

### 
**Promotion activity  registration page**

**Activity Introduction: **The top information bar displays the activity name, time, status, and an example of what it looks on the buyer's side.

### 
**Recommended products:**

| 

**Product name**
 | 

Displays the product picture + name + ID
 
| 

**Variations**
 | 

Displays variations + SKU ID + SKU
 
| 

**Daily （base） price**
 | 

Displays the corresponding SKU price
 
| 

**Activity （base） price**
 | 

The base price you set for activities, which can be sold at the activity price during the activity period
 
| 

**Activity quantity**
 | 

The quantity you set for participating activities. It will be deducted from the available quantity until the activity ends or you leave the activity
 

### 
** Promotion activity  Registration Process： **

- 
#### 
Step 1: Select the products from the product list in the store that you want to register.

- 
#### 
Step 2: Set the activity base price or use the recommended base price.

- 
#### 
Step 3: Set the activity quantity.

- 
#### 
Step 4: Submit and confirm registration.

- 
#### 
Step 5: View the activities you have registered for or continue to register for other activities.

#### 
 

# 
**API List**

You can create and manage your promotion activities in Seller Center and Seller App; you can also do that with Promotion APIs. Here's the list of Promotion APIs:

- 
To search and obtain promotion activity information under the store, please refer to:

- 
[bg.promotion.activity.query](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=05820fed7179430c8e353905692d51b6)

- 
To view the details of candidate products eligible to participate in this promotion activity, please refer to:

- 
[bg.promotion.activity.candidate.goods.query](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=0a11814e7d4146b595918ff3c0f3e239)

- 
View registration details for specific promotion activity, please refer to:

- 
[bg.promotion.activity.goods.query](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=08f3f87d05a24bac882732141e0d9672)

- 
To register a product for a promotion and set a discounted price and corresponding inventory, refer to:

- 
[bg.promotion.activity.goods.enroll](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=27a87ec9d0d94273a48096c050f17854)

- 
To view the registration or update the adjustment results of an promotion activity , please refer to:

- 
[bg.promotion.activity.goods.operation.query](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=57a37eb5dd104e3f9f90118e3276b291)

- 
To Update the product information of promotion activities, such as changing activity inventory, updating activity supply prices, offline activity products, and adding activity SKUs. Please refer to:

- 
[bg.promotion.activity.goods.update](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=29959238217c41f38f5904e32bf1d14f)
