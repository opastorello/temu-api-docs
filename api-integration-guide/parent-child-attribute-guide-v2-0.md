# Parent-child Attribute Guide V2.0

### 

**Parent-child Attributes**

When sellers select a value from a parent attribute, the available child attributes and the selectable values for those child attributes are determined by the selected value from the parent attribute.

Even if the same child attribute appears under different values from the parent attribute, the range of selectable values of the child attribute may differ.

### 

**From UI perspective:**

![image](https://bstatic.kwcdn.com/open-outer/212a0c49b4/0713c395ca3b500e69d0c6a8790e6255.png)

**Material** is a **parent attribute** and is **mandatory**.

- 

When the seller selects **“Wood”**, the child attribute **“Wood Type”** will appear.

- 

If the seller further selects **“Log”**, another child attribute **“Wood Species”** will appear.

Please note:

- 

Child attributes can be skipped if they are **not marked as mandatory**.

- 

If a child attribute is marked as **mandatory** (`required: true`), it **must be selected** before submitting the product.

### 

**From API perspective:**

Query temu.local.product.attributes.get

```
{  
    "type": "temu.local.product.attributes.get",  
    "catId": 24318  
}
```

Result

![image](https://bstatic.kwcdn.com/open-outer/212a0c49b4/0b7b39721f880b76ee0c7e7b9803bf8a.png)

Category 24318 includes 3 attributes. Please ensure that all attributes marked with `required = true` are filled in when creating or updating a product.

#### 

**"Material" Attribute**

```
{  
  "attributeName": "Material",  
  "attributeRules": {  
    "attributeValueRules": {  
      "maxValue": "",  
      "minValue": "",  
      "numberInputTitle": null,  
      "propertyChooseTitle": null,  
      "valuePrecision": 0,  
      "valueRule": 0  
    },  
    "chooseMaxNum": 1,  
    "controlType": 1,  
    "transnationalAttribute": null  
  },  
  "attributeValueDetail": [  
    {  
      "attributeValueList": [  
        {  
          "childAttribute": [],  
          "value": "Aluminum Alloy",  
          "vid": 66  
        },  
        {  
          "childAttribute": [],  
          "value": "Stainless Steel",  
          "vid": 381  
        },  
        {  
          "childAttribute": [  
            {  
              "childAttributeId": 7317,  
              "childAttributeValueGroupId": "12-7317-0"  
            }  
          ],  
          "value": "Wood",  
          "vid": 410  
        },  
        {  
          "childAttribute": [],  
          "value": "ABS",  
          "vid": 26485  
        },  
        {  
          "childAttribute": [],  
          "value": "Acrylic",  
          "vid": 1145  
        },  
        ...  
        ...,  
        {  
          "childAttribute": [],  
          "value": "Carbon-fiber",  
          "vid": 26619  
        },  
        {  
          "childAttribute": [],  
          "value": "Polyester",  
          "vid": 26042  
        }  
      ],  
      "groupId": null  
    }  
  ],  
  "attributeValueUnitList": null,  
  "refPid": 12,  
  "required": true  
}
```

"Material" attribute Breakdown

```
"required": true, This is a mandatory attribute.  
"controlType": 1, This is a Select type attribute  
"chooseMaxNum": 1, Can only choose one value from attributeValueList  
"refPid": 12, Attribute ID 
```

Assemble attribute objects in temu.local.goods.add -> goodsProperty

```
{  
    "refPid": 12,  
    "vid": 410  
}
```

Please note not all parent attributes would have a child attribute, it depends on the value you select.

For example, if sellers select “Composite Wood” for “Wood Type”, there is no child attribute.

#### 

**"Wood Type" Attribute**

```
{  
  "attributeName": "Wood Type",  
  "attributeRules": {  
    "attributeValueRules": {  
      "maxValue": "",  
      "minValue": "",  
      "numberInputTitle": null,  
      "propertyChooseTitle": null,  
      "valuePrecision": 0,  
      "valueRule": 0  
    },  
    "chooseMaxNum": 1,  
    "controlType": 1,  
    "transnationalAttribute": null  
  },  
  "attributeValueDetail": [  
    {  
      "attributeValueList": [  
        {  
          "childAttribute": [  
            {  
              "childAttributeId": 7318,  
              "childAttributeValueGroupId": "7317-7318-0"  
            }  
          ],  
          "value": "Log",  
          "vid": 213321  
        },  
        {  
          "childAttribute": null,  
          "value": "Composite Wood",  
          "vid": 213322  
        }  
      ],  
      "groupId": "12-7317-0"  
    }  
  ],  
  "attributeValueUnitList": null,  
  "refPid": 7317,  
  "required": false  
}
```

"Wood Type" attribute Breakdown

Since  "Wood" is selected under "Material", its child attribute "Wood Type" is triggerred and a value from "groupId": "12-7317-0" should be choosed.

```
"required": false, This is not a mandatory attribute.  
"controlType": 1, This is a Select type attribute  
"chooseMaxNum": 1, Can only choose one value from attributeValueList  
"refPid": 7317, Attribute ID 
```

Assemble attribute objects in temu.local.goods.add -> goodsProperty

```
{  
    "refPid": 7317,  
    "vid": 213321  
}
```

#### 

**"Wood Species” Attribute**

```
{  
  "attributeName": "Wood Species",  
  "attributeRules": {  
    "attributeValueRules": {  
      "maxValue": "",  
      "minValue": "",  
      "numberInputTitle": null,  
      "propertyChooseTitle": null,  
      "valuePrecision": 0,  
      "valueRule": 0  
    },  
    "chooseMaxNum": 1,  
    "controlType": 1,  
    "transnationalAttribute": null  
  },  
  "attributeValueDetail": [  
    {  
      "attributeValueList": [  
        {  
          "childAttribute": null,  
          "value": "Pterocarpus dalbergioides",  
          "vid": 213324  
        },  
        {  
          "childAttribute": null,  
          "value": "Amomum testaceum",  
          "vid": 213326  
        },  
...  
...  
...,  
        {  
          "childAttribute": null,  
          "value": "Pterocarpus indicus",  
          "vid": 213608  
        },  
        {  
          "childAttribute": null,  
          "value": "Chosenia arbutifolia",  
          "vid": 213609  
        }  
      ],  
      "groupId": "7317-7318-0"  
    }  
  ],  
  "attributeValueUnitList": null,  
  "refPid": 7318,  
  "required": false  
}
```

"Wood Species” Breakdown

Since  "Log" is selected under "Wood Type", its child attribute "Wood Species" is triggerred and a value from "groupId": "7317-7318-0" should be choosed.

```
{  
  "attributeName": "Wood Species",  
  "attributeRules": {  
    "attributeValueRules": {  
      "maxValue": "",  
      "minValue": "",  
      "numberInputTitle": null,  
      "propertyChooseTitle": null,  
      "valuePrecision": 0,  
      "valueRule": 0  
    },  
    "chooseMaxNum": 1,  
    "controlType": 1,                          //Select type attribute  
    "transnationalAttribute": null  
  },  
  "attributeValueDetail": [  
    {  
      "attributeValueList": [                    //values can be selected under "Wood Species"  
        {  
          "childAttribute": null,  
          "value": "Pterocarpus dalbergioides",  
          "vid": 213324  
        },  
        {  
          "childAttribute": null,  
          "value": "Amomum testaceum",  
          "vid": 213326  
        },  
...  
...  
...,  
        {  
          "childAttribute": null,  
          "value": "Skapanthus oreophilus",  
          "vid": 213604  
        },  
        {  
          "childAttribute": null,  
          "value": "Pterocarpus indicus",  
          "vid": 213608  
        },  
        {  
          "childAttribute": null,  
          "value": "Chosenia arbutifolia",  
          "vid": 213609  
        }  
      ],  
      "groupId": "7317-7318-0"  
    }  
  ],  
  "attributeValueUnitList": null,  
  "refPid": 7318,  
  "required": false  
}
```

Assemble attribute objects in temu.local.goods.add -> goodsProperty

```
{  
    "refPid": 7318,  
    "vid": 213604  
}
```
