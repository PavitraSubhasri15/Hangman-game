from tkinter import *
expression=""
def press(num):
    global expression
    expression=expression+str(num)
    equation.set(expression)
def equalpress():
    try:
        global expression
        total=eval(str(expression))
        equation.set(total)
        expression=""
    except:
        equation.set("error")
        expression=""
def clear():
    global expression
    expression=""
    equation.set("")
if __name__=="__main__":
    gui=Tk()
    gui.configure(background="black")
    gui.title("calci")
    gui.geometry("300x300")
    equation=StringVar()
    expression_field=Entry(gui,textvariable=equation)
    expression_field.grid(columnspan=4,ipadx=50)
    button1=Button(gui,text="1",fg="black",bg="yellow",command=lambda: press(1),height=1,width=5)
    button2=Button(gui,text="2",fg="black",background="yellow",command=lambda: press(2),height=1,width=5)
    button3=Button(gui,text="3",fg="black",background="yellow",command=lambda: press(3),height=1,width=5)
    button4=Button(gui,text="4",fg="black",background="yellow",command=lambda: press(4),height=1,width=5)
    button5=Button(gui,text="5",fg="black",background="yellow",command=lambda: press(5),height=1,width=5)
    button6=Button(gui,text="6",fg="black",background="yellow",command=lambda: press(6),height=1,width=5)
    button7=Button(gui,text="7",fg="black",background="yellow",command=lambda: press(7),height=1,width=5)
    button8=Button(gui,text="8",fg="black",background="yellow",command=lambda: press(8),height=1,width=5)
    button9=Button(gui,text="9",fg="black",background="yellow",command=lambda: press(9),height=1,width=5)
    button0=Button(gui,text="0",fg="black",background="yellow",command=lambda: press(0),height=1,width=5)
    equal=Button(gui,text="=",fg="white",background="green",command=lambda: equalpress(),height=1,width=5)
    mul=Button(gui,text="*",fg="white",background="green",command=lambda: press('*'),height=1,width=5)
    div=Button(gui,text="/",fg="white",background="green",command=lambda: press('/'),height=1,width=5)
    add=Button(gui,text="+",fg="white",background="green",command=lambda: press('+'),height=1,width=5)
    sub=Button(gui,text="-",fg="white",background="green",command=lambda: press('-'),height=1,width=5)
    delete=Button(gui,text="clear",fg="white",background="green",command=lambda: clear(),height=1,width=5)
    button1.grid(row=2, column=0) 
    button2.grid(row=2, column=1) 
    button3.grid(row=2, column=2) 
    button4.grid(row=2, column=3) 
    button5.grid(row=3, column=0) 
    button6.grid(row=3, column=1) 
    button7.grid(row=3, column=2) 
    button8.grid(row=3, column=3) 
    button9.grid(row=4, column=0) 
    button0.grid(row=4, column=1) 
    delete.grid(row=4, column=2) 
    equal.grid(row=4, column=3)
    add.grid(row=5, column=0) 
    sub.grid(row=5, column=1) 
    mul.grid(row=5, column=2) 
    div.grid(row=5, column=3) 
    decimal=Button(gui,text=".",fg="white",background="green",command=lambda:press('.'),height=1,width=2)
    decimal.grid(row=6, column=0) 
    gui.mainloop() 



