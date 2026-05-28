# Governance Attribute Guide V2.0

API Interfaces:

- 

temu.local.goods.v2.add

- 

temu.local.goods.compliance.v2.edit

[****](https://partner-eu.temu.com/documentation?menu_code=7289390cfd724be4a196f11ebe45a896&sub_menu_code=a34c866fee414d3d9894be754f40f2cc)

****

****

````````````

``

| Properties | How to fill in | Precautions |
|---|---|---|
| governProperty | User inputs & Retrieve from other APIs | -When publishing a product, it is not mandatory. Merchants need to supplement it completely before selling, otherwise the sale will be restricted-get from bg.local.goods.compliance.extra.template.getAccording to this interface, obtain the qualification rules that need to be uploaded [isRequired=true]. When calling this interface, you need to pass in the product category and attributes(goodsProperty). Different attribute information for the same category will affect the qualification requirements-The entry rules here are similar to the normal attributes of the product, and it is important to pay attention to the type of ControlType & parentVidList , which can affect different entry methods. parentPid and parentVidList determine that the current attribute refPid will be triggered when its parent attribute (parentPid) has one of the specified values (parentVidList) selected. Therefore, the parent attribute must also be included as a separate governance attribute in governProperty.*parentPid = null/0 indicates that the current governance attribute does not have a parent attribute. |

****

![image](https://bstatic.kwcdn.com/open-outer/21137b27f2e/1443e796538b83a11664abce9e679f69)

![image](https://bstatic.kwcdn.com/open-outer/21137b27f2e/7f82053c1bcc3fbc23e6b953a55bb316)

![image](https://bstatic.kwcdn.com/open-outer/21137b27f2e/1915e1295cbb77616e9375d39c9cf45e)

![image](https://bstatic.kwcdn.com/open-outer/21137b27f2e/777f300bb24f68f585c9f9dd5af9a2e6)

![image](https://bstatic.kwcdn.com/open-outer/21137b27f2e/5eef929992a00a4d463b002a758ecc64)

![image](https://bstatic.kwcdn.com/open-outer/21137b27f2e/7d7c248d22d4d22df41ff4296e87da6e)

![image](https://bstatic.kwcdn.com/open-outer/21137b27f2e/38134b84a0756cb9c4c9878b17081f76)

[](https://pfs-eu.file.temu.com/display-e/Mjp5NvnkK0VWUkBLUvujduVirLl-I2gs0w7YTVd6tUezMCx9ue016VHWs2sCVptNBW4ye1q3t-PPSBBUNdeZxCFqvSXE7QcTzAUahH-bqQnpdA0dqbZ2QT7ij6Us0K-u18Bcm76xyair0hFM6P7kLdFP?sign=q-sign-algorithm%3Dsha1%26q-ak%3D1GVq67ME6zW9gizj1v59fbzoduABkN5o%26q-sign-time%3D1779719528%3B1779723128%26q-key-time%3D1779719528%3B1779723128%26q-header-list%3D%26q-url-param-list%3D%26q-signature%3D65ac977d6c5663a6e6e35018f4681d66d9da1e91)

![image](https://bstatic.kwcdn.com/open-outer/21137b27f2e/2aa0fc3c8f8df80fb7bfdbec6fd41989)

| controlType | Description | Paramters | UI Reference | Query "bg.local.goods.compliance.extra.template.get" |
|---|---|---|---|---|
| "controlType": 5 | 5 - SINGLE_YMD_DATE | {  "templateId": 1038,  "refPid": 1100101197,  "value": "2026-05-18"} |  | {        "controlType": 5,        "propertyName": "Testing Testing Testing",         ......         "refPid": 1100101197      }, |
| "controlType": 6 | 6 - MULTIPLE_YMD_DATE | {  "templateId": 1038,  "refPid": 1100101198,  "value": "2025-05-18,2026-05-19"} |  | {        ......        "controlType": 6,        "propertyName": "testrefpid0525",        ......        "refPid": 1100101198      } |
| "controlType": 1 | 1 - CHOOSE | {  "templateId": 1038,  "refPid": 1100100550,  "vid": 1000300943}, |  | {        "parentPid": 0,        "excludeVidMap": {          "1000300943": [            1000332743          ]        },        "valuePrecision": 0,        "selectNum": 2,        "controlType": 1,        "propertyName": "Testing Testing Testing",        ......        "propertyValueList": [          {            "vid": 1000300943,            "valueName": "testvidm",            "parentVidList": []          },          {            "vid": 1000332743,            "valueName": "performance-account-health.bb_epr_doc_tip_weee",            "parentVidList": []          },          {            "vid": 1000434243,            "valueName": "Testing Testing Testing",            "parentVidList": []          }        ],        "refPid": 1100100550      }, |
| "controlType": 0 | 0 - INPUT | {  "templateId": 1038,  "refPid": 1100100578,  "value": "10"} |  | {        "max": 10,        "parentPid": 0,        "parentVidList": [],        "excludeVidMap": {},        "inputTitle": null,        "valuePrecision": 2,        "unit": null,        "selectNum": null,        "inputNum": null,        "min": 4,        "controlType": 0,        "propertyName": "testrefpid3",        "propertyDesc": null,        "inputType": 1,        "propertyValueList": [],        "refPid": 1100100578      }, |
| "controlType": 17 | 17 - MULTIPLE_LINES_INPUT | {        "templateId": 51,        "refPid": 1100100115,        "value": "aa"      },      {        "templateId": 51,        "refPid": 1100100115,        "value": "bb"      } |  | {        "max": null,        "parentPid": 0,        "parentVidList": [],        "excludeVidMap": {},        "inputTitle": null,        "valuePrecision": 0,        "unit": null,        "selectNum": null,        "inputNum": 50,        "min": null,        "controlType": 17,        "propertyName": "Product Identification",        "propertyDesc": null,        "inputType": 0,        "propertyValueList": [],        "refPid": 1100100115      }    ]  }, |
| "controlType": 3 | INPUT_CHOOSE | {        "templateId": 36,        "refPid": 1000100110,        "value": "aaaa"      }or    {        "templateId": 36,        "refPid": 1000100110,        "vid": 1000131288      } |  | {        "max": null,        "parentPid": 0,        "parentVidList": [],        "excludeVidMap": {},        "inputTitle": null,        "valuePrecision": 0,        "unit": null,        "selectNum": 1,        "inputNum": 1000,        "min": null,        "controlType": 3,        "propertyName": "Warning or safety information（supplement）",        "propertyDesc": null,        "inputType": 0,        "propertyValueList": [          {            "vid": 1000131288,            "valueName": "Information Not Applicable",            "parentVidList": []          },          {            "vid": 1000131289,            "valueName": "View Product Details Page",            "parentVidList": []          }        ],        "refPid": 1000100110      }    ]  }, |
| "controlType": 18 | 18 - DUAL_VALUE_RATIO | {        "templateId": 210,        "refPid": 1100100148,        "vid": 1000151543,        "value": "Hair dye",        "inputValue": "999"      },      {        "templateId": 210,        "refPid": 1100100148,        "vid": 1000151643,        "value": "Oxidants",        "inputValue": "11"      } |  | {        "max": 100000,        "parentPid": 1100100151,        "parentVidList": [          1000152143,          1000152543,          1000152443,          1000152343,          1000152144,          1000152243        ],        "excludeVidMap": {},        "inputTitle": null,        "valuePrecision": 2,        "unit": null,        "selectNum": null,        "inputNum": null,        "min": 0.01,        "controlType": 18,        "propertyName": "Hair dye mixing ratio (hair dye: oxidizing agent)",        "propertyDesc": null,        "inputType": 1,        "propertyValueList": [          {            "vid": 1000151543,            "valueName": "Hair dye",            "parentVidList": [              1000152143,              1000152543,              1000152443,              1000152343,              1000152144,              1000152243            ]          },          {            "vid": 1000151643,            "valueName": "Oxidants",            "parentVidList": [              1000152143,              1000152543,              1000152443,              1000152343,              1000152144,              1000152243            ]          } |
| "controlType": 20 | 20 - UPLOAD_IMAGE | {      "templateId": 1033,      "refPid": 1100100532,      "value": "https://pfs-eu.file.temu.com/display-e/Mjp5NvnkK0VWUkBLUvujduVirLl-I2gs0w7YTVd6tUezMCx9ue016VHWs2sCVptNBW4ye1q3t-PPSBBUNdeZxCFqvSXE7QcTzAUahH-bqQnpdA0dqbZ2QT7ij6Us0K-u18Bcm76xyair0hFM6P7kLdFP?sign=q-sign-algorithm%3Dsha1%26q-ak%3D1GVq67ME6zW9gizj1v59fbzoduABkN5o%26q-sign-time%3D1779719528%3B1779723128%26q-key-time%3D1779719528%3B1779723128%26q-header-list%3D%26q-url-param-list%3D%26q-signature%3D65ac977d6c5663a6e6e35018f4681d66d9da1e91"    } |  | {            "controlType": 20,            "excludeVidMap": {},            "inputNum": null,            "inputTitle": null,            "inputType": 6,            "max": 1,            "min": 1,            "parentPid": 0,            "parentVidList": [],            "propertyDesc": null,            "propertyName": "Calculation Grid",            "propertyValueList": [],            "refPid": 1100100532,            "selectNum": null,            "unit": null,            "valuePrecision": 0          }, |
