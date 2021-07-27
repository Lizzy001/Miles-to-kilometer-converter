import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)
# Label

my_label = tkinter.Label(text="I am a Label", font=("Arial", 20, "italic"))
my_label.config(text="New Text")
my_label["fg"] = "green"
my_label.grid(column=0, row=0)

# Button
button = tkinter.Button(text="Click Me", command="button_clicked")
button["fg"] = "yellow"
button.grid(column=1, row=1)

button = tkinter.Button(text="My Name is: Lizzy!")
button["fg"] = "coral"
button.grid(column=2, row=0)

# Entry
input = tkinter.Entry(width=15)
input.grid(column=3, row=2)





window.mainloop()
