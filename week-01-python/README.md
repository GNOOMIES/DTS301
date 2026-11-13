# Week 01: Python Fundamentals - Coursework README

## 1. High-Level Overview

Welcome to the **week-01-python** university coursework folder. This module serves as an intensive foundational introduction to Python programming, designed to transition students from core programming logic to practical problem-solving. 

The primary script, `workshop1.py`, acts as an interactive command-line application housing a centralized menu system. It covers essential programming paradigms including:
* Control flow (conditional statements and iterative loops)
* Data structures (lists, strings, and dictionaries)
* User input handling and string manipulation
* Algorithmic thinking (mathematical sequences, search algorithms, cryptography, and state management games)

---

## 2. Detailed Breakdown of `workshop1.py`

The script is modularly structured, separating individual tasks into distinct functions and providing a dispatch dictionary inside a `main()` runner loop. Below is a comprehensive breakdown of every function and task implemented in the file.

### Task Group 1: Basic Control Flow and Functions

#### `task_1a()`
* **Purpose:** Prints integers from 1 to 10 inclusively.
* **Logic & Concepts:** Utilizes a `for` loop combined with Python's built-in `range(start, stop)` function. `range(1, 11)` starts at `1` and stops right before `11`.
* **Inputs/Outputs:** Takes no inputs; prints integers line-by-line to standard output.

#### `task_1b()`
* **Purpose:** Prints even integers from 2 to 10 inclusively.
* **Logic & Concepts:** Uses a `for` loop with a step parameter: `range(2, 11, 2)`. The third argument (`2`) dictates the increment step between iterations.
* **Inputs/Outputs:** Takes no inputs; prints even numbers line-by-line to standard output.

#### `task_1c()`
* **Purpose:** Generates and prints the first 5 numbers of the Fibonacci sequence.
* **Logic & Concepts:** Employs a `while` loop running up to 5 iterations. Uses tuple unpacking (`a, b = b, a + b`) to dynamically compute the next term in the sequence where each number is the sum of the preceding two, starting with `0` and `1`.
* **Inputs/Outputs:** Takes no inputs; prints the sequence values sequentially.

#### `task_1d(num1, num2)` & `run_task_1d()`
* **Purpose:** Computes and displays the arithmetic sum of two numbers.
* **Logic & Concepts:** 
  * `task_1d(num1, num2)` is a pure function that accepts two parameters and returns their sum using the `+` operator.
  * `run_task_1d()` acts as a wrapper function that provides sample arguments (`5` and `7`) to `task_1d` and prints the formatted result.
* **Inputs/Outputs:** `task_1d` takes two numeric parameters and returns a numeric sum. `run_task_1d` outputs the result via `print()`.

#### `task_1e(numbers)` & `run_task_1e()`
* **Purpose:** Finds and returns the maximum numerical value within a list.
* **Logic & Concepts:** 
  * `task_1e` implements a linear search algorithm. It assumes the first element (`numbers[0]`) is the largest, iterates through every element in the list, and updates the `largest` variable whenever a larger value is encountered.
  * `run_task_1e` initializes a sample list (`[12, 45, 7, 89, 23]`) and invokes the search function.
* **Inputs/Outputs:** `task_1e` accepts a list of integers/floats and returns the single highest numerical value.

#### `task_1f(text)` & `run_task_1f()`
* **Purpose:** Counts the total number of vowels (case-insensitive) in a given string.
* **Logic & Concepts:** 
  * Defines a reference string containing all vowels (`"aeiouAEIOU"`). Iterates through each character of the target text, checking membership via the `in` keyword, and increments a running counter.
  * `run_task_1f` supplies a sample string (`"Applied Artificial Intelligence"`) to demonstrate functionality.
* **Inputs/Outputs:** `task_1f` accepts a string and returns an integer representing the vowel count.

---

### Task Group 2: Temperature Conversions

#### `task_2a()`
* **Purpose:** Demonstrates hardcoded temperature conversions between Fahrenheit and Centigrade (Celsius).
* **Logic & Concepts:** Applies algebraic formulas:
  * Fahrenheit to Celsius: $C = \frac{F - 32}{1.8}$
  * Celsius to Fahrenheit: $F = (C \times 1.8) + 32$
  Uses f-strings with precision formatting (`:.2f`) to display results rounded to two decimal places.
* **Inputs/Outputs:** Hardcoded inputs; formatted conversion strings printed to the console.

#### `task_2b()`
* **Purpose:** Provides an interactive command-line interface (CLI) for users to convert temperatures dynamically.
* **Logic & Concepts:** Uses `input()` to capture user selections and numeric values. Leverages `.strip()` for clean string handling and `float()` for type casting. Conditional `if-elif-else` branches handle user choices and input validation.
* **Inputs/Outputs:** Prompts the user for menu choices and temperature floats; outputs the converted temperature.

---

### Task Group 3: Cryptography (Caesar Cipher)

#### `caesar_cypher(message, key, mode)`
* **Purpose:** Encrypts or decrypts a text message using a classical Caesar shift cipher.
* **Logic & Concepts:** 
  * If `mode` is set to `"decrypt"`, the shift key is inverted (`key = -key`).
  * Iterates through every character in the message. If the character is alphabetic (`char.isalpha()`), it determines whether it is uppercase or lowercase to establish the correct ASCII base (`ord('A')` or `ord('a')`).
  * Applies modular arithmetic: `(ord(char) - base + key) % 26 + base` to wrap around the alphabet smoothly, then converts the resulting ASCII code back to a character using `chr()`. Non-alphabetic characters (spaces, punctuation) are preserved untouched.
* **Inputs/Outputs:** Accepts `message` (string), `key` (integer shift value), and `mode` (string: `"encrypt"` or `"decrypt"`). Returns the transformed ciphertext or plaintext string.

#### `task_3()`
* **Purpose:** Interactive wrapper for the Caesar cipher algorithm.
* **Logic & Concepts:** Prompts the user for a message, integer shift key, and operational mode. Validates user input before invoking `caesar_cypher()`.
* **Inputs/Outputs:** Interactive console inputs and outputs.

---

### Task Group 4: Hangman Game

#### `task_4()`
* **Purpose:** Implements a text-based guessing game (Hangman) where players attempt to uncover a secret word letter by letter.
* **Logic & Concepts:**
  * Uses the `random` module to randomly select a secret word from a predefined list (`["python", "java", "javascript"]`).
  * Tracks game state using `guessed_letters` (a list) and `incorrect_guesses` (an integer counter capped at `max_guesses = 6`).
  * Uses list comprehensions and `.join()` to construct the current word display string, showing correctly guessed letters and masking unguessed letters with underscores (`_`).
  * Implements input validation to ensure users enter a single alphabetic character and prevents duplicate guesses from incrementing the penalty counter.
* **Inputs/Outputs:** Interactive single-letter guesses via console prompts; outputs game status, hidden word state, and win/loss messages.

---

### Application Core

#### `main()`
* **Purpose:** Central control hub and menu dispatcher for the entire workshop script.
* **Logic & Concepts:** 
  * Stores task mappings inside a dictionary where keys correspond to menu options and values are tuples containing descriptions and callable function references.
  * Runs an infinite `while` loop that displays the menu, captures user input via `.strip().lower()`, and conditionally executes the targeted function or breaks the loop when `"q"` is entered.
* **Inputs/Outputs:** Terminal menu navigation inputs and dynamic function execution outputs.

---

## 3. How to Run the Script

Ensure you have **Python 3.6 or higher** installed on your system.

1. Open your terminal or command prompt.
2. Navigate to the directory containing `workshop1.py`:
   ```bash
   cd path/to/week-01-python
   ```
3. Execute the script using Python:
   ```bash
   python workshop1.py
   ```
4. Follow the on-screen interactive menu prompts by typing the corresponding task identifier (e.g., `1a`, `3`, `4`) and pressing **Enter**. Type `q` to exit the program.
