# Split and ship a package examples

Order fulfillment supports two primary approaches: **Buy Shipping** and **Self-Fulfilled Shipments**.

- 

With **Buy Shipping**, sellers use platform-generated shipping labels to complete delivery.

- 

With **Self-Fulfilled Shipments**, sellers manage shipping independently using their own logistics providers.

This document provides concrete **examples** demonstrating how to split an order into multiple packages under each fulfillment approach, including two scenarios for Buy Shipping and two scenarios for Self-Fulfilled Shipments. For a comprehensive explanation of rules, constraints, and end-to-end workflows, please refer to the [**Order Fulfillment Guide**](https://partner-us.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=f34f5859554e4c06a69727942afdbade).

### 

**Buy Shipping **

#### 

Scenario 1: Multiple items in one or more parent orders, and I want to split them into multiple packages.

Original Order

![image](https://bstatic.kwcdn.com/open-outer/21a4885502/be3335faedcb7066b1e98278755047a7.png)

Request Example

```
{  
  "app_key": "4ebbc9190ae410443d65b4c2faca981f",  
  "access_token": "uplv3hfyt5kcwoymrgnajnbl1ow5qxlz4sqhev6hl3xosz5dejrtyl2jre7",  
  "data_type": "JSON",  
  "timestamp": 1767097533,  
  "type": "bg.logistics.shipment.create",  
  "version": "V1",  
  "shipLater": true,  
  "sendType": 1,  
  "sendRequestList": [  
    {  
      "extendWeightUnit": "oz",  
      "extendWeight": "1",  
      "length": "1",  
      "dimensionUnit": "in",  
      "weight": "1",  
      "shipCompanyId": 998264938,  
      "warehouseId": "WH-03541043302552414",  
      "width": "1",  
      "shipLogisticsType": "Standard",  
      "channelId": 684244464201728,  
      "weightUnit": "lb",  
      "height": "1",  
      "orderSendInfoList": [  
        {  
          "quantity": 1,  
          "orderSn": "211-19373803543673450",  
          "parentOrderSn": "PO-211-19373740629113450",  
          "goodsId": 602368171198347,  
          "skuId": 37386079732361  
        }  
      ]  
    },  
    {  
      "extendWeightUnit": "oz",  
      "extendWeight": "1",  
      "length": "1",  
      "dimensionUnit": "in",  
      "weight": "1",  
      "shipCompanyId": 998264938,  
      "warehouseId": "WH-03541043302552414",  
      "width": "1",  
      "shipLogisticsType": "Standard",  
      "channelId": 684244464201728,  
      "weightUnit": "lb",  
      "height": "1",  
      "orderSendInfoList": [  
        {  
          "quantity": 2,  
          "orderSn": "211-19373803543673450",  
          "parentOrderSn": "PO-211-19373740629113450",  
          "goodsId": 602368171198347,  
          "skuId": 37386079732361  
        }  
      ]  
    }  
  ],  
  "sign": "B798170D01600467CD0269D3C5884FE1"  
}
```

Response

```
{  
    "result": {  
        "packageSnList": [  
            "PK-0878421204009732414",  
            "PK-0878442678846212414"  
        ],  
        "warningMessage": null,  
        "shipLaterLimitTime": "48"  
    },  
    "success": true,  
    "requestId": "us-f056872f-5ad5-4cbb-ab94-f3eda5e76fad",  
    "errorCode": 1000000,  
    "errorMsg": ""  
}
```

Result

![image](https://bstatic.kwcdn.com/open-outer/21a4885502/99d774f631f4c79648380dc2b5d8bb43)

#### 

Scenario 2:  I have only one item, but it is too large or consists of multiple parts, so I need to split it into multiple packages.

Original Order

![image](https://bstatic.kwcdn.com/open-outer/21a4885502/629df10fb54be7fcb1515dda856879c3.png)

Request Example

```
{  
  "app_key": "4ebbc9190ae410443d65b4c2faca981f",  
  "access_token": "uplv3hfyt5kcwoymrgnajnbl1ow5qxlz4sqhev6hl3xosz5dejrtyl2jre7",  
  "data_type": "JSON",  
  "timestamp": 1767100614,  
  "type": "bg.logistics.shipment.create",  
  "version": "V1",  
  "shipLater": true,  
  "sendType": 1,  
  "sendRequestList": [  
    {  
      "extendWeightUnit": "oz",  
      "extendWeight": "1",  
      "length": "1",  
      "dimensionUnit": "in",  
      "weight": "1",  
      "shipCompanyId": 998264938,  
      "warehouseId": "WH-03541043302552414",  
      "width": "1",  
      "shipLogisticsType": "Standard",  
      "channelId": 684244464201728,  
      "weightUnit": "lb",  
      "height": "1",  
      "orderSendInfoList": [  
        {  
          "quantity": 1,  
          "orderSn": "211-19373806759033450",  
          "parentOrderSn": "PO-211-19373712387193450",  
          "goodsId": 602368171198347,  
          "skuId": 37386079732361  
        }  
      ],  
      "splitSubPackage": true,  
      "sendSubRequestList": [  
        {  
          "extendWeightUnit": "oz",  
          "extendWeight": "1",  
          "length": "1",  
          "dimensionUnit": "in",  
          "weight": "1",  
          "shipCompanyId": 998264938,  
          "warehouseId": "WH-03541043302552414",  
          "width": "1",  
          "shipLogisticsType": "Standard",  
          "channelId": 684244464201728,  
          "weightUnit": "lb",  
          "height": "1"  
        }  
      ]  
    }  
  ],  
  "sign": "6DE383E9F40C1E31CC22B8FD54357837"  
}
```

Response

```
{  
    "result": {  
        "warningMessage": null,  
        "packageSnList": [  
            "PK-0878417535959812414",  
            "PK-0878439010796292414"  
        ],  
        "shipLaterLimitTime": "48"  
    },  
    "success": true,  
    "requestId": "us-f45341cb-5a28-4473-9951-64c140be8bb1",  
    "errorCode": 1000000,  
    "errorMsg": ""  
}
```

Result

![image](https://bstatic.kwcdn.com/open-outer/21a4885502/5aa82a522f4ca0e84de27ec4c05d5060)

### 

**Self-Fulfilled Shipments**

#### 

Scenario 1: There are multiple items under one parent orders, and they are shipped in multiple packages with different tracking numbers.

Original Order

![image](https://bstatic.kwcdn.com/open-outer/21a4885502/e69635401f669c6ea79477985b8c3b3c.png)

Request Example

```
{  
  "app_key": "4ebbc9190ae410443d65b4c2faca981f",  
  "access_token": "uplv3hfyt5kcwoymrgnajnbl1ow5qxlz4sqhev6hl3xosz5dejrtyl2jre7",  
  "data_type": "JSON",  
  "timestamp": 1768189927,  
  "type": "bg.logistics.shipment.v2.confirm",  
  "version": "V1",  
  "sendRequestList": [  
    {  
      "orderSendInfoList": [  
        {  
          "quantity": 1,  
          "orderSn": "211-03568305731193450",  
          "parentOrderSn": "PO-211-03568242816633450",  
          "goodsId": 602368171198347,  
          "skuId": 37386079732361  
        }  
      ],  
      "selfShippingWarehouseId": "WH-04024228864152414",  
      "carrierId": 998264743,  
      "trackingNumber": "AAAstwbsn1767818982181269"  
    },  
    {  
      "orderSendInfoList": [  
        {  
          "quantity": 1,  
          "orderSn": "211-03568305731193450",  
          "parentOrderSn": "PO-211-03568242816633450",  
          "goodsId": 602368171198347,  
          "skuId": 37386079732361  
        }  
      ],  
      "selfShippingWarehouseId": "WH-04024228864152414",  
      "carrierId": 998264743,  
      "trackingNumber": "BBBstwbsn1767818982181269"  
    }  
  ],  
  "sendType": 1,  
  "sign": "78D868729C113975C644FD07962DDE96"  
}
```

Response

```
{  
    "result": {  
        "assistantAgreementText": null,  
        "warningMessage": []  
    },  
    "success": true,  
    "requestId": "us-30a4269b-67f6-4e03-95a5-bd6afb68a310",  
    "errorCode": 1000000,  
    "errorMsg": “"  
}
```

Result

![image](https://bstatic.kwcdn.com/open-outer/21a4885502/7a117c49d2761a87d3f5a9be6568292a)

### 

#### 

Scenario 2: For one parent order, there is only one line item. Because the item is too large, it is split into two packages, and two shipping labels are purchased—one for each package.

Original Order

![image](https://bstatic.kwcdn.com/open-outer/21a4885502/0d85662576bb22bd1a56abfb366716ab.png)

Request Example

```
{  
  "app_key": "4ebbc9190ae410443d65b4c2faca981f",  
  "access_token": "uplv3hfyt5kcwoymrgnajnbl1ow5qxlz4sqhev6hl3xosz5dejrtyl2jre7",  
  "data_type": "JSON",  
  "timestamp": 1767967820,  
  "type": "bg.logistics.shipment.v2.confirm",  
  "version": "V1",  
  "sendRequestList": [  
    {  
      "orderSendInfoList": [  
        {  
          "quantity": 1,  
          "orderSn": "211-07092887880312890",  
          "parentOrderSn": "PO-211-07092877394552890",  
          "goodsId": 602368171198347,  
          "skuId": 37386079732361  
        }  
      ],  
      "selfShippingWarehouseId": "WH-04024228864152414",  
      "subSendRequests": [  
        {  
          "carrierId": 998264743,  
          "trackingNumber": "FTEstwbsn1767818982181268",  
          "selfShippingWarehouseId": "WH-04024228864152414"  
        }  
      ],  
      "carrierId": 998264743,  
      "trackingNumber": "AAAstwbsn1767818982181269"  
    }  
  ],  
  "sendType": 1,  
  "sign": "2C5EFE5352301B5238A25AF7D005DD48"  
}
```

Response

```
{  
    "result": {  
        "assistantAgreementText": null,  
        "warningMessage": []  
    },  
    "success": true,  
    "requestId": "us-999540ca-d142-4c3b-975f-0984b53a8126",  
    "errorCode": 1000000,  
    "errorMsg": ""  
}
```

Result

![image](https://bstatic.kwcdn.com/open-outer/21a4885502/3a486cbeb8d6551bb12f49497dedc266)
