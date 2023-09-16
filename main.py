from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1600x900+0+0")
        self.root.title("Face Recognition System")

        # 1st image
        img1=Image.open(r"C:\Users\HIMADRI\Desktop\Project\Images\College.jpg")
        img1=img1.resize((530,130))#resize((530,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=535,height=130)

        # 2nd image
        img2=Image.open(r"C:\Users\HIMADRI\Desktop\Project\Images\College.jpg")
        img2=img2.resize((530,130))#resize((530,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=530,y=0,width=535,height=130)

        # 3rd image
        img3=Image.open(r"C:\Users\HIMADRI\Desktop\Project\Images\College.jpg")
        img3=img3.resize((530,130))#resize((530,130),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1060,y=0,width=535,height=130)


        # bg image
        img4=Image.open(r"C:\Users\HIMADRI\Desktop\Project\Images\College.jpg")
        img4=img4.resize((530,130))#resize((530,130),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_lbl=Label(self.root,image=self.photoimg4)
        bg_lbl.place(x=0,y=130,width=535,height=130)






if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()


