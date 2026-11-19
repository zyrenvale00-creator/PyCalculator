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

# Button hover effects
def on_enter(event):
    if event.widget["text"] == "=":
        event.widget.config(bg="#20B4D8")
    else:
        event.widget.config(bg="#505866")

def on_leave(event, original_color):
    event.widget.config(bg=original_color)

# Window
window = t.Tk()
window.title("PyCalculator")
window.resizable(False, False)
window.configure(bg="#17191F")

# Application heading
heading = t.Label(
    window,
    text="PyCalculator",
    font=("Segoe UI", 15, "bold"),
    fg="#6BDCF8",
    bg="#17191F"
)
heading.pack(anchor="w", padx=15, pady=(10, 0))

# Display
display = t.Entry(
    window,
    font=("Segoe UI", 30, "bold"),
    fg="#FFFFFF",
    bg="#22252D",
    justify="right",
    cursor="xterm",
    width=14,
    relief="flat",
    bd=0,
    insertbackground="white"
)
display.pack(ipady=12, padx=10, pady=10)


# Button Frame
button_frame = t.Frame(
    window,
    bg="#17191F"
)
button_frame.pack(padx=8, pady=8)

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

for col in range(col_count):
    button_frame.grid_columnconfigure(col, weight=1)

for row in range(row_count):
    for col in range(col_count):

        value = buttons[row][col]

        if value == "=":
            color = "#1D95B3"
        elif value in right_symbols:
            color = "#263F4A"
        elif value in top_symbols:
            color = "#424957"
        else:
            color = "#292D36"

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
            font=("Segoe UI", 21, "bold"),
            bg=color,
            fg="#6BDCF8" if value in right_symbols else "white",
            activebackground="#505866",
            activeforeground="white",
            width=4,
            height=1,
            relief="flat",
            bd=0,
            cursor="hand2",
            command=command
        )
        button.grid(row=row, column=col, padx=4, pady=4, sticky="nsew")
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", lambda event, c=color: on_leave(event, c))

#Enter 
display.bind("<Return>", lambda event: calculate())

#autoPointToText
display.focus_set()

# Run application
window.mainloop()
