from tkinter import *
import tkinter as tk

class MathOperations():
    def addition():
        n1=float(e1.get())
        n2=float(e2.get())
        result["text"]=str(n1+n2)

    def subtraction():
        n1=float(e1.get())
        n2=float(e2.get())
        result["text"]=str(n1-n2)    

    def multiplication():
        n1=float(e1.get())
        n2=float(e2.get())
        result["text"]=str(n1*n2) 

    def dividing():
        n1=float(e1.get())
        n2=float(e2.get())
        result["text"]=str(n1/n2)     

app = tk.Tk()
app.title("Simple Math Operations App")
app.geometry("400x200")
app.config(bg="lightgray")
app.resizable(0,0)

#User login and result screen
title=Label(app,text="@berktugates")
title.place(x=160,y=10)
e1=Entry(app,fg="black",width="10",font="20")
e1.place(x=20,y=40)
e2=Entry(app,fg="black",width="10",font="20")
e2.place(x=140,y=40)
equal=Label(app,text="=",fg="black")
equal.place(x=260,y=42)
result=Label(app,fg="black",width="15")
result.place(x=280,y=42)

#Placing action buttons
add=tk.Button(app,text="+",fg="black",font="30",width="5",command=MathOperations.addition)
add.place(x=40,y=100)
sub=Button(app,text="-",fg="black",font="30",width="5",command=MathOperations.subtraction)
sub.place(x=120,y=100)
multi=Button(app,text="x",fg="black",font="30",width="5",command=MathOperations.multiplication)
multi.place(x=200,y=100)
div=Button(app,text="/",fg="black",font="30",width="5",command=MathOperations.dividing)
div.place(x=280,y=100)

app.mainloop()