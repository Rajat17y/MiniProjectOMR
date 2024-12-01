from tkinter import *
from tkinter import messagebox

# Initialize the main window
root = Tk()
root.title("Quiz Application")
root.geometry("600x600")

# Create frames for the form and the quiz
form_frame = Frame(root)
quiz_frame = Frame(root)

# Pack the frames and stack them
for frame in (form_frame, quiz_frame):
    frame.place(relwidth=1, relheight=1)

# Global variables for the quiz
numques = 5
numchoices = 4
opts = ["A", "B", "C", "D", "E", "F"]
current_question = 0
user_data = [""] * numques

# Function to switch between frames
def show_frame(frame):
    frame.tkraise()

### Form Interface ###
def submit_form():
    name = name_entry.get()
    age = age_entry.get()

    if name and age.isdigit():
        # Save form data or perform validation if needed
        messagebox.showinfo("Form Submitted", "Form submitted successfully!")
        show_frame(quiz_frame)  # Switch to the quiz frame
        display(current_question + 1)  # Display the first question
    else:
        messagebox.showerror("Error", "Please enter valid details!")

# Form Widgets
Label(form_frame, text="Enter Your Details", font=("Arial", 16)).pack(pady=20)
Label(form_frame, text="Name:", font=("Arial", 12)).pack(pady=5)
name_entry = Entry(form_frame, font=("Arial", 12))
name_entry.pack(pady=5)
Label(form_frame, text="Age:", font=("Arial", 12)).pack(pady=5)
age_entry = Entry(form_frame, font=("Arial", 12))
age_entry.pack(pady=5)
Button(form_frame, text="Submit", command=submit_form, font=("Arial", 12), bg="green", fg="white").pack(pady=20)

### Quiz Interface ###
def display(number):
    heading.config(text=f"Question {number}")
    for i in range(0, numchoices):
        option_buttons[i].config(text=opts[i], value=opts[i])

def next_question():
    global current_question
    user_data[current_question] = selected_opt.get()
    if current_question < numques - 1:
        current_question += 1
        display(current_question + 1)
    else:
        messagebox.showinfo("Quiz Completed", "You've reached the end of the quiz.")

def previous_question():
    global current_question
    if current_question > 0:
        current_question -= 1
        display(current_question + 1)

# Quiz Widgets
heading = Label(quiz_frame, text="", font=("Arial", 16))
heading.pack(pady=20)

selected_opt = StringVar()
option_buttons = []

for i in range(4):  # Assuming 4 options (A, B, C, D)
    rb = Radiobutton(quiz_frame, text="", variable=selected_opt, value="", font=("Arial", 12))
    rb.pack(anchor="w", padx=20)
    option_buttons.append(rb)

button_frame = Frame(quiz_frame)
button_frame.pack(pady=20)

Button(button_frame, text="Previous", command=previous_question, font=("Arial", 12), bg="blue", fg="white").grid(row=0, column=0, padx=10)
Button(button_frame, text="Next", command=next_question, font=("Arial", 12), bg="green", fg="white").grid(row=0, column=1, padx=10)

# Initially display the form frame
show_frame(form_frame)

# Start the main event loop
root.mainloop()
