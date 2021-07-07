from tkinter import*

root=Tk()
root.geometry("300x250")
root.resizable(0,0)
root.title ("BMI Calculator")

#variables
wetentget=DoubleVar()
hitentget=DoubleVar()

#C  O   D   E 
def bmical():
  height=hitentget.get()
  weight=wetentget.get()
  meter=height*0.3048
  
  bmi=weight/(meter**2)

  if bmi<18.5:
    under=Label(root,text="UNDERWEIGHT",bg="white")
    under.place(x=100,y=210)
    print(under)

  elif bmi>18.5 and bmi<=25:
    normal=Label(root,text="NORMAL",bg="white")
    normal.place(x=115,y=210)
    print(normal)

  elif bmi>25 and bmi<=29.9:
    overweight=Label(root,text="OVERWEIGHT",bg="white")
    overweight.place(x=102,y=210)
    print(overweight)

  elif bmi>=30 and bmi<=34.9:
    obese=Label(root,text="OBESE",bg="white")
    obese.place(x=120,y=210)
    print(obese)

  else:
    exobese=Label(root,text="EXTREMELY OBESE",bg="white")
    exobese.place(x=80,y=210)
    print(exobese)
  return None


#Title
titel=Label(root,text="BMI Calculator",bg="magenta",fg="white",font=("Helvetica","20","bold"))
titel.place(x=60,y=20)

#Heading  - weight
wethead=Label(root,text="Weight",font=("Helvetica","14","bold"))
wethead.place(x=30,y=90)

#Heading  - height
hithead=Label(root,text="Height",font=("Helvetica","14","bold"))
hithead.place(x=30,y=120)

#EntryBox - weight  
wetent=Entry(root,bd=2,textvariable=wetentget)
wetent.place(x=100,y=90)

#EntryBox - height
hitent=Entry(root,bd=2,textvariable=hitentget)
hitent.place(x=100,y=120)

#Button - Submit
subton=Button(root,text="Submit",bg="orange",bd=2,command=bmical)
subton.place(x=110,y=160)


root.mainloop()