from tkinter import *

result = 0
window = Tk()
window.title("Calc")
window.minsize(300, 300)
m_label = Label(text="Mile(s):", font=("Courier", 15, "bold"))
m_label.config(padx=20, pady=20)
m_label.grid(column=1, row=1)

m_entry = Entry(width=7, borderwidth=5, bg="lightblue")
m_entry.insert(END, 0)
m_entry.grid(column=2, row=1)

filler_label = Label(text="Is equal to:", font=("Courier", 15, "bold"))
filler_label.config(padx=20, pady=20)
filler_label.grid(column=1, row=2)

output = Label(text=("0 km"), font=("Courier", 15, "bold"))
output.config(padx=10, pady=10)
output.grid(column=2, row=2)

def calculate():
    global result
    miles = int(m_entry.get())
    result = round(miles * 1.609, 3)
    print("calculating.....")
    output.config(text=f"{result} km")
    return

button = Button(text="Calculate", width=10, command=calculate)
button.grid(column=1, row=3)



window.mainloop()
