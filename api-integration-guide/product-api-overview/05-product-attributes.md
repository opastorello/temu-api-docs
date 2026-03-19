# Product Attributes

**Last update:** 2025-01-26 12:04:24

## Understanding Attribute Structure

Temu attributes have a parent-child structure. Each category has a set of attribute templates, retrieved via `bg.local.goods.template.get`.

Attributes are divided into:
- **Sales attributes** (`isSale=true`): Used to create variants. Typical examples: color, size. Specification values combine in a Cartesian product to form variants.
- **Normal attributes** (`isSale=false`): Describe the product's characteristics.

Sales attributes are further classified based on customization:
- `inputMaxSpecNum > 0`: Category allows user-defined attributes.
- `inputMaxSpecNum = 0`: Category only allows predefined attributes. Select attributes marked with `required=true` in `goodsSpecProperties`.

Both sales and normal attributes are assembled and passed to the `goodsProperty` parameter in `bg.local.goods.add`.

---

## Custom Sales Attributes

Custom attributes are only allowed when `inputMaxSpecNum > 0`.

**Process:**
1. Choose a `parentSpec` from `userInputParentSpecList`.
2. Use `bg.local.goods.spec.id.get` to generate specification values.
3. Pass generated values as input parameters in `skuList[*].specIdList` of `bg.local.goods.add`.

**Notes:**
- `inputMaxSpecNum > 0` and `goodsSpecProperties != []` can coexist — the category allows both custom and predefined attribute values.
  - Example: Predefined color options `['red', 'blue']` + custom type attribute can both be used to create variants.
- `singleSpecValueNum` defines the maximum number of variants that can be created.

---

## Normal Attributes

### Control Type Definition

`controlType` defines how the attribute interacts with the user:

| Value | Name | Description |
|---|---|---|
| `0` | INPUT | Input Field |
| `1` | CHOOSE | Selectable Option |
| `3` | INPUT_CHOOSE | Both Input and Selectable |
| `5` | SINGLE_YMD_DATE | Single Date Selector (Year, Month, Day) |
| `6` | MULTIPLE_YMD_DATE | Range Date Selector (Year, Month, Day) |
| `7` | SINGLE_YM_DATE | Single Date Selector (Year, Month) |
| `8` | MULTIPLE_YM_DATE | Range Date Selector (Year, Month) |
| `16` | PROPERTY_CHOOSE_AND_INPUT | Property Selection and Value Input |

### Attribute Object Parameters by ControlType

| ControlType | Description | Property Object Parameters |
|---|---|---|
| `0` | Input type | `{ "templatePid": ..., "refPid": ..., "pid": ..., "vid": 0, "value": "..." }` |
| `0` (with unit) | Input type with unit | Add `"valueUnitId": ..., "valueUnit": "..."` |
| `1` | Select type | `{ "templatePid": ..., "refPid": ..., "pid": ..., "vid": values[0].vid, "value": values[0].value }` |
| `1` (sale property) | Sale property (from `goodsSpecProperties`) | `{ "templatePid": ..., "refPid": ..., "pid": ..., "vid": ..., "specId": ... }` |
| `16` | Numeric Input + Select | `{ "templatePid": ..., "refPid": ..., "pid": ..., "vid": ..., "value": "Nylon", "numberInputValue": "50", "valueUnitId": ..., "valueUnit": "..." }` |

---

## Parent-Child Attributes

Parent-child relationships are defined by the `showType` field:

- `showType = 0`: Parent attribute.
- `showType = 1`: Child attribute.

Child attributes appear based on the `controlType` of the parent attribute:
- If parent `controlType = 0`: `showCondition` indicates conditions under which child attributes are triggered based on parent attribute values.
- If parent `controlType` is `1`, `3`, or `16`: `templatePropertyValueParentList` determines when child attributes are triggered.

**Example:** "Fabric Weight (g/m²)" attribute with `controlType=0`:
- `required=true` → must be provided.
- `showType=1` → it's a child attribute.
- Check `showCondition`: if parent attribute (`parentRefPid=6926`) has selected one of `parentVids=[161198]`, the child attribute is shown and should be assembled using `controlType=0`.

---

## Attributes with Units

Attributes with units should include both `valueUnitId` and `valueUnit` when available in `valueUnitList`. Typically used with `controlType=0`.
