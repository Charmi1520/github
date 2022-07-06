from tkinter import *
root=Tk()
root.geometry('600x600')
root.title('Forms')

def send():
    f=firstname.get()
    g=lastname.get()
    p=password.get()
    if p=='1234':
        l=Label(text=' LOGIN SUCCESS ',fg='red',font='10')
        l.place(x=210,y=350)
        f1=open('data.txt','a')
        f1.write('first name:'+f+'\n')
        f1.write('Last name:'+g+'\n')
        f1.write('Password:'+p+'\n')
        f1.close()
    else:
        l=Label(text='WRONG PASSWORD',fg='red',font='10')
        l.place(x=195,y=350)


a=Label(text='LOGIN FORM',bg='orange',fg='black',font='10',width='70',height='3')
a.pack()
a=Label(text='First Name:',font='15')
b=Label(text='Last Name:',font='15')
c=Label(text='Enter Password:',font='15')
a.place(x=15,y=70)
b.place(x=15,y=140)
c.place(x=15,y=210)

firstname=Entry(textvariable=StringVar(),width='60')
firstname.place(x=150,y=73)
lastname=Entry(textvariable=StringVar(),width='60')
lastname.place(x=150,y=143)
password=Entry(textvariable=StringVar(),width='60')
password.place(x=150,y=213)

button=Button(root,text='SUBMIT',font='10',bg='violet',fg='black',command=send)

button.place(x=250,y=300)



root.mainloop()

