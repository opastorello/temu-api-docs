# Parent-child Attribute Guide

**Last update:** 2026-01-25 00:29:45

---

## 
**Parent-child Attributes**

Parent-child relationships are defined by the `showType` field:

- 
`showType = 0`: Parent attribute.

- 
`showType = 1`: Child attribute.

- 
Child attributes appear based on the `controlType` of the parent attribute. If `controlType = 0`, `showCondition` will indicate the conditions under which child attributes are triggered based on parent attribute values.

- 
If `controlType` is `1`, `3`, or `16`, the `templatePropertyValueParentList` will determine when child attributes are triggered.

For example, the "Fabric Weight 1 (g/m²)" attribute with `controlType = 0` indicates that the value must be inputted. If `required = true`, it must be provided. `showType = 1` indicates it is a child attribute, and you should check the `showCondition` to see if the parent attribute, identified by `parentRefPid = 6926`, has selected one of the `parentVids` values (e.g., `parentVids = [161198]`). If the condition is met, the child attribute should be assembled according to `controlType = 0`.

For details on product attributes, refer to the [Product Attributes](https://partner.temu.com/documentation?menu_code=38e79b35d2cb463d85619c1c786dd303&sub_menu_code=c1bf67656f404183997c74675c635087).

## 
**API Call Process**

### 
**Overview**

## 
Example

### 
**From UI perspective**

Power Supply is a Parent attribute.

If sellers choose Battery Powered (with Plug)

Child attributes Operating Voltage & Plug Type appeared and they are mandatory.

### 
**From API perspective**

Query bg.local.goods.template.get

```
{
  "app_key": "4ebbc9190ae410443d65b4c2faca981f",
  "data_type": "JSON",
  "access_token": "uplv3hfyt5kcwoymrgnajnbl1ow5qxlz4sqhev6hl3xosz5dejrtyl2jre7",
  "timestamp": 1768725666,
  "type": "bg.local.goods.template.get",
  "version": "1.0",
  "catId": 14599,
  "sign": "BC1268F6732367701093E7A2959FF73D"
}
```

Result

#### 
**"Power Supply" Attribute**

```
{
  "chooseMaxNum": 1,
  "controlType": 1,
  "feature": 0,
  "isSale": false,
  "mainSale": null,
  "maxValue": "",
  "minValue": "",
  "name": "Power Supply",
  "numberInputTitle": null,
  "parentSpecId": null,
  "parentTemplatePid": 0,
  "pid": 1425,
  "propertyChooseTitle": null,
  "propertyValueType": 0,
  "refPid": 1561,
  "referenceType": null,
  "required": true,
  "showCondition": null,
  "showType": 0,
  "templateModuleId": 20359,
  "templatePid": 891917,
  "templatePropertyValueParentList": null,
  "transnationalAttribute": null,
  "valuePrecision": 0,
  "valueRule": 0,
  "valueUnitList": null,
  "values": [
    {
      "additionalInfo": null,
      "brandId": null,
      "extendInfo": null,
      "group": null,
      "parentVids": null,
      "specId": null,
      "subGroup": null,
      "value": "Use Without Electricity",
      "vid": 36627
    },
    {
      "additionalInfo": null,
      "brandId": null,
      "extendInfo": null,
      "group": null,
      "parentVids": null,
      "specId": null,
      "subGroup": null,
      "value": "Plug Powered",
      "vid": 36781
    },
    {
      "additionalInfo": null,
      "brandId": null,
      "extendInfo": null,
      "group": null,
      "parentVids": null,
      "specId": null,
      "subGroup": null,
      "value": "Solar Charging",
      "vid": 36782
    },
    {
      "additionalInfo": null,
      "brandId": null,
      "extendInfo": null,
      "group": null,
      "parentVids": null,
      "specId": null,
      "subGroup": null,
      "value": "Battery Powered (with Plug)",
      "vid": 36789
    },
    {
      "additionalInfo": null,
      "brandId": null,
      "extendInfo": null,
      "group": null,
      "parentVids": null,
      "specId": null,
      "subGroup": null,
      "value": "Battery Powered (no Plug)",
      "vid": 36790
    },
    {
      "additionalInfo": null,
      "brandId": null,
      "extendInfo": null,
      "group": null,
      "parentVids": null,
      "specId": null,
      "subGroup": null,
      "value": "USB Powered",
      "vid": 36791
    },
    {
      "additionalInfo": null,
      "brandId": null,
      "extendInfo": null,
      "group": null,
      "parentVids": null,
      "specId": null,
      "subGroup": null,
      "value": "Hard-Wired",
      "vid": 36792
    },
    {
      "additionalInfo": null,
      "brandId": null,
      "extendInfo": null,
      "group": null,
      "parentVids": null,
      "specId": null,
      "subGroup": null,
      "value": "DC Power Supply",
      "vid": 69104
    }
  ]
}
```

 

"Power Supply Attribute" Breakdown

```
"isSale": false, This is a normal attribute.
"required": true, This is a mandatory attribute.
"showType": 0, This is a Parent attribute
"controlType": 1, This is a Select type property
"chooseMaxNum": 1, Can only choose one value from values
"values": [
...
]
```

Assemble attribute objects in bg.local.goods.add -> goodsProperty. goodsProperties

```
{
    “templatePid": 891917,
    “refPid": 1561,
    “pid": 1425,
    "vid": 36789,
    “value": "Battery Powered (with Plug)"
}
```

Please note not all parent attributes would have a child attribute, it depends on the value you select.

For example, if sellers select “Solar Charging” for “Power Supply”, there is no child attribute.

#### 
**"Operating Voltage” Attribute**

```
{
  "chooseMaxNum": 1,
  "controlType": 1,
  "feature": 0,
  "isSale": false,
  "mainSale": null,
  "maxValue": "",
  "minValue": "",
  "name": "Operating Voltage",
  "numberInputTitle": null,
  "parentSpecId": null,
  "parentTemplatePid": 891917,
  "pid": 1155,
  "propertyChooseTitle": null,
  "propertyValueType": 0,
  "refPid": 1132,
  "referenceType": null,
  "required": true,
  "showCondition": null,
  "showType": 1,
  "templateModuleId": 20359,
  "templatePid": 892359,
  "templatePropertyValueParentList": [
    {
      "parentVids": [
        69104
      ],
      "vids": [
        28317
      ]
    },
    {
      "parentVids": [
        36789
      ],
      "vids": [
        46117,
        52830,
        52831,
        36204,
        36205,
        36649,
        36650,
        36651,
        63031
      ]
    },
    {
      "parentVids": [
        36781
      ],
      "vids": [
        46117,
        52830,
        52831,
        36204,
        36205,
        36649,
        36650,
        36651
      ]
    }
  ],
  "transnationalAttribute": null,
  "valuePrecision": 0,
  "valueRule": 0,
  "valueUnitList": null,
  "values": [
    {
      "additionalInfo": null,
      "brandId": null,
      "extendInfo": null,
      "group": null,
      "parentVids": [
        36789
      ],
      "specId": null,
      "subGroup": null,
      "value": "125V",
      "vid": 63031
    },
    {
      "additionalInfo": null,
      "brandId": null,
      "extendInfo": null,
      "group": null,
      "parentVids": [
        36781,
        36789
      ],
      "specId": null,
      "subGroup": null,
      "value": "110V (included)-240V (included)",
      "vid": 36649
    },
    {
      "additionalInfo": null,
      "brandId": null,
      "extendInfo": null,
      "group": null,
      "parentVids": [
        36781,
        36789
      ],
      "specId": null,
      "subGroup": null,
      "value": "110V",
      "vid": 36650
    },
    {
      "additionalInfo": null,
      "brandId": null,
      "extendInfo": null,
      "group": null,
      "parentVids": [
        36781,
        36789
      ],
      "specId": null,
      "subGroup": null,
      "value": "120V",
      "vid": 36651
    },
    {
      "additionalInfo": null,
      "brandId": null,
      "extendInfo": null,
      "group": null,
      "parentVids": [
        36781,
        36789
      ],
      "specId": null,
      "subGroup": null,
      "value": "110V (included)-130V (included)",
      "vid": 36204
    },
    {
      "additionalInfo": null,
      "brandId": null,
      "extendInfo": null,
      "group": null,
      "parentVids": [
        69104
      ],
      "specId": null,
      "subGroup": null,
      "value": "≤36V",
      "vid": 28317
    },
    {
      "additionalInfo": null,
      "brandId": null,
      "extendInfo": null,
      "group": null,
      "parentVids": [
        36781,
        36789
      ],
      "specId": null,
      "subGroup": null,
      "value": "100V (inclusive)-127V (inclusive)",
      "vid": 52830
    },
    {
      "additionalInfo": null,
      "brandId": null,
      "extendInfo": null,
      "group": null,
      "parentVids": [
        36781,
        36789
      ],
      "specId": null,
      "subGroup": null,
      "value": "110V (inclusive)-127V (inclusive)",
      "vid": 52831
    }
  ]
}
```

"Operating Voltage” Breakdown

```
{
  "chooseMaxNum": 1,  Can only choose one value from values
  "controlType": 1, Child attributes appear based on the controlType of the parent attribute, If controlType is 1, 3, or 16, the templatePropertyValueParentList will determine when child attributes are triggered.
  "isSale": false,
  "name": "Operating Voltage",
  "parentTemplatePid": 891917, This is its parent attribute -> "Power Supply", which  "templatePid" is 891917,
  "pid": 1155,
  "propertyValueType": 0,
  "refPid": 1132,
  "required": true,
  "showType": 1,    This is a Child attribute
  "templateModuleId": 20359,
  "templatePid": 892359,
  "templatePropertyValueParentList": [
    
    ...
    ,
    {
      "parentVids": [
        36789        When the parent attribute chooses value "36789", this Child attribute "Operating Voltage" is triggered and if "required": true, it must be passed in goodsProperty.goodsProperties
      ],
      "vids": [
        46117,
        52830,
        52831,
        36204,
        36205,
        36649,
        36650,
        36651,
        63031
      ]
    },
    ...
  ],
  "values": [
    {
      ...
    }
  ]
}
```

Assemble attribute objects in bg.local.goods.add -> goodsProperty. goodsProperties

```
{
    “templatePid": 891917,
    “refPid": 1561,
    “pid": 1425,
    "vid": 36789,
    “value": "Battery Powered (with Plug)"
}
```

#### 
**"Plug Type" Attribute**

```
{
  "chooseMaxNum": 1,  Can only choose one value from values
  "controlType": 1, Child attributes appear based on the controlType of the parent attribute, If controlType is 1, 3, or 16, the templatePropertyValueParentList will determine when child attributes are triggered.
  "isSale": false,
  "name": "Plug Type",
  ...,
  "parentTemplatePid": 891917, This is its parent attribute -> "Power Supply", which  "templatePid" is 891917
  "pid": 1404,
  "refPid": 1485,
  "required": true,
  "showType": 1, This is a Child attribute
  "templateModuleId": 20359,
  "templatePid": 892360,
  "templatePropertyValueParentList": [
    {
      "parentVids": [
        36789.   When the parent attribute chooses value "36789", this Child attribute "Plug Type" is triggered and if "required": true, it must be passed in goodsProperty.goodsProperties 
      ],
      "vids": [
        36261,
        36262,
        36263,
        36264,
        46457,
        55512,
        55513,
        55495
      ]
    },
    {
      "parentVids": [
        36781
      ],
      "vids": [
        36261,
        36262,
        36263,
        36264,
        46457,
        55512,
        55513,
        55495,
        199366,
        199640
      ]
    }
  ],
   ...,
  "values": [
    {
      "additionalInfo": null,
      "brandId": null,
      "extendInfo": null,
      "group": null,
      "parentVids": [
        36789,
        36781
      ],
      "specId": null,
      "subGroup": null,
      "value": "US Plug",
      "vid": 36261
    }
  ]
}
```

Assemble attribute objects in bg.local.goods.add -> goodsProperty. goodsProperties

```
{
    "templatePid": 892360,
    "refPid": 1485,
    "pid": 1404,
    “vid": 36261,
    “value":"US Plug"
}
```

#### 
**If other required Child Attribute needs to be passed? **

Take "Acceptable Voltage Range" as an example

```
{
  "chooseMaxNum": 1,
  "controlType": 1,
  "isSale": false,
  "name": "Acceptable Voltage Range",
  "parentTemplatePid": 891917,
  "pid": 1432,
  "propertyValueType": 0,
  "refPid": 1571,
  "required": true,       Required is true, it's a child attribute, parent attribute 891917 "Power Supply" is selected, 
  "showType": 1,
  "templateModuleId": 20359,
  "templatePid": 892361,
  "templatePropertyValueParentList": [
    {
      "parentVids": [
        36792            however, 36792 "Hard-Wired" is not selected by parent attribute "Power Supply". So this "Acceptable Voltage Range" shouldn't be passed in  goodsProperty. goodsProperties
      ], 
      "vids": [
        36895,
        36896,
        46145,
        52832,
        47126,
        52833,
        46104,
        47128,
        46174,
        47121,
        47122,
        47124,
        47125,
        47127
      ]
    }
  ],
  "transnationalAttribute": null,
  "valuePrecision": 0,
  "valueRule": 0,
  "valueUnitList": null,
  "values": [
    {
      "additionalInfo": null,
      "brandId": null,
      "extendInfo": null,
      "group": null,
      "parentVids": [
        36792
      ],
      "specId": null,
      "subGroup": null,
      "value": "50-80V",
      "vid": 36896
    },
    {
      "additionalInfo": null,
      "brandId": null,
      "extendInfo": null,
      "group": null,
      "parentVids": [
        36792
      ],
      "specId": null,
      "subGroup": null,
      "value": "110 V-240 V",
      "vid": 47121
    },
    {
      "additionalInfo": null,
      "brandId": null,
      "extendInfo": null,
      "group": null,
      "parentVids": [
        36792
      ],
      "specId": null,
      "subGroup": null,
      "value": "110 V",
      "vid": 47124
    },
    {
      "additionalInfo": null,
      "brandId": null,
      "extendInfo": null,
      "group": null,
      "parentVids": [
        36792
      ],
      "specId": null,
      "subGroup": null,
      "value": "120 V",
      "vid": 47125
    },
    {
      "additionalInfo": null,
      "brandId": null,
      "extendInfo": null,
      "group": null,
      "parentVids": [
        36792
      ],
      "specId": null,
      "subGroup": null,
      "value": "110 V-130 V",
      "vid": 46104
    },
    {
      "additionalInfo": null,
      "brandId": null,
      "extendInfo": null,
      "group": null,
      "parentVids": [
        36792
      ],
      "specId": null,
      "subGroup": null,
      "value": "110V-220V",
      "vid": 46174
    },
    {
      "additionalInfo": null,
      "brandId": null,
      "extendInfo": null,
      "group": null,
      "parentVids": [
        36792
      ],
      "specId": null,
      "subGroup": null,
      "value": "Below 50 V",
      "vid": 36895
    }
  ]
}
```

Required is true, it's a child attribute, and parent attribute 891917 "Power Supply" is selected, however, 36792 "Hard-Wired" is not selected by parent attribute "Power Supply". 

So this "Acceptable Voltage Range" shouldn't be passed in goodsProperty. goodsProperties
