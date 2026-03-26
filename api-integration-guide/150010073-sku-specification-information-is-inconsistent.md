# [150010073] SKU specification information is inconsistent

| Error Code | Error Message |
|---|---|
| 150010073 | SKU specification information is inconsisten |

- 

**Root cause:**

In a single sku, if the parentSpecId is the same, this error will occur. Within a single SKU, if the specId list (e.g. [id1, id2]) contains specIds that belong to the same parent specId, it means the variants are from the same variation type, which is not allowed in Temu Seller center

For example, if a SKU (SKU1) already has Color as a variation type(parentSpecId) and its variant (specId) is Black,

   SKU1 = Black

- 

**From seller center perspective:**

You cannot define the same SKU with another value under the same variation type, such as Black + Green.

![image](https://bstatic.kwcdn.com/open-outer/211a2a4ba4a/11fe009bf22192d39c927aee84f28748.png)

- 

**Next step:**

Please check whether any two SKUs in your request payload have the same parentSpecId, and ensure that each SKU has a unique parentSpecId.
