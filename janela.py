from cores.cores import *
from tkinter import *
from tkinter import Tk, ttk


#tamanho da janela - jn 
jn = Tk()
titlejn =("")
jn.geometry("310x300")
jn.configure(background=c1)
jn.resizable(width=FALSE, height=FALSE)

#criando os frames-jn 
fm1 = Frame(jn,width=310,height=50,bg=c1,relief="flat")
fm1.grid(row=0,column=0,pady=1,padx=0,sticky=NSEW)

fm2 = Frame(jn,width=310,height=250,bg=c1,relief="flat")
fm2.grid(row=1,column=0,pady=1,padx=0,sticky=NSEW)





jn.mainloop()

