# ITAP-COSC-3411-Gamma
## Integrated Command Line Python Calculator

A menu-driven command-line calculator written in Python. This tool integrates basic arithmetic, trignometric functions, unit conversions, and number system conversions into a single, colour-coded interface with history tracking.

## Features
- **Arithmetic Operations**: Addition, subtraction, multipulication, division, modulus, exponentiation, and floor division.
- **Trignometry**: Supports sin, cos, tan, cot, cosec, and sec. Includes a toggle for **Degrees** and **Radians**
- **Unit Conversion**: Convert between Temperature (Celcius/Fahrenheit), Length (km/miles, m/ft), and Weight (kg/lb)
- **Number Systems**: Convert between Deciman, Binary, and Octal
- **Smart History & Memory**:
    Tracks the last 5 calculations
    Use the keyword `ans` to use the result of the previous calculation in a new equation
- **Safety and Formatting**: Prevents crashes from division by zero or invalid inputs and formats large numbers using scientific notation
- **Colour-Coded Output**: Uses ANSI escape codes for clear, coloured terminal output (Red for errors, Green for results)

## Prerequisites
Python 3.x must be installed on your system
- To check if Python is installed, open your terminal/command prompt and type `python --version` or `python3 --version`

## Installation & Configuration
1. Download: Save the file SP_Project.py to a directory of your choice.
2. Dependencies: This program uses only Python standard libraries (`math`, `sys`, `operator`). No external `pip` installations are required.
3. Permissions (Linux/macOS): If you wish to run the script directly as an executable, you may need to grant execution permissions:
                                  `chmod +x SP_ Project.py`

## How to Run
Open your terminal or command prompt, navigate to the folder containing the file, and run one of the following commands:

- **Windows** -> `python SP_Project.py`
- **Linux/macOS** -> `python3 SP_Project.py` or `./SP_Project.py`

## Usage Guide
1. Navigation: The program uses a numbered menu system. Enter the number corresponding to the option you want (for example, `1` for Arithmetic)
2. Inputs: Follow the on-screen prompts
     - for numbers, type the value (e.g., 50, 3.14)
     - To use previous result, type `ans`
     - To return to the main menu for sub-menus (like conversios), type `101` or `back` as indicated by the prompt
3. Exiting: Select option `7` from the main menu or press `Ctrl+C` to force quit safely.

## Example Workflow
Here is a short example of calculating the hypotenuse of a triangle using the `ans` feature:

**Step 1: Calculate 3 squared**
1. Select **1** (Arithmetic)
2. Enter number 1: `3`
3. Enter number 2: `2`
4. Select operation **6** (Exponential)
      - Result: `3.0^2.0 = 9.0` (saved to `ans`)

**Step 2: Add 4 squared to the previous result**
1. Select **1** (Arithmetic)
2. Enter number 1: `ans` (9.0)
3. Enter number 2: `16`
4. Select operation **1** (Add)
      - Result: `9.0 + 16.0 = 25.0` (saved to `ans`)

**Step 3: Find the square root (exponent 0.5)**
1. Select **1** (Arithmetic)
2. Enter number 1: `ans` (25.0)
3. Enter number 2: `0.5`
4. Select operation **6** (Exponential)
     - Result: `25.0^0.5 = 5.0`
