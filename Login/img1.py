from tkinter import *
def delete_root():
  root.destroy()
global root
root = Tk()
root.configure(background='light cyan')
root.geometry("400x700")
logo = PhotoImage(file="virat1.png")

w1 = Label(root, image=logo).pack()
Button(root,text = "back",height = "2", width = "20", command=delete_root,bg = "gray").pack(side=BOTTOM)  
root.mainloop()
