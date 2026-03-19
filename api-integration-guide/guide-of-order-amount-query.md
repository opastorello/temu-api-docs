# Guide of Order Amount Query

# 

**Background**

To improve clarity around order amount fields and reduce misunderstandings related to tax calculations, subsidy treatments, and discount amounts, the Order Amount V2 API (`temu.order.amount.v2.query`) has been launched. This version standardizes field definitions and calculation rules to ensure a consistent and transparent presentation of order amounts.

The order logic and APIs covered in this document currently apply only to Japan and Korea sites within GLOBAL.

# 

**Order structure and calculation relationships**

When Temu displays order amounts externally, product amounts, shipping fees, and their corresponding taxes are itemized separately. Detailed breakdowns of discounts and subsidies are also provided. This allows sellers to clearly understand the composition of order amounts and how settlement calculations are derived.

The order amount API is divided into two main modules: Sales Proceeds and Customer Paid. For each parent order, the correspondence between these two modules—as shown in the platform interface and API response—and their corresponding calculation logic is outlined below.

1. 
## 

**Sales proceeds**

**Description:** This amount represents the **estimated settlement amount** for reference. The actual settlement amount should be confirmed via the order **Statements**.

**Temu Platform Display Logic: Estimated Total Settlement Amount**

- 

This represents the estimated amount the seller will receive for the order.

- 

**Estimated Total Settlement Amount = (Base Price after Seller Discount * Quantity) + Shipping Total + Tax Total + Tax on Platform Discount − Estimated Deduction Amount.**

- 

The final payable amount is subject to the actual settlement shown in the order statement.

![image](https://bstatic.kwcdn.com/open-outer/21a4880000/b8ec14ffaf5a0b23a5b50c125488dad5.png)

**Corresponding API Calculation:**

```
estimatedSettlementTotal  
= basePriceDiscountedTotal  
+ shippingTotalTaxExcl  
+ productTax  
+ shippingTax  
+ taxTemuDiscount  
- estimatedDeduction
```

1. 
## 

**Customer paid**

This section mainly displays the **actual amount paid by the customer** and its breakdown.

**Temu platform display logic: Total paid**

- 

This is the actual amount paid by the customer.

- 

The total amount = Retail price after discount * Quantity + Shipping total + Tax total − Refunds total.

![image](https://bstatic.kwcdn.com/open-outer/21a4880000/61b45cebc4f9cc5e6af8b301395e99c5.png)

**Corresponding API Calculation:**

```
totalPaid  
= retailPriceCustomerTotalTaxExcl  
+ shippingCustomerTotalTaxExcl  
+ productTaxCustomerTotal  
+ shippingTaxCustomerTotal  
- productRefundsTotal
```

# 

 Key API Parameters and Corresponding Mapping

**Corresponding interface:** `temu.order.amount.v2.query`

The following section describes the **Sales Proceeds** and** Customer Paid** amount modules returned by this API at the **parent order** level, along with explanations of the related fields and their corresponding mappings on the Temu platform.

## 

Sales Proceeds

****

****

****

****

``

****

![image](https://bstatic.kwcdn.com/open-outer/21a4880000/22773e308daa3b1ac8b1ce2c3af36d2f.png)

- 

- 

- 

****

![image](https://bstatic.kwcdn.com/open-outer/21a4880000/4e4c23c216a2ef828b47ed600c101b16.png)

- 

- 

****

![image](https://bstatic.kwcdn.com/open-outer/21a4880000/d98c8e25b2283a9f4a8e8a312b713f60.png)

- 

**

- 

**

****

![image](https://bstatic.kwcdn.com/open-outer/21a4880000/1a7a86450902e867f05e9274475b163f.png)

- 

- 

![image](https://bstatic.kwcdn.com/open-outer/21a4880000/f016578b18fe7180c41ec890dc55b6d7.png)

****

![image](https://bstatic.kwcdn.com/open-outer/21a4880000/d97ec7761bb94936fd0e8fbbfb5ce00d.png)

****

![image](https://bstatic.kwcdn.com/open-outer/21a4880000/f493e2d5b6c672776abfe9c5992434e6.png)

****

![image](https://bstatic.kwcdn.com/open-outer/21a4880000/b7d19c43e62a4d838b6af4dcaaf996ac.png)

- 

****

- 

- 

![image](https://bstatic.kwcdn.com/open-outer/21a4880000/fb5bc5940bb6a3e166f0cf8ec2f4c7c1.png)

- 

- 

![image](https://bstatic.kwcdn.com/open-outer/21a4880000/9ed9b83d88c4fcba9b83741b6a9b5afc.png)

****

![image](https://bstatic.kwcdn.com/open-outer/21a4880000/4a1df1eaafb7587bf52ebea22c476865.png)

- 

- 

![image](https://bstatic.kwcdn.com/open-outer/21a4880000/77ede4214fdcedd372294a9a79362a4f.png)

![image](https://bstatic.kwcdn.com/open-outer/21a4880000/7fbe6389ce50c84db92e61e061d59690.png)

| Properties | Type | Description | Fields as displayed on the Temu platform | Temu platform order fields screenshot |
|---|---|---|---|---|
| ---salesProceeds | OBJECT | Sales proceeds |  |  |
| ----basePriceDiscountedTotal | OBJECT | Base price total after seller discountCalculation logic：basePriceDiscountedTotal = basePriceTotal - basePriceSellerDiscount - basePriceOff | Base price total  after discount |  |
| ----basePriceTotal | OBJECT | Base price totalBase price before discount. If there is an active promotional base price, this field displays the promotional base price. | Base price total |
| ----basePriceSellerDiscount | OBJECT | Seller discount This discount is generated from seller-initiated promotional activities. | Seller discount |
| ----basePriceOff | OBJECT | base price offThis amount includes personalized discounts and cross-store cumulative discounts. | base price off |
| ----shippingTotalTaxExcl | OBJECT | Shipping total(tax excl.）Shipping amount excluding tax.  Calculation logic：shippingTotalTaxExcl=shippingCustomerTotalTaxExcl+shippingTemuTotalTaxExcl | Shipping total(tax excl.） |  |
| ----shippingCustomerTotalTaxExcl | OBJECT | Customer paid-shipping totalShipping amount paid by the consumer, excluding tax. | Customer paid-Shipping |
| ----shippingTemuTotalTaxExcl | OBJECT | Platform incentive-ShippingShipping amount paid by the  platform, excluding tax. If the order is not eligible for platform free shipping, this field is set to 0. | Platform incentive-Shipping |
| ----productTax | OBJECT | Product taxProduct tax amount.  Calculation logic：productTax=productTaxCustomerDiscounted+productTaxTemu | Product tax |  |
| ----productTaxCustomerDiscounted | OBJECT | Customer paid-Product taxProduct tax amount paid by the consumer. | Not displayed on the Temu platform |
| ----productTaxTemu | OBJECT | Platform incentive-Product taxProduct tax amount subsidized by the platform. | Not displayed on the Temu platform |
| ----shippingTax | OBJECT | Shipping TaxShipping tax amount.  Calculation logic：shippingTax=shippingTaxCustomerDiscounted+shippingTaxTemu | Shipping Tax |  |
| ----shippingTaxCustomerDiscounted | OBJECT | Customer paid-Shipping taxShipping tax amount paid by the consumer after discount. | Customer paid-Shipping tax |
| ----shippingTaxTemu | OBJECT | Platform incentive-Shipping TaxShipping tax amount subsidized by the platform. If the order is not eligible for platform free shipping, this field is set to 0. | Platform incentive-Shipping Tax |
| ----taxTemuDiscount | OBJECT | Tax on platform discount.Only returned for Japan and South Korea sites. | Tax on platform discount |  |
| ----estimatedDeduction | OBJECT | Estimated deduction amount Estimated deduction amount is calculated based on theamount of customer's refunds. | Estimated deduction amount |  |
| ----estimatedSettlementTotal | OBJECT | Estimated total settlement amountEstimated total revenue for the seller. Calculation logic：estimatedSettlementTotal=  basePriceDiscountedTotal+shippingTotalTaxExcl+productTax+shippingTax+taxTemuDiscount-estimatedDeduction | Estimated total settlement amount |  |
| ---customerPaid | OBJECT | Sales proceedsAmount paid by the consumer. |  |  |
| ----retailPriceCustomerTotalTaxExcl | OBJECT | Retail price total after discounts(tax excel.)Discounted retail price excluding tax.   Calculation logic：retailPriceCustomerTotalTaxExcl=retailPriceTotalTaxExcl-retailPriceSellerDiscountTaxExcl-retailPriceTemuDiscountTaxExcl | Retail price total after discounts(tax excel.) |  |
| ----retailPriceTotalTaxExcl | OBJECT | Retail price (tax excel.)Retail price excluding tax. | Retail price (tax excel.) |
| ----retailPriceSellerDiscountTaxExcl | OBJECT | Seller discount Seller discount amount included in the retail price. | Seller discount |
| ----retailPriceTemuDiscountTaxExcl | OBJECT | Temu discountPlatform discount amount that is included in the retail price, excluding tax. | Temu discount |
| ----shippingCustomerTotalTaxExcl | OBJECT | Shipping total after discount (tax excl.）Shipping amount paid by the consumer, excluding tax.  Calculation logic：shippingCustomerTotalTaxExcl=shippingTotalTaxExcl-shippingTemuTotalTaxExcl | Shipping total after discount (tax excl.） |  |
| ----shippingTotalTaxExcl | OBJECT | Shipping total (tax excl.）Shipping amount excluding tax. | Shipping total (tax excl.） |
| ----shippingTemuTotalTaxExcl | OBJECT | Temu discountShipping amount paid by the  platform, excluding tax. If the order is not eligible for platform free shipping, this field is set to 0. | Temu discount |
| ----productTaxCustomerTotal | OBJECT | Product TaxProduct tax amount actually paid by the consumer after discount. | Product Tax |  |
| ----shippingTaxCustomerTotal | OBJECT | Shipping Tax after discountDiscounted shipping tax amount.   Calculation logic： shippingTaxCustomerTotal=shippingTax- shippingTaxTemuTotal | Shipping Tax after discount |  |
| ----shippingTax | OBJECT | Shipping taxShipping tax amount. | Shipping tax |
| ----shippingTaxTemuTotal | OBJECT | Temu discountShipping tax amount subsidized by the platform. If the order is not eligible for platform free shipping, this field is set to 0. | Temu discount |
| ----productRefundsTotal | OBJECT | Product refundProduct refund amount. | Product refund |  |
| ----customerPaidTotal | OBJECT | Total paidActual amount paid by the consumer.  Calculation logic：customerPaidTotal=  retailPriceCustomerTotalTaxExcl+shippingCustomerTotalTaxExcl+productTaxCustomerTotal+shippingTaxCustomerTotal-productRefundsTotal | Total paid |  |

## 

Customer Paid

****

****

****

****

****

![image](https://bstatic.kwcdn.com/open-outer/21a4880000/57be182b773266668db1154f15d0ba4c.png)

- 

****

- 

- 

![image](https://bstatic.kwcdn.com/open-outer/21a4880000/4e4a3afb59092cbeeea1acf2794078ac.png)

- 

- 

![image](https://bstatic.kwcdn.com/open-outer/21a4880000/d196b02bdfda33073fd30785a72049bb.png)

****

![image](https://bstatic.kwcdn.com/open-outer/21a4880000/4dcb4b0fd528e5b1956cbaad20dcd84a.png)

- 

- 

![image](https://bstatic.kwcdn.com/open-outer/21a4880000/f89a5d85f9e1f604cc2c58f754e059a8.png)

![image](https://bstatic.kwcdn.com/open-outer/21a4880000/b700400aaccf9143aceb422efd431b0d.png)

| Properties | Type | Description | Fields as displayed on the Temu platform | Temu platform order fields screenshot |
|---|---|---|---|---|
| ---customerPaid | OBJECT | Sales proceedsAmount paid by the consumer. |  |  |
| ----retailPriceCustomerTotalTaxExcl | OBJECT | Retail price total after discounts(tax excel.)Discounted retail price excluding tax.   Calculation logic：retailPriceCustomerTotalTaxExcl=retailPriceTotalTaxExcl-retailPriceSellerDiscountTaxExcl-retailPriceTemuDiscountTaxExcl | Retail price total after discounts(tax excel.) |  |
| ----retailPriceTotalTaxExcl | OBJECT | Retail price (tax excel.)Retail price excluding tax. | Retail price (tax excel.) |
| ----retailPriceSellerDiscountTaxExcl | OBJECT | Seller discount Seller discount amount included in the retail price. | Seller discount |
| ----retailPriceTemuDiscountTaxExcl | OBJECT | Temu discountPlatform discount amount that is included in the retail price, excluding tax. | Temu discount |
| ----shippingCustomerTotalTaxExcl | OBJECT | Shipping total after discount (tax excl.）Shipping amount paid by the consumer, excluding tax.  Calculation logic：shippingCustomerTotalTaxExcl=shippingTotalTaxExcl-shippingTemuTotalTaxExcl | Shipping total after discount (tax excl.） |  |
| ----shippingTotalTaxExcl | OBJECT | Shipping total (tax excl.）Shipping amount excluding tax. | Shipping total (tax excl.） |
| ----shippingTemuTotalTaxExcl | OBJECT | Temu discountShipping amount paid by the  platform, excluding tax. If the order is not eligible for platform free shipping, this field is set to 0. | Temu discount |
| ----productTaxCustomerTotal | OBJECT | Product TaxProduct tax amount actually paid by the consumer after discount. | Product Tax |  |
| ----shippingTaxCustomerTotal | OBJECT | Shipping Tax after discountDiscounted shipping tax amount.   Calculation logic： shippingTaxCustomerTotal=shippingTax- shippingTaxTemuTotal | Shipping Tax after discount |  |
| ----shippingTax | OBJECT | Shipping taxShipping tax amount. | Shipping tax |
| ----shippingTaxTemuTotal | OBJECT | Temu discountShipping tax amount subsidized by the platform. If the order is not eligible for platform free shipping, this field is set to 0. | Temu discount |
| ----productRefundsTotal | OBJECT | Product refundProduct refund amount. | Product refund |  |
| ----customerPaidTotal | OBJECT | Total paidActual amount paid by the consumer.  Calculation logic：customerPaidTotal=  retailPriceCustomerTotalTaxExcl+shippingCustomerTotalTaxExcl+productTaxCustomerTotal+shippingTaxCustomerTotal-productRefundsTotal | Total paid |  |

# 

**Interface Access Permission Application Process**

This API is classified as a sensitive interface and is subject access permission control. Please submit a permission application under the appropriate role based on your application type. After the permission application process is approved, re-authorization and an updated access token are required before the API can be called normally.

- 

**Self-developed applications**: Please contact your store operations manager to submit the permission application on your behalf.

- 

**Third-party ERP applications**: Please contact your platform business representative to submit the permission application on your behalf.
