# Task 3 - Basic File Handling

## Description

A Python program that reads data from a text file, finds and replaces specific words, and saves the modified data back to the file.

## Features

* Read data from a text file
* Find specific words
* Replace specific words
* Save modified data back to the file
* Handle `FileNotFoundError` using exception handling

## Technologies Used

* Python
* File Handling
* String Manipulation
* Exception Handling

## Project Files

```text
Task-3-Basic-File-Handling/
│
├── file_handling.py
├── sample.txt
└── README.md
```

## How to Run

1. Make sure Python is installed.
2. Keep `file_handling.py` and `sample.txt` in the same folder.
3. Open the folder in VS Code.
4. Open the terminal.
5. Run the program:

```bash
python file_handling.py
```

6. Enter the word you want to find.
7. Enter the word you want to replace it with.

## Example

### Input

```text
Enter word to find: Python
Enter word to replace with: Java
```

### Output

```text
Original Data:
Python is easy to learn.
Python is a powerful programming language.

File updated successfully!
```

The modified content will be saved back to `sample.txt`.

## Error Handling

If `sample.txt` is not found, the program displays:

```text
Error: sample.txt file not found.
```

## Internship Task

**Task 3: Basic File Handling**

This project demonstrates:

* File Input/Output in Python
* String Manipulation
* Exception Handling
