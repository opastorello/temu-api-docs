# Authorize and Authorization Callback

Authorization is an important step to using Open API.ERP need to be authorized by the seller in order to call non-public APIs required for shop management.​​

# 

What is Authorization callback

Authorization callback representatives will not directly return tokens, and tokens need to be exchanged through code​

- 

Seller In House System：Authorize callback address through operational feedback

- 

Enterprise Resource Planning：Fill in the authorization Redirect URL address on the open platform

  - 

US：[https://partner-us.temu.com/app/app-mgmt/detail/edit?app_key=](https://partner.temu.com/app/app-mgmt/detail/edit?app_key=1fae1e2d914449deda95378857a77331){{your appkey}}

  - 

Global：[https://partner.temu.com/app/app-mgmt/detail/edit?app_key=](https://partner.temu.com/app/app-mgmt/detail/edit?app_key=1fae1e2d914449deda95378857a77331){{your appkey}}

  - 

EU：[https://partner-eu.temu.com/app/app-mgmt/detail/edit?app_key=](https://partner.temu.com/app/app-mgmt/detail/edit?app_key=1fae1e2d914449deda95378857a77331){{your appkey}}

**Note:** You currently need to edit the `redirect_url` field in the App to configure the callback address. Note that once configured, it will take effect immediately on the App Store.

![image](https://bstatic.kwcdn.com/open-outer/1f193485780/1b0a7b1341f20729f944d44c3d3673c9.jpeg)

# 

How to get Code

Merchants can go to the seller center for authorization just like direct authorization.After authorization, the front-end page will redirect to the redirect URL in your authorization link，like：[https://seller.temu.com](https://seller.temu.com/)[/?code=xxxxxx](https://open.shopee.com/?code=xxxxxx&main_account_id=xxxxxx)​

After the seller has granted authorization, Open Platform will return the authorization code to the callback address redirect URL. ERP can then use the code to get access_token for the first time.​

# 

How to get Accesstoken

After successful authorization, use the code in the redirect URL to call this API（bg.open.accesstoken.create）. This helps you obtain the mall_id, access_token。​

When calling the interface for the first time, the **token** is equal to the **code**

**API  Reference**：[bg.open.accesstoken.create](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a)

**Request**

```
{  
 "access_token": "uplmntfsagmk84f4fm6grdjwm5nvugxqclvzl8b7uyxp04qfxskkoveopgz",  
 "app_key": "1024",  
 "code": "uplmntfsagmk84f4fm6grdjwm5nvugxqclvzl8b7uyxp04qfxskkoveopgz",  
 "data_type": "JSON",  
 "sign": "A03C3D255210263CDE6A56FAEEA008AB",  
 "timestamp": 1734098171,  
 "type": "bg.open.accesstoken.create"  
}
```

**Response**

```
{  
 "errorCode": 1000000,  
 "errorMsg": "",  
 "requestId": "us-0b0bfc9c-f61d-4530-b1a3-bb19704de637",  
 "result": {  
  "accessToken": "uplv3hfyt5kcwoymrgnajnbl1ow5qxlz4sqhev6hl3xosz5dejrtyl2jre7",  
  "apiScopeList": [  
   "bg.aftersales.aftersales.list.get",  
   "bg.aftersales.parentaftersales.list.get",  
   "bg.aftersales.parentreturnorder.get",  
   "bg.freight.template.list.query",  
   "bg.local.compliance.goods.list.query",  
   "bg.local.goods.add",  
   "bg.local.goods.brand.trademark.get",  
   "bg.local.goods.category.recommend",  
   "bg.local.goods.cats.get",  
   "bg.local.goods.compliance.edit",  
   "bg.local.goods.compliance.extra.template.get",  
   "bg.local.goods.compliance.property.check",  
   "bg.local.goods.compliance.rules.get",  
   "bg.local.goods.gallery.signature.get",  
   "bg.local.goods.list.query",  
   "bg.local.goods.out.sn.check",  
   "bg.local.goods.out.sn.set",  
   "bg.local.goods.partial.update",  
   "bg.local.goods.priceorder.accept",  
   "bg.local.goods.priceorder.change.sku.price",  
   "bg.local.goods.priceorder.negotiate",  
   "bg.local.goods.priceorder.query",  
   "bg.local.goods.property.get",  
   "bg.local.goods.publish.status.get",  
   "bg.local.goods.sale.status.set",  
   "bg.local.goods.size.element.get",  
   "bg.local.goods.sku.list.price.query",  
   "bg.local.goods.sku.list.query",  
   "bg.local.goods.sku.out.sn.check",  
   "bg.local.goods.sku.out.sn.set",  
   "bg.local.goods.spec.id.get",  
   "bg.local.goods.stock.edit",  
   "bg.local.goods.template.get",  
   "bg.local.goods.update",  
   "bg.logistics.companies.get",  
   "bg.logistics.shipment.confirm",  
   "bg.logistics.shipment.create",  
   "bg.logistics.shipment.document.get",  
   "bg.logistics.shipment.get",  
   "bg.logistics.shipment.result.get",  
   "bg.logistics.shipment.shippingtype.update",  
   "bg.logistics.shipment.sub.confirm",  
   "bg.logistics.shipment.update",  
   "bg.logistics.shippingservices.get",  
   "bg.logistics.warehouse.list.get",  
   "bg.open.accesstoken.info.get",  
   "bg.order.amount.query",  
   "bg.order.combinedshipment.list.get",  
   "bg.order.detail.get",  
   "bg.order.list.get",  
   "bg.order.shippinginfo.get",  
   "bg.tmc.message.update"  
  ],  
  "appSubscribeEventCodeList": [  
   "bg_open_event_test",  
   "bg_order_status_change_event",  
   "bg_trade_logistics_address_changed",  
   "bg_aftersales_status_change",  
   "bg_cancel_order_status_change"  
  ],  
  "appSubscribeStatus": 0,  
  "authEventCodeList": [],  
  "expiredTime": 1765634102,  
  "mallId": 1024  
 },  
 "success": true  
}
```
