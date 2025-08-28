# SQL Injection Report

I completed two basic SQL injection labs. Here's what I did.

## Lab 1: Show Hidden Products
*   **Goal:** Make the website show all products, including hidden ones.
*   **How:** I changed the URL parameter to break the SQL query.
*   **The Fix:** I added `' OR 1=1--` to the category.
    *   The `'` closes the string.
    *   `OR 1=1` makes the query always true.
    *   `--` comments out the rest of the query that would hide products.
*   **Result:** It worked. All products were displayed.
*   **Proof:**
>    <img width="1366" height="768" alt="Screenshot 2025-08-27 070352" src="https://github.com/user-attachments/assets/428d0174-9a42-4f20-9008-842cbf453749" />
>    <img width="1366" height="768" alt="Screenshot 2025-08-27 070457" src="https://github.com/user-attachments/assets/5f9c89c9-5219-45c1-8396-95c83f3f9d31" />


## Lab 2: Login Without Password
*   **Goal:** Log in as the administrator without knowing the password.
*   **How:** I used SQL injection in the login box to bypass the password check.
*   **The Fix:** I typed `administrator'--` in the username field and left the password blank.
    *   This makes the database only check for the username `administrator` and ignores the password completely.
*   **Result:** I successfully logged in as the administrator.
*   **Proof:**
>   <img width="1366" height="768" alt="Screenshot 2025-08-27 072942" src="https://github.com/user-attachments/assets/9247d5f0-d7c1-4f85-9704-7c843c8a116a" />


**In Summary:** SQL injection remains a critical threat. Demonstrating these fundamental techniques highlights the importance of strict input validation and using prepared statements in all database interactions.
