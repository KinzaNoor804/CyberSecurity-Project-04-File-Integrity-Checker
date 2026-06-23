# File Integrity Checker

## Project Description

This project calculates the SHA-256 hash of a file and helps verify its integrity.

A hash acts as a digital fingerprint of a file. If the file is modified, even slightly, the generated hash changes completely. This technique is widely used in cybersecurity to detect unauthorized file modifications.

## Features

* Generates SHA-256 hash values
* Verifies file integrity
* Detects file modifications
* Simple and user-friendly interface
* Error handling for missing files

## Technologies Used

* Python 3
* VS Code

## How to Run

1. Open terminal.
2. Run:

```bash
python file_integrity_checker.py
```

3. Enter the file name with extension.

## Sample Output

```text
FILE INTEGRITY CHECKER

Enter file name with extension: test.txt

File Name: test.txt

SHA-256 Hash:
a1b2c3d4e5f6...
```

## How It Works

* The user enters a file name.
* The program reads the file contents.
* A SHA-256 hash is generated.
* The hash acts as a unique digital fingerprint of the file.
* Any modification to the file produces a completely different hash.

## Author

Kinza Noor
