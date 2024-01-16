import tkinter as tk


def show_selected_option():
    selected_option = clicked.get()
    label.config(text=f"Selected option: {selected_option}")


# Create a Tkinter window
root = tk.Tk()
root.title("Dropdown Menu Example")

# Define options for the dropdown
options = ["Module 1", "Module 2", "Module 5", "Module 7",
           "Module 13", "Module 14", "Module 15", "Module 16",
           "Module 17", "Module 18", "Module 19", "Module 20",
           "Module 21", "Module 22", "Module 24", "Module 25",
           "Module 26", "Module 28", "Module 30", "Module 27",
           "Module 29", "Module 33", "Module 34", "Module 38"]


# Create a variable to store selected option
clicked = tk.StringVar()
clicked.set(options[0])  # Set default value

# Create a dropdown menu
drop = tk.OptionMenu(root, clicked, *options)
drop.pack()

# Create a button to display the selected option
show_btn = tk.Button(root, text="Show Selected Option", command=show_selected_option)
show_btn.pack()

# Label to display selected option
label = tk.Label(root, text="")
label.pack()

# Run the main loop
root.mainloop()
