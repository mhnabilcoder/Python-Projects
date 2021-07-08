import random
from tkinter import*
root=Tk()

#print("!!!!put a comma(,)  after every item!!!!")
#Variable
foodget=StringVar()

#   C   O   D   E      
def choose():
    items=foodget.get()
    temp=items.split(",")
    food=random.choice(temp)
    eat=Label(root,bg="white",text="You Should Eat:",font=("raleway","12"))
    eat.place(x=10,y=200)
    eatfood=Label(root,bg="lightgreen",text=food,font=("raleway","12"))
    eatfood.place(x=150,y=200)
    return None


#TITLE
titl=Label(root,text="Random Food Chooser",bg="orange",font=("Helvetica","18","bold"))
titl.place(x=20,y=5)

#Introduction
txt=Label(root,text="#Put a comma(,) after every item you enter. \n Example(cake,sprite,chiken,pasta)",bg="white",fg="red",font=("Helvetica","8","bold"))
txt.place(x=10,y=80)

#Heading    -   Foods
head1=Label(root,text="Enter the food list",bg="lightblue",font=("Helvetica","11","bold"))
head1.place(x=5,y=112)

#ENTRYBox   -   Foods
hr=Entry(root,bd=2,textvariable=foodget)
hr.place(x=140,y=110)

#BUTTON
submit=Button(root,text="Submit",bg="lightgreen",bd=2,command=choose)
submit.place(x=110,y=150)

#ADDITIONAL PART
root.geometry("320x250")
root.resizable(0,0)
root.title("Random Food Selector")
root.mainloop()