from tkinter import *
from PIL import Image,ImageTk
from tkinter.filedialog import askopenfile
import PyPDF2

root=Tk()
root.title("PDF To TEXT Extractor")
root.geometry("600x620")
root.resizable(0,0)

#CODE
def openfile():
    browse_txt.set("Loading...")
    file = askopenfile(mode ='rb', filetypes =[('PDF File', '*.pdf')])
    if file is not None:
        read_pdf=PyPDF2.PdfFileReader(file)
        page=read_pdf.getPage(0)
        page_content=page.extractText()
    #content area
        textbox=Text(root,height=10, width=63,padx=5,pady=5)
        textbox.insert(1.0,page_content)
        textbox.place(x=50,y=400)

    browse_txt.set("Browse")
   

    
#logo
logo = ImageTk.PhotoImage(Image.open("logo.png"))
logo_lebel=Label(image=logo)
logo_lebel.image=logo
logo_lebel.place(x=50,y=40)

#heading
head=Label(root,text="PDF to Text",bg="#a62400",fg="white",font=("raleway","22","bold"))
head.place(x=200,y=20)

#instuction
instruction =Label(root,text="Choose a PDF file on your computer to extract all its TEXT",font="raleway")
instruction.place(x=70,y=305)

#Browse Button
browse_txt=StringVar()
browse_btn=Button(bg="#a62400",fg="white",font="raleway",textvariable=browse_txt,height=1,width=10,bd=2,command=openfile)
browse_txt.set("Browse")
browse_btn.place(x=235,y=340)


root.mainloop()