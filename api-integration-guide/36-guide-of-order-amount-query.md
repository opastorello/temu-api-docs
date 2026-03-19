# Guide of Order Amount Query

**Last update:** 2026-01-18 23:59:02

---

# 
**Background**

To improve clarity around order amount fields and reduce misunderstandings related to tax calculations, subsidy treatments, and discount amounts, the Order Amount V2 API (`temu.order.amount.v2.query`) has been launched. This version standardizes field definitions and calculation rules to ensure a consistent and transparent presentation of order amounts.

The order logic and APIs covered in this document currently apply only to Japan and Korea sites within GLOBAL.

# 
**Order structure and calculation relationships**

When Temu displays order amounts externally, product amounts, shipping fees, and their corresponding taxes are itemized separately. Detailed breakdowns of discounts and subsidies are also provided. This allows sellers to clearly understand the composition of order amounts and how settlement calculations are derived.

The order amount API is divided into two main modules: Sales Proceeds and Customer Paid. For each parent order, the correspondence between these two modules—as shown in the platform interface and API response—and their corresponding calculation logic is outlined below.

- 
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

- 
## 
**Customer paid**

This section mainly displays the **actual amount paid by the customer** and its breakdown.

**Temu platform display logic: Total paid**

- 
This is the actual amount paid by the customer.

- 
The total amount = Retail price after discount * Quantity + Shipping total + Tax total − Refunds total.

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

| 

**Properties**
 | 

**Type**
 | 

Description 
 | 

**Fields as displayed on the Temu platform**
 | 

**Temu platform order fields screenshot**
 
| 

---salesProceeds
 | 

OBJECT
 | 

Sales proceeds

 | 

 | 

 
| 

----basePriceDiscountedTotal
 | 

OBJECT
 | 

Base price total after seller discount

Calculation logic：

`basePriceDiscountedTotal = basePriceTotal - basePriceSellerDiscount - basePriceOff`
 | 

**Base price total  after discount**
 | 

 
| 

----basePriceTotal
 | 

OBJECT
 | 

Base price total

Base price before discount. If there is an active promotional base price, this field displays the promotional base price. 

 | 

- 
Base price total

 
| 

----basePriceSellerDiscount
 | 

OBJECT
 | 

Seller discount 

This discount is generated from seller-initiated promotional activities.

 
 | 

- 
Seller discount 

 
| 

----basePriceOff
 | 

OBJECT
 | 

base price off

This amount includes personalized discounts and cross-store cumulative discounts. 

 
 | 

- 
base price off

 
| 

----shippingTotalTaxExcl
 | 

OBJECT
 | 

Shipping total(tax excl.）

Shipping amount excluding tax. 

 Calculation logic：shippingTotalTaxExcl=shippingCustomerTotalTaxExcl+shippingTemuTotalTaxExcl
 | 

**Shipping total(tax excl.）**
 | 

 
| 

----shippingCustomerTotalTaxExcl
 | 

OBJECT
 | 

Customer paid-shipping total

Shipping amount paid by the consumer, excluding tax. 

 
 | 

- 
Customer paid-Shipping

 
| 

----shippingTemuTotalTaxExcl
 | 

OBJECT
 | 

Platform incentive-Shipping

Shipping amount paid by the  platform, excluding tax. If the order is not eligible for platform free shipping, this field is set to 0.

 
 | 

- 
Platform incentive-Shipping

 
| 

----productTax
 | 

OBJECT
 | 

Product tax

Product tax amount. 

 Calculation logic：productTax=productTaxCustomerDiscounted+productTaxTemu
 | 

**Product tax**
 | 

 
| 

----productTaxCustomerDiscounted
 | 

OBJECT
 | 

Customer paid-Product tax

Product tax amount paid by the consumer. 

 
 | 

- 
*Not displayed on the Temu platform*

 
| 

----productTaxTemu
 | 

OBJECT
 | 

Platform incentive-Product tax

Product tax amount subsidized by the platform. 

 
 | 

- 
*Not displayed on the Temu platform*

 
| 

----shippingTax
 | 

OBJECT
 | 

Shipping Tax

Shipping tax amount. 

 Calculation logic：shippingTax=shippingTaxCustomerDiscounted+shippingTaxTemu
 | 

**Shipping Tax**
 | 

 
| 

----shippingTaxCustomerDiscounted
 | 

OBJECT
 | 

Customer paid-Shipping tax

Shipping tax amount paid by the consumer after discount. 

 
 | 

- 
Customer paid-Shipping tax

 
| 

----shippingTaxTemu
 | 

OBJECT
 | 

Platform incentive-Shipping Tax

Shipping tax amount subsidized by the platform. If the order is not eligible for platform free shipping, this field is set to 0.

 
 | 

- 
Platform incentive-Shipping Tax

 
| 

----taxTemuDiscount
 | 

OBJECT
 | 

Tax on platform discount.

Only returned for Japan and South Korea sites.

 | 

Tax on platform discount 

 | 

 
| 

----estimatedDeduction
 | 

OBJECT
 | 

Estimated deduction amount 

Estimated deduction amount is calculated based on theamount of customer's refunds. 

 
 | 

**Estimated deduction amount**
 | 

 
| 

----estimatedSettlementTotal
 | 

OBJECT
 | 

Estimated total settlement amount

Estimated total revenue for the seller. 

Calculation logic：estimatedSettlementTotal=  basePriceDiscountedTotal+shippingTotalTaxExcl+productTax+shippingTax+taxTemuDiscount-estimatedDeduction
 | 

**Estimated total settlement amount**
 | 

 
| 

---customerPaid
 | 

OBJECT
 | 

Sales proceeds

Amount paid by the consumer. 

 
 | 

 | 

 
| 

----retailPriceCustomerTotalTaxExcl

 | 

OBJECT
 | 

Retail price total after discounts(tax excel.)

Discounted retail price excluding tax. 

  Calculation logic：

retailPriceCustomerTotalTaxExcl=retailPriceTotalTaxExcl-retailPriceSellerDiscountTaxExcl-retailPriceTemuDiscountTaxExcl
 | 

**Retail price total after discounts(tax excel.)**
 | 

 
| 

----retailPriceTotalTaxExcl
 | 

OBJECT
 | 

Retail price (tax excel.)

Retail price excluding tax. 

 
 | 

- 
**Retail price (tax excel.)**

 
| 

----retailPriceSellerDiscountTaxExcl
 | 

OBJECT
 | 

Seller discount 

Seller discount amount included in the retail price. 

 
 | 

- 
Seller discount 

 
| 

----retailPriceTemuDiscountTaxExcl
 | 

OBJECT
 | 

Temu discount

Platform discount amount that is included in the retail price, excluding tax. 

 
 | 

- 
Temu discount

 
| 

----shippingCustomerTotalTaxExcl
 | 

OBJECT
 | 

Shipping total after discount (tax excl.）

Shipping amount paid by the consumer, excluding tax. 

 Calculation logic：

shippingCustomerTotalTaxExcl=shippingTotalTaxExcl-shippingTemuTotalTaxExcl

 | 

Shipping total after discount (tax excl.）
 | 

 
| 

----shippingTotalTaxExcl

 | 

OBJECT
 | 

Shipping total (tax excl.）

Shipping amount excluding tax. 

 
 | 

- 
Shipping total (tax excl.）

 
| 

----shippingTemuTotalTaxExcl
 | 

OBJECT
 | 

Temu discount

Shipping amount paid by the  platform, excluding tax. If the order is not eligible for platform free shipping, this field is set to 0.

 
 | 

- 
Temu discount

 
| 

----productTaxCustomerTotal
 | 

OBJECT
 | 

Product Tax

Product tax amount actually paid by the consumer after discount. 

 
 | 

Product Tax
 | 

 
| 

----shippingTaxCustomerTotal
 | 

OBJECT
 | 

Shipping Tax after discount

Discounted shipping tax amount. 

  Calculation logic： shippingTaxCustomerTotal=shippingTax- shippingTaxTemuTotal
 | 

**Shipping Tax after discount**
 | 

 
| 

----shippingTax
 | 

OBJECT
 | 

Shipping tax

Shipping tax amount. 

 
 | 

- 
Shipping tax

 
| 

----shippingTaxTemuTotal
 | 

OBJECT
 | 

Temu discount

Shipping tax amount subsidized by the platform. If the order is not eligible for platform free shipping, this field is set to 0.

 
 | 

- 
Temu discount

 
| 

----productRefundsTotal
 | 

OBJECT
 | 

Product refund

Product refund amount. 

 
 | 

Product refund
 | 

 
| 

----customerPaidTotal
 | 

OBJECT
 | 

Total paid

Actual amount paid by the consumer. 

 Calculation logic：customerPaidTotal=  retailPriceCustomerTotalTaxExcl+shippingCustomerTotalTaxExcl+productTaxCustomerTotal+shippingTaxCustomerTotal-productRefundsTotal
 | 

Total paid
 | 

 

## 
Customer Paid

| 

**Properties**
 | 

**Type**
 | 

Description 
 | 

**Fields as displayed on the Temu platform**
 | 

**Temu platform order fields screenshot**
 
| 

---customerPaid
 | 

OBJECT
 | 

Sales proceeds

Amount paid by the consumer. 

 
 | 

 | 

 
| 

----retailPriceCustomerTotalTaxExcl

 | 

OBJECT
 | 

Retail price total after discounts(tax excel.)

Discounted retail price excluding tax. 

  Calculation logic：

retailPriceCustomerTotalTaxExcl=retailPriceTotalTaxExcl-retailPriceSellerDiscountTaxExcl-retailPriceTemuDiscountTaxExcl
 | 

**Retail price total after discounts(tax excel.)**
 | 

 
| 

----retailPriceTotalTaxExcl
 | 

OBJECT
 | 

Retail price (tax excel.)

Retail price excluding tax. 

 
 | 

- 
**Retail price (tax excel.)**

 
| 

----retailPriceSellerDiscountTaxExcl
 | 

OBJECT
 | 

Seller discount 

Seller discount amount included in the retail price. 

 
 | 

- 
Seller discount 

 
| 

----retailPriceTemuDiscountTaxExcl
 | 

OBJECT
 | 

Temu discount

Platform discount amount that is included in the retail price, excluding tax. 

 
 | 

- 
Temu discount

 
| 

----shippingCustomerTotalTaxExcl
 | 

OBJECT
 | 

Shipping total after discount (tax excl.）

Shipping amount paid by the consumer, excluding tax. 

 Calculation logic：

shippingCustomerTotalTaxExcl=shippingTotalTaxExcl-shippingTemuTotalTaxExcl

 | 

Shipping total after discount (tax excl.）
 | 

 
| 

----shippingTotalTaxExcl

 | 

OBJECT
 | 

Shipping total (tax excl.）

Shipping amount excluding tax. 

 
 | 

- 
Shipping total (tax excl.）

 
| 

----shippingTemuTotalTaxExcl
 | 

OBJECT
 | 

Temu discount

Shipping amount paid by the  platform, excluding tax. If the order is not eligible for platform free shipping, this field is set to 0.

 
 | 

- 
Temu discount

 
| 

----productTaxCustomerTotal
 | 

OBJECT
 | 

Product Tax

Product tax amount actually paid by the consumer after discount. 

 
 | 

Product Tax
 | 

 
| 

----shippingTaxCustomerTotal
 | 

OBJECT
 | 

Shipping Tax after discount

Discounted shipping tax amount. 

  Calculation logic： shippingTaxCustomerTotal=shippingTax- shippingTaxTemuTotal
 | 

**Shipping Tax after discount**
 | 

 
| 

----shippingTax
 | 

OBJECT
 | 

Shipping tax

Shipping tax amount. 

 
 | 

- 
Shipping tax

 
| 

----shippingTaxTemuTotal
 | 

OBJECT
 | 

Temu discount

Shipping tax amount subsidized by the platform. If the order is not eligible for platform free shipping, this field is set to 0.

 
 | 

- 
Temu discount

 
| 

----productRefundsTotal
 | 

OBJECT
 | 

Product refund

Product refund amount. 

 
 | 

Product refund
 | 

 
| 

----customerPaidTotal
 | 

OBJECT
 | 

Total paid

Actual amount paid by the consumer. 

 Calculation logic：customerPaidTotal=  retailPriceCustomerTotalTaxExcl+shippingCustomerTotalTaxExcl+productTaxCustomerTotal+shippingTaxCustomerTotal-productRefundsTotal
 | 

Total paid
 | 

 
# 
**Interface Access Permission Application Process**

This API is classified as a sensitive interface and is subject access permission control. Please submit a permission application under the appropriate role based on your application type. After the permission application process is approved, re-authorization and an updated access token are required before the API can be called normally.

- 
**Self-developed applications**: Please contact your store operations manager to submit the permission application on your behalf.

- 
**Third-party ERP applications**: Please contact your platform business representative to submit the permission application on your behalf.
