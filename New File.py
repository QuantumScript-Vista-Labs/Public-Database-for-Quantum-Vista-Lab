import tkinter as tk
from tkinter import scrolledtext, Menu, filedialog, messagebox
import webbrowser

# Function to switch themes
def switch_theme():
    current_theme = txt_area.cget("background")
    if current_theme == "white":
        txt_area.config(background="black", foreground="white")
        root.config(background="black")
    else:
        txt_area.config(background="white", foreground="black")
        root.config(background="white")

# Function to open the settings window
def open_settings():
    settings_window = tk.Toplevel(root)
    settings_window.title("Settings")

    # Function to change font size
    def change_font_size():
        try:
            font_size = int(font_size_entry.get())
            txt_area.config(font=("TkFixedFont", font_size))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid font size.")

    font_size_label = tk.Label(settings_window, text="Font Size:")
    font_size_label.grid(row=0, column=0)

    font_size_entry = tk.Entry(settings_window)
    font_size_entry.grid(row=0, column=1)

    apply_button = tk.Button(settings_window, text="Apply", command=change_font_size)
    apply_button.grid(row=1, columnspan=2)

# Function to create a new file
def new_file():
    txt_area.delete(1.0, tk.END)

# Function to open a file
def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            txt_area.insert(tk.END, file.read())

# Function to save a file
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".py", filetypes=[("Python files", "*.py")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(txt_area.get(1.0, tk.END))

# Function to show about information
def about():
    messagebox.showinfo("About", "Visq Code - Simple Python IDE")

# Function to open about website
def open_about_website():
    about_url = "https://quantumscript-vista-labs.itch.io/visq-code"
    webbrowser.open_new(about_url)

# Main window
root = tk.Tk()
root.title("Visq Code")
root.configure(background="black")

# Text area for code editing
txt_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20, background="black", foreground="white")
txt_area.pack(expand=True, fill='both')

# Menu bar
menu_bar = Menu(root)

# File menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# Theme menu
theme_menu = Menu(menu_bar, tearoff=0)
theme_menu.add_command(label="Switch Theme", command=switch_theme)
menu_bar.add_cascade(label="Theme", menu=theme_menu)

# Help menu
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=about)
help_menu.add_command(label="About Website", command=open_about_website)
menu_bar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menu_bar)

root.mainloop()

