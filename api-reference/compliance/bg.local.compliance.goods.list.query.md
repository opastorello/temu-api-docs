# bg.local.compliance.goods.list.query

**Product compliance list query**

Product management attribute list query

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
| pageNo | 1 | No |  |  |
| pageSize | 1 | No |  |  |
| searchText | 4 | No |  |  |
| statusList | 8 | No |  |  |
| optionalConditionList | 8 | No |  |  |

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