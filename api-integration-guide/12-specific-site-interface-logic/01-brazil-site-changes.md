# Changes to the Associated Interface of the Newly Opened Site in Brazil

**Last update:** 2025-08-17 06:49:02

---

## I. Background of Changes

- Based on the unique **tax logic** in Brazil: Merchants are required to provide a tax invoice before shipping.
- Based on the specific **fulfillment model** in Brazil: By default, the vast majority of orders will be fulfilled through **Buy-shipping on TEMU** (shipping label cost borne by Temu). Only specific orders on the whitelist can switch to self-shipment.

---

## II. Changes to Corresponding Interfaces

### Changes caused by special tax logic:

- During product listing, `costTemplate` **must** be filled in.
- An address field for the consumer's **tax number** is added to be returned for generating invoices.
- The CALL form interface for retrieving available logistics providers for Brazilian orders requires an additional parameter `invoiceAccessKey` (unique identifier for tax invoices).
- Since the cost is borne by the platform, only the platform's assessed unique available channel is returned — **no estimated freight amount**.
- For Brazilian orders under the CALL form interface:
  - Additional parameter `invoiceAccessKey` is required.
  - Only after successful verification can the call succeed.
  - Supports **re-calling** for packages already successfully called.
  - Use `confirmAcceptance = SUCCESSFUL_RETRY` to re-call with a new `accesskey`.

### Restrictions on fulfillment mode:

- Order marking added: `RESTRICT_SELF_SHIPPING`, `RESTRICT_CALL_SHIPPING`.
- Orders restricting self-fulfillment → error when calling self-fulfillment interface.
- Orders restricting CALL form → error when calling Buy-shipping on TEMU interface.

---

## III. Detailed Logic of Interface Changes

### 1. Product Interface Change: Mandatory `costTemplateId`

- **Interface:** `bg.local.goods.add`
- **Change:** Added mandatory validation for `costTemplateId` field during submission.
- **Affected area:** Products listed in a Brazilian store.

---

### 2. Order Interface Change: `fulfillmentWarning` field

- **Interfaces:** `bg.order.list.v2.get`, `bg.order.detail.v2.get`
- **Changes:**
  - Order restricted from self-shipment: `fulfillmentWarning` returns `RESTRICT_SELF_SHIPPING`
  - Order restricted from call shipping: `fulfillmentWarning` returns `RESTRICT_CALL_SHIPPING`
- **Affected areas:** Brazilian orders

**Example response (RESTRICT_SELF_SHIPPING):**
```json
{
  "parentOrderMap": {
    "fulfillmentWarning": ["RESTRICT_SELF_SHIPPING"],
    "regionId": 29,
    "parentOrderSn": "PO-029-06682144932474090",
    "siteId": 132,
    "parentOrderStatus": 2
  }
}
```

**Example response (RESTRICT_CALL_SHIPPING):**
```json
{
  "parentOrderMap": {
    "fulfillmentWarning": ["RESTRICT_CALL_SHIPPING"],
    "regionId": 29,
    "parentOrderSn": "PO-029-06420938453110273",
    "siteId": 132
  }
}
```

---

### 3. Order Address Interface Change: Consumer Tax Number

- **Interfaces:** `bg.order.shippinginfo.v2.get`, `bg.order.decryptshippinginfo.get`
- **Changes:** Returns real phone number + virtual email + four-level zoning address + `taxCode` (consumer CPF number)
- **Affected regions:** Brazilian orders

**Example response:**
```json
{
  "result": {
    "regionName1": "Brazil",
    "regionName2": "Churrasco",
    "regionName3": "Red",
    "regionName4": "Meat",
    "mobile": "+55 1234232122",
    "mail": "qsblabp3ak12066@g.shipping.temuemail.com",
    "taxCode": "00412950995",
    "addressLine1": "1231sads2",
    "postCode": "00000-001",
    "receiptName": "ROSANA west"
  }
}
```

---

### 4. Shipping Interface: Error When Order Restrictions Prevent Automatic Shipment

- **Interfaces:** `bg.logistics.shipment.v2.confirm`, `bg.logistics.shipment.sub.confirm`, `bg.logistics.shipment.shippingtype.update`
- **Change:** Added error code `120015537`, message: `"Brazil orders require Temu shipping labels exclusively"`
- **Affected regions:** Brazil — restricted self-shipped orders

---

### 5. Available Channels Interface: Mandatory `invoiceAccessKey`

- **Interface:** `bg.logistics.shippingservices.get`
- **Changes:**
  - Intercepts errors when attempting new call for call form orders.
  - Requires mandatory field `invoiceAccessKey` — only after verification returns estimated/successful channels.
  - **No longer returns channel quotation** (`estimatedAmount` = null).
- **Affected regions:** Brazil — restricted self-fulfillment orders

**Error codes:**
- `120015538`: Brazil orders restricted to TEMU platform shipping labels for self-fulfillment
- `120011094`: Required parameter `invoiceAccessKey` is missing
- `120011088`: Invoice access key verification failed

---

### 6. CALL and RECALL Interfaces: Mandatory `invoiceAccessKey`

- **Interfaces:** `bg.logistics.shipment.create`, `bg.logistics.shipment.update`, `bg.logistics.shipment.result.get`
- **Changes:**
  - Intercepts new Buy-shipping calls for restricted call order forms.
  - Requires mandatory `invoiceAccessKey`.
  - Supports re-calling after successful call (use `confirmAcceptance: ["SUCCESSFUL_RETRY"]`).

**Successful CALL request example:**
```json
{
  "type": "bg.logistics.shipment.create",
  "sendRequestList": [{
    "parentOrderSn": "PO-029-18238241505913274",
    "channelId": 640131572895744,
    "invoiceAccessKey": "35250557643824000105550010000005531177558229"
  }]
}
```

**Successful RECALL request example:**
```json
{
  "type": "bg.logistics.shipment.update",
  "retrySendPackageRequestList": [{
    "packageSn": "PK-0592545917174551592",
    "invoiceAccessKey": "36250557643824000105550010000005531177558999",
    "confirmAcceptance": ["SUCCESSFUL_RETRY"]
  }]
}
```

---

### 7. Call Result Interface: Added `invoiceAccessKey` Field

- **Interface:** `bg.logistics.shipment.result.get`
- **Change:** Added return field `invoiceAccessKey` in output parameters. `estimatedAmount` = null for Brazil.
- **Affected regions:** Brazil — restricted self-fulfillment orders
