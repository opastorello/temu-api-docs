# [Error SOP][4000000]Temu internal system error, please try again later.

| Error Code | Error Message |
|---|---|
| 4000000 | Temu internal system error, please try again later. |

- 

**Potential cause:**

1. 

Affected Interface: bg.local.goods.add

This issue may occur if too many SKUs are added under the same goods, causing downstream interfaces to take longer to process the request and eventually hit the maximum timeout. It may also be caused by network instability. Please retry the request. If the issue persists, feel free to submit an API issue ticket.

**For API error investigation, please provide the following information:**

1. 

**JSON request payload** (including the app key)

1. 

**JSON response payload** (including the request ID)

1. 

**Request timestamp**

1. 

**Request endpoint**

The request ID and timestamp help us locate the relevant logs in our backend systems. Without the timestamp, it may be difficult for the engineering team to find the logs and accurately identify the issue.

The request ID is required for the engineering team to review and accept the issue ticket.

The engineering team is unable to review personal code. Please provide the issue in the form of a JSON request and response payload.

Sample request payload:

curl -X POST \

'[https://openapi-b-global.temu.com/openapi/router](https://openapi-b-global.temu.com/openapi/router)' \

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

Sample response payload:

{

  "result": {

   Xxxxxxxxxxxxxxx

  "errorCode": 1,

  "success": true,

  "errorMsg": "test",

  "requestId": "eu-7af3e77xxxxxxxxx2c84da30",

}
