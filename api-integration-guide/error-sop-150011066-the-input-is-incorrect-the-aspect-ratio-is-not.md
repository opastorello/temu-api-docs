# [Error SOP][150011066]The input {*} is incorrect, the aspect ratio is not {*}.

| Error Code | Error Message |
|---|---|
| 150011066 | The input {*} is incorrect, the aspect ratio is not {*}. |

- 

**Root Cause:**

The image provided in the request payload doesn't meet the requirements in temu seller center.

Requirements:

******

******

******

******

******

******

| Functional module | Material | Dimensions | Size | Type | Note |
|---|---|---|---|---|---|
| Product Description | Detail Video | Duration: ≤180sAspect Ratio: 1:1, 4:3, 16:9Resolution: ≥720P | ≤300 MB | wmv, avi, 3gp, mov, mp4, flv, rmvb, mkv, m4v, x-flv, WMV, AVI, 3GP, MOV, MP4, FLV, RMVB, MKV, M4V, X-FLV | Product Description, Detail Video, Product Images make up the detailed presentation. By default, the video is displayed as the first element of this presentation. |
| Product Images | Quantity: ≤50Aspect Ratio: ≥1:3Width: ≥480pxHeight: ≥480px | ≤3MB | JPEG, JPG, PNG |
| SKU Carousel Images | Apparel Carousel Images | Quantity: 1-10Aspect Ratio: 3:4Width:≥1340pxHeight: ≥1785px | ≤3 MB | JPEG, JPG, PNG | Take the first image of each SKC as the SKC preview image |
| Non-Apparel Carousel Images | Quantity: 1-10Aspect Ratio: 1:1Width:≥800pxHeight: ≥800px | ≤3 MB | JPEG, JPG, PNG | SPU carousel- Take the first image of the first SKU as the first image- Splice the images of each SKU from the second image onwards after the first imageSKU preview image- Take the first image of each SKU as the SKU preview image |
| Product Video | Product Video | Quantity: ≤1Aspect Ratio: Not restrictedDuration: ≤60sResolution: ≥720P | ≤100 MB | wmv, avi, 3gp, mov mp4, flv, rmvb, mkv, m4v, x-flv, WMV, AVI, 3GP, MOV, MP4, FLV, RMVB, MKV, M4V, X-FLV |  |
| Safety and Compliance | Product Actual Images | Quantity: 1-6 | ≤3 MB | JPG, PNG, JPEG |  |
| Product Guides or Documents | Quantity: same as the language requirement | ≤3 MB | JPG, PNG, JPEG |  |

***Please note:** In the `bg.local.goods.cats.get` API, when `catType = 0` (Apparel), the images in `skuList` must comply with the Apparel Carousel Image requirements:

Aspect Ratio: 3:4

Width:≥1340px

Height: ≥1785px

- 

**Next Step**

Use the `bg.local.goods.image.upload` API to replace the image with one that meets the requirements.

| Parameters | Description |  |
|---|---|---|
| scalingType | Scaling Target: 0-Original size, 1-800*800 (1:1), 2-1350*1800 (3:4) | Modify ratio |
| compressionType | Compression: 0-false, 1-true | Modify size |
| Format conversion: 0-jpg, 1-jpeg, 2-png | While compressionType=1 and formatConversionType=0 or 1. To complete the image compression | Modify format |
