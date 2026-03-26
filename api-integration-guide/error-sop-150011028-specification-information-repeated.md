# [Error SOP][150011028]Specification information repeated: [{*}]

| Error Code | Error Message |
|---|---|
| 150011028 | Specification information repeated: [{*}] |

- 

**Potential cause:**

A SKU with the same specification combination already exists.

- 

**From seller center perspective:**

Variant duplicate.

*Variants can split the same product into different SKUs, helping consumers clearly view and choose.Even if there is only one SKU, you must select at least one variant type. You can select a key variant type and fill in a unique variant value.For example, a "white" mug can select "color=white" or "material=ceramic" as the unique variant information.

For example, if a product already contains a SKU with `color=red`, creating another SKU with the same specification (`color=red`) is not allowed.

![image](https://bstatic.kwcdn.com/open-outer/211a2a4ba4a/5fdbb89b168092666713aad6ea3e6376.png)

- 

**Next Steps**

Please remove the duplicate specification information from your request payload, as it already exists.
