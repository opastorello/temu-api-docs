# Ads Introduction

## 

**Temu ads Introduction**

**Introduction:** To empower sellers in acquiring enhanced traffic, attracting customers, and driving sales growth, we have launched **Temu Ads** – a streamlined advertising solution enabling sellers to rapidly create and optimize campaigns.

## 

**How to Create Ads on ads.temu.com**

1. 

**Sign In & Agreement**

  - 

Access the advertising system by logging into [ads.temu.com](https://ads.temu.com/) or navigating through the **"Product ADS"** tab in the left-hand primary menu of the merchant portal.

  - 

Have your primary account sign the Advertising Services Agreement.

1. 

**Set Up Financial Management**

  - 

Configure your **Advertising  Reserve** under the **"Billing"** section.

1. 

**Launch Product Ads**

  - 

Go to the **"Product Ads"** section.

  - 

Select the product(s) to promote.

  - 

Set your **ROAS bid** and** Daily Budget** to initiate the campaign.

## 

**API List**

You can create and manage advertising campaigns at [https://us.ads.temu.com](https://us.ads.temu.com/). Alternatively, you may utilize the Advertising API to perform these operations. Below is the list of Advertising APIs:

1. 

**Query Advertising ROAS**

  - 

*Functionality*: Supports querying tiered ROAS recommendations for products.

  - 

*Best Practice*: Use system-recommended ROAS when creating campaigns for optimal performance.

  - 

**Endpoint**: `temu.searchrec.ad.roas.pred`

1. 

**Store-Level Campaign Analytics**

  - 

*Functionality*: Retrieves store-level advertising metrics including ROAS, order volume, impressions, clicks, and CTR.

  - 

**Endpoint**: `temu.searchrec.ad.reports.mall.query`

1. 

**Product-Level Campaign Analytics**

  - 

*Functionality*: Retrieves product-level advertising metrics including ROAS, order volume, impressions, clicks, and CTR.

  - 

**Endpoint**: `temu.searchrec.ad.reports.goods.query`

1. 

**Create Advertising Campaign**

  - 

*Functionality*: Enables creation of campaigns for specific products with configurable daily budgets and ROAS targets.

  - 

**Endpoint**: `temu.searchrec.ad.create`

1. 

**Query Campaign Status**

  - 

*Functionality*: Fetches real-time campaign details (e.g., active daily budget, target ROAS).

  - 

**Endpoint**: `temu.searchrec.ad.detail.query`

1. 

**Query Advertising Operation Logs**

  - 

*Functionality*: Provides access to operational logs for campaign troubleshooting and auditing.

  - 

**Endpoint**: `temu.searchrec.ad.log.query`

1. 

**Product Advertising Eligibility Check**

  - 

*Functionality*: Verifies product eligibility for advertising campaigns.

  - 

*Workflow Requirement*: Mandatory pre-check before invoking the campaign creation API.

  - 

**Endpoint**: `temu.searchrec.ad.goods.create.query`

1. 

**Modify Advertising Campaign**

  - 

*Functionality*: Allows dynamic updates to ROAS targets and daily budgets for active campaigns.

  - 

**Endpoint**: `temu.searchrec.ad.modify`

1. 

**Batch Modify Advertising**

  - 

*Functionality: *Enables batch updates to ROAS targets, daily budgets, and campaign status for multiple products. 

  - 

*Workflow Requirement:* Non-atomic operation (supports partial success); subject to a strict rate limit of 1 request per 5 seconds. 

  - 

**Endpoint:**`temu.searchrec.ad.batch.modify`
