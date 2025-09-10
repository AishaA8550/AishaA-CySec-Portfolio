# Insecure Direct Object Reference (IDOR) Vulnerability in Chat Transcript Download

## Vulnerability Details

| | |
|----------|----------|
| **Title** | Insecure Direct Object Reference in Chat Transcript Download Function |
| **Type** | Insecure Direct Object Reference (IDOR) |
| **Threat** | Medium |
| **CVSS Score** | 6.5 (Medium) |
| **Affected URL** | `https://0a19004e048febd487df064600150008.web-security-academy.net` |
| **Endpoint** | `/download-transcript/1.txt` |

## Description
An Insecure Direct Object Reference (IDOR) vulnerability was identified in the support chat application's transcript download feature. The application uses a predictable sequential filename (`1.txt`, `2.txt`) to serve chat transcripts without performing any authorization checks. This allows any user to download the confidential chat transcripts of other users by simply incrementing or decrementing the filename in the download URL.

## Proof of Concept (PoC)

### Steps to Reproduce:
1.  Log in to the application with your assigned user credentials.
2.  Initiate a live chat with support and then end the chat.
3.  On the chat history page, a link is provided to download your transcript: `https://0a19004e048febd487df064600150008.web-security-academy.net/download-transcript/2.txt`
4.  Observe that the URL contains your transcript filename (`2.txt`).
5.  Change the filename in the URL from `2.txt` to `1.txt`.
6.  Access the new URL: `https://0a19004e048febd487df064600150008.web-security-academy.net/download-transcript/1.txt`
7.  The application will successfully download the chat transcript for the user who had the previous chat session (e.g., `carlos`), revealing their entire conversation with support.

### Supporting Evidence:
**Request to download another user's transcript:**
```http
GET /download-transcript/1.txt HTTP/2
Host: 0a19004e048febd487df064600150008.web-security-academy.net
Cookie: session=LAwGTX5YreUD4BdPOVACe43DGLqPTHIF
````
**Response:**
```http
HTTP/2 200 OK
Content-Type: text/plain
Content-Disposition: attachment; filename="1.txt"

[The server responded with a 200 OK status and the full contents of the user's chat transcript, confirming the vulnerability. The actual file content is redacted to protect sensitive information.]
````

## Impact
An attacker can:
-   Access the private and potentially sensitive support chat history of any other user.
-   Harvest personal information, password hints, or other confidential details disclosed during the chat sessions.
-   Use the gathered information to perform further attacks, such as social engineering or account takeover.

## Remediation Recommendations
1.  Implement access control checks. Before serving a file, verify that the currently authenticated user is authorized to access the requested transcript.
2.  Use unpredictable identifiers. Instead of sequential numbers (1,2,3), use long, random, unique tokens for each file (e.g., `download-transcript/AbCdEf123GhIjKlMnOp.txt`).
3.  Map users to their resources on the server-side. Maintain a database table that links user IDs to their corresponding transcript filenames.

## References
-   [OWASP IDOR Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Insecure_Direct_Object_Reference_Prevention_Cheat_Sheet.html)
-   [PortSwigger Web Security Academy: IDOR Lab](https://portswigger.net/web-security/access-control/lab-insecure-direct-object-references)

## Timeline
-   **Date Discovered**: October 26, 2023
-   **Report Created**: October 26, 2023
