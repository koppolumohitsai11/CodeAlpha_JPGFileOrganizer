# CodeAlpha JPG File Organizer

## Project Overview

This project is a simple file automation script developed using Python as part of the CodeAlpha Python Programming Internship.

The program automatically finds all `.jpg` files in a source folder and moves them to a destination folder.

## Features

- Automatically finds JPG files
- Moves JPG files between folders
- Creates the destination folder if it does not exist
- Handles uppercase and lowercase `.jpg` extensions
- Displays the files that were moved
- Shows the total number of moved files

## Technologies Used

- Python
- os module
- shutil module

## Python Concepts Used

- File handling
- Directory handling
- `for` loop
- `if` condition
- Functions from Python standard library
- User input
- String methods

## How It Works

1. The user enters the source folder path.
2. The user enters the destination folder path.
3. The program checks whether the source folder exists.
4. The destination folder is created if necessary.
5. The program checks all files in the source folder.
6. Files ending with `.jpg` are identified.
7. The JPG files are moved to the destination folder.
8. The program displays the number of files moved.

## How to Run

1. Install Python.
2. Clone or download this repository.
3. Open the project folder in VS Code or Command Prompt.
4. Run:

```bash
python file_organizer.py
