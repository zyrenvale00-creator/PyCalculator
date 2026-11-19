import tkinter as t

#Click register
def button_click(value):
    if display.get() == "Error!":
        display.delete(0, t.END)

    operators = ["÷", "×", "−", "+", "%"]
    if display.get():
        if value in operators and display.get()[-1] in operators:
            return
    display.insert(t.END, value)

#Calculation
def calculate():
    if not display.get():
        return
    expression = display.get()
    expression = expression.replace("×", "*").replace("÷", "/").replace("−", "-").replace("%", "/100")
    try:
        result = eval(expression)
        display.delete(0, t.END)
        display.insert(t.END, result)
    except Exception:
        display.delete(0, t.END)
        display.insert(t.END, "Error!")

# +- conversion 
def toggle_sign():
    if not display.get():
        return
    try:
        number = float(display.get())*-1
        display.delete(0, t.END)  
        display.insert(t.END, number)
    except Exception:
        display.delete(0, t.END)
        display.insert(t.END)

# Window
window = t.Tk()
window.title("PyCalculator")
window.resizable(False, False)
window.configure(bg="#383636")

# Display
display = t.Entry(
    window,
    font=("Arial", 24, "bold"),
    fg="white",
    bg="#1C1A1A",
    justify="right",
    cursor="xterm",
    width=16,
    relief="flat",
    bd = 0
)
display.pack(ipady=8, pady=5)

# Button Frame
button_frame = t.Frame(
    window,
    bg="#383636"
)
button_frame.pack(pady=10)

# Buttons
buttons = [
    ["C", "DEL", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "−"],
    ["1", "2", "3", "+"],
    ["±", "0", ".", "="]
]

right_symbols = ["÷", "×", "−", "+", "="]
top_symbols = ["C", "DEL", "%"]

row_count = len(buttons)
col_count = len(buttons[0])

for row in range(row_count):
    for col in range(col_count):

        value = buttons[row][col]

        if value in right_symbols:
            color = "#E05215"
        elif value in top_symbols:
            color = "#8F8F8F"
        else:
            color = "#3C3A3A"

        if value == "DEL":
            command = lambda: display.delete(len(display.get()) - 1, t.END) if display.get() else None
        elif value == "C":
            command = lambda: display.delete(0, t.END)
        elif value == "=":
            command = calculate
        elif value == "±":
            command = toggle_sign
        else:
            command = lambda v=value: button_click(v)

        button = t.Button(
            button_frame,
            text=value,
            font=("Arial", 23, "bold"),
            bg=color,
            fg="white",
            activebackground="#605C5C",
            width=3,
            height=1,
            command=command
        )

        button.grid(row=row, column=col, padx=3, pady=3)

#Enter 
display.bind("<Return>", lambda event: calculate())

#autoPointToText
display.focus_set()

# Run application
window.mainloop()
