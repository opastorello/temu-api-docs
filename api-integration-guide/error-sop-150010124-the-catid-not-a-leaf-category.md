# [Error SOP][150010124]The catId not a leaf category

| Error Code | Error Message |
|---|---|
| 150010124 | The catId not a leaf category |

- 

**Root Cause:**

A category can be used to list a product only if it meets the following two requirements in bg.local.goods.cats.get:

| Properties | Value | Description |
|---|---|---|
| leaf | true | Is Leaf Category |
| availableStatus | 0 | Category status: 0-Available, 1-Not available |

*Please note that some categories are sensitive. Only after the seller obtains approval from Temu will the corresponding catId be returned by bg.local.goods.cats.get. In this case, please query the interface again to ensure the updated catId is returned for the seller’s shop.

- 

**From temu seller center perspective:**

If you want to use a category, you must provide a leaf-level category (i.e., the last level in the category hierarchy).

![image](https://bstatic.kwcdn.com/open-outer/211a2a4549c/9c837e41087022562927c1ba7b3e55cb.png)
