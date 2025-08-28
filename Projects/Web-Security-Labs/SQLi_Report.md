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

---

## Lab 3: Find How Many Columns a Query Has
*   **Goal:** Figure out how many columns the website's SQL query uses so I can perform a UNION attack.
*   **How:** I used the `ORDER BY` trick to cause an error, which revealed the limit.
*   **The Fix:** I kept adding `' ORDER BY 1--`, `' ORDER BY 2--`, `' ORDER BY 3--` until the website broke on `' ORDER BY 4--`. This meant there are **3 columns**.
*   **Result:** I confirmed the query returns 3 columns, which is the first step to stealing data with a UNION attack.
*   **Proof:**
> <img width="1366" height="768" alt="Screenshot 2025-08-28 080812" src="https://github.com/user-attachments/assets/e3780080-439d-4b3b-902c-d591f4a97cb2" />

> <img width="1366" height="768" alt="Screenshot 2025-08-28 080709" src="https://github.com/user-attachments/assets/70a32992-23c2-45b2-a42a-1501c248dea0" />


---
## Lab 4: Find Which Column Can Hold Text
*   **Goal:** Discover which of the 3 columns can display text data stolen from the database.
*   **How:** I used `UNION SELECT` with `NULL` values and replaced them one-by-one with a letter.
*   **The Fix:** I injected `' UNION SELECT NULL,'a',NULL--`. The letter **'a'** appeared on the page, proving the **second column** can hold text.
*   **Result:** I found the perfect column to use for extracting usernames and passwords.
*   **Proof:**
> <img width="572" height="768" alt="Screenshot 2025-08-28 082217" src="https://github.com/user-attachments/assets/e35e6568-481d-4f7a-96d1-415fd1452b33" />

> <img width="1366" height="768" alt="Screenshot 2025-08-28 082202" src="https://github.com/user-attachments/assets/08ef9e90-6001-4c5f-8a0a-a111b5acb4d1" />

---
## Lab 5: Steal All Usernames and Passwords
*   **Goal:** Extract the login credentials for every user in the database.
*   **How:** I used a UNION attack to pull data from the `users` table into the text column I found earlier.
*   **The Fix:** I injected: `' UNION SELECT NULL,username||':'||password,NULL FROM users--`
    *   This combines the `username` and `password` into one string (like `admin:password123`) and puts it in the second column.
*   **Result:** The website displayed the full list of usernames and passwords right on the page.
*   **Proof:**
> <img width="1366" height="768" alt="Screenshot 2025-08-28 083312" src="https://github.com/user-attachments/assets/27808847-5888-4e9d-86fd-13f388f05b87" />

><img width="1366" height="768" alt="Screenshot 2025-08-28 083346" src="https://github.com/user-attachments/assets/26ab8c23-59c0-44bc-8e20-5aa68e08357a" />


**In Summary:** SQL injection remains a critical threat. Demonstrating these fundamental techniques highlights the importance of strict input validation and using prepared statements in all database interactions.
