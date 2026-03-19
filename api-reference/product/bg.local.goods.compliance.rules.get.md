# bg.local.goods.compliance.rules.get

**Query Mandatory Qualification Information**

Query Mandatory Qualification Information

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
| catId | 2 | No |  |  |
| normalPropertyList | 8 | No |  |  |
| governPropertyList | 8 | No |  |  |
| repInfoList | 8 | No |  |  |

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
| 150010002 | System error, please try again later |
| 150010003 | Invalid Request Parameters |
| 150010005 | Try again later |
| 150010124 | The catId not a leaf category |

## Request Example

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "goodsId" : 1,
  "sign" : "test",
  "language" : "test",
  "type" : "test",
  "version" : "test",
  "access_token" : "test",
  "catId" : 1,
  "governPropertyList" : [ {
    "vid" : 1,
    "pid" : 1,
    "value" : "test",
    "refPid" : 1
  } ],
  "app_key" : "test",
  "data_type" : "test",
  "repInfoList" : [ {
    "complianceRepType" : 1,
    "repIdList" : [ 1, 1 ]
  } ],
  "normalPropertyList" : [ {
    "vid" : 1,
    "pid" : 1,
    "value" : "test",
    "refPid" : 1
  } ],
  "timestamp" : "test"
}'
```

## Response Example

```json
{
  "result" : {
    "checkInfoList" : [ {
      "checkType" : 1,
      "exampleDesc" : "test",
      "checkFailReason" : "test",
      "checkResultDesc" : "test",
      "examplePicList" : [ "test", "test" ],
      "checkShowName" : "test",
      "checkStyle" : 1,
      "checkName" : "test",
      "checkFailCode" : 1,
      "checkResult" : 1,
      "complianceType" : 1,
      "guideFileLanguageList" : [ "test", "test" ]
    } ],
    "goodsCertList" : [ {
      "isRequired" : true,
      "certType" : 1,
      "certName" : "test",
      "matchType" : 1,
      "uploadStatus" : 1,
      "strongCheckItems" : {
        "$key" : "test",
        "$value" : [ 1, 1 ]
      },
      "uploadStatusLanguageMap" : {
        "$key" : "test",
        "$value" : 1
      },
      "goodsCertNeedUploadItemList" : [ {
        "showStrongCheckItems" : true,
        "needChooseCheckItems" : true,
        "errorTip" : "test",
        "uploadExample" : {
          "uploadExamplePicUrl" : [ "test", "test" ],
          "uploadRequire" : "test"
        },
        "docMandatoryField" : {
          "$key" : "test",
          "$value" : [ "test", "test" ]
        },
        "alias" : "test",
        "rejectReasonsByLanguage" : {
          "$key" : "test",
          "$value" : [ "test", "test" ]
        },
        "checkItems" : [ {
          "aliasName" : "test",
          "refPid" : 1,
          "refValues" : [ {
            "vid" : 1,
            "name" : "test",
            "remark" : "test"
          } ]
        } ],
        "supportLanguages" : [ {
          "languageCode" : "test",
          "languageName" : "test"
        } ],
        "contentType" : 1,
        "rejectReasons" : [ "test", "test" ]
      } ]
    } ],
    "actualPhotoRequirement" : [ {
      "maxPhotoSize" : 1,
      "position" : 1,
      "photoRequirementList" : [ {
        "exampleDesc" : "test",
        "examplePicList" : [ "test", "test" ],
        "requirement" : "test"
      } ]
    } ],
    "mustHaveActualPhoto" : true
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```