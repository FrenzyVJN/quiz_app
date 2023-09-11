import csv
import tkinter as tk
from tkinter import END,FLAT,RAISED
from tkinter import messagebox
from tkinter import PhotoImage
quiz=[]
def nextq():
    q=e1.get()
    a=e2.get()
    oo1=oe1.get()
    oo2=oe2.get()
    oo3=oe3.get()
    #oo4=oe4.get()
    if q=="" or a=="":
        messagebox.showinfo("ERROR", "Try Again, Question or Answer cannot be blank")
        print("Try again")
    else:
        quiz.append([q,a])
        print(quiz)
        with open("login.csv","w",newline="") as csvfile:
            writer=csv.writer(csvfile,delimiter=",")
            writer.writerows(quiz)
        e1.delete(0,END)
        e2.delete(0,END)
        oe1.delete(0,END)
        oe2.delete(0,END)
        oe3.delete(0,END)
        #oe4.delete(0,END)
        messagebox.showinfo("Success","Entry successfully added!!!")

def submit():
    nextq()
    win.destroy()

def login():
    global win
    win=tk.Tk()
    win.geometry("1100x600")
    win.title("Registration Portal")
    bg=PhotoImage(file="QuizBG1.png")
    l1=tk.Label(win,image=bg).place(x=0,y=0)
    frame=tk.Frame(win,height=0,width=0).place(x=175,y=100)
    #bg3=PhotoImage(file="entrybox1.png")
    global e1,e2,oe1,oe2,oe3
    #cnt=tk.Label(frame,text=x,fg="White",bg="#1F244A").place(x=375,y=20)
    head=tk.Label(frame,text="Test Registration Portal",bg="#1F244A",fg="White" ,font=("Vijaya",30)).place(x=375,y=60)
    q1=tk.Label(frame,text="Name ",bg="#1F244A",fg="White",font=("Vijaya",20)).place(x=325,y=130)
    e1=tk.Entry(frame,bd=0,font=("Vijaya",20),bg="#1F244A",fg="White")
    a2_line=tk.Canvas(win,width=255,height=2.0,bg="white",highlightthickness=0).place(x=530,y=168)
    e1.place(x=550,y=130)
    a1=tk.Label(frame,text="USN Number ",bg="#1F244A",fg="White",font=("Vijaya",20))
    a1.place(x=325,y=180)
    e2=tk.Entry(frame,bd=0,font=("Vijaya",20),bg="#1F244A",fg="White")
    a2_line=tk.Canvas(win,width=255,height=2.0,bg="white",highlightthickness=0).place(x=530,y=218)
    e2.place(x=550,y=180)
    o1=tk.Label(frame,text="Student or Teacher (S/N)  ",bg="#1F244A",fg="White",font=("Vijaya",20))
    o1.place(x=325,y=230)
    oe1=tk.Entry(frame,bd=0,font=("Vijaya",20),bg="#1F244A",fg="White")
    a2_line=tk.Canvas(win,width=255,height=2.0,bg="white",highlightthickness=0).place(x=530,y=268)
    oe1.place(x=550,y=230)
    o2=tk.Label(frame,text="Section ",bg="#1F244A",fg="White",font=("Vijaya",20))
    o2.place(x=325,y=280)
    oe2=tk.Entry(frame,bd=0,font=("Vijaya",20),bg="#1F244A",fg="White")
    oe2.place(x=550,y=280)
    a2_line=tk.Canvas(win,width=255,height=2.0,bg="white",highlightthickness=0).place(x=530,y=318)
    o3=tk.Label(frame,text="School Code ",bg="#1F244A",fg="White",font=("Vijaya",20))
    o3.place(x=325,y=330)
    oe3=tk.Entry(frame,bd=0,font=("Vijaya",20),bg="#1F244A",fg="White")
    a2_line=tk.Canvas(win,width=255,height=2.0,bg="white",highlightthickness=0).place(x=530,y=368)
    oe3.place(x=550,y=330)
##    o4=tk.Label(frame,text="MISC ",bg="#1F244A",fg="White",font=("Vijaya",20))
##    o4.place(x=325,y=380)
##    oe4=tk.Entry(frame,bd=0,font=("Vijaya",20))
##    oe4.place(x=550,y=380)
    bg1=PhotoImage(file="submitbtn.png")
    bg2=PhotoImage(file="nextbtn.png")
    btn=tk.Button(frame,text="Next Question",image=bg2,bg="#1F244A",border=0,font=30,command=nextq)
    btn.place(x=460,y=430)
    exitbtn=tk.Button(frame,text="Submit and exit",image=bg1,bg="#1F244A",border=0,font=30,command=submit).place(x=440,y=480)
    win.mainloop()
login()
