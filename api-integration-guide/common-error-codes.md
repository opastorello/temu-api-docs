# Common Error Codes

When making API requests to Temu, we first perform a validation at the gateway layer. The errors from this layer are provided in the following table format:

# 

Common Errors

****

****

****

``

``

``

``

````

``

| Error Code | Error Msg | Description |
|---|---|---|
| 1000000 | SUCCESS | SUCCESS. |
| 2000000 | BUSINESS_EXCEPTION | Call Internal API failed. |
| 3000000 | BAD_PARAMS | BAD_PARAMS. |
| 3000001 | SIGN_UNVALID | Sign invalid. |
| 3000002 | there is no type in body. | API type is missing. |
| 3000003 | type not exists | API type status did not exist. |
| 3000004 | type has been sunset, please stop calling this type and change to use another one. | API type status is wrong. |
| 3000010 | there is no timestamp in body. | timestamp is missing. |
| 3000011 | timestamp is invalid. | timestamp is invalid, if timestamp>current_time+300s. |
| 3000012 | timestamp is expired. | timestamp is expired. |
| 3000013 | there is no data_type in body. | data_type type is missing. |
| 3000014 | data_type is invalid | The data_type parameter value is invalid (other characters besides "Json" (case-insensitive) were passed). |
| 3000019 | there is no client_id in body. | app_key is missing. |
| 3000020 | client_id not exists. | app_key did not exist. |
| 3000021 | client_id don't have this api permission. | The app_key does not have permission to call the Type interface. |
| 3000022 | client_id have been suspended, please contact temu product support team to recover your app status. | The APP status is unavailable. |
| 3000025 | there is no app_key in body. | app_key is missing. |
| 3000026 | app_key not exists. | app_key did not exist. |
| 3000027 | app_key don't have this api permission. | The app_key does not have permission to call the Type interface. |
| 3000028 | app_key have been suspended, please contact temu product support team to recover your app status. | The APP status is unavailable. |
| 3000030 | there is no access_token in body. | access_token is missing. |
| 3000031 | access_token not exists. | access_token did not exist. |
| 3000032 | access_token don't have this api access, please ask for seller to authorize this api in seller center first，and share the new access_token with you. | The access_token does not have permission to call the Type interface. |
| 3000033 | access_token and app_key are not mapping. | The access_token does not match the app_key. |
| 3000034 | access_token is expired or have been refreshed, please contact seller to share the new access_token with you. | The access_token status is abnormal. |
| 3000040 | there is no sign in body. | sign is missing |
| 4000000 | SYSTEM_EXCEPTION | SYSTEM_EXCEPTION |
| 4000004 | RATE_LIMIT_EXCEED_EXCEPTION | The request exceeds the rate limit threshold. |
| 5000000 | AUTHORIZE_NOT_ALLOW | The merchant is not authorized / access token verification failed / interface authentication failed. |
| 5000001 | ROUTER_NOT_ALLOW | The file upload route must include "upload". |
| 5000002 | NOT_SUPPORT_STAGING_ENV | The current request environment is not the formal environment. Please check the request header information. |
| 5000003 | NOT_IN_IP_WHITE_LIST | The requesting IP address is not on the whitelist. |
| 6000001 | RPC_INTERFACE_NOT_FOUND | Internal api is missing. |
| 7000000 | BUSINESS_SERVICE_ERROR | BUSINESS_SERVICE_ERROR |
