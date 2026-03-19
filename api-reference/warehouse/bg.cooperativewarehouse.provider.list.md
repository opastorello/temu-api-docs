# bg.cooperativewarehouse.provider.list

**Cooperative warehouse provider list**

cooperate warehouse erp order

**Method:** POST  
**URL:** https://openapi-b-global.temu.com/openapi/router

---

## Common Parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| type | 4 | No |  |
| app_key | 4 | No |  |
| access_token | 4 | No |  |
| sign | 4 | No |  |
| timestamp | 4 | No |  |
| data_type | 4 | No |  |
| version | 4 | No |  |

## Request Parameters

| Parameter | Type | Required | Description | Example |
|---|---|---|---|---|
| needAllPlatformProviders | 5 | No |  |  |

## Response Parameters

| Parameter | Type | Required | Description | Example |
|---|---|---|---|---|
| success | 5 | No |  |  |
| errorCode | 1 | No |  |  |
| errorMsg | 4 | No |  |  |
| result | 6 | No |  |  |

## Error Codes

| Error Code | Message |
|---|---|
| 170020001 | This ERP provider is not supported. |
| 170020002 | This mall is not authorized to the cooperative warehouse  service provider. |
| 170020003 | The parameter is illegal, please check  and try again. |
| 170020004 | This fulfillment order not exists, please check if the fulfillment number is correct. |
| 170020005 | This cooperative warehouse customer code is not match the authorized customer code. |

## Request Example

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
  "timestamp" : "test",
  "needAllPlatformProviders" : true
}'
```

## Response Example

```json
{
  "result" : {
    "permitsStatus" : 1,
    "warehouseProviderList" : [ {
      "supportedPackageDeliveryType" : [ 1, 1 ],
      "supportedShipCompany" : [ {
        "shipCompanyName" : "test",
        "shipCompanyId" : 1
      } ],
      "regionId" : [ "test", "test" ],
      "supportNoCwCustomCode" : 1,
      "cwCustomerCodeList" : [ "test", "test" ],
      "warehouseProviderBrandName" : "test",
      "warehouseProviderCode" : "test"
    } ]
  },
  "errorCode" : 1,
  "success" : true,
  "errorMsg" : "test"
}
```