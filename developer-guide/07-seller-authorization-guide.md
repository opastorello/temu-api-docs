# Seller Authorization Guide

**Last update:** 2026-01-07 01:40:37

---

# 
Introduction

For Crossborder sellers and Local sellers, different types of sellers log in to different backends for operation authorization. Authorization means that the seller uses a third-party ISV (Independent Software Vendor). The seller's authorization permission must be obtained in advance before the open platform's API capabilities can be used normally.

# 
Seller Authorization

| 

**Seller Type**
 | 

**Site Region**
 | 

**Authorization Type**
 | 

**Website Url**
 
| 

**Crossborder sellers**
 | 

US
 | 

Mannual
 | 

[https://agentseller.temu.com/open-platform/system-manage/client-manage](https://agentseller.temu.com/open-platform/system-manage/client-manage)
 
| 

**Crossborder sellers**
 | 

EU
 | 

Mannual
 | 

[https://agentseller-eu.temu.com/open-platform/system-manage/client-manage](https://agentseller-eu.temu.com/open-platform/system-manage/client-manage)
 
| 

**Local sellers**
 | 

US
 | 

Mannual

Callback `New` 
 | 

[https://seller.temu.com/open-platform/client-manage](https://seller.temu.com/open-platform/client-manage)
 
| 

**Local sellers**
 | 

EU
 | 

Mannual

Callback `New` 
 | 

[https://seller-eu.temu.com/open-platform/client-manage](https://seller-eu.temu.com/open-platform/client-manage)
 
# 
Authorization Type

Once your app is published on the App Store, sellers will be able to authorize it. There are two types of authorization:

- 
**Manual Authorization:** The user manually authorizes the app in the Seller Center and selects the permissions to be granted (defining the API scope the app can access). Once the authorization is complete, the system directly displays the access_token to the user. The user copies the access_token into the app for configuration, and the developer saves the access_token for subsequent program calls.

- 
**Callback Authorization:** The user authorizes the app in the Seller Center and selects the permissions to be granted (defining the API scope the app can access). After completing the authorization, a code is sent to the app's pre-configured redirect_url. The app's front end retrieves the code and passes it to the back end, which then uses the code to generate an access_token. This authorization method is suitable for immediate installation from the app store and provides a better user experience, making it the recommended approach.

- 
**In-app Authorization (Lauch Soon): **In-app Authorization allows sellers to authorize a mall to your application directly within your app, without manually navigating to the Seller Center. This method leverages Temu’s authorization URL and callback mechanism and provides the most streamlined authorization flow for connecting a mall to an app.

# 
Authorization Steps

## 
**Local Seller**

Local Seller permissions for accessing product lists, order lists, order shipments, etc.

- 
Log in to the Local Seller Center - System Management - Authorization Management page (link address:

[https://seller.temu.com/open-platform/client-manage)](https://seller.temu.com/open-platform/client-manage))

- 
Click on **Authorize a new app**, which will display a list of available systems as shown below.

- 
Select the app name, and the permissions that can be granted to the selected system for the current store will be displayed.

- 
Click **Submit** at the bottom of the page, and the following screen will appear. Copy the **Access Token** and paste it into the software page to complete the configuration.

- 
If app is an **Callback Authorization, **Click OK then you will jump to app pages and start to have it worked.

- 
After successful authorization, the authorized permissions and expiration time will be displayed in the authorization list.And you can deauthorized an app in the list.

# 
How to trigger the authorization page of temu within your application (In-app Authorization)

- 
Temu allows you to trigger an authorization page specific to your application by constructing an authorization URL. You may also pass custom parameters through the `state` field. After the authorization is completed, Temu will invoke your callback URL and return the value you provided in the `state` field as part of the response.

- 
The authorization URL is constructed as follows:

- 
Use the Temu Seller Center URL for the corresponding site. For example, in the United States: [https://seller.temu.com](https://seller.temu.com)

- 
Append the fixed path: /open-platform/client-manage/authorization?

- 
Add the required parameters: appKey = XXX, where XXX is your application appkey

- 
redirect_uri = XXX, where XXX is your callback URL address 

- 
Complete Logic: [https://seller.temu.com/open-platform/client-manage/authorization?appKey=XXX&redirect_uri=XXX&state=XXX](https://seller.temu.com/open-platform/client-manage/authorization?appKey=XXX&redirect_uri=XXX&state=XXX)

Example (U.S. test application):  [https://seller.temu.com/open-platform/client-manage/authorization?appKey=4ebbc9190ae410443d65b4c2faca981f&redirect_uri=https://fanyi.baidu.com/&state=888](https://seller.temu.com/open-platform/client-manage/authorization?appKey=4ebbc9190ae410443d65b4c2faca981f&redirect_uri=https://fanyi.baidu.com/&state=888)

After the Temu authorization is completed, Temu will redirect the user to the specified callback URL and append the following parameters: 

- 
app_key

- 
callback_host

- 
code

- 
state

Example callback URL:[https://fanyi.baidu.com/mtpe-individual/transText?app_key=4ebbc9190ae410443d65b4c2faca981f&callback_host=openapi-b-us.temu.com&code=uplkzb4duvf8jyozva8jcmjwxsgth0heypmnrj3fjfavsyry5cf3ywmwzp4&state=888#/](https://fanyi.baidu.com/mtpe-individual/transText?app_key=4ebbc9190ae410443d65b4c2faca981f&callback_host=openapi-b-us.temu.com&code=uplkzb4duvf8jyozva8jcmjwxsgth0heypmnrj3fjfavsyry5cf3ywmwzp4&state=888#/)
