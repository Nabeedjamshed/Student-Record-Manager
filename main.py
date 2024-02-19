from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import pyodbc

m=Tk()
screen_width = m.winfo_screenwidth()
screen_height = m.winfo_screenheight()
m.geometry(f"{screen_width}x{screen_height}")
var1=StringVar()
var2=StringVar()
var3=StringVar()
var4=StringVar()

conncetor = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Nabeed\Documents\project.accdb'
connect = pyodbc.connect(conncetor)
cursor = connect.cursor()
def clear():
    var1.set("")
    var2.set("")
    var3.set("")
    var4.set("")
def display():
    query = '''
            SELECT Student.S_Name, Student.Dept_ID, Department.Year, Department.GPA
            FROM Student INNER JOIN Department ON Student.S_ID = Department.S_ID;
            '''
    cursor.execute(query)
    rows=cursor.fetchall()
    new = Toplevel()
    screen_width = new.winfo_screenwidth()
    screen_height = new.winfo_screenheight()
    new.geometry(f"{screen_width}x{screen_height}")
    style=ttk.Style()
    style.configure('Treeview.Heading',font=("Arial black",14,"bold"))
    tree_view=ttk.Treeview(new) 
    tree_view.tag_configure('font',font=('Arial',11))
    tree_view.tag_configure('bg', background="light blue")
    tree_view['columns']=('1','2','3','4')
    tree_view.heading('1',text="Std_Name",anchor=W)
    tree_view.heading('2',text="Std_ID",anchor=W)
    tree_view.heading('3',text="Year",anchor=W)
    tree_view.heading('4',text="GPA",anchor=W)

    for i in rows:
        tree_view.insert('',index='end',values=(i[0],i[1],i[2],i[3]),tags=('font','bg'))  
    tree_view.place(x=160,y=200)
    f3 = Frame(new,bg='black',width=800,height=40)
    f3.pack(side=TOP, fill=X)
    f4 = Frame(new,bg='black',width=1400,height=40)
    f4.place(x=0,y=665)
    new.mainloop()
def add():
    cursor.execute(f"INSERT INTO Student VALUES('{var1.get()}','{var2.get()}','{var3.get()}','{var4.get()}')")
    cursor.commit()
    messagebox.showinfo("One record has been added")

def update():
    cursor.execute(f"UPDATE Student SET Address='{var3.get()}' WHERE S_ID={var1.get()}")
    cursor.commit()
    messagebox.showinfo("One record has been UPDATED")

def delete():
    cursor.execute(f"DELETE FROM Student WHERE S_ID={var1.get()}")
    cursor.commit()
    messagebox.showinfo("One record has been DELETED")

l1=Label(m, text="Student Management System", bg="#3f92ff", fg="black", font=("Arial Black",25))
l1.pack(side=TOP,fill=X)
f1=Frame(bg="grey",width=500,height=750)
f1.place(x=0,y=45)
l2=Label(f1,text="Std_ID",bg="black", fg="white",width=10, font=("Arial Black",15))
l2.grid(column=0,row=1,padx=50,pady=20)
l3=Label(f1,text="Std_Name",bg="black", fg="white",width=10, font=("Arial Black",15))
l3.grid(column=0,row=2,padx=50,pady=20)
l4=Label(f1,text="Address",bg="black", fg="white",width=10, font=("Arial Black",15))
l4.grid(column=0,row=3,padx=50,pady=20)
l5=Label(f1,text="Dept_ID",bg="black", fg="white",width=10, font=("Arial Black",15))
l5.grid(column=0,row=4,padx=50,pady=20)
l6=Label(f1,text="Program",bg="black", fg="white",width=10, font=("Arial Black",15))
l6.grid(column=0,row=5,padx=50,pady=20)
e1=Entry(f1,textvariable=var1,font=("Arial Black",15)).grid(column=1,row=1,padx=50,pady=20)
e2=Entry(f1,textvariable=var2,font=("Arial Black",15)).grid(column=1,row=2,padx=50,pady=20)
e3=Entry(f1,textvariable=var3,font=("Arial Black",15)).grid(column=1,row=3,padx=50,pady=20)
e4=Entry(f1,textvariable=var4,font=("Arial Black",15)).grid(column=1,row=4,padx=50,pady=20)

lst=Listbox(f1,bg="light blue",fg="black",font=("Arial Black",10))
lst.insert(1,"SE")
lst.insert(2,"CSIT")
lst.insert(3,"EE")
lst.insert(4,"CIS")
lst.grid(column=1,row=5)

b1=Button(f1,text="Display",bg="black",fg="white",font=("Arial Black",15),command=display)
b1.grid(column=0,row=10,padx=50,pady=20)
b2=Button(f1,text="Add",bg="black",fg="white",font=("Arial Black",15),command=add)
b2.grid(column=1,row=10,padx=50,pady=20)
b3=Button(f1,text="Delete",bg="black",fg="white",font=("Arial Black",15),command=delete)
b3.grid(column=0,row=11,padx=50,pady=20)
b4=Button(f1,text="Update",bg="black",fg="white",font=("Arial Black",15),command=update)
b4.grid(column=1,row=11,padx=50,pady=20)
b4=Button(f1,text="Clear",width=12,height=1,bg="blue",fg="white",font=("Arial Black",15),command=clear)
b4.place(x=339,y=440)
f2=Frame(bg="white",width=800,height=750)
f2.place(x=600,y=45)

img = Image.open("R.webp")
rez = img.resize((350,300))
n_img = ImageTk.PhotoImage(rez)
imag = Label(m, image=n_img,bg='white')
imag.image=n_img
imag.place(x=800,y=270)


m.mainloop()