# Temu Open API Request Example with Signature Generation in Python

**Last update:** 2025-10-27 03:26:28

This example demonstrates how to call a Temu Open API interface in Python, including how to assemble request parameters, generate the request signature, and send the signed request to the Temu server.

The example includes two files:

1. **TestSign.py** — Implements the signature generation algorithm required by the Temu Open API.
2. **TestRequestwithSign.py** — Shows a full example of calling the Temu API using a test app and test shop under the "Sandbox Test Shops" environment.

---

## TestSign.py

```python
import json
import hashlib

def api_sign_method(app_secret, request_params):
    temp = []
    # Sort parameters by key
    request_params = sorted(request_params.items())

    for k, v in request_params:
        v = json.dumps(v, ensure_ascii=False, separators=(',', ':'))
        temp.append(str(k) + str(v.strip('"')))

    un_sign = ''.join(temp)
    un_sign = str(app_secret) + un_sign + str(app_secret)
    sign = hashlib.md5(un_sign.encode('utf-8')).hexdigest().upper()
    return sign
```

---

## TestRequestwithSign.py

```python
import requests
import json
import time
import TestSign as testSign

# Global Test App & Test mall in "Sandbox Test Shops"
app_secret = "7c1aa1dd9523801b667ec59dc36541acbc7318b3"
app_key    = "f7f83a8058228c1bc8f4993f28d95557"
access_token = "upl0gho4ovopvyvfiky4x7prgwh3dt1gfjea8ogdfqq1czzblsxs5aeyqew"

# Global Endpoint for apps/shops registered in Global Region
url = "https://openapi-b-global.temu.com/openapi/router?app_secret=" + app_secret

# Common Params
type = "bg.local.goods.cats.get"
version = "V1"
data_type = "JSON"
timestamp = int(time.time())

common_params = {
    "app_key": app_key,
    "data_type": data_type,
    "access_token": access_token,
    "timestamp": timestamp,
    "type": type,
    "version": version
}

# Request Params
parentCatId = 0

request_params = {
    "parentCatId": parentCatId
}

# Before sign Params
before_sign_request = {**common_params, **request_params}

# Sign the request
sign = testSign.api_sign_method(app_secret, before_sign_request)

# Initiate an API request
headers = {
    "Content-Type": "application/json"
}

request_payload = {
    **before_sign_request,
    "sign": sign
}

response = requests.post(url, headers=headers, data=json.dumps(request_payload))

try:
    response_json = response.json()
    formatted_json = json.dumps(response_json, indent=4, ensure_ascii=False)
    print(formatted_json)
except json.JSONDecodeError:
    print("Response is not in JSON format:")
    print(response.text)
```

---

## Summary of Steps

1. Define `app_key`, `app_secret`, and `access_token`
2. Set the appropriate endpoint URL (US / EU / Global)
3. Build common parameters (`app_key`, `data_type`, `access_token`, `timestamp`, `type`, `version`)
4. Add request-specific parameters (e.g., `parentCatId` for category query)
5. Merge common + request params into one dict
6. Generate `sign` using `api_sign_method(app_secret, before_sign_request)`
7. Add `sign` to the payload and POST to the endpoint

## API Reference for bg.local.goods.cats.get

See: https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=966e9ddacb924082a33de7c017c3f248
