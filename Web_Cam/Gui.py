from tkinter import *
from tkinter import messagebox  # Import messagebox explicitly
root = Tk()
root.title("OMR")
root.geometry("600x600")
'''
def on_button_click():
    label.config(text="Button Clicked!")

label = Label(root, text="Press the button below", font=("Arial", 14))
label.pack(pady=20)

button = Button(
    root,
    text = 'Click Me',
    font=("Arial", 12), 
    command=on_button_click, 
    bg="lightblue", 
    fg="black", 
    width=10, 
    height=2
)
button.pack(pady=20)
'''
'''
#Form 
q = 0
o = 0
def submit_from():
    q = ques.get()
    o = opt.get()
    scr = selected_option.get()

#Function to reset form
def reset_form():
    pass

#Variables to store user input
question = IntVar()
option = IntVar()
scr = StringVar()

#From Labels and entry fields
Label(root,text="Number of Questions: ",font=("Arial", 12)).grid(row=0, column=0, pady=50, padx=30, sticky="w")
ques = Entry(root,textvariable=question,font=("Arial", 12))
ques.grid(row=0, column=1, pady=5, padx=10)

Label(root,text="Number of Options: ",font=("Arial", 12)).grid(row=1, column=0, pady=50, padx=30, sticky="w")
opt = Entry(root,textvariable=option,font=("Arial", 12))
opt.grid(row=1, column=1, pady=5, padx=10)

# Create a StringVar to hold the selected value
selected_option = StringVar()
selected_option.set("Source")  # Default value

Label(root,text="Select Source: ",font=("Arial", 12)).grid(row=2, column=0, pady=50, padx=30, sticky="w")
options = ["WebCam","Image"]
dropdown = OptionMenu(root,selected_option,*options)
dropdown.config(font=("Arial",12))
dropdown.grid(row=2, column=1, pady=50, padx=30, sticky="w")

#Submit Button
submit = Button(root,text = "SUBMIT",command=submit_from,font=("Arial",12),bg="blue",fg="white")
submit.grid(row=3, column=1, pady=50, padx=30, sticky="w")
'''

form_frame = Frame(root)
answer_frame = Frame(root)

# Pack the frames and stack them
for frame in (form_frame, answer_frame):
    frame.place(relwidth=1, relheight=1)

def show_frame(frame):
    frame.tkraise()

#Form
numques = 4
numchoices = 6
q = 0
o = 0
_scr=""
def submit_from():
    global numchoices, numques
    numques = int(ques.get())
    numchoices = int(opt.get())
    _scr = selected_option.get()
    print(numques," ",numchoices," ",_scr)
    show_frame(answer_frame)

#Function to reset form
def reset_form():
    pass

#Variables to store user input
question = IntVar()
option = IntVar()
scr = StringVar()

#From Labels and entry fields
Label(form_frame,text="Number of Questions: ",font=("Arial", 12)).grid(row=0, column=0, pady=50, padx=30, sticky="w")
ques = Entry(form_frame,textvariable=question,font=("Arial", 12))
ques.grid(row=0, column=1, pady=5, padx=10)

Label(form_frame,text="Number of Options: ",font=("Arial", 12)).grid(row=1, column=0, pady=50, padx=30, sticky="w")
opt = Entry(form_frame,textvariable=option,font=("Arial", 12))
opt.grid(row=1, column=1, pady=5, padx=10)

# Create a StringVar to hold the selected value
selected_option = StringVar()
selected_option.set("WebCam")  # Default value

Label(form_frame,text="Select Source: ",font=("Arial", 12)).grid(row=2, column=0, pady=50, padx=30, sticky="w")
options = ["WebCam","Image"]
dropdown = OptionMenu(form_frame,selected_option,*options)
dropdown.config(font=("Arial",12))
dropdown.grid(row=2, column=1, pady=50, padx=30, sticky="w")

#Submit Button
submit = Button(form_frame,text = "SUBMIT",command=submit_from,font=("Arial",12),bg="blue",fg="white")
submit.grid(row=3, column=1, pady=50, padx=30, sticky="w")




#Answer for each questions

opts = ["A","B","C","D","E","F"]
current_question = 0
user_data = [""]*numques

def display(number):
    heading.config(text=f"Enter correct option for question number {number}")
    for i in range(0,numchoices):
        option_buttons[i].config(text=opts[i],value=opts[i])
    # Pre-select the previously chosen answer, if any
    

def previous_question():
    global current_question
    if current_question > 0:
        current_question -= 1
        display(current_question+1)

def next_question():
    global current_question
    user_data[current_question] = selected_opt.get()
    if current_question < numques-1:
        current_question += 1
        display(current_question+1)
    else:
        messagebox.showinfo("Quiz Completed", "You've reached the end of the quiz.")

def submit_quiz():
    user_data[current_question] = selected_opt.get()  # Save the last answer
    print(user_data)

def reenter():
    show_frame(form_frame)


#Heading Label
heading = Label(answer_frame, text="", font=("Arial", 14), wraplength=350, justify="center")
heading.pack(pady=20)

#Options
selected_opt = StringVar()
option_buttons = [] #List of option buttons

#Showing Options
for i in range(numchoices):  # Assuming 4 options (A, B, C, D)
    rb = Radiobutton(answer_frame, text="", variable=selected_opt, value="", font=("Arial", 12))
    rb.pack(anchor="w", padx=20)
    option_buttons.append(rb)

#Nevigation Buttons
button_frame = Frame(answer_frame)
button_frame.pack(pady=20)

re_enter = Button(button_frame, text="ReEnter", command=reenter, font=("Arial", 12), bg="purple", fg="white")
re_enter.grid(row=0, column=0, padx=10)

prev_button = Button(button_frame, text="Previous", command=previous_question, font=("Arial", 12), bg="blue", fg="white")
prev_button.grid(row=0, column=1, padx=10)

next_button = Button(button_frame, text="Next", command=next_question, font=("Arial", 12), bg="green", fg="white")
next_button.grid(row=0, column=2, padx=10)

submit_button = Button(button_frame, text="Submit", command=submit_quiz, font=("Arial", 12), bg="red", fg="white")
submit_button.grid(row=0, column=3, padx=10)

display(current_question+1)

show_frame(form_frame)

root.mainloop()