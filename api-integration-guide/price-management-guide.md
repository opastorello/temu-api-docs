# Price Management Guide

#### 

**overview**

Price management is crucial in the sales process, involving competitive analysis, dynamic pricing, promotional strategies, and other aspects. By implementing a reasonable pricing strategy, product competitiveness can be improved while optimizing inventory and maximizing sales revenue. Price management also needs to be adjusted according to consumer demand and market changes, flexibly utilizing promotional activities and discount management to enhance user experience and loyalty, ultimately promoting the long-term development of product sales.

#### 

**Price management mode**

- 

**Incomplete offers**

Overview: After the product is released, the platform will evaluate the base price of the product to ensure consistency and transparency of the seller's product price.

- 

**Pricing opportunities**

Overview: After the sale of goods, the platform will evaluate the base price of the products being sold, helping merchants optimize their pricing strategies and avoid profit losses or sales declines caused by unreasonable prices.

- 

**Pricing modification**

Overview: The seller modifies the base price of the product

- 
#### 

How to implement price integration

**Incomplete offers**

![image](https://bstatic.kwcdn.com/open-outer/201365d0000/4f0060ad7b9e2bd64975066ef4d31357.png)

**Step 1: Call the interface to check if there are any pending price tasks**

Call this interface** [bg.local.goods.priceorder.query] **When entering **priceOrderType=1**, obtain the corresponding task information

The following is a description of the corresponding document status

100=under review

201=Through

202=Reject pending modification

206=Reject

101=awaiting confirmation from the merchant

203=Merchant Confirmation

205=merchant refuses

204=Merchant initiates modification

When the **status is 101**, the user needs to perform subsequent operations

**Step 2: Call these interfaces to perform task operations, where users can agree, refuse, or negotiate**

If you agree with the platform's suggested price, call **[bg.local.goods.priceorder.accept]** Confirm.

If the price is rejected, call **[temu.local.goods.priceorder.reject] **

If you need to adjust the price, please call **[bg.local.goods.priceorder.negotiate] **Adjust the price again and wait for the platform's price evaluation results.

**Restricted traffic**

![image](https://bstatic.kwcdn.com/open-outer/2066d9156e/5b913bafda2a06061f7ce94a4ffebf6d)

**Step 1: Call the API to check whether there are products with restricted traffic.**

Call the API** [temu.local.goods.recommendedprice.query]****,**** **and set **recommendedPriceType=20** to** **obtain** **the recommended price of the corresponding product.

**Step 2: Call the API ****[bg.local.goods.priceorder.change.sku.price]**** to modify the price.**

Pass the recommended price as the value of the **newSupplierPrice **parameter.

- 
#### 

How to Pricing opportunities integration

**Pricing opportunities**

![image](https://bstatic.kwcdn.com/open-outer/201365d0000/0b88c3c036b0608ab45c9cfd55f7c896.png)

**Step 1: Call the interface to check if there are any pending price tasks**

Call this interface** [bg.local.goods.priceorder.query] **When entering **priceOrderType=2 **, obtain the corresponding task information

At the same time, this field **[priceOrderSubType]** can be used to confirm the specific price subtask type

The following is a description of the corresponding document status

100=under review

201=Through

202=Reject pending modification

206=Reject

101=awaiting confirmation from the merchant

203=Merchant Confirmation

205=merchant refuses

204=Merchant initiates modification

When the **status is 101**, the user needs to perform subsequent operations

**Step 2: Call these interfaces to perform task operations, where users can agree, refuse**

If you agree with the platform's suggested price, call **[bg.local.goods.priceorder.accept]** Confirm.

If the price is rejected, call **[temu.local.goods.priceorder.reject].**

![image](https://bstatic.kwcdn.com/open-outer/201365d0000/dc69772a81df2b783d159ee5ca98fe6b.png)![image](https://bstatic.kwcdn.com/open-outer/201365d0000/b2823ea2776e69050b89ebe7e8787e8e.png)

**Step 3: Call the interface to view price proposal data **

Call this interface **[temu.local.goods.appealorder.query] **,The following is the status of the document task

10=APPEALING

20=PLATFORM_PASS

30=PLATFORM_REJECT

40=PLATFORM_TERMINATE

When the state is 10

The user calls this interface to accept the price [**bg.local.goods.priceorder.accept**], or calls the interface **[temu.local.goods.appealorder.create]** to initiate price propsose again

- 
#### 

How to Pricing modification integration

**Pricing modification**

![image](https://bstatic.kwcdn.com/open-outer/201365d0000/a0b7bc6eb862157ffbae4ee10802fe82.png)

**Step 1: Call the interface ****[bg.local.goods.priceorder.query] ****when entering priceOrderType=2**** ****  to check if there are any ongoing tasks**

The following is a description of the corresponding document status

100=under review

201=Through

202=Reject pending modification

206=Reject

101=awaiting confirmation from the merchant

203=Merchant Confirmation

205=merchant refuses

204=Merchant initiates modification

**Only these states can initiate price modification**

201=Through

202=Reject pending modification

203=Merchant Confirmation

205=merchant refuses

206=Reject

**Step 2: Call the interface ****[bg.local.goods.priceorder.change.sku.price]**** to modify the price**

**Note **

1. 

the current baseprice can be obtained through this interface [bg.local.goods.sku.list.price.query]

1. 

[bg.local.goods.sku.list.price.query] This interface can only be used by self-developed sellers or a small number of third-party service providers

####
