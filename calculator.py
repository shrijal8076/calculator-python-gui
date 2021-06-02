from tkinter import*
def btnClick(numbers):
      global operator
      global text_input
      operator =operator+str(numbers)
      text_input.set(operator)
      if numbers=="C":
            text_input.set("")
def result():
      global operator
      global text_input
      result=str(eval(operator))
      text_input.set(result)
      operator=""
            
            
      

#======================
root = Tk()
root.title("Callculator")
root.minsize(370,640)
root.maxsize(370,640)
root.configure(bg="pink")
operator=""
text_input = StringVar()
text_display = Entry(root,textvar=text_input,font=("arial",20,'bold'),bd=30,insertwidth=4,bg="pink",justify="right")
text_display.grid(columnspan=4)
#======================row 1=====================
btn7=Button(root,padx=16,pady=30,bd=8,fg="black",font=("arial",20,"bold"),bg="pink",text="7",command=lambda:btnClick(7)).grid(row=1,column=0)
btn8=Button(root,padx=16,pady=30,bd=8,fg="black",font=("arial",20,"bold"),bg="pink",text="8",command=lambda:btnClick(8)).grid(row=1,column=1)
btn9=Button(root,padx=16,pady=30,bd=8,fg="black",font=("arial",20,"bold"),bg="pink",text="9",command=lambda:btnClick(9)).grid(row=1,column=2)
Addition=Button(root,padx=16,pady=30,bd=8,fg="white",font=("arial",20,"bold"),bg="black",text="+",command=lambda:btnClick("+")).grid(row=1,column=3)

#=====================row2=======================
btn4=Button(root,padx=16,pady=30,bd=8,fg="black",font=("arial",20,"bold"),bg="pink",text="4",command=lambda:btnClick(4)).grid(row=2,column=0)
btn5=Button(root,padx=16,pady=30,bd=8,fg="black",font=("arial",20,"bold"),bg="pink",text="5",command=lambda:btnClick(5)).grid(row=2,column=1)
btn6=Button(root,padx=16,pady=30,bd=8,fg="black",font=("arial",20,"bold"),bg="pink",text="6",command=lambda:btnClick(6)).grid(row=2,column=2)
Subtraction=Button(root,padx=16,pady=30,bd=8,fg="white",font=("arial",20,"bold"),bg="black",text="-",command=lambda:btnClick("-")).grid(row=2,column=3)
#=====================row2=======================
btn3=Button(root,padx=16,pady=30,bd=8,fg="black",font=("arial",20,"bold"),bg="pink",text="3",command=lambda:btnClick(3)).grid(row=3,column=0)
btn2=Button(root,padx=16,pady=30,bd=8,fg="black",font=("arial",20,"bold"),bg="pink",text="2",command=lambda:btnClick(2)).grid(row=3,column=1)
btn1=Button(root,padx=16,pady=30,bd=8,fg="black",font=("arial",20,"bold"),bg="pink",text="1",command=lambda:btnClick(1)).grid(row=3,column=2)
Multiplication=Button(root,padx=16,pady=30,bd=8,fg="white",font=("arial",20,"bold"),bg="black",text="*",command=lambda:btnClick("*")).grid(row=3,column=3)
#=====================row2=======================
btn0=Button(root,padx=20,pady=50,bd=8,fg="black",font=("arial",20,"bold"),bg="pink",text="0",command=lambda:btnClick(0)).grid(row=4,column=0)
btnClear=Button(root,padx=20,pady=50,bd=8,fg="white",font=("arial",20,"bold"),bg="red",text="C",command=lambda:btnClick("C")).grid(row=4,column=1)
btnEquals=Button(root,padx=20,pady=50,bd=8,fg="black",font=("arial",20,"bold"),bg="pink",text="=",command=result).grid(row=4,column=2)
Division=Button(root,padx=20,pady=50,bd=8,fg="white",font=("arial",20,"bold"),bg="black",text="/",command=lambda:btnClick("/")).grid(row=4,column=3)


root.mainloop()
