import tkinter as tk

window = tk.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

# Label
## first needs to create a label
my_label = tk.Label(text = "I am a label", font = ("Arial", 24, "bold"))
## second get hold and pack / place it in the screen
#my_label.pack()
my_label.place(x= 100, y = 100)

# both of the following are doing the same, just two different ways
my_label["text"] = "New Text"
#my_label.config(text="New Text")
my_label.grid(column=0, row = 0)

#Button
def button_clicked():
    print("I got clicked")
    my_label.config(text=input.get())

button = tk.Button(text = "Click Me", command=button_clicked)
#button.pack()
button.grid(column = 1, row = 1)

# Entry
input = tk.Entry(width=10)
#input.pack()
input.grid(column = 3, row = 3)

#input.get()

window.mainloop()

