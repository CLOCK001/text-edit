from tkinter import *

def save():
    extention = TextExtention.get()
    code = TextBox.get("1.0",END)
    
    with open(extention,'w') as f:
        f.write(code)

window = Tk()
window.geometry("550x550")
window.title("text-edit📝")

TextBox = Text(window,font=("mono",15))
TextBox.pack(fill=BOTH, expand=1)

TextSmall = Label(window,text="Save as:")
TextSmall.pack()

TextExtention = Entry(window,font=("mono",13))
TextExtention.pack()

ButtonSave = Button(window,text="save",command=save,fg="#000000")
ButtonSave.pack(pady= 10, padx= 10)

window.mainloop()