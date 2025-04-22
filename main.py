from tkinter import *
from tkinter import messagebox

PASTEL_BLUE = "#A7C7E7"

window = Tk()
window.title("TO-DO!!")
window.minsize(width=693, height=478)
window.config(bg=PASTEL_BLUE)

#Background
canvas = Canvas(width=693,height=478, bg=PASTEL_BLUE, highlightthickness=0)
cloud_img = PhotoImage(file = "clouds.png")
card = canvas.create_image(346.5,239.5,image=cloud_img)
canvas.grid(row=0,column=0,columnspan=2)

#The heading
title = canvas.create_text(346.5,30,text="To-Do List", font=("Comic Sans MS", 18, "bold"), fill ="#4A61A1")

# Text
enter = canvas.create_text(170,100,text="Enter the task  :", font=("Comic Sans MS", 18, "bold"), fill ="#4A61A1")

# Entry box
task_entry = Entry(width=25, font=("Comic Sans MS", 12), bg=PASTEL_BLUE, fg="#4A61A1")
canvas.create_window(425, 100, window=task_entry)
task_entry.focus()

task_y = 120
#function to add the text
def add_text():
    text = task_entry.get()

    def on_check():
        if is_checked.get():
            messagebox.showinfo(title='YAY!', message="Task marked as completed!! 🎉")

    if text != "":
        global task_y
        task_y+=50
        is_checked = IntVar()
        checkbox = Checkbutton(text=text, font=("Comic Sans MS", 12), fg="#4A61A1" ,variable=is_checked, bg=PASTEL_BLUE,
                               highlightthickness=0, wraplength=550, justify="left", command=on_check)
        canvas.create_window(100, task_y, window=checkbox, anchor="w")
        task_entry.delete(0,"end")

        if not is_checked:
            messagebox.showinfo(title='OOPS', message="YAYYYY!! TASK COMPLETED!! ALMOST DONE!!")
    else:
        messagebox.showinfo(title='OOPS', message="Please don't leave the field empty!!")

# Button to add
add_button = Button(text="Add Task", font=("Comic Sans MS", 12, "bold"), bg="#4A61A1", fg="white", command=add_text)
canvas.create_window(620, 100, window=add_button)

window.mainloop()