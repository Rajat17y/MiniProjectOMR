from tkinter import *
from tkinter import messagebox
import Main

root = Tk()
root.title("OMR Application")
root.geometry("600x600")

# Frames
form_frame = Frame(root)
answer_frame = Frame(root)

# Pack the frames and stack them
for frame in (form_frame, answer_frame):
    frame.place(relwidth=1, relheight=1)

def scan():
    # Create a new top-level window
    new_window = Toplevel(root)
    new_window.title("Ananlysis")
    new_window.geometry("600x600")
    # Add some content to the new window
    label1 = Label(new_window, text="This is Analysis Window!", font=("Arial", 14))
    label1.pack(pady=20)

    def run():
        Main.reading(numques,numchoices,ans_ind,checkbox_vars[0].get(),checkbox_vars[1].get(),checkbox_vars[2].get(),checkbox_vars[4].get(),checkbox_vars[3].get())


    def update_label():
        selected_options = []
        for i, var in enumerate(checkbox_vars):
            if var.get() == 1:  # If the checkbox is checked (state is 1)
                selected_options.append(checkbox_labels[i])
        label.config(text="Selected: " + ", ".join(selected_options))
        #print(checkbox_vars[0].get())
        
    # List of checkbox options
    checkbox_labels = ["Rectangle", "Score", "Analysis","Record","WebCam"]
    checkbox_vars = []  # List to hold the IntVar() for each checkbox

    for label in checkbox_labels:
        var = IntVar()  # Create an IntVar() for each checkbox to hold its state (0 or 1)
        checkbox_vars.append(var)
        checkbox = Checkbutton(new_window, text=label, variable=var, command=update_label)
        checkbox.pack(anchor="w", padx=20, pady=5)

    # Label to display selected options
    label = Label(new_window, text="Selected: ", font=("Arial", 12))
    label.pack(pady=20)
    
    
    # Add a button in the new window to close it
    run_button = Button(new_window, text="RUN", command=run)
    run_button.pack(pady=20)
    close_button = Button(new_window, text="Close", command=new_window.destroy)
    close_button.pack(pady=10)

def show_frame(frame):
    frame.tkraise()

# Form
numques = 0
numchoices = 0
opts = ["A", "B", "C", "D", "E", "F"]
current_question = 0
user_data = []
ans_ind = []

def submit_form():
    global numques, numchoices, user_data, option_buttons
    
    # Get input values from the form
    numques = int(ques.get())
    numchoices = int(opt.get())
    _scr = selected_option.get()
    
    print(f"Questions: {numques}, Choices: {numchoices}, Source: {_scr}")
    
    if(numchoices==0 or numques==0):
        messagebox.showinfo("Not Accepted!","Number of questions or number of options can't be 0")
        return
    # Reset user_data and recreate option_buttons
    user_data = [""] * numques
    for rb in option_buttons:
        rb.destroy()
    option_buttons.clear()
    
    for i in range(numchoices):
        rb = Radiobutton(answer_frame, text="", variable=selected_opt, value="", font=("Arial", 12))
        rb.pack(anchor="w", padx=20)
        option_buttons.append(rb)
    
    # Show the answer frame and display the first question
    show_frame(answer_frame)
    display(1)

# Answer for each question
def display(number):
    global current_question
    heading.config(text=f"Enter correct option for question number {number}")
    for i in range(numchoices):
        option_buttons[i].config(text=opts[i], value=opts[i])
    # Pre-select the previously chosen answer, if any
    selected_opt.set(user_data[current_question])

def previous_question():
    global current_question
    if current_question > 0:
        user_data[current_question] = selected_opt.get()
        current_question -= 1
        display(current_question + 1)

def next_question():
    global current_question
    user_data[current_question] = selected_opt.get()
    if current_question < numques - 1:
        current_question += 1
        display(current_question + 1)
    else:
        messagebox.showinfo("Completed", "You've reached the end of the questions.")

def submit_quiz():
    user_data[current_question] = selected_opt.get()  # Save the last answer
    print("User Answers:", user_data)
    if("" in user_data):
        messagebox.showinfo("No value","Cannot be Empty!")
        return
    listbox.delete(0,END)
    for k in range(0,numques):
        listbox.insert(END,f"{k+1}. {user_data[k]}")
    ans_ind.clear()
    for i in user_data:
        ans_ind.append(opts.index(i))
    print(ans_ind)

    

def reenter():
    show_frame(form_frame)


listbox = Listbox(answer_frame,font=("Arial",12))
listbox.pack(pady=10)
# Form Variables
question = IntVar()
option = IntVar()
scr = StringVar()
selected_option = StringVar()
selected_option.set("WebCam")  # Default value

# Form Widgets
Label(form_frame, text="Number of Questions: ", font=("Arial", 12)).grid(row=0, column=0, pady=10, padx=10, sticky="w")
ques = Entry(form_frame, textvariable=question, font=("Arial", 12))
ques.grid(row=0, column=1, pady=5, padx=10)

Label(form_frame, text="Number of Options: ", font=("Arial", 12)).grid(row=1, column=0, pady=10, padx=10, sticky="w")
opt = Entry(form_frame, textvariable=option, font=("Arial", 12))
opt.grid(row=1, column=1, pady=5, padx=10)

Label(form_frame, text="Select Source: ", font=("Arial", 12)).grid(row=2, column=0, pady=10, padx=10, sticky="w")
options = ["WebCam", "Image"]
dropdown = OptionMenu(form_frame, selected_option, *options)
dropdown.config(font=("Arial", 12))
dropdown.grid(row=2, column=1, pady=10, padx=10)

Button(form_frame, text="SUBMIT", command=submit_form, font=("Arial", 12), bg="blue", fg="white").grid(row=3, column=1, pady=10, padx=10)

# Quiz Widgets
selected_opt = StringVar()
option_buttons = []

heading = Label(answer_frame, text="", font=("Arial", 14), wraplength=350, justify="center")
heading.pack(pady=20)

button_frame = Frame(answer_frame)
button_frame.pack(pady=20)

Button(button_frame, text="ReEnter", command=reenter, font=("Arial", 12), bg="purple", fg="white").grid(row=0, column=0, padx=10)
Button(button_frame, text="Previous", command=previous_question, font=("Arial", 12), bg="blue", fg="white").grid(row=0, column=1, padx=10)
Button(button_frame, text="Next", command=next_question, font=("Arial", 12), bg="green", fg="white").grid(row=0, column=2, padx=10)
Button(button_frame, text="Submit", command=submit_quiz, font=("Arial", 12), bg="red", fg="white").grid(row=0, column=3, padx=10)

Button(answer_frame,text="Scan", command=scan, font=("Arial", 12), bg="yellow", fg="black").pack(pady=20)

# Start with the form frame
show_frame(form_frame)

root.mainloop()
