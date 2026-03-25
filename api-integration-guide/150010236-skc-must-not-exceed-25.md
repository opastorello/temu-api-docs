# [150010236]  SKC must not exceed 25

| Error Code | Error Message |
|---|---|
| 150010236 | SKC must not exceed 25 |

- 

**Root cause:**

For category which catType is Apparel in bg.local.goods.cats.get

If the number of specId(Variants which variation type is "Color") >= 25, this error will occur.

- 

**From seller center perspective:**

For Apparel category products, a maximum of 25 color variants is allowed.

![image](https://bstatic.kwcdn.com/open-outer/211a2a4ba4a/3cd9ab6a275e287da5ff669d7481004e.png)

- 

**Next step:**

Removing low-performing color options

Splitting the product into multiple listings under the same category
