## Linux Bandit Walkthrough: Levels 0-11

### Level 0 → Level 1
**Learning Objective:** Basic file reading.

**Command:**
```bash
cat readme
```
**Key Takeaway:** The `cat` (concatenate) command is the primary tool for outputting the contents of a file to the standard output (stdout).

**Screenshot:**
> <img width="1366" height="768" alt="0-1BANDIT" src="https://github.com/user-attachments/assets/dba2e371-8224-4056-aa4e-527b290246da" />


---

### Level 1 → Level 2
**Learning Objective:** Handling filenames with special characters.

**Challenge:** The filename is a single dash (`-`), which the shell interprets as standard input (stdin).

**Solution:** Prefix the filename with its path (`./`) to clarify it's a file in the current directory.

**Command:**
```bash
cat ./-
```
**Key Takeaway:** Using `./` before a filename prevents the shell from interpreting special characters as commands or flags.

**Screenshot:**
> <img width="1366" height="768" alt="1-2BANDIT" src="https://github.com/user-attachments/assets/19f8d4bb-e792-451f-8b56-afc92b94fd79" />


---

## Level 2 → Level 3
***Learning Objective:*** Handling filenames with spaces and leading special characters.

***Challenge:*** The filename contains spaces and starts with dashes (`--spaces in this filename--`), which are interpreted as command options.

***Solution:*** Use `--` to signal the end of command options and escape the spaces with a backslash (`\`).

***Command:***
```bash
cat -- --spaces\ in\ this\ filename--
```
***Key Takeaway:*** The `--` argument is a crucial tool for handling filenames that begin with hyphens. Escaping spaces with `\` ensures the shell treats the entire name as a single argument.

**Screenshot:**
> <img width="1366" height="768" alt="2-3BANDIT" src="https://github.com/user-attachments/assets/06bcfbaa-5b8a-444b-8391-b6c5ae3efa96" />


---

### Level 3 → Level 4
**Learning Objective:** Finding and reading hidden files.

**Challenge:** The password is stored in a hidden file.

**Solution:** Use `ls -a` to list all files, including hidden ones (which start with a dot `.`).

**Commands:**
```bash
ls -la inhere/
cat inhere/...hiding-from-you
```
**Key Takeaway:** The `-a` flag for `ls` is crucial for revealing hidden files and directories.

**Screenshot:**
> <img width="1366" height="768" alt="3-4BANDIT" src="https://github.com/user-attachments/assets/2b203606-77ed-4422-a190-a6e9944fcfdd" />


---

### Level 4 → Level 5
**Learning Objective:** Identifying file types.

**Challenge:** The password is in the only human-readable file among many non-readable files.

**Solution:** Use the `file` command to determine the type of each file.

**Commands:**
```bash
cd inhere
file ./*
cat ./-file07 # (The specific filename identified as 'ASCII text')
```
**Key Takeaway:** The `file` command is an essential tool for inspecting file contents.

**Screenshot:**
> <img width="1366" height="768" alt="4-5 BANDIT" src="https://github.com/user-attachments/assets/9d8ecf11-1301-4c8d-999d-92e1780639fd" />


---

### Level 5 → Level 6
**Learning Objective:** Using the `find` command with specific criteria.

**Challenge:** Find a file that is human-readable, 1033 bytes in size, and not executable.

**Solution:** Use `find` with the `-size`, `-type`, and `! -executable` flags.

**Command:**
```bash
find . -type f -size 1033c ! -executable
cat ./maybehere07/.file2 # (The path returned by find)
```
**Key Takeaway:** The `find` command is powerful for locating files based on exact attributes.

**Screenshot:**
> <img width="1366" height="768" alt="5-6BANDIT" src="https://github.com/user-attachments/assets/593d4897-b787-4495-9a33-1ebf57d1927b" />


---

### Level 6 → Level 7
**Learning Objective:** Filtering file content with `grep`.

**Challenge:** The password is next to the word "millionth" in a large file.

**Solution:** Pipe the output of `cat` into `grep` to search for a specific string.

**Command:**
```bash
cat data.txt | grep "millionth"
```
**Key Takeaway:** `grep` is the fundamental tool for searching text. The pipe (`|`) sends output from one command to another.

**Screenshot:**
> <img width="774" height="280" alt="6-7BANDIT" src="https://github.com/user-attachments/assets/4de4152b-ab61-455e-850b-50eda79e80f2" />

---

### Level 7 → Level 8
**Learning Objective:** Finding a unique line in a file.

**Challenge:** The password is the only line of text that occurs only once.

**Solution:** Sort the lines with `sort` and then use `uniq -u` to find the unique line.

**Command:**
```bash
cat data.txt | sort | uniq -u
```
**Key Takeaway:** Combining `sort` and `uniq` is a classic pattern for analyzing text.

**Screenshot:**
> <img width="1366" height="768" alt="7-8BANDIT" src="https://github.com/user-attachments/assets/86b3a2c9-b28a-4ba0-b805-a9b1d6da1940" />

---

### Level 8 → Level 9
**Learning Objective:** Extracting human-readable strings from a binary file.

**Challenge:** The password is a human-readable string preceded by several ‘=’ characters.

**Solution:** Use the `strings` command to extract text, then `grep` for the pattern.

**Command:**
```bash
strings data.txt | grep "==="
```
**Key Takeaway:** The `strings` command pulls plain text out of binary files.

**Screenshot:**
> <img width="1366" height="768" alt="8-9 BANDIT" src="https://github.com/user-attachments/assets/c79ca973-60f5-4a86-ab4b-dcee0d3965d9" />


---

### Level 9 → Level 10
**Learning Objective:** Decoding base64.

**Challenge:** The password is stored encoded in base64.

**Solution:** Use the `base64` command with the `-d` (decode) flag.

**Command:**
```bash
base64 -d data.txt
```
**Key Takeaway:** The `base64` tool is used to decode data from a common encoding scheme.

**Screenshot:**
> <img width="1366" height="768" alt="9-10BANDIT" src="https://github.com/user-attachments/assets/a598f3e6-be31-4669-8933-c896a1bbcbcf" />

---

### Level 10 → Level 11
**Learning Objective:** Decoding a Rot13 cipher.

**Challenge:** All alphabetical characters have been rotated by 13 positions (Rot13).

**Solution:** Use the `tr` (translate) command to perform the character substitution.

**Command:**
```bash
cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
```
**Key Takeaway:** The `tr` command is used for translating or deleting characters.

**Screenshot:**
> <img width="1366" height="768" alt="10-11BANDIT" src="https://github.com/user-attachments/assets/2d300011-1f9e-4a68-a862-7c67d29a59a8" />


---

# Level 11 → Level 12: File Identification & Recursive Decompression

## Learning Objective
File identification and recursive decompression.

## Challenge
The password was hexdumped and then buried under 8 layers of different compression and archive formats.

## Solution
A systematic process of identifying each file type and using the correct tool to decompress/extract it.

## Key Commands
```bash
xxd -r data.txt > file
file file
# Then based on file type:
mv file file.gz && gzip -d file.gz
# OR
mv file file.bz2 && bzip2 -d file.bz2
# OR
mv file file.tar && tar -xf file.tar
# Repeat until ASCII text is revealed
```

## Key Takeaway
This is a fundamental forensics skill. The file command is critical for identifying how data is structured. Understanding how to chain decompression tools is essential for handling malicious payloads, firmware images, and forensic data dumps.

## Screenshot
> <img width="1366" height="768" alt="11-12bandit" src="https://github.com/user-attachments/assets/d91f58a5-49d1-416b-a113-e33bf3961bed" />
> <img width="726" height="381" alt="continue" src="https://github.com/user-attachments/assets/a0e76e3b-bfe8-411e-8758-c25659d4ec56" />
