# [Error SOP][3000032] access_token don't have this api access

| Error Code | Error Message |
|---|---|
| 3000032 | access_token don't have this api access, please ask for seller to authorize this api in seller center first.and share the new access_token with you. |

- 

**Root cause:**

The token used to authorize this appkey does not have permission to access these interfaces.

Please ensure that the seller has selected all required permission packages.

![image](https://bstatic.kwcdn.com/open-outer/211a2a4ba4a/bd3bc426135aa96f925938235243f677.png)

Permission packages include different interfaces.

The following interfaces are **sensitive** and require contacting the seller’s BD to apply for whitelist access:

bg.order.amount.query

bg.local.goods.sku.list.price.query

temu.pay.tax.invoice.pdf.download

temu.pay.tax.invoice.info.query

After being whitelisted, you need to **re-authorize the mall to your app and generate a new token** to ensure the permissions take effect.

*Please note that permissions for **sensitive interfaces** are usually whitelisted at the **mallId level for **app type: self-developed app. Make sure the mall associated with your API request has already been granted whitelist access.

You can verify whether you are requesting the correct mall by calling `bg.open.accesstoken.info.get`.
