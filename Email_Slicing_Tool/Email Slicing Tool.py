from tkinter import*
root=Tk()
background = Canvas(bg = "pink",height = 250,width = 400)
background.place(x=0,y=0)

#VARIABLES
emailget=StringVar()

#Function
def slice():
   emailin=emailget.get()
   email=emailin.strip()
#strip() function will remove any additional & unwanted spacing on both sides of strings.

   username=email[:email.index("@")]
#we are making use of the slicing operator: and index() function.

   domain=email[email.index("@")+1:]
   page_content=(f"Username is {username} \n Domain is {domain}")
   
   if True:
      #content area
      textbox=Text(root,height=3, width=45,padx=5,pady=5)
      textbox.insert(1.0,page_content)
      textbox.place(x=14,y=170)

#TITLE
titl=Label(root,text="Email Slicer",bg="orange",font=("Helvetica","20","bold"))
titl.place(x=130,y=5)

#ENTER YOUR EMAIL
head=Label(root,text="Enter Your Email",bg="lightblue",fg="red",font=("Helvetica","11","bold"))
head.place(x=5,y=72)

#ENTRY BOXES
#email input box
inemail=Entry(root,bd=2,width=30,textvariable=emailget)
inemail.place(x=130,y=70)

#BUTTON
submit=Button(root,text="Submit",bg="lightgreen",command=slice)
submit.place(x=160,y=110)


#ADDITIONAL PART
root.geometry("400x250")
root.resizable(0,0)
root.title("Email Slicer")


root.mainloop()