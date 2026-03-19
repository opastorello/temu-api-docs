# Deal With second-hand products

Sellers selling second-hand products on the Temu platform must ensure compliance with all applicable laws, regulations, and platform policies. 

### 

Steps to publish a second-hand product

1. 

Before listing secondhand items, you need to ensure that your Temu store has been registered as a secondhand store.

Sellers must possess prior experience in selling second-hand products and be able to prove that their products comply with laws, regulations, and platform policies. Before selling second-hand products to customers, your products must undergo inspection, refurbishment, cleaning, testing, and repackaging (if applicable).

To apply for the qualification to sell second-hand products, follow the process below:

Step 1: Register a Temu seller account and obtain a store ID

Step 2: Provide the following information to your account manager:

- Store ID;

- Proof of prior second-hand sales experience;

- Planned sales sites;

- Types of second-hand products to be sold (e.g., brand, category information);

- Proof of sourcing and procurement documentation for second-hand products;

- Other supplementary information, if applicable (e.g., brand authorization, product compliance documents).

For further assistance, please contact your account manager.

1. 

Select the product category. Please refer to the table for available categories of secondhand goods: [《Parameter configuration options for different categories of secondhand goods》](#parameter_configuration_options_for_different_categories_of_secondhand_goods)

1. 

Please select the type of pre-owned product you wish to list. There are three category options: 'Regular Items', 'Collectibles', and 'Luxury Items'.

  1. 

If the item primarily serves a basic functional purpose and does not carry a significant brand premium or scarcity, please select 'Regular Items'. Different pre-owned product types will require you to provide different product information. For 'Collectibles' and 'Luxury Items', you may need to provide documentation verfiying the item's authenticity or your authorization to list it.

  1. 

Selecting a pre-owned product type is optional. If no type is specified, the item will be treated as a 'Regular Item' by default.

  1. 

Different categories offer different types of secondhand goods, corresponding to the businessScope in the API.

1. 

When selecting the condition of a secondhand item,

  1. 

The options "Regular items" and "Luxury Items" can only be specified using the level in the API, indicating the item's condition.

  1. 

The options "Collectibles" can use either "level" or "insName + grade" to indicate the condition of the product.

### 

Sample Seller Center Secondhand Settings Page

![image](https://bstatic.kwcdn.com/open-outer/21a488b5e6/4b04aaf84a8cb5015de9908d804fcb9c)

API implementation of "Used product details" in bg.local.goods.add

```
"secondHand" : {  
    "businessScope" : 1,  
    "secondHandGoods" : true,  
    "level" : 1,  
    "insName" : "test",  
    "grade" : "test"  
}
```

![image](https://bstatic.kwcdn.com/open-outer/21a488b5e6/aadebeb8fdb8b26aa60ac09bc88bf54c)

### 

Parameter configuration options for different categories of secondhand goods

****

****

****

****

****

| businessScope | catId | level | insName | grade |
|---|---|---|---|---|
| 0: Regular items | First-level category:17719, 13512, 4673, 653, 1464, 25439, 44933, 23177, 19858, 9711, 31148, 24389, 1, 54033, 27011 | 1, 2, 3, 4 | - | - |
| first-level category:2542, 24252, 39316, 2096, 26207 | 1, 2, 3, 4, 5 | - | - |
| 1: Collectibles | Leaf Category:26032, 26033, 26034, 25624, 25622, 25625 | 21, 22, 23, 24 | - | - |
| Leaf Category:26030, 31214, 31460, 31462, 31463, 31464, 31465,31466, 31470, 31473, 31474, 31475, 31476, 31477, 31479 | 21, 25, 26, 27 | - | - |
| Leaf Category:26032, 26033, 26034, 25624, 25622, 2562526030, 31214, 31460, 31462, 31463, 31464, 31465,31466, 31470, 31473, 31474, 31475, 31476, 31477, 31479 | - | PSA | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 |
| - | BGS | 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, |
| - | SGC | 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, |
| - | CGC | 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, |
| 2: Luxury Items | first-level category:17719, 13512, 4673, 653, 1464, 25439, 2542, 24252, 39316, 44933, 2096, 23177, 19858, 9711, 31148, 24389, 1, 54033, 27011, 26207 | 41, 42, 43, 44 | - | - |

**Used item condition configuration rules:**

1. 

When `catId` in the table is a first-level category, all leaf subcategories under that first-level category support used condition configuration.

1. 

For Collectibles, only one of `level` or `insName` can be selected for configuration. When configuring `insName`, the corresponding `grade` must also be set.

1. 

If `businessScope` is not provided, the item defaults to Regular items.

### 

Specific quality description corresponding to level:：

****

****

****

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

| level | Option text | Condition Description |
|---|---|---|
| 1 | Used · Like New | An apparently untouched item in perfect condition.The original plastic wrap may be missing, but the original packaging is intact.There are absolutely no signs of wear.Suitable for presenting as a gift. |
| 2 | Used · Very Good | A well-cared-for item that has seen limited use but remains in great condition.The item and its instructions are complete and undamaged, but may show some signs of wear.The item works perfectly. |
| 3 | Used · Good | The item shows wear from consistent use, but remains in good condition.The original instructions are included, and are in acceptable condition.The item may bemarked or identified, and show other signs of previous use.The item works perfectly and is in good overall shape. |
| 4 | Used · Fair | The item is fairly worn, but it continues to work perfectly.The signs of wear can include scratches, dents and other aesthetic problems.The box and nonessential instructions may be missing or damaged.The item may be marked or identified, and show other signs of previous use. |
| 5 | Open Box | The item is in excellent condition, brand new with no signs of wear, and has never been used.The original packaging has been opened and may show minor damage, or the item may have been repackaged.All original accessories, including the user manual, are included. |
| 21 | Pre-owned ·Near Mint or Better | Equivalent to a fresh pack with minimal visible wear.May have 1-3 slightly rounded or soft corners and slightly rough edges.Any other damage lowers the card's condition. |
| 22 | Pre-owned · Lightly Played | May have moderate chipping, indentations, or surface scratches.Still looks clean overall and remains legal for play in a sleeved deck.Could show slight edge or corner wear. |
| 23 | Pre-owned · Moderately Played | Shows noticeable flaws like heavy edge or corner chipping, discoloration, scratches, or stains.May include creases, indentations, or visible surface wear, but no liquid damage.Can display signs of creasing or slight card layering. |
| 24 | Pre-owned · Heavily Played | Exhibits heavy wear with rounded, chipped, or damaged corners and edges.Shows major discoloration, scratches, stains, and multiple creases or wrinkles.May have edge or corner chipping, surface scuffing, and up to 30% liquid damage. |
| 25 | Pre-owned · Excellent | Shows visible signs of wear with rough edges and fuzzy corners.May have moderate chipping, minor discoloration, or slight indentations.Can display minor surface scuffing, edge chipping, or noticeable scratches. |
| 26 | Pre-owned · Very Good | Exhibits moderate-to-heavy damage across the card.May show discoloration, chipping, creases, indentations, or scratches.Could have slight paper loss, rounded edges, or soft corners. |
| 27 | Pre-owned · Poor | Extremely worn, often with missing or heavily rounded corners.Shows major creases, multiple scratches, stains, or heavy discoloration.May have torn edges or noticeable border wear. |
| 41 | Pre-owned · Like New | The item has never been worn or only tried on, with virtually no signs of use.No fading, stains, damage, pilling, or other flaws. Fully functional and looks brand new.Original tags may be present or missing. Packaging is intact or slightly damaged. |
| 42 | Pre-owned· Very Good | The item has been worn a few times but remains in very good overall condition.May show minimal signs of wear or handling, but no noticeable defects.All minor imperfections must be clearly described and displayed on the product page. |
| 43 | Pre-owned·Good | The item shows visible signs of use such as fading, light wear, small stains, or pilling, but remains in good condition.Fully functional and suitable for everyday wear, with no major damage.All flaws must be clearly described and displayed on the product page. |
| 44 | Pre-owned · Fair | The item shows clear signs of frequent use and visible wear or defects.May be missing non-essential parts, such as a detachable belt, but is still wearable.All flaws must be clearly described and displayed on the product page. |

### 

Second-hand collectibles institutions

****

****

****

****

****

****

| insName | Full name of the inspection company | Inspection company profile | grade | Certification number | Certification number description |
|---|---|---|---|---|---|
| PSA | Professional Sports Authenticator | The world’s largest company, with business covering sports cards (baseball, basketball, American football, etc.) and trading card games (Pokémon, Magic: The Gathering, Yu-Gi-Oh!, etc.). | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 | Digits + “-”, with no letters or other characters | Usually an 8-digit or longer numeric sequence, for example 81070909; historically, a “year-serial number” format was also used (such as 19-123456). The numbering generally increases sequentially in the order of submission. |
| BGS | Beckett Grading Services | A well-known sports card grading company that also extensively grades Pokémon, Yu-Gi-Oh!, Magic: The Gathering, and other trading cards. | 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, | Numbers only | A multi-digit numeric sequence with undisclosed rules. The number is printed at the bottom of the label and can be checked via the official website or app. |
| SGC | Sportscard Guaranty Corporation | With a long history, it initially focused on sports cards but has gradually expanded into trading card games as well. | 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, | Numbers only | A numeric sequence with an undisclosed structure. It can be looked up by entering the number on the SGC official website. |
| CGC | Certified Guaranty Company | It initially focused on comic books and trading card games, and after a merger, it also began grading sports cards. | 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, | Numbers only | Previously an 11-digit number (for example, starting with 2); since 2023 it has changed to a 13-digit number (for example, 1401xxxxxxxxx). The number is accompanied by a barcode or QR code and can be verified on the CGC official website. |
