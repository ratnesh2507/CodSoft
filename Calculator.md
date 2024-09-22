# Calculator Application

## Features and Functionality

This Python script implements a basic calculator application using a class-based approach. The calculator provides options for addition, subtraction, multiplication, and division. The user interacts with the calculator through a simple console interface.

### Calculator Class

- The `Calculator` class contains four methods (`add`, `subtract`, `multiply`, `divide`) to perform basic arithmetic operations.
  - Each method takes two parameters, `a` and `b`, and prints the result of the corresponding operation.

### User Interface Loop

- The script creates an instance of the `Calculator` class named `ob`.

- A `while` loop runs indefinitely, presenting the user with a menu for calculator operations.

- The user is prompted to input a choice:
  - Press 1 for Addition
  - Press 2 for Subtraction
  - Press 3 for Multiplication
  - Press 4 for Division
  - Press 5 to Exit

- Based on the user's input, the script performs the selected operation by calling the corresponding method from the `Calculator` class.

- The loop continues until the user chooses to exit by pressing 5.

### User Input and Error Handling

- The script prompts the user to enter numbers for the chosen operation.
- If the user enters a choice other than 1-5, an error message is displayed, and the loop continues.

### Exiting the Application

- If the user chooses to exit (presses 5), the `sys.exit(0)` statement is used to terminate the script with a status code of 0.

### Running the Calculator

- To use the calculator, execute the script.
- Follow the on-screen instructions to perform addition, subtraction, multiplication, and division operations.
- To exit the calculator, choose option 5.

### Sample Usage

```python
if __name__ == "__main__":
    ob = Calculator()
    while True:
        print("\n----Calculator Application----")
        # ... (menu options)
        choice = int(input("Enter your choice:"))
        # ... (perform operations based on user choice)
