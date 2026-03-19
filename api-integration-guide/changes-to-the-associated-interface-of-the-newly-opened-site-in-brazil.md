# Changes to the associated interface of the newly opened site in Brazil

## 

I. Background of Changes

- Based on the unique tax logic in Brazil: Merchants are required to provide a tax invoice before shipping to proceed with the shipment.

- Based on the specific fulfillment model in Brazil: By default, the vast majority of orders will be fulfilled through the Buy-shipping on TEMU, and the shipping label cost is borne by temu; only specific orders on the whitelist can be switched to self-shipment.

## 

II. Changes to Corresponding Interfaces

- General logic explanation of changes

- Changes caused by special tax logic:

- During product listing, the `costTemplate` must be filled in;

- An address field for the consumer's tax number is added to be returned to the merchant for generating invoices;

- The CALL form interface retrieves available logistics providers for Brazilian orders:

- An additional parameter`invoiceAccessKey`  (the unique identifier for tax invoices) is required;

- Since the cost is borne by the platform, only the platform's assessment of the unique available channel for this package will be returned, and there will be no estimated freight amount for the channel;

- For Brazilian orders under the CALL form interface:

- An additional parameter `invoiceAccessKey` (the unique identifier for tax invoices) is required;

- Only after successful verification can the call be successful;

- Considering the possibility of incorrect correspondence between packages and `invoiceAccessKey`, this period supports re-calling for packages that have been successfully called;

- For the parameter` confirmAcceptance` with the value `SUCCESSFUL_RETRY`, it means re-calling. At this time, a new accesskey can be re-entered for retrying the order;

- Restrictions on fulfillment mode lead to changes:

- An order marking is added: whether to restrict `RESTRICT_SELF_SHIPPING,` `RESTRICT_CALL_SHIPPING`

- Fulfillment restrictions are added: orders restricting self-fulfillment will be intercepted with an error message when calling the self-fulfillment interface; orders restricting the CALL form will be intercepted with an error message when calling the Buy-shipping on TEMU;

## 

III. Detailed Logic of Interface Changes

### 

1. Changes to product interface: When placing orders, add the mandatory field` costTemplateId`

a. Associated interface: [bg.local.goods.add](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=b68f47b094e7469eab7cf58c2b7cf0c6)

b. Changed content:Add a mandatory validation for the `"costTemplateId`" field during the submission process.

c. Affected area: Scene of products being displayed in a Brazilian store

### 

2. Order Interface Change: The order will be marked with `RESTRICT_SELF_SHIPPING,` `RESTRICT_CALL_SHIPPING`

a. Associated interfaces: [bg.order.list.v2.get](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=554fd46b45ee49269cbdd6d4008a5dc1)、[bg.order.detail.v2.get](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=9bf33a25319e4d7bbaf5ece4b823b9c3)

b. Changes:

i. The order is restricted from self-shipment: The field` [fulfillmentWarning]` in the interface will add the return value `**RESTRICT_SELF_SHIPPING**`

ii. The order is restricted from call shipping: The field `[fulfillmentWarning]` in the interface will add the return value `**RESTRICT_CALL_SHIPPING**`

c. Affected areas: Brazilian orders

d. Code demonstration

i. `fulfillmentWarning `field returns `**RESTRICT_SELF_SHIPPING**`

```
{  
    "result": {  
        "result": {  
            "totalItemNum": 1,  
            "pageItems": [  
                {  
                    "parentOrderMap": {  
                        "parentOrderLabel": [  
                            {  
                                "name": "soon_to_be_overdue",  
                                "value": 0  
                            },  
                            {  
                                "name": "past_due",  
                                "value": 0  
                            },  
                            {  
                                "name": "pending_buyer_cancellation",  
                                "value": 0  
                            },  
                            {  
                                "name": "pending_buyer_address_change",  
                                "value": 0  
                            },  
                            {  
                                "name": "pending_risk_control_alert",  
                                "value": 0  
                            },  
                            {  
                                "name": "signature_required_on_delivery",  
                                "value": 0  
                            }  
                        ],  
                        "shippingMethod": 1,  
                        "parentShippingTime": null,  
                        "updateTime": 1754794123,  
                        "latestDeliveryTime": 1755745199,  
                        "fulfillmentWarning": [  
                            "RESTRICT_SELF_SHIPPING"  
                        ],  
                        "parentOrderTime": 1754793163,  
                        "orderPaymentType": "PPD",  
                        "batchOrderNumberList": null,  
                        "regionId": 29,  
                        "parentOrderSn": "PO-029-06682144932474090",  
                        "parentOrderPendingFinishTime": 1754794123,  
                        "siteId": 132,  
                        "expectShipLatestTime": 1755054959,  
                        "parentOrderStatus": 2,  
                        "hasShippingFee": true  
                    },  
                    "orderList": [  
                        {  
                            "canceledQuantityBeforeShipment": 0,  
                            "quantity": 1,  
                            "orderSn": "029-06682165903994090",  
                            "goodsId": 604422071509424,  
                            "orderLabel": [  
                                {  
                                    "name": "customized_products",  
                                    "value": 0  
                                },  
                                {  
                                    "name": "US_to_CA",  
                                    "value": 0  
                                }  
                            ],  
                            "inventoryDeductionWarehouseId": null,  
                            "orderStatus": 2,  
                            "originalGoodsName": "Packaging tape 72 pieces. baxi",  
                            "fulfillmentType": "fulfillBySeller",  
                            "isCancelledDuringPending": false,  
                            "spec": "yellow",  
                            "fulfillmentWarning": [],  
                            "orderPaymentType": "PPD",  
                            "originalSpecName": "yellow",  
                            "originalOrderQuantity": 1,  
                            "thumbUrl": "https://img.kwcdn.com/local-image/s132/2079f62283/d8218dc7-3455-49b4-bf7f-f3cebcca1ac3_800x800.jpeg.format.jpg",  
                            "inventoryDeductionWarehouseName": null,  
                            "goodsName": "Packaging Tape 72pcs. Baxi",  
                            "skuId": 78037408334151,  
                            "productList": [  
                                {  
                                    "productSkuId": 139696845689,  
                                    "soldFactor": 1,  
                                    "extCode": "",  
                                    "productId": 10574011393  
                                }  
                            ]  
                        }  
                    ]  
                }  
            ]  
        },  
        "success": true,  
        "errorCode": 0,  
        "serverTime": 1754811272339,  
        "errorMsg": "SUC"  
    },  
    "success": true,  
    "requestId": "gl-d280b860-e9cd-4eb6-a651-56a9bbd337e4",  
    "errorCode": 1000000,  
    "errorMsg": ""  
}
```

    1. 

`fulfillmentWarning `field returns `**RESTRICT_CALL_SHIPPING**`

```
{  
    "result": {  
        "result": {  
            "totalItemNum": 1,  
            "pageItems": [  
                {  
                    "parentOrderMap": {  
                        "parentOrderLabel": [  
                            {  
                                "name": "soon_to_be_overdue",  
                                "value": 0  
                            },  
                            {  
                                "name": "past_due",  
                                "value": 0  
                            },  
                            {  
                                "name": "pending_buyer_cancellation",  
                                "value": 0  
                            },  
                            {  
                                "name": "pending_buyer_address_change",  
                                "value": 0  
                            },  
                            {  
                                "name": "pending_risk_control_alert",  
                                "value": 0  
                            },  
                            {  
                                "name": "signature_required_on_delivery",  
                                "value": 0  
                            }  
                        ],  
                        "shippingMethod": 1,  
                        "parentShippingTime": null,  
                        "updateTime": 1754826878,  
                        "latestDeliveryTime": 1755658799,  
                        "fulfillmentWarning": [  
                            "RESTRICT_CALL_SHIPPING"  
                        ],  
                        "parentOrderTime": 1754825917,  
                        "orderPaymentType": "PPD",  
                        "batchOrderNumberList": null,  
                        "regionId": 29,  
                        "parentOrderPendingFinishTime": 1754826878,  
                        "parentOrderSn": "PO-029-06420938453110273",  
                        "siteId": 132,  
                        "expectShipLatestTime": 1754968559,  
                        "hasShippingFee": true,  
                        "parentOrderStatus": 2  
                    },  
                    "orderList": [  
                        {  
                            "canceledQuantityBeforeShipment": 0,  
                            "quantity": 1,  
                            "orderSn": "029-06420896510070273",  
                            "goodsId": 604407039143364,  
                            "orderLabel": [  
                                {  
                                    "name": "customized_products",  
                                    "value": 0  
                                },  
                                {  
                                    "name": "US_to_CA",  
                                    "value": 0  
                                }  
                            ],  
                            "inventoryDeductionWarehouseId": null,  
                            "orderStatus": 2,  
                            "originalGoodsName": "test",  
                            "fulfillmentType": "fulfillBySeller",  
                            "isCancelledDuringPending": false,  
                            "spec": "black",  
                            "fulfillmentWarning": [],  
                            "orderPaymentType": "PPD",  
                            "originalSpecName": "black",  
                            "originalOrderQuantity": 1,  
                            "thumbUrl": "https://img.kwcdn.com/local-image/s132/20ef5f1908/dc2378e4-1436-4054-a6df-dfc25d6424e7_900x900.jpeg.format.jpg",  
                            "goodsName": "Test",  
                            "inventoryDeductionWarehouseName": null,  
                            "skuId": 83019570350735,  
                            "productList": [  
                                {  
                                    "productSkuId": 158840640462,  
                                    "soldFactor": 1,  
                                    "extCode": "",  
                                    "productId": 62873718696  
                                }  
                            ]  
                        }  
                    ]  
                }  
            ]  
        },  
        "success": true,  
        "errorCode": 0,  
        "serverTime": 1754828814870,  
        "errorMsg": "SUC"  
    },  
    "success": true,  
    "requestId": "gl-ad6138a3-5b64-46b8-8774-ceec25dd82b9",  
    "errorCode": 1000000,  
    "errorMsg": ""  
}
```

### 

3. Change in Order Address Interface: Add return of consumer tax number information

a. Associated interfaces:[bg.order.shippinginfo.v2.get](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=ccc2f59661584f5e8e205d85ddb9a6c9)、[bg.order.decryptshippinginfo.get](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=001b8d067220423c9da40c8c3b4010be)

b. Changes: Return real phone number + virtual email + add return of four-level zoning address and `taxCode `(consumer CPF number)

c. Affected regions: Brazilian orders

d. Code demonstration:

```
{  
    "result": {  
        "regionName3": "Red",  
        "receiptAdditionalName": null,  
        "regionName4": "Meat",  
        "regionName1": "Brazil",  
        "mail": "qsblabp3ak12066@g.shipping.temuemail.com",  
        "regionName2": "Churrasco",  
        "mobile": "+55 1234232122",  
        "taxCode": "00412950995",  
        "addressLineAll": "1231sads2",  
        "receiptName": "ROSANA west",  
        "addressLine1": "1231sads2",  
        "backupMobile": null,  
        "postCode": "00000-001",  
        "addressLine2": "",  
        "addressLine3": null  
    },  
    "success": true,  
    "requestId": "gl-fe18b57d-8298-4da4-924a-fd9794835fd4",  
    "errorCode": 1000000,  
    "errorMsg": ""  
}
```

### 

4. When the order restrictions prevent the automatic shipment, calling the shipping interface will result in error interception

a. Associated interfaces: [bg.logistics.shipment.v2.confirm](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=27ff4f3d7b0b4c07862769d11f638ef0)、[bg.logistics.shipment.sub.confirm](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=4903f4955b2244329d78f9ee65785847)、[bg.logistics.shipment.shippingtype.update](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=ad80159112524d58aac61172246cd0f3)

b. Changes: Added error code 120015537, error message "`Brazil orders require Temu shipping labels exclusively`"

c. Affected regions: Brazil - restriction on self-shipped orders

d. Code demonstration

```
{  
    "success": false,  
    "requestId": "gl-103440e4-9b49-43aa-87d6-b67db60adb12",  
    "errorCode": 120015537,  
    "errorMsg": "Brazil orders require Temu shipping labels exclusively"  
}
```

### 

5. Change in the available channels interface for obtaining CALL forms: Add the mandatory field "`invoiceAccessKey`" to the channel acquisition interface, and disable the return of estimated amounts.

a. Changed interface: [bg.logistics.shippingservices.get](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=faf297e439f841009d417aabe52b7999)

b. Changed content:

i. For call form orders, intercept errors when attempting to place a new call;

ii. Obtain recommended channels and add the mandatory field `invoiceAccessKey` when placing a call. Only after verification is passed will the estimated channel and successful call channel be returned;

iii. No longer return channel quotation information for recommendations.

c. Affected regions: Brazil - restrict self-fulfillment orders.

d. Code demonstration

i. When obtaining available logistics providers for call form orders, intercept errors when attempting to place a new call.

```
{  
    "success": false,  
    "requestId": "gl-6472fdc3-cd6a-48b3-a5c6-962f98f840cf",  
    "errorCode": 120015538,  
    "errorMsg": "Brazil orders are restricted to using exclusively TEMU platform shipping labels for self-fulfillment"  
}
```

    1. 

Obtaining available logistics providers failed as the required parameter` [invoiceAccessKey]` was not provided or the validation of this field was unsuccessful, resulting in an error interception.

```
{  
    "success": false,  
    "requestId": "gl-48901c97-29e1-446b-8fb0-10b754e9b29d",  
    "errorCode": 120011094,  
    "errorMsg": "The necessary parameter invoiceAccessKey is missing"  
}
```

```
{  
    "success": false,  
    "requestId": "gl-d1409d73-bc5d-4059-8a6c-ad1733e431ea",  
    "errorCode": 120011088,  
    "errorMsg": "Invoice access key verification failed. Please check if the invoiceAccessKey is valid"  
}
```

    1. 

The "`estimatedAmount`" field returned by the available logistics provider is NULL.

```
{  
    "result": {  
        "unavailableChannelDtoList": [],  
        "onlineChannelDtoList": [  
            {  
                "estimatedText": "7-18 work days,",  
                "estimatedCurrencyCode": null,  
                "infoNeeded": null,  
                "signServiceName": null,  
                "shipCompanyId": 202398511,  
                "pickupRules": null,  
                "availablePickupTimeSlotList": null,  
                "signServiceId": null,  
                "shipLogisticsType": "PICKUP",  
                "shippingCompanyName": "J&T express",  
                "estimatedAmount": null,  
                "channelId": 897039159485005824,  
                "payWayCode": null  
            }  
        ]  
    },  
    "success": true,  
    "requestId": "gl-75d77fc0-bd23-4635-a954-b92994771db1",  
    "errorCode": 1000000,  
    "errorMsg": ""  
}
```

### 

6.Changes to the CALL and RECALL interfaces: Added the mandatory field` invoiceAccessKey`

  1. 

Change of interface：[bg.logistics.shipment.create](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=0af17643465346f9b72bd7478b2a8254)、[bg.logistics.shipment.update](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=e698d355abd641119dd3f5f44d60804a)、[bg.logistics.shipment.result.get](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=122ba56121114e4ba72292fafe0ff509)

  1. 

 Changes

i. Restrict call order forms and intercept with error messages when making a new Buy-shipping on TEMU;

ii. Obtain recommended channels and add the mandatory "`invoiceAccessKey`" field when making a call. Only after verification is passed will the estimated channel and successful call channel be returned;

iii. Support re-calling after a successful call.

c. Affected areas: Brazil - restrict self-fulfillment orders.

d. Code example

i. Restrict call order forms and intercept when making a Temu order call.

```
{  
    "success": false,  
    "requestId": "gl-0c778ff6-f3a5-4cb4-82ea-f574811dca0d",  
    "errorCode": 120015538,  
    "errorMsg": "Brazil orders are restricted to using exclusively TEMU platform shipping labels for self-fulfillment"  
}
```

    1. 

The required field [invoiceAccessKey] is missing or the validation of this field fails, resulting in an error interception.

```
{  
    "success": false,  
    "requestId": "gl-b8e3aab3-5a2a-450a-ab7c-ea842e542af8",  
    "errorCode": 120011094,  
    "errorMsg": "The necessary parameter invoiceAccessKey is missing"  
}
```

```
{  
    "success": false,  
    "requestId": "gl-c3fc79f3-9417-41a4-a159-33ddb58a3ab4",  
    "errorCode": 120011088,  
    "errorMsg": "Invoice access key verification failed. Please check if the invoiceAccessKey is valid"  
}
```

    1. 

Without obtaining the available channels, proceed with the call and encounter error interception.

    1. 

Successful call demonstration

      1. 

request

```
request  
{  
    "type": "bg.logistics.shipment.create",  
    "timestamp": 1754292122,  
    "app_key": "demo-0190292bdc8f6f84230974904bs",  
    "data_type": "JSON",  
    "access_token": "utl2xdsktba0vj7b1yro62cvlugaksy87hkjsgpwld6jtyyo3na0sl9m7rv",  
    "sendType": 0,  
    "shipLater": true,  
    "sendRequestList": [  
        {  
            "orderSendInfoList": [  
                {  
                    "parentOrderSn": "PO-029-18238241505913274",  
                    "orderSn": "029-18238283448953274",  
                    "quantity": 1  
                }  
            ],  
            "warehouseId": "WH-06397197516951276",  
            "weight": "1",  
            "weightUnit": "kg",  
            "length": "5",  
            "width": "5",  
            "height": "5",  
            "dimensionUnit": "cm",  
            "channelId": 640131572895744,  
            "shipCompanyId": 202398511,  
            "invoiceAccessKey": "35250557643824000105550010000005531177558229"  
        }  
    ],  
    "sign": "CF99234C8F8FE205C6643603F27848CC"  
}
```

      1. 

response

```
{  
    "result": {  
        "warningMessage": null,  
        "packageSnList": [  
            "PK-A240711840563991276"  
        ],  
        "shipLaterLimitTime": "48"  
    },  
    "success": true,  
    "requestId": "gst-c045d1aa-976f-4fab-952b-46fdcac5b258",  
    "errorCode": 1000000,  
    "errorMsg": ""  
}
```

    1. 

Successful Recall demonstration

      1. 

request

```
{  
    "type": "bg.logistics.shipment.update",  
    "timestamp": 1754988854,  
    "app_key": "f9d5cc9313893a20d5aa85c654e8f503",  
    "data_type": "JSON",  
    "access_token": "gpl0trbmelr8bp7ubcldzeuloe1atvxqpnpfx8ozuwvitk5j18vftvsnk0y",  
    "retrySendPackageRequestList": [  
        {  
            "packageSn": "PK-0592545917174551592",  
            "orderSendInfoList": [  
                {  
                    "parentOrderSn": "PO-029-06420954181750273",  
                    "orderSn": "029-06420912238710273",  
                    "quantity": 1  
                }  
            ],  
            "warehouseId": "WH-02274030100631592",  
            "weight": "1",  
            "weightUnit": "kg",  
            "length": "1",  
            "width": "1",  
            "height": "1",  
            "dimensionUnit": "cm",  
            "channelId": 897039159485005824,  
            "shipCompanyId": 202398511,  
            "invoiceAccessKey": "36250557643824000105550010000005531177558999",  
            "confirmAcceptance": [  
                "SUCCESSFUL_RETRY"  
            ]  
        }  
    ],  
    "sign": "CBA33DA90E8C29FE932887F8D8ADD765"  
}
```

    1. 

response

```
{  
    "result": true,  
    "success": true,  
    "requestId": "gl-7a5aede2-ae69-4c2c-8190-e39e0b2b1c7c",  
    "errorCode": 1000000,  
    "errorMsg": ""  
}
```

### 

7.Change in the call result interface: Add the returned field` invoiceAccessKey`

  1. 

Change of interface：[bg.logistics.shipment.result.get](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=122ba56121114e4ba72292fafe0ff509)

  1. 

Changes

i. Added return field `invoiceAccessKey` to the output parameters

e. Affected regions: Brazil has restrictions on self-fulfillment orders

f. Code demonstration

```
  
{  
    "result": {  
        "packageInfoResultList": [  
            {  
                "estimatedText": "7-18 work days",  
                "estimatedCurrencyCode": "USD",  
                "extendWeight": null,  
                "packageDeliveryType": 2,  
                "dimensionUnit": "cm",  
                "solutionText": null,  
                "warehouseName": "巴西dhkhk",  
                "failReasonText": "Please check if the package information is correct and try again, or confirm shipment instead",  
                "subPackageSnList": [],  
                "reservationSn": null,  
                "mainPackageSn": "PK-5166520113562391592",  
                "isConfirmAfterPickup": false,  
                "signServiceId": null,  
                "shipLogisticsType": "PICKUP",  
                "subPackageType": "MAIN",  
                "trackingNumber": "",  
                "channelId": 897039159485005824,  
                "height": "5",  
                "invoiceAccessKey": "35250557643824000105550010000005531177558229",  
                "extendWeightUnit": null,  
                "pickupStartTime": null,  
                "shippingLabelStatus": 2,  
                "canChangeToManualSend": true,  
                "pickupEndTime": null,  
                "packageSn": "PK-5166520113562391592",  
                "length": "5",  
                "weight": "1",  
                "warningMessage": null,  
                "shipCompanyId": 202398511,  
                "warehouseId": "WH-02274030100631592",  
                "width": "5",  
                "orderSendInfoList": [  
                    {  
                        "quantity": 1,  
                        "orderSn": "029-06420912238710273",  
                        "parentOrderSn": "PO-029-06420954181750273",  
                        "goodsId": 604422071509424,  
                        "skuId": 78037408334151  
                    }  
                ],  
                "shippingCompanyName": "J&T express",  
                "estimatedAmount": NULL,  
                "weightUnit": "kg"  
            }  
        ]  
    },  
    "success": true,  
    "requestId": "gl-56e89d98-10ce-4bb3-8665-86764099c09c",  
    "errorCode": 1000000,  
    "errorMsg": ""  
}
```
