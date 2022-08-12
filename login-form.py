from tkinter import *
root=Tk()
root.geometry("980x700+0+0")
root.title("Cyber Security")
root.configure(bg="sky blue")

Tops = Frame(root,bg="light blue",width = 950,height=50,relief=SUNKEN)
Tops.pack(side=TOP)


#-----------------INFO TOP------------
lblinfo = Label(Tops, font=( 'aria' ,30, 'bold' ),text="Login Form",fg="steel blue")
lblinfo.grid(row=0,column=1)
lbl = Label(Tops,bg="light blue",bd='50')
lbl.grid(row=0,column=2)
lbl = Label(Tops,bg="light blue")
lbl.grid(row=0,column=3)
lbl = Label(Tops,bg="light blue",bd='50')
lbl.grid(row=0,column=0)
lbl = Label(Tops,bg="light blue")
lbl = Label(Tops,bg="light blue")
lbl.grid(row=2,column=0)
lbl = Label(Tops,bg="light blue")
lbl.grid(row=3,column=0)
lbl = Label(Tops)
lbl.grid(row=4,column=0)
lbl = Label(Tops, font=( 'aria' ,16, 'bold' ),text="UserName:",fg="steel blue",)
lbl.grid(row=5,column=0)
e1 = Entry(Tops,font=('ariel' ,16,'bold') ,justify='left')
e1.grid(row=5,column=1)
lbl = Label(Tops, font=( 'aria' ,16, 'bold' ),text="Password:",fg="steel blue",)
lbl.grid(row=6,column=0)
e2 = Entry(Tops,font=('ariel' ,16,'bold'),show="*",justify='left')
e2.grid(row=6,column=1)
def call():
    if e1.get()=="rakesh" and e2.get()=="1234":
        messagebox.showinfo("Login","login done")
    else:
        messagebox.showerror("Login","invalid credentials")
        
btn=Button(Tops,text="Login",font=('ariel' ,16,'bold'),command=call)
btn.grid(column=1,row=7)

root.mainloop()
