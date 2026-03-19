# Signature Method for API Request

**Last update:** 2025-01-26 09:58:09

## Signature Method

In order to prevent malicious tampering during the API call process, any API call needs to carry a request signature. The open platform server will verify the signature based on the request parameters, and requests with illegal signatures will be rejected.

The currently supported signature method is: **MD5** (`sign_method = md5`).

### Signature Process

1. All request parameters (including common parameters and request parameters) in this request are **sorted in ascending order by the first letter in ASCII format**. For the same letters, the next letter is used for secondary sorting. The alphabetical order is from left to right.

2. The sorted results are concatenated in the order of `parameter_name` + `parameter_value` — the concatenation does not contain any separator characters.

3. The concatenated strings are further joined into one long string containing all kv pairs. Then `app_secret` is **prepended and appended** to complete the signature string assembly.

4. Finally, the signature string is encrypted using MD5, and the resulting ciphertext is **converted to uppercase** — this is the `sign` value.

## Signature Example

### Step 1 — Determine Request Parameters

```json
{
  "sendRequestList": [
    {
      "trackingNumber": "270324232756",
      "carrierId": "699272611",
      "orderSendInfoList": [
        {
          "goodsId": 601099548666279,
          "orderSn": "211-21905473070712792",
          "parentOrderSn": "PO-211-21905452099192792",
          "quantity": 1,
          "skuId": 17592352673534
        }
      ]
    }
  ],
  "sendType": 0
}
```

### Step 2 — Assemble Request + Common Parameters (sorted by ASCII key)

Add common parameters to the JSON object dictionary, sort all keys by ASCII ascending order, then concatenate `$key$value`:

```
[
  "access_token2nifvmpyymvypwmcms5ct4uqqudrwgpmzbcnmkt1jzjkuaf3x56iixym",
  "app_keyf9d5cc9313893a20d5aa85c654e8f503",
  "data_typeJSON",
  "sendRequestList[{\"orderSendInfoList\":[{\"quantity\":1,\"orderSn\":\"211-21905473070712792\",\"parentOrderSn\":\"PO-211-21905452099192792\",\"goodsId\":601099548666279,\"skuId\":17592352673534}],\"carrierId\":\"699272611\",\"trackingNumber\":\"270324232756\"}]",
  "sendType0",
  "timestamp1711009072",
  "typebg.logistics.shipment.confirm"
]
```

### Step 3 — Concatenate and Wrap with app_secret

Seamlessly concatenate all strings, then add `app_secret` to **head and tail**.

Assume `app_secret = c7e0a1a63542be4de3cb5488f9fba8149e8fc290`

```
c7e0a1a63542be4de3cb5488f9fba8149e8fc290access_token2nifvmpyymvypwmcms5ct4uqqudrwgpmzbcnmkt1jzjkuaf3x56iixymapp_keyf9d5cc9313893a20d5aa85c654e8f503data_typeJSONsendRequestList[{"orderSendInfoList":[{"quantity":1,"orderSn":"211-21905473070712792","parentOrderSn":"PO-211-21905452099192792","goodsId":601099548666279,"skuId":17592352673534}],"carrierId":"699272611","trackingNumber":"270324232756"}]sendType0timestamp1711009072typebg.logistics.shipment.confirmc7e0a1a63542be4de3cb5488f9fba8149e8fc290
```

### Step 4 — Generate MD5 Signature (uppercase)

Apply MD5 to the string above, then convert to uppercase:

```
4CCF219942D4180C6DDA3CE36C1B838F
```

### Step 5 — Full Request Body

```json
{
  "app_key": "f9d5cc9313893a20d5aa85c654e8f503",
  "data_type": "JSON",
  "access_token": "2nifvmpyymvypwmcms5ct4uqqudrwgpmzbcnmkt1jzjkuaf3x56iixym",
  "sendRequestList": [
    {
      "carrierId": "699272611",
      "trackingNumber": "270324232756",
      "orderSendInfoList": [
        {
          "goodsId": 601099548666279,
          "skuId": 17592352673534,
          "orderSn": "211-21905473070712792",
          "parentOrderSn": "PO-211-21905452099192792",
          "quantity": 1
        }
      ]
    }
  ],
  "sendType": 0,
  "sign": "4CCF219942D4180C6DDA3CE36C1B838F",
  "timestamp": 1711009072,
  "type": "bg.logistics.shipment.confirm"
}
```

### Step 6 — Make the API Request

- **Method:** POST
- **URL:** `{host}` (e.g., `https://openapi-b-us.temu.com/openapi/router`)
- **Header:** `Content-Type: application/json`
- **Body:** See Step 5 above

```bash
curl -X POST {host} \
-H "Content-Type: application/json" \
-d '{
  "app_key": "f9d5cc9313893a20d5aa85c654e8f503",
  "data_type": "JSON",
  "access_token": "2nifvmpyymvypwmcms5ct4uqqudrwgpmzbcnmkt1jzjkuaf3x56iixym",
  "sendRequestList": [...],
  "sendType": 0,
  "sign": "4CCF219942D4180C6DDA3CE36C1B838F",
  "timestamp": 1711009072,
  "type": "bg.logistics.shipment.confirm"
}'
```
