from tkinter import *
from tkinter import messagebox
import ast

root=Tk()
root.title("Login")
root.geometry("925x500+300+200")
root.config(bg="white")
root.resizable(False,False)
def signup():
  username=user.get()
  password=code.get()
  confuirmpassword=sanno.get()
  if password==confuirmpassword:
     try:
        file=open("datasheet.txt","r+")
        d=file.read()
        r=ast.literal_eval(d) 

        dict2={username:password}
        r.update(dict2)
        file.truncate(0)
        file.close()

        file=open("datasheet.txt","w")
        w=file.write(str(r))
        
        messagebox.showinfo("Signup","Sucessfully sign up")
     except:
         file=open("datasheet.txt","w")
         pp=str({"username":"password"})
         file.write(pp)
         file.close()
  else:
     messagebox.showinfo("Invali","Both Password should match")

img=PhotoImage(file="L.png")
Label(root,image=img,bg="white").place(x=50,y=50)

frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)

heading=Label(frame,text="Sign in",fg="green",bg="white",font=("Microsoft Yahei UI Light",23,"bold"))
heading.place(x=110,y=5)

#########---------------------------------------------------------------------------------
def on_enter(e):
  user.delete(0,"end")

def on_leave(e):
  name=user.get()
  if name=="":
   user.insert(0,"Username")

user=Entry(frame,width=25,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",11,"bold"))
user.place(x=40,y=80)
user.insert(0,"Username")
user.bind("<FocusIn>",on_enter)
user.bind("<FocusOut>",on_leave)

Frame(frame,width=295,height=2,bg="black").place(x=25,y=107)
#########---------------------------------------------------------------------------------
def on_enter(e):
  code.delete(0,"end")

def on_leave(e):
  name=code.get()
  if name=="":
    code.insert(0,"Password")

code=Entry(frame,width=25,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",11,"bold"))
code.place(x=40,y=150)
code.insert(0,"Password")
code.bind("<FocusIn>",on_enter)
code.bind("<FocusOut>",on_leave)

Frame(frame,width=295,height=2,bg="black").place(x=25,y=177)
#########---------------------------------------------------------------------------------
def on_enter(e):
  sanno.delete(0,"end")

def on_leave(e):
  name=sanno.get()
  if name=="":
    sanno.insert(0,"ConfuirmPassword")

sanno=Entry(frame,width=25,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",11,"bold"))
sanno.place(x=40,y=230)
sanno.insert(0,"ConfuirmPassword")
sanno.bind("<FocusIn>",on_enter)
sanno.bind("<FocusOut>",on_leave)

Frame(frame,width=295,height=2,bg="black").place(x=25,y=250)
##############################################################
Button(frame,width=39,pady=7,text="Sign in",bg="skyblue",fg="white",border=0,command=signup).place(x=35,y=280)
label=Label(frame,text="Don't have an account?",fg="black",bg="white",font=("Microsoft Yahei UI Light",9))
label.place(x=75,y=320)

sign_up=Button(frame,width=6,text="Sign up",border=0,bg="white",cursor="hand2",fg="skyblue")
sign_up.place(x=200,y=320)

root.mainloop()