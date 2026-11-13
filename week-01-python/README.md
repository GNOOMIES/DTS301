# Week 01: Python Fundamentals - Coursework README

## 1. High-Level Overview of the Workshop

Welcome to the **Week 01 Python Workshop** folder (`week-01-python`). This module is designed to bridge the gap between fundamental programming concepts and practical application in Python. Whether you are entirely new to programming or reviewing core language constructs, this week establishes the building blocks required for subsequent advanced topics in data science, software engineering, and artificial intelligence.

The primary script provided in this folder, `workshop1.py`, acts as a comprehensive, interactive command-line application. It encapsulates multiple foundational programming tasks ranging from basic loops and conditionals to modular function design, string manipulation, algorithmic implementations (such as the Fibonacci sequence and the Caesar Cipher), and a fully playable text-based game of Hangman.

---

## 2. Detailed Breakdown of Files, Functions, and Tasks

The `workshop1.py` file is structured modularly. Below is a detailed technical breakdown of every function implemented inside the script, detailing its logic, inputs, outputs, algorithms, and underlying programming concepts.

### Control Flow & Basic Algorithms (Tasks 1A - 1C)

*   **`task_1a()`**
    *   **Logic:** Iterates through a fixed numerical sequence using a `for` loop and prints each value.
    *   **Inputs:** None.
    *   **Outputs:** Prints integers from `1` to `10` inclusive to the console.
    *   **Concepts Used:** `range(start, stop)` generator, `for` loops, basic `print()` output.

*   **`task_1b()`**
    *   **Logic:** Iterates through an even-numbered numerical sequence and prints each value.
    *   **Inputs:** None.
    *   **Outputs:** Prints even integers from `2` to `10` inclusive to the console.
    *   **Concepts Used:** `range(start, stop, step)` generator parameter, step-based iteration.

*   **`task_1c()`**
    *   **Logic:** Generates the first 5 numbers of the Fibonacci sequence. It initializes the first two terms (`a = 0`, `b = 1`), tracks iterations using a `count` variable, and updates values simultaneously via Python tuple assignment.
    *   **Inputs:** None.
    *   **Outputs:** Prints the first 5 Fibonacci numbers (`0, 1, 1, 2, 3`) sequentially.
    *   **Concepts Used:** `while` loops, accumulator pattern (`count += 1`), simultaneous multiple assignment (`a, b = b, a + b`).

---

### Functions, Data Structures, and Strings (Tasks 1D - 1F)

*   **`task_1d(num1, num2)` & `run_task_1d()`**
    *   **Logic:** `task_1d` accepts two numerical values, computes their arithmetic sum, and returns the result. `run_task_1d` serves as a wrapper function that feeds hardcoded arguments (`5` and `7`) into the calculation and formats the output.
    *   **Inputs (`task_1d`):** `num1` (int/float), `num2` (int/float).
    *   **Outputs (`task_1d`):** Returns `num1 + num2`.
    *   **Concepts Used:** Function definition, parameters, `return` statements, modular wrapper design.

*   **`task_1e(numbers)` & `run_task_1e()`**
    *   **Logic:** Iterates through a list of numbers, treating the first element as the current maximum (`largest`). If any subsequent number exceeds this threshold, the threshold is updated. `run_task_1e` provides a sample list (`[12, 45, 7, 89, 23]`) to test the function.
    *   **Inputs (`task_1e`):** `numbers` (List of ints/floats).
    *   **Outputs (`task_1e`):** Returns the maximum value found in the list.
    *   **Concepts Used:** List traversal, comparative logic, initial state assumptions (`numbers[0]`).

*   **`task_1f(text)` & `run_task_1f()`**
    *   **Logic:** Scans a given string character by character, checking whether each character exists within a predefined string of vowels (`aeiouAEIOU`). It increments a counter for every match found. `run_task_1f` supplies the sample string `"Applied Artificial Intelligence"`.
    *   **Inputs (`task_1f`):** `text` (String).
    *   **Outputs (`task_1f`):** Returns the integer count of vowels.
    *   **Concepts Used:** String iteration, membership testing (`in`), case-insensitive considerations.

---

### Practical Applications & Mathematical Logic (Tasks 2A - 2B)

*   **`task_2a()`**
    *   **Logic:** Performs hardcoded conversions between Fahrenheit and Centigrade using standard temperature formulas:
        *   $C = (F - 32) / 1.8$
        *   $F = (C \times 1.8) + 32$
    *   **Inputs:** None.
    *   **Outputs:** Prints formatted floating-point strings rounded to two decimal places.
    *   **Concepts Used:** Arithmetic operators, string interpolation (`f"{value:.2f}"`).

*   **`task_2b()`**
    *   **Logic:** Presents a text menu allowing the user to choose a conversion direction. It dynamically accepts user input, casts it to floating-point numbers, computes the conversion, and handles invalid menu selections gracefully.
    *   **Inputs:** User keyboard input (`input()`) for menu choice and temperature values.
    *   **Outputs:** Prints converted temperature calculations or error messages.
    *   **Concepts Used:** Conditional branching (`if`, `elif`, `else`), type casting (`float()`), string sanitization (`.strip()`).

---

### Cryptography (Task 3)

*   **`caesar_cypher(message, key, mode)` & `task_3()`**
    *   **Logic:** Implements a classic Caesar Cipher encryption and decryption algorithm. 
        *   If `mode` is set to `"decrypt"`, the shift key is inverted (multiplied by `-1`).
        *   The algorithm iterates through each character in the message. If the character is alphabetical, it determines whether it is uppercase or lowercase to establish the correct ASCII base (`ord('A')` or `ord('a')`).
        *   It shifts the character code relative to the base, applies modulo arithmetic (`% 26`) to wrap around the alphabet cleanly, converts it back to a character using `chr()`, and leaves non-alphabetic characters untouched.
    *   **Inputs (`caesar_cypher`):** `message` (String), `key` (Integer shift amount), `mode` (String: `"encrypt"` or `"decrypt"`).
    *   **Outputs (`caesar_cypher`):** Returns the transformed cipher/plain text string.
    *   **Concepts Used:** ASCII conversion (`ord()`, `chr()`), modulo arithmetic for circular data structures, conditional evaluation, text manipulation.

---

### Game Development (Task 4)

*   **`task_4()`**
    *   **Logic:** A command-line implementation of the classic word-guessing game, **Hangman**.
        *   Randomly selects a secret word from a predefined list (`["python", "java", "javascript"]`).
        *   Maintains a game loop bounded by `max_guesses = 6`.
        *   Dynamically renders the current state of the word using list comprehensions and string joining (`_` for unguessed letters, letters for correctly guessed ones).
        *   Validates user input to ensure single alphabetical characters are entered and prevents duplicate guesses from draining attempts.
        *   Tracks incorrect guesses and terminates when the word is fully solved or attempts are exhausted.
    *   **Inputs:** User letter guesses via `input()`.
    *   **Outputs:** Game state updates, prompts, success ("Congratulations"), or failure ("Game over") messages.
    *   **Concepts Used:** Random module (`random.choice()`), `while` loops, list comprehensions, input validation, state tracking.

---

### Application Orchestration (`main()`)

*   **`main()`**
    *   **Logic:** Acts as the central menu controller. It stores task descriptions and function references in a structured dictionary, presenting a continuous interactive prompt to the user. When a user selects a valid task key, the corresponding function reference is executed dynamically.
    *   **Inputs:** Menu selection choices via `input()`.
    *   **Outputs:** Formatted terminal menu displays and execution output of selected tasks.
    *   **Concepts Used:** Dictionary data structures, function pointers/first-class functions, infinite loops (`while True`), application entry-point guards (`if __name__ == "__main__":`).

---

## 3. How to Run the Script

To run the workshop script, ensure you have **Python 3.6+** installed on your system. 

1. Open your terminal or command prompt.
2. Navigate to the directory containing `workshop1.py`:
   ```bash
   cd path/to/week-01-python
   ```
3. Execute the script using Python:
   ```bash
   python workshop1.py
   ```
4. Follow the interactive terminal prompts to select and run any of the workshop tasks (1a through 4), or type `q` to quit the application.
