
---

## HOW_IT_WORKS.md

markdown
# How the Advanced Python Calculator Works

## Overview

This project is a GUI calculator built in Python using the Tkinter library.  
It was designed to provide a simple yet powerful calculator experience with an easy-to-use interface.

## Key Features

- The calculator supports the four basic arithmetic operations: addition (+), subtraction (-), multiplication (*), and division (/).
- It allows the user to enter decimal numbers and use parentheses for grouping expressions.
- There is a toggle button (+/-) to quickly change the sign of the current number.
- The Clear (C) button resets the input, while the Backspace (⌫) button deletes the last character.
- Errors like division by zero or invalid expressions are caught and notified to the user via dialog boxes.
- The UI has been styled with custom colors and interactive hover effects on buttons for a modern look.
- The input field is read-only, ensuring users can only enter expressions via the buttons to avoid input errors.

## Implementation Details

- The calculator uses the eval() function to compute the result of the expression entered by the user.
- Input is managed exclusively via button presses to maintain control and avoid invalid input.
- Regular expressions are used to identify the last number for the sign toggle functionality.
- The interface uses a grid layout to organize buttons into a 4x6 grid for consistency and responsiveness.
- Colorama or other external libraries are not used here; the focus is on Tkinter for simplicity.

## How to Run

1. Make sure you have Python 3 installed.
2. Run the script `calcolatrice_gui.py` using the command:

bash
python calcolatrice_gui.py
