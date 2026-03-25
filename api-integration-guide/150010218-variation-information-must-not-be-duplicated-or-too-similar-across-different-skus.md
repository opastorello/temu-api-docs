# [150010218] Variation information must not be duplicated or too similar across different SKUs

| Error Code | Error Message |
|---|---|
| 150010218 | Variation information must not be duplicated or too similar across different SKUs |

- 

**Root cause:**

Two variants are considered same by Temu seller center.

For example, 

{"value":"Orange","parentSpecId":1001,"specId":204716906},{"value":"Orange","parentSpecId":1001,"specId":102683361},

Although 204716906 and 102683361 may represent different values in the Korean language, their displayed value in English is the same ("Orange"). As a result, the TEMU Seller Center will treat the corresponding SKUs as duplicate SKUs.

- 

**Next step:**

Please add the SKUs one by one and observe the system behavior. 

For example, add SKU1 with specId1 first to verify whether the API request succeeds. If it succeeds, then gradually add additional SKUs (such as SKU2) to identify which SKU combination triggers the error. This will help narrow down which two variants are conflicting and causing the duplicate issue.
