from sqlite3 import Row
from tkinter import*


root=Tk()
root.title("Registration Form")
root.geometry("500x300")


def getvals():
    print("Your Information has been Submitted")


#heading
Label(root,text="Payment Registration Form",font="ar 15 bold").grid(row=0,column=3)


#field name
name=Label(root,text="Name")
phone=Label(root,text="Phone")
gender=Label(root,text="Gender")
emergency=Label(root,text="Emergency")
paymentmode=Label(root,text="Payment Mode")


#packing fields
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergency.grid(row=4,column=2)
paymentmode.grid(row=5,column=2)


#Create some variable for storing data
namevalue=StringVar
phonevalue=StringVar
gendervalue=StringVar
emergencyvalue=StringVar
paymentmodevalue=StringVar
checkvalue=IntVar


#Created entry field
nameentry=Entry(root,textvariable=namevalue)
phoneentry=Entry(root,textvariable=phonevalue)
genderentry=Entry(root,textvariable=gendervalue)
paymentmodeentry=Entry(root,textvariable=paymentmodevalue)
emergencyentry=Entry(root,textvariable=emergencyvalue)



#packing entry fields
nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
paymentmodeentry.grid(row=5,column=3)
emergencyentry.grid(row=4,column=3)


# created checkbox

checkbtn=Checkbutton(text="Remember me?",variable=checkvalue)
checkbtn.grid(row=6,column=3)


#Submit button

subbutton=Button(text="Submit",command=getvals)
subbutton.grid(row=7,column=3)


root.mainloop()