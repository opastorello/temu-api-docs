# Webhook Integration Guide

# 

Webhook Introduction

Webhook is a technical capability provided by the Temu Open Platform to improve the efficiency of information retrieval for developers. Unlike polling APIs, when a subscribed event generates a new message, the application receives a push notification from the open platform and then calls the query API to obtain detailed information. This approach not only enhances the timeliness of information acquisition but also effectively reduces the frequency of API calls.

# 

Conditions for Use

To receive message push notifications for a specific event, you need to complete the following steps:

1. 

**The application must be registered **(handled in partner platform)(Compliance and security assessment must be approved).

1. 

**The application has subscribed to the topics with valid push website** (handled in partner platform).

1. 

**The seller has granted authorization for the topics to the application** (handled by the seller through the Seller Center).

1. 

**The application has subscribed to the topics on behalf of the seller** (handled via API operations).

When all three conditions are met, the open platform will invoke the application's callback URL to send notifications for the event.

# 

Integration Process

**Process:Prepare Push Website➡️Subscribe to Events in Partner Platform➡️Seller Authorization➡️Call "Event Subscription" API➡️Receive webhook**

#### 

**Step 1: Prepare the Callback URL**

- 

Developers must prepare a callback URL to receive push messages from TEMU. 

- 

The callback URL **must use the HTTPS protocol**.

- 

Any configuration or modification of the callback URL requires an **approval process**.

---

#### 

**Step 2: Subscribe to Events in Partner Platform**

- 

Subscribe to events via the **Partner Platform > Webhook** in the Partner Platform.

![image](https://bstatic.kwcdn.com/open-outer/20ef5f4698/b20a38c10b318d9b2d7b29be499af6ba)

- 

**Complete Basic Information，**Select the event types you wish to receive via webhook.

  - 

Only apps that have been **approved** and passed the **Compliance and security assessment** are eligible

  - 

Manage event subscriptions. Toggle unwanted events to **"OFF"** to disable the Certain** **event from notifying.

  - 

For event details, refer to the document:[The event of webhook](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=0cc16b077a3343d08e87bc3c0a7593a8)

![image](https://bstatic.kwcdn.com/open-outer/20ef5f4698/e4e113a785e0b17bc5ac792622f843e8)

- 

**Submit for approval**. The approval process may take up to one week to complete. You can check the approval status in the Operation Log.

![image](https://bstatic.kwcdn.com/open-outer/20ef5f4698/3064bd58f2824fa8b14b01776f8bd110)

---

#### 

**Step 3: Seller Authorization**

- 

Guide sellers to authorize the required events for your application in the **Seller Center**, following the same process as API authorization.

![image](https://bstatic.kwcdn.com/open-outer/20ef5f4698/80b601c69ca20937bd8db0ab1268cfce)

---

#### 

**Step 4: Subscribe to Events for Sellers**

- 

Use the **Message Push API Group（**[**bg.tmc.message.update**](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=6e5817f037534093ba2dd91399aeff46)**） **to subscribe to events on behalf of the seller.

---

#### 

**Step 5: Receive Event Notifications**

- 

Once all the above steps are completed, developers will start receiving the latest event notifications from the open platform.You can click the **Test** button to verify whether the URL receives messages.

![image](https://bstatic.kwcdn.com/open-outer/20ef5f4698/17a314fbe1dfef25910527d7d8702a77)

# 

Callback Message Content

- 

**Request Type**: POST

The message is sent as a **POST** request to the developer's callback URL.

- 

**Message Content**: Header and Body

- 

**Header**

The notification sent from the TEMU Partner Center to the developer will include a signature in the HTTP request header, specifically in the `"x-tm-signature"` field. The signature is generated using the **HMAC-SHA256** algorithm, and developers are required to verify the signature to ensure the authenticity of the message.

**Header**

****

****

****

| Request Header | Type | Description |
|---|---|---|
| x-tm-app-key | String | appKey |
| x-tm-event-code | String | eventCode |
| x-tm-timestamp | String | Request timestamp (milliseconds) |
| x-tm-signature | String | Signature |
| x-tm-ext-param | String | Extension Information |
| Content-Type | String | application/json |

**Body**

****

****

****

****

****

****

``

```
  
  

```

****

```
  
  
  

```

| Name | Type | Description | Example |
|---|---|---|---|
| eventData | String | Encrypted Content，Decrypted JSON format data, fields consistent with the gateway API format: camel case format. | Encrypted ContentIn the request, the encrypted content is returned in the eventData field.Encrypted data:{    "eventData": "sQmNTAKR2o4HrmCO3OchFgGyJU5Qta57+JQxxgVyVPU="}Decrypted Format:{    "orderSn": "XXYYZZ",    "status": 1} |

### 

Signature Rules

To prevent malicious tampering during the callback process, every URL request must carry a request signature. The external service provider's server must verify the signature based on the request parameters and reject any request with an invalid signature.

The supported signature algorithm is: **HMAC-SHA256** (`sign_method=HMAC-SHA256`), and the signing process is as follows:

- 

The request parameters in the **Header**: `x-tm-app-key`, `x-tm-event-code`, `x-tm-timestamp`,  `eventData` and `x-tm-ext-param` parameter (decrypted data) in the **Body**.

- 

Sort the parameters by their names in ascending order.

- 

Concatenate the sorted parameters into a single string, where each key-value pair is concatenated in the form of `key=value` without any additional characters between them.

- 

After concatenating the parameters, generate a single long string containing all the key-value pairs.

- 

Finally, apply the **HMAC-SHA256** algorithm to the concatenated string to generate the signature. The resulting **HMAC-SHA256** value is then **HEX-encoded** to produce the signature (`sign` value).

**Example**

1. 

**Your application secret key** is `12345678abcdefgh`.

1. 

Decrypt the `eventData` to get the original data.

1. 

Suppose the message content is:

```
{  
  "orderSn": "XXYYZZ",  
  "status": 1  
}
```

1. 

According to the rules, concatenate the following values as the base string for the signature (without any formatting when concatenating):

```
eventData{"orderSn":"XXYYZZ","status":1}x-tm-app-keydemo-test-appx-tm-event-codebg_test_eventx-tm-ext-param{}x-tm-timestamp1726127013525
```

1. 

Use your **application secret key** (`12345678abcdefgh`) for the signature.

1. 

Pass the base string and the signature key into the **HMAC-SHA256** hashing algorithm to calculate the signature. The result will be:

```
b5143d1a831453afbcf76d4621baa74a2dc07a486f26f5a956c6e50c61a338fb
```

### 

Signature & Decryption Tool

```
import com.fasterxml.jackson.databind.DeserializationFeature;  
import com.fasterxml.jackson.databind.ObjectMapper;  
import com.google.common.collect.Maps;  
import com.google.common.util.concurrent.ThreadFactoryBuilder;  
import org.apache.commons.lang3.StringUtils;  
import org.slf4j.Logger;  
import org.slf4j.LoggerFactory;  
import org.springframework.http.ResponseEntity;  
import org.springframework.util.Base64Utils;  
import org.springframework.web.bind.annotation.PostMapping;  
import org.springframework.web.bind.annotation.RequestBody;  
import org.springframework.web.bind.annotation.RequestMapping;  
import org.springframework.web.bind.annotation.RestController;  
  
import javax.crypto.Cipher;  
import javax.crypto.Mac;  
import javax.crypto.spec.IvParameterSpec;  
import javax.crypto.spec.SecretKeySpec;  
import javax.servlet.http.HttpServletRequest;  
import java.io.IOException;  
import java.io.Serializable;  
import java.security.Key;  
import java.util.Arrays;  
import java.util.HashMap;  
import java.util.Map;  
import java.util.TreeMap;  
import java.util.concurrent.ExecutorService;  
import java.util.concurrent.LinkedBlockingQueue;  
import java.util.concurrent.ThreadPoolExecutor;  
import java.util.concurrent.TimeUnit;  
  
@RestController  
public class PushMessageTestController {  
  
    private static Logger logger = LoggerFactory.getLogger(PushMessageTestController.class);  
    /**  
     * Your secret key  
     */  
    private static final String TEST_APP_SECRET = "12345678abcdefgh";  
  
    public static final String X_TM_APP_KEY = "x-tm-app-key";  
    /**  
     * Timestamp request header  
     */  
    public static final String X_TM_TIMESTAMP = "x-tm-timestamp";  
    /**  
     * Signature request header  
     */  
    public static final String X_TM_SIGNATURE = "x-tm-signature";  
    /**  
     * Event name  
     */  
    public static final String X_TM_EVENT_CODE = "x-tm-event-code";  
      
    public static final String X_TM_EXT_PARAM = "x-tm-ext-param";  
  
    public static final String X_TM_BODY_KEY = "eventData";  
  
    private final ExecutorService executor = new ThreadPoolExecutor(10, 10,  
            0L, TimeUnit.MILLISECONDS,  
            new LinkedBlockingQueue<>(1024),  
            new ThreadFactoryBuilder().setNameFormat("sync-msg-processor-%d").build());  
  
    /**  
     * Accept message push callback  
     *  
     * @param request  
     * @return  
     */  
    @PostMapping(value = "/pushMessageCallBack", consumes = {"application/json"})  
    public ResponseEntity<?> pushMessageCallBack(HttpServletRequest request, @RequestBody EventCallbackRequest callbackRequest) {  
        String signature = null == request.getHeader(X_TM_SIGNATURE) ? null : request.getHeader(X_TM_SIGNATURE);  
        Map<String, String> headers = getHeaders(request);  
        String eventData = callbackRequest.getEventData();  
        logger.info("pushMessageCallBack headers value:{} eventData:{}", JsonUtils.toJson(headers), eventData);  
        String decryptData = AESTools.decrypt(eventData, TEST_APP_SECRET);  
        boolean checkSign = SignHandler.checkSign(genSignMap(headers, decryptData), TEST_APP_SECRET, signature);  
        if (!checkSign) {  
            return ResponseEntity.badRequest().body("Signature is not valid");  
        }  
        String eventCode = headers.get(X_TM_EVENT_CODE);  
        if (StringUtils.isNotEmpty(eventCode) && JsonUtils.isLegalJson(decryptData)) {  
            executor.execute(() -> handler(eventCode, decryptData));  
        } else {  
            logger.info("The message format is invalid. eventData:{} ", decryptData);  
            return ResponseEntity.badRequest().build();  
        }  
        return ResponseEntity.ok().body(newSuccessMap());  
    }  
  
    private void handler(String eventCode, String decryptData) {  
        logger.info("pushMessageCallBack handler success");  
        // Business code  
    }  
  
    private Map<String, String> genSignMap(Map<String, String> headers, String eventData) {  
        Map<String, String> signMap = new HashMap<>(headers);  
        signMap.put(X_TM_BODY_KEY, eventData);  
        return signMap;  
    }  
  
    /**  
     * Get gateway authentication parameters from request  
     */  
    private static Map<String, String> getHeaders(HttpServletRequest request) {  
        Map<String, String> headers = new HashMap<>();  
        headers.put(X_TM_APP_KEY, request.getHeader(X_TM_APP_KEY));  
        headers.put(X_TM_TIMESTAMP, request.getHeader(X_TM_TIMESTAMP));  
        headers.put(X_TM_EVENT_CODE, request.getHeader(X_TM_EVENT_CODE));  
        headers.put(X_TM_SIGNATURE, request.getHeader(X_TM_SIGNATURE));  
        headers.put(X_TM_SIGNATURE, request.getHeader(X_TM_EXT_PARAM));  
        return headers;  
    }  
  
    /**  
     * Construct return result  
     * @return  
     */  
    public static Map<String, Object> newSuccessMap() {  
        Map<String, Object> retMap = Maps.newHashMap();  
        retMap.put("result", new HashMap<>());  
        return retMap;  
    }  
  
    /**  
     * AES encryption and decryption tool  
     */  
    public static class AESTools {  
  
        private static final String UTF_8 = "utf-8";  
        private static final String KEY_ALGORITHM = "AES";  
  
        /**  
         * Default encryption algorithm  
         */  
        private static final String DEFAULT_CIPHER_ALGORITHM = "AES/CBC/PKCS5Padding";  
  
        /**  
         * AES encryption operation  
         *  
         * @param content          Content to be encrypted  
         * @param key              Encryption password  
         * @return Returns Base64 encoded encrypted data string  
         */  
        public static String encrypt(String content, String key) {  
            if (content == null || content.length() == 0  
                    || key == null || key.length() == 0 ) {  
                throw new IllegalArgumentException("Content/Key cannot be empty");  
            }  
            if (key.getBytes().length < 16) {  
                throw new IllegalArgumentException("Key length cannot be less than 16 bytes");  
            }  
            try {  
                // Create cipher  
                Cipher cipher = Cipher.getInstance(DEFAULT_CIPHER_ALGORITHM);  
                byte[] byteContent = content.getBytes(UTF_8);  
                byte[] ivSeedBytes = key.getBytes();  
                byte[] ivBytes = new byte[16];  
                System.arraycopy(ivSeedBytes, 0, ivBytes, 0, 16);  
  
                IvParameterSpec ivSpec = new IvParameterSpec(ivBytes);  
                // Initialize cipher in encryption mode  
                cipher.init(Cipher.ENCRYPT_MODE, getSecretKey(key), ivSpec);  
                // Encrypt  
                byte[] result = cipher.doFinal(byteContent);  
                // Return Base64 encoded  
                return java.util.Base64.getEncoder().encodeToString(result);  
            } catch (Exception ex) {  
                logger.warn("AES encryption failed:{}", ex);  
                throw new RuntimeException("AES encryption failed");  
            }  
        }  
  
        /**  
         * @param key   the key  
         * @return  
         */  
        private static Key getSecretKey(String key) {  
            try {  
                return new SecretKeySpec(Arrays.copyOf(key.getBytes(UTF_8), 16), KEY_ALGORITHM);  
            } catch (Exception ex) {  
                logger.warn("AES encryption key generation failed:{}", ex);  
                throw new RuntimeException("AES encryption key generation failed", ex);  
            }  
        }  
  
        /**  
         * AES decryption operation  
         *  
         * @param content         The encrypted string in BASE64 format  
         * @param decryptKey      The key  
         * @return Decrypted result string  
         */  
        public static String decrypt(String content, String decryptKey) {  
            if (content == null || content.length() == 0 || decryptKey == null || decryptKey.length() == 0) {  
                throw new IllegalArgumentException("Ciphertext and key cannot be empty");  
            }  
            if (decryptKey.getBytes().length < 16) {  
                throw new IllegalArgumentException("Key length cannot be less than 16 bytes");  
            }  
            try {  
                // Instantiate  
                Cipher cipher = Cipher.getInstance(DEFAULT_CIPHER_ALGORITHM);  
                byte[] ivSeedBytes = decryptKey.getBytes();  
                byte[] ivBytes = new byte[16];  
                System.arraycopy(ivSeedBytes, 0, ivBytes, 0, 16);  
                IvParameterSpec ivSpec = new IvParameterSpec(ivBytes);  
                cipher.init(Cipher.DECRYPT_MODE, getSecretKey(decryptKey), ivSpec);  
                // First decode with base64  
                byte[] original = cipher.doFinal(Base64Utils.decode(content.getBytes()));  
                return new String(original, "utf-8");  
            } catch (Exception ex) {  
                logger.warn("AES decryption failed:{}", ex);  
            }  
  
            return null;  
        }  
  
    }  
  
    public static class SignHandler {  
  
        public static boolean checkSign(Map<String, String> requestParams, String clientSecret, String sign) {  
            String valid = sign(getSignMap(requestParams), clientSecret);  
            logger.info("valid sign:{}", valid);  
            return sign != null && sign.equals(valid);  
        }  
  
        private static Map<String, String> getSignMap(Map<String, String> bodyMap) {  
            Map<String, String> signMap = Maps.newHashMap();  
            for (String k : bodyMap.keySet()) {  
                if (StringUtils.equals(X_TM_SIGNATURE, k)) {  
                    continue;  
                }  
                signMap.put(k, bodyMap.get(k));  
            }  
            return signMap;  
        }  
  
        /**  
         * Construct the original signature string  
         * When requestParams is null or empty, the original string is empty  
         *  
         * @param requestParams : Request parameters  
         * @return  
         */  
        public static String buildSignSource(Map<String, String> requestParams) {  
            if (null == requestParams || requestParams.isEmpty()) {  
                return "";  
            }  
  
            Map<String, String> signSrcMap = requestParams;  
            // If not TreeMap, convert to TreeMap mainly for key sorting  
            if (!(requestParams instanceof TreeMap)) {  
                signSrcMap = new TreeMap<>(requestParams);  
            }  
            // Construct the original signature string  
            StringBuilder sb = new StringBuilder();  
            for (Map.Entry<String, String> entry : signSrcMap.entrySet()) {  
                if (StringUtils.isBlank(entry.getValue()) || X_TM_SIGNATURE.equals(entry.getKey())) {  
                    continue;  
                }  
                sb.append(entry.getKey()).append("=").append(entry.getValue()).append("&");  
            }  
            // Remove the last '&'  
            if (sb.length() > 0) {  
                sb.delete(sb.length() - 1, sb.length());  
            }  
            return sb.toString();  
        }  
  
        public static String sign(Map<String, String> params, String clientSecret) {  
            String signSource = buildSignSource(params);  
            return getHmacSHA256(signSource, clientSecret);  
        }  
  
        private static String getHmacSHA256(String data, String key) {  
            try {  
                Mac mac = Mac.getInstance("HmacSHA256");  
                SecretKeySpec secretKey = new SecretKeySpec(key.getBytes("UTF-8"), "HmacSHA256");  
                mac.init(secretKey);  
                byte[] hash = mac.doFinal(data.getBytes("UTF-8"));  
                return bytesToHex(hash);  
            } catch (Exception e) {  
                logger.warn("HMAC SHA256 sign failed:{}", e);  
                return null;  
            }  
        }  
  
        public static String bytesToHex(byte[] bytes) {  
            StringBuilder sb = new StringBuilder();  
            for (byte b : bytes) {  
                sb.append(String.format("%02x", b));  
            }  
            return sb.toString().toUpperCase();  
        }  
    }  
  
    public static class JsonUtils {  
  
        private static final ObjectMapper objectMapper = new ObjectMapper();  
        static {  
            objectMapper.configure(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, false);  
        }  
  
        /**  
         * Convert object to JSON string  
         *  
         * @param obj object  
         * @return JSON string  
         */  
        public static String toJson(Object obj) {  
            try {  
                return objectMapper.writeValueAsString(obj);  
            } catch (IOException e) {  
                logger.error("JSON serialization failed", e);  
            }  
            return null;  
        }  
  
        public static boolean isLegalJson(String json) {  
            try {  
                objectMapper.readTree(json);  
                return true;  
            } catch (IOException e) {  
                logger.error("Invalid JSON", e);  
            }  
            return false;  
        }  
    }  
  
    public static class EventCallbackRequest implements Serializable {  
        private static final long serialVersionUID = 1L;  
  
        private String eventData;  
  
        public String getEventData() {  
            return eventData;  
        }  
  
        public void setEventData(String eventData) {  
            this.eventData = eventData;  
        }  
    }  
}
```

### 

Example Callback data 

**HTTP Request**

```
POST /pushMessageCallBack HTTP/1.1  
Host: www.baidu.com  
x-tm-app-key: demo-test-app  
x-tm-event-code: bg_test_event  
x-tm-timestamp: 1726127013525  
x-tm-signature: 987875c01ea5c7f608502fb92e1de102c59e1c9195c010ab8a80bdb501a04fbc  
x-tm-ext-param: {}  
Content-Type: application/json  
Content-Length: 69
```

**Body (JSON)**

```
{  
  "eventData": "sQmNTAKR2o4HrmCO3OchFgGyJU5Qta57+JQxxgVyVPU="  
}
```

**Breakdown of the Headers**

- 

`x-tm-app-key`: The application key (`demo-test-app`).

- 

`x-tm-event-code`: The event code (`bg_test_event`).

- 

`x-tm-ext-param`: The extention information (`{}` ).

- 

`x-tm-timestamp`: The timestamp when the request was sent (`1726127013525`).

- 

`x-tm-signature`: The signature used to verify the integrity and authenticity of the request (`987875c01ea5c7f608502fb92e1de102c59e1c9195c010ab8a80bdb501a04fbc`).

- 

`Content-Type`: The type of content in the body (`application/json`).

- 

`Content-Length`: The length of the request body in bytes (`69`).

**Decrypted **`**eventData**`

The `eventData` field contains a Base64-encoded string that is encrypted. It would be decrypted using the provided secret key (`TEST_APP_SECRET`), which is done by the `AESTools.decrypt` method in your code. The encrypted string is:

```
sQmNTAKR2o4HrmCO3OchFgGyJU5Qta57+JQxxgVyVPU=
```

This Base64-encoded string would need to be decrypted using AES with the appropriate key and IV, and then the result would be the plaintext data related to the event.

### 

**Activate or deactivate event subscriptions**

Interface input parameters：bg.tmc.message.update

- 

  - 

- 

  - 

| parameter interface | Type | require | desc |
|---|---|---|---|
| cancelEventCodeList | LIST | false | Cancel store subscription event list, maximum quantity 20 |
| $item | STRING | false |  |
| permitEventCodeList | LIST | false | Add store subscription event list, maximum quantity 20-bg_order_status_change_event-bg_trade_logistics_address_changed-bg_aftersales_status_change-bg_cancel_order_status_change |
| $item | STRING | false |  |

### 

Success and Failure Retrying

**Acknowledgment Mechanism**

Currently, the client is required to return a `200` status code to acknowledge the receipt of data. If the server does not receive the `200` response within 500 milliseconds, it considers the message delivery as failed. In case of failure, the message will be retried at intervals: 2 minutes, 10 minutes, 30 minutes, 1 hour, 1 hour, 1 hour, 12 hours, and 12 hours. The system will attempt up to 8 retries before completely giving up on the message push.

**Recommended Handling Approach**

To minimize system resource consumption caused by retries, it is recommended that the receiving application buffers the incoming messages and processes them later, rather than processing them synchronously. Additionally, due to potential network issues or other uncertainties, relying solely on message callbacks is not advisable. It is crucial to implement business logic that involves periodic tasks, such as pulling orders, to ensure robustness.

 after being pushed into the consumption queue.
