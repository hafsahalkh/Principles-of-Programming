import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog, scrolledtext, messagebox

# Import the tokenize function and symbol_table variable from lexer.py
from lexer import tokenize, symbol_table

# Function to load a file and display its content
def load_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
            input_text.delete(1.0, tk.END)
            input_text.insert(tk.END, content)

# Function to run the lexer and display only the symbol table
def run_lexer():
    source_code = input_text.get(1.0, tk.END)
    if not source_code.strip():
        messagebox.showwarning("no input!", "please load or enter source code to analyze <3")
        return
    
    # Run the lexer to generate tokens and populate the symbol table
    tokenize(source_code)  # Tokenizes the source code and populates the symbol table

    result_text.delete(1.0, tk.END)  # Clear previous results

    # Display the symbol table with updated scopes and formatting
    result_text.insert(tk.END, "Symbol Table:\n")
    result_text.insert(tk.END, f"{'Lexeme':<15}{'Token Class':<15}{'Symbol Type':<15}{'Data Type':<12}{'Value':<10}{'Scope':<10}\n")
    result_text.insert(tk.END, "-" * 70 + "\n")
    for entry in symbol_table:
        lexeme = entry["lexeme"]
        token_class = entry["token_class"]
        symbol_type = entry["symbol_type"]
        data_type = entry["data_type"] if entry["data_type"] else "None"
        value = entry["value"] if entry["value"] else "0"
        scope = entry["scope"]
        result_text.insert(tk.END, f"{lexeme:<15}{token_class:<15}{symbol_type:<15}{data_type:<12}{value:<10}{scope}\n")


# Setting up the GUI window using tkinter
window = tk.Tk()
window.configure(bg="#f9baff")  
window.title("Fall 2024: Group 2 Programming Languages Lexical Analyzer GUI")

# Set the window size and center it on the screen
window_width = 650
window_height = 650
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Input text area
label = tk.Label(window, text="Source Code:", font=("Helvetica", 10))
label.pack(pady=2)
input_text = scrolledtext.ScrolledText(window, wrap=tk.WORD, height=10, bg="#fcdfff")
input_text.pack(fill=tk.BOTH, expand=True)

# Define a custom style for rounded buttons
style = ttk.Style()
style.configure("Rounded.TButton", font=("Helvetica", 10), padding=2, relief="flat")
style.map("Rounded.TButton", background=[("active", "#d1d1e0")])

# Create a frame for the buttons
button_frame = tk.Frame(window)
button_frame.pack(fill=tk.X, pady=2)

# Load and Run Lexer buttons
load_button = ttk.Button(button_frame, text="Load File", style="Rounded.TButton", command=load_file)
load_button.pack(side=tk.LEFT, padx=5, pady=5)

run_button = ttk.Button(button_frame, text="Run Lexer", style="Rounded.TButton", command=run_lexer)
run_button.pack(side=tk.LEFT, padx=5, pady=5)

# Result text area for displaying only the symbol table
label2 = tk.Label(window, text="Symbol Table:", font=("Helvetica", 10))
label2.pack(pady=2)
result_text = scrolledtext.ScrolledText(window, wrap=tk.WORD, height=20, bg="#fcdfff")
result_text.pack(fill=tk.BOTH, expand=True)

# Run the GUI loop
window.mainloop()
