#!/usr/local/bin/python3

from tkinter import *
from tkinter.font import Font
from tkinter import filedialog
import pickle

root = Tk()
root.title('Lista De Tareas')


my_frame=Frame(root)
my_frame.pack(pady=10)

my_list = Listbox(my_frame,
                width=40,
                height=10,
                bd=0,
                fg="red",
                highlightthickness=0,
                selectbackground="#a6a6a6",
                activestyle="none")

my_list.grid(row=0,column=0)
my_list.config(font=("Courier", 16, "italic"))

my_scrollbar= Scrollbar(my_frame)
my_scrollbar.grid(row=0,column=1,sticky="nsew")

my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

my_entry = Entry(root,width=40)
my_entry.pack()

button_frame = Frame(root)
button_frame.pack(pady=20)

def delete_item():
    my_list.delete(ANCHOR)
def add_item():
    my_list.insert(END,my_entry.get())
    my_entry.delete(0,END)
def cross_off_item():
    my_list.itemconfig(
        my_list.curselection(),
        fg="green"
    )
    my_list.selection_clear(0, END)
def uncross_off_item():
    my_list.itemconfig(
        my_list.curselection(),
        fg="blue"
    )
    my_list.selection_clear(0, END)
    
def delete_crossed():
    count = 0
    while count < my_list.size():
        if my_list.itemcget(count,"fg")== "green":
            my_list.delete(my_list.index(count))
        else:
            count+=1
            
def save_list():
    file_name=filedialog.asksaveasfilename(initialdir="/home/jungar/Escritorio/Python/listatarea/",title="Save File",filetypes=(("Dat Files",".dat"),("All Files","*.*")))
    
    if file_name:
        if file_name.endswith(".dat"):
            pass
        else:
            file_name= f'{file_name}.dat'
            
    count = 0
    while count < my_list.size():
        if my_list.itemcget(count,"fg")== "green":
            my_list.delete(my_list.index(count))
        else:
            count+=1
            
    stuff=my_list.get(0,END)
    
    output_file=open(file_name,'wb')
    
    pickle.dump(stuff,output_file)
def open_list():
    file_name = filedialog.askopenfilename(initialdir="/home/jungar/Escritorio/Python/listatarea/",title="Open File",filetypes=(("Dat Files",".dat"),("All Files","*.*")))
    
    if file_name:
        my_list.delete(0,END)
        
        input_file=open(file_name,'rb')
        
        stuff = pickle.load(input_file)
        
        for item in stuff:
            my_list.insert(END,item)
def delete_list():
    my_list.delete(0,END)


my_menu=Menu(root)
root.config(menu=my_menu)

file_menu=Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="Archivo",menu=file_menu)

file_menu.add_command(label="Abrir Lista",command=open_list)
file_menu.add_command(label="Guardar Lista",command=save_list)
file_menu.add_separator()
file_menu.add_command(label="Borrar Lista",command=delete_list)

delete_button=Button(button_frame,text="Borrar", command=delete_item)
add_button=Button(button_frame,text="Crear", command=add_item)
cross_of_button=Button(button_frame,text="Tarea Completada", command=cross_off_item)
uncross_of_button=Button(button_frame,text="Descompletar Tarea", command=uncross_off_item)
deletecross_of_button=Button(button_frame,text="Borrar Tareas Completadas", command=delete_crossed)

delete_button.grid(row=0,column=0)
add_button.grid(row=0,column=1,padx=10)
cross_of_button.grid(row=0,column=2)
uncross_of_button.grid(row=0,column=3,padx=10)
deletecross_of_button.grid(row=0,column=4)
    
root.mainloop()
    
