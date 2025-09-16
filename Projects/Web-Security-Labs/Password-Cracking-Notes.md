# Password Cracking with John the Ripper

## Overview
This document outlines the steps taken to crack password hashes using John the Ripper on Kali Linux, as part of a cybersecurity learning exercise.

## Tools Used
- Kali Linux VM
- John the Ripper (password cracking tool)
- Nano text editor

## Steps Performed

### 1. Installation
John the Ripper was installed on Kali Linux using the command:
```bash
sudo apt install john
```

### 2. Creating Hash File
Created a text file named `hashes.txt` containing sample hashes:
```bash
nano hashes.txt
```

File content:
```
admin:$1$admin$NxguBTkLJNYug6Ia
user1:5f4dcc3b5aa765d61d8327deb882cf99
```

### 3. Password Cracking Attempts

**First Attempt:**
```bash
john --format=md5 hashes.txt
```
Result: Error - Unknown ciphertext format

**Second Attempt (Correct Approach):**
Created a new file `new_hashes.txt` with only the MD5 hash:
```
user1:5f4dcc3b5aa765d61d8327deb882cf99
```

Ran John the Ripper with correct format specification:
```bash
john --format=raw-md5 new_hashes.txt
```

### 4. Results
Displayed cracked passwords:
```bash
john --show --format=raw-md5 new_hashes.txt
```

**Output:**
```
user1:password

1 password hash cracked, 0 left
```

## Findings
- Successfully cracked the MD5 hash: `5f4dcc3b5aa765d61d8327deb882cf99`
- The password for user1 was revealed to be: `password`
- This demonstrates the vulnerability of simple passwords and weak hashing algorithms like MD5


## Screenshots
> ![WhatsApp Image 2025-09-16 at 06 12 11_0cb7d33a](https://github.com/user-attachments/assets/95e7219a-52e1-4c39-972b-821bc6fa2204)


## Conclusion
This exercise demonstrated:
1. Basic usage of John the Ripper for password cracking
2. The importance of specifying correct hash formats
3. How weak passwords (like "password") can be easily cracked
4. The vulnerability of MD5 hashing for password storage

## Security Recommendations
- Use strong, complex passwords
- Implement modern hashing algorithms (e.g., bcrypt, Argon2)
- Use salt values with hashes
- Implement account lockout policies after failed attempts

---
