# Add Products Guide

## 

**Add Products API Call Process**

### 

**Overview:**

![image](https://bstatic.kwcdn.com/open-outer/21a4885b68/52b6b9b32bdbc3efbc792c51efedc566)

### 

**Minimum Viable Integration**

#### 

**1.Product identity**

![image](https://bstatic.kwcdn.com/open-outer/21a4885b68/d4d08fcaaa79902a3bea4ec42a18f21c)

![image](https://bstatic.kwcdn.com/open-outer/21a4885b68/59704c0190e42a391783ae2bf7e3c77f)

1. 

1. 

1. 

1. 

[](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=b49f03d2b1744700ab762b9fe80d1af7)

[](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=244c900c28ee4c16b3e7cc88296f74d9)

![image](https://bstatic.kwcdn.com/open-outer/21a4885b68/04c16e0e90dbc5da9f40ec8850f5b7c5)

[](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=b49f03d2b1744700ab762b9fe80d1af7)

1. 

``

1. 

````

  1. 

1. 

1. 

``````

1. 

| Properties | Required | How to fill in | Precautions |
|---|---|---|---|
| goodsBasic | True | - |  |
| -goodsName | True | User inputs | Validation Rules:Only supports English letters, numbers, and symbols.Does not support decorative characters: ~ ! * $ ? _ ~ { } # < > \| * ; ^ ¬ ¦Does not support high ASCII characters type 1, such as ®, ©, ™, etc.Character count: Within 500 characters.temu.local.goods.illegal.vocabulary.checkPlease note that it is recommended to use this interface to check for any violations in product information to avoid affecting sales |
| -catId | True | Retrieve from other APIsbg.local.goods.cats.getThis api  bg.local.goods.category.recommend will help you quickly match temu categories based on product information | bg.local.goods.cats.getEntering parentCatId=0 retrieves all available first-level categories for posting.To obtain leaf categories: Recursively call this interface, entering parentCatId with the catId selected from the previous call's results to get the next level of category ID until the leaf categories are reached.When entering a leaf category, the interface returns empty.ImportantEnsure to use the most specific (leaf) category ID for posting products; you must keep calling the aforementioned interface until the most specific category is obtained.catType is an important varibale for judgement whether category is an Apparel (catType=0) or Non-Apparel(catType=1) one, it will effect at the image required shape.Some categories on different sites are not sellable, only the categories with availableStatus=0 need to be obtained |

#### 

**2.Attributes**

  - 

**Product attributes: **Divided into required attributes and optional attributes;

    - 

Required attributes are important product attributes and can help buyers get a better understanding of the product. Please ensure that all required attributes are passed in goodsProperty.

    - 

Optional attributes can enhance the product description. You can choose to pass them in, but it is recommended to fill in as many optional attributes as possible.

Different category have different required attributes.

![image](https://bstatic.kwcdn.com/open-outer/21a4885b68/17f5c5740c9246be02ad583c22d2f426)

[](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=0f94f542969a4473a9bb77d4c55bf821)

****

********

1. 

[](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=0f94f542969a4473a9bb77d4c55bf821)

1. 

  - 

``

  - 

``

  - 

``````

  - 

``````````

1. 

````````

[](https://partner.temu.com/documentation?menu_code=38e79b35d2cb463d85619c1c786dd303&sub_menu_code=c1bf67656f404183997c74675c635087)

| Properties | Required | How to fill in | Precautions |
|---|---|---|---|
| goodsProperty | True | Retrieve from other APIsbg.local.goods.template.get | This is a very important and complex piece of information, and it takes more time to process it when entering it-Determine whether the field isSale=false is a normal attribute or  isSale=true is a variant attribute, This array is used to set product data about isSale=false-Pay attention to the contentRequired attributes must be passed in, judging by bg.local.goods.template.get -  required=TrueThere is a parent-child relationship attribute. When the parent attribute selects a value, the child attribute must be passed inshowType = 0: Parent attribute.showType = 1: Child attribute.Child attributes appear based on the controlType of the parent attribute. If controlType = 0, showCondition will indicate the conditions under which child attributes are triggered based on parent attribute values.If controlType is 1, 3, or 16, the templatePropertyValueParentList will determine when child attributes are triggered.Attributes that have units should include both valueUnitId and valueUnit when available in the valueUnitList. These are typically used in combination with controlType = 0.bg.local.goods.compliance.property.checkPlease note that it is recommended to use this interface to check for any violations in product information to avoid affecting salesPlease refer to this document for details |

#### 

**3.Variations **

- 

**Variation:** You must set either 1 or 2 variations for each SKU. It is used for buyers to choose from.

Different category have different variations.

![image](https://bstatic.kwcdn.com/open-outer/21a4885b68/9042b216f617c87d206b0f4055ee20ce)

[``](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=0f94f542969a4473a9bb77d4c55bf821)

- 

![image](https://bstatic.kwcdn.com/open-outer/21a4885b68/1c354b7ebec2c63f2980691ffcbebf58)

  - 

``

![image](https://bstatic.kwcdn.com/open-outer/21a4885b68/611ecf80c4d184a122a7df067dfc945a)

  - 

``````

- 

``

  - 

``````````

  - 

****``````````````

  - 

****``

- 

[``](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=727a1977afd547109a1d3be70abe42d4)````

[](https://partner.temu.com/documentation?menu_code=38e79b35d2cb463d85619c1c786dd303&sub_menu_code=d7943785ff2e4185976170f07924256e)

| Properties | Required | How to fill in | Precautions |
|---|---|---|---|
| -specIdList | True | User inputs & Retrieve from other APIs | This is a field used to distinguish variants, such as color, size, etc. Please note that there are two ways to set this information for different categories on the platform. Setting this information is often prone to errors and requires special attentionEach category has a set of attribute templates, which can be retrieved via the bg.local.goods.template.get interface.Sales attributes are further classified based on whether customization is allowed: If the category allows user-defined attributes, inputMaxSpecNum > 0 is returned. If the category only allows selecting predefined attributes, inputMaxSpecNum = 0 is returned. In this case, you should only select attributes marked with required = true in the goodsSpecProperties object, and pick a few values.Custom attributes are allowed only when inputMaxSpecNum > 0.In this case, you can choose a parentSpec from userInputParentSpecList, and use bg.local.goods.spec.id.get to generate specification values. These values will form variants, such as creating a custom specification value like color1 under the color attribute.Note: It’s possible for inputMaxSpecNum > 0 and goodsSpecProperties != [] to occur at the same time, which means the category allows both custom attributes and predefined attribute values. For example, a predefined color attribute might have options like ['red', 'blue'], and a custom attribute like type can also be added. You can combine these to create variants by selecting values from both color and type.Note: singleSpecValueNum defines the maximum number of variants that can be created.bg.local.goods.spec.id.get generates specification values, which should be passed as input parameters in the skuList[*].specIdList field of the goods.add method.please refer to this document for details |

#### 

**4.Add Product SKUs**

**SKU**: Can be used for sellers' internal inventory management and must be unique within the store. 

![image](https://bstatic.kwcdn.com/open-outer/21a4885b68/c9f1528855669ba71531826f649be285)

[](https://partner.temu.com/documentation?menu_code=38e79b35d2cb463d85619c1c786dd303&sub_menu_code=2cc05ca389ca4eeb8e704e903ebcc6bd)

****

[](https://partner.temu.com/documentation?menu_code=38e79b35d2cb463d85619c1c786dd303&sub_menu_code=2cc05ca389ca4eeb8e704e903ebcc6bd)

[](https://partner.temu.com/documentation?menu_code=38e79b35d2cb463d85619c1c786dd303&sub_menu_code=2cc05ca389ca4eeb8e704e903ebcc6bd)

[](https://partner.temu.com/documentation?menu_code=38e79b35d2cb463d85619c1c786dd303&sub_menu_code=2cc05ca389ca4eeb8e704e903ebcc6bd)

[](https://partner.temu.com/documentation?menu_code=38e79b35d2cb463d85619c1c786dd303&sub_menu_code=2cc05ca389ca4eeb8e704e903ebcc6bd)

[](https://partner.temu.com/documentation?menu_code=38e79b35d2cb463d85619c1c786dd303&sub_menu_code=2cc05ca389ca4eeb8e704e903ebcc6bd)

[](https://partner.temu.com/documentation?menu_code=38e79b35d2cb463d85619c1c786dd303&sub_menu_code=2cc05ca389ca4eeb8e704e903ebcc6bd)

[](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=b49f03d2b1744700ab762b9fe80d1af7)

- 

****

- 

****

[](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=2760e68837bc4716b0208e624558d0f4)

| Properties | Required | How to fill in | Precautions |
|---|---|---|---|
| skuList | True | User inputs & Retrieve from other APIs | This amount information is the amount that the merchant plans to sell in TEMU. If there are subsequent orders generated, this amount information will be used to calculate the settlement amount with the merchant |
| -basePrice | True | User inputs | Different sites have corresponding requirements for currency information, please refer to this document for details |
| -quantity | True | User inputs | This is the inventory information corresponding to the product, with a setting range of [0, 999999] |
| -weight | True | User inputs | Different sites have corresponding requirements for this information, please refer to this document for details |
| -weightUnit | True | User inputs | Different sites have corresponding requirements for this information, please refer to this document for details |
| -length | True | User inputs | Different sites have corresponding requirements for this information, please refer to this document for details |
| -width | True | User inputs | Different sites have corresponding requirements for this information, please refer to this document for details |
| -height | True | User inputs | Different sites have corresponding requirements for this information, please refer to this document for details |
| -volumeUnit | True | User inputs | Different sites have corresponding requirements for this information, please refer to this document for details |
| -images | True | User inputs | Identify whether it belongs to the clothing category through the bg.local.goods.cats.get-catType, as different types have differences in size ratiosApparel Carousel ImagesAspect Ratio: 3:4Width:≥1340pxHeight: ≥1785pxNon-Apparel Carousel ImagesAspect Ratio: 1:1Width:≥800pxHeight: ≥800px-Size：≤3 MB-Format: jpeg, jpg, pngIt is necessary to upload the images to TEMU in advance, and using bg.local.goods.image.upload will facilitate users to handle the corresponding image proportions and sizes in a portable manner |

#### 

**5.Offer **

- 

Handling time: The number of days from when you receive an order to when it can be shipped. Example: 0.5 working days.

- 

Shipping template: A corresponding shipping template must be selected before the product can be listed. Click Add shipping template if there isn't one available for use.

- 

Fulfillment channel: Self-delivery is selected by default in TEMU seller center

![image](https://bstatic.kwcdn.com/open-outer/21a4885b68/b33cfe270a10bad22aac2eb6fef44178)

[](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=01a44ea6e787400fbd375947e4012ddb)

![image](https://bstatic.kwcdn.com/open-outer/21a4885b68/f77752d1e8f019aa5b2adb78c9202e47)

****

****

| Properties | Required | How to fill in | Precautions |
|---|---|---|---|
|  |  |  |  |
| -costTemplateId | True | Retrieve from other APIsbg.freight.template.list.query | Users need to go to the seller center to create the shipping template page in order for this interface to return the corresponding data |
| -fulfillmentType | True | User inputs | Delivery Method: 1 - Self-fulfillment, Fixed setting to 1 |
| -shipmentLimitDay | True | User inputs | Indicates the time, in days, between when you receive an order for an item and when you can ship the item. The default production time is 1 or 2. |

#### 

**6. Safety and Compliance**

The API allows products to be added to the Seller Center without completing the Safety and Compliance information.

If the Seller Center later determines that additional qualifications or governance attributes are required for the product to become on sale (active), these details can be provided and updated afterward.

Compliance and governance attribute requirements are determined dynamically by factors including, but not limited to, the product category, store region, and product attributes.

  - 

**California Proposition 65 Warning Type** (optional): If your product is subject to California Proposition 65, it is essential that you provide accurate information, otherwise you will receive penalties from relevant administrative regulatory agencies in California. Temu will display corresponding content depending on the selected warning type.

  - 

**Product guides or documents**: Please upload a PDF file of the product instructions. File size: Up to 15 MB.

  - 

**Actual product photos**: Please follow the prompts at the top of the page to upload a photo of the product packaging or the product itself with the required label.

  - 

**Compliance documents:** A complete test report proving that the product has passed all necessary tests must be uploaded. Example: IEC, UL, or CSA standards.

    - 

**Actual product photos**: It is recommended that the photo's aspect ratio is 1:1, with a width and height of ≥800 pixels. The recommended photo size should not exceed 3 MB to prevent upload failures.

    - 

**Compliance documents**: The file is allowed to upload up to 30Mb. If you have any questions about the uploaded qualification content, you can contact the docking investment promotion.

After the product is submitted, the Seller Center backend system may initiate a compliance assessment and require additional compliance documents.

![image](https://bstatic.kwcdn.com/open-outer/21a4885b68/0cbc08ea3fab7de82dc51b8bfc96e305)

[](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=1b5e6495f73c4e599d9f08872cb23177)

[](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=1b5e6495f73c4e599d9f08872cb23177)

[](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=1b5e6495f73c4e599d9f08872cb23177)

[](https://partner.temu.com/documentation?menu_code=38e79b35d2cb463d85619c1c786dd303&sub_menu_code=5bb50d82c08740688068d960977f8d52)

[](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=1b5e6495f73c4e599d9f08872cb23177)

[](https://partner.temu.com/documentation?menu_code=38e79b35d2cb463d85619c1c786dd303&sub_menu_code=5bb50d82c08740688068d960977f8d52)

[](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=1b5e6495f73c4e599d9f08872cb23177)

****

[](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=1b5e6495f73c4e599d9f08872cb23177)

[](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=1b5e6495f73c4e599d9f08872cb23177)

[](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=1b5e6495f73c4e599d9f08872cb23177)

[](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=e9141097cdfc4e2f9c68ab0dee57f9c9)

[](https://partner-eu.temu.com/documentation?menu_code=85762c6ccc5a4dbc8c023ea5e10c6dc0&sub_menu_code=4fe287d454d14fd89056bd80438bb08a)

****

****

****

****

****

****

****

****

[](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=e9141097cdfc4e2f9c68ab0dee57f9c9)

[](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=e9141097cdfc4e2f9c68ab0dee57f9c9)

[](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=e9141097cdfc4e2f9c68ab0dee57f9c9)

[](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=1b5e6495f73c4e599d9f08872cb23177)

[](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=1b5e6495f73c4e599d9f08872cb23177)

[](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=e311a6f798fb4ab4b98aa4a2a7b8129c)

[](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=e311a6f798fb4ab4b98aa4a2a7b8129c)

- 

[](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=e9141097cdfc4e2f9c68ab0dee57f9c9)

- 

- 

- 

```
  
  
  
  

```

[](https://partner.temu.com/documentation?menu_code=38e79b35d2cb463d85619c1c786dd303&sub_menu_code=5bb50d82c08740688068d960977f8d52)

| Properties | Required | How to fill in | Precautions |
|---|---|---|---|
| certificationInfo | False | User inputs & Retrieve from other APIs | -When publishing a product, it is not mandatory. Merchants need to supplement it completely before selling, otherwise the sale will be restricted- |
| -certificateInfo | False | User inputs & Retrieve from other APIs | bg.local.goods.compliance.rules.getAccording to this interface, obtain the qualification rules that need to be uploaded [isRequired=true]. When calling this interface, you need to pass in the product category and attributes. Different attribute information for the same category will affect the qualification requirements |
| --certType | True | User inputs & Retrieve from other APIs | bg.local.goods.compliance.rules.getReturn the corresponding qualification type that needs to be set from this interface. It should be noted that there may be multiple qualifications that need to be uploaded, and they should be passed in according to the format of the object |
| --authCodes | False | User inputs | The user manually enters the corresponding file nameSize: ≤120 characters Only supports English and numbers |
| --certFiles | False | User inputs & Retrieve from other APIs | bg.local.goods.compliance.rules.getReturn the corresponding qualification type that needs to be set from this interface. It should be noted that there may be multiple qualifications that need to be uploaded, and they should be passed in according to the format of the object |
| ---fileName | False | User inputs | Size: ≤200 characters Only supports English and numbersquantity: ≤6 |
| ---fileUrl | False | User inputs & Retrieve from other APIs | Need to call the file upload interface to upload the file to temu in advanceDocument upload instructionsbg.local.goods.gallery.signature.get-uploadFileType : 4-Qualification Document |
| --inspectReportFiles | False | User inputs & Retrieve from other APIs | bg.local.goods.compliance.rules.getReturn the corresponding qualification type that needs to be set from this interface. It should be noted that there may be multiple qualifications that need to be uploaded, and they should be passed in according to the format of the object |
| ---fileName | False | User inputs | Size: ≤200 characters Only supports English and numbersquantity: ≤6 |
| ---fileUrl | False | User inputs & Retrieve from other APIs | Need to call the file upload interface to upload the file to temu in advanceDocument upload instructionsbg.local.goods.gallery.signature.get-uploadFileType : 4-Qualification Document |
| --energyLabel | False | User inputs | bg.local.goods.compliance.rules.getReturn the corresponding qualification type that needs to be set from this interface. It should be noted that there may be multiple qualifications that need to be uploaded, and they should be passed in according to the format of the object |
| ---model | False | User inputs | Merchants need to register on relevant EU websites in advance and enter the corresponding value information themselves |
| ---brand | False | User inputs | Merchants need to register on relevant EU websites in advance and enter the corresponding value information themselves |
| ---agreeAuthorization | False | User inputs | Default True |
| --selectedCheckItems | False | User inputs & Retrieve from other APIs | bg.local.goods.compliance.rules.get-Return the corresponding qualification type that needs to be set from this interface. It should be noted that there may be multiple qualifications that need to be uploaded, and they should be passed in according to the format of the object- |
| ---key | False | User inputs & Retrieve from other APIs | Obtain the qualification corresponding to isRequired=true from the interface bg.local.goods.compliance.rules.get, and the page displays the information of all refPid under the checkItems object |
| ---value | False | User inputs & Retrieve from other APIs | Obtain the qualification corresponding to isRequired=true from the interface bg.local.goods.compliance.rules.get, and the page displays the information of all vid under the checkItems object |
| -extraTemplate | False | User inputs & Retrieve from other APIs | -When publishing a product, it is not mandatory. Merchants need to supplement it completely before selling, otherwise the sale will be restricted-get from bg.local.goods.compliance.extra.template.get~templateDimensionTypetemplateDimensionType=1 (goods) or 2 (goods and sku) this value needs to be passed inAccording to this interface, obtain the qualification rules that need to be uploaded [isRequired=true]. When calling this interface, you need to pass in the product category and attributes. Different attribute information for the same category will affect the qualification requirements-The entry rules here are similar to the general attributes of the product, and it is important to pay attention to the type of ControlType & parentVidList , which can affect different entry methods. Please refer to the document for details-contentType=1 represents the qualification certificate（use certFiles to upload）contentType=2 the inspection report（use inspectReportFiles to upload）contentType=3 the qualification code（use authCodes  to upload）contentType=4 actualPhoto（use actualPhoto  to upload）contentType=5 selectedCheckItems （use selectedCheckItems  to upload）contentType=6 EU-energyLabel （use energyLabel to upload）demo"extraTemplate":{"extraTemplateDetailList": [{"templateId": 51,"inputText": {"refPid": {"multiLineInputs": [{"name": "2222"},{"name": "111"}]}}} |
| --extraTemplateDetailList | False | User inputs & Retrieve from other APIs |  |
| ---templateId | False | User inputs & Retrieve from other APIs | -get from bg.local.goods.compliance.extra.template.get ~templateId |
| ---properties | False | User inputs & Retrieve from other APIs | -get from bg.local.goods.compliance.extra.template.get ~ vid & refPid |
| ---compliancePropertyList | False | User inputs & Retrieve from other APIs | -When publishing a product, it is not mandatory. Merchants need to supplement it completely before selling, otherwise the sale will be restricted-get from bg.local.goods.compliance.extra.template.get~templateDimensionTypetemplateDimensionType=2(goods and sku) or 3(sku) this value needs to be passed indemo"extraTemplate": {"extraTemplateDetailList": [{"templateId": 36,"properties": {"1000100110": [1000131288]}},{"templateId": 51,"inputText": {"1100100115": {"multiLineInputs": [{"name": "12"}]}}},{"templateId": 248,"properties": {"refPid": [vid]}},{"templateId": 1004,"compliancePropertyList": [{"specIdList": [72537019,77008250],"inputTextList": [{"properties": {"1100100460": [1000274743],"1100100461": [1000278143],"1100100463": [ 1000277743,"1100100475": [1000277343]},"inputText": {"1100100464": {"name": "1"}}}]}]}]} |
| -actualPhoto | False | User inputs & Retrieve from other APIs | -When publishing a product, it is not mandatory. Merchants need to supplement it completely before selling, otherwise the sale will be restricted,-get from bg.local.goods.compliance.rules.get ~actualPhotoRequirement  Determine whether it is mandatory based on bg.local.goods.compliance.rules.get ~mustHaveActualPhoto |
| -gpsrInfo | False | User inputs & Retrieve from other APIs | -Need to apply in advance in the seller center-When publishing a product, it is not mandatory. Merchants need to supplement it completely before selling, otherwise the sale will be restricted,-get from bg.local.goods.compliance.info.fill.list.queryrepType: 2 -EU Head——only eurepType: 3 -EU Manufacturer——only euand repStatus=3: Application successful |
| -repInfo | False | User inputs & Retrieve from other APIs | -Need to apply in advance in the seller center-When publishing a product, it is not mandatory. Merchants need to supplement it completely before selling, otherwise the sale will be restricted,-get from bg.local.goods.compliance.info.fill.list.query repType: 4 - Korea A/S REP——only Korea repType: 5 -Turkey REP——only Turkeyand repStatus=3: Application successful |
| guideFileInfo | False | - |  |
| -lang2GuideFileUrl | False | User inputs | According to the bg.local.goods.compliance.extra.template.get, determine whether it is necessary to upload the instruction manual. It is not mandatory when publishing products, but some categories will be restricted from sale if they are not supplemented before sale. It is recommended to add a feature for users to set when publishing productsLanguage-PDF Product Manual Mapping: key is the language, value is the file URL.The English version must be importedUploading requires an additional call to the file upload interface.Correct parameter example："lang2GuideFileUrl": {      "en": "",      "es": "",      "de": ""  } Please refer to this document for details |

### 

**Complete Integration Capabilities**

Ref: [https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=0366595cb7a840bcbde5ae1f24657d69](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=0366595cb7a840bcbde5ae1f24657d69)

### 

**Examples:**

1. 
#### 

Quick Start

The minimum required parameters to successfully add a product in Seller Center. This section focuses only on mandatory parameters and the simplest workflow to add a product.

![image](https://bstatic.kwcdn.com/open-outer/21a4885b68/f71cb382e9882f84f8274dc63632423c.png)

```
{  
  "app_key": "f7f83a8058228c1bc8f4993f28d95557",  
  "data_type": "JSON",  
  "access_token": "upl0gho4ovopvyvfiky4x7prgwh3dt1gfjea8ogdfqq1czzblsxs5aeyqew",  
  "timestamp": 1768888324,  
  "type": "bg.local.goods.add",  
  "version": "V1",  
  "goodsBasic": {  
    "goodsName": "DemoProduct",  
    "catId": 1466  
  },  
  "goodsServicePromise": {  
    "shipmentLimitDay": 1,  
    "fulfillmentType": 1,  
    "costTemplateId": "LFT-15630053225717890848"  
  },  
  "goodsProperty": {  
    "goodsProperties": [  
      {  
        "pid": 1,  
        "vid": 381,  
        "value": "Stainless Steel",  
        "templatePid": 937018,  
        "refPid": 12  
      }  
    ]  
  },  
  "skuList": [  
    {  
      "price": {  
        "listPriceType": 1,  
        "basePrice": {  
          "amount": "3",  
          "currency": "KRW"  
        }  
      },  
      "quantity": 1,  
      "specIdList": [  
        266386378,  
        266375920  
      ],  
      "weight": "1",  
      "weightUnit": "g",  
      "length": "1",  
      "width": "1",  
      "height": "1",  
      "volumeUnit": "cm",  
      "images": [  
        "https://img.kwcdn.com/local-image/s119/21a4885b68/198fc479-f78e-4549-a900-3c73f88cf556_1024x1024.png"  
      ]  
    }  
  ],  
  "sign": "681E1596372E4BB770B9C18233134290"  
}
```

```
{  
    "result": {  
        "goodsId": 604890541711850,  
        "skuInfoList": [  
            {  
                "specList": [  
                    {  
                        "specId": 266386378,  
                        "parentSpecId": 1001  
                    },  
                    {  
                        "specId": 266375920,  
                        "parentSpecId": 3001  
                    }  
                ],  
                "outSkuSn": "",  
                "skuId": 77600126949823  
            }  
        ],  
        "productType": 1  
    },  
    "success": true,  
    "requestId": "gl-24d74835-1524-4961-b323-a2a53fd2e72a",  
    "errorCode": 1000000,  
    "errorMsg": ""  
}
```

1. 
#### 

Add a product with Brand&Size chart

       Extend your product information by providing brand details and size chart data. 

![image](https://bstatic.kwcdn.com/open-outer/21a4885b68/35d9c2b0df946cdc8651982195528e69.png)

```
{  
  "app_key": "f7f83a8058228c1bc8f4993f28d95557",  
  "data_type": "JSON",  
  "access_token": "upl0gho4ovopvyvfiky4x7prgwh3dt1gfjea8ogdfqq1czzblsxs5aeyqew",  
  "timestamp": 1768891819,  
  "type": "bg.local.goods.add",  
  "version": "V1",  
  "goodsBasic": {  
    "goodsName": "DemoProduct-Brand&Sizechart",  
    "catId": 33160,  
    "outGoodsSn": "outGoodsSntest1",  
    "goodsGallery": {  
      "detailVideo": {  
        "vid": "local-video#yukshwpoj9thodhhxzrf79e89e1ipiio",  
        "videoUrl": "https://goods-vod.kwcdn.com/local-video/s119/21a4885b68/8e5d5aa06ee560c7d074f476a4f390d9.mp4"  
      },  
      "carouselVideo": {  
        "vid": "local-video#x3ngbx7wgnkrxmjbvhaa79e8pg7d7ev4",  
        "videoUrl": "https://goods-vod.kwcdn.com/local-video/s119/21a4885b68/a2b32c828f83b703c211b917b1a77ec7.mp4"  
      },  
      "detailImage": [  
        "https://img.kwcdn.com/local-image/s119/21a4885b68/464d0c3c-a31e-400a-b483-4d0b7116b3b4_1024x1024.png"  
      ]  
    },  
    "productType": 1  
  },  
  "goodsServicePromise": {  
    "shipmentLimitDay": 2,  
    "fulfillmentType": 1,  
    "costTemplateId": "LFT-15630053225717890848"  
  },  
  "goodsProperty": {  
    "goodsProperties": [  
      {  
        "pid": 1,  
        "vid": 2,  
        "value": "Linen",  
        "templatePid": 315432,  
        "refPid": 12  
      },  
      {  
        "pid": 5,  
        "vid": 172,  
        "value": "Hooded",  
        "templatePid": 315512,  
        "refPid": 21  
      },  
      {  
        "pid": 2,  
        "vid": 35385,  
        "value": "Nylon",  
        "valueUnit": "%",  
        "templatePid": 878027,  
        "refPid": 15,  
        "numberInputValue": "100"  
      },  
      {  
        "pid": 1467,  
        "vid": 277759,  
        "value": "TEST202506131408",  
        "templatePid": 946978,  
        "refPid": 1960  
      },  
      {  
        "pid": 13,  
        "vid": 433,  
        "value": "Beige",  
        "templatePid": 315451,  
        "refPid": 63,  
        "parentSpecId": "1001",  
        "specId": "15060"  
      },  
      {  
        "pid": 14,  
        "vid": 313,  
        "value": "XS",  
        "templatePid": 315550,  
        "refPid": 65,  
        "parentSpecId": "3001",  
        "specId": "12001"  
      },  
      {  
        "pid": 14,  
        "vid": 315,  
        "value": "S",  
        "templatePid": 315550,  
        "refPid": 65,  
        "parentSpecId": "3001",  
        "specId": "10004"  
      }  
    ]  
  },  
  "skuList": [  
    {  
      "price": {  
        "listPriceType": 0,  
        "listPrice": {  
          "amount": "4",  
          "currency": "KRW"  
        },  
        "basePrice": {  
          "amount": "3",  
          "currency": "KRW"  
        }  
      },  
      "quantity": 999,  
      "specIdList": [  
        12001,  
        15060  
      ],  
      "weight": "1",  
      "weightUnit": "g",  
      "length": "1",  
      "width": "1",  
      "height": "1",  
      "volumeUnit": "cm",  
      "images": [  
        "https://img.kwcdn.com/local-image/s119/21a4885b68/432bd406-c14d-4767-96b7-8862fa38c886_1340x1787.png"  
      ],  
      "outSkuSn": "testexternalproductid11",  
      "referenceLink": "https://partner-us.temu.com/documentation?menu_code=38e79b35d2cb463d85619c1c786dd303&sub_menu_code=d7943785ff2e4185976170f07924256e"  
    },  
    {  
      "price": {  
        "listPriceType": 0,  
        "listPrice": {  
          "amount": "4",  
          "currency": "KRW"  
        },  
        "basePrice": {  
          "amount": "3",  
          "currency": "KRW"  
        }  
      },  
      "quantity": 888,  
      "specIdList": [  
        10004,  
        15060  
      ],  
      "weight": "2",  
      "weightUnit": "g",  
      "length": "2",  
      "width": "2",  
      "height": "2",  
      "volumeUnit": "cm",  
      "images": [  
        "https://img.kwcdn.com/local-image/s119/21a4885b68/432bd406-c14d-4767-96b7-8862fa38c886_1340x1787.png"  
      ],  
      "outSkuSn": "testexternalproductid22",  
      "referenceLink": "https://partner-us.temu.com/documentation?menu_code=38e79b35d2cb463d85619c1c786dd303&sub_menu_code=d7943785ff2e4185976170f07924256e"  
    }  
  ],  
  "goodsTrademark": {  
    "trademarkId": 111000826001,  
    "noTrademark": false,  
    "brandId": 110033793002  
  },  
  "goodsSizeChartList": {  
    "goodsSizeChartList": [  
      {  
        "meta": {  
          "groups": [  
            {  
              "id": 1,  
              "name": "Size"  
            },  
            {  
              "id": 21,  
              "name": "Korea"  
            }  
          ],  
          "elements": [  
            {  
              "id": 10002,  
              "name": "Chest"  
            },  
            {  
              "id": 10003,  
              "name": "Length"  
            }  
          ]  
        },  
        "classId": 5,  
        "records": [  
          {  
            "values": [  
              {  
                "id": 1,  
                "value": "XS"  
              },  
              {  
                "id": 10002,  
                "value": "1"  
              },  
              {  
                "id": 10003,  
                "value": "2"  
              },  
              {  
                "id": 21,  
                "value": "XS"  
              }  
            ]  
          },  
          {  
            "values": [  
              {  
                "id": 1,  
                "value": "S"  
              },  
              {  
                "id": 10002,  
                "value": "3"  
              },  
              {  
                "id": 10003,  
                "value": "4"  
              },  
              {  
                "id": 21,  
                "value": "S"  
              }  
            ]  
          }  
        ],  
        "bodyMeta": {  
          "groups": [  
            {  
              "id": 1,  
              "name": "Size"  
            }  
          ],  
          "elements": [  
            {  
              "id": 30000,  
              "name": "Waist"  
            },  
            {  
              "id": 30001,  
              "name": "Hips"  
            }  
          ]  
        },  
        "bodyRecords": [  
          {  
            "values": [  
              {  
                "id": 30000,  
                "value": "1-2"  
              },  
              {  
                "id": 1,  
                "value": "XS"  
              },  
              {  
                "id": 30001,  
                "value": "3-4"  
              }  
            ]  
          },  
          {  
            "values": [  
              {  
                "id": 30000,  
                "value": "5-6"  
              },  
              {  
                "id": 1,  
                "value": "S"  
              },  
              {  
                "id": 30001,  
                "value": "7-8"  
              }  
            ]  
          }  
        ]  
      }  
    ]  
  },  
  "goodsOriginInfo": {  
    "agreeDefaultOriginRegion": true,  
    "originRegion1": "Mainland China",  
    "originRegion2": "Guangdong"  
  },  
  "sign": "A1D51AA17A98F0489C7132FC9F672286"  
}
```

```
{  
    "result": {  
        "goodsId": 604753102744178,  
        "productType": 1,  
        "skuInfoList": [  
            {  
                "specList": [  
                    {  
                        "specId": 10004,  
                        "parentSpecId": 3001  
                    },  
                    {  
                        "specId": 15060,  
                        "parentSpecId": 1001  
                    }  
                ],  
                "outSkuSn": "testexternalproductid22",  
                "skuId": 79799150211029  
            },  
            {  
                "specList": [  
                    {  
                        "specId": 12001,  
                        "parentSpecId": 3001  
                    },  
                    {  
                        "specId": 15060,  
                        "parentSpecId": 1001  
                    }  
                ],  
                "outSkuSn": "testexternalproductid11",  
                "skuId": 79799150227413  
            }  
        ]  
    },  
    "success": true,  
    "requestId": "gl-922c4460-c1ff-4475-8fd8-673578fb2e80",  
    "errorCode": 1000000,  
    "errorMsg": ""  
}
```
