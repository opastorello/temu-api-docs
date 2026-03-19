# Make your Calls with Postman

Using Postman for quick API testing is a common practice, so we've specially updated this documentation to provide you with faster onboarding tools.

# 

Import From Postman

```
https://api.postman.com/collections/22962806-af9fef2f-a956-4667-a3a1-59c176d422d5?access_key=PMAT-01JPFB038YSF79SM1ZK3M8882F
```

# 

Set Variables 

Set all variables within the Postman project as common parameters, and ensure each API request in the project only includes the request body.

![image](https://bstatic.kwcdn.com/open-outer/20a3d4b51f/ef4fa1a92fee1a64d420b5642638b2a6.png)

# 

Set Pre-request

Use a pre-request script for signing.Here is an example code.

```
pm.variables.set("timestamp", Math.floor(Date.now() / 1000));  
const app_secret = pm.collectionVariables.get("app_secret");  
const app_key = pm.collectionVariables.get("app_key");  
const access_token = pm.collectionVariables.get("access_token");  
const data_type = pm.collectionVariables.get("data_type");  
  
let body = pm.request.body.raw;  
let request_params = JSON.parse(body);  
let additionalParams = {  
    app_key: app_key,  
    access_token: access_token,  
    data_type: data_type,  
    timestamp: pm.variables.get("timestamp")   
};  
Object.assign(request_params, additionalParams);   
console.log("request_params:", request_params);  
  
let keys = Object.keys(request_params).sort();  
let temp = [];  
keys.forEach(key => {  
    let value = JSON.stringify(request_params[key], null, 0)  
        .replace(/^"|"$/g, '');   
    temp.push(key + value);  
});  
  
let un_sign = app_secret + temp.join('') + app_secret;  
console.log("Un-Sign String:", un_sign);  
  
let sign = CryptoJS.MD5(un_sign).toString().toUpperCase();  
console.log("Signature:", sign);  
  
request_params["sign"] = sign;  
pm.request.body.update(JSON.stringify(request_params));  
console.log("Updated Body with Signature:", request_params);
```

# 

Request Parameter

Set request parameters for each API according to the API documentation.

![image](https://bstatic.kwcdn.com/open-outer/20a3d4b51f/b9b815909853c7093c963207319a4f04.png)

# 

Appendix

Here is a Postman collection that you can directly import into Postman for making API requests and debugging.

Collection 2.1

```
{  
 "info": {  
  "_postman_id": "af9fef2f-a956-4667-a3a1-59c176d422d5",  
  "name": "Temu Open APIs",  
  "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",  
  "_exporter_id": "22962806"  
 },  
 "item": [  
  {  
   "name": "Authorization",  
   "item": [  
    {  
     "name": "getAccessTokenInfo",  
     "request": {  
      "method": "POST",  
      "header": [  
       {  
        "key": "content-type",  
        "value": "application/json",  
        "type": "text"  
       }  
      ],  
      "body": {  
       "mode": "raw",  
       "raw": "{\n    \"type\": \"bg.open.accesstoken.info.get\"\n}",  
       "options": {  
        "raw": {  
         "language": "json"  
        }  
       }  
      },  
      "url": {  
       "raw": "{{us_endpoints}}",  
       "host": [  
        "{{us_endpoints}}"  
       ],  
       "query": [  
        {  
         "key": "type",  
         "value": "bg.order.list.get",  
         "disabled": true  
        },  
        {  
         "key": "app_key",  
         "value": "c9a17fa695a07be52f1836c3e2ec0b23",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713382474",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "2811DADD6B8C790638C96D4C9E4471E4",  
         "disabled": true  
        },  
        {  
         "key": "data_type",  
         "value": "JSON",  
         "disabled": true  
        },  
        {  
         "key": "access_token",  
         "value": "dfgu5e5yafdl4aervx58b3rih807wjbdsrugcnogo4z8cky7watooijq",  
         "disabled": true  
        },  
        {  
         "key": "app_secret",  
         "value": "c54100b5b15d69d5cf0db9e8a653333a60f73c23",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "B68B05A75DA27E2A3731B666965D3206",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713385043",  
         "disabled": true  
        }  
       ]  
      }  
     },  
     "response": []  
    },  
    {  
     "name": "createAccessTokenInfo",  
     "request": {  
      "method": "POST",  
      "header": [  
       {  
        "key": "content-type",  
        "value": "application/json",  
        "type": "text"  
       }  
      ],  
      "body": {  
       "mode": "raw",  
       "raw": "{\n    \"type\": \"bg.open.accesstoken.create\",\n    \"code\": \"\"\n}",  
       "options": {  
        "raw": {  
         "language": "json"  
        }  
       }  
      },  
      "url": {  
       "raw": "{{us_endpoints}}",  
       "host": [  
        "{{us_endpoints}}"  
       ],  
       "query": [  
        {  
         "key": "type",  
         "value": "bg.order.list.get",  
         "disabled": true  
        },  
        {  
         "key": "app_key",  
         "value": "c9a17fa695a07be52f1836c3e2ec0b23",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713382474",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "2811DADD6B8C790638C96D4C9E4471E4",  
         "disabled": true  
        },  
        {  
         "key": "data_type",  
         "value": "JSON",  
         "disabled": true  
        },  
        {  
         "key": "access_token",  
         "value": "dfgu5e5yafdl4aervx58b3rih807wjbdsrugcnogo4z8cky7watooijq",  
         "disabled": true  
        },  
        {  
         "key": "app_secret",  
         "value": "c54100b5b15d69d5cf0db9e8a653333a60f73c23",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "B68B05A75DA27E2A3731B666965D3206",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713385043",  
         "disabled": true  
        }  
       ]  
      }  
     },  
     "response": []  
    }  
   ]  
  },  
  {  
   "name": "Products Listing",  
   "item": [  
    {  
     "name": "getGoodsCategories",  
     "request": {  
      "method": "POST",  
      "header": [  
       {  
        "key": "content-type",  
        "value": "application/json",  
        "type": "text"  
       }  
      ],  
      "body": {  
       "mode": "raw",  
       "raw": "{\n    \"type\": \"bg.local.goods.cats.get\",\n    \"parentCatId\": 0\n}",  
       "options": {  
        "raw": {  
         "language": "json"  
        }  
       }  
      },  
      "url": {  
       "raw": "{{us_endpoints}}",  
       "host": [  
        "{{us_endpoints}}"  
       ],  
       "query": [  
        {  
         "key": "type",  
         "value": "bg.order.list.get",  
         "disabled": true  
        },  
        {  
         "key": "app_key",  
         "value": "c9a17fa695a07be52f1836c3e2ec0b23",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713382474",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "2811DADD6B8C790638C96D4C9E4471E4",  
         "disabled": true  
        },  
        {  
         "key": "data_type",  
         "value": "JSON",  
         "disabled": true  
        },  
        {  
         "key": "access_token",  
         "value": "dfgu5e5yafdl4aervx58b3rih807wjbdsrugcnogo4z8cky7watooijq",  
         "disabled": true  
        },  
        {  
         "key": "app_secret",  
         "value": "c54100b5b15d69d5cf0db9e8a653333a60f73c23",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "B68B05A75DA27E2A3731B666965D3206",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713385043",  
         "disabled": true  
        }  
       ]  
      }  
     },  
     "response": []  
    },  
    {  
     "name": "getGoodsTemplate",  
     "request": {  
      "method": "POST",  
      "header": [  
       {  
        "key": "content-type",  
        "value": "application/json",  
        "type": "text"  
       }  
      ],  
      "body": {  
       "mode": "raw",  
       "raw": "{\n    \"type\": \"bg.local.goods.template.get\",\n    \"catId\": 4\n}",  
       "options": {  
        "raw": {  
         "language": "json"  
        }  
       }  
      },  
      "url": {  
       "raw": "{{us_endpoints}}",  
       "host": [  
        "{{us_endpoints}}"  
       ],  
       "query": [  
        {  
         "key": "type",  
         "value": "bg.order.list.get",  
         "disabled": true  
        },  
        {  
         "key": "app_key",  
         "value": "c9a17fa695a07be52f1836c3e2ec0b23",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713382474",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "2811DADD6B8C790638C96D4C9E4471E4",  
         "disabled": true  
        },  
        {  
         "key": "data_type",  
         "value": "JSON",  
         "disabled": true  
        },  
        {  
         "key": "access_token",  
         "value": "dfgu5e5yafdl4aervx58b3rih807wjbdsrugcnogo4z8cky7watooijq",  
         "disabled": true  
        },  
        {  
         "key": "app_secret",  
         "value": "c54100b5b15d69d5cf0db9e8a653333a60f73c23",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "B68B05A75DA27E2A3731B666965D3206",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713385043",  
         "disabled": true  
        }  
       ]  
      }  
     },  
     "response": []  
    },  
    {  
     "name": "getAvailableBrandAndTrademark",  
     "request": {  
      "method": "POST",  
      "header": [  
       {  
        "key": "content-type",  
        "value": "application/json",  
        "type": "text"  
       }  
      ],  
      "body": {  
       "mode": "raw",  
       "raw": "{\n    \"type\": \"bg.local.goods.brand.trademark.get\",\n    \"brandId\": 4,\n    \"page\": 1,\n    \"size\": 25\n}",  
       "options": {  
        "raw": {  
         "language": "json"  
        }  
       }  
      },  
      "url": {  
       "raw": "{{us_endpoints}}",  
       "host": [  
        "{{us_endpoints}}"  
       ],  
       "query": [  
        {  
         "key": "type",  
         "value": "bg.order.list.get",  
         "disabled": true  
        },  
        {  
         "key": "app_key",  
         "value": "c9a17fa695a07be52f1836c3e2ec0b23",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713382474",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "2811DADD6B8C790638C96D4C9E4471E4",  
         "disabled": true  
        },  
        {  
         "key": "data_type",  
         "value": "JSON",  
         "disabled": true  
        },  
        {  
         "key": "access_token",  
         "value": "dfgu5e5yafdl4aervx58b3rih807wjbdsrugcnogo4z8cky7watooijq",  
         "disabled": true  
        },  
        {  
         "key": "app_secret",  
         "value": "c54100b5b15d69d5cf0db9e8a653333a60f73c23",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "B68B05A75DA27E2A3731B666965D3206",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713385043",  
         "disabled": true  
        }  
       ]  
      }  
     },  
     "response": []  
    },  
    {  
     "name": "getSignature",  
     "request": {  
      "method": "POST",  
      "header": [  
       {  
        "key": "content-type",  
        "value": "application/json",  
        "type": "text"  
       }  
      ],  
      "body": {  
       "mode": "raw",  
       "raw": "{\n    \"type\": \"bg.local.goods.brand.trademark.get\",\n    \"brandId\": 4,\n    \"page\": 1,\n    \"size\": 25\n}",  
       "options": {  
        "raw": {  
         "language": "json"  
        }  
       }  
      },  
      "url": {  
       "raw": "{{us_endpoints}}",  
       "host": [  
        "{{us_endpoints}}"  
       ],  
       "query": [  
        {  
         "key": "type",  
         "value": "bg.order.list.get",  
         "disabled": true  
        },  
        {  
         "key": "app_key",  
         "value": "c9a17fa695a07be52f1836c3e2ec0b23",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713382474",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "2811DADD6B8C790638C96D4C9E4471E4",  
         "disabled": true  
        },  
        {  
         "key": "data_type",  
         "value": "JSON",  
         "disabled": true  
        },  
        {  
         "key": "access_token",  
         "value": "dfgu5e5yafdl4aervx58b3rih807wjbdsrugcnogo4z8cky7watooijq",  
         "disabled": true  
        },  
        {  
         "key": "app_secret",  
         "value": "c54100b5b15d69d5cf0db9e8a653333a60f73c23",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "B68B05A75DA27E2A3731B666965D3206",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713385043",  
         "disabled": true  
        }  
       ]  
      }  
     },  
     "response": []  
    },  
    {  
     "name": "getShippingTemplates",  
     "request": {  
      "method": "POST",  
      "header": [  
       {  
        "key": "content-type",  
        "value": "application/json",  
        "type": "text"  
       }  
      ],  
      "body": {  
       "mode": "raw",  
       "raw": "{\n    \"type\": \"bg.freight.template.list.query\"\n}",  
       "options": {  
        "raw": {  
         "language": "json"  
        }  
       }  
      },  
      "url": {  
       "raw": "{{us_endpoints}}",  
       "host": [  
        "{{us_endpoints}}"  
       ],  
       "query": [  
        {  
         "key": "type",  
         "value": "bg.order.list.get",  
         "disabled": true  
        },  
        {  
         "key": "app_key",  
         "value": "c9a17fa695a07be52f1836c3e2ec0b23",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713382474",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "2811DADD6B8C790638C96D4C9E4471E4",  
         "disabled": true  
        },  
        {  
         "key": "data_type",  
         "value": "JSON",  
         "disabled": true  
        },  
        {  
         "key": "access_token",  
         "value": "dfgu5e5yafdl4aervx58b3rih807wjbdsrugcnogo4z8cky7watooijq",  
         "disabled": true  
        },  
        {  
         "key": "app_secret",  
         "value": "c54100b5b15d69d5cf0db9e8a653333a60f73c23",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "B68B05A75DA27E2A3731B666965D3206",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713385043",  
         "disabled": true  
        }  
       ]  
      }  
     },  
     "response": []  
    },  
    {  
     "name": "getSizeElements",  
     "request": {  
      "method": "POST",  
      "header": [  
       {  
        "key": "content-type",  
        "value": "application/json",  
        "type": "text"  
       }  
      ],  
      "body": {  
       "mode": "raw",  
       "raw": "{\n    \"type\": \"bg.local.goods.size.element.get\",\n    \"catId\": 4\n}",  
       "options": {  
        "raw": {  
         "language": "json"  
        }  
       }  
      },  
      "url": {  
       "raw": "{{us_endpoints}}",  
       "host": [  
        "{{us_endpoints}}"  
       ],  
       "query": [  
        {  
         "key": "type",  
         "value": "bg.order.list.get",  
         "disabled": true  
        },  
        {  
         "key": "app_key",  
         "value": "c9a17fa695a07be52f1836c3e2ec0b23",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713382474",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "2811DADD6B8C790638C96D4C9E4471E4",  
         "disabled": true  
        },  
        {  
         "key": "data_type",  
         "value": "JSON",  
         "disabled": true  
        },  
        {  
         "key": "access_token",  
         "value": "dfgu5e5yafdl4aervx58b3rih807wjbdsrugcnogo4z8cky7watooijq",  
         "disabled": true  
        },  
        {  
         "key": "app_secret",  
         "value": "c54100b5b15d69d5cf0db9e8a653333a60f73c23",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "B68B05A75DA27E2A3731B666965D3206",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713385043",  
         "disabled": true  
        }  
       ]  
      }  
     },  
     "response": []  
    },  
    {  
     "name": "uploadImageWithAutoTransformer",  
     "request": {  
      "method": "POST",  
      "header": [  
       {  
        "key": "content-type",  
        "value": "application/json",  
        "type": "text"  
       }  
      ],  
      "body": {  
       "mode": "raw",  
       "raw": "{\n    \"type\": \"bg.local.goods.image.upload\",\n    \"fileUrl\": \"https://m.media-amazon.com/images/I/61PYfD6yciL._AC_SX679_.jpg\",\n    \"formatConversionType\": 1,\n    \"scalingType\": 1,\n    \"compressionType\": 0\n}",  
       "options": {  
        "raw": {  
         "language": "json"  
        }  
       }  
      },  
      "url": {  
       "raw": "{{us_endpoints}}",  
       "host": [  
        "{{us_endpoints}}"  
       ],  
       "query": [  
        {  
         "key": "type",  
         "value": "bg.order.list.get",  
         "disabled": true  
        },  
        {  
         "key": "app_key",  
         "value": "c9a17fa695a07be52f1836c3e2ec0b23",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713382474",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "2811DADD6B8C790638C96D4C9E4471E4",  
         "disabled": true  
        },  
        {  
         "key": "data_type",  
         "value": "JSON",  
         "disabled": true  
        },  
        {  
         "key": "access_token",  
         "value": "dfgu5e5yafdl4aervx58b3rih807wjbdsrugcnogo4z8cky7watooijq",  
         "disabled": true  
        },  
        {  
         "key": "app_secret",  
         "value": "c54100b5b15d69d5cf0db9e8a653333a60f73c23",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "B68B05A75DA27E2A3731B666965D3206",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713385043",  
         "disabled": true  
        }  
       ]  
      }  
     },  
     "response": []  
    },  
    {  
     "name": "createSpecId",  
     "request": {  
      "method": "POST",  
      "header": [  
       {  
        "key": "content-type",  
        "value": "application/json",  
        "type": "text"  
       }  
      ],  
      "body": {  
       "mode": "raw",  
       "raw": "{\n    \"type\": \"bg.local.goods.spec.id.get\",\n    \"catId\": 4,\n    \"parentSpecId\": 1,\n    \"childSpecName\": \"spec name\"\n}",  
       "options": {  
        "raw": {  
         "language": "json"  
        }  
       }  
      },  
      "url": {  
       "raw": "{{us_endpoints}}",  
       "host": [  
        "{{us_endpoints}}"  
       ],  
       "query": [  
        {  
         "key": "type",  
         "value": "bg.order.list.get",  
         "disabled": true  
        },  
        {  
         "key": "app_key",  
         "value": "c9a17fa695a07be52f1836c3e2ec0b23",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713382474",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "2811DADD6B8C790638C96D4C9E4471E4",  
         "disabled": true  
        },  
        {  
         "key": "data_type",  
         "value": "JSON",  
         "disabled": true  
        },  
        {  
         "key": "access_token",  
         "value": "dfgu5e5yafdl4aervx58b3rih807wjbdsrugcnogo4z8cky7watooijq",  
         "disabled": true  
        },  
        {  
         "key": "app_secret",  
         "value": "c54100b5b15d69d5cf0db9e8a653333a60f73c23",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "B68B05A75DA27E2A3731B666965D3206",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713385043",  
         "disabled": true  
        }  
       ]  
      }  
     },  
     "response": []  
    },  
    {  
     "name": "createGoods",  
     "request": {  
      "method": "POST",  
      "header": [  
       {  
        "key": "content-type",  
        "value": "application/json",  
        "type": "text"  
       }  
      ],  
      "body": {  
       "mode": "raw",  
       "raw": "{\n    \"type\": \"bg.local.goods.add\",\n    \"goodsBasic\": {\n        \"catId\": 31159,\n        \"goodsName\": \"Dewalt DWD210G 120V 10 Amp VSR Pistol Grip 1/2 in. Corded Drill\"\n    },\n    \"goodsProperty\": {\n        \"goodsProperties\": [\n            {\n                \"pid\": 13,\n                \"refPid\": 63,\n                \"specId\": 2001,\n                \"templatePid\": 1182811,\n                \"value\": \"White\",\n                \"vid\": 376\n            },\n            {\n                \"pid\": 14,\n                \"refPid\": 65,\n                \"specId\": 10002,\n                \"templatePid\": 1182812,\n                \"value\": \"XXS\",\n                \"vid\": 311\n            },\n            {\n                \"pid\": 21,\n                \"refPid\": 83,\n                \"templatePid\": 1182819,\n                \"value\": \"Fake Buttons\",\n                \"vid\": 549\n            },\n            {\n                \"pid\": 10,\n                \"refPid\": 26,\n                \"templatePid\": 1182820,\n                \"value\": \"Solid color\",\n                \"vid\": 215\n            },\n            {\n                \"pid\": 67,\n                \"refPid\": 115,\n                \"templatePid\": 1182821,\n                \"value\": \"Adult\",\n                \"vid\": 25920\n            },\n            {\n                \"pid\": 7,\n                \"refPid\": 24,\n                \"templatePid\": 1182822,\n                \"value\": \"Semi-Sheer\",\n                \"vid\": 209\n            },\n            {\n                \"pid\": 6,\n                \"refPid\": 22,\n                \"templatePid\": 1182823,\n                \"value\": \"Medium Stretch\",\n                \"vid\": 205\n            },\n            {\n                \"pid\": 5,\n                \"refPid\": 21,\n                \"templatePid\": 1182826,\n                \"value\": \"Off the Shoulder\",\n                \"vid\": 170\n            },\n            {\n                \"pid\": 23,\n                \"refPid\": 84,\n                \"templatePid\": 1182828,\n                \"value\": \"Shirting\",\n                \"vid\": 860\n            },\n            {\n                \"pid\": 24,\n                \"refPid\": 76,\n                \"templatePid\": 1182830,\n                \"value\": \"Fall\",\n                \"vid\": 639\n            },\n            {\n                \"pid\": 4,\n                \"refPid\": 20,\n                \"templatePid\": 1182831,\n                \"value\": \"Hand wash or professional dry clean\",\n                \"vid\": 165\n            },\n            {\n                \"pid\": 3,\n                \"refPid\": 19,\n                \"templatePid\": 1182833,\n                \"value\": \"Vintage\",\n                \"vid\": 136\n            },\n            {\n                \"pid\": 1,\n                \"refPid\": 12,\n                \"templatePid\": 1182837,\n                \"value\": \"Recycle Polyester\",\n                \"vid\": 1\n            },\n            {\n                \"pid\": 1437,\n                \"refPid\": 1919,\n                \"templatePid\": 1182839,\n                \"value\": \"No Printing\",\n                \"vid\": 36892\n            },\n            {\n                \"numberInputValue\": \"50\",\n                \"pid\": 2,\n                \"refPid\": 15,\n                \"templatePid\": 1182840,\n                \"value\": \"Nylon\",\n                \"valueUnitId\": 57,\n                \"vid\": 35385\n            },\n            {\n                \"numberInputValue\": \"50\",\n                \"pid\": 2,\n                \"refPid\": 15,\n                \"templatePid\": 1182840,\n                \"value\": \"Polyester\",\n                \"valueUnitId\": 57,\n                \"vid\": 35386\n            },\n            {\n                \"pid\": 1224,\n                \"refPid\": 1192,\n                \"templatePid\": 1182841,\n                \"value\": \"Woven\",\n                \"vid\": 29810\n            },\n            {\n                \"pid\": 2054,\n                \"refPid\": 6926,\n                \"templatePid\": 1292709,\n                \"value\": \"Smooth fabric\",\n                \"vid\": 161198\n            },\n            {\n                \"pid\": 2050,\n                \"refPid\": 6928,\n                \"templatePid\": 1295084,\n                \"value\": \"Smooth fabric\",\n                \"vid\": 161110\n            },\n            {\n                \"pid\": 2052,\n                \"refPid\": 6930,\n                \"templatePid\": 1296332,\n                \"value\": \"2539\",\n                \"valueUnitId\": 240,\n                \"vid\": 0\n            },\n            {\n                \"pid\": 2052,\n                \"refPid\": 6934,\n                \"templatePid\": 1299089,\n                \"value\": \"4396\",\n                \"valueUnitId\": 240,\n                \"vid\": 0\n            }\n        ]\n    },\n    \"goodsServicePromise\": {\n        \"costTemplateId\": \"LFT-1092101837701122414\",\n        \"fulfillmentType\": 1,\n        \"shipmentLimitDay\": 1\n    },\n    \"goodsSizeChartList\": {\n        \"goodsSizeChartList\": [\n            {\n                \"classId\": 5,\n                \"meta\": {\n                    \"elements\": [\n                        {\n                            \"id\": 10001,\n                            \"name\": \"Shoulder width\"\n                        },\n                        {\n                            \"id\": 10002,\n                            \"name\": \"Bust size\"\n                        },\n                        {\n                            \"id\": 10003,\n                            \"name\": \"Clothes length\"\n                        }\n                    ],\n                    \"groups\": [\n                        {\n                            \"id\": 1,\n                            \"name\": \"size\"\n                        },\n                        {\n                            \"id\": 6,\n                            \"name\": \"US\"\n                        }\n                    ]\n                },\n                \"records\": [\n                    {\n                        \"values\": [\n                            {\n                                \"id\": 1,\n                                \"value\": \"XXS\"\n                            },\n                            {\n                                \"id\": 6,\n                                \"value\": \"5\"\n                            },\n                            {\n                                \"id\": 10001,\n                                \"value\": \"10\"\n                            },\n                            {\n                                \"id\": 10002,\n                                \"value\": \"10\"\n                            },\n                            {\n                                \"id\": 10003,\n                                \"value\": \"10\"\n                            }\n                        ]\n                    }\n                ]\n            }\n        ]\n    },\n    \"skuList\": [\n        {\n            \"height\": \"1.0\",\n            \"images\": [\n                \"https://img.kwcdn.com/local-goods-image/20a3d467c2/7c0e96c4-707e-4c2a-a647-b870b69e2183.jpeg\"\n            ],\n            \"length\": \"1.0\",\n            \"price\": {\n                \"basePrice\": {\n                    \"amount\": \"1.99\",\n                    \"currency\": \"USD\"\n                }\n            },\n            \"quantity\": 0,\n            \"specIdList\": [\n                2001,\n                10002\n            ],\n            \"volumeUnit\": \"in\",\n            \"weight\": \"1.0\",\n            \"weightUnit\": \"lb\",\n            \"width\": \"1.0\"\n        }\n    ]\n}",  
       "options": {  
        "raw": {  
         "language": "json"  
        }  
       }  
      },  
      "url": {  
       "raw": "{{us_endpoints}}",  
       "host": [  
        "{{us_endpoints}}"  
       ],  
       "query": [  
        {  
         "key": "type",  
         "value": "bg.order.list.get",  
         "disabled": true  
        },  
        {  
         "key": "app_key",  
         "value": "c9a17fa695a07be52f1836c3e2ec0b23",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713382474",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "2811DADD6B8C790638C96D4C9E4471E4",  
         "disabled": true  
        },  
        {  
         "key": "data_type",  
         "value": "JSON",  
         "disabled": true  
        },  
        {  
         "key": "access_token",  
         "value": "dfgu5e5yafdl4aervx58b3rih807wjbdsrugcnogo4z8cky7watooijq",  
         "disabled": true  
        },  
        {  
         "key": "app_secret",  
         "value": "c54100b5b15d69d5cf0db9e8a653333a60f73c23",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "B68B05A75DA27E2A3731B666965D3206",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713385043",  
         "disabled": true  
        }  
       ]  
      }  
     },  
     "response": []  
    },  
    {  
     "name": "recommendCategories",  
     "request": {  
      "method": "POST",  
      "header": [  
       {  
        "key": "content-type",  
        "value": "application/json",  
        "type": "text"  
       }  
      ],  
      "body": {  
       "mode": "raw",  
       "raw": "{\n    \"type\": \"bg.local.goods.category.recommend\",\n    \"goodsName\": \"Dewalt DWD210G 120V 10 Amp VSR Pistol Grip 1/2 in. Corded Drill\"\n}",  
       "options": {  
        "raw": {  
         "language": "json"  
        }  
       }  
      },  
      "url": {  
       "raw": "{{us_endpoints}}",  
       "host": [  
        "{{us_endpoints}}"  
       ],  
       "query": [  
        {  
         "key": "type",  
         "value": "bg.order.list.get",  
         "disabled": true  
        },  
        {  
         "key": "app_key",  
         "value": "c9a17fa695a07be52f1836c3e2ec0b23",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713382474",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "2811DADD6B8C790638C96D4C9E4471E4",  
         "disabled": true  
        },  
        {  
         "key": "data_type",  
         "value": "JSON",  
         "disabled": true  
        },  
        {  
         "key": "access_token",  
         "value": "dfgu5e5yafdl4aervx58b3rih807wjbdsrugcnogo4z8cky7watooijq",  
         "disabled": true  
        },  
        {  
         "key": "app_secret",  
         "value": "c54100b5b15d69d5cf0db9e8a653333a60f73c23",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "B68B05A75DA27E2A3731B666965D3206",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713385043",  
         "disabled": true  
        }  
       ]  
      }  
     },  
     "response": []  
    },  
    {  
     "name": "recommendProperties",  
     "request": {  
      "method": "POST",  
      "header": [  
       {  
        "key": "content-type",  
        "value": "application/json",  
        "type": "text"  
       }  
      ],  
      "body": {  
       "mode": "raw",  
       "raw": "{\n    \"type\": \"bg.local.goods.property.get\",\n    \"catId\": 4,\n    \"goodsName\": \"Dewalt DWD210G 120V 10 Amp VSR Pistol Grip 1/2 in. Corded Drill\",\n    \"goodsPropList\": [\n        {\n            \"propName\": \"White\"\n        },\n        {\n            \"propName\": \"XXS\"\n        },\n        {\n            \"propName\": \"Fake Buttons\"\n        },\n        {\n            \"propName\": \"Solid color\"\n        }\n    ]\n}",  
       "options": {  
        "raw": {  
         "language": "json"  
        }  
       }  
      },  
      "url": {  
       "raw": "{{us_endpoints}}",  
       "host": [  
        "{{us_endpoints}}"  
       ],  
       "query": [  
        {  
         "key": "type",  
         "value": "bg.order.list.get",  
         "disabled": true  
        },  
        {  
         "key": "app_key",  
         "value": "c9a17fa695a07be52f1836c3e2ec0b23",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713382474",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "2811DADD6B8C790638C96D4C9E4471E4",  
         "disabled": true  
        },  
        {  
         "key": "data_type",  
         "value": "JSON",  
         "disabled": true  
        },  
        {  
         "key": "access_token",  
         "value": "dfgu5e5yafdl4aervx58b3rih807wjbdsrugcnogo4z8cky7watooijq",  
         "disabled": true  
        },  
        {  
         "key": "app_secret",  
         "value": "c54100b5b15d69d5cf0db9e8a653333a60f73c23",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "B68B05A75DA27E2A3731B666965D3206",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713385043",  
         "disabled": true  
        }  
       ]  
      }  
     },  
     "response": []  
    }  
   ]  
  },  
  {  
   "name": "Products Management",  
   "item": [  
    {  
     "name": "getGoodsList",  
     "request": {  
      "method": "POST",  
      "header": [  
       {  
        "key": "content-type",  
        "value": "application/json",  
        "type": "text"  
       }  
      ],  
      "body": {  
       "mode": "raw",  
       "raw": "{\n    \"type\": \"bg.local.goods.list.query\",\n    \"goodsStatusFilterType\": 1,\n    \"orderField\": \"outGoodsSn\",\n    \"orderType\": 1,\n    \"pageNo\": 1,\n    \"pageSize\": 25\n}",  
       "options": {  
        "raw": {  
         "language": "json"  
        }  
       }  
      },  
      "url": {  
       "raw": "{{us_endpoints}}",  
       "host": [  
        "{{us_endpoints}}"  
       ],  
       "query": [  
        {  
         "key": "type",  
         "value": "bg.order.list.get",  
         "disabled": true  
        },  
        {  
         "key": "app_key",  
         "value": "c9a17fa695a07be52f1836c3e2ec0b23",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713382474",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "2811DADD6B8C790638C96D4C9E4471E4",  
         "disabled": true  
        },  
        {  
         "key": "data_type",  
         "value": "JSON",  
         "disabled": true  
        },  
        {  
         "key": "access_token",  
         "value": "dfgu5e5yafdl4aervx58b3rih807wjbdsrugcnogo4z8cky7watooijq",  
         "disabled": true  
        },  
        {  
         "key": "app_secret",  
         "value": "c54100b5b15d69d5cf0db9e8a653333a60f73c23",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "B68B05A75DA27E2A3731B666965D3206",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713385043",  
         "disabled": true  
        }  
       ]  
      }  
     },  
     "response": []  
    },  
    {  
     "name": "getGoodsSkuList",  
     "request": {  
      "method": "POST",  
      "header": [  
       {  
        "key": "content-type",  
        "value": "application/json",  
        "type": "text"  
       }  
      ],  
      "body": {  
       "mode": "raw",  
       "raw": "{\n    \"type\": \"bg.local.goods.sku.list.query\",\n    \"skuStatusFilterType\": 2,\n    \"pageNo\": 1,\n    \"pageSize\": 25\n}",  
       "options": {  
        "raw": {  
         "language": "json"  
        }  
       }  
      },  
      "url": {  
       "raw": "{{us_endpoints}}",  
       "host": [  
        "{{us_endpoints}}"  
       ],  
       "query": [  
        {  
         "key": "type",  
         "value": "bg.order.list.get",  
         "disabled": true  
        },  
        {  
         "key": "app_key",  
         "value": "c9a17fa695a07be52f1836c3e2ec0b23",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713382474",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "2811DADD6B8C790638C96D4C9E4471E4",  
         "disabled": true  
        },  
        {  
         "key": "data_type",  
         "value": "JSON",  
         "disabled": true  
        },  
        {  
         "key": "access_token",  
         "value": "dfgu5e5yafdl4aervx58b3rih807wjbdsrugcnogo4z8cky7watooijq",  
         "disabled": true  
        },  
        {  
         "key": "app_secret",  
         "value": "c54100b5b15d69d5cf0db9e8a653333a60f73c23",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "B68B05A75DA27E2A3731B666965D3206",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713385043",  
         "disabled": true  
        }  
       ]  
      }  
     },  
     "response": []  
    },  
    {  
     "name": "getGoodsDetail",  
     "request": {  
      "method": "POST",  
      "header": [  
       {  
        "key": "content-type",  
        "value": "application/json",  
        "type": "text"  
       }  
      ],  
      "body": {  
       "mode": "raw",  
       "raw": "{\n    \"type\": \"bg.local.goods.detail.query\",\n    \"goodsId\": 602771461874681\n}",  
       "options": {  
        "raw": {  
         "language": "json"  
        }  
       }  
      },  
      "url": {  
       "raw": "{{us_endpoints}}",  
       "host": [  
        "{{us_endpoints}}"  
       ],  
       "query": [  
        {  
         "key": "type",  
         "value": "bg.order.list.get",  
         "disabled": true  
        },  
        {  
         "key": "app_key",  
         "value": "c9a17fa695a07be52f1836c3e2ec0b23",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713382474",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "2811DADD6B8C790638C96D4C9E4471E4",  
         "disabled": true  
        },  
        {  
         "key": "data_type",  
         "value": "JSON",  
         "disabled": true  
        },  
        {  
         "key": "access_token",  
         "value": "dfgu5e5yafdl4aervx58b3rih807wjbdsrugcnogo4z8cky7watooijq",  
         "disabled": true  
        },  
        {  
         "key": "app_secret",  
         "value": "c54100b5b15d69d5cf0db9e8a653333a60f73c23",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "B68B05A75DA27E2A3731B666965D3206",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713385043",  
         "disabled": true  
        }  
       ]  
      }  
     },  
     "response": []  
    },  
    {  
     "name": "updateGoodsInfo<Full>",  
     "request": {  
      "method": "POST",  
      "header": [  
       {  
        "key": "content-type",  
        "value": "application/json",  
        "type": "text"  
       }  
      ],  
      "body": {  
       "mode": "raw",  
       "raw": "{\n    \"type\": \"bg.local.goods.update\",\n    \"goodsId\": 602521816893354,\n    \"goodsBasic\": {\n        \"catId\": 31159,\n        \"goodsName\": \"Dewalt DWD210G 120V 10 Amp VSR Pistol Grip 1/2 in. Corded Drill\"\n    },\n    \"goodsProperty\": {\n        \"goodsProperties\": [\n            {\n                \"pid\": 13,\n                \"refPid\": 63,\n                \"specId\": 2001,\n                \"templatePid\": 1182811,\n                \"value\": \"White\",\n                \"vid\": 376\n            },\n            {\n                \"pid\": 14,\n                \"refPid\": 65,\n                \"specId\": 10002,\n                \"templatePid\": 1182812,\n                \"value\": \"XXS\",\n                \"vid\": 311\n            },\n            {\n                \"pid\": 21,\n                \"refPid\": 83,\n                \"templatePid\": 1182819,\n                \"value\": \"Fake Buttons\",\n                \"vid\": 549\n            },\n            {\n                \"pid\": 10,\n                \"refPid\": 26,\n                \"templatePid\": 1182820,\n                \"value\": \"Solid color\",\n                \"vid\": 215\n            },\n            {\n                \"pid\": 67,\n                \"refPid\": 115,\n                \"templatePid\": 1182821,\n                \"value\": \"Adult\",\n                \"vid\": 25920\n            },\n            {\n                \"pid\": 7,\n                \"refPid\": 24,\n                \"templatePid\": 1182822,\n                \"value\": \"Semi-Sheer\",\n                \"vid\": 209\n            },\n            {\n                \"pid\": 6,\n                \"refPid\": 22,\n                \"templatePid\": 1182823,\n                \"value\": \"Medium Stretch\",\n                \"vid\": 205\n            },\n            {\n                \"pid\": 5,\n                \"refPid\": 21,\n                \"templatePid\": 1182826,\n                \"value\": \"Off the Shoulder\",\n                \"vid\": 170\n            },\n            {\n                \"pid\": 23,\n                \"refPid\": 84,\n                \"templatePid\": 1182828,\n                \"value\": \"Shirting\",\n                \"vid\": 860\n            },\n            {\n                \"pid\": 24,\n                \"refPid\": 76,\n                \"templatePid\": 1182830,\n                \"value\": \"Fall\",\n                \"vid\": 639\n            },\n            {\n                \"pid\": 4,\n                \"refPid\": 20,\n                \"templatePid\": 1182831,\n                \"value\": \"Hand wash or professional dry clean\",\n                \"vid\": 165\n            },\n            {\n                \"pid\": 3,\n                \"refPid\": 19,\n                \"templatePid\": 1182833,\n                \"value\": \"Vintage\",\n                \"vid\": 136\n            },\n            {\n                \"pid\": 1,\n                \"refPid\": 12,\n                \"templatePid\": 1182837,\n                \"value\": \"Recycle Polyester\",\n                \"vid\": 1\n            },\n            {\n                \"pid\": 1437,\n                \"refPid\": 1919,\n                \"templatePid\": 1182839,\n                \"value\": \"No Printing\",\n                \"vid\": 36892\n            },\n            {\n                \"numberInputValue\": \"50\",\n                \"pid\": 2,\n                \"refPid\": 15,\n                \"templatePid\": 1182840,\n                \"value\": \"Nylon\",\n                \"valueUnitId\": 57,\n                \"vid\": 35385\n            },\n            {\n                \"numberInputValue\": \"50\",\n                \"pid\": 2,\n                \"refPid\": 15,\n                \"templatePid\": 1182840,\n                \"value\": \"Polyester\",\n                \"valueUnitId\": 57,\n                \"vid\": 35386\n            },\n            {\n                \"pid\": 1224,\n                \"refPid\": 1192,\n                \"templatePid\": 1182841,\n                \"value\": \"Woven\",\n                \"vid\": 29810\n            },\n            {\n                \"pid\": 2054,\n                \"refPid\": 6926,\n                \"templatePid\": 1292709,\n                \"value\": \"Smooth fabric\",\n                \"vid\": 161198\n            },\n            {\n                \"pid\": 2050,\n                \"refPid\": 6928,\n                \"templatePid\": 1295084,\n                \"value\": \"Smooth fabric\",\n                \"vid\": 161110\n            },\n            {\n                \"pid\": 2052,\n                \"refPid\": 6930,\n                \"templatePid\": 1296332,\n                \"value\": \"2539\",\n                \"valueUnitId\": 240,\n                \"vid\": 0\n            },\n            {\n                \"pid\": 2052,\n                \"refPid\": 6934,\n                \"templatePid\": 1299089,\n                \"value\": \"4396\",\n                \"valueUnitId\": 240,\n                \"vid\": 0\n            }\n        ]\n    },\n    \"goodsServicePromise\": {\n        \"costTemplateId\": \"LFT-1092101837701122414\",\n        \"fulfillmentType\": 1,\n        \"shipmentLimitDay\": 1\n    },\n    \"goodsSizeChartList\": {\n        \"goodsSizeChartList\": [\n            {\n                \"classId\": 5,\n                \"meta\": {\n                    \"elements\": [\n                        {\n                            \"id\": 10001,\n                            \"name\": \"Shoulder width\"\n                        },\n                        {\n                            \"id\": 10002,\n                            \"name\": \"Bust size\"\n                        },\n                        {\n                            \"id\": 10003,\n                            \"name\": \"Clothes length\"\n                        }\n                    ],\n                    \"groups\": [\n                        {\n                            \"id\": 1,\n                            \"name\": \"size\"\n                        },\n                        {\n                            \"id\": 6,\n                            \"name\": \"US\"\n                        }\n                    ]\n                },\n                \"records\": [\n                    {\n                        \"values\": [\n                            {\n                                \"id\": 1,\n                                \"value\": \"XXS\"\n                            },\n                            {\n                                \"id\": 6,\n                                \"value\": \"5\"\n                            },\n                            {\n                                \"id\": 10001,\n                                \"value\": \"10\"\n                            },\n                            {\n                                \"id\": 10002,\n                                \"value\": \"10\"\n                            },\n                            {\n                                \"id\": 10003,\n                                \"value\": \"10\"\n                            }\n                        ]\n                    }\n                ]\n            }\n        ]\n    },\n    \"skuList\": [\n        {\n            \"skuId\": 38914551223686,\n            \"height\": \"1.0\",\n            \"images\": [\n                \"https://img.kwcdn.com/local-goods-image/20a3d467c2/7c0e96c4-707e-4c2a-a647-b870b69e2183.jpeg\"\n            ],\n            \"length\": \"1.0\",\n            \"price\": {\n                \"basePrice\": {\n                    \"amount\": \"1.99\",\n                    \"currency\": \"USD\"\n                }\n            },\n            \"quantity\": 0,\n            \"specIdList\": [\n                2001,\n                10002\n            ],\n            \"volumeUnit\": \"in\",\n            \"weight\": \"1.0\",\n            \"weightUnit\": \"lb\",\n            \"width\": \"1.0\"\n        }\n    ]\n}",  
       "options": {  
        "raw": {  
         "language": "json"  
        }  
       }  
      },  
      "url": {  
       "raw": "{{us_endpoints}}",  
       "host": [  
        "{{us_endpoints}}"  
       ],  
       "query": [  
        {  
         "key": "type",  
         "value": "bg.order.list.get",  
         "disabled": true  
        },  
        {  
         "key": "app_key",  
         "value": "c9a17fa695a07be52f1836c3e2ec0b23",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713382474",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "2811DADD6B8C790638C96D4C9E4471E4",  
         "disabled": true  
        },  
        {  
         "key": "data_type",  
         "value": "JSON",  
         "disabled": true  
        },  
        {  
         "key": "access_token",  
         "value": "dfgu5e5yafdl4aervx58b3rih807wjbdsrugcnogo4z8cky7watooijq",  
         "disabled": true  
        },  
        {  
         "key": "app_secret",  
         "value": "c54100b5b15d69d5cf0db9e8a653333a60f73c23",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "B68B05A75DA27E2A3731B666965D3206",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713385043",  
         "disabled": true  
        }  
       ]  
      }  
     },  
     "response": []  
    },  
    {  
     "name": "updateGoodsInfo<Partial>",  
     "request": {  
      "method": "POST",  
      "header": [  
       {  
        "key": "content-type",  
        "value": "application/json",  
        "type": "text"  
       }  
      ],  
      "body": {  
       "mode": "raw",  
       "raw": "{\n    \"type\": \"bg.local.goods.partial.update\",\n    \"goodsId\": 603233170851842,\n    \"goodsOriginInfo\": {\n        \"agreeDefaultOriginRegion\": true,\n        \"originRegion1\": \"Mainland China\",\n        \"originRegion2\": \"Guangdong\"\n    }\n}",  
       "options": {  
        "raw": {  
         "language": "json"  
        }  
       }  
      },  
      "url": {  
       "raw": "{{us_endpoints}}",  
       "host": [  
        "{{us_endpoints}}"  
       ],  
       "query": [  
        {  
         "key": "type",  
         "value": "bg.order.list.get",  
         "disabled": true  
        },  
        {  
         "key": "app_key",  
         "value": "c9a17fa695a07be52f1836c3e2ec0b23",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713382474",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "2811DADD6B8C790638C96D4C9E4471E4",  
         "disabled": true  
        },  
        {  
         "key": "data_type",  
         "value": "JSON",  
         "disabled": true  
        },  
        {  
         "key": "access_token",  
         "value": "dfgu5e5yafdl4aervx58b3rih807wjbdsrugcnogo4z8cky7watooijq",  
         "disabled": true  
        },  
        {  
         "key": "app_secret",  
         "value": "c54100b5b15d69d5cf0db9e8a653333a60f73c23",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "B68B05A75DA27E2A3731B666965D3206",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713385043",  
         "disabled": true  
        }  
       ]  
      }  
     },  
     "response": []  
    },  
    {  
     "name": "getGoodsSaleStatus",  
     "request": {  
      "method": "POST",  
      "header": [  
       {  
        "key": "content-type",  
        "value": "application/json",  
        "type": "text"  
       }  
      ],  
      "body": {  
       "mode": "raw",  
       "raw": "{\n    \"type\": \"bg.local.goods.publish.status.get\",\n    \"goodsIdList\": [602771461874681]\n}",  
       "options": {  
        "raw": {  
         "language": "json"  
        }  
       }  
      },  
      "url": {  
       "raw": "{{us_endpoints}}",  
       "host": [  
        "{{us_endpoints}}"  
       ],  
       "query": [  
        {  
         "key": "type",  
         "value": "bg.order.list.get",  
         "disabled": true  
        },  
        {  
         "key": "app_key",  
         "value": "c9a17fa695a07be52f1836c3e2ec0b23",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713382474",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "2811DADD6B8C790638C96D4C9E4471E4",  
         "disabled": true  
        },  
        {  
         "key": "data_type",  
         "value": "JSON",  
         "disabled": true  
        },  
        {  
         "key": "access_token",  
         "value": "dfgu5e5yafdl4aervx58b3rih807wjbdsrugcnogo4z8cky7watooijq",  
         "disabled": true  
        },  
        {  
         "key": "app_secret",  
         "value": "c54100b5b15d69d5cf0db9e8a653333a60f73c23",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "B68B05A75DA27E2A3731B666965D3206",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713385043",  
         "disabled": true  
        }  
       ]  
      }  
     },  
     "response": []  
    },  
    {  
     "name": "updateGoodsSaleStatus",  
     "request": {  
      "method": "POST",  
      "header": [  
       {  
        "key": "content-type",  
        "value": "application/json",  
        "type": "text"  
       }  
      ],  
      "body": {  
       "mode": "raw",  
       "raw": "{\n    \"type\": \"bg.local.goods.sale.status.set\",\n    \"goodsId\": 602771461874681,\n    \"onsale\": 1\n}   ",  
       "options": {  
        "raw": {  
         "language": "json"  
        }  
       }  
      },  
      "url": {  
       "raw": "{{us_endpoints}}",  
       "host": [  
        "{{us_endpoints}}"  
       ],  
       "query": [  
        {  
         "key": "type",  
         "value": "bg.order.list.get",  
         "disabled": true  
        },  
        {  
         "key": "app_key",  
         "value": "c9a17fa695a07be52f1836c3e2ec0b23",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713382474",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "2811DADD6B8C790638C96D4C9E4471E4",  
         "disabled": true  
        },  
        {  
         "key": "data_type",  
         "value": "JSON",  
         "disabled": true  
        },  
        {  
         "key": "access_token",  
         "value": "dfgu5e5yafdl4aervx58b3rih807wjbdsrugcnogo4z8cky7watooijq",  
         "disabled": true  
        },  
        {  
         "key": "app_secret",  
         "value": "c54100b5b15d69d5cf0db9e8a653333a60f73c23",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "B68B05A75DA27E2A3731B666965D3206",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713385043",  
         "disabled": true  
        }  
       ]  
      }  
     },  
     "response": []  
    }  
   ]  
  },  
  {  
   "name": "Inventory Management",  
   "item": [  
    {  
     "name": "updateGoodsStock",  
     "request": {  
      "method": "POST",  
      "header": [  
       {  
        "key": "content-type",  
        "value": "application/json",  
        "type": "text"  
       }  
      ],  
      "body": {  
       "mode": "raw",  
       "raw": "{\n    \"type\": \"bg.local.goods.stock.edit\",\n    \"requestUniqueKey\": \"123\",\n    \"goodsId\": 602238349110173,\n    \"skuStockTargetList\": [\n        {\n            \"skuId\": 43510166225830,\n            \"stockTarget\": 100\n        }\n    ],\n    \"skuStockChangeList\": [\n        {\n            \"skuId\": 43510166225830,\n            \"stockDiff\": 100\n        }\n    ]\n}",  
       "options": {  
        "raw": {  
         "language": "json"  
        }  
       }  
      },  
      "url": {  
       "raw": "{{us_endpoints}}",  
       "host": [  
        "{{us_endpoints}}"  
       ],  
       "query": [  
        {  
         "key": "type",  
         "value": "bg.order.list.get",  
         "disabled": true  
        },  
        {  
         "key": "app_key",  
         "value": "c9a17fa695a07be52f1836c3e2ec0b23",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713382474",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "2811DADD6B8C790638C96D4C9E4471E4",  
         "disabled": true  
        },  
        {  
         "key": "data_type",  
         "value": "JSON",  
         "disabled": true  
        },  
        {  
         "key": "access_token",  
         "value": "dfgu5e5yafdl4aervx58b3rih807wjbdsrugcnogo4z8cky7watooijq",  
         "disabled": true  
        },  
        {  
         "key": "app_secret",  
         "value": "c54100b5b15d69d5cf0db9e8a653333a60f73c23",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "B68B05A75DA27E2A3731B666965D3206",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713385043",  
         "disabled": true  
        }  
       ]  
      }  
     },  
     "response": []  
    }  
   ]  
  },  
  {  
   "name": "Pricing",  
   "item": [  
    {  
     "name": "getGoodsPriceList",  
     "request": {  
      "method": "POST",  
      "header": [  
       {  
        "key": "content-type",  
        "value": "application/json",  
        "type": "text"  
       }  
      ],  
      "body": {  
       "mode": "raw",  
       "raw": "{\n    \"type\": \"bg.local.goods.sku.list.price.query\",\n    \"querySupplierPriceBaseList\": [\n        {\n            \"goodsId\": 602521816893354,\n            \"skuIdList\": [38914551223686]\n        }\n    ]\n}",  
       "options": {  
        "raw": {  
         "language": "json"  
        }  
       }  
      },  
      "url": {  
       "raw": "{{us_endpoints}}",  
       "host": [  
        "{{us_endpoints}}"  
       ],  
       "query": [  
        {  
         "key": "type",  
         "value": "bg.order.list.get",  
         "disabled": true  
        },  
        {  
         "key": "app_key",  
         "value": "c9a17fa695a07be52f1836c3e2ec0b23",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713382474",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "2811DADD6B8C790638C96D4C9E4471E4",  
         "disabled": true  
        },  
        {  
         "key": "data_type",  
         "value": "JSON",  
         "disabled": true  
        },  
        {  
         "key": "access_token",  
         "value": "dfgu5e5yafdl4aervx58b3rih807wjbdsrugcnogo4z8cky7watooijq",  
         "disabled": true  
        },  
        {  
         "key": "app_secret",  
         "value": "c54100b5b15d69d5cf0db9e8a653333a60f73c23",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "B68B05A75DA27E2A3731B666965D3206",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713385043",  
         "disabled": true  
        }  
       ]  
      }  
     },  
     "response": []  
    },  
    {  
     "name": "updateGoodsPrice",  
     "request": {  
      "method": "POST",  
      "header": [  
       {  
        "key": "content-type",  
        "value": "application/json",  
        "type": "text"  
       }  
      ],  
      "body": {  
       "mode": "raw",  
       "raw": "{\n    \"type\": \"bg.local.goods.priceorder.change.sku.price\",\n    \"goodsId\": 1,\n    \"changeSkuPriceDTOList\": [\n        {\n            \"reason\": \"11\",\n            \"skuChangePriceBaseDTOList\": [\n                {\n                    \"newSupplierPrice\": {\n                        \"amount\": \"11\",\n                        \"currency\": \"USD\"\n                    },\n                    \"skuId\": 11\n                }\n            ]\n        }\n    ]\n}",  
       "options": {  
        "raw": {  
         "language": "json"  
        }  
       }  
      },  
      "url": {  
       "raw": "{{us_endpoints}}",  
       "host": [  
        "{{us_endpoints}}"  
       ],  
       "query": [  
        {  
         "key": "type",  
         "value": "bg.order.list.get",  
         "disabled": true  
        },  
        {  
         "key": "app_key",  
         "value": "c9a17fa695a07be52f1836c3e2ec0b23",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713382474",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "2811DADD6B8C790638C96D4C9E4471E4",  
         "disabled": true  
        },  
        {  
         "key": "data_type",  
         "value": "JSON",  
         "disabled": true  
        },  
        {  
         "key": "access_token",  
         "value": "dfgu5e5yafdl4aervx58b3rih807wjbdsrugcnogo4z8cky7watooijq",  
         "disabled": true  
        },  
        {  
         "key": "app_secret",  
         "value": "c54100b5b15d69d5cf0db9e8a653333a60f73c23",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "B68B05A75DA27E2A3731B666965D3206",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713385043",  
         "disabled": true  
        }  
       ]  
      }  
     },  
     "response": []  
    },  
    {  
     "name": "getGoodsPriceOrder",  
     "request": {  
      "method": "POST",  
      "header": [  
       {  
        "key": "content-type",  
        "value": "application/json",  
        "type": "text"  
       }  
      ],  
      "body": {  
       "mode": "raw",  
       "raw": "{\n    \"type\": \"bg.local.goods.priceorder.query\",\n    \"page\": 1,\n    \"size\": 5\n}",  
       "options": {  
        "raw": {  
         "language": "json"  
        }  
       }  
      },  
      "url": {  
       "raw": "{{us_endpoints}}",  
       "host": [  
        "{{us_endpoints}}"  
       ],  
       "query": [  
        {  
         "key": "type",  
         "value": "bg.order.list.get",  
         "disabled": true  
        },  
        {  
         "key": "app_key",  
         "value": "c9a17fa695a07be52f1836c3e2ec0b23",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713382474",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "2811DADD6B8C790638C96D4C9E4471E4",  
         "disabled": true  
        },  
        {  
         "key": "data_type",  
         "value": "JSON",  
         "disabled": true  
        },  
        {  
         "key": "access_token",  
         "value": "dfgu5e5yafdl4aervx58b3rih807wjbdsrugcnogo4z8cky7watooijq",  
         "disabled": true  
        },  
        {  
         "key": "app_secret",  
         "value": "c54100b5b15d69d5cf0db9e8a653333a60f73c23",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "B68B05A75DA27E2A3731B666965D3206",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713385043",  
         "disabled": true  
        }  
       ]  
      }  
     },  
     "response": []  
    },  
    {  
     "name": "acceptGoodsPriceOrder",  
     "request": {  
      "method": "POST",  
      "header": [  
       {  
        "key": "content-type",  
        "value": "application/json",  
        "type": "text"  
       }  
      ],  
      "body": {  
       "mode": "raw",  
       "raw": "{\n    \"type\": \"bg.local.goods.priceorder.accept\",\n    \"priceOrderInfoList\": [\n        {\n            \"priceOrderId\": 710125012236476084,\n            \"goodsId\": 602771461874681,\n            \"priceCommitVersion\": 1\n        }\n    ]\n}",  
       "options": {  
        "raw": {  
         "language": "json"  
        }  
       }  
      },  
      "url": {  
       "raw": "{{us_endpoints}}",  
       "host": [  
        "{{us_endpoints}}"  
       ],  
       "query": [  
        {  
         "key": "type",  
         "value": "bg.order.list.get",  
         "disabled": true  
        },  
        {  
         "key": "app_key",  
         "value": "c9a17fa695a07be52f1836c3e2ec0b23",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713382474",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "2811DADD6B8C790638C96D4C9E4471E4",  
         "disabled": true  
        },  
        {  
         "key": "data_type",  
         "value": "JSON",  
         "disabled": true  
        },  
        {  
         "key": "access_token",  
         "value": "dfgu5e5yafdl4aervx58b3rih807wjbdsrugcnogo4z8cky7watooijq",  
         "disabled": true  
        },  
        {  
         "key": "app_secret",  
         "value": "c54100b5b15d69d5cf0db9e8a653333a60f73c23",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "B68B05A75DA27E2A3731B666965D3206",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713385043",  
         "disabled": true  
        }  
       ]  
      }  
     },  
     "response": []  
    },  
    {  
     "name": "negotiateGoodsPriceOrder",  
     "request": {  
      "method": "POST",  
      "header": [  
       {  
        "key": "content-type",  
        "value": "application/json",  
        "type": "text"  
       }  
      ],  
      "body": {  
       "mode": "raw",  
       "raw": "{\n    \"type\": \"bg.local.goods.priceorder.negotiate\",\n    \"priceOrderId\": 711240924547164,\n    \"goodsId\": 602667845790155,\n    \"priceCommitVersion\": 1,\n    \"priceCommitId\": 202096051,\n    \"negotiatedPriceSkuList\": [\n        {\n            \"reason\": \"1\",\n            \"skuId\": 37119254897789,\n            \"newSupplierPrice\": {\n                \"amount\": \"21\",\n                \"currency\": \"USD\"\n            }\n        }\n    ]\n}",  
       "options": {  
        "raw": {  
         "language": "json"  
        }  
       }  
      },  
      "url": {  
       "raw": "{{us_endpoints}}",  
       "host": [  
        "{{us_endpoints}}"  
       ],  
       "query": [  
        {  
         "key": "type",  
         "value": "bg.order.list.get",  
         "disabled": true  
        },  
        {  
         "key": "app_key",  
         "value": "c9a17fa695a07be52f1836c3e2ec0b23",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713382474",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "2811DADD6B8C790638C96D4C9E4471E4",  
         "disabled": true  
        },  
        {  
         "key": "data_type",  
         "value": "JSON",  
         "disabled": true  
        },  
        {  
         "key": "access_token",  
         "value": "dfgu5e5yafdl4aervx58b3rih807wjbdsrugcnogo4z8cky7watooijq",  
         "disabled": true  
        },  
        {  
         "key": "app_secret",  
         "value": "c54100b5b15d69d5cf0db9e8a653333a60f73c23",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "B68B05A75DA27E2A3731B666965D3206",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713385043",  
         "disabled": true  
        }  
       ]  
      }  
     },  
     "response": []  
    },  
    {  
     "name": "getOrderPrice",  
     "request": {  
      "method": "POST",  
      "header": [  
       {  
        "key": "content-type",  
        "value": "application/json",  
        "type": "text"  
       }  
      ],  
      "body": {  
       "mode": "raw",  
       "raw": "{\n    \"type\": \"bg.order.amount.query\",\n    \"parentOrderSn\": \"PO-211-06934735803430536\"\n}",  
       "options": {  
        "raw": {  
         "language": "json"  
        }  
       }  
      },  
      "url": {  
       "raw": "{{us_endpoints}}",  
       "host": [  
        "{{us_endpoints}}"  
       ],  
       "query": [  
        {  
         "key": "type",  
         "value": "bg.order.list.get",  
         "disabled": true  
        },  
        {  
         "key": "app_key",  
         "value": "c9a17fa695a07be52f1836c3e2ec0b23",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713382474",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "2811DADD6B8C790638C96D4C9E4471E4",  
         "disabled": true  
        },  
        {  
         "key": "data_type",  
         "value": "JSON",  
         "disabled": true  
        },  
        {  
         "key": "access_token",  
         "value": "dfgu5e5yafdl4aervx58b3rih807wjbdsrugcnogo4z8cky7watooijq",  
         "disabled": true  
        },  
        {  
         "key": "app_secret",  
         "value": "c54100b5b15d69d5cf0db9e8a653333a60f73c23",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "B68B05A75DA27E2A3731B666965D3206",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713385043",  
         "disabled": true  
        }  
       ]  
      }  
     },  
     "response": []  
    }  
   ]  
  },  
  {  
   "name": "Order Management",  
   "item": [  
    {  
     "name": "getOrderDetail",  
     "request": {  
      "method": "POST",  
      "header": [  
       {  
        "key": "content-type",  
        "value": "application/json",  
        "type": "text"  
       }  
      ],  
      "body": {  
       "mode": "raw",  
       "raw": "{\n    \"type\": \"bg.order.detail.get\",\n    \"parentOrderSn\": \"PO-211-06934735803430536\"\n}",  
       "options": {  
        "raw": {  
         "language": "json"  
        }  
       }  
      },  
      "url": {  
       "raw": "{{us_endpoints}}",  
       "host": [  
        "{{us_endpoints}}"  
       ],  
       "query": [  
        {  
         "key": "type",  
         "value": "bg.order.list.get",  
         "disabled": true  
        },  
        {  
         "key": "app_key",  
         "value": "c9a17fa695a07be52f1836c3e2ec0b23",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713382474",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "2811DADD6B8C790638C96D4C9E4471E4",  
         "disabled": true  
        },  
        {  
         "key": "data_type",  
         "value": "JSON",  
         "disabled": true  
        },  
        {  
         "key": "access_token",  
         "value": "dfgu5e5yafdl4aervx58b3rih807wjbdsrugcnogo4z8cky7watooijq",  
         "disabled": true  
        },  
        {  
         "key": "app_secret",  
         "value": "c54100b5b15d69d5cf0db9e8a653333a60f73c23",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "B68B05A75DA27E2A3731B666965D3206",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713385043",  
         "disabled": true  
        }  
       ]  
      }  
     },  
     "response": []  
    },  
    {  
     "name": "getOrderList",  
     "request": {  
      "method": "POST",  
      "header": [  
       {  
        "key": "content-type",  
        "value": "application/json",  
        "type": "text"  
       }  
      ],  
      "body": {  
       "mode": "raw",  
       "raw": "{\n    \"type\": \"bg.order.list.get\",\n    \"parentOrderStatus\": 0,\n    \"regionId\": 211,\n    \"pageNumber\": 1,\n    \"pageSize\": 1\n}",  
       "options": {  
        "raw": {  
         "language": "json"  
        }  
       }  
      },  
      "url": {  
       "raw": "{{us_endpoints}}",  
       "host": [  
        "{{us_endpoints}}"  
       ],  
       "query": [  
        {  
         "key": "type",  
         "value": "bg.order.list.get",  
         "disabled": true  
        },  
        {  
         "key": "app_key",  
         "value": "c9a17fa695a07be52f1836c3e2ec0b23",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713382474",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "2811DADD6B8C790638C96D4C9E4471E4",  
         "disabled": true  
        },  
        {  
         "key": "data_type",  
         "value": "JSON",  
         "disabled": true  
        },  
        {  
         "key": "access_token",  
         "value": "dfgu5e5yafdl4aervx58b3rih807wjbdsrugcnogo4z8cky7watooijq",  
         "disabled": true  
        },  
        {  
         "key": "app_secret",  
         "value": "c54100b5b15d69d5cf0db9e8a653333a60f73c23",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "B68B05A75DA27E2A3731B666965D3206",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713385043",  
         "disabled": true  
        }  
       ]  
      }  
     },  
     "response": []  
    },  
    {  
     "name": "getOrderShippingInfo",  
     "request": {  
      "method": "POST",  
      "header": [  
       {  
        "key": "content-type",  
        "value": "application/json",  
        "type": "text"  
       }  
      ],  
      "body": {  
       "mode": "raw",  
       "raw": "{\n    \"type\": \"bg.order.shippinginfo.get\",\n    \"parentOrderSn\": \"PO-211-07146026222631295\"\n}",  
       "options": {  
        "raw": {  
         "language": "json"  
        }  
       }  
      },  
      "url": {  
       "raw": "{{us_endpoints}}",  
       "host": [  
        "{{us_endpoints}}"  
       ],  
       "query": [  
        {  
         "key": "type",  
         "value": "bg.order.list.get",  
         "disabled": true  
        },  
        {  
         "key": "app_key",  
         "value": "c9a17fa695a07be52f1836c3e2ec0b23",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713382474",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "2811DADD6B8C790638C96D4C9E4471E4",  
         "disabled": true  
        },  
        {  
         "key": "data_type",  
         "value": "JSON",  
         "disabled": true  
        },  
        {  
         "key": "access_token",  
         "value": "dfgu5e5yafdl4aervx58b3rih807wjbdsrugcnogo4z8cky7watooijq",  
         "disabled": true  
        },  
        {  
         "key": "app_secret",  
         "value": "c54100b5b15d69d5cf0db9e8a653333a60f73c23",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "B68B05A75DA27E2A3731B666965D3206",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713385043",  
         "disabled": true  
        }  
       ]  
      }  
     },  
     "response": []  
    },  
    {  
     "name": "getOrderShippingCompanies",  
     "request": {  
      "method": "POST",  
      "header": [  
       {  
        "key": "content-type",  
        "value": "application/json",  
        "type": "text"  
       }  
      ],  
      "body": {  
       "mode": "raw",  
       "raw": "{\n    \"type\": \"bg.logistics.companies.get\",\n    \"regionId\": \"211\"\n}",  
       "options": {  
        "raw": {  
         "language": "json"  
        }  
       }  
      },  
      "url": {  
       "raw": "{{us_endpoints}}",  
       "host": [  
        "{{us_endpoints}}"  
       ],  
       "query": [  
        {  
         "key": "type",  
         "value": "bg.order.list.get",  
         "disabled": true  
        },  
        {  
         "key": "app_key",  
         "value": "c9a17fa695a07be52f1836c3e2ec0b23",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713382474",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "2811DADD6B8C790638C96D4C9E4471E4",  
         "disabled": true  
        },  
        {  
         "key": "data_type",  
         "value": "JSON",  
         "disabled": true  
        },  
        {  
         "key": "access_token",  
         "value": "dfgu5e5yafdl4aervx58b3rih807wjbdsrugcnogo4z8cky7watooijq",  
         "disabled": true  
        },  
        {  
         "key": "app_secret",  
         "value": "c54100b5b15d69d5cf0db9e8a653333a60f73c23",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "B68B05A75DA27E2A3731B666965D3206",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713385043",  
         "disabled": true  
        }  
       ]  
      }  
     },  
     "response": []  
    }  
   ]  
  },  
  {  
   "name": "Order Fulfillment",  
   "item": [  
    {  
     "name": "getOrderShipmentConfirm",  
     "request": {  
      "method": "POST",  
      "header": [  
       {  
        "key": "content-type",  
        "value": "application/json",  
        "type": "text"  
       }  
      ],  
      "body": {  
       "mode": "raw",  
       "raw": "{\n    \"type\": \"bg.logistics.shipment.confirm\",\n    \"sendRequestList\": [\n        {\n            \"carrierId\": 960246690,\n            \"orderSendInfoList\": [\n                {\n                    \"goodsId\": 601099512037184,\n                    \"orderSn\": \"211-00023968318071120\",\n                    \"parentOrderSn\": \"PO-211-00023989289591120\",\n                    \"quantity\": 1,\n                    \"skuId\": 47\n                }\n            ],\n            \"trackingNumber\": \"930000000\"\n        }\n    ],\n    \"sendType\": 0\n}",  
       "options": {  
        "raw": {  
         "language": "json"  
        }  
       }  
      },  
      "url": {  
       "raw": "{{us_endpoints}}",  
       "host": [  
        "{{us_endpoints}}"  
       ],  
       "query": [  
        {  
         "key": "type",  
         "value": "bg.order.list.get",  
         "disabled": true  
        },  
        {  
         "key": "app_key",  
         "value": "c9a17fa695a07be52f1836c3e2ec0b23",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713382474",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "2811DADD6B8C790638C96D4C9E4471E4",  
         "disabled": true  
        },  
        {  
         "key": "data_type",  
         "value": "JSON",  
         "disabled": true  
        },  
        {  
         "key": "access_token",  
         "value": "dfgu5e5yafdl4aervx58b3rih807wjbdsrugcnogo4z8cky7watooijq",  
         "disabled": true  
        },  
        {  
         "key": "app_secret",  
         "value": "c54100b5b15d69d5cf0db9e8a653333a60f73c23",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "B68B05A75DA27E2A3731B666965D3206",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713385043",  
         "disabled": true  
        }  
       ]  
      }  
     },  
     "response": []  
    },  
    {  
     "name": "getOrderShipmentInfo",  
     "request": {  
      "method": "POST",  
      "header": [  
       {  
        "key": "content-type",  
        "value": "application/json",  
        "type": "text"  
       }  
      ],  
      "body": {  
       "mode": "raw",  
       "raw": "{\n    \"type\": \"bg.logistics.shipment.get\",\n    \"parentOrderSn\": \"PO-211-00023989289591120\",\n    \"orderSn\": \"211-00023968318071120\"\n}",  
       "options": {  
        "raw": {  
         "language": "json"  
        }  
       }  
      },  
      "url": {  
       "raw": "{{us_endpoints}}",  
       "host": [  
        "{{us_endpoints}}"  
       ],  
       "query": [  
        {  
         "key": "type",  
         "value": "bg.order.list.get",  
         "disabled": true  
        },  
        {  
         "key": "app_key",  
         "value": "c9a17fa695a07be52f1836c3e2ec0b23",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713382474",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "2811DADD6B8C790638C96D4C9E4471E4",  
         "disabled": true  
        },  
        {  
         "key": "data_type",  
         "value": "JSON",  
         "disabled": true  
        },  
        {  
         "key": "access_token",  
         "value": "dfgu5e5yafdl4aervx58b3rih807wjbdsrugcnogo4z8cky7watooijq",  
         "disabled": true  
        },  
        {  
         "key": "app_secret",  
         "value": "c54100b5b15d69d5cf0db9e8a653333a60f73c23",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "B68B05A75DA27E2A3731B666965D3206",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713385043",  
         "disabled": true  
        }  
       ]  
      }  
     },  
     "response": []  
    },  
    {  
     "name": "updateOrderShipmentInfo",  
     "request": {  
      "method": "POST",  
      "header": [  
       {  
        "key": "content-type",  
        "value": "application/json",  
        "type": "text"  
       }  
      ],  
      "body": {  
       "mode": "raw",  
       "raw": "{\n    \"type\": \"bg.logistics.shipment.get\",\n    \"packageSn\": \"PK-00023989289591120\",\n    \"shipCompanyId\": \"89289591120\",\n    \"trackingNumber\": \"211-00023968318071120\"\n}",  
       "options": {  
        "raw": {  
         "language": "json"  
        }  
       }  
      },  
      "url": {  
       "raw": "{{us_endpoints}}",  
       "host": [  
        "{{us_endpoints}}"  
       ],  
       "query": [  
        {  
         "key": "type",  
         "value": "bg.order.list.get",  
         "disabled": true  
        },  
        {  
         "key": "app_key",  
         "value": "c9a17fa695a07be52f1836c3e2ec0b23",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713382474",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "2811DADD6B8C790638C96D4C9E4471E4",  
         "disabled": true  
        },  
        {  
         "key": "data_type",  
         "value": "JSON",  
         "disabled": true  
        },  
        {  
         "key": "access_token",  
         "value": "dfgu5e5yafdl4aervx58b3rih807wjbdsrugcnogo4z8cky7watooijq",  
         "disabled": true  
        },  
        {  
         "key": "app_secret",  
         "value": "c54100b5b15d69d5cf0db9e8a653333a60f73c23",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "B68B05A75DA27E2A3731B666965D3206",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713385043",  
         "disabled": true  
        }  
       ]  
      }  
     },  
     "response": []  
    }  
   ]  
  },  
  {  
   "name": "Refund And Return",  
   "item": [  
    {  
     "name": "getParentAftersaleOrderList",  
     "request": {  
      "method": "POST",  
      "header": [  
       {  
        "key": "content-type",  
        "value": "application/json",  
        "type": "text"  
       }  
      ],  
      "body": {  
       "mode": "raw",  
       "raw": "{\n    \"type\": \"bg.aftersales.parentaftersales.list.get\",\n    \"pageNo\": 1,\n    \"pageSize\": 10,\n    \"afterSalesStatusGroup\": 2\n}",  
       "options": {  
        "raw": {  
         "language": "json"  
        }  
       }  
      },  
      "url": {  
       "raw": "{{us_endpoints}}",  
       "host": [  
        "{{us_endpoints}}"  
       ],  
       "query": [  
        {  
         "key": "type",  
         "value": "bg.order.list.get",  
         "disabled": true  
        },  
        {  
         "key": "app_key",  
         "value": "c9a17fa695a07be52f1836c3e2ec0b23",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713382474",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "2811DADD6B8C790638C96D4C9E4471E4",  
         "disabled": true  
        },  
        {  
         "key": "data_type",  
         "value": "JSON",  
         "disabled": true  
        },  
        {  
         "key": "access_token",  
         "value": "dfgu5e5yafdl4aervx58b3rih807wjbdsrugcnogo4z8cky7watooijq",  
         "disabled": true  
        },  
        {  
         "key": "app_secret",  
         "value": "c54100b5b15d69d5cf0db9e8a653333a60f73c23",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "B68B05A75DA27E2A3731B666965D3206",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713385043",  
         "disabled": true  
        }  
       ]  
      }  
     },  
     "response": []  
    },  
    {  
     "name": "getAftersaleOrderList",  
     "request": {  
      "method": "POST",  
      "header": [  
       {  
        "key": "content-type",  
        "value": "application/json",  
        "type": "text"  
       }  
      ],  
      "body": {  
       "mode": "raw",  
       "raw": "{\n    \"type\": \"bg.aftersales.aftersales.list.get\",\n    \"pageNo\": 1,\n    \"pageSize\": 10,\n    \"parentAfterSalesSnList\": []\n}",  
       "options": {  
        "raw": {  
         "language": "json"  
        }  
       }  
      },  
      "url": {  
       "raw": "{{us_endpoints}}",  
       "host": [  
        "{{us_endpoints}}"  
       ],  
       "query": [  
        {  
         "key": "type",  
         "value": "bg.order.list.get",  
         "disabled": true  
        },  
        {  
         "key": "app_key",  
         "value": "c9a17fa695a07be52f1836c3e2ec0b23",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713382474",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "2811DADD6B8C790638C96D4C9E4471E4",  
         "disabled": true  
        },  
        {  
         "key": "data_type",  
         "value": "JSON",  
         "disabled": true  
        },  
        {  
         "key": "access_token",  
         "value": "dfgu5e5yafdl4aervx58b3rih807wjbdsrugcnogo4z8cky7watooijq",  
         "disabled": true  
        },  
        {  
         "key": "app_secret",  
         "value": "c54100b5b15d69d5cf0db9e8a653333a60f73c23",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "B68B05A75DA27E2A3731B666965D3206",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713385043",  
         "disabled": true  
        }  
       ]  
      }  
     },  
     "response": []  
    },  
    {  
     "name": "getReturnOrderList",  
     "request": {  
      "method": "POST",  
      "header": [  
       {  
        "key": "content-type",  
        "value": "application/json",  
        "type": "text"  
       }  
      ],  
      "body": {  
       "mode": "raw",  
       "raw": "{\n    \"type\": \"bg.aftersales.parentreturnorder.get\",\n    \"parentAfterSalesSn\": \"\",\n    \"afterSalesSn\": \"\"\n}",  
       "options": {  
        "raw": {  
         "language": "json"  
        }  
       }  
      },  
      "url": {  
       "raw": "{{us_endpoints}}",  
       "host": [  
        "{{us_endpoints}}"  
       ],  
       "query": [  
        {  
         "key": "type",  
         "value": "bg.order.list.get",  
         "disabled": true  
        },  
        {  
         "key": "app_key",  
         "value": "c9a17fa695a07be52f1836c3e2ec0b23",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713382474",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "2811DADD6B8C790638C96D4C9E4471E4",  
         "disabled": true  
        },  
        {  
         "key": "data_type",  
         "value": "JSON",  
         "disabled": true  
        },  
        {  
         "key": "access_token",  
         "value": "dfgu5e5yafdl4aervx58b3rih807wjbdsrugcnogo4z8cky7watooijq",  
         "disabled": true  
        },  
        {  
         "key": "app_secret",  
         "value": "c54100b5b15d69d5cf0db9e8a653333a60f73c23",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "B68B05A75DA27E2A3731B666965D3206",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713385043",  
         "disabled": true  
        }  
       ]  
      }  
     },  
     "response": []  
    }  
   ]  
  },  
  {  
   "name": "Buy Shipping",  
   "item": [  
    {  
     "name": "getShippingServices",  
     "request": {  
      "method": "POST",  
      "header": [  
       {  
        "key": "content-type",  
        "value": "application/json",  
        "type": "text"  
       }  
      ],  
      "body": {  
       "mode": "raw",  
       "raw": "{\n    \"type\": \"bg.logistics.shippingservices.get\",\n    \"warehouseId\": \"WH-03283345879192414\",\n    \"length\": \"222\",\n    \"width\": \"222\",\n    \"height\": \"222\",\n    \"weight\": \"11\",\n    \"dimensionUnit\": \"in\",\n    \"weightUnit\": \"lb\",\n    \"orderSnList\": [\n        \"211-08525158244391299\"\n    ]\n}",  
       "options": {  
        "raw": {  
         "language": "json"  
        }  
       }  
      },  
      "url": {  
       "raw": "{{us_endpoints}}",  
       "host": [  
        "{{us_endpoints}}"  
       ],  
       "query": [  
        {  
         "key": "type",  
         "value": "bg.order.list.get",  
         "disabled": true  
        },  
        {  
         "key": "app_key",  
         "value": "c9a17fa695a07be52f1836c3e2ec0b23",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713382474",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "2811DADD6B8C790638C96D4C9E4471E4",  
         "disabled": true  
        },  
        {  
         "key": "data_type",  
         "value": "JSON",  
         "disabled": true  
        },  
        {  
         "key": "access_token",  
         "value": "dfgu5e5yafdl4aervx58b3rih807wjbdsrugcnogo4z8cky7watooijq",  
         "disabled": true  
        },  
        {  
         "key": "app_secret",  
         "value": "c54100b5b15d69d5cf0db9e8a653333a60f73c23",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "B68B05A75DA27E2A3731B666965D3206",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713385043",  
         "disabled": true  
        }  
       ]  
      }  
     },  
     "response": []  
    },  
    {  
     "name": "getWarehouseList",  
     "request": {  
      "method": "POST",  
      "header": [  
       {  
        "key": "content-type",  
        "value": "application/json",  
        "type": "text"  
       }  
      ],  
      "body": {  
       "mode": "raw",  
       "raw": "{\n    \"type\": \"bg.logistics.warehouse.list.get\"\n}",  
       "options": {  
        "raw": {  
         "language": "json"  
        }  
       }  
      },  
      "url": {  
       "raw": "{{us_endpoints}}",  
       "host": [  
        "{{us_endpoints}}"  
       ],  
       "query": [  
        {  
         "key": "type",  
         "value": "bg.order.list.get",  
         "disabled": true  
        },  
        {  
         "key": "app_key",  
         "value": "c9a17fa695a07be52f1836c3e2ec0b23",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713382474",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "2811DADD6B8C790638C96D4C9E4471E4",  
         "disabled": true  
        },  
        {  
         "key": "data_type",  
         "value": "JSON",  
         "disabled": true  
        },  
        {  
         "key": "access_token",  
         "value": "dfgu5e5yafdl4aervx58b3rih807wjbdsrugcnogo4z8cky7watooijq",  
         "disabled": true  
        },  
        {  
         "key": "app_secret",  
         "value": "c54100b5b15d69d5cf0db9e8a653333a60f73c23",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "B68B05A75DA27E2A3731B666965D3206",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713385043",  
         "disabled": true  
        }  
       ]  
      }  
     },  
     "response": []  
    },  
    {  
     "name": "createShipment",  
     "request": {  
      "method": "POST",  
      "header": [  
       {  
        "key": "content-type",  
        "value": "application/json",  
        "type": "text"  
       }  
      ],  
      "body": {  
       "mode": "raw",  
       "raw": "{\n    \"type\": \"bg.logistics.shipment.create\",\n    \"sendType\": 0,\n    \"sendRequestList\": [\n        {\n            \"warehouseId\": \"WH-015653600871924144\",\n            \"length\": \"1.01\",\n            \"width\": \"1.01\",\n            \"height\": \"1.01\",\n            \"weight\": \"1.01\",\n            \"dimensionUnit\": \"in\",\n            \"weightUnit\": \"lb\",\n            \"shipCompanyId\": 314439762,\n            \"channelId\": 25459115954176,\n            \"orderSendInfoList\": [\n                {\n                    \"quantity\": 1,\n                    \"orderSn\": \"211-17609009288231171\",\n                    \"parentOrderSn\": \"PO-211-17608988316711171\",\n                    \"goodsId\": 602242644031031,\n                    \"skuId\": 36165772167792\n                }\n            ]\n        }\n    ]\n}",  
       "options": {  
        "raw": {  
         "language": "json"  
        }  
       }  
      },  
      "url": {  
       "raw": "{{us_endpoints}}",  
       "host": [  
        "{{us_endpoints}}"  
       ],  
       "query": [  
        {  
         "key": "type",  
         "value": "bg.order.list.get",  
         "disabled": true  
        },  
        {  
         "key": "app_key",  
         "value": "c9a17fa695a07be52f1836c3e2ec0b23",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713382474",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "2811DADD6B8C790638C96D4C9E4471E4",  
         "disabled": true  
        },  
        {  
         "key": "data_type",  
         "value": "JSON",  
         "disabled": true  
        },  
        {  
         "key": "access_token",  
         "value": "dfgu5e5yafdl4aervx58b3rih807wjbdsrugcnogo4z8cky7watooijq",  
         "disabled": true  
        },  
        {  
         "key": "app_secret",  
         "value": "c54100b5b15d69d5cf0db9e8a653333a60f73c23",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "B68B05A75DA27E2A3731B666965D3206",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713385043",  
         "disabled": true  
        }  
       ]  
      }  
     },  
     "response": []  
    },  
    {  
     "name": "updateShipment",  
     "request": {  
      "method": "POST",  
      "header": [  
       {  
        "key": "content-type",  
        "value": "application/json",  
        "type": "text"  
       }  
      ],  
      "body": {  
       "mode": "raw",  
       "raw": "{\n    \"type\": \"bg.logistics.shipment.update\",\n    \"retrySendPackageRequestList\": [\n        {\n            \"warehouseId\": \"PK-5248977270210713114\",\n            \"packageSn\": \"PK-5248977270210713114\",\n            \"length\": \"1.01\",\n            \"width\": \"1.01\",\n            \"height\": \"1.01\",\n            \"weight\": \"1\",\n            \"dimensionUnit\": \"in\",\n            \"weightUnit\": \"lb\",\n            \"shipCompanyId\": 314439762,\n            \"channelId\": 25459115954176,\n            \"orderSendInfoList\": [\n                {\n                    \"quantity\": 1,\n                    \"orderSn\": \"211-17609009288231171\",\n                    \"parentOrderSn\": \"PO-211-17608988316711171\",\n                    \"goodsId\": 602242644031031,\n                    \"skuId\": 36165772167792\n                }\n            ]\n        }\n    ]\n}",  
       "options": {  
        "raw": {  
         "language": "json"  
        }  
       }  
      },  
      "url": {  
       "raw": "{{us_endpoints}}",  
       "host": [  
        "{{us_endpoints}}"  
       ],  
       "query": [  
        {  
         "key": "type",  
         "value": "bg.order.list.get",  
         "disabled": true  
        },  
        {  
         "key": "app_key",  
         "value": "c9a17fa695a07be52f1836c3e2ec0b23",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713382474",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "2811DADD6B8C790638C96D4C9E4471E4",  
         "disabled": true  
        },  
        {  
         "key": "data_type",  
         "value": "JSON",  
         "disabled": true  
        },  
        {  
         "key": "access_token",  
         "value": "dfgu5e5yafdl4aervx58b3rih807wjbdsrugcnogo4z8cky7watooijq",  
         "disabled": true  
        },  
        {  
         "key": "app_secret",  
         "value": "c54100b5b15d69d5cf0db9e8a653333a60f73c23",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "B68B05A75DA27E2A3731B666965D3206",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713385043",  
         "disabled": true  
        }  
       ]  
      }  
     },  
     "response": []  
    },  
    {  
     "name": "getShippingLabel",  
     "request": {  
      "method": "POST",  
      "header": [  
       {  
        "key": "content-type",  
        "value": "application/json",  
        "type": "text"  
       }  
      ],  
      "body": {  
       "mode": "raw",  
       "raw": "{\n    \"type\": \"bg.logistics.shipment.document.get\",\n    \"packageSnList\": [\n        \"PK-3907568816619673114\"\n    ]\n}",  
       "options": {  
        "raw": {  
         "language": "json"  
        }  
       }  
      },  
      "url": {  
       "raw": "{{us_endpoints}}",  
       "host": [  
        "{{us_endpoints}}"  
       ],  
       "query": [  
        {  
         "key": "type",  
         "value": "bg.order.list.get",  
         "disabled": true  
        },  
        {  
         "key": "app_key",  
         "value": "c9a17fa695a07be52f1836c3e2ec0b23",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713382474",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "2811DADD6B8C790638C96D4C9E4471E4",  
         "disabled": true  
        },  
        {  
         "key": "data_type",  
         "value": "JSON",  
         "disabled": true  
        },  
        {  
         "key": "access_token",  
         "value": "dfgu5e5yafdl4aervx58b3rih807wjbdsrugcnogo4z8cky7watooijq",  
         "disabled": true  
        },  
        {  
         "key": "app_secret",  
         "value": "c54100b5b15d69d5cf0db9e8a653333a60f73c23",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "B68B05A75DA27E2A3731B666965D3206",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713385043",  
         "disabled": true  
        }  
       ]  
      }  
     },  
     "response": []  
    },  
    {  
     "name": "getShipLaterPackages",  
     "request": {  
      "method": "POST",  
      "header": [  
       {  
        "key": "content-type",  
        "value": "application/json",  
        "type": "text"  
       }  
      ],  
      "body": {  
       "mode": "raw",  
       "raw": "{\n    \"type\": \"bg.order.unshipped.package.get\",\n    \"pageSize\": 1,\n    \"pageNumber\": 1\n}",  
       "options": {  
        "raw": {  
         "language": "json"  
        }  
       }  
      },  
      "url": {  
       "raw": "{{us_endpoints}}",  
       "host": [  
        "{{us_endpoints}}"  
       ],  
       "query": [  
        {  
         "key": "type",  
         "value": "bg.order.list.get",  
         "disabled": true  
        },  
        {  
         "key": "app_key",  
         "value": "c9a17fa695a07be52f1836c3e2ec0b23",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713382474",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "2811DADD6B8C790638C96D4C9E4471E4",  
         "disabled": true  
        },  
        {  
         "key": "data_type",  
         "value": "JSON",  
         "disabled": true  
        },  
        {  
         "key": "access_token",  
         "value": "dfgu5e5yafdl4aervx58b3rih807wjbdsrugcnogo4z8cky7watooijq",  
         "disabled": true  
        },  
        {  
         "key": "app_secret",  
         "value": "c54100b5b15d69d5cf0db9e8a653333a60f73c23",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "B68B05A75DA27E2A3731B666965D3206",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713385043",  
         "disabled": true  
        }  
       ]  
      }  
     },  
     "response": []  
    },  
    {  
     "name": "confirmShipLaterPackagesShipped",  
     "request": {  
      "method": "POST",  
      "header": [  
       {  
        "key": "content-type",  
        "value": "application/json",  
        "type": "text"  
       }  
      ],  
      "body": {  
       "mode": "raw",  
       "raw": "{\n    \"type\": \"bg.logistics.shipped.package.confirm\",\n    \"packageSendInfoList\": [\n        {\n            \"trackingNumber\": \"111\",\n            \"packageSn\": \"111\",\n            \"packageDetail\": {\n                \"quantity\": 1,\n                \"orderSn\": \"11\",\n                \"parentOrderSn\": \"11\"\n\n            }\n\n        }\n    ]\n}",  
       "options": {  
        "raw": {  
         "language": "json"  
        }  
       }  
      },  
      "url": {  
       "raw": "{{us_endpoints}}",  
       "host": [  
        "{{us_endpoints}}"  
       ],  
       "query": [  
        {  
         "key": "type",  
         "value": "bg.order.list.get",  
         "disabled": true  
        },  
        {  
         "key": "app_key",  
         "value": "c9a17fa695a07be52f1836c3e2ec0b23",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713382474",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "2811DADD6B8C790638C96D4C9E4471E4",  
         "disabled": true  
        },  
        {  
         "key": "data_type",  
         "value": "JSON",  
         "disabled": true  
        },  
        {  
         "key": "access_token",  
         "value": "dfgu5e5yafdl4aervx58b3rih807wjbdsrugcnogo4z8cky7watooijq",  
         "disabled": true  
        },  
        {  
         "key": "app_secret",  
         "value": "c54100b5b15d69d5cf0db9e8a653333a60f73c23",  
         "disabled": true  
        },  
        {  
         "key": "sign",  
         "value": "B68B05A75DA27E2A3731B666965D3206",  
         "disabled": true  
        },  
        {  
         "key": "timestamp",  
         "value": "1713385043",  
         "disabled": true  
        }  
       ]  
      }  
     },  
     "response": []  
    }  
   ]  
  }  
 ],  
 "event": [  
  {  
   "listen": "prerequest",  
   "script": {  
    "type": "text/javascript",  
    "exec": [  
     "pm.variables.set(\"timestamp\", Math.floor(Date.now() / 1000));",  
     "const app_secret = pm.collectionVariables.get(\"app_secret\");",  
     "const app_key = pm.collectionVariables.get(\"app_key\");",  
     "const access_token = pm.collectionVariables.get(\"access_token\");",  
     "const data_type = pm.collectionVariables.get(\"data_type\");",  
     "",  
     "let body = pm.request.body.raw;",  
     "let request_params = JSON.parse(body);",  
     "let additionalParams = {",  
     "    app_key: app_key,",  
     "    access_token: access_token,",  
     "    data_type: data_type,",  
     "    timestamp: pm.variables.get(\"timestamp\") ",  
     "};",  
     "Object.assign(request_params, additionalParams); ",  
     "console.log(\"request_params:\", request_params);",  
     "",  
     "let keys = Object.keys(request_params).sort();",  
     "",  
     "let temp = [];",  
     "keys.forEach(key => {",  
     "    let value = JSON.stringify(request_params[key], null, 0)",  
     "        .replace(/^\"|\"$/g, ''); ",  
     "    temp.push(key + value);",  
     "});",  
     "",  
     "let un_sign = app_secret + temp.join('') + app_secret;",  
     "console.log(\"Un-Sign String:\", un_sign);",  
     "",  
     "let sign = CryptoJS.MD5(un_sign).toString().toUpperCase();",  
     "console.log(\"Signature:\", sign);",  
     "",  
     "request_params[\"sign\"] = sign;",  
     "pm.request.body.update(JSON.stringify(request_params));",  
     "console.log(\"Updated Body with Signature:\", request_params);"  
    ]  
   }  
  },  
  {  
   "listen": "test",  
   "script": {  
    "type": "text/javascript",  
    "exec": [  
     ""  
    ]  
   }  
  }  
 ],  
 "variable": [  
  {  
   "key": "us_endpoints",  
   "value": "https://openapi-b-us.temu.com/openapi/router",  
   "type": "default"  
  },  
  {  
   "key": "app_key",  
   "value": "",  
   "type": "default"  
  },  
  {  
   "key": "app_secret",  
   "value": "",  
   "type": "default"  
  },  
  {  
   "key": "access_token",  
   "value": "",  
   "type": "default"  
  },  
  {  
   "key": "data_type",  
   "value": "JSON",  
   "type": "default"  
  }  
 ]  
}
```
