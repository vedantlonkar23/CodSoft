import tkinter as gui
from tkinter import messagebox 

window = gui.Tk()
window.geometry('300x500')
window.title("TO DO LIST")
window.configure(bg="lightgrey")
t1 = gui.StringVar()
def add_task():
    t1 = addtask.get()
    if t1:
        list.insert(gui.END,t1)
        addtask.delete(0,gui.END)
    else:
        messagebox.showwarning("Warning","EMPTY ENTRY")
def delete_task():
    selectedtask = list.curselection()
    if selectedtask:
        list.delete(selectedtask)
    else:
        messagebox.showwarning("Warning","NO TASK SELECTED")
def clearall():
    list.delete(0,gui.END)

addtask = gui.Entry(window,bd=2,width=30)
addtask.pack(pady=30)#place(relx=0.15,rely=0.5)
list = gui.Listbox(window,selectmode="SINGLE",width=30,bd=2)
list.pack(pady=20)
btn1 = gui.Button(window, text="ADD TASK",width=30,command=add_task,bg='grey',fg='white').place(relx = 0.15   , rely = 0.7,anchor="nw")
btn2 = gui.Button(window, text="DELETE TASK",width=30,command=delete_task,bg='grey',fg='white').place(relx = 0.15   , rely = 0.8,anchor="nw")
btn3 = gui.Button(window, text="CLEAR ALL TASKS",width=30,command=clearall,bg='grey',fg='white').place(relx = 0.15   , rely = 0.9,anchor="nw")
window.mainloop()