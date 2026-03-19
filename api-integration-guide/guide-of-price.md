# Guide of price

# 

**Overview**

This Price API is primarily used for bulk price management of products. It covers core operations such as querying product prices, modifying product prices, and querying price offer lists.

Note that the Price API is a sensitive interface and is only available to whitelisted, locally developed applications. 

**If you need access, submit an application at the store level through the business team.**

![image](https://bstatic.kwcdn.com/open-outer/21a488e82c/f5e3e51bea125a2fb9dd05b46464b415.jpeg)

The following are the interfaces involved in price management：

| API name | Interface Overview |
|---|---|
| temu.local.goods.baseprice.recommend | Supports merchants in querying the estimated base price of products. |
| temu.local.goods.recommendedprice.query | Support merchants in querying the recommended base prices. |
| bg.local.goods.priceorder.change.sku.price | Support merchants within the white list to modify sku base prices in batches. |
| bg.local.goods.priceorder.query | Support merchants within the white list to query the price offer list. |

### 

**What is a base price？**

Base price：The base price reflects the amount you receive from each sale under standard, non-promotional conditions. The base price should cover your costs and desired profit. You are free to set the base price at any value you consider fair.

![image](https://bstatic.kwcdn.com/open-outer/21a488e82c/29d033139d0816cf9adc22974e576ac1.png)![image](https://bstatic.kwcdn.com/open-outer/21a488e82c/1093504fbe68acd5e37068e0b81f1a88.png)

### 

### 

**How to Set Product Base Prices？**

You can set the base price either manually or by using the Base Price Calculator. You may always choose a base price that you consider fair.

To use the Base Price Calculator, enter a selling price from e-commerce platforms, and our system will then automatically calculate the base price on Temu to maintain the same settlement amount of yours. The base price is for your reference only. Make sure the entered price is accurate and corresponds to the same product. The corresponding API is** [temu.local.goods.baseprice.recommend]**.

For **newly listed products**, first call **[temu.local.goods.baseprice.recommend]** to obtain the base price on Temu to maintain the same settlement amount for you. Then, when listing the product via **[bg.local.goods.add]**, apply this recommended base price.

For **already listed products**, call **[temu.local.goods.recommendedprice.query]** to retrieve the recommended base price for gaining potential traffic boost opportunities. If you need to update prices, call **[bg.local.goods.priceorder.change.sku.price]** to adjust SKU base prices in bulk.

![image](https://bstatic.kwcdn.com/open-outer/21a488e82c/7f5e941673b2881e75f831e93ad8b2e7.png)

As shown in the screenshot, you can choose either method to set the base price.
