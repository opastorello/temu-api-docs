# [Error SOP][3000001]sign is invalid, please check your sign calculation

| Error Code | Error Message |
|---|---|
| 3000001 | sign is invalid, please check your sign calculation |

- 

**Potential cause:**

1. 

The app_secret does not match the app_key.

1. 

Please check whether there are two sign values in your request payload. The server may use the first one as the signature, which could cause the validation to fail.

1. 

The signature calculation is incorrect.

- 

**Next step:**

Please note that "sign" validation is performed first. Only after this validation passes will the server start checking the other parameters in your request.

Signature Method for API request: [https://partner.temu.com/documentation?menu_code=38e79b35d2cb463d85619c1c786dd303&sub_menu_code=4a821c90d06442a09e061b0d4316fbf3](https://partner.temu.com/documentation?menu_code=38e79b35d2cb463d85619c1c786dd303&sub_menu_code=4a821c90d06442a09e061b0d4316fbf3)

Temu Open API Request Example with Signature Generation in Python: [https://partner.temu.com/documentation?menu_code=38e79b35d2cb463d85619c1c786dd303&sub_menu_code=89e9f25227e5496bbbd894cbfac9c4fa](https://partner.temu.com/documentation?menu_code=38e79b35d2cb463d85619c1c786dd303&sub_menu_code=89e9f25227e5496bbbd894cbfac9c4fa)
