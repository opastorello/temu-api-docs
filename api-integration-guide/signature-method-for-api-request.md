# Signature Method for API request

# 

Signature Method

- 

In order to prevent malicious tampering during the API call process, any API call needs to carry a request signature. The open platform server will verify the signature based on the request parameters, and requests with illegal signatures will be rejected.

- 

The currently supported signature method is: `MD5`  ( sign_method = md5), and the signature process is as follows:

  - 

All request parameters (including common parameters and request parameters) in this request are sorted in ascending order by the first letter in ASCII format . For the same letters, the next letter is used for secondary sorting. The alphabetical order is from left to right, and so on.

  - 

The sorted results are concatenated in the order of parameter name $key parameter value `$value` , and the concatenation does not contain any characters.

  - 

The concatenated strings are further concatenated into one string (a long string containing all kv strings), and app_secret is concatenated at the head and tail of the long string to complete the assembly of the signature string.

  - 

Finally, the signature string is encrypted using the MD5 method, and the resulting MD5 encrypted ciphertext is converted to uppercase, which is the sign value. 

# 

Signature Example

****

****

****

****

```
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

```

****

- 

- 

- 

```
  
  
  
  
  
  
  
  

```

****

************``

```

```

****

- 

``

- 

****

```
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

```

****

- 

``

- 

``

- 

``

- 

``

```
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

```

| Steps | Actions | Example |
|---|---|---|
| Step 1 | Determine request parameters | { " sendRequestList ": [  {   " trackingNumber ": "270324232756",   "carrierId": "699272611",   "orderSendInfoList": [    {     "goodsId": 601099548666279,     "orderSn": "211-21905473070712792",     "parentOrderSn": "PO-211-21905452099192792",     "quantity": 1,     "skuId": 17592352673534    }   ]  } ], " sendType ": 0} |
| Step 2 | Assemble request parameters and common parametersAdd common parameters to JSON object dictionaryby $key in ascending order using asciiString concatenation $key and $value | [ "access_token2nifvmpyymvypwmcms5ct4uqqudrwgpmzbcnmkt1jzjkuaf3x56iixym", "app_keyf9d5cc9313893a20d5aa85c654e8f503", "data_typeJSON", "sendRequestList[{\"orderSendInfoList\":[{\"quantity\":1,\"orderSn\":\"211-21905473070712792\",\"parentOrderSn\":\"PO-211-21905452099192792\",\"goodsId\":601099548666279,\"skuId\":17592352673534}],\"carrierId\":\"699272611\",\"trackingNumber\":\"270324232756\"}]", "sendType0", "timestamp1711009072", "typebg.logistics.shipment.confirm"] |
| Step 3 | Seamlessly concatenate strings. After concatenation, add app_secret to the head and tail . Assume that app_secret is c7e0a1a63542be4de3cb5488f9fba8149e8fc290 | c7e0a1a63542be4de3cb5488f9fba8149e8fc290access_token2nifvmpyymvypwmcms5ct4uqqudrwgpmzbcnmkt1jzjkuaf3x56iixymapp_keyf9d5cc931 3893a20d5aa85c654e8f503data_typeJSONsendRequestList[{"orderSendInfoList":[{"quantity":1,"orderSn":"211-21905473070712792","pa rentOrderSn":"PO-211-21905452099192792","goodsId":601099548666279,"skuId":17592352673534}],"carrierId":"699272611","tracking Number":"270324232756"}]sendType0timestamp1711009072typebg.logistics.shipment.confirmc7e0a1a63542be4de3cb5488f9fba8149e8fc290 |
| Step 4 | Generate the signature sign from the above concatenated stringThe signature is signed using the MD5  method to generate an MD5 signatureThe upperCase method converts the MD5 signature to uppercase format | 4CCF219942D4180C6DDA3CE36C1B838F |
| Step 5 | Insert the sign value into the original assembled JSON to construct a complete request body | { "app_key ": "f9d5cc9313893a20d5aa85c654e8f503", "data_type ": "JSON", "access_token": "2nifvmpyymvypwmcms5ct4uqqudrwgpmzbcnmkt1jzjkuaf3x56iixym", "sendRequestList": [  {   " carrierId ": "699272611",   " trackingNumber ": "270324232756",   "orderSendInfoList": [    {     " goodsId ": 601099548666279,     " skuId ": 17592352673534,     "orderSn": "211-21905473070712792",     "parentOrderSn": "PO-211-21905452099192792",     "quantity": 1    }   ]  } ], "sendType": 0, "sign": "4CCF219942D4180C6DDA3CE36C1B838F", "timestamp": 1711009072, "type": " bg.logistics .shipment.confirm "} |
| Step 6 | Initiate an API request (taking JSON data format request as an example)Request method: POST Request url : host Request header: content-type: application/json  Request body: See the example of step 5 above | curl -X POST {{host}} \-H "Content-Type: application/json" \-d '{  "app_key": "f9d5cc9313893a20d5aa85c654e8f503",  "data_type": "JSON",  "access_token": "2nifvmpyymvypwmcms5ct4uqqudrwgpmzbcnmkt1jzjkuaf3x56iixym",  "sendRequestList": [    {      "carrierId": "699272611",      "trackingNumber": "270324232756",      "orderSendInfoList": [        {          "goodsId": 601099548666279,          "skuId": 17592352673534,          "orderSn": "211-21905473070712792",          "parentOrderSn": "PO-211-21905452099192792",          "quantity": 1        }      ]    }  ],  "sendType": 0,  "sign": "4CCF219942D4180C6DDA3CE36C1B838F",  "timestamp": 1711009072,  "type": "bg.logistics.shipment.confirm"}' |
