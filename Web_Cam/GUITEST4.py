from tkinter import *

def update_label():
    # Update the label based on the selected checkboxes
    selected_options = []
    for i, var in enumerate(checkbox_vars):
        if var.get() == 1:  # If the checkbox is checked (state is 1)
            selected_options.append(checkbox_labels[i])
    label.config(text="Selected: " + ", ".join(selected_options))

root = Tk()
root.title("Live Checkbox Example")
root.geometry("400x300")

# List of checkbox options
checkbox_labels = ["Option A", "Option B", "Option C", "Option D"]
checkbox_vars = []  # List to hold the IntVar() for each checkbox

# Create checkboxes dynamically
for label in checkbox_labels:
    var = IntVar()  # Create an IntVar() for each checkbox to hold its state (0 or 1)
    checkbox_vars.append(var)
    checkbox = Checkbutton(root, text=label, variable=var, command=update_label)
    checkbox.pack(anchor="w", padx=20, pady=5)

# Label to display selected options
label = Label(root, text="Selected: ", font=("Arial", 12))
label.pack(pady=20)

root.mainloop()
