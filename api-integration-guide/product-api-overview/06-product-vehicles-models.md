# Product Vehicles Models

**Last update:** 2025-01-26 12:15:40

## New Product Release

**Interface:** `bg.local.goods.add`

When creating a new product, add the `goodsVehiclePropertyRelation` field to associate it with the vehicle model library data:

| Field | Description |
|---|---|
| `relationType` | Enumeration value. `1` = vehicle model library |
| `relationId` | Vehicle library ID. Query via `bg.local.goods.property.relations.level.template` (different sites and categories have different vehicle libraries) |
| `leafPropertyValueDependencyIdList` | Set adaptive vehicle models. Only pass leaf attributes (data of the last level). Query via `bg.local.goods.property.relations.template` |

---

## Query Extended Attribute Data of the Product

**Interface:** `bg.local.goods.property.relations`

Query the extended attribute library data associated with the product.

**Notes:**
- A product may have multiple associated attribute libraries.
- `relationType==1` = vehicle model library.
- Different vehicle libraries for different countries/categories are distinguished using `relationId`.
- After editing online products, there will be an online version and an edited new version, which may correspond to different vehicle model library information. Use `queryLastVersion` to query the product version.

---

## Query Comprehensive Hierarchical Data of the Expanded Attribute Library

**Interface:** `bg.local.goods.property.relations.level.template`

Queries the hierarchical attributes of each layer in cascading data.

The response is an array, where each element represents metadata of a column:

| Field | Description |
|---|---|
| `parentLoadDependencyId` | ID of the property on the previous layer of `PropertyDependencyId` |
| `level` | Number of columns represented by this attribute |
| `propertyName` | Attribute classification name (e.g., first column = manufacturer) |
| `propertyDependencyId` | Hierarchical ID, reflects current level and sorting. Used when querying sub-attributes |
| `relationId` | Vehicle library ID (different sites/categories have different vehicle libraries) |

---

## Query Hierarchical Data of the Expanded Attribute Library

**Interface:** `bg.local.goods.property.relations.template`

Used to query the full range of adapted vehicle models in a specific vehicle library. Selected adapted vehicle model enumerations must belong to the corresponding vehicle library.

| Field | Description |
|---|---|
| `propertyRelationQueryDTOList` | If empty → query full attribute data in the first column. If not empty → query corresponding sub-attributes |
| `parentPropertyValueDependencyId` | Used to query previous layer attribute values of the current attribute enumeration |
| `propertyDependencyId` | Attribute dependency id / hierarchy id |

If `isLeafProperty=true` for a node → it is a leaf property with no data in the next level.

---

## Model Library Template Data Query Logic

**Step 1:** Use `bg.local.goods.property.relations.level.template` to query vehicle model library metadata for the site and category. Returns:
1. The model library ID (`relationId`) for the currently maintained model library.
2. Hierarchical attribute classification (e.g., 5 levels: Manufacturer → Model → Year → Trim → Engine).
3. Hierarchical ID (`propertyDependencyId`) for each layer.

**Step 2:** Query first column attribute data using `bg.local.goods.property.relations.template`:
- Pass `propertyDependencyId` of the first column.
- Do not pass `propertyRelationQueryDTOList` (leave empty) to get the complete first column.
- Use returned attribute value dependency IDs to query child attribute data.

**Step 3:** Query sub-attribute data recursively:
- Use each attribute's `propertyValueDependencyId` + next level's `propertyDependencyId` to query the next level sub-data.
- Continue until `isLeafProperty=true`.
