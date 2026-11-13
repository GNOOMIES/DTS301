import random


def task_1a():
    for i in range(1, 11):
        print(i)


def task_1b():
    for i in range(2, 11, 2):
        print(i)


def task_1c():
    a, b = 0, 1
    count = 0
    while count < 5:
        print(a)
        a, b = b, a + b
        count += 1


def task_1d(num1, num2):
    return num1 + num2


def run_task_1d():
    print("Sum of 5 and 7:", task_1d(5, 7))


def task_1e(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest


def run_task_1e():
    sample_list = [12, 45, 7, 89, 23]
    print("List:", sample_list)
    print("Largest number:", task_1e(sample_list))


def task_1f(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count


def run_task_1f():
    sample_text = "Applied Artificial Intelligence"
    print("String:", sample_text)
    print("Number of vowels:", task_1f(sample_text))


def task_2a():
    f_val = 68
    c_converted = (f_val - 32) / 1.8
    print(f"{f_val}°F is {c_converted:.2f}°C")

    c_val = 20
    f_converted = (c_val * 1.8) + 32
    print(f"{c_val}°C is {f_converted:.2f}°F")


def task_2b():
    print("1. Fahrenheit to Centigrade")
    print("2. Centigrade to Fahrenheit")
    choice = input("Choose conversion (1 or 2): ").strip()

    if choice == "1":
        temp = float(input("Enter temperature in Fahrenheit: "))
        result = (temp - 32) / 1.8
        print(f"Converted temperature: {result:.2f}°C")
    elif choice == "2":
        temp = float(input("Enter temperature in Centigrade: "))
        result = (temp * 1.8) + 32
        print(f"Converted temperature: {result:.2f}°F")
    else:
        print("Invalid conversion option selected.")


def caesar_cypher(message, key, mode):
    result = ""
    if mode == "decrypt":
        key = -key

    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + key) % 26 + base
            result += chr(shifted)
        else:
            result += char

    return result


def task_3():
    message = input("Enter message: ")
    key = int(input("Enter key (shift amount): "))
    mode = input("Enter mode (encrypt/decrypt): ").strip().lower()

    if mode in ["encrypt", "decrypt"]:
        output = caesar_cypher(message, key, mode)
        print("Output:", output)
    else:
        print("Invalid mode. Please choose 'encrypt' or 'decrypt'.")


def task_4():
    word_list = ["python", "java", "javascript"]
    max_guesses = 6
    secret_word = random.choice(word_list)
    guessed_letters = []
    incorrect_guesses = 0

    while incorrect_guesses < max_guesses:
        display = " ".join([letter if letter in guessed_letters else "_" for letter in secret_word])
        print(display)

        if "_" not in display:
            print(f'Congratulations, you guessed the word "{secret_word}"!')
            return

        guess = input("Guess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            incorrect_guesses += 1
            print(f"Wrong guess! {max_guesses - incorrect_guesses} guesses left.")

    print(f'Game over! The word was "{secret_word}".')


def main():
    tasks = {
        "1a": ("Task 1a: Numbers 1 to 10", task_1a),
        "1b": ("Task 1b: Even numbers 2 to 10", task_1b),
        "1c": ("Task 1c: Fibonacci sequence (first 5)", task_1c),
        "1d": ("Task 1d: Sum of two numbers", run_task_1d),
        "1e": ("Task 1e: Largest number in a list", run_task_1e),
        "1f": ("Task 1f: Count vowels in a string", run_task_1f),
        "2a": ("Task 2a: Predefined temperature conversions", task_2a),
        "2b": ("Task 2b: Interactive temperature converter", task_2b),
        "3": ("Task 3: Caesar Cypher", task_3),
        "4": ("Task 4: Hangman Game", task_4),
    }

    while True:
        print("\n--- DTS301 Workshop 1 Menu ---")
        for key, (desc, _) in tasks.items():
            print(f"[{key}] {desc}")
        print("[q] Quit")

        choice = input("\nSelect a task to run: ").strip().lower()

        if choice == "q":
            break
        elif choice in tasks:
            print(f"\n--- Running {tasks[choice][0]} ---")
            tasks[choice][1]()
        else:
            print("Invalid selection. Try again.")


if __name__ == "__main__":
    main()
    