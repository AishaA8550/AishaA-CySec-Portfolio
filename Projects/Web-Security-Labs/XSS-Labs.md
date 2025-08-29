# Security Lab Report: Reflected XSS Exploitation

**Lab:** PortSwigger Web Security Academy - Lab #1

**Vulnerability:** Reflected Cross-Site Scripting (XSS)

**Difficulty:** Apprentice

**Status:** Solved

### 1. Objective
To successfully exploit a reflected XSS vulnerability in a web application's search function by achieving arbitrary JavaScript execution (`alert`).

### 2. Vulnerability Summary
The application's search feature directly reflected user input in the HTML response without any sanitization or encoding. This failure to treat user input as untrusted data allowed for the injection and execution of malicious scripts.

### 3. Proof of Concept
**Attack Vector:** HTTP GET Request Parameter (`search`).
**Payload:**
```html
<script>alert('XSS')</script>
```
**Execution:**
1.  The payload was submitted via the search bar.
2.  The server embedded the malicious script directly into the HTML response.
3.  The victim's browser interpreted the reflected `<script>` tag, executing the `alert()` function.

**Result:** Successful execution confirmed by the appearance of a JavaScript alert popup.

> <img width="1366" height="768" alt="Screenshot 2025-08-29 092149" src="https://github.com/user-attachments/assets/fdb1e74a-719f-4195-94f9-7492a0dc69e8" />



### 4. Key Takeaway
This lab demonstrates a classic XSS flaw where the failure to validate and encode user input creates a significant security risk, enabling client-side code execution.
