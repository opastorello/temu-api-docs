# [150010090] SKU duplicated

| Error Code | Error Message |
|---|---|
| 150010090 | SKU duplicated |

- 

**Root cause:**

Either outSkuSn or outGoodsSn in your request payload is already exist in the seller’s mall.

- 

**From seller center perspective:**

The SKU is considered duplicated because either the Contribution SKU or the Contribution Goods already exists in the Seller Center.

outSkuSn -> Contribution SKU

![image](https://bstatic.kwcdn.com/open-outer/211a2a4ba4a/aed3ac44b057169673a92c00935465ca.png)

outGoodsSn -> Contribution Goods

![image](https://bstatic.kwcdn.com/open-outer/211a2a4ba4a/b70d05d899bdca210ba9fa466b93241b.png)

- 

**Next Steps**

Modify outSkuSn, outGoodsSn, make sure outSkuSn, and outGoodsSn are unique in seller’s mall.

Modify Contribution SKU,  Contribution Goods, make sure Contribution SKU, and  Contribution Goods are unique in seller’s mall.
