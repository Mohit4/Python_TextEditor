__author__ = 'MOHIT'

from tkinter import *   #import tkinter and all neccessary libraries inside it
from tkinter import filedialog     #imported filedialog box for choosing a file
from tkinter import messagebox     #imported message boxes for use
from tkinter.scrolledtext import ScrolledText   #import scrolledtext from tkinter

mgui = Tk()    #created gui object
mgui.geometry('400x450')     #giving the size of the window
mgui.title('TextEditor')     #giving the title of the window

textpad = ScrolledText(mgui,height=600,width=400)    #created a ScrolledText obj linked to mgui,with height and width

def mnew():
    #add code here
    return
def mopen():
    ofil = filedialog.askopenfile(parent=mgui,mode='rb',title='Select a file')  #ask to open a file,read mode,title
    if (ofil != None):  #if file exists
        contents = ofil.read()  #read the contents
        textpad.insert('1.0',contents)  #insert on textpad
        ofil.close()  #close the file
def msave():
    sfil = filedialog.asksaveasfile(mode='w')  #ask to save a file, write mod
    if (sfil != None):   #if file exists
        data = textpad.get('1.0',END+'-1c')  #removed the last character as an extra return is added
        sfil.write(data)  #written the data
        sfil.close()  #closed the file
def mexit():
    if messagebox.askyesno(title='Quit',message='Are you sure?'):
        mgui.destroy()    #destroyed the gui
def mhelp():
    #add help here
    return
def mabout():
    about=messagebox.showinfo(title='About',message='A text editor created in Python 3.4')
    return

menubar = Menu(mgui)  #created a Menu object
filemenu = Menu(menubar,tearoff=0)  #linked a submenu filemenu to menubar,tearoff is false

filemenu.add_command(label='New',command=mnew)   #created a filemenu entry New and linked with method mnew
filemenu.add_command(label='Open',command=mopen)  #created a filemenu entry Open and linked with method mopen
filemenu.add_command(label='Save',command=msave)   #created a filemenu entry Save and linked with method msave
filemenu.add_command(label='Exit',command=mexit)   #created a filemenu entry Exit and linked with method mexit

menubar.add_cascade(label='File',menu=filemenu)    #cascaded filemenu to menubar with label File

helpmenu = Menu(menubar,tearoff=0)   #creating another menu in menubar
helpmenu.add_command(label='Help',command=mhelp)
helpmenu.add_command(label='About',command=mabout)
menubar.add_cascade(label='Help',menu=helpmenu)

"""editmenu = Menu(menubar,tearoff=0)  #creating another menu
editmenu.add_command(label='Find',command=)"""

textpad.pack()   #to put the textpad on gui
mgui.config(menu=menubar)       #configured to mgui
mgui.mainloop()    #for windows only, to call the gui mainloop
