# bg.local.goods.compliance.edit

**Edit product qualification information**

Edit product qualification information

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
| goodsId | 2 | No |  |  |
| certificateInfo | 6 | No |  |  |
| actualPhoto | 6 | No |  |  |
| repInfo | 6 | No |  |  |
| extraTemplate | 6 | No |  |  |

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
| 150011114 | Image upload failed. Please try again later. |
| 150011113 | The product does not belong to the current store. Please check the product information before submitting. |
| 150011112 | The product does not exist. Please reselect and submit again. |
| 150011111 | Too many images for this category. Please remove extra photos and submit again. |
| 150011110 | Required photos are missing: both the product photo and the outer package photo are not uploaded. Please upload them and submit again. |
| 150011109 | Unsupported image format. Please upload images in JPG/JPEG/PNG format and try again. |
| 150011108 | The image file is too large. Please compress it and upload again. |
| 150011107 | Image resolution is too high. Please resize (reduce pixels) and upload again. |
| 150011106 | The image URL is unsupported or inaccessible. Please use a valid image link, or re-upload the image and submit again. |
| 150011105 | Some photo information is missing, so we can't submit for review. Please check the affected image and complete the required details (e.g., photo type/position), then submit again. |
| 150011104 | Incomplete product information. Unable to submit for review. Please reselect the product and try again. |
| 150011068 | The specified goodsId does not exist or does not belong to the current shop. |
| 150011062 | Compliance information cannot be edited while the SKU is under product review. |
| 150011061 | Compliance information cannot be edited while the SKU is under price review. |
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
| 150010131 | Pricing in progress |
| 150010207 | Compliance information is incorrect |
| 150011019 | The input {*}:{*} is incorrect, please modify it. |
| 150010165 | Manufacturer is not available. |
| 150010166 | Failed to add the manufacturer. |
| 150010167 | Select the responsible person. |
| 150010168 | Responsible person is not available. |
| 150010169 | Failed to add the responsible person. |

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "extraTemplate" : {
    "extraTemplateDetailList" : [ {
      "inputText" : {
        "$key" : "test",
        "$value" : {
          "name" : "test",
          "multiLineInputs" : [ {
            "name" : "test",
            "vid" : 1
          } ]
        }
      },
      "compliancePropertyList" : [ {
        "specIdList" : [ 1, 1 ],
        "inputTextList" : [ {
          "inputText" : {
            "$key" : "test",
            "$value" : {
              "name" : "test",
              "multiLineInputs" : [ {
                "name" : "test",
                "vid" : 1
              } ]
            }
          },
          "properties" : {
            "$key" : "test",
            "$value" : [ 1, 1 ]
          }
        } ]
      } ],
      "templateId" : 1,
      "properties" : {
        "$key" : "test",
        "$value" : [ 1, 1 ]
      }
    } ]
  },
  "goodsId" : 1,
  "repInfo" : {
    "repDetailList" : [ {
      "complianceRepType" : 1,
      "repIdList" : [ 1, 1 ]
    } ]
  },
  "sign" : "test",
  "language" : "test",
  "type" : "test",
  "certificateInfo" : {
    "certificateDetailList" : [ {
      "authCodes" : [ {
        "authCode" : "test"
      } ],
      "certType" : 1,
      "skip" : true,
      "certFiles" : [ {
        "fileName" : "test",
        "fileUrl" : "test",
        "language" : "test"
      } ],
      "inspectReportFiles" : [ {
        "fileName" : "test",
        "fileUrl" : "test",
        "language" : "test"
      } ],
      "authCode" : "test"
    } ]
  },
  "version" : "test",
  "access_token" : "test",
  "app_key" : "test",
  "data_type" : "test",
  "actualPhoto" : {
    "actualPhotoInfoList" : [ {
      "skuPhotoInfoList" : [ {
        "specIdList" : [ 1, 1 ],
        "imageList" : [ {
          "imageUrl" : "test"
        } ]
      } ],
      "sameSku" : true,
      "position" : 1
    } ],
    "skip" : true
  },
  "timestamp" : "test"
}'
```

## Response Example

```json
{
  "result" : {
    "goodsId" : 1
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```