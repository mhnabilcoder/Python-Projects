from tkinter import*
import random
import string

root=Tk()

#Variable
long=IntVar()

def genrate():
	length=long.get()

	upper=string.ascii_uppercase

	lower=string.ascii_lowercase

	num=string.digits

	all= upper+lower+num

	temp= random.sample(all,length)

	passw="".join(temp)
    
	txtbox=Text(root,height=10,width=30)
	txtbox.insert(1.0,passw)
	txtbox.place(x=30,y=170)
	
	return None

#TITLE
titl=Label(root,text="Password Generator",bg="orange",font=("Helvetica","20","bold"))
titl.place(x=30,y=5)

#Heading    -   lengtth
head1=Label(root,text="Enter the length of your password",bg="lightblue",font=("Helvetica","11","bold"))
head1.place(x=5,y=80)

#ENTRYBox   -   length
hr=Entry(root,bd=2,textvariable=long)
hr.place(x=250,y=80)

#BUTTON
submit=Button(root,text="Submit",bg="lightgreen",bd=2,command=genrate)
submit.place(x=110,y=120)

#ADDITIONAL PART
root.geometry("320x230")
root.resizable(0,0)
root.title("Password Generator")
root.mainloop()
