import tkinter as tk

def create_calculator():
    """Creates a functional GUI calculator using tkinter."""

    # --- Main Window Setup ---
    window = tk.Tk()
    window.title("Calculator")
    window.geometry("350x450")
    window.resizable(False, False)
    window.configure(bg='#2e2e2e')

    # --- Global variable for the expression ---
    expression = ""

    # --- Functions ---
    def press(num):
        """Appends the pressed number or operator to the expression string."""
        nonlocal expression
        expression += str(num)
        equation.set(expression)

    def equals():
        """Evaluates the final expression and displays the result."""
        nonlocal expression
        try:
            total = str(eval(expression))
            equation.set(total)
            expression = total
        except (SyntaxError, ZeroDivisionError):
            equation.set("Error")
            expression = ""

    def clear():
        """Clears the input field."""
        nonlocal expression
        expression = ""
        equation.set("")

    # --- UI Elements ---
    equation = tk.StringVar()
    display = tk.Entry(
        window,
        textvariable=equation,
        font=('Arial', 24),
        bd=10,
        insertwidth=2,
        width=14,
        borderwidth=4,
        bg="#f0f0f0",
        justify='right'
    )
    display.grid(columnspan=4, padx=10, pady=20, ipady=10)

    # --- Button Layout and Styling ---
    button_params = {
        'font': ('Arial', 18),
        'height': 1,
        'width': 4,
        'bd': 3,
        'relief': 'raised'
    }
    
    buttons_layout = [
        ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
        ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
        ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
        ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('+', 5, 3)
    ]
    
    # --- Creating and Placing Buttons ---
    for (text, row, col) in buttons_layout:
        if text.isdigit() or text == '.':
            btn = tk.Button(window, text=text, **button_params, bg='#e0e0e0', command=lambda t=text: press(t))
        elif text == '=':
            btn = tk.Button(window, text=text, **button_params, bg='#a5d6a7', command=equals)
        else:
            btn = tk.Button(window, text=text, **button_params, bg='#ffab91', command=lambda t=text: press(t))
        btn.grid(row=row, column=col, pady=5)

    # --- CORRECTED SECTION FOR CLEAR BUTTON ---
    # Create a copy of the base parameters to avoid modifying the original
    clear_button_params = button_params.copy()
    # Set the specific width for the clear button
    clear_button_params['width'] = 19
    
    # Create the button using the new parameters
    clear_button = tk.Button(window, text='Clear', **clear_button_params, bg='#ef9a9a', command=clear)
    clear_button.grid(row=6, column=0, columnspan=4, pady=10)

    window.mainloop()

# Run the calculator
if __name__ == "__main__":
    create_calculator()