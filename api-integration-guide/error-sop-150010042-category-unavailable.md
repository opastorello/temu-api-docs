# [Error SOP][150010042]Category unavailable

| Error Code | Error Message |
|---|---|
| 150010042 | Category unavailable |

- 

**Root Cause:**

A category can be used to list a product only if it meets the following two requirements in bg.local.goods.cats.get:

| Properties | Value | Description |
|---|---|---|
| leaf | true | Is Leaf Category |
| availableStatus | 0 | Category status: 0-Available, 1-Not available |

*Please note that some categories are sensitive. Only after the seller obtains approval from Temu will the corresponding catId be returned by bg.local.goods.cats.get. In this case, please query the interface again to ensure the updated catId is returned for the seller’s shop.

![image](https://bstatic.kwcdn.com/open-outer/211a2a4549c/05aaa8cfe7c357c628e9f195ab27e701.png)
