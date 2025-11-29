#! /usr/bin/python

#basic arithmetic operations
import operator
# standard trigonometric functions
import math
import sys

#--- ANSI Color class---

class ANSI():
        def color_text(code):
        	return "\33[{code}m".format(code=code)
        #providing ANSI color code will color the required text
        #0 is reset or no color, 31 is red, 32 is green, 34 is blue 

#--- Math Execution and Formatting ---

# handling output formatting
def format_output(value):
    try:
        # if the value is not a number, return as is
        if not isinstance(value, (int, float)):
            return value
        
        # handle scientific notation for very large or very small numbers
        if abs(value) >1e9 or (abs(value) < 1e-4 and abs(value) > 0):
            return "{:.4e}".format(value)
        
        # handle float rounding; limiting to 4 decimals and removing trailing zeroes
        if isinstance(value, float):
            return "{:.4f}".format(value).rstrip('0').rstrip('.')
        
        return str(value)
    except Exception:
        return str(value)
    
# error handling to safely execute a math function and catch errors
def safe_execute(func, *args):
    try:
        return func(*args)
    except ZeroDivisionError:
        return ANSI.color_text(31) + "Error: Division by zero" + ANSI.color_text(0)
    except ValueError:
        return ANSI.color_text(31) + "Error: Invalid math domain" + ANSI.color_text(0)
    except OverflowError:
        return ANSI.color_text(31) + "Error: Result too large" + ANSI.color_text(0)
    except Exception as e:
        return f"Error: {str(e)}"
        
#-----History--------

class Memory:
    def __init__(self):
        self.ans = 0
        self.history = []
    
    def add_calc(self, expr, result):
        # Store the numeric result, not the formatted string
        if isinstance(result, (int, float)):
            self.ans = result
        # But store the formatted version in history for display
        formatted_result = format_output(result)
        self.history.append(f"{expr} = {formatted_result}")
        if len(self.history) > 5: # sets history length shows last 5 calculations
            self.history.pop(0) #removes and returns items from list
    
    def show_history(self):
        print(ANSI.color_text(35) + "\n" + "="*40)
        print("CALCULATION HISTORY")
        print("="*40 + ANSI.color_text(0))
        if not self.history:
            print("No calculations yet!")
        else:
            for calc in self.history:
                print(calc)
            print(f"Current Ans: {self.ans}")
        print(ANSI.color_text(35) + "="*40  + ANSI.color_text(0))

# Create memory object
memory = Memory()

def get_number(prompt):
    while True:
        try:
            value = input(prompt)
            if value.lower() == 'ans':
                return memory.ans
            return float(value)
        except ValueError:
            print(ANSI.color_text(31) + "Invalid input! Enter a number or 'ans'" + ANSI.color_text(0))

#--- Math Library Integration ---

# adds two numbers
def add(a, b):
    return operator.add(a, b)

# subtracts b from a 
def subtract(a, b):
    return operator.sub(a, b)

# multiplies two numbers
def multiply(a, b):
    return operator.mul(a, b)

# divides a by b (returns quotient as float)
def div(a, b):
    return operator.truediv(a, b)

# returns remainder 
def modulus(a, b):
    return operator.mod(a, b)

# returns a to the power of b
def expo(a, b):
    return operator.pow(a, b)

# returns quotient as integer
def floor_div(a, b):
    return operator.floordiv(a, b)

# arithmetic menu
def arithmetic_menu():
    print()
    try:
        n1 = get_number("Enter number 1 or ans: ")
        n2 = get_number("Enter number 2 or ans: ")
    except ValueError:
        print(ANSI.color_text(31) + "Error: Please enter valid numbers." + ANSI.color_text(0))
        return

    while True:  # Add loop to keep asking for operation until valid
        # operation options
        print()
        print(ANSI.color_text(35) + "Select operation:" + ANSI.color_text(0))
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")
        print("6. Exponentiation")
        print("7. Floor Division")

        try:
            op = int(input("\nEnter (1-7) or ('101' to return to main menu): "))
            if op == 101:
                return
        except ValueError:
            print(ANSI.color_text(31) + "Error: Invalid option. Please enter a number between 1-7." + ANSI.color_text(0))
            continue  # Go back to the start of the loop
        
        result = None
        symbol = ""
        expression = ""
        if op == 1:
            symbol = "+"
            result = safe_execute(add, n1, n2)
        elif op == 2:
            symbol = "-"
            result = safe_execute(subtract, n1, n2)
        elif op == 3:
            symbol = "x"
            result = safe_execute(multiply, n1, n2)
        elif op == 4:
            symbol = "/"
            result = safe_execute(div, n1, n2)
        elif op == 5:
            symbol = "%"
            result = safe_execute(modulus, n1, n2)
        elif op == 6:
            symbol = "^"
            result = safe_execute(expo, n1, n2)
        elif op == 7:
            symbol = "//"
            result = safe_execute(floor_div, n1, n2)
        else:
            print(ANSI.color_text(31) + "Invalid option chosen! Please enter a number between 1-7." + ANSI.color_text(0))
            continue  # Go back to the start of the loop
        
        # Format for display only
        formatted_n1 = format_output(n1)
        formatted_n2 = format_output(n2)
        formatted_res = format_output(result)
        
        print(f"{ANSI.color_text(32)} {formatted_n1} {symbol} {formatted_n2} = {formatted_res} {ANSI.color_text(0)}")
        
        # ADD TO HISTORY - only if result is not an error
        expression = f"{formatted_n1} {symbol} {formatted_n2}"
        if not isinstance(result, str) or not result.startswith("Error"):
            memory.add_calc(expression, result)  # Pass the ACTUAL result, not formatted
        
        break  # Exit the loop after successful operation
#-----------------------------------------------------------------------

unit = "radians"  # initialize unit as radians

# converts degrees to radians
def to_radians(deg):
    return math.radians(deg)

# sine
def sin(num):
    if unit == "degrees":
        num = to_radians(num)
    return math.sin(num)

# cosine
def cos(num):
    if unit == "degrees":
        num = to_radians(num)
    return math.cos(num)

# tangent
def tan(num):
    if unit == "degrees":
        num = to_radians(num)
    return math.tan(num)

# cotangent
def cot(num):
    if unit == "degrees":
        num = to_radians(num)
    return 1 / math.tan(num)

# cosecant
def cosec(num):
    if unit == "degrees":
        num = to_radians(num)
    return 1 / math.sin(num)

# secant
def sec(num):
    if unit == "degrees":
        num = to_radians(num)
    return 1 / math.cos(num)

# toggles between degrees & radians
def toggle_unit():
    global unit #to change unit
    while True:
        unit = str(input("\nEnter unit, degrees/radians (d/r): ")).lower()
        
        if unit in ["r", "radians"]:
            unit = "radians"
            print("Current unit chosen is: radians")
            break
        elif unit in ["d", "degrees"]:
            unit = "degrees"
            print("Current unit chosen is: degrees")
            break
        else:
            print(ANSI.color_text(31) + "Invalid input! Please enter 'd' for degrees or 'r' for radians." + ANSI.color_text(0))


# trigonometric menu
def trigno_menu():
    toggle_unit()
    
    try:
        val = get_number("\nEnter value (or 'ans' for previous result): ")
    except ValueError:
        print(ANSI.color_text(31) + "Error: Please enter a valid number." + ANSI.color_text(0))
        return

    print(ANSI.color_text(35) + "Select trigonometric function:" + ANSI.color_text(0))
    print("1. sin")
    print("2. cos")
    print("3. tan")
    print("4. cot")
    print("5. cosec")
    print("6. sec")

    try:
        op = int(input("Enter (1-6): "))
    except:
        print(ANSI.color_text(31) + "Error: Invalid option" + ANSI.color_text(0))
        return
    
    func_name = ""
    result = None
    expression = ""

    if op == 1:
        func_name = "sin"
        result = safe_execute(sin, val)
        expression = f"sin({format_output(val)})"
    elif op == 2:
        func_name = "cos"
        result = safe_execute(cos, val)
        expression = f"cos({format_output(val)})"
    elif op == 3:
        func_name = "tan"
        result = safe_execute(tan, val)
        expression = f"tan({format_output(val)})"
    elif op == 4:
        func_name = "cot"
        result = safe_execute(cot, val)
        expression = f"cot({format_output(val)})"
    elif op == 5:
        func_name = "cosec"
        result = safe_execute(cosec, val)
        expression = f"cosec({format_output(val)})"
    elif op == 6:
        func_name = "sec"
        result = safe_execute(sec, val)
        expression = f"sec({format_output(val)})"
    else:
        print(ANSI.color_text(31) + "Invalid option chosen!" + ANSI.color_text(0))
        return
    
    formatted_val = format_output(val)
    formatted_res = format_output(result)
    
    print(f"{ANSI.color_text(32)} {func_name} ({formatted_val}) = {formatted_res} {ANSI.color_text(0)}")
    
    # ADD TO HISTORY - only if result is not an error
    if not isinstance(result, str) or not result.startswith("Error"):
        memory.add_calc(expression, formatted_res)
        
#--- Unit Conversions ---
def convert_units(value, from_unit, to_unit):
    value = float(value)
    
    if from_unit == to_unit:
        return value
    elif from_unit == "c" and to_unit == "f":
        return (value * 9/5) + 32
    elif from_unit == "f" and to_unit == "c":
        return (value - 32) * 5/9
    elif from_unit == "km" and to_unit == "miles":
        return value * 0.62137
    elif from_unit == "miles" and to_unit == "km":
        return value * 1.60934
    elif from_unit == "kg" and to_unit == "lb":
        return value * 2.20462
    elif from_unit == "lb" and to_unit == "kg":
        return value * 0.45359
    elif from_unit == "m" and to_unit == "ft":
        return value * 3.28084
    elif from_unit == "ft" and to_unit == "m":
        return value * 0.3048
    else:
        return ANSI.color_text(31) + "Error: Unknown conversion" + ANSI.color_text(0)

def handle_conversion_command():
    print("\n--- Unit Conversion ---")
    print("Format: [value] [from_unit] to [to_unit]")
    print("Examples: 25 c to f, 10 km to miles, 150 lb to kg")
    print("Available units: c, f, km, miles, kg, lb, m, ft")
    
    while True:
        cmd = input("\nEnter conversion or ('back' to return to main menu): ").strip()
        if cmd.lower() == 'back':
            return
        parts = cmd.split()
        
        if len(parts) == 4 and parts[2] == "to":
            value = parts[0]
            from_unit = parts[1]
            to_unit = parts[3]
            
            result = convert_units(value, from_unit, to_unit)
            formatted_result = format_output(result)
            print(f"{ANSI.color_text(32)} {value} {from_unit} = {formatted_result} {to_unit} {ANSI.color_text(0)}")
            
            # Add to history
            expression = f"Convert {value} {from_unit} to {to_unit}"
            if not isinstance(result, str) or not result.startswith("Error"):
                memory.add_calc(expression, result)
            break
        else:
            print(ANSI.color_text(31) + "Error: Use format '[value] [from_unit] to [to_unit]'" + ANSI.color_text(0))

#--- Number System Conversions ---
def convert_numsys(value, from_unit, to_unit):
    value = str(value)
    
    if from_unit == "bin" and not all(char in '01' for char in value):
        print(ANSI.color_text(31) + "Error: Binary numbers can only have 0s and 1s! " + ANSI.color_text(0))
        return
    if from_unit == "oct" and not all(char in '01234567' for char in value):
        print(ANSI.color_text(31) + "Error: Octal numbers can only have 0,1,2,3,4,5,6,7!" + ANSI.color_text(0))
        return
    if from_unit == "dec" and not all(char in '0123456789' for char in value):
        print(ANSI.color_text(31) + "Error: Binary numbers can only have 0,1,2,3,4,5,6,7,8,9! " + ANSI.color_text(0))
        return
        
    if from_unit == to_unit:
        return int(value)
    elif from_unit == "bin" and to_unit == "dec":
        return int(value, 2)
    elif from_unit == "bin" and to_unit == "oct":
        return int(format(int(value, 2), 'o'))   #bin to dec to oct
    elif from_unit == "dec" and to_unit == "bin":
        return int(format(int(value), 'b'))  
    elif from_unit == "dec" and to_unit == "oct":
        return int(format(int(value), 'o'))
    elif from_unit == "oct" and to_unit == "bin":
        return int(format(int(value, 8), 'b'))  #oct to dec to bin
    elif from_unit == "oct" and to_unit == "dec":
        return int(value, 8)    
    else:
        return ANSI.color_text(31) + "Error: Unknown conversion" + ANSI.color_text(0)

def numsys_conversion_command():
    print(ANSI.color_text(35) + "\n--- Number System Conversion ---" + ANSI.color_text(0))
    print("Format: [value] [from_unit] to [to_unit]")
    print("Examples: 1001 bin to oct, 99 oct to dec")
    print("Available units: bin, dec, oct")
    print("Note: bin is 0-1, oct is 0-7 & dec is 0-9")
    
    while True:
        cmd = input("\nEnter conversion or ('back' to return to main menu): ").strip()
        if cmd.lower() == 'back':
            return
        parts = cmd.split()
        
        if len(parts) == 4 and parts[2] == "to":
            value = parts[0]
            from_unit = parts[1]
            to_unit = parts[3]        
            
            result = convert_numsys(value, from_unit, to_unit)
            formatted_result = format_output(result)
            print(f"{ANSI.color_text(32)} {value} {from_unit} = {formatted_result} {to_unit} {ANSI.color_text(0)}")
            
            # Add to history
            expression = f"Convert {value} {from_unit} to {to_unit}"
            if not isinstance(result, str) or not result.startswith("Error"):
                memory.add_calc(expression, result)
            break
        else:
            print(ANSI.color_text(31) + "Error: Use format '[value] [from_unit] to [to_unit]'" + ANSI.color_text(0))
        
def showhelp():
	print("1. Basic Arithmetic Operations\n\tPut 2 numbers or ans (result of previous operation if any) that will undergo one of the following aritmetic operations:")
	print("\t1. Addition of the first number with the second number\n\t2. Subtraction of the second number from the first number\n\t3. Multiplication of the first number with the second number\n\t4. Division of the first number by the second number\n\t5. Modulus function which gives you the remainder when you divide the two numbers\n\t6. Exponentiation which gives you the first number to the power of the second number\n\t7. Floor division is the integer quotient, rounded down, when you divide the two numbers")
	print("2. Trignometric Operations\n\tSelect the unit of your angle: d for degree or r for radians\n\tInput value of your angle or ans (result of previous operation if any)\n\tThen choose your trignometric function")
	print("\t1. sine of your angle\n\t2. cosine of your angle\n\t3. tangent of your angle\n\t4. cotangent of your angle\n\t5. cosecant of your angle\n\t6. secant of your angle")
	print("3. Unit Conversions\n\tConverts given unit to desired unit.\n\tFormat: value given_unit to desired_unit\n\t**Failure to follow the format will result in an error.\n\t**Input both units from the same domain or else it will give an error.")
	print("\tUnits offered:\n\t\tTemperature: c for Celcius, f for Fahrenheit\n\t\tLength: m for Metres, km for Kilometres, ft for Feet, miles for Miles\n\t\tWeight: kg for kilograms, lb for Pounds")
	print("4. Number System Conversions\n\tConverts value from given number system to desired number system.\n\tFormat: value given_numberSystem to desired_numberSystem\n\t**Failure to follow the format will result in an error.\n\t**Number systems have only specific accepted digits which must be followed or else it gives an error.")
	print("\tNumber Systems offered:\n\t\tbin for Binary [0 1]\n\t\toct for Octal [0 1 2 3 4 5 6 7]\n\t\tdec for Decimal [0 1 2 3 4 5 6 7 8 9]")
	print("5. Show history\n\tShows ALL previous expressions calculated with their results and present value of ans.")
	print("6. Help Manual\n\tAccess information to help with easy usage of the calculator program.")
	print("7. Exiting the calculator\n\tLeaves the calculator program!\n")
	print(ANSI.color_text(31) + "**Any other input apart from what is required will directly result in an error.\n**Errors are highlighted in red" + ANSI.color_text(32) + "\n**Results are highlighted in green" + ANSI.color_text(0))

#--- Main Application Loop ---
def main():
    print(ANSI.color_text(35) + "\nWelcome to the Command Line Python Calculator")
    print("---------------------------------------------" + ANSI.color_text(0))
    
    while True:
        print(ANSI.color_text(35) + "\n--- Main Menu ---"+ ANSI.color_text(0))
        print("1. Arithmetic Operations")
        print("2. Trigonometric Operations")
        print("3. Unit Conversions")
        print("4. Number System Conversions")
        print("5. Show History")
        print("6. Show Help")
        print("7. Exit Program")
        
        choice = input("\nSelect an option (1-7): ").strip()
        
        if choice == '1':
            arithmetic_menu()
        elif choice == '2':
            trigno_menu()
        elif choice == '3':
            handle_conversion_command()
        elif choice == '4':
            numsys_conversion_command()
        elif choice == '5':
            memory.show_history()
        elif choice == '6':
            showhelp()
        elif choice == '7':
            print(ANSI.color_text(35) + "\nExiting calculator. Goodbye!" + ANSI.color_text(0))
            sys.exit()
        else:
            print(ANSI.color_text(31) + "\n[!] Invalid selection. Please choose options 1 to 7" + ANSI.color_text(0))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(ANSI.color_text(35) + "\n\nProgram interrupted by user. Exiting..." + ANSI.color_text(0))
        sys.exit()

