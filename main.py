from tkinter import *

PASTEL_BLUE = "#A7C7E7"

window = Tk()
window.title("TO-DO!!")
window.minsize(width=500, height=500)
window.config(bg=PASTEL_BLUE)

#label for the heading
heading = Label(window, text="To-Do List", font=("Helvetica", 18, "bold"), bg=PASTEL_BLUE, fg="white")
heading.grid(row=,column=,columnspan=)

window.mainloop()