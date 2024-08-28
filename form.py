from tkinter import *
from tkinter.filedialog import asksaveasfile
from cgitb import reset
def sabtnam():
    file=asksaveasfile()
    file.write(firstname_entry.get()+'\n')
    file.write(lastname_entry.get()+'\n')
    file.write(tahsilat.get()+'\n')
    file.write(jensiyat.get()+'\n')
    file.write(x.get()+',')
    file.write(y.get()+',')
    file.write(z.get()+',')
    file.write(w.get()+'\n')
    file.write(address_entry.get(1.0,END)+'\n')
    file.write(phone_entry.get()+'\n')
    file.close()
def clear():
    firstname_entry.delete(0,END)
    lastname_entry.delete(0,END)
    phone_entry.delete(0,END)
    address_entry.delete(1.0,END)
    tahsilat.set(reset)
    jensiyat.set(reset)
    x.set(0)
    y.set(0)
    z.set(0)
    w.set(0)






screen=Tk()
screen.geometry('800x800')
screen.title('Register Form')
#from HML COLOR website you can import your favor color code:
screen.configure(bg='#363834',borderwidth=5,highlightthickness=7,highlightcolor='#e674f4')
# برای اینکه مکان لیبل رو مشخص نکنم و بصورت خودکار خودش از اول صفحع شروع کنه از فرم هدینگ استفاده کردم که دیگر امکان اضافه کردن چیزی بهش وجود نداره.
#لیبل همیشه نیازمند ایکس ایگرگ یا ردیف وستون است
formheading=Label(screen,text='فرم ارزیابی',font=('b nazanin',25,'bold'),bg='#363834',fg='#f8ea04',width='500',height='3')
formheading.pack()
firstname_text=Label(text=':نام',font=('b nazanin',14,'bold'),bg='#363834',fg='#04bcf8')
firstname_text.place(x=1200,y=100)
firstname=StringVar()
firstname_entry=Entry(textvariable=firstname,width='60',border='3',highlightthickness=3,highlightcolor='#db5aba',highlightbackground='#e674f4')
firstname_entry.place(x=800,y=100)

lastname_text=Label(text=':نام خانوادگی',font=('b nazanin',14,'bold'),bg='#363834',fg='#04bcf8')
lastname_text.place(x=1200,y=150)
lastname=StringVar()
lastname_entry=Entry(textvariable=lastname,width='60',border='3',highlightthickness=3,highlightcolor='#db5aba',highlightbackground='#e674f4')
lastname_entry.place(x=800,y=150)

tahsilat_text=Label(text=':تحصیلات',font=('b nazanin',14,'bold'),bg='#363834',fg='#04bcf8')
tahsilat_text.place(x=1200,y=200)
tahsilat=StringVar()

tahsilat1=Radiobutton(screen,text='دانش اموز',variable=tahsilat,value='danesh amooz',font=('b nazanin',14,'bold'),bg='#363834',fg='#04bcf8',activebackground='#1f2421',activeforeground='#ff6f59').place(x=1200,y=250)

tahsilat2=Radiobutton(screen,text='دیپلم ',variable=tahsilat,value='diplom',font=('b nazanin',14,'bold'),bg='#363834',fg='#04bcf8',activebackground='#1f2421',activeforeground='#ff6f59').place(x=1000,y=250)
tahsilat3=Radiobutton(screen,text='کاردانی',variable=tahsilat,value='kardani',font=('b nazanin',14,'bold'),bg='#363834',fg='#04bcf8',activebackground='#1f2421',activeforeground='#ff6f59').place(x=800,y=250)
tahsilat4=Radiobutton(screen,text='کارشناسی',variable=tahsilat,value='karshenasi',font=('b nazanin',14,'bold'),bg='#363834',fg='#04bcf8',activebackground='#1f2421',activeforeground='#ff6f59').place(x=600,y=250)
tahsilat5=Radiobutton(screen,text='کارشناسی ارشد ',variable=tahsilat,value=' karshenasi arshad',font=('b nazanin',14,'bold'),bg='#363834',fg='#04bcf8',activebackground='#1f2421',activeforeground='#ff6f59').place(x=400,y=250)
tahsilat5=Radiobutton(screen,text='دکتری ',variable=tahsilat,value=' doctora',font=('b nazanin',14,'bold'),bg='#363834',fg='#04bcf8',activebackground='#1f2421',activeforeground='#ff6f59').place(x=200,y=250)

jensiyat_text=Label(text=':جنسیت',font=('b nazanin',14,'bold'),bg='#363834',fg='#04bcf8')
jensiyat_text.place(x=1200,y=300)
jensiyat=StringVar()
jensiyat1=Radiobutton(screen,text='اقا',variable=jensiyat,value='agha',font=('b nazanin',14,'bold'),bg='#363834',fg='#04bcf8',activebackground='#1f2421',activeforeground='#ff6f59').place(x=1200,y=350)
jensiyat2=Radiobutton(screen,text='خانم',variable=jensiyat,value='khanom',font=('b nazanin',14,'bold'),bg='#363834',fg='#04bcf8',activebackground='#1f2421',activeforeground='#ff6f59').place(x=1000,y=350)

a=Label(text='رشته تحصیلی مورد علاقه',font=('b nazanin',14,'bold'),bg='#363834',fg='#04bcf8')
a.place(x=1150,y=400)
#چون میتوان بیش از یک گزینه انتخاب کرد چهار variableداریم
x=StringVar()
y=StringVar()
z=StringVar()
w=StringVar()
reshte1=Checkbutton(screen,text='شبکه',font=('b nazanin',14,'bold'),bg='#363834',fg='#04bcf8',variable=x,activebackground='#1f2421',activeforeground='#ff6f59',onvalue='network').place(x=1200,y=450)


reshte2=Checkbutton(screen,text='وب',font=('b nazanin',14,'bold'),bg='#363834',fg='#04bcf8',variable=y,activebackground='#1f2421',activeforeground='#ff6f59',onvalue='web').place(x=1000,y=450)

reshte3=Checkbutton(screen,text='برنامه نویسی',font=('b nazanin',14,'bold'),bg='#363834',fg='#04bcf8',variable=z,activebackground='#1f2421',activeforeground='#ff6f59',onvalue='barnamenevisi').place(x=800,y=450)

reshte4=Checkbutton(screen,text='مهارت های پایه',font=('b nazanin',14,'bold'),bg='#363834',fg='#04bcf8',variable=w,activebackground='#1f2421',activeforeground='#ff6f59',onvalue='maharat').place(x=600,y=450)

address_text=Label(screen,text='ادرس:',font=('b nazanin',14,'bold'),bg='#363834',fg='#04bcf8')
address_text.place(x=1250,y=500)

#چون ادرس جای بیشتری لازم داره از انتری استفادع نمیکنم و روش جدیدی داریم
address_entry=Text(screen,height=5,width=50,border=3,highlightthickness=3,highlightcolor='#db5aba',highlightbackground='#e674f4')
address_entry.place(x=800,y=500)

phone_text=Label(text=':تلفن',font=('b nazanin',14,'bold'),bg='#363834',fg='#04bcf8')
phone_text.place(x=1200,y=600)
phone=StringVar()
phone_entry=Entry(textvariable=phone,width=60,border='3',highlightthickness=3,highlightcolor='#db5aba',highlightbackground='#e674f4')
phone_entry.place(x=800,y=600)

sabtenam_button=Button(screen,text='ثبت',width=4,height=1,font=('b nazanin',14,'bold'),bg='#363834',fg='#04bcf8',border=3,activebackground='#db5aba',activeforeground='#1f2421',command=lambda:sabtnam())
sabtenam_button.place(x=600,y=600)
clear_button=Button(screen,text='clear',width=4,height=1,font=('b nazanin',14,'bold'),bg='#363834',fg='#04bcf8',border=3,activebackground='#db5aba',activeforeground='#1f2421',command=lambda:clear())
clear_button.place(x=400,y=600)









screen.mainloop()