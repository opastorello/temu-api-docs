# Common Issues During Product Publishing

During the product publishing process, the following common issues may arise, which can lead to confusion. To address this, we have created a dedicated guide to describe frequently encountered errors, helping developers quickly identify and resolve problems.

1. 

**Incorrect **`**importDesignation**`** value (e.g., capitalization, spaces, etc.)**

- 

Error Message:

"Invalid Request Parameters"

- 

Requirement:

Currently, the following four values are supported: ["Imported", "Made in the USA", "Made in the USA and Imported", "Made in the USA or Imported"]

Case sensitivity and the number of spaces between words must be exact.

- 

Error Example:

Error Cause: The first letter of `importDesignation` was lowercase.

```
"goodsBasic": {  
  "catId": 28949,  
  "goodsName": "Drop Shoulder Kangaroo Pocket Hoodie, Casual Zipper Long Sleeve Drawstring Hoodies Sweatshirt, Women's Clothing goods2",  
  "importDesignation": "imported"  
 }
```

1. 

`**outSkuSn**`** and **`**outGoodsSn**`** length issue**

- 

Requirement:

`outSkuSn` and `outGoodsSn` should have a length of less than 100 characters(<=100).

- 

Error Example:

Error Cause: `out_sku_sn` length exceeded 100 characters(<=100).

```
 "skuList": [  
  {  
   "outSkuSn": "101 chars is too long for the out sku sn",  
   "height": "20.0",
```

1. 

**Issues with images, videos, and links**

- 

Requirement:

The backend will validate the size, dimensions, and ratio of images and videos. Therefore, links and their content should follow the guidelines.

The `image` field requires at least 3 distinct images.

- 

Error Example:

Error Cause: The link must be accessible.

```
 "skuList": [  
  {  
   "outSkuSn": "101 chars is too long for the out sku sn",  
   "height": "20.0",  
   "images": [  
    "https://img.kwcdn.com/local-goods-image/1fad1860e0/47d92024-994d-4092-ab2a-53f874bebe63.png",  
    "https://img.kwcdn.com/local-goods-image/1fad1860e0/47d92024-994d-4092-ab2a-53f874bebe63.png",  
    "https://img.kwcdn.com/local-goods-image/1fad1860e0/47d92024-994d-4092-ab2a-53f874bebe63.png"  
   ],
```

1. 

**Issues with qualification links**

- 

Error:

"Invalid Request Parameters"

- 

Requirement:

The backend will validate qualification-related files and images, but unlike other links, these links are signed with `mallId`, so switching stores may render the links unusable.

- 

Error Example:

Error Cause: The qualification file for Store A was used for Store B.

![image](https://bstatic.kwcdn.com/open-outer/1f193488500/a41d99d66532b30e45d8c6e3bf1b40ec.png)

1. 

`**specIdList**`** in the SKU list and the relationship between **`**specId**`** in **`**goodsProperties**`

- 

Error:

"System error, please try again later"

- 

Requirement:

When adding products, there can be multiple SKUs, and each SKU's `specIdList` should contain at least one `specId` and no more than two `specIds`. Each `specId` must also be listed in `goodsProperties`.

- 

Error Example:

Error Cause 1: Not all `specId` in SKU are listed in `goodsProperties` (or not completely listed).

Error Cause 2: Each SKU can have no more than two `specId`.

![image](https://bstatic.kwcdn.com/open-outer/1f193488500/d5af31090ac1ff5ee61e2bb45efbb96c.png)

1. 

`**costTemplateId**`** is linked to **`**mallId**`

- 

Requirement:

Each store has its own shipping template, as configured.

When adding products, the store information is used to query the shipping template of that store, which will validate whether the `costTemplateId` is correct.

1. 

**Field type issues**

- 

Requirement:

  - 

The `weight`, `length`, `width`, and `height` fields in `skuList` should be of type `String`, not `Integer`.

  - 

For volume parameters, the integer part should have no more than 3 digits, and the decimal part should have no more than 1 digit. For weight parameters, the integer part should have no more than 4 digits, and the decimal part should have no more than 1 digit.

- 

Error Example:

Error Cause: `weight`, `length`, `width`, `height` fields were incorrectly entered as `Integer` types.

1. 

**Missing trademark information**

- 

Error:

"Invalid Request Parameters"

- 

Cause:

If the product attribute includes a brand (i.e., `name=brand`, `templatePid=597281`, `refPid=1960`), trademark information must be included when adding the product.

1. 

**Incorrect attribute field mapping**

- 

Error:

"Invalid Request Parameters"

- 

Cause:

The product attribute template returned `templatePid=597281`, but when adding the product, `templatePid` was incorrectly set to `504023`.

When adding a product, the relevant attribute fields must match the fields returned by the interface.
