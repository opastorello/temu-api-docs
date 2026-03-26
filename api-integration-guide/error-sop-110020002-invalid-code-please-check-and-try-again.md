# [Error SOP][110020002] Invalid code, please check and try again.

| Error Code | Error Message |
|---|---|
| 110020002 | Invalid code, please check and try again. |

- 

**Potential cause:**

Please note that the **temporary authorization code** can only be used **once** and will **expire after 10 minutes**.

We have observed many cases where partners send the `**bg.open.accesstoken.create**` request **twice within one second**. In some situations, they only log the **second request**, which may lead them to believe that everything is correct while the request still fails.

This happens because the `**code**` can only be used **once**. After it is used to create an **access token**, it immediately becomes **invalid**.

- 

**Next step:**

Please ensure that the **authorization code is used only once** when calling the `**bg.open.accesstoken.create**` API and use it within 10 minutes.

ref: [https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=82674d12ebe64af2820d62ebbc2ecc16](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=82674d12ebe64af2820d62ebbc2ecc16)
