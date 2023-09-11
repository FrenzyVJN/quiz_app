import tkinter as tk
import csv
from tkinter import PhotoImage,FLAT
import stuguiv12
from tkinter import messagebox
from tkinter import END,FLAT,RAISED
import matplotlib.pyplot as plt
import numpy as np
csvfile= open("login.csv","r")
read = csv.reader(csvfile,delimiter = ",")
log = list(read)
print(log)

def logg():
    if str(a2.get()).lower()=='teacher':
        win.destroy()
        def teacher():
            win1=tk.Tk()
            win1.geometry("1100x600")
            win1.title("TP")
            win1.resizable(0,0)
            bg=PhotoImage(file="QuizBG1.png")
            l1=tk.Label(win1,image=bg).place(x=0,y=0)
            frame=tk.Frame(win1,height=0,width=0).place(x=175,y=100)
            def button1():
                win1.destroy()
                def teacher_gui():
                    quiz=[]
                    def nextq():
                        q=e1.get()
                        a=e2.get()
                        oo1=oe1.get()
                        oo2=oe2.get()
                        oo3=oe3.get()
                        oo4=oe4.get()
                        if q=="" or a=="":
                            messagebox.showinfo("ERROR", "Try Again, Question or Answer cannot be blank")
                            print("Try again")
                        else:
                            def count():
                                with open("question.csv") as csvfile:
                                    reader=csv.reader(csvfile,delimiter=",")
                                    global a
                                    a=list(reader)
                                    global x
                                    x=len(a)
                                    print(x)
                            quiz.append([q,a,oo1,oo2,oo3,oo4])
                            print(quiz)
                            with open("question.csv","a",newline="") as csvfile:
                                writer=csv.writer(csvfile,delimiter=",")
                                writer.writerows(quiz)
                            e1.delete(0,END)
                            e2.delete(0,END)
                            oe1.delete(0,END)
                            oe2.delete(0,END)
                            oe3.delete(0,END)
                            oe4.delete(0,END)
                            messagebox.showinfo("Success","Entry successfully added!!!")

                            
                    def submit():
                        nextq()
                        win.destroy()

                    def login():
                        global win
                        win=tk.Tk()
                        win.geometry("1100x600")
                        win.title("Teacher Portal")
                        bg=PhotoImage(file="QuizBG1.png")
                        l1=tk.Label(win,image=bg).place(x=0,y=0)
                        frame=tk.Frame(win,height=0,width=0).place(x=175,y=100)
                        #bg3=PhotoImage(file="entrybox1.png")
                        global e1,e2,oe1,oe2,oe3,oe4
                        #cnt=tk.Label(frame,text=x,fg="White",bg="#1F244A").place(x=375,y=20)
                        head=tk.Label(frame,text="Teacher Test Portal",bg="#1F244A",fg="White" ,font=("Vijaya",30)).place(x=375,y=60)
                        q1=tk.Label(frame,text="Enter question ",bg="#1F244A",fg="White",font=("Vijaya",20)).place(x=325,y=130)
                        e1=tk.Entry(frame,bd=0,font=("Vijaya",20))
                        e1.place(x=550,y=130)
                        a1=tk.Label(frame,text="Enter correct answer ",bg="#1F244A",fg="White",font=("Vijaya",20))
                        a1.place(x=325,y=180)
                        e2=tk.Entry(frame,bd=0,font=("Vijaya",20))
                        e2.place(x=550,y=180)
                        o1=tk.Label(frame,text="Enter option 1 ",bg="#1F244A",fg="White",font=("Vijaya",20))
                        o1.place(x=325,y=230)
                        oe1=tk.Entry(frame,bd=0,font=("Vijaya",20))
                        oe1.place(x=550,y=230)
                        o2=tk.Label(frame,text="Enter option 2 ",bg="#1F244A",fg="White",font=("Vijaya",20))
                        o2.place(x=325,y=280)
                        oe2=tk.Entry(frame,bd=0,font=("Vijaya",20))
                        oe2.place(x=550,y=280)
                        o3=tk.Label(frame,text="Enter option 3 ",bg="#1F244A",fg="White",font=("Vijaya",20))
                        o3.place(x=325,y=330)
                        oe3=tk.Entry(frame,bd=0,font=("Vijaya",20))
                        oe3.place(x=550,y=330)
                        o4=tk.Label(frame,text="Enter option 4 ",bg="#1F244A",fg="White",font=("Vijaya",20))
                        o4.place(x=325,y=380)
                        oe4=tk.Entry(frame,bd=0,font=("Vijaya",20))
                        oe4.place(x=550,y=380)
                        bg1=PhotoImage(file="submitbtn.png")
                        bg2=PhotoImage(file="nextbtn.png")
                        btn=tk.Button(frame,text="Next Question",image=bg2,bg="#1F244A",border=0,font=30,command=nextq)
                        btn.place(x=460,y=430)
                        exitbtn=tk.Button(frame,text="Submit and exit",image=bg1,bg="#1F244A",border=0,font=30,command=submit).place(x=440,y=480)
                        win.mainloop()
                    login()
                def login_gui():
                    def a():
                        win=tk.Tk()
                        win.geometry("920x500")
                        win.title("Login Portal")
                        bg1=PhotoImage(file="QuizBG2.png")

                        tk.Label(win,image=bg1).place(x=0,y=0)
                        global login
                        def login():
                            if [a2.get(),(b2.get())] in log:
                                messagebox.showinfo("Login", "Login Successful")
                                global z
                                z="Login"
                                win.destroy()
                                teacher_gui()
                            else:
                                messagebox.showinfo("Login", "Login Unsuccessful. Wrong Credentials/n If you have not created a account, Please contact your school administrator.")
                        tk.Label(win,text="Login Portal",fg="white",bg="#1F244A",font=("Comic Sans MS",40)).place(x=300,y=100)

                        a1=tk.Label(text="UserName",bg="#1F244A",fg="white",font=("Comic Sans MS",16))
                        a1.place(x=180,y=200)
                        a2=tk.Entry(bg="#1F244A",fg="White",relief=FLAT,font=16)
                        a2.place(x=395,y=200)
                        a2_line=tk.Canvas(win,width=275,height=2.0,bg="white",highlightthickness=0).place(x=365,y=225)
                        b1=tk.Label(text="USN Number",bg="#1F244A",fg="white",font=("Comic Sans MS",16))
                        b1.place(x=180,y=250)
                        b2=tk.Entry(bg="#1F244A",fg="White",relief=FLAT,font=16)
                        b2.place(x=395,y=250)
                        a3_line=tk.Canvas(win,width=275,height=2.0,bg="white",highlightthickness=0).place(x=365,y=275)
                        bg2=PhotoImage(file="submitbtn.png")
                        btn1=tk.Button(text="Login",image=bg2,border=0,bg="#1F244A",command=login)
                        btn1.place(x=430,y=300)
                        win.mainloop()
                    global log
                    csvfile= open("login.csv","r")
                    read = csv.reader(csvfile,delimiter = ",")
                    log = list(read)
                    print(log)
                    a() ##if StudentName == x and USN_Number == y:
                    csvfile.close()
                    
                login_gui()
            def button2():
                win1.destroy()
                def result():
                    win=tk.Tk()
                    win.geometry("1100x600")
                    win.title("Results Portal")
                    bg=PhotoImage(file="QuizBG1.png")
                    l1=tk.Label(win,image=bg).place(x=0,y=0)
                    frame=tk.Frame(win,height=0,width=0).place(x=175,y=100)
                    answerfile=open("answer.csv",mode="r")
                    questionfile=open("question.csv",mode="r")
                    myreader=list(csv.reader(answerfile))
                    myquestions=list(csv.reader(questionfile))
                    b=[]
                    c=[]
                    d=[]
                    m=[]
                    x=[]

                    wq=0
                    ccount=0
                    wcount=0
                    ##for x in myreader:
                    ##    x.append(myreader[0])
                    for i in range(len(myreader)):
                        a=myreader[i][2:]
                        for j in range(len(a)):
                            if a[j]==myquestions[j][1]:
                                b.append([myreader[i][0],j])
                            else:
                                c.append([myreader[i][0],j])
                    for i in range(len(myreader)):
                        d.append(myreader[i][0])
                    for i in d:
                        cq=0
                        for j in range(len(b)):    
                            if b[j][0]==i:
                                cq+=1
                        m.append([i,cq])
                        wq=0
                        for k in range(len(c)):
                            if c[k][0]==i:
                                wq+=1
                        x.append([i,wq])

                    #print(myreader)
                    #print(b)
                    print("no of correct questions of each student=",m)
                    print("no of wrong questions of each student=",x)
                    def printer():
                        giv=Entrybox1.get()
                        num=len(b)
                        #print(len(myreader))
                        for i in range(len(myreader)):
                            if giv==m[i][0]:
                                avg=(m[i][1]/num)*100 # avg = % of correct answers
                                y=np.array([avg,100-avg])
                                mylabel=[('Correct answer',avg),('Incorrect answer',100-avg)]
                                plt.pie(y,labels=mylabel)
                                plt.show()
                                lbl1=tk.Label(text=('number of correct answers of {} = '.format(i[0]),m[i][1]),font=30,bg="#1F244A",fg="White").place(x=300,y=400)
                                lbl2=tk.Label(text=('number of wrong answers of {} = '.format(i[0]),x[i][1]),font=30,bg="#1F244A",fg="White").place(x=300,y=430)

                            else:
                                continue
                    Label1=tk.Label(text='Enter student name to be searched : ',font=('Vijaya',25),fg='White',bg='#1F244A')
                    Label1.place(x=150,y=200)
                    a2_line=tk.Canvas(win,width=275,height=2.0,bg="white",highlightthickness=0).place(x=530,y=260)
                    Entrybox1=tk.Entry(frame,bd=0,relief=FLAT,bg="#1F244A",fg="White",font=('Vijaya',30))
                    Entrybox1.place(x=550,y=200)
                    btn1=tk.Button(text='Continue',font=30,command=printer).place(x=500,y=300)
                    
                    win.resizable(0,0)

                    win.mainloop()
                    result()
            btn1=tk.Button(text='Question Portal',command=button1,font=30,bg="#1F244A",fg="White").place(x=250,y=300)
            btn2=tk.Button(text='Result',command=button2,font=30,bg="#1F244A",fg="White").place(x=600,y=300)
            win1.mainloop()
        teacher()
        
        
    elif str(a2.get()).lower()=='student':
        win.destroy()
        stuguiv12.stu()
win=tk.Tk()
win.geometry("920x500")
win.title("Login Portal")
bg1=PhotoImage(file="QuizBG2.png")

tk.Label(win,image=bg1).place(x=0,y=0) 
a1=tk.Label(text="Student/Teacher",bg="#1F244A",fg="white",font=("Comic Sans MS",16))
a1.place(x=180,y=200)
a2=tk.Entry(bg="#1F244A",fg="White",font=16)
a2.place(x=395,y=200)
btn1=tk.Button(text="Submit",font=30,command=logg).place(x=250,y=250)

win.mainloop()
