# Make your Calls with Postman

**Last update:** 2025-04-02 00:05:16

Using Postman for quick API testing is a common practice. This guide provides faster onboarding tools.

## Import from Postman

Import URL:
```
https://api.postman.com/collections/22962806-af9fef2f-a956-4667-a3a1-59c176d422d5?access_key=PMAT-01JPFB038YSF79SM1ZK3M8882F
```

## Setup Steps

### 1. Set Variables

Set all variables within the Postman project as common parameters. Ensure each API request in the project only includes the request body.

### 2. Set Pre-request Script

Use a pre-request script for signing. Example code:

```javascript
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

### 3. Set Request Parameters

Set request parameters for each API according to the API documentation.

## Appendix — Postman Collection (v2.1)

A ready-to-use Postman collection with the following API groups:

### Authorization APIs
- `getAccessTokenInfo` → `bg.open.accesstoken.info.get`
- `createAccessTokenInfo` → `bg.open.accesstoken.create`

### Products Listing APIs
- `getGoodsCategories` → `bg.local.goods.cats.get`
- `getGoodsTemplate` → `bg.local.goods.template.get`
- `getAvailableBrandAndTrademark`

### Environment Variables to Configure

| Variable | Description |
|---|---|
| `us_endpoints` | US production endpoint: `https://openapi-b-us.temu.com/openapi/router` |
| `eu_endpoints` | EU production endpoint: `https://openapi-b-eu.temu.com/openapi/router` |
| `global_endpoints` | Global endpoint: `https://openapi-b-global.temu.com/openapi/router` |
| `app_key` | Your application key |
| `app_secret` | Your application secret |
| `access_token` | Seller access token |
| `data_type` | Fixed value: `JSON` |
