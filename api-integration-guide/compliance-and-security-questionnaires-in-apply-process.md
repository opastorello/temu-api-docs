# Compliance and security questionnaires in apply process

**Questions to focus on: **

## 

Compliance questionnaire:

![image](https://bstatic.kwcdn.com/open-outer/20237f3dc4/4da8ed74593f8fef086c6a46ba8f9376.png)

Question 1: This is about which country/region the business is located in. This needs to be the same as the DPA on the Seller Center. 

Question 2: This is about the country/region where user data authorization is granted. Multiple selections can be made. After the application is approved, other authorized countries/regions can be added. The selected countries/regions must match the domain (for example, EU domains can only apply for EU permissions), otherwise your submission will be rejected. You are recommended to select regions where orders may be potentially made in the future.

Question 3: This is about the country/region where servers processing users' personal data are located. Only non-Chinese cloud service providers are supported. The server location must match the platform region. US IPs cannot belong to EU countries, and vice versa.

Questions, 3, 4, and 5: The server location, cloud service provider, and IP must be the same. It is recommended that you use AWS or Microsoft Azure.

Multiple IPs can be configured, and only these IPs will be allowed to request APIs.

![image](https://bstatic.kwcdn.com/open-outer/20237f3dc4/47c7923a68893d7bb53576889af601c3.png)

(Optional, can be skipped). If the selected user country includes Europe (EEA, Switzerland, UK), compliance documents must be uploaded if personal data is transferred or stored in the US or a non-EU-adequate country:

a. What are adequacy decisions? 

[https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/adequacy-decisions_en](https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/adequacy-decisions_en)

b. What is DPF (Data Privacy Framework)? 

[https://www.dataprivacyframework.gov/](https://www.dataprivacyframework.gov/)

c. What is TIA (Transfer Impact Assessment)? 

[https://www.edps.europa.eu/data-protection/data-protection/reference-library/international-transfers_en](https://www.edps.europa.eu/data-protection/data-protection/reference-library/international-transfers_en)

d. List of EEA countries (30): 

[https://en.wikipedia.org/wiki/European_Economic_Area](https://en.wikipedia.org/wiki/European_Economic_Area)

e. Fully recognized countries (15): 

[https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/adequacy-](https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/adequacy-) decisions_en

## 

Security questionnaire:

![image](https://bstatic.kwcdn.com/open-outer/20237f3dc4/a70c64143860c1eefb9b20b308abc2f7.png)

Question 1: This is about whether user information is stored in an encrypted format. You are required to encrypt sensitive information and upload screenshots proving that storage is encrypted. If encryption is not used, your submission will be rejected. Base64 is not encryption and it is recommended that you use symmetric encryption such as AES instead.

**Answer sample**

1. Directly provide a screenshot of the database storage example.

![image](https://bstatic.kwcdn.com/open-outer/20237f7164/7d4849f29e210bc7e55d9d9123f50eac.jpg)

2. If you cannot provide a screenshot, please briefly describe the encryption method used for data storage.
