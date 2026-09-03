# Guide of Order Amount V1 / V2 / V3 Query

# 

**Background**

To improve clarity around order amount fields and reduce misunderstandings related to tax calculations, subsidy treatments, and discount amounts, the Order Amount API (bg.order.amount.query / temu.order.amount.v2.query / temu.order.amount.v3.query) has been launched. This version standardizes field definitions and calculation rules to ensure a consistent and transparent presentation of order amounts.

# 

**Difference**

| API | Limitation | Site ID |
|---|---|---|
| bg.order.amount.query | N/A | Open for all countries |
| temu.order.amount.v2.query | Countries requiring tax calculation | 105, 106, 109, 107, 112, 140, 137, 145, 138, 143, 108, 142, 139, 113, 144, 111, 115, 147, 141, 146, 117, 150, 116, 149, 148, 174, 118, 119, 110 |
| temu.order.amount.v3.query | For countries that do not levy separate taxes, the order's merchandise value and shipping costs are inclusive of taxes by default. | 156, 158, 159, 168, 165, 166 |

Reference: [Model site and region](https://partner.temu.com/documentation?menu_code=38e79b35d2cb463d85619c1c786dd303&sub_menu_code=07938e60f95344a0a9444f524ea61e31)

# 

**Order structure and calculation relationships**

When Temu displays order amounts externally, product amounts, shipping fees, and their corresponding taxes are itemized separately. Detailed breakdowns of discounts and subsidies are also provided. This allows sellers to clearly understand the composition of order amounts and how settlement calculations are derived.

The order amount API is divided into two main modules: Sales Proceeds and Customer Paid. For each parent order, the correspondence between these two modules—as shown in the platform interface and API response—and their corresponding calculation logic is outlined below.

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

![image](https://bstatic.kwcdn.com/open-outer/211523406cc/899167e1c042762edaa99557a471a005)

**Corresponding API Calculation:**

Copy

Switch color

estimatedSettlementTotal

= basePriceDiscountedTotal

+ shippingTotalTaxExcl

+ productTax

+ shippingTax

+ taxTemuDiscount

- estimatedDeduction

## 

**Customer paid**

This section mainly displays the **actual amount paid by the customer** and its breakdown.

**Temu platform display logic: Total paid**

- 

This is the actual amount paid by the customer.

- 

The total amount = Retail price after discount * Quantity + Shipping total + Tax total − Refunds total.

![image](https://bstatic.kwcdn.com/open-outer/211523406cc/65237f18ff21b6036a5e9e2fc533a5e9)

**Corresponding API Calculation:**

Copy

Switch color

totalPaid

= retailPriceCustomerTotalTaxExcl

+ shippingCustomerTotalTaxExcl

+ productTaxCustomerTotal

+ shippingTaxCustomerTotal

- productRefundsTotal

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

![image](https://bstatic.kwcdn.com/open-outer/211523406cc/c4db0067c2b84dbfe5baac018567fef9)

- 

- 

- 

****

![image](https://bstatic.kwcdn.com/open-outer/211523406cc/674c746ac1b1de2840a8c8b6f6bab007)

- 

- 

****

![image](https://bstatic.kwcdn.com/open-outer/211523406cc/f20da2872a2eeca2d6ff273fc0931f6d)

- 

**

- 

**

****

![image](https://bstatic.kwcdn.com/open-outer/211523406cc/30dcb54cf16f9d501178d1bdfb885ee1)

- 

- 

![image](https://bstatic.kwcdn.com/open-outer/211523406cc/6eb8b591145c05050d4427db0bbb5421)

****

![image](https://bstatic.kwcdn.com/open-outer/211523406cc/812df041cbb194ad864a0c09ffe074f2)

****

![image](https://bstatic.kwcdn.com/open-outer/211523406cc/8d9e96c82a3c50694b51251f23b03157)

****

![image](https://bstatic.kwcdn.com/open-outer/211523406cc/6def5966d02e3baf20db2d2edba78219)

- 

****

- 

- 

![image](https://bstatic.kwcdn.com/open-outer/211523406cc/b5948d883b0ddbe72210bd662f18a8a0)

- 

- 

![image](https://bstatic.kwcdn.com/open-outer/211523406cc/99d4bf5eb33fc9d183bf35fa69a89559)

****

![image](https://bstatic.kwcdn.com/open-outer/211523406cc/e088d195353ae6613dac96320ac99557)

- 

- 

![image](https://bstatic.kwcdn.com/open-outer/211523406cc/e8d8ebf052f77fb1cd9ad91d283aa77b)

![image](https://bstatic.kwcdn.com/open-outer/211523406cc/b74f9e542219e342fde74bdc7d00a0f0)

| Properties | Type | Description | Fields as displayed on the Temu platform | Temu platform order fields screenshot |
|---|---|---|---|---|
| ---salesProceeds | OBJECT | Sales proceeds |  |  |
| ----basePriceDiscountedTotal | OBJECT | Base price total after seller discountCalculation logic：basePriceDiscountedTotal = basePriceTotal - basePriceSellerDiscount - basePriceOff | Base price total after discount |  |
| ----basePriceTotal | OBJECT | Base price totalBase price before discount. If there is an active promotional base price, this field displays the promotional base price. | Base price total |
| ----basePriceSellerDiscount | OBJECT | Seller discountThis discount is generated from seller-initiated promotional activities. | Seller discount |
| ----basePriceOff | OBJECT | base price offThis amount includes personalized discounts and cross-store cumulative discounts. | base price off |
| ----shippingTotalTaxExcl | OBJECT | Shipping total(tax excl.）Shipping amount excluding tax.Calculation logic：shippingTotalTaxExcl=shippingCustomerTotalTaxExcl+shippingTemuTotalTaxExcl | Shipping total(tax excl.） |  |
| ----shippingCustomerTotalTaxExcl | OBJECT | Customer paid-shipping totalShipping amount paid by the consumer, excluding tax. | Customer paid-Shipping |
| ----shippingTemuTotalTaxExcl | OBJECT | Platform incentive-ShippingShipping amount paid by the platform, excluding tax. If the order is not eligible for platform free shipping, this field is set to 0. | Platform incentive-Shipping |
| ----productTax | OBJECT | Product taxProduct tax amount.Calculation logic：productTax=productTaxCustomerDiscounted+productTaxTemu | Product tax |  |
| ----productTaxCustomerDiscounted | OBJECT | Customer paid-Product taxProduct tax amount paid by the consumer. | Not displayed on the Temu platform |
| ----productTaxTemu | OBJECT | Platform incentive-Product taxProduct tax amount subsidized by the platform. | Not displayed on the Temu platform |
| ----shippingTax | OBJECT | Shipping TaxShipping tax amount.Calculation logic：shippingTax=shippingTaxCustomerDiscounted+shippingTaxTemu | Shipping Tax |  |
| ----shippingTaxCustomerDiscounted | OBJECT | Customer paid-Shipping taxShipping tax amount paid by the consumer after discount. | Customer paid-Shipping tax |
| ----shippingTaxTemu | OBJECT | Platform incentive-Shipping TaxShipping tax amount subsidized by the platform. If the order is not eligible for platform free shipping, this field is set to 0. | Platform incentive-Shipping Tax |
| ----taxTemuDiscount | OBJECT | Tax on platform discount.Only returned for Japan and South Korea sites. | Tax on platform discount |  |
| ----estimatedDeduction | OBJECT | Estimated deduction amountEstimated deduction amount is calculated based on theamount of customer's refunds. | Estimated deduction amount |  |
| ----estimatedSettlementTotal | OBJECT | Estimated total settlement amountEstimated total revenue for the seller.Calculation logic：estimatedSettlementTotal= basePriceDiscountedTotal+shippingTotalTaxExcl+productTax+shippingTax+taxTemuDiscount-estimatedDeduction | Estimated total settlement amount |  |
| ---customerPaid | OBJECT | Sales proceedsAmount paid by the consumer. |  |  |
| ----retailPriceCustomerTotalTaxExcl | OBJECT | Retail price total after discounts(tax excel.)Discounted retail price excluding tax.Calculation logic：retailPriceCustomerTotalTaxExcl=retailPriceTotalTaxExcl-retailPriceSellerDiscountTaxExcl-retailPriceTemuDiscountTaxExcl | Retail price total after discounts(tax excel.) |  |
| ----retailPriceTotalTaxExcl | OBJECT | Retail price (tax excel.)Retail price excluding tax. | Retail price (tax excel.) |
| ----retailPriceSellerDiscountTaxExcl | OBJECT | Seller discountSeller discount amount included in the retail price. | Seller discount |
| ----retailPriceTemuDiscountTaxExcl | OBJECT | Temu discountPlatform discount amount that is included in the retail price, excluding tax. | Temu discount |
| ----shippingCustomerTotalTaxExcl | OBJECT | Shipping total after discount (tax excl.）Shipping amount paid by the consumer, excluding tax.Calculation logic：shippingCustomerTotalTaxExcl=shippingTotalTaxExcl-shippingTemuTotalTaxExcl | Shipping total after discount (tax excl.） |  |
| ----shippingTotalTaxExcl | OBJECT | Shipping total (tax excl.）Shipping amount excluding tax. | Shipping total (tax excl.） |
| ----shippingTemuTotalTaxExcl | OBJECT | Temu discountShipping amount paid by the platform, excluding tax. If the order is not eligible for platform free shipping, this field is set to 0. | Temu discount |
| ----productTaxCustomerTotal | OBJECT | Product TaxProduct tax amount actually paid by the consumer after discount. | Product Tax |  |
| ----shippingTaxCustomerTotal | OBJECT | Shipping Tax after discountDiscounted shipping tax amount.Calculation logic： shippingTaxCustomerTotal=shippingTax- shippingTaxTemuTotal | Shipping Tax after discount |  |
| ----shippingTax | OBJECT | Shipping taxShipping tax amount. | Shipping tax |
| ----shippingTaxTemuTotal | OBJECT | Temu discountShipping tax amount subsidized by the platform. If the order is not eligible for platform free shipping, this field is set to 0. | Temu discount |
| ----productRefundsTotal | OBJECT | Product refundProduct refund amount. | Product refund |  |
| ----customerPaidTotal | OBJECT | Total paidActual amount paid by the consumer.Calculation logic：customerPaidTotal= retailPriceCustomerTotalTaxExcl+shippingCustomerTotalTaxExcl+productTaxCustomerTotal+shippingTaxCustomerTotal-productRefundsTotal | Total paid |  |

## 

Customer Paid

****

****

****

****

****

![image](https://bstatic.kwcdn.com/open-outer/211523406cc/5cdfb6992c19064c2b690a5f61bf67f3)

- 

****

- 

- 

![image](https://bstatic.kwcdn.com/open-outer/211523406cc/15a4de07407744e4f8193673fb3028c8)

- 

- 

![image](https://bstatic.kwcdn.com/open-outer/211523406cc/1e25dfe9cb2bb7fd487e7110860113a8)

****

![image](https://bstatic.kwcdn.com/open-outer/211523406cc/9b5166eb5b4ae0c11c168b8f80c298d2)

- 

- 

![image](https://bstatic.kwcdn.com/open-outer/211523406cc/31f3ff013dbf5011e5fa04f174d25090)

![image](https://bstatic.kwcdn.com/open-outer/211523406cc/be6844fc909ffcebbbac077bcbf18842)

| Properties | Type | Description | Fields as displayed on the Temu platform | Temu platform order fields screenshot |
|---|---|---|---|---|
| ---customerPaid | OBJECT | Sales proceedsAmount paid by the consumer. |  |  |
| ----retailPriceCustomerTotalTaxExcl | OBJECT | Retail price total after discounts(tax excel.)Discounted retail price excluding tax.Calculation logic：retailPriceCustomerTotalTaxExcl=retailPriceTotalTaxExcl-retailPriceSellerDiscountTaxExcl-retailPriceTemuDiscountTaxExcl | Retail price total after discounts(tax excel.) |  |
| ----retailPriceTotalTaxExcl | OBJECT | Retail price (tax excel.)Retail price excluding tax. | Retail price (tax excel.) |
| ----retailPriceSellerDiscountTaxExcl | OBJECT | Seller discountSeller discount amount included in the retail price. | Seller discount |
| ----retailPriceTemuDiscountTaxExcl | OBJECT | Temu discountPlatform discount amount that is included in the retail price, excluding tax. | Temu discount |
| ----shippingCustomerTotalTaxExcl | OBJECT | Shipping total after discount (tax excl.）Shipping amount paid by the consumer, excluding tax.Calculation logic：shippingCustomerTotalTaxExcl=shippingTotalTaxExcl-shippingTemuTotalTaxExcl | Shipping total after discount (tax excl.） |  |
| ----shippingTotalTaxExcl | OBJECT | Shipping total (tax excl.）Shipping amount excluding tax. | Shipping total (tax excl.） |
| ----shippingTemuTotalTaxExcl | OBJECT | Temu discountShipping amount paid by the platform, excluding tax. If the order is not eligible for platform free shipping, this field is set to 0. | Temu discount |
| ----productTaxCustomerTotal | OBJECT | Product TaxProduct tax amount actually paid by the consumer after discount. | Product Tax |  |
| ----shippingTaxCustomerTotal | OBJECT | Shipping Tax after discountDiscounted shipping tax amount.Calculation logic： shippingTaxCustomerTotal=shippingTax- shippingTaxTemuTotal | Shipping Tax after discount |  |
| ----shippingTax | OBJECT | Shipping taxShipping tax amount. | Shipping tax |
| ----shippingTaxTemuTotal | OBJECT | Temu discountShipping tax amount subsidized by the platform. If the order is not eligible for platform free shipping, this field is set to 0. | Temu discount |
| ----productRefundsTotal | OBJECT | Product refundProduct refund amount. | Product refund |  |
| ----customerPaidTotal | OBJECT | Total paidActual amount paid by the consumer.Calculation logic：customerPaidTotal= retailPriceCustomerTotalTaxExcl+shippingCustomerTotalTaxExcl+productTaxCustomerTotal+shippingTaxCustomerTotal-productRefundsTotal | Total paid |  |

# 

**Interface Access Permission Application Process**

This API is classified as a sensitive interface and is subject access permission control. Please submit a permission application under the appropriate role based on your application type. After the permission application process is approved, re-authorization and an updated access token are required before the API can be called normally.

- 

**Self-developed applications**: Please contact your store operations manager to submit the permission application on your behalf.

- 

**Third-party ERP applications**: Please contact your platform business representative to submit the permission application on your behalf.
