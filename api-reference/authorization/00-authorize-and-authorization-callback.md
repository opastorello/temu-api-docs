# Authorize and Authorization Callback

**Last update:** 2025-03-14 08:52:09

---

Authorization is an important step to using Open API. ERP needs to be authorized by the seller in order to call non-public APIs required for shop management.

---

## What is Authorization Callback

Authorization callback means the platform will not directly return tokens — tokens need to be exchanged through a `code`.

- **Seller In House System:** Authorize callback address through operational feedback.
- **Enterprise Resource Planning:** Fill in the authorization `Redirect URL` address on the open platform:
  - **US:** `https://partner-us.temu.com/app/app-mgmt/detail/edit?app_key={{your appkey}}`
  - **Global:** `https://partner.temu.com/app/app-mgmt/detail/edit?app_key={{your appkey}}`
  - **EU:** `https://partner-eu.temu.com/app/app-mgmt/detail/edit?app_key={{your appkey}}`

> **Note:** You currently need to edit the `redirect_url` field in the App to configure the callback address. Once configured, it takes effect immediately on the App Store.

---

## How to Get Code

Merchants go to the Seller Center for authorization. After authorization, the front-end page redirects to the redirect URL in the authorization link, like:
```
https://seller.temu.com/?code=xxxxxx
```

After the seller grants authorization, the Open Platform returns the authorization code to the callback `redirect_url`. The ERP can then use the code to get `access_token` for the first time.

---

## How to Get Access Token

After successful authorization, use the code in the redirect URL to call `bg.open.accesstoken.create`. This helps you obtain the `mall_id` and `access_token`.

> **Note:** When calling the interface for the first time, the `token` is equal to the `code`.

**API Reference:** `bg.open.accesstoken.create`

### Request

```json
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

### Response

```json
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
