from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector


class Student:
        def __init__(self,root):
                self.root=root
                self.root.geometry("1600x900+0+0")#you can set your own monitor resolution
                self.root.title("Face Recognition System")


        #==========variables==========
                self.var_dep=StringVar()
                self.var_year=StringVar()
                self.var_semester=StringVar()
                self.var_std_id=StringVar()
                self.var_std_name=StringVar()
                self.var_roll=StringVar()
                self.var_gender=StringVar()
                self.var_dob=StringVar()
                self.var_email=StringVar()
                self.var_phone=StringVar()
                self.var_address=StringVar()


         # 1st image
                img1=Image.open(r"C:\Users\user\major project\Image-Processing-Project\project-images\1.jpg")#insert a image 
                img1=img1.resize((530,130))#resize((530,130),Image.ANTIALIAS)
                self.photoimg1=ImageTk.PhotoImage(img1)

                f_lbl=Label(self.root,image=self.photoimg1)
                f_lbl.place(x=0,y=0,width=535,height=130)

        # 2nd image
                img2=Image.open(r"C:\Users\user\major project\Image-Processing-Project\project-images\3.jpg")#insert a image
                img2=img2.resize((530,130))#resize((530,130),Image.ANTIALIAS)
                self.photoimg2=ImageTk.PhotoImage(img2)

                f_lbl=Label(self.root,image=self.photoimg2)
                f_lbl.place(x=535,y=0,width=535,height=130)        

        # 3rd image
                img3=Image.open(r"C:\Users\user\major project\Image-Processing-Project\project-images\2.jpg")#insert a image
                img3=img3.resize((530,130))#resize((530,130),Image.ANTIALIAS)
                self.photoimg3=ImageTk.PhotoImage(img3)

                f_lbl=Label(self.root,image=self.photoimg3)
                f_lbl.place(x=1070,y=0,width=535,height=130)   

        # bg image
                img4=Image.open(r"C:\Users\user\major project\Image-Processing-Project\project-images\bg5.webp")#insert a image
                img4=img4.resize((1600,900))#resize((530,130),Image.ANTIALIAS)
                self.photoimg4=ImageTk.PhotoImage(img4)

                bg_img=Label(self.root,image=self.photoimg4)
                bg_img.place(x=0,y=130,width=1600,height=700)

                title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",36,"bold"),bg="white",fg="blue")
                title_lbl.place(x=0,y=0,width=1600,height=45)

                main_frame=Frame(bg_img,bd=2,bg="white")
                main_frame.place(x=10,y=45,width=1570,height=650)


        #left label frame
                Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
                Left_frame.place(x=10,y=10,width=770,height=630)

                img_left=Image.open(r"C:\Users\user\major project\Image-Processing-Project\project-images\7.jpg")#insert a image
                img_left=img_left.resize((760,130))#resize((530,130),Image.ANTIALIAS)
                self.photoimg_left=ImageTk.PhotoImage(img_left)

                f_lbl=Label(Left_frame,image=self.photoimg_left)
                f_lbl.place(x=10,y=0,width=760,height=130) 

        #current course
                current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current course information")
                current_course_frame.place(x=10,y=140,width=750,height=120)


        #department
                dep_label=Label(current_course_frame,text="Department:",font=("times new roman",12,"bold"),bg="white")
                dep_label.grid(row=0,column=0,padx=10)

                dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly",width=30)
                dep_combo["values"]=("Select Department","CST","ETCE","CE","EIE","ARCH","EE")
                dep_combo.current(0)
                dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Year
                year_label=Label(current_course_frame,text="Year:",font=("times new roman",12,"bold"),bg="white")
                year_label.grid(row=1,column=0,padx=2)

                year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly",width=30)
                year_combo["values"]=("Select Year","2021-2022","2022-2023","2023-2024")
                year_combo.current(0)
                year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #semester
                semester_label=Label(current_course_frame,text="Semester:",font=("times new roman",12,"bold"),bg="white")
                semester_label.grid(row=0,column=2,padx=10)

                semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly",width=30)
                semester_combo["values"]=("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6")
                semester_combo.current(0)
                semester_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        
        #class student information
                class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student information")
                class_student_frame.place(x=10,y=265,width=750,height=330)

        #student ID
                studentID_label=Label(class_student_frame,text="Student ID:",font=("times new roman",12,"bold"),bg="white")
                studentID_label.grid(row=0,column=0,padx=10,sticky=W)

                studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=25,font=("times new roman",12,"bold"))
                studentID_entry.grid(row=0,column=1,padx=10,sticky=W)

        #student name

                studentName_label=Label(class_student_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
                studentName_label.grid(row=0,column=2,padx=10,sticky=W)

                studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=25,font=("times new roman",12,"bold"))
                studentName_entry.grid(row=0,column=3,padx=10,pady=10,sticky=W)

        #roll no
                Roll_label=Label(class_student_frame,text="Roll:",font=("times new roman",12,"bold"),bg="white")
                Roll_label.grid(row=1,column=0,padx=10,sticky=W)

                Roll_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=25,font=("times new roman",12,"bold"))
                Roll_entry.grid(row=1,column=1,padx=10,pady=10,sticky=W)

        #gender
                gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
                gender_label.grid(row=1,column=2,padx=10,sticky=W)

                gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly",width=25)
                gender_combo["values"]=("Select Gender","Male","Female","Others")
                gender_combo.current(0)
                gender_combo.grid(row=1,column=3,padx=10,pady=10,sticky=W)
 
        #DOB
                dob_label=Label(class_student_frame,text="D.O.B:",font=("times new roman",12,"bold"),bg="white")
                dob_label.grid(row=2,column=0,padx=10,sticky=W)

                dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=25,font=("times new roman",12,"bold"))
                dob_entry.grid(row=2,column=1,padx=10,pady=10,sticky=W)

        #email
                email_label=Label(class_student_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
                email_label.grid(row=2,column=2,padx=10,sticky=W)

                email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=25,font=("times new roman",12,"bold"))
                email_entry.grid(row=2,column=3,padx=10,pady=10,sticky=W)

        #phone no
                Phone_no_label=Label(class_student_frame,text="Phone no:",font=("times new roman",12,"bold"),bg="white")
                Phone_no_label.grid(row=3,column=0,padx=10,sticky=W)

                Phone_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=25,font=("times new roman",12,"bold"))
                Phone_no_entry.grid(row=3,column=1,padx=10,pady=10,sticky=W)

        #address
                address_label=Label(class_student_frame,text="Address:",font=("times new roman",12,"bold"),bg="white")
                address_label.grid(row=3,column=2,padx=10,sticky=W)

                address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=25,font=("times new roman",12,"bold"))
                address_entry.grid(row=3,column=3,padx=10,pady=10,sticky=W)

        #radio Buttons
                self.var_radio1=StringVar()
                radiobtn1=ttk.Radiobutton(class_student_frame,textvariable=self.var_radio1,text="Take a Photo Sample",value="Yes & No")
                radiobtn1.grid(row=4,column=0) 

                self.var_radio2=StringVar()
                radiobtn2=ttk.Radiobutton(class_student_frame,textvariable=self.var_radio2,text="No Photo Sample",value="Yes")
                radiobtn2.grid(row=4,column=1) 

        #buttons frame
                btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
                btn_frame.place(x=0,y=210,width=728,height=37)
       
                save_btn=Button(btn_frame,text="Save",command=self.add_data,width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
                save_btn.grid(row=0,column=0)

                update=Button(btn_frame,text="Update",width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
                update.grid(row=0,column=1)

                delete=Button(btn_frame,text="Delete",width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
                delete.grid(row=0,column=2)

                reset=Button(btn_frame,text="Reset",width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
                reset.grid(row=0,column=3)

        #2nd button 
                btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
                btn_frame1.place(x=0,y=250,width=728,height=37)
        
                take_photo_btn=Button(btn_frame1,text="Take Photo Sample",width=40,font=("times new roman",12,"bold"),bg="blue",fg="white")
                take_photo_btn.grid(row=1,column=0)

                update_photo=Button(btn_frame1,text="Update Photo Sample",width=40,font=("times new roman",12,"bold"),bg="blue",fg="white")
                update_photo.grid(row=1,column=1)


        #right label frame
                Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
                Right_frame.place(x=780,y=10,width=780,height=630)


                img_right=Image.open(r"C:\Users\user\major project\Image-Processing-Project\project-images\7.jpg")#insert a image
                img_right=img_right.resize((780,130))#resize((530,130),Image.ANTIALIAS)
                self.photoimg_right=ImageTk.PhotoImage(img_right)

                f_lbl=Label(Right_frame,image=self.photoimg_right)
                f_lbl.place(x=10,y=0,width=780,height=130) 
 
        #========Search System===============
                Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System")#,font=("times new roman",12,"bold"))
                Search_frame.place(x=10,y=140,width=750,height=70)

                search_label=Label(Search_frame,text="Search By:",font=("times new roman",12,"bold"),bg="green",fg="white")
                search_label.grid(row=0,column=0,padx=10,sticky=W)

                search_combo=ttk.Combobox(Search_frame,font=("times new roman",12,"bold"),state="readonly",width=14)
                search_combo["values"]=("Select","Roll_NO","Phone_NO")
                search_combo.current(0)
                search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
                
                search_entry=ttk.Entry(Search_frame,width=17,font=("times new roman",12,"bold"))
                search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
                
                search_btn=Button(Search_frame,text="Search",width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
                search_btn.grid(row=0,column=3)

                showAll_btn=Button(Search_frame,text="Show All",width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
                showAll_btn.grid(row=0,column=4)


        #========table frame=====
                table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
                table_frame.place(x=10,y=220,width=750,height=380)

                scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
                scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

                self.student_table=ttk.Treeview(table_frame,column=("dep","year","sem","id","name","roll","gender","dob","email","phone","address","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
                
                scroll_x.pack(side=BOTTOM,fill=X)
                scroll_y.pack(side=RIGHT,fill=Y)
                scroll_x.config(command=self.student_table.xview)
                scroll_y.config(command=self.student_table.yview)

                self.student_table.heading("dep",text="Department",)
                self.student_table.heading("year",text="Year")
                self.student_table.heading("sem",text="Semester")
                self.student_table.heading("id",text="Student ID")
                self.student_table.heading("name",text="Name")
                self.student_table.heading("roll",text="Roll No")
                self.student_table.heading("gender",text="Gender")
                self.student_table.heading("dob",text="DOB")
                self.student_table.heading("email",text="Email")
                self.student_table.heading("phone",text="Phone No")
                self.student_table.heading("address",text="Address")
                self.student_table.heading("photo",text="PhotoSamplestatus")
                self.student_table["show"]="headings"

                self.student_table.column("dep",width=80)
                self.student_table.column("year",width=80)
                self.student_table.column("sem",width=80)
                self.student_table.column("id",width=80)
                self.student_table.column("name",width=80)
                self.student_table.column("roll",width=80)
                self.student_table.column("gender",width=80)
                self.student_table.column("dob",width=80)
                self.student_table.column("email",width=80)
                self.student_table.column("phone",width=80)
                self.student_table.column("address",width=80)
                self.student_table.column("photo",width=130)

                self.student_table.pack(fill=BOTH,expand=1)
        #=========functios declaration========
        def add_data(self):
         if self.var_dep.get()=="Select Department"or self.var_std_name.get()=="":
               messagebox.showerror("Error","All Fields are required",parent=self.root)
         else:
                try:
                        conn=mysql.connector.connect(host="localhost",username="root",password="Himadri@124",database="face_recognizer")
                        my_cursor=conn.cursor()
                        my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                        
                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                        self.var_year.get(),
                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                        self.var_std_id.get(),
                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                        self.var_email.get(),
                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                        self.var_address.get(),
                                                                                                                                                        self.var_radio1.get()

                                                                                                                                                ))
                        conn.commit()
                        conn.close()
                        messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
                except Exception as es:
                       messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
if __name__=="__main__":
        root=Tk()
        obj=Student(root)
        root.mainloop()

