# temu.local.mall.tags.get

**Last update:** 2025-12-02 09:11:12

**Description:** This API allows sellers to retrieve the list of store tags currently assigned to their store.

---

## Request URL

| Method | URL | Region |
|---|---|---|
| POST | `https://openapi-b-global.temu.com/openapi/router` | GLOBAL |

---

## Common Parameters

| Property | Type | Required | Description |
|---|---|---|---|
| `type` | STRING | True | API name, e.g. `bg.*` |
| `app_key` | STRING | True | |
| `access_token` | STRING | True | A secure token for access control. |
| `sign` | STRING | True | |
| `timestamp` | STRING | True | UNIX time format (seconds), 10 digits, within ±300 seconds of current time. |
| `data_type` | STRING | False | Data format — fixed as JSON. |
| `version` | STRING | False | API version, defaults to V1. |

---

## Request Parameters

No specific request parameters beyond common parameters.

---

## Response

| Property | Type | Description |
|---|---|---|
| `response` | OBJECT | |
| `success` | BOOLEAN | success |
| `errorCode` | INTEGER | error code |
| `errorMsg` | STRING | error message |
| `result` | OBJECT | Specific information |
| `result.tags` | LIST\<INTEGER\> | List of store tag IDs |

---

## Request Example (cURL)

```bash
curl -X POST \
'https://openapi-b-global.temu.com/openapi/router' \
 -H 'content-type: application/json' \
 -d '{
  "access_token" : "test",
  "app_key" : "test",
  "sign" : "test",
  "data_type" : "test",
  "type" : "test",
  "version" : "test",
  "timestamp" : "test"
}'
```

---

## Response Example

```json
{
  "result": {
    "tags": [1, 1]
  },
  "errorCode": 1,
  "success": true,
  "errorMsg": "test"
}
```

---

## Error Codes

No specific error codes documented.

---

## Permission Package

| Permission Package | App Type |
|---|---|
| Local Basic Management | private, public |
