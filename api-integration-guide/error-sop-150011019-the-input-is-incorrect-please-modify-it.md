# [Error SOP][150011019]The input {*}:{*} is incorrect, please modify it.

| Error Code | Error Message |
|---|---|
| 150011019 | The input {*}:{*} is incorrect, please modify it. |

- 

**Potential cause:**

Please make sure the input barCodeId mathes the barCodeType (external product code type, 1=EAN 2=UPC 3=ISBN 4=GTIN-14), and the barCodeId is a valid Id.

Example:  "errorMsg": "The input barCodeId:012345678905111 is incorrect, please modify it."

"012345678905111" is not a valid UPC code, as it didn't pass the seller center's validation.

- 

**From temu seller center perspective:**

You need to provide a valid external product ID for the SKU.

![image](https://bstatic.kwcdn.com/open-outer/211a2a4ba4a/644e3652685049d1f00ae0abfdb0fe8a.png)

- 

**Next step:**

Please ask the seller to provide the correct **barCodeId**. You can verify whether it is valid by listing a product manually in the Temu Seller Center using the same **barCodeType** and **barCodeId**.
