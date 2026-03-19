# Order Retrieve and Management

Order inquiry is a necessary step for sellers, and we provide the following methods for order retrieval.

# 

Order Basic Model

1. 

**Temu Orders follow the PO Order - O Order structure.** When a consumer places an order, the order contains both the `parentOrder` and the order itself:

  - 

We use `parentOrderSn` as the unique identifier for the order, which is globally unique.

  - 

In the structure, a `parentOrder` contains multiple `orders`, and each `order` is associated with a single Temu SKU.

1. 

**Order information and shipping address information are not coupled.** To query the shipping address, use** **[`**bg.order.shippinginfo.v2.get**`](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=ccc2f59661584f5e8e205d85ddb9a6c9)** **separately.

  - 

Similarly, to query order amount information, use the** **[`**bg.order.amount.query**`](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=ba20da993f7d4605909dd49a5c186c21) interface.

# 

Order Inquiry Steps and Process

1. 

**Determine the **`**regionId**`** for the order to be queried:**

  - 

If `regionId` is not provided, the system defaults to querying all orders within the current shop's regions.

  - 

If a specific region is required, please refer to the table below to choose the region.

1. 

**Use **[`**bg.order.list.v2.get**`](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=554fd46b45ee49269cbdd6d4008a5dc1)** for continuous order polling.** It is recommended to query orders based on the last update time:

  - 

Use the `updateTime` parameter as the input to the interface. The time window for queries can be customized as needed.

  - 

Note that the returned order list is paginated. Make sure to iterate through all pages to avoid missing any orders.

1. 

**If you need more detailed information, use **[`**bg.order.detail.v2.get**`](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=9bf33a25319e4d7bbaf5ece4b823b9c3)** to query individual orders** and retrieve more detailed order information.

1. 

**Use **[`**bg.order.shippinginfo.v2.get**`](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=ccc2f59661584f5e8e205d85ddb9a6c9)** to query shipping address information:**

  - 

The shipping address contains detailed structured information such as `addressLine1` and `addressLine2`. Please ensure to save this information.

  - 

For most regions, invalid phone numbers will be returned first. The phone number format will be like `XXX-XXX`, where the last four digits usually represent the extension (i.e., a format of 10digits + 4 digits).

1. 

**Use **[`**bg.order.decryptshippinginfo.get**`](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=001b8d067220423c9da40c8c3b4010be)** to query full shipping address information:**

  - 

In this interface you can retrieve sensitive shipping address information for a specific order.

# 

RegionId Enum Values

******

******

| regionId | regionEnName |
|---|---|
| 2 | Afghanistan |
| 3 | Albania |
| 4 | Algeria |
| 5 | Andorra |
| 6 | Angola |
| 7 | Anguilla |
| 8 | Antigua and Barbuda |
| 9 | Argentina |
| 10 | Armenia |
| 11 | Aruba |
| 12 | Australia |
| 13 | Austria |
| 14 | Azerbaijan |
| 15 | Bahamas |
| 16 | Bahrain |
| 17 | Bangladesh |
| 18 | Barbados |
| 19 | Belarus |
| 20 | Belgium |
| 21 | Belize |
| 22 | Benin |
| 23 | Bermuda |
| 24 | Bhutan |
| 25 | Bolivia |
| 26 | Bosnia and Herzegovina |
| 27 | Botswana |
| 28 | Bouvet Island |
| 29 | Brazil |
| 30 | British Indian Ocean Territory |
| 31 | Brunei Darussalam |
| 32 | Bulgaria |
| 33 | Burkina Faso |
| 34 | Burundi |
| 35 | Cambodia |
| 36 | Cameroon |
| 37 | Canada |
| 38 | Cape Verde |
| 39 | Cayman Islands |
| 40 | Central African Republic |
| 41 | Chad |
| 42 | Chile |
| 43 | China |
| 44 | Christmas Island |
| 45 | Colombia |
| 46 | Comoros |
| 47 | Congo |
| 48 | Cook Islands |
| 49 | Costa Rica |
| 50 | Croatia |
| 51 | Cuba |
| 52 | Cyprus |
| 53 | Czech Republic |
| 54 | Denmark |
| 55 | Djibouti |
| 56 | Dominica |
| 57 | Dominican Republic |
| 58 | East Timor |
| 59 | Ecuador |
| 60 | Egypt |
| 61 | El Salvador |
| 62 | Equatorial Guinea |
| 63 | Eritrea |
| 64 | Estonia |
| 65 | Ethiopia |
| 66 | Faroe Islands |
| 67 | Fiji |
| 68 | Finland |
| 69 | France |
| 70 | French Guiana |
| 71 | French Polynesia |
| 72 | French Southern Territories |
| 73 | Gabon |
| 74 | Gambia |
| 75 | Georgia |
| 76 | Germany |
| 77 | Ghana |
| 78 | Gibraltar |
| 79 | Greece |
| 80 | Greenland |
| 81 | Grenada |
| 82 | Guadeloupe |
| 83 | Guam |
| 84 | Guatemala |
| 85 | Guinea |
| 86 | Guinea-Bissau |
| 87 | Guyana |
| 88 | Haiti |
| 89 | Honduras |
| 226 | Hong Kong |
| 90 | Hungary |
| 91 | Iceland |
| 92 | India |
| 93 | Indonesia |
| 94 | Iran |
| 95 | Iraq |
| 96 | Ireland |
| 97 | Israel |
| 98 | Italy |
| 99 | Jamaica |
| 100 | Japan |
| 101 | Jordan |
| 102 | Kazakhstan |
| 103 | Kenya |
| 104 | Kiribati |
| 235 | Kosovo |
| 105 | Kuwait |
| 106 | Kyrgyzstan |
| 107 | Lao People's Democratic Republic |
| 108 | Latvia |
| 109 | Lebanon |
| 110 | Lesotho |
| 111 | Liberia |
| 112 | Liechtenstein |
| 113 | Lithuania |
| 114 | Luxembourg |
| 115 | Macau |
| 116 | Macedonia |
| 117 | Madagascar |
| 118 | Malawi |
| 119 | Malaysia |
| 120 | Maldives |
| 121 | Mali |
| 122 | Malta |
| 123 | Marshall Islands |
| 124 | Martinique |
| 125 | Mauritania |
| 126 | Mauritius |
| 127 | Mayotte |
| 128 | Mexico |
| 129 | Micronesia |
| 130 | Moldova |
| 131 | Monaco |
| 132 | Mongolia |
| 134 | Montenegro |
| 133 | Montserrat |
| 135 | Morocco |
| 136 | Mozambique |
| 137 | Myanmar |
| 138 | Namibia |
| 139 | Nauru |
| 140 | Nepal |
| 141 | Netherlands |
| 142 | Netherlands Antilles |
| 143 | New Caledonia |
| 144 | New Zealand |
| 145 | Nicaragua |
| 146 | Niger |
| 147 | Nigeria |
| 148 | Niue |
| 149 | Norfolk Island |
| 150 | North Korea |
| 151 | Norway |
| 152 | Oman |
| 153 | Pakistan |
| 154 | Palau |
| 155 | Palestine |
| 156 | Panama |
| 157 | Papua New Guinea |
| 158 | Paraguay |
| 159 | Peru |
| 160 | Philippines |
| 161 | Pitcairn |
| 162 | Poland |
| 163 | Portugal |
| 164 | Puerto Rico |
| 165 | Qatar |
| 185 | Republic of Korea |
| 166 | Reunion |
| 167 | Romania |
| 168 | Russian Federation |
| 169 | Rwanda |
| 170 | Saint Lucia |
| 171 | Samoa |
| 172 | San Marino |
| 173 | Sao Tome and Principe |
| 174 | Saudi Arabia |
| 176 | Senegal |
| 175 | Serbia |
| 177 | Seychelles |
| 178 | Sierra Leone |
| 179 | Singapore |
| 180 | Slovakia (Slovak Republic) |
| 181 | Slovenia |
| 182 | Solomon Islands |
| 183 | Somalia |
| 184 | South Africa |
| 186 | Spain |
| 187 | Sri Lanka |
| 188 | Sudan |
| 189 | Suriname |
| 190 | Swaziland |
| 191 | Sweden |
| 192 | Switzerland |
| 193 | Syrian Arab Republic |
| 194 | Taiwan, China |
| 195 | Tajikistan |
| 196 | Tanzania |
| 197 | Thailand |
| 198 | Togo |
| 199 | Tokelau |
| 200 | Tonga |
| 201 | Trinidad and Tobago |
| 202 | Tunisia |
| 203 | Turkey |
| 204 | Turkmenistan |
| 205 | Turks and Caicos Islands |
| 206 | Tuvalu |
| 207 | Uganda |
| 208 | Ukraine |
| 209 | United Arab Emirates |
| 210 | United Kingdom |
| 211 | United States |
| 212 | Uruguay |
| 213 | Uzbekistan |
| 214 | Vanuatu |
| 215 | Vatican City State (Holy See) |
| 216 | Venezuela |
| 217 | Vietnam |
| 218 | Virgin Islands (British) |
| 219 | Virgin Islands (U.S.) |
| 220 | Wallis And Futuna Islands |
| 221 | Western Sahara |
| 222 | Yemen |
| 223 | Yugoslavia |
| 224 | Zambia |
| 225 | Zimbabwe |
