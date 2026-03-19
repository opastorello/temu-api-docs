# Product Attributes

**Last update:** 2025-01-26 12:04:24

---

# 
Understanding Attribute Structure

- 
**Temu attributes** have a parent-child structure, and each category has a set of attribute templates, which can be retrieved via the `bg.local.goods.template.get` interface.

- 
Attributes are divided into **sales attributes** and **normal attributes**, controlled by the `isSale` property. Attributes returning `true` are considered sales attributes.

- 
**Sales attributes** are used to create variants. For example, typical attributes like `color` and `size` combine their specification values in a Cartesian product to form variants.

- 
**Normal attributes** describe the product itself, providing more detailed information about the product's characteristics.

- 
Sales attributes are further classified based on whether customization is allowed:

- 
If the category allows user-defined attributes, `inputMaxSpecNum > 0` is returned.

- 
If the category only allows selecting predefined attributes, `inputMaxSpecNum = 0` is returned. In this case, you should only select attributes marked with `required = true` in the `goodsSpecProperties` object, and pick a few values.

- 
Both **sales attributes** and **normal attributes** need to be assembled and passed to the `goodsProperty` parameter when making a request via the `bg.local.goods.add` interface.

# 
Custom Sales Attributes

- 
Custom attributes are allowed only when `inputMaxSpecNum > 0`.

- 
In this case, you can choose a `parentSpec` from `userInputParentSpecList`, and use `bg.local.goods.spec.id.get` to generate specification values. These values will form variants, such as creating a custom specification value like `color1` under the `color` attribute.

- 
**Note:** It’s possible for `inputMaxSpecNum > 0` and `goodsSpecProperties != []` to occur at the same time, which means the category allows both custom attributes and predefined attribute values. For example, a predefined `color` attribute might have options like `['red', 'blue']`, and a custom attribute like `type` can also be added. You can combine these to create variants by selecting values from both `color` and `type`.

- 
**Note:** `singleSpecValueNum` defines the maximum number of variants that can be created.

- 
`bg.local.goods.spec.id.get` generates specification values, which should be passed as input parameters in the `skuList[*].specIdList` field of the `goods.add` method.

# 
Normal Attributes

- 
**Control Type Definition**

`controlType` defines how the attribute interacts with the user. The common control types are:

- 
`INPUT(0, "Input Field")`

- 
`CHOOSE(1, "Selectable Option")`

- 
`INPUT_CHOOSE(3, "Both Input and Selectable")`

- 
`SINGLE_YMD_DATE(5, "Single Date Selector - Year, Month, Day")`

- 
`MULTIPLE_YMD_DATE(6, "Range Date Selector - Year, Month, Day")`

- 
`SINGLE_YM_DATE(7, "Single Date Selector - Year, Month")`

- 
`MULTIPLE_YM_DATE(8, "Range Date Selector - Year, Month")`

- 
`PROPERTY_CHOOSE_AND_INPUT(16, "Property Selection and Value Input")`

- 
**Common control types** and how to assemble attributes can be found in the relevant tables.

| 

***ControlType***
 | 

***Description***
 | 

***Property Object Paramters***
 
| 

*0*
 | 

Input type property
 | 

```
{
    "templatePid": property['templatePid'],
    "refPid": property['refPid'],
    "pid": property['pid'],
    "vid": 0,
    "value": str(random.randint(int(property['minValue']), int(property['maxValue'])))
}
```

Note: if value property['valueUnitList'] defined an unit for value

```
{
    "templatePid": property['templatePid'],
    "refPid": property['refPid'],
    "pid": property['pid'],
    "vid": 0,
    "value": str(random.randint(int(property['minValue']), int(property['maxValue']))),
    "valueUnitId": property['valueUnitList'][0]['valueUnitId'],
    "valueUnit": property['valueUnitList'][0]['valueUnit']
}
```

 
| 

*1*
 | 

Select type property
 | 

```
{
    "templatePid": property['templatePid'],
    "refPid": property['refPid'],
    "pid": property['pid'],
    "vid": property['values'][0]['vid'],
    "value": property['values'][0]['value']
}
```

Note: If property is defined at `goodsSpecProperties` , you should follow the Sale Property rule, model like that:

```
{
    "templatePid": saleProperty['templatePid'],
    "refPid": saleProperty['refPid'],
    "pid": saleProperty['pid'],
    "vid": saleProperty['values'][0]['vid'],
    "specId": saleProperty['values'][0]['specId']
}
```

 
| 

*16*
 | 

Numeric Input type property
 | 

```
{
    "templatePid": property['templatePid'],
    "refPid": property['refPid'],
    "pid": property['pid'],
    "vid": property['values'][0]['vid'],
    "value": property['values'][0]['value'], // "Nylon"
    "numberInputValue": "50",
    "valueUnitId": property['valueUnitList'][0]['valueUnitId'],
    "valueUnit": property['valueUnitList'][0]['valueUnit']
},
{
    "templatePid": property['templatePid'],
    "refPid": property['refPid'],
    "pid": property['pid'],
    "vid": property['values'][0]['vid'],
    "value": property['values'][0]['value'], // "Cotton"
    "numberInputValue": "50",
    "valueUnitId": property['valueUnitList'][0]['valueUnitId'],
    "valueUnit": property['valueUnitList'][0]['valueUnit']
}
```

 

- 
**Parent-Child Attributes**

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

- 
**Attributes with Units**

Attributes that have units should include both `valueUnitId` and `valueUnit` when available in the `valueUnitList`. These are typically used in combination with `controlType = 0`.
