#CALCULATOR
from tkinter import *
root=Tk()


root.geometry("280x380")
root.resizable(0,0)
root.configure(background="black")

first=second=opperator=None


def printdigit(digit):
    screen = result_label["text"]
    new=screen+str(digit)
    result_label.config(text=new)
    
def clear():
    result_label.config(text="")
    
    
def getopprator(op):
    global first, opperator
    first=int(result_label["text"])
    opperator=op
    result_label.config(text=" ")
    
def get_result():
    global first,second, opperator
    
    second = int(result_label["text"])
    
    if opperator=="+":
        result_label.config(text=str(first+second))
    
    elif opperator=="-":
        result_label.config(text=str(first-second))
        
    elif opperator=="/":
        result_label.config(text=str(first/second))
    
    elif opperator=="*":
        result_label.config(text=str(first*second))

    
result_label = Label(root,text="", bg= "black" , fg = "white")
result_label.grid(row=0,column=0, columnspan=20, pady=(50,25),sticky=W)
result_label.config(font=("verdana",30,"bold"))

bt7=Button(root,text="7",bg="#050a14",fg="white",width=5,height=2 , command=lambda:printdigit(7))
bt7.grid(row=1,column=0 )
bt7.config(font=("verdana",14))

bt8=Button(root,text="8",bg="#050a14",fg="white",width=5,height=2 , command=lambda:printdigit(8))
bt8.grid(row=1,column=1)
bt8.config(font=("verdana",14))

bt9=Button(root,text="9",bg="#050a14",fg="white",width=5,height=2 , command=lambda:printdigit(9))
bt9.grid(row=1,column=2)
bt9.config(font=("verdana",14))

btdiv=Button(root,text="/",bg="#3366cc",fg="white",width=5,height=2 , command=lambda:getopprator("/"))
btdiv.grid(row=1,column=3)
btdiv.config(font=("verdana",14))


bt4=Button(root,text="4",bg="#050a14",fg="white",width=5,height=2 , command=lambda:printdigit(4))
bt4.grid(row=2,column=0)
bt4.config(font=("verdana",14))

bt5=Button(root,text="5",bg="#050a14",fg="white",width=5,height=2  , command=lambda:printdigit(5))
bt5.grid(row=2,column=1)
bt5.config(font=("verdana",14))

bt6=Button(root,text="6",bg="#050a14",fg="white",width=5,height=2 , command=lambda:printdigit(6))
bt6.grid(row=2,column=2)
bt6.config(font=("verdana",14))

btmul=Button(root,text="*",bg="#3366cc",fg="white",width=5,height=2 , command=lambda:getopprator("*"))
btmul.grid(row=2,column=3)
btmul.config(font=("verdana",14))

bt1=Button(root,text="1",bg="#050a14",fg="white",width=5,height=2 , command=lambda:printdigit(1))
bt1.grid(row=3,column=0)
bt1.config(font=("verdana",14))

bt2=Button(root,text="2",bg="#050a14",fg="white",width=5,height=2 , command=lambda:printdigit(2))
bt2.grid(row=3,column=1)
bt2.config(font=("verdana",14))

bt3=Button(root,text="3",bg="#050a14",fg="white",width=5,height=2 , command=lambda:printdigit(3))
bt3.grid(row=3,column=2)
bt3.config(font=("verdana",14))


btc=Button(root,text="C",bg="#FF0000",fg="white",width=5,height=2  , command=lambda:clear())
btc.grid(row=4,column=0)
btc.config(font=("verdana",14))

bt0=Button(root,text="0",bg="#050a14",fg="white",width=5,height=2 , command=lambda:printdigit(0))
bt0.grid(row=4,column=1)
bt0.config(font=("verdana",14))


btequal=Button(root,text="=",bg="#ff9900",fg="white",width=5,height=2 , command=lambda:get_result())
btequal.grid(row=4,column=2)
btequal.config(font=("verdana",14))

btadd=Button(root,text="+",bg="#3366cc",fg="white",width=5,height=2 , command=lambda:getopprator("+"))
btadd.grid(row=4,column=3)
btadd.config(font=("verdana",14))

btsub=Button(root,text="-",bg="#3366cc",fg="white",width=5,height=2 , command=lambda:getopprator("-"))
btsub.grid(row=3,column=3)
btsub.config(font=("verdana",14))

mainloop()