from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1600x900+0+0")#you can set your own monitor resolution
        self.root.title("Face Recognition System")

        # 1st image
        img1=Image.open(r"C:\Users\HIMADRI\Desktop\Project\Images\College.jpg")#insert a image
        img1=img1.resize((530,130))#resize((530,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=535,height=130)

        # 2nd image
        img2=Image.open(r"C:\Users\HIMADRI\Desktop\Project\Images\College.jpg")#insert a image
        img2=img2.resize((530,130))#resize((530,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=535,y=0,width=535,height=130)

        # 3rd image
        img3=Image.open(r"C:\Users\HIMADRI\Desktop\Project\Images\College.jpg")#insert a image
        img3=img3.resize((530,130))#resize((530,130),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1070,y=0,width=535,height=130)


        # bg image
        img4=Image.open(r"C:\Users\HIMADRI\Desktop\Project\Images\College.jpg")#insert a image
        img4=img4.resize((1600,900))#resize((530,130),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1600,height=700)


        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",36,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1600,height=45)

        # student button
        img5=Image.open(r"C:\Users\HIMADRI\Desktop\Project\Images\College.jpg")#insert a image
        img5=img5.resize((1600,900))#resize((530,130),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5)
        b1.place(x=200,y=100,width=180,height=180)





if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()


