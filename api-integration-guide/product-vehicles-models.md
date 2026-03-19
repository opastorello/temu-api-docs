# Product Vehicles models

# 

New product release

**bg.local.goods.add**

When creating a new product, add the `goodsVehiclePropertyRelation` field to associate it with the vehicle model library data

-`**relationType**`: is an enumeration value, 1 represents the vehicle model library

-`**relationId**`: Because different sites and categories have different vehicle libraries, it is necessary to query the specific vehicle library corresponding to the site and category through** ****bg.local.goods.property.relations.level.template**. **relationId**** ** is the vehicle library ID

-`**leafPropertyValueDependencyIdList**`：The  meaning is to set an adaptive vehicle model, and when passing parameters, it is not necessary to pass all levels of data, only the leaf attributes (the data of the last level) are needed, which can be queried through**bg.local.goods.property.relations.template**

# 

Query the extended attribute data of the product

`**bg.local.goods.property.relations**`

Query the extended attribute library data associated with the product

instructions:

The product has multiple associated attribute libraries, and the enumeration value **relationType==1**** **is the vehicle model library. At the same time, vehicle libraries vary in different countries and categories, and different vehicle libraries can be distinguished using relationId.

After editing online products, there will be online versions and edited new versions, and different product versions may correspond to different vehicle model library information filled in. You can query the product version through the `**queryLastVersion**`** ** field.

# 

Query the comprehensive hierarchical data of the expanded attribute library

![image](https://bstatic.kwcdn.com/open-outer/20a3d467c2/1b4fdcbd0474112558c2cd5199883955.png)

`**bg.local.goods.property.relations.level.template**`Query the hierarchical attributes of each layer in cascading data

The response parameter is an array, where each element represents the metadata of a certain column, such as the first column:

**ParentLoadDependency Id**** **: The ID of the property on the previous layer of **Property Dependency Id **

**level**:   The number of columns represented by this attribute

**propertyName**:  Attribute classification name, the first column represents the manufacturer

**propertyDependencyId**:  Hierarchical ID, reflecting the current level and sorting of the data. When querying specific sub attributes in interface 4, it is necessary to use

**relationId**:  Vehicle library ID, different sites/categories have different vehicle libraries, and the 'relationId' will be used to distinguish them

# 

Query the hierarchical data corresponding to the expanded attribute library

`**bg.local.goods.property.relations.template**`

Used to query the full range of adapted vehicle models in a specific vehicle library. When submitting the adapted vehicle models associated with a product, the selected adapted vehicle model enumeration needs to belong to the corresponding vehicle library.

The query order is to first query the full attribute data in the first column, and then query the next level sub attributes of a certain attribute based on the queried attribute data

`**propertyRelationQueryDTOList**`： If it is empty, query the full attribute data in the first column. If it is not empty, query the corresponding sub attributes of the attribute

`**parentPropertyValueDependencyId**` ： Used to query the previous layer attribute values of the current attribute enumeration

`**propertyDependencyId**`:  Attribute dependency id/hierarchy id

# 

Model library template data query logic

1. First, use **bg.local.goods.property.relations.level.template **to query the metadata of the vehicle model library corresponding to the site and category

The returned data includes three key points

The first is the model library ID corresponding to the currently maintained model library

The second is the hierarchical attribute classification value of the vehicle library, such as using five levels of ** ****Manufacturer ,  Model , Year,  Trim , and  Engine**** ** to classify the data in the vehicle library

The third is the hierarchical ID, which can be understood as an ID corresponding to each layer **propertyDependencyId**

2. Query the first column attribute data

Use **bg.local.goods.property.relations.template **to query, and use the hierarchy of the first column obtained in step 1 to pass the parameters, **propertyDependencyId **， The set of attribute value dependency IDs that do not pass the parent attribute, called `**propertyRelationQueryDTOList**`, represents the complete data of the first page column for querying. Subsequent queries need to use the attribute value dependency IDs of each node in the query result to query the data of child attributes

3. Query sub attribute data

Using the **bg.local.goods.property.relations.template**** **query, in step 2, retrieve the full set of attributes in the first column. Use the attribute value dependency of each attribute, `**propertyValueDependencyId**`, and the next level's`**propertyDependencyId**`to query the next level's sub data of a node to determine the last level,

If the `**isLeafProperty**` field of a node is true, it means that the property is a leaf property and there is no data in the next level
