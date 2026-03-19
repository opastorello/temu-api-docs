# Deal With Second-Hand Products

**Last update:** 2026-01-28 00:15:23

Sellers selling second-hand products on the Temu platform must ensure compliance with all applicable laws, regulations, and platform policies.

---

## Steps to Publish a Second-Hand Product

**Prerequisites:** Your Temu store must be registered as a secondhand store before listing.

**Step 1:** Register a Temu seller account and obtain a store ID.

**Step 2:** Provide the following to your account manager:
- Store ID
- Proof of prior second-hand sales experience
- Planned sales sites
- Types of second-hand products to be sold (brand, category information)
- Proof of sourcing and procurement documentation
- Other supplementary information (brand authorization, product compliance documents)

**Step 3:** Select the product category (see Parameter configuration table below).

**Step 4:** Select the type of pre-owned product:
- **Regular Items**: Item primarily serves a basic functional purpose, no significant brand premium or scarcity.
- **Collectibles**: Cards, comics, etc. (requires authenticity documentation).
- **Luxury Items**: High-end branded goods (requires authenticity or authorization documentation).

If no type is specified, defaults to **Regular Items**.

---

## API Implementation

In `bg.local.goods.add`, the `secondHand` object:

```json
"secondHand": {
  "businessScope": 1,
  "secondHandGoods": true,
  "level": 1,
  "insName": "test",
  "grade": "test"
}
```

---

## Parameter Configuration for Different Categories

| `businessScope` | catId | `level` | `insName` | `grade` |
|---|---|---|---|---|
| `0`: Regular items | First-level categories: 17719, 13512, 4673, 653, 1464, 25439, 44933, 23177, 19858, 9711, 31148, 24389, 1, 54033, 27011 | 1, 2, 3, 4 | — | — |
| `0`: Regular items | First-level categories: 2542, 24252, 39316, 2096, 26207 | 1, 2, 3, 4, 5 | — | — |
| `1`: Collectibles | Leaf categories: 26032, 26033, 26034, 25624, 25622, 25625 | 21, 22, 23, 24 | — | — |
| `1`: Collectibles | Leaf categories: 26030, 31214, 31460, 31462, 31463, 31464, 31465, 31466, 31470, 31473, 31474, 31475, 31476, 31477, 31479 | 21, 25, 26, 27 | — | — |
| `1`: Collectibles (graded) | Same leaf categories above | — | PSA | 1–10 |
| `1`: Collectibles (graded) | Same leaf categories above | — | BGS | 1, 1.5, 2, ..., 10 |
| `1`: Collectibles (graded) | Same leaf categories above | — | SGC | 1, 1.5, 2, ..., 10 |
| `1`: Collectibles (graded) | Same leaf categories above | — | CGC | 1, 1.5, 2, ..., 10 |
| `2`: Luxury items | First-level categories: 17719, 13512, 4673, 653, 1464, 25439, 2542, 24252, 39316, 44933, 2096, 23177, 19858, 9711, 31148, 24389, 1, 54033, 27011, 26207 | 41, 42, 43, 44 | — | — |

**Rules:**
- When `catId` is a first-level category, all leaf subcategories support used condition configuration.
- For Collectibles, only one of `level` or `insName` can be selected. When using `insName`, `grade` must also be set.
- If `businessScope` is not provided, defaults to Regular items.

---

## Condition Levels (Regular Items & Luxury Items)

| `level` | Option Text | Condition Description |
|---|---|---|
| `1` | Used · Like New | Untouched, perfect condition. Original packaging intact. No signs of wear. Suitable as a gift. |
| `2` | Used · Very Good | Limited use, great condition. Complete instructions, may show minor wear. Works perfectly. |
| `3` | Used · Good | Shows wear from consistent use, good condition. Original instructions included. May be marked. Works perfectly. |
| `4` | Used · Fair | Fairly worn but works perfectly. Scratches, dents, aesthetic problems. Box/instructions may be missing. |
| `5` | Open Box | Brand new, never used. Original packaging opened/slightly damaged. All original accessories included. |
| `21` | Pre-owned · Near Mint or Better | Fresh pack with minimal visible wear. 1-3 slightly rounded corners. |
| `22` | Pre-owned · Lightly Played | Moderate chipping, indentations, slight scratches. Clean overall. |
| `23` | Pre-owned · Moderately Played | Noticeable flaws: heavy chipping, discoloration, scratches. No liquid damage. |
| `24` | Pre-owned · Heavily Played | Heavy wear, rounded/chipped corners, major discoloration, up to 30% liquid damage. |
| `25` | Pre-owned · Excellent | Visible wear, rough edges, minor scratches. |
| `26` | Pre-owned · Very Good | Moderate-to-heavy damage, discoloration, chipping, creases. |
| `27` | Pre-owned · Poor | Extremely worn, missing corners, major creases, stains, torn edges. |
| `41` | Pre-owned · Like New | Never worn or tried on. No flaws. Fully functional. Tags may be present or missing. |
| `42` | Pre-owned · Very Good | Worn a few times, very good condition, minimal signs of wear. Imperfections must be described. |
| `43` | Pre-owned · Good | Visible signs of use (fading, light wear, small stains). Flaws must be described. |
| `44` | Pre-owned · Fair | Clear signs of frequent use, visible wear or defects. May be missing non-essential parts. Flaws must be described. |

---

## Second-Hand Collectibles Grading Institutions

| `insName` | Full Name | Profile | `grade` Values | Certification Number Format |
|---|---|---|---|---|
| `PSA` | Professional Sports Authenticator | World's largest grading company. Covers sports cards and TCGs (Pokémon, MTG, Yu-Gi-Oh!). | 1–10 | Digits + "-", no letters. Usually 8+ digit numeric. |
| `BGS` | Beckett Grading Services | Well-known sports card grading, also grades Pokémon, Yu-Gi-Oh!, MTG. | 1, 1.5, 2, ..., 10 | Numbers only, multi-digit. |
| `SGC` | Sportscard Guaranty Corporation | Long history, sports cards and TCGs. | 1, 1.5, 2, ..., 10 | Numbers only. |
| `CGC` | Certified Guaranty Company | Started with comics and TCGs, now includes sports cards. | 1, 1.5, 2, ..., 10 | Pre-2023: 11-digit. Post-2023: 13-digit (starts with 1401xxxxxxxxx). |
