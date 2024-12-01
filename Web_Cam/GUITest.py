import tkinter as tk
from tkinter import messagebox

# Sample quiz data
quiz_data = [
    {"question": "What is the capital of France?", "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"], "answer": "C"},
    {"question": "Which programming language is known as the 'language of AI'?", "options": ["A. Python", "B. Java", "C. C++", "D. Ruby"], "answer": "A"},
    {"question": "What is 5 + 7?", "options": ["A. 10", "B. 12", "C. 15", "D. 11"], "answer": "B"},
]#List of dictionary

# Initialize variables
current_question = 0
user_answers = [""] * len(quiz_data)  # To store user selections

# Function to display a question
def display_question():
    question_label.config(text=quiz_data[current_question]["question"])
    for idx, option in enumerate(quiz_data[current_question]["options"]):
        option_buttons[idx].config(text=option, value=option[0])
    # Pre-select the previously chosen answer, if any
    selected_option.set(user_answers[current_question])

# Function to handle "Next" button click
def next_question():
    global current_question
    # Save the current answer
    user_answers[current_question] = selected_option.get()
    if current_question < len(quiz_data) - 1:
        current_question += 1
        display_question()
    else:
        messagebox.showinfo("Quiz Completed", "You've reached the end of the quiz.")

# Function to handle "Previous" button click
def previous_question():
    global current_question
    if current_question > 0:
        current_question -= 1
        display_question()

# Function to submit the quiz
def submit_quiz():
    user_answers[current_question] = selected_option.get()  # Save the last answer
    score = 0
    for idx, answer in enumerate(user_answers):
        if answer == quiz_data[idx]["answer"]:
            score += 1
    messagebox.showinfo("Quiz Results", f"You scored {score}/{len(quiz_data)}")

# Create the main window
root = tk.Tk()
root.title("Quiz Application")
root.geometry("400x300")

# Question label
question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=350, justify="center")
question_label.pack(pady=20)

# Options (Radio buttons)
selected_option = tk.StringVar()
option_buttons = []
for i in range(4):  # Assuming 4 options (A, B, C, D)
    rb = tk.Radiobutton(root, text="", variable=selected_option, value="", font=("Arial", 12))
    rb.pack(anchor="w", padx=20)
    option_buttons.append(rb)

# Navigation buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

prev_button = tk.Button(button_frame, text="Previous", command=previous_question, font=("Arial", 12), bg="blue", fg="white")
prev_button.grid(row=0, column=0, padx=10)

next_button = tk.Button(button_frame, text="Next", command=next_question, font=("Arial", 12), bg="green", fg="white")
next_button.grid(row=0, column=1, padx=10)

submit_button = tk.Button(button_frame, text="Submit", command=submit_quiz, font=("Arial", 12), bg="red", fg="white")
submit_button.grid(row=0, column=2, padx=10)

# Display the first question
display_question()

# Run the main loop
root.mainloop()
