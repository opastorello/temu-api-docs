# Special Category Requirements

In **bg.local.goods.cats.get**, the `expandCatType` field (0 = Apparel, 1 = Others, 2 = Books, 3 = DVD, 4 = CD, 5 = Seed) indicates special category types. Certain categories may have additional requirements when listing products in the Temu Seller Center.

### 

**Books Category**

- 
#### 

**Require attributes: Publisher **

![image](https://bstatic.kwcdn.com/open-outer/212a0ccbb8/a8cf272197d10809be7001b560ac2b8b.png)

Publisher information needs to be created by the seller in advance on the [Seller Center -> Products -> Brands & intellectual property -> Copyright] page.

Please note this attribute's "controlType" is 0 in temu.local.product.attributes.get (**0 – Input only: **Users can only enter a value manually), so the goodsProperty.value parameter's provided value must exist in the seller's temu shop. If goodsProperty.value is not found in [Seller Center~Performance~Account health~Copyright] 

Please note that this attribute’s `controlType` is `0` in `temu.local.product.attributes.get` (0 – Input only: users can only enter a value manually). Therefore, the value provided in the `goodsProperty.value` parameter must already exist in the seller’s Temu shop. If a mismatch occurs, the product may still be successfully added in Seller Center; however, the **Publisher** attribute will be considered empty.

- 
#### 

**Require ISBN**

![image](https://bstatic.kwcdn.com/open-outer/212a0ccbb8/154b5b1867c0923a4c772e7a7e87d2ad.png)

temu.local.goods.v2.add

| Properties | Description |
|---|---|
| barCodeType | External product code type, 1=EAN 2=UPC 3=ISBN 4=GTIN-14. |
| barCodeId | External goods code. It needs to conform to the standard specifications of the encoding type. |

a. `barCodeType` is mandatory, and the value must be **3**.

b. `barCodeId` is mandatory and must match the actual book information; otherwise, it may ultimately affect the product’s listing and sale. 

Seller or Partners can verify it at: [https://eancheck.com/](https://eancheck.com/)

bg.local.goods.add

| Properties | Description |
|---|---|
| externalProductType | External product code type, 1=EAN 2=UPC 3=ISBN 4=GTIN-14. |
| externalProductId | External goods code. It needs to conform to the standard specifications of the encoding type. |

a. `externalProductType` is mandatory, and the value must be **3**.

b. `externalProductId` is mandatory and must match the actual book information; otherwise, it may ultimately affect the product’s listing and sale. 

Seller or Partners can verify it at: [https://eancheck.com/](https://eancheck.com/)

### 

**DVD and CD category**

- 
#### 

** Require attributes: Studio/Manufacturer**

![image](https://bstatic.kwcdn.com/open-outer/212a0ccbb8/343483dc2cec19a4b1d284f209e3db17.png)

Studio/Manufacturer needs to be created by the seller in advance on the [Seller Center -> Products -> Brands & intellectual property -> Copyright] page.

- 
#### 

**Require ISBN** if the copyright information selected in "Studio/Manufacturer" is configured "China" as "Manufacturer's country of origin"

![image](https://bstatic.kwcdn.com/open-outer/212a0ccbb8/2583a2f005ab7faed4981325dfb49f10.png)

![image](https://bstatic.kwcdn.com/open-outer/212a0ccbb8/67440ee89fa6529d944d1600a0d85a48.png)

temu.local.goods.v2.add

| Properties | Description |
|---|---|
| barCodeType | External product code type, 1=EAN 2=UPC 3=ISBN 4=GTIN-14. |
| barCodeId | External goods code. It needs to conform to the standard specifications of the encoding type. |

a. `barCodeType` is mandatory, and the value must be **3**.

b. `barCodeId` is mandatory and must match the actual book information; otherwise, it may ultimately affect the product’s listing and sale. 

Seller or Partners can verify it at: [https://eancheck.com/](https://eancheck.com/)

bg.local.goods.add

| Properties | Description |
|---|---|
| externalProductType | External product code type, 1=EAN 2=UPC 3=ISBN 4=GTIN-14. |
| externalProductId | External goods code. It needs to conform to the standard specifications of the encoding type. |

a. `externalProductType` is mandatory, and the value must be **3**.

b. `externalProductId` is mandatory and must match the actual book information; otherwise, it may ultimately affect the product’s listing and sale. 

Seller or Partners can verify it at: [https://eancheck.com/](https://eancheck.com/)

***Additional Notes:** EAN, UPC, GTIN-14 are optional fields and are not subject to mandatory validation constraints during product creation. No additional special requirements apply to other categories at this time.
