# Common Parameters

**Last update:** 2025-01-26 09:58:41

## Common Parameters

Common parameters are the parameters that must be passed in when calling any open API. The current Common parameters are as follows:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `type` | STRING | Y | API interface name, such as: `bg.*` |
| `app_key` | STRING | Y | app_key has been successfully created. Contact the operator for issuance. |
| `timestamp` | STRING | Y | Timestamp, in UNIX time format (seconds), 10 digits long. Constraint: `current time - 300s <= input time <= current time + 300s` |
| `sign` | STRING | Y | The API input parameter signature. The signature value is calculated according to the signing algorithm. |
| `access_token` | STRING | Y | User authorization token `access_token`. Can be obtained from Seller Center. The operation will issue the corresponding online store token. |
| `data_type` | STRING | Y | The data format returned by the request. The optional parameters are fixed as `JSON`. |
| `version` | STRING | N | The default API version is V1. If no requirement is set, this parameter is not passed. |

## Request Parameters

In addition to common parameters, API requests must also include request-level parameters if the API itself has them. For detailed descriptions of each API's request parameters, please refer to the corresponding API documentation.
