# temu.local.goods.v2.add

**Add New Items On Temu**

Add New Items On Temu

**Method:** POST  
**URL:** https://openapi-b-global.temu.com/openapi/router

---

## Common Parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| type | 4 | No |  |
| app_key | 4 | No |  |
| access_token | 4 | No |  |
| sign | 4 | No |  |
| timestamp | 4 | No |  |
| data_type | 4 | No |  |
| version | 4 | No |  |

## Request Parameters

| Parameter | Type | Required | Description | Example |
|---|---|---|---|---|
| language | 4 | No |  |  |
| goodsBasic | 6 | No |  |  |
| goodsServicePromise | 6 | No |  |  |
| goodsProperty | 8 | No |  |  |
| goodsOriginInfo | 6 | No |  |  |
| goodsSize | 6 | No |  |  |
| skuList | 8 | No |  |  |

## Response Parameters

| Parameter | Type | Required | Description | Example |
|---|---|---|---|---|
| success | 5 | No |  |  |
| errorCode | 1 | No |  |  |
| errorMsg | 4 | No |  |  |
| result | 6 | No |  |  |

## Error Codes

| Error Code | Message |
|---|---|
| 150010300 | Attribute input is non-compliant: {*} |
| 150010157 | The groupId  is required. |
| 150011100 | The number of products that can be listed each day is limited to {*}. Reason: {*} |
| 150011077 | {*} is invalid or not provided. |
| 150010255 | The selected level is not applicable to the current product. |
| 150010254 | Second-hand stores do not support publishing products in this category. |
| 150010253 | The selected businessScope is not applicable to the current product. |
| 150010257 | For "Made-to-order" products in the food category, "Shelf Life" field should be between 1-10 days. |
| 150010256 | This category is not supported for "Made-to-order" products. |
| 150011074 | Upload {*} to {*} images |
| 150011073 | Use {*} characters or fewer for bullet point |
| 150011072 | Bullet point must not exceed {*} |
| 150011071 | Use {*} characters or fewer for product description |
| 150011070 | Use {*} characters or fewer for product name |
| 150010251 | The value of the "numberOfPieces" field should be between 1-10000. |
| 150010239 | For "single set",  the "numberOfPieces" field can only be "1" and the "individuallyPacked" field can only be "yes". |
| 150010240 | For "Multi-piece set", "numberOfPieces" needs to be greater than 1. |
| 150010241 | The value of the "netContentNumber" field should be between 0-10000. |
| 150010242 | The value of the "originTotalNetContentNumber" field should be between 0-10000. |
| 150010243 | "multiplePackage" is required, please fill in and try again. |
| 150010244 | The "originNetContentNumber"/"originTotalNetContentNumber" and the "netContentUnitCode" field need to be filled in simultaneously |
| 150010245 | Fields "originNetContentNumber" and "originTotalNetContentNumber" cannot be filled in simultaneously. |
| 150010246 | The field "originNetContentNumber" can only be filled in for "Single set" and "Multi-piece set". |
| 150010247 | The field "originTotalNetContentNumber" can only be filled in for "Mixed set of different products" and "Mixed set of different specifications" |
| 150010248 | "skuClassification", "numberOfPieces","pieceUnitCode"and "individuallyPacked" are required, |
| 150010249 | "originNetContentNumber" field is required, please fill in and try again. |
| 150010252 | "originTotalNetContentNumber" field is required, please fill in and try again. |
| 150010250 | The field "mixedSetType" can only be filled in for "Mixed set of different products" and "Mixed set of different specifications". |
| 150010238 | The "productType" does not exist. Please check and try again. The current corresponding relationship is as follows: 1/null: NON_CUSTOM, 2: CUSTOM,3: MTO |
| 150011013 | Used-product shop do not support the listing of custom products. |
| 150011015 | Refurbished product shop do not support the listing of custom products. |
| 150011057 | "Made-to-order" feature is only available to select qualified sellers. To qualify, please contact your sales representitive. |
| 150011059 | "Made-to-order products" are mutually exclusive with other product types, such as used, custom, and refurbished products. |
| 150011067 | Invalid preparation time. This product only supports a preparation time range of {*}-{*}. |
| 150011027 | The product is missing tax code information. |
| 150011066 | The input {*} is incorrect, the aspect ratio is not {*}. |
| 150011065 | The input {*} is incorrect, the width and height are below {*}. |
| 150011064 | The input {*} is incorrect, image exceeds {*}. |
| 150010237 | The newly added specification information is missing in the goods properties. |
| 150011063 | Upload at most {*} images for Detail image |
| 150010236 | SKC must not exceed 25 |
| 150010235 | Please enter template name of size charts |
| 150010234 | The property value of the charger type is invalid. |
| 150010149 | The size specification entry is not in one group. |
| 150010142 | Template name of size charts duplicate |
| 150011060 | Video resolution should not below {*}p |
| 150011056 | Use {*} characters or fewer for product description |
| 150011055 | {*} is required fields. |
| 150011054 | The actual photo link for the SKU is missing. |
| 150011053 | The energy efficiency label is non-compliant. |
| 150011052 | An unknown certification was uploaded. |
| 150011051 | Exceeded the maximum number of uploaded files. |
| 150011050 | AVI storage check failed (domain name, tag, etc. validation failed). |
| 150011049 | The certification type is null.Please fill in again and submit. |
| 150011048 | Certification name or link has not been provided. |
| 150011047 | The values of {*} are mutually exclusive. Please fill in again and submit. |
| 150011046 | Certification details not filled in. |
| 150011045 | {*} are required fields. |
| 150011044 | Invalid input for {*}. Please update and resubmit. |
| 150011043 | {*}  is required. |
| 150011042 | {*} numeric value validation failed, such as missing value, non-numeric input, invalid decimal precision, or out-of-range value. |
| 150011041 | Exceeded the maximum number of {*} allowed. |
| 150011040 | "{*}" requires manual input and does not support direct selection. |
| 150011039 | "{*}" must be selected from predefined options and does not support custom input. |
| 150011038 | Duplicate attribute values were entered for a single SKU. |
| 150011037 | The SKU-level {*} was mistakenly assigned to the goods-level. |
| 150011036 | Multilingual support is not configured. Please check and configure. |
| 150011035 | Invalid date. Please check and enter correctly. |
| 150011034 | The value of {*} is empty. Please check and enter correctly. |
| 150011033 | The  {*}  format is not compliant. |
| 150011032 | The attribute ID of  {*}  is invalid. |
| 150011031 | The entered {*} is non-compliant. Please fill in again and submit. |
| 150011024 | The country/region of origin is filled in incorrectly, please select a valid value given by the system from the drop-down list. |
| 150011019 | The input {*}:{*} is incorrect, please modify it. |
| 150011018 | Price currency {*} can have at most {*} decimal points. |
| 150011010 | The keyword attribute [{*}] is required, please fill in accurately and appropriately |
| 150011006 | Shipping template binding error: {*} |
| 150011004 | Supports up to {*} images of product label for country/region of origin. |
| 150010224 | Unsupported value for Unit count. |
| 150010225 | For mixed sets, fields do not need to be filled in. |
| 150010226 | SKU type field is required, please fill in and try again. |
| 150010227 | The value should be between 0 and 10000. |
| 150010228 | Unsupported value for Unit type. |
| 150010223 | Second-hand stores can only list books and consumer electronics. |
| 150010230 | For used-product, "Condiiton" field is required. |
| 150010231 | The "Condition" field cannot be edited after the product is published. |
| 150010232 | The "Condition" field should not be filled in for this product. |
| 150010175 | The current product does not have permission to be linked to the selected shipping template. |
| 150011003 | Invalid Request Parameters [{*}] |
| 150010002 | System error, please try again later |
| 150010003 | Invalid Request Parameters |
| 150010005 | Try again later |
| 150010007 | Enter the correct property |
| 150010008 | Category not found |
| 150010009 | Enter the product name |
| 150010010 | Use 500 characters or fewer for product name |
| 150010011 | Only use letters, numbers and common punctuation for product name |
| 150010012 | Use 2000 characters or fewer for product description |
| 150010013 | Bullet point must not exceed 5 |
| 150010014 | Use 200 characters or fewer for bullet point |
| 150010015 | Value for apparel SKC is required |
| 150010016 | Add at least one SKU |
| 150010017 | Some SKU specifications are empty |
| 150010018 | Invalid handling time |
| 150010019 | Invalid fulfillment channel |
| 150010020 | Upload 3 to 10 images |
| 150010021 | Upload at most one video |
| 150010022 | Upload image URL link |
| 150010023 | Upload the video |
| 150010024 | Upload 3 to 10 images |
| 150010025 | Select the shipping template |
| 150010026 | Weight must be greater than 0 |
| 150010027 | Variant too long |
| 150010028 | Quantity must be between 0 and 1000000 |
| 150010029 | Incorrect price unit |
| 150010030 | Price input error |
| 150010031 | Shipping template not found |
| 150010032 | The size chart parameters are abnormal |
| 150010033 | Complete the size chart |
| 150010034 | Only use numbers for size chart |
| 150010035 | Size chart element value exceeds limit |
| 150010036 | Enter the US size |
| 150010038 | Size element is required |
| 150010039 | US size must be an integer or a decimal ending in 0.5 |
| 150010040 | Complete the required fields |
| 150010041 | List price must be greater than base price |
| 150010042 | Category unavailable |
| 150010043 | Chinese characters not allowed in text |
| 150010044 | Special characters not allowed in text |
| 150010045 | Incorrect text language |
| 150010046 | Invalid image format |
| 150010047 | Inappropriate content |
| 150010048 | Upload product carousel images |
| 150010049 | Upload SKU thumbnail image |
| 150010050 | Upload SKC carousel images |
| 150010051 | Invalid video |
| 150010052 | Rich text not supported |
| 150010053 | Upload 3 to 10 images |
| 150010054 | Invalid image |
| 150010055 | Incorrect image ratio |
| 150010056 | Image exceeds 3MB |
| 150010057 | Width below 1340px, height below 1785px |
| 150010058 | Width and Height below 800px |
| 150010059 | Video length exceeds 180 seconds |
| 150010060 | Video exceeds 100MB |
| 150010061 | Incorrect video ratio |
| 150010062 | Video resolution below 720P |
| 150010063 | Invalid video format |
| 150010065 | SKU must not exceed 500 |
| 150010066 | Published variants cannot be deleted |
| 150010067 | For non-apparel categories, only one SKC is allowed |
| 150010068 | Apparel category SKC's specId is invalid |
| 150010069 | SKC specification does not exist within the SKU specifications |
| 150010070 | Partial SKU specification information is incomplete |
| 150010071 | Parent specification ID retrieval failed |
| 150010072 | Number of specifications exceeds limit |
| 150010073 | SKU specification information is inconsisten |
| 150010074 | The number of SKUs and the product of specifications do not match |
| 150010075 | Within the same SKC, SKU specification value IDs are duplicated |
| 150010076 | SKU specification value ID is incorrect |
| 150010077 | SKU's parent specifications are inconsistent |
| 150010078 | Product must have at least one SKC |
| 150010079 | The sub-specification names for a single SKU are duplicated |
| 150010080 | If an SKC is in a listed status, then at least one SKU must be in a listed status |
| 150010081 | If goods are in a listed status, then at least one SKC must be in a listed status |
| 150010082 | Base price must be greater than 0 with valid currency |
| 150010083 | List price must be greater than base price |
| 150010084 | Invalid currency |
| 150010085 | List price for the same color must match |
| 150010086 | Base price for the same color must match |
| 150010087 | Invalid currency |
| 150010088 | Quantity must be between 0 and 1000000 |
| 150010089 | Published SKU cannot be deleted |
| 150010090 | SKU duplicated |
| 150010091 | Only use letters, numbers and common punctuation for contribution SKU |
| 150010092 | Invalid attribute |
| 150010093 | Invalid variant |
| 150010094 | Attribute or Specification Error |
| 150010095 | Variant cannot be edited |
| 150010096 | Refresh for latest version |
| 150010097 | Category attribute template is abnormal, publishing products is not allowed |
| 150010098 | Product deleted |
| 150010099 | Product blocked |
| 150010100 | Invalid shop |
| 150010101 | The product type does not support listing |
| 150010102 | The product type does not support modification |
| 150010103 | System error: Create a new product |
| 150010104 | Refresh for latest version |
| 150010105 | Mall information not found |
| 150010106 | Shop status abnormal |
| 150010107 | Shipping address abnormal |
| 150010108 | Complete the shop commission info |
| 150010109 | Complete the certification |
| 150010110 | Editing Disabled During Review |
| 150010111 | Refresh for latest version |
| 150010112 | Refresh for latest version |
| 150010113 | Apparel SKC attribute should be color type |
| 150010114 | SKU duplicated |
| 150010115 | Product processing, please try again later. |
| 150010116 | Complete the certification |
| 150010117 | Add the product guides or documents |
| 150010118 | Add the actual photo |
| 150010119 | Attribute input is non-compliant |
| 150010120 | Approved certification cannot be edited |
| 150010121 | Complete the compliance information |
| 150010122 | Product processing, please update the certifications later |
| 150010123 | SKU must not exceed 500 |
| 150010124 | The catId not a leaf category |
| 150010125 | Non-existent parentSpecId |
| 150010126 | Video exceeds 300MB |
| 150010127 | Video length exceeds 60 seconds |
| 150010128 | Incorrect image dimensions |
| 150010129 | Image exceeds 3MB |
| 150010130 | Please add at least two size charts. |
| 150010132 | Incorrect file format |
| 150010133 | File size is too large. |
| 150010134 | Complete the trademark or brand information |
| 150010135 | Re-check the trademark or brand information. |
| 150010139 | Detail images must not exceed 49 |
| 150010140 | For Books, only one SKU is allowed |
| 150010141 | Price input error |
| 150010162 | Invalid listPriceType |
| 150010163 | Please enter list price |
| 150010179 | The compliance information entered incorrectly. |
| 150010180 | The compliance information exceeds the maximum number of characters allowed. |
| 150010181 | Up to 10 compliance information can be entered. |
| 150010182 | The compliance information must contain numbers. |
| 150010183 | The compliance information cannot include Chinese characters. |
| 150010184 | The compliance information must include letters. |
| 150010185 | The compliance information should be entered in the local language. |
| 150010186 | The compliance information exceeds the maximum number of characters allowed. |
| 150010187 | The compliance information contains prohibited content. |
| 150010176 | Select the manufacturer. |
| 150010165 | Manufacturer is not available. |
| 150010166 | Failed to add the manufacturer. |
| 150010167 | Select the responsible person. |
| 150010168 | Responsible person is not available. |
| 150010169 | Failed to add the responsible person. |
| 150010200 | Please check and enter the correct compliance information. |
| 150010201 | Due to the low pricing assessment approval rate recently, we will limit the number of products that can be submitted each day. Today, you have reached the maximum limit. |
| 150010202 | Invalid unit for weight/Invalid unit for volume |
| 150010207 | Compliance information is incorrect |
| 150010208 | The relation id or type can not be empty |
| 150010209 | The relation type is not match |
| 150010210 | The property value id is not exist |
| 150010211 | The relation type is not allowed |
| 150010212 | The relation id is wrong |
| 150010213 | The goods property relation not exist |
| 150010218 | Variation information must not be duplicated or too similar across different SKUs |
| 150010219 | Bookstores can only list books |
| 150010220 | Book products cannot be published by non-book store |
| 150011001 | We have limited the number of products that can be listed per day to {*} to optimize product listing  efficiency. |
| 150011000 | Attribute or Specification Error: {*} |
| 150010217 | The shipping fee calculated by the shipping template bound to the item exceeds the upper limit. Please reduce the additional shipping fee amount of the shipping template |
| 150011023 | New version processing. |

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "skuList" : [ {
    "barCodeId" : "test",
    "images" : [ "test", "test" ],
    "barCodeType" : 1,
    "quantity" : 1,
    "specDetails" : [ {
      "parentSpecId" : 1,
      "specId" : 1,
      "specName" : "test"
    } ],
    "externalSkuId" : "test",
    "price" : {
      "listPrice" : {
        "amount" : "test",
        "currency" : "test"
      },
      "basePrice" : {
        "amount" : "test",
        "currency" : "test"
      }
    },
    "packageInfo" : {
      "length" : "test",
      "width" : "test",
      "weight" : "test",
      "height" : "test"
    },
    "referenceLink" : "test"
  } ],
  "goodsServicePromise" : {
    "costTemplateId" : "test",
    "fulfillmentType" : 1,
    "shipmentLimitDay" : 1
  },
  "sign" : "test",
  "goodsSize" : {
    "goodsSizeImage" : [ "test", "test" ],
    "groupId" : 1
  },
  "language" : "test",
  "goodsOriginInfo" : {
    "originRegion2" : "test",
    "originRegion1" : "test"
  },
  "type" : "test",
  "version" : "test",
  "goodsBasic" : {
    "catId" : 1,
    "itemTaxCode" : "test",
    "bulletPoints" : [ "test", "test" ],
    "externalGoodsId" : "test",
    "goodsName" : "test",
    "brand" : {
      "trademarkId" : 1,
      "noTrademark" : true
    },
    "secondHand" : {
      "businessScope" : 1,
      "level" : 1,
      "insName" : "test",
      "grade" : "test"
    },
    "goodsGallery" : {
      "detailVideoId" : "test",
      "goodsCarouselImage" : [ "test", "test" ],
      "carouselVideoId" : "test",
      "detailImage" : [ "test", "test" ]
    },
    "productType" : 1,
    "goodsDesc" : "test"
  },
  "access_token" : "test",
  "app_key" : "test",
  "goodsProperty" : [ {
    "vid" : 1,
    "numberInputValue" : "test",
    "value" : "test",
    "refPid" : 1,
    "valueUnitId" : 1
  } ],
  "data_type" : "test",
  "timestamp" : "test"
}'
```

## Response Example

```json
{
  "result" : {
    "goodsId" : 1,
    "productType" : 1,
    "skuInfoList" : [ {
      "specList" : [ {
        "specName" : "test",
        "specId" : 1,
        "parentSpecId" : 1
      } ],
      "skuId" : 1,
      "outSkuSn" : "test"
    } ],
    "warnings" : [ {
      "message" : "test"
    } ]
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```