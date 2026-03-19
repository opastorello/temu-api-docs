# bg.local.compliance.goods.list.query

**Product compliance list query**

Product management attribute list query

**Method:** POST  
**URL:** https://openapi-b-global.temu.com/openapi/router

---

## Common Parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| type | STRING | Yes | API name,eg:bg.* |
| app_key | STRING | Yes |  |
| access_token | STRING | Yes | A secure token for access control. |
| sign | STRING | Yes |  |
| timestamp | STRING | Yes | The timestamp is in UNIX time format (seconds), with a length of 10 digits, and should be within a range of 300 seconds before the current time to 300 seconds after the current time. |
| data_type | STRING | No | The data format of the request response is fixed as JSON for optional parameters. |
| version | STRING | No | API version, defaults to V1, no need to pass this parameter if not required. |

## Request Parameters

| Parameter | Type | Required | Description | Example |
|---|---|---|---|---|
| pageNo | INTEGER | Yes | Page NO. | 1 |
| pageSize | INTEGER | Yes | Page Size, Default 25 | 1 |
| searchText | STRING | No | Support searching goodName/goodsId/skuId | test |
| statusList | INTEGER[] | No | Status, 1: not submitted, 2: To be reviewed, 3: Reviewing, 4: Action required, 5: Approved, 6: Rejected, 7: To be updated | [1, 1] |
| optionalConditionList | OBJECT[] | No | Compliance Information Filters |  |
|   complianceType | INTEGER | No | 1:Governance attributes,2:General Product Safety Regulation | 1 |
|   templateId | INTEGER | No | 1:Governance attributes,2:General Product Safety Regulation | 1 |
|   repType | INTEGER | No | 2: EU responsible person 3: manufacturer. required when complianceType is 2 | 1 |
|   actualPhotoCheckType | LONG | No | checkType of actual photo, required when complianceType is 3 | 1 |
|   certType | LONG | No | If complianceType is 4, enter the checkType of the qualification | 1 |

## Response Parameters

| Parameter | Type | Required | Description | Example |
|---|---|---|---|---|
| success | BOOLEAN | No | Success or not | True |
| errorCode | INTEGER | No | Error code | 1 |
| errorMsg | STRING | No | Error message | test |
| result | OBJECT | No | Result |  |
|   total | LONG | No | Total | 1 |
|   goodsList | OBJECT[] | No | Goods list |  |
|     goodsId | LONG | No | Goods Id | 1 |
|     goodsName | STRING | No | Goods Name | test |
|     thumbUrl | STRING | No | Goods Thumb Url | test |
|     outGoodsSn | STRING | No | External SKU Codes | test |
|     crtTime | LONG | No | Creation time, in seconds | 1 |
|     extraTemplateInfoList | OBJECT[] | No | Governance attribute template information list |  |
|       templateId | INTEGER | No | template ID of governance attributes. | 1 |
|       status | INTEGER | No | Status, 1: not submitted, 2: To be reviewed, 3: Reviewing, 4: Action required, 5: Approved, 6: Rejected, 7: To be updated | 1 |
|     gpsrInfoList | OBJECT[] | No | gpsr info list |  |
|       repType | INTEGER | Yes | 2: EU responsible person 3: manufacturer | 1 |
|       status | INTEGER | No | Status, 1: not submitted, 2: To be reviewed, 3: Reviewing, 4: Action required, 5: Approved, 6: Rejected, 7: To be updated | 1 |
|     repInfoList | OBJECT[] | No | Responsible Person Info |  |
|       repType | INTEGER | No | 4: A/S Responsible Person | 1 |
|       status | INTEGER | No | 1:not submitted,2:To be reviewed,3:Reviewing,4:Action required,5:Approved,6:Rejected,7:To be updated | 1 |
|     actualPhotoList | OBJECT[] | No | Actual photo list |  |
|       actualPhotoCheckType | LONG | Yes | checkType of actual photo | 1 |
|       status | INTEGER | No | 1:not submitted,2:To be reviewed,3:Reviewing,4:Action required,5:Approved,6:Rejected,7:To be updated | 1 |
|     certificateInfoList | OBJECT[] | No | certification list  |  |
|       certType | LONG | No | certType of this certificate | 1 |
|       status | INTEGER | No | 1:not submitted,2:To be reviewed,3:Reviewing,4:Action required,5:Approved,6:Rejected,7:To be updated | 1 |

## Error Codes

| Error Code | Message |
|---|---|
| 150010005 | Try again later |
| 150010003 | Invalid Request Parameters |
| 150010002 | System error, please try again later |

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "access_token" : "test",
  "searchText" : "test",
  "app_key" : "test",
  "statusList" : [ 1, 1 ],
  "optionalConditionList" : [ {
    "actualPhotoCheckType" : 1,
    "certType" : 1,
    "templateId" : 1,
    "repType" : 1,
    "complianceType" : 1
  } ],
  "pageNo" : 1,
  "sign" : "test",
  "data_type" : "test",
  "pageSize" : 1,
  "type" : "test",
  "version" : "test",
  "timestamp" : "test"
}'
```

## Response Example

```json
{
  "result" : {
    "goodsList" : [ {
      "gpsrInfoList" : [ {
        "repType" : 1,
        "status" : 1
      } ],
      "outGoodsSn" : "test",
      "goodsId" : 1,
      "crtTime" : 1,
      "extraTemplateInfoList" : [ {
        "templateId" : 1,
        "status" : 1
      } ],
      "repInfoList" : [ {
        "repType" : 1,
        "status" : 1
      } ],
      "thumbUrl" : "test",
      "actualPhotoList" : [ {
        "actualPhotoCheckType" : 1,
        "status" : 1
      } ],
      "goodsName" : "test",
      "certificateInfoList" : [ {
        "certType" : 1,
        "status" : 1
      } ]
    } ],
    "total" : 1
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```
