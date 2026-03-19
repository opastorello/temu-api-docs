# Common Parameters

**Last update:** 2025-01-26 09:58:41

---

# 
Common Parameters

- 
Common parameters are the parameters that must be passed in when calling any open API. The current Common parameters are as follows:

| 

**Parameters**  
 | 

**Type**
 | 

**Required**
 | 

**Description** 
 
| 

**type**
 | 

STRING
 | 

Y
 | 

API interface name, such as: bg.*
 
| 

**app_key**
 | 

STRING
 | 

Y
 | 

app_key has been successfully created . Contact the operator for issuance
 
| 

**timestamp**
 | 

STRING
 | 

Y
 | 

Timestamp, in UNIX time format (seconds), 10 digits long, current time - 300 seconds <= input time <= current time + 300 seconds
 
| 

**sign**
 | 

STRING
 | 

Y
 | 

The API input parameter signature, the signature value is calculated according to the following algorithm
 
| 

**access_token**
 | 

STRING
 | 

Y
 | 

User authorization token access_token , can be obtained from Seller Center, and the operation will issue the corresponding online store token
 
| 

**data_type**
 | 

STRING
 | 

Y
 | 

The data format returned by the request, the optional parameters are fixed as JSON
 
| 

**version**
 | 

STRING
 | 

N
 | 

The default API version is V1. If no requirement is set, this parameter is not passed.
 
# 
Requests Parameters

In addition to common parameters, API requests must also include request-level parameters if the API itself has them. For detailed descriptions of each API's request parameters, please refer to the corresponding API documentation.
