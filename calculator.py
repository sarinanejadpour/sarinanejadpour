#simple calculator:
from tkinter import *
#panjere misazad:
root=Tk()
a=StringVar()
def addnum(num):
    a.set(a.get()+num)

def func2():
    a.set(eval(a.get()))

def func3(num):
    z=a.get()[-1]
    if z=='+' or z=='-' or z=='/' or z=='*':
       a.set(a.get()[:-1]+num)
    else:
        a.set(a.get()+num)
    
#label hara misazim

label1=Label(root,textvariable=a,font=('times new roman',20,'bold'),fg='blue',bg='silver')
label1.grid(columnspan=4)
#make button
btn1=Button(root,text='1',font=('times new roman',20,'bold'),fg='blue',bg='silver',width=5,height=2,command=lambda:addnum('1'))
btn1.grid(row=1,column=0)

btn2=Button(root,text='2',font=('times new roman',20,'bold'),fg='blue',bg='silver',width=5,height=2,command=lambda:addnum('2'))
btn2.grid(row=1,column=1)
btn3=Button(root,text='3',font=('times new roman',20,'bold'),fg='blue',bg='silver',width=5,height=2,command=lambda:addnum('3'))
btn3.grid(row=1,column=2)
btn4=Button(root,text='+',font=('times new roman',20,'bold'),fg='blue',bg='silver',width=5,height=2,command=lambda:func3('+'))
btn4.grid(row=1,column=3)
btn5=Button(root,text='4',font=('times new roman',20,'bold'),fg='blue',bg='silver',width=5,height=2,command=lambda:addnum('4'))
btn5.grid(row=2,column=0)
btn6=Button(root,text='5',font=('times new roman',20,'bold'),fg='blue',bg='silver',width=5,height=2,command=lambda:addnum('5'))
btn6.grid(row=2,column=1)
btn7=Button(root,text='6',font=('times new roman',20,'bold'),fg='blue',bg='silver',width=5,height=2,command=lambda:addnum('6'))
btn7.grid(row=2,column=2)
btn8=Button(root,text='-',font=('times new roman',20,'bold'),fg='blue',bg='silver',width=5,height=2,command=lambda:func3('-'))
btn8.grid(row=2,column=3)
btn9=Button(root,text='7',font=('times new roman',20,'bold'),fg='blue',bg='silver',width=5,height=2,command=lambda:addnum('7'))
btn9.grid(row=3,column=0)
btn10=Button(root,text='8',font=('times new roman',20,'bold'),fg='blue',bg='silver',width=5,height=2,command=lambda:addnum('8'))
btn10.grid(row=3,column=1)
btn11=Button(root,text='9',font=('times new roman',20,'bold'),fg='blue',bg='silver',width=5,height=2,command=lambda:addnum('9'))
btn11.grid(row=3,column=2)
btn12=Button(root,text='*',font=('times new roman',20,'bold'),fg='blue',bg='silver',width=5,height=2,command=lambda:func3('*'))
btn12.grid(row=3,column=3)
btn13=Button(root,text='c',font=('times new roman',20,'bold'),fg='blue',bg='silver',width=5,height=2,command=lambda:a.set(' '))
btn13.grid(row=4,column=0)
btn14=Button(root,text='0',font=('times new roman',20,'bold'),fg='blue',bg='silver',width=5,height=2,command=lambda:addnum('0'))
btn14.grid(row=4,column=1)
btn15=Button(root,text='=',font=('times new roman',20,'bold'),fg='blue',bg='silver',width=5,height=2,command=func2)
btn15.grid(row=4,column=2)
btn16=Button(root,text='/',font=('times new roman',20,'bold'),fg='blue',bg='silver',width=5,height=2,command=lambda:func3('/'))
btn16.grid(row=4,column=3)



















mainloop()
