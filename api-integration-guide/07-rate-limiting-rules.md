# Rate Limiting Rules

**Last update:** 2025-01-26 10:48:35

To ensure the stable operation of the open platform, rate limiting has been implemented for API requests. Typically, the initial rate limit for each `app_key` is set to **20 requests per second (qps)**.

## How to Find the Limit Rules

You can find information about the rate limiting rules in the platform's documentation.

## What Should I Do If I Hit the Rate Limit?

Rate limiting rules are dynamically adjustable. If you urgently need to increase your traffic, please contact Temu promptly via email at **partner@temu.com** or through other available channels.

Temu will urgently evaluate the reasonableness of a traffic increase upon receipt of your request and adjust traffic rules accordingly based on the evaluation results.

## Rate Limit Error

When the rate limit is exceeded, the API returns:
- **Error Code:** `4000004`
- **Error Msg:** `RATE_LIMIT_EXCEED_EXCEPTION`
- **Description:** The request exceeds the rate limit threshold.
